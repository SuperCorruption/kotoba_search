from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    html = models.TextField(blank=True, null=True)
    work_title = models.CharField(max_length=255, choices=[
        ("紅魔郷", "紅魔郷"), ("妖々夢", "妖々夢"), ("萃夢想", "萃夢想"),
        ("永夜抄", "永夜抄"), ("花映塚", "花映塚"), ("文花帖(ゲーム)", "文花帖(ゲーム)"),
        ("風神録", "風神録"), ("地霊殿", "地霊殿"), ("緋想天", "緋想天"),
        ("星蓮船", "星蓮船"), ("非想天則", "非想天則"), ("ダブルスポイラー", "ダブルスポイラー"),
        ("妖精大戦争", "妖精大戦争"), ("神霊廟", "神霊廟"), ("心綺楼", "心綺楼"),
        ("輝針城", "輝針城"), ("深秘録", "深秘録"), ("弾幕アマノジャク", "弾幕アマノジャク"),
        ("紺珠伝", "紺珠伝"), ("憑依華", "憑依華"), ("天空璋", "天空璋"),
        ("秘封ナイトメアダイアリー", "秘封ナイトメアダイアリー"), ("鬼形獣", "鬼形獣"), ("強欲異聞", "強欲異聞"),
        ("虹龍洞", "虹龍洞"), ("バレットフィリア達の闇市場", "バレットフィリア達の闇市場"), ("獣王園", "獣王園"),
        ("香霖堂(第一期)", "香霖堂(第一期)"), ("香霖堂(第二期)", "香霖堂(第二期)"),
        ("三月精_~_Eastern_and_Little_Nature_Deity", "三月精_~_Eastern_and_Little_Nature_Deity"),
        ("三月精_~_Strange_and_Bright_Nature_Deity", "三月精_~_Strange_and_Bright_Nature_Deity"),
        ("三月精_~_Oriental_Sacred_Place", "三月精_~_Oriental_Sacred_Place"),
        ("三月精_~_Visionary_Fairies_in_Shrine.", "三月精_~_Visionary_Fairies_in_Shrine."),
        ("儚月抄(マンガ)", "儚月抄(マンガ)"), ("儚月抄(小説)", "儚月抄(小説)"), ("茨歌仙", "茨歌仙"),
        ("鈴奈庵", "鈴奈庵"), ("智霊奇殿", "智霊奇殿"), ("酔蝶華", "酔蝶華"), ("文花帖(書籍)", "文花帖(書籍)"),
        ("求聞史紀", "求聞史紀"), ("グリモワールオブマリサ", "グリモワールオブマリサ"), ("求聞口授", "求聞口授"),
        ("文果真報", "文果真報"), ("グリモワールオブウサミ", "グリモワールオブウサミ"), ("紫香花", "紫香花"),
        ("外来韋編_壱", "外来韋編_壱"), ("外来韋編_弐", "外来韋編_弐"), ("外来韋編_参", "外来韋編_参"),
        ("外来韋編_肆", "外来韋編_肆"), ("外来韋編_2018_春", "外来韋編_2018_春"),
        ("外来韋編_2018_秋", "外来韋編_2018_秋"), ("外来韋編_2019_春", "外来韋編_2019_春"),
        ("外来韋編_2019_秋", "外来韋編_2019_秋"), ("外来韋編_2021_春", "外来韋編_2021_春"),
        ("外来韋編_2024", "外来韋編_2024"),
        ("人妖名鑑_常闇編", "人妖名鑑_常闇編"), ("人妖名鑑_常世編", "人妖名鑑_常世編"),
        ("蓬莱人形", "蓬莱人形"), ("蓮台野夜行", "蓮台野夜行"), ("夢違科学世紀", "夢違科学世紀"),
        ("卯酉東海道", "卯酉東海道"), ("大空魔術", "大空魔術"), ("未知の花_魅知の旅", "未知の花_魅知の旅"),
        ("鳥船遺跡", "鳥船遺跡"), ("伊弉諾物質", "伊弉諾物質"), ("燕石博物誌", "燕石博物誌"),
        ("旧約酒場", "旧約酒場"), ("虹色のセプテントリオン", "虹色のセプテントリオン"), ("幺樂団の歴史", "幺樂団の歴史"),("東方幻存神籤","東方幻存神籤"),
        ]
    )
    volume = models.IntegerField(null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True)
    subtitle = models.CharField(max_length=255,null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
