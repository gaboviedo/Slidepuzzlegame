from numpy import random
import numpy as np
import unittest

class Board():
    def __init__(self):
        self.emptyTile = 0 # initial positioning of empty tile
        self.size = 3 #
        self.positions = self.Positions() #dictionary that takes key  vals and points to positions
        self.tiles = self.Tiles() #inversion of positions, points to tiles
        self.moves = self.Possiblemoves() #defines possible moves given tile positions


    #    assign random placements to each tile return dictionary with all placements
    # takes tiles and points to positions
    def Positions(self):
        arr = [i for i in range(1,self.size**2)]
        random.shuffle(arr)

        permdict = dict()
        for i,j in enumerate(arr):
            permdict[i] = j
        permdict[0]=self.emptyTile
        return permdict


    # return dictionary that takes positions points to tiles
    def Tiles(self):
        inv_map = {v: k for k, v in self.positions.items()}
        return inv_map


    # assign possible moves
    def Possiblemoves(self):
        size = self.size
        moves = ["left","right","up","down"]
        if self.emptyTile%size==0:
            moves.remove("left")
        if self.emptyTile%size==size-1:
            moves.remove("right")
        if self.emptyTile<size-1:
            moves.remove("up")
        if self.emptyTile>size**2-size:
            moves.remove("down")

        return moves


    # attempt to move empty space
    # TO DO: define moves: swap empty with correct tile
    def move(self, move):
        if move in self.moves:
            if move == "up":
                newPos = self.emptyTile-self.size
                self.positions[self.tiles[newPos]],self.positions[self.emptyTile]=newPos+self.emptyTile, newPos
                self.emptyTile=newPos
            elif move =="down":
                newPos = self.emptyTile + self.size
                self.positions[self.tiles[newPos]], self.positions[self.emptyTile] = newPos - self.emptyTile, newPos
                self.emptyTile=newPos
            elif move =="right":
                newPos = self.emptyTile +1
                print(newPos)
                self.positions[self.tiles[newPos]], self.positions[self.emptyTile] = newPos -1, newPos
                self.emptyTile=newPos
            elif move =="left":
                newPos=self.emptyTile-1
                self.positions[self.tiles[newPos]], self.positions[self.emptyTile] = newPos +1, newPos
                self.emptyTile = newPos
            self.tiles =self.Tiles()
        else:
            print("invalid move")










if __name__ == '__main__':
    unittest.main()