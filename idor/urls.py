from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all_students, name='list_all_students'),
    path("student/<uuid:pk>/", views.student_info, name="student_info"),
    path('json-data/<uuid:pk>/', views.json_data, name="json_data"),
]
