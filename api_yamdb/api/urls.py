from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentsViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, check_token,
                    create_user)

app_name = 'api'

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews',
)

router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentsViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', create_user, name='signup'),
    path('v1/auth/token/', check_token, name='token')
]
