# Mixed-core forward rectangles have a global upper-current obstruction

**Date:** 2026-08-07  
**Input:** `MATH_THEOREM_VARIABLE_SUPPORT_FACET_RINGS_AND_LITERAL_RECTANGLE_FUSION_20260807.md` and its audit  
**Method:** center--owner incidence counting  
**Status:** theorem.  This extends the fixed-\((r-3)\)-core obstruction to
arbitrary mixed cores.  In the triangular range, no nonempty owner-disjoint
family of fixed-size forward rectangle fusions can have zero immediate-upper
current.  In fact, every such family has upper defect linear in the number of
component reductions.

## 1. The global center model

Let

\[
                         n=2r-1
\]

and work in the complemented owner layer \(\binom{[n]}{r-1}\).  A forward
rectangle is a triple

\[
 \rho=(S;A,B),\qquad
 |S|=r-3,\quad |A|=p,\quad |B|=p+1,                 \tag{1.1}
\]

where \(S,A,B\) are pairwise disjoint.  Its owner inventory is

\[
 E(\rho)=\{S+a+b:a\in A,\ b\in B\}.                 \tag{1.2}
\]

The forward fusion replaces the \(p+1\) stars centered at

\[
                         S+b\quad(b\in B)
\]

by the \(p\) stars centered at

\[
                         S+a\quad(a\in A).
\]

It reduces the formal component count by one.  Under the injective
complementation map, an immediate-upper colour is indexed by a rank-
\((r-2)\) center \(G\): the colour is \([n]-G\).  Thus the signed
immediate-upper current of \(\rho\), written on centers, is

\[
 u(\rho)
   =(p+1)\sum_{a\in A}[S+a]
      -p\sum_{b\in B}[S+b].                          \tag{1.3}
\]

The formula is independent of the cyclic orders used to realize the facet
rings.

Call a family \(\mathcal F\) **owner-disjoint** if the sets \(E(\rho)\),
\(\rho\in\mathcal F\), are pairwise disjoint.  The cores \(S\) are not
required to agree.

## 2. Exact mixed-core no-go

### Theorem 2.1 (global upper-neutrality obstruction)

Let \(\mathcal F\) be an owner-disjoint family of forward
\(K_{p,p+1}\) rectangle fusions with arbitrary rank-\((r-3)\) cores.  If

\[
                         2p(p+1)>r+1,                \tag{2.1}
\]

then

\[
             \sum_{\rho\in\mathcal F}u(\rho)=0
             \quad\Longrightarrow\quad
             \mathcal F=\varnothing.                \tag{2.2}
\]

In particular, allowing the core to vary does not repair the fixed-core
one-copy circulation obstruction.

#### Proof

Fix a rank-\((r-2)\) center \(G\).  Let

\[
 \begin{aligned}
 a_G&=\#\{(\rho,a):G=S_\rho+a, a\in A_\rho\},\\
 b_G&=\#\{(\rho,b):G=S_\rho+b, b\in B_\rho\}.
 \end{aligned}                                       \tag{2.3}
\]

By (1.3), the current at \(G\) is

\[
                         u_G=(p+1)a_G-pb_G.           \tag{2.4}
\]

If the total current vanishes, then \(u_G=0\).  Since
\(\gcd(p,p+1)=1\), there is an integer \(t_G\ge0\) such that

\[
                         a_G=pt_G,
             \qquad     b_G=(p+1)t_G.                \tag{2.5}
\]

Each occurrence of \(G=S+a\) on an \(A\)-shore uses the \(p+1\) distinct
owners

\[
                         G+b\qquad(b\in B),           \tag{2.6}
\]

and each occurrence of \(G=S+b\) on a \(B\)-shore uses the \(p\) distinct
owners

\[
                         G+a\qquad(a\in A).           \tag{2.7}
\]

Owner-disjointness makes all owners counted in (2.6)--(2.7) distinct, even
when the underlying cores differ.  Hence the selected family uses exactly

\[
 (p+1)a_G+pb_G=2p(p+1)t_G                           \tag{2.8}
\]

different rank-\((r-1)\) owners containing \(G\).

But a fixed rank-\((r-2)\) center has only

\[
 n-(r-2)=r+1                                         \tag{2.9}
\]

rank-\((r-1)\) supersets.  Equations (2.1), (2.8), and (2.9) force
\(t_G=0\).  Thus \(a_G=b_G=0\) for every center \(G\).  Every rectangle
has \(p\) centers of the first kind and \(p+1\) of the second, so no
rectangle remains. \(\square\)

### Corollary 2.2 (optimal triangular range)

For the facet-ring construction, \(p\ge D+1=d+2\).  Since at the optimal
triangular scale

\[
                         d^2\sim {\pi\over4}r,
\]

we have, uniformly for every admissible \(p\),

\[
 2p(p+1)\ge2(d+2)(d+3)\sim {\pi\over2}r>r+1         \tag{2.10}
\]

for all sufficiently large \(r\).  Therefore no asymptotic fixed-size
forward rectangle bank can be simultaneously owner-disjoint and exactly
upper-neutral, regardless of how its rank-\((r-3)\) cores are mixed.

This conclusion already follows from the immediate-upper row; requiring
zero proper-target current can only make the system more restrictive.

## 3. Quantitative unavoidable defect

The same count gives more than nonexistence.

### Theorem 3.1 (linear upper-defect bound)

Assume (2.1), and let \(H=|\mathcal F|\).  For each center put

\[
 \ell_G=(p+1)a_G+pb_G,
 \qquad
 u_G=(p+1)a_G-pb_G.                                  \tag{3.1}
\]

Then

\[
 \boxed{
 \sum_G|u_G|
   \ \ge\
 \left\lceil{2p(p+1)H\over r+1}\right\rceil .}
                                                               \tag{3.2}
\]

Since \(\sum_Gu_G=0\), the positive and negative masses separately satisfy

\[
 \boxed{
 \sum_G(u_G)_+
   =\sum_G(-u_G)_+
   \ \ge\
 {p(p+1)H\over r+1}.}                                \tag{3.3}
\]

Thus \(H\) forward component reductions create \(\Omega(H)\) uncompensated
named upper **occurrence current** in the triangular regime.

#### Proof

Owner-disjointness gives

\[
                         \ell_G\le r+1               \tag{3.4}
\]

for every \(G\), by (2.9).  If \(\ell_G>0\) but \(u_G=0\), the argument
of Theorem 2.1 gives \(\ell_G=2p(p+1)t_G\ge2p(p+1)>r+1\), contradicting
(3.4).  Hence every touched center has nonzero integral current and
therefore contributes at least one to \(\sum_G|u_G|\).

One rectangle contributes

\[
 p(p+1)+(p+1)p=2p(p+1)                               \tag{3.5}
\]

to \(\sum_G\ell_G\).  Consequently the number of touched centers is at
least

\[
                         {2p(p+1)H\over r+1}.
\]

This proves (3.2).  Finally, every individual rectangle has total signed
current

\[
                         p(p+1)-(p+1)p=0,
\]

so \(\sum_Gu_G=0\); splitting the \(\ell_1\)-mass into its positive and
negative parts gives (3.3). \(\square\)

At \(p^2\sim(\pi/4)r\), (3.2) is asymptotically

\[
                         \sum_G|u_G|
                         \ge({\pi\over2}-o(1))H.       \tag{3.6}
\]

Hence a Catalan- or owner-scale number of forward fusions cannot leave only
bounded uncompensated upper occurrence current.  This is a current statement,
not by itself a lower bound on missing upper colours: a separately proved
duplicate/slack bank could absorb some negative current while preserving
setwise coverage.

## 4. Exact boundary of the obstruction

The proof uses three hypotheses, each essentially:

1. **fixed rectangle size \(p\):** it is the coprimality equation
   \((p+1)a_G=pb_G\) that forces \(2p+1\) shore memberships at a touched
   center;
2. **forward trades only:** inserting inverse trades supplies current with
   the opposite sign but forfeits monotone component reduction; and
3. **one-copy owner-disjointness:** allowing temporary owner multiplicity
   invalidates (3.4) and requires a later owner rerouting theorem.

Varying the core is not an escape, because the bottleneck is the global
rank-\((r-2)\) center \(G\), not its presentation \(G=S+x\).

There is, however, a genuine arithmetic escape if consecutive rectangle
sizes are mixed.  An \(A\)-incidence from a size-\(p\) rectangle has current
\(+(p+1)\), while a \(B\)-incidence from a size-\((p+1)\) rectangle has
current \(-(p+1)\).  Those two incidences cancel with owner load only
\(2(p+1)\), well below \(r+1\).  Thus the next viable rectangle-circulation
problem must use at least two star sizes (or another actuator type), and must
cancel the proper-target currents simultaneously.  The fixed-size mixed-core
problem is closed negatively by Theorem 2.1.

The escape is not merely a two-term observation.  At the abstract center-role
level it has an exact finite factor.

### Proposition 4.1 (two-size zero-current center ledger)

Assume that \(p\) is even.  Take

\[
                         H_p=p+2
\]

formal size-\(p\) rectangles and

\[
                         H_{p+1}=p
\]

formal size-\((p+1)\) rectangles.  Their complete center-role inventory can
be partitioned into zero-current groups of the following two types:

\[
 \begin{array}{c|c|c|c}
 \text{type}&\text{number of groups}&\text{positive roles}&
                      \text{negative roles}\\ \hline
 I&p(p+2)&1\text{ of weight }p+1&1\text{ of weight }p+1\\
 II&2(p+1)&p/2\text{ of weight }p+2&(p+2)/2\text{ of weight }p.
 \end{array}                                             \tag{4.1}
\]

The owner loads of the two group types are respectively

\[
                         2(p+1),\qquad p(p+2).        \tag{4.2}
\]

Consequently, if

\[
                         p(p+2)\le r+1,               \tag{4.3}
\]

this ledger satisfies every single-center owner-capacity inequality.

#### Proof

The size-\(p\) rectangles supply

\[
 \begin{array}{c|c}
 \text{role}&\text{count}\\ \hline
 A_p\ (+p+1)&p(p+2),\\
 B_p\ (-p)&(p+1)(p+2),
 \end{array}                                           \tag{4.4}
\]

whereas the size-\((p+1)\) rectangles supply

\[
 \begin{array}{c|c}
 A_{p+1}\ (+(p+2))&p(p+1),\\
 B_{p+1}\ (-(p+1))&p(p+2).
 \end{array}                                           \tag{4.5}
\]

Pair every \(A_p\) role with one \(B_{p+1}\) role.  This gives exactly
the \(p(p+2)\) type-I groups and exhausts both rows.

For each type-II group, take \(p/2\) roles from \(A_{p+1}\) and
\((p+2)/2\) roles from \(B_p\).  Its signed current is

\[
 {p\over2}(p+2)-{p+2\over2}p=0.                       \tag{4.6}
\]

The \(2(p+1)\) groups use respectively

\[
 2(p+1){p\over2}=p(p+1),
 \qquad
 2(p+1){p+2\over2}=(p+1)(p+2),                       \tag{4.7}
\]

so they exhaust the remaining two rows.  Summing absolute role weights gives
(4.2), and (4.3) is exactly the global number of owner supersets available
at one center. \(\square\)

At the optimal scale, one may choose an even admissible \(p=d+O(1)\), for
which

\[
                         p(p+2)=({\pi\over4}+o(1))r<r+1.  \tag{4.8}
\]

Thus mixing two consecutive sizes removes the **local** center-capacity
separator with constant-factor room.  Proposition 4.1 is not yet a Boolean
rectangle packing: one must realize the prescribed role identifications by
actual rank-\((r-2)\) centers, keep all owner blocks disjoint, and cancel the
proper-target currents at every width.  It identifies that joint realization,
rather than upper-current arithmetic, as the sharp next problem.

## 5. The two-size upper ledger has an explicit one-copy realization

The first two requirements left after Proposition 4.1 can in fact be met
exactly.  The construction is a pair of orthogonal coarse partitions.

### Theorem 5.1 (owner-disjoint two-size upper circulation)

Assume that \(p\) is even and

\[
 D+1\le p,
 \qquad
 p^2+4p\le r.                                        \tag{5.1}
\]

Then, over one fixed rank-\((r-3)\) core \(S\), there is an
owner-disjoint family consisting of

\[
                         p+2
\]

forward size-\(p\) rectangles and

\[
                         p
\]

forward size-\((p+1)\) rectangles such that:

1. their owner inventories partition one complete bipartite graph;
2. their total immediate-upper current is zero pointwise;
3. all rectangles have literal state-balanced facet-ring realizations; and
4. their formal component current is \(-(2p+2)\).

#### Construction and proof

Put

\[
                         U=[n]-S,
 \qquad                 |U|=r+2.
\]

Condition (5.1) allows disjoint coordinate banks

\[
 X,Y\subseteq U,
 \qquad
 |X|=p(p+2),
 \qquad
 |Y|=2(p+1),                                          \tag{5.2}
\]

because their total size is

\[
                         p^2+4p+2\le r+2.
\]

Split

\[
                         Y=Y_0\mathbin{\dot\cup}Y_1,
 \qquad                 |Y_0|=|Y_1|=p+1.            \tag{5.3}
\]

For \(\epsilon\in\{0,1\}\), choose an index set \(I_\epsilon\) of size

\[
                         h={p+2\over2}.               \tag{5.4}
\]

Partition \(X\) into rows

\[
 X=\mathbin{\dot\bigcup}_{\epsilon\in\{0,1\}}
      \mathbin{\dot\bigcup}_{i\in I_\epsilon}X_i,
 \qquad                 |X_i|=p.                    \tag{5.5}
\]

For each \(\epsilon\), repartition

\[
 X^\epsilon:=\mathbin{\dot\bigcup}_{i\in I_\epsilon}X_i
   =\mathbin{\dot\bigcup}_{k\in\mathbb Z_{p/2}}Z_{\epsilon,k},
 \qquad                 |Z_{\epsilon,k}|=p+2.        \tag{5.6}
\]

Such a repartition exists because both sides of (5.6) have size
\(p(p+2)/2\).  One completely explicit choice labels each row by
\(\mathbb Z_p\) and lets \(Z_{\epsilon,k}\) take coordinates \(2k,2k+1\)
from every row in \(I_\epsilon\).

Now take the following forward rectangles:

\[
 \rho_i=(S;X_i,Y_\epsilon)
 \quad(i\in I_\epsilon),                             \tag{5.7}
\]

of size \(p\), and

\[
 \sigma_{\epsilon,k}
    =(S;Y_{1-\epsilon},Z_{\epsilon,k})
 \quad(\epsilon\in\{0,1\},\ k\in\mathbb Z_{p/2}), \tag{5.8}
\]

of size \(p+1\).

The owner edges of (5.7) are

\[
                         X_i\times Y_\epsilon,
\]

and those of (5.8) are

\[
                         Z_{\epsilon,k}\times Y_{1-\epsilon}.
\]

Equations (5.5)--(5.6) show that these blocks partition

\[
                         X\times Y.                  \tag{5.9}
\]

Thus every owner \(S+x+y\), \(x\in X,y\in Y\), occurs exactly once.

For \(x\in X^\epsilon\), its unique row rectangle gives upper current
\(+(p+1)\), while its unique block rectangle gives current \(-(p+1)\).
These cancel.  For \(y\in Y_\epsilon\), the \(h=(p+2)/2\) row rectangles
with index in \(I_\epsilon\) give current

\[
                         -ph,
\]

while the \(p/2\) block rectangles with first index \(1-\epsilon\) give
current

\[
                         {p\over2}(p+2)=ph.
\]

These cancel as well.  No other center is used, proving exact pointwise
upper neutrality.

Condition (5.1) implies the fit and length conditions for both rectangle
sizes once \(p\ge2\): in particular \(2(p+1)\le r+1\) and \(p+2\le r+1\).
The variable-support facet-ring theorem therefore realizes every rectangle
literally and state-balances each shore.  Finally there are
\((p+2)+p=2p+2\) forward trades, each of component current \(-1\). \(\square\)

At \(p=d+O(1)\), condition (5.1) holds for all sufficiently large \(r\),
since \(p^2+4p=(\pi/4+o(1))r<r\).  Hence owner-disjoint exact upper
circulation is not the obstruction once two neighboring star sizes are
available.

## 6. Why the explicit upper circulation still cannot close the proper row

The use of one fixed core in Theorem 5.1 is fatal at the first proper
target width, independently of the choice of sizes.

### Theorem 6.1 (fixed-core width-\((D-1)\) obstruction)

Assume \(D\ge2\).  Let \(\mathcal F\) be any nonempty owner-disjoint family
of forward rectangle trades sharing one rank-\((r-3)\) core \(S\).  The
rectangle sizes and cyclic orders may vary.  Then its signed proper-target
current at width

\[
                         q=D-1                       \tag{6.1}
\]

is nonzero.  More precisely, the positive and negative target occurrence
multisets are disjoint, and therefore

\[
 \left\|u_{D-1}(\mathcal F)\right\|_1
       =2\sum_{\rho\in\mathcal F}p_\rho(p_\rho+1).   \tag{6.2}
\]

#### Proof

At width \(D-1\), the complementary interval length in Section 5 of the
facet-ring theorem is

\[
                         h=D-(D-1)+1=2.
\]

A positive target occurrence of a rectangle \((S;A,B)\) has the form

\[
                         T=S+a+b+b',                 \tag{6.3}
\]

where \(a\in A\) and \(b,b'\) are consecutive in the chosen cyclic order
on \(B\).  That occurrence contains the two selected owners

\[
                         S+a+b,\qquad S+a+b'.        \tag{6.4}
\]

A negative target occurrence has the form

\[
                         T'=S+b+a+a',                \tag{6.5}
\]

and contains the two selected owners

\[
                         S+b+a,\qquad S+b+a'.        \tag{6.6}
\]

Suppose a positive and a negative occurrence belonging to different
rectangles had the same named target.  After deleting the common core
\(S\), both are the same three-element set.  Each of (6.4) and (6.6) is a
two-edge subset of the triangle on those three elements.  Two two-edge
subsets of a triangle intersect.  Hence the two rectangles would share a
selected owner, contradicting owner-disjointness.

Within one rectangle, its positive and negative proper-target families are
disjoint by the complete turnover theorem; that argument applies at every
allowed rectangle size.  Thus no positive occurrence anywhere can equal a
negative occurrence anywhere.  A size-\(p_\rho\) rectangle contributes
\(p_\rho(p_\rho+1)\) occurrences of each sign, proving (6.2). \(\square\)

Theorem 5.1 therefore closes the owner and upper rows but deliberately fails
the proper rows.  The exact surviving design problem is now genuinely
mixed-core:

> **Mixed-core decorated two-size fusion lemma.**  Replace the fixed-core
> packing (5.7)--(5.8) by an owner-disjoint family over varying cores, retain
> its pointwise upper balance and positive component current, and pair every
> proper-target occurrence at every \(h=2,\ldots,D\) with an opposite
> occurrence using disjoint owner resources.

For \(h=2\), varying the core is exactly what removes the triangle argument:
one rank-\(r\) target has \(r\) rank-\((r-1)\) facets, so opposite
occurrences can use disjoint two-facet tickets.  The unresolved issue is to
make those ticket pairings coherent simultaneously across all widths and
with the upper-balanced rectangle incidence factor.
