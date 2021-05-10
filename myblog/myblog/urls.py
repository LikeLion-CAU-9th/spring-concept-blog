from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('my-post', blog.views.my_post, name="myPost"),
    path('new', blog.views.new_post, name = "new"),
    path('post/<int:pk>', blog.views.post_detail, name = "post-detail"),
    path('post/edit/<int:pk>', blog.views.post_update, name = "post-edit"),
    path('post/delete/<int:pk>', blog.views.post_delete, name = "post-delete")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
