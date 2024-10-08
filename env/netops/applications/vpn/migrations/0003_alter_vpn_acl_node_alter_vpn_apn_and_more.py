# Generated by Django 5.0.3 on 2024-06-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0002_remove_vpn_rango_ip_mag_remove_vpn_rango_ip_mun_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpn',
            name='acl_node',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='ACL Node'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='apn',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='APN'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='cliente_acm',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Cliente ACM'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='conectividad_entre_moviles',
            field=models.CharField(blank=True, choices=[('1', 'Full mesh'), ('2', 'Hub & spoke')], max_length=1, null=True, verbose_name='Conectividad entre moviles'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='contacto',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contacto'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='dns_1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='DNS 1'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='dns_2',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='DNS 2'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='empresa',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='ip_mag',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='IP de MAG'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='ip_mun',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='IP de MUN'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='ip_router',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='IP Router'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='nombre_acl',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nombre ACL'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='nombre_pool',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Nombre del pool'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='nombre_pool_moviles',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Nombre del pool moviles'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='peer_mag',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Peer de MAG'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='peer_mun',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Peer de MUN'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='primer_ip_mag',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Primer IP MAG'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='primer_ip_mun',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Primer IP MUN'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='prioridad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Prioridad'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='route_distinguisher',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Route distinguisher'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='server_ip',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Server IP'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='tinco_fija',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='TINCO fija'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='tinco_movil',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Tinco movil'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='tipo_ip',
            field=models.CharField(blank=True, choices=[('1', 'Fijas'), ('2', 'Dinamicas')], max_length=1, null=True, verbose_name='Tipo de IPs'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='ultima_ip_mag',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Última IP MAG'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='ultima_ip_mun',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Última IP MUN'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='vpn_instance',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='VPN instance'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='vprn_id',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='VPRN Id'),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='wildcard',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Wildcard'),
        ),
    ]
