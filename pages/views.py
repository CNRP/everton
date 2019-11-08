from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from everton.models import NewsPost
from django.views.generic import DetailView
from analytics.mixins import ObjectViewMixin

class ArticleViews(ObjectViewMixin, DetailView):
    template_name = 'pages/article.html'
    queryset = NewsPost.objects.all()

    def get_object(self):
        if(self.kwargs.get("id")):
            id_ = self.kwargs.get("id")
        else:
            id_ = NewsPost.objects.filter(visible='1').latest('published_on').id
            self.template_name = 'pages/articlepreview.html'
        return get_object_or_404(NewsPost, id=id_)

def latest(request):
    latest = NewsPost.objects.all().filter(visible='1').order_by('-published_on')[0];
    context = {
        'title': 'Latest',
        'id': latest.id,
    }
    return render(request, 'pages/latest.html', context)