# Audit of the K16 three-named-host common-envelope and rethread theorem

Date: 2026-07-30  
Verdict: **PASS with the stated finite-family scopes**

Audited source:

```text
MATH_THEOREM_R_K16_THREE_NAMED_HOST_COMMON_ENVELOPE_AND_RETHREAD_NOGO_20260730.md
```

## 1. Symbolic theorem audit

The individual-host criterion is necessary and sufficient under its explicit
maximal-envelope hypotheses.  If a lower host `J` realizes `S`, then `S` is
contained in the envelope union, no middle bit outside `S` can have its whole
carrier inside `J`, and every edited physical cell must meet `S`.  Conversely
`x_p=E_p intersect S` on `J`, with maximal envelopes elsewhere, realizes `S`
and preserves every middle row.

The simultaneous theorem is also exact.  Any feasible assignment is
pointwise contained in

```text
K_p = E_p intersect intersection_(R:p in J_R) R.
```

Hence feasibility forces nonempty cores and all displayed row equalities.
Those same cores are a constructive assignment when the equalities hold.
No matching, fractional, or independent-rank assumption is used.

The decomposition

```text
K=0x4831, u=0x0040, v=0x0008, w=0x0400
A=K|u|w=0x4c71
B=K|u|v=0x4879
C=K|v|w=0x4c39
```

and all pair/triple intersections were checked bitwise.  Conditioned on the
three individual host tests, overlap cores, six ear rows, and combined
outside-`0x4c79` carrier covers exhaust all coordinate types.  Pairwise host
distance at least four is sufficient because every proper host has length at
most three and every middle carrier has diameter at most three.

## 2. Frozen chronology audit

Independent reconstruction gives:

```text
u0: 0x4879 -> (9717,2), 0x4c39 -> (12164,2), 0x4c71 -> empty
u1: 0x4879 -> empty, 0x4c39 -> empty, 0x4c71 -> (3279,3)
```

The capacities 29,065 and 31,512, terminal flat positions, nonzero envelopes,
middle reconstruction, and arbitrary upper completeness agree with the
previous independent state2 audits.

## 3. Twelve-label atlas audit

The catalogue contains six distinct physical length-three blocks, one from
each `X` parent.  Each has exactly one middle-preserving placement in `u1`, at
start 3279.  Duplicating these six rows over `Y in {1,5}` gives twelve
provenance labels.  The theorem correctly does not call them twelve distinct
rethreads.

Literal replay verifies that all six substitutions:

* preserve every prescribed middle row;
* preserve all upper masks;
* lose no mask covered by the `u1` maximal-envelope word;
* retain the empty physical host domains of `0x4879` and `0x4c39`.

Their lower-hole counts are exactly

```text
3985,3985,3986,3985,3986,3984.
```

Thus the singleton obstruction `{0x4879}->empty` is valid for every row of
this local atlas.

## 4. Rethread census audit

The standard 2/3-opt ledger has one relevant 2-opt key and 299 genuine 3-opt
keys.  Its only two upper-complete exact carriers are `u0,u1`, with protected
host vectors `(B,C,A)=110,001`.

For the fixed-three-plus-one family there are exactly

```text
(12869-3) * 3! * 2^3 = 617568
```

representations.  Every counter partition in the saved result sums exactly.
The single row passing the two `u1` debts and arbitrary upper coverage is
independently reconstructed from its four cuts, segment order and orientation.
It is byte-identical to `u0`, whose `0x4c71` host domain is empty.  Hence the
reported scoped no-go is valid.

## 5. Implication boundary

The report does not exclude movable original cuts, terminal-flat cuts,
five-cut or nonstandard rethreads, unrelated chronologies, or the separate
twelve-pair tri-window collar family.  It does not infer a full compiler from
individual host existence.  No global K16 bound improvement is claimed.

No correction was required.
