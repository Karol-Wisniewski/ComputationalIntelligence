# Zadanie 4
# Wykonaj zadanie 3 wykorzystując inną paczkę: keras. Jest to bardziej zaawansowana
# biblioteka dedykowana sieciom neuronowym.
# a) Wykonaj kroki b-d z poprzedniego zadania.
# b) Nanieś na wykres krzywą błędu (loss curve) dla zbioru treningowego i zbioru
# walidującego (u nas zbiorem walidującym może być zbiór testowy). Wykres
# powinien wyglądać mniej więcej tak:
# c) Czy trenowanie powinno się przerwać w pewnym momencie, by uniknąć
# przeuczenia? Jak odczytać to z wykresu? A może mamy do czynienia z
# niedouczeniem? Podpowiedzi:
# • Wykład
# • https://machinelearningmastery.com/learning-curves-for-diagnosingmachine-learning-model-performance/
# • https://rstudio-conf-2020.github.io/dl-keras-tf/notebooks/learning-curvediagnostics.nb.html
# d) Przetestuj jak sieć będzie uczyła się z różnymi optimizerami (adam, itd.) i
# różnymi funkcjami aktywacji (reLU, itp.). Wyświetl i porównaj wykresy krzywych
# uczenia się dla różnych konfiguracji.
# e) Dodatkowo, w miarę możliwości, zwizualizuj sieć neuronową w formie grafu,
# obrazka. Jeśli się da to najlepiej z uwzględnieniem poszczególnych neuronów,
# krawędzi i wag. Być może przydatne będą linki:
# • https://datascience.stackexchange.com/questions/12851/how-do-youvisualize-neural-network-architectures
# • https://towardsdatascience.com/visualizing-artificial-neural-networks-annswith-just-one-line-of-code-b4233607209e

import numpy as np
import pandas as pd
import tensorflow as tf

diabetes_csv = pd.read_csv("diabetes.csv")


train_set, test_set = tf.keras.utils.split_dataset(list(diabetes_csv.values), 0.7)


print(train_set)
print(test_set)

print(len(train_set))
print(len(test_set))