from django.urls import path

from records import views

urlpatterns = [
    path("list/", views.ListPracticeSessions.as_view(), name="practice_list"),
    path("create/", views.CreatePracticeSession.as_view(), name="practice_create"),
    path(
        "delete/<int:prs_id>",
        views.delete_practice_record_session,
        name="practice_delete",
    ),
    path(
        "detail/<int:prs_id>",
        views.DetailPracticeSession.as_view(),
        name="practice_detail",
    ),
]
