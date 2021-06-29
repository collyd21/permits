from django.db import models


class Mewp(models.Model):
    make_model = models.CharField(max_length=120)
    sn_no = models.CharField(max_length=120)
    inspected_by = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    date = models.DateField()
    question_1 = models.BooleanField()
    question_2 = models.BooleanField()
    question_3 = models.BooleanField()
    question_4 = models.BooleanField()
    question_5 = models.BooleanField()
    question_6 = models.BooleanField()
    question_7 = models.BooleanField()
    question_8 = models.BooleanField()
    question_9 = models.BooleanField()
    question_10 = models.BooleanField()
    question_11 = models.BooleanField()
    question_12 = models.BooleanField()
    question_13 = models.BooleanField()
    question_14 = models.BooleanField()
    question_15 = models.BooleanField()
    question_16 = models.BooleanField()
    question_17 = models.BooleanField()
    question_18 = models.BooleanField()
    question_19 = models.BooleanField()
    question_20 = models.BooleanField()
    comments = models.CharField(max_length=300)

    class Meta:
        ordering = ['location']

    def __str__(self):
        return self.inspected_by