# The two-coordinate five-flow ledger versus the canonical product SCD

Date: 2026-07-31  
Status: exact product ledger and solver-free two-shore BTK-local no-go;
deterministic replay for ambient `m=4,...,8`; no non-BTK or nonproduct claim

## 0. Verdict

The fractional five-flow recursion of Theorem 5.3 is correct, but the most
literal product-SCD rounding does not realize it.

Fix collar coordinates `{c,z}` and reserve trace `{c}`.  The unique collar
SCD having `{c}` as a singleton is

```text
empty < {z} < {c,z},          {c}.
```

Producting it with a core SCD gives the correct outer palettes, but every
core singleton chain creates a crossing `empty->{c,z}` flag whose opposite
middle corner lies in the reserved trace.  Replacing all crossings by the
five-flow ledger requires one common `K`-set of `{z}->{z}` donor flags and
two independent perfect assignments: singleton lower endpoints into donor
uppers, and donor lowers into singleton upper endpoints.  This is exactly a
common-basis problem for two transversal matroids.

For the canonical BTK core both incidence matrices are empty in every
dimension.  Every rank-`n-1` neighbour below a BTK singleton and every
rank-`n+1` neighbour above it belongs to a radius-one BTK chain, whereas
`{z}->{z}` flags come exactly from chains of radius at least two.  Thus both
transversal ranks, and hence the common-basis rank, are zero.

The raw product is acyclic and tail-injective, but not head-injective; its
physical maximum degree is `m`.  This is a sharply scoped failure of the
canonical product rounding, not of the fractional theorem.

## 1. Exact product ledger

Put `n=m-1` and

```text
M=binom(2n,n),  N=binom(2n,n-1),  P=binom(2n,n-2),
K=M-N=Cat_n,    C=M-P,             R=P-K.
```

Let `c_d` be the number of core SCD chains of radius `d`.  For every SCD,

```text
c_d=binom(2n,n-d)-binom(2n,n-d-1).
```

The boundary-peeling product of one core chain with the displayed collar
has these central flags:

* radius `d=0`: one crossing `empty->{c,z}` flag;
* radius `d=1`: one `empty->{z}` and one `{z}->{c,z}` flag;
* radius `d>=2`: one flag in each of `empty->empty`, `{z}->{z}`, and
  `{c,z}->{c,z}`.

Therefore the raw complement ledger is

```text
empty->empty       P
empty->{z}         N-P
{z}->{z}           P
{z}->{c,z}         N-P
{c,z}->{c,z}       P
empty->{c,z}       K          (crosses the reserved middle trace).
```

Theorem 5.3 instead prescribes `P,C,R,C,P` on its five allowed sectors.
Since `C=(N-P)+K` and `R=P-K`, the exact difference is `K` copies of

```text
delete: empty->{c,z}, {z}->{z}
add:    empty->{z},   {z}->{c,z}.
```

Thus the singleton seams are precisely the integral transfer units required
by the fractional ledger.

## 2. Exact two-shore donor condition

Let the crossing seam lower endpoint be a core singleton `W^-`, and let its
upper endpoint use an independently assigned core singleton `W^+`:

```text
lower W^-,                 upper W^++{c,z}.
```

Let a candidate `{z}->{z}` donor have core outer flag `R<U`.  The only
two-for-two replacement with the same four outer endpoints is

```text
W^- -> U+z,                R+z -> W^++{c,z}.
```

These two flags are legal exactly when

```text
W^- subset U,              R subset W^+.              (2.1)
```

Hence define two incidence graphs on the common donor ground set:

* lower shore: `W^- -- e` iff `W^- subset U_e`;
* upper shore: `e -- W^+` iff `R_e subset W^+`.

A product-local correction requires a `K`-set of donors which is a base of
both transversal matroids.  Conversely, perfect assignments on both shores
to one common donor set make all new outer flags legal.  Ordered physical
orientations are downstream: they do not alter (2.1).  In particular,
requiring `W^-=W^+` would be an invalid diagonal restriction and is not used.

## 3. Solver-free two-sided BTK radius gate

### Lemma 3.1

Let `W` be a BTK singleton in `B_(2n)`.

1. Every rank-`n-1` set `R subset W` belongs to a radius-one BTK chain.
2. Every rank-`n+1` set `U supseteq W` belongs to a radius-one BTK chain.

### Proof

A BTK singleton has no free coordinate.  In the zero-open, one-close
bracketing convention its word is a fully matched Dyck word.  A rank-`n-1`
subset is obtained by changing one closing `1` to `0`.  This preserves every
prefix inequality and changes total zero-minus-one balance from zero to two,
so the result has exactly two free zeros and lies in a radius-one chain.

The second assertion is the complement-and-reversal dual of the first.  That
involution preserves BTK chain radius and takes a singleton to a singleton.
`square`

The `{z}->{z}` donors arise only from core chains of radius at least two.
Lemma 3.1 therefore makes both incidence graphs in (2.1) empty.

### Corollary 3.2

For every canonical BTK core, each of the two product-local transversal
matroids has rank zero.  Their common-basis rank is zero instead of the
required `K=Cat_n`.

The conclusion is invariant under a coordinate conjugacy of BTK and under
either ordered orientation of a proposed switch.  It does not cover a
central rethread which changes the BTK singleton set or nonmiddle skeleton.

## 4. Exact finite replay

The independent standard-library audit checks every core singleton, every
radius-at-least-two donor, both shore incidence matrices, and the raw product
graph for `m=4,...,8`.

| ambient `m` | seams `K` | donors `P` | lower incidences | upper incidences | common rank | raw max degree |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 5 | 6 | 0 | 0 | 0 | 4 |
| 5 | 14 | 28 | 0 | 0 | 0 | 5 |
| 6 | 42 | 120 | 0 | 0 | 0 | 6 |
| 7 | 132 | 495 | 0 | 0 | 0 | 7 |
| 8 | 429 | 2002 | 0 | 0 | 0 | 8 |

In every row the raw product tails are distinct.  Its heads are repeated,
with maximum multiplicity `m`.  The undirected physical graph is a forest
with `Cat_m` components, but its degree exceeds two, so no orientation can
make both middle roles injective.

Run:

```text
python3 scratch/audit_catalan_a1_fiveflow_product_btk_gate_20260731.py
```

The separate exact atom enumerator

```text
scratch/audit_balanced_subcube_two_coordinate_fractional_recursion_20260731.py
```

passes for the same five values of `m`; its middle loads agree with (5.7).
Thus the integral product-local failure is not reinterpreted as a fractional
capacity failure.

## 5. Exact scope

Proved here:

1. the exact raw product ledger and its `K`-unit difference from the
   five-flow ledger;
2. the exact two-shore common-transversal condition for a local correction;
3. the all-`n` two-sided BTK radius-one obstruction; and
4. finite middle-role and physical-topology audits through ambient `m=8`.

Not proved or claimed:

* a no-go for another SCD or a rethreaded nonmiddle skeleton;
* a no-go for a nonlocal or nonproduct integral realization of (5.6);
* failure of Theorem 5.3's fractional matching;
* unrestricted Catalan Linear Matching or the full compiler theorem.

