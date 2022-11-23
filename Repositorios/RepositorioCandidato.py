from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Candidato import Candidato
from bson.objectid import ObjectId
class RepositorioCandidato(InterfaceRepositorio[Candidato]):

    def getListadosCandidato(self,id_candidato):
        theQuery = {"candidatos.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
