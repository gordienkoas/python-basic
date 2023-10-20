from django.db import migrations

CATEGORY_NAME = "default"


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Category = apps.get_model("shop", "Category")
    db_alias = schema_editor.connection.alias
    Category.objects.using(db_alias).create(
        name=CATEGORY_NAME,
        description="default category",
    )


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Category = apps.get_model("shop", "Category")
    db_alias = schema_editor.connection.alias
    Category.objects.using(db_alias).filter(name=CATEGORY_NAME).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_category"),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_func,
            reverse_code=reverse_func,
        ),
    ]