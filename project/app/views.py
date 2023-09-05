from django.http import JsonResponse
from .models import Post
from .services import generate_post_content


def generate_post(request):
    title = "Post del Giorno"
    content = generate_post_content("Scrivi un articolo sulle ultime tendenze della tecnologia.")
    post = Post(title=title, content=content)
    post.save()
    return JsonResponse({"status": "success", "title": title, "content": content})
