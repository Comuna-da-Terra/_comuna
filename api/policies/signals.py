# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Policy, UserPolicy

# @receiver(post_save, sender=Policy)
# def update_user_policy_approval(sender, instance, **kwargs):
#     # Quando uma policy for atualizada, definir 'approval' como negativo
#     user_policies = UserPolicy.objects.filter(policy=instance)
#     user_policies.update(approval=False)
