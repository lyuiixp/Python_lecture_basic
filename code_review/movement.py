class Movement:                                             # 로봇의 움직임 구현 클래스
    def __init__(self, speed):
        self.speed = speed

    def move_forward(self):
        print(f"{self.speed}의 속도로 앞으로 이동했습니다..")

    def move_backward(self):
        print(f"{self.speed}의 속도로 뒤로 이동했습니다.")

    def turn_left(self):
        print(f"{self.speed}의 속도로 왼쪽으로 이동했습니다.")

    def turn_right(self):
        print(f"{self.speed}의 속도로 오른쪽으로 이동했습니다.")


if __name__ == "__main__":  
    movement = Movement(100)
    movement.move_forward()         # Movement(100).move_forward()
    # movement.move_backward