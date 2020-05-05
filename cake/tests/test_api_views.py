from copy import deepcopy

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
import logging

from cake.factories import CakeFactory
from cake.models import Cake

logger = logging.getLogger(__name__)

FAKE_RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'  # always pass
FAKE_RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'  # always pass


@override_settings(
    LANGUAGE_CODE='EN',
    RECAPTCHA_PUBLIC_KEY=FAKE_RECAPTCHA_PUBLIC_KEY,
    RECAPTCHA_PRIVATE_KEY=FAKE_RECAPTCHA_PRIVATE_KEY,
)
class CakeCreateListViewSetTest(TestCase):
    def setUp(self):
        self.data = {
            'name': 'Name :)',
            'text': 'Text :)',
        }

        self.data_with_captcha = dict(captcha='x', **self.data)

    def test_create_without_captcha(self):
        self.assertEqual(Cake.objects.count(), 0)
        response = self.client.post(
            reverse(
                'api:cake-list'
            ),
            data=self.data
        )
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(
            response.json(),
            {'captcha': ['This field is required.']}
        )
        self.assertEqual(Cake.objects.count(), 0)

    def test_create_with_empty_captcha(self):
        data = deepcopy(self.data_with_captcha)
        data['captcha'] = ''

        self.assertEqual(Cake.objects.count(), 0)
        response = self.client.post(
            reverse(
                'api:cake-list'
            ),
            data=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(
            response.json(),
            {'captcha': ['This field may not be blank.']}
        )
        self.assertEqual(Cake.objects.count(), 0)

    def test_create_with_captcha(self):
        self.assertEqual(Cake.objects.count(), 0)
        response = self.client.post(
            reverse(
                'api:cake-list'
            ),
            data=self.data_with_captcha
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Cake.objects.count(), 1)

    def test_create_with_captcha_strip_tags(self):
        data = dict(captcha='xx', name='<script>alert(1)</script>', text='<script>alert(2)</script>')

        self.assertEqual(Cake.objects.count(), 0)
        response = self.client.post(
            reverse(
                'api:cake-list'
            ),
            data=data
        )
        self.assertEqual(response.status_code, 201)
        response_data: dict = response.json()
        self.assertEqual(response_data['name'], 'alert(1)')
        self.assertEqual(response_data['text'], 'alert(2)')

        self.assertEqual(Cake.objects.count(), 1)

    def test_list(self):
        CakeFactory()
        CakeFactory()

        response = self.client.get(
            reverse(
                'api:cake-list'
            )
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
