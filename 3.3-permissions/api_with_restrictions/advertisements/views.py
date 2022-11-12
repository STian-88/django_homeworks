from django.conf import settings

from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer, UserSerializer

from advertisements.permissions import IsOwnerOrOnlyRead
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter,
            OrderingFilter, ]
    search_fields = ['title', 'description']
    ordering = ['-created_at']
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.request.user.id in settings.ADMIN_IDS:
            return []
        if self.action in ['create', ]:
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy', ]:
            return [IsOwnerOrOnlyRead()]
        return []

