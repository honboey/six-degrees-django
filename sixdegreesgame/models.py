from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=200)
    artists = ...
    number = ...

    def is_a_valid_answer(self):
        ...

    def is_final_answer(self):
        ...

    def matches_final_artist(self):
        ...

    def __str__(self):
        return f"{self.name}"
