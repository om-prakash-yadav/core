from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OfferLetter(models.Model):
    candidate_name = models.CharField(max_length=100)
    candidate_city = models.CharField(max_length=100)
    candidate_pin_code = models.CharField(max_length=10)
    candidate_state = models.CharField(max_length=100)
    candidate_country = models.CharField(max_length=100)
    candidate_phone = models.CharField(max_length=15)  # Adjust the max length as necessary
    candidate_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.FloatField()

    def __str__(self):
        return  self.candidate_name
    
class IntroductoryLetter(models.Model):
    candidate_name = models.CharField(max_length=100)
    candidate_city = models.CharField(max_length=100)
    candidate_pin_code = models.CharField(max_length=10)
    candidate_state = models.CharField(max_length=100)
    candidate_country = models.CharField(max_length=100)
    candidate_phone = models.CharField(max_length=15)  # Adjust the max length as necessary
    candidate_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.FloatField()

    def __str__(self):
        return self.candidate_name

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/')
    company_city = models.CharField(max_length=100)
    company_pin_code = models.CharField(max_length=10)
    company_state = models.CharField(max_length=100)
    company_country = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=15)  # Adjust the max length as necessary
    company_email = models.EmailField()
    company_cin = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
    

class AppointmentLetter(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=100)
    employee_city = models.CharField(max_length=100)
    employee_pin_code = models.CharField(max_length=10)
    employee_state = models.CharField(max_length=100)
    employee_country = models.CharField(max_length=100)
    employee_phone = models.CharField(max_length=15)
    employee_email = models.EmailField()
    joining_date = models.DateField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.employee_name



class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    message = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)
   