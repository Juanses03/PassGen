import random
import string
import curses
import time

def generar_contrasena(longitud, incluir_especiales=False):
    """
    EN: Generates a secure password of the specified length.
    ES: Genera una contraseña segura de la longitud especificada.
    FR: Génère un mot de passe sécurisé de la longueur spécifiée.

    EN: If incluir_especiales is True, includes special characters.
    ES: Si incluir_especiales es True, incluye caracteres especiales.
    FR: Si incluir_especiales est True, inclut des caractères spéciaux.
    """
    caracteres = string.ascii_letters + string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def mostrar_animacion(stdscr, textos):
    """
    EN: Displays an animation while generating the password.
    ES: Muestra una animación mientras se genera la contraseña.
    FR: Affiche une animation pendant la génération du mot de passe.
    """
    avatar = ["(•_•)", "( •_•)>⌐■-■", "(⌐■_■)"]
    stdscr.clear()
    y, x = 10, 30  # EN: Animation position | ES: Posición de la animación | FR: Position de l'animation
    curses.curs_set(0)  # EN: Hide cursor during animation | ES: Ocultar el cursor durante la animación | FR: Masquer le curseur pendant l'animation

    for i in range(len(avatar)):
        stdscr.clear()
        stdscr.addstr(y, x, avatar[i], curses.color_pair(5))  # EN: Display avatar | ES: Mostrar avatar | FR: Afficher l'avatar
        stdscr.addstr(y + 2, x - 5, textos["generando"], curses.color_pair(2))
        stdscr.refresh()
        time.sleep(0.5)  # EN: Pause to create animation | ES: Pausa para crear la animación | FR: Pause pour créer l'animation
    curses.curs_set(1)  # EN: Show cursor again | ES: Mostrar de nuevo el cursor | FR: Réafficher le curseur

def main(stdscr):
    try:
        # EN: Initialize colors | ES: Inicializar colores | FR: Initialiser les couleurs
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)   # EN: Selection color | ES: Color de selección | FR: Couleur de sélection
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # EN: Normal text color | ES: Color de texto normal | FR: Couleur de texte normale
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # EN: Warning or error color | ES: Color para advertencias o errores | FR: Couleur pour avertissements ou erreurs
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # EN: Title color | ES: Color para el título | FR: Couleur pour le titre
        curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)  # EN: Success message color | ES: Color para mensajes de éxito | FR: Couleur pour les messages de succès

        # EN: Display title | ES: Mostrar título | FR: Afficher le titre
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(1, 2, "===========================================")
        stdscr.addstr(2, 2, "           Password Generator              ")
        stdscr.addstr(3, 2, "===========================================")
        stdscr.attroff(curses.color_pair(4))

        # EN: List of languages | ES: Lista de idiomas | FR: Liste des langues
        idiomas = ["English", "Español", "Français"]
        seleccion = 0

        # EN: Language selection UI | ES: UI de selección de idioma | FR: Interface de sélection de la langue
        while True:
            stdscr.clear()

            # EN: Display title | ES: Mostrar título | FR: Afficher le titre
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(1, 2, "===========================================")
            stdscr.addstr(2, 2, "           Password Generator              ")
            stdscr.addstr(3, 2, "===========================================")
            stdscr.attroff(curses.color_pair(4))

            stdscr.addstr(5, 2, "Selecciona un idioma utilizando las flechas del teclado:", curses.color_pair(2))

            for idx, idioma in enumerate(idiomas):
                if idx == seleccion:
                    stdscr.addstr(7 + idx, 4, f"> {idioma}", curses.color_pair(1))  # EN: Selection color | ES: Color de selección | FR: Couleur de sélection
                else:
                    stdscr.addstr(7 + idx, 4, f"  {idioma}", curses.color_pair(2))  # EN: Normal color | ES: Color normal | FR: Couleur normale

            stdscr.refresh()

            # EN: Capture pressed key | ES: Capturar la tecla presionada | FR: Capturer la touche appuyée
            tecla = stdscr.getch()

            # EN: Handle selection with arrow keys | ES: Manejar la selección con las flechas del teclado | FR: Gérer la sélection avec les flèches du clavier
            if tecla == curses.KEY_UP and seleccion > 0:
                seleccion -= 1
            elif tecla == curses.KEY_DOWN and seleccion < len(idiomas) - 1:
                seleccion += 1
            elif tecla == ord('\n'):
                break

        idioma_seleccionado = idiomas[seleccion]

        # EN: Define messages in each language | ES: Definir los mensajes en cada idioma | FR: Définir les messages dans chaque langue
        mensajes = {
            "English": {
                "incluir": "Include special characters? (Y/N): ",
                "longitud": "Enter password length (min. 8): ",
                "generando": "Generating password...",
                "contrasena": "Generated password: ",
                "error_longitud": "Minimum length is 8 characters."
            },
            "Español": {
                "incluir": "¿Incluir caracteres especiales? (Y/N): ",
                "longitud": "Ingrese la longitud de la contraseña (min. 8): ",
                "generando": "Generando contraseña...",
                "contrasena": "Contraseña generada: ",
                "error_longitud": "La longitud mínima es 8 caracteres."
            },
            "Français": {
                "incluir": "Inclure des caractères spéciaux? (Y/N): ",
                "longitud": "Entrez la longueur du mot de passe (min. 8): ",
                "generando": "Génération du mot de passe...",
                "contrasena": "Mot de passe généré: ",
                "error_longitud": "La longueur minimale est de 8 caractères."
            }
        }

        textos = mensajes[idioma_seleccionado]

        # EN: Ask if special characters should be included | ES: Preguntar si incluir caracteres especiales | FR: Demander si des caractères spéciaux doivent être inclus
        incluir_especiales = False
        stdscr.clear()

        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(1, 2, "===========================================")
        stdscr.addstr(2, 2, "           Password Generator              ")
        stdscr.addstr(3, 2, "===========================================")
        stdscr.attroff(curses.color_pair(4))

        stdscr.addstr(5, 2, textos["incluir"], curses.color_pair(2))
        stdscr.refresh()

        tecla = stdscr.getch()
        if tecla in [ord('y'), ord('Y')]:
            incluir_especiales = True

        # EN: Length input UI | ES: UI de entrada de longitud | FR: Interface de saisie de longueur
        stdscr.clear()

        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(1, 2, "===========================================")
        stdscr.addstr(2, 2, "           Password Generator              ")
        stdscr.addstr(3, 2, "===========================================")
        stdscr.attroff(curses.color_pair(4))

        stdscr.addstr(5, 2, textos["longitud"], curses.color_pair(2))
        stdscr.refresh()

        curses.echo()  # EN: Enable visible input for length | ES: Habilitar la entrada visible para la longitud | FR: Activer la saisie visible pour la longueur
        longitud_str = stdscr.getstr(6, 2).decode("utf-8")
        try:
            longitud = int(longitud_str)

            # EN: Validate minimum length | ES: Validación de longitud mínima | FR: Validation de la longueur minimale
            if longitud < 8:
                raise ValueError(textos["error_longitud"])

        except ValueError as e:
            stdscr.clear()

            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(1, 2, "===========================================")
            stdscr.addstr(2, 2, "           Password Generator              ")
            stdscr.addstr(3, 2, "===========================================")
            stdscr.attroff(curses.color_pair(4))

            stdscr.addstr(5, 2, str(e), curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            return

        # EN: Display animation while generating password | ES: Mostrar animación mientras se genera la contraseña | FR: Afficher l'animation pendant la génération du mot de passe
        mostrar_animacion(stdscr, textos)

        # EN: Generate and display the password | ES: Generar y mostrar la contraseña | FR: Générer et afficher le mot de passe
        contrasena = generar_contrasena(longitud, incluir_especiales)

        stdscr.clear()

        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(1, 2, "===========================================")
        stdscr.addstr(2, 2, "           Password Generator              ")
        stdscr.addstr(3, 2, "===========================================")
        stdscr.attroff(curses.color_pair(4))

        stdscr.addstr(5, 2, textos["contrasena"], curses.color_pair(5))
        stdscr.addstr(7, 4, contrasena, curses.color_pair(2))

        stdscr.refresh()
        stdscr.getch()

    except Exception as e:
        stdscr.clear()
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(10, 10, f"Error inesperado: {str(e)}", curses.color_pair(3))
        stdscr.attroff(curses.color_pair(3))
        stdscr.refresh()
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
