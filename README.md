# lab9

#### Цель проекта

Очистка и анализ метеорологических данных Австралии с использованием PySpark. Проект реализует загрузку датасета с Kaggle, обработку пропусков и некорректных значений, приведение типов данных, заполнение числовых полей медианой, категориальных — модой, фильтрацию по заданным условиям и сохранение итоговых данных в формате CSV.

#### Используемые инструменты

Python 3
PySpark
KaggleHub
Google Colab
Модули: glob, os, shutil

#### Источники данных

Набор данных: Weather Dataset
Источник: [https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
Формат хранения: CSV
Файл: weatherAUS.csv

#### Структура проекта

- README.md
- lab9.ipynb
  
#### Как запустить проект

1. Установить зависимости: pip install pyspark kagglehub
2. Открыть и выполнить ноутбук lab9.ipynb в среде Jupyter Notebook или Google Colab.
   Скрипт автоматически загрузит датасет, выполнит предобработку и сохранит результат в output/lab9.csv.

#### Результаты

Данные очищены и приведены к корректным типам, пропуски обработаны медианой и модой, выполнена фильтрация записей по указанным условиям, итоговый результат сохранён в output/lab9.csv.

#### Структура датасета:

 - Date — object 
 - Location — object 
 - MinTemp — float64 
 - MaxTemp — float64 
 - Rainfall — float64 
 -  Evaporation — float64  
 - Sunshine — float64 
 - WindGustDir — object  
 - WindGustSpeed — float64 
 - WindDir9am — object 
 -  WindDir3pm — object  
 - WindSpeed9am — float64  
 - WindSpeed3pm — float64 
 -  Humidity9am — float64      
 - Humidity3pm — float64 
 - Pressure9am —float64     
 - Pressure3pm — float64      
 - Cloud9am — float64     
 - Cloud3pm — float64     
 - Temp9am — float64     
 - Temp3pm — float64     
 - RainToday — object     
 - RainTomorrow — object
