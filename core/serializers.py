from dataclasses import field
from re import M
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class meta:
        model = Categoria
        fields = "__all__" 