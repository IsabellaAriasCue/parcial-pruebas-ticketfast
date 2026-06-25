from sqlalchemy import func
from sqlalchemy.orm import Session

from src.database.models import ReservaDB


class ReservasRepositorio:

    PRECIOS = {
        "VIP": 150000,
        "General": 50000
    }

    def __init__(self, db: Session):
        self.db = db

    def guardar_reserva(self, evento_id, cliente_email, zona, cantidad):
        reserva = ReservaDB(
            evento_id=evento_id,
            cliente_email=cliente_email,
            zona=zona,
            cantidad=cantidad
        )

        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)

        return reserva

    def calcular_total_evento(self, evento_id):
        reservas = (
            self.db.query(
                ReservaDB.zona,
                func.sum(ReservaDB.cantidad).label("cantidad")
            )
            .filter(ReservaDB.evento_id == evento_id)
            .group_by(ReservaDB.zona)
            .all()
        )

        total = 0

        for zona, cantidad in reservas:
            total += self.PRECIOS[zona] * cantidad

        return total