import connexion

from swagger_server.models.request_update_offer import RequestUpdateOffer  # noqa: E501

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.update_offer_uses_cases import UpdateOfferUseCase
from swagger_server.repository.update_offer_repository import UpdateOfferRepository
from swagger_server.resources.db import db

class UpdateOfferView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        update_offer_repository = UpdateOfferRepository(mysql, log)
        self.update_offer_use_case = UpdateOfferUseCase(update_offer_repository, log)

    def update_offer(self, id_offer):  # noqa: E501
        """Actualizar oferta.

        Actualizar oferta. # noqa: E501

        :param id_offer: 
        :type id_offer: int
        :param body: 
        :type body: dict | bytes

        :rtype: ResponseUpdateOffer
        """

        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "update_offer"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:

            body = RequestUpdateOffer.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.update_offer_use_case.update_offer(id_offer, body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response