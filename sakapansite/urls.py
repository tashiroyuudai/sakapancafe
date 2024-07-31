from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'sakapansite'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path("detail/<int:pk>/", views.DetaView.as_view(), name='data-detail'),
        path('menu', views.MenuView.as_view(), name='menu'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)