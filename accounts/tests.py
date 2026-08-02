from django.contrib.auth import get_user_model
from django.test import TestCase

# Code modified from https://testdriven.io/blog/django-custom-user-model/#tests


# Create your tests here.
class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="example@example.com", password="fooBar!123"
        )  # type: ignore
        self.assertEqual(user.email, "example@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()  # type: ignore
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")  # type: ignore
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")  # type: ignore

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com", password="foo"
        )  # type: ignore
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )  # type: ignore
