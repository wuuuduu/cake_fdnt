from captcha.fields import ReCaptchaField
from django.utils.html import strip_tags
from rest_framework import serializers

from cake.models import Cake

re_captcha_field = ReCaptchaField()


class CakeSerializer(serializers.ModelSerializer):
    captcha = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Cake
        fields = ('id', 'name', 'text', 'captcha')
        read_only_fields = ('id',)

    def validate_name(self, value):
        return strip_tags(value)

    def validate_text(self, value):
        return strip_tags(value)

    def validate_captcha(self, value):
        re_captcha_field.validate(value)
        return value

    def create(self, validated_data):
        del validated_data['captcha']
        return super(CakeSerializer, self).create(validated_data)
