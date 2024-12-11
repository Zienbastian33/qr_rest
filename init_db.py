from app import create_app, db
from app.models import MenuItem

def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()

        # Crear productos de ejemplo
        menu_items = [
            # Handrolls
            MenuItem(name='California Roll', description='Kanikama, palta, queso crema', price=3990, category='Handrolls'),
            MenuItem(name='Sake Roll', description='Salmón, palta', price=4290, category='Handrolls'),
            MenuItem(name='Ebi Roll', description='Camarón, palta, queso crema', price=4190, category='Handrolls'),
            
            # Sushi
            MenuItem(name='Nigiri Salmón', description='2 unidades de salmón fresco', price=3590, category='Sushi'),
            MenuItem(name='Nigiri Atún', description='2 unidades de atún fresco', price=3790, category='Sushi'),
            MenuItem(name='Roll Tempura', description='10 piezas tempura con salmón', price=8990, category='Sushi'),
            
            # Bebidas
            MenuItem(name='Coca-Cola', description='350ml', price=1500, category='Bebidas'),
            MenuItem(name='Ramune', description='Gaseosa japonesa 200ml', price=2500, category='Bebidas'),
            MenuItem(name='Cerveza Sapporo', description='350ml', price=3500, category='Bebidas'),
            
            # Extras
            MenuItem(name='Gyoza', description='5 empanaditas japonesas', price=4500, category='Extras'),
            MenuItem(name='Arrollado Primavera', description='2 unidades vegetarianas', price=3900, category='Extras'),
            MenuItem(name='Edamame', description='Porotos de soya al vapor', price=2900, category='Extras'),
        ]

        for item in menu_items:
            db.session.add(item)
        
        db.session.commit()

if __name__ == '__main__':
    init_db()
