import pytest

from tracelib.accounts import account_factory
from tracelib.contracts import deployer


@pytest.fixture
def owner():
    return account_factory.owner


@pytest.fixture
def caller():
    return account_factory[1]


@pytest.fixture
def contract_c():
    return deployer.contract_c


@pytest.fixture
def contract_b():
    return deployer.contract_b


@pytest.fixture
def contract_a():
    return deployer.contract_a
