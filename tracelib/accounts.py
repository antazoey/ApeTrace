from functools import cached_property

from ape.api import AccountAPI
from ape.cli import select_account
from ape.utils import ManagerAccessMixin
from ape_accounts.accounts import KeyfileAccount
from ape_ethereum.ecosystem import NETWORKS


class AccountFactory(ManagerAccessMixin):
    @cached_property
    def owner(self) -> AccountAPI:
        if self.provider.network.is_dev:
            return self[0]

        elif self.provider.network.name in NETWORKS:
            return self.account_manager.load("metamask0")

        prompt = "Select an account to own these contracts"
        return select_account(prompt_message=prompt, key=KeyfileAccount)

    def __getitem__(self, index: int) -> AccountAPI:
        return self.account_manager.test_accounts[index]


account_factory = AccountFactory()
