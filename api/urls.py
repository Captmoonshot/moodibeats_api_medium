from django.conf.urls import url

from .views import NewVideoAPIView

urlpatterns = [
	url(r'^new-videos/$', NewVideoAPIView.as_view()),
]