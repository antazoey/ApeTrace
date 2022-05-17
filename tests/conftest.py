import pytest


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def caller(accounts):
    return accounts[1]


@pytest.fixture
def contract_c(project, owner):
    return project.ContractC.deploy(sender=owner)


@pytest.fixture
def contract_b(project, contract_c, owner):
    return project.ContractB.deploy(contract_c.address, sender=owner)


@pytest.fixture
def contract_a(project, contract_b, contract_c, owner):
    return project.ContractA.deploy(
        contract_b.address, contract_c.address, sender=owner
    )
