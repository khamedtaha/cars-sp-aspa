
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.main),
    path('upload-file/',views.upload_file),
    path('all-video/' , views.all_video)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)