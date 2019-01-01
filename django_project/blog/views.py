from django.shortcuts import render
#from django.http import HttpResponse

# data in ARRAY of DICT
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 1, 2019'
    },
    {
        'author': 'JohnnyB',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 1, 2019'
    },
]

#
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1> Blog About </h1>')
    return render(request, 'blog/about.html', {'title': 'About JOHNNYB'})
