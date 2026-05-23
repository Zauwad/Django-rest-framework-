from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost",
            old_name="poublished_date",
            new_name="published_date",
        ),
    ]
