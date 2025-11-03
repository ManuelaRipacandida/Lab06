from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.lista_auto=[]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        #connessione al database
        try:
            cnx=mysql.connector.connect(user='root', password='', host='localhost', database='autonoleggio')
            cursor = cnx.cursor()
            query_read = ("SELECT * FROM automobile")
            cursor.execute(query_read)
            self.lista_auto.clear()# svuota lista precedente
            for row in cursor:
                auto = Automobile(row[0], row[1], row[2], row[3],row[4],row[5])
                self.lista_auto.append(auto)

            cursor.close()
            cnx.close()
            return self.lista_auto
        except mysql.connector.Error as err:
            print(err)
            return None



    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            tutte_auto=self.get_automobili()
            risultati = []
            modello = modello.lower().strip()
            for auto in tutte_auto:
                if modello in auto.modello.lower():
                    risultati.append(auto)
            return risultati

        except Exception as err:
            print("❌ Errore nella ricerca:", err)
            return None
