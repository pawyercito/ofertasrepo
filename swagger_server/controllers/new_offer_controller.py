import connexion

from swagger_server.models.request_new_offer import RequestNewOffer  # noqa: E501

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.new_offer_uses_cases import NewOfferUseCase
from swagger_server.repository.new_offer_repository import NewOfferRepository
from swagger_server.resources.db import db


class NewOfferView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        new_offer_repository = NewOfferRepository(mysql, log)
        self.new_offer_use_case = NewOfferUseCase(new_offer_repository, log)

    def new_offer(self):  # noqa: E501
        """Crear una nueva oferta.

        Crear una nueva oferta. # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseNewOffer
        """

        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "new_offer"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestNewOffer.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.new_offer_use_case.new_offer(body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response