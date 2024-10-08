# Generated by Django 5.0.3 on 2024-06-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vpn',
            name='rango_ip_mag',
        ),
        migrations.RemoveField(
            model_name='vpn',
            name='rango_ip_mun',
        ),
        migrations.RemoveField(
            model_name='vpn',
            name='red_mag',
        ),
        migrations.AddField(
            model_name='vpn',
            name='ip_mag',
            field=models.CharField(default=None, max_length=15, verbose_name='IP de MAG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='ip_mun',
            field=models.CharField(default=None, max_length=15, verbose_name='IP de MUN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='peer_mag',
            field=models.CharField(default='', max_length=15, verbose_name='Peer de MAG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='peer_mun',
            field=models.CharField(default=' ', max_length=15, verbose_name='Peer de MUN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='primer_ip_mag',
            field=models.CharField(default=True, max_length=15, verbose_name='Primer IP MAG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='primer_ip_mun',
            field=models.CharField(default='0', max_length=15, verbose_name='Primer IP MUN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='ultima_ip_mag',
            field=models.CharField(default='0', max_length=15, verbose_name='Última IP MAG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vpn',
            name='ultima_ip_mun',
            field=models.CharField(default='0', max_length=15, verbose_name='Última IP MUN'),
            preserve_default=False,
        ),
    ]
