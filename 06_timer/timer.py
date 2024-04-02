class Timer:
    # write your code here
    def __init__(self):
        self.seconds = 0
    
    def time_string(self):
        return f"{self.seconds//3600:02d}:{(self.seconds//60)%60:02d}:{self.seconds%60:02d}"