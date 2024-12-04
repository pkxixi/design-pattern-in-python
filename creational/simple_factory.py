"""
首先将需要创建的各种不同对象（例如各种不同的Chart对象）的相关代码封装到不同的类中，这些类称为具体产品类，
而将它们公共的代码进行抽象和提取后封装在一个抽象产品类中，每一个具体产品类都是抽象产品类的子类。
然后提供一个工厂类用于创建各种产品，在工厂类中提供一个创建产品的工厂方法，该方法可以根据所传入的参数不同创建不同的具体产品对象。
客户端只需调用工厂类的工厂方法并传入相应的参数即可得到一个产品对象。
"""
from abc import ABC, abstractmethod


# 抽象类实现接口
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA(Product):
    def operation(self):
        print("result of operation of ConcreteProductA")

class ConcreteProductB(Product):
    def operation(self):
        print("result of operation of ConcreteProductB")

class SimpleFactory:
    @staticmethod
    def create_product(product_type):
        if type == "A":
            return ConcreteProductA()
        elif type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Invalid product type")

product_t = "A"
product = SimpleFactory.create_product(product_t)