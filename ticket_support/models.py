from django.utils.translation import gettext_lazy as _
from django.db import models

from accounts.models import User

# Create your models here.

class TicketTypes(models.TextChoices):
    # IT and Tech
    ACCOUNTS = "accounts", _("Accounts")
    CLASSES = "classes", _("Classes")
    TEAMS = "teams", _("Teams")
    PEARSON_E_TEXTBOOK = "pearson_e_textbook", _("Pearson E-Text Book")

    # Registrations and Admission
    UNIFORMS = "uniforms", _("Uniforms")
    FEES = "fees", _("Fees")
    BOOKS = "books", _("Books")
    STUDENT_DOCUMENTS = "student_documents", _("Student's Documents")

    # Teacher
    HOMEWORK = "homework", _("Homework")
    CLASSROOM_CONCERNS = "classroom_concerns", _("Classroom Concerns")
    ACADEMIC_PROGRRESS = "academic_progress", _("Academic Progress")

    # Student Counseller
    VIOLENCE = "violence", _("Violence")
    BULLYING = "bullying", _("Bullying")
    ID_SPECIAL_NEEDS = "identifying_special_needs", _("Identifying Special Needs")
    UNIFORM_ISSUE = "uniform_issue", _("Unioform Issue")
    STUDENT_ABSENCE = "student_absence", _("Student Absence")

    # Principal
    TEACHER_CLASS_CONCERN = "teacher_rel_class_concern", _("Teacher Related Class Concerns")
    TEACHER_NOT_COMMUNICATING = "teacher_not_communicationg", _("Teacher Not Communicationg")
    TEACHER_ATTITUDE = "teacher_attitude", _("Teacher's Attitude with Student")
    TEACHER_ABSENCE = "teacher_absence", _("Teacher's Recurring Absence and Lateness")
    ACADEMIC_CONCERNS = "academic_concern", _("Academic Concerns")

    # Transport and Maintenance
    STUDENT_BEHAVIOUR = "student_behaviour", _("Student Behaviour on Buses")
    NANNY = "nanny", _("Nanny")
    MAINTENANCE = "maintenance", _("Building Maintenance")


class Ticket(models.Model):
    STATUS = (
        ("AC", "Active"),
        ("OH", "On Hold"),
        ("CL", "Closed")
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="ticket_author", null=False, blank=False)
    ticket_type = models.CharField(max_length=50, choices=TicketTypes.choices, null=False, blank=False)
    assignees = models.ManyToManyField(User, related_name="ticket_assignees",verbose_name=_("assignees"))
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS, default="AC")
    closed_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="ticket_closer", null=True)
    closing_remarks = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.author} -> {self.title}"


class TicketConversation(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING, related_name="ticket_convo", null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="ticket_convo")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} -> {self.created_at}"
