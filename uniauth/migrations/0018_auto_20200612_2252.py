# Generated by Django 3.0.7 on 2020-06-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniauth', '0017_auto_20200314_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='attribute_mapping',
            field=models.TextField(blank=True, default='{\n    "cn": "cn",\n    "codice_fiscale": "codice_fiscale",\n    "displayName": "displayName",\n    "eduPersonAffiliation": "eduPersonAffiliation",\n    "eduPersonEntitlement": "eduPersonEntitlement",\n    "eduPersonHomeOrganization": "eduPersonHomeOrganization",\n    "eduPersonPrincipalName": "eduPersonPrincipalName",\n    "eduPersonScopedAffiliation": "eduPersonScopedAffiliation",\n    "eduPersonTargetedID": "eduPersonTargetedID",\n    "email": [\n        "mail",\n        "email"\n    ],\n    "givenName": "givenName",\n    "mail": [\n        "mail",\n        "email"\n    ],\n    "matricola_dipendente": "matricola_dipendente",\n    "matricola_studente": "matricola_studente",\n    "schacHomeOrganization": "schacHomeOrganization",\n    "schacPersonalUniqueCode": "schacPersonalUniqueCode",\n    "schacPersonalUniqueID": "schacPersonalUniqueID",\n    "sn": "sn"\n}', help_text='Attribute that would be release to this SP, in JSON format.', null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='attribute_processor',
            field=models.CharField(blank=True, default='idp.processors.LdapUnicalMultiAcademiaProcessor', help_text='"package.file.classname", example: "idp.processors.LdapAcademiaProcessor"', max_length=256),
        ),
    ]
