from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('day2app/', include('day2app.urls')),
    # path('day3app/', include('day3app.urls')),
    path('', views.index, name='book_list'),
]