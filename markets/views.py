from django.shortcuts import render, redirect
from markets.models import Market,HashTag,MarketImage,Festival
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

        form = MarketForm(request.POST, request.FILES)

        if form.is_valid():
            market = form.save(commit = False)
            market.user = request.user
            market.save()

            return redirect("markets/"+ f"{market.market_id}")
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


def market_detail(request, market_id):
    post = Market.objects.get(pk = market_id)
    context = {
        "post" : post
    }
    return render(request, "markets/market_detail.html", context)



