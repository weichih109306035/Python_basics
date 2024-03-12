from TPBank import TPbank
class SSbank(TPbank):
    def __init__(self,username):
        self.title="SSBank from TPBank"
    def bank_title(self):
        return self.title
