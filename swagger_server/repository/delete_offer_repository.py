from swagger_server.models.db.offer_model import Offer
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class DeleteOfferRepository:

    def __init__(self, mysql: db, log: logging ) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def delete_offer(self, id_offer, internal_transaction_id):
        try:
            offer = Offer.query.get(id_offer)
            if offer:
                offer.destroy()
                return offer.to_json()
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id, "delete_offer", __name__, error)
            return ""