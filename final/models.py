from django.db import models

class Invoice(models.Model):
    logo = models.ImageField(upload_to='logo_images/', null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    billTo = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    invoice_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    company_number = models.CharField(max_length=255, null=True, blank=True)
    billing_number = models.CharField(max_length=255, null=True, blank=True)
    taxed = models.IntegerField(null=True, blank=True)
    company_address = models.CharField(max_length=255, null=True, blank=True)
    billing_address = models.CharField(max_length=255, null=True, blank=True)
    BCity = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    BState = models.CharField(max_length=255, null=True, blank=True)
    Bzip = models.IntegerField(null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    statement = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    quantity  = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Invoice #{self.id}"
