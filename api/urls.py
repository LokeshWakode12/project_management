# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, UserViewSet, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet, basename="user")

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),

    # Protected endpoints (automatically covered by IsAuthenticated)
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users-list'),
    path('users/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))
] + router.urls
