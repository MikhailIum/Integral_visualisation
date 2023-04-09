import manim
from manim import *
import numpy as np
from manimlib.imports import *


class CreateCircle(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=1,
            y_min=0,
            y_max=2,
            graph_origin=3 * DOWN,
            axes_color=GRAY,
            x_labeled_nums=np.arange(-1, 1.01, 1),  # x tickers
            y_labeled_nums=np.arange(0.0, 2.01, 1),  # y tickers
            **kwargs
        )





    def construct(self):
        self.setup_axes(animate=True)



        def func(x):
            return x**2


        graph = self.get_graph(func, x_min=-1.0, x_max=1.0)
        graph.set_color(YELLOW)

        self.play(ShowCreation(graph), run_time=3)
        self.wait(1)

        kwargs = {
            "x_min" : -1,
            "x_max" : 1,
            "fill_opacity": 0.75,
            "stroke_width" : 0.25
        }


        for i in range(3):
            type_name = ""
            self.graph = graph
            iterations = 6
            if i == 0:
                type_name = "LEFT"
                self.rect_list = self.get_riemann_rectangles_list(graph, iterations, input_sample_type="left",
                                                                  start_color=PURPLE, end_color=ORANGE, **kwargs)
            elif i == 1:
                type_name = "CENTER"
                self.rect_list = self.get_riemann_rectangles_list(graph, iterations, input_sample_type="center",
                                                                  start_color=PURPLE, end_color=ORANGE, **kwargs)
            else:
                type_name = "RIGHT"
                self.rect_list = self.get_riemann_rectangles_list(graph, iterations, input_sample_type="right",
                                                                  start_color=PURPLE, end_color=ORANGE, **kwargs)

            type = Text("type: " + type_name)
            type.next_to(self.y_labeled_nums[1], RIGHT_SIDE)
            type.set_color(GREEN)
            self.play(Write(type))


            text = Text("n = 8")
            text.next_to(graph, RIGHT)
            text.set_color(DARK_BLUE)
            self.play(Write(text))

            int_sum = 0
            n = len(self.rect_list[1]) + 1
            for k in range(1, n):
                int_sum += 2 * (k / n * 1.0) ** 2 * (1 / n)
            int_sum_text = Text(
                "I = " + str(round(int_sum, 2))
            ).to_edge(UL).shift([1.3,-1.3,0])
            # int_sum_text.next_to(type, BOTTOM)
            int_sum_text.set_color(PINK)
            self.play(Write(int_sum_text))

            for j in range(2, iterations):
                if j != 2:
                    self.remove(text)
                    self.remove(int_sum_text)

                    text = Text("n = " + str(len(self.rect_list[j])))
                    text.next_to(graph, RIGHT)
                    text.set_color(DARK_BLUE)

                    int_sum = 0
                    n = len(self.rect_list[j - 1]) + 1
                    for k in range(1, n):
                        int_sum += 2 * (k / n * 1.0) ** 2 * (1 / n)
                    int_sum_text = Text(
                        "I = " + str(round(int_sum, 2))
                    ).to_edge(UL).shift([1.3, -1.3, 0])
                    int_sum_text.set_color(PINK)


                self.transform_between_riemann_rects(self.rect_list[j - 1], self.rect_list[j], dx=1,
                                                     replace_mobject_with_target_in_scene=True,
                                                     run_time=1)
                if j == 2:
                    self.remove(text)
                    self.remove(int_sum_text)
                    text = Text("n = " + str(len(self.rect_list[j])))
                    text.next_to(graph, RIGHT)
                    text.set_color(DARK_BLUE)

                    int_sum = 0
                    n = len(self.rect_list[j - 1]) + 1
                    for k in range(1, n):
                        int_sum += 2 * (k / n * 1.0) ** 2 * (1 / n)
                    int_sum_text = Text(
                        "I = " + str(round(int_sum, 2))
                    ).to_edge(UL).shift([1.3, -1.3, 0])
                    int_sum_text.set_color(PINK)
                self.play(Write(text))
                self.play(Write(int_sum_text))

                self.wait(2)
            self.remove(text)
            self.remove(int_sum_text)
            self.remove(type)
            for i in self.rect_list:
                self.remove(i)


