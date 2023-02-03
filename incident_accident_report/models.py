from django.db import models
from accounts.models import StudentProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from school_management.utils import send_mail
from django.conf import settings




class IncidentAccidentReport(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    details = models.TextField()
    first_aid_administered = models.TextField()
    witnesses = models.CharField(max_length=255)
    send_notification_guardian = models.BooleanField(default=False)
    send_mail_guardian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


@receiver(post_save, sender=IncidentAccidentReport, dispatch_uid="send_mail_notification_incident_accident")
def send_mail_notification_incident_accident(sender, instance, **kwargs):
    if instance.send_mail_guardian:
        message = instance.details
        send_mail(subject="Incident Alert", message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[instance.student.guardian.user.email])

    if instance.send_notification_guardian:
        pass