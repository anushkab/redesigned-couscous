from simplegraphics import *

n = 5
MakeWindow(n, bgcolor=CYAN, labels=False)
x=0; y=0; L=5; W=3
DrawRect(x,y,L,W,FillColor=GREEN,EdgeWidth=2,theta=45)
ShowWindow()