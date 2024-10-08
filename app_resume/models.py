from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Resume(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)

    job_title = models.CharField(max_length=70,null=True)
    about = models.TextField(null=True)
    field_type  = models.CharField(max_length=70,null=True)

    def __str__(self):
        return self.user.username
        #return f'{self.job_title} of {self.user}' 


class WorkExprience(models.Model):

    resume = models.ForeignKey(Resume,on_delete= models.CASCADE,null=True)

    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True)
    title = models.CharField(max_length=70,null=True)
    company_name = models.CharField(max_length=70,null=True)
    job_type = models.CharField(max_length=70,null=True)


    def __str__(self):
        return self.title




