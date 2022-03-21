from .views import CategoryViewSet, PostViewSet, UserViewSet,CommentViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('users',UserViewSet,basename='users')
router.register('comments',CommentViewSet,basename='comment')
router.register('category',CategoryViewSet,basename='category')
router.register('',PostViewSet,basename='posts')

urlpatterns = router.urls