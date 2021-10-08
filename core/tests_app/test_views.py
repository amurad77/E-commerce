from django.conf import settings
from django.test import TestCase
from django.urls import reverse_lazy

from core.models import Contact


class CreateContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('core:contact')
        cls.valid_data = {
            'first_name': 'Murad',
            'last_name': 'Abdullayev',
            'phone_number': '0506531341',
            'email': 'murad@gmail.com',
            'message': 'Hello World',
        }

        cls.invalid_data = {
            'email': 'murad',
            'phone_number': '0506531341',
            'message': 'Hello World',
        }

        cls.contact_url = f'/{settings.LANGUAGE_CODE}/core/contact/'

    def test_url(self):

        self.assertEqual(self.url, self.contact_url)

    def test_get_request(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        contact_data = Contact.objects.last()
        self.assertEqual(self.valid_data['first_name'], contact_data.first_name)
        self.assertEqual(self.valid_data['email'], contact_data.email)
        self.assertEqual(self.valid_data['message'], contact_data.message)

    def test_post_invalid_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        print('ContactViewTest')