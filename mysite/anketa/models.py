from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Professia(models.Model):
    title = models.TextField(max_length=50, verbose_name="Профессия")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Professia._meta.fields]


class Naviki(models.Model):
    title = models.TextField(max_length=50, verbose_name="Навыки")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Naviki._meta.fields]


class Role(models.Model):
    title = models.TextField(max_length=50, verbose_name="Роль")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Role._meta.fields]


class Polzovatel(models.Model):
    title = models.TextField(max_length=50, verbose_name="ФИО")
    login = models.TextField(max_length=50, verbose_name="Логин")
    password = models.TextField(max_length=50, verbose_name="Пароль")
    email = models.TextField(max_length=50, verbose_name="Электронная почта")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='Роль')

    class Meta:
        ordering = ["-title"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Polzovatel._meta.fields]


class Vopros(models.Model):
    title = models.TextField(max_length=50, verbose_name="Вопрос")
    score = models.IntegerField(default=0, verbose_name="Балл")
    navik1 = models.ForeignKey(Naviki, on_delete=models.CASCADE, related_name='Навык')

    class Meta:
        ordering = ["-title"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Vopros._meta.fields]


class Otvet(models.Model):
    title = models.ForeignKey(Polzovatel, on_delete=models.CASCADE, related_name='Пользователь')
    navik2 = models.ForeignKey(Naviki, on_delete=models.CASCADE, related_name='Навык')
    score = models.IntegerField(default=0, verbose_name="Балл")
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-title"]
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Otvet._meta.fields]


class ModelProf(models.Model):
    title = models.ForeignKey(Professia, on_delete=models.CASCADE, related_name='Профессия')
    navik3 = models.ForeignKey(Naviki, on_delete=models.CASCADE, related_name='Навык')
    score = models.IntegerField(default=0, verbose_name="Количество баллов")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Модельная профессия"
        verbose_name_plural = "Модельные профессии"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ModelProf._meta.fields]


class EmptyCert(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    pathtofull = models.TextField(max_length=50, verbose_name="Путь к полному сертификату")
    pathtosingle = models.TextField(max_length=50, verbose_name="Путь к одинарному серфитикату")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Пустой сертификат"
        verbose_name_plural = "Пустые сертификаты"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in EmptyCert._meta.fields]


class UserCert(models.Model):
    title = models.ForeignKey(EmptyCert, on_delete=models.CASCADE, related_name='Сертификат')
    polzovatel = models.ForeignKey(Polzovatel, on_delete=models.CASCADE, related_name='Пользователь')
    glavnavik = models.IntegerField(default=0, verbose_name="Основной навык")
    vsenaviki = models.TextField(max_length=50, verbose_name="Все навыки")
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-title"]
        verbose_name = "Сертификат пользователя"
        verbose_name_plural = "Сертификаты пользователя"

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserCert._meta.fields]
