from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CustomUser(User):
    

    def save(self, *args, **kwargs):
        if self.id is None :
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)
    

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = "00_custom_users"


# Step 2 Classes
class EducationalLevel(models.Model):
    name = models.CharField(max_length=100, verbose_name="المرحلة الدراسية")

    def __str__(self):
        return self.name
  
    class Meta:
      verbose_name_plural = "01_educational_level"
      
class ClassLevel(models.Model):
    name = models.CharField(max_length=100, verbose_name="الصف الدراسي")

    def __str__(self):
        return self.name
  
    class Meta:
      verbose_name_plural = "02_class_level"
      
class Curriculum(models.Model):
    name = models.CharField(max_length=100, verbose_name="المنهج الدراسي")

    def __str__(self):
        return self.name
  
    class Meta:
      verbose_name_plural = "03_curriculum"
      
      
# Step 3 Classes
class Subject(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subject_images/', null=True, blank=True)

    def __str__(self):
        return self.name
  
    class Meta:
      verbose_name_plural = "04_subject"
      

# Step 4 Classes
class StudentCount(models.Model):
    count = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.count}"
  
    class Meta:
      verbose_name_plural = "05_student_count"
      
class StudyGoal(models.Model):
    goal = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.goal}"
  
    class Meta:
      verbose_name_plural = "06_study_goal"
      

      
# Step 5 Classes
class Day(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم اليوم")

    def __str__(self):
      return f"{self.name}"
      
    class Meta:
      verbose_name_plural = "07_day"

class SuitableTiming(models.Model):
    time = models.CharField(max_length=50, verbose_name="التوقيت المناسب")
    
    def __str__(self):
        return f"{self.time}"
      
    class Meta:
      verbose_name_plural = "08_suitable_timing"
      

# Step 6 Classes
class SessionFrequency(models.Model):
    name = models.CharField(max_length=50, verbose_name="عدد الحصص الأسبوعية")
  
    def __str__(self):
        return f"{self.name}"
  
    class Meta:
      verbose_name_plural = "09_session_frequency"
      
class SessionDuration(models.Model):
    name = models.CharField(max_length=50, verbose_name="مدة الحصة الواحدة")

    def __str__(self):
        return f"{self.name}"
  
    class Meta:
      verbose_name_plural = "10_session_duration"
      
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50, verbose_name="نوع الاشتراك")
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="الخصم")
    duration = models.CharField(max_length=50, verbose_name="المدة")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="السعر")
  
    def __str__(self):
        return f"Subscription:{self.name}, Price:{self.price}"
      
    class Meta:
      verbose_name_plural = "11_subscription_plan"
      
      
# Final Step
class StudentApplication(models.Model):
      
    # Step 1
    first_name = models.CharField(max_length=100, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=100, verbose_name="اسم العائلة")
    age = models.IntegerField(verbose_name="العمر")
    GENDER_CHOICES = [
        ('ذكر', 'ذكر'),
        ('انثى', 'انثى')
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="النوع")
    nationality = models.CharField(max_length=100, verbose_name="الجنسية")
    whatsapp_number = models.CharField(max_length=100, verbose_name="رقم الواتساب")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    difficulties = models.BooleanField(verbose_name="هل تواجه اي صعوبات في الدراسة؟")
    notes = models.TextField(verbose_name="ملاحظات إضافية", blank=True, null= True)

    # Step 2
    educational_level = models.ForeignKey(EducationalLevel, on_delete=models.DO_NOTHING, verbose_name="المرحلة الدراسية")
    class_level = models.ForeignKey(ClassLevel, on_delete=models.DO_NOTHING, verbose_name="الصف الدراسي")
    curriculum = models.ForeignKey(Curriculum, on_delete=models.DO_NOTHING, verbose_name="المنهج الدراسي")

    # Step 3
    subjects = models.ManyToManyField(Subject, verbose_name="المواد")
    
    # Step 4
    student_count = models.ForeignKey(StudentCount, on_delete=models.CASCADE, verbose_name="عدد الطلاب")
    goals = models.ManyToManyField(StudyGoal, verbose_name="أهداف الدراسة")
      
    # Step 5

    suitable_day = models.ManyToManyField(Day, verbose_name="الأيام المناسبة")    
    time_period = models.CharField(max_length=100, verbose_name="الفترة الزمنية المناسبة")
    suitable_timing = models.ForeignKey(SuitableTiming, on_delete=models.CASCADE, verbose_name="التوقيت المناسب")
          
    # Step 6
    session_frequency = models.ForeignKey(SessionFrequency, on_delete=models.CASCADE, verbose_name="عدد الحصص الأسبوعية")
    session_duration = models.ForeignKey(SessionDuration, on_delete=models.CASCADE, verbose_name="مدة الحصة الواحدة")
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, verbose_name="نوع الاشتراك")
    

    # Step 7
    card_number = models.CharField(max_length=16, verbose_name="رقم البطاقة")
    security_code = models.CharField(max_length=20, verbose_name="رمز الحماية")
    expiration_date = models.CharField(max_length=10, verbose_name="تاريخ انتهاء الصلاحية")
    card_name = models.CharField(max_length=100, verbose_name="الاسم على البطاقة")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
      
    class Meta:
      verbose_name_plural = "12_student_application"
      