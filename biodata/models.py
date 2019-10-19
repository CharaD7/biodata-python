from django.db import models



# Create your models here.

class Biodata(models.Model):
    """
        This Employee class is our table and the variables below are the columns
    """
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female', 'Female')
    )
    # Creating our database table's columns
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length = 20, choices = GENDER_CHOICES)
    address = models.CharField(max_length = 200)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length = 200)


    def __str__(self):
        # Making a prefered formating of items to be displayed
        return '{0} {1} '.format(
            self.firstname,
            self.lastname,
        )
