from django.http import HttpResponse
from django.views.generic import TemplateView



class IndexPageView(TemplateView):
    template_name = 'mainapp/index.html'
    test = 123
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['news_title'] = 'Новости'
        context['news_data'] = 'Описание новости'
        
        return context



class AboutPageView(TemplateView):
    template_name = 'mainapp/about.html'


class ContactPageView(TemplateView):
    template_name = 'mainapp/contact.html'


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses.html'


class PortfolioPageView(TemplateView):
    template_name = 'mainapp/portfolio.html'


class PricingPageView(TemplateView):
    template_name = 'mainapp/pricing.html'