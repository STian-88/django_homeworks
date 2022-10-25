from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from measurement.views import SensorView, SensorDetailView, MeasurementView


urlpatterns = [
        path('sensor/', SensorView.as_view()),
        path('sensordetail/<pk>/', SensorDetailView.as_view()),
        path('measurement/', MeasurementView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

