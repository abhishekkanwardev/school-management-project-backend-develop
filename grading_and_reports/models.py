from django.db import models
from school_process.models import Lesson,Class
from accounts.models import StudentProfile

from django.core.validators import MaxValueValidator, MinValueValidator 


class GradingType(models.Model):
    name  = models.CharField(max_length=55)
    effect = models.PositiveIntegerField()

    def __str__(self):
        return  f"{self.name} - {self.effect}"


class GradingKey(models.Model):
    rank_name = models.CharField(max_length=30)
    starting_mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    finish_mark = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return  f"{self.rank_name} {self.starting_mark}-{self.finish_mark}"


class StudentGrades(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name = 'student_grade_list')

    def __str__(self):
        return  self.student.user.email

class LessonGrade(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, related_name='lesson_grade_list')
    student_grades = models.ForeignKey(StudentGrades, on_delete=models.DO_NOTHING, null=True, related_name='lesson_grade_list')

    def __str__(self):
        return  f"Student-{self.student_grades.student.pk}. {self.lesson.lesson_name}"

class Grading(models.Model):
    grading_type = models.ForeignKey(GradingType, on_delete=models.DO_NOTHING, related_name='grade_list')
    grade = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    lesson_grade = models.ForeignKey(LessonGrade, on_delete=models.CASCADE, null=True, related_name='grade_list')

    def __str__(self):
        return  f"{self.lesson_grade.pk}. {self.grading_type.name} - {self.grade}"
