

# Db Schema

## Status

* id: int, pk=true, index=true
* name: str, unique=true, nullable=false
### relationship

*  One-2-Many EcoMonitoring

## Type Incident

* id: int, pk=true, index=true
* name: str, unique=true, nullable=false
### relationship

*  One-2-Many EcoMonitoring

## File

* id: type=int, pk=true, index=true
* user_id: type=UUID, nullable=false
* type_file: str, nullable=true
* eco_monitoring_id: type=int, ForeignKey('eco_monitorings.id')
* storage_id: type=id, nullable=true
* created_at: type=datetime, default=datetime.utcnow
### relationship

*  One-2-Many EcoMonitoring


## Eco Monitoring

* id: type=UUID, pk=true, index=true
* creator_id: type=UUID, nullable=false
* manager_id: type=UUID, nullable=true
* title: type=str, nullable=false
* description: type=str, nullable=true
* status_id: type=int, nullable=false
* type_incident_id: type=int, nullable=false
* longitude: type=str, nullable=true
* latitude: type=str, nullable=true
* is_closed: type=bool, default=false, nullable=false

* created_at: type=datetime, default=datetime.utcnow
* updated_at: type=datetime, default=datetime.utcnow, onupdate=datetime.utcnow

### relationships

*  One-2-Many Status
*  One-2-Many Type Incident
*  One-2-Many File


# API methods

## Status #protected 

CRUD for status

## Type Incidents #protected

CRUD for type incidents

## File #protected

CRUD files
add file for type monitoring (eco_monitoring_id, user_id, file: str)


## Eco Monitoring #protected

CRUD for eco monitoring

* patch method for change status (eco_monitoring_id)

* patch method for set manager for eco monitoring (eco_monitoring_id, manager_id)

* patch method for closed eco monitoring (eco_monitoring_id)

# Schemas
![Image](https://github.com/user-attachments/assets/133f473f-2d85-4600-9b75-36a85317583a)
![Image](https://github.com/user-attachments/assets/d4478fba-ce0f-41f9-9943-dbd06a0c7dde)
