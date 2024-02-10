from numpy import random
import numpy as np
import unittest

class Board():
    def __init__(self):
        self.emptyTile = 0
        self.size = 3
        self.positions = self.Positions()
        self.tiles = self.Tiles()
        self.moves = self.Possiblemoves()


    #    assign random placements to each tile return dictionary with all placements
    # takes tiles and points to positions
    def Positions(self):
        arr = [i for i in range(1,self.size**2)]
        random.shuffle(arr)

        permdict = dict()
        for i,j in enumerate(arr):
            permdict[i] = j
        permdict[self.emptyTile]=0
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
    def move(self, moveAttempt):
        if move in self.moves:
            if move == "up":
                newPos = self.emptyTile-self.size
                self.positions[self.tiles[newPos]],self.positions[emptyTile]=newPos+self.emptyTile, newPos
            elif move =="down":
                newPos = self.emptyTile + self.size
                self.positions[self.tiles[newPos]], self.positions[emptyTile] = newPos + self.emptyTile, newPos
            elif move =="right":
                self.emptyTile-=1
            elif move =="left":
                self.emptyTile+=1
            self.Tiles()
        else:
            print("invalid move")


        pass


# todo: define tests for moves
class TestBoardMethods(unittest.TestCase):
    def test_Positions(self):
        b = Board()
        self.assertEquals(b.emptyTile,0)
        self.assertEquals(b.size**2-1,len(b.positions))
    def test_moves(self):
        b = Board()

        self.assertEqual(b.moves,["right","down"])
    def test_Tiles(self):
        b = Board()
        self.assertEquals(b.positions[0],b.tiles[b.positions[0]])



if __name__ == '__main__':
    unittest.main()