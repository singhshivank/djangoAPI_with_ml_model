from django.db import models

class User(models.Model):
    
    userName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact = models.IntegerField()
    exp = models.IntegerField(default=5)
    salary = models.IntegerField(default=76349)


    def __str__(self):
        return "{} - {}".format(self.userName, self.email)
