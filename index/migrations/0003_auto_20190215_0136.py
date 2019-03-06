# Generated by Django 2.1.1 on 2019-02-15 01:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("index", "0002_auto_20190215_0130")]

    operations = [
        migrations.AlterField(
            model_name="petition",
            name="ID",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="petition",
            name="author",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="petitions",
                to="index.User",
            ),
        ),
        migrations.AlterField(
            model_name="petition",
            name="created_date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2019, 2, 15, 1, 36, 53, 117699, tzinfo=utc),
            ),
        ),
        migrations.AlterField(
            model_name="petition",
            name="senate_response",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="petitions",
                to="index.Response",
            ),
        ),
        migrations.AlterField(
            model_name="petition",
            name="signatures",
            field=models.ManyToManyField(
                blank=True, related_name="petitions", to="index.Signature"
            ),
        ),
        migrations.AlterField(
            model_name="petition",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="petitions", to="index.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="signature",
            name="signed_date",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 2, 15, 1, 36, 53, 116985, tzinfo=utc)
            ),
        ),
    ]