from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from datetime import date



class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


# Create your models here.
class Biodata(models.Model):
    firstname = models.CharField('Firstname', max_length = 100)
    lastname = models.CharField('Lastname', max_length = 100)
    age = models.IntegerField('Age')
    date_of_birth = models.DateField('Date of Birth')
    date_of_employment = models.DateField('Date of Employment')
    position = models.CharField('Position', max_length=100)
    department = models.CharField('Department', max_length = 100)
    salary = models.IntegerField('Salary')
    supervisors = models.ManyToManyRel(settings.AUTH_USER_MODEL, 'Supervisors')


    def __str__(self):
        return '{0} {1} '.format(
            self.firstname,
            self.lastname,
        )

    def calculate_age(self):
        today = date.today()
        return today.year - self.year - ((today.month, today.day) < (self.month, self.day))

