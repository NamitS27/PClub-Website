from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/',include("events.urls")),
    path('summernote/',include("django_summernote.urls")),
    path('resources/',include("resources.urls")),
    path('contact_us/',include("contact_us.urls")),
    path('about_us/',include("about_us.urls")),
    path('cp/',include("competitive_programming.urls")),
    path('',include("home_announce.urls")),
    path('testing/',include("testing.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
