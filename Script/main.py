from graphics import Canvas
import math as mt 
import time    
CANVAS_WIDTH = 2000
CANVAS_HEIGHT =1000
SIZE=230
Pi=3.1416

#Gravitional accelarations
gme=3.61
gv=8.83
ge=9.81
gm=3.75
gj=26
gs=11.2
gu=10.5
gn=13.3

delay=.01
#initial velocity and angle with horizontal for projectile
v=110
theta=(45*Pi)/180

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0,0,2000,800)
    canvas.create_line(0,CANVAS_HEIGHT-200 ,CANVAS_WIDTH, CANVAS_HEIGHT-200)
    planet_box=canvas.create_rectangle(20,CANVAS_HEIGHT-180, 200, CANVAS_HEIGHT-20,'black')
    
    canvas.create_text(40, 890, font='Consolas', font_size = 25, text='CLICK HERE', color='white')
   
    #CIP logo and text
    image = canvas.create_image_with_size(1850, 830,60, 100,'CIP.jpg')
    CIP=canvas.create_text(1800, 950, font='Arial', font_size = 20, text='Code in Place 2023', color='black')
    
    ## Intro screen texts
    design=canvas.create_rectangle(420,230,520,420,'white')
    explo=canvas.create_text(650, 250, font='Consolas', font_size = 60, text='SOLAR SYSTEM EXPLORATION &', color='white')
    dyna=canvas.create_text(650, 350, font='Consolas', font_size = 60, text='DYNAMICS SIMULATOR', color='white')
    
    ##nasa logo
    intro = canvas.create_image_with_size(400, 200,250, 250,'nasa logo.png')
    pendulum=canvas.create_image_with_size(600, 500,270, 180,'pen.jpg')
    pen=canvas.create_text(700, 680, font='Consolas', font_size = 20, text='PENDULUM', color='white')
    projectile=canvas.create_image_with_size(1000, 500,360, 140,'pro.jpg')
    pro=canvas.create_text(1100, 680, font='Consolas', font_size = 20, text='PROJECTILE', color='white')
    ##to show all planet
    show_planets(canvas,planet_box)
    
    while True:
        canvas.delete(intro)
        canvas.delete(explo)
        canvas.delete(dyna)
        canvas.delete(design)
        canvas.delete(pendulum)
        canvas.delete(projectile)
        canvas.delete(pro)
        canvas.delete(pen)
        
        
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        
        p_x=30
        p_y=700
        mercury,venus,earth,mars,jupiter,saturn,uranus,naptune=planet_projectile(canvas,p_x,p_y)
        
        graphic(canvas,370,400,800,830,x,y,mercury,p_x,p_y,v,theta,gme)
        graphic(canvas,590,620,800,830,x,y,venus,p_x,p_y,v,theta,gv)
        graphic(canvas,810,840,800,830,x,y,earth,p_x,p_y,v,theta,ge)
        graphic(canvas,1030,1060,800,830,x,y,mars,p_x,p_y,v,theta,gm)
        graphic(canvas,370,400,900,930,x,y,jupiter,p_x,p_y,v,theta,gj)
        graphic(canvas,590,620,900,930,x,y,saturn,p_x,p_y,v,theta,gs)
        graphic(canvas,810,840,900,930,x,y,uranus,p_x,p_y,v,theta,gu)
        graphic(canvas,1030,1060,900,930,x,y,naptune,p_x,p_y,v,theta,gn)
    
    
    
    
    
    
    
######  HELPER FUNCTIONS ####

#1.Grraphics
def graphic(canvas,l_x,r_x,t_y,b_y,x,y,planet,p_x,p_y,v,theta,g):
    if l_x<=x<=r_x and t_y<=y<=b_y:
        slect_button= canvas.create_image_with_size(l_x, t_y+10, 30, 30, 'select.png')
        xs=x
        ys=y
        print(xs,ys)
        #canvas.wait_for_click()
        box=canvas.create_rectangle(1300,810,1600,890,'black')
        text=canvas.create_text(1400,840,font='Arial', font_size = 20, text='PROJECTILE', color='white')
        box=canvas.create_rectangle(1300,910,1600,990,'black')
        text=canvas.create_text(1400,940, font='Arial', font_size = 20, text='PENDULUM', color='white')
        image=details(canvas,g)
        while True:
            canvas.wait_for_click()
            m = canvas.get_mouse_x()
            n = canvas.get_mouse_y()
            print('a',m,n)
            
            
            if 1300<=m<=1600 and 910<=n<=990:
                canvas.delete(image)
                pendulum(canvas,g)
                continue
              
            elif 1300<=m<=1600 and 810<=n<=890:
                canvas.delete(image)
                axis=canvas.create_line(30,700,30,800,'white')
                axis=canvas.create_line(40,710,30,700,'white')
                axis=canvas.create_line(20,710,30,700,'white')
                axis=canvas.create_line(130,790,140,800,'white')
                axis=canvas.create_line(130,810,140,800,'black')
                animation(canvas,planet,p_x,p_y,v,theta,g)
                continue
    
            
                    
#2.To show the detail picture of a planet.
def details(canvas,g):
    if g==3.61:
        image = canvas.create_image_with_size(0,0,2000, 800,'mercury.jpg')
    if g==8.83:
        image = canvas.create_image_with_size(0,0,2000, 800,'venus.jpg')
    if g==9.81:
        image = canvas.create_image_with_size(0,0,2000, 800,'earth.jpg')
    if g==3.75:
        image = canvas.create_image_with_size(0,0,2000, 800,'mars.jpg')
    if g==26.0:
        image = canvas.create_image_with_size(0,0,2000, 800,'jupiter.jpg')
    if g==11.2:
        image = canvas.create_image_with_size(0,0,2000, 800,'saturn.jpg')
    if g==10.5:
        image = canvas.create_image_with_size(0,0,2000, 800,'uranus.jpg')
    if g==13.3:
        image = canvas.create_image_with_size(0,0,2000, 800,'neptune.jpg')
    return image
    

#3.To choose a planet 
def select_planet(canvas):
    
    while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        print('b',x,y)
        i_x,i_y=20,20
        if 200<=x<=400 and 810<=y<=890:
            #rcanvas.wait_for_click()
            icon=canvas.create_rectangle(400+i_x, 820+i_y,40, 40,'white')
            
            

#4.To show all planet option box
def show_planets(canvas,planet_box):
      while True:
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        time.sleep(0)
        print('c',x,y)
        if x>=20 and x<=200 and y>=820 and y<=1000:
            #click=canvas.wait_for_click()
            canvas.delete(planet_box)
            all_planets(canvas)
            break
 
 
 
##5 Planet projectile objects 
def planet_projectile(canvas,p_x,p_y):
    mercury=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    venus=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    earth=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    mars=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    jupiter=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    saturn=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    uranus=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    naptune=canvas.create_oval(p_x, CANVAS_HEIGHT-SIZE,p_x+30,CANVAS_HEIGHT-200,'white')
    return mercury,venus,earth,mars,jupiter,saturn,uranus,naptune 
        
#5.1.all planets 
def all_planets(canvas):
    Mercury=a_planet(canvas,200,810,400,890,'MERCURY')
    venus=a_planet(canvas,420,810,620,890,'VENUS')
    earth=a_planet(canvas,640,810,840,890,'EARTH')
    mars=a_planet(canvas,860,810,1060,890,'MARS')
    jupiter=a_planet(canvas,200,910,400,990,'JUPITER')
    saturn=a_planet(canvas,420,910,620,990,'SATURN')
    uranus=a_planet(canvas,640,910,840,990,'URANUS')
    naptune=a_planet(canvas,860,910,1060,990,'NAPTUNE')
    image = canvas.create_image_with_size(10, 820,180, 180,'nasa logo.png')
    
    i_y=0
    x=370
    for i in range(4):
        y=810+i_y
        icon=canvas.create_rectangle(x,y,x+30,y+30,'white')
        x+=220
    x=370
    for j in range(4):
        y=910+i_y
        icon=canvas.create_rectangle(x,y,x+30, y+30,'white')
        x+=220
    
    return Mercury#,venus,earth,mars,jupiter,saturn,uranus,naptune


#6.Single planet    
def a_planet(canvas,x1,y1,x2,y2,planets):
    
    X=(x1+x2)/2-40
    Y=(y1+y2)/2-10
    box=canvas.create_rectangle(x1,y1,x2,y2,'black')
    text=canvas.create_text(X,Y, font='Arial', font_size = 20, text=planets, color='white')
    outline=canvas.set_outline_color(box, 'blue')
    return box

#7.Projectile Animation
def animation(canvas,projectile,x,y,v,theta,g):
    max_h=((v*mt.sin(theta))**2)/(2*g)
    
    max_r= (v*v*mt.sin(2*theta))/g
    T=(2*(v*(mt.sin(theta))))/g
    
    monitor=canvas.create_rectangle(1500,0,2000,400)
    monitor=canvas.create_rectangle(1505,3,1995,30,'white')
    canvas.create_text(1515,6,font='Consolas',font_size=25,text='::Monitor',color='black')
    maximum_hieght=canvas.create_text(1550,50,font='Consolas ', font_size = 25,text='>>> Max_Height = '+str(round(max_h, 3))+' m',color='white')
    Horizontal_range=canvas.create_text(1550,100,font='Consolas', font_size = 25,text='>>> Hor_Range = '+str(round(max_r, 3))+' m',color='white')
    time_traveled=canvas.create_text(1550,150,font=' Consolas', font_size = 25,text='>>> Flight_Time = '+str(round(T, 3))+' s',color='white')
    xy=canvas.create_text(1550,200,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(0, 1))+','+str(round(0, 1)),color='white')
    a=mt.tan(theta)
    b=(g/(2*v*v))*((mt.cos(theta))**-2)
    R,r=R_r(a,b)
    canvas.delete(xy)
    print(R,r)
    
    while x<=r:
        y=-(a*x-b*x*x)
        y+=800
        y=int(y)
        x+=2
        print(x,y)
        xy=canvas.create_text(1550,200,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(x, 1))+','+str(round(-y+770, 1)),color='white')
        canvas.moveto(projectile, x, y)
        canvas.create_oval(x+14,y+14,x+16,y+16,'white')
        time.sleep(delay)
        canvas.delete(xy)
    
    while x>=r and x<R and y<=770:
        
        y=-(a*x-b*x*x)
        y+=800
        y=int(y)
        x+=2
        print(x,y)
        xy=canvas.create_text(1550,200,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(x, 1))+','+str(round(-y+770, 1)),color='white')
        canvas.moveto(projectile, x, y)
        canvas.create_oval(x+14,y+14,x+16,y+16,'white')
        time.sleep(delay)
        canvas.delete(xy)

    print('MAximum Hieght:')
  
## 8.Get horizontal range of projectile by gradient descent 
def R_r(a,b):
    X=0  
    dy=1
    for i in range(50000):
        dy=a-2*b*X
        X=X+.1*dy
        
    r=X
    R=2*r
    #H_max=-(a*x-b*x*x)
    #print(H_max)
    return R,r
    
#9..Get horizontal range of projectile by without gradient descent
def R_max(v,theta,g,x):
    theta=(Pi/180)*theta
    R=(v*v*mt.sin(2*theta))/g
    return R
    
 
#10.Pendulum Animation 
def pendulum(canvas,g):
    period=2*Pi*((1/g)**.5)
    Delay=period/66
    frequency=1/period
    x=100
    y=0
    
    monitor=canvas.create_rectangle(1500,0,2000,400)
    monitor=canvas.create_rectangle(1505,3,1995,30,'white')
    canvas.create_text(1515,6,font='Consolas',font_size=25,text='::Monitor',color='black')
    
    bob = canvas.create_oval(x, y, x+20, y+20,'white')
    cable=canvas.create_line(400,200,400,550,'white')
    beam=canvas.create_line(300,200,500,200,'white')
    holder=canvas.create_oval(395,195,405,205,'white')
    
    #constant=canvas.create_text(750,100,font='Arial', font_size = 50,text='Amplitude and cable length are constant for all planets')
    period=canvas.create_text(1515,50,font='Consolas', font_size = 25,text='>>> Time Period'+' ,'+'T = '+str(round(period, 3))+' Sec',color='white')
    frequency=canvas.create_text(1515,100,font='Consolas', font_size = 25,text='>>> Frequency'+' ,'+'f = '+str(round(frequency, 3))+' Hz',color='white')
    #maximum_hieght=canvas.create_text(1550,50,font='Consolas ', font_size = 25,text='>>> Max_Height = '+str(round(period, 3))+' m',color='white')
    
    #xy=canvas.create_text(1515,150,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(0, 1))+','+str(round(0, 1)),color='white')
    
    
    while True:
        canvas.delete(cable)
        x=400
        y=200
        for i in range(62):
            canvas.create_line(x,y,x,y+2,'white')
            y+=5
        first_half(canvas,bob,cable,delay)
        second_half(canvas,bob,cable,delay)
        
    
#11.To get first half cycle of pendulum   
def first_half(canvas,bob,cable,Delay):
    count=0
    x=100
    y=0
    s=1
    while True:
        if x<=400:
            canvas.delete(cable)
            y=(400**2-(x-400)**2)**.5+100
            canvas.moveto(bob,x, y)
            cable = canvas.create_line(400, 200, x+10,y,'white')
            canvas.create_oval(x+6,y+6,x+8,y+8,'white')
            
            xy=canvas.create_text(1515,150,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(x, 1))+','+str(round(y, 1)),color='white')
            time.sleep(Delay)
            canvas.delete(xy)
            x+=s
            s+=.5
            count+=1
           
        if x>=397:
            canvas.delete(cable)
            x=400
            s=17
            break
       
            
    #x=400
    #s=17
    while True:    
        if 400<=x<=700:
            canvas.delete(cable)
            y=(400**2-(x-400)**2)**.5+100
            cable = canvas.create_line(400, 200, x+5,y,'white')
            canvas.moveto(bob, x, y)
            canvas.create_oval(x+6,y+6,x+8,y+8,'white')
            xy=canvas.create_text(1515,150,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(x, 1))+','+str(round(y, 1)),color='white')
            time.sleep(Delay)
            canvas.delete(xy)
            x+=s
            s-=.5
            count+=1
        if x>=697:
            canvas.delete(cable)
            x=697
            break
        
    #return x   
#12.To get second half cycle of Pendulum       
def second_half(canvas,bob,cable,Delay): 
        count=0
        x=697
        y=0
        s=1
        while True: 
            if 400<=x<=700:
                canvas.delete(cable)
                y=(400**2-(x-400)**2)**.5+100
                cable= canvas.create_line(400, 200, x+5,y,'white')
                canvas.moveto(bob, x, y)
                xy=canvas.create_text(1515,150,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(x, 1))+','+str(round(y, 1)),color='white')
                time.sleep(Delay)
                canvas.delete(xy)
                x-=s
                s+=.5
                count+=1
                
            if x<=400:
                canvas.delete(cable)
                x=400
                s=17
                break
            
        
        #x=400
        #s=17
        while True:
            if x<=400:
                canvas.delete(cable)
                y=(400**2-(x-400)**2)**.5+100
                cable = canvas.create_line(400, 200, x+15,y,'white')
                canvas.moveto(bob, x, y)
                xy=canvas.create_text(1515,150,font='Consolas', font_size = 25,text='>>> (x,y) = '+str(round(x, 1))+','+str(round(y, 1)),color='white')
                time.sleep(Delay)
                canvas.delete(xy)
                x-=s
                s-=.5
                count+=1
                
            if x<=102.5:
                canvas.delete(cable)
                break
            
            
              
   
    
    
    

if __name__ == '__main__':
    main()