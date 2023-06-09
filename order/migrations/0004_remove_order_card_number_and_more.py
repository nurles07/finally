# Generated by Django 4.2.1 on 2023-06-03 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_tiket_departure_alter_country_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_alter_order_card_number_alter_order_cvv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cardholder_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='order',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='validity',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='tiket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.tiket'),
        ),
    ]
