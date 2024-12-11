from app import create_app, db
from app.models import MenuItem, Order, OrderItem, TableToken

app = create_app()

with app.app_context():
    # Eliminar todas las tablas existentes
    db.drop_all()
    
    # Crear todas las tablas nuevamente
    db.create_all()
    
    print("Base de datos recreada exitosamente")
