from django.shortcuts import render
from .models import location,category,Image
from django.http  import HttpResponse
# Create your views her
def main(request):
    return render(request,'index.html')

def search_results(request):
    if  'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories =category.search_by_name(search_term)
        message = f"{search_term}"
        
        return render (request,'search.html',{"message":message,"category":searched_categories})

    else:
        message = "You haven't searched for any term" 
        return render(request,'search.html',{"message":message})   