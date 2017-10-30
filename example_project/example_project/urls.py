# -*- coding: utf-8 -*-

from blog import views
from django.contrib import admin
from django.urls import path, include

from setup import hitcount

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="index"),

    path('generic-detail-view-ajax/<int:pk>/', views.PostDetailJSONView.as_view(), name="ajax"),
    path('hitcount-detail-view/<int:pk>/$', views.PostDetailView.as_view(), name="detail"),
    path('hitcount-detail-view-count-hit/<int:pk>/$', views.PostCountHitDetailView.as_view(), name="detail-with-count"),
    # for our built-in ajax post view
    path('hitcount/', include(hitcount.urls)),
]
