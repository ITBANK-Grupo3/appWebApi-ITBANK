from database.models import Cliente


class CustomMethods:
    def get_customer_id(self, request):
        dni = request.user.username
        cliente_id = (
            Cliente.objects.using("homebanking").filter(customer_dni=dni).first()
        )
        return cliente_id.customer_id
