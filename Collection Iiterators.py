orders = {
    "2023-10-01": [
        {"id": 101, "items": ["Хлеб", "Сыр"], "total": 370},
        {"id": 102, "items": ["Кофе"], "total": 280},
    ],
    "2023-10-02": [
        {"id": 103, "items": ["Яблоки", "Хлеб", "Сок"], "total": 460},
    ],
    "2023-10-03": []
}


#даты_заказов= [ дата по дате, заказа_лист в заказах.все() если будет заказа_лист существовать]
dates_orders = [date for date, order_list in orders.items() if order_list]
print(dates_orders)

#сумма_заказов=сум(заказы["запл"] по дата, заказа_лист в  заказах.все()  по  заказ в заказа_лист)
'''те мы с начала перебераем все даты, потом заходим в зачения этихдат, берем тотал и ссумируем'''
total_ordering=sum(order["total"] for date, order_list in orders.items() for order in order_list)
print(total_ordering)

#самое_дорогое=макс(заказ[всего]  по  дата,заказа_лист в  заказах.всех() по заказ в заказа_лист) )
most_expensive=max(order["total"] for date, order_list in orders.items() for order in order_list )
print(most_expensive)


'''все предметы={предмет
                  по  дата,заказа_лист в  заказах.всех()
                  по заказ в заказа_лист
                  по предмет в заказ[предметы]}

          {} - показывают что это сет, те нет повторяющихся объектов '''

all_items={item for date, order_list in orders.items()
           for order in order_list
           for item in order["items"]}

print(all_items)

#Исправлено, использовал енумирейт чтобы добавить последовательность
for i,v in enumerate(all_items, 1):
  print(f" {i}.{v}")
