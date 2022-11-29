import re

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import FormView

from equipment.models.arrows import Arrow
from records.models import PracticeRecordSession, PracticeRecord
from records.forms import PracticeRecordSessionForm


# about practice sessions
class ListPracticeSessions(View):
    @method_decorator(login_required)
    def get(self, request):
        ctx = {}
        user = request.user
        practice_record_sessions = PracticeRecordSession.objects.filter(user=user).all()
        ctx["practice_sessions"] = practice_record_sessions
        return render(request, "records/list_practice_sessions.html", context=ctx)


class CreatePracticeSession(FormView):
    @method_decorator(login_required)
    def get(self, request):
        form = PracticeRecordSessionForm()
        ctx = {}
        ctx["form"] = form
        return render(request, "records/create_practice_session.html", context=ctx)

    @method_decorator(login_required)
    def post(self, request):
        ctx = {}
        form = PracticeRecordSessionForm(request.POST)
        if form.is_valid():
            ctx["form"] = form.cleaned_data
            user = request.user
            PracticeRecordSession.objects.create(
                user=user,
                conditions=ctx["form"].get("conditions"),
                distance=ctx["form"].get("distance"),
                comment=ctx["form"].get("comment"),
                max_arrows_in_volley=ctx["form"].get("max_arrows_in_volley"),
                number_of_volleys=ctx["form"].get("number_of_volleys"),
            )
        return redirect("practice_list")


class DetailPracticeSession(View):
    @method_decorator(login_required)
    def get(self, request, prs_id):
        ctx = {}
        prs = PracticeRecordSession.objects.get(id=prs_id)
        ctx["prs"] = prs
        ctx["volley_range"] = range(1, prs.number_of_volleys + 1)
        ctx["arrow_range"] = range(1, prs.max_arrows_in_volley + 1)
        practice_records = PracticeRecord.objects.filter(practice_session=prs).all()
        shots = {}
        for practice_record in practice_records:
            shot = {}
            shot["arrow_id"] = practice_record.arrow.id
            shot["score"] = practice_record.score
            try:
                temp = shots[practice_record.volley]
            except KeyError as key_error:
                shots[practice_record.volley] = []
            finally:
                shots[practice_record.volley].append(shot)

        ctx["practice_records"] = shots
        return render(request, "records/detail_practice_session.html", context=ctx)

    @method_decorator(login_required)
    def post(self, request, prs_id):

        score_pattern = re.compile(r"input-score-[0-9]+-[0-9]+")
        prs = PracticeRecordSession.objects.get(id=prs_id)
        post = request.POST
        for key, value in post.items():
            if re.fullmatch(score_pattern, key):
                if value != "":
                    key_splitted = key.split("-")
                    volley = int(key_splitted[2])
                    shot = int(key_splitted[3])
                    score = int(value)

                    arrow_id = int(post.get(f"input-arrow-{volley}-{shot}"))

                    try:
                        arrow = Arrow.objects.get(id=arrow_id)
                        try:
                            PracticeRecord.objects.create(
                                arrow=arrow,
                                practice_session=prs,
                                volley=volley,
                                score=score,
                            )

                        except ValidationError as exception:
                            practice_record = PracticeRecord.objects.get(
                                arrow=arrow,
                                practice_session=prs,
                                volley=volley,
                            )
                            practice_record.score = score
                            practice_record.save()

                    except Arrow.DoesNotExist as exception:
                        print(exception)
        return redirect("practice_detail", prs_id=prs.id)


@login_required(login_url="/user/login/")
def delete_practice_record_session(request, prs_id):
    prs = PracticeRecordSession.objects.get(id=prs_id)
    prs.delete()
    return redirect("practice_list")


# about stats sessions
