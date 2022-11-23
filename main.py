from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa

app = Flask(__name__)
cors = CORS(app)
miControladorResultado = ControladorResultado()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorMesa = ControladorMesa()

###############################################################
######### MENSAJE DE CONEXION CON EL SERVIDOR #################
###############################################################

@app.route("/", methods = ['GET'])
def inicio():
    json = {}
    json["message"] = "Servidor Activo y Corriendo..."
    return jsonify(json)

###########################################################
######### VISTAS PARA EL METODO RESULTADO #################
###########################################################
@app.route("/resultados", methods = ['GET'])
def verResultados():
    json = miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>", methods = ['POST'])
def crearResultado(id_mesa,id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data,id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id>", methods = ['GET'])
def verResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>", methods = ['PUT'])
def actualizarResultado(id_resultado,id_mesa,id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado,data,id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>", methods = ['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)

#########################################################
######### VISTAS PARA EL METODO PARTIDO #################
#########################################################
@app.route("/partidos", methods = ['GET'])
def verPartidos():
    json = miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos", methods = ['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>", methods = ['GET'])
def verPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>", methods = ['PUT'])
def actualizarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>", methods = ['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

######################################################
######### VISTAS PARA EL METODO MESA #################
######################################################
@app.route("/mesas", methods = ['GET'])
def verMesas():
    json = miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas", methods = ['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>", methods = ['GET'])
def verMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>", methods = ['PUT'])
def actualizarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>", methods = ['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

###########################################################
######### VISTAS PARA EL METODO CANDIDATO #################
###########################################################
@app.route("/candidatos", methods = ['GET'])
def verCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos", methods = ['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods = ['GET'])
def verCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods = ['PUT'])
def actualizarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods = ['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>/partidos/<string:id_partido>", methods = ['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json = miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)


#########################################################
######### VISTAS PARA FILTROS DE CANDIDATOS #############
#########################################################

@app.route("/mesas/resultados/<string:id_candidato>",methods=['GET'])
def inscritosEnCandidato(id_candidato):
    json=miControladorCandidato.listarInscritosEnCandidatos(id_candidato)
    return jsonify(json)

###############################################################
######### CARGUE DE ARCHIVO DE CONEXION MONGO #################
###############################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataconfig = loadFileConfig()
    print("Servidor Corriendo : " + "http://" + dataconfig["url-backend"] + ":" + str(dataconfig["port"]))
    serve(app, host = dataconfig["url-backend"], port = dataconfig["port"])