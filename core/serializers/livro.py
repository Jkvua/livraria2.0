from rest_framework.serializers import ModelSerializer
# from core.serializers import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer, LivroListRetrieveSerializer
from core.models import Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco")

# class LivroRetrieveSerializer(ModelSerializer):
#     class Meta:
#         model = Livro
#         fields = "__all__"
#         depth = 1


# class LivroListRetrieveSerializer(ModelSerializer):
#     class Meta:
#         model = Livro
#         fields = "__all__"
#         depth = 1




