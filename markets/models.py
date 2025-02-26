from django.db import models

# Create your models here.

class Market(models.Model):
    user = models.ForeignKey("users.User", on_delete = models.CASCADE, related_name = 'markets') # user 모델과 foreign key 연결 
    name = models.CharField(max_length=32, verbose_name= '상호명') 
    address = models.CharField(max_length= 128, verbose_name= '주소') 
    call_number = models.CharField(max_length=15, verbose_name= '전화번호') 
    content = models.TextField(verbose_name= '가게 소개') # 업로드한 사진들(MarketImage)에 대한 소개 
    tags = models.ManyToManyField("markets.HashTag", max_length= 50, blank= True, verbose_name= '해시태그 목록') 
    festival = models.ForeignKey("markets.Festival", on_delete= models.SET_NULL, related_name = 'markets'),

class MarketImage(models.Model):
    post = models.ForeignKey("markets.Market",
                             verbose_name = "이미지",
                             on_delete = models.CASCADE)
    photo = models.ImageField("사진", upload_to = "post")
    

class HashTag(models.Model):
    name = models.CharField(max_length=50, verbose_name="태그명",)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=10, unique=True)

class Festival(models.Model):
    name = models.CharField(max_length= 50, verbose_name = "축제명")
    start_month = models.IntegerField()
    middle_month = models.IntegerField()
    end_month = models.IntegerField()
    location = models.CharField(max_length = 128, verbose_name = '축제위치')
    description = models.TextField(verbose_name = '축제소개')
    festival_thumbnail = models.ImageField(verbose_name= '축제 썸네일', upload_to = "festivals/thumbnail", blank = True)
    season = models.IntegerField()
    region = models.ForeignKey("markets.Region", on_delete = models.SET_NULL, null = True )

    def __str__(self):
        return self.name
    
    def region_from_location(self,location):
        if '서울' in location or '인천' in location  or '경기' in location :
            return Region.objects.get(name="수도권")
        
        elif '충청' in location or '대전' in location or '세종' in location:
            return Region.objects.get(name="충청권")
        
        elif '전라' in location or'광주' in location:
            return Region.objects.get(name="호남권")
        
        elif '강원' in location:
            return Region.objects.get(name="강원권")
        
        elif '경상' in location or '대구' in location or '부산' in location or '울산' in location:
            return Region.objects.get(name="영남권")
        
        elif '제주' in location:
            return Region.objects.get(name="제주권")

class Comment(models.Model):
    user = models.ForeignKey("users.User", verbose_name = "작성자", on_delete = models.CASCADE)
    market =  models.ForeignKey("markets.Market", verbose_name = "가게명", on_delete = models.CASCADE)
    content = models.TextField(verbose_name = "리뷰내용")
    created =  models.DateTimeField(verbose_name="작성일시", auto_now_add = True)