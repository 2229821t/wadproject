from django.test import TestCase


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from LanguageExchange.models import MyUser
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):
    
    def setUp(TestCase):
        MyUser.objects.create(email="hsjo12@student.gla.ac.uk", username="DAEN",password="123456789" )
       
    def test_login(self):
        self.client.login(email="hsjo12@student.gla.ac.uk", password='123456789')
        response = self.client.get('/LanguageExchange/')
        user = MyUser.objects.get(email="hsjo12@student.gla.ac.uk")
        self.assertEqual(user.email, "hsjo12@student.gla.ac.uk")
 
class DBTest(TestCase):   
    def test_usingGUmail(self):
        user = MyUser.objects.all()
        for i in user:
            self.assertTrue(i.email.endswith("gla.ac.uk"))

    def test_more_than_8_password(self):
        user = MyUser.objects.all()
        for i in user:
            self.assertTrue(len(i.password)>7)   

