from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


from .views import ActorViewSet, MovieViewSet, CommentViewset, \
    ComentAPI_create

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('comments', CommentViewset, 'comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/', obtain_auth_token),
    path('api', ComentAPI_create.as_view()),
]
