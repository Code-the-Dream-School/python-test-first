# write your code here

class Book:
    def get_title(self):
        return self.__title
    
    def set_title(self,title):
        self.__title = self.titleize(title)

    def titleize(self, s):
        little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
        s_split=s.split(" ")
        for i in range(0,len(s_split)):
            if (i == 0):
                s_split[i] = s_split[i].capitalize()
            elif s_split[i] not in little_words:
                s_split[i] = s_split[i].capitalize()
            elif i == len(s_split) - 1:
                s_split[i] = s_split[i].capitalize()
        return " ".join(s_split)