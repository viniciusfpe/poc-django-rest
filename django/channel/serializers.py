from rest_framework import serializers

from channel.models import Channel


class ChannelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Channel
        fields = ('id', 'description', 'create_user', 'create_date')