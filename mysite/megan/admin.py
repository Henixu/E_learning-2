from django.contrib import admin
from .models import Learner, Progress, Course, Recommendation


# Customizing the Learner admin view
class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'niveau', 'date_inscription')  # Fields to display in the table
    search_fields = ('user__username', 'user__email')  # Allows search by username or email
    list_filter = ('niveau',)  # Adds a filter sidebar by 'niveau' (débutant, intermédiaire, avancé)

# Register the Learner model with the custom admin view
admin.site.register(Learner, LearnerAdmin)
# Register the other models without customization

# Customizing the Progress admin view
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('learner', 'course', 'progress_percentage', 'status', 'date_updated')  # Fields to display
    search_fields = ('learner__user__username', 'course__titre')  # Allows search by learner username or course title
    list_filter = ('status', 'course__niveau_difficulte')  # Adds a filter sidebar by status and course difficulty

# Register the Progress model with the custom admin view
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Course)
admin.site.register(Recommendation)
