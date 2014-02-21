from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

def send_ack_email(data):
    subject = "Thank you for subscribing to Gallery Maskara"
    send_email("email/ack_email.txt", data, subject, [data['email']])
    return

def send_admin_email(data):
    subject = "New sign-up on Gallery Maskara website"
    send_email("email/admin_email.txt", data, subject, ['info@gallerymaskara.com', 'sanjaybhangar@gmail.com'])
    return

def send_email(template_path, data, subject, to_emails):
    template = get_template(template_path)
    c = Context(data)
    email_text = template.render(c)
    #print email_text
    #send_mail(subject, email_text, "info@gallerymaskara.com", to_emails)
    return
