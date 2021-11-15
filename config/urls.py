from django.conf import settings
from django.conf.urls.static import static, serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from apps.data_access.views import CustomLoginView

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin/login/", CustomLoginView.as_view(), name="login"),
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
    path("", TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
