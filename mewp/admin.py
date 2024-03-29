from django.contrib import admin
from .models import Mewp

class MewpAdmin(admin.ModelAdmin):
    list_display = ('make_model', 'sn_no', 'inspected_by', 'location', 'date', 'question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9', 'question_10', 'question_11', 'question_12', 'question_13', 'question_14', 'question_15', 'question_16', 'question_17', 'question_18', 'question_19', 'question_20','comments',)
    search_fields = ('make_model', 'sn_no', 'inspected_by', 'location', 'date')

admin.site.register(Mewp, MewpAdmin)

