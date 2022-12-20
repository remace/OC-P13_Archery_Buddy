"""stats sessions management related views"""
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import FormView

from equipment.models.arrows import Arrow
from records.models import StatsRecordSession, StatsRecord
from records.forms import StatsRecordSessionForm


class ListStatsSessions(View):
    @method_decorator(login_required)
    def get(self, request):
        pass


class CreateStatsSession(FormView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pass

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        pass


class DetailStatsSession(View):
    @method_decorator(login_required)
    def get(self, request, prs_id):
        pass

    @method_decorator(login_required)
    def post(self, request, prs_id):
        pass


@login_required(login_url="/user/login/")
def delete_stats_record_session(request, prs_id):
    pass
