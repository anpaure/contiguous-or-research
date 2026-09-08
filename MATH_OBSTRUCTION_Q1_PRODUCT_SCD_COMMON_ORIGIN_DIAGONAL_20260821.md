# The product-SCD `q=1` matching has an unavoidable common-origin diagonal obstruction

**Status (2026-08-21).** Every assertion below is proved.  Fix complementary
tight-cycle factors and one relative counter origin for each order pair.
At a nontrivial payload rank, the physical clustered atom colors each entire
counter-sum diagonal `A` or `B`.  The product-SCD matching instead colors a
source `(X,Y)` by whether the bottom rank of the SCD chain containing `X` is
smaller or larger than the bottom rank of the chain containing `Y`.

These two color rules cannot agree on every selected cell of any active
order-pair atom.  More quantitatively, an active atom at payload rank `r`
has at least `min(r,b-r)` wrong-side SCD edges for every origin.  Across the
near-perfect `q=1` product-SCD matching, any lift which keeps its prescribed
edges must therefore switch or delete at least

\[
 \Omega(W_b/b),\qquad W_b={2b\choose b},
\]

before the separate cyclic-successor-label constraint is even considered.

This is a precise obstruction to a zero-switch atomwise lift, not to
coefficient one.  The forced cost is `o(W_b)`.  A switch/absorption theorem
could still replace all wrong cells while preserving labelled-target
uniqueness and the clustered color capacities.

## 1. Exact physical cell map in one clustered atom

Let `b` be an odd prime, let `1<=r<=b-1`, and fix a cyclic order `alpha` on
`A` and a cyclic order `beta` on `B`.  Write their relevant window decks as

\[
 X_u=\{\alpha_u,\ldots,\alpha_{u+r-1}\},\qquad
 Y_v=\{\beta_v,\ldots,\beta_{v+b-r-1}\},             \tag{1.1}
\]

with indices in `Z_b`.  Use the clustered type schedule

\[
 \tau_r=A^rB^{b-r}                                   \tag{1.2}
\]

and start the `B` stream at relative origin `theta in Z_b`.

Write a word position as `t=bm+s`, where `m,s in Z_b`.  Let `a_s` and
`b_s` be the numbers of `A` and `B` symbols before phase `s` of (1.2), so
`a_s+b_s=s`.  The two window-start indices at `t` are

\[
 u=rm+a_s,qquad v=(b-r)m+b_s+\theta\pmod b.          \tag{1.3}
\]

Consequently

\[
 s=u+v-\theta\pmod b.                               \tag{1.4}
\]

Conversely, (1.4) determines `s`, after which (1.3) determines `m` because
`r` is invertible modulo the prime `b`.  Thus the `b^2` middle windows of
the atom are exactly the Cartesian cells `(X_u,Y_v)`, each once.

The symbol immediately after a length-`b` window has the same type as its
starting phase.  Hence the physical `q=1` color of the cell `(u,v)` is

\[
 \chi_\theta(u,v)=
 \begin{cases}
 A,&u+v\in D_A(\theta):=\theta+\{0,1,\ldots,r-1\},\\
 B,&u+v\notin D_A(\theta).
 \end{cases}                                         \tag{1.5}
\]

In particular, all `b` cells on one counter-sum diagonal have the same
physical color.  If the color is `A`, the actual added label is
`alpha_(u+r)`; if it is `B`, the actual added label is `beta_(v+b-r)`.

## 2. The two exact consistency constraints

Fix SCDs on the Boolean lattices of `A` and `B`.  For a set in either SCD,
let `bot` denote the bottom rank of its unique chain.  On the two decks put

\[
 p_u=\operatorname{bot}_A(X_u),\qquad
 q_v=\operatorname{bot}_B(Y_v).                     \tag{2.1}
\]

The product-SCD matching selects

\[
 \begin{array}{c|c}
 p_u<q_v&\text{the SCD successor of }X_u\text{, an `A` edge},\\
 p_u>q_v&\text{the SCD successor of }Y_v\text{, a `B` edge},\\
 p_u=q_v&\text{no edge}.
 \end{array}                                         \tag{2.2}
\]

The successors in the first two rows exist because the chain with smaller
bottom rank is not at its top at this product rank.

There are two distinct requirements for an atomwise lift.

1. **Common-origin side consistency.**  Define

   \[
   \begin{aligned}
   \mathcal B_\theta={}&
   \{(u,v):p_u<q_v,\ u+v\notin D_A(\theta)\}\\
   &\cup\{(u,v):p_u>q_v,\ u+v\in D_A(\theta)\}.
   \end{aligned}                                     \tag{2.3}
   \]

   Every cell in \(\mathcal B_\theta\) must be switched or deleted: its
   physical side is opposite to the side of its prescribed SCD edge.

2. **Cyclic-successor consistency.**  Even outside (2.3), a retained
   `A` edge requires

   \[
   X_u^+=X_u\cup\{\alpha_{u+r}\},                    \tag{2.4}
   \]

   where `X_u^+` is its SCD successor.  A retained `B` edge analogously
   requires

   \[
   Y_v^+=Y_v\cup\{\beta_{v+b-r}\}.                  \tag{2.5}
   \]

   These conditions must hold for the one cyclic order containing the set
   in the fixed tight-cycle factor; tokens cannot choose a new conjugation
   independently.

As a useful necessary ledger for (2.4), every label occurs as the entering
successor of exactly

\[
 {1\over b}{b\choose r}                              \tag{2.6}
\]

rank-`r` windows in a tight-cycle factor.  Indeed each cyclic order uses
every label once as an entering symbol, and the factor has
\(\binom br/b\) orders.  Thus the number of distinct retained rank-`r` sets
whose SCD successor adds any one fixed label may not exceed (2.6).
Equations (2.3)--(2.6), not the global token
color caps alone, are the exact first physical consistency constraints.

## 3. A diagonal-comparison lemma

The next lemma uses only common-origin side consistency.

### Lemma 3.1 (every active comparison matrix has many wrong diagonals)

Let `b` be prime, let `p=(p_u)` and `q=(q_v)` be two real sequences indexed
by `Z_b`, and color `r` counter-sum diagonals `A` and the other `b-r`
diagonals `B`, where `0<r<b`.  A cell desires color `A` when `p_u<q_v`,
color `B` when `p_u>q_v`, and no color when they are equal.

If at least one cell has unequal entries, then the number of cells whose
desired color disagrees with the diagonal color is at least

\[
 \min(r,b-r).                                        \tag{3.1}
\]

In particular, zero disagreements are possible only when both sequences
are constant with the same value, in which case every cell is unselected.

#### Proof

For a diagonal `d`, put

\[
 \Delta_{d,u}=p_u-q_{d-u}.
\]

Its sum

\[
 \Delta=\sum_u p_u-\sum_v q_v                      \tag{3.2}
\]

is independent of `d`.

If `Delta>0`, every `A`-colored diagonal contains a positive entry
`Delta_(d,u)>0`; that cell desires `B`.  The `r` disjoint `A` diagonals
therefore contain at least `r` disagreements.  If `Delta<0`, the same
argument on the `b-r` `B` diagonals gives at least `b-r` disagreements.

Suppose `Delta=0`.  On every diagonal which is not identically zero, the
entries include both a positive and a negative value.  Whichever color that
diagonal receives, it contains a disagreement.  If two distinct diagonals
`d,d'` were identically zero, then

\[
 q_{d-u}=p_u=q_{d'-u}\quad\hbox{for all }u,
\]

so `q` would have the nonzero period `d'-d`.  Primality of `b` would make
`q`, and then `p`, constant.  In the active case at most one diagonal is
identically zero.  Hence there are at least `b-1` disagreements, which is
at least (3.1).  The same argument shows that zero disagreements forces the
constant equal case.  \(\square\)

### Theorem 3.2 (no active atom admits an exact product-SCD lift)

For every order pair and every relative origin,

\[
 \boxed{\mathcal B_\theta=\varnothing
 \quad\Longrightarrow\quad
 p_u=q_v\text{ for all }u,v.}                       \tag{3.3}
\]

Consequently an atom on which the product-SCD matching selects even one
source cannot realize all of its prescribed edges.  This remains true if
the cyclic orders satisfy every successor-label condition (2.4)--(2.5).

#### Proof

Apply Lemma 3.1 to the `r` physical `A` diagonals (1.5).  Its disagreement
set is exactly (2.3).  If it is empty, the two bottom-rank sequences are
constant and equal, so (2.2) selects no cell.  \(\square\)

Thus choosing phases after constructing the product-SCD matching cannot be
an exact lift algorithm.  The obstruction is caused by the one shared
origin inside each physical atom, not by a shortage in the global `A/B`
token ledger.

## 4. A global lower bound on the required switch set

Let

\[
 L_r={b\choose r}^2,\qquad t=\min(r,b-r),
\]

and retain the notation

\[
 M_r=2F_t                                                   \tag{4.1}
\]

for the exact number of product-SCD matching edges whose source has split
`r`.  Conditional tight-cycle factors contain exactly

\[
 N_r={L_r\over b^2}                                      \tag{4.2}
\]

order-pair atoms at this payload rank, and their `b^2` source cells
partition \(\mathcal U_r\).

Call an atom active if it contains at least one of the `M_r` selected
sources.  Since one atom has only `b^2` cells, the number of active atoms is
at least `M_r/b^2`.  Lemma 3.1 gives at least `t` wrong-side cells in every
active atom, for every choice of its origin.  Therefore every physical lift
which starts from the prescribed product-SCD edges must switch or delete at
least

\[
 \boxed{B_r\ge {tM_r\over b^2}}                       \tag{4.3}
\]

edges at split `r` merely to repair their sides.

Summed over the central third, (4.3) gives

\[
 \boxed{\sum_r B_r\ge(1-o(1)){W_b\over3b}.}           \tag{4.4}
\]

Indeed, the product-SCD matching has total size

\[
 {2b\choose b+1}-O(W_b/\sqrt b)=(1-o(1))W_b.
\]

The number of sources with `r` outside `[b/3,2b/3]` is
\(e^{-\Omega(b)}W_b\), so

\[
 \sum_{b/3\le r\le2b/3}M_r=(1-o(1))W_b.             \tag{4.5}
\]

On this interval `t>=b/3-O(1)`.  Sum (4.3) and use (4.5) to obtain (4.4).

The bound (4.4) is asymptotically sublinear.  It rules out a zero-change
compiler but is compatible with an `o(W_b)` absorber.

## 5. Exact switch/absorption target left open

For a fixed physical factor bank define the full local repair ledger as the
union of

* the side-mismatch cells \(\mathcal B_\theta\) in (2.3); and
* the correct-side cells failing the successor identities (2.4)--(2.5).

A sufficient physical lifting theorem would find, after choosing one origin
per order pair, vertex-disjoint alternating containment switches which
replace this ledger and preserve:

1. distinct middle sources and distinct labelled upper targets;
2. the rankwise clustered `A/B` capacities;
3. one common cyclic order and origin on every atom; and
4. total switched or discarded mass `o(W_b)`.

Such a switch cannot be confined to one unequal-bottom product-SCD
rectangle.  At `q=1` that rectangle's source and target diagonals have the
same size and their containment graph has a unique perfect matching: the
all-`A` matching when the `A`-chain bottom is smaller, and the all-`B`
matching when it is larger.  Therefore every side-changing repair which
still saturates the affected targets must cross between distinct SCD chain
pairs (or deliberately leave a target unmatched).  The required absorber
is genuinely a cross-rectangle object.

The ambient adjacent-level Boolean incidence graph has no `4`-cycle: two
distinct `b`-sets have at most one common `(b+1)`-superset.  Its smallest
alternating repair is therefore a `6`-cycle.  Explicitly, for a
`(b-1)`-set `R` and three distinct outside labels `x,y,z`, its lower shore is

\[
 R\cup\{x\},\quad R\cup\{y\},\quad R\cup\{z\},
\]

and its upper shore is

\[
 R\cup\{x,y\},\quad R\cup\{y,z\},\quad R\cup\{z,x\}.
\]

Switching the two alternating perfect matchings cyclically permutes the
three added labels.  Hence the first plausible absorber is a packing of
cross-rectangle Boolean `6`-cycles (and longer alternating cycles) whose
label permutations repair the ledger while respecting the fixed physical
successors.  Existence of such a packing at `o(W_b)` cost remains open.

The present theorem proves that the ledger can never be empty and has size
at least \(\Omega(W_b/b)\).  It gives no matching upper bound for an optimally
chosen SCD/factor bank, and it does not rule out an absorber of size
`O(W_b/b)` or larger but still `o(W_b)`.  Offsets `q>=2` impose additional
nested-prefix consistency and are outside this note.
