import click

from tracelib.utils import TxnConstants

verbose_option = click.option(
    "--verbose", is_flag=True, help="Show more information on the trace."
)
raw_option = click.option("--raw", is_flag=True, help="Show the raw, non-pretty trace.")


def txn_hash_callback(ctx, param, value):
    hash_set = set()
    for tx_hash in value:
        if tx_hash in TxnConstants.SPECIAL_KEYS:
            special_hash = TxnConstants.SPECIAL_KEYS[tx_hash]
            if isinstance(special_hash, (list, tuple)):
                for spec_hash in special_hash:
                    hash_set.add(spec_hash)
            else:
                hash_set.add(special_hash)
        else:
            hash_set.add(tx_hash)

    return [h for h in hash_set]


txn_arg = click.argument("txn_hash", nargs=-1, callback=txn_hash_callback)
