from core.views import *
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",Home.as_view(),name="home"),
    path("song/<int:id>/",SongView.as_view(),name="song"),
    path("favoiritesong/<int:id>/",FavouriteSongView.as_view(),name="favoiritesong"),
    path('add-to-favorite/<int:id>/', AddToFavoritesView.as_view(), name='add-to-favorite'),
    path('remove-favorite/<int:id>/', deleteview, name='remove-favorite'),
    path("register/",RegisterView.as_view(),name="register"),
    path("",LoginView.as_view(),name="login"),  
    path("add-song/",AddSongView.as_view(),name="add-song"),
    path("logout/",LogoutView,name="logout"),
    path("favoirite/",FavouriteView.as_view(),name="favourite"),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('google-signup/', google_signup, name='google_signup'),
    path('googlelogin/', TemplateView.as_view(template_name="login.html")),
    path("api/",include("api.urls"))
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
