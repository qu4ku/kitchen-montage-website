from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('my_admin/', admin.site.urls),
	path('', include('core.urls')),    
]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	# Media files are not, by default, served during development.
	] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)