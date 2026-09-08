# The coatom flag lattice is saturated but its short packets are not a Markov basis

Date: 2026-08-01  
Lane: serial coatom lower routing / occurrence-resolved flags  
Status: exact nonnegative counterexample for the **common-order short-flag
subcatalogue**, with an explicit two-packet signed decomposition.  This is
an abstract subcatalogue theorem; the displayed tables are not claimed to
occur in a particular safe carrier.

Scope correction (2026-08-01):
`MATH_THEOREM_COATOM_SINGLE_BLOCK_ORDER_REFLECTION_BREAKER_20260801.md`
supplies a safe endpoint-planted move outside the common-order action (1.2).
It breaks the reflected pair current while retaining U1--U4 and residence.
Consequently the isolation proved below is **not** an obstruction for the
enlarged planted safe-move catalogue.

## 0. Result

The signed conclusions of
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`
are correct and remain authoritative:

* at depth two, short coatom Pluecker squares generate the entire integer
  point-degree kernel; and
* after forgetting cross-depth occurrence ownership, the coupled maximal-
  chain signatures generate the stated saturated reflected lattice.

Neither statement is a nonnegative Markov theorem for that subcatalogue.
Already at residence depth three there are two occurrence-resolved strict-
flag tables which

1. have the same point degrees at both depths;
2. have the same reflected pair signature;
3. have the same deletion word and every conditioned terminal degree
   `J_(x,i)`;
4. differ by the sum of exactly two legitimate signed coatom actions; but
5. are both isolated under nonnegative coatom actions.

Thus allowing all common-order filler flags removes the signed lattice-index
obstruction, but does not remove the applicability obstruction *inside that
move family*.  Algebraic cancellation uses two intermediate flags which are
absent at either endpoint.  The one-block order breaker is a different move
family and is not represented in this sparse strict-flag fibre.

## 1. Depth-three flag form

Fix a bottom rank `s>=3`.  For an `s`-set `B` and a coordinate `x` outside
`B`, write

\[
              \widehat B_x=(B\cup\{x\}\supset B).       \tag{1.1}
\]

This is a strict flag at depths two and three, with deletion word `(x)`.
For `d=3`, the coatom formula has internal fillers `(f_1,x,f_3)`.  Its
bottom action is

\[
 [Gaf_1]+[Gbf_3]-[Gbf_1]-[Gaf_3],                    \tag{1.2}
\]

where `|G|=s-2`, and its top action is obtained by adjoining `x` to all
four sets.  Hence every short rank-`s` Pluecker square avoiding `x` lifts
to one coupled depth-three flag action.

Conversely, the two negative bottoms of a nonzero action (1.2) intersect
in exactly the `(s-2)`-set `G`.  This is the only fact about applicability
needed below.

## 2. A two-flag fibre with two-packet signed distance

Let `C` be any `(s-3)`-set and choose distinct coordinates

\[
                    1,2,3,4,5,6,x\notin C.           \tag{2.1}
\]

The ambient ground set may contain additional unused coordinates.  In the
literal stable packet range, take enough of them to supply the four inactive
packet roles required by each labelled short square.

Define

\[
\begin{aligned}
 X&=[\widehat{C123}_x]+[\widehat{C456}_x],\\
 Y&=[\widehat{C124}_x]+[\widehat{C356}_x].           \tag{2.2}
\end{aligned}
\]

At depth three, both tables contain every coordinate of `C` twice and each
of `1,...,6` once.  At depth two they have those same degrees and additionally
contain `x` twice.  Thus all point degrees agree.

The deletion word of all four flags is `(x)`.  Consequently the nested
invariant from
`MATH_AUDIT_H2_COATOM_FLAG_PLUCKER_SCOPE_AND_NESTED_J_OBSTRUCTION_20260801.md`
is

\[
 J_{x,i}(Z)=\sum_{\widehat B_x} Z_{\widehat B_x}
                              {\bf1}_{\{i\in B\}}.    \tag{2.3}
\]

It agrees on `X,Y`, because their bottom point degrees agree.  Their
reflected pair signatures agree as well.  Indeed, adjoining `x` changes
`deg^(2)_2-deg^(2)_3` only on pairs `{x,i}`, where its value is exactly
the common bottom degree of `i`.

Nevertheless, `X,Y` are in the same *integer* coatom-move lattice.  Put

\[
\begin{aligned}
 M_1={}&[\widehat{C124}_x]+[\widehat{C135}_x]
       -[\widehat{C123}_x]-[\widehat{C145}_x],\\
 M_2={}&[\widehat{C145}_x]+[\widehat{C356}_x]
       -[\widehat{C135}_x]-[\widehat{C456}_x].       \tag{2.4}
\end{aligned}
\]

The four bottoms of `M_1` have common `(s-2)`-core `C1`; those of `M_2`
have common core `C5`.  Hence both are literal actions of the form (1.2),
and

\[
                             Y-X=M_1+M_2.             \tag{2.5}
\]

The intermediate flags `C145` and `C135` cancel in (2.5).  This is a
two-step signed identity, not a legal serial order from either endpoint.

## 3. Both endpoints are isolated

The two occupied bottoms of `X` intersect exactly in `C`, of size `s-3`.
The same is true of the two occupied bottoms of `Y`.  A nonnegative coatom
move needs two donor bottoms sharing an `(s-2)`-core.  Since each table has
total mass two, neither has any other possible donor pair.  Therefore

\[
                 \deg_{\rm move}(X)=\deg_{\rm move}(Y)=0.       \tag{3.1}
\]

Equations (2.5) and (3.1) prove:

### Theorem 3.1

For `d=3` and every bottom rank `s>=3`, the common-order catalogue of coupled
coatom flag actions of the form (1.2) is not a Markov basis for nonnegative
strict-flag tables, even after fixing point degrees, the reflected pair
signature, the deletion word, and all conditioned terminal degrees
`J_(x,i)`.

The obstruction has minimum possible mass.  At mass one, the bottom and top
point-degree rows recover the sole flag.  It also has minimum signed packet
length: `Y-X` is not one short square because its negative bottoms meet in
only `s-3`, while (2.5) uses two.

The packet's stable physical rank hypothesis uses `r>=d+4`; here
`s=r-3`, so the first directly stable instance is `s=4`.  The unpadded
`s=3` table is the smallest abstract incidence model, and suspension by
`C` gives every larger rank.

## 4. Exact missing actuator

The degree-two long exchange

\[
 [\widehat{C124}_x]+[\widehat{C356}_x]
 -[\widehat{C123}_x]-[\widehat{C456}_x]              \tag{4.1}
\]

is the smallest actuator which joins this fibre.  It is a general symmetric
exchange, not a short common-core coatom square.  Equivalently, either of the
intermediate flags `C145,C135` would act as a catalyst for the two short
packets in (2.4), but neither is present in (2.2).

The catalyst statement is literal and sharp.  Add one copy of
`widehat(C145)_x` to both endpoints.  Then

\[
\begin{aligned}
 X+[\widehat{C145}_x]
 &\xrightarrow{M_1}
 [\widehat{C124}_x]+[\widehat{C135}_x]+[\widehat{C456}_x]\\
 &\xrightarrow{M_2}
 Y+[\widehat{C145}_x].                              \tag{4.2}
\end{aligned}
\]

Every coefficient in (4.2) is nonnegative.  Zero catalysts cannot work by
Theorem 3.1, while one does, so this fibre has exact abstract catalyst number
one.  The two moves use distinct square cores `C1` and `C5`: even the
smallest positive shelling already needs cancellation across different
filler flags.

There is also an exact **common-order** fixed-filler limitation.  In the
authoritative maximal-chain sublattice, complement antisymmetry gives

\[
                  x_{d-1}(F-X)=-x_1(X).             \tag{4.3}
\]

Thus a nonzero depth-two action cannot have zero deepest action inside one
common-order `(G,a,b,F)` flag block.  A pure depth-two correction made only
from those flags must cancel between different filler blocks or against
outside witnesses.  Formula (4.2) shows that cross-block cancellation is
algebraically and nonnegatively possible at `d=3`, but only after the
catalyst flag is physically present.  This conclusion does not apply to the
label-attached single-block reorder, whose filler order differs between
active blocks and whose exact reflection defect is

\[
 [f_0f_1]-[f_0f_2]-[pf_1]+[pf_2].                 \tag{4.4}
\]

This identifies the next physical question precisely.  A serial theorem
needs one of:

1. a resident upper-transparent long-exchange packet;
2. a guaranteed catalyst bank supporting telescoping short squares; or
3. a carrier-specific positivity theorem showing that relevant compiler
   fibres never approach the sparse isolated face (2.2).

Signed saturation alone supplies none of these.

## 5. Scope reconciliation

There are three distinct objects.

* **Signed rankwise marginals.**  The authoritative maximal-chain and
  Pluecker theorems are GO.
* **Occurrence-resolved signed flags.**  Deletion-word-conditioned degrees
  survive projection, as proved in the independent `J` audit.
* **Common-order nonnegative applicability.**  Even after fixing those `J`
  degrees, Theorem 3.1 gives a disconnected subcatalogue fibre.
* **Enlarged planted catalogue.**  The one-block order breaker escapes the
  reflected quadratic fibre; connectivity of its full occurrence-labelled
  nonnegative fibres is not decided here.

The common-order statement does not contradict saturation: the two missing
intermediate flags occur with opposite signs and cancel in the integer
identity.  Nor does the abstract table prove that a particular safe carrier
contains such an isolated state.  It refutes only the claim that the
common-order short-flag subcatalogue is, by itself, a universal Markov basis.

## 6. Independent replay

Run

```text
python3 scratch/audit_h2_coatom_flag_nonnegative_markov_obstruction_20260801.py
```

The dependency-free audit checks bottom ranks `3,...,10`, both depth-degree
rows, every reflected pair coordinate, deletion-conditioned terminal
degrees, the two short-square cores, their exact cancellation, and zero
applicable moves at both endpoints.  It also verifies the one-catalyst
two-step path (4.2) and enumerates the smallest
rank-three point-degree-one fibre: its ten unordered two-edge partitions
are all isolated under short squares.

It reports

```text
PASS_COATOM_FLAG_INTEGER_SPAN_BUT_NONNEGATIVE_MARKOV_NOGO
```

with canonical payload SHA-256

```text
7296ae14288bcb5956e6340c77d1395a063f6a2471738911fd17ddfa378c5345
```

Artifacts:

```text
scratch/audit_h2_coatom_flag_nonnegative_markov_obstruction_20260801.py
  71ba9cd06a985bca2cc1badbac76ac91d249694165fc68b660adcdd2c55dc7ce
scratch/h2_coatom_flag_nonnegative_markov_obstruction_20260801.audit.json
  87ba936ac9b85e6e58e411bda613c90953f3f570d9f41feb4b8f79d4c4e60b78
```
