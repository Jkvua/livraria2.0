from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from uploader.router import router as uploader_router

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet
from core.views import CategoriaViewSet
from core.views import EditoraViewSet
from core.views import AutorViewSet
from core.views import LivroViewSet
from core.views import CompraViewSet
from core.views import ComentarioViewSet

router = DefaultRouter()

# router.register("usuarios", UserViewSet, basename="users")
router.register("autores", AutorViewSet)
router.register("categorias", CategoriaViewSet)
router.register("comentarios", ComentarioViewSet)
router.register("compras", CompraViewSet)
router.register("editoras", EditoraViewSet)
router.register("livros", LivroViewSet)
router.register(r"usuarios", UserViewSet, basename="usuarios")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        "api/media/", 
        include(uploader_router.urls)
    ),

    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)