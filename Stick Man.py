import turtle

def main():
  turtle.speed(1)
  jim = turtle.Turtle() #Remember the capital T
  jim.speed(1) #A speed of 0 makes him go as fast as possible

  arm_length = 100 #Change these if you want
  leg_length = 120

  def reset(): #reset sends him back to the center
    jim.pu() #pu is short for penup. Either work, you can use them interchangeably
    jim.setpos(0,0)
    jim.pd() #pd is short for pendown


  #draw a stickman

  reset()

  #head
  jim.seth(90) #seth is short for set_heading, and it changes the direction jim is facing.
  jim.fd(30)
  jim.rt(90)
  jim.circle(50)

  reset()

  #arm 1
  jim.seth(160)
  jim.fd(arm_length/2)
  jim.rt(20)
  jim.fd(arm_length/2)

  reset()

  #arm 2
  jim.seth(20)
  jim.fd(arm_length/2)
  jim.lt(20)
  jim.fd(arm_length/2)

  reset()

  #leg 1
  jim.seth(270)
  jim.fd(50)
  jim.seth(230)
  jim.fd(leg_length/2)
  jim.lt(40)
  jim.fd(leg_length/2)

  reset()

  #leg 2
  jim.seth(270)
  jim.fd(50)
  jim.seth(310)
  jim.fd(leg_length/2)
  jim.rt(40)
  jim.fd(leg_length/2)

main()