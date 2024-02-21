from accounts import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('creg/',views.cusreg,name='creg'),
    path('vreg/',views.venreg,name='vreg'),
]
