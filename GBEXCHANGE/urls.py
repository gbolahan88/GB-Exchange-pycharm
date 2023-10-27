from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('blog', views.blog, name="blog"),
    path('rates', views.rates, name="rates"),
    path('contact', views.contact, name="contact"),
]
