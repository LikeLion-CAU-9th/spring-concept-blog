from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post


def home(request):
    return render(request, 'home.html')


def my_post(request):
    post_list = Post.objects.all()
    return render(request, 'myPost.html', {"post_list" : post_list})


def new_post(request):
    if request.method == 'POST':
        if request.FILES.get('image'):
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
            )
            print("b")
        post_list = Post.objects.all()
        return render(request, 'myPost.html', {"post_list" : post_list})
    print("a")
    return redirect('/')


def post_detail(request, pk):
    post = get_object_or_404(Post, id = pk)
    return render(request, 'postDetail.html', {"post": post})


def post_update(request, pk):
    post = Post.objects.get(id = pk)

    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('/post/'+str(post.id))
    else:
        return render(request, 'editPost.html', {"post": post})


def post_delete(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect('/my-post')


def funcname(self, parameter_list):
    try:
        Post.objects.filter(parameter_list)
    raise NotImplementedError

