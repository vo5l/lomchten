from django.urls import path
from .views import *
from . import views
from django.urls import re_path as url


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('doc/create/', PostCreate.as_view(), name='post_create_url'),
    path('doc/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('doc/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('doc/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('sections/', sections_list, name='sections_list_url'),
    path('section/create/', SectionCreate.as_view(), name='section_create_url'),
    path('section/<str:slug>/', SectionDetail.as_view(), name='section_detail_url'),
    path('section/<str:slug>/update/', SectionUpdate.as_view(), name='section_update_url'),
    path('section/<str:slug>/delete/', SectionDelete.as_view(), name='section_delete_url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
