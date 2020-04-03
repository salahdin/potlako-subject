from django.db import models
from django.utils import timezone

from edc_base.model_validators import date_not_future, date_is_future
from edc_protocol.validators import date_not_before_study_start

from .model_mixins import CrfModelMixin


class MissedCall(CrfModelMixin):

    entry_date = models.DateField(
        verbose_name='Date of entry',
        default=timezone.now,
        validators=[date_not_before_study_start, date_not_future, ],)

    notes = models.TextField(
        max_length=150,)

    repeat_call = models.DateField(
        verbose_name='Scheduled date for repeat call',
        validators=[date_is_future, ],)

    class Meta(CrfModelMixin.Meta):
        app_label = 'potlako_subject'
        verbose_name = 'Missed Call'
