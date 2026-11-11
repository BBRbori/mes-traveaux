import tkinter as tk
import math

root = tk.Tk()
root.title("Special Letter ❤️")
root.geometry("800x600")
root.configure(bg="black")
root.resizable(False, False)

canvas = tk.Canvas(
    root, width=800, height=600,
    bg="black", highlightthickness=0
)
canvas.pack()

# Création du cœur
def heart_points(cx, cy, size):
    points = []
    for i in range(100):
        t = i * 2 * math.pi / 100
        x = 16 * math.sin(t)**3
        y = (13 * math.cos(t) - 5 * math.cos(2*t)
             - 2 * math.cos(3*t) - math.cos(4*t))
        points.extend((cx + x * size / 16,
                       cy - y * size / 16))
    return points


# Affichage de la lettre
def show_letter():
    canvas.create_rectangle(
        120, 40, 680, 560,
        fill="#fff0d9", outline="#d9a66f", width=4
    )

    canvas.create_text(
        400, 100, text="Une petite lettre pour toi",
        fill="#9c542d", font=("Georgia", 24, "bold")
    )

    canvas.create_text(
        400, 170,
        text="Il y a des choses qu'on ne peut pas\n"
             "toujours exprimer avec des mots...",
        fill="#543522", font=("Georgia", 16),
        justify="center"
    )

    canvas.create_text(
        400, 450,
        text="Clique sur le cœur ❤️",
        fill="#9c542d", font=("Georgia", 17)
    )

    canvas.create_polygon(
        heart_points(400, 315, 115),
        fill="#ff3155", outline="#b90032",
        width=3, tags="heart"
    )

    canvas.tag_bind("heart", "<Button-1>", bloom)


# Création d'un pétale
def make_petal(cx, cy, angle, length, width, color):
    points = []

    for i in range(21):
        t = i / 20
        x = length * t
        y = width * math.sin(math.pi * t)
        px = cx + x * math.cos(angle) - y * math.sin(angle)
        py = cy + x * math.sin(angle) + y * math.cos(angle)
        points.extend((px, py))

    for i in range(20, -1, -1):
        t = i / 20
        x = length * t
        y = -width * math.sin(math.pi * t)
        px = cx + x * math.cos(angle) - y * math.sin(angle)
        py = cy + x * math.sin(angle) + y * math.cos(angle)
        points.extend((px, py))

    canvas.create_polygon(
        points, fill=color, outline="#8c285c"
    )


# Animation de la fleur
def animate_flower(step=1):
    cx, cy = 400, 260

    canvas.delete("all")

    # Tige
    canvas.create_line(
        cx, cy + 10, cx, 560,
        fill="#238b45", width=9
    )

    # Feuilles
    canvas.create_oval(
        cx - 105, 410, cx, 465,
        fill="#39a852", outline=""
    )
    canvas.create_oval(
        cx, 460, cx + 105, 515,
        fill="#39a852", outline=""
    )

    colors = [
        "#ff4fa3", "#ff79bd",
        "#ffb0d5", "#ff5591"
    ]

    # Les pétales grandissent progressivement
    for i in range(12):
        angle = i * 2 * math.pi / 12
        make_petal(
            cx, cy, angle,
            165 * step / 20,
            42 * step / 20,
            colors[i % len(colors)]
        )

    # Centre de la fleur
    radius = 30 * step / 20
    canvas.create_oval(
        cx - radius, cy - radius,
        cx + radius, cy + radius,
        fill="#ffdc38", outline="#e9a600"
    )

    if step < 20:
        root.after(50, lambda: animate_flower(step + 1))
    else:
        canvas.create_text(
            400, 570,
            text="Une fleur pour toi 🌸",
            fill="white", font=("Georgia", 20, "bold")
        )


# Action au clic
def bloom(event):
    canvas.unbind("<Button-1>")
    animate_flower()


show_letter()
root.mainloop()
