from django.core.management.base import BaseCommand
from core.utils import get_mono_bank_currency, get_vkurse_currency, get_kurs_currency, get_minfin_currency, get_industrial_bank_currency


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_mono_bank_currency()
        get_vkurse_currency()
        get_kurs_currency()
        get_industrial_bank_currency()
        get_minfin_currency()
