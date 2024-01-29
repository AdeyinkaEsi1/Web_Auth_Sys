from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pword = models.CharField(max_length=50, unique=True)
    # id = models.UUIDField(primary_key=True, default=id.uuid4, editable=False)


    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email
