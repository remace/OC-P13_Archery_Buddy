from django.urls import path

from equipment.views import bows

urlpatterns = [
    path("list/", bows.bows_list, name="bows_list"),
    path("create/", bows.create, name="bows_create"),
    path("detail/<str:bow_type>/<int:bow_id>/",
         bows.detail,
         name="bows_detail"),
    path("update/<str:bow_type>/<int:bow_id>/",
         bows.update,
         name="bows_update"),
    path("delete/<str:bow_type>/<int:bow_id>/",
         bows.delete,
         name="bows_delete"),
]
