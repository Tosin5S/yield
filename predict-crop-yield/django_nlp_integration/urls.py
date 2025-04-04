from django.contrib import admin
from django.urls import path, include
from .nlp_app import views
# from .views import fielddata_list, fielddata_explain, chatbot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('fielddata/', views.fielddata_list, name='fielddata_list'),
    path('explain/<int:pk>/', views.fielddata_explain, name='fielddata_explain'),
    #path('chatbot/', views.chatbot_response, name='fielddata_explain'),
    path('chatbot/<int:pk>/', views.chatbot_response, name='chatbot_response'),
    # path('chatbot/', views.chatbot, name='chatbot'),
    path('fielddata/<int:pk>/', views.fielddata_detail, name='fielddata_detail'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('fielddata/new/', views.fielddata_create, name='fielddata_create'),
    path('fielddata/<int:pk>/edit/', views.fielddata_update, name='fielddata_update'),
    path('fielddata/<int:pk>/delete/', views.fielddata_delete, name='fielddata_delete'),
    path('fielddata/<int:pk>/predict/', views.fielddata_predict, name='fielddata_predict'),
    path('table', views.table, name='table'),
]