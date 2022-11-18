from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name',]

class AdvertisementSerializer(serializers.ModelSerializer):
    creator = UserSerializer(
            read_only=True
    )

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator',
                'status','created_at', ]

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        print(self.context['request'].data.get('status'))
        if Advertisement.objects.filter(creator=self.context['request'].user,
                status='OPEN').count() > 9 and self.context['request'].data.get('status') == 'OPEN':
            raise serializers.ValidationError('Превышено количество открытых обьявлений')
        return data

