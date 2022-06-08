# The Ape Trace Project

To see a trace, run:

```bash
ape run show 0xb7d7f1d5ce7743e821d3026647df486f517946ef1342a1ae93c96e4a8016eab7 --network ethereum:mainnet:alchemy
```

It will fetch the transactions, relevant contract types, and display a trace in your terminal using the `show_trace()` method on Ape's transaction receipt objects.

## The Sim

Additionally, this project comes with test contracts for seeing a trace locally.
To view the local trace, run:

```bash
ape run sim
```
