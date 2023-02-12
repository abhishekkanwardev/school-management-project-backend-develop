from django.db import models

from accounts.models import StudentProfile
from school_process.models import Lesson,Class



PROGRESS_TYPE = (
    ('Attendance ', 'Attendance '),
    ('Punctuality', 'Punctuality'),
    ('Effort', 'Effort'),
    ('Behaviour', 'Behaviour'),
    ('Homework', 'Homework'),
    ('Quiz', 'Quiz'),

)

SCORE = (
    ('Unacceptable', 'Unacceptable'),
    ('On Level', 'On Level'),
    ('Off Level', 'Off Level'),
)


class ProggressRecord(models.Model):
    date = models.DateField()


class StudentProgress(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name = 'student_progress_list')
    progress_record = models.ForeignKey(ProggressRecord, on_delete=models.CASCADE, null=True, related_name='student_progress_list')

    def __str__(self):
        return  f"{self.pk}.{self.student.user.get_full_name()} progress"


class ProgressScore(models.Model):
    progress_type = models.CharField(max_length=30, choices=PROGRESS_TYPE)
    score = models.CharField(max_length=30, choices=SCORE, default='On Level')

    def __str__(self):
        return  f"{self.progress_type} - {self.score}"


class LessonProgress(models.Model):
    progressScore = models.ManyToManyField(ProgressScore, blank=True, related_name='lesson_progress_list')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_progress_list')
    student_progress = models.ForeignKey(StudentProgress, on_delete=models.CASCADE, null=True, related_name='lesson_progress_list')

    def __str__(self):
        return  f"{self.pk}.{self.lesson.lesson_name} progress for {self.student_progress.student.user.get_full_name()}"

