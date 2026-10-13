class Cliente:
    """MODELO: representa un cliente. Si los datos están mal, el objeto no se crea."""

    # ===== ATRIBUTOS DE CLASE (estáticos): existen una sola vez =====
    CAMPOS = ("nombre", "apellido", "email", "telefono", "ciudad", "direccion")
    OBLIGATORIOS = ("nombre", "apellido", "email")
    total_creados = 0

    def __init__(self, id_cliente, nombre, apellido, email,
                 telefono="", ciudad="", direccion=""):
        self.__id = id_cliente        # privado y sin setter: no se puede cambiar
        # Asignamos por las PROPIEDADES para que la validación corra también al crear
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.direccion = direccion
        Cliente.total_creados += 1    # el contador vive en la CLASE, no en el objeto

    # ===== MÉTODOS ESTÁTICOS: reglas que no dependen de ningún cliente =====
    @staticmethod
    def limpiar(texto):
        return str(texto).strip()

    @staticmethod
    def es_email_valido(texto):
        texto = str(texto).strip()
        if texto.count("@") != 1:
            return False
        usuario, dominio = texto.split("@")
        return len(usuario) > 0 and "." in dominio and not dominio.endswith(".")

    # ===== PROPIEDADES =====
    @property
    def id(self):
        # SOLO LECTURA: no tiene setter, así que cliente.id = 5 lanza AttributeError
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        valor = Cliente.limpiar(valor)
        if not valor:
            raise ValueError("El nombre es obligatorio")
        self.__nombre = valor.title()

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        valor = Cliente.limpiar(valor)
        if not valor:
            raise ValueError("El apellido es obligatorio")
        self.__apellido = valor.title()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        valor = Cliente.limpiar(valor)
        if not Cliente.es_email_valido(valor):
            raise ValueError(f"Email inválido: '{valor}'")
        self.__email = valor.lower()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        valor = Cliente.limpiar(valor)
        if valor and not valor.isdigit():
            raise ValueError("El teléfono solo puede tener números")
        self.__telefono = valor

    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, valor):
        self.__ciudad = Cliente.limpiar(valor).title()

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, valor):
        self.__direccion = Cliente.limpiar(valor)

    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    # ===== MÉTODOS DE INSTANCIA: necesitan los datos de ESTE cliente =====
    def a_diccionario(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
            "telefono": self.__telefono,
            "ciudad": self.__ciudad,
            "direccion": self.__direccion,
        }

    def __str__(self):
        return f"[{self.__id}] {self.nombre_completo} - {self.__email}"

    # ===== MÉTODO DE CLASE: fabrica un objeto a partir de un diccionario =====
    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos.get("telefono", ""),
            datos.get("ciudad", ""),
            datos.get("direccion", ""),
        )
