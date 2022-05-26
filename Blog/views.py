from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForms


class HomeView(View):
    def get(self, request):
        post = Post.objects.all()
        form = PostForms()
        context = {
            'posts': post,
            'forms': form
            }
        return render(request, 'blog/home.html', context)

    def post(self, request):

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # im = request.POST.get('image')
        # rasm = im.split("/photo/")
        # a = Post.objects.create(
        #     title=title,
        #     content=content,
        #     image=im,
        #     author=request.user
        # )

        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            img_object = form.instance
            img_object.author = request.user
            img_object.save()

            # Getting the current instance object to display in the template

            # return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})
            print(img_object)
        return redirect('home-page')


def PostView(request, pk):
    post = Post.objects.get(id=pk)
    # form = PostForms()
    # print(pk)
    return render(request, 'blog/post-view.html', {"post":post})
