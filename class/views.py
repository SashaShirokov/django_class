from django.shortcuts import render

posts = [
    {
        'author': 'Shirokov',
        'title': 'Swift method',
        'content': 'Nullam maximus tellus vel dapibus iaculis. Aenean feugiat libero nec ipsum venenatis elementum. Integer at dapibus massa. Morbi non auctor sapien. In turpis nisl, volutpat in cursus quis, pretium sed nibh. Nulla ornare, quam et varius dictum, est ligula ornare neque, et hendrerit lacus est eu mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin aliquet ',
        'date_posted': 'April 22, 2019'
    },
    {
        'author': 'Smith',
        'title': 'Smooth method',
        'content': 'Nullam maximus tellus vel dapibus iaculis. Aenean feugiat libero nec ipsum venenatis elementum. Integer at dapibus massa. Morbi non auctor sapien. In turpis nisl, volutpat in cursus quis, pretium sed nibh. Nulla ornare, quam et varius dictum, est ligula ornare neque, et hendrerit lacus est eu mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin aliquet ',
        'date_posted': 'April 23, 2019'
    }
]


def home(request):
    return render(request, 'class/home.html')


def about(request):
    return render(request, 'class/about.html', {'title': 'About'})


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'class/blog.html', context)
