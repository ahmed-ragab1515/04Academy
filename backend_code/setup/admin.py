from django.contrib import admin
from .models import *

admin.site.register(CustomUser)

admin.site.register(EducationalLevel)
admin.site.register(ClassLevel)
admin.site.register(Curriculum)
admin.site.register(Subject)
admin.site.register(StudentCount)
admin.site.register(StudyGoal)
admin.site.register(Day)
admin.site.register(SuitableTiming)
admin.site.register(SessionFrequency)
admin.site.register(SessionDuration)
admin.site.register(SubscriptionPlan)
admin.site.register(StudentApplication)

