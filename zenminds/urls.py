from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('player/',include('player.urls')),
    path('match/',include('match.urls')),
    path('ball/',include('ball.urls')),
    path('accounts/',include('accounts.urls'))
]
