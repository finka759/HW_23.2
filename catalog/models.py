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
        return f"{self.category_name}"


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
        upload_to="products",
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
    product_pay_for_sail = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="стоимость покупки",
        help_text="введите стоимость покупки",
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


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        related_name="version_product",
    )
    version_number = models.PositiveSmallIntegerField(
        verbose_name="номер версии",
        help_text="введите номер версии",
        default=1
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="название версии",
        help_text="введите наименование версии",
        **NULLABLE,
    )
    is_current_version = models.BooleanField(
        default=False,
        verbose_name="актуальность версии",
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ["version_number"]

    def __str__(self):
        return (f"номер верси: {self.version_number},название версии: {self.version_name},"
                f"актуальность версии: {self.is_current_version}, продукт: {self.product}")
