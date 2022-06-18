#!/usr/bin/python3

import sqlite3
import re
import random

def getMap():
    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM map WHERE id = 1')
    query = cur.fetchall()[0][1]
    query = query.split("\n")
    mapa = []
    for i in range(len(query)):
        mapa.append(query[i].split(' '))
        mapa[i] = [m for m in mapa[i] if m != '' ]
    mapa = [m for m in mapa if m != []]
    
    cur.execute('select * from attraction')
    attrs = cur.fetchall()
    attrs_dict = {}
    for i in attrs:
        attrs_dict[str(i[0])] = i[1]

    conn.close()

    return mapa, attrs_dict

def saveMap(mapa, vis, visStatus):
    string = ''
    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            string += mapa[x][y]+' '
        string += "\n"

    conn = sqlite3.connect('../database.db')
    cur = conn.cursor()
    cur.execute('update map set content ="'+string+'" where id = 1')
    
    if visStatus != None:
        cur.execute('update visitor set status = "'+str(visStatus)+'" where id = '+str(vis))

    conn.commit()
    conn.close()


def updatePosition(mapa, id_vis, pos, newPos):
    visStatus = None
    if newPos != -1 and int(mapa[newPos[0]][newPos[1]]) < 0:
        return mapa, pos

    if newPos == -1:
        mapa = [ m if m != '-'+str(id_vis) else '0' for m in mapa]
        saveMap(mapa, id_vis, 'disconnected')
        return 
        

    for x in range(len(mapa)):
        for y in range(len(mapa[x])):
            if mapa[x][y] == "-"+str(id_vis):
                mapa[x][y] = '0'
            if x == newPos[0] and y == newPos[1]:
                if mapa[x][y] == '0':
                    visStatus = "walking"
                    mapa[x][y] = "-"+str(id_vis)
                else:
                    visStatus = str(mapa[x][y])

    saveMap(mapa, id_vis, visStatus)
    
    return mapa, newPos

def getRandomEmpty(mapa):
    x = random.randrange(0,19)
    y = random.randrange(0,19)

    while mapa[x][y] != '0':
        x = random.randrange(0,19)
        y = random.randrange(0,19)
        
    return [x,y]
