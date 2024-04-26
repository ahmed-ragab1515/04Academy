from django.urls import path

from .views import *

urlpatterns = [
      
    path('login/', UserLoginView.as_view(), name="login"),
    

    # Step 2 URLs
    path('EducationalLevelOp/add/', EducationalLevelOp.as_view(), name="EducationalLevelOp_add"),
    path('EducationalLevelOp/edit/<int:pk>/', EducationalLevelOp.as_view(), name="EducationalLevelOp_edit"),
    path('EducationalLevelOp/delete/<int:pk>/', EducationalLevelOp.as_view(), name="EducationalLevelOp_delete"),
    path('GetEducationalLevelById/<int:pk>/', GetEducationalLevelByID.as_view(), name="GetEducationalLevelById"),
    path('GetEducationalLevelList/', EducationalLevelList.as_view(), name="GetEducationalLevelList"),
    path('EducationalLevelList/', EducationalLevelList.as_view(), name="EducationalLevelList"),
    
    path('ClassLevelOp/add/', ClassLevelOp.as_view()),
    path('ClassLevelOp/edit/<int:pk>/', ClassLevelOp.as_view()),
    path('ClassLevelOp/delete/<int:pk>/', ClassLevelOp.as_view()),
    path('GetClassLevelGetById/<int:pk>/', GetClassLevelByID.as_view()),
    path('GetClassLevelList/', ClassLevelList.as_view()),
    path('ClassLevelList/', ClassLevelList.as_view()),
    
    path('CurriculumOp/add/', CurriculumOp.as_view()),
    path('CurriculumOp/edit/<int:pk>/', CurriculumOp.as_view()),
    path('CurriculumOp/delete/<int:pk>/', CurriculumOp.as_view()),
    path('GetCurriculumById/<int:pk>/', GetCurriculumByID.as_view()),
    path('GetCurriculumList/', CurriculumList.as_view()),
    path('CurriculumList/', CurriculumList.as_view()),
    
    
    # Step 3 URLs
    path('SubjectOp/add/', SubjectOp.as_view()),
    path('SubjectOp/edit/<int:pk>/', SubjectOp.as_view()),
    path('SubjectOp/delete/<int:pk>/', SubjectOp.as_view()),
    path('GetSubjectById/<int:pk>/', GetSubjectByID.as_view()),
    path('GetSubjectList/', SubjectList.as_view()),
    path('SubjectList/', SubjectList.as_view()),
    
    
    # Step 4 URLs
    path('StudentCountOp/add/', StudentCountOp.as_view()),
    path('StudentCountOp/edit/<int:pk>/', StudentCountOp.as_view()),
    path('StudentCountOp/delete/<int:pk>/', StudentCountOp.as_view()),
    path('GetStudentCountById/<int:pk>/', GetStudentCountByID.as_view()),
    path('GetStudentCountList/', StudentCountList.as_view()),
    path('StudentCountList/', StudentCountList.as_view()),
    
    path('StudyGoalOp/add/', StudyGoalOp.as_view()),
    path('StudyGoalOp/edit/<int:pk>/', StudyGoalOp.as_view()),
    path('StudyGoalOp/delete/<int:pk>/', StudyGoalOp.as_view()),
    path('GetStudyGoalById/<int:pk>/', GetStudyGoalByID.as_view()),
    path('GetStudyGoalList/', StudyGoalList.as_view()),
    path('StudyGoalList/', StudyGoalList.as_view()),
    
    
    # Step 5 URLs
    path('DayOp/add/', DayOp.as_view()),
    path('DayOp/edit/<int:pk>/', DayOp.as_view()),
    path('DayOp/delete/<int:pk>/', DayOp.as_view()),
    path('GetDayById/<int:pk>/', GetDayByID.as_view()),
    path('GetDaysList/', DayList.as_view()),
    path('DaysList/', DayList.as_view()),
    
    path('SuitableTimingOp/add/', SuitableTimingOp.as_view()),
    path('SuitableTimingOp/edit/<int:pk>/', SuitableTimingOp.as_view()),
    path('SuitableTimingOp/delete/<int:pk>/', SuitableTimingOp.as_view()),
    path('GetSuitableTimingById/<int:pk>/', GetSuitableTimingByID.as_view()),
    path('GetSuitableTimingList/', SuitableTimingList.as_view()),
    path('SuitableTimingList/', SuitableTimingList.as_view()),
    
    
    # Step 6 URLs
    path('SessionFrequencyOp/add/', SessionFrequencyOp.as_view()),
    path('SessionFrequencyOp/edit/<int:pk>/', SessionFrequencyOp.as_view()),
    path('SessionFrequencyOp/delete/<int:pk>/', SessionFrequencyOp.as_view()),
    path('GetSessionFrequencyById/<int:pk>/', GetSessionFrequencyByID.as_view()),
    path('GetSessionFrequencyList/', SessionFrequencyList.as_view()),
    path('SessionFrequencyList/', SessionFrequencyList.as_view()),
    
    path('SessionDurationOp/add/', SessionDurationOp.as_view()),
    path('SessionDurationOp/edit/<int:pk>/', SessionDurationOp.as_view()),
    path('SessionDurationOp/delete/<int:pk>/', SessionDurationOp.as_view()),
    path('GetSessionDurationById/<int:pk>/', GetSessionDurationByID.as_view()),
    path('GetSessionDurationList/', SessionDurationList.as_view()),
    path('SessionDurationList/', SessionDurationList.as_view()),
    
    path('SubscriptionPlanOp/add/', SubscriptionPlanOp.as_view()),
    path('SubscriptionPlanOp/edit/<int:pk>/', SubscriptionPlanOp.as_view()),
    path('SubscriptionPlanOp/delete/<int:pk>/', SubscriptionPlanOp.as_view()),
    path('GetSubscriptionPlanById/<int:pk>/', GetSubscriptionPlanByID.as_view()),
    path('GetSubscriptionPlanList/', SubscriptionPlanList.as_view()),
    path('SubscriptionPlanList/', SubscriptionPlanList.as_view()),
    
    
    # Final Step URLs
    path('StudentApplicationOp/add/', StudentApplicationAllowed.as_view()),
    path('StudentApplicationOp/edit/<int:pk>/', StudentApplicationOp.as_view()),
    path('StudentApplicationOp/delete/<int:pk>/', StudentApplicationOp.as_view()),
    path('GetStudentApplicationGetById/<int:pk>/', StudentApplicationAllowed.as_view()),
    path('GetStudentApplicationList/', StudentApplicationList.as_view()),
    path('StudentApplicationList/', StudentApplicationList.as_view()),

]

