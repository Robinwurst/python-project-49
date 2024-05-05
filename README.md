### Hexlet tests and linter status:
[![Actions Status](https://github.com/Robinwurst/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Robinwurst/python-project-49/actions)

<a href="https://codeclimate.com/github/Robinwurst/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/cd600558cd12fe5fc893/maintainability" /></a>


# **Проект: Игры разума**

### **Описание**
#### Это проект студента Хекслет
#### Суть проекта - написание 5 работающих приложений-игр, отработка полученных навыков.
#### Системные требования:
*Минимальные системные требования*
- Операционная система: Windows 7 SP1, 8.1, 10, macOS 10.10 Yosemite и выше, Linux (в том числе Ubuntu, Fedora, CentOS)
- Версия Python: 3.12 и новее
- Процессор: 1,6 ГГц и выше
- ОЗУ: 1 ГБ и выше
- Место на жестком диске: не менее 1 ГБ

*Рекомендуемые системные требования (для пользователей Mac OS)*
- Процессор Apple M3 Max 16-Core 16 x 2.7 - 4.1 GHz, 56 W PL1 / Sustained
- Графический адаптерApple M3 Max 40-Core GPU, 60 W TDP 
- ОЗУ 48 Гбайт  
- LPDDR5-6400, Dual-Channel, onboard
### Инструкция по установке (актуально для Mac OS, скорее всего и для любых других ОС)
#### 1. Устанавливаем poetry-проект из github.com [Инструкция по установке](https://ru.hexlet.io/courses/python-setup-environment/lessons/poetry-and-packaging/theory_unit)
> $ pip install git+  

> *Однако стоит иметь в виду, что pip относительно недавно научился понимать pyproject.toml. 
Поэтому советую периодически обновлять pip с помощью команды _$ pip install --user --upgrade pip_*

#### 2. Запускаем игры в терминале

###### Перечень игр:
#### - Калькулятор. Арифметические выражения, которые необходимо вычислить
Команда для запуска игры: *brain-calc*
[![asciicast](https://asciinema.org/a/nU6YFANpqszq9NzRivh8Wbe9H.svg)](https://asciinema.org/a/nU6YFANpqszq9NzRivh8Wbe9H)
#### - Прогрессия. Поиск пропущенных чисел в последовательности чисел
Команда для запуска игры: *brain-progression*
[![asciicast](https://asciinema.org/a/FFhiOhSwQgSVUbVotEdJbxDl0.svg)](https://asciinema.org/a/FFhiOhSwQgSVUbVotEdJbxDl0)

#### - Определение четного числа
Команда для запуска игры: *brain-even*
[![asciicast](https://asciinema.org/a/zDk0HVaQagspr76ICPJlXHKF1.svg)](https://asciinema.org/a/zDk0HVaQagspr76ICPJlXHKF1)
#### - Определение наибольшего общего делителя
Команда для запуска игры: *brain-gcd*
[![asciicast](https://asciinema.org/a/LwspA1LcBUtoiNR5IV8ZEsVMG.svg)](https://asciinema.org/a/LwspA1LcBUtoiNR5IV8ZEsVMG)
#### - Определение простого числа
Команда для запуска игры: *brain-prime*
[![asciicast](https://asciinema.org/a/1EahG7pC8Wr0Qk9uXzRXvT98T.svg)](https://asciinema.org/a/1EahG7pC8Wr0Qk9uXzRXvT98T)

### Общие правила для всех игр
- Для победы участнику необходимо правильно ответить на три вопроса подряд
- В случае неправильного ответа прогресс сбрасывается, для повторной попытки необходимо запустить программу заново