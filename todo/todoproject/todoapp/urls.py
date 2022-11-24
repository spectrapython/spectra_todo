from django.conf import settings
from django.conf.urls.static import static

from .import views
from django.urls import path

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('cbvhome/',views.tlistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.tdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.tupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.tdeleteview.as_view(),name='cbvdelete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)