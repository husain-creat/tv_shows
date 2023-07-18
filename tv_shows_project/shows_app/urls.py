from django.urls import path     
from . import views
urlpatterns = [ path('', views.index ), 
               path('shows/new', views.new_show, name='new_show' ),
               path('shows/<int:id>', views.desc,name='desc_page' ),
               path('shows/<int:id>/edit', views.update,name='update_show' ),  
               
                 ]
               