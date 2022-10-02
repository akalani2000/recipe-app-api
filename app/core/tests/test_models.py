# Tests for Models

from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email='user@exmple.com', password='Test105*'):
    '''Create and return a new user'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    # Test models.

    def test_create_user_with_email_successful(self):
        # Test creating a user with email is successful.
        email = 'test@example.com'
        password = 'Test105*'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test email is normalized for new users.
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_raises_error(self):
        # Test that creating a user without an email raises a ValueError.
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Test123')

    def test_create_superuser(self):
        # Test createing a Superuser.
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'Test105*'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        # Test creating a recipe is successfull.
        user = get_user_model().objects.create_user(
            'test@example.com',
            'Test105*',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Recipe1',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Test recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        '''Test creating a tag successful.'''
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)

    def test_create_ingrediants(self):
        '''Test creating a ingredients successful.'''
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user, name='Ingrediant1')

        self.assertEqual(str(ingredient), ingredient.name)
