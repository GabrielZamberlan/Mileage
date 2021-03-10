from flask import Flask, jsonify, request

app=Flask(__name__)

carros= [
    { 
        'modelo': 'HB20',
        'velocidade_max': '180.0',
        'motor': '1.6',
        'marca': 'Hyundai'
    },

    { 
        'modelo': 'XC60',
        'velocidade_max': '175.0',
        'motor': '2.0',
        'marca': 'Volvo'
    },

    { 
        'modelo': 'Compass',
        'velocidade_max': '195.0',
        'motor': '2.0',
        'marca': 'Jeep'
    },

    { 
        'modelo': 'Fox',
        'velocidade_max': '160.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

    { 
        'modelo': 'Evoque',
        'velocidade_max': '185.0',
        'motor': '2.0',
        'marca': 'Land Rover'
    },

    { 
        'modelo': 'Polo',
        'velocidade_max': '195.0',
        'motor': '1.6',
        'marca': 'Volkswagen'
    }


]

# INSIRA SEU CÓDIGO

@app.route('/carros')
def mostrar_carros():
    return "modelo: HB20,velocidade_max: 180.0,motor: 1.6,marca: Hyundai / modelo: XC60,velocidade_max: 175.0,motor: 2.0,marca: Volvo / modelo: Compass,velocidade_max: 195.0,motor: 2.0,marca: Jeep / modelo: Fox,velocidade_max: 160.0,motor: 1.6,marca: Volkswagen / modelo: Evoque,velocidade_max: 185.0,motor: 2.0,marca: Land Rover / modelo: Polo,velocidade_max: 195.0,motor: 1.6,marca: Volkswagen"
# Não sei se é assim que faz, mas nesse ponto não tenho mais ideia. Vou fazer dos dois jeitos que pensei que funcionam.

@app.route('/carros')
def get_carros():
    return (carros)
# Esse é outro jeito que pensei que pode dar certo, ele seria mais eficiente e mais rápido do que o outro. Também faz mais sentido ser perto disso pelo fato de o outro sempre que eu querer adicionar um valor à lista eu teria que modificar no código e adicioná-lo ali também.

@app.route('/carros/motor')
def mostrar_motores():
    return "motor:1.6 / motor: 2.0 / motor: 2.0 / motor: 1.6 / motor: 2.0 / motor 1.6"
# Para selecionar apenas os motores eu pensei nesse método que é praticamente igual ao que usei no de mostrar todos os carros.

@app.route('/carros/motor')
def get_motores():
    return (carros / modelo)
# Aqui é a mesma ideia da outra do carro, que seria eu selecionar a categoria modelo dentro dos carros.

@app.route('/carros/modelo')
def put_carros():
    input ("Qual modelo do carro será adicionado?  ")
    return (carros / modelo)
# Esse foi o único jeito que pensei nesse, seria utilizando o put para atualizar a lista de carros de acordo com o que a pessoa escrever no input.

@app.route('/carros/motor')
def get_carros():
    input ("Gostaria de mudar o motor para qual valor?  ")
    return (carros / motor)
# Nesse jeito a pessoa puxaria todos os valores e escolheria algum, ainda não sei como, e com o input mudaria o valor do motor escolhido.

@app.route('/carros/modelo')
input("Qual modelo gostaria de deletar? ")
def delete_carros(input):
    return (carros/modelo)
# Aqui eu pensei em a pessoa digitar o modelo que ela quer deletar, o programa deleta e no final retorna a nova lista com o modelo deletado.

if __name__ == '__main__': 
    app.run(debug=True)