from django.urls import path
from articleapp import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('form/',views.form_view, name='form'),
    path('all_articles/',views.all_articles, name='all_articles'),
    path('spec_art/<int:id>',views.spec_article_view, name='spec_art'),
    path('delete/<int:id>',views.delete_article, name='delete'), 
    path('update/<int:id>',views.update_view, name='update'),
    path('deleteall/',views.delete_all, name='delete_all'), 
]
