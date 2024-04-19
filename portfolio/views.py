from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView
from django.contrib import messages
from .models import Category, Message, Work, Service, Testimony, Author

class IndexView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(kwargs={'categories': Category.objects.all(),
                               'works': Work.objects.all(),
                               'services': Service.objects.all(),
                               'testimonies': Testimony.objects.all()})
        return context

class AboutView(TemplateView):

    template_name = 'about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        kw_args = {'author': Author.objects.all()[0]}
        context.update(author=Author.objects.get())
        return context
    
class WorkDetailView(DetailView):

    template_name = 'work_detail.html'
    model = Work
    slug_url_kwarg = 'work_slug'
    context_object_name = 'work'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(kwargs={'testimonies': Testimony.objects.all()})
        return context

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return get_object_or_404(Work.objects.filter(is_published=True), slug=self.kwargs[self.slug_url_kwarg])
    
class ContactView(FormView):

    template_name = 'contact.html'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return render(request, template_name='contact.html')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        msg = Message(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        msg.save()
        messages.success(request, 'Message sent')
        return redirect(request, 'contact')