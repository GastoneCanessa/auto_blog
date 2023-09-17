from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .services import generate_post_content
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.core.cache import cache
from datetime import datetime, date
from celery import shared_task


def generate_post(request):
    # # Controlla l'ultima data di accesso dal cache
    # last_accessed = cache.get('last_accessed_date')

    # # Se la view è stata già acceduta oggi, rifiuta l'accesso
    # if last_accessed == date.today():
    #     return HttpResponse("Questa funzione può essere chiamata solo una volta al giorno.")

    # # Altrimenti, aggiorna la data di accesso nel cache
    # cache.set('last_accessed_date', date.today())

    title = "Post del Giorno"
    content = generate_post_content("Scrivi un articolo sulle ultime tendenze della tecnologia.")
    post = Post(title=title, content=content)
    post.save()
    # return JsonResponse({"status": "success", "title": title, "content": content})
    return HttpResponseRedirect('/blog/')


@shared_task
def call_my_view_task():
    request = HttpRequest()
    request.method = 'POST'
    response = generate_post(request)
    return response


def post_list(request):
    last_accessed = cache.get('last_accessed_date')
    show_button = last_accessed != date.today()
    posts = Post.objects.all().order_by('-date_created')
    context = {
        'show_button': show_button,
        'posts': posts
    }
    return render(request, 'post_list.html', context)