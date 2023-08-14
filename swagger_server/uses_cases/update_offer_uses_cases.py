from swagger_server.models.response_update_offer import ResponseUpdateOffer
from swagger_server.repository.update_offer_repository import UpdateOfferRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_update_offer import RequestUpdateOffer


class UpdateOfferUseCase:

    def __init__(self, offer_repository: UpdateOfferRepository, log: Logging):
        self.log = log
        self.offer_repository = offer_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def update_offer(self, id_offer, body: RequestUpdateOffer, internal_transaction_id: str):
        
        offer_exist = self.offer_repository.check_offer(id_offer, internal_transaction_id, body.external_transaction_id)
        
        if offer_exist is None:
            response = ResponseUpdateOffer(
                code="404",
                message="No hay ofertas registradas.",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 404
        
        offer_data = body.data.to_dict()
        data = self.offer_repository.save_changes(offer_exist, offer_data, internal_transaction_id, body.external_transaction_id)
        
        if data:
            response = ResponseUpdateOffer(
                code="200",
                message="Oferta actualizada exitosamente.",
                data=data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        else:
            return 400