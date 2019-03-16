from django.shortcuts import render

movies = [
    {
        "title": "Stranger Things",
        "description" : "Podczas powrotu do domu znika dwunastoletni Will Byers. Zaginięcie chłopca jest początkiem dziwnych i niebezpiecznych wydarzeń trapiących prowincjonalne miasteczko.",
        "image_thumbnail": "https://www.kawerna.pl/wp-content/uploads/2018/02/Stranger_Things_top3.jpg",
        "release_date": "22 marca 2015",
    },
        {
        "title": "Stranger Things",
        "description" : "Podczas powrotu do domu znika dwunastoletni Will Byers. Zaginięcie chłopca jest początkiem dziwnych i niebezpiecznych wydarzeń trapiących prowincjonalne miasteczko.",
        "image_thumbnail": "https://www.kawerna.pl/wp-content/uploads/2018/02/Stranger_Things_top3.jpg",
        "release_date": "22 marca 2015",
    },
        {
        "title": "Stranger Things",
        "description" : "Podczas powrotu do domu znika dwunastoletni Will Byers. Zaginięcie chłopca jest początkiem dziwnych i niebezpiecznych wydarzeń trapiących prowincjonalne miasteczko.",
        "image_thumbnail": "https://www.kawerna.pl/wp-content/uploads/2018/02/Stranger_Things_top3.jpg",
        "release_date": "22 marca 2015",
    }
]

def home(request):
    context = {
        "movies": movies
    }
    return render(request, 'filmweb/home/home.html', context)