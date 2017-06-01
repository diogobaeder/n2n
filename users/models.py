from uuid import uuid4

from django.db import models


class IdentifiableModel(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Company(IdentifiableModel):
    pass


class Project(IdentifiableModel):
    pass


class User(IdentifiableModel):
    company = models.ForeignKey(Company, related_name='users', null=True)
    projects = models.ManyToManyField(Project, related_name='users')
