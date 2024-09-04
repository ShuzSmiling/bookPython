import turtle

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200
RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180
LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20
MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0
RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20
LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180
RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140


turtle.setup(500, 600)
turtle.hideturtle()
turtle.penup()

# левое плечо
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.write('Бетельгейзе')

# правое плечо
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.write('Хатиса')

# левая звезда на поясе
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.write('Альнитак')

# средняя звезда на поясе
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.write('Альнилам')

# правая звезда на поясе
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.write('Минтака')

# левое колено
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.write('Саиф')

# правое колено
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()
turtle.write('Ригель')

# линия из левого плеча в левое колено через левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# линия из правого плеча в правое колено через правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

# линия из правой звезды пояса в левую звезду пояса
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()


turtle.done()

