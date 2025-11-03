import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_auto(self,e):
        lista_auto=self._model.get_automobili()
        lista = self._view.lista_auto
        # Svuoto la ListView della view prima di aggiornare
        lista.controls.clear()
        # Se la lista è vuota o None viene stampato un messaggio per l'utente
        if not lista_auto:
            lista.controls.append(
                ft.Text("Nessuna automobile trovata nel database."))
        else:
            for auto in lista_auto:
                testo=f"{auto.codice}| {auto.marca} {auto.modello} {auto.anno}"
                lista.controls.append(ft.Text(testo))

                # mostra il contenitore solo se cliccato
        self._view.contenitore_lista_auto.visible = True
        self._view.update()



    def cerca_auto(self,e):
        #Prendo il testo dal TextField della view
        modello = self._view.input_modello_auto.value.strip()
        #Chiamo il model
        lista_auto=self._model.cerca_automobili_per_modello(modello)
        # Pulisco il contenitore prima di mostrare i nuovi risultati
        lista=self._view.lista_auto_ricerca
        lista.controls.clear()
        if not lista_auto:
            lista.controls.append(ft.Text("Nessuna automobile trovata."))
        else:
            for auto in lista_auto:
                testo = f"{auto.codice} | {auto.marca} {auto.modello} ({auto.anno})"
                lista.controls.append(ft.Text(testo))

        self._view.contenitore_lista_ricerca.visible=True
        self._view.update()


