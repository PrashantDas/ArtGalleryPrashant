from django.contrib import admin
from django.urls import path
from Artist import views as artist_views
from Photos import views as photos_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # routes belonging to Photos
    path('', photos_views.home, name='home'),
    path('add/', photos_views.AddPhotoView.as_view(), name='add'),    
    path('add_category/', photos_views.AddCategoryView.as_view(), name='add_category'),
    path('gallery/', photos_views.gallery, name='gallery'),    
    path('details/<int:pk>/', photos_views.ViewOne.as_view(), name='details'),
    path('delete/<int:pk>/', photos_views.DeletePhoto.as_view(), name='delete'),

    # routes belonging to Artist
    path('login/', artist_views.artist_login_view, name='login'),
    path('register/', artist_views.register_artist_view, name='register'),
    path('viewall/', artist_views.ViewAllArtists.as_view(), name='viewall'),
    path('viewone/<int:pk>/', artist_views.ViewOneArtist.as_view(), name='viewone'),
    path('edit/<int:pk>/', artist_views.UpdateArtistProfile.as_view(), name='edit'),
    path('logout/', artist_views.ArtistLogout.as_view(), name='logout'),

    # Views to reset password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='artist/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='artist/password_reset_done.html'),
         name='password_reset_done'), # actually jsst a template showing that instructions for resert have been sent

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='artist/password_reset_confirm.html'),
         name='password_reset_confirm'), # required, as shown by error template
         
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='artist/password_reset_complete.html'),
         name='password_reset_complete'), # required, shows that the password is reset
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
