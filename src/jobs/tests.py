from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций работы.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.
        :return:
        """

        Job.objects.create(
            description="description",
            content="content" * 100,
            image="Job №1 image path",
        )

    def test_blog_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для работы.
        :return:
        """

        job = Job.objects.get(description="description")

        content = "content" * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
