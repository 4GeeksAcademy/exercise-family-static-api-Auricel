
"""
actualice este archivo para implementar los siguientes métodos ya declarados: - 
add_member: debe agregar un miembro a la lista self._members -
delete_member: debe eliminar un miembro de la lista self._members - 
update_member: debe actualizar un miembro de la lista self._members - 
get_member: debe devolver un miembro de la lista self._members """
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        
        # example list of members
        self._members = []

    # Solo lectura (read-only): use este método para generar identificaciones de miembros aleatorios al agregar miembros a la lista
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Rellene este método y actualice la devolución.
        # La lista de python tiene un metodo llamado append Agrega un ítem al final de la lista

        #si no tiene Id
        if not member.get("id"):
            #creale un nuevo ID
            member["id"] = self._generateId()
        self._members.append(member)


    def delete_member(self, id):
        print(id)
        
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
            # si no existe ese miembro
        return False
       

    def get_member(self, id):
         # Rellene este método y actualice la devolución.
         for member in self._members:
          if member["id"] == id:
             return member
            

    # Este método está hecho, devuelve una lista con todos los miembros de la familia.
    def get_all_members(self):
        return self._members
