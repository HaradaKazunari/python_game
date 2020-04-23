import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption='Hello pyxel')
        pyxel.image(0).load(0, 0, '../assets/cat_16x16.png')

        pyxel.run(self.update, self.draw)


    def update(self):
        #Qを押したら終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
    def draw(self):
        pyxel.cls(0)
        # 猫を表示
        pyxel.blt(16, 16, 0, 0, 0, 16, 16, 11)
        #テキスト表示
        pyxel.text(120/2 -15, 120/2 - 10, 'Hello Pyxel', pyxel.frame_count % 16)

App()        
