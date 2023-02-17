from django.db.models import (
    CASCADE, CharField, ForeignKey, BooleanField, DateField,
    IntegerField, Model, TextField) 

class ShoppingList(Model):
    title = CharField('Shopping list name', max_length=100)

    def __str__(self):
        return self.title



class ShoppingItem(Model):
    name = CharField("Shopping list item name", max_length=100)
    description = CharField("Shopping list item description", max_length=30)
    isCompleted = BooleanField(blank=False, null=False, default=False)
    shopping_list = ForeignKey(ShoppingList, on_delete=CASCADE)

    def __str__(self):
        return self.name
    