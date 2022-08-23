from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Developer, Skill
from .serializers import ProjectSerializer, DeveloperSerializer, SkillSerializer


@api_view(['GET'])
def project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def developer(request):
    if request.method == 'GET':
        projects = Developer.objects.prefetch_related('skill')
        serializer = DeveloperSerializer(projects, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def skill(request):
    if request.method == 'GET':
        projects = Skill.objects.all()
        serializer = SkillSerializer(projects, many=True)
        return Response(serializer.data)

