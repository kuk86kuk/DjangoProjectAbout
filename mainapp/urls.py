from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.IndexPageView.as_view()),
    path("index/", views.IndexPageView.as_view(), name='index'),
    path("about/", views.AboutPageView.as_view(), name='about'),
    path("contact/", views.ContactPageView.as_view(), name='contact'),
    path("courses/", views.CoursesPageView.as_view(), name='courses'),
    path("portfolio/", views.PortfolioPageView.as_view(), name='portfolio'),
    path("pricing/", views.PricingPageView.as_view(), name='pricing'),
]