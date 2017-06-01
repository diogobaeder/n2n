from uuid import UUID

from django.test import TestCase

from .models import *


class UserTest(TestCase):
    def test_creates_basic_user(self):
        user = User.objects.create(name='John')

        self.assertEqual(user.name, 'John')
        self.assertIsInstance(user.uuid, UUID)

    def test_adds_a_project(self):
        user = User.objects.create(name='John')
        project = Project.objects.create(name='Lunch')

        user.projects.add(project)

        self.assertEqual(user.projects.first().name, 'Lunch')

    def test_can_belong_to_a_company(self):
        company = Company.objects.create(name='Acme')
        user = User.objects.create(name='John', company=company)

        self.assertEqual(user.company.name, 'Acme')

    def test_gets_by_uuid(self):
        user = User.objects.create(name='John')

        retrieved = User.objects.get_by_uuid(user.uuid)

        self.assertEqual(retrieved.id, user.id)


class CompanyTest(TestCase):
    def test_creates_basic_company(self):
        company = Company.objects.create(name='Acme')

        self.assertEqual(company.name, 'Acme')
        self.assertIsInstance(company.uuid, UUID)

    def test_gets_by_uuid(self):
        company = Company.objects.create(name='Acme')

        retrieved = Company.objects.get_by_uuid(company.uuid)

        self.assertEqual(retrieved.id, company.id)


class ProjectTest(TestCase):
    def test_creates_basic_project(self):
        project = Project.objects.create(name='Lunch')

        self.assertEqual(project.name, 'Lunch')
        self.assertIsInstance(project.uuid, UUID)
