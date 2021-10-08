from django.test import TestCase 
from core.models import Contact, Subscribe


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        data1 = {
            'first_name': 'Murad',
            'last_name': 'Abdullayev',
            'phone_number': '0506531341',
            'email': 'murad@gmail.com',
            'message': 'Sehife isleyir',

        }        

        data2 = {
            'first_name': 'Idris',
            'last_name': 'Shabanli',
            'phone_number': '0555555555',
            'email': 'idris@gmail.com',
            'message': 'Sehife islemir',

        }

        Contact.objects.create(**data1)
        Contact.objects.create(**data2)

        cls.contact_info1 = Contact.objects.first()
        cls.contact_info2 = Contact.objects.last()
        
    def test_created_data(self):
        self.assertEqual(self.contact_info1.first_name, 'Murad')
        self.assertEqual(self.contact_info2.email, 'idris@gmail.com')
    
    @classmethod
    def tearDownClass(cls):
        print('ContactModel')



class SubscribeModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'email': 'murad1@gmail.com',

        }

        Subscribe.objects.create(**data)

        cls.contact_info = Subscribe.objects.first()


    def test_created_data(self):
        self.assertEqual(self.contact_info.email, 'murad1@gmail.com')

    def test_str_method(self):
        self.assertEqual(str(self.contact_info), 'murad1@gmail.com')


    @classmethod
    def tearDownClass(cls):
        print('SubscribeModel')



