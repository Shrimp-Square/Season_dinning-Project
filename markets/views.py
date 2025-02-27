from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from markets.models import Market,Comment,HashTag,MarketImage,Festival
from markets.forms import MarketForm, CommentForm

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
            
            for image_file in request.FILES.getlist("images"):
                MarketImage.objects.create(
                    post = market, 
                    photo = image_file,
                )
            # 'tags'에 전달된 문자열을 분리해 HashTag 생성
            tag_string = request.POST.get("tags")
            if tag_string:
                tag_name_list = [tag_name.strip() for tag_name in tag_string.split(",")]
                for tag_name in tag_name_list:
                    tag, _ = HashTag.objects.get_or_create(
                        name = tag_name,
                    )
                    # get_or_create로 생성하거나 가져온 HashTag 객체를 Post의 tags에 추가
                    market.tags.add(tag)

            return redirect("/markets/")
    else:
        form = MarketForm()

    context = {
            'form' : form
        }
    return render(request, "markets/market_add.html", context)

def nearby_tag_markets(request, tag_id, festival_id): # 해시태그를 통해 축제인근 가게를 검색
    try:
        tag = HashTag.objects.get(id = tag_id)
        festival = Festival.objects.get(id = festival_id)
    except HashTag.DoesNotExist:
        tag_markets = Market.objects.none()

    nearby_markets = festival.markets.all()
    tag_markets = nearby_markets.filter(tags=tag)

    context = { "festival" : festival, "tag" : tag, "tag_markets" : tag_markets}

    return render(request, "tag_search_list.html", context)

def comment_add(request, market_id):
    if request.method == "POST":
        form = CommentForm(data = request.POST)    
        print(request.POST)
        print(form)
        if form.is_valid():
            print("is_valid 이후")
            comment = form.save(commit = False)
            comment.user = request.user
            comment.save()            

            if request.GET.get("next"):
                url_next = request.GET.get("next")
            else:
                url_next = request.GET.get("next") or reverse("markets:market_detail", kwargs={"market_id": market_id})
            return redirect(url_next)

    # return redirect(url)
    return redirect(f"/markets/{market_id}/")
    

def market_detail(request, market_id):
    market = Market.objects.get(id = market_id)
    comment_form = CommentForm()
    context = {
        "market" : market,
        "comment_form" : comment_form,
        "market_id" : market_id,
    }
    return render(request,"markets/market_detail.html", context)

def market_like(request, market_id):
    market = Market.objects.get(id = market_id)
    user = request.user
    
    if user.like_markets.filter(id = market_id).exists():
        user.like_markets.remove(market)
    else:
        user.like_markets.add(market)
        
    url_next = request.GET.get("next") or reverse("markets:market_detail", kwargs={"market_id": market_id})
    
    return redirect(url_next)

def market_edit(request, market_id):
    market = get_object_or_404(Market, pk=market_id)

    if request.method =="POST":
        form = MarketForm(request.POST, instance = market)
        if form.is_valid():
            market.user = request.user
            market.save()
            return redirect("market_list")
    else:
        form = MarketForm(instance = market)
        
        context = {
            "form" : form
        }
        
        return render(request, "markets/add.html", context)