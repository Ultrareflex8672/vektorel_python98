import turtle
import random

# Ekrana çizgi çizdir
def draw_line():
    turtle.forward(100)

# Ekrana kare çizdir
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Kenarları farklı renk bir kare çizdir
def draw_colored_square():
    colors = ['red', 'green', 'blue', 'yellow']
    for color in colors:
        turtle.color(color)
        turtle.forward(100)
        turtle.right(90)

# Desen çizdir
def draw_pattern():
    for _ in range(36):
        draw_square()
        turtle.right(10)

# İki boyutlu bir harf çizdir
def draw_letter():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)

# Sarı renkli bir üçgen oluştur
def draw_yellow_triangle():
    turtle.color('yellow')
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

# Dikdörtgen oluştur (kare olmasın)
def draw_rectangle():
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

# 5 gen oluştur
def draw_pentagon():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)

# 6 gen oluştur
def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)

# Fonksiyonlar ile şekiller çizdir
def draw_shapes():
    draw_line()
    turtle.penup()
    turtle.goto(150, 0)
    turtle.pendown()
    draw_square()
    turtle.penup()
    turtle.goto(300, 0)
    turtle.pendown()
    draw_colored_square()
    turtle.penup()
    turtle.goto(450, 0)
    turtle.pendown()
    draw_pattern()
    turtle.penup()
    turtle.goto(600, 0)
    turtle.pendown()
    draw_letter()
    turtle.penup()
    turtle.goto(750, 0)
    turtle.pendown()
    draw_yellow_triangle()
    turtle.penup()
    turtle.goto(900, 0)
    turtle.pendown()
    draw_rectangle()
    turtle.penup()
    turtle.goto(1050, 0)
    turtle.pendown()
    draw_pentagon()
    turtle.penup()
    turtle.goto(1200, 0)
    turtle.pendown()
    draw_hexagon()

# Bir şekli rastgele noktalara çizdir
def draw_random_shapes():
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_square()

# Kenarları görünmeyen bir kare çiz
def draw_invisible_square():
    turtle.penup()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Bir labirent çizdir
def draw_maze():
    for _ in range(20):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)

# Ekrana rasgele yerlere farklı renkli kareler çizdir
def draw_random_colored_squares():
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        color = random.choice(colors)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        draw_square()

# Kesik çizgili bir altıgen çizdir
def draw_dashed_hexagon():
    for _ in range(6):
        for _ in range(5):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
        turtle.right(60)

# Ana fonksiyon
def main():
    turtle.speed(5)
    draw_shapes()
    turtle.clear()
    draw_random_shapes()
    turtle.clear()
    draw_invisible_square()
    turtle.clear()
    draw_maze()
    turtle.clear()
    draw_random_colored_squares()
    turtle.clear()
    draw_dashed_hexagon()
    turtle.done()

if __name__ == "__main__":
    main()