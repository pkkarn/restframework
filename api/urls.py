from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiUrls, name='api'),
    path('teachersQuestion/', views.teachersQuestion, name='questions'),
    path('studentQuestionSubmit/', views.studentQuestionSubmit, name='student'),
    path('question/<str:pk>/', views.question, name='question_detail'),
    path('submitQuery', views.submitQuestionForm, name='submit_question')
]
