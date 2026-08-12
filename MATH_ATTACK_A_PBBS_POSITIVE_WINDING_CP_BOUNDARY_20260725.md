# Positive-winding PBBS returns at the Catalan packing scale

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B=\operatorname{Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
\]

where (A>0) is fixed.  This report treats only positive-winding
step-two PBBS return intervals.  It does **not** prove their desired
quotient packing bound (O_A(B/N)).

It proves three exact statements.

1.  A return of winding (w\ge1) carries two strictly monotone sector
    partitions.  Their common lifted range has length exactly (wN), and
    their common refinement has at most (2s-1) nonempty cells for a
    step-two return time (s).  Consequently some chronological
    even--odd sector pair has overlap at least

    \[
      \boxed{\frac{wN}{2s-1}.}
      \tag{0.1}
    \]

    In the Gaussian window this is at least
    (c_Aw\sqrt r).  This retains both endpoint chronologies; it is not a
    pointwise deficit charge.

2.  For every pairwise quotient-edge-disjoint family \(\mathcal P^+\) of
    positive-winding intervals,

    \[
      \boxed{
      \sum_{I\in\mathcal P^+}
       \left(2Nw(I)+\delta(D_0(I))+\delta(D_s(I))\right)
      \le 2\sum_{D\in\mathcal D_r}d(D).}
      \tag{0.2}
    \]

    The audited first-deficit moment therefore gives

    \[
      \sum_{I\in\mathcal P^+}w(I)=O(B/\sqrt r).
      \tag{0.3}
    \]

    In particular, for every fixed \(\eta>0\), the subfamily with
    (w(I)\ge\eta\sqrt r) already has packing

    \[
       \boxed{O_\eta(B/r)=O_\eta(B/N).}
       \tag{0.4}
    \]

3.  The numerical information in the centered winding identities, both
    endpoint ledgers, height stratification, cycle closure, the area
    coboundary, and full edge-disjoint trace capacities is not sufficient
    to improve (0.3).  An explicit formal cycle profile below satisfies
    all those numerical constraints and has \(\Theta(\sqrt N)\) disjoint
    winding-one intervals per (N)-edge cycle.  It is deliberately **not**
    claimed to be a PBBS orbit: it violates literal omitted-coordinate
    coverage.  Thus it is a rigorous no-go for products of the listed
    ledgers, not a counterexample to \((CP_A)\).

The exact surviving positive-winding class is therefore

\[
 \boxed{w=o(\sqrt r),\quad\text{and in particular }w=1,}
 \tag{0.5}
\]

together with the large transported sector-pair cell in (0.1).  Any proof
of the Catalan-order bound for this class must use literal PBBS
voltage-word/Dyck compatibility, not only marginal sector mass or trace
length.

## 1. Exact two-endpoint notation

Let \(\phi\) be the one-step normalized PBBS map and
\(\tau=\phi^2\).  Along a step-two trajectory put

\[
 D_j=\tau^jD_0,
 \qquad
 a_j=\delta(D_j),
 \qquad
 b_j=\delta(\phi D_j),
 \tag{1.1}
\]

and

\[
 c_j=d(D_j),
 \qquad
 \widehat c_j=d(\phi D_j).
 \tag{1.2}
\]

The exact block-rotation identities are

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1}.
 \tag{1.3}
\]

In particular every (c_j,\widehat c_j) is a positive odd integer and

\[
 \boxed{a_{j+1}-a_j-c_j=-\widehat c_j.}
 \tag{1.4}
\]

Define

\[
 C_j=\sum_{i=0}^{j-1}c_i,
 \qquad
 Y_j=a_j-C_j.
 \tag{1.5}
\]

Then (1.4) gives the strict recursion

\[
 \boxed{Y_{j+1}=Y_j-\widehat c_j.}
 \tag{1.6}
\]

Suppose the omitted coordinate returns after (2s+1<N) ordinary PBBS
steps.  Its uniquely determined two-step winding (w\ge0) is defined by

\[
 \boxed{C_s=a_s+wN.}
 \tag{1.7}
\]

Equations (1.5)--(1.7) yield the dual endpoint ledger

\[
 \boxed{
 \sum_{j=0}^{s-1}\widehat c_j=a_0+wN.}
 \tag{1.8}
\]

Indeed (Y_0=a_0), while (Y_s=a_s-C_s=-wN), and (1.6)
telescopes.  Using the audited fact that sub-circumference same-label gaps
are odd, the return is consecutive exactly when

\[
 Y_j\not\equiv0\pmod N\qquad(1\le j<s).
 \tag{1.9}
\]

No zero-winding converse or static sector transport is used here.

## 2. The overlap-staircase theorem

For (0\le j<s), define half-open real intervals

\[
 E_j=(-C_{j+1},-C_j],
 \qquad
 O_j=(Y_{j+1},Y_j].
 \tag{2.1}
\]

They have lengths

\[
 |E_j|=c_j,
 \qquad
 |O_j|=\widehat c_j.
 \tag{2.2}
\]

### Theorem 2.1 (exact two-endpoint overlap staircase)

For a winding-(w\) return of step-two time (s),

\[
 \bigcup_{j<s}E_j=(-a_s-wN,0],
 \qquad
 \bigcup_{j<s}O_j=(-wN,a_0].
 \tag{2.3}
\]

Consequently

\[
 \boxed{
 \left(\bigcup_{j<s}E_j\right)
 \cap
 \left(\bigcup_{j<s}O_j\right)
 =(-wN,0],}
 \tag{2.4}
\]

and therefore

\[
 \boxed{
 \sum_{0\le j,k<s}|E_j\cap O_k|=wN.}
 \tag{2.5}
\]

The nonempty cells (E_j\cap O_k), ordered from left to right, form a
monotone path in the (s\)-by-(s) index grid.  There are at most
(2s-1) such cells.  If (w\ge1), at least one satisfies

\[
 \boxed{|E_j\cap O_k|\ge\frac{wN}{2s-1}.}
 \tag{2.6}
\]

#### Proof

The (C_j)'s strictly increase from (0) to (a_s+wN).  Hence the
(E_j)'s are consecutive, interior-disjoint intervals whose union is the
first interval in (2.3).  By (1.6), the (Y_j)'s strictly decrease from
(a_0) to (-wN), so the (O_j)'s similarly partition the second
interval in (2.3).  Since (a_0,a_s>0), their intersection is exactly
((-wN,0]), proving (2.4)--(2.5).

Restrict both ordered partitions to the common interval ((-wN,0]).
Each has at most (s-1) internal boundary points.  Their common
refinement therefore has at most

\[
 (s-1)+(s-1)+1=2s-1
\]

nonempty atoms.  As one moves from left to right, one crosses boundaries
of each partition in its fixed order, so the corresponding pair of
indices moves monotonically in the product grid.  Finally (2.5) and the
pigeonhole principle give (2.6).  \(\square\)

For (s\le H=\lceil A\sqrt r\rceil), (2.6) implies, for all large (r),

\[
 |E_j\cap O_k|
 \ge {w(2r+1)\over2\lceil A\sqrt r\rceil-1}
 \ge {w\sqrt r\over A+1}.
 \tag{2.7}
\]

Thus even winding one forces a mesoscopic overlap between one actual
even sector and one actual half-shifted sector.  The theorem also records
the complete chronology of all such overlaps, rather than merely their
total mass.

## 3. Exact packing budget and the solved high-winding range

Let

\[
 \mathscr D_r=\sum_{D\in\mathcal D_r}d(D).
 \tag{3.1}
\]

The audited first-deficit moment theorem states that an absolute constant
(C) satisfies

\[
 \mathscr D_r\le C\sqrt r\,B.
 \tag{3.2}
\]

### Theorem 3.1 (two-endpoint winding budget)

Let \(\mathcal P\) be a family of pairwise quotient-edge-disjoint return
intervals.  If (D_0(I),\ldots,D_{s(I)-1}(I)) are the step-two edges in
the core of (I), then

\[
 \boxed{
 \sum_{I\in\mathcal P}
 \bigl(2Nw(I)+a_0(I)+a_s(I)\bigr)
 \le2\mathscr D_r.}
 \tag{3.3}
\]

#### Proof

The even step-two supports of distinct intervals are disjoint.  Using
(1.7),

\[
 \sum_{I\in\mathcal P}(a_s(I)+Nw(I))
 =\sum_{I\in\mathcal P}\sum_{j<s(I)}d(D_j(I))
 \le\mathscr D_r.
 \tag{3.4}
\]

The map \(\phi\) is a bijection.  Therefore the half-shifted supports

\[
 \{\phi D_j(I):0\le j<s(I)\}
\]

are also pairwise disjoint.  Equation (1.8) gives

\[
 \sum_{I\in\mathcal P}(a_0(I)+Nw(I))
 =\sum_{I\in\mathcal P}\sum_{j<s(I)}d(\phi D_j(I))
 \le\mathscr D_r.
 \tag{3.5}
\]

Adding (3.4) and (3.5) proves (3.3).  \(\square\)

### Corollary 3.2 (winding stratification)

For every integer (K\ge1),

\[
 \boxed{
 \#\{I\in\mathcal P:w(I)\ge K\}
 \le {\mathscr D_r\over KN}
 =O\!\left({B\over K\sqrt r}\right).}
 \tag{3.6}
\]

In particular, for every fixed \(\eta>0\),

\[
 \boxed{
 \#\{I\in\mathcal P:w(I)\ge\eta\sqrt r\}
 =O_\eta(B/N).}
 \tag{3.7}
\]

#### Proof

Drop the positive endpoint terms in (3.3), use (3.2), and use
(N\asymp r).  \(\square\)

This is an actual (CP_A)-scale theorem for the high-winding sector.  It
leaves every fixed winding, particularly (w=1), untouched at the
larger (B/\sqrt r) scale.

## 4. Why the overlap theorem does not by itself add a factor

For one interval, the cells in Theorem 2.1 use only its even roots
(D_j) and its half-shifted roots \(\phi D_k).  Across a
quotient-edge-disjoint family, no even root and no half-shifted root occurs
in two different cell staircases.  Nevertheless the full cell mass is
exactly

\[
 \sum_{j,k}|E_j\cap O_k|=wN,
\]

and it is bounded globally by the same sector resource as (3.4).  Thus
simply summing overlap lengths reproduces the winding budget; it does not
square it.  Similarly, selecting the largest cell in (2.6) produces a
bipartite matching of transported even--odd sector pairs, but a bound on
the sum of their cell lengths is still only (O(\mathscr D_r)).

The next lemma shows that this loss is not an artefact of a loose
inequality.

## 5. A sharp numerical pseudoprofile

The purpose of this section is a no-go statement about proof inputs.  The
object constructed here is **not** asserted to be a Dyck/PBBS orbit.

Choose odd integers (s\ge5) and (e\ge3), with

\[
 s\not\equiv1\pmod3,
 \tag{5.1}
\]

and put

\[
 N=e(2s+1),
 \qquad
 h=s-1,
 \qquad
 a=b=e(s-1),
 \qquad
 c=\widehat c=3e.
 \tag{5.2}
\]

For a prescribed fixed Gaussian cutoff (A>0), one may take
(e/s) in any fixed compact interval above (4/A^2).  Then
(s\le A\sqrt{(N-1)/2}) for all large (s), while
(e=\Theta_A(s)) and (N=\Theta_A(s^2)).

Then (N) is odd and

\[
 a+b+c=N.
 \tag{5.3}
\]

Consider a formal directed (N)-edge cycle all of whose vertices carry
the constant data in (5.2), and declare its step-two first-maximum
positions to be (a_j=a), its complementary positions (b_j=b), and
its two deficits (c_j=\widehat c_j=c).

### Proposition 5.1 (simultaneous saturation of the numerical ledgers)

The formal profile (5.2) has the following properties.

1.  It obeys both block identities (1.3), the recurrence (1.4), the
    centered deficit identity, and the area increment identity
    (a_j-b_j=0).

2.  Every phase has a first return at step-two time (s), of winding
    exactly one.

3.  The return respects the height and parity restrictions
    (h=s-1\le s) and (a\equiv h\pmod2).

4.  The total step-two voltage on the formal cycle is
    (Nc=3eN), a multiple of (N).

5.  The cycle contains \(\lfloor N/s\rfloor\) edge-disjoint
    (s)-edge return cores.  Even if two endpoint edges are added to
    every support, it still contains \(\Theta_A(s)=\Theta_A(\sqrt N)\)
    disjoint full traces.

6.  Both the winding budget and the reciprocal-height trace budget are
    saturated to constant factors.  Replicating the profile on a total of
    (B) formal vertices gives packing

    \[
       \Theta_A(B/s)=\Theta_A(B/\sqrt N),
       \tag{5.4}
    \]

    while its total deficit mass is

    \[
       3eB=\Theta_A(B\sqrt N).
       \tag{5.5}
    \]

#### Proof

Equation (5.3) proves the first block identity.  Since (a_{j+1}=a_j),

\[
 N-b_j-a_{j+1}=N-2a=3e=c,
\]

so the half-shifted identity and (1.4) also hold.  The area increment is
(a-b=0).

At time (s),

\[
 sc=3es=N+a,
 \tag{5.6}
\]

so the winding is one.  Equivalently, the formal one-step voltage is
constantly (a), and

\[
 \gcd(a,N)
 =e\gcd(s-1,2s+1)
 =e\gcd(s-1,3)
 =e
 \tag{5.7}
\]

by (5.1).  Hence its first repeated omitted label has gap

\[
 {N\over\gcd(a,N)}=2s+1,
\]

which proves first-return minimality.  The forward winding of this
one-step loop is

\[
 {(2s+1)a\over N}=s-1,
\]

so its two-step winding is (s-(s-1)=1), consistently with (5.6).

The centered identity is also exact:

\[
 s(c-1)=3es-s=a+N-s.
 \tag{5.8}
\]

Since (s,e) are odd, (h=s-1) and (a=e(s-1)) are both even.  Thus the
first-maximum parity condition holds, and the height--gap restriction is
an equality up to one.  The cycle-voltage assertion is immediate.

Taking consecutive nonwrapping (s)-edge arcs with starts spaced by (s)
gives \(\lfloor N/s\rfloor\) disjoint return cores.  Homogeneity makes
each one a return core.  Spacing starts by (s+2) instead still leaves
\(\Theta_A(N/s)=\Theta_A(s)\) disjoint endpoint-augmented traces.
Finally (e=\Theta_A(s)) and (N=\Theta_A(s^2)), so the displayed packing
and mass estimates follow.  \(\square\)

### Why this is not a PBBS counterexample

In the formal profile the ordinary omitted label advances constantly by
(a).  Equation (5.7) shows that it visits only (2s+1<N) coordinate
labels.  A genuine PBBS component has the audited omitted-coordinate
coverage/reconstruction property: every coordinate occurs, and the full
voltage itinerary reconstructs the quotient cycle.  Thus the profile
cannot be promoted to a literal PBBS orbit.  This failure is intentional
and identifies exactly the information absent from the numerical ledgers.

The example nevertheless proves a precise logical point: the following
data, even imposed simultaneously, admit (\Theta(B/\sqrt N)) packing:

* both exact endpoint winding ledgers;
* the centered floor (c-1);
* height (h=\Theta(\sqrt N)) and full trace-length capacity;
* cycle-voltage closure;
* the area coboundary; and
* the complete overlap staircase of Theorem 2.1.

Therefore no nonnegative product or interpolation of only these data can
prove (O(B/N)).  Literal voltage coverage or an equally strong Dyck-word
correlation is essential.

## 6. Exact remaining lemma

For a genuine return, transport the intervals (E_j,O_k) of (2.1) to
their actual common spatial lift.  Call a pair ((D_j,\phi D_k))
**large** when

\[
 |E_j\cap O_k|\ge {N\over2H-1}.
 \tag{6.1}
\]

Theorem 2.1 says that every positive-winding return of time at most (H)
contains a large pair.  In a quotient-edge-disjoint family, choosing one
such pair per interval gives a matching: all chosen even roots are
distinct and all chosen half-shifted roots are distinct.

Thus the smallest chronology-sensitive statement isolated by this lane is
the following.

> **Genuine transported-sector matching lemma (unproved).**  For every
> fixed (A>0), among the genuine PBBS/Dyck voltage trajectories at rank
> (r), every matching obtained by choosing one transported large pair
> from each edge-disjoint winding-(w) return with
> (1\le w=o(\sqrt r)) and (s\le\lceil A\sqrt r\rceil) has size
> (O_A(B/N)).

This is stronger than a marginal high-deficit count and weaker than
reproving the whole residence theorem from scratch: it asks only for one
certified even--odd crossing cell from each positive-winding interval.
The pseudoprofile proves that the word “genuine” cannot be dropped.

## 7. Adversarial audit

1.  **Sign check.**  From
    (a_{j+1}-a_j-c_j=-\widehat c_j) and
    (Y_j=a_j-C_j), one gets
    (Y_{j+1}=Y_j-\widehat c_j), not the opposite sign.  Hence
    (Y_s=-wN), and the common interval in (2.4) is exactly
    ((-wN,0]).

2.  **Cell count.**  The (2s-1) bound is applied after restricting both
    partitions to their common interval.  Truncation cannot increase the
    number of internal boundaries, so no endpoint cell is missing.

3.  **Half-shifted capacity.**  Quotient-edge-disjointness makes the
    (D_j)'s distinct across intervals.  Applying the bijection \(\phi\)
    makes all \(\phi D_j)'s distinct as well.  Thus (3.5) does not assume
    an independent odd-parity packing.

4.  **Normalization.**  Theorem 3.1 is a quotient statement, so its total
    resource is \(\mathscr D_r\), not (N\mathscr D_r).  The latter is
    the corresponding physical-deck resource.

5.  **Scope of the pseudoprofile.**  Proposition 5.1 is explicitly an
    axiomatic counterprofile.  It is not a Dyck word, PBBS factor, or
    counterexample to (CP_A).  Its omitted-label coverage failure is
    stated and is precisely the missing literal constraint.

6.  **What is actually solved.**  Corollary 3.2 reaches (O(B/N)) only
    for winding at least a fixed multiple of \(\sqrt r\).  It gives no
    (CP_A)-scale estimate for winding one.  The latter remains the sharp
    positive-winding residual.

Accordingly, the proved/conditional boundary is

\[
 \boxed{
 \begin{aligned}
 &w\ge\eta\sqrt r:
   &&O_\eta(B/N)\quad\text{proved},\\
 &1\le w=o(\sqrt r):
   &&\text{exact overlap staircase proved, packing open},\\
 &\text{all positive winding at }H=A\sqrt r:
   &&O_A(B/N)\quad\text{not proved},\\
 &CP_A\text{ and coefficient one}:
   &&\text{not claimed}.
 \end{aligned}}
 \tag{7.1}
\]
