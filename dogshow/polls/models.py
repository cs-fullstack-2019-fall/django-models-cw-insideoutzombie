from django.db import models

class DogData(models.Model):
    name = models.CharField(max_length = 100)
    breed = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)


#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)




# class BankEmployees(models.Model):
#     SSN = models.IntegerField()
#     name = models.CharField(max_length = 100)
#     salary = models.DecimalField(max_digits = 10, decimal_places = 3)
