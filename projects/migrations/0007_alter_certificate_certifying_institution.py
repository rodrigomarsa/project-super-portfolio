# Generated by Django 4.2.3 on 2023-09-01 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0006_alter_certificate_certifying_institution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="certifying_institution",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="certificates",
                to="projects.certifyinginstitution",
            ),
        ),
    ]
