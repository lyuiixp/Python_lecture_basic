# import test_dir.test_import                                          # test_import.py
# from test_dir.test_import import TestModule
import test_dir

if __name__ == '__main__':                                  # 단위 테스트 실행
    test_result = test_dir.TestModule("민주")
    print(test_result.greet())


