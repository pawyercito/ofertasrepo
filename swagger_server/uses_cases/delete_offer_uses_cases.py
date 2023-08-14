from swagger_server.models.response_delete_offer import ResponseDeleteOffer
from swagger_server.repository.delete_offer_repository import DeleteOfferRepository
from swagger_server.utils.logs.logging import log as logging


class DeleteOfferUseCase:

    def __init__(self, offer_repository: DeleteOfferRepository, log: logging):
        self.log = log
        self.offer_repository = offer_repository
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def delete_offer(self, id_offer: int, internal_transaction_id: str):
        
        offer_data = self.offer_repository.delete_offer(id_offer, internal_transaction_id)
        
        if offer_data:
            response = ResponseDeleteOffer(
                code="200",
                message="Oferta eliminada exitosamente.",
                data=offer_data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=None
            )
            return response, 200
        else:
            response = ResponseDeleteOffer(
                code="404",
                message="La oferta ingresada no existe.",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=None
            )
            return response, 400