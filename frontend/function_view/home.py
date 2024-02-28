from django.db.models import Avg
from django.shortcuts import render

from produk.models import Kategori, Produk

from ..models import Banner
from .base_view import FrontPage


class Home(FrontPage):
    def get(self, request):
        kategori_param = None
        if request.GET.get("kategori"):
            kategori_param = request.GET.get("kategori")
        kategori = []
        produk = []
        banner = Banner.objects.all()
        try:
            produk = Produk.objects.annotate(count_star=Avg("ulasancart__produk"))
            produk = produk.filter(is_archive=False)
            if kategori_param:
                produk = produk.filter(kategori_id=request.GET.get("kategori"))
            produk = produk.order_by("-pk")
        except Exception as e:
            print(e)
            produk = []

        try:
            kategori = Kategori.objects.all()
        except Exception as e:
            print(e)
            kategori = []

        return render(
            request,
            "home/product.html",
            {
                "produk": produk,
                "kategori": kategori,
                "banner": banner,
                "range_value": range(1, 6),
            },
        )
