from swagger_server.models.response_new_offer import ResponseNewOffer
from swagger_server.repository.new_offer_repository import NewOfferRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_new_offer import RequestNewOffer


class NewOfferUseCase:

    def __init__(self, offer_repository: NewOfferRepository, log: Logging):
        self.log = log
        self.offer_repository = offer_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def new_offer(self, body: RequestNewOffer, internal_transaction_id: str):
        offer = body.data.to_dict()
        data = self.offer_repository.create_offer(offer, internal_transaction_id, body.external_transaction_id)
        
        if data:
            response = ResponseNewOffer(
                code="200",
                message="Oferta creada exitosamente.",
                data=data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        else:
            response = ResponseNewOffer(
                code="404",
                message="No hay ofertas registradas.",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 404