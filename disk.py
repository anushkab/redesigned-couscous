from simplegraphics import *
MakeWindow(10,bgcolor=WHITE)
x = -4
r = 4
DrawDisk(x,0,r,FillColor=MAGENTA,EdgeWidth=0)
x = x + 1.5*r
r = r/2
DrawDisk(x,0,r,FillColor=CYAN,EdgeWidth=0)
x = x + 1.5*r
r = r/2
DrawDisk(x,0,r,FillColor=MAGENTA,EdgeWidth=0)
x = x + 1.5*r
r = r/2
DrawDisk(x,0,r,FillColor=CYAN,EdgeWidth=0)
DrawDisk(x,0,r,FillColor=CYAN,EdgeWidth=0)
ShowWindow()