from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import Learner
import json
from .models import Learner, Progress, Recommendation
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import JsonResponse
from .models import Course


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        # Parse the JSON data from the request body
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        # Check if required fields are provided
        if not username or not password or not email:
            return JsonResponse({'error': 'All fields (username, password, email) are required'}, status=400)

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=409)

        try:
            # Create a new User instance (Django’s built-in user model)
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password  # Django will handle password hashing automatically
            )

            # Create a new Learner instance with default niveau set to 'débutant'
            learner = Learner.objects.create(
                user=user,  # Associate the Learner with the User model
                niveau='débutant',  # Set default niveau to 'débutant'
                preferences={},  # You can set preferences as an empty JSON object or leave it empty
            )
            learner.save()

            return JsonResponse({'message': 'Learner registered successfully', 'learner_id': learner.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': f'Failed to create learner due to: {str(e)}'}, status=500)

    # If the request is not POST, return a method not allowed error
    return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            email = data.get('email')  # Use email instead of username
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        # Validate fields
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        # Check if the user exists by email (query User model instead of Learner)
        try:
            user = User.objects.get(email=email)  # Query by email in the User model
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

        # Verify the password using the User's password field
        if not user.check_password(password):
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

        # Retrieve the learner associated with the user
        try:
            learner = learner = Learner.objects.get(user=user)  # Use the learner's user field
        except Learner.DoesNotExist:
            return JsonResponse({'error': 'Learner not found'}, status=404)

        # Retrieve progress and recommendations
        progress = [
            {
                'course_title': p.course.titre,
                'progress_percentage': p.progress_percentage,
                'status': p.status,
                'date_updated': p.date_updated
            }
            for p in learner.progress.all()
        ]

        recommendations = [
            {
                'type': r.type_recommendation,
                'content': r.contenu,
                'date_recommendation': r.date_recommandation
            }
            for r in learner.recommendations.all()
        ]

        # Construct the response
        response_data = {
            'learner': {
                'id': learner.id,
                'username': learner.user.username,  # Access the User's username
                'email': learner.user.email,  # Access the User's email
                'niveau': learner.niveau,
                'preferences': learner.preferences,
                'date_inscription': learner.date_inscription
            },
            'progress': progress,
            'recommendations': recommendations
        }

        return JsonResponse(response_data, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


# View to list all courses
def list_courses(request):
    if request.method == 'GET':
        # Retrieve all courses from the database
        courses = Course.objects.all()

        # Prepare the courses data to return
        courses_data = [
            {
                'id': course.id,
                'titre': course.titre,
                'description': course.description,
                'niveau_difficulte': course.niveau_difficulte,
                'date_creation': course.date_creation,
                'image': course.image
            }
            for course in courses
        ]

        # Return the list of courses as a JSON response
        return JsonResponse({'courses': courses_data}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




# View to add a course to a learner
@csrf_exempt
def add_course_to_learner(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            learner_id = data.get('learner_id')
            course_id = data.get('course_id')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        # Check if required fields are provided
        if not learner_id or not course_id:
            return JsonResponse({'error': 'Learner ID and Course ID are required'}, status=400)

        # Check if the learner and course exist
        try:
            learner = Learner.objects.get(id=learner_id)
        except Learner.DoesNotExist:
            return JsonResponse({'error': 'Learner not found'}, status=404)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)

        # Check if the learner is already enrolled in the course
        if Progress.objects.filter(learner=learner, course=course).exists():
            return JsonResponse({'error': 'Learner is already enrolled in this course'}, status=409)

        # Create a new progress record for the learner and course
        try:
            progress = Progress.objects.create(
                learner=learner,
                course=course,
                progress_percentage=0,  # Initialize progress to 0%
                status='en cours',  # Set status to 'in progress'
            )
            progress.save()

            return JsonResponse({'message': 'Course successfully added to learner', 'progress_id': progress.id}, status=201)

        except IntegrityError:
            return JsonResponse({'error': 'Failed to add course due to a database error'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_course_from_learner(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            learner_id = data.get('learner_id')
            course_id = data.get('course_id')

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        # Check if required fields are provided
        if not learner_id or not course_id:
            return JsonResponse({'error': 'Learner ID and Course ID are required'}, status=400)

        # Check if the learner and course exist
        try:
            learner = Learner.objects.get(id=learner_id)
        except Learner.DoesNotExist:
            return JsonResponse({'error': 'Learner not found'}, status=404)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)

        # Find the progress record for the learner and course
        try:
            progress = Progress.objects.get(learner=learner, course=course)
        except Progress.DoesNotExist:
            return JsonResponse({'error': 'Progress record not found for this learner and course'}, status=404)

        # Delete the progress record
        progress.delete()

        return JsonResponse({'message': 'Course successfully removed from learner'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
