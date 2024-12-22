import tkinter
import random


class SnakeGame:
    def __init__(self, root):#__init__ 是 Python 的类专用方法，称为“初始化方法”或“构造函数”
        """初始化游戏"""
        self.root = root            #root是根窗口，使得能访问并操作这个窗口  self后跟一“类”
        self.root.title('贪吃蛇')

        # 创建画布并放置
        self.can = tkinter.Canvas(self.root, height=500, width=800, bg="lightblue")#tkinter.Canvas 是 tkinter 库中的一个类，用来创建一个画布控件。self.root: 这是父容器，画布控件将被放置在这个窗口中，画布被创建并赋值给 self.can，你可以通过 self.can 进行各种操作
        self.can.pack()                                                             #.pack是tkinter中的一种布局方法，将控件放在父容器中。

        # 初始化游戏参数
        self.snake = [(0, 0), (0, 1), (0, 2)]            # 蛇身的初始位置
        self.score = 0                                   #初始分数
        self.direction = 'Down'                          # 初始方向
        self.food_x, self.food_y = self.generate_food()  # 生成食物位置，调用 self.generate_food() 方法来生成食物的位置，并将返回的坐标赋值给 self.food_x 和 self.food_y。

        # 显示开始游戏的按钮.button
        self.start_btn = tkinter.Button(self.root, text="点击按钮开始游戏！", command=self.start_game, height=1, width=20, bg="yellow", fg="red")#创建一个 按钮 控件，并将其绑定到窗口 self.root 上。该按钮的文本是 "点击按钮开始游戏！"，并且在点击时会触发 self.start_game 方法。
        self.start_btn.pack()

        # 绑定键盘事件
        self.root.bind_all("<Key>", self.change_direction)
        #.bind_all() 是 tkinter 中的一个方法，用于将事件绑定到整个应用程序，"<Key>" 是一个特殊的事件，表示键盘按键的按下事件。self.change_direction 是要触发的回调方法，当键盘按键被按下时，change_direction 方法会被调用。

        # 重新开始的按钮
        self.restart_btn = tkinter.Button(self.root, text="重新开始", command=self.restart_game, height=1, width=20, bg="green", fg="white")#tkinter.Button 是 tkinter 中的按钮控件类，用来在窗口中显示一个按钮
        self.restart_btn.pack_forget()
        # 游戏开始前按钮隐藏

        # 显示得分的标签
        self.score_label = tkinter.Label(self.root, text="得分: 0", font=('Arial', 14), bg="lightblue")
        self.score_label.pack()                                                                               #tkinter中的，暂时隐藏功能，可通过pack稍后调用

    def generate_food(self):
        """生成食物并确保食物不与蛇身重叠"""
        while True:
            x = random.randint(1, 39)#生成一个 1 到 39 之间的随机整数
            y = random.randint(1, 24)#生成一个 1 到 24 之间的随机整数
            if (x, y) not in self.snake:
                return x, y

    def start_game(self):
        """开始游戏"""
        self.score = 0  # 重置分数
        self.snake = [(0, 0), (0, 1), (0, 2)]  # 重置蛇的位置
        self.direction = 'Down'  # 重置方向
        self.food_x, self.food_y = self.generate_food()  # 重新生成食物
        self.start_btn.pack_forget()  # 隐藏开始按钮
        self.move_snake()  # 开始蛇的移动

    def restart_game(self):
        """重新开始游戏"""
        self.snake = [(0, 0), (0, 1), (0, 2)]  # 重置蛇的位置
        self.score = 0  # 重置分数
        self.direction = 'Down'  # 重置方向
        self.food_x, self.food_y = self.generate_food()  # 重新生成食物
        self.restart_btn.pack_forget()  # 隐藏重新开始按钮
        self.move_snake()  # 重新开始游戏

    def draw_snake(self):
        """绘制蛇"""
        self.can.delete("all")                                                        # 清空画布，delete() 是 tkinter.Canvas 中的方法
        for segment in self.snake:                                                    #每次循环时，segment 会依次获取列表中的一个坐标值，segment 是蛇身的坐标
            self.create_snake_part(segment)                                           # 绘制每一段蛇身

        # 绘制蛇头
        self.draw_head(self.direction, self.snake[-1][0], self.snake[-1][1])          #根据传入的方向（self.direction）来确定蛇头的绘制方向，并在对应的位置绘制蛇头。self.snake[-1] 表示 self.snake 列表中的最后一个元素，也就是蛇头的位置，例如，如果蛇的身体是 [(0, 0), (0, 1), (0, 2)]，则 self.snake[-1] 会返回 (0, 2)，也就是蛇头的位置。self.snake[-1][0] 是蛇头的 x 坐标，self.snake[-1][1] 是蛇头的 y 坐标。

    def create_snake_part(self, position):
        """绘制蛇身每一部分"""
        x, y = position
        self.can.create_oval(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill='darkgreen', outline='green', width=3)             #self.can.create_oval() 是 tkinter 中用来创建椭圆形（圆形）的绘图函数
        self.can.create_oval(x * 20 + 4, y * 20 + 4, x * 20 + 16, y * 20 + 16, fill='lightgreen', outline='green', width=3)

    def draw_head(self, direction, x, y):
        """根据方向绘制蛇头"""
        if direction == 'Up':
            self.can.create_oval(x * 20 + 5, y * 20 - 10, x * 20 + 15, y * 20, fill='green', outline='black')
        elif direction == 'Down':
            self.can.create_oval(x * 20 + 5, y * 20 + 20, x * 20 + 15, y * 20 + 30, fill='green', outline='black')
        elif direction == 'Left':
            self.can.create_oval(x * 20 - 10, y * 20 + 5, x * 20, y * 20 + 15, fill='green', outline='black')
        elif direction == 'Right':
            self.can.create_oval(x * 20 + 20, y * 20 + 5, x * 20 + 30, y * 20 + 15, fill='green', outline='black')

    def draw_food(self):
        """绘制食物"""
        self.can.create_oval(self.food_x * 20, self.food_y * 20, self.food_x * 20 + 20, self.food_y * 20 + 20, fill='yellow', outline='orange')
        self.can.create_oval(self.food_x * 20 + 5, self.food_y * 20 + 5, self.food_x * 20 + 15, self.food_y * 20 + 15, fill='red')

    def move_snake(self):
        """控制蛇的移动"""
        head_x, head_y = self.snake[-1]

        # 根据方向移动蛇头
        if self.direction == 'Right':
            head_x += 1
        elif self.direction == 'Left':
            head_x -= 1
        elif self.direction == 'Up':
            head_y -= 1
        elif self.direction == 'Down':
            head_y += 1

        # 向蛇身添加新的蛇头
        self.snake.append((head_x, head_y))

        # 检查是否吃到食物
        if (head_x, head_y) == (self.food_x, self.food_y):
            self.score += 1  # 增加得分
            self.food_x, self.food_y = self.generate_food()  # 重新生成食物
            print(f"当前得分: {self.score}")
        else:
            del self.snake[0]  # 如果没吃到食物，去掉蛇尾，以保持蛇身长度不变。

        # 绘制蛇和食物
        self.draw_snake()  # 绘制蛇
        self.draw_food()  # 绘制食物

        # 更新得分显示
        self.score_label.config(text=f"得分: {self.score}")#config 是 tkinter 中用于更新控件属性的方法

        # 检查是否碰到边界或自己
        if head_x < 0 or head_x > 39 or head_y < 0 or head_y > 24 or (head_x, head_y) in self.snake[:-1]:
            #self.snake[:-1] 是列表中去掉最后一个元素（蛇头）的部分
            self.game_over()  # 游戏结束
            return

        # 继续移动蛇
        self.root.after(200, self.move_snake)
        # 每200毫秒更新一次，after 是 tkinter 中的一个方法，用于设置定时器。它让你能够在指定的时间后执行一个函数或方法

    def game_over(self):
        """游戏结束"""
        self.can.create_text(400, 250, text="游戏结束", font=('Arial', 30), fill='red')#font=('Arial', 30):这个参数指定了文本的字体和大小
        self.restart_btn.pack()  # 显示重新开始按钮

    def change_direction(self, event):
        if event.keysym in ["Right", "Left", "Up", "Down"]:#keysym它的值是键盘里按键的名称
            # 防止蛇掉头
            if (event.keysym == "Right" and self.direction != "Left") or \
               (event.keysym == "Left" and self.direction != "Right") or \
               (event.keysym == "Up" and self.direction != "Down") or \
               (event.keysym == "Down" and self.direction != "Up"):
                self.direction = event.keysym


# 创建游戏窗口并运行
root = tkinter.Tk()             #Tk() 是 Tkinter 库中的一个类，它用来创建一个 主窗口 或 根窗口，调用 Tk() 创建了一个名为 root 的根窗口对象。后续我们将通过 root 来访问和操作这个窗口。
game = SnakeGame(root)
root.mainloop()                     #mainloop() 是 Tkinter 提供的一个方法，保持窗口打开