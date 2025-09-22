
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from blog import settings


from .views import home, contact,tech,employ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home-page',home, name='home'),
    path('contact-page',contact, name='contact'),
    path('tech-page',tech, name='tech'),
    path('employ-page',employ, name='employ'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


