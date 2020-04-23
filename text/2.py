import pyxel

class Vec:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

class Cat:
    def __init__(self, img_id):
        self.pos = Vec(0,0)
        self.img_id = img_id
        
    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y


class App:
    def __init__(self):
        pyxel.init(160, 120, caption='Hello pyxel')
        pyxel.image(0).load(0, 0, '../assets/cat_16x16.png')

        self.cat = Cat(0)

        pyxel.run(self.update, self.draw)


    def update(self):
        #Qを押したら終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.cat.update(30,30)
            
    def draw(self):
        pyxel.cls(0)
        # 猫を表示
        pyxel.blt(self.cat.pos.x, self.cat.pos.y, self.cat.img_id, 0, 0, 16, 16, 13)
        #テキスト表示
        pyxel.text(120/2 -15, 120/2 - 10, 'Hello Pyxel', pyxel.frame_count % 16)

App()        

