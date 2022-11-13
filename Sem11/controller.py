import intersection
import draw_chart


def button_click(task):
    match task:
        case 1:
            lst = intersection.get_intersection()
            for i in lst:
                print(i)
        case 2:
            draw_chart.draw_func()
        case 3:
            draw_chart.draw_general_func()