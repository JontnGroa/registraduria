from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()

    ####################################################
    ###### ASIGNAR MESA Y CANDIDATO A RESULTADO  #######
    ####################################################
    def create(self,infoResultado,id_mesa,id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    ####################################################
    ###### MODIFICAR RESULTADO (MESA Y CANDIDATO) ######
    ####################################################
    def update(self,id,infoResultado,id_mesa,id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa = infoResultado["numero_mesa"]
        elResultado.id_partido = infoResultado["id_partido"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)
    def delete(self,id):
        return self.repositorioResultado.delete(id)