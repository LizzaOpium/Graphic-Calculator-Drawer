import matplotlib.pyplot as plt
import numpy as np
import re


def has_parameter_p(equation):
    return bool(re.search(r'\bp\b', equation))


def parse_circle_equation(equation, p=1):
    eq = equation.replace('p', str(p))
    pat = r'\(\s*x\s*([-+])\s*(\d+(\.\d+)?)\)\*\*2\+\(\s*y\s*([-+])\s*(\d+(\.\d+)?)\)\*\*2=(\d+(\.\d+)?)'
    match = re.fullmatch(pat, eq.replace(' ', ''))
    if match:
        sx, xval, _, sy, yval, _, r2, _ = match.groups()
        xc = float(xval) * (-1 if sx == '-' else 1)
        yc = float(yval) * (-1 if sy == '-' else 1)
        r = float(r2) ** 0.5
        return ('circle', xc, yc, r)
    match = re.fullmatch(r'x\*\*2\+y\*\*2=(\d+(\.\d+)?)', eq.replace(' ', ''))
    if match:
        r2 = float(match.group(1))
        return ('circle', 0, 0, r2 ** 0.5)
    return None


def parse_square_equation(equation, p=1):
    eq = equation.replace('p', str(p))
    pat = r'abs\(x([-\+]\d+(\.\d+)?)\)<=([\d\.]+)andabs\(y([-\+]\d+(\.\d+)?)\)<=([\d\.]+)'
    eq_str = eq.replace(' ', '')
    match = re.fullmatch(pat, eq_str)
    if match:
        x_shift, _, size_x, y_shift, _, size_y = match.groups()
        xc = -float(x_shift)
        yc = -float(y_shift)
        lx = float(size_x) * 2
        ly = float(size_y) * 2
        return ('square', xc, yc, lx, ly)
    match = re.fullmatch(r'abs\(x\)<=([\d\.]+)andabs\(y\)<=([\d\.]+)', eq_str)
    if match:
        lx, ly = map(lambda s: float(s) * 2, match.groups())
        return ('square', 0, 0, lx, ly)
    return None


def parse_line_equation(equation, p=1):
    eq = equation.replace('p', str(p)).replace(' ', '')
    match_x = re.fullmatch(r'x=([-+]?\d+(\.\d+)?)', eq)
    if match_x:
        val = float(match_x.group(1))
        return ('vertical', val)
    match_y = re.fullmatch(r'y=([-+]?\d+(\.\d+)?)', eq)
    if match_y:
        val = float(match_y.group(1))
        return ('horizontal', val)
    return None


def plot_object(ax, inp, p=1, color=None):
    result = parse_circle_equation(inp, p)
    if result:
        _, xc, yc, r = result
        t = np.linspace(0, 2 * np.pi, 400)
        x = xc + r * np.cos(t)
        y = yc + r * np.sin(t)
        ax.plot(x, y, color=color)
        ax.set_aspect('equal')
        return
    result = parse_square_equation(inp, p)
    if result:
        _, xc, yc, lx, ly = result
        x_ = np.array([xc - lx / 2, xc + lx / 2, xc + lx / 2, xc - lx / 2, xc - lx / 2])
        y_ = np.array([yc - ly / 2, yc - ly / 2, yc + ly / 2, yc + ly / 2, yc - ly / 2])
        ax.plot(x_, y_, color=color)
        ax.set_aspect('equal')
        return
    result = parse_line_equation(inp, p)
    if result:
        t, val = result
        if t == 'vertical':
            y = np.linspace(-10, 10, 1000)
            x = np.ones_like(y) * val
            ax.plot(x, y, color=color)
        else:
            x = np.linspace(-10, 10, 1000)
            y = np.ones_like(x) * val
            ax.plot(x, y, color=color)
        return
    # Обычная функция
    x = np.linspace(-10, 10, 1000)
    y = eval(inp.replace('p', str(p)), {
        "x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
        "sinh": np.sinh, "cosh": np.cosh, "tanh": np.tanh, "exp": np.exp,
        "log": np.log, "log10": np.log10, "sqrt": np.sqrt, "abs": np.abs,
        "pi": np.pi, "e": np.e, "p": p})
    ax.plot(x, y, color=color)


def ask_graph_input(order_text):
    print(f"\n{order_text} (окружность, квадрат, прямую x=.../y=..., или y=f(x), можно с p):")
    return input("> ").strip()


def ask_p_params():
    p_min = float(input("Минимум p: "))
    p_max = float(input("Максимум p: "))
    n = int(input("Сколько графиков на оси: "))
    return p_min, p_max, n


try:
    fig, ax = plt.subplots(figsize=(8, 8))

    inp1 = ask_graph_input("Введите основной график")
    if has_parameter_p(inp1):
        p_min, p_max, n = ask_p_params()
        p_values = np.linspace(p_min, p_max, n)
        for i, p_val in enumerate(p_values):
            plot_object(ax, inp1, p_val, color=f"C{i % 10}")
    else:
        plot_object(ax, inp1, color="C0")

    add_second = input("\nДобавить второй график на оси? (да/нет): ").strip().lower()
    if add_second in ("да", "yes", "y"):
        inp2 = ask_graph_input("Введите второй график")
        if has_parameter_p(inp2):
            p_min, p_max, n = ask_p_params()
            p_values = np.linspace(p_min, p_max, n)
            for i, p_val in enumerate(p_values):
                plot_object(ax, inp2, p_val, color=f"C{(i + 3) % 10}")
        else:
            plot_object(ax, inp2, color="C1")

    print("\nГрафик готов. Закройте окно графика для выхода.")
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(-10, 11, 2))
    ax.set_yticks(np.arange(-10, 11, 2))
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.show()
except Exception as e:
    print("\nОшибка:", e)