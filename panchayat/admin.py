from django.contrib import admin

from .models import (
    CitizenProfile,
    Complaint,
    ComplaintImage,
    ComplaintUpdate,
    Notice,
    DevelopmentWork,
    WorkImage,
    GramSabhaMeeting,
    PanchayatFund,
)


# =========================================================
# CITIZEN PROFILE
# =========================================================

@admin.register(CitizenProfile)
class CitizenProfileAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "mobile",
        "user",
        "created_at",
    )

    search_fields = (
        "full_name",
        "mobile",
        "user__username",
    )

    list_filter = (
        "created_at",
    )


# =========================================================
# COMPLAINT IMAGE INLINE
# =========================================================

class ComplaintImageInline(admin.TabularInline):

    model = ComplaintImage

    extra = 1


# =========================================================
# COMPLAINT UPDATE INLINE
# =========================================================

class ComplaintUpdateInline(admin.TabularInline):

    model = ComplaintUpdate

    extra = 1

    readonly_fields = (
        "created_at",
    )


# =========================================================
# COMPLAINT
# =========================================================

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = (
        "complaint_id",
        "citizen",
        "category",
        "subject",
        "status",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "category",
        "status",
        "created_at",
    )

    search_fields = (
        "complaint_id",
        "subject",
        "description",
        "location",
        "citizen__username",
    )

    readonly_fields = (
        "complaint_id",
        "created_at",
        "updated_at",
    )

    inlines = (
        ComplaintImageInline,
        ComplaintUpdateInline,
    )

    ordering = (
        "-created_at",
    )


# =========================================================
# NOTICE
# =========================================================

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "notice_date",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "notice_date",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-notice_date",
    )


# =========================================================
# DEVELOPMENT WORK IMAGE INLINE
# =========================================================

class WorkImageInline(admin.TabularInline):

    model = WorkImage

    extra = 1


# =========================================================
# DEVELOPMENT WORK
# =========================================================

@admin.register(DevelopmentWork)
class DevelopmentWorkAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "location",
        "budget",
        "progress",
        "status",
        "start_date",
        "expected_completion",
    )

    list_filter = (
        "status",
        "start_date",
        "expected_completion",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )

    inlines = (
        WorkImageInline,
    )

    ordering = (
        "-created_at",
    )


# =========================================================
# GRAM SABHA MEETING
# =========================================================

@admin.register(GramSabhaMeeting)
class GramSabhaMeetingAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "meeting_date",
        "meeting_time",
        "venue",
        "created_at",
    )

    list_filter = (
        "meeting_date",
    )

    search_fields = (
        "title",
        "description",
        "venue",
    )

    ordering = (
        "-meeting_date",
    )
@admin.register(PanchayatFund)
class PanchayatFundAdmin(admin.ModelAdmin):

    list_display = (
        "year",
        "fund_type",
        "description",
        "amount_received",
        "amount_spent",
        "remaining_amount",
        "date",
    )

    list_filter = (
        "year",
        "fund_type",
        "date",
    )

    search_fields = (
        "year",
        "description",
    )

    ordering = (
        "-date",
    )