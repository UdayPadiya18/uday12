from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Home, name='home'),
    path('gallery/', views.GalleryView, name='gallery'),
    path('about/', views.AboutView, name='about'),
    path('festival/', views.FestivalView, name='festival'),
    path('facilities/', views.FacilitiesView, name='facilities'),
    path('academic/', views.AcademicView, name='academic'),
    path('techno/', views.TechnoView, name='techno'),
    path('science/', views.ScienceView, name='science'),
    path('health/', views.HealthView, name='health'),
    path('nursing/', views.NursingView, name='nursing'),
    path('humanity/', views.HumanityView, name='humanity'),
    path('commerce/', views.CommerceView, name='commerce'),
    path('kset/', views.kset, name='kset'),
    path('ksds/', views.ksds, name='ksds'),
    path('kss/', views.kss, name='kss'),
    path('ksp/', views.ksp, name='ksp'),
    path('kst/', views.kst, name='kst'),
    path('kamc/', views.kamc, name='kamc'),
    path('kspr/', views.kspr, name='kspr'),
    path('ksn/', views.ksn, name='ksn'),
    path('ksc/', views.ksc, name='ksc'),
    path('ksbm/', views.ksbm, name='ksbm'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    
]