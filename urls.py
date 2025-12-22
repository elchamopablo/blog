from django.urls import path, reverse_lazy
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name = "home"),
    path("about-me", views.about_me, name = "about-me"),
    path("certificates", views.certificates, name = "certificates"),
    path("projects", views.projects, name = "projects"),
    #path("contact-me", views.contact_me, name = "contact-me"),
#Spanish
    path("es", views.es_home, name = "es-home"),
    path("es/sobre-mi", views.sobre_mi, name = "sobre-mi"),
    path("es/certificados", views.certificados, name = "certificados"),
    path("es/proyectos", views.proyectos, name = "proyectos"),
    #path("contactame", views., name = "contactame"),
    path("es/proyectos/1er", views.primer_dan_indice, name = "1er-dan-indice"),
    path("es/proyectos/1er/resumen", views.primer_dan_resumen, name = "1er-dan-resumen"),
    path("es/proyectos/2do", views.segundo_dan_indice, name = "2do-dan-indice"),
    path("es/proyectos/2do/agradecimientos", views.segundo_dan_agradecimientos, name = "2do-dan-agradecimientos"),
    path("es/proyectos/2do/conclusiones", views.segundo_dan_conclusiones, name = "2do-dan-conclusiones"),
    path("es/proyectos/2do/diagramas", views.segundo_dan_diagramas, name = "2do-dan-diagramas"),
    path("es/proyectos/2do/intro", views.segundo_dan_intro, name = "2do-dan-intro"),
    path("es/proyectos/2do/tabla", views.segundo_dan_tabla, name = "2do-dan-tabla"),
    path("es/proyectos/sutta", views.sutta_indice, name = "sutta-indice"),
    path("es/proyectos/sutta/anguttara", views.sutta_anguttara, name = "sutta-anguttara"),
    path("es/proyectos/sutta/antecedentes", views.sutta_antecedentes, name = "sutta-antecedentes"),
    path("es/proyectos/sutta/bibliografia", views.sutta_bibliografia, name = "sutta-bibliografia"),
    path("es/proyectos/sutta/conclusiones", views.sutta_conclusiones, name = "sutta-conclusiones"),
    path("es/proyectos/sutta/intro", views.sutta_intro, name = "sutta-intro"),
    path("es/proyectos/sutta/khuddaka", views.sutta_khuddaka, name = "sutta-khuddaka"),
    path("es/proyectos/sutta/marco", views.sutta_marco, name = "sutta-marco"),
    path("es/proyectos/sutta/samyutta", views.sutta_samyutta, name = "sutta-samyutta"),
]
