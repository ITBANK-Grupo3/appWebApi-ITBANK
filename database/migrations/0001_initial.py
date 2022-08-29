# Generated by Django 4.1 on 2022-08-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaCuenta',
            fields=[
                ('old_id', models.AutoField(primary_key=True, serialize=False)),
                ('new_id', models.IntegerField()),
                ('old_balance', models.IntegerField()),
                ('new_balance', models.IntegerField()),
                ('old_iban', models.IntegerField()),
                ('new_iban', models.IntegerField()),
                ('old_type', models.TextField()),
                ('new_type', models.TextField()),
                ('user_action', models.TextField()),
                ('created_at', models.TextField()),
            ],
            options={
                'db_table': 'auditoria_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrespondenciaDirecciones',
            fields=[
                ('correspondencia_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.TextField()),
            ],
            options={
                'db_table': 'correspondencia_direcciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('tipo_cuenta', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('dir_id', models.AutoField(primary_key=True, serialize=False)),
                ('titular_id', models.IntegerField()),
                ('calle', models.TextField()),
                ('numero', models.IntegerField()),
                ('ciudad', models.TextField()),
                ('provincia', models.TextField()),
                ('pais', models.TextField()),
            ],
            options={
                'db_table': 'direccionesprueba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MarcaTarjeta',
            fields=[
                ('marca_tarjeta_id', models.AutoField(primary_key=True, serialize=False)),
                ('marca_tarjeta_nombre', models.TextField()),
            ],
            options={
                'db_table': 'marca_tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('type', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('tarjeta_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_tarjeta', models.CharField(max_length=16, unique=True)),
                ('cvv', models.TextField()),
                ('fecha_creacion', models.TextField()),
                ('fecha_vencimiento', models.TextField()),
                ('tipo_tarjeta', models.TextField()),
                ('cliente_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': True,
            },
        ),
    ]
