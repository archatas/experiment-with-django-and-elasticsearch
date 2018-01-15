from django.conf.urls import include, url
from django.contrib import admin

from library.libraryapp.views import book_list


urlpatterns = [
    url(r'^$', book_list),
    url(r'^admin/', include(admin.site.urls)),
]
