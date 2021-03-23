from turtle import Turtle
import random

color_list = ["#FFE99B", "#FB321E", "#757A2B", "#7F7F99", "#EFF2EB", "#FABF50", "#0D37C3", "#941A88", "#6BFF00", "#6ABF0B", "#8C0C7F", "#FFE500", "#525CF5", "#8C0C7F", "#FFE500", "#2D9314", "#8C0C7F", "#005BFF", "#EEAA05", "#8C0C7F", "#17774F", "#425113", "#8C0C7F", "#FFE500", "#09950B", "#8C0C7F", "#005BFF", "#D88602", "#5C0A61", "#05E7CE", "#FBD704", "#8C0C7F", "#1BC3D8", "#FF6C00", "#6C0676", "#FFE500", "#8EDBB8", "#8C0C7F", "#FFE500", "#0DA182", "#8C0C7F", "#FFE500", "#8EBB1A", "#8C0C7F", "#FFE500", "#4A2126", "#A5267F", "#FFE500", "#0D195E", "#B97E1A", "#FF5937", "#79B726", "#A52B85", "#ECC50A", "#319471", "#BF3E24", "#B986ED", "#85E378", "#3D59DE", "#FFA427", "#60AB43", "#891A7F", "#FFB500", "#65B799", "#9736B2", "#8ED11E", "#DD9016", "#4D24A3", "#A1E896", "#2E0CB5", "#F86300", "#FDFF00", "#26229F", "#91B00B", "#FF7F19", "#799516", "#6E068A", "#118991", "#228CFF", "#E85407", "#EFF66E", "#007EDC", "#E1A307", "#D01D79", "#CF581B", "#141494", "#FFFF00", "#C93457", "#048188", "#890B5D", "#C83D79", "#409D3B", "#2BDCED", "#DA3781", "#ED9408", "#A577FF", "#20837D", "#DF641A", "#AD7710"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        color= random.choice(color_list)
        self.color(color)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        color= random.choice(color_list)
        self.color(color)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)