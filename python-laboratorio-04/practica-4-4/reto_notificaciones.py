# reto_notificaciones.py
# Beneficio de la operación común: Permite aplicar polimorfismo, recorriendo colecciones de 
# objetos heterogéneos y llamando al método 'enviar()' de forma unificada sin requerir condicionales 'if'.
# Responsabilidades que deben permanecer fuera de las clases de notificación: La lógica de negocio 
# sobre CUÁNDO enviar una notificación, QUÉ destinatarios incluir o CÓMO formatear los datos empresariales 
# debe manejarse en servicios externos o controladores, manteniendo las clases de notificación enfocadas 
# exclusivamente en el canal de entrega del mensaje.

class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Subclases deben implementar este método.")


class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        return f"[CORREO ELECTRÓNICO] Enviando mensaje: '{mensaje}'"


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        return f"[CONSOLA] Alerta en pantalla: '{mensaje}'"


if __name__ == "__main__":
    sistema_notificaciones = [
        NotificacionCorreo(),
        NotificacionConsola()
    ]

    aviso = "El inventario ha registrado una actualización exitosa."

    for notif in sistema_notificaciones:
        print(notif.enviar(aviso))