import pymaze
from aStar import *
from pymaze import maze,agent,textLabel,COLOR

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))

if __name__=='__main__':

    m=maze(20,20)

    m.CreateMaze(theme=COLOR.light, loopPercent=75)


    searchPath,aPath,fwdPath=aStar(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red)

    m.tracePath({a:searchPath},delay=50)
    m.tracePath({b:aPath},delay=50)
    m.tracePath({c:fwdPath},delay=50)

    l=textLabel(m,'A Star Tamanho do caminho',len(fwdPath)+1)
    l=textLabel(m,'A Star Tamanho da busca',len(searchPath))
    m.run()

