from django.db import models


class User(models.Model):
    email = models.EmailField(verbose_name='Почта')
    password = models.CharField(max_length=16, verbose_name='Пароль')

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=20, verbose_name='Имя')
    card_number = models.CharField(max_length=16, verbose_name='Номер карточки')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'clients'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=20, verbose_name='Имя')
    position = models.CharField(max_length=20, verbose_name='Должность')

    def __str__(self):
        return f'{self.name} в должности {self.position}'

    class Meta:
        db_table = 'workers'
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Ingredient(models.Model):
    name = models.CharField(max_length=20, verbose_name='Ингридиент')
    extra_price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.name} - {self.extra_price}'

    class Meta:
        db_table = 'ingridients'
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Food(models.Model):
    name = models.CharField(max_length=20, verbose_name='Блюдо')
    start_price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.name}-{self.start_price}'

    class Meta:
        db_table = 'food'
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Работник')
    order_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')


class FoodOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='food_orders')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', verbose_name='Добавленные ингридиенты')

    def __str__(self):
        return f'Заказ номер {self.order.id} принят'

    class Meta:
        db_table = 'orders'
        verbose_name = 'Позиция для заказа'
        verbose_name_plural = 'Позиции для заказа'
