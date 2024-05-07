from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=128,
        verbose_name="наименование категории",
        help_text="введите наименование категории",
    )
    category_description = models.CharField(
        max_length=256,
        verbose_name="описание категории",
        help_text="введите описание категории",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]

    def __str__(self):
        return f"{self.category_name} {self.category_description}"


class Product(models.Model):
    product_name = models.CharField(
        max_length=128,
        verbose_name="наименование продукта",
        help_text="введите наименование продукта",
    )
    product_description = models.CharField(
        max_length=256,
        verbose_name="описание продукта",
        help_text="введите описание продукта",
    )
    product_image = models.ImageField(
        upload_to="products/images/",
        verbose_name="изображение",
        help_text="загрузите изображение продукта",
        **NULLABLE,
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="категория продукта",
        help_text="введите категорию продукта",
        related_name="products",
        **NULLABLE,
    )
    product_created_at = models.DateField(
        verbose_name="дата создания", help_text="заполните дату создания", **NULLABLE
    )
    product_updated_at = models.DateField(
        verbose_name="дата последнего изменения",
        help_text="заполните дату изменения",
        **NULLABLE,
    )
    product_pay_for_sail = models.CharField(
        max_length=128,
        verbose_name="стоимость покупки",
        help_text="введите стоимость покупки",
    )
    manufactured_at = models.DateField(
        verbose_name="дата производства продукта",
        help_text="заполните дату производства продукта",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]

    def __str__(self):
        return (
            f"{self.product_name} {self.product_description} {self.product_category} {self.product_pay_for_sail} "
            f"{self.product_created_at} {self.product_updated_at} {self.product_image}"
        )

