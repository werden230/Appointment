from django.urls import path
from . import views

urlpatterns = [
    path('', views.info),
    path('blog/', views.blog),
    path('blog/<int:post_id>', views.post)
]