# K16 gap one: anchor private-fan packing and blocker-component escape

Date: 2026-07-30  
Lane: AD  
Status: proved exact all-anchor cut and an endpoint form of anchored durable
rows; no profile SAT or UNSAT verdict

## 1. Frozen setting

Use the three fixed-gap profiles

\[
                  (4,9,4),\qquad(5,8,4),\qquad(5,9,3)
\tag{1.1}
\]

and the common 57-target repair family from the authenticated chart ledger.
Write

\[
                         E=\mathtt{8000}.
\tag{1.2}
\]

The eighteen repair targets omitting \(E\) form the low family
\(\mathcal L\).  Fix the WLOG singleton \(E\)-chart at a position \(p\),
choose one chart \(I_T\) for every repair target, and put

\[
                         Z=\bigcup_{L\in\mathcal L}I_L.
\tag{1.3}
\]

Thus \(p\notin Z\).  Earlier anchor-fan cuts proved
\(|P\setminus Z|\ge2\) only at 8 or 9 of the 17 possible anchor positions,
depending on the profile.  The argument below removes that positional
restriction.

## 2. A general private-fan transversal lemma

Let \(P\) be a disjoint union of paths and let \(I_1,\ldots,I_s\) be
intervals, each lying in one path.  Suppose each \(I_i\) has a point private
against all the other intervals:

\[
                    I_i\setminus\bigcup_{j\ne i}I_j\ne\varnothing.
\tag{2.1}
\]

### Lemma 2.1 (point capacity two)

No point of \(P\) belongs to three of the intervals.  Consequently, if a
set \(S\subseteq P\) meets every \(I_i\), then

\[
                              |S|\ge\left\lceil\frac{s}{2}\right\rceil.
\tag{2.2}
\]

If \(s=4\) and equality holds in (2.2), each interval meets exactly one of
the two points of \(S\), and exactly two intervals meet each point.

#### Proof

Suppose three intervals share a point.  In their common path, choose one
with the leftmost left endpoint and one with the rightmost right endpoint.
Because both contain the common point, their union is the full interval
between those two extreme endpoints and covers the third interval.  The
third therefore has no point private against the other two, contradicting
(2.1).

Every point of a transversal \(S\) consequently meets at most two of the
intervals.  Counting incidences between \(S\) and the intervals gives
\(s\le2|S|\).  When \(s=4\) and \(|S|=2\), equality holds throughout:
both points have incidence two and every interval has incidence one.
\(\square\)

The lemma is an interval-order statement, not a Helly/nonempty-intersection
statement.  It uses the durable private points.

## 3. A four-target context-safe fan

Consider the following four high repair targets and coordinates:

\[
\begin{array}{c|c|c}
T&e_T&\text{possible maximal contexts over all three profiles}\\ \hline
\mathtt{8c62}&\mathtt{0002}&\{\mathtt{0000}\}\\
\mathtt{942d}&\mathtt{0004}&\{\mathtt{0000},\mathtt{1009}\}\\
\mathtt{a879}&\mathtt{0010}&\{\mathtt{0000}\}\\
\mathtt{c421}&\mathtt{4000}&\{\mathtt{0000}\}.
\end{array}
\tag{3.1}
\]

Every target in (3.1) contains \(E\), while none of its possible contexts
contains \(E\).  Moreover

\[
 e_T\in T\setminus b_T(I_T),\qquad
 e_T\notin U\quad(U\ne T\text{ in (3.1)}).
\tag{3.2}
\]

The four private coordinates are respectively bits 1, 2, 4, and 14.  The
claims in (3.1)--(3.2) are direct hexadecimal inclusions.  In particular,
the sole nonzero possible context `0x1009` for `0x942d` omits both `0x8000`
and its private bit `0x0004`.

### Theorem 3.1 (all-anchor low-union cut)

Every feasible chart selection in every profile (1.1) satisfies

\[
                              |P\setminus Z|\ge2.
\tag{3.3}
\]

This holds for all seventeen possible singleton-anchor locations.

#### Proof

For any target \(T\) in (3.1), bit \(E\) is not supplied by its fixed
context.  The exact durable-point condition therefore gives

\[
                         I_T\setminus Z\ne\varnothing,
\tag{3.4}
\]

because the targets omitting \(E\) are exactly the low family whose union
is \(Z\).  Hence \(S=P\setminus Z\) is a transversal of the four displayed
intervals.

For each displayed \(T\), its private bit \(e_T\) is required by (3.2).
Every other displayed target omits that bit.  The durable-point condition
for \(e_T\) therefore supplies a point of \(I_T\) outside all three other
displayed intervals.  Thus the four intervals satisfy (2.1).  Lemma 2.1
with \(s=4\) yields (3.3). \(\square\)

### Corollary 3.2 (sharp equality packet form)

If \(|P\setminus Z|=2\), write its two points as \(p,y\), with \(p\) the
singleton `0x8000` anchor.  Then the four charts in (3.1) split into two
pairs: exactly two contain \(p\), exactly two contain \(y\), and none
contains both points.

Thus every equality branch has only three possible pairings of the four
named targets.  This is an exact branch decomposition; it does not assert
that any pairing extends to a complete chart selection.

#### Proof

Apply the equality statement of Lemma 2.1 to the transversal
\(P\setminus Z\). \(\square\)

### Corollary 3.3 (interior-crossing necessity at equality)

If \(|P\setminus Z|=2\), both low-free points are interior cells of their
respective collars.  At either low-free point, the two displayed charts
through it are incomparable intervals.  After exchanging their names, their
endpoints obey

\[
                    \ell_1<\ell_2\le x\le r_1<r_2.
\tag{3.5}
\]

In particular, if the singleton `0x8000` anchor is at any collar endpoint,
then

\[
                              |P\setminus Z|\ge3.
\tag{3.6}
\]

#### Proof

Each chart in (3.1) has a private point outside the other three displayed
charts.  Hence the two charts paired at a low-free point each have a point
outside the other; neither interval contains the other.  Two intervals on a
line which meet and are incomparable have their left and right endpoints in
the same strict order, giving (3.5).  Such a crossing needs a cell on each
side of their common point.  At a collar endpoint all intervals through the
point are nested, so equality is impossible there. \(\square\)

## 4. Exact blocker-component endpoint form

The preceding fan is one instance of a more general anchored chronology
principle.  Work in the collar containing the singleton anchor \(p\).  For
a low coordinate bit \(q\), let

\[
 Z_q=\bigcup_{T:\ q\notin T} I_T
\tag{4.1}
\]

inside that collar.  Since the singleton target \(E\) omits \(q\), we have
\(p\in Z_q\).  Let

\[
                       C_q(p)=[L_q,R_q]
\tag{4.2}
\]

be the connected component of the covered cells \(Z_q\) containing \(p\),
where connectivity is in the discrete collar path.

### Theorem 4.1 (anchored durable row equals component escape)

Let a selected chart \(I_T=[\ell_T,r_T]\) contain \(p\), and suppose

\[
                         q\in T\setminus b_T(I_T).
\tag{4.3}
\]

Then its durable-\(q\) condition is equivalent to

\[
                 \ell_T<L_q\qquad\text{or}\qquad r_T>R_q.
\tag{4.4}
\]

#### Proof

The durable condition is \(I_T\nsubseteq Z_q\).  Both \(I_T\) and the
component \(C_q(p)\) contain \(p\).  If the interval remains between
\(L_q\) and \(R_q\), it lies in the covered component and fails.  If its
left endpoint lies left of \(L_q\), the first cell immediately before the
component along the interval is uncovered; the right case is symmetric.
Thus escape from \(Z_q\) is exactly endpoint escape from (4.2). \(\square\)

The component endpoints have a monotone closure description.  Start from
\([L,R]=[p,p]\), and repeatedly adjoin every selected \(q\)-omitting
interval whose distance from \([L,R]\) in the discrete path is at most one;
replace \([L,R]\) by the hull.  The process stabilizes after at most the
collar width and its fixed point is exactly \([L_q,R_q]\).  Therefore all
durable rows of charts through the anchor can be tested by a component-growth
state followed by the two endpoint alternatives (4.4).  This is an exact
decomposable formulation beyond static marginals and pairwise Helly cuts.

As a necessary anchored-only relaxation, if

\[
 d_L(T)=p-\ell_T,qquad d_R(T)=r_T-p,
\]

then every demand (4.3) must choose one of

\[
\begin{split}
d_L(T)&>\max\{d_L(U):p\in I_U,\ q\notin U\},\\
d_R(T)&>\max\{d_R(U):p\in I_U,\ q\notin U\}.
\end{split}
\tag{4.5}
\]

The full component test (4.4), not merely (4.5), also accounts for
non-anchored blocker intervals joined to the anchor component by a chain.

## 5. Exact remaining boundary

Theorem 3.1 proves the all-location cut \(|P\setminus Z|\ge2\), and
Corollaries 3.2--3.3 give a two-packet crossing normal form when equality
holds, including the stronger endpoint-anchor bound (3.6).  They do not
eliminate an anchor location or prove any profile infeasible: the low charts
may leave the required two or three cells uncovered.  A further contradiction must
either

* rule out all three equality pairings while also controlling the second
  low-free cell;
* prove a third low-free cell is necessary; or
* combine the blocker-component escapes (4.4) with context and width limits
  for targets assigned away from the anchor collar.

All statements remain inside the exact one-chart-per-target literal model.
No assertion is made about a changed fixed gap or an unrelated
length-12,873 word.
