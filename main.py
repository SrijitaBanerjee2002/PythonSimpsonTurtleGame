# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-2-srijitabanerjee#main.py >
######################################################
import turtle
import random
import math


game_objects = []
s = turtle.Screen()
score=0
level=1

def start_screen():
  turtle.listen()
  turtle.hideturtle()
  s.screensize(300,300)
  s.bgcolor("light blue")
  turtle.penup()
  turtle.goto(-60,0)
  turtle.write("WELCOME!!", align = "left", font = ("Arial",20,'bold'))
  turtle.goto(-80,-20)
  turtle.write("Press spacebar to continue.", align = 'left', font = ("Arial", 15, 'normal')) 
  turtle.onkey(main , "space")
  

#def score_board():
  #turtle.penup()
  #turtle.goto(-130,130)
  #turtle.write("Score: "+str(score), align = "left", font = ("Arial",12,'normal'))
  #turtle.goto(130,130)
  #turtle.write("Level: "+str(level), align = "left", #font = ("Arial",12,'normal'))
  #turtle.hideturtle()
  

  
  
  

  
def end_screen():
  global score
  global level
  #making the start screen
  s.screensize(300,300)
  s.bgcolor("light blue")
  turtle.penup()
  turtle.goto(-60,0)
  turtle.write("GAME OVER!!!", align = 'left', font = ("Arial",20,'bold'))
  
  turtle.goto(-60,-20)
  turtle.write(("Score:"+ str(score)), align = 'left',font = ("Arial", 15,'normal'))
  turtle.goto(-60,-40)
  turtle.write(("Level:"+ str(level)), align = 'left',font = ("Arial", 15,'normal'))
  turtle.hideturtle()


  


def main():
  global game_objects,s,score,level
  
  
  
  

  turtle.clearscreen()
  s.setup(320,320)
  s.screensize(300,300)
  s.bgpic("background.gif")
  w,h = s.screensize()
  s.tracer(0)

  #declaring variables
  no_of_lives = 3
  
  
  
  game_objects = [
    {"t":turtle.Turtle() , "type": "harm", "image":"harmobjects.gif", "radius":10, "speed": 0.1}
  ]
  game_objects.append({"t":turtle.Turtle() , "type": "harm","image":"harmobjects.gif","radius":10,"speed": 0.03})

  game_objects.append({"t":turtle.Turtle() ,  "type": "harm" ,"image":"harmobjects.gif","radius":10,"speed": 0.075})

  game_objects.append({"t":turtle.Turtle() , "type": "harm","image":"harmobjects.gif","radius":10,"speed": 0.105})

  game_objects.append({"t":turtle.Turtle() ,  "type": "harm","image":"harmobjects.gif","radius":10, "speed": 0.025}) #added details of harm objects

  #adding details of the player
  game_objects.append({"t":turtle.Turtle() ,  "type": "player","image":"babysimpson.gif","radius":10, "speed": 0.0})
  
  #adding details of benefit object
  game_objects.append({"t":turtle.Turtle() ,  "type": "donut","image":"donutsimpson.gif","radius":10,"speed": 0.0})

  #some important variables
  
  player_rad = game_objects[5]["radius"]

  for obj in game_objects:
    obj["t"].penup()
    if obj["type"]=="harm":
      obj["t"].goto(random.randint(-w/3,w/2),random.randint(-h/3,h/2))
    elif obj["type"]=="player":
      obj["t"].goto(0,-150)
    elif obj["type"]=="donut":
      obj["t"].goto(0,150)

  
  #print(game_objects)
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])
    print(obj["image"])
    
  
  #adding key press events for player object
  p_turtle = game_objects[5]["t"]
  
  #print(game_objects[5]["t"])
  def up():
    p_turtle.setheading(90)
    p_turtle.forward(5)
    

  def down():
    p_turtle.setheading(270)
    p_turtle.forward(5)
  
  def right():
    p_turtle.setheading(0)
    p_turtle.forward(5)
  
  def left():
    p_turtle.setheading(180)
    p_turtle.forward(5)

  turtle.listen()
  turtle.onkey(up, 'Up')
  turtle.onkey(down, 'Down')
  turtle.onkey(right, 'Right')
  turtle.onkey(left, 'Left')
  
  
  while True:
    #score board
    turtle.penup()
    turtle.goto(-200,150)
    turtle.write("Score: "+str(score), align = "left", font = ("Arial",12,'normal'))
    turtle.goto(-200,130)
    turtle.write("Lives: "+str(no_of_lives), align = "left", font = ("Arial",12,'normal'))
    turtle.goto(-200,110)
    turtle.write("Level: "+str(level), align = "left", font = ("Arial",12,'normal'))
    turtle.hideturtle()
    turtle.clear()
    #game functioning starts here
    for obj in game_objects:
      obj["t"].setheading(0)
      obj["t"].forward(obj["speed"])
      x = obj["t"].xcor()
      y = obj["t"].ycor()
      if x >= 150:
        x = -150
      elif x <= -150:
        x = 150
      obj["t"].goto(x,y)
    #checking for collisions
    player_x = game_objects[5]["t"].xcor()
    player_y = game_objects[5]["t"].ycor()
    #score_board()
    
    for obj in game_objects:
      x = obj["t"].xcor()
      y = obj["t"].ycor()
      if obj["type"]=="harm":
        
        distance = math.dist([player_x,player_y],[x,y])
        if distance < (player_rad+obj["radius"]):
          no_of_lives -= 1
          player_x = 0
          player_y = -150
          p_turtle.goto(player_x,player_y)

      elif obj["type"]=="donut": 
        distance = math.dist([player_x,player_y],[x,y])
        
        
        if distance< (player_rad+obj["radius"]):
          score += 10
          
          player_x = 0
          player_y = -150
          level += 1
          
          p_turtle.goto(player_x,player_y)

          
          
    if no_of_lives == 0:
      turtle.clearscreen()
      end_screen()
      break
      
    s.update()

start_screen()
