from ._utils import deploy, owner
from ape.logging import logger


logger.set_level("ERROR")


def main():
    contract_a, contract_b, contract_c = deploy()

    contract_a.methodWithoutArguments(
      sender=owner, value="2 ETH"
    ).show_trace()

    print()

    # contract_a.methodWithSingleArgument(
    #   5, sender=owner, value="2 ETH"
    # ).show_trace()
