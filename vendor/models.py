from django.db import models

from accounts.models import User, UserProfile
from accounts.utils import send_notification


class Vendor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name='userprofile')
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.ImageField(upload_to='vendor/license')
    is_aproved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modifiet_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # update
            orig = Vendor.objects.get(pk=self.pk)
            if orig.is_aproved != self.is_aproved:

                mail_template = 'accounts/emails/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_aproved': self.is_aproved,
                }

                if self.is_aproved == True:
                    # send notification email
                    mail_subject = 'congratulations, your restaurante has been approved'
                    send_notification(mail_subject, mail_template, context)
                else:
                    # send notification email
                    mail_subject = 'we are not eligible for publish in marketplace'
                    send_notification(mail_subject, mail_template, context)
        return super(Vendor, self).save(*args, **kwargs)
