from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from DB import menu

app = Flask(__name__) #Crio o aplicativo
CORS(app)


#Import the table 'Products' of the CandyCakes_DB.db Database, like Dictionary  inside a list 'products'. 
products = {}
db = menu(2)
for iten in db:
    products[f'{iten[2]}'] = []
for linha in db:    
    for tipo in products:
        if tipo == linha[2]:
            products[tipo].append({'ID': linha[0], 'nome': linha[1], 'tipo': linha[2], 'price': linha[3], 'quantidade': linha[4]})


#create products
@app.route('/products/', methods=['POST'])
@cross_origin(origins=['http://127.0.0.1:5500'],
               allow_headers=['access-control-allow-origin','Access-Control-Request-Headers', 'content-type'], 
               methods=['GET', 'POST', 'OPTIONS'])
def creatable():
    data = request.get_json()
    menu(1, 0, data)
    menu(5)
    print(data)
    return 'OK!'


#query_get_all
@app.route('/products/', methods=['GET'])
@cross_origin(origins=['http://127.0.0.1:5500'],
               allow_headers=['access-control-allow-origin','Access-Control-Request-Headers', 'content-type'], 
               methods=['GET', 'POST', 'OPTIONS'])
def getdb():
    try: 
        return jsonify(products)
    except:
        return print('Erro, seu dado por id não foi encontrado!')


# query_Get_id
@app.route('/products/<objeto>', methods=['GET'])
@cross_origin(origins=['http://127.0.0.1:5500'],
               allow_headers=['access-control-allow-origin','Access-Control-Request-Headers', 'content-type'], 
               methods=['GET', 'POST', 'OPTIONS'])
def query_get_id(objeto):
    lista =  []
    cont = 0
    print(objeto, 'queryID')
    for propriedade in products:
        for produto in products[propriedade]:
            if produto.get('ID') == int(objeto):
                cont = cont + 1
                lista.append(produto)
    if cont == 0:
                return f"Nada encontrado para {objeto}!"
    elif cont != 0:
        for iten in lista:
             return iten



#DELETE LINE
@app.route('/products/<int:id>', methods=['DELETE'])
def deliten(id):
    print(f'O ID é {id}')
    menu(3, id)
    print('Produto deletado!')
    att = menu(2)
    return ( att)
    
# HTTP status response of request codes -> https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
app.run(port=5000, host='localhost', debug=True) 
