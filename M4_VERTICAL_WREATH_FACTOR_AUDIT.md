# Independent audit of the `Q_9` vertical wreath factor

## Verdict

`m4_fully_vertical_wreath_factor.txt` is a valid fully vertical exact wreath
factor.  Its fourteen length-four cyclic-interval families partition
`binom([9],4)`, and its cyclic intervals cover every target at all other
proper ranks.  The derived 224-entry word covers all 511 nonzero nine-bit
masks.

## Checks

The verifier `scratch/verify_m4_vertical_wreath_factor.py` is independent of
the SAT generator.  It reads only the fourteen-row certificate and checks:

1. every row is a permutation of `1,...,9`;
2. all 126 rank-four interval occurrences are distinct and equal the full
   middle layer;
3. the supports at ranks one, two, and three have sizes `9,36,84` and equal
   their complete Boolean ranks;
4. ranks five through eight are also enumerated directly, rather than trusted
   only through the complement argument;
5. the linearized 224-entry singleton word covers every integer `1,...,511`
   by exhaustive subarray-OR enumeration.

Its output is

```text
rank 1 covered 9 / 9 multiplicity_hist {14: 9}
rank 2 covered 36 / 36 multiplicity_hist {1: 1, 2: 7, 3: 8, 4: 15, 5: 3, 6: 2}
rank 3 covered 84 / 84 multiplicity_hist {1: 44, 2: 38, 3: 2}
rank 4 covered 126 / 126 multiplicity_hist {1: 126}
rank 5 covered 126 / 126 multiplicity_hist {1: 126}
rank 6 covered 84 / 84 multiplicity_hist {1: 44, 2: 38, 3: 2}
rank 7 covered 36 / 36 multiplicity_hist {1: 1, 2: 7, 3: 8, 4: 15, 5: 3, 6: 2}
rank 8 covered 9 / 9 multiplicity_hist {14: 9}
linearized_word 224 entries; nonzero_masks 511 PASS
```

The SAT encoder is used only to discover the factor.  Even an encoding or
solver error cannot invalidate the explicit certificate because the audit
recomputes the claimed combinatorial objects from scratch.

## Scope

This proves a positive finite seed and refutes a universal obstruction at
`m=4`.  It does not prove an all-dimensional vertical wreath theorem, an
inductive lift, or the optimal OR length at `k=9` (which was already known to
be 128 nonzero entries).

Two independent follow-ups have also been checked:

* `m4_balanced_vertical_wreath_factor.txt` has first-shadow histogram
  `1^42 2^42` and full coverage at every rank;
* `m4_switch_fully_vertical_wreath_factor.txt` is the endpoint of the
  verified balanced-switch path in `WREATH_SHADOW_SWITCH_AUDIT.md` and is
  likewise fully vertical under this verifier.
