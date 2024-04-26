from django.test import TestCase
from setup.models import EducationalLevel


class EducationalLevelModelTestCase(TestCase):
    def test_educational_level_creation(self):
        # Create an instance of EducationalLevel
        educational_level = EducationalLevel.objects.create(name='Test Educational Level')

        # Check if the object was created successfully
        self.assertIsNotNone(educational_level)
        self.assertEqual(educational_level.name, 'Test Educational Level')

    def test_educational_level_str(self):
        # Create an instance of EducationalLevel
        educational_level = EducationalLevel.objects.create(name='Test Educational Level')

        # Check if the __str__ method returns the expected string representation
        self.assertEqual(str(educational_level), 'Test Educational Level')

    def test_educational_level_verbose_name_plural(self):
        # Check if the verbose name plural is correctly set
        self.assertEqual(
            EducationalLevel._meta.verbose_name_plural,
            '01_educational_level'
        )

