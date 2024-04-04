# ISA

isa è un'applicazione da linea di comando che, date due liste di numeri calcola alcune metriche di errore:
-MAE (mean absolute error)
-MSE (mean squared error)

Esempio:
predicted=[1,2,3]
expected=[1,2,4]

MAE=1/len(predicted)*somma(|predicted[i]-expected[i]|)
(|1-1| + |2-2| + |3-4|)/3
$isa --predicted 123 --expected 124 --metrics MAE
