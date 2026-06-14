from django.contrib import admin
from .models import 使用者, 產品, 訂單

@admin.register(使用者)
class 使用者Admin(admin.ModelAdmin):
    list_display = ['姓名', '電郵', '電話', '建立時間']
    search_fields = ['姓名', '電郵']

@admin.register(產品)
class 產品Admin(admin.ModelAdmin):
    list_display = ['產品名稱', '價格', '庫存']
    search_fields = ['產品名稱']

@admin.register(訂單)
class 訂單Admin(admin.ModelAdmin):
    list_display = ['購買者', '產品', '數量', '訂單時間']