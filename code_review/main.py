from robot import Robot
from movement import Movement

# 로봇 생성
robot = Robot("rokey", "T100", 90, 20)

# 로봇의 동작
print(robot.introduce())
robot.move("전진")
robot.move("우회전")
robot.move("후진")
robot.move("좌회전")
robot.recharge()

# 로봇 데이터를 JSON 파일에 저장하고 불러오기
robot.save_to_json("robot_data.json")
robot.load_from_json("robot_data.json")
