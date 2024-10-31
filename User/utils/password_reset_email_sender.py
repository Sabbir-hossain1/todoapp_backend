from User.models import PasswordResetCode
from django.utils.timezone import now, timedelta
from django.core.mail import send_mail
from django.conf import settings


def send_password_reset_email(user):
    reset_code = PasswordResetCode.objects.create(
        user=user, expires_at=now() + timedelta(hours=1)
    )
    subject = "Password Reset Request"
    message = f"Your Password Reset Code is : {reset_code}.It will be expire in 1 hour."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
