from views import ClienteController


class MenuClientes:
    """VISTA: muestra, pide y presenta. No decide reglas del negocio."""

    def __init__(self, controlador=ClienteController):
        # ATRIBUTOS DE INSTANCIA: estado de ESTE menú
        self.__controlador = controlador
        self.__activo = True
        # DICCIONARIO tecla -> (texto, método)
        self.__opciones = {
            "1": ("Crear cliente", self.crear),
            "2": ("Ver todos", self.listar),
            "3": ("Ver por id", self.ver_por_id),
            "4": ("Actualizar", self.actualizar),
            "5": ("Eliminar", self.eliminar),
            "0": ("Salir", self.salir),
        }

    # ===== ESTÁTICOS: utilidades del menú, no dependen del estado =====
    @staticmethod
    def pausa():
        input("\nPresione Enter para continuar...")

    @staticmethod
    def pedir_entero(etiqueta):
        """Devuelve un entero o None si el usuario escribió cualquier otra cosa."""
        try:
            return int(input(etiqueta))
        except ValueError:
            return None

    @staticmethod
    def mostrar_resultado(exito, mensaje):
        print(("OK: " if exito else "ERROR: ") + mensaje)

    # ===== MÉTODOS DE INSTANCIA =====
    def mostrar_tabla(self, clientes):
        print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CIUDAD':<15}{'TELEFONO':<12}")
        print("-" * 85)
        for cliente in clientes:
            print(f"{cliente.id:<5}{cliente.nombre_completo:<25}"
                  f"{cliente.email:<28}{cliente.ciudad:<15}{cliente.telefono:<12}")
        print("-" * 85)
        print(f"Total: {len(clientes)} cliente(s)")

    def crear(self):
        print("\n--- CREAR NUEVO CLIENTE ---")
        # Recorro la TUPLA de campos del Modelo: si el Modelo cambia, el formulario también
        datos = {}
        for campo in self.__controlador.MODELO.CAMPOS:
            datos[campo] = input(f"{campo.capitalize()}: ")

        self.mostrar_resultado(*self.__controlador.crear(datos))
        self.pausa()

    def listar(self):
        print("\n--- LISTA DE CLIENTES ---")
        clientes = self.__controlador.listar()
        if not clientes:
            print("Todavía no hay clientes. Use la opción 1 para crear el primero.")
        else:
            self.mostrar_tabla(clientes)
        self.pausa()

    def ver_por_id(self):
        print("\n--- VER CLIENTE POR ID ---")
        id_cliente = self.pedir_entero("Id del cliente: ")
        if id_cliente is None:
            print("El id debe ser un número entero")
            return self.pausa()

        cliente = self.__controlador.obtener(id_cliente)
        if cliente is None:
            print(f"No existe un cliente con id {id_cliente}")
        else:
            for clave, valor in cliente.a_diccionario().items():
                print(f"  {clave.capitalize():<12}: {valor}")
        self.pausa()

    def actualizar(self):
        print("\n--- ACTUALIZAR CLIENTE ---")
        id_cliente = self.pedir_entero("Id del cliente: ")
        if id_cliente is None:
            print("El id debe ser un número entero")
            return self.pausa()

        cliente = self.__controlador.obtener(id_cliente)
        if cliente is None:
            print(f"No existe un cliente con id {id_cliente}")
            return self.pausa()

        print(f"Editando a {cliente.nombre_completo}")
        print("Deje en blanco el campo que no quiera cambiar.\n")

        cambios = {}
        for campo in self.__controlador.MODELO.CAMPOS:
            actual = getattr(cliente, campo)          # lee la PROPIEDAD
            nuevo = input(f"{campo.capitalize()} [{actual}]: ").strip()
            if nuevo:
                cambios[campo] = nuevo

        self.mostrar_resultado(*self.__controlador.actualizar(id_cliente, cambios))
        self.pausa()

    def eliminar(self):
        print("\n--- ELIMINAR CLIENTE ---")
        id_cliente = self.pedir_entero("Id del cliente: ")
        if id_cliente is None:
            print("El id debe ser un número entero")
            return self.pausa()

        cliente = self.__controlador.obtener(id_cliente)
        if cliente is None:
            print(f"No existe un cliente con id {id_cliente}")
            return self.pausa()

        print(f"Se eliminará: {cliente}")
        respuesta = input("¿Confirma la eliminación? (si/no): ").strip().lower()
        if respuesta in ("si", "sí", "s"):
            self.mostrar_resultado(*self.__controlador.eliminar(id_cliente))
        else:
            print("Operación cancelada")
        self.pausa()

    def salir(self):
        self.__activo = False          # cambia el estado del objeto
        print("Hasta luego.")

    def mostrar_menu(self):
        print("\n=== SISTEMA DE GESTIÓN DE CLIENTES ===")
        for tecla, (texto, _metodo) in self.__opciones.items():
            print(f"  {tecla}. {texto}")
        print()

    def ejecutar(self):
        """El bucle principal: vive mientras __activo sea True."""
        while self.__activo:
            self.mostrar_menu()
            tecla = input("Seleccione una opción: ").strip()

            if tecla not in self.__opciones:
                print("Opción no válida")
                self.pausa()
                continue

            _texto, metodo = self.__opciones[tecla]
            metodo()          # el diccionario guarda el método: aquí se ejecuta


if __name__ == "__main__":
    try:
        MenuClientes().ejecutar()      # se crea el objeto y se lo pone a correr
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
