from django.contrib import admin
from .models import Resume, Profile, Work, WorkHighlight, Education, Course, Award, Publication

REGISTER_MODELS = [
    Resume,
    Profile,
    Work,
    WorkHighlight,
    Education,
    Course,
    Award,
    Publication
]

# Register your models here.
admin.site.register(REGISTER_MODELS)