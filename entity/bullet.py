from base_bullet import BaseBullet

class PlayerBullet(BaseBullet):
    def __init__(self, screenTemp, x, y):
        BaseBullet.__init__(self,screenTemp, x+40, y-20, "./images/bullet.png")

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y <  0:
            return True
        else:
            return False