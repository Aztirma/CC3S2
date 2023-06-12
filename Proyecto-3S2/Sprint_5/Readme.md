**Proyecto: SOS**  

**Descripción:**  
Este proyecto es un juego basado en el clásico juego de mesa SOS. El objetivo principal es crear secuencias SOS en un tablero para ganar puntos. El proyecto está diseñado para brindar una experiencia de juego interactiva y permite diferentes modos de juego.  

**Sprint 5:**
En este sprint, se realizaron mejoras y cambios en varias partes del proyecto

**En la clase Board:**
- Se agregó la funcionalidad de registro de movimientos del juego. Ahora, cada movimiento realizado se registra automáticamente en una lista llamada moves para un seguimiento detallado.  
- Se implementó un nuevo método llamado **record_game** que permite grabar el juego en un archivo de texto. Este método guarda la información del modo de juego, el tamaño del tablero y registra cada movimiento realizado durante el juego, incluyendo las secuencias SOS creadas.

**En la clase Computer:**  
- Se mejoró el método **play_turn** para una selección más precisa de jugadas. Ahora, en lugar de devolver None cuando no hay jugadas disponibles, se devuelve una tupla vacía ().   
- Se simplificó el código en el bucle for dentro del método **play_turn** para mejorar la eficiencia y eliminar declaraciones redundantes.   
- Se corrigió un error en el método **copy_cells** que generaba una lista con dimensiones invertidas.

 **En la clase GUI:**
- En el método **create_right_frame**, se agregó un nuevo botón llamado "Guardar Juego" al marco de la derecha. Este botón permite al usuario guardar el progreso del juego en un archivo de texto.
- En el método **add_letter_board**, se agregó soporte para el modo de juego "P vs PC", iniciando automáticamente el turno de la computadora cuando corresponde.
- Se introdujeron dos nuevas variables, *valor_sos_creados_1* y *valor_sos_creados_2*, para almacenar la cantidad de SOS creados por cada jugador.  
- Se implemento el método **guardar_juego**, este método permite guardar el progreso del juego en un archivo de texto. Registra los movimientos realizados, los SOS creados y el resultado del juego.

**Links:**
- Demo Sprint 05: https://drive.google.com/drive/folders/1Uqg_zyOr0l8ePMsXLdePr2JvKw1b1x0G?usp=sharing 
- Documento Sprint 05: https://docs.google.com/document/d/1pXt0pUqrprK0AZgJzzsIt-6ES9N-qg-N-G4x1vWvfjM/edit?usp=sharing