# AM: exact laminar flag quotas and the successor-Hall obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

This note continues the integral port reduction in
`MATH_THEOREM_FINE_STRIP_INTEGRAL_PORT_SPARSIFICATION_AND_ANNULUS_MATCHING_GATE_20260726.md`.
It tests the most direct flag-aware strategy for proving
\((\mathrm{AM}_{m,H,h})\).

There is a complete positive theorem before physical cycle grouping.
Every symmetric-chain decomposition of \(B_{2m}\) gives:

* one middle owner \(X\) on each symmetric chain;
* an integral lifetime \(\lambda(X)\in\{0,1,\ldots,m\}\); and
* nested lower and upper flags

  \[
  L_q(X)\subset X\subset U_q(X)
  \qquad(1\le q\le\lambda(X)),                    \tag{0.1}
  \]

such that, for every \(q\),

\[
 \boxed{
 X\longmapsto L_q(X),\qquad X\longmapsto U_q(X)} \tag{0.2}
\]

are bijections from the owners with \(\lambda(X)\ge q\) onto the complete
rank-\((m-q)\) and rank-\((m+q)\) layers.  In particular,

\[
                         |\{X:\lambda(X)\ge q\}|=N_q.           \tag{0.3}
\]

Thus every all-depth target quota, every nesting condition, every
integrality condition, and the exact Gaussian lifetime census have a
simultaneous integral solution.  No fractional rounding remains at the
flag level.

However, an unsplittable physical strip imposes an additional condition
which is absent from the layered flow.  The first lower and upper members
of a prescribed owner flag determine the unique Johnson neighbor

\[
 \boxed{
 p(X)=L_1(X)\cup\bigl(U_1(X)\setminus X\bigr).}    \tag{0.4}
\]

If a cyclic strip realizes the prescribed flag at phase \(X\), its next
middle owner is necessarily \(p(X)\).  Consequently a family of
owner-disjoint \(C_{2h}\)-strips realizing all but \(e\) of the active
flags must satisfy the Hall inequalities

\[
 \boxed{
 |p(A)|\ge |A|-e
 \quad\text{for every }A\subseteq\{X:\lambda(X)\ge1\}.}        \tag{0.5}
\]

These cuts are exact at the first-flag level: their maximum deficiency is

\[
 |A_1|-|p(A_1)|=\sum_Y(|p^{-1}(Y)|-1)_+,           \tag{0.5a}
\]

the minimum number of first flags that must be deleted to remove all
successor collisions.

More is true on every strip all of whose phases retain their first flags:
there \(p\) is the physical successor permutation and the component is a
directed \(2h\)-cycle.  In general the inactive or discarded phases are
breaks in the forced successor system, so this conclusion has an explicit
\(2h\)-loss; see Corollary 3.2.  If the prescribed deletion and insertion
words are

\[
 \mathbf d(X)=(d_1(X),\ldots,d_H(X)),qquad
 \mathbf a(X)=(a_1(X),\ldots,a_H(X)),              \tag{0.6}
\]

then along every retained successor arc one must have the exact cocycle

\[
 \boxed{
 d_i(pX)=d_{i+1}(X),qquad
 a_i(pX)=a_{i+1}(X)}                               \tag{0.7}
\]

whenever both sides are prescribed.  These are literal coordinate
equalities, not target-count identities.  On a fully constrained strip the
two arms also obey the antipodal identity

\[
 \boxed{a_i(X)=d_i(p^hX)}.                         \tag{0.8}
\]

This last identity is essential: a physical strip has one cyclic
\(2h\)-letter word, not two independently chosen \(h\)-letter words.

Equations (0.5)--(0.8) are a precise obstruction to obtaining AM by first
rounding an arbitrary laminar/SCD flag flow and then grouping it.  An SCD
proves (0.2)--(0.3), but those equations say nothing about the indegrees,
component lengths, shift cocycle, or antipodal coupling of (0.4).

There is also a reserve-scale obstruction to an iterative theorem stated
only in terms of the number of unused owners.  The final inward extension
from depth two to depth one has owner reserve

\[
 W-N_2=\left(\frac4m+O(m^{-2})\right)W.            \tag{0.9}
\]

Yet the Johnson graph contains an independent owner set of size

\[
                         \Omega(W/m),              \tag{0.10}
\]

and hence a reserve of the correct order which contains no nontrivial
strip at all.  Therefore no iterative laminar matching lemma based only on
residual cardinalities, layer loads, or the original orbit degrees can be
valid.  The residual must retain a cycle-compatible successor structure.

The surviving positive theorem is consequently cycle-first:

> construct the lifetimes and two-sided flags simultaneously with a
> near-spanning physical \(C_{2h}\)-factor so that (0.2) holds up to
> aggregate \(o(W)\) target leave and the shift/antipodal equations
> (0.7)--(0.8) hold on all certified prefixes.

Such a construction would give the desired flag-aware matching of the port
hypergraph and, by the already proved literal compiler, coefficient one.
It is not proved here.  The note supplies a sharp Hall/cocycle obstruction,
not a negative theorem for AM itself.

## 1. Exact SCD lifetime flags

Write \(V=\binom{[2m]}m\), so \(|V|=W\), and fix a symmetric-chain
decomposition \(\mathscr D\) of \(B_{2m}\).  Every
chain has the form

\[
 C:quad C_r\subset C_{r+1}\subset\cdots\subset C_{2m-r},
 \qquad |C_j|=j,                                   \tag{1.1}
\]

for a unique minimum rank \(0\le r\le m\).  It contains a unique middle
set

\[
                         X(C)=C_m.                 \tag{1.2}
\]

Every middle set lies on one chain, so \(C\mapsto X(C)\) is a bijection
between the chains of \(\mathscr D\) and \(\binom{[2m]}m\).

For \(X=X(C)\), define

\[
                         \lambda(X)=m-r.           \tag{1.3}
\]

For \(1\le q\le\lambda(X)\), put

\[
                         L_q(X)=C_{m-q},qquad
                         U_q(X)=C_{m+q}.            \tag{1.4}
\]

These are nested in the required order.

### Theorem 1.1 (exact integral laminar quotas)

For every \(0\le q\le m\), the maps in (0.2) are bijections and (0.3)
holds.

#### Proof

Every set \(T\) of rank \(m-q\) belongs to a unique symmetric chain.  A
chain containing that rank has minimum rank at most \(m-q\), hence its
middle owner has lifetime at least \(q\).  Conversely, a chain of lifetime
at least \(q\) contains exactly one rank-\((m-q)\) member.  This proves the
lower bijection.  The upper statement is identical, or follows from chain
symmetry.  Counting either target layer gives (0.3). \(\square\)

The active owner sets

\[
                         A_q=\{X:\lambda(X)\ge q\}               \tag{1.5}
\]

are nested:

\[
                         A_m\subseteq\cdots\subseteq A_1.       \tag{1.6}
\]

Thus Theorem 1.1 is exactly the integral priority/lifetime solution which
one would want from a layered Hoffman flow.  It is stronger than a
rankwise matching: all depths use one common owner priority and one common
nested flag.

## 2. The unique first-step successor

For an active owner \(X\in A_1\), the two first flag members have the
forms

\[
 L_1(X)=X\setminus\{d_1(X)\},qquad
 U_1(X)=X\cup\{a_1(X)\},                           \tag{2.1}
\]

where \(d_1(X)\in X\) and \(a_1(X)\notin X\).  Define \(p(X)\) by
(0.4), equivalently

\[
                         p(X)=X-d_1(X)+a_1(X).      \tag{2.2}
\]

### Lemma 2.1 (successor uniqueness)

Let \(Y\) be Johnson-adjacent to \(X\).  Then

\[
 X\cap Y=L_1(X),qquad X\cup Y=U_1(X)              \tag{2.3}
\]

if and only if \(Y=p(X)\).

#### Proof

The first equality forces the deleted coordinate to be \(d_1(X)\); the
second forces the inserted coordinate to be \(a_1(X)\).  Hence (2.2) is
the only possible neighbor.  Direct substitution proves sufficiency.
\(\square\)

For a physical strip

\[
 X_t=K\cup I_z(t,h),                               \tag{2.4}
\]

the first lower and upper targets are

\[
 X_t\cap X_{t+1}=X_t\setminus\{z_t\},qquad
 X_t\cup X_{t+1}=X_t\cup\{z_{t+h}\}.              \tag{2.5}
\]

Therefore, if the strip realizes the prescribed flag at \(X_t\), Lemma
2.1 gives

\[
                         X_{t+1}=p(X_t).            \tag{2.6}
\]

This is the first place where the physical whole-cycle constraint enters.
The target quotas alone do not record (2.6).

## 3. The Hall and component conditions

Suppose a family of owner-disjoint physical strips, with owner union \(S\),
realizes the prescribed first flags on a set \(G\subseteq A_1\cap S\).  Let

\[
                         e=|A_1\setminus G|.        \tag{3.1}
\]

Every \(X\in G\) has the distinct physical successor \(p(X)\) in the
same selected strip.  Thus \(p|_G\) is injective and \(p(G)\) lies in the
selected owner union.

### Theorem 3.1 (successor Hall obstruction)

For every \(A\subseteq A_1\),

\[
                         |p(A)|\ge |A|-e.           \tag{3.2}
\]

Consequently the defect

\[
 \operatorname {def}(p)
 =\max_{A\subseteq A_1}(|A|-|p(A)|)                \tag{3.3}
\]

is a lower bound for the number of exceptional active owners in every
owner-disjoint strip realization.

#### Proof

At least \(|A|-e\) members of \(A\) lie in \(G\).  Their successors are
distinct by owner-disjointness and all belong to \(p(A)\).  This proves
(3.2); maximize over \(A\). \(\square\)

Because each owner has only one prescribed successor, the apparent family
of Hall cuts has an exact closed form.

### Corollary 3.1a (exact collision form of the Hall defect)

Let

\[
 d_p(Y)=|\{X\in A_1:p(X)=Y\}|.
\]

Then

\[
 \operatorname {def}(p)
 =|A_1|-|p(A_1)|
 =\sum_{Y\in V}(d_p(Y)-1)_+.                      \tag{3.4}
\]

This is also the minimum number of active first flags which must be
discarded merely to make the remaining prescribed successor arcs
owner-disjoint.

#### Proof

For any \(A\subseteq A_1\), each nonempty fibre of \(p|_A\) contributes at
most its full-fibre excess, so

\[
 |A|-|p(A)|
 =\sum_Y(|A\cap p^{-1}(Y)|-1)_+
 \le\sum_Y(d_p(Y)-1)_+.
\]

Equality holds at \(A=A_1\).  Keeping one owner from every nonempty fibre
gives an injective restriction and deletes exactly the displayed number;
no injective restriction can keep two members of one fibre. \(\square\)

The Hall condition is the part which survives even when inactive owners
are used as gaps between forced arcs.  The stronger component statement
must keep track of those gaps.  Let \(S\) be the union of the owners in the
selected strips and put

\[
 Z=(S\setminus A_1)\cup(A_1\cap S\setminus G).     \tag{3.5}
\]

Thus \(Z\) consists exactly of the selected phases at which the prescribed
first flag is not enforced.  Every selected strip disjoint from \(Z\) is a
directed \(p\)-cycle of exact length \(2h\).  A strip meeting \(Z\) contains
at most \(2h\) owners, and distinct selected strips are disjoint.

### Corollary 3.2 (component obstruction)

Let \(B\subseteq A_1\) be the union of the vertices lying on directed
\(p\)-cycles of exact length \(2h\).  Then every selected strip family as
above satisfies

\[
                         |S\setminus B|\le 2h|Z|.   \tag{3.6}
\]

In particular, if \(|V\setminus S|=o(W)\) and the number of discarded
active flags is \(e\), then

\[
 |V\setminus B|
 \le o(W)+2h\left(e+\frac{W}{m+1}\right).          \tag{3.7}
\]

Thus \(|V\setminus B|=o(W)\) follows from the sharp exception scale
\(e=o(W/h)\), since \(h=o(m)\).  It does **not** follow merely from
\(e=o(W)\); the factor \(2h\) is a real part of the ledger.

#### Proof

On a selected strip avoiding \(Z\), (2.6) holds at all \(2h\) phases, so
the strip is a directed \(p\)-cycle.  Every remaining strip contains at
least one member of \(Z\).  Charge that strip to one such member.  The
charges are injective because the strips are disjoint, and each charged
strip has \(2h\) owners.  This proves (3.6).  Also
\(|S\setminus A_1|\le |V\setminus A_1|=W-N_1=W/(m+1)\), which gives
(3.7). \(\square\)

This condition is not implied by the bijections (0.2).  Those bijections
make the lower and upper **target colors** exact; they impose no middle
indegree or component-length condition on the unique neighbor map (0.4).

## 4. Higher-prefix shift cocycle

Write the prescribed flags as ordered coordinate words:

\[
 L_q(X)=X\setminus\{d_1(X),\ldots,d_q(X)\},        \tag{4.1}
\]

\[
 U_q(X)=X\cup\{a_1(X),\ldots,a_q(X)\}.            \tag{4.2}
\]

For the physical strip (2.4), the native words at phase \(t\) are

\[
 d_i(X_t)=z_{t+i-1},qquad
 a_i(X_t)=z_{t+h+i-1}.                             \tag{4.3}
\]

They therefore satisfy not only the one-step shifts but also

\[
 a_i(X_t)=d_i(X_{t+h}).                            \tag{4.4}
\]

At the successor phase,

\[
 d_i(X_{t+1})=z_{t+i}=d_{i+1}(X_t),                \tag{4.5}
\]

\[
 a_i(X_{t+1})=z_{t+h+i}=a_{i+1}(X_t).              \tag{4.6}
\]

This proves the promised cocycle.

### Theorem 4.1 (literal prefix compatibility)

Suppose \(X,p(X)\) are consecutive retained phases of one physical strip.
For every \(i\ge1\) satisfying

\[
 i+1\le\lambda(X),\qquad i\le\lambda(pX),         \tag{4.7}
\]

one necessarily has

\[
 d_i(pX)=d_{i+1}(X),qquad
 a_i(pX)=a_{i+1}(X).                               \tag{4.8}
\]

If \(X\) and its antipodal phase are both prescribed at depth \(i\), then

\[
                         a_i(X)=d_i(\sigma^hX),     \tag{4.9}
\]

where \(\sigma\) is the physical successor.  If all intervening first
flags are retained, then \(\sigma^hX=p^hX\).

Conversely, suppose \(p\) is a directed \(2h\)-cycle, the first-step
equations (2.2) hold, the \(2h\) coordinates

\[
                         z_t=d_1(p^tX_0)            \tag{4.10}
\]

are distinct, and every prescribed entry obeys the shifts (4.8) and the
cycle-form antipodal identities

\[
 a_i(p^tX_0)=d_i(p^{t+h}X_0).                     \tag{4.11}
\]

Then this component is the physical strip

\[
                         p^tX_0=K\cup I_z(t,h),     \tag{4.12}
\]

and all its certified prefixes are the literal prefixes of that one
cyclic word.

#### Proof

Necessity is (4.3)--(4.6).  Conversely, (4.8) gives
\(d_i(p^tX_0)=z_{t+i-1}\), wherever the left side is prescribed, and
(4.11) gives \(a_i(p^tX_0)=z_{t+h+i-1}\).  By (2.2),

\[
 p^{t+1}X_0=p^tX_0-z_t+z_{t+h}.                   \tag{4.13}
\]

For \(0\le t<h\), the exchange at time \(t\) is legal, so \(z_t\) is
present and \(z_{t+h}\) is absent immediately before that exchange.
Using distinctness in (4.13), induction gives
\(\{z_0,\ldots,z_{h-1}\}\subset X_0\) and
\(\{z_h,\ldots,z_{2h-1}\}\cap X_0=\varnothing\).  Therefore, with
\(K=X_0\setminus\{z_0,\ldots,z_{h-1}\}\), a second induction in (4.13)
proves (4.12).  The displayed form then proves that every prescribed
prefix is literal. \(\square\)

The distinctness and antipodal clauses are important.  The shift equations
alone are only two separate chronology conditions: they neither identify
the upper arm with the second half of the deletion orbit nor prevent a
repeated coordinate before the isometric return time.

On a directed \(p\)-cycle, define the prefix-cocycle defect to be the
number of active owners at which at least one required shift (4.8) or
cycle-form antipodal identity (4.11) fails, together with the owners on
components violating the final distinctness condition.  Every
prescribed-flag realization must discard or alter all those defects.
Therefore an \(o(W)\)-owner-toll proof through preselected flags requires
both

\[
                         \operatorname {def}(p)=o(W)             \tag{4.14}
\]

and small prefix-cocycle defect on the fully constrained components.
Neither follows from layered Hoffman cuts or SCD ownership.  For a partial
realization, the universally valid obstruction is (3.2); converting the
component condition into an \(o(W)\) conclusion requires the sharper
exception ledger in (3.7).

### Theorem 4.2 (exact weighted SCD-to-strip completion)

Put

\[
                         \lambda_H(X)=\min\{\lambda(X),H\}.
\]

Let \(\mathcal P\) be a family of owner-disjoint physical
\(C_{2h}\)-strips, let \(G\) be its owner union, and suppose that at every
\(X\in G\) the native strip prefixes agree with the SCD lower and upper
flags through depth \(\lambda_H(X)\).  Set \(R=V\setminus G\).  Then:

1. the middle leave is exactly \(|R|\);
2. at signed depth \(q\), the lower and upper leaves are both exactly
   \(|R\cap A_q|\);
3. the total nonmiddle leave through depth \(H\) is exactly

   \[
   2\sum_{q=1}^H|R\cap A_q|
   =2\sum_{X\in R}\lambda_H(X);                   \tag{4.15}
   \]

4. no retained certified target is repeated; and
5. the strip blocks plus literal repair of every hole have total length

   \[
   \begin{aligned}
   &(2h+2H)\frac{|G|}{2h}+|R|
        +2\sum_{X\in R}\lambda_H(X)\\
   &\qquad =W+\frac{H}{h}|G|
        +2\sum_{X\in R}\lambda_H(X).             \tag{4.16}
   \end{aligned}
   \]

Consequently, under \(H/h=o(1)\), the two conditions

\[
 |R|=o(W),\qquad
 \sum_{X\in R}\lambda_H(X)=o(W)                  \tag{4.17}
\]

give an integral flag-aware annulus matching and a \(W+o(W)\) literal
word.

#### Proof

At depth \(q\), Theorem 1.1 assigns every lower target and every upper
target a unique active owner in \(A_q\).  Restricting those two bijections
to \(G\cap A_q\) creates no collision and misses precisely the targets
whose owners lie in \(R\cap A_q\).  This proves assertions 1, 2, and 4.
Double-counting pairs \((X,q)\) with \(X\in R\) and
\(1\le q\le\lambda_H(X)\) proves (4.15).  There are \(|G|/(2h)\) selected
strips, each with literal cost \(2h+2H\).  Adding one literal for every
middle and nonmiddle hole and using \(|G|+|R|=W\) gives (4.16).  Finally,
(4.17) and \(H/h=o(1)\) make every excess term \(o(W)\). \(\square\)

The weight in (4.17) is sharp for this exact SCD reduction.  An absorber
may leave many lifetime-zero owners for free, whereas discarding one owner
of lifetime \(H\) creates \(2H\) literal holes.  Thus an unweighted
\(o(W)\) owner leave is not by itself the right flag-aware conclusion.

## 5. Why rowwise TU ports lose the needed information

The integral port theorem marks, separately at every depth, exactly
\(D_1\) of the \(D_q\) incidences of each target.  This is a bipartite
\(b\)-matching and is totally unimodular.  However, a phase of one strip
contains the nested flag

\[
 L_1\supset L_2\supset\cdots\supset L_H,qquad
 U_1\subset U_2\subset\cdots\subset U_H.           \tag{5.1}
\]

Theorem 1.1 is exactly what the generic hypergraph nibble cannot see when
\(D^{1/K}=1+o(1)\): it resolves all \(2h\) laminar flag arms integrally,
with perfect target quotas, without paying an edge-width exponent.  What
remains is not rankwise concentration but the unsplittable ganging of
those \(2h\) flags into one physical component.

Separate rankwise port choices may retain \(L_q\) but reject \(L_{q+1}\),
then make the opposite choice on another phase.  The port degrees remain
perfect, but there is no lifetime \(\lambda\) whose prefix is being
selected.  Thus the rowwise TU theorem is an exact surplus
sparsification, not a flag-aware rounding theorem.

One may add variables \(y_{f,q}\) for a phase flag \(f\), with

\[
                         y_{f,q+1}\le y_{f,q}.       \tag{5.2}
\]

The uniform fractional point \(y_{f,q}=N_q/N_1\) satisfies all target
quotas.  If paths are allowed to switch identities whenever they meet the
same target, (5.2) becomes an ordinary layered network flow and is
integral.  A physical strip forbids that switch: the same phase identity
must continue through every layer and must remain ganged with the other
\(2h-1\) phases of its cycle.  The successor map and cocycle in Sections
3--4 are exactly the lost unsplittable-path constraints.

## 6. A reserve-scale obstruction to arbitrary iterative extension

An inward construction might try to choose a depth-\((q+1)\) family first
and extend it by new cycles at depth \(q\), using only the sizes of the
unused owner and target reservoirs.  Even at the last step this cannot be
a uniform theorem over arbitrary residual owner sets.

The exact layer ratios are

\[
 {N_1\over W}={m\over m+1},qquad
 {N_2\over W}={m(m-1)\over(m+1)(m+2)}.             \tag{6.1}
\]

Hence

\[
 W-N_2={4m+2\over(m+1)(m+2)}W
       =\left({4\over m}+O(m^{-2})\right)W,         \tag{6.2}
\]

and

\[
 N_1-N_2={3m\over(m+1)(m+2)}W
       =\left({3\over m}+O(m^{-2})\right)W.         \tag{6.3}
\]

Thus the final owner reserve and the owner mass which must be recruited are
both on the \(W/m\) scale.

### Lemma 6.1 (a cycle-free owner reservoir of the critical size)

The Johnson graph on \(\binom{[2m]}m\) has an independent set of size at
least

\[
                         {W\over4m}.                \tag{6.4}
\]

Consequently it has an \(\Omega(W/m)\)-sized owner set containing no
physical \(C_{2h}\)-strip.

#### Proof

Choose a prime \(p\) with

\[
                         2m<p<4m,                  \tag{6.5}
\]

using Bertrand's postulate, and label the \(2m\) ground coordinates by
distinct residues in \(\mathbb Z_p\).  Partition the middle sets according
to their coordinate sum modulo \(p\).  One class \(I\) has size at least
\(W/p>W/(4m)\).

If two middle sets are Johnson-adjacent, one is obtained from the other by
replacing distinct labels \(a\) and \(b\).  Their sums differ by
\(b-a\ne0\pmod p\), because the labels are distinct residues.  Hence no two
members of \(I\) are adjacent.  Every nontrivial strip contains Johnson
edges, so none lies inside \(I\). \(\square\)

Lemma 6.1 does not say that the actual residual generated by a successful
outer stage is independent.  It proves the precise scope failure: a Hall
or nibble lemma whose hypotheses retain only residual cardinality and the
unconditioned catalogue degrees cannot guarantee even one residual strip
at the required scale.  The outer stages must preserve successor/cycle
structure deliberately.

## 7. The exact cycle-first flag theorem still needed

The preceding results isolate a sufficient integral theorem with no
fractional or literal ambiguity.

### CFAM\(_{m,H,h}\) (cycle-first annulus matching)

Find an owner set \(G\subseteq\binom{[2m]}m\), a partition of \(G\) into
physical cyclic \(h\)-strips, and for every \(X\in G\) a lifetime
\(\lambda(X)\le H\), such that:

1. \(|\binom{[2m]}m\setminus G|=o(W)\);
2. for every \(1\le q\le H\), the native lower targets at phases with
   \(\lambda(X)\ge q\) cover all but a total \(o(W)\) targets over all
   lower depths;
3. the analogous aggregate upper leave is \(o(W)\);
4. each certified phase uses its literal initial deletion/insertion prefix,
   so (4.8)--(4.9) hold automatically; and
5. the total number of certified phase occurrences at depth \(q\) is at
   most \(N_q+o(W/H)\), preventing hidden duplicate mass.

Given CFAM, select the strip cycles partitioning \(G\).  A target certified
at any phase is physically present in that selected strip.  Append the
middle leave and all nonmiddle target holes literally.  Conditions 1--3
make those repairs \(o(W)\), while the exact strip blocks cost

\[
 (2h+2H){|G|\over2h}
 =W+O(HW/h)+o(W)=W+o(W).                           \tag{7.1}
\]

Thus CFAM implies AM's literal conclusion and coefficient one after the
proved exterior tail.

Theorem 1.1 proves all CFAM target and lifetime quotas before cycle
grouping.  Theorems 3.1 and 4.1 prove exactly what grouping adds:

\[
 \boxed{
 \text{near-\(C_{2h}\) successor factor}
 +\text{ shift/antipodal prefix cocycle}.}          \tag{7.2}
\]

No current theorem supplies (7.2).  In particular, an arbitrary SCD, a
rowwise TU port solution, or a layered flow with path switching cannot be
inserted into the physical strip compiler.

## 8. Final audited boundary

Proved:

1. exact integral nested lower/upper quotas at every depth, Theorem 1.1;
2. the unique first-step successor forced by a two-sided flag;
3. the exact collision formula for the Hall defect and the gap-sensitive
   component ledger (3.6)--(3.7);
4. the higher-prefix shift and antipodal cocycle (4.8)--(4.9);
5. the exact weighted completion ledger (4.15)--(4.17), with no rounding
   or duplicate-target loss;
6. the logical failure of independently rounded row ports to preserve
   flag identity; and
7. an \(\Omega(W/m)\) cycle-free residual owner set, matching the final
   inward-reserve scale.

Not proved:

1. CFAM or \((\mathrm{AM}_{m,H,h})\);
2. a laminar absorber which changes the successor/cocycle state on only
   \(o(W)\) owners; or
3. an asymptotic Hall obstruction for every possible cycle-first flag
   choice.

The result is therefore a precise Hall/cocycle obstruction to the proposed
SCD-first and arbitrary-residual iterative routes.  It is not a refutation
of the owner-recycling strip conjecture.
