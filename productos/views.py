from django.shortcuts import render


def lista_productos(request):
    productos = [
        {
            "nombre": "Notebook",
            "precio": 599990,
            "categoria": "Tecnología"
        },
        {
            "nombre": "Mouse inalámbrico",
            "precio": 19990,
            "categoria": "Accesorios"
        },
        {
            "nombre": "Teclado mecánico",
            "precio": 49990,
            "categoria": "Accesorios"
        },
    ]

    return render(request, "productos/lista.html", {
        "productos": productos
    })


def informacion_productos(request):
    return render(request, "productos/informacion.html")
