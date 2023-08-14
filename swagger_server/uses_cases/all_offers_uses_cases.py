from swagger_server.models.response_all_offers import ResponseAllOffers
from swagger_server.repository.all_offers_repository import AllOffersRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_all_offers import RequestAllOffers


class AllOffersUseCase:

    def __init__(self, offer_repository: AllOffersRepository, log: Logging):
        self.log = log
        self.offer_repository = offer_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def get_all_offers(self, body: RequestAllOffers, internal_transaction_id: str):

        offers_data = self.offer_repository.get_all_offers(body.external_transaction_id, internal_transaction_id)
        
        if offers_data:
            response = ResponseAllOffers(
                code="200",
                message="Datos obtenidos exitosamente",
                data=offers_data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
        else:
            response = ResponseAllOffers(
                code="404",
                message="No hay ofertas registradas.",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
        return response