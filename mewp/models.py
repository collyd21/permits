from django.db import models
QUESTION_MEWP = (
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
    question_1 = models.CharField(max_length=3, null=True, default=None, choices=QUESTION_MEWP)
    question_2 = models.CharField(max_length=3, null=True, default=None, choices=QUESTION_MEWP)
    question_3 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_4 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_5 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_6 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_7 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_8 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_9 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_10 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_11 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_12 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_13 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_14 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_15 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_16 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_17 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_18 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_19 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    question_20 = models.CharField(max_length=3, null=True, default=None,  choices=QUESTION_MEWP)
    comments = models.CharField(max_length=300)

    class Meta:
        ordering = ['location']

    def __str__(self):
        return self.inspected_by