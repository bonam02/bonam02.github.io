from django.db import models

class Student(models.Model):
    name = models.CharField("Name", max_length=240).primary_key
    email = models.EmailField()
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name

class Table1(models.Model):
    name = models.CharField("Name", max_length=240)
    id = models.IntegerField
    salary = models.IntegerField

class user_details(models.Model):
    id = models.IntegerField
    user_id = models.IntegerField(default=None)
    title = models.CharField("Name", max_length=240)
    body = models.CharField("body",max_length=500)

