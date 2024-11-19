from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from basketplans.models import BasketPlan, BasketDelivered

def create_basket_deliveries():
    # Obtemos a data atual
    today = make_aware(datetime.now())
    
    # Lista para armazenar as informações das entregas
    result = {
        "created": [],
        "already_exists": []
    }
    
    # Buscamos todos os planos ativos
    active_plans = BasketPlan.objects.filter(is_active=True)

    # Itera sobre cada plano ativo
    for plan in active_plans:
        # Determina a data da primeira quarta-feira após a data atual
        days_until_wednesday = (2 - today.weekday()) % 7  # Calcula a quantidade de dias até a próxima quarta-feira
        first_delivery_date = today + timedelta(days=days_until_wednesday)

        # Se o tipo de plano for quinzenal, entregas devem ser feitas em semanas alternadas
        if plan.type == "Q":
            weeks = 2  # Quinzenal, a cada duas semanas
        else:
            weeks = 1  # Semanal, a cada semana

        # Vamos criar entregas para as próximas 4 semanas
        for i in range(4):
            delivery_date = first_delivery_date + timedelta(weeks=i * weeks)
            
            # Verifica se já existe uma entrega para o mesmo plano e o mesmo dia/mês
            if not BasketDelivered.objects.filter(
                plan=plan,
                delivered_date__month=delivery_date.month,
                delivered_date__day=delivery_date.day
            ).exists():
                # Se a entrega não existir, cria uma nova entrega
                BasketDelivered.objects.create(
                    plan=plan,
                    delivered_date=delivery_date,
                    delivered=False  # A entrega ainda não foi realizada
                )
                result["created"].append({
                    "plan": plan.id,
                    "delivery_date": delivery_date.date()
                })
            else:
                result["already_exists"].append({
                    "plan": plan.id,
                    "delivery_date": delivery_date.date()
                })
    
    return result
