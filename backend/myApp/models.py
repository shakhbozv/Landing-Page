from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=355)
    project_thumb = models.ImageField(null=True, blank=True)

    def __int__(self):
        return self.title


STACK = {
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Full-stack', 'Full-stack'),
}


class Developer(models.Model):
    full_name = models.CharField(max_length=255)
    stack = models.CharField(max_length=255, choices=STACK)
    description = models.CharField(max_length=255)
    developer_thumb = models.ImageField(null=True, blank=True)
    skill = models.ManyToManyField('Skill', null=True, blank=True)

    def __int__(self):
        return self.skill.title

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    title = models.CharField(max_length=255)
    skill_thumb = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
