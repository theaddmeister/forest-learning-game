import turtle

def draw_forest_canvas():
    screen = turtle.Screen()
    screen.title('Forest Canvas')
    screen.bgcolor('skyblue')

    # Draw ground
    ground = turtle.Turtle()
    ground.color('green')
    ground.penup()
    ground.goto(-400, -200)
    ground.pendown()
    ground.begin_fill()
    for _ in range(2):
        ground.forward(800)
        ground.right(90)
        ground.forward(200)
        ground.right(90)
    ground.end_fill()

    # Draw trees
    def draw_tree(x, y):
        tree_trunk = turtle.Turtle()
        tree_trunk.color('saddlebrown')
        tree_trunk.penup()
        tree_trunk.goto(x, y)
        tree_trunk.pendown()
        tree_trunk.begin_fill()
        for _ in range(2):
            tree_trunk.forward(20)
            tree_trunk.right(90)
            tree_trunk.forward(50)
            tree_trunk.right(90)
        tree_trunk.end_fill()

        tree_leaves = turtle.Turtle()
        tree_leaves.color('forestgreen')
        tree_leaves.penup()
        tree_leaves.goto(x - 30, y + 50)
        tree_leaves.pendown()
        tree_leaves.begin_fill()
        tree_leaves.setheading(60)
        for _ in range(3):
            tree_leaves.forward(60)
            tree_leaves.left(120)
        tree_leaves.end_fill()

    # Draw multiple trees
    for i in range(-360, 400, 80):
        draw_tree(i, -150)

    turtle.done()

draw_forest_canvas()