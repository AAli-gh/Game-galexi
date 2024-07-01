from django.contrib import admin
from .models import Category, Developer, Publisher, Game, Review, UserLibrary, Order, Wishlist, UserProfile

admin.site.register(Category)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(UserLibrary)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(UserProfile)