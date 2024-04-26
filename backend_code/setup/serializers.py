from rest_framework import serializers
from .models import *


# Step 2
class EducationalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalLevel
        fields = '__all__'
        
class ClassLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLevel
        fields = '__all__'
        
class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'
      
       
# Step 3
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
    
        
# Step 4
class StudentCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCount
        fields = '__all__'
        
class StudyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGoal
        fields = '__all__'
        
        
# Step 5
class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'
        
class SuitableTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuitableTiming
        fields = '__all__'
        
        
# Step 6
class SessionFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionFrequency
        fields = '__all__'
        
class SessionDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionDuration
        fields = '__all__'
        
class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'
        
        
# Final Step
class StudentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApplication
        fields = '__all__'