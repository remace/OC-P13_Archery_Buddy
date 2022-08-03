from django.urls import path

from equipment.views import arrows

urlpatterns = [
    path("list/", arrows.arrows_list, name="arrows_list"),
    path("create/", arrows.create, name="arrows_create"),
    path("detail/<int:arrow_id>/", arrows.detail, name="arrows_detail"),
    path("update/<int:arrow_id>/", arrows.update, name="arrows_update"),
    path("delete/<int:arrow_id>/", arrows.delete, name="arrows_delete"),
]
