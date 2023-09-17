from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .services import generate_post_content
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.core.cache import cache
from datetime import datetime, date
from celery import shared_task
from django.urls import reverse


def generate_post(request):
    # Controlla l'ultima data di accesso dal cache
    last_accessed = cache.get('last_accessed_date')

    # Se la view è stata già acceduta oggi, rifiuta l'accesso
    if last_accessed == date.today():
        return HttpResponse("Questa funzione può essere chiamata solo una volta al giorno.")

    # Altrimenti, aggiorna la data di accesso nel cache
    cache.set('last_accessed_date', date.today())

    response_content = generate_post_content('Scrivi un articolo su una curiosità in ambito tecnologico in stile divulgativo. deve avere un Titolo: " " e un Contenuto: " "')

    # Dividiamo il testo utilizzando "Titolo:" e "Contenuto:" come indicatori
    parti = response_content.split("Contenuto:")
    titolo_parte = parti[0].split("Titolo:")

    # Estraiamo il titolo e il contenuto
    titolo = titolo_parte[1].strip().strip('"')
    contenuto = parti[1].strip()

    post = Post(title=titolo, content=contenuto)
    post.save()
    # return JsonResponse({"status": "success", "title": title, "content": content})
    return HttpResponseRedirect(reverse('list'))


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