from django.contrib import admin, messages
from django.db.models import QuerySet, Q
from .models import Movie


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        rating = self.value()
        match rating:
            case '<40':
                return queryset.filter(rating__lt=40)
            case 'от 40 до 59':
                return queryset.filter(Q(rating__gte=40), Q(rating__lte=59))
            case 'от 60 до 79':
                return queryset.filter(Q(rating__gte=60), Q(rating__lte=79))
            case _:
                return queryset.filter(rating__gte=80)


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug', 'budget']
    # readonly_fields = ['year', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['id', 'name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'currency', 'budget']
    ordering = ['rating']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть?!'
        elif movie.rating < 70:
            return 'Разок можно глянуть'
        elif movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей'
        )

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.ERROR
        )
