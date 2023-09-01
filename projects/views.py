from rest_framework import viewsets
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            get_profile_id = kwargs.get("pk")
            profile = Profile.objects.get(id=get_profile_id)
            # busque o id do perfil
            # crie uma variável para guardar esse perfil

            return render(
                request,
                "profile_detail.html",
                {"profile": profile},
                # passe os parâmetros necessários para o template:
                # a requisição, o caminho do template e um dict com dados
                # para o template
            )
        return super().retrieve(request, *args, **kwargs)
