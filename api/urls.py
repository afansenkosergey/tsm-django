from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('choices', views.ChoiceViewSet)
router.register('article', views.ArticleViewSet)
router.register('category', views.CategoryViewSet)
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:question_id>/vote', views.choice_vote),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
