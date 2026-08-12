# Period-three filters inside a clean cyclic scaffold

Date: 2026-07-31  
Status: exact scoped audit and composition theorem; superseded as the primary
existential palette route by global-matching-first; exact \(m=8\) sector
ledger and topology counterexample retained

## 1. Scope and conclusion

**Supersession notice.**  Sections 3--7 analyze the stronger subclass in
which period-three filters are prescribed before the bulk matching.  The
theorem
`MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md`
removes that residual-Hall gate from the existential route: choose one global
quotient perfect matching first and read its exceptional filters afterward.
Accordingly, the prescribed-phase and sector-diagonal statements below are
only sufficient subclasses and diagnostics.  They are not WLOG, and their
residual Hall problem is not the current existence gate.  The topology,
socket, voltage, and small counterexample statements remain valid in their
stated scopes.

Put

\[
 q=2m-1,\qquad K=\operatorname {Cat}_m,\qquad
 N=mK,\qquad M=(m+1)K.
\]

The arithmetic, freeness, and voltage statements in
`MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`
are correct.  If

\[
 s=3^{v_3(q)},\qquad h=q/s,\qquad H=\langle s\rangle\cong\mathbb Z_h,
\]

then (H) is the largest translation subgroup acting freely on all three
ranks (m-1,m,m+1), and (h\mid K).  A quotient cycle lifts to one
physical cycle exactly when its total voltage is a unit of
\(\mathbb Z_h\).

The complement-paired filters in
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_RECURSION_20260731.md` are also
correct.  When (v_3(q)=1), they give a collision-free prescribed partial
two-sided-rainbow matching of the sharp size (2\operatorname {Cat}_a),
where

\[
 q=6a+3=3(2a+1),\qquad m=3a+2.
\]

This note proves the exact way in which those filters compose with a cyclic
carrier.  There are two versions.

1. In an unrestricted clean-(H) quotient, extension is an exact common
   independent-set problem for four partition matroids and one graphic
   matroid.
2. Once a spanning Hamilton path or unit-voltage Hamilton-cycle scaffold is
   fixed, all topology disappears: extension of the prescribed filters is
   **exactly** a residual bipartite Hall problem on the literal edge
   occurrences of that scaffold.  The matching may be completely
   asymmetric even when the scaffold is (H)-invariant.

The second version is the one compatible with the authenticated K16
anatomy: symmetry organizes the four strict spirals, but neither the
integral palette selection nor the compiler is required to be equivariant.

There is no unconditional extension theorem from collision-freeness alone.
At (m=2), the exact complement-paired filter has a unique palette
completion, and that completion is a four-cycle plus two isolated middle
vertices.  Thus it is not a spanning path forest.  A one-phase twist of the
upper filter repairs this base case.  The phase is therefore a genuine
topological variable, not cosmetic notation.

No all-(m) directed repair or contiguous-OR word is claimed.

## 2. Audit of the clean three-primary quotient

Let (G=\mathbb Z_q) act by translation on the finite coordinates and fix
\(\infty\).  The isomorphism (\mathbb Z_h\to H) is

\[
 t\longmapsto st\pmod q.                                \tag{2.1}
\]

Thus every voltage below is measured in units of the physical translation
by (s).

The identity

\[
 (m^2-1)\operatorname {Cat}_m
   =2q\binom{q-1}{m-2}                                  \tag{2.2}
\]

and

\[
 \gcd(q,m^2-1)=\gcd(q,3)                               \tag{2.3}
\]

give (h\mid K), because (3\nmid h).  If a subgroup of order (d)
stabilizes a subset of (\Omega=\mathbb Z_q\sqcup\{\infty\}), then
(d) divides the size of its finite part.  The possible finite-part sizes
at ranks (m-1,m,m+1) are

\[
 m-2,m-1,m,m+1,
\]

and

\[
 \gcd(q,m)=\gcd(q,m-1)=1,\qquad
 \gcd(q,m-2)=\gcd(q,m+1)=\gcd(q,3).                    \tag{2.4}
\]

This proves freeness under (H).  It also proves maximality: any
translation subgroup whose order is divisible by three contains the unique
order-three subgroup, which fixes the outer-rank states described below.

When (3\mid q), every shortened outer-rank stabilizer has order exactly
three, not a larger order.  Every Johnson edge orbit is free: an odd-order
translation cannot interchange the two endpoints, and a translation fixing
one middle endpoint is the identity.  Hence a free edge orbit lying over a
short lower or upper colour hits each member of that colour orbit exactly
three times.  This is the exact obstruction to full-(G) rainbow
equivariance.

For a quotient path forest, closure-edge orbits must use every quotient
path endpoint once and make one spanning quotient cycle.  If its total gain
is (v\in\mathbb Z_h), its lift has

\[
 \gcd(v,h)                                               \tag{2.5}
\]

cycles.  Condition (2.5), with voltages interpreted through (2.1), is the
complete composite-order correction.

## 3. The prescribed period-three filters and their phases

Assume for the rest of Sections 3--7 that (v_3(q)=1).  Put

\[
 h=2a+1,\qquad G\cong\mathbb Z_h\times\mathbb Z_3,
\]

and write a finite coordinate as ((z,r)), with (z\in\mathbb Z_h) and
(r\in\mathbb Z_3).  Let

\[
 t=\operatorname {Cat}_a.
\]

For one representative of each translation necklace
(A\in\binom{\mathbb Z_h}{a}), put (B=\mathbb Z_h\setminus A), choose
distinct (b,c\in B), and for a phase (r\in\mathbb Z_3) put

\[
\begin{aligned}
 L_A&=\{\infty\}\cup(A\times\mathbb Z_3),\\
 U_B&=B\times\mathbb Z_3,\\
 x_r&=(b,r),\qquad y_r=(c,r),\\
 e^-_{A,r}&=\{L_A+x_r,L_A+y_r\},\\
 e^+_{A,r}&=\{U_B-x_r,U_B-y_r\}.
\end{aligned}                                           \tag{3.1}
\]

Take the complete \(H\)-orbits of these edges.  For any phase assignment
(\phi) to the (t) necklaces, the bank

\[
 P_\phi=\{e^-_{A,\phi(A)},e^+_{A,\phi(A)}:A\}           \tag{3.2}
\]

has the following exact properties.

* It consists of (2t) quotient edge orbits.
* It covers every shortened lower and every shortened upper quotient colour
  exactly once.
* It also uses (t) distinct regular lower and (t) distinct regular
  upper quotient colours.
* Its (4t) middle quotient endpoints are pairwise distinct.
* The two edges belonging to (A) are setwise complements.

The collision proof survives arbitrary independent choices of
(\phi(A)).  From an endpoint containing (\infty), recover (A) as the
set of columns present in all three phases and recover the unique added
point.  The endpoints avoiding (\infty) are their complements.  Thus the
necklace, translation, selected point, and phase are all recoverable.

There is a useful, slightly broader phase freedom.  One may choose
independent phases

\[
 \phi^-(A),\phi^+(A)\in\mathbb Z_3                     \tag{3.3}
\]

for the lower and upper filter.  All palette and collision conclusions
remain true.  Exact complementation is replaced by shifted complementation:

\[
 e^+_{A,\phi^+(A)}
 =\tau^{\phi^+(A)-\phi^-(A)}
   \bigl(\overline{e^-_{A,\phi^-(A)}}\bigr),            \tag{3.4}
\]

where (\tau) is the order-three CRT factor.  This twist has zero
(H)-voltage.  The diagonal choice in (3.2) is therefore sufficient for
the sharp palette floor, but it is not a valid WLOG restriction for global
topology.

## 4. Exact three-sector count ledger

The rank-(m) middle states have free (G)-orbits.  Let

\[
 V=\frac Mq.                                             \tag{4.1}
\]

There are (V) middle (G)-orbits, hence (V) middle quotient vertices
in each of the three residual sectors.

On either outer rank, there are (t) shortened (G)-orbits.  They become
(t) fixed vertices after quotienting by (H).  The remaining outer
orbits occur in residual triples.  Put

\[
 R=\frac{N/h-t}{3}.                                     \tag{4.2}
\]

Thus each sector has (R) regular lower and (R) regular upper quotient
colours.  Finally put

\[
 p=V-R=\frac{K/h+t}{3}.                                 \tag{4.3}
\]

The second equality follows from

\[
 \frac Kh=3V-(3R+t).                                    \tag{4.4}
\]

For a diagonal phase assignment, let

\[
 r_j=|\phi^{-1}(j)|,\qquad r_0+r_1+r_2=t.               \tag{4.5}
\]

In sector (j), the filters use two edges per necklace and consume one
regular colour on each outer shore.  Therefore a sector-diagonal residual
forest must have

\[
 R-r_j                                                   \tag{4.6}
\]

regular--regular edges.  Together with its (2r_j) filter edges, that
sector has

\[
 R+r_j                                                   \tag{4.7}
\]

forest edges on (V) vertices, and hence, if it is acyclic and spanning,

\[
 p_j=p-r_j                                               \tag{4.8}
\]

path components.  Summing (4.8) gives exactly (K/h).

For the independent phases (3.3), write (r_i^+) for the number of upper
filters in phase (i), and (r_j^-) for the number of lower filters in
phase (j).  If (x_{ij}) regular--regular residual edges run from lower
sector (i) to upper sector (j), exact palette balance is

\[
 \sum_jx_{ij}=R-r_i^+,\qquad
 \sum_ix_{ij}=R-r_j^-.                                  \tag{4.9}
\]

Equation (4.9) is the exact sector transportation law.  It shows why the
three sectors are synchronized rails rather than independent copies.

## 5. A conditional filter-to-spiral composition theorem

### Theorem 5.1 (sector composition)

Fix a diagonal phase assignment (4.5), with (p-r_j\ge1) for every
sector.  Suppose that for each (j\in\mathbb Z_3) there is a set (F_j)
of (R-r_j) sector-(j) Johnson-edge orbits such that:

1. (F_j) uses every regular lower and upper sector-(j) colour not used
   by the filters exactly once;
2. (F_j\cup P_{\phi,j}) is a spanning linear forest on the (V) middle
   vertices of sector (j).

Then

\[
 F=P_\phi\cup F_0\cup F_1\cup F_2                     \tag{5.1}
\]

is an exact two-sided-rainbow quotient forest with (K/h) paths.  Its
(H)-lift is a literal two-sided-rainbow forest on all (M) middle masks
with exactly (K) paths.

If, in addition,

* (p_j-1) legal connector orbits chain the paths of sector (j) into one
  superpath;
* three legal seams join the superpaths cyclically; and
* the resulting quotient-cycle voltage is a unit of (\mathbb Z_h),

then the physical lift is one Hamilton cycle on all (M) middle masks.

#### Proof

The filters cover the (t) fixed outer vertices and (r_j) regular
vertices on each shore in sector (j).  Condition 1 and (4.6) cover every
remaining outer vertex once.  Thus (5.1) is exactly rainbow on both shores.
Condition 2 and (4.8) give (p_j) paths in sector (j), so the quotient
has

\[
 \sum_jp_j=3p-t=K/h
\]

paths.  Every quotient tree lifts to (h) disjoint trees, proving the
physical path count (K).

The internal connector count is

\[
 \sum_j(p_j-1)=K/h-3.
\]

Adding three cross-sector seams gives exactly (K/h) closure edges and one
spanning quotient cycle.  The voltage criterion is (2.5).  \(\square\)

If the three seams are consecutive translates of one seam with clean gain
(c\in\mathbb Z_h), then (\tau^3) is one generator of (H), and their
total voltage is

\[
 v=3c+1\pmod h.                                         \tag{5.2}
\]

Thus a literal zero-gain seam triple has unit voltage one.  Formula (5.2)
is an arithmetic identity, not a claim that the three required Johnson
seams exist.

### Unproved extension lemma

The existence of the (F_j) and of the connector bank in Theorem 5.1 is
not implied by the collision-free filter construction.  This is the exact
residual sector-forest gate.  In the phase-twisted case, (4.9) replaces
condition 1 and off-diagonal sector edges must be allowed.

## 6. Fixed-scaffold collapse with asymmetric palette selection

The preceding sufficient theorem keeps the forest (H)-equivariant.  The
known K16 construction shows that this is stronger than necessary.

Let \(S\) be any fixed spanning Hamilton path or Hamilton cycle in
\(J(\Omega,m)\).  For each literal edge occurrence \(e\) of \(S\), write

\[
 \ell(e)=e^-\cap e^+,\qquad u(e)=e^-\cup e^+.
\]

Form the bipartite occurrence multigraph (I(S)) with the rank-((m-1))
colours on the left, the rank-((m+1)) colours on the right, and one column
for every edge occurrence (e), joining (\ell(e)) to (u(e)).

### Theorem 6.1 (fixed-scaffold Hall collapse)

Let (P\subseteq E(S)) be a prescribed partial matching in (I(S)).  The
following are equivalent.

1. (P) extends inside (S) to a spanning two-sided-rainbow (K)-path
   forest.
2. The residual occurrence graph obtained by deleting the lower and upper
   colour vertices used by (P) has a perfect matching.
3. For every set (X) of unused lower colours,

   \[
   |N_{I(S)}(X)\setminus U(P)|\ge |X|.                  \tag{6.1}
   \]

#### Proof

A perfect matching of (I(S)) chooses exactly (N) edge occurrences and
uses every lower and upper colour once.  Any proper edge subset of one
Hamilton cycle is a linear forest, and every edge subset of one Hamilton
path is a linear forest.  In either case it spans the (M) middle vertices
and has

\[
 M-N=K
\]

components, with isolated middle vertices counted as singleton paths.
Conversely, every two-sided-rainbow forest contained in (S) selects one
column at every vertex of both colour shores.  Fixing (P) is exactly
deletion of its used shore vertices.  Hall's theorem gives the equivalence
of 2 and 3.  \(\square\)

Theorem 6.1 is intentionally physical.  If (S) is an (H)-invariant
strict-spiral scaffold, the residual matching in (I(S)) may break every
remaining symmetry.  The carrier geometry and, for a cyclic scaffold, its
unit voltage are already certified by (S); they are not reimposed on the
matching.  This is the correct way to permit asymmetric long-orbit palette
repairs.  A common-cap compiler is still a later, independent integral
problem and is not constrained to be equivariant.

If an (H)-invariant matching is desired, replace (I(S)) by its orbit
multigraph.  That is a sufficient subclass, not WLOG.

For the complete (unfrozen) lower--upper inclusion graph there is a useful
equivalent form of the residual Hall cut.  Identify an upper colour \(U\)
with the lower-rank set \(D=\Omega\setminus U\).  Then

\[
 L\subset U\quad\Longleftrightarrow\quad L\cap D=\varnothing.
\]

For the diagonal complement-paired filters, the deleted upper shore becomes
the same set \(S\) as the deleted lower shore.  Palette extension is
therefore equivalent to

\[
 \left|\{D\notin S:\exists L\in X,\ L\cap D=\varnothing\}\right|
 \ge |X|\qquad
 (X\subseteq\binom{\Omega}{m-1}\setminus S).            \tag{6.2}
\]

In an equivariant quotient it is enough, and necessary, to test the
\(H\)-stable unions \(X\).  Formula (6.2) is the exact
Kneser-disjointness cut missing from endpoint injectivity; the latter does
not imply it.

## 7. Exact unrestricted extension model

Without a fixed scaffold, orient each usable quotient Johnson-edge orbit.
There are five independent systems:

1. at most one selected edge leaves any middle vertex;
2. at most one selected edge enters any middle vertex;
3. at most one selected edge has any lower colour;
4. at most one selected edge has any upper colour;
5. the selected underlying edges are independent in the graphic matroid.

The first four are partition matroids.  Treat the two orientations of one
underlying edge as parallel elements of the graphic matroid.  A common
independent set of size (N/h), containing an orientation of every edge of
the prescribed filter bank, is exactly a quotient spanning linear forest
which is rainbow on both shores.  Its size forces (K/h) components.

Equivalently, contract an oriented filter bank in all five matroids and ask
for a common independent set of residual size (N/h-2t).  This is an exact
formulation, but it is not a two-matroid intersection and has no generic
min--max theorem.  Ordinary palette Hall omits the tail, head, and graphic
cuts.

There is no generic small-prescribed-matching theorem capable of replacing
these cuts.  The physical filter bank already has

\[
 2h\operatorname {Cat}_a=2\binom{2a+1}{a}              \tag{7.2}
\]

edges, while the degree of the complete outer-colour incidence graph is

\[
 d=\binom{m+1}{2}=\binom{3a+3}{2}.                      \tag{7.3}
\]

The quantity in (7.2) exceeds (7.3) from \(a=3\) onward.  Even after the
clean quotient, \(2\operatorname {Cat}_a>d\) from \(a=6\) onward.  Hence
an extension proof must use the special filter geometry and the literal
cuts (6.1) or (6.2), rather than a theorem asserting extendability for all
small partial matchings.

There is a second exact formulation when a unit-voltage quotient Hamilton
cycle is co-designed.  Give every loopless quotient edge one state in

\[
 \{0,R,C\},                                               \tag{7.1}
\]

where (R) is a rainbow-forest edge and (C) a closure edge.  Require:

* the prescribed filters have state (R);
* every lower and upper quotient colour occurs on exactly one (R)-edge;
* every middle quotient vertex has degree two in (R\cup C);
* (R\cup C) is connected; and
* its total voltage is a unit of (\mathbb Z_h).

Then (|R|=N/h), (|C|=K/h), the (R\)-edges are automatically a
(K/h)-path forest, and the lift is Hamilton.  Conversely every
(H)-equivariant central Hamilton cycle containing the prescribed common
transversal gives (7.1).

This central-cycle criterion still does not imply the uniformly outgoing
directed-repair normal form.  That stronger conclusion additionally needs
one designated tail on every path, the equal-union closure identity, the
signed (D\to Z) palette identity, and distinct incoming cut colours.

## 8. Exact (m=8) specialization

For (m=8),

\[
 q=15,\quad h=5,\quad t=\operatorname {Cat}_2=2,quad
 (M/h,N/h,K/h)=(2574,2288,286).
\]

Equations (4.1)--(4.3) give

\[
 V=858,\qquad R=762,\qquad p=96.                       \tag{8.1}
\]

The two smaller necklaces may be represented by

\[
 A_0=\{0,1\},\qquad A_1=\{0,2\}\subset\mathbb Z_5.
\]

For example choose distinct outside columns

\[
 (b_0,c_0)=(2,3),\qquad (b_1,c_1)=(1,3),               \tag{8.2}
\]

and put the two complement-paired packets in two different phases.  Up to
cyclic relabelling,

\[
 (r_0,r_1,r_2)=(0,1,1).                                \tag{8.3}
\]

The four selected (H)-edge orbits contain twenty literal forest edges,
cover the ten shortened physical colours on each outer side exactly once,
and have forty distinct literal middle endpoints.

The exact sector target is

\[
\begin{array}{c|ccc}
 &0&1&2\\ \hline
\text{residual regular edges}&762&761&761\\
\text{filter edges}&0&2&2\\
\text{total forest edges}&762&763&763\\
\text{path components}&96&95&95.
\end{array}                                             \tag{8.4}
\]

The internal connector count is

\[
 95+94+94=283,                                          \tag{8.5}
\]

and three cross-sector seams give all (286) closures.  A zero-gain
translated seam triple has total (\mathbb Z_5)-voltage one.

Equations (8.1)--(8.5) are exact arithmetic and a complete sufficient
certificate shape.  They do not assert the residual forests, the 286 legal
closure records, or the compiler.

For a complete (H)-equivariant search, the loopless quotient Johnson
catalogue has 2,574 middle vertices, 2,288 lower and 2,288 upper rows, and
82,344 usable edge orbits.  Fixing the four filters in state (R) in
(7.1) is the complete filter-conditioned carrier model.  For a frozen
spiral path or cycle, Theorem 6.1 is strictly smaller and should be used
instead.

The authenticated K16 optimum has four strict (\mathbb Z_{15}) spiral
blocks of base lengths (426,426,3,3), common sheet voltage (+4), and
three physical seams.  Its four final edge defects are **not** the four
short-orbit services above, and its compiler is highly non-equivariant.
It authenticates the scaffold philosophy, not an identification of the two
four-element ledgers.

## 9. Smallest obstruction and the minimal phase repair

Take (m=2) and

\[
 \Omega=\{\infty,0,1,2\}.
\]

The exact diagonal complement-paired filter is

\[
 \{\infty0,\infty1\},\qquad \{12,02\}.                 \tag{9.1}
\]

Its used colour pairs are

\[
 (\infty,\infty01),\qquad(2,012).                       \tag{9.2}
\]

The remaining lower colours are (0,1), and the remaining upper colours
are (\infty02,\infty12).  Inclusion forces the only completion:

\[
 \{\infty0,02\},\qquad\{\infty1,12\}.                 \tag{9.3}
\]

Together, (9.1) and (9.3) form the four-cycle

\[
 \infty0-\infty1-12-02-\infty0,                        \tag{9.4}
\]

while (01) and (\infty2) are isolated.  Hence the exact palette
completion is not a spanning two-path forest.  This disproves the statement
that the prescribed collision-free complement filters always extend.

Now shift only the upper filter phase and use

\[
 \{\infty0,\infty1\},\qquad\{01,02\}.                  \tag{9.5}
\]

The forced residual edges are

\[
 \{\infty1,12\},\qquad\{\infty2,02\},                 \tag{9.6}
\]

and (9.5)--(9.6) are two spanning three-vertex paths.  Thus one relative
phase twist repairs the smallest obstruction without spending clean
(H)-voltage.

The counterexample is a topology no-go, not a no-go for all large (m).
For (a\ge2), the precise remaining theorem is to construct either:

* the residual sector forests and seams of Theorem 5.1, with phase twists
  allowed through (4.9); or
* one strict-spiral path/cycle scaffold containing the filters and satisfying
  the residual Hall inequalities (6.1).

Only after this carrier theorem is proved should the asymmetric integral
compiler be imposed.

## 10. Proven and conditional boundary

Proved here:

1. the clean three-primary quotient audit, including the exact order-three
   multiplicity and unit-voltage convention;
2. phase-wise collision-free filter packets;
3. the exact all-(a) sector count and transportation ledgers;
4. the conditional filter-to-spiral composition theorem;
5. the exact fixed-scaffold Hall equivalence allowing asymmetric palette
   selection;
6. the exact five-matroid and ternary-state formulations;
7. the (m=8) (96/95/95), (283+3), voltage-one certificate shape; and
8. the literal (m=2) diagonal-filter obstruction and its one-phase repair.

Not proved:

1. residual Hall or residual sector-forest existence for all (a\ge2);
2. a bounded strict-spiral scaffold containing every prescribed filter;
3. palette-safe connector existence in all dimensions;
4. uniformly outgoing signed-repair compatibility of those connectors;
5. residence, higher-shadow preservation, or a common-cap compiler; or
6. (\nu(k)=B(k)) beyond the already authenticated finite cases.
