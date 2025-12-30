from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.tags = request.POST["tags"]
        post.save()
        return redirect("post_list")

    return render(request, "blog/post_edit.html", {
        "post": post
    })

def ai_home(request):
    posts = Post.objects.filter(tags__icontains="ai").order_by("-created_at")
    return render(request, "ai/ai_home.html", {"posts": posts})

def study_home(request):
    posts = Post.objects.filter(tags__icontains="study").order_by("-created_at")
    return render(request, "study/study_home.html", {"posts": posts})

def projects_home(request):
    posts = Post.objects.filter(tags__icontains="projects").order_by("-created_at")
    return render(request, "projects/projects_home.html", {"posts": posts})


