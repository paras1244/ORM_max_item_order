# from dataclasses import field, fields
# from django.contrib import admin

# from .models import Items, Order

# # Register your models here.

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#         list_display = [
#             "id",
#             "cus_name",
#         ]

# @admin.register(Items)
# class ItemsAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "order",
#         "product_name",
#         "quantity",
#     )




# # Book.objects.all().aggregate(Max('price'))
# # Order.objects.all().values("id","cus
# # _name").annotate(count = Count("cus_name"))
# # from django.db.models import Avg


# // how to register model to admin ?
#     $ django-admin startproject authentication . 
#     $ python manage.py startapp users


#     #users/urls.py
#     from django.contrib.auth.models import AbstractUser
#     from django.urls import reverse

#     class CustomUser(AbstractUser):
#         pass

#     def get_absolute_url(self):
#         return reverse("login_page", args=[str(self.id)])


#     from django.contrib.auth.forms import UserChangeForm, UserCreationForm
#     from .models import CustomUser

#     class CustomUserCreationForm(UserCreationForm):
#         class Meta(UserCreationForm.Meta):
#             model = CustomUser
#             fields = [
#                 'first_name',
#                 'last_name',
#                 'username',
#                 'email',
#                 'password1',
#                 'password2',
#                 'is_staff',
#                 'is_superuser',
#             ]
        
#     class CustomUserChangeForm(UserChangeForm):
#         class Meta:
#             model = CustomUser
#             fields = UserChangeForm.Meta.fields


# from django.contrib import admin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     list_display = [
#             'first_name',
#             'last_name',
#             'email',
#             'is_staff',
#             'is_superuser',
#         ]    

# admin.site.register(CustomUser, CustomUserAdmin)


#     $ python manage.py makemigrations
#     $ python manage.py migrate


#     $ mkdir templates
#     $ touch templates/create_new.html


#     # authentication/settings.py
#     TEMPLATES:
#          'DIRS': [BASE_DIR/'templates']  # new


#     <!DOCTYPE html>
#     <html lang="en">

#     <head>
#         <meta charset="UTF-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <meta name="viewport" content="width=device-width, initial- 
#     scale=1.0">
#         <title>New admin</title>
#     </head>

#     <body>
#         <form method="post">
#             {% csrf_token %} {{ form.as_p }}
#         <input type="submit" value="Create new user" />
#         </form>
#     </body>

#     </html>


#     # users/views.py
#     from django.views.generic.edit import CreateView
#     from .models import CustomUser
#     from .forms import CustomUserCreationForm

#     class UserCreateView(CreateView):
#         model = CustomUser
#         template_name = 'create_new.html'
#         form_class = CustomUserCreationForm


#     # authentication/urls.py
#     from django.contrib import admin
#     from django.urls import path, include # new

#     urlpatterns = [
#         path('admin/', admin.site.urls,),
#         path('', include('users.urls')), # new
#     ]


# #user/urls.py
# from django.urls import path
# from .views import UserCreateView

# urlpatterns = [
#     path('', UserCreateView.as_view(), name='home'),
# ]


# // how to write APIView Django ?
# class PracticeSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Practice
#         fields = ('practice_id',
#                   'score',
#                   'correct',
#                   'wrong',
#                   'not_answered',
#                   )

#     def to_representation(self, instance):
#         """
#         Object instance -> Dict of primitive datatypes.
#         """
#         return {
#             "labels": ["Practice"],
#             "datasets": [
#                 {
#                     "label": "Correct",
#                     "data": instance.correct,
#                 },
#                 {
#                     "label": "Wrong",
#                     "data": instance.wrong
#                 },
#                 {
#                     "label": "Not_answered",
#                     "data": instance.not_answered,
#                 }
#             ]
#         }


# $ curl http://127.0.0.1:8000/api/practice/485
# {"labels": ["Practice"], "datasets": [{"label": "Correct", "data": 2}, {"label": "Wrong", "data": 3}, {"label": "Not_answered", "data": 0}]}


