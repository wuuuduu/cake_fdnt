from captcha.fields import ReCaptchaField
from django.utils.html import strip_tags
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cake.models import Cake, Position

re_captcha_field = ReCaptchaField()


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        exclude = ('id', 'cake')


class CakeSerializer(serializers.ModelSerializer):
    captcha = serializers.CharField(required=True, write_only=True)
    position = PositionSerializer(read_only=True)

    class Meta:
        model = Cake
        fields = ('id', 'name', 'text', 'captcha', 'position')
        read_only_fields = ('id', 'position')

    def validate_name(self, value):
        return strip_tags(value)

    def validate_text(self, value):
        return strip_tags(value)

    def validate_captcha(self, value):
        re_captcha_field.validate(value)
        return value

    def validate(self, attrs):
        raise ValidationError('Adding new positions to cake has been closed.')
        # return attrs

    def create(self, validated_data):
        del validated_data['captcha']
        return super(CakeSerializer, self).create(validated_data)
