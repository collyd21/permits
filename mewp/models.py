from django.db import models
YES_NO_NA = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('na', 'NA'),
)


class Mewp(models.Model):
    make_model = models.CharField(max_length=120)
    sn_no = models.CharField(max_length=120)
    inspected_by = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    date = models.DateField()
    question_1 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_2 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_3 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_4 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_5 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_6 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_7 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_8 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_9 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_10 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_11 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_12 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_13 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_14 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_15 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_16 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_17 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_18 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_19 = models.CharField(max_length=3, choices=YES_NO_NA)
    question_20 = models.CharField(max_length=3, choices=YES_NO_NA)
    comments = models.CharField(max_length=300)

    class Meta:
        ordering = ['location']

    def __str__(self):
        return self.inspected_by