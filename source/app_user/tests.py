from django.test import TestCase

from app_user.models import User


class UserTestCase(TestCase):
    def test_create_superuser(self):
        self.assertIs(User.objects.exists(), False)
        superuser = User.objects.create_superuser('superuser')
        self.assertEquals(User.objects.count(), 1)

        self.assertIs(superuser.is_superuser, True)
        self.assertIs(superuser.is_staff, True)
        self.assertIs(superuser.is_active, True)

    def test_create_staff(self):
        self.assertIs(User.objects.exists(), False)
        staff = User.objects.create_user('staff', is_staff=True)
        self.assertEquals(User.objects.count(), 1)

        self.assertIs(staff.is_superuser, False)
        self.assertIs(staff.is_staff, True)
        self.assertIs(staff.is_active, True)

    def test_create_user(self):
        self.assertIs(User.objects.exists(), False)
        staff = User.objects.create_user('user')
        self.assertEquals(User.objects.count(), 1)

        self.assertIs(staff.is_superuser, False)
        self.assertIs(staff.is_staff, False)
        self.assertIs(staff.is_active, True)
