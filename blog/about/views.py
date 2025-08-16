from django.shortcuts import render


def about(request):
    context = {
        'author_info': "Это Космос и его верный раб",
    }
    return render(request, 'about/about.html', context)


def technology(request):
    tech_stack = [
        "Python",
        "Django",
        "SQLite",
        "HTML",
        "CSS"
    ]
    context = {
        'technologies': tech_stack,
    }
    return render(request, 'about/tech.html', context)
