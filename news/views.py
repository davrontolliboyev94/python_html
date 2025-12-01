from django.shortcuts import render

def news_view(request):
    context = {
        'new': 'Davron'
    }
    return  render(request,'index.html',context)

# Create your views here.
