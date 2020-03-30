from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.static import serve
from django.conf.urls.static import static
from .settings import MEDIA_ROOT


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="posts/")),
    path("posts/", include("posts.urls")),
    path("media/<path:path>", serve, {"document_root": MEDIA_ROOT}),
]