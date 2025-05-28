class TestModule:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}!"


if __name__ == '__main__': 
    test_result = TestModule("민주")
    print(test_result.greet())

