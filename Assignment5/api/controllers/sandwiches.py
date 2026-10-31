
from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models


# Create a new sandwich
def create(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )

    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)

    return db_sandwich


# Read all sandwiches
def read_all(db: Session):
    return db.query(models.Sandwich).all()


# Read one sandwich by its ID
def read_one(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(
        models.Sandwich.id == sandwich_id
    ).first()


# Update an existing sandwich
def update(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(
        models.Sandwich.id == sandwich_id
    )

    update_data = sandwich.model_dump(exclude_unset=True)

    db_sandwich.update(update_data, synchronize_session=False)
    db.commit()

    return db_sandwich.first()


# Delete a sandwich
def delete(db: Session, sandwich_id):
    db_sandwich = db.query(models.Sandwich).filter(
        models.Sandwich.id == sandwich_id
    )

    db_sandwich.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
