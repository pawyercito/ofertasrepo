from swagger_server.resources.db import db


class Offer(db.Model):
    __tablename__ = "offers"
    id_offer = db.Column(db.Integer, primary_key=True)
    offerName = db.Column(db.String(50))
    offerPrice = db.Column(db.Float(10,2))
    validity_from = db.Column(db.Date)
    validity_until = db.Column(db.Date)

    def __init__(self, payload):
        self.offerName = payload.get('offerName')
        self.offerPrice = payload.get('offerPrice')
        self.validity_from = payload.get('validity_from')
        self.validity_until = payload.get('validity_until')

    def to_json(self):
        return {
            "id_offer": self.id_offer,
            "offerName": self.offerName,
            "offerPrice": self.offerPrice,
            "validity_from": self.validity_from,
            "validity_until": self.validity_until,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()