from django.urls import path
from django.conf.urls.static import static
from .views import pIndex, workExperienceDetail, certificatesDetail


urlpatterns = [
    path('', pIndex.as_view(), name='portfolio'),
    path('experience/<slug:slug>', workExperienceDetail.as_view(), name='work_experience_detail'),
    path('certificates/<slug:slug>', certificatesDetail.as_view(), name='certificate_detail'),
]
