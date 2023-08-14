from swagger_server.models.db.offer_model import Offer
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class NewOfferRepository:

    def __init__(self, mysql: db, log: logging ) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def create_offer(self, offer, internal_transaction_id: str, external_transaction_id: str):
        try:
            new_offer = Offer(offer)
            new_offer.save()
            return new_offer.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "new_offer", __name__, error)
            return ""