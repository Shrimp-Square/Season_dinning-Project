from django.db import models

# Create your models here.

class Market(models.Model):
    
    market_id = models.CharField(max_length= 32, primary_key= True, verbose_name='가게ID') # type: ignore
    market_name = models.CharField(max_length=32, verbose_name= '상호명') # type: ignore
    address = models.CharField(max_length= 128, verbose_name= '주소') # type: ignore
    call_number = models.CharField(max_length=15, verbose_name= '전화번호') # type: ignore
    content = models.TextField(verbose_name= '내용')  # type: ignore
    tags = models.ForeignKey("markets.HashTag", max_length= 50, blank= True, verbose_name= '해시태그 목록', on_delete= models.CASCADE) # type: ignore
    festival_id = models.ForeignKey("markets.Festival_id", verbose_name= '축제ID', on_delete= models.CASCADE) # type: ignore

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
    