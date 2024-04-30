class C:
    def make_str(self, s):
        return s;

    def hello_world(self):
        return f'{self.make_str("Hello")} {self.make_str("world!")}'
