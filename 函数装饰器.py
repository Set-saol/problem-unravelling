
#编程小白震惊函数还能以参数和值的形式存在,太抽象了！！！！
#不把函数当函数你就理解大半了

def decorater(func):
    print('lll')
    def make_up():
        func() # people
        #1. 为什么 func 能记住原始 people 函数？
        #闭包（Closure）机制：make_up 函数会"记住"它定义时的环境变量（包括 func）
        #即使装饰器已经执行完毕，func 依然绑定着原始 people。
        print('-'*40,'开始化妆')
        print('第一步')
        print('第二步')
    return make_up


@decorater #(people)
#装饰器的核心就是：在函数定义时完成函数对象的替换，后续所有调用都会走新函数逻辑
def people():
    print('素颜')

if __name__ == '__main__':
    people()  # make_up()

    #我的理解
    # 通过 @ 把decorater这个函数修饰成装饰器时，decorater函数就已经执行了，传入进去的参数是people函数，people函数作为实参传入
    # 此时的形参func就是people函数，所以decorater函数满足执行条件，先执行了print，再定义了make_up，因为func()调用在make_up里面
    # 在make_up被定义时会"记住"它定义时的环境变量（包括 func和func里面的people值）最后return make_up
    # 然后返回make_up到调用处，即传入的实参位置people函数，此时的people函数被make_up顶替
    # 此时才完成准备工作，接下来调用people函数其实就是在调用make_up函数
    # 现在执行make_up函数，第一句func（）调用即调用people函数和函数中语句print函数，然后再往下执行第二第三第四语句，至此程序结束