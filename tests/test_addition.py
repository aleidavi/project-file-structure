import src.addition as addition
# from src.addition import perform_operation

def test_addition():
    # Assert
    assert addition.perform_operation(1, 1) == 2
    assert addition.perform_operation(800, 88) == 888
    assert addition.perform_operation(-1, 1) == 0