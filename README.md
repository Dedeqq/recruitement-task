# Klasyfikacja wiarygodności artykułów

## Treść zadania

Twoim zadaniem jest zaprojektowanie rozwiązania, które będzie w stanie przewidywać, czy dany artykuł jest wiarygodny, czy nie. Artykuły mogą pochodzić z różnych źródeł - rzetelnych mediów, blogów, mediów społecznościowych i stron o wątpliwej wiarygodności.
Wygeneruj własny zbiór danych i zaprezentuj swoje rozwiązanie.

## Dane — notebooks/01_dataset_creation.ipynb

Zbiór danych pochodzi z [fake-and-real-news-dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). Został przefiltrowany i oczyszczony: zachowano artykuły mające co najmniej 100 słów, usunięto duplikaty oraz fragmenty typu "(Reuters)", które mogłyby ujawnić źródło i zniekształcić ocenę modelu.

**Plik danych:** zapisywany w ścieżce zadeklarowanej w `src/env.py`.

Zobacz: [notebooks/01_dataset_creation.ipynb](notebooks/01_dataset_creation.ipynb)

## Eksploracja danych — notebooks/02_data_exploration.ipynb

- Krótkie podsumowanie: analiza jakości danych, rozkłady długości tekstu i liczby słów, sprawdzenie braków danych.
- Analizy zawierają: wykresy rozkładów (`word_count`, `text_length`), porównania statystyk dla klas (real vs fake), najczęstsze n-gramy dla każdej klasy.
- Generowanie chmur słów dla klas, analiza słownictwa oraz projektowanie reprezentacji TF-IDF.
- Redukcja wymiaru (TruncatedSVD) i wizualizacja 2D, aby ocenić separowalność klas.

Zobacz: [notebooks/02_data_exploration.ipynb](notebooks/02_data_exploration.ipynb)

## Eksperymenty — notebooks/03_experiments.ipynb

- Krótkie podsumowanie: trening i ewaluacja modeli klasyfikacyjnych na reprezentacjach TF-IDF.
- Modele porównywane w notebooku: Logistic Regression, Random Forest, XGBoost. Zawiera też prosty GridSearch (Logistic Regression) dla strojenia hiperparametrów.
- Generowanie metryk klasyfikacyjnych i analiza cech (wagi/importance), zapisywanie najlepszego modelu za pomocą `joblib`.

Zobacz: [notebooks/03_experiments.ipynb](notebooks/03_experiments.ipynb)

## Aplikacja — src/app.py

- Prosty interfejs CLI do szybkich predykcji. Klasa `FakeNewsCLI` wczytuje wytrenowany model z lokalizacji `MODEL_PATH` (zdefiniowanej w `src/env.py`) i przyjmuje tekst od użytkownika.
- Działa interaktywnie: wklej tekst → Enter → wyświetlana jest etykieta `REAL 🟢` lub `FAKE 🔴`.
- Uruchomienie: z katalogu projektu użyj jednej z komend:
