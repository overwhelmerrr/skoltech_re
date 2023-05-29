# skoltech_re
Задание состоит из трех частей. 

В качестве решения нужно прислать код на гитхабе для всех трех заданий, каждое задание в отдельной папке.



1.	Имплементировать код статьи для модели классификации временных рядов. (15 баллов).

ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels. https://arxiv.org/abs/1910.13051

- Датасет для проверки: 
https://www.timeseriesclassification.com/description.php?Dataset=Ham  

Предлагается имплементировать три вида генерации ядер как описано в статье, равномерное семплирование, бинарные [-1,1] и тернарные значения  [-1,0,1] и сравнить результаты работы для них. Для каждого типа ядер нужно будет посчитать несколько запусков модели и представить результат с доверительными интервалами.


Критерии оценки:
-	Качество представления результатов. Сравнить с результатами ROCKET в статье.
-	Качество кода, его работоспособность, читаемость и  комментарии (использование официальных репозиториев возможно, но финальный код должен быть написан вами)

2.	Графы (15 баллов).

Написать модуль с использованием классов который имеет следующие методы (10):

А. Добавление узла с какой-то информацией.
Б. Добавление ребра между двумя узлами;
B. Генерация случайного графа;
Г. Отрисовка получившегося графа с matplotlib.

Реализовать следующий алгоритм (5):

“Вы выбираете из группы из N друзей, с кем пойти на пикник. Однако друзья, связанные ребром на графе, находятся в очень недружественных отношениях друг с другом, поэтому, если они оба отправятся на пикник, он будет испорчен. Чтобы на пикнике было как можно больше друзей, кого следует пригласить?. Протестируйте алгоритм на случайных графах (5 - 10 штук)  различного размера, отрисуйте случайные графы и выведите финальный список на экран или в фаил.”


 


3.	BASH+Docker (15).

		Создайте образ docker на основе операционной системы Linux. Напишите два скрипта с помощью командной оболочки Bash и исключительно ее которые будут выполнять операции ниже. Запустите эти команды внутри докер контейнера.

1.	Посчитать сколько раз каждое слово встречается в файле. (5) 
Результат подсчета выводится на экран.

2.	Взять 10 самых встречаемых слов и создать пустые файлы с их именами $word_n. (10)

Пример запуска: docker exec mycontainer /path/to/my_script.sh $filename $output
*предпологаем что докер контейнер уже запущен.

$filename - путь к файлу
$output - папка куда сохранить результат


Текстовый фаил для задания: https://github.com/benbrandt/cs50/blob/master/pset5/texts/dracula.txt

Подсказка, возможно потребуются функции grep, wc, sort, sed и даже awk.
