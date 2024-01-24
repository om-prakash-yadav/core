from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout


from django.contrib.auth.decorators import login_required

from .models import *

from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import InvoiceForm, LineItemFormset, OfferLetterForm, IntroductoryLetterForm, AppointmentLetterForm, CompanyForm
import pdfkit

# importing the openai API
import openai

openai.api_key = "sk_test_51JQ5QvSIL5ZQZ2Z2"


@login_required
def index(request):
#   user = request.user
#   if not Company.objects.filter(user=user).exists():
#                 return company_form_view(request)

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)







def generate_offer_letter(request):
    if request.method == 'POST':
        form = OfferLetterForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
            # Redirect to a success page or another view after successful form submission
            return redirect('generate_offer_letter')  # Replace 'success_page' with the name of your success page view
        else:
            print(form.errors)
    else:
        form = OfferLetterForm()
        try:
            company = Company.objects.get(user=request.user)  # Assuming you associate the company with the user
        except Company.DoesNotExist:
            company = None  # Handle the case when the company does not exist
    
    return render(request, 'pages/offer_letter_form.html', {'form': form , 'company':company})


def generate_introductory_letter(request):
    if request.method == 'POST':
        form = IntroductoryLetterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view after successful form submission
            return redirect('generate_introductory_letter')  # Replace 'success_page' with the name of your success page view
    else:
        form = OfferLetterForm()
    return render(request, 'pages/introductory_letter_form.html', {'form': form})


def generate_appointment_letter(request):
    if request.method == 'POST':
        form = AppointmentLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/appointment_letter_form.html', {'form': form})
    else:
        form = AppointmentLetterForm()
    return render(request, 'pages/appointment_letter_form.html', {'form': form})



class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'pages/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice-list')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

  
    if request.method == 'GET':
        formset = LineItemFormset(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(customer=form.data["customer"],
                    customer_email=form.data["customer_email"],
                    billing_address = form.data["billing_address"],
                    date=form.data["date"],
                    due_date=form.data["due_date"], 
                    message=form.data["message"],
                    )
            # invoice.save()
            
        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0
            for form in formset:
                service = form.cleaned_data.get('service')
                description = form.cleaned_data.get('description')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')
                if service and description and quantity and rate:
                    amount = float(rate)*float(quantity)
                    total += amount
                    LineItem(customer=invoice,
                            service=service,
                            description=description,
                            quantity=quantity,
                            rate=rate,
                            amount=amount).save()
            invoice.total_amount = total
            invoice.save()
            try:
                generate_PDF(request, id=invoice.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('invoice-list')
    context = {
        "title" : "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'pages/invoice-create.html', context)


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()

    context = {
        "company": {
            "name": "Tetratrion Technologies Pvt. Ltd.",
            "address" :"Odisha, India",
            "phone": "+91 0000000000",
            "email": "info.tetratrion.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "customer": invoice.customer,
        "customer_email": invoice.customer_email,
        "date": invoice.date,
        "due_date": invoice.due_date,
        "billing_address": invoice.billing_address,
        "message": invoice.message,
        "lineitem": lineitem,

    }
    return render(request, 'pages/pdf_template.html', context)

def generate_PDF(request, id):
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response


def change_status(request):
    return redirect('invoice-list')

def view_404(request,  *args, **kwargs):

    return redirect('invoice-list')

def remove_invoice(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id')
        # Your logic to remove the invoice with the given invoice_id
        try:
            invoice = Invoice.objects.get(pk=invoice_id)
            invoice.delete()
            # Optionally, you can return a success message or a JSON response
            return HttpResponse("Invoice successfully removed", status=200)
        except Invoice.DoesNotExist:
            # If the invoice does not exist, return a relevant error message or a JSON response
            return HttpResponse("Invoice does not exist", status=404)
    # Handle the case if the request method is not POST
    return HttpResponse("Method not allowed", status=405)


def generate_offer_letter_content(request):
    prompt = f"Generate an offer letter for om prakash for the position of software engineer starting on 17th july 2023 with a salary of 13200."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200
    )
    print(response)
    generated_content = response.choices[0].text.strip()

    return generated_content

def company_form_view(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view after successful form submission
            return redirect('index')
        else:
            print(form.errors)  # Print form errors in the console

    else:
        form = CompanyForm()
    return render(request, 'pages/company_form.html', {'form': form})

