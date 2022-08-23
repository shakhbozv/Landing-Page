from rest_framework import serializers
from .models import Project, Developer, Skill


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'project_thumb')


class DeveloperSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['skill'] = SkillSerializer(instance.skill, many=True).data
        return data

    class Meta:
        model = Developer
        fields = ('id', 'full_name', 'stack', 'description', 'skill', 'developer_thumb')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'title', 'skill_thumb')
