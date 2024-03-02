# Name

    venti

# Version And Stage

    V0.0.1 (2 Pre-Alpha)

# Profile

    venti是Python Web项目脚手架。它考虑OCP、DIP、IoC、OTI、AOP、DI。
    Venti的目标是在抽象和复杂性之间取得平衡，同时也致力于实现快速开发和减少测试。

    Venti is a Python Web scaffold that takes into account principles such as OCP, DIP, IoC, OTI, AOP, and DI.
    Venti aims to strike a balance between abstraction and complexity, while also aiming to achieve rapid development and reduced testing.

# Quick Start

    The main.py and test/utils_test.py contains a demo for reference.

# About Venti

    1 OCP开闭
        目的：可维护性
        实现：
            1 ioC控制反转
                目的：降低代码之间的耦合度，使得代码更加的模块化
                实现：Vinject依赖注入，使用yml管理对象
            2 AOP面向切面
                目的：非侵入式扩展、代码模块复用
                实现：利用 venti/utils/handler 装饰器
            3 OTI面向接口
                目的：规范实现类行为
                实现：基于abc的抽象基类
            4 DIP依赖倒置
                目的：解耦
                实现：MVC分层设计
    2 utils
        目的：减少面对基础模块
        实现：对基础模块更加高级的封装

# Contact Information

    Email: tails@greypoints.com
    URL: https://www.greypoints.com
