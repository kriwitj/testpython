from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()

class Items(models.Model):
    PositionID=models.ForeignKey('User_Manage',on_delete=models.CASCADE)
    Regist_datetime=models.DateTimeField()
    Number_item=models.TextField()
    Type=models.TextField()
    Type_details=models.TextField()
    OS=models.TextField()
    Software=models.CharField(max_length=100)
    Status=models.TextField()
    def __unicode__(self):
        return self.PositionID     

class Software_Regist(models.Model):
    Name=models.TextField()
    Details=models.TextField()
    License_Type=models.TextField()
    License_User=models.TextField()
    License_Number=models.TextField()
    First_use_datetime=models.DateTimeField()
    Start_use_datetime=models.DateTimeField()
    End_use_datetime=models.DateTimeField()

class User_Manage(models.Model):
    PositionID=models.IntegerField()
    Name=models.TextField()
    LastName=models.TextField()
    Department=models.TextField()
    def __unicode__(self):
        return self.PositionID
        
# class Acts(models.Model):
#     DateTime=models.DateTimeField()
#     Regist_Datetime=models.DateTimeField()
#     Name=models.TextField()
#     Type=models.TextField()
#     Department=models.TextField()

class UploadFileForm(models.Model):
    Date_Register = models.DateTimeField()
    Date_Act_Notice  = models.DateTimeField()
    Date_Act_Use  = models.DateTimeField()
    Act_Type = models.TextField()
    Act_Name_TH     = models.CharField("Enter Act Name", max_length = 100)
    Act_Name_ENG     = models.CharField("Enter Act Name", max_length = 100)
    Act_Year  = models.TextField()
    Act_Status = models.TextField()
    Act_Reason = models.TextField()
    Act_Description = models.TextField()
    Act_Freq_Repeat = models.IntegerField()
    Act_Response_Department = models.TextField()
    Act_Department_Effect = models.TextField()
    file      = models.FileField() # for creating file input  
   
    class Meta:  
        db_table = "act_pdf"

# models.py image https://www.geeksforgeeks.org/python-uploading-images-in-django/
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')

class Photo(models.Model):
    # By default null=False and blank=False 
    image = models.ImageField(upload_to="images/")
    # Others fields here