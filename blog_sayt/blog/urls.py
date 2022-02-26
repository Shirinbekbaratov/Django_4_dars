from django.urls import path
from .views import BlogList,BlogDetail,BlogCreate,BlogUpdate,BlogDelete

urlpatterns=[
    path('post/<int:pk>/delete/',BlogDelete.as_view(),name='post_delete'),
    path('post/<int:pk>/edit/',BlogUpdate.as_view(),name='post_edit'),
    path('post/new/',BlogCreate.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogDetail.as_view(),name='post_detail'),
    path('',BlogList.as_view(),name='home'),

]