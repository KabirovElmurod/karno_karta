
from django.urls import path
from . import views
urlpatterns = [
    path('',  views.index),
    path('f_qiymatlar/', views.f_qiymatlar),
    path('f_qiymat_much/', views.f_qiymat_much),
    path('son_input/', views.son_input),

]
