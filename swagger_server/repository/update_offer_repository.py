from swagger_server.models.db.offer_model import Offer
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class UpdateOfferRepository:

    def __init__(self, mysql: db, log: logging ) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def save_changes(self, offer_exist, offer_data ,internal_transaction_id, external_transaction_id):
        try:
            offer_exist.description = offer_data.get("description")
            offer_exist.idcategory = offer_data.get("idcategory")
            offer_exist.name = offer_data.get("name")
            offer_exist.older_age = offer_data.get("older_age")
            offer_exist.price = offer_data.get("price")
            offer_exist.status = offer_data.get("status")

            offer_exist.save()
            return offer_exist.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "save_changes", __name__, error)
            return ""
    
    def check_offer(self, id_offer ,internal_transaction_id, external_transaction_id):
        try:
            offer = Offer.query.get(id_offer)
            return offer
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "check_offer", __name__, error)
            return ""