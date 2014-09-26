from aniversario.views import PessoaListView, Home, router, pizzas
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$',
        Home.as_view()
        , name='home'
    ),
    url(r'^pizzas/$',
        pizzas
        , name='pizzas'
    ),


    url(r'^ajax/',
        include(router.urls)
        , name='pessoa-list'
    ),

    # url(r'^blog/', include('blog.urls')),
    #url(r'^djangular/', include('djangular.urls')),
    url(r'^admin/', include(admin.site.urls)),
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
