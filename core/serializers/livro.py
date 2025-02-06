from rest_framework.serializers import ModelSerializer, SlugRelatedField, Serializer, SlugRelatedField, ValidationError
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        capa = ImageSerializer(
            required=False,
            read_only=True,
        )

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco")

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1


class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 110
        capa = ImageSerializer(required=False)

# class LivroAlterarPrecoSerializer(serializers.Serializer):
#     preco = serializers.DecimalField(max_digits=10, decimal_places=2)

#     def validate_preco(self, value):
#         """Valida se o preço é um valor positivo."""
#         if value <= 0:
#             raise serializers.ValidationError("O preço deve ser um valor positivo.")
#         return value




