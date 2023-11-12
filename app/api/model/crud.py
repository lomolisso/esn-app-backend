from sqlalchemy.orm import Session
from app.api.model import models
from app.api.model import schemas
from sqlalchemy import select, update

# --- Crud utils for EdgeGateway ---

def read_edge_gateways(session: Session, page=0, page_size=10) -> list[models.EdgeGateway]:
    query = select(models.EdgeGateway).offset(page).limit(page_size)
    result = session.execute(query)
    return result.scalars().all()

def read_edge_gateway_by_uuid(session: Session, uuid) -> models.EdgeGateway:
    query = select(models.EdgeGateway).where(
        models.EdgeGateway.uuid == uuid
    )
    result = session.execute(query)
    return result.scalars().first()

def create_edge_gateway(session: Session, edge_gateway: schemas.EdgeGatewayIn) -> models.EdgeGateway:
    db_instance = models.EdgeGateway(**edge_gateway.model_dump())
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return db_instance

def update_edge_gateway(session: Session, uuid: str, fields: dict) -> models.EdgeGateway:
    query = update(models.EdgeGateway).where(
        models.EdgeGateway.uuid == uuid
    ).values(fields)
    session.execute(query)
    session.commit()
    return read_edge_gateway_by_uuid(session=session, uuid=uuid)

# --- Crud utils for EdgeSensor ---

def read_edge_sensors(session: Session, page=0, page_size=10) -> list[models.EdgeSensor]:
    query = select(models.EdgeSensor).offset(page).limit(page_size)
    result = session.execute(query)
    return result.scalars().all()

def read_edge_sensor_by_uuid(session: Session, uuid) -> models.EdgeSensor:
    query = select(models.EdgeSensor).where(
        models.EdgeSensor.uuid == uuid
    )
    result = session.execute(query)
    return result.scalars().first()

def read_edge_sensor_by_edgex_device_uuid(session: Session, edgex_device_uuid) -> models.EdgeSensor:
    query = select(models.EdgeSensor).where(
        models.EdgeSensor.edgex_device_uuid == edgex_device_uuid
    )
    result = session.execute(query)
    return result.scalars().first()

def read_edge_sensor_by_device_name(session: Session, device_name) -> models.EdgeSensor:
    query = select(models.EdgeSensor).where(
        models.EdgeSensor.device_name == device_name
    )
    result = session.execute(query)
    return result.scalars().first()

def create_edge_sensor(session: Session, gateway_uuid: str, edge_sensor: schemas.EdgeSensorIn) -> models.EdgeSensor:
    db_instance = models.EdgeSensor(gateway_uuid=gateway_uuid, **edge_sensor.model_dump())
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return db_instance

def update_edge_sensor_by_uuid(session: Session, uuid: str, fields: dict) -> models.EdgeSensor:
    query = update(models.EdgeSensor).where(
        models.EdgeSensor.uuid == uuid
    ).values(fields)
    session.execute(query)
    session.commit()
    return read_edge_sensor_by_uuid(session=session, uuid=uuid)

def update_edge_sensor_by_device_name(session: Session, device_name: str, fields: dict) -> models.EdgeSensor:
    query = update(models.EdgeSensor).where(
        models.EdgeSensor.device_name == device_name
    ).values(fields)
    session.execute(query)
    session.commit()
    return read_edge_sensor_by_device_name(session=session, device_name=device_name)

# --- Crud utils for PredictiveModel ---
"""
def read_predictive_models(session: Session, page=0, page_size=10) -> list[models.PredictiveModel]:
    query = select(models.PredictiveModel).offset(page).limit(page_size)
    result = session.execute(query)
    return result.scalars().all()

def read_predictive_model_by_uuid(session: Session, uuid) -> models.PredictiveModel:
    query = select(models.EdgeGateway).where(models.EdgeGateway.uuid == uuid)
    result = session.execute(query)
    return result.scalars().first()

def create_predictive_model(session: Session, predictive_model: schemas.PredictiveModelIn) -> models.PredictiveModel:
    db_instance = models.PredictiveModel(**predictive_model.model_dump())
    session.add(db_instance)
    session.commit()
    session.refresh(db_instance)
    return db_instance

def update_predictive_model(session: Session, uuid: str, fields: dict) -> models.PredictiveModel:
    query = update(models.PredictiveModel).where(
        models.PredictiveModel.uuid == uuid
    ).values(fields)
    session.execute(query)
    session.commit()
    return read_edge_gateway_by_uuid(session=session, uuid=uuid)
"""