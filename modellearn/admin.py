from django.contrib import admin

from modellearn.models import Person, Student, PersonAddress

# Register your models here.

# Method 1
# admin.site.register(Person)
admin.site.register(Student)
admin.site.register(PersonAddress)


# Method 2

@admin.action(description='تغییر جنسیت کاربران')
def change_sex(modeladmin, request, queryset):
    for obj in queryset:
        if obj.sex is not None:
            obj.sex = not obj.sex
            obj.save()
        else:
            obj.sex = True
            obj.save()


@admin.action(description='ارسال پیامک')
def sendsms(modeladmin, request, queryset):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'sex')
    list_filter = ('first_name', 'last_name')
    list_editable = ('mobile',)
    list_per_page = 2
    search_fields = ('first_name', 'last_name')
    actions = [change_sex, sendsms]
