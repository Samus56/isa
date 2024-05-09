# ISA v01

`isa` è un'applicazione da linea di comando che, date due liste di numeri calcola metriche di errore:
- MAE (mean absolute error)
- MSE (mean squared error)
- RMSE (root mean squared error)

## Installazione
```
python3 -m pip install .

```
## Utilizzo 
```
usage: isa [-h] --predicted PREDICTED [PREDICTED ...] --expected EXPECTED [EXPECTED ...] --metrics {MAE,MSE}

Computes error metrics

optional arguments:
  -h, --help            show this help message and exit
  --predicted PREDICTED [PREDICTED ...]
                        Predicted values
  --expected EXPECTED [EXPECTED ...]
                        expected values
  --metrics {MAE,MSE}   Metrics to compute
  
```
## Esempio:
```
$isa --predicted 1 2 3 --expected 1 2 4 --metrics MAE
0.3333333333333333
```
