# The Ape Trace Project

To see a trace, run:

```bash
ape run show 0xb7d7f1d5ce7743e821d3026647df486f517946ef1342a1ae93c96e4a8016eab7 --network ethereum:mainnet:alchemy
```

It will fetch the transactions, relevant contract types, and display a trace in your terminal using the `show_trace()` method on Ape's transaction receipt objects.

To see additional information on the trace, use the `--verbose` flag:

```bash
ape run show 0x... --verbose
```

To see the raw `evm-trace` package version of the trace display, use the `--raw` flag:

```bash
ape run show 0x... --raw
```

There are some hard-coded transaction you can use as well with special keys, e.g.:

```bash
ape run show fail
ape run show 0
ape run show 1
ape run show vyper
```

## The Sim

Additionally, this project comes with test contracts for seeing a trace locally.
To view the local trace, run:

```bash
ape run sim
```

You can skip sections of the simulation by using the `--skip` flag:

```bash
ape run sim --skip methodWithoutArguments 
```

The `--verbose` and `--raw` flags mentioned in the first section also work for the `sim` command.
