class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
    
    def listarTareas(self):
     for tarea in self.tareas:
        if tarea.estaLista():
<<<<<<< HEAD
            print(f"[X] {tarea.obtenerNombre()}" )
=======
            print(f"La tarea {tarea.obtenerNombre()} no está lista")
>>>>>>> 5637fcc1366dd08c276f6137d8a9c30a686a7f6e
