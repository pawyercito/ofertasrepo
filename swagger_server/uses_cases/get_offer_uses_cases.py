from swagger_server.models.response_get_single_offer import ResponseGetSingleOffer
from swagger_server.repository.get_offer_repository import GetOfferRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_get_single_offer import RequestGetSingleOffer


class GetOfferUseCase:

    def __init__(self, offer_repository: GetOfferRepository, log: Logging):
        self.log = log
        self.offer_repository = offer_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def get_offer(self, body: RequestGetSingleOffer, internal_transaction_id: str):
        print(body)
        data = self.offer_repository.get_offer(body, internal_transaction_id, body.external_transaction_id)
       
        if data:
            response = ResponseGetSingleOffer(
                code="200",
                message="Datos obtenidos exitosamente",
                data=data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        else:
            response = ResponseGetSingleOffer(
                code="404",
                message="No hay ofertas registradas.",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 404