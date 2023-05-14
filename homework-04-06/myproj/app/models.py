from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название предмета')
    description = models.TextField(verbose_name='Описание предмета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    age = models.IntegerField(verbose_name='Возраст')
    subjects = models.ManyToManyField(Subject, verbose_name='Предметы')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    mark = models.IntegerField(verbose_name='Оценка')

    def __str__(self):
        return f'{self.student} {self.subject}'

    class Meta:
        verbose_name = "Зачетка"
        verbose_name_plural = "Зачетки"
