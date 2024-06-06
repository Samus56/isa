import pytest
import isa.isa as isa
import argparse

class TestIntegration:

    def test_integration_argument(self, monkeypatch):

        def return_value()-> argparse.Namespace:
            return argparse.Namespace(
                predicted=[1,2,3],
                expected=[1,2,3],
                metrics="MAE"
            )
        
        monkeypatch.setattr(isa,"setup_parser", return_value)

        assert isa.main(isa.setup_parser())==0