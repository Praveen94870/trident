"""
URL configuration for trident project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from master import views
app_name = 'master'

urlpatterns = [

    
    path('about.html', views.about, name='about.html'),
    path('blog_home.html', views.blog_home, name='blog_home.html'),
    path('blog_post.html', views.blog_post, name='blog_post.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('faq.html', views.faq, name='faq.html'),
    path('index.html', views.index, name='index.html'),
    path('portfolio_item.html', views.portfolio_item, name='portfolio_item.html'),
    path('portfolio_overview.html', views.portfolio_overview, name='portfolio_overview.html'),
    path('kart', views.kart, name='kart'),
    path('order', views.order, name='order'),
    path('product', views.product, name='product'),
    path('products', views.products, name='products'),



    ###for user registratio, sign-in sign-out
    path('info', views.info, name = 'info'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

]