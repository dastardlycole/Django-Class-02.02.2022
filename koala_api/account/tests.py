from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

# Create your tests here.
User = get_user_model()

class UserModelTestcase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name="Peter", last_name="John", password="111b2", email="email@gmail.com",phone="090398475895")

    def test_single_user(self):
        user = User.objects.get(id=1)
        # print(hashed_password)
        self.assertEqual(str(user), "email@gmail.com")
        self.assertEqual(user.first_name, 'Peter')
        self.assertEqual(user.last_name, 'John')
        self.assertEqual(check_password('111b2', user.password), True)
    
    def test_all_user(self):
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        
   