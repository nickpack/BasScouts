import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from django.template.context import RequestContext
from scouts.forms import ContactForm
from scouts.models import *
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view_article(request, slug):
    return render_to_response( 'news/article.html' , {
        'post': get_object_or_404(NewsArticle, slug=slug)
    })

def news_index(request):
    news_articles = NewsArticle.objects.all().order_by('-article_date')
    groups = ScoutPack.objects.all()
    categories = NewsCategory.objects.all()
    paginator = Paginator(news_articles, 5)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render_to_response( 'news/index.html' , { 'articles': articles, 'groups': groups, 'categories': categories })

def news_category_index(request, slug):
    category = get_object_or_404(NewsCategory, slug=slug)
    articles = NewsArticle.objects.filter(category=category)
    groups = ScoutPack.objects.all()
    categories = NewsCategory.objects.all()
    return render_to_response( 'news/index.html' , {'articles': articles, 'groups': groups, 'categories': categories})

def news_group_index(request, slug):
    group = get_object_or_404(ScoutPack, slug=slug)
    articles = NewsArticle.objects.filter(group=group)
    groups = ScoutPack.objects.all()
    categories = NewsCategory.objects.all()
    return render_to_response( 'news/index.html' , {'articles': articles, 'groups': groups, 'categories': categories})

def main_index(request):
    news_articles = NewsArticle.objects.all().order_by('-article_date')
    paginator = Paginator(news_articles, 5)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render_to_response( 'index.html' , {'articles': articles})

def faq_index(request):
    faqs = FAQEntry.objects.all()
    return render_to_response( 'faq.html' , {'faqs': faqs})

def group_index(request, group):
    if group is None:
        raise Http404

    if group == 'scouts':
        return render_to_response( 'scouts.html' , {})
    elif group == 'cubs':
        return render_to_response( 'cubs.html' , {})
    elif group == 'beavers':
        return render_to_response( 'beavers.html' , {})
    else:
        raise Http404

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['duncanstockwell@hotmail.co.uk', 'claire@nickpack.com']
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {
        'form': form,
        }, context_instance=RequestContext(request))