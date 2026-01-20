from django.shortcuts import render,redirect
from articleapp.models import ArticleModel

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def form_view(request):
    submitted = False
    if request.method == 'POST':
        title = request.POST.get('title')
        description=request.POST.get('Description')
        author=request.POST.get('author')
        date=request.POST.get('date')
        ArticleModel.objects.create(title=title,description=description,author=author,date=date)
        submitted = True
    return render(request,'form.html',{'submitted':submitted})

from django.db.models import Q
def all_articles(request):
    all_data = ArticleModel.objects.all()
    query = request.GET.get('q')

    if query:
        all_data = all_data.filter(
            Q(title__icontains = query) |
            Q(description__icontains = query) |
            Q(author__icontains = query)
        )
    print(query)
    return render(request,'all_articles.html',{"all_data":all_data})





def spec_article_view(request, id):
    data = ArticleModel.objects.get(id = id)
    return render(request,'spec_art.html',{'data':data})

def delete_article(request,id):
    article = ArticleModel.objects.get(id = id)
    if request.method=='POST':
     article.delete()
     return redirect("all_articles")
    return render(request,'delete_article.html',)

def update_view(request,id):
    data = ArticleModel.objects.get(id = id)
    context = {'data':data}
    if request.method == 'POST':
        data.title = request.POST.get('title')
        data.author = request.POST.get('author')
        data.description = request.POST.get('Description')
        data.date = request.POST.get('date')
        data.save()
        return redirect("spec_art",id = data.id)
   
    return render (request,'update.html',context)



def delete_all(request):
    if request.method == 'POST':
        ArticleModel.objects.all().delete()
        return redirect("home")
    return render(request,"delete_article.html")




    
