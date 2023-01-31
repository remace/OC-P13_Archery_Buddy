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
        "delete/<int:pk>/",
        stats_sessions.DeleteStatsSession.as_view(),
        name="stats_delete",
    ),
    path(
        "detail/<int:pk>/",
        stats_sessions.DetailStatsSession.as_view(),
        name="stats_detail",
    ),
]