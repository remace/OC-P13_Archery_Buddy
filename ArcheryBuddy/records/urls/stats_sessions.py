from django.urls import path

from records.views import stats_sessions

urlpatterns = [
    path(
        "list/", stats_sessions.ListStatsSessions.as_view(), name="stats_session_list"
    ),
    path(
        "create/",
        stats_sessions.CreateStatsSession.as_view(),
        name="stats_session_create",
    ),
    path(
        "delete/<int:pk>/",
        stats_sessions.DeleteStatsSession.as_view(),
        name="stats_session_delete",
    ),
    path(
        "detail/<int:pk>/",
        stats_sessions.DetailStatsSession.as_view(),
        name="stats_session_detail",
    ),
    path(
        "record/create/",
        stats_sessions.CreateStatsRecord.as_view(),
        name="stats_create",
    ),
    path(
        "<int:stats_session_pk>/record/<int:stat_pk>/delete/",
        stats_sessions.DeleteStatsRecord.as_view(),
        name="stats_delete",
    ),
    path(
        "<int:stats_session_pk>/results/",
        stats_sessions.StatsRecordResults.as_view(),
        name="stats_result",
    ),
]
