"""
单例模式：比如window任务管理器，只能创建一个。
在实际开发中也经常遇到类似的情况，为了节约系统资源，有时需要确保系统中某个类只有唯一一个实例，
当这个唯一实例创建成功之后，无法再创建一个同类型的其他对象，所有的操作都只能基于这个唯一实例。
为了确保对象的唯一性，可以通过单例模式来实现，这就是单例模式的动机所在。

单例模式（Singleton Pattern）：确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，
这个类称为单例类，它提供全局访问的方法。单例模式是一种对象创建型模式。
单例模式是结构最简单的设计模式，在它的核心结构中只包含一个被称为单例类的特殊类。

单例模式的主要缺点如下：
（1）由于单例模式中没有抽象层，因此单例类的扩展有很大的困难。
（2）单例类的职责过重，在一定程度上违背了单一职责原则。因为单例类既提供了业务方法，又提供了创建对象的方法（工厂方法），
将对象的创建和对象本身的功能耦合在一起。
（3）现在很多面向对象语言（如Java、C＃）的运行环境都提供了自动垃圾回收技术，
因此，如果实例化的共享对象长时间不被利用，系统会认为它是垃圾，会自动销毁并回收资源，
下次利用时又将重新实例化，这将导致共享的单例对象状态的丢失。

"""

# 类装饰器实现
def singleton(cls):
    _instances = {}
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return get_instance

@singleton
class SingleMan:
    def __init__(self, value):
        self.value = value

s1 = SingleMan(20)
s2 = SingleMan(30)

print("decorator: ", s1==s2)
print("it's value is ", s1.value, s2.value)


# __new__ 实现
class SingleMan2:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = SingleMan2()
s2 = SingleMan2()

print("__new__: ", s1==s2)


# 饿汉式
## 在类加载时创建实例，线程安全但可能浪费资源
class SingletonEager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SingletonEager, cls).__new__(cls)
        return cls.__instance

# 在模块加载时就创建实例
# 使用
singleton_instance = SingletonEager()

# 懒汉式
## 在调用时才创建实例，线程不安全，但能减少资源浪费。
## 为避免多个线程同时调用， 可以加上线程锁

import threading

class SingletonLazy:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(SingletonLazy, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.value = "SingletonLazy Instance"

# 测试
print(f"lazy singleton test: ")
s1 = SingletonLazy()
s2 = SingletonLazy()

print(s1 is s2)  # 输出: True
print(s1.value)  # 输出: SingletonLazy Instance

# 饿汉式单例类在类被加载时就将自己实例化，它的优点在于无须考虑多线程访问问题，可以确保实例的唯一性；
# 从调用速度和反应时间角度来讲，由于单例对象一开始就得以创建，因此要优于懒汉式单例。
# 但是无论系统在运行时是否需要使用该单例对象，由于在类加载时该对象就需要创建，因此从资源利用效率角度来讲，饿汉式单例不及懒汉式单例，
# 而且在系统加载时由于需要创建饿汉式单例对象，加载时间可能会比较长。懒汉式单例类在第一次使用时创建，无须一直占用系统资源，实现了延迟加载。
# 但是必须处理好多个线程同时访问的问题，特别是当单例类作为资源控制器，在实例化时必然涉及资源初始化，而资源初始化很有可能耗费大量时间，
# 这意味着出现多线程同时首次引用此类的概率变得较大，需要通过双重检查锁定等机制进行控制，这将导致系统性能受到一定影响。

# java编程语言中还有一种IoDH(Initialization on Demand Holder)的方式来实现单例模式，暂且放在一边。

