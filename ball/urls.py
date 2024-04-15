from django.urls import path
from . import views

urlpatterns = [
    path('balls/all',views.getAllBalls),
    path('balls/add/',views.addBall),
    path('balls/<int:ball_id>/',views.getBallById),
    path('balls/update/<int:ball_id>/', views.updateBall, name='update_ball_by_id'),
    path('balls/delete/<int:ball_id>/', views.deleteBall, name='delete_ball_by_id'),
]