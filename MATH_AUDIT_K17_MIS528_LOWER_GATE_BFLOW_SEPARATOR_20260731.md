# K17 MIS528 lower-gate candidate and residual-flow separator

Date: 2026-07-31  
Status: exact infeasible recourse witness; not a completed carrier

The bounded-presolve feasibility master on the deterministic 528-target
casualty-independent bank returned a seam/protection bank with:

```text
selected seams                    2543
scaffold cuts                     4024
protected old edges               9236
duplicate seam-colour excess         0
protected-source colour conflicts    0
partial upper holes               1121
```

The result and solver log are:

```text
scratch/k17_fragment_mis528_feas_fast_20260731.result.json
SHA-256 1f58d2009ebcb1ba8567a821248f639ddc58d8693ab3bfd342ecca293eed599c

scratch/k17_fragment_mis528_feas_fast_20260731.log
SHA-256 6e5789cb1e9e4ae955074f705e4e044e7d67c39d4199559672f00f995ff1dee2
```

This candidate passes the two eager lower-colour screens but does not have a
balanced-factor completion when all selected service seams and protected old
edges are frozen.  Exact residual b-flow gives

```text
required flow  25062
maximum flow   25027
deficiency        35
overfull upper     0
overfull lower     0
```

The retained b-flow artifact is

```text
scratch/k17_fragment_mis528_feas_fast_bflow_20260731.json
SHA-256 0abeb57397676349c9ed73ae12cca6330f43d5b83b66cb9f598d1af23d24dc8e
```

For the minimum source-side cut, |A|=33 and |B|=263.  The exact
cancelled Benders row is

\[
 \sum_{(u,\ell)\in F:\,u\notin A,\ell\in B}1
 \le 2|B|+I(A,L\setminus B)-2|A|.
\]

On this candidate its left side is 526 and its right side is 491, reproducing
the flow deficiency 35.  All 263 currently positive fixed-edge terms have
coefficient two, so every continuation in this restricted support must
release at least 18 of them.  The independent minimum-cut audit is

```text
scratch/k17_fragment_mis528_feas_fast_benders_min_20260731.audit.json
SHA-256 f4bb0e97d9467124073b4755b3de0992e92be4d90701b8f9ad57a6eae6232a22
payload bb7eafc2ed14571d94a9539dd623e66ccda8ca2a000a1180ac75e954c75eef41
```

The model-level restricted cut is

```text
scratch/k17_fragment_mis528_feas_fast_benders_modelcut_20260731.json
SHA-256 f8fa9c5f8cacd78fda8964d29f77fbf42677f497898597a293df9e03caaaac35
payload 384ab721547257077a3b3922e69db947fc8651184c4666ac4055a716e964bb1c
```

Finally, deterministic q1 freezing exposes 924 rank-ten rows for which this
candidate has neither a selected seam provider nor an uncut colour-compatible
old provider.  Thus q1 selection must be coupled inside the master; it cannot
be inferred from the partial scaffold and repaired after arbitrary b-flow.

The next compressed master includes both the Benders row and an explicit
chosen/frozen q1 provider for every rank-ten target.  No claim about K17
equality, D3 realization, or common-cap compilation is made here.

## First separated continuation

A hint-directed compressed continuation enforced the first 128 unresolved
q1 targets, 128 casualty-independent old targets, and the first Benders row.
It returned after 272.40 seconds with 2,455 seams, 4,040 scaffold cuts, and
8,860 protected old edges.  Its retained result is

```text
scratch/k17_fragment_active256_benders_hint_20260731.result.json
SHA-256 a9f7c018fb399269e105f4997ab4fe00b5b7ad24379795054ce7084c9301be1f
```

This is again an infeasible recourse witness, but both exact residuals moved
in the intended direction:

```text
q1 unresolved     924 -> 849
b-flow deficiency  35 -> 22
```

The second exact residual-flow certificate has required flow 25,990 and
maximum flow 25,968.  Its minimum-cut Benders row has 169 currently positive
fixed edges, all of coefficient two, and reads 338 <= 316.  Hence the next
continuation must release at least 11 of those edges.  The artifacts are

```text
scratch/k17_fragment_active256_benders_hint_bflow_20260731.json
SHA-256 99c43706cd9064e122c1d88a98b70a3c7077950527e3389c7acf822eee0e51a5

scratch/k17_fragment_active256_benders_hint_cut2_20260731.audit.json
SHA-256 2861ba892796d500e6de4ac8ddbbc928e4ff8ee02a15964cc5db063b2085ba16
payload c67d62e5c905f6fb9dee51de20a7157845d5dbd6ce116286ee0fa81af1e85533
```

Thus the Benders/q1 loop is not merely rotating an unchanged obstruction:
both independently audited deficits decreased.  The second continuation
adds 128 new q1 obligations, 128 new literal casualties, and this second cut.
