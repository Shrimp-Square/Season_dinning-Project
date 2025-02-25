from django.shortcuts import render, redirect

def index(request):
    # 로그인 되어있든, 안되어있든 index.html 보여줌 (인덱스페이지에 로그인 버튼이 있으므로)
    # 후에 기능 개발하다가 변경, 추가 사항있으면 그때 변경~
    return render(request, "index.html")

