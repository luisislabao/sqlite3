from DB import menu
products = {
    "Doces": 
    [
        {'Id': 0, "nome": 'Quindim', "tipo": "Doces", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'Brigad.', "tipo": "Doces", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'P.coco', "tipo": "Doces", "price": 0, "quantidade": 0 }
    ],
    "Bolos":
    [
        {'Id': 0, "nome": 'Bolo P', "tipo": "Bolos", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'Bolo M', "tipo": "Bolos", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'Bolo G', "tipo": "Bolos", "price": 0, "quantidade": 0 }
        
    ],
    "Salgados":
    [
        {'Id': 0, "nome": 'Empada de F', "tipo": "Salgados", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'Hamburger', "tipo": "Salgados", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'HotDog', "tipo": "Salgados", "price": 0, "quantidade": 0 }
    ],
    "Bebidas":
    [
        {'Id': 0, "nome": 'Coca250ml', "tipo": "Bebidas", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'Pepsi250ml', "tipo": "Bebidas", "price": 0, "quantidade": 0 },
        {'Id': 0, "nome": 'Fanta250ml', "tipo": "Bebidas", "price": 0, "quantidade": 0 }
    ]
}
menu(1,0,products)
print("ok!")