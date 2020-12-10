class Assert:
    def __init__(self,move_data,result):
        self.data=move_data
        self.result = result
        # print(self.data,self.result)

    def assert_equation(self):
        assert self.data == self.result

    def assert_greater(self):
        assert int(self.data) > int(self.result)

    def assert_less(self):
        assert int(self.data) < int(self.result)

    def assert_not_equation(self):
        assert self.data != self.result

    def assert_in(self):
        assert self.result in self.data

    def assert_notin(self):
        assert self.result not in self.data
