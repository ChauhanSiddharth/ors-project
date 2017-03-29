from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from course.views import searchbox
from .views import (login_views,logout_views,register_views,details_views,edit_profile,delete_data

)
urlpatterns = [
    url(r'^$', login_views, name="login"),
    url(r'^login/', login_views, name="login"),
    url(r'^logout/', logout_views, name="logout"),
    url(r'^register/', register_views, name="register"),
    url(r'^details/', details_views, name="details"),
    url(r'^edit_profile/',  edit_profile,name="edit_profile"),
    url(r'^delete_data/', delete_data,name="delete_data"),
    url(r'^searchbox/', searchbox ,name="searchbox"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)