from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
import json
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken


class UserLoginView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            if username is None or password is None:
                raise AuthenticationFailed('Username and password are required.')
            user = authenticate(request, username=username, password=password)      
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({'message': 'Login successful', 'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                raise AuthenticationFailed('Login failed. Invalid username or password.')
        
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GenralCRUD(APIView):
    model = None
    serializer_class = None
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"data": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"data": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({"data": "Delete successful"}, status=status.HTTP_200_OK)

class GenralCRUDAllowed(APIView):
    model = None
    serializer_class = None
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"data": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = self.get_serializer(instance)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

class GenralList(APIView):
    model = None
    serializer_class = None

    def filter_objects(self, data, search):
        if hasattr(data, 'name') :
            return data.filter(name__icontains=search)
        else:
            return data

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request, format=None):
        try:
            page_number = request.data.get('pageNum', 1)
            page_size = request.data.get('pageLen', 10)
            search = request.data.get('search', '')
            data = self.filter_objects(self.model.objects.all(), search)
            paginator = Paginator(data, page_size)
            pages = paginator.get_page(page_number)
            serializer = self.get_serializer(pages, many=True)
            response_data = {
                'count': len(data),
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except:
            return Response({"data": "Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        try:
            data = self.model.objects.all().order_by('id')
            serializer = self.get_serializer(data, many=True)
            response_data = {
                'count': len(data),
                'data': serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except:
            return Response({"data": "Not Found"}, status=status.HTTP_400_BAD_REQUEST)
      
      


class EducationalLevelOp(GenralCRUD):
    model = EducationalLevel
    serializer_class = EducationalLevelSerializer

class GetEducationalLevelByID(GenralCRUDAllowed):
    model = EducationalLevel
    serializer_class = EducationalLevelSerializer
    
class EducationalLevelList(GenralList):
    model = EducationalLevel
    serializer_class = EducationalLevelSerializer
   
# ---------------------------------------------------------
 
class ClassLevelOp(GenralCRUD):
    model = ClassLevel
    serializer_class = ClassLevelSerializer
    
class GetClassLevelByID(GenralCRUDAllowed):
    model = ClassLevel
    serializer_class = ClassLevelSerializer
    
class ClassLevelList(GenralList):
    model = ClassLevel
    serializer_class = ClassLevelSerializer
   
# ---------------------------------------------------------
 
class CurriculumOp(GenralCRUD):
    model = Curriculum
    serializer_class = CurriculumSerializer
    
class GetCurriculumByID(GenralCRUDAllowed):
    model = Curriculum
    serializer_class = CurriculumSerializer

class CurriculumList(GenralList):
    model = Curriculum
    serializer_class = CurriculumSerializer
   
# ---------------------------------------------------------
 
class SubjectOp(GenralCRUD):
    model = Subject
    serializer_class = SubjectSerializer
    
class GetSubjectByID(GenralCRUDAllowed):
    model = Subject
    serializer_class = SubjectSerializer
    
class SubjectList(GenralList):
    model = Subject
    serializer_class = SubjectSerializer
   
# ---------------------------------------------------------
 
class StudentCountOp(GenralCRUD):
    model = StudentCount
    serializer_class = StudentCountSerializer
    
class GetStudentCountByID(GenralCRUDAllowed):
    model = StudentCount
    serializer_class = StudentCountSerializer
    
class StudentCountList(GenralList):
    model = StudentCount
    serializer_class = StudentCountSerializer
   
# ---------------------------------------------------------
 
class StudyGoalOp(GenralCRUD):
    model = StudyGoal
    serializer_class = StudyGoalSerializer
    
class GetStudyGoalByID(GenralCRUDAllowed):
    model = StudyGoal
    serializer_class = StudyGoalSerializer

class StudyGoalList(GenralList):
    model = StudyGoal
    serializer_class = StudyGoalSerializer
   
# ---------------------------------------------------------
 
class DayOp(GenralCRUD):
    model = Day
    serializer_class = DaySerializer
    
class GetDayByID(GenralCRUDAllowed):
    model = Day
    serializer_class = DaySerializer

class DayList(GenralList):
    model = Day
    serializer_class = DaySerializer
   
# ---------------------------------------------------------
 
class SuitableTimingOp(GenralCRUD):
    model = SuitableTiming
    serializer_class = SuitableTimingSerializer
    
class GetSuitableTimingByID(GenralCRUDAllowed):
    model = SuitableTiming
    serializer_class = SuitableTimingSerializer

class SuitableTimingList(GenralList):
    model = SuitableTiming
    serializer_class = SuitableTimingSerializer
   
# ---------------------------------------------------------
 
class SessionFrequencyOp(GenralCRUD):
    model = SessionFrequency
    serializer_class = SessionFrequencySerializer
    
class GetSessionFrequencyByID(GenralCRUDAllowed):
    model = SessionFrequency
    serializer_class = SessionFrequencySerializer

class SessionFrequencyList(GenralList):
    model = SessionFrequency
    serializer_class = SessionFrequencySerializer
   
# ---------------------------------------------------------
 
class SessionDurationOp(GenralCRUD):
    model = SessionDuration
    serializer_class = SessionDurationSerializer
    
class GetSessionDurationByID(GenralCRUDAllowed):
    model = SessionDuration
    serializer_class = SessionDurationSerializer
    
class SessionDurationList(GenralList):
    model = SessionDuration
    serializer_class = SessionDurationSerializer
   
# ---------------------------------------------------------
 
class SubscriptionPlanOp(GenralCRUD):
    model = SubscriptionPlan
    serializer_class = SubscriptionPlanSerializer
    
class GetSubscriptionPlanByID(GenralCRUDAllowed):
    model = SubscriptionPlan
    serializer_class = SubscriptionPlanSerializer
    
class SubscriptionPlanList(GenralList):
    model = SubscriptionPlan
    serializer_class = SubscriptionPlanSerializer
    
# ---------------------------------------------------------
    
class StudentApplicationOp(GenralCRUD):
    model = StudentApplication
    serializer_class = StudentApplicationSerializer
    
    
class StudentApplicationAllowed(GenralCRUDAllowed):
    model = StudentApplication
    serializer_class = StudentApplicationSerializer
    

class StudentApplicationList(GenralList):
    model = StudentApplication
    serializer_class = StudentApplicationSerializer
    
    