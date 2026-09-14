from django.urls import path
from . import views


urlpatterns = [

    # ==========================================
    # LANGUAGE SELECTION
    # ==========================================

    path(
        "language/",
        views.language_selection,
        name="language_selection"
    ),


    # ==========================================
    # HOME
    # ==========================================

    path(
        "",
        views.home,
        name="home"
    ),


    # ==========================================
    # COMPLAINT
    # ==========================================

    path(
        "complaint/",
        views.submit_complaint,
        name="submit_complaint"
    ),

    path(
        "complaint/success/<str:complaint_id>/",
        views.complaint_success,
        name="complaint_success"
    ),

    path(
        "complaint/detail/<str:complaint_id>/",
        views.complaint_detail,
        name="complaint_detail"
    ),

    path(
        "track/",
        views.track_complaint,
        name="track_complaint"
    ),


    # ==========================================
    # AUTHENTICATION
    # ==========================================

    path(
        "signup/",
        views.signup,
        name="signup"
    ),

    path(
        "login/",
        views.citizen_login,
        name="login"
    ),

    path(
        "logout/",
        views.citizen_logout,
        name="logout"
    ),


    # ==========================================
    # CITIZEN
    # ==========================================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "profile/edit/",
        views.edit_profile,
        name="edit_profile"
    ),


    # ==========================================
    # INFORMATION PAGES
    # ==========================================

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "services/",
        views.services,
        name="services"
    ),

    path(
        "schemes/",
        views.schemes,
        name="schemes"
    ),

    path(
        "members/",
        views.members,
        name="members"
    ),

    path(
        "funds/",
        views.funds,
        name="funds"
    ),


    # ==========================================
    # NOTICES
    # ==========================================

    path(
        "notices/",
        views.notices,
        name="notices"
    ),

    path(
        "notices/<int:notice_id>/",
        views.notice_detail,
        name="notice_detail"
    ),


    # ==========================================
    # DEVELOPMENT
    # ==========================================

    path(
        "development/",
        views.development,
        name="development"
    ),

    path(
        "development/<int:work_id>/",
        views.development_detail,
        name="development_detail"
    ),


    # ==========================================
    # GRAM SABHA MEETINGS
    # ==========================================

    path(
        "meetings/",
        views.meetings,
        name="meetings"
    ),

    path(
        "meetings/<int:meeting_id>/",
        views.meeting_detail,
        name="meeting_detail"
    ),


    # ==========================================
    # CONTACT
    # ==========================================

    path(
        "contact/",
        views.contact,
        name="contact"
    ),


    # ==========================================
    # ADMIN DASHBOARD
    # ==========================================

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "admin-dashboard/complaint/<str:complaint_id>/",
        views.admin_update_complaint,
        name="admin_update_complaint"
    ),
]