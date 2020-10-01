from django.db import models


class user_login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class user(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='user/profile_img/')
    mobile = models.IntegerField(max_length=12)
    emailid = models.ForeignKey(user_login, on_delete=models.CASCADE)
    def __str__(self):
        return self.Firstname+self.Lastname

class education_detail(models.Model):
    emailid = models.ForeignKey(user, on_delete=models.CASCADE)
    sec_school = models.CharField(max_length=50)
    sec_board = models.CharField(max_length=10)
    sec_percent = models.IntegerField(max_length=10)
    Int_school = models.CharField(max_length=50)
    Int_board = models.CharField(max_length=10)
    Int_percent = models.IntegerField(max_length=10)
    def __str__(self):
        return self.emailid


class graduation(models.Model):
    emailid = models.ForeignKey(education_detail, on_delete=models.CASCADE)
    sem1 = models.IntegerField(max_length=10, default=0)
    sem2 = models.IntegerField(max_length=10, default=0)
    sem3 = models.IntegerField(max_length=10, default=0)
    sem4 = models.IntegerField(max_length=10, default=0)
    sem5 = models.IntegerField(max_length=10, default=0)
    sem6 = models.IntegerField(max_length=10, default=0)
    sem7 = models.IntegerField(max_length=10, default=0)
    sem8 = models.IntegerField(max_length=10, default=0)
    def __str__(self):
        return self.emailid
