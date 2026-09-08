# Independent audit of the odd-diamond residence tax

Date: 2026-07-31  
Status: specialization GO; universal run wording corrected

## Verdict

The authenticated `K15 -> K17` specialization and its `1425/165` forced
packet conclusion are correct.  The unrestricted sentence saying that every
positive run on every cyclic Johnson component shortens by one needs two
boundary cases.

Let (b_i=1_{x\in T_i}) and

\[
                  c_i=1_{x\in C_i}=b_i b_{i+1},
                  \qquad C_i=T_i\cap T_{i+1}.
\]

Then the exact statement is:

1. every proper cyclic run of ones of length \(\ell\ge2\) in (b) becomes
   the run with the same start and length \(\ell-1\) in (c);
2. a singleton run disappears; and
3. an all-one trace remains all one.

For the intended lower-edge-colour-injective owner cycle, singleton runs are
impossible: if the unique owner (U) containing (x) is flanked by owners
omitting (x), both incident lower colours equal (U\setminus\{x\}), a
duplicate.  All parent runs in the authenticated `6390+45` input are proper
and have length at least four, so the one-unit tax applies exactly there.

## Small counterexample to the unrestricted wording

The rank-two Johnson cycle

```text
0x3, 0x5, 0x9, 0xa
```

has coordinate `0x4` trace `0100`.  Its consecutive-intersection trace is
`0000`, not a positive run of length zero.  This does not affect the
depth-(d) application, whose minimum parent runs have length (d+1\ge2).

## Correct regenerative consequence

For a flat depth-(d) odd-diamond child:

- parent proper minimum run (d+2) guarantees every unmodified `A`-shore
  macro-interior run has length at least (d+1);
- a proper parent run of length (d+1) produces the forbidden local packet
  (0,1^d,0), supported by (d+1) consecutive trace edges; and
- under one fixed occurrence transversal, that packet is broken exactly
  when at least one of those support occurrences is actually unretained.

The last point is a local macro-interior condition.  Per-packet availability
does not prove a simultaneous hitting transversal, and even a simultaneous
hitting set does not alone prove global residence: port-boundary runs can
merge, and upper/deep-shadow and common-cap compiler rows remain correlated.
Thus the recursive state must export either one extra proper-run unit or a
jointly certified compensation mechanism, not merely an abstract hitting
set.

## Exact finite replay

The independent script

```text
scratch/audit_odd_diamond_residence_tax_independent_20260731.py
```

reads the frozen parent components and checks every run directly.  It finds:

```text
component lengths                    6390, 45
parent minimum run                   4
child-intersection minimum run       3
runs per old coordinate              429
parent length-four runs/coordinate   95
parent length-four runs total        1425
unique-colour forced packets         165
forced packets/coordinate            11
CNF                                  2805 variables, 4285 clauses
empty clauses                        165
```

The authenticated builder source has been restored byte-for-byte at SHA
`deea6a938c18ba457708e55f05e2d316c8698c23e6c5e6e4b741831d0e086871`;
its default output reproduces both the frozen CNF and map exactly.  The
optional `--relax-forced` extension is preserved separately as
`scratch/build_k17_macro_residence_cnf_relax_forced_20260731.py`.

No alternative-parent, nonflat-compiler, global `K17`, or all-(k) no-go is
claimed.
