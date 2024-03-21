from django.shortcuts import render

from produk.models import GambarProduk, Produk
from profiles.models import LangSupport

from .base_view import FrontPage


class Detail(FrontPage):
    def get(self, request, slug):
        produk = Produk.objects.get(slug=slug)
        languages = LangSupport.objects.filter(is_active=True)
        gambar = None
        try:
            gambar = GambarProduk.objects.filter(produk_id=produk.id)
        except Exception as e:
            print(e)
        return render(
            request,
            "home/detail.html",
            {"slug": slug, "produk": produk, "gambar": gambar, "languages": languages},
        )
