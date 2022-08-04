from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import FormView

from records.models import PracticeRecordSession
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
        return render(request, "records/detail_practice_session.html", context=ctx)

    @method_decorator(login_required)
    def post(self, request):
        ctx = {}
        form = PracticeRecordSessionForm(request.POST)
        return render(request, "records/detail_practice_session.html", context=ctx)


@login_required(login_url="/user/login/")
def delete_practice_record_session(request, prs_id):
    prs = PracticeRecordSession.objects.get(id=prs_id)
    prs.delete()
    return redirect("practice_list")


# about stats sessions
