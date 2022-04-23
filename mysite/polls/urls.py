from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('',views.ForumListDetail.as_view(),name="home"),
    path("<int:pk>", views.ForumDetailView.as_view(), name="profile_detail"),
    path('auth/signup',views.register_request,name='auth')
]

