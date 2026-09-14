from django.core.serializers import python
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import (
    Complaint,
    ComplaintUpdate,
    CitizenProfile,
    Notice,
    GramSabhaMeeting,
    DevelopmentWork,
    WorkImage,
    PanchayatFund,
)

from .models import (
    Complaint,
    ComplaintUpdate,
    CitizenProfile,
    GramSabhaMeeting,
    Notice
)



from .models import (
    Complaint,
    CitizenProfile,
    Notice
)

from .forms import (
    ComplaintForm,
    CitizenProfileForm
)
def language_selection(request):

    if request.method == "POST":

        language = request.POST.get("language")

        if language in ["hi", "en"]:

            request.session["language"] = language

            return redirect("home")

    return render(
        request,
        "language_selection.html"
    )


# ==========================================
# HOME
# ==========================================

def home(request):

    if "language" not in request.session:
        return redirect("language_selection")

    return render(
        request,
        "home.html"
    )

# ==========================================
# SUBMIT COMPLAINT
# ==========================================

@login_required
def submit_complaint(request):

    if request.method == "POST":

        form = ComplaintForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            complaint = form.save(
                commit=False
            )

            complaint.citizen = request.user

            complaint.save()

            messages.success(
                request,
                "Complaint submitted successfully."
            )

            return redirect(
                "complaint_success",
                complaint_id=complaint.complaint_id
            )

    else:

        form = ComplaintForm()

    return render(
        request,
        "submit_complaint.html",
        {
            "form": form
        }
    )


# ==========================================
# COMPLAINT SUCCESS
# ==========================================

@login_required
def complaint_success(
    request,
    complaint_id
):

    complaint = get_object_or_404(
        Complaint,
        complaint_id=complaint_id,
        citizen=request.user
    )

    return render(
        request,
        "complaint_success.html",
        {
            "complaint": complaint
        }
    )


# ==========================================
# TRACK COMPLAINT
# ==========================================

def track_complaint(request):

    complaint = None
    error = None

    if request.method == "POST":

        complaint_id = request.POST.get(
            "complaint_id"
        )

        if complaint_id:

            try:

                complaint = Complaint.objects.get(
                    complaint_id=complaint_id
                )

            except Complaint.DoesNotExist:

                error = (
                    "Complaint not found. "
                    "Please check your Complaint ID."
                )

        else:

            error = "Please enter Complaint ID."

    return render(
        request,
        "track_complaint.html",
        {
            "complaint": complaint,
            "error": error
        }
    )


# ==========================================
# SIGNUP
# ==========================================

def signup(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        email = request.POST.get(
            "email"
        )

        password = request.POST.get(
            "password"
        )

        confirm_password = request.POST.get(
            "confirm_password"
        )

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("signup")

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully."
        )

        return redirect("login")

    return render(
        request,
        "signup.html"
    )


# ==========================================
# LOGIN
# ==========================================

def citizen_login(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                "dashboard"
            )

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "login.html"
    )


# ==========================================
# LOGOUT
# ==========================================

def citizen_logout(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("home")


# ==========================================
# CITIZEN DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    user_complaints = Complaint.objects.filter(
        citizen=request.user
    )

    total_complaints = user_complaints.count()

    pending_complaints = user_complaints.filter(
        status="PENDING"
    ).count()

    progress_complaints = user_complaints.filter(
        status="PROGRESS"
    ).count()

    resolved_complaints = user_complaints.filter(
        status="RESOLVED"
    ).count()

    recent_complaints = user_complaints.order_by(
        "-created_at"
    )[:5]

    return render(
        request,
        "dashboard.html",
        {
            "total_complaints": total_complaints,
            "pending_complaints": pending_complaints,
            "progress_complaints": progress_complaints,
            "resolved_complaints": resolved_complaints,
            "recent_complaints": recent_complaints,
        }
    )


# ==========================================
# PROFILE
# ==========================================

@login_required
def profile(request):

    profile_data, created = CitizenProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "full_name": request.user.username,
            "mobile": "",
            "address": ""
        }
    )

    return render(
        request,
        "profile.html",
        {
            "profile": profile_data
        }
    )


# ==========================================
# EDIT PROFILE
# ==========================================

@login_required
def edit_profile(request):

    profile_data, created = CitizenProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "full_name": request.user.username,
            "mobile": "",
            "address": ""
        }
    )

    if request.method == "POST":

        form = CitizenProfileForm(
            request.POST,
            instance=profile_data
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect(
                "profile"
            )

    else:

        form = CitizenProfileForm(
            instance=profile_data
        )

    return render(
        request,
        "edit_profile.html",
        {
            "form": form
        }
    )


# ==========================================
# NOTICES
# ==========================================

def notices(request):

    notices = Notice.objects.filter(
        is_active=True
    ).order_by(
        "-notice_date"
    )

    return render(
        request,
        "notices.html",
        {
            "notices": notices
        }
    )


# ==========================================
# NOTICE DETAIL
# ==========================================

def notice_detail(
    request,
    notice_id
):

    notice = get_object_or_404(
        Notice,
        id=notice_id,
        is_active=True
    )

    return render(
        request,
        "notice_detail.html",
        {
            "notice": notice
        }
    )
def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def development(request):
    return render(request, "development.html")
def contact(request):
    return render(request, "contact.html")

# =========================
# ADMIN DASHBOARD
# =========================

@login_required
def admin_dashboard(request):

    # Sirf staff/admin user dashboard access kar sakta hai
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to access admin dashboard.")
        return redirect("dashboard")

    complaints = Complaint.objects.all().order_by("-created_at")

    total_complaints = complaints.count()
    pending_complaints = complaints.filter(status="PENDING").count()
    review_complaints = complaints.filter(status="REVIEW").count()
    progress_complaints = complaints.filter(status="PROGRESS").count()
    resolved_complaints = complaints.filter(status="RESOLVED").count()
    rejected_complaints = complaints.filter(status="REJECTED").count()

    recent_complaints = complaints[:10]

    context = {
        "complaints": complaints,
        "recent_complaints": recent_complaints,

        "total_complaints": total_complaints,
        "pending_complaints": pending_complaints,
        "review_complaints": review_complaints,
        "progress_complaints": progress_complaints,
        "resolved_complaints": resolved_complaints,
        "rejected_complaints": rejected_complaints,
    }

    return render(
        request,
        "admin_dashboard.html",
        context
    )


# =========================
# ADMIN COMPLAINT UPDATE
# =========================

@login_required
def admin_update_complaint(request, complaint_id):

    # Sirf staff/admin access
    if not request.user.is_staff:
        messages.error(request, "You are not authorized.")
        return redirect("dashboard")

    complaint = get_object_or_404(
        Complaint,
        complaint_id=complaint_id
    )

    if request.method == "POST":

        new_status = request.POST.get("status")
        admin_response = request.POST.get("admin_response", "").strip()

        # Status update
        if new_status in dict(Complaint.STATUS_CHOICES):
            complaint.status = new_status

        # Admin response update
        complaint.admin_response = admin_response

        complaint.save()

        # Complaint history me update save karo
        ComplaintUpdate.objects.create(
            complaint=complaint,
            status=complaint.status,
            message=admin_response
        )

        messages.success(
            request,
            f"Complaint {complaint.complaint_id} updated successfully."
        )

        return redirect(
            "admin_update_complaint",
            complaint_id=complaint.complaint_id
        )

    updates = complaint.updates.all().order_by("-created_at")

    return render(
        request,
        "admin_complaint_detail.html",
        {
            "complaint": complaint,
            "updates": updates,
        }
    )

@login_required
def complaint_detail(request, complaint_id):

    complaint = get_object_or_404(
        Complaint,
        complaint_id=complaint_id,
        citizen=request.user
    )

    updates = complaint.updates.all().order_by("-created_at")

    return render(
        request,
        "complaint_detail.html",
        {
            "complaint": complaint,
            "updates": updates,
        }
    )
def meetings(request):
    meetings = GramSabhaMeeting.objects.all().order_by("meeting_date", "meeting_time")

    return render(
        request,
        "meetings.html",
        {
            "meetings": meetings
        }
    )


def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(
        GramSabhaMeeting,
        id=meeting_id
    )

    return render(
        request,
        "meeting_detail.html",
        {
            "meeting": meeting
        }
    )
def development(request):
    works = DevelopmentWork.objects.all().order_by("-created_at")

    return render(
        request,
        "development.html",
        {
            "works": works
        }
    )


def development_detail(request, work_id):
    work = get_object_or_404(
        DevelopmentWork,
        id=work_id
    )

    images = work.images.all().order_by("-uploaded_at")

    return render(
        request,
        "development_detail.html",
        {
            "work": work,
            "images": images,
        }
    )
def schemes(request):
    return render(request, "schemes.html")
def members(request):
    return render(request, "members.html")
def funds(request):

    selected_year = request.GET.get("year", "").strip()

    funds = PanchayatFund.objects.all().order_by("-date")

    if selected_year:
        funds = funds.filter(year=selected_year)

    total_received = sum(
        fund.amount_received for fund in funds
    )

    total_spent = sum(
        fund.amount_spent for fund in funds
    )

    remaining = total_received - total_spent

    years = (
        PanchayatFund.objects
        .values_list("year", flat=True)
        .distinct()
        .order_by("-year")
    )

    return render(
        request,
        "funds.html",
        {
            "funds": funds,
            "total_received": total_received,
            "total_spent": total_spent,
            "remaining": remaining,
            "years": years,
            "selected_year": selected_year,
        }
    )
def meetings(request):
    meetings = GramSabhaMeeting.objects.all().order_by("-meeting_date")

    return render(
        request,
        "meetings.html",
        {
            "meetings": meetings
        }
    )


def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(
        GramSabhaMeeting,
        id=meeting_id
    )

    return render(
        request,
        "meeting_detail.html",
        {
            "meeting": meeting
        }
    )