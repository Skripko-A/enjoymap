from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.show_map, name='main_page'),
                  path('places/<int:location_id>/', views.show_location, name='location_page'),
                  path('tinymce/', include('tinymce.urls')),
              ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

