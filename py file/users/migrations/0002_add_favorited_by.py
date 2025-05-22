from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_gigs', to=settings.AUTH_USER_MODEL),
        ),
    ]
