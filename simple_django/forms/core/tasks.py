import pytz
from core.models import Logger, MyUser
from core.utils import get_mono_bank_currency, get_vkurse_currency, get_kurs_currency, get_minfin_currency, get_industrial_bank_currency
from django.core.mail import send_mail
from datetime import datetime, timedelta
from forms import celery_app
from rest_framework.authtoken.models import Token


@celery_app.task
def send_mail_celery(title, sender, message):
    send_mail(subject=title, message=message, from_email=sender, recipient_list=[sender])
    print("Mail sent!")


@celery_app.task
def check_date():
    now = datetime.now()
    now = pytz.utc.localize(now)
    Logger.objects.filter(time_created__lte=now - timedelta(days=7)).delete()


@celery_app.task
def store_currency():
    get_mono_bank_currency()
    get_vkurse_currency()
    get_kurs_currency()
    get_minfin_currency()
    get_industrial_bank_currency()


@celery_app.task
def token_generate():
    queryset = MyUser.objects.all()
    Token.objects.filter(user__in=queryset).delete()
    new_tokens = [Token(user=u, key=Token.generate_key()) for u in queryset.iterator()]
    Token.objects.bulk_create(new_tokens)
