from datetime import date
from django.test import TestCase
from core.forms import ContactForm


class ContactFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
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
        
    def test_form_with_valid_data(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = ContactForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('Bu sahə tələb edilir.', form.errors['first_name'])
        self.assertIn('Keçərli e-poçt ünvanı daxil edin.', form.errors['email'])


    @classmethod
    def tearDownClass(cls):
        print('ContactForm')