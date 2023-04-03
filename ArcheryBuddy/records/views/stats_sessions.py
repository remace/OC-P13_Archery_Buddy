"""stats sessions management related views"""
import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView

from equipment.models.arrows import Arrow
from records.models import StatsRecordSession, StatsRecord
from records.forms import StatsRecordSessionForm
from records.utils import calculate_barycentre, calculate_quiver

import pdb


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
        ctx = {}
        try:
            srs = StatsRecordSession.objects.create(
                user=request.user,
                conditions=request.POST.get("conditions"),
                distance=request.POST.get("distance"),
                comment=request.POST.get("comment"),
            )
            srs.save()

            available_arrow_indexes = request.POST.getlist("available_arrows")
            arrows = [
                Arrow.objects.filter(pk=int(index), user=request.user).first()
                for index in available_arrow_indexes
            ]

            srs.available_arrows.set(arrows)
            srs.save()

        except:
            raise

        return redirect("stats_session_list")


class DetailStatsSession(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        """get the stats session summary

        Args:
            pk (int): Stats Record Session identifyer
        """
        # TODO find a way do display available arrows checked
        user = request.user

        srs = get_object_or_404(StatsRecordSession, user=user, pk=pk)
        srs_dict = srs.__dict__

        head_form = StatsRecordSessionForm(srs_dict, user=user)

        records = StatsRecord.objects.filter(stats_session=srs) or None
        available_arrows = srs.available_arrows.all()

        ctx = {
            "srs": srs,
            "form": head_form,
            "records": records,
            "available_arrows": available_arrows,
        }
        return render(request, "records/detail_stats_session.html", context=ctx)

    @method_decorator(login_required)
    def post(self, request, pk):
        """update arrow stats

        Args:
            pk (int): Stats Record Session identifyer
        """

        user = request.user
        # réécrire les champs de la session de statistiques
        srs = StatsRecordSession.objects.get(user=user, pk=pk)
        srs.conditions = request.POST.get("conditions")
        srs.distance = request.POST.get("distance")
        srs.comment = request.POST.get("comment")
        available_arrow_ids = [int(a) for a in request.POST.getlist("available_arrows")]

        srs.available_arrows.clear()

        print(f"{available_arrow_ids}")

        for id in available_arrow_ids:
            srs.available_arrows.add(id)
        srs.save()
        print(srs.available_arrows.all())
        return redirect("stats_session_detail", srs.pk)


class DeleteStatsSession(DeleteView):
    model = StatsRecordSession

    def get_success_url(self):
        return reverse("stats_session_list")


class CreateStatsRecord(View):
    @method_decorator(login_required)
    def post(self, request):
        ctx = {}

        body = request.POST
        try:
            srs_id = body.get("srs_id")
            arrow_id = body.get("arrow_id")
            pos_x = body.get("pos_x")
            pos_y = body.get("pos_y")

            arrow = get_object_or_404(Arrow, pk=arrow_id)
            srs = get_object_or_404(StatsRecordSession, pk=srs_id)
            stats_record = StatsRecord.objects.create(
                arrow=arrow, stats_session=srs, pos_x=pos_x, pos_y=pos_y
            )
            stats_record.save()

        except Exception as e:
            raise e

        return JsonResponse(
            json.dumps(
                {
                    "record": {
                        "arrow": arrow.pk,
                        "stats_session": srs.pk,
                        "pos_x": pos_x,
                        "pos_y": pos_y,
                        "id": stats_record.pk,
                    },
                    "status_code": 200,
                }
            ),
            safe=False,
        )


class DeleteStatsRecord(View):
    @method_decorator(login_required)
    def get(self, request, stats_session_pk, stat_pk):
        stats_record = get_object_or_404(StatsRecord, pk=stat_pk)
        stats_record.delete()
        stats_dict = {
            "id": stats_record.id,
            "session_id": stats_record.stats_session.id,
            "arrow_id": stats_record.arrow_id,
            "pos_x": stats_record.pos_x,
            "pos_y": stats_record.pos_y,
        }

        return JsonResponse({"data": stats_dict, "status_code": 200})


class StatsRecordResults(View):
    @method_decorator(login_required)
    def get(self, request, stats_session_pk):

        from pprint import pprint

        shots = StatsRecord.objects.filter(stats_session=stats_session_pk)

        pk_list = [id.get("arrow_id") for id in shots.values("arrow_id").distinct()]

        records = {}
        for id in pk_list:
            records[id] = [rec for rec in shots.filter(arrow_id=id)]

        barycentres = []
        for record in records.values():
            barycentre_coords = calculate_barycentre(record)
            barycentre = {
                "arrow_id": record[0].arrow_id,
                "pos_x": barycentre_coords[0],
                "pos_y": barycentre_coords[1],
            }

            barycentres.append(barycentre)

        quiver = calculate_quiver(barycentres)
        for arrow in quiver:
            continue
        ctx = {"stats_session_id": stats_session_pk, "arrows": quiver}
        return render(request, "records/stats_session_result.html", context=ctx)
