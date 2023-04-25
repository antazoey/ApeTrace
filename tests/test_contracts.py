def test_method(contract_a, caller):
    receipt = contract_a.methodWithoutArguments(sender=caller, value="1 ETH")
    assert not receipt.failed
