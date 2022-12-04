from django.contrib import admin
from django.urls import include, path

'''When to use include()
You should always use include() when you include other URL patterns. 
admin.site.urls is the only exception to this.'''
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('polls_generic/', include('polls_generic.urls')),
    path('admin/', admin.site.urls),
]
# path has four args
'''
route, view, kwargs, name
'''
