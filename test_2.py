
import tkinter as tk
import math
import random

WIDTH = 1000
HEIGHT = 700
COLS = 100
ROWS = 42

root = tk.Tk()
root.title("Special Letter ❤️")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="black")
root.resizable(False, False)

canvas = tk.Canvas(
    root, width=WIDTH, height=HEIGHT,
    bg="black", highlightthickness=0
)
canvas.pack()

symbols = "@#$%&*+=-:."
heart_colors = ["#ffcc99", "#ffad66", "#ff8050",
                "#ff5733", "#ff3030"]
flower_colors = ["#ffb6d9", "#ff80bf", "#ff4fa3",
                 "#ff267e", "#ffda55"]

mode = "letter"
animation = 0
particles = []


def draw_text(x, y, text, color, size=15):
    canvas.create_text(
        x, y, text=text, fill=color,
        font=("Courier New", size, "bold"),
        tags="ui"
    )


# Forme mathématique du cœur
def heart(x, y):
    return (
        (x*x + y*y - 1)**3 - x*x*y**3
    ) <= 0


# Forme de la fleur
def flower(x, y, progress):
    distance = math.sqrt(x*x + y*y)
    angle = math.atan2(y, x)

    radius = (0.85 + 0.32 * math.cos(6 * angle))
    radius *= progress

    petals = distance <= radius

    stem = (
        abs(x) < 0.065
        and 0.9 < y < 2
        and progress >= 0.8
    )

    leaf = (
        ((x + 0.22) / 0.3)**2
        + ((y - 1.35) / 0.13)**2 < 1
        or
        ((x - 0.22) / 0.3)**2
        + ((y - 1.65) / 0.13)**2 < 1
    )

    return petals, stem, leaf and progress >= 0.8


# Dessiner en caractères ASCII
def render_art(shape, progress=1):
    canvas.delete("art")

    for row in range(ROWS):
        line = ""
        color = "#ffad66"

        for col in range(COLS):
            x = (col - COLS / 2) / 30
            y = (row - ROWS / 2) / 13

            if shape == "heart":
                inside = heart(x, -y)
                stem = False
                leaf = False
                palette = heart_colors
            else:
                inside, stem, leaf = flower(x, y, progress)
                palette = flower_colors

            if inside:
                char = random.choice(symbols)
                index = min(
                    len(palette) - 1,
                    int((abs(x) + abs(y)) * 2)
                )
                color = palette[index]

            elif stem or leaf:
                char = random.choice("|||/\\")
                color = "#39a852"

            else:
                char = " "

            line += char

        canvas.create_text(
            WIDTH // 2, 100 + row * 13,
            text=line,
            fill=color,
            font=("Courier New", 10, "bold"),
            tags="art"
        )

    if shape == "heart":
        canvas.tag_bind("art", "<Button-1>", start_flower)


# Création des particules
def create_particles():
    for i in range(90):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        size = random.choice([2, 3, 4])
        speed = random.uniform(0.5, 2)

        particle = canvas.create_oval(
            x, y, x + size, y + size,
            fill="#ffad66",
            outline="",
            tags="particles"
        )

        particles.append({
            "id": particle,
            "speed": speed,
            "size": size
        })


# Animation des particules
def animate_particles():
    colors = [
        "#ffad66", "#ff8050",
        "#ff4fa3", "#ffffff",
        "#ffcc99"
    ]

    for p in particles:
        item = p["id"]
        canvas.move(item, random.uniform(-0.5, 0.5),
                    -p["speed"])

        x1, y1, x2, y2 = canvas.coords(item)

        if y2 < 0:
            x = random.randint(0, WIDTH)
            canvas.coords(
                item, x, HEIGHT,
                x + p["size"], HEIGHT + p["size"]
            )

        if random.random() < 0.08:
            canvas.itemconfig(
                item,
                fill=random.choice(colors)
            )

    root.after(40, animate_particles)


# Afficher la lettre
def show_letter():
    draw_text(
        WIDTH // 2, 55,
        "A SPECIAL LETTER",
        "#ffb36b", 24
    )

    draw_text(
        WIDTH // 2, 100,
        "There is something special for you...",
        "#ffcc99", 15
    )

    render_art("heart")

    draw_text(
        WIDTH // 2, 660,
        "CLICK ON THE HEART ❤️",
        "#ff603b", 17
    )


# Transformation en fleur
def start_flower(event=None):
    global mode, animation

    if mode != "letter":
        return

    mode = "flower"
    animation = 0
    canvas.delete("ui")
    animate_flower()


def animate_flower():
    global animation

    animation += 1
    progress = min(animation / 35, 1)

    render_art("flower", progress)

    canvas.delete("ui")

    draw_text(
        WIDTH // 2, 55,
        "JUST FOR YOU",
        "#ff80bf", 23
    )

    if animation < 35:
        root.after(60, animate_flower)
    else:
        draw_text(
            WIDTH // 2, 660,
            "A FLOWER FOR YOU 🌸",
            "#ffb6d9", 20
        )


create_particles()
show_letter()
animate_particles()

root.mainloop()
