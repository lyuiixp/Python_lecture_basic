import json
from movement import Movement

# 로봇 기본속성 클래스
class Robot:
    def __init__(self, name, model, battery, speed):
        self.name = name
        self.model = model
        self.battery = battery
        self.speed = speed
        self.movement = Movement(speed)
        
    def introduce(self):                                            # 간단한 로봇명, 모델명 소개
        return f"안녕, 내 이름은 {self.name}, 모델명은 {self.model}야."

    def recharge(self):                                             # 로봇의 배터리 충전 및 알림
        self.battery = 100  
        print(f"{self.name}의 배터리가 완충되었습니다.")

    def save_to_json(self, filename):                               # 로봇명, 모델명, 배터리 상태 json파일 저장
        data = {
            "name": self.name,
            "model": self.model,
            "battery": self.battery
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"{filename}에 로봇 정보 저장.")

    def load_from_json(self, filename):                             # 로봇명, 모델명, 배터리 상태 json파일 불러오기
        with open(filename, 'r') as f:
            data = json.load(f)
        self.name = data["name"]
        self.model = data["model"]
        self.battery = data["battery"]
        print(f"{filename}에서 로봇 정보 불러오기.")

    def move(self, direction):                                      # 방향을 입력받아 실제 로봇 움직이기
        if self.battery >= 10:
            if direction == "전진":
                self.movement.move_forward()                        # Movement.move_forward()
            elif direction == "후진":
                self.movement.move_backward()
            elif direction == "좌회전":
                self.movement.turn_left()
            elif direction == "우회전":
                self.movement.turn_right()
            self.battery -= 10                                      # 이동 시 배터리 10 감소
            print(f"남은 배터리: {self.battery}")
        else:
            print("배터리가 부족하여 움직일 수 없습니다.")


if __name__ == "__main__":                                          # 단위 테스트
    robot = Robot("rokey", "T100", 50, 5)                           # 이름, 모델, 배터리, 속도
    print(robot.introduce())

    robot.move("전진")
    robot.move("우회전")
    robot.move("후진")
    robot.move("좌회전")
    robot.move("전진")                                              # 배터리가 10 남음
    robot.move("우회전")                                            # 배터리가 부족해 움직일 수 없음
# 
    robot.recharge()                                                # 배터리 충전
    robot.save_to_json("robot_data.json")
    # robot.load_from_json("robot_data.json")
# rokey, T100 , 100