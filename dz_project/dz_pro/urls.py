from django.urls import path
from .views import WindowView, PostView, WriteView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', WindowView.as_view(), name="window"),
    path('article/<int:pk>', PostView.as_view(), name="postview"),
    path('write/', WriteView.as_view(), name='write'),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post')
]
