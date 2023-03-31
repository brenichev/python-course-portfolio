from django.db import models
from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель автора блога.
    """

    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя",
        help_text="Имя",
    )

    last_name = models.CharField(
        max_length=30,
        verbose_name="Фамилия",
        help_text="Фамилия",
    )

    about = models.CharField(
        max_length=255,
        verbose_name="Обо мне",
        help_text="Обо мне",
    )

    email = models.EmailField(
        max_length=50,
        verbose_name="Email",
        help_text="Адрес электронной почты",
    )

    github_link = models.URLField(
        blank=True,
        verbose_name="GitHub",
        help_text="Ссылка на GitHub",
    )

    resume_link = models.URLField(
        blank=True,
        verbose_name="Резюме",
        help_text="Ссылка на резюме",
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'

    def fullname(self) -> str:
        """
        Формирование строки "Имя Фамилия".
        :return:
        """
        return self.first_name + " " + self.last_name
