from swagger_server.models.db.offer_model import Offer
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class AllOffersRepository:

    def __init__(self, mysql: db, log: logging ) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def get_all_offers(self, internal_transaction_id, external_transaction_id):
        try:
            offers = Offer.query.all()
            if offers:
                data = [o.to_json() for o in offers]
                return data
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "get_all_offers", __name__, error)
            return ""