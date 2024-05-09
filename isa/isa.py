import argparse #modulo per fare il parsing degli argomenti da linea di comando
import sys
import logging 

class Operation():#per convenzione i nomi delle classi iniziano con maiuscolo e i metodi vengono dichiarati con lo snake_case
    """
    Class to handle the metrics computation
    """
    def __init__(self,
            predicted: 'list[float]',
            expected: 'list[float]',
            metrics:str
        ) -> None: #significa che il metodo restituisce valore None (funziona anche senza!!)
        self.predicted: 'list[float]'=predicted
        self.expected: 'list[float]'=expected
        self.metrics: str =metrics
        
        if not self._is_consistent():
            #print("Predicted and Expected must have the same length")
            #logging.critical("Predicted and Expected must have the same length")
            raise ValueError("Predicted and Expected must have the same length")      def _is_consistent(self)-> bool:
        """
        check the consistence of the input list:
        they must have the same length.
        """
        return len(self.predicted)==len(self.expected)   
    def _mae(self)->float:
        """
        Compute the mean absolute error
        """
        result: float = 0
        for i in range(0,len(self.predicted)):
            result += abs(self.predicted[i] - self.expected[i])
        return result/len(self.predicted)  
    def _mse(self)->float:
        """
        Compute the mean square error
        """
        result: float = 0
        for i in range(0,len(self.predicted)):
            result += abs(self.predicted[i]-self.expected[i]) ** 2
        return result/len(self.predicted)      
    def compute_metrics(self)-> float:
        """
        Compute metrics
        """
        if self.metrics == "MAE":
            return self._mae()
        if self.metrics =="MSE":
            return self._mse()
        else:
            return -1   

def main():
    """
    Compute the mean absolute error in the main function.
    """
    #1.interpretazione argomenti da linea di comando
    parser = argparse.ArgumentParser(
        prog="isa",
        description="Computes error metrics"
    )
    parser.add_argument("--predicted", 
        type=float,
        nargs='+',
        required=True,
        help="Predicted values"
    )
    parser.add_argument("--expected", 
        type=float,
        nargs='+',
        required=True,
        help="expected values"
    )
    parser.add_argument("--metrics",
        type=str,
        required=True,
        help="Metrics to compute",
        choices=["MAE","MSE"]
        )
    logging.basicConfig(level=logging.DEBUG)
    
    arguments= parser.parse_args()
    logging.debug(arguments.predicted)#alla stampa di predicted vai associare il livello di debug
    logging.debug(arguments.expected)
    logging.debug(arguments.metrics)
    solver=Operation(arguments.predicted, arguments.expected, arguments.metrics)
    result=solver.compute_metrics()
    print(f"Result: {result}")
    
if __name__=="__main__": #quando lancio da linea di comando cerca se name è uguali a main ed eseguo il modulo il cui nome è main
    main()   
#...quando scriviamo un file in python attenzione che vengono eseguiti moduli al di fuori del modulo main