from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField(Author, related_name="books")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="books"
    )
    publication_date = models.DateField(editable=False)
    pages = models.IntegerField()

    def __str__(self) -> str:
        return str(self.title)

class Bug(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    title = models.CharField("Назва багу", max_length=200)
    description = models.TextField("Опис")
    severity = models.PositiveSmallIntegerField("Рівень критичності")
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"