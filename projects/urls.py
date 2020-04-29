from django.urls import path
from . import views

urlpatterns = [
    # path('home', home, name='all_projects'),
    path('<int:id>', views.project_page, name='project_page'),
    path('<int:project_id>/donate/', views.donate, name='donate'),
    path('<int:project_id>/comment/', views.comment, name='comment'),
    path('<int:id>/cancel', views.cancel_project, name='cancel_project'),
    path('<int:id>/rating/<int:rate>', views.project_rating, name='project_rating')
    ]
