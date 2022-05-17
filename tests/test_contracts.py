def test_method(contract_a, caller):
    receipt = contract_a.methodA(sender=caller, value="1 ETH")
    assert receipt
