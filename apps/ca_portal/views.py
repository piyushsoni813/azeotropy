
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm
from .forms import Azeo_idForm
#from django.contrib import messages
from .models import Extendeduser
from .models import Azeo_id_user
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.exceptions import ValidationError

# added for visitor pdf
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from io import BytesIO
# upto this

def Index(request):
    return render(request, 'main_website/index.html')

def Schedule(request):
    return render(request, 'main_website/schedule.html')

def Events(request):
    return render(request, 'main_website/events.html')

def About_us(request):
    return render(request, 'main_website/about_us.html')

def Sponsors(request):
    return render(request, 'main_website/sponsors.html')

def Competition(request):
    return render(request, 'main_website/competitions.html')

def Workshop(request):
    return render(request, 'main_website/workshop.html')

def Chem_o_philia(request):
    return render(request, 'main_website/competitions_folder/chem-o-philia.html')

def Chem_e_cross(request):
    return render(request, 'main_website/competitions_folder/chem-e-cross.html')

def Optimiser(request):
    return render(request, 'main_website/competitions_folder/optimiser.html')

def Luminescence(request):
    return render(request, 'main_website/events_folder/luminescence.html')

def Q_viz_it(request):
    return render(request, 'main_website/competitions_folder/q-viz-it.html')

def IDP(request):
    return render(request, 'main_website/competitions_folder/IDP.html')

def workshop(request):
    return render(request, 'main_website/events_folder/DWSIM.html')

def Impact(request):
    return render(request, 'main_website/events_folder/impact.html')

def Ansys(request):
    return render(request, 'main_website/events_folder/ansys.html')

def R_workshop(request):
    return render(request, 'main_website/events_folder/R_workshop.html')

def Chemathon(request):
    return render(request, 'main_website/competitions_folder/chemathon.html')

def Cipher(request):
    return render(request, 'main_website/competitions_folder/cipher.html')

def Lca(request):
    return render(request, 'main_website/competitions_folder/lca.html')

def AZeopardy(request):
    return render(request, 'main_website/competitions_folder/azeopardy.html')

def AZeorover(request):
    return render(request, 'main_website/competitions_folder/azeorover.html')

def AZeocube(request):
    return render(request, 'main_website/competitions_folder/azeocube.html')

def Chempreneur(request):
    return render(request, 'main_website/competitions_folder/chempreneur.html')


def Affiche(request):
    return render(request, 'main_website/competitions_folder/affiche.html')

def Paneldiscussion(request):
    return render(request, 'main_website/events_folder/panel-discussion.html')

def Paneld2(request):
    return render(request, 'main_website/events_folder/paneld2.html')

def Paneld1(request):
    return render(request, 'main_website/events_folder/paneld1.html')

def Matlab(request):
    return render(request, 'main_website/events_folder/matlab.html')

def Python(request):
    return render(request, 'main_website/events_folder/python.html')

def Research101(request):
    return render(request, 'main_website/events_folder/research101.html')

def DWSIM(request):
    return render(request, 'main_website/events_folder/DWSIM.html')


def COMSOL(request):
    return render(request, 'main_website/events_folder/COMSOL.html')

def OpenModelica(request):
    return render(request, 'main_website/events_folder/OpenModelica.html')

def OpenFoam(request):
    return render(request, 'main_website/events_folder/OpenFOAM.html')

def FETA(request):
    return render(request, 'main_website/events_folder/FETA.html')

def Chemvision(request):
    return render(request, 'main_website/events_folder/chemvision.html')

def Chemvision1(request):
    return render(request, 'main_website/events_folder/chemvision1.html')

def Chemvision2(request):
    return render(request, 'main_website/events_folder/chemvision2.html')

def Speaker1(request):
    return render(request, 'main_website/events_folder/speaker1.html')

def Registration(request):

    return render(request,'ca_portal/ca.html')

def user_register(request):
    template = 'ca_portal/register.html'  # Template for rendering the form

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = RegisterForm(request.POST)
        
        # Check whether it's valid
        if form.is_valid():
            # Check if the email already exists
            if Extendeduser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            else:
                # Create an Extendeduser instance
                extendeduser = Extendeduser()
                extendeduser.first_name = form.cleaned_data['first_name']
                extendeduser.last_name = form.cleaned_data['last_name']
                extendeduser.phone_number = form.cleaned_data['phone_number']
                extendeduser.alternate_phone_number = form.cleaned_data['alternate_phone_number']
                extendeduser.college = form.cleaned_data['college']
                extendeduser.current_year = form.cleaned_data['current_year']
                extendeduser.permanent_address = form.cleaned_data['permanent_address']
                extendeduser.state = form.cleaned_data['state']
                extendeduser.email = form.cleaned_data['email']
                extendeduser.pincode = form.cleaned_data['pincode']

                # Save the user data
                extendeduser.save()

                # Prepare the email
                subject = "Successfully registered for AZeotropy Campus Ambassador"
                name1 = str(extendeduser.first_name).title()
                html_message = render_to_string("ca_portal/mail.html", {'name': name1})
                message = strip_tags(html_message)
                to_email = extendeduser.email

                email = EmailMultiAlternatives(subject, message, 'azeotropy2025@gmail.com', [to_email])
                email.attach_alternative(html_message, 'text/html')
                email.send()

                # Success message
                success_message = 'You have successfully registered on CA portal'
                return render(request, "ca_portal/ca.html", {'message': success_message})
    
    # If not a POST request, display the empty form
    else:
        form = RegisterForm()
    
    return render(request, template, {'form': form})

def AZeo_id(request):
    # if this is a POST request we need to process the form data
        template = 'main_website/register_user.html'

        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = Azeo_idForm(request.POST)
            # check whether it's valid:
            if form.is_valid():

                if Azeo_id_user.objects.filter(email=form.cleaned_data['email']).exists():
                    return render(request, template, {
                        'form': form,
                        'error_message': 'Email already exists.'
                    })



                else:
                    # print('hellow world')
                    # Create the user:

                    # user = User.objects.create_user(
                    #     # form.cleaned_data['username'],
                    #     form.cleaned_data['email']

                    # )

                    extendeduser = Azeo_id_user()
                    extendeduser.first_name = form.cleaned_data['first_name']
                    extendeduser.last_name = form.cleaned_data['last_name']
                    extendeduser.phone_number = form.cleaned_data['phone_number']
                    extendeduser.alternate_phone_number = form.cleaned_data['alternate_phone_number']
                    extendeduser.college = form.cleaned_data['college']
                    extendeduser.current_year = form.cleaned_data['current_year']
                    extendeduser.permanent_address = form.cleaned_data['permanent_address']
                    extendeduser.state = form.cleaned_data['state']
                    extendeduser.email = form.cleaned_data['email']
                    extendeduser.pincode = form.cleaned_data['pincode']
                    Azeo_no =f"AZ-{extendeduser.first_name[:3].upper()}-{Azeo_id_user.objects.only('id').last().id+1}"
                    extendeduser.azeo_id = Azeo_no
                    # extendeduser.user = user
                    extendeduser.save()





                    subject = "Successfully created your AZeo ID "
                    # message = f'congratulations {extendeduser.first_name}{extendeduser.last_name} have successfully registered on CA portal'
                    to_email = extendeduser.email

                    name1 = str(extendeduser.first_name).title()
                    collegename = str(extendeduser.college).title()
                    html_message = render_to_string("main_website/email.html",{'name':name1,'college':collegename,'AZeo_ID':Azeo_no})
                    message = strip_tags(html_message)

                    email3 = EmailMultiAlternatives(subject,
                                message,
                                'azeo2022@gmail.com',
                                [to_email],
                                )
                    email3.attach_alternative(html_message,'text/html')

                            # Generate PDF
                    # pdf_buffer = generate_pdf({
                    #     'first_name': extendeduser.first_name,
                    #     'last_name': extendeduser.last_name,
                    #     'azeo_id': Azeo_no
                    # })
                      # Attach PDF to the email
                    # email3.attach('Visiting_Pass_Card.pdf', pdf_buffer.getvalue(), 'application/pdf')

                    email3.send()

                    # send_mail(
                    #             subject,
                    #             message,
                    #             from_email,
                    #             [to_email],
                    #             fail_silently=False,
                    #         )
                    # extendeduser.save()
                    message = 'You have successfully registered on CA portal'
                    return render(request, "main_website/confirmation_page.html",{'AZeo_ID':Azeo_no})




                    # redirect to home page:
                    #return redirect('registration_ca:index')

    # No post data availabe, let's just show the page.
        else:
            form = Azeo_idForm()

        return render(request, template, {'form': form})








