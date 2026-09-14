from django.db import models
from django.contrib.auth.models import User


# ==========================================
# CITIZEN PROFILE
# ==========================================

class CitizenProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=15
    )

    address = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name


# ==========================================
# COMPLAINT
# ==========================================

class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ("ROAD", "Road"),
        ("WATER", "Water Supply"),
        ("LIGHT", "Street Light"),
        ("SANITATION", "Sanitation"),
        ("DRAINAGE", "Drainage"),
        ("ELECTRICITY", "Electricity"),
        ("EDUCATION", "Education"),
        ("HEALTH", "Health"),
        ("SCHEME", "Government Scheme"),
        ("OTHER", "Other"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("REVIEW", "Under Review"),
        ("PROGRESS", "In Progress"),
        ("RESOLVED", "Resolved"),
        ("REJECTED", "Rejected"),
    ]

    complaint_id = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    citizen = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    subject = models.CharField(
        max_length=200
    )

    description = models.TextField()

    location = models.CharField(
        max_length=300
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    admin_response = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.complaint_id:

            last_id = Complaint.objects.count() + 1

            self.complaint_id = (
                f"GP-2026-{last_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.complaint_id


# ==========================================
# COMPLAINT IMAGE
# ==========================================

class ComplaintImage(models.Model):

    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="complaints/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.complaint.complaint_id


# ==========================================
# COMPLAINT UPDATE / TIMELINE
# ==========================================

class ComplaintUpdate(models.Model):

    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name="updates"
    )

    status = models.CharField(
        max_length=20,
        choices=Complaint.STATUS_CHOICES
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.complaint.complaint_id


# ==========================================
# PANCHAYAT NOTICE
# ==========================================

class Notice(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    notice_date = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# ==========================================
# DEVELOPMENT WORK
# ==========================================

class DevelopmentWork(models.Model):

    STATUS_CHOICES = [
        ("PLANNED", "Planned"),
        ("PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    ]

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    location = models.CharField(
        max_length=300
    )

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    progress = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PLANNED"
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    expected_completion = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# ==========================================
# DEVELOPMENT WORK IMAGE
# ==========================================

class WorkImage(models.Model):

    work = models.ForeignKey(
        DevelopmentWork,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="development/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.work.title


# ==========================================
# GRAM SABHA MEETING
# ==========================================

class GramSabhaMeeting(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    meeting_date = models.DateField()

    meeting_time = models.TimeField()

    venue = models.CharField(
        max_length=200
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class PanchayatFund(models.Model):

    FUND_TYPES = [
        ("GENERAL", "General Fund"),
        ("FINANCE", "Finance Commission"),
        ("SCHEME", "Government Scheme"),
        ("OTHER", "Other"),
    ]

    year = models.CharField(max_length=20)

    fund_type = models.CharField(
        max_length=20,
        choices=FUND_TYPES
    )

    description = models.CharField(max_length=300)

    amount_received = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    amount_spent = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def remaining_amount(self):
        return self.amount_received - self.amount_spent

    def __str__(self):
        return f"{self.year} - {self.description}"