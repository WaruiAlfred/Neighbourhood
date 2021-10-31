from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver): 
  #Creating message subject and sender
  subject = 'Welcome to My Neighbourhood'
  sender = 'alfred.kahenya@student.moringaschool.com'
  
  #passing in the context variables
  text_content = render_to_string('email/hoodmail.txt',{"name":name})
  html_content = render_to_string('email/hoodmail.html',{"name":name})
  
  message = EmailMultiAlternatives(subject,text_content,sender,[receiver])
  message.attach_alternative(html_content,'text/html')
  message.send()