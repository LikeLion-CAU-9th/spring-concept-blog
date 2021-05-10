from django.shortcuts import render, redirect
from blog.models import Post


def home(request):
    return render(request, 'home.html')


def my_post(request):
    post_list = Post.objects.all()
    return render(request, 'myPost.html', {"post_list" : post_list})

def new_post(request):
    if request.method == 'POST':
        if request.FILES['image']:
            print(request.FILES)
            a = Post.objects.create(
                title=request.POST['title'],
                body=request.POST['body'],
                image=request.FILES['image'],
            )
            print(a.title)

        else:
            new_article=Post.objects.create(
                title=request.POST['title'],
                body=request.POST['body'],
                image=request.FILES['post-image']
            )
            print("b")
        post_list = Post.objects.all()
        return render(request, 'myPost.html', {"post_list" : post_list})
    print("a")
    return redirect('/')
