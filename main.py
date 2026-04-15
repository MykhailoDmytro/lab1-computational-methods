# Модель: Метод Ньютона (5 семестр)
# Автор: Михайлов Дмитро павлович, група АІ-233

def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return x

f = lambda x: x**2 - 2
df = lambda x: 2*x

root = newton_method(f, df, 1)
print("Корінь:", root)
