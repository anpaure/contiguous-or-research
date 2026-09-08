# Erosion--Johnson controller duality

Date: 2026-07-28

Status: unconditional structural theorem, independently verified on every
raw optimum `k=9,...,14`.  It does not construct the missing `k=15` word.

## 1. From a resident middle carrier to a lower Johnson controller

Let

\[
 T_0,T_1,\ldots,T_{W-1}\in{[k]\choose r}
\]

be a Johnson path, with

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\tag{1.1}
\]

Assume every internal coordinate run in `T` has length at least `d+1`, and
define its maximal depth-`d` erosion

\[
 P_j=\bigcap_{i=\max(0,j-d)}^{\min(j,W-1)}T_i,
 \qquad 0\le j<W+d.
\tag{1.2}
\]

### Theorem 1.1 (erosion is a Johnson controller)

For every fully interior index,

\[
 |P_j|=r-d,
\]

and consecutive erosion states are Johnson-adjacent.  More precisely,

\[
 \boxed{
 P_j\setminus P_{j+1}=\{\alpha_j\},\qquad
 P_j\setminus P_{j-1}=\{\beta_{j-d-1}\}.}
\tag{1.3}
\]

#### Proof

Across the `d` transitions from `T_(j-d)` to `T_j`, the deleted coordinates
are distinct.  Otherwise one coordinate would have to be reinserted and
deleted again inside fewer than `d+1` carrier positions, contradicting
residence.  Hence

\[
 P_j=T_{j-d}\setminus
 \{\alpha_{j-d},\ldots,\alpha_{j-1}\}
\]

and has rank `r-d`.

The coordinate `alpha_j` lies throughout `T_(j-d),...,T_j`, because its
run ends at transition `j` and is at least `d+1` positions long.  It is
absent from `T_(j+1)`, giving the first equality in (1.3).  Dually,
`beta_(j-d-1)` is absent just before `T_(j-d)` and remains present through
`T_j`; it is the unique coordinate gained when the erosion window moves
from `j-1` to `j`.  Equal ranks then give Johnson adjacency. \(\square\)

Thus the maximal erosion is not merely a family of legal envelopes: its
flat interior is one rank-`(r-d)` Johnson walk.

## 2. The physical word is a pinning of the controller

Suppose a physical word `A` satisfies

\[
 D^dA=T.
\]

Then `A_j subseteq P_j`.  The run-boundary lemma and (1.3) sharpen this to

\[
 \boxed{
 \bigl(P_j\setminus P_{j-1}\bigr)
 \cup\bigl(P_j\setminus P_{j+1}\bigr)
 \subseteq A_j\subseteq P_j.}
\tag{2.1}

In words: every physical letter contains the incoming and outgoing
transition coordinates of the erosion-controller walk.

### Corollary 2.1 (minimum carrier runs are singleton ports)

The two mandatory coordinates in (2.1) coincide exactly when one coordinate
has a carrier run of the minimum allowed length `d+1`.  Equivalently, that
coordinate has a one-vertex run in the controller `P`.

This is the structural reason that threshold residence is useful.  Such a
controller vertex has a one-coordinate mandatory core and can host a
singleton or another very small compiler letter.  Making every run much
longer removes, rather than creates, this capacity.

## 3. Exact run-pinning condition

The port condition (2.1) is necessary but not sufficient on a long
controller run.  Let `[u,v]` be an internal maximal run of coordinate `x`
in `P`, and let

\[
 Q_x=\{j\in[u,v]:x\in A_j\}.
\]

Then the coordinatewise identity `D^dA=T` is equivalent to

\[
 \boxed{
 u,v\in Q_x,
 \qquad q_{t+1}-q_t\le d+1
 \text{ for consecutive }q_t,q_{t+1}\in Q_x.}
\tag{3.1}

The two endpoints are the incoming and outgoing ports in (2.1); additional
pins are needed only when the controller run is too long.

#### Proof

If the corresponding carrier run is `[a,b]`, its erosion run is
`[u,v]=[a+d,b]`.  An occurrence of `x` in physical position `q` covers
carrier indices `[q-d,q]`.  These intervals cover `[a,b]` exactly when the
first and last pins are `a+d=u` and `b=v`, and consecutive pins have gap at
most `d+1`.  No pin may lie outside `[u,v]` because `A_q subseteq P_q`.
\(\square\)

Boundary runs have the analogous one-sided endpoint condition.

## 4. Reframed construction target

### Theorem 4.1 (controller-incidence congruence)

For a coordinate `x`, let `t_x` be its number of occurrences in the middle
carrier `T`, let `p_x` be its number of occurrences in the maximal erosion
controller `P`, and let `i_x` be the number of internal maximal `x`-runs in
`T`.  Let `b_x=1` if `x` occurs in every state of `T`, and let `b_x=0`
otherwise.  Then, counting all `W+d` one-sided controller positions,

\[
 \boxed{p_x=t_x-d i_x+d b_x.}
\tag{4.1}
\]

In particular, if `T` is the exact middle deck and `d>=1`, then

\[
 p_x\equiv {k-1\choose r-1}\pmod d
\tag{4.2}
\]

for every coordinate.

#### Proof

An internal carrier run `[a,b]` erodes to `[a+d,b]` and therefore loses
exactly `d` incidences.  A proper run touching only the left boundary erodes
to `[0,b]`, and a proper run touching only the right boundary erodes to
`[a+d,W+d-1]`; each retains its original number of incidences because the
erosion window is clipped at that boundary.  A run spanning both boundaries
is present in all `W+d` controller states and gains `d` incidences.  Summing
over all runs gives (4.1).  In an exact middle deck with `0<r<k`, no
coordinate occurs everywhere, so `b_x=0`; every coordinate occurs in exactly
`{k-1 choose r-1}` middle sets, giving (4.2) when `d>=1`. \(\square\)

This is a genuine global constraint on a braid's maximal controller `P`; it
does not count occurrences in a pinned physical compiler \(A\subseteq P\).
For an exact middle deck, adding desired maximal-controller incidences at
selected coordinates must be accompanied by deletions so that every
coordinate count changes by a multiple of `d`, in addition to preserving the
rank of every controller state.

The flat-carrier architecture can therefore be stated one level lower:

1. construct a maximal controller `P` whose flat interior has rank `r-d`,
   together with its canonical clipped one-sided collars;
2. require every `(d+1)`-window union of `P` to be a different rank-`r`
   set, exhausting the middle layer;
3. require longer window unions to cover the upper ideal;
4. choose, on every coordinate run of `P`, a pin set satisfying (3.1) so
   that the resulting physical letters cover the lower ideal.

This is equivalent to the resident flat-carrier problem, but it exposes the
only genuine compiler freedom: the placement of extra pins between forced
incoming/outgoing ports.  The `k=15` Hall-29 defect is a failure of these
port/pin choices to furnish enough distinct short physical cells.

## 5. Raw-certificate audit

The exact script

```text
python3 scratch/audit_erosion_johnson_controller.py
```

reconstructs `T` and `P` only from `answers/k09.word` through
`answers/k14.word`.  In every case it verifies:

* the flat interior rank `r-d`;
* Johnson adjacency of every consecutive interior `P_j`;
* both identities in (1.3);
* containment of the forced controller ports in the raw `A_j`; and
* the endpoint-and-gap pin rule (3.1) on every internal coordinate run.
