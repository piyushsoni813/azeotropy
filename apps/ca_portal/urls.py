from django.urls import path

from . import views

app_name = "registration_ca"



urlpatterns = [
    path('',views.Index, name = 'main_website'),
    path('schedule',views.Schedule, name = 'schedule'),
    path('competitions',views.Competition, name = 'competition'),
    path('events',views.Events, name = 'events'),
    path('about_us',views.About_us, name = 'about_us'),
    path('sponsors',views.Sponsors, name = 'sponsors'),
    path('workshop',views.Workshop, name = 'workshop'),
    path('ca/',views.Registration,name='index'),
    path('register', views.user_register, name = "register"),
    path('azeo_id',views.AZeo_id, name='azeo_id'),
    path('competitions/chem-o-philia', views.Chem_o_philia, name ='chem-o-philia'),
    path('competitions/chem-e-cross', views.Chem_e_cross, name ='chem-e-cross'),
    path('competitions/optimiser', views.Optimiser, name ='optimiser'),
    path('competitions/q-viz-it', views.Q_viz_it, name ='q-viz-it'),
    path('competitions/IDP', views.IDP, name ='IDP'),
    path('events/luminescence', views.Luminescence, name ='luminescence'),
    path('events/workshop', views.workshop, name ='workshop'),
    path('events/impact', views.Impact, name ='impact'),
    path('events/ansys', views.Ansys, name ='ansys'),
    path('events/r_workshop', views.R_workshop, name ='r_workshop'),
    path('competitions/chemathon/', views.Chemathon, name ='chemathon'),
    path('competitions/cipher/', views.Cipher, name ='cipher'),
    path('competitions/lca/', views.Lca, name ='lca'),
    path('events/panel_discussion', views.Paneldiscussion, name ='panel-discussion'),
    path('events/matlab', views.Matlab, name ='matlab'),
]


