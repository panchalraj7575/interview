# Generated by Django 2.0 on 2021-06-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutomerOreder',
            fields=[
                ('co_id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=50)),
                ('productPrice', models.IntegerField()),
                ('Qty', models.IntegerField()),
                ('TotalPrice', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
