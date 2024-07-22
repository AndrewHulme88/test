require 'turtle'

timmy = Turtle.new
screen = Screen.new

def move_forward
  timmy.forward(10)
end

def move_backward
  timmy.backward(10)
end

def turn_left
  timmy.left(10)
end

def turn_right
  timmy.right(10)
end

def reset_drawing
  timmy.clear
  timmy.reset
end

screen.onkey(:w, &method(:move_forward))
screen.onkey(:s, &method(:move_backward))
screen.onkey(:a, &method(:turn_left))
screen.onkey(:d, &method(:turn_right))
screen.onkey(:c, &method(:reset_drawing))

screen.listen
screen.mainloop
