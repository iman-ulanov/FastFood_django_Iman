import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kfc.settings')

django.setup()

from project.models import *

# user1 = Client(user=User.objects.create(email='nikname21@gmail.com', password='defender42'),
#                name='Азата Соколов', card_number='4147 5657 9878 9009')
# user1.save()
#
# user2 = Worker(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'),
#                name='Алтынай Алиева', position='Оператор кассы')
# user2.save()
#
# cheese = Ingredient.objects.create(name='Сыр', extra_price=10)
# chicken = Ingredient.objects.create(name='Курица', extra_price=70)
# beef = Ingredient.objects.create(name='Говядина', extra_price=80)
# salad = Ingredient.objects.create(name='Салат', extra_price=15)
# french_fries = Ingredient.objects.create(name='Фри', extra_price=15)
#
# food1 = Food.objects.create(name='Шаурма', start_price=50)
# food2 = Food.objects.create(name='Гамбургер', start_price=25)
#
# # order1 = Order.objects.create(food1.ingredients.set([cheese, beef, salad, french_fries],
# #                                                     through_defaults={'food': food1,
# #                                                                       'client': user1,
# #                                                                       'worker': user2}))
#
# order1 = Order.objects.create(client=user1, worker=user2)
#
#
#
#
# food_order1 = FoodOrder.objects.create(order=order1, food=food1)
# food_order1.ingredients.set([cheese, beef, salad, french_fries])
#
# food_order2 = FoodOrder.objects.create(order=order1, food=food2)
# food_order2.ingredients.set([cheese, chicken, salad])

# cl = Client.objects.all()
# id_client = 0
# for i in list(cl):
#     if i.name == 'Азата Соколов':
#         id_client = i.id
#         for price in list(Order.objects.filter(client_id=id_client)):
#             if price.client_id == id_client:
#                 for f in Food.objects.filter(name='Шаурма'):
#                     food = f.start_price
#                     ingra = 0
#                     for ingredient in Ingredient.objects.all():
#                         if price.id == f.id:
#                             ingra = ingra + ingredient.extra_price
#                         print(ingra)
#                     break

print("TESTING")
client = Client.objects.all().first()

order = Order.objects.get(client=client.id)

food_orders = order.food_orders.all()

total_order_price = 0
for food_order in food_orders:
    food_order_details = {
        'client': food_order.order.client.name,
        'worker': food_order.order.worker.name,
        'food': food_order.food.name,
        'start_price': food_order.food.start_price
    }

    total_extra_price = sum(list(food_order.ingredients.all().values_list('extra_price', flat=True)))
    food_order_details['extra_price'] = total_extra_price
    total_order_price += food_order_details['start_price'] + food_order_details['extra_price']
    print(f"{food_order_details['client']} заказал {food_order_details['food']} "
          f"стоимостью {food_order_details['start_price'] + food_order_details['extra_price']}")

print(f'Общая стоимость заказа-{total_order_price}')

