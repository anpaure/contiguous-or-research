# Tight enumerations, Middle Levels cycles, and the exact double-rainbow fusion gate

Date: 2026-07-26

## 0. Verdict

Put

\[
 n=2m+1,\qquad
 \mathcal X=\binom{[n]}m,\quad
 \mathcal L=\binom{[n]}{m-1},\quad
 \mathcal U=\binom{[n]}{m+1},
\]

\[
 W=|\mathcal X|=|\mathcal U|,\qquad
 N=|\mathcal L|={m\over m+2}W,\qquad
 D=W-N={2W\over m+2}.
\tag{0.1}
\]

The two literature inputs in the question are correct and admit exact
converses.

1. A tight enumeration of levels \(m-1,m\) projects to a Hamilton cycle
   of \(J(n,m)\) which covers every lower intersection colour.  Conversely,
   every such Johnson Hamilton cycle expands to a tight enumeration.
2. A Hamilton cycle of the Middle Levels graph projects to a Hamilton
   cycle of \(J(n,m)\) which uses every upper union colour exactly once.
   Conversely, every such Johnson Hamilton cycle expands to a Middle
   Levels Hamilton cycle.
3. Their common strengthening is exactly one coloured-perfect-matching
   problem.  After one perfect matching \(M_0\) of the middle-level
   incidence graph is fixed, one must find a second perfect matching
   \(M_1\), disjoint from \(M_0\), which hits every one of \(N\) canonical
   lower-colour classes and whose monodromy is a single cycle.

There is an exact uniform fractional solution, so no degree or ordinary
Hall obstruction separates the two theorems.  The obstruction is integral
colour coverage together with monodromy.

Three proposed shortcuts require correction.

* A complement-invariant Middle Levels Hamilton cycle cannot have the
  proposed reflection symmetry: a reflection would force a cycle edge
  joining complementary sets.  Only the half-turn is possible, hence only
  in the Mersenne-parity dimensions.  Even there, complementation sends a
  lower \((m-1)\)-intersection to an \((m+2)\)-union on the opposite
  shore, not to the \((m+1)\)-union from the upper-perfect projection.
* A length-\(n\) Johnson cycle with distinct deleted coordinates need not
  be a wreath.  Constant residence time is an additional necessary and
  sufficient condition.
* An SCD consists of \(W\) variable-length partial chains, not \(W\)
  maximal flags.  It partitions each rank with \(N_q\) occurrences,
  whereas \(W\) cyclic flags have \(W\) occurrences at every rank.  The
  missing \(W-N_q\) occurrences are exactly the balancing problem, so SCD
  bundling is not the sole remaining issue.

No double-rainbow Hamilton cycle is constructed below.  The gain is an
exact statement of the common theorem and a complete audit of what the
two known cycles do and do not imply.

## 1. Tight enumeration is exactly lower-complete Hamiltonicity

Let

\[
 \mathcal T=(V_0,V_1,\ldots,V_{W+N-1})
\tag{1.1}
\]

be a cyclic listing of all vertices of levels \(m-1,m\).  A step is
called upper--upper, lower--lower, or cross according to the ranks of its
endpoints.  Write the respective numbers as \(b,s,c\).

Counting the two incidences of every listed vertex gives

\[
 2W=c+2b,\qquad 2N=c+2s,
\tag{1.2}
\]

and hence

\[
 b-s=W-N=D.
\tag{1.3}
\]

Every cross step flips at least one bit and every same-level step flips at
least two.  Therefore the total number of flips is at least

\[
 c+2b+2s=2W+2s.
\tag{1.4}
\]

The tight-enumeration value is

\[
 (W+N)+(W-N)=2W.
\tag{1.5}
\]

### Theorem 1.1 (forced step structure)

Every tight enumeration of levels \(m-1,m\) has

\[
 s=0,\qquad b=D,
\tag{1.6}
\]

all cross steps have Hamming length one, and all upper--upper steps have
Hamming length two.

#### Proof

Equality between (1.4) and (1.5) forces \(s=0\) and equality in every
individual step lower bound.  Equation (1.3) then gives \(b=D\).
\(\square\)

Delete the \((m-1)\)-sets from the cyclic listing.  By (1.6), two
consecutive retained \(m\)-sets are either a direct Hamming-distance-two
pair or have exactly one \((m-1)\)-set between them.  They are therefore
adjacent in \(J(n,m)\).  Every \(m\)-set is retained exactly once.

If the segment is

\[
 X,R,Y,qquad |R|=m-1,
\tag{1.7}
\]

then \(R\subset X,Y\), and distinctness gives

\[
 R=X\cap Y.
\tag{1.8}
\]

Every lower set occurs once in the listing, so every lower colour appears
on the projected cycle.

### Corollary 1.2 (GMM projection, with converse)

A tight enumeration of levels \(m-1,m\) projects to a Hamilton cycle
\(C\) of \(J(n,m)\) satisfying

\[
 \{X\cap Y:XY\in E(C)\}=\mathcal L.
\tag{1.9}
\]

Conversely, every Hamilton cycle satisfying (1.9) expands to a tight
enumeration: choose one occurrence of each \(R\in\mathcal L\), subdivide
that Johnson edge by \(R\), and leave the other \(D\) Johnson edges as
direct distance-two steps.

Thus the tight enumeration is strictly stronger than the earlier
lower-saturating cycle in owner count, but it contains no hidden condition
beyond lower-complete Hamiltonicity.

If \(\ell_C(R)\) denotes the lower load and \(h_C\) the number of missed
lower colours, then every Hamilton cycle obeys the exact ledger

\[
 h_C=\sum_{R\in\mathcal L}(\ell_C(R)-1)_+-D.
\tag{1.10}
\]

In particular, lower completeness means that the repeat excess is exactly
the unavoidable value \(D\).

## 2. Middle Levels Hamiltonicity is exactly upper-perfect Hamiltonicity

Let a Hamilton cycle of the Middle Levels graph be written

\[
 X_0,U_0,X_1,U_1,\ldots,X_{W-1},U_{W-1},X_0,
\tag{2.1}
\]

where \(X_i\in\mathcal X\) and \(U_i\in\mathcal U\).  Then

\[
 X_i\subset U_i\supset X_{i+1}.
\]

The two distinct \(m\)-facets of \(U_i\) have union \(U_i\), so

\[
 U_i=X_i\cup X_{i+1}.
\tag{2.2}
\]

Suppressing the upper shore yields a Hamilton cycle of \(J(n,m)\), and
the colours (2.2) exhaust \(\mathcal U\) exactly once.

Conversely, if a Johnson Hamilton cycle has pairwise distinct upper
colours, then there are \(W=|\mathcal U|\) of them, so they exhaust
\(\mathcal U\).  Inserting \(X_i\cup X_{i+1}\) on each edge gives a
Hamilton cycle of the Middle Levels graph.

### Theorem 2.1 (exact upper projection equivalence)

Middle Levels Hamilton cycles are in bijection with Johnson Hamilton
cycles satisfying

\[
 XY\longmapsto X\cup Y
\quad\hbox{is a bijection }E(C)\longrightarrow\mathcal U.
\tag{2.3}
\]

The lower colours \(X_i\cap X_{i+1}\) are not vertices of (2.1), and
Middle Levels Hamiltonicity imposes no completeness condition on them.

## 3. The exact fusion theorem

Every Johnson edge \(XY\) determines the rank-two Boolean interval

\[
 R=X\cap Y\in\mathcal L,qquad
 U=X\cup Y\in\mathcal U,qquad R\subset U.
\tag{3.1}
\]

Conversely, if \(U\setminus R=\{a,b\}\), the flag \((R,U)\) lifts to the
Johnson edge

\[
 \lambda(R,U)=\{R\cup\{a\},R\cup\{b\}\}.
\tag{3.2}
\]

Let \(\Gamma\) be the bipartite flag graph between \(\mathcal L\) and
\(\mathcal U\), with \(R\sim U\) when \(R\subset U\).

### Theorem 3.1 (phase-free flag normal form)

A flag family \(F\subseteq E(\Gamma)\) lifts to a spanning Johnson
two-factor which is upper-perfect and lower-complete if and only if

\[
 d_F(U)=1\quad(U\in\mathcal U),
\tag{3.3}
\]

\[
 d_F(R)\ge1\quad(R\in\mathcal L),
\tag{3.4}
\]

and every \(X\in\mathcal X\) has degree two in the lifted graph
\(\Lambda(F)\).

It lifts to one Hamilton cycle if and only if, in addition,
\(\Lambda(F)\) is connected.

#### Proof

The flag projections are exactly the lower and upper colours.  A Johnson
edge determines its flag uniquely, so different flags never give parallel
lifted edges.  Conditions (3.3)--(3.4) are precisely upper perfection and
lower completeness; degree two at every middle vertex is precisely a
spanning two-factor.  A finite two-regular graph is one cycle exactly when
it is connected. \(\square\)

This formulation has an exact fractional barycentre.  Give every flag
weight

\[
 x_{R,U}={1\over\binom{m+1}{2}}.
\tag{3.5}
\]

Then

\[
 \sum_{R\subset U}x_{R,U}=1,
\tag{3.6}
\]

\[
 \sum_{U\supset R}x_{R,U}
 ={\binom{m+2}{2}\over\binom{m+1}{2}}
 ={m+2\over m},
\tag{3.7}
\]

and

\[
 \sum_{(R,U):X\in\lambda(R,U)}x_{R,U}
 ={m(m+1)\over\binom{m+1}{2}}=2.
\tag{3.8}
\]

Thus every upper equation, every middle degree-two equation, and every
lower covering inequality is satisfied with the exact correct mean.  The
fusion problem has no fractional degree shortage.

## 4. Paired-perfect-matching normal form

Let \(B_m\) be the \((m+1)\)-regular bipartite incidence graph between
\(\mathcal U\) and \(\mathcal X\).  An upper-perfect Johnson two-factor
lifts to a spanning two-factor of \(B_m\), which is the union of two
edge-disjoint perfect matchings \(M_0,M_1\).  Write

\[
 f_i:\mathcal U\longrightarrow\mathcal X
\tag{4.1}
\]

for the facet bijection defined by \(M_i\).

Starting at \(U\), two alternating matching edges send it to

\[
 \sigma(U)=f_1^{-1}f_0(U).
\tag{4.2}
\]

Hence matching-union components are exactly the cycles of \(\sigma\).
At \(U\), the projected Johnson edge has lower colour

\[
 c(U)=f_0(U)\cap f_1(U).
\tag{4.3}
\]

### Theorem 4.1 (exact paired-matching fusion gate)

A two-sided depth-one Johnson Hamilton cycle exists if and only if there
are edge-disjoint perfect matchings \(M_0,M_1\) of \(B_m\) such that

\[
 \{c(U):U\in\mathcal U\}=\mathcal L
\tag{4.4}
\]

and \(f_1^{-1}f_0\) is one \(W\)-cycle.

For a two-factor, replace the one-cycle condition by no condition.

Fix \(M_0\) and delete it.  The residual graph is \(m\)-regular.  Colour
an edge \(UX\) by

\[
 c_0(UX)=f_0(U)\cap X.
\tag{4.5}
\]

For each \(R\in\mathcal L\), its colour class has exactly \(m+2\)
edges.  Indeed, for every \(Y=R\cup\{a\}\in\mathcal X\), take the unique
\(U=f_0^{-1}(Y)=Y\cup\{b\}\) and the opposite facet
\(X=R\cup\{b\}\).  These are all the edges of colour \(R\).

Consequently Theorem 4.1 is equivalently the following single finite
statement:

\[
 \boxed{
 \begin{array}{l}
 \text{find a perfect matching }M_1\subseteq B_m-M_0\text{ which}\
 \text{meets every canonical colour class and for which}\
 f_1^{-1}f_0\text{ is one cycle.}
 \end{array}}
\tag{4.6}
\]

The uniform fractional perfect matching \(x_e=1/m\) gives every colour
class weight \((m+2)/m\).  Thus (4.6) is an integral coloured-matching plus
monodromy theorem, not an ordinary Hall theorem.

The incidence graph \(B_m\) has no four-cycle: two distinct upper sets
intersect in at most one common \(m\)-facet.  Therefore the smallest
perfect-matching exchange is an alternating six-cycle.  If such a flip
cyclically permutes the three affected upper vertices by
\(\tau=(U_0U_1U_2)\), then its exact derivatives are

\[
 \sigma'=\tau\sigma,
\tag{4.7}
\]

\[
 \ell'-\ell
 =\sum_{i=0}^2
 \left(
 e_{f_0(U_i)\cap f_1(U_{i-1})}
 -e_{f_0(U_i)\cap f_1(U_i)}
 \right).
\tag{4.8}
\]

When \(\sigma\) is one cycle, \(\tau\sigma\) remains one cycle exactly
for one of the two cyclic orders of \(U_0,U_1,U_2\) along \(\sigma\); in
the other order it splits into three cycles.  Hence even the minimal
colour repair has a genuine chronology constraint.  The two literature
cycles do not automatically fuse by unstructured alternating exchanges.

There is also a small but exact reachability invariant.  A three-cycle is
even, so every sequence using only alternating six-cycle flips preserves
\(\operatorname{sgn}(\sigma)\), equivalently the parity of the number of
components of the matching union.  Starting from a Hamilton cycle, such
flips can only produce an odd number of components.  This does not obstruct
returning to one component, but it shows that six-cycle exchange alone
does not connect all perfect matchings; an even-half-length alternating
cycle is needed to change the component parity.

## 5. Complement symmetry: reflection is impossible

Complementation is a fixed-point-free involutory automorphism of the
Middle Levels graph.  If a Hamilton cycle \(H\) is complement-invariant,
its restriction to the abstract cycle \(C_{2W}\) is a fixed-point-free
dihedral involution.

It is therefore abstractly either

* the half-turn rotation, possible only when it swaps the bipartition,
  i.e. when \(W\) is odd; or
* a reflection through two opposite edge midpoints.

The reflection case cannot occur in the Middle Levels graph.  Such a
reflection fixes two cycle edges setwise and swaps the endpoints of each.
Since the involution is complementation, either fixed edge would be

\[
                         X--X^c.
\tag{5.1}
\]

But a Middle Levels edge is an incidence \(X\subset U\), whereas
\(X\cap X^c=\varnothing\); for \(m\ge1\), \(X\not\subset X^c\).
Vertex-axis reflections are also impossible because complementation has
no fixed vertex.  Therefore the half-turn is the only possible action.

By Lucas' theorem,

\[
 W=\binom{2m+1}m\text{ is odd}
 \quad\Longleftrightarrow\quad m\mathbin{\&}(m+1)=0
 \quad\Longleftrightarrow\quad m=2^t-1.
\tag{5.2}
\]

Consequently a complement-invariant Middle Levels Hamilton cycle can
exist only for

\[
                         m=2^t-1.
\tag{5.3}
\]

The proposed generic reflection-symmetric target is empty.

Write the Hamilton cycle as in (2.1) and put

\[
 R_i=X_i\cap X_{i+1}.
\tag{5.4}
\]

When the half-turn exists, write \(W=2s+1\).  After an index shift it has

\[
 X_i^c=U_{i+s},\qquad U_i^c=X_{i+s+1}.
\tag{5.5}
\]

Therefore

\[
 R_i^c=X_i^c\cup X_{i+1}^c
       =U_{i+s}\cup U_{i+s+1},
\tag{5.6}
\]

which has rank \(m+2\), not \(m+1\).

Thus complement symmetry identifies lower intersections of the
\(m\)-shore projection with consecutive-upper unions on the opposite
shore.  It does not identify them with the already perfect colours
\(U_i=X_i\cup X_{i+1}\).  A complement-invariant Middle Levels cycle is
lower-complete exactly when this additional rank-\((m+2)\) opposite-shore
colouring is complete; that is a new condition, not a symmetry
consequence.

## 6. Correct characterization of a wreath Johnson cycle

Let

\[
 X_0,X_1,\ldots,X_{n-1},X_0
\tag{6.1}
\]

be a directed cycle of \(J(n,m)\), and write

\[
 X_{i+1}=X_i-\{a_i\}+\{b_i\}.
\tag{6.2}
\]

For a cyclic order \(\pi=(\pi_0,\ldots,\pi_{n-1})\), the wreath cycle
\(X_i=I_\pi(i,m)\) has

\[
 a_i=\pi_i,\qquad b_i=\pi_{i+m}.
\tag{6.3}
\]

### Theorem 6.1 (exact wreath test)

The directed cycle (6.1) is a wreath cycle if and only if the \(a_i\) are
pairwise distinct and

\[
 b_i=a_{i+m}\qquad(i\in\mathbb Z_n).
\tag{6.4}
\]

Equivalently, the deleted coordinates are pairwise distinct and every
ground coordinate occurs in exactly \(m\) of the vertices \(X_i\).

#### Proof

Necessity is (6.3).  Conversely, set \(\pi_i=a_i\).  The candidate
intervals \(Y_i=\{a_i,\ldots,a_{i+m-1}\}\) obey

\[
 Y_{i+1}=Y_i-a_i+a_{i+m}.
\]

Under (6.4), this is the same recurrence as (6.2).  Each coordinate is
inserted once and deleted once; (6.4) places its insertion exactly \(m\)
steps before its deletion, so \(X_0=Y_0\), and induction gives
\(X_i=Y_i\) for all \(i\).

If the deletions are distinct, each coordinate has one cyclic residence
interval between its insertion and deletion.  Requiring exactly \(m\)
owner occurrences makes every residence interval have length \(m\),
which is precisely (6.4). \(\square\)

Distinct deletions alone are not sufficient.  In \(J(5,2)\),

\[
 12,\ 23,\ 34,\ 14,\ 15,\ 12
\tag{6.5}
\]

is a five-cycle whose deleted coordinates are respectively

\[
 1,2,3,4,5.
\]

It is not a wreath: coordinate \(1\) occurs in three listed sets and
coordinate \(5\) occurs in one, whereas every coordinate of a wreath
occurs in exactly \(m=2\) middle intervals.  Hence a Johnson Hamilton
cycle, or any collection of \(\Theta(m)\)-cycles, cannot be called a
wreath factor without the residence condition (6.4).

## 7. What an SCD solves, and what it does not

An SCD of \(Q_{2m+1}\) has exactly \(W\) symmetric chains, because every
chain contains one rank-\(m\) set and those sets form the largest level.
The chains partition the entire cube, so at rank \(m-q\) they contain
each of the

\[
 N_q=\binom{2m+1}{m-q}
\]

targets exactly once.

They are not \(W\) maximal flags.  A symmetric chain beginning above rank
\(m-q\) has no entry at that rank.  In contrast, \(W\) maximal chains, or
the \(W\) rotations coming from \(W/n\) cyclic orders, have exactly \(W\)
rank-\((m-q)\) occurrences.  The discrepancy is

\[
 W-N_q,
\tag{7.1}
\]

which is exactly the unavoidable repeat quota in the balanced-flag
problem.

Extending every SCD chain to a maximal chain inserts these missing
occurrences, but the extensions need not distribute them without
collisions and need not group into cyclic-order bundles.  Therefore:

\[
 \boxed{
 \begin{array}{c}
 \text{SCD set partition: solved;}\\
 \text{simultaneous balanced maximal flags: a separate rounding problem;}\\
 \text{cyclic bundling of those flags: an additional problem.}
 \end{array}}
\tag{7.2}
\]

The 1951 SCD theorem is an exact unbundled partition theorem, but it is not
the same as the simultaneous integral maximal-flag theorem and does not
reduce the residue to bundling alone.

## 8. Exact remaining statement

The strongest clean depth-one theorem suggested by the two literature
inputs is now unambiguous:

> Find edge-disjoint perfect matchings \(M_0,M_1\) of the middle-level
> incidence graph such that the intersection map
> \(U\mapsto f_0(U)\cap f_1(U)\) covers every \((m-1)\)-set and the
> monodromy \(f_1^{-1}f_0\) is one cycle.

For the constant-one programme, one may weaken “one cycle” to
\(o(W/H)\) cycles and allow \(o(W)\) missed lower colours, provided the
component collars are charged separately.  The fractional solution
(3.5)--(3.8) and the two separate Hamilton theorems show that all
marginals are feasible.  What remains is their common integral rounding
with chronological component control.
