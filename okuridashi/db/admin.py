from django.contrib import admin
from .models import Bout, Heya, Measurement, Retirement, Rikishi, TournamentDay, Rank, Shikona, Banzuke

# Register your models here.
admin.site.register(Rikishi)
admin.site.register(Banzuke)
admin.site.register(TournamentDay)
admin.site.register(Shikona)
admin.site.register(Rank)
admin.site.register(Measurement)
admin.site.register(Heya)
admin.site.register(Retirement)
admin.site.register(Bout)
