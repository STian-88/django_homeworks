from django.conf import settings
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser

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
        if self.request.user.is_staff:
            return []
        if self.action in ['create', ]:
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update', 'destroy', ]:
            return [IsOwnerOrOnlyRead()]
        return []

    def list(self, request):
        if type(request.user) is AnonymousUser:
            queryset = Advertisement.objects.filter(status='OPEN')
            serializer = AdvertisementSerializer(queryset, many=True)
            return Response(serializer.data)
        queryset = Advertisment.objects.exclude(creator!=request.user, status='DRAFT')
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

