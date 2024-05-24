from django.db import models

NULLABLE = {"blank": True, "null": True}


class Edit(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name="заголовок",
        help_text="введите заголовок",
    )
    content = models.TextField(
        verbose_name="содержимое статьи",
        help_text="введите содержимое статьи",
    )
    image = models.ImageField(
        upload_to="blog_entries",
        verbose_name="изображение",
        help_text="загрузите изображение",
        **NULLABLE,
    )
    created_at = models.DateField(
        verbose_name="дата создания",
        help_text="заполните дату создания",
        **NULLABLE,
    )
    is_published = models.BooleanField(
        default=False,
    )
    slug = models.CharField(
        max_length=150,
        verbose_name='slug',
        **NULLABLE,
    )
    count_of_views = models.IntegerField(
        verbose_name="количество просмотров",
        help_text="отображается количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "записи блога"
        verbose_name_plural = "записи блога"
        ordering = ['created_at']

    def __str__(self):
        return (
            f"{self.title} {self.created_at} {self.content}"
        )
