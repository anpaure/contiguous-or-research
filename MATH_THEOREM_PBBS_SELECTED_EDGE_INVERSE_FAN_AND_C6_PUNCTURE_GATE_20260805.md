# The inverse fan of a selected PBBS edge and the sharp `q3` gate for a clean `C6` puncture

**Date:** 2026-08-05  
**Method:** q1-row intersection calculus; no computation or search  
**Status:** unconditional classification and local obstruction.  The targets
whose protected whole-fan paths use one punctured edge form a triangular
two-sided prefix family.  A common-pivot clean `C6` transports this family
through q1 and q2, but not through q3 without a second common-history flag.

## 1. The inverse fan of one edge

Let `F` be a directed middle-owner two-factor and let

\[
                    e_i=P_i\longrightarrow Q_i             \tag{1.1}
\]

be a selected edge.  Write the consecutive q1 intersection rows around
this occurrence as

\[
 \ldots,H_{i,-2},H_{i,-1},H_{i,0}=R_i,
             H_{i,1},H_{i,2},\ldots,                       \tag{1.2}
\]

where `H_(i,h)` is the intersection colour of the `h`-th edge relative to
`e_i`.

For `u,v>=0`, put

\[
 T_i(u,v)=\bigcap_{h=-u}^{v}H_{i,h}.                       \tag{1.3}
\]

The corresponding owner interval has

\[
                     q=u+v+1                               \tag{1.4}
\]

edges and `q+1` owners.

### Theorem 1.1 (exact puncture triangle)

Every canonical whole-fan lower witness which uses `e_i` has target
`T_i(u,v)` for a unique pair `u,v>=0`.  At fixed depth `q`, the only
possible affected targets are

\[
              T_i(0,q-1),T_i(1,q-2),\ldots,T_i(q-1,0).
 \tag{1.5}
\]

When the corridor is correct-rank, `|T_i(u,v)|=m-q`.  Its complementary
upper witness has target

\[
                         [n]\setminus T_i(u,v).             \tag{1.6}
\]

Consequently one punctured selected edge affects at most

\[
                         \sum_{q=1}^{m}q=\binom{m+1}{2}     \tag{1.7}
\]

members of the named lower bank, and the same number of paired upper
members.

#### Proof

The intersection of a directed owner interval equals the intersection of
the q1 rows on its internal edges.  If it contains `e_i`, there are unique
numbers `u,v` of preceding and succeeding internal edges, giving (1.3).
Conversely (1.3) is the intersection of that literal interval.  The
whole-fan theorem says every named corridor is correct-rank and its
complemented owner path has union (1.6).  There are `q` nonnegative
solutions to `u+v=q-1`, proving (1.7). `square`

The actual named bank may use only a subset of (1.5); (1.5) is the exact
local universe and does not assume that every interval is the chosen
witness of its value.

## 2. What a clean `C6` does to the triangle

Use the common-core clean-C6 notation

\[
 R_i=K+a_i,
 \quad P_i=K+a_i+a_{i+1},
 \quad Q_i=K+a_i+c.                                \tag{2.1}
\]

The old shore is `P_i Q_i`; the new shore is `P_i Q_(i+1)`.  Therefore
the new occurrence of the **same** q1 row `R_i` is

\[
                         P_{i-1}\longrightarrow Q_i.        \tag{2.2}
\]

The right exterior after `Q_i` is unchanged, whereas the left exterior is
the one formerly ending at `P_(i-1)`.

Define

\[
 L_i(u)=\bigcap_{h=-u}^{0}H_{i,h},
 \qquad
 R_i(v)=\bigcap_{h=0}^{v}H_{i,h}.                  \tag{2.3}
\]

Here the notation `R_i(v)` is a ray and should not be confused with the
central q1 set `R_i=H_(i,0)`.

### Theorem 2.1 (diagonal-to-shifted pairing law)

Before the switch, the puncture triangle is

\[
                         T_i(u,v)=L_i(u)\cap R_i(v).         \tag{2.4}
\]

After the switch, the literal path through the transported occurrence
(2.2) has target

\[
 \widetilde T_i(u,v)
   =R_i\cap
     \left(\bigcap_{h=1}^{u}H_{i-1,-h}\right)\cap
     \left(\bigcap_{h=1}^{v}H_{i,h}\right).        \tag{2.5}
\]

Thus one clean `C6` changes the old diagonal coupling

\[
                         (\text{left }i,\text{ right }i)
\]

to the shifted coupling

\[
                         (\text{left }i-1,\text{ right }i). \tag{2.6}
\]

#### Proof

Equation (2.4) is (1.3) split at its central row.  The clean switch changes
only the three central edges.  The new edge carrying row `R_i` has left
endpoint `P_(i-1)` and right endpoint `Q_i`; all exterior incidences at
those owners remain.  Intersecting its central row with the inherited left
and right q1 histories gives (2.5). `square`

This formula classifies every possible local repair.  The other two new
shores do not create additional pairings: cycling `i` in (2.5) lists all
three of them.

## 3. Why q1 and q2 close

Assume the clean `C6` is q2-neutral.  The common-deletion theorem gives one
`d in K` such that the companion row at `P_i` is

\[
                         H_{i,-1}=P_i-d.                    \tag{3.1}
\]

Hence

\[
 R_i\cap H_{i,-1}=(K-d)+a_i
   =R_i\cap H_{i-1,-1}.                            \tag{3.2}
\]

The right companion at `Q_i` is pointwise unchanged.

### Corollary 3.1 (the puncture triangle transports through q2)

For every `i`,

\[
 T_i(0,0)=\widetilde T_i(0,0),
 \quad
 T_i(1,0)=\widetilde T_i(1,0),
 \quad
 T_i(0,1)=\widetilde T_i(0,1).                    \tag{3.3}
\]

Thus every affected q1 or q2 lower path, and its complementary upper path,
has a literal replacement after the switch.

#### Proof

The q1 equality is the retained row label `R_i`.  The left q2 equality is
(3.2), and the right q2 equality is pointwise invariance of the exterior at
`Q_i`. `square`

## 4. The first uncontrolled flag is q3

The common-pivot theorem says nothing about `H_(i,-2)`.  The following
Johnson-legal exterior shows that no q3 identity follows from q2
neutrality.

Choose pairwise distinct `e_0,e_1,e_2 in K-{d}` and fresh labels `u_i,v_i`.
Put

\[
 X_i=(P_i-d)+u_i,
 \qquad
 Z_i=(X_i-e_i)+v_i.                                \tag{4.1}
\]

Then

\[
                         Z_i\longrightarrow X_i
                              \longrightarrow P_i
                              \longrightarrow Q_i           \tag{4.2}
\]

is a Johnson path, with q1 rows

\[
 X_i-e_i,
 \qquad P_i-d,
 \qquad R_i.                                      \tag{4.3}
\]

### Theorem 4.1 (sharp q3 obstruction)

The old three-edge paths (4.2) have targets

\[
                         S_i=(K-\{d,e_i\})+a_i.             \tag{4.4}
\]

After the clean switch, the three paths through the transported row
occurrences (2.2) have targets

\[
                 \widetilde S_i=(K-\{d,e_{i-1}\})+a_i.     \tag{4.5}
\]

If the `e_i` are distinct, the old and new target multisets differ.  Hence
a q2-neutral clean `C6` is not an all-depth finite fan trade.

#### Proof

All sets in (4.1) have rank `m`.  Consecutive pairs differ by one exchange,
so (4.2) is Johnson.  Intersecting (4.3) gives (4.4).  Formula (2.5) takes
the two left companion rows from port `i-1`, giving (4.5).

Every set in either family contains exactly one active label, namely
`a_i`.  Thus equality of the two multisets would force equality of the
members carrying each fixed `a_i`, and hence `e_i=e_(i-1)` for all `i`.
Distinct `e_i` contradict this. `square`

This is sharp: q2 is exact by Corollary 3.1, and q3 is the first row with an
unpriced exterior deletion flag.

## 5. Exact all-depth criterion

For each port and left depth, define the central-truncated history

\[
 A_i(u)=R_i\cap\bigcap_{h=1}^{u}H_{i,-h},          \tag{5.1}
\]

and define the pointwise fixed right history

\[
 B_i(v)=R_i\cap\bigcap_{h=1}^{v}H_{i,h}.           \tag{5.2}
\]

### Theorem 5.1 (fan-transport criterion)

One clean `C6` transports every affected named path in its puncture
triangle if and only if, for every affected triple `(i,u,v)`, its target

\[
                         A_i(u)\cap B_i(v)                  \tag{5.3}
\]

occurs among the shifted family

\[
                         A_{j-1\to j}(u')\cap B_j(v'),      \tag{5.4}
\]

where (5.4) denotes (2.5) and the candidate interval has the required
correct rank.  A simple sufficient condition is the all-depth common-left
history identity

\[
 R_i\cap\bigcap_{h=1}^{u}H_{i,-h}
   =R_i\cap\bigcap_{h=1}^{u}H_{i-1,-h}
 \quad\text{for every }i,u.                       \tag{5.5}
\]

The common-pivot q2 theorem is exactly the `u=1` case of (5.5).  It does
not imply any `u>=2` case.

#### Proof

Theorem 1.1 lists every old affected occurrence, and Theorem 2.1 lists
every new occurrence through a changed edge.  Comparing those two finite
families gives the necessary and sufficient condition.  Under (5.5), use
the same `(i,u,v)` in (2.5), proving sufficiency. `square`

## 6. Consequence for the protected-section programme

Deleting one selected edge does not create an unstructured global upper
problem.  It creates the explicit triangular bank (1.5).  But one
q2-neutral clean `C6` repairs only its q1/q2 boundary automatically.

For the canonical PBBS exterior, the remaining audit is now exact: compute
the literal left q1 history flags at the three C6 ports and test (5.3)--
(5.4) only for the named whole-fan paths using the punctured edge.  Without
an all-depth common-history theorem or alternate corridors, q3 is already
a genuine possible obstruction.

Thus protected-section Hamiltonization requires one of:

1. a PBBS-specific proof of (5.5) on the selected puncture bank;
2. alternate canonical corridors avoiding the punctured edge; or
3. a compound packet which carries the complete triangular fan bank.

No exact or additive upper bound is claimed here.

