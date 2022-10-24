from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect

from equipment.models.bows import *


@login_required()
def bows_list(request):
    user = request.user
    olympics = OlympicBow.objects.filter(user=user).all()
    barebows = Barebow.objects.filter(user=user).all()
    compounds = CompoundBow.objects.filter(user=user).all()

    bb_ids = [ob.barebow_id for ob in olympics]
    for identifier in bb_ids:
        barebows = barebows.exclude(id=identifier)
    print(
        f"barebows: {barebows}\nOlympic bows: {olympics}\ncompound bows: {compounds}\n"
    )

    ctx = {
        "olympics": olympics,
        "barebows": barebows,
        "compounds": compounds,
    }
    return render(request, template_name="equipment/list_bows.html", context=ctx)


@login_required()
def create(request):

    if request.method == "GET":
        return render(request, template_name="equipment/create_bows.html")

    elif request.method == "POST":
        if request.POST.get("fail"):
            messages.error(request, message="saisie incorrecte")
            ctx = {"forms": request.POST}
            return render(
                request, template_name="equipment/create_bows.html", context=ctx
            )
        else:
            bow_type = request.POST.get("bow_type")
            match bow_type:
                case "Barebow":
                    error = False
                    # general
                    bow_power = request.POST.get("power")
                    laterality = request.POST.get("laterality")

                    # riser
                    riser_brand = request.POST.get("riser_brand")
                    riser_size = request.POST.get("riser_size")
                    riser_color = request.POST.get("riser_color")
                    riser_grip = request.POST.get("riser_grip")

                    try:
                        riser = Riser(
                            user=request.user,
                            brand=riser_brand,
                            size=riser_size,
                            color=riser_color,
                            grip=riser_grip,
                        )
                        riser.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Poignée: {integrity}")
                        error = True

                    # limbs
                    limbs_brand = request.POST.get("limbs_brand")
                    limbs_power = request.POST.get("limbs_power")
                    limbs_size = request.POST.get("limbs_size")

                    try:
                        limbs = Limbs(
                            user=request.user,
                            brand=limbs_brand,
                            power=limbs_power,
                            size=limbs_size,
                        )
                        limbs.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Branches: {integrity}")
                        error = True
                    # String
                    string_brand = request.POST.get("string_brand")
                    material = request.POST.get("material")
                    strands = request.POST.get("strands")

                    try:
                        bow_string = EquipmentString(
                            user=request.user,
                            brand=string_brand,
                            material=material,
                            number_of_strands=strands,
                        )
                        bow_string.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Corde: {integrity}")
                        error = True

                    # Arrow Rest
                    rest_type = request.POST.get("rest_type")
                    rest_brand = request.POST.get("rest_brand")

                    try:
                        rest = ArrowRest(
                            user=request.user, brand=rest_brand, rest_type=rest_type
                        )
                        rest.save()
                    except IntegrityError as integrity:
                        messages.error(request, f"Repose_flèche: {integrity}")
                        error = True

                    # Berger
                    berger_brand = request.POST.get("berger_brand")
                    berger_color = request.POST.get("berger_color")
                    spring = request.POST.get("berger_spring")

                    try:
                        berger = BergerButton(
                            user=request.user,
                            brand=berger_brand,
                            color=berger_color,
                            spring=spring,
                        )
                        berger.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Berger: {integrity}")
                        error = True

                    string_turns = request.POST.get("string_turns")
                    nockset_offset = request.POST.get("nockset_offset")
                    band = request.POST.get("band")
                    high_tiller = request.POST.get("high_tiller")
                    low_tiller = request.POST.get("low_tiller")

                    try:
                        bow = Barebow(
                            user=request.user,
                            power=bow_power,
                            laterality=laterality,
                            riser=riser,
                            limbs=limbs,
                            string=bow_string,
                            arrow_rest=rest,
                            berger_button=berger,
                            band=band,
                            number_of_turns=string_turns,
                            nockset_offset=nockset_offset,
                            high_tiller=high_tiller,
                            low_tiller=low_tiller,
                        )
                        bow.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"barebow: {integrity}")
                        riser.delete()
                        limbs.delete()
                        bow_string.delete()
                        rest.delete()
                        berger.delete()

                case "Olympic":
                    error = False
                    # general
                    bow_power = request.POST.get("power")
                    laterality = request.POST.get("laterality")

                    # riser
                    riser_brand = request.POST.get("riser_brand")
                    riser_size = request.POST.get("riser_size")
                    riser_color = request.POST.get("riser_color")
                    riser_grip = request.POST.get("riser_grip")

                    try:
                        riser = Riser(
                            user=request.user,
                            brand=riser_brand,
                            size=riser_size,
                            color=riser_color,
                            grip=riser_grip,
                        )
                        riser.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Poignée: {integrity}")
                        error = True

                    # limbs
                    limbs_brand = request.POST.get("limbs_brand")
                    limbs_power = request.POST.get("limbs_power")
                    limbs_size = request.POST.get("limbs_size")

                    try:
                        limbs = Limbs(
                            user=request.user,
                            brand=limbs_brand,
                            power=limbs_power,
                            size=limbs_size,
                        )
                        limbs.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Branches: {integrity}")
                        error = True
                    # String
                    string_brand = request.POST.get("string_brand")
                    material = request.POST.get("material")
                    strands = request.POST.get("strands")

                    try:
                        bow_string = EquipmentString(
                            user=request.user,
                            brand=string_brand,
                            material=material,
                            number_of_strands=strands,
                        )
                        bow_string.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Corde: {integrity}")
                        error = True

                    # Arrow Rest
                    rest_type = request.POST.get("rest_type")
                    rest_brand = request.POST.get("rest_brand")

                    try:
                        rest = ArrowRest(
                            user=request.user, brand=rest_brand, rest_type=rest_type
                        )
                        rest.save()
                    except IntegrityError as integrity:
                        messages.error(request, f"Repose_flèche: {integrity}")
                        error = True

                    # Berger
                    berger_brand = request.POST.get("berger_brand")
                    berger_color = request.POST.get("berger_color")
                    spring = request.POST.get("berger_spring")

                    try:
                        berger = BergerButton(
                            user=request.user,
                            brand=berger_brand,
                            color=berger_color,
                            spring=spring,
                        )
                        berger.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Berger: {integrity}")
                        error = True

                    # scope
                    scope_brand = request.POST.get("scope_brand")

                    try:
                        scope = Scope(user=request.user, brand=scope_brand)
                        scope.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Scope: {integrity}")
                        error = True

                    # clicker
                    clicker_brand = request.POST.get("clicker_brand")

                    try:
                        clicker = Clicker(user=request.user, brand=clicker_brand)
                        clicker.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"Clicker: {integrity}")
                        error = True

                    # stabilisation
                    stab_brand = request.POST.get("stab_brand")

                    try:
                        stab = Stabilisation(user=request.user, brand=stab_brand)
                        stab.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"stabilisation: {integrity}")
                        error = True

                    # dampeners
                    front_brand = request.POST.get("front_brand")
                    rears_brand = request.POST.get("rears_brand")

                    try:
                        dampeners = Dampeners(
                            user=request.user,
                            front_brand=front_brand,
                            rears_brand=rears_brand,
                        )
                        dampeners.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"dampeners: {integrity}")
                        error = True

                    string_turns = request.POST.get("string_turns")
                    nockset_offset = request.POST.get("nockset_offset")
                    band = request.POST.get("band")
                    high_tiller = request.POST.get("high_tiller")
                    low_tiller = request.POST.get("low_tiller")

                    try:
                        barebow = Barebow(
                            user=request.user,
                            power=bow_power,
                            laterality=laterality,
                            riser=riser,
                            limbs=limbs,
                            string=bow_string,
                            arrow_rest=rest,
                            berger_button=berger,
                            band=band,
                            number_of_turns=string_turns,
                            nockset_offset=nockset_offset,
                            high_tiller=high_tiller,
                            low_tiller=low_tiller,
                        )
                        barebow.save()

                        bow = OlympicBow(
                            user=request.user,
                            barebow=barebow,
                            power=bow_power,
                            laterality=laterality,
                            scope=scope,
                            clicker=clicker,
                            stabilisation=stab,
                            dampeners=dampeners,
                        )
                        bow.save()

                    except IntegrityError as integrity:
                        messages.error(request, f"barebow: {integrity}")
                        riser.delete()
                        limbs.delete()
                        bow_string.delete()
                        rest.delete()
                        berger.delete()
                        scope.delete()
                        clicker.delete()
                        stab.delete()
                        dampeners.delete()
                        barebow.delete()
                        bow.delete()

                case "Compound":

                    print("création compound")

                    user = request.user
                    laterality = request.POST.get("laterality")
                    power = request.POST.get("power")

                    bow_brand = request.POST.get("bow_brand")
                    entraxe = request.POST.get("entraxe")
                    draw_weight = request.POST.get("compound_power")
                    draw_weight_dropped = request.POST.get("reduced_power")
                    brace_height = request.POST.get("compoundBand")
                    draw_length = request.POST.get("drawLength")

                    # scope
                    scope_brand = request.POST.get("CompoundScopeBrand")
                    magnitude = request.POST.get("ScopeMagnitude")

                    try:
                        compound_scope = CompoundScope(
                            magnitude=magnitude, user=user, brand=scope_brand
                        )
                        compound_scope.save()

                    except IntegrityError as integrity:
                        print(integrity)
                        messages.error(request, f"compound scope: {integrity}")

                    # arrow rest
                    arrow_rest_brand = request.POST.get("CompoundRestBrand")
                    arrow_rest_type = request.POST.get("CompoundRestType")
                    try:
                        arrow_rest = CompoundArrowRest(
                            brand=arrow_rest_brand, rest_type=arrow_rest_type, user=user
                        )
                        arrow_rest.save()
                    except IntegrityError as integrity:
                        print(integrity)
                        messages.error(request, f"compound arrow rest: {integrity}")

                    # stabilisation
                    stabilisation_brand = request.POST.get("stab_brand")
                    try:
                        stabilisation = Stabilisation(
                            user=user, brand=stabilisation_brand
                        )
                        stabilisation.save()
                    except IntegrityError as integrity:
                        print(integrity)
                        messages.error(request, f"compound stabilisation: {integrity}")

                    # dampeners
                    dampeners_front = request.POST.get("front_brand")
                    dampeners_rears = request.POST.get("rears_brand")
                    try:
                        dampeners = Dampeners(
                            user=user,
                            front_brand=dampeners_front,
                            rears_brand=dampeners_rears,
                        )
                        dampeners.save()
                    except IntegrityError as integrity:
                        print(integrity)
                        messages.error(request, f"compound dampeners: {integrity}")

                    try:
                        bow = CompoundBow(
                            user=user,
                            power=power,
                            laterality=laterality,
                            bow_brand=bow_brand,
                            bow_axle_to_axle=entraxe,
                            draw_weight=draw_weight,
                            draw_weight_dropped=draw_weight_dropped,
                            brace_height=brace_height,
                            draw_length=draw_length,
                            scope=compound_scope,
                            arrow_rest=arrow_rest,
                            stabilisation=stabilisation,
                            dampeners=dampeners,
                        )
                        bow.save()

                    except IntegrityError as integrity:
                        print(integrity)
                        messages.error(request, f"Compound: {integrity}")
                        arrow_rest.delete()
                        compound_scope.delete()
                        stabilisation.delete()
                        dampeners.delete()
                        bow.delete()

            return redirect("bows_list")


@login_required()
def detail(request, bow_type, bow_id):

    match bow_type:
        case "olympic":
            bow = OlympicBow.objects.get(id=bow_id)
        case "barebow":
            bow = Barebow.objects.get(id=bow_id)
        case "compound":
            bow = CompoundBow.objects.get(id=bow_id)
        case other:
            bow = None
            messages.error(request, message="type d'arc inexistant")
    ctx = {"bow": bow, "bow_type": bow_type}
    return render(request, template_name="equipment/detail_bow.html", context=ctx)


@login_required()
def update(request, bow_type, bow_id):
    if request.method == "GET":
        ctx = {"bow_type": bow_type}
        match bow_type:
            case "barebow":
                bow = Barebow.objects.get(id=bow_id)
            case "olympic":
                bow = OlympicBow.objects.get(id=bow_id)
                barebow = Barebow.objects.get(id=bow.barebow_id)
            case "compound":
                bow = CompoundBow.objects.get(id=bow_id)
            case other:
                messages.error(request, "type d'arc inexistant")
        ctx["bow"] = bow
        return render(request, "equipment/update_bow.html", context=ctx)

    else:
        match bow_type:
            case "barebow":
                bow = Barebow.objects.get(id=bow_id)
                error = False
                # general
                bow_power = request.POST.get("power")
                laterality = request.POST.get("laterality")

                # riser
                riser_brand = request.POST.get("riser_brand")
                riser_size = request.POST.get("riser_size")
                riser_color = request.POST.get("riser_color")
                riser_grip = request.POST.get("riser_grip")

                try:
                    riser = bow.riser
                    riser.brand = riser_brand
                    riser.size = riser_size
                    riser.color = riser_color
                    riser.grip = riser_grip
                    riser.save()

                except IntegrityError as integrity:
                    messages.error(request, f"Poignée: {integrity}")
                    error = True

                # limbs
                limbs_brand = request.POST.get("limbs_brand")
                limbs_power = request.POST.get("limbs_power")
                limbs_size = request.POST.get("limbs_size")

                try:
                    limbs = bow.limbs
                    limbs.brand = limbs_brand
                    limbs.power = limbs_power
                    limbs.size = limbs_size
                    limbs.save()

                except IntegrityError as integrity:
                    messages.error(request, f"Branches: {integrity}")
                    error = True

                # String
                string_brand = request.POST.get("string_brand")
                material = request.POST.get("material")
                strands = request.POST.get("strands")

                try:
                    bow_string = bow.string
                    bow_string.brand = string_brand
                    bow_string.material = material
                    bow_string.strands = strands
                    bow_string.save()

                except IntegrityError as integrity:
                    messages.error(request, f"Corde: {integrity}")
                    error = True

                # Arrow Rest
                rest_type = request.POST.get("rest_type")
                rest_brand = request.POST.get("rest_brand")

                try:
                    rest = bow.arrow_rest
                    rest.rest_type = rest_type
                    rest.brand = rest_brand
                    rest.save()
                except IntegrityError as integrity:
                    messages.error(request, f"Repose_flèche: {integrity}")
                    error = True

                # Berger
                berger_brand = request.POST.get("berger_brand")
                berger_color = request.POST.get("berger_color")
                spring = request.POST.get("berger_spring")

                try:

                    berger = bow.berger_button
                    berger.brand = berger_brand
                    berger.color = berger_color
                    berger.spring = spring

                    berger.save()

                except IntegrityError as integrity:
                    messages.error(request, f"Berger: {integrity}")
                    error = True

                string_turns = request.POST.get("string_turns")
                nockset_offset = request.POST.get("nockset_offset")
                band = request.POST.get("band")
                high_tiller = request.POST.get("high_tiller")
                low_tiller = request.POST.get("low_tiller")

                try:
                    bow.number_of_turns = string_turns
                    bow.nockset_offset = nockset_offset
                    bow.band = band
                    bow.high_tiller = high_tiller
                    bow.low_tiller = low_tiller
                    bow.save()

                except IntegrityError as integrity:
                    messages.error(
                        request, f"impossible de modifier cet arc: {integrity}"
                    )

                return redirect("bows_list")

            case "Olympic":
                pass

            case "Compound":
                pass


@login_required()
def delete(request, bow_type, bow_id):
    if request.method == "GET":
        match bow_type:
            case "barebow":
                bow = Barebow.objects.get(id=bow_id)
                bow.riser.delete()
                bow.limbs.delete()
                bow.arrow_rest.delete()
                bow.berger_button.delete()
                bow.string.delete()
            case "olympic":
                bow = OlympicBow.objects.get(id=bow_id)
                bow.barebow.riser.delete()
                bow.barebow.limbs.delete()
                bow.barebow.arrow_rest.delete()
                bow.barebow.berger_button.delete()
                bow.barebow.string.delete()
                bow.clicker.delete()
                bow.stabilisation.delete()
                bow.scope.delete()
                bow.dampeners.delete()
            case "compound":
                bow = CompoundBow.objects.get(id=bow_id)
                bow.scope.delete()
                bow.arrow_rest.delete()
                bow.stabilisation.delete()
                bow.dampeners.delete()
            case other:
                messages.error(request, "type d'arc inexistant")
        bow.delete()
        messages.success(request, "arc supprimé avec succès")
        return redirect("bows_list")
