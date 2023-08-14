from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.delete_offer_uses_cases import DeleteOfferUseCase
from swagger_server.repository.delete_offer_repository import DeleteOfferRepository
from swagger_server.resources.db import db


class DeleteOfferView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        delete_offer_repository = DeleteOfferRepository(mysql, log)
        self.delete_offer_use_case = DeleteOfferUseCase(delete_offer_repository, log)

    def delete_offer(self, id_offer: int):  # noqa: E501
        """Eliminar oferta.

        Eliminar una oferta existente. # noqa: E501

        :param id_offer: 
        :type id_offer: int

        :rtype: ResponseDeleteOffer
        """

        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "delete_offer"
        package_name = __name__
        log = self.log
        start_time = default_timer()

        message = f"start request: {function_name}"
        log.info(
            self.msg_log,
            internal_transaction_id, function_name, package_name, message)

        response = self.delete_offer_use_case.delete_offer(id_offer, internal_transaction_id)

        end_time = default_timer()
        log.info("ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
        return response