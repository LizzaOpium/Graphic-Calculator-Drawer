# Graphic Calculator (ENG) 

## Project Information

**Project:** Ladder Geometry Visualizer / Graphic Calculator
**Author:** Alexey Popov

This application visualizes a vertical ladder-like structure made of wooden beams and horizontal platforms using coordinate-based geometry. The project is implemented in Python and distributed as a standalone Windows executable (.exe).

The program is designed for educational purposes and demonstrates how geometric objects can be constructed and visualized using numerical methods.

---

## Project Description

The program builds a 2D geometric projection of the following structure:

* 4 vertical wooden beams
* Each beam has a height of **1.8 meters**
* The distance between neighboring beams is **0.2 meters**
* 6 horizontal platforms
* Platforms are placed every **0.2 meters** in height
* All platforms connect all four beams

The result is a clear geometric model that resembles a ladder or scaffolding structure.

---

## Purpose of the Project

* Visual demonstration of geometry using coordinates
* Demonstration of numerical model construction
* Practice with plotting and scaling
* Visualization of real-world structures in a mathematical form
* Easy conversion into an executable (.exe) file

---

## Technologies Used

* **Python 3** — main programming language
* **matplotlib.pyplot** — used for drawing the figure
* **numpy** — used for numerical arrays and clean range generation

---

## How the Structure is Built

### Vertical Beams

* Height: 1.8 meters
* X coordinates: `0`, `0.2`, `0.4`, `0.6`
* Each beam is drawn as a vertical line segment

### Horizontal Platforms

* First platform at height `0.2 m`
* Step size: `0.2 m`
* Total: 6 platforms
* Each platform connects all beams from `x = 0` to `x = 0.6`

---

## Axis Settings and Visualization

* Equal scaling on both axes
* Grid enabled
* Correct proportional geometry
* Clear axis labels and title

---

## Executable Version (.exe)

The compiled Windows executable is named:

```
grafik.exe
```

It is located inside the archive:

```
Graphic Calculator
```

and published in this GitHub repository.

---

## Educational Value

This project can be used for:

* School geometry projects
* Demonstration of coordinate systems
* Learning numerical modeling
* Introduction to scientific visualization

---

## Author

Alexey Popov



---



# Graphic Calculator / Графический калькулятор (RU)

## Информация о проекте

**Проект:** Ladder Geometry Visualizer / Графический калькулятор
**Автор:** Alexey Popov

Программа визуализирует вертикальную лестничную конструкцию, состоящую из деревянных балок и горизонтальных платформ, используя координатный метод и численное моделирование.

Проект реализован на Python и распространяется также в виде готового исполняемого файла Windows (.exe).

---

## Описание проекта

Программа строит двумерную геометрическую проекцию следующей конструкции:

* 4 вертикальные деревянные балки
* Высота каждой балки — **1.8 метра**
* Расстояние между соседними балками — **0.2 метра**
* 6 горизонтальных площадок
* Площадки расположены через каждые **0.2 метра по высоте**
* Каждая площадка соединяет все четыре балки

В результате получается наглядная геометрическая модель лестничного типа.

---

## Цель проекта

* Наглядное представление геометрических объектов
* Демонстрация построения через координаты
* Работа с масштабами и пропорциями
* Визуализация реальных объектов в математической форме
* Возможность лёгкой сборки в .exe-файл

---

## Используемые технологии

* **Python 3** — основной язык программирования
* **matplotlib.pyplot** — отвечает за отрисовку графика
* **numpy** — используется для массивов чисел и построения диапазонов

---

## Как строится конструкция

### Вертикальные балки

* Высота: 1.8 м
* Координаты по оси X: `0`, `0.2`, `0.4`, `0.6`
* Каждая балка рисуется как вертикальный отрезок

### Горизонтальные площадки

* Первая площадка: `0.2 м`
* Шаг: `0.2 м`
* Всего: 6 площадок
* Каждая площадка соединяет балки от `x = 0` до `x = 0.6`

---

## Оси и визуализация

* Одинаковый масштаб по осям
* Включена сетка
* Сохранены правильные пропорции фигуры
* Подписи осей и заголовок

---

## Готовая версия (.exe)

Скомпилированный исполняемый файл называется:

```
grafik.exe
```

Он находится в архиве:

```
Graphic Calculator
```

и опубликован в этом GitHub-репозитории.

Для запуска `.exe` версия **не требует установленного Python**.

---

## Образовательная ценность

Проект подходит для:

* Школьных проектных работ
* Демонстрации координатной плоскости
* Изучения численного моделирования
* Начального уровня научной визуализации

---

## Автор

Alexey Popov

