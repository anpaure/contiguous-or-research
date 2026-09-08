# Clean packages extend conformally through a row-disjoint wreath-trade portal bank

**Date:** 2026-08-13  
**Status:** unconditional sufficient theorem and exact matching reduction.
It converts simultaneous clean-package extension from an arbitrary
protected-row completion problem into a portal matching inside one exact
wreath factor.  Middle-owner and immediate-lower compatibility are then
automatic.  Coverage and conflict bounds for the required PBBS casualty
targets in a concrete MSW trade bank remain separate.

## 1. Exact wreath factors and trades

Put

\[
                         n=2m+1.                    \tag{1.1}
\]

For an unoriented cyclic order `C` on `[n]`, let `B_m C` be the incidence
vector of its `n` cyclic rank-`m` windows.  An exact wreath factor is a
set `F` of cyclic orders satisfying

\[
                         \sum_{C\in F}B_mC=\mathbf1. \tag{1.2}
\]

A squarefree support-feasible trade is a pair of row packings `(P,N)`
with

\[
                         \sum_{C\in P}B_mC
                         =\sum_{C\in N}B_mC.       \tag{1.3}
\]

It is applicable to `F` when `N subset F`.

### Lemma 1.1 (conformal simultaneous substitution)

Let `(P_j,N_j)`, `j in J`, be trades applicable to one exact factor `F`.
If the negative row sets `N_j` are pairwise disjoint, then

\[
 F'=\left(F\setminus\bigcup_{j\in J}N_j\right)
       \mathbin{\dot\cup}\bigcup_{j\in J}P_j       \tag{1.4}
\]

is an exact wreath factor.  In particular:

1. the positive row sets are automatically pairwise middle-window
   disjoint;
2. every positive row is middle-window disjoint from every untouched row
   of `F`; and
3. no extra cross-trade packing check is needed at the middle rank.

#### Proof

The negative supports are rows of one exact factor, so the middle-window
supports

\[
                         B_mN_j:=\sum_{C\in N_j}B_mC \tag{1.5}
\]

are pairwise disjoint and are disjoint from the support of every untouched
row.  Equation `(1.3)` identifies `B_mP_j` with `B_mN_j`.  Hence the same
statements hold for the positive supports.  Summing `(1.3)` over `j` and
substituting in `(1.2)` proves `(1.4)`. \(\square\)

Because complementation sends the rank-`m` window deck of one row to its
rank-`m+1` window deck with a fixed start shift, Lemma 1.1 also gives
automatic owner disjointness for the full-aperture source convention.
The rank-`m` windows themselves are the immediate-lower resources.  Thus
both exact central rows survive the simultaneous trade without a separate
Hall calculation.

## 2. Every interval occurrence is a clean-package portal

Fix

\[
                         1\le q\le d,
 \qquad                  m\ge3d+2,                 \tag{2.1}
\]

and a target

\[
                         S\in{[n]\choose m+1-q}.    \tag{2.2}

\]

Let `sigma` be an **oriented and pointed occurrence** of a cyclic order in
which `S` is one consecutive `(m+1-q)`-window.  Rotate this pointed
occurrence so that

\[
                         \sigma=(D,C,I,S),          \tag{2.3}

\]

where the consecutive blocks have sizes

\[
 |D|=q,qquad |C|=m-q,qquad |I|=q,qquad
 |S|=m+1-q.                                       \tag{2.4}

\]

Put

\[
                         L_0=D\mathbin{\dot\cup}C,
 \qquad                  Z=[n]\setminus S
                         =D\mathbin{\dot\cup}C\mathbin{\dot\cup}I. \tag{2.5}

\]

Order `D=(d_1,...,d_q)` and `I=(i_1,...,i_q)` as they occur in
`sigma`, and set

\[
 L_j=L_0\setminus\{d_1,\ldots,d_j\}
             \cup\{i_1,\ldots,i_j\}
 \qquad(0\le j\le q).                              \tag{2.6}

\]

### Lemma 2.1 (interval-to-clean-package equivalence)

The row `sigma` contains, literally:

1. the clean upper path on the consecutive owners
   `L_(j-1) union L_j`, `1<=j<=q`;
2. the complementary clean intersection path whose `q+1` owners have
   common intersection exactly `S`; and
3. the four compatible length-`d+1` monotone halo arms around the two
   central paths.

The two collared owner arcs are disjoint under `(2.1)`.  Conversely, the
host row of the normal-form clean package has `S` as the interval block in
`(2.3)`.

#### Proof

With starts indexed immediately before the `D` block, the first `q+1`
rank-`m` windows of `(2.3)` are precisely `(2.6)`.
Writing

\[
                         A_t=I_\sigma(t-1,m+1),     \tag{2.7}

\]

the clean upper owners are `A_1,...,A_q`.  Cyclic complementation gives

\[
 \overline{L_j}=A_{m+j+1},
 \qquad
 \overline{L_{j-1}\cup L_j}=I_\sigma(m+j,m),      \tag{2.8}

\]

so the antipodal consecutive owners `A_(m+1),...,A_(m+q+1)` have common
intersection `S`.  Extending each central arc by the adjacent `d+1`
row transitions gives the four monotone arms.  Their owner-index blocks
are

\[
 [-d,q+d+1],
 \qquad[m-d,m+q+d+2]\pmod n.                      \tag{2.9}

\]

The cyclic gap in either direction is `m-q-2d-2>=0`; equality makes the
far-port owners consecutive but does not identify them.  This is exactly
the clean-row calculation.  Reading the four blocks back from any
normal-form package proves the converse. \(\square\)

Thus a **middle portal** for the occurrence `(S,q)` is a positive trade
row together with an oriented start at which `S` is the cyclic
`(m+1-q)`-window.  No separate choice of `D,C,I` is needed once that
oriented pointed occurrence is fixed.  An unoriented row may supply two
orientations or several starts for the same set `S`; these are distinct
portals when their protected arcs differ.

## 3. A row-disjoint trade bank reduces simultaneous extension to Hall

Let `F` be an exact factor and let `mathcal B` be a family of applicable
trades

\[
                         b=(P_b,N_b)                \tag{3.1}

\]

whose negative row sets are pairwise disjoint.  The trades may have any
fixed degree; the main application is the degree-two universal wreath
trade.

Let `mathcal T` be a multiset of requested clean-package occurrences
`t=(S_t,q_t)`.  Define a bipartite portal graph

\[
                         G_{F,\mathcal B}(\mathcal T) \tag{3.2}

\]

with left shore `mathcal T` and right shore `mathcal B`, where `t~b` when
some row of `P_b` contains `S_t` as a cyclic
`(m+1-q_t)`-window.

### Theorem 3.1 (protected middle-row extension criterion)

If

\[
 |N_G(J)|\ge|J|
 \qquad(J\subseteq\mathcal T),                    \tag{3.3}

\]

then one may select one distinct trade for every requested occurrence and
apply all selected trades simultaneously.  The resulting exact factor
contains one clean collared package for every `t in mathcal T`, and all
their owner and immediate-lower resources are mutually disjoint.  If one
positive row contains portals for several tasks, selecting its trade once
installs only the one task assigned to that trade in this theorem; the
other interval occurrences are not counted as separately protected
packages.

For the fixed trade bank `mathcal B`, condition `(3.3)` is also necessary
for an installation which assigns at most one requested package to each
trade.

#### Proof

Hall gives a matching `t mapsto b_t`.  Use the witnessing positive row
and interval occurrence on `b_t`, and apply Lemma 2.1.  The selected
negative supports are disjoint because all of `mathcal B` is row-disjoint.
Lemma 1.1 applies the trades simultaneously and proves exactness and
central-resource disjointness.  Necessity is ordinary Hall. \(\square\)

This theorem is already stronger than arbitrary protected-row extension:
it never asks the residual exact-cover polytope to complete prescribed
rows.  Every installed row enters through a conformal kernel move from a
known exact factor.

## 4. Full protected halos: the remaining conflict layer

Different factor rows can share nonmiddle interval values.  In particular,
their rank-`m+2` upper windows, source-history tickets, or externally named
cap data need not be distinct merely because their middle windows are.

Refine a portal to a triple

\[
                         p=(t,b,C,i),               \tag{4.1}

\]

where `C in P_b` is the chosen positive row and `i` is the start of the
target interval.  Let `H(p)` be its complete extra protected halo, after
removing the owner and immediate-lower resources already controlled by
Lemma 1.1.  Two portals conflict when they use the same trade or their
extra halos meet.

### Lemma 4.1 (elementary portal-conflict transversal)

Suppose `M=|mathcal T|`, every task `t` has a portal list `mathcal P_t`,
and for every distinct `s,t` and every `p in mathcal P_s`, at most
`Delta` members of `mathcal P_t` conflict with `p`.  If

\[
                         |\mathcal P_t|>(M-1)\Delta
                         \qquad(t\in\mathcal T),    \tag{4.2}

\]

then there are pairwise nonconflicting portals, one for each task.

#### Proof

Choose the tasks in any order.  After fewer than `M` choices, at most
`(M-1)Delta` portals in the next list are forbidden, so one remains.
\(\square\)

Under `(4.2)`, applying the selected trades gives a simultaneous extension
with every resource listed in `H(p)` protected.  More refined lopsided or
rainbow-matching estimates may replace `(4.2)`; the point is that middle
exactness has disappeared from the conflict calculation.

## 5. Universal degree-two specialization

For distinct labels `alpha,beta,gamma,delta` and ordered complementary
lists `E,O` of lengths `m-1,m-2`, put

\[
\begin{aligned}
C  &=(\delta,\gamma,E,\beta,\alpha,O),\\
D  &=(\beta,\delta,E,\alpha,\gamma,O),\\
C' &=(\delta,\beta,E,\gamma,\alpha,O),\\
D' &=(\gamma,\delta,E,\alpha,\beta,O).
\end{aligned}                                        \tag{5.1}
\]

The universal trade identity is

\[
                         B_m(C+D)=B_m(C'+D').       \tag{5.2}

\]

Both signs are row packings.  Thus any row-disjoint bank of applicable
instances of `(5.1)` is a valid `mathcal B` for Theorem 3.1.

The canonical MSW factor has an explicit row-disjoint inverse-triple
packet obtained by the first aligned `1100 <-> 1010` block rule.  The
negative sides of those packet trades are rows of that factor, so they are
applicable simultaneously.  Hence Theorem 3.1 gives an immediate, finite
portal-Hall test for that concrete resident factor.

There is also a much larger overlapping inverse-triple atlas of size

\[
                         N_m=(2m-1)\operatorname{Cat}_{m-2}. \tag{5.3}

\]

It cannot be applied conformally all at once because its negative row
pairs overlap.  A tailored use of the full atlas asks for a rainbow
matching of target portals whose selected negative row pairs are disjoint.
Once that matching is found, Lemma 1.1 again makes every middle-rank
cross-conflict vanish automatically.

## 6. Scale diagnostic

Let `s=m+1-q`.  A row-disjoint degree-two bank of size `B_0` has exactly
`2nB_0` positive row/start occurrences of `s`-windows, counted with
multiplicity.  Therefore its average portal-occurrence degree over all
rank-`s` targets is

\[
                         \overline d_s
 =\frac{2nB_0}{\binom ns}.                         \tag{6.1}

\]

For a bank occupying at most all rows of one factor,
`2B_0<=Cat_m=binom(n,m)/n`, so

\[
                         \overline d_s
 \le\frac{\binom nm}{\binom ns}.                  \tag{6.2}

\]

At the deadline scale `q=Theta(sqrt m)`, the ratio in `(6.2)` is only
`exp(Theta(q^2/m))=Theta(1)`.  Consequently a single fixed row-disjoint
packet cannot obtain a uniform large portal degree from counting alone.
Its Hall property must use special structure of the PBBS casualty targets.

By contrast, `(5.3)` satisfies

\[
 \frac{2nN_m}{\binom ns}
 =\frac{m(m+1)}{2(2m-3)}
   \frac{\binom nm}{\binom ns}                    \tag{6.3}

\]

and the prefactor is `n/8+O(1)`.  It therefore has average
portal-occurrence degree `Theta(n)` at the same
scale.  This identifies the overlapping inverse-triple atlas, rather than
one aligned disjoint packet, as the first plausible trade supply.  The
new exact question is whether its portals to the `O(d^3)` named casualty
multiset contain a negative-row-disjoint rainbow matching with acceptable
extra-halo conflicts.

Equation `(6.3)` is only an average.  It does not prove that every casualty
has a portal or that the negative-row conflict graph is sparse.

## 7. Exact frontier

The arbitrary protected-row inference is false, but the following
replacement is sufficient:

\[
 \boxed{
 \begin{gathered}
 \text{find clean interval portals in positive rows of applicable trades},\\
 \text{select a negative-row-disjoint rainbow family},\\
 \text{then handle only the residual nonmiddle halo conflicts.}
 \end{gathered}}                                  \tag{7.1}
\]

The first two lines imply exact integral owner/immediate-lower extension
by Lemma 1.1, without a Smith, normality, or residual exact-cover theorem.
For the present PBBS bank, the decisive next calculation is the portal
degree/codegree profile of the full inverse-triple atlas on the literal
crossing-casualty targets.
