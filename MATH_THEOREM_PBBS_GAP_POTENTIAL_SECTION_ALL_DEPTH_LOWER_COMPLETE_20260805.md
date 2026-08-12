# A fixed PBBS gap-potential section is lower-complete at every depth

**Date:** 2026-08-05  
**Method:** pure cyclic-parenthesis mathematics; no computation or search  
**Status:** unconditional for every `m>=1`.  This closes the one-sided
fixed-factor common-section gate.  It does not claim simultaneous
phase-shifted upper coverage, cycle hitting, residence after cutting, or a
literal ordinary-word realization.

## 1. The canonical section

Put

\[
 n=2m+1,
 \qquad
 g=f^2:{[n]\choose m}\longrightarrow{[n]\choose m},
\]

where `f` is the canonical cyclic-parenthesis PBBS map.  For

\[
 K\in{[n]\choose m-1},
\]

write `A` on every forward-unmatched zero of the deficit-three word of
`K`, and `C` on every reverse-unmatched zero.  There are three symbols of
each type.  If a physical coordinate has both labels, expand it in the
fixed order

\[
                         C_x,A_x.                 \tag{1.1}
\]

Index the `C` symbols cyclically.  Let `z_i` be the number of `A` symbols
strictly between `C_i` and `C_(i+1)`, and define a cyclic potential, up to
an additive constant, by

\[
                  h(i+1)-h(i)=z_i-1.              \tag{1.2}
\]

Since `sum z_i=3`, the potential is periodic.  Choose any `C_i` at which
`h` is maximal and let `A_i^*` be the last `A` symbol strictly before it.
The preceding gap is nonempty: maximality gives

\[
 z_{i-1}-1=h(i)-h(i-1)\ge0.                       \tag{1.3}
\]

The two symbols in this `A-->C` boundary are at different physical
coordinates, because a shared coordinate is ordered `C,A`, not `A,C`.

The global-maximum corridor theorem at depth one says exactly that

\[
                     g(K+C_i)=K+A_i^*.            \tag{1.4}
\]

Thus (1.4) is a corrected occurrence of the q1 colour `K`.  Resolve any
remaining tie between maximal `C` symbols by an arbitrary fixed rule
(for example, least physical coordinate).  Denote the resulting start by

\[
                         \sigma(K)=K+C_i.          \tag{1.5}
\]

This defines one occurrence of every q1 colour using only the literal
deficit-three word `K`.  No target at a deeper depth enters its definition.

## 2. The survivor-order lemma

Fix `q>=2` and

\[
                         S\in{[n]\choose m-q}.
\]

Apply the audited all-depth global-maximum corridor construction to the
expanded deficit-`(2q+1)` word of `S`.  At its selected boundary write

\[
 A_0,C_0,
\]

number the `C` symbols forward as

\[
 C_0,C_1,\ldots,C_{2q},
\]

and the `A` symbols backward as

\[
 A_0,A_1,\ldots,A_{2q}.
\]

The corridor inequalities are

\[
 x_j\le j,
 \qquad
 y_j\le j,                                        \tag{2.1}
\]

where `y_j` is the number of `C` symbols crossed on moving backward from
`A_0` to `A_j`.  The corridor fan is

\[
 B_t=S+\{C_0,\ldots,C_{q-t-1}\}
       +\{A_0,\ldots,A_{t-1}\},
 \qquad 0\le t\le q.                              \tag{2.2}
\]

Its first q1 core is

\[
                  K_0=S+\{C_0,\ldots,C_{q-2}\},   \tag{2.3}
\]

and the first transition is

\[
                  B_0=K_0+C_{q-1}
                  \longrightarrow
                  B_1=K_0+A_0.                    \tag{2.4}
\]

### Lemma 2.1 (literal induced survivor order)

In the deficit-three word of `K_0`, the forward-unmatched symbols are

\[
                         A_0,A_1,A_2,              \tag{2.5}
\]

and the reverse-unmatched symbols are

\[
                         C_{q-1},C_q,C_{q+1}.       \tag{2.6}
\]

Their expanded cyclic order is inherited by deleting all other symbols
from the expanded word of `S`.  In that induced six-symbol word:

1. there is no retained `A` strictly between `C_(q-1)` and `C_q`;
2. there is at most one retained `A` strictly between `C_q` and
   `C_(q+1)`;
3. `A_0` is the last retained `A` before `C_(q-1)`.

#### Proof

The survivor identities (2.5)--(2.6) are the exact forward and reverse
survivor calculation in the all-depth corridor theorem, specialized to
`t=0`.  Parenthesis contraction deletes matched symbols but does not
change the cyclic order of surviving physical symbols.  At a shared
coordinate both the old and induced expanded words use (1.1), so the
induced word is literally the stated restriction.

The `A` labels are numbered backward.  Hence `A_1,A_2` are the first two
`A` symbols met on moving backward from `A_0`.  By (2.1), that backward
arc crosses at most two `C` symbols.  Equivalently, in forward order both
`A_1,A_2` occur after `C_(2q-2)` (allowing equality at a shared
`C,A` coordinate), while `A_0` is in the final gap before `C_0`.

Since

\[
                 2q-2\ge q\qquad(q\ge2),          \tag{2.7}
\]

none of `A_0,A_1,A_2` lies strictly between `C_(q-1)` and `C_q`.
Moreover

\[
                 2q-2\ge q+1\qquad(q\ge3),        \tag{2.8}
\]

so for `q>=3` none lies in the next gap either.  When `q=2`, only `A_2`
can lie in that next gap.  This proves assertions 1--2.

Finally, `A_1,A_2` precede `A_0` in the backward `A` order, whereas the
symbols `C_0,...,C_(q-2)` lying after the boundary have been deleted.
Thus, among retained `A` symbols, `A_0` is the last one before
`C_(q-1)`.  This proves assertion 3. `square`

The phrase "after `C_(2q-2)`" in the proof is meant cyclically in the
forward arc ending at `A_0,C_0`.  More explicitly, if moving backward
from `A_0` to `A_h` crosses `e<=h` `C` symbols, then `A_h` belongs to
one of the last `e+1` `C`-gaps before `C_0`; this is precisely the order
used in (2.7)--(2.8).

## 3. The first fan edge is forced by the fixed section

### Theorem 3.1 (unique induced maximum)

For the q1 core `K_0` in (2.3), the potential (1.2) has its unique
maximum at `C_(q-1)`, and the last `A` before that maximum is `A_0`.
Consequently the fixed section (1.5) selects exactly the first edge
(2.4), independently of its tie rule.

#### Proof

Normalize the induced potential to be zero at `C_(q-1)`.  By Lemma 2.1,
the first induced `A`-gap has size zero, so the potential at `C_q` is
`-1`.  The union of the first two gaps contains at most one retained `A`;
therefore the potential at `C_(q+1)` is at most `-1`.  There are only
three `C` symbols and the total increment is zero.  Hence
`C_(q-1)` is the unique maximum.  Lemma 2.1(3) identifies the last
preceding `A` as `A_0`.  Equations (1.4)--(1.5) now give (2.4). `square`

### Theorem 3.2 (one fixed section is lower-complete at all depths)

For every `m>=1`, the single section `sigma` of (1.5) has the following
property.  For every `1<=q<=m` and every

\[
                         S\in{[n]\choose m-q},
\]

there is a q1 colour `K` such that

\[
 \sigma(K)=X,
 \qquad
 \bigcap_{t=0}^{q}g^tX=S.                         \tag{3.1}
\]

#### Proof

For `q=1`, take `K=S`; the selected occurrence has first intersection
`S` by definition.  For `q>=2`, apply the all-depth corridor construction
to `S` and take `K=K_0`.  Theorem 3.1 says that `sigma(K)=B_0`.  The
corridor theorem says that `g^tB_0=B_t` for `0<=t<=q` and that the
intersection of these states is `S`.  This proves (3.1).

Only the first/root occurrence is selected.  That is sufficient: after a
root `X` is fixed, all later states `gX,g^2X,...` and hence its entire
nested future tower are deterministic.  No independent representative at
a later depth is being chosen. `square`

This theorem is stronger than singleton support and proves the integral
one-sided fixed-factor common section whose existence was left open in
Section 5 of
`MATH_AUDIT_N_PBBS_NESTED_FAN_SECTION_AND_MORTALITY_GATE_20260727.md`.
It uses one canonical PBBS factor throughout; no root-dependent coordinate
conjugacy or symmetry averaging occurs.

## 4. Exact mortality, hole, and repeat ledgers

Let

\[
 \mathcal X=\{\sigma(K):K\in{[n]\choose m-1}\},
 \qquad
 M=|\mathcal X|=N_1={n\choose m-1}.                \tag{4.1}
\]

Different q1 colours give different starts, because a start `X` has the
unique outgoing q1 colour `X cap gX`.  At depth `q`, let `b_q` be the
number of selected starts of wrong rank, let `G_q=M-b_q` be the correct
mass, let `H_q` be the number of missing rank-`(m-q)` targets, and let
`E_q` and `tilde E_q` be respectively raw and floor-correct repeat excess
as in the mortality audit.

### Corollary 4.1 (exact synchronized ledger)

For every `1<=q<=m`,

\[
 \boxed{
 H_q=0,
 \qquad
 G_q\ge N_q,
 \qquad
 b_q\le N_1-N_q,
 \qquad
 E_q=G_q-N_q,
 \qquad
 \widetilde E_q=0.}                               \tag{4.2}
\]

The mortality sequence is nondecreasing and, for every `2<=q<=m`, obeys
the exact layerwise identity

\[
 0\le b_q-b_{q-1}
 = N_{q-1}-N_q-(E_q-E_{q-1}).                     \tag{4.3}
\]

equivalently,

\[
 (b_q-b_{q-1})+(E_q-E_{q-1})=N_{q-1}-N_q.         \tag{4.4}
\]

#### Proof

Theorem 3.2 gives full support, hence `H_q=0`.  Every supported target
uses a correct selected occurrence, so `G_q>=N_q` and therefore
`b_q=M-G_q<=N_1-N_q`.  If `D_q=N_q` is the support size, then

\[
                         E_q=G_q-D_q=G_q-N_q.
\]

The forced floor is `(G_q-N_q)_+=G_q-N_q`, giving
`tilde E_q=0`.  Absorbing rank excess makes `b_q` nondecreasing.  Finally,
subtraction of

\[
 H_q=N_q-M+b_q+E_q=0
\]

at consecutive depths gives (4.4); (4.3) is the same identity with the
nonnegative mortality increment isolated. `square`

Thus the mortality and floor-balanced-colour conditions of the prior audit
are solved simultaneously, not estimated asymptotically.

## 5. Integral occurrence compiler corollary

For a selected root `X` and live depth `q`, regard

\[
 (X,q)\longmapsto\bigcap_{t=0}^{q}g^tX             \tag{5.1}
\]

as an occurrence-labelled lower cell.  Cells with different ordered pairs
`(X,q)` are distinct physical interval occurrences even if their intervals
overlap in the PBBS chronology.

### Corollary 5.1 (one-sided lower occurrence SDR)

There is an injection from all nonempty targets below the middle rank into
the cells (5.1), sending every target to a cell having exactly that value.

#### Proof

At every depth `q`, Theorem 3.2 makes (5.1) surjective onto the entire
rank-`(m-q)` layer.  Choose one preimage for every target.  Within one
depth, two different targets cannot choose the same cell because a cell
has one value.  Across two depths, the cells have different second
coordinates (and their correct values have different ranks), so they are
also distinct.  The union of the depthwise choices is the required
injection. `square`

This is an occurrence-level compiler for the lower PBBS intersection
deck.  It does **not** by itself assert that all these cyclic intersection
cells survive a later opening, erosion, Ferrers-boundary deletion, or
translation into one ordinary OR word.  Any such operation must preserve
the chosen occurrence labels or provide replacements.  No additional
owner capacity is consumed inside the uncut PBBS deck: each target uses a
distinct occurrence cell, while the section already uses one distinct
root per q1 colour.

## 6. Exact scope boundary

The theorem proves:

1. one literal, fixed-factor, deterministic q1 occurrence section;
2. complete lower support at every depth on that same section;
3. zero holes and zero floor-correct repeat excess at every depth;
4. an integral one-sided lower occurrence SDR.

It does not prove:

1. that `f(\mathcal X)` is the same section, or even a lower-complete
   section;
2. simultaneous upper coverage, since
   \[
   U_q(X)=[n]\setminus L_{q-1}(fX)
   \]
   involves the phase-shifted root `fX`;
3. that the selected or unselected occurrences meet every PBBS component;
4. survival of the occurrence SDR under cutting or literal erosion;
5. residence or terminal common-cap compatibility in an ordinary word.

In particular, the rotational no-equivariant-section theorem is not
contradicted: the tie rule in (1.5) may break coordinate rotation symmetry,
and Theorem 3.1 needs no equivariant tie decision because its induced
maximum is unique.

### Proposition 6.1 (the selected roots cannot alone cover the first upper row)

No tie rule in (1.5), and in fact no family of one start per q1 lower
colour, can by itself cover every rank-`(m+1)` upper q1 target.

#### Proof

Such a family has

\[
             N_1={n\choose m-1}
\]

starts.  Each start has one upper q1 value `X union gX`.  The number of
rank-`(m+1)` targets is

\[
             {n\choose m+1}={n\choose m}=W>N_1.   \tag{6.1}
\]

Thus even support is impossible by cardinality. `square`

Equivalently, the complement identity

\[
 U_q(X)=[n]\setminus L_{q-1}(fX)
\]

shows that at `q=1` the selected phase would have to cover all `W`
middle targets with only `N_1` shifted roots.  Therefore the correct
two-sided use of this theorem must retain the unselected PBBS owner/upper
bank (or another upper bank); it cannot demand that the thinned lower
section alone be upper-complete.  This is a scalar obstruction, not a
failure of the one-sided section theorem.
