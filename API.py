from flask import Flask,jsonify,request
#disse que do flask quero importar flas,jsonify(leitor de codigo JSON) e o request para fazer requisições
app = Flask(__name__)
#criei um objeto como manda a documentação
livros=[
    {
        'id':1,
        'titulo':'branca de neve e os 7 anões',
        'autor':'dominio publico',
    },
    {
         'id':2,
         'titulo':'senhor dos aneis- a sociedade de baitola',
         'autor':'J.K HOWLING',

    },
     {
          'id':3,
          'titulo':'lord macaco',
          'autor':'teu pai aquele corno',

     },


]
#o banco de dados sskksksks

@app.route('/livros',methods=['GET'])#criei uma rota e restringi as requests há apenas metodo GET(puxar dados)
def ver_livros ():#isso é uma função
    return jsonify(livros)#mandei retornar o array livros em JSON que geralmente se usa em APIs
#explorar outros metodos
@app.route('/livros/<int:id>',methods=['GET'])#aqui especifiquei"olha no segundo barra só pode ter numeros inteiros"
def get_on_id (id):#criei uma nova função passando um parametro id
    for livro in livros:#criei um laço de repetição
        if livro.get('id')== id:#livro é o dicionario em livros usei get('id') para acessar valores com o parametro id
            return jsonify(livro)#retoma as informações do livro em JSON
#agora vou editar pelo ID   

@app.route('/livros/<int:id>',methods =['PUT'])#especifiquei que quero o metodo PUT
def edit_by_id(id):#outra função
    edited = request.get_json()#criei uma variavel que tem valor das requisições em json
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
          livros[indice].update(edited) 
          return jsonify(livros[indice])
#agora um parametro que adiciona um novo livro
@app.route('/livros',methods=['POST'])
def new_book():
    one_new_book =request.get_json
    livros.append(one_new_book)
    return jsonify(livros)



app.run(port=5000,host='localhost',debug='true')#informações do meu server    