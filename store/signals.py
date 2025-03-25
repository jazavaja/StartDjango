from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from store.models import Product


@receiver(post_save,sender=Product)
def create_products(sender,instance,created,**kwargs):
    if created:
        # sendMail
        send_mail(
            "Test",
            f"Product {instance.name}",
            "from@javad.com",
            ["to@javad.com"]
        )
        print(f"Product with name {instance.name} price: {instance.price} Created")
