from django.shortcuts import render, redirect, get_object_or_404
from markets.models import Market,Comment,HashTag,MarketImage,Festival
from markets.forms import MarketForm
from django.urls import reverse




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
            market = form.save(commit = False)
            market.user = request.user
            market.save()
            return render(request, "markets/market_list.html")
    else:
        form = MarketForm()
        context = {
            'form' : form
        }
    return render(request, "markets/market_add.html", context)

def nearby_tag_markets(request, tag_id, festival_id): # 해시태그를 통해 축제인근 가게를 검색
    tag = HashTag.objects.get(id = tag_id)
    festival = Festival.objects.get(id = festival_id)

    nearby_markets = festival.markets.all()
    tag_markets = nearby_markets.filter(tags=tag)

    context = { "festival" : festival, "tag" : tag, "tag_markets" : tag_markets}

    return render(request, "tag_search_list.html", context)


def market_detail(request, id):
    post = Market.objects.get(pk = id)
    print(post)
    
    if request.method == "POST":
        comment_content = request.POST["comment"]
        
        Comment.objects.create(
            post = post,
            comment_content = comment_content,
        )
    context = {
        'post' : post
    }
    return render(request, "markets/market_detail.html", context)

def market_like(request, market_id):
        market = Market.objects.get(id = market_id)
        user = request.user
        
        if user.like_markets.filter(id = market_id).exists():
            user.like_markets.remove(market)
        else:
            user.like_markets.add(market)
            
        url_next = request.GET.get("next") or reverse("market:detail") + f"market-{market_id}"
        
        return redirect(url_next)
