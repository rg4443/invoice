# Generated by Django 5.0 on 2024-01-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("final", "0008_invoice_statement"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvoiceHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="logo_images/"),
                ),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("billTo", models.CharField(blank=True, max_length=255, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                ("invoice_number", models.IntegerField(blank=True, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "company_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "billing_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("taxed", models.IntegerField(blank=True, null=True)),
                (
                    "company_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "billing_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("BCity", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("state", models.CharField(blank=True, max_length=255, null=True)),
                ("BState", models.CharField(blank=True, max_length=255, null=True)),
                ("Bzip", models.IntegerField(blank=True, null=True)),
                ("zip", models.IntegerField(blank=True, null=True)),
                ("statement", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("amount", models.IntegerField(blank=True, null=True)),
                ("quantity", models.IntegerField(blank=True, null=True)),
                ("notes", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
