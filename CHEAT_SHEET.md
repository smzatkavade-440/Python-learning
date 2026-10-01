# Python Cheat Sheet

## Function

```python
def add(a, b):
    return a + b
```

## `*args`

```python
def show(*args):
    print(args)
```

## `**kwargs`

```python
def show(**kwargs):
    print(kwargs)
```

## Callback

```python
def process(func):
    return func()
```

## Closure

```python
def outer(x):
    def inner():
        return x
    return inner
```

## Decorator

```python
def decorator(func):
    def wrapper():
        func()
    return wrapper
```

## Class

```python
class Student:
    pass
```

## Constructor

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## Inheritance

```python
class Child(Parent):
    pass
```

## Abstraction

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass
```

## Operator overloading

```python
def __add__(self, other):
    return ...
```
