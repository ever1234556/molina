import turtle

# Configuración inicial de la ventana
screen = turtle.Screen()
screen.title("Luna con Estrella")
screen.bgcolor("midnightblue")
screen.setup(width=800, height=600)

# Crear la tortuga para dibujar
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# ---------- Función para dibujar la luna ----------
def draw_moon(x, y, radius):
    """Dibuja una luna creciente en la posición (x, y) con el radio dado."""
    pen.up()
    pen.goto(x, y - radius)          # Posicionar en el borde inferior del círculo
    pen.setheading(0)
    pen.color("white")
    pen.begin_fill()
    pen.circle(radius)               # Círculo principal (luna llena)
    pen.end_fill()

    # Recorte para crear el efecto de luna creciente
    pen.up()
    pen.goto(x + radius * 0.4, y - radius)  # Desplazamiento del círculo de recorte
    pen.setheading(0)
    pen.color("midnightblue")
    pen.begin_fill()
    pen.circle(radius * 0.9)          # Círculo de recorte (color de fondo)
    pen.end_fill()

# ---------- Función para dibujar una estrella ----------
def draw_star(x, y, size, color="yellow"):
    """Dibuja una estrella de 5 puntas centrada en (x, y)."""
    pen.up()
    pen.goto(x, y)
    pen.setheading(90)               # Orientación inicial
    pen.color(color)
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)               # Ángulo interno de la estrella
    pen.end_fill()

# Dibujar la luna
draw_moon(x=-150, y=50, radius=120)

# Dibujar varias estrellas alrededor de la luna
star_positions = [
    (-250, 180, 30),
    (-80, 200, 25),
    (-30, 120, 20),
    (-180, -20, 22),
    (0, 250, 28),
    (120, 180, 24),
    (200, 80, 30)
]

for x, y, size in star_positions:
    draw_star(x, y, size)

# Esperar a que el usuario cierre la ventana
turtle.done()