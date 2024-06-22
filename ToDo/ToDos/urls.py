from django.urls import path

from . import views

app_name = 'ToDos'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_item, name='add'),
    path('update/<int:pk>', views.update_item, name='update'),
    path('delete/<int:pk>', views.delete_item, name='delete'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    # path('accounts/logout', views.custom_logout_view, name='logout'),
    path('accounts/logout/', views.UserLogoutView.as_view(http_method_names=['get', 'post', 'options']), name='logout'),

]
