from django.db import models

# Create your models here.

class Market(models.Model):
    
    market_id = models.CharField(max_length= 32, primary_key= True, verbose_name='사업자등록번호') 
    market_name = models.CharField(max_length=32, verbose_name= '상호명') 
    address = models.CharField(max_length= 128, verbose_name= '주소') 
    call_number = models.CharField(max_length=15, verbose_name= '전화번호') 
    content = models.TextField(verbose_name= '내용')  
    tags = models.ManyToManyField("markets.HashTag", max_length= 50, blank= True, verbose_name= '해시태그 목록') 
    festival_id = models.ForeignKey("markets.Festival_id", verbose_name= '축제ID', on_delete= models.CASCADE),
    thumbnail = models.ImageField("썸네일 이미지", upload_to = "post", blank = True)

# class Markets(models.Model):
#    pass

class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50)

class Festival_id(models.Model):
    name = models.CharField("축제ID", max_length= 50)

class MarketImage(models.Model):
    post = models.ForeignKey(Market,
                             verbose_name = "이미지",
                             on_delete = models.CASCADE)
    photo = models.ImageField("사진", upload_to = "post")

    def __str__(self):
        return self.name
    