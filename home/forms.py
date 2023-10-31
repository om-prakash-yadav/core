from django import forms
from .models import AppointmentLetter, OfferLetter, Company, Invoice, LineItem , IntroductoryLetter
from django.forms import formset_factory


class OfferLetterForm(forms.ModelForm):
    class Meta:
        model = IntroductoryLetter
        fields = [
            'candidate_name',
            'candidate_city',
            'candidate_pin_code',
            'candidate_state',
            'candidate_country',
            'candidate_phone',
            'candidate_email',
            'job_title',
            'joining_date',
            'salary',
        ]
        widgets = {
    'candidate_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Candidate Name'}),
    'candidate_city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'City'}),
    'candidate_pin_code': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Pin Code'}),
    'candidate_state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'State'}),
    'candidate_country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Country'}),
    'candidate_phone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Phone'}),
    'candidate_email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
    'job_title': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Job Title'}),
    'joining_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Joining Date'}),
    'salary': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Salary'}),
                    }

class IntroductoryLetterForm(forms.ModelForm):
    class Meta:
        model = OfferLetter
        fields = [
            'candidate_name',
            'candidate_city',
            'candidate_pin_code',
            'candidate_state',
            'candidate_country',
            'candidate_phone',
            'candidate_email',
            'job_title',
            'joining_date',
            'salary',
        ]
        widgets = {
    'candidate_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Candidate Name'}),
    'candidate_city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'City'}),
    'candidate_pin_code': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Pin Code'}),
    'candidate_state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'State'}),
    'candidate_country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Country'}),
    'candidate_phone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Phone'}),
    'candidate_email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
    'job_title': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Job Title'}),
    'joining_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Joining Date'}),
    'salary': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Salary'}),
                    }



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'company_logo',
            'company_city',
            'company_pin_code',
            'company_state',
            'company_country',
            'company_phone',
            'company_email',
            'company_cin',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_logo': forms.FileInput(attrs={'class': 'form-control'}),
            'company_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'company_pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'}),
            'company_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'company_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'company_cin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CIN'}),
        }


class AppointmentLetterForm(forms.ModelForm):
    class Meta:
        model = AppointmentLetter
        fields = [
            'employee_name',
            'employee_address',
            'employee_city',
            'employee_pin_code',
            'employee_state',
            'employee_country',
            'employee_phone',
            'employee_email',
            'joining_date',
            'designation',
            'department',
            'salary',
        ]
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}),
            'employee_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'employee_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'employee_pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'}),
            'employee_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'employee_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'employee_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'employee_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Joining Date'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }



class InvoiceForm(forms.Form):
    customer = forms.CharField(
        label='Customer',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Customer/Company Name',
        })
    )
    customer_email = forms.CharField(
        label='Customer Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'customer@company.com',
        })
    )
    billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Billing Address',
        })
    )
    message = forms.CharField(
        label='Message/Note',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Message',
        })
    )

class LineItemForm(forms.Form):
    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Service Name',
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter item name here',
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.NumberInput(attrs={
            'class': 'form-control quantity',
            'placeholder': 'Quantity',
        })
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.TextInput(attrs={
            'class': 'form-control rate',
            'placeholder': 'Rate',
        })
    )

LineItemFormset = formset_factory(LineItemForm, extra=1)
