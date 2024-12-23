from django.db import models


# Create your models here.

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='portfolio')
    SKILL_CHOICES = (
        ('1', 'Python'),
        ('2', 'HTML'),
        ('3', 'CSS'),
        ('4', 'Django'),
        ('5', 'Tailwind'),
        ('6', 'WordPress'),
    )
    skill_id = models.CharField(max_length=1, primary_key=True, choices=SKILL_CHOICES)

    def __str__(self):
        return self.name




