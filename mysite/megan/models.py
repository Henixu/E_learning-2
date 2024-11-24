from django.db import models
from django.contrib.auth.models import User
# Learner model to hold learner-specific data
# Learner model to hold learner-specific data
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="learner")
    
    niveau = models.CharField(max_length=50, choices=[('débutant', 'Débutant'), ('intermédiaire', 'Intermédiaire'), ('avancé', 'Avancé')])
    preferences = models.JSONField(null=True, blank=True)
    date_inscription = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Learner: {self.user.username}"

# Course model to hold course data
class Course(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    niveau_difficulte = models.CharField(max_length=50, choices=[('débutant', 'Débutant'), ('intermédiaire', 'Intermédiaire'), ('avancé', 'Avancé')])
    date_creation = models.DateField(auto_now_add=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.titre
    
# Progress model to track learner's progress in courses
class Progress(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name='progress')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='progress')
    progress_percentage = models.IntegerField(default=0)  # Progress in percentage (0-100)
    status = models.CharField(max_length=50, choices=[('en cours', 'En Cours'), ('terminé', 'Terminé'), ('échoué', 'Échoué')], default='en cours')
    date_updated = models.DateField(auto_now=True)  # Track last update date for progress
    
    def __str__(self):
        return f"Progress for {self.learner.user.username} in {self.course.titre} - {self.progress_percentage}%"



# Recommendation model to suggest content to learners
class Recommendation(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name="recommendations")
    type_recommendation = models.CharField(max_length=50, choices=[('cours', 'Cours'), ('article', 'Article'), ('vidéo', 'Vidéo'), ('quiz', 'Quiz')])
    contenu = models.TextField()
    date_recommandation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Recommandation pour {self.learner.username}"


