from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),     #   представления приложения
    path('accounts/', include('django.contrib.auth.urls'))  #   представления аутентификации
] + staticfiles_urlpatterns()
