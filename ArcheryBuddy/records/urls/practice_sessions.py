from django.urls import path

from records.views import practice_sessions

urlpatterns = [
    path(
        "list/", practice_sessions.ListPracticeSessions.as_view(), name="practice_list"
    ),
    path(
        "create/",
        practice_sessions.CreatePracticeSession.as_view(),
        name="practice_create",
    ),
    path(
        "delete/<int:prs_id>",
        practice_sessions.delete_practice_record_session,
        name="practice_delete",
    ),
    path(
        "detail/<int:prs_id>",
        practice_sessions.DetailPracticeSession.as_view(),
        name="practice_detail",
    ),
]
