#_*_ coding: UTF-8 _*_
import lei2fa as f
class Human(f.Creature):
    
    #类变量
    __sum_hum= 2
    
    #实例方法
    def __init__(self,nameIput,ageInput,kind,live,genderInput='male',scoreInput=0):
        #实例变量
        self.name=nameIput
        self.age=ageInput
        self.gender=genderInput
        
        #传入父类的参数,此方法是利用实例方法去调用父类变量，，此方法十分不可取
        #虽然可行，但当遭遇需要修改父类名时会变得很麻烦
        #f.Creature.__init__(self,kind,live)
        #应该使用super关键字方法
        super(Human,self).__init__(kind,live)

        #实例方法中调用类变量
        # self.__class__.sum_hum+=1
        self.score=scoreInput
    
    def markingScore(self,x):
        if x<0:
            print('input wrong')
        else:
            self.score = x
            print(self.name +'的分数是：'+str(self.score))
            #可以在类下的一个方法中调用另一个方法
            self.fallSleepHour()

    def __fallSleepHour(self):
        sleepHours = self.age/1.7
        sleepHours=round(sleepHours,2)
        print(self.name+" sleep for "+str(sleepHours)+' hours everyday.')
    #类方法
    @classmethod
    def leiMethod(cls):
        cls.sum_hum+=1
        print(cls.sum_hum)
    #静态方法
    @staticmethod
    def staticTest():
        print(Human.sum_hum)

#实例化三个变量   
person1=Human("per1",30,kind='people',live=1)
person2=Human('per2',22,kind='dog',live=0)
person3=Human('per3',22,kind='cat',live=0)

print(person1.live)
