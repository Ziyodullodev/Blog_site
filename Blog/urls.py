from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.HomeView.as_view(), name="home-page"),
    path('post/<int:pk>', views.PostView, name="post-detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)