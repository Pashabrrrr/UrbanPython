def introspection_info(obj):
    """Проводит интроспекцию объекта и возвращает информацию о нем."""
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': obj.__class__.__module__,
        'other_properties': {}
    }

    # Сбор атрибутов и методов
    for attr_name in dir(obj):
        try:
            attr = getattr(obj, attr_name)
            if callable(attr):
                info['methods'].append(attr_name)
            else:
                info['attributes'].append(attr_name)
        except Exception:
            continue

    # Дополнительные свойства в зависимости от типа
    if isinstance(obj, (int, float)):
        info['other_properties']['value'] = obj
    elif isinstance(obj, str):
        info['other_properties']['length'] = len(obj)
    elif isinstance(obj, (list, tuple, set)):
        info['other_properties']['length'] = len(obj)
    elif isinstance(obj, dict):
        info['other_properties']['keys'] = list(obj.keys())

    return info

# Пример использования с пользовательским классом
class MyClass:
    """Тестовый класс для демонстрации."""
    class_var = "Hello"

    def __init__(self, value):
        self.instance_var = value

    def greet(self):
        return f"{self.class_var}, {self.instance_var}!"

#Создаем объект и тестируем
my_obj = MyClass(175.5)
result = introspection_info(my_obj)
print(result)

print()

result = introspection_info('Строка')
print(result)

print()

result = introspection_info(654)
print(result)



