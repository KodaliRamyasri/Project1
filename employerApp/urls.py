from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('addJobPost/', views.addJobPost, name='addJobPost'),
    path('addJobPost1/', views.addJobPost1, name='addJobPost1'),
    path('viewJobDetails/', views.viewJobDetails, name='viewJobDetails'),
    path('deleteJobDetails/<int:job_id>/', views.deleteJobDetails, name='deleteJobDetails'),
    path('editJobDetails/<int:job_id>/', views.editJobDetails, name='editJobDetails'),
    path('jobApplicationList/', views.jobApplicationList, name='jobApplicationList'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)