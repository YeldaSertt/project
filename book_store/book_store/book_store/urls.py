"""book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views4
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
from django.conf.urls import url,include
from book.views import homepage
from django.conf.urls.static import static
from django.conf import settings

# book altındaki viewde bulunan defleri burada tanıt
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r"^$",homepage),
    url(r"^bookstore/",include("book.urls")),
    url(r"^bookstore/",include("login.urls"))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)