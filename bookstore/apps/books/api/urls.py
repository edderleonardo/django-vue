from rest_framework.routers import DefaultRouter
from .views import BooksViewSet

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')

urlpatterns = []
urlpatterns += router.urls
