from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Pablo A. Roufogalis"
    context = { "title" : title}
    return render(request, "portfolio/en/home.html", context)

def about_me(request):
    title = "About Me"
    context = {"title" : title}
    return render(request, "portfolio/en/about-me.html", context)

def certificates(request):
    title = "Certificates"
    context = {"title" : title}
    return render(request, "portfolio/en/certificates.html", context)

def projects(request):
    title = "Projects"
    context = {"title" : title}
    return render(request, "portfolio/en/projects.html", context)

#def contact_me(request):
#    title = "Contact Me"
#    context = {"title" : title}
#    return render(request, "portfolio/en/contact-me.html", context)

#Spanish
def es_home(request):
    title = "Pablo A. Roufogalis"
    context = {"title" : title}
    return render(request, "portfolio/es/es-home.html", context)

def sobre_mi(request):
    title = "Sobre Mi"
    context = {"title" : title}
    return render(request, "portfolio/es/sobre-mi.html", context)

def certificados(request):
    title = "Certificados"
    context = {"title" : title}
    return render(request, "portfolio/es/certificados.html", context)

def proyectos(request):
    title = "Proyectos"
    context = {"title" : title}
    return render(request, "portfolio/es/proyectos.html", context)

#def contactame(request):
#    title = "Contáctame"
#    context = {"title" : title}
#    return render(request, "portfolio/es/contactame.html", context)

def primer_dan_indice(request):
    title = "Proyecto 1er Dan"
    context = {"title" : title}
    return render(request, "portfolio/es/1er/index.html", context)

def primer_dan_resumen(request):
    return render(request, "portfolio/es/1er/resumen.html")

def segundo_dan_indice(request):
    title = "Proyecto 2do Dan"
    context = {"title" : title}
    return render(request, "portfolio/es/2do/index.html", context)

def segundo_dan_agradecimientos(request):
    title = "Agradecimientos"
    context = {"title" : title}
    return render(request, "portfolio/es/2do/agradecimientos.html", context)

def segundo_dan_conclusiones(request):
    title = "Conclusiones"
    context = {"title" : title}
    return render(request, "portfolio/es/2do/conclusiones.html", context)

def segundo_dan_diagramas(request):
    title = "Diagramas"
    context = {"title" : title}
    return render(request, "portfolio/es/2do/diagramas.html", context)

def segundo_dan_intro(request):
    title = "Introducción"
    context = {"title" : title}
    return render(request, "portfolio/es/2do/intro.html", context)

def segundo_dan_tabla(request):
    title = "Tabla"
    context = {"title" : title}
    return render(request, "portfolio/es/2do/tabla.html", context)

def sutta_indice(request):
    title = "Sutta Pitaka"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/index.html", context)

def sutta_anguttara(request):
    title = "Anguttara Nikaya"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/anguttara.html", context)

def sutta_antecedentes(request):
    title = "Antecedentes"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/antecedentes.html", context)

def sutta_bibliografia(request):
    title = "Bibliografía"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/bibliografia.html", context)

def sutta_conclusiones(request):
    title = "Conclusiones"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/conclusiones.html", context)

def sutta_intro(request):
    title = "Introducción"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/intro.html", context)

def sutta_khuddaka(request):
    title = "Khuddaka Nikaya"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/khuddaka.html", context)

def sutta_marco(request):
    title = "Marco Teórico"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/marco-teorico.html", context)

def sutta_samyutta(request):
    title = "Samyutta Nikaya"
    context = {"title" : title}
    return render(request, "portfolio/es/sutta/samyutta.html", context)
