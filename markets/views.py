from django.shortcuts import render, redirect
from markets.models import Market,Comment
from markets.forms import MarketForm

# Create your views here.
def market_list(request):
    markets = Market.objects.all()

    # 템플릿에 전달할 딕셔너리
    context = {
        "markets" : markets,
    }
    return render(request, "markets/market_list.html", context)

def market_add(request):
    if request.method == "POST":

        form = MarketForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "markets/market_list.html")
    else:
        form = MarketForm()
        context = {"form": form}

    return render(request, "markets/market_add.html", context)


def tags(request, tag_name):
    return render(request, "markets/markets/tags.html")

def market_detail(request, id):
    post = Market.objects.get(pk = id)
    
    if request.method == "POST":
        comment_content = request.POST["comment"]
        
        Comment.objects.create(
            content = comment_content,
        )
    context = {
        'content' : comment_content
    }
    return render(request, "markets/market_detail.html", context)

