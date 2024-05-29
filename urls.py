# flashlearn_app/urls.py
from django.urls import path
from . import views
from .views import delete_teacher


urlpatterns = [
    path('', views.home, name='home'),
    
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    
    path('manageadmins/', views.manageadmins, name='manageadmins'),
    path('managestudents/', views.managestudents, name='managestudents'),
    path('manageteachers/', views.manageteachers, name='manageteachers'),
    
    #manage cards
    path('managecharacters/', views.managecharacters, name='managecharacters'),
    path('managecards/', views.managecards, name='managecards'),
    path('charactercard/', views.charactercard, name='charactercard'),

    #manage user 
    path('editusers/<int:user_id>/', views.edit_user, name='edit_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),

    #manage admin
    path('editadmin/<int:admin_id>/', views.edit_admin, name='edit_admin'),
    path('update_admin/<int:user_id>/', views.update_admin, name='update_admin'),
    path('delete-admin/<int:user_id>/', views.delete_admin, name='delete_admin'),

    #manage teachers
    path('editteacher/<int:user_id>/', views.edit_teacher, name='edit_teacher'),
    path('update_teacher/<int:user_id>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:user_id>/', views.delete_teacher, name='delete_teacher'),

    #manage character cards
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),

    #for editing character cards
    path('teachercards/<int:cardid>/', views.edit_tcards, name='edit_tcards'), #teachercards.html
    path('update_tcards/<int:cardid>/', views.update_tcards, name='update_tcards'), #teachercards.html
    path('managequiz/', views.managequiz, name='managequiz'), 

   
    #character cards
    path('teachermenu/', views.teachermenu, name='teachermenu'),
    path('quiz/', views.quiz, name='quiz'),
    path('select_card/', views.select_card, name='select_card'),
]
