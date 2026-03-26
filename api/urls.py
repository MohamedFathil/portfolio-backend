from django.urls import path
from .views import (
    ContactView,
    ProjectListView,
    SkillListView,
    CertificationListView,
    PortfolioSummaryView,
)

urlpatterns = [
    # Contact form submission
    path('contact/', ContactView.as_view(), name='contact'),

    # Portfolio data endpoints
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('skills/', SkillListView.as_view(), name='skills'),
    path('certifications/', CertificationListView.as_view(), name='certifications'),
    path('summary/', PortfolioSummaryView.as_view(), name='summary'),
]
