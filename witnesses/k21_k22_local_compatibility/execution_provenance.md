# Historical352862/705724 verification provenance

One reviewed source ran on h100 (`arboghast`) with120 CPU/150 wall seconds,
3 GiB address space and512 MiB per file. The output directory was fresh;
there was no retry. The complete suffix enumeration, all-target range-OR
recheck, exact all-rank lower bounds and byte-identical ordinary22 lift
passed. Wall time was13.356800350826234 seconds, exit0.

```sh
ssh h100 'timeout 150s python3 /home/amodo/exact-b-k21-k22-local-compatibility-20260909/verify_k21_k22_local_compatibility_suffix_and_lift.py --inputs /home/amodo/exact-b-k21-k22-local-compatibility-20260909/inputs --out /home/amodo/exact-b-k21-k22-local-compatibility-20260909/output > /home/amodo/exact-b-k21-k22-local-compatibility-20260909/run.log 2>&1'
```

Source SHA `798867bed6d3fcc779b4f2c2f17c2bf84d78b3814dcc5a2b6f92755c93437459`.
Complete report SHA `78863b81c7187d06544fefb30724834dee81ed3533362e49e15928358f187524`.
The complete output and run log were copied. The complete report hash
was compared with the remote original. These143/289 gaps are historical;
the subsequent supplied optimal21/22 pair closes both gaps completely.
The prepared separate forward checker for this historical pair was never
executed; forward verification instead checked the newer optimal pair.
