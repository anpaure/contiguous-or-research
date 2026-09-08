# Facet modules: corrected primitive ledger and a weighted joint greedy theorem

Date: 2026-08-02  
Status: exact ledger and exact sparse owner/target-label packing theorem,
conditional on the physical source ledger.  This note
retracts the reading that the buffered primitive count is
`t=A_(d+1)`.  It does not close the remaining factor-`q` interval-packing
gap.

## 0. Outcome

Put

\[
 r=\lceil k/2\rceil,\qquad q=d+2,\qquad
 c=r-d-1=r-q+1,\qquad W=\binom kr.
\]

The literal module statements use `d>=2` (hence `q>=4`) and `c>=1`.
The displayed binomial-difference formulas use the separated Ferrers range;
the sufficient inequality `c-1>d` will be assumed whenever those formulas
are invoked.  Write `n_s` for the available rank-`s` named-target inventory;
in the unreserved full-deck face, `n_s=K_s=binom(k,s)`.

A length-`q` facet module is not just one copy of
`g_(d-1,d+1)`.  Its sharp literal realization also uses `d` short
`e_(d-1)` buffers.  Consequently it consumes `q-1=d+1` occurrences from
coordinate `A_(d-1)`.  A length-`q+1` module consumes one more short
buffer and hence `q` such occurrences.

If `t` modules are used and `B` of them have length `q+1`, the exact
necessary ledger is

\[
\begin{aligned}
 t&\le A_{d+1},\\
 (q-1)t+B&\le A_{d-1},\\
 dt+B&\le E:=L-H,\\
 qt+B&\le n_{c+2}.
\end{aligned}                                                    \tag{0.1}
\]

In the canonical separated range,

\[
 A_{d+1}=\binom kc-\binom k{c-1},\qquad
 A_{d-1}=\binom k{c+2}-\binom k{c+1}.
\]

Moreover `A_(d-1)/A_(d+1)->1`.  Thus (0.1), not the owner-only bound
`t<=A_(d+1)`, gives

\[
 t\le {A_{d-1}\over q-1}=\Theta(W/q^2)=o(A_{d+1}).               \tag{0.2}
\]

Even without the buffer-coordinate row, the rank-`(c+2)` target row makes
`t=A_(d+1)` impossible: exactly

\[
 {qA_{d+1}\over\binom k{c+2}}\longrightarrow {\pi\over2}>1.     \tag{0.3}
\]

The positive result is a genuinely joint choice of owner block and full
labeling.  Let

\[
 K_s=\binom ks,
\qquad
 \Gamma={q^2\over W}+{1\over K_c}+{1\over K_{c+1}}
       +\sum_{j=2}^{q-2}{q^2\over K_{c+j}}.                     \tag{0.4}
\]

At the owner/named-target selection layer there are target-simple,
pairwise owner-disjoint labeled length-`q` module candidates of every
cardinality `t` satisfying

\[
                         (t-1)\Gamma<1.                         \tag{0.5}
\]

Canonically,

\[
 \Gamma\sim {q^3\over W}\,{1\over a}\int_0^a e^{x^2}\,dx,
 \qquad a={\sqrt\pi\over2},                                    \tag{0.6}
\]

and, more crudely but conveniently, `Gamma<=17q^3/W` for all sufficiently
large `k`.  Hence every

\[
                         t\le {W\over18q^3}                     \tag{0.7}
\]

is available exactly.  This is one factor `q` below the buffer-coordinate
ceiling (0.2); other ledger rows can lower the physically available count.

Interpreting these candidates as a physical buffered inventory additionally
requires the primitive and short-buffer source occurrences and every row of
(0.1), especially `dt+B<=E`.  The greedy theorem does not allocate that
source inventory.

The same proof allows a protected/preused bank.  Its exact weighted load is
displayed in Theorem 3.2 below.  That one scalar spread row is strictly
weaker in scope than OFHT: it only packs the primitive facet modules and
asserts none of the remaining role, predecessor-Hall, component, residence,
upper, or compiler rows.

## 1. The corrected module ledger

Write

\[
                         s=r-d=c+1.
\]

The primitive types are

\[
 P=(s-1,2,1,\ldots,1),\qquad H=(s,1,\ldots,1).
\]

The fully marked `P` occurrence has targets at ranks

\[
                    c,\ c+2,c+3,\ldots,r-1,                    \tag{1.1}
\]

because its age-one cell has size two.  The distinguished fully marked
`H` occurrence has targets at ranks

\[
                    c+1,c+2,c+3,\ldots,r-1.                    \tag{1.2}
\]

A short `e_(d-1)` copy of `H` is marked only at

\[
                    c+2,c+3,\ldots,r-1.                         \tag{1.3}
\]

### Proposition 1.1 (exact mixed-size ledger)

Suppose `t-B` primitive packets use length-`q` facet modules and `B` use
length-`q+1` common-core modules.  Then their aggregate consumption is

\[
\begin{array}{c|c}
\text{resource}&\text{consumption}\\ \hline
e_{d+1}&t\\
e_{d-1}&(q-1)t+B\\
\text{short-loop resource }L-H&dt+B\\
\text{rank-}c\text{ targets}&t\\
\text{rank-}(c+1)\text{ targets}&t\\
\text{rank-}(c+j)\text{ targets},\ 2\le j\le q-2&qt+B\\
\text{rank-}r\text{ owners}&qt+B.
\end{array}                                                     \tag{1.4}
\]

Consequently (0.1) is necessary for any such buffered realization.

#### Proof

A length-`q` module contains one primitive `P`, one primitive `H`, and `d`
short `H` buffers.  It therefore realizes

\[
                  g_{d-1,d+1}+d e_{d-1}
                 =e_{d+1}+(d+1)e_{d-1}.                        \tag{1.5}
\]

Equations (1.1)--(1.3) show that it uses one target at ranks `c,c+1` and
`d+2=q` targets at every displayed higher rank.  It has `q` owners.

A length-`q+1` module has `d+1` rather than `d` short buffers.  Relative
to (1.5), it adds one `e_(d-1)` occurrence, one target at every displayed
higher rank, and one owner.  Summing the two module sizes gives every row
of (1.4).

Every nontrivial rotor package has equal low and high resource.  A short
`e_(d-1)` loop leaves one unit of low resource, because
`d-(d-1)=1`.  The added buffers alone therefore consume slack `dt+B`, and
all other short loops contribute nonnegative slack.  This proves the
`dt+B<=L-H` row.  The remaining inequalities in (0.1) are the corresponding
coordinate and named-resource capacities.  \(\square\)

### Proposition 1.2 (the equality reading is asymptotically impossible)

For all sufficiently large canonical `k`, the assignment
`t=A_(d+1)` violates both the `A_(d-1)` row and the rank-`(c+2)` row of
(0.1), even when `B=0`.

#### Proof

In the separated range the Ferrers correction vanishes at
`c-1,c,c+1,c+2`, so the two displayed difference formulas in Section 0
hold.  For

\[
                         D_m=\binom km-\binom k{m-1}
\]

one has

\[
                         D_m=\binom km {k-2m+1\over k-m+1}.      \tag{1.6}
\]

Using (1.6) at `m=c,c+2` gives the exact ratio

\[
 {A_{d-1}\over A_{d+1}}
 = {(k-c)(k-c+1)(k-2c-3)
       \over (c+1)(c+2)(k-2c+1)}.                              \tag{1.7}
\]

If `k=2r`, (1.7) is

\[
 {(r+q-1)(r+q)(2q-5)
       \over(r-q+2)(r-q+3)(2q-1)},                             \tag{1.8}
\]

and if `k=2r-1`, it is

\[
 {(r+q-2)(r+q-1)(2q-6)
       \over(r-q+2)(r-q+3)(2q-2)}.                             \tag{1.9}
\]

Since `q->infinity` and `q/r->0`, both ratios tend to one.  Hence

\[
 {(q-1)A_{d+1}\over A_{d-1}}\sim q\longrightarrow\infty,       \tag{1.10}
\]

contradicting the second row of (0.1).

For the independent target obstruction, (1.6) and the two-step binomial
ratio give

\[
 {qA_{d+1}\over\binom k{c+2}}
 ={q(k-2c+1)(c+1)(c+2)
       \over(k-c+1)(k-c)(k-c-1)}.                              \tag{1.11}
\]

For `k=2r`, this becomes

\[
 {q(2q-1)(r-q+2)(r-q+3)
       \over(r+q)(r+q-1)(r+q-2)},                              \tag{1.12}
\]

and for `k=2r-1`, it becomes

\[
 {2q(q-1)(r-q+2)(r-q+3)
       \over(r+q-1)(r+q-2)(r+q-3)}.                            \tag{1.13}
\]

The canonical estimate `q^2/r->pi/4` makes both (1.12) and (1.13) tend
to `2q^2/r->pi/2`.  They therefore exceed one for all sufficiently large
`k`, contradicting the rank-`(c+2)` capacity.  Taking `B>0` only increases
the left sides of both violated resource rows.  \(\square\)

### Corollary 1.3 (the genuine buffered scale)

Every buffered primitive inventory obeys

\[
 t\le \min\left\{A_{d+1},\left\lfloor{A_{d-1}-B\over q-1}\right\rfloor,
       \left\lfloor{E-B\over d}\right\rfloor,
       \left\lfloor{n_{c+2}-B\over q}\right\rfloor\right\}.   \tag{1.14}
\]

Furthermore

\[
 {q^2\over W}{A_{d-1}\over q-1}
       \longrightarrow {\pi\over2}e^{-\pi/4}.                  \tag{1.15}
\]

Thus the buffer-coordinate ceiling is `Theta(W/q^2)`, and the fraction of
owners occupied by all these modules is only `O(1/q)`.

#### Proof

Only (1.15) remains.  Put `ell=d-1`.  Uniformly for
`ell=O(sqrt(r))`, the central product gives

\[
 {\binom k{r-\ell}\over W}
       =\exp\left(-{\ell^2\over r}+O(\ell/r+\ell^3/r^2)\right).
                                                                    \tag{1.16}
\]

Here `d/sqrt(r)->sqrt(pi)/2`.  Formula (1.6), in the even and odd cases,
has prefactor respectively

\[
 {2\ell+1\over r+\ell+1},\qquad {2\ell\over r+\ell}.
\]

Therefore

\[
 {A_{d-1}\over W}\sim {2d\over r}e^{-\pi/4}.
\]

Multiplication by `q^2/(q-1)`, with `q/d->1` and
`d^2/r->pi/4`, proves (1.15).  \(\square\)

## 2. Completely labeled candidates and exact degrees

For the rest of the note use only length-`q` modules.  This is allowed in
a subinventory packing; no scalar owner divisibility row forces the use of
length `q+1`.

A bare block is an ordered disjoint pair `(C,V)` with

\[
                         |C|=c,\qquad |V|=q.
\]

It represents `B(C union V,V)`.  The number of bare blocks is

\[
 N=\binom kc\binom{k-c}q
   =\binom k{r+1}\binom{r+1}q.                                \tag{2.1}
\]

A complete labeling is `(b,sigma,w,h)`, where `b in C`, `sigma` is an
oriented cyclic order of `V` modulo rotation, `w in V`, and
`h in V-{w}`.  Its number is

\[
                         J=cq(q-1)(q-1)!.                       \tag{2.2}
\]

Let `\mathscr A` be the resulting set of `X=NJ` completely labeled
candidates.  Regard one candidate as a resource hyperedge containing its
`q` owners and every emitted named target.

### Lemma 2.1 (exact resource degrees)

Every owner belongs to exactly

\[
                         \delta_O={Xq\over W}                   \tag{2.3}
\]

labeled candidates.  A fixed target of rank `c` or `c+1` belongs to
exactly

\[
                         \delta_c={X\over K_c},\qquad
                         \delta_{c+1}={X\over K_{c+1}}          \tag{2.4}
\]

candidates.  For `2<=j<=q-2`, a fixed rank-`(c+j)` target belongs to
exactly

\[
                         \delta_{c+j}={Xq\over K_{c+j}}         \tag{2.5}
\]

candidates.

#### Proof

Every candidate contains `q` owners, one target at each of ranks `c,c+1`,
and `q` targets at each rank `c+j`.  The symmetric group on `[k]` is
transitive on every one of these resource species and preserves the
candidate family.  Double-counting candidate--resource incidences gives
(2.3)--(2.5).  \(\square\)

### Lemma 2.2 (exact conflict-degree bound)

The number of labeled candidates sharing at least one owner or target with
a fixed labeled candidate is at most `X Gamma`, with `Gamma` as in (0.4).

#### Proof

Union-bound over the resources of the fixed candidate.  Its `q` owners
contribute at most `q delta_O`; its two low targets contribute at most
`delta_c+delta_(c+1)`; and its `q` targets at each high rank contribute at
most `q delta_(c+j)`.  Divide the resulting expression by `X` and use
Lemma 2.1.  The count includes the candidate itself, which is harmless.
\(\square\)

## 3. Joint greedy selection, including a preused bank

### Theorem 3.1 (exact sparse joint facet-label packing)

If `(t-1)Gamma<1`, there are `t` completely labeled candidates whose owner
and named-target resource sets are pairwise disjoint.

#### Proof

Choose candidates greedily.  After `m` choices, Lemma 2.2 excludes at most
`m X Gamma` of the `X` candidates.  If `m<=t-1`, this number is strictly
less than `X`; hence a further candidate exists.  Continue to `m=t`.
Because the labeling is part of the candidate, this chooses blocks and
cyclic orders jointly rather than labeling an owner matching afterward.
\(\square\)

The theorem is an exact packing in the owner/named-target candidate
hypergraph.  A physical use must separately bind every selected candidate
to the required primitive and short-buffer occurrences and satisfy (0.1).

### Theorem 3.2 (one weighted forbidden-bank spread row)

Let `O_0` be a preused owner bank and let
`F_s subseteq binom([k],s)` be the forbidden target bank at every relevant
rank.  Put

\[
 \Psi={q|O_0|\over W}+{|F_c|\over K_c}+{|F_{c+1}|\over K_{c+1}}
       +\sum_{j=2}^{q-2}{q|F_{c+j}|\over K_{c+j}}.               \tag{3.1}
\]

If

\[
                         \Psi+(t-1)\Gamma<1,                    \tag{3.2}
\]

then there are `t` completely labeled, pairwise resource-disjoint facet
modules avoiding the whole preused bank.

#### Proof

By Lemma 2.1 and a union bound, the number of candidates meeting the
preused bank is at most `X Psi`: a fixed preused owner occurs in fraction
`q/W` of candidates, a fixed low target in fraction `1/K_s`, and a fixed
high target in fraction `q/K_s`.  After `m` choices, their resources
exclude at most a further `m X Gamma` candidates.  Condition (3.2) leaves
at least one candidate at every step.  \(\square\)

Condition (3.2) is only sufficient.  It is the exact first-moment weighted
load of the unavailable resource bank plus the already chosen candidates;
no claim of necessity is made.

### Corollary 3.3 (canonical quantitative range)

For all sufficiently large canonical `k`,

\[
                         \Gamma\le {17q^3\over W}.               \tag{3.3}
\]

Consequently Theorem 3.1 applies to every

\[
                         t\le \left\lfloor{W\over18q^3}\right\rfloor.
                                                                    \tag{3.4}
\]

More generally, if `Psi<=1-epsilon` for a fixed `epsilon>0`, it applies to
every `t<=epsilon W/(18q^3)`.

#### Proof

The binomial coefficients increase from rank `c` through rank `r-1`, so
`K_s>=K_c` for every target rank in the deck.  The uniform product
expansion (1.16), now with `ell=q-1=d+1`, gives

\[
                         {K_c\over W}\longrightarrow e^{-\pi/4}.
                                                                    \tag{3.5}
\]

In particular `K_c>=W/16` for all sufficiently large `k`.  There are
`q-3` high ranks, and hence

\[
 \Gamma
 \le {q^2\over W}+{16\over W}\{2+(q-3)q^2\}
 \le {17q^3\over W}                                             \tag{3.6}
\]

for `q>=3`.  Equations (3.4) and its banked variant now follow from
Theorems 3.1 and 3.2.  \(\square\)

### Proposition 3.4 (sharp first-order asymptotic for the greedy load)

With `a=sqrt(pi)/2`, equation (0.6) holds.

#### Proof

At rank `c+j` put

\[
                         \ell=q-1-j.
\]

As `j` runs from `2` to `q-2`, `ell` runs from `d-1` down to `1`.
The central product expansion is uniform on this range:

\[
 {K_{c+j}\over W}
   =\exp\left(-{\ell^2\over r}+O(r^{-1/2})\right).               \tag{3.7}
\]

The owner term in `Gamma` is `O(q^2/W)` and the two low terms are
`O(1/W)`, both negligible compared with `q^3/W`.  Therefore

\[
 {W\Gamma\over q^3}
 ={1+o(1)\over q}\sum_{\ell=1}^{d-1}e^{\ell^2/r}
 \longrightarrow {1\over a}\int_0^a e^{x^2}\,dx,               \tag{3.8}
\]

by a Riemann sum and `q/sqrt(r)->a`.  \(\square\)

The constant in (3.8) is approximately `1.33703`; this numerical value is
only descriptive and is not used in any proof.

## 4. Exact remaining gate

The corrected buffer-coordinate ceiling and the proved joint
owner/target-label range are

\[
             \Theta(W/q^2)\qquad\hbox{and}\qquad\Theta(W/q^3),
\]

respectively.  Thus the target problem left by this module route is a
factor-`q` strengthening of Theorem 3.1, not a construction of
`A_(d+1)=Theta(W/q)` buffered modules.

There is a second independent ledger gate: an aggregate semigroup
decomposition does not automatically reserve the `d` short loops needed
by every primitive.  The primitive multiplicity and its buffers must be
chosen jointly so that the second and third rows of (0.1) hold.  In
particular, if `E=0`, this specific one-primitive buffered construction
forces `t=0`; the unbuffered multi-primitive construction is a different
module and is not covered by this note.

Theorems 3.1--3.2 settle the exact primitive facet selection whenever its
chosen count and preused bank satisfy (3.2).  They do not imply the full
OFHT exact cover or any downstream physical assertion.

## 5. Nibble audit: an exact nested-target codegree

It is tempting to try to recover the missing factor `q` by applying a
Rödl--Pippenger nibble directly to the resource hypergraph.  The first
independence heuristic for that attempt is false because targets at
successive ranks lie on the same interval chains.

Strip off `b,w,h`, which do not affect owners or high targets, and let
`mathcal H` have one labelled edge for every `(C,V,sigma)`.  Its vertices
are the rank-`r` owners and the targets at ranks `c+2,...,r-1`.  Opposite
orientations of one cyclic order give parallel resource edges, so
`mathcal H` is naturally a labelled multihypergraph.  Quotienting this
uniform reversal multiplicity leaves every degree and codegree ratio below
unchanged.  Put

\[
                         X_0=N(q-1)!.
\]

Every edge of `mathcal H` has size

\[
                 R=q+q(q-3)=q(q-2)=\Theta(q^2).                 \tag{5.1}
\]

As in Lemma 2.1, an owner has degree `X_0 q/W` and a rank-`u` high
target has degree `X_0 q/K_u`.

### Proposition 5.1 (exact adjacent-rank chain codegree)

Assume `q>=5`, so that both ranks `r-2` and `r-1` belong to the high-target
vertex set of `mathcal H`.

Fix

\[
                  P\in\binom{[k]}{r-2},\qquad
                  Q=P\cup\{x\}\in\binom{[k]}{r-1}.
\]

Their codegree in `mathcal H` is

\[
 \deg_{\mathcal H}(P,Q)
 =4\binom{r-2}{q-3}\binom{k-r+1}{2}(q-3)!.                     \tag{5.2}
\]

More significantly, the two exact relative codegrees are

\[
 {\deg(P,Q)\over\deg(Q)}={2\over r-1},\qquad
 {\deg(P,Q)\over\deg(P)}={2\over k-r+2}.                       \tag{5.3}
\]

#### Proof

If one edge emits both targets, its core satisfies `C subseteq P` and has
size `c`.  Hence there are

\[
                         \binom{r-2}{c}=\binom{r-2}{q-3}
\]

choices for `C`.  The set `Q-C` contains `q-2` tags, so the remaining two
tags of `V` are an arbitrary pair from `[k]-Q`, giving
`binom(k-r+1,2)` choices.

Put `I=P-C` and `J=Q-C=I+{x}`.  The two targets are emitted precisely when
both `I` and `J` are cyclic intervals.  Equivalently, the two tags outside
`J` are adjacent and those two tags together with `x` form a cyclic
three-interval.  Contract that three-interval.  There are four internal
orders in which the two outside tags are adjacent, and `(q-3)!` oriented
cyclic orders of the contracted objects.  This proves (5.2).

For comparison, the degrees of the two individual targets are

\[
\begin{aligned}
 \deg(Q)&=2\binom{r-1}{q-2}\binom{k-r+1}{2}(q-2)!,\\
 \deg(P)&=6\binom{r-2}{q-3}\binom{k-r+2}{3}(q-3)!.
\end{aligned}                                                   \tag{5.4}
\]

Dividing (5.2) by the two rows of (5.4) gives (5.3).  \(\square\)

### Corollary 5.2 (the independent pair heuristic is false)

For the nested pair in Proposition 5.1,

\[
 {\deg(P,Q)\over X_0}
 ={2q\over(r-1)K_{r-1}}
 =\Theta\!\left({1\over qW}\right).                           \tag{5.5}
\]

In particular this is not `O(q^4/W^2)`.  Also

\[
 R\,{\deg(P,Q)\over\deg(Q)}
 ={2q(q-2)\over r-1}\longrightarrow {\pi\over2}.               \tag{5.6}
\]

#### Proof

The top-target degree is `X_0 q/K_(r-1)`, so (5.5) follows from
(5.3).  Canonically `K_(r-1)=Theta(W)`, `q^2/r->pi/4`, and (5.6) follows
from (5.1).  Since `W` is exponential whereas `q` is polynomial,
`1/(qW)` is asymptotically much larger than `q^4/W^2`.  \(\square\)

Thus the maximum relative pair codegree is at least
`Theta(1/q^2)`.  It does tend to zero, but the edge uniformity grows as
`Theta(q^2)`.  More precisely, the maximum vertex degree in `mathcal H` is

\[
                         D={X_0q\over K_{c+2}},                 \tag{5.7}
\]

because the binomial coefficients increase from rank `c+2` through
`r-1`.  Since `Delta_2>=deg(P,Q)`, (5.3) gives

\[
 {R\Delta_2\over D}
 \ge {2q(q-2)\over r-1}{K_{c+2}\over K_{r-1}}
 \longrightarrow {\pi\over2}e^{-\pi/4}>0.                    \tag{5.8}
\]

Here the central product gives
`K_(c+2)/K_(r-1)->e^(-pi/4)`, while
`2q(q-2)/(r-1)->pi/2`.

The classical Rödl--Pippenger matching theorem fixes the uniformity before
its codegree tolerance is chosen, so `Delta_2/D=o(1)` cannot simply be
diagonalized here.  Quantitative growing-uniformity criteria requiring
`R Delta_2/D=o(1)` fail by (5.8), even though
`Delta_2/D=Theta(1/q^2)->0`.  Adding the low targets or restoring the
independent choices `b,w,h` does not reduce this nested-chain obstruction.

This does not prove that a specialized nibble is impossible.  At the
desired scale `t=Theta(W/q^2)`, every high target would have load only
`Theta(1/q)`.  A plausible direct program would use `Theta(q)` bites, each
of per-vertex size `Theta(1/q^2)`, while tracking complete interval-chain
links rather than only pair codegrees.  No audited growing-uniformity
theorem currently turns (5.3) into that conclusion.  Equivalently, one may
first expose or contract the `q` vertical interval chains of every module
and then seek a chain-level matching/SCD theorem.  That chain-aware
augmentation is the exact remaining factor-`q` gate.
