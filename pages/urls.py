from django.urls import include, path
from . import views
from .views import(
    ArticleViews,    
)

app_name = 'pages'

urlpatterns = [
    #url(r'(?P<id>\d+)/$', views.article, name='article'),
    path('<int:id>/', ArticleViews.as_view(), name='article'),
    path('latest/', views.latest, name='latest'),
]
