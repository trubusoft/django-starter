from http import HTTPStatus

from django.test import TestCase
from django.test.utils import override_settings


class ExampleTestCase(TestCase):

    def test_index_with_debug_false(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, HTTPStatus.NOT_FOUND)

    @override_settings(DEBUG=True)
    def test_index_with_debug_true(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'The install worked successfully! Congratulations!')
        self.assertContains(response, 'You are seeing this page because')
        self.assertContains(response, 'DEBUG=True')
        self.assertContains(response, 'is in your settings file and you have not configured any URLs.')
