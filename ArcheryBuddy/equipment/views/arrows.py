from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from equipment.forms.arrow import ArrowForm
from equipment.models.arrows import Arrow, Nock, Feathering, Tip, Tube


@login_required(login_url="/user/login/")
def arrows_list(request):
    ctx = {}
    user = request.user
    arrows = Arrow.objects.filter(user=user)
    ctx["arrows"] = arrows
    return render(request, "equipment/list_arrows.html", context=ctx)


@login_required(login_url="/user/login/")
def create(request):
    ctx = {}
    if request.method == "GET":
        form = ArrowForm()
        ctx["form"] = form
        return render(request, "equipment/create_arrows.html", context=ctx)

    if request.method == "POST":
        form = ArrowForm(request.POST)
        if not form.is_valid():
            return render(
                request, "equipment/create_arrows.html", context={"form": form}
            )

        user = request.user
        nock, _ = Nock.objects.get_or_create(
            user=user,
            brand=form.cleaned_data.get("nock_brand"),
            color=form.cleaned_data.get("nock_color"),
            size=form.cleaned_data.get("nock_size"),
            uses_nock_pin=form.cleaned_data.get("uses_nock_pin"),
        )

        feathering, _ = Feathering.objects.get_or_create(
            user=user,
            laterality=form.cleaned_data.get("feathering_laterality"),
            feathering_type=form.cleaned_data.get("feathering_type"),
            brand=form.cleaned_data.get("feathering_brand"),
            color=form.cleaned_data.get("feathering_color"),
            cock_color=form.cleaned_data.get("feathering_cock_color"),
            size=form.cleaned_data.get("feathering_size"),
            angle=form.cleaned_data.get("feathering_angle"),
            nock_distance=form.cleaned_data.get("feathering_to_nock_distance"),
        )

        tip, _ = Tip.objects.get_or_create(
            user=user,
            brand=form.cleaned_data.get("tip_brand"),
            profile=form.cleaned_data.get("tip_profile"),
            weight=form.cleaned_data.get("tip_weight"),
        )

        tube, _ = Tube.objects.get_or_create(
            user=user,
            brand=form.cleaned_data.get("tube_brand"),
            material=form.cleaned_data.get("tube_material"),
            tube_length=form.cleaned_data.get("tube_length"),
            spine=form.cleaned_data.get("tube_spine"),
            tube_diameter=form.cleaned_data.get("tube_diameter"),
        )

        for _ in range(1, form.cleaned_data.get("number_of_arrows") + 1):
            Arrow.objects.create(
                user=user,
                nock=nock,
                feathering=feathering,
                tip=tip,
                tube=tube,
                not_broken=form.cleaned_data.get("not_broken"),
            )

        return redirect(arrows_list)


@login_required(login_url="/user/login/")
def detail(request, arrow_id):
    arrow = Arrow.objects.get(id=arrow_id)
    ctx = {}
    ctx["arrow"] = arrow
    return render(request, "equipment/detail_arrow.html", context=ctx)


@login_required(login_url="/user/login/")
def update(request, arrow_id):
    arrow = Arrow.objects.get(id=arrow_id)
    arrow.not_broken = False if arrow.not_broken else True
    arrow.save()
    return redirect("arrows_detail", arrow_id=arrow_id)


@login_required(login_url="/user/login/")
def delete(request, arrow_id):
    arrow = Arrow.objects.get(id=arrow_id)
    arrow.delete()
    return redirect(arrows_list)
