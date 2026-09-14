
from django import forms

from .models import Complaint, CitizenProfile


class ComplaintForm(forms.ModelForm):

    class Meta:

        model = Complaint

        fields = [
            "category",
            "subject",
            "description",
            "location",
        ]

        widgets = {

            "category": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter complaint subject"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Describe your problem..."
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Village / Street / Location"
                }
            ),
        }


class CitizenProfileForm(forms.ModelForm):

    class Meta:

        model = CitizenProfile

        fields = [
            "full_name",
            "mobile",
            "address",
        ]

        widgets = {

            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your full name"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your mobile number"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter your address"
                }
            ),
        }

