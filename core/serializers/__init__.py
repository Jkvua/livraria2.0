from .user import UserSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer
# from .livro import LivroSerializer, LivroListRetrieveSerializer, LivroListSerializer
from .livro import LivroSerializer, LivroDetailSerializer, LivroListSerializer, LivroRetrieveSerializer
from .compra import CompraSerializer, CompraCreateUpdateSerializer, ItensCompraSerializer, CompraListSerializer, ItensCompraListSerializer
