# """
# URL configuration for crud project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# # Examples:
# # Function views
# #     1. Add an import:  from my_app import views
# #     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# # Class-based views
# #     1. Add an import:  from other_app.views import Home
# #     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# # Including another URLconf
# #     1. Import the include() function: from django.urls import include, path
# #     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# # """
# from django.conf import settings
# from django.contrib import admin
# from django.urls import path,include
# from app.views import  home,login,test,signup,logout,saveprofile
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home ,name='index'),
#     path('login/', login, name='login'),
#     path('test/',test,name='test'),
#     path('signup/',signup,name= 'signup'),
#     path('logout/',logout,name= 'logout'),
#     path('saveprofile/',saveprofile,name= 'saveprofile'),
  
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf import settings
from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, logoutu, profileCreate, profileEdit, profileDelete
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logoutu, name='logout'),   
    path('profileCreate/', profileCreate, name='profileCreate'),
    path('profileEdit/<int:pk>/', profileEdit, name='profileEdit'),
    path('profileDelete/<int:pk>/', profileDelete,name='profileDelete'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
