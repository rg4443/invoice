from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Invoice
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.template.loader import get_template
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from weasyprint import HTML
import locale

def index(request):
    return render(request, "index.html")

def invoice(request):
    return render(request, "invoice.html")

def generate_invoice(request):
    if request.method == 'POST':
        try:
            # Initialize logo_url to None
            logo_url = None
            # Access form data from POST
            logo = request.FILES.get('formFile')
            fs = FileSystemStorage()
            if logo:
                filename = fs.save(logo.name, logo)
                logo_url = fs.url(filename)

            company_name = request.POST.get('inputBName')
            billTo = request.POST.get('billTo')
            date = request.POST.get('inputDate')
            invoice_number = request.POST.get('invoice_number') or None
            email = request.POST.get('inputEmail4')
            company_number = request.POST.get('company')
            billing_number = request.POST.get('billing')
            taxed_percentage = request.POST.get('taxed') or None
            company_address = request.POST.get('inputAddress')
            billing_address = request.POST.get('inputBAddress')
            city = request.POST.get('inputCity')
            BCity = request.POST.get('BCity')
            state = request.POST.get('inputState')
            BState = request.POST.get('BState')
            Bzip = request.POST.get('Bzip') or None
            zip_code = request.POST.get('zip') or None
            statement = request.POST.get('statement')
            description = request.POST.get('description1')
            amount = request.POST.get('amount1') or None
            quantity = request.POST.get('quantity1') or None
            notes = request.POST.get('notes')
            selected_type = request.POST.get('invoice_type')

            # Create an instance of the Invoice model
            invoice = Invoice(
                logo=logo,
                company_name=company_name,
                billTo=billTo,
                date=date,
                invoice_number=invoice_number,
                email=email,
                company_number=company_number,
                billing_number=billing_number,
                taxed=taxed_percentage,
                company_address=company_address,
                billing_address=billing_address,
                BCity=BCity,
                city=city,
                state=state,
                BState=BState,
                Bzip=Bzip,
                zip=zip_code,
                statement=statement,
                description=description,
                amount=amount,
                quantity=quantity,
                notes=notes,
            )

            # Save the instance to the database
            invoice.save()

            # Process services
            services = []

            # Set the locale to the user's default
            locale.setlocale(locale.LC_ALL, '')

            total_amount = 0
            field_count = int(request.POST.get('field_count', 1))

            for i in range(1, field_count + 1):
                quantity = request.POST.get(f'quantity{i}')
                description = request.POST.get(f'description{i}')
                amount = request.POST.get(f'amount{i}')

                # Default amount to 0 if it is an empty string
                amount = int(amount) if amount and amount.isdigit() else 0

                # Format the amount as currency
                formatted_amount = locale.currency(amount, grouping=True)

                # Create a dictionary for each service
                service = {
                    'quantity': quantity,
                    'description': description,
                    'amount': formatted_amount,
                }

                # Add the service to the list
                services.append(service)

                # Update the total amount
                total_amount += int(amount)

                formatted_total = locale.currency(total_amount, grouping=True)

                # Calculate the tax amount based on the percentage
                if taxed_percentage:
                    taxed_percentage = int(taxed_percentage)
                    tax_amount = total_amount * (taxed_percentage / 100)
                else:
                    tax_amount = 0

                # Update the total amount with tax
                total_amount_with_tax = total_amount + tax_amount

                # Format the total amount with tax as currency
                formatted_total_with_tax = locale.currency(total_amount_with_tax, grouping=True)

            # Get the most recent invoice
            recent_invoice = Invoice.objects.latest('id')

            # Get the absolute URL for the image
            absolute_image_url = request.build_absolute_uri(invoice.logo.url) if invoice.logo else None

            # Pass the recent_invoice object to the template
            context = {
                'invoice': recent_invoice,
                'services': services,
                'total_amount': formatted_total,
                'field_count': field_count,
                'total_amount_with_tax': formatted_total_with_tax,
                'tax_amount': tax_amount,
                'taxed_percentage': taxed_percentage,
                'absolute_image_url': absolute_image_url,
                'selected_type': selected_type,
            }

            # Store relevant data in session
            request.session['invoice_data'] = {
                'logo': logo_url if logo_url else None,
                'company_name': company_name,
                'billTo': billTo,
                'date': date,
                'invoice_number': invoice_number,
                'email': email,
                'company_number': company_number,
                'billing_number': billing_number,
                'taxed_percentage': taxed_percentage,
                'company_address': company_address,
                'billing_address': billing_address,
                'city': city,
                'BCity': BCity,
                'state': state,
                'BState': BState,
                'Bzip': Bzip,
                'zip_code': zip_code,
                'statement': statement,
                'description': description,
                'amount': amount,
                'quantity': quantity,
                'notes': notes,
                'selected_type': selected_type,
            }

            # Render the HTML template
            html_template = get_template("generate_invoice.html")
            rendered_html = html_template.render(context)

            # Create a PDF response
            pdf_file = HTML(string=rendered_html).write_pdf()
            response = HttpResponse(pdf_file, content_type='application/pdf')

            return response
        except ValidationError as e:
            # Handle the validation error and provide a custom error message
            error_message = "Date is Required"
            return render(request, "invoice.html", {'error_message': error_message})

    return render(request, "invoice.html")

def invoice_history(request):
    # Retrieve data from session
    invoice_data = request.session.get('invoice_data', {})

    return render(request, 'history.html', {'invoice_data': invoice_data})
