"""stats sessions management related views"""
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import FormView, CreateView, BaseDeleteView

from equipment.models.arrows import Arrow
from records.models import StatsRecordSession, StatsRecord
from records.forms import StatsRecordSessionForm

from pprint import pprint


class ListStatsSessions(View):
    @method_decorator(login_required)
    def get(self, request):
        ctx = {}
        user = request.user
        stats_record_sessions = StatsRecordSession.objects.filter(user=user).all()
        ctx["stats_sessions"] = stats_record_sessions
        return render(request, "records/list_stats_sessions.html", context=ctx)


class CreateStatsSession(CreateView):
    def get_form_kwargs(self):
        kwargs = super(CreateStatsSession, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        form = StatsRecordSessionForm(user=user)
        ctx = {"form": form}
        return render(request, "records/create_stats_session.html", context=ctx)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        try:
            srs = StatsRecordSession.objects.create(
                user=request.user,
                conditions=request.POST.get("conditions"),
                distance=request.POST.get("distance"),
                comment=request.POST.get("comment"),
            )
            available_arrows = request.POST.getlist("available_arrows")
            srs.available_arrows.set(available_arrows)

        except:
            raise

        ctx = {}
        return redirect("stats_list")


class DetailStatsSession(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        """get the stats session summary

        Args:
            pk (int): Stats Record Session identifyer
        """
        # find a way do display available arrows checked
        user = request.user

        srs = StatsRecordSession.objects.get(user=user, pk=pk)

        srs_dict = srs.__dict__
        srs_dict["user"] = user

        head_form = StatsRecordSessionForm(srs_dict, user=user)

        records = StatsRecord.objects.filter(stats_session=srs) or None
        ctx = {"srs": srs, "form": head_form, "records": records}
        return render(request, "records/detail_stats_session.html", context=ctx)

    @method_decorator(login_required)
    def post(self, request, pk):
        """update arrow stats

        Args:
            pk (int): Stats Record Session identifyer
        """
        # TODO écrire les nouveaux champs de la session de statistiques

        # réécrire les champs de la session de statistiques
        srs = StatsRecordSession.objects.get(user=user, pk=pk)
        srs.conditions = request.POST.get("conditions")
        srs.distance = request.POST.get("distance")
        srs.comment = request.POST.get("comment")
        available_arrows = request.POST.getlist("available_arrows")
        srs.available_arrows.set(available_arrows)


class DeleteStatsSession(View):
    def get(self, request, pk):
        user = request.user
        srs = StatsRecordSession.objects.get(user=user, pk=pk)
        try:
            srs.delete()
        except:
            raise
        return redirect("stats_list")
