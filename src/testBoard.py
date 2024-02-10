import unittest


class TestBoardMethods(unittest.TestCase):
    def test_Positions(self):
        b = Board()
        self.assertEqual(b.emptyTile,0)
        self.assertEqual(b.size**2-1,len(b.positions))
    def test_moves(self):
        b = Board()
        self.assertEqual(b.moves,["right","down"])

    def test_move(self):
        b = Board()
        tile1 = b.tiles[1]
        b.move("right")
        self.assertEqual(b.emptyTile,1)
        self.assertEqual(b.positions[0],1)
        self.assertEqual(b.tiles[1],0)
        self.assertEqual(b.tiles[0], tile1)
    def test_move2(self):
        b =Board()
        b.move("down")
        self.assertEquals(b.emptyTile,b.size)
        self.assertEquals(b.positions[0],b.size)

    def test_move3(self):
        b=Board()
        b.move("up")
        self.assertEquals(b.emptyTile,0)
        self.assertEquals(b.positions[0],0)
    def test_Tiles(self):
        b = Board()
        self.assertEquals(b.positions[0],b.tiles[b.positions[0]])


if __name__ == '__main__':
    unittest.main()
