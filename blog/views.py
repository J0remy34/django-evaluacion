from django.shortcuts import render


def inicio_blog(request):
    publicaciones = [
        {
            "titulo": "Aprendiendo Django",
            "autor": "Estudiante",
            "contenido": "Django permite desarrollar aplicaciones web utilizando Python."
        },
        {
            "titulo": "Git y GitHub",
            "autor": "Estudiante",
            "contenido": "Git permite administrar las diferentes versiones de un proyecto."
        },
    ]

    return render(request, "blog/inicio.html", {
        "publicaciones": publicaciones
    })


def sobre_blog(request):
    return render(request, "blog/sobre.html")
