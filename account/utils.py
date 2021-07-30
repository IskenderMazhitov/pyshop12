from django.core.mail import send_mail


def send_welcome_email(email):
    url = 'http://localhost:8000/'
    message = f'<h1> Our whole team is giving a huge appreciating to you for sign in PyShop12: </h1> {url}'
    send_mail(
        'Welcome to PyShop12',
        message,
        'azazaza@gmail.com',
        [email,],
        fail_silently=False
    )
