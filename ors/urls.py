"""ors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from login.views import login_views
from django.conf.urls.static import static
from member.views import changePassword, DeleteAccount, editProfile ,MemberProfile, My_Course
from admin_user.views import AdminProfile
from contact.views import Contact_View
from orders.views import new_order,Payment_Gateway
from class_details.views import Add_Class, View_Class
from schedule.views import Change_Schedule,Update_Schedule


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('login.urls')),
    url(r'^',include('admin_user.urls')),
    url(r'^', include('instructor.urls')),
    url(r'^adminprofile/',AdminProfile),
    url(r'^login/', login_views),
    url(r'^cpass/', changePassword),
    url(r'^account/', DeleteAccount),
    url(r'^editprofile/', editProfile),
    url(r'^profile/', MemberProfile),
    url(r'^contact/', Contact_View),
    url(r'^order/', new_order),
    url(r'^payment/', Payment_Gateway),
    url(r'^my_course/', My_Course),
    url(r'^add_class/', Add_Class),
    url(r'^view_class/', View_Class),
    url(r'^change_schedule/',Change_Schedule),
    url(r'^update_schedule/', Update_Schedule),
    url(r'^admin_tools/', include('admin_tools.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
