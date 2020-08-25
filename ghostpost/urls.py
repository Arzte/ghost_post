"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from homepage.views import homepage_view, add_post, add_upvote, add_downvote, boast_view, roast_view, vote_view

urlpatterns = [
    path('', homepage_view, name='home'),
    path('addpost', add_post, name='addpost'),
    path('addupvote/<int:post_id>', add_upvote, name='addupvote'),
    path('adddownvote/<int:post_id>', add_downvote, name='downvote'),
    path('boasts', boast_view, name='boast_view'),
    path('roasts', roast_view, name='roast_view'),
    path('votes', vote_view, name='vote_view'),
    path('admin/', admin.site.urls),
]
