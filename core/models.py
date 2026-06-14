from django.db import models

class 使用者(models.Model):
    姓名 = models.CharField(max_length=50, verbose_name="姓名")
    電郵 = models.EmailField(unique=True, verbose_name="電郵")
    電話 = models.CharField(max_length=20, blank=True, null=True, verbose_name="電話")
    建立時間 = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    def __str__(self):
        return self.姓名

    class Meta:
        verbose_name = "使用者"
        verbose_name_plural = "使用者"

class 產品(models.Model):
    產品名稱 = models.CharField(max_length=100, verbose_name="產品名稱")
    價格 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="價格")
    庫存 = models.IntegerField(default=0, verbose_name="庫存")
    描述 = models.TextField(blank=True, verbose_name="描述")

    def __str__(self):
        return self.產品名稱

    class Meta:
        verbose_name = "產品"
        verbose_name_plural = "產品"

class 訂單(models.Model):
    購買者 = models.ForeignKey(使用者, on_delete=models.CASCADE, verbose_name="購買者")
    產品 = models.ForeignKey(產品, on_delete=models.CASCADE, verbose_name="產品")
    數量 = models.IntegerField(default=1, verbose_name="數量")
    訂單時間 = models.DateTimeField(auto_now_add=True, verbose_name="訂單時間")

    def __str__(self):
        return f"{self.購買者} - {self.產品}"

    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = "訂單"