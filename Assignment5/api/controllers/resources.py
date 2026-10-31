
from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models


# CREATE - Add a new resource
def create(db: Session, resource):
    db_resource = models.Resource(
        item=resource.item,
        amount=resource.amount
    )

    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)

    return db_resource


# READ - Get all resources
def read_all(db: Session):
    return db.query(models.Resource).all()


# READ - Get one resource by ID
def read_one(db: Session, resource_id):
    return db.query(models.Resource).filter(
        models.Resource.id == resource_id
    ).first()


# UPDATE - Update an existing resource
def update(db: Session, resource_id, resource):
    db_resource = db.query(models.Resource).filter(
        models.Resource.id == resource_id
    )

    update_data = resource.model_dump(exclude_unset=True)

    db_resource.update(
        update_data,
        synchronize_session=False
    )

    db.commit()

    return db_resource.first()


# DELETE - Remove a resource
def delete(db: Session, resource_id):
    db_resource = db.query(models.Resource).filter(
        models.Resource.id == resource_id
    )

    db_resource.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
