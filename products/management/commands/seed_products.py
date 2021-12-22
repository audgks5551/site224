from random import random
from django.core.management.base import BaseCommand
import markets
from products.models import Product, ProductReal
from markets.models import Market
import random


class Command(BaseCommand):

    help = '가짜 제품을 생성합니다.'

    # python manage.py 'seed_products' 추가
    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=1, type=int, help="생성하고 싶은 가짜 제품의 개수를 입력하세요"
        )

    # python manage.py seed_products를 실행하였을 때의 내용
    def handle(self, *args, **options):
        product_count = Product.objects.count()
        market_count = Market.objects.count()
        number = options.get('number') + product_count + 1

        for num in range(product_count+1, number):
            product = Product(market_id=random.randrange(1, market_count), name=f"티셔츠{num}",
                              display_name=f"인스타여신티셔츠{num}", price=random.randrange(40000, 50000), sale_price=random.randrange(20000, 39000))
            product.save()
            lastProduct = Product.objects.last()
            ProductReal(product=lastProduct, option_1_name="44", option_1_display_name="44", option_2_name="RED",
                        option_2_display_name="감성레드").save()
            ProductReal(product=lastProduct, option_1_name="55", option_1_display_name="55", option_2_name="RED",
                        option_2_display_name="감성레드").save()
            ProductReal(product=lastProduct, option_1_name="66", option_1_display_name="66", option_2_name="RED",
                        option_2_display_name="감성레드").save()
            ProductReal(product=lastProduct, option_1_name="44", option_1_display_name="44", option_2_name="BLUE",
                        option_2_display_name="감성블루").save()
            ProductReal(product=lastProduct, option_1_name="55", option_1_display_name="55", option_2_name="BLUE",
                        option_2_display_name="감성블루").save()
            ProductReal(product=lastProduct, option_1_name="66", option_1_display_name="66", option_2_name="BLUE",
                        option_2_display_name="감성블루").save()
        self.stdout.write(self.style.SUCCESS("가짜 데이터 생성!!"))
