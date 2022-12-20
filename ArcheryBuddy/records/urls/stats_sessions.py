from django.urls import path

from records.views import stats_sessions

urlpatterns = [
    path("list/", stats_sessions.ListStatsSessions.as_view(), name="stats_list"),
    path(
        "create/",
        stats_sessions.CreateStatsSession.as_view(),
        name="stats_create",
    ),
    path(
        "delete/<int:prs_id>",
        stats_sessions.delete_stats_record_session,
        name="stats_delete",
    ),
    path(
        "detail/<int:prs_id>",
        stats_sessions.DetailStatsSession.as_view(),
        name="stats_detail",
    ),
]
