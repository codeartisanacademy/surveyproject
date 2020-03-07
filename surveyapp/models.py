from django.db import models

# Create your models here.
class Participant(models.Model):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    # first name, last name, phone, gender, email
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDERS)


class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question
    


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='answers')
    answered_date = models.DateTimeField(auto_now_add=True)
