from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.IndexPageView.as_view()),
    path("index/", views.IndexPageView.as_view()),
    path("about/", views.AboutPageView.as_view()),
    path("contact/", views.ContactPageView.as_view()),
    path("courses/", views.CoursesPageView.as_view()),
    path("portfolio/", views.PortfolioPageView.as_view()),
    path("pricing/", views.PricingPageView.as_view()),
]