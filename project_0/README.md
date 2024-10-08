# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Описание-проекта) \
[2. Какой кейс решаем?](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Какой-кейс-решаем) \
[3. Краткая информация о данных](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Краткая-информация-о-данных) \
[4. Этапы работы над проектом](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Этапы-работы-над-проектом) \
[5. Результат](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Результат) \
[6. Выводы](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Выводы) \
[7. Ссылки](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Ссылки)

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**
Учимся писать хороший код на python

### Краткая информация о данных
Источник: Компьютер генерирует случайное число. \
Тип: Целое число в диапазоне от 1 до 100. \
Использование: Проверка скорости алгоритма в угадывании числа.

:arrow_up: [к оглавлению](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Оглавление)

### Этапы работы над проектом
Первым этапом было предложено угадывание числа случайным образом, это очень неэффективный метод, заключающийся в том чтобы просто случайным образом угадать число.

Вторым этапом был предложен более эффективный метод, так называемое угадывание числа с коррекцией. Сначала устанавливается любое случайное число, а потом уменьшается или увеличивается в зависимости от того, больше оно или меньше нужного.

Третим этапом был использован метод бинарного поиска. Его суть заключается в том что требуется каждый раз брать число, которое делит пополам диапазон поиска, если загадано не это число, то, в зависимости от того больше это число или меньше, сужать диапазон поиска. В конце, если между числами остался лишь один вариант, попытка не считается, так как ответ становится очевидным.

:arrow_up: [к оглавлению](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Оглавление)

### Результаты
Первый метод угадывает загаданное число со средним количеством попыток равным 100.

Второй метод угадывает загаданное число со средним количеством попыток равным 33.

Третий метод угадывает загаданное число со средним количеством попыток равным 5.

:arrow_up: [к оглавлению](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Оглавление)

### Выводы
Из полученных результатов понятно, что третий метод самый эффективный, так как благодаря бинарному поиску максимальное количество попыток требуемое для определения числа равно 6, а среднее количество попыток равно 5.

:arrow_up: [к оглавлению](https://github.com/DaniilFad/test_ds/tree/main/project_0/README.md#Оглавление)

### Ссылки
[1. Google Colab с проектом](https://colab.research.google.com/drive/1GcohUj9btrJc---L9fDUC-Oce11wNoTP?usp=sharing)

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень благодарен, если отиетите репозиторий и профиль ⭐️⭐️⭐️-дами