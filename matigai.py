import pyxel 
import random
import time

WINDOW_W = 160
WINDOW_H = 120
CAT_W = 16
CAT_H = 16
ENEMY_W = 12
ENEMY_H = 12
CIRC_SIZE = 10
NUMBER_OF_MOUSE = 2 
GAME_OVER = 1

class vec:
    #座標
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Img:
    def __init__(self, img_id):
        self.pos = vec(0, 0)
        self.img_id = img_id
        self.draw_flag = 0

    def update(self, x, y, a, flag):
        self.pos.x = x
        self.pos.y = y
        self.img_a = a
        #1 = maru   2 = batu
        self.draw_flag = flag

class Score:
    def __init__(self):
        self.point = 0

    def update(self, point):
        self.point += point

class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/cat_16x16.png")
        pyxel.image(1).load(0, 0, "assets/animal_mouse.gif")

        self.set()

        pyxel.run(self.update, self.draw)


    def Random(self,x):
        # 最初と最後、30狭めて16の倍数で乱数を生成
       return random.randrange(32,x - 32,16)

    def set(self):
        #フラグ管理
        #ネズミが一定数になったら表示しないようにする
        self.mouse_flag = 0
        #NUMBER_OF_MOUSE　＝ game_over_flag GameOver
        self.game_over_flag = 0
        #ネコを表示で1、猫をクリックで0
        self.cat_flag = 0
        #マル表示フラグ
        self.maru_flag = 0
        #インスタンス生成
        self.cat = Img(0)
        self.mouses = []
        self.score = Score()
        #バツフラグのカウント
        self.batu_count = 0

    def reset(self):
        #ネズミが一定数になったら表示しないようにする
        self.mouse_flag = 0
        self.mouses = []
        #NUMBER_OF_MOUSE　＝ game_over_flag GameOver
        self.game_over_flag = 0
        #ネコを表示で1、猫をクリックで0
        self.cat_flag = 0
        #マル表示フラグ
        self.maru_flag = 0
        #バツフラグのカウント
        self.batu_count = 0


    def update(self):
        #ゲームオーバー後に左クリックしたら
        if self.game_over_flag == GAME_OVER and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.set()

        #マルを表示したら
        if self.maru_flag != 0:
            time.sleep(1)
            self.reset()

        #q_keyをおしたら終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #マウスポインタ表示
        pyxel.mouse(True)

        #猫とネズミの座標
        if self.cat_flag != 1:
            self.cat_flag = 1
            x = self.Random(WINDOW_W)
            y = self.Random(WINDOW_H)
            self.cat.update(x,y,13,0)

        if self.mouse_flag != 1 and len(self.mouses) < 1:
            for i in range(NUMBER_OF_MOUSE):
                x = self.Random(WINDOW_W)
                y = self.Random(WINDOW_H)

                new_mouse = Img(1)
                new_mouse.update(x,y,11,0)
                self.mouses.append(new_mouse)
            self.mouse_flag = 1


        # クリックしたら、マル or バツを表示
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if((pyxel.mouse_x > self.cat.pos.x )
                and (pyxel.mouse_x < self.cat.pos.x + CAT_W)
                and (pyxel.mouse_y > self.cat.pos.y)
                and (pyxel.mouse_y < self.cat.pos.y + CAT_H)):
                self.cat.update(self.cat.pos.x, self.cat.pos.y, self.cat.img_a, 1)
                self.score.update(10)

            else:
                for i in range(len(self.mouses)):
                    if((pyxel.mouse_x > self.mouses[i].pos.x )
                        and (pyxel.mouse_x < self.mouses[i].pos.x + ENEMY_W)
                        and (pyxel.mouse_y > self.mouses[i].pos.y)
                        and (pyxel.mouse_y < self.mouses[i].pos.y + ENEMY_H)):
                        self.mouses[i].update(self.mouses[i].pos.x, self.mouses[i].pos.y, self.mouses[i].img_a, 2)
                        self.game_over_flag += 1


                        
    def draw(self):
        pyxel.cls(0)
        if self.game_over_flag != GAME_OVER:
            #スコア表示
            pyxel.text(5,5,"score:" + str(self.score.point),7)

            #ネコ表示
            pyxel.blt(self.cat.pos.x, self.cat.pos.y, self.cat.img_id, 0, 0, CAT_W, CAT_H, self.cat.img_a)

            #ネズミ表示
            mouse_count = len(self.mouses)
            for i in range(mouse_count):
                pyxel.blt(self.mouses[i].pos.x, self.mouses[i].pos.y, self.mouses[i].img_id, 0, 0, ENEMY_W, ENEMY_H, self.mouses[i].img_a)

            #マル表示
            if self.cat.draw_flag == 1:
                pyxel.circb(self.cat.pos.x + CAT_W/2, self.cat.pos.y + CAT_H/2, CIRC_SIZE, 8)
                self.maru_flag = 1

            #バツ表示
            for i in range(len(self.mouses)):
                if self.mouses[i].draw_flag == 2:
                    x = self.mouses[i].pos.x
                    y = self.mouses[i].pos.y
                    pyxel.line(x-2, y-2, x+CAT_W+2, y+CAT_H+2,5)
                    pyxel.line(x+CAT_W+2, y-2, x-2, y+CAT_H+2,5)
                    self.batu_count += 1


                    
        #ゲームオーバーになったら        
        else:
            pyxel.cls(0)
            pyxel.text(WINDOW_W/2 - 15, WINDOW_H/2 - 10, "Game Over", pyxel.frame_count % 16)
            pyxel.text(WINDOW_W/2 - 10, WINDOW_H/2 , "score:" + str(self.score.point) , pyxel.frame_count % 16)
            pyxel.text(WINDOW_W/2 - 60, WINDOW_H/2 + 20, "restart:push mouse left button", pyxel.frame_count % 16)




App()
