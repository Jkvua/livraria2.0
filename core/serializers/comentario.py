from rest_framework.serializers import ModelSerializer

from core.models import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("id", "comentario", "data", "usuario", "livro")