from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import BookViewSet, AuthorViewSet, GenreViewSet, CategoryViewSet, CartViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"cart", CartViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/google/", include("allauth.socialaccount.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)