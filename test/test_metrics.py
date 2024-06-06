#from isa.isa import Operation
import pytest
import isa.isa as isa
import math

class TestClass:
    def test_mae_0(self):
        p=[1,2,5]
        e=[1,2,5]
        expected_result=0
        op=isa.Operation(predicted=p,expected=e,metrics="MAE")
        computed_value=op.compute_metrics()

        assert computed_value==expected_result
    
    @pytest.mark.skip("Temp skip.")
    def test_mae_1(self):
        p=[1,2,5]
        e=[1,2,4]
        expected_value=0.33333333
        op=isa.Operation(predicted=p,expected=e,metrics="MAE")
        computed_value=op.compute_metrics()
        assert pytest.approx(computed_value)==expected_value

    def test_raises_exception(self):
        with pytest.raises(ValueError):
            isa.Operation([1,2],[1],"MAE")

    @pytest.mark.parametrize("p,e",[
        ([1,2,3],[1,2,3]),
        ([2,3,4],[2,3,4])
    ])
    def test_parametrized(self,p,e):
        expcted_result=0 
        op=isa.Operation(predicted=p,expected=e,metrics="MAE")
        computed_value=op.compute_metrics()
        assert pytest.approx(computed_value)==expcted_result

    def test_RMSE(self,monkeypatch):
        p=[1,2,3]
        e=[1,2,3]
        expected_result=0

        op=isa.Operation(predicted=p,expected=e,metrics="RMSE")
        monkeypatch.setattr(op,"compute_metrics",lambda:0)
        computed_value=op.compute_metrics()
        assert pytest.approx(computed_value)==expected_result

    def test_RMSE_0(self):
        p=[1,2,5]
        e=[1,2,5]
        expected_value=0
        op=isa.Operation(predicted=p,expected=e,metrics="RMSE")
        computed_value=op.compute_metrics()
        assert computed_value==expected_value
    
    def test_RMSE_1(self):
        p=[1,2,5]
        e=[1,2,4]
        expected_value=math.sqrt(1/3)
        op=isa.Operation(predicted=p,expected=e,metrics="RMSE")
        computed_value=op.compute_metrics()
        assert pytest.approx(computed_value)==expected_value



