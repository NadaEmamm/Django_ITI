from django.shortcuts import render,get_object_or_404
from .models import Author, Post
# posts = [
#     {
#         'id': 1,
#         'title': 'The Power of Habit: How Small Changes Make a Big Impact',
#         'content': 'Discover how forming small, consistent habits can lead to massive personal and professional growth. Based on behavioral psychology and real-life examples, this post explores the science behind habit formation.',
#         'image': 'posts/images/img1.jpeg'
#     },
#     {
#         'id': 2,
#         'title': 'AI in 2025: What to Expect from the Future of Technology',
#         'content': 'Artificial intelligence is evolving fast. In this article, we dive into the upcoming trends, ethical debates, and real-world applications of AI that will shape our world in 2025 and beyond.',
#         'image': 'posts/images/img2.jpeg'
#     },
#     {
#         'id': 3,
#         'title': '10 Must-Visit Hidden Gems in Europe',
#         'content': 'Tired of crowded tourist spots? This travel guide lists 10 breathtaking, lesser-known destinations across Europe that offer rich culture, scenic beauty, and unforgettable experiences.',
#         'image': 'posts/images/img3.jpeg'
#     }
# ]

def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", context = {
      'posts': posts,  
    })

def post_detail(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = author.posts.all()
    return render(request, 'posts/author_detail.html', {'author': author, 'posts': posts})