# Integral rotor rounding has a mandatory two-sided collar

**Date:** 2026-08-03  
**Status:** unconditional necessary invariant, exact maximal-factor pinning
criterion, and a sufficient separated singleton-packing theorem.  This
extends the previously proved depth-three one-position run-boundary lemma to
arbitrary depth and to every short physical interval.  It does **not**
construct the required owner/coatom cycle or prove an additive upper bound.

## 0. Outcome

Let \(W={k\choose r}\), and let

\[
 T_0,T_1,\ldots,T_{W-1}\in { [k]\choose r}
\]

be a cyclic Johnson carrier which runs through the complete rank-\(r\)
layer once, with indices modulo \(W\), and write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.                 \tag{0.1}
\]

Assume it has a depth-\(d\) literal factor

\[
 T_i=A_i\cup A_{i+1}\cup\cdots\cup A_{i+d},
 \qquad A_i\ne\varnothing.                              \tag{0.2}
\]

Every source position has the compulsory footprint

\[
 \boxed{\{\alpha_j,\beta_{j-d-1}\}\subseteq A_j.}       \tag{0.3}
\]

More generally, every \(q\)-cell lower interval has the mandatory collar

\[
 \boxed{
 K_{j,q}:=
 \{\alpha_j,\ldots,\alpha_{j+q-1}\}
 \cup
 \{\beta_{j-d-1},\ldots,\beta_{j+q-d-2}\}
 \subseteq \bigcup_{h=j}^{j+q-1}A_h .}                 \tag{0.4}
\]

When \(1\le q\le d+1\), each displayed alpha block and beta block has
cardinality \(q\).  Their overlap is exactly a census of positive carrier
runs whose lengths are close to the deadline.  If \({\cal R}\) is the
multiset of maximal positive coordinate runs and \(L(R)\) is their number
of carrier vertices, then

\[
 \boxed{
 \sum_{j\in\mathbb Z_W}|K_{j,q}|
 =2qW-\sum_{R\in{\cal R}}
       \bigl(q-(L(R)-d-1)\bigr)_+.}                   \tag{0.5}
\]

In particular, a one-coordinate source letter can occur only at the end of
an exact minimum positive run of length \(d+1\).  On the cyclic face,

\[
 \boxed{A_j=\{x\}\quad\Longrightarrow\quad
 \alpha_j=\beta_{j-d-1}=x,}                           \tag{0.6}
\]

and the \(x\)-run is precisely

\[
 T_{j-d},T_{j-d+1},\ldots,T_j.                        \tag{0.7}
\]

Thus every residual singleton target \(\{x\}\) requires a minimum run of
the **same coordinate**.  This is a labelled obstruction, not just a scalar
count.  It is absent from the stationary same-owner fractional pull clock.

There is also a sharp constructive statement.  The maximal erosion factor

\[
 E_j:=\bigcap_{i=j-d}^{j}T_i                           \tag{0.8}
\]

can be pinned at selected positions.  Prescribing nonempty
\(S_j\) with

\[
 \{\alpha_j,\beta_{j-d-1}\}\subseteq S_j\subseteq E_j \tag{0.9}
\]

and leaving every other position equal to \(E_j\) remains a factor exactly
when no required coordinate is deleted from all \(d+1\) suppliers of one
owner occurrence.  Pairwise cyclic distance at least \(d+1\) makes this
condition automatic.  Consequently, if each required coordinate has at
least

\[
                   (2d+1)(s-1)+1                     \tag{0.10}
\]

minimum-run positions, where \(s\) singleton targets are to be planted,
then all \(s\) singleton letters can be planted simultaneously by a greedy
separated transversal.

The theorem sharpens the post-fractional integral gate:

\[
 \boxed{
 \text{rank-stationary clockability}
 \quad\not\Rightarrow\quad
 \text{the labelled lag-}(d+1)\text{ collar system (0.4)}.}
\]

Any integral rotor-fusion theorem must synthesize that collar globally
while it rethreads the owners.

## 1. The one-position compulsory footprint

### Lemma 1.1

Every factor (0.2) satisfies (0.3).

### Proof

The coordinate \(\alpha_j\) belongs to \(T_j\) and not to \(T_{j+1}\).
The two source windows are

\[
 [j,j+d]\quad\hbox{and}\quad[j+1,j+d+1].
\]

Their only old position is \(j\), so \(\alpha_j\in A_j\).

Likewise \(\beta_{j-d-1}\) is absent from \(T_{j-d-1}\) and present in
\(T_{j-d}\).  The only new source position in the latter window is \(j\),
so \(\beta_{j-d-1}\in A_j\).  This proves (0.3). \(\square\)

Taking unions of Lemma 1.1 over \(h=j,\ldots,j+q-1\) proves (0.4).

## 2. The mandatory-collar/run identity

Depth-\(d\) factorability implies that every positive coordinate run in
the carrier has length at least \(d+1\).  Also, any \(q\le d+1\)
consecutive departure labels are distinct, and the same holds for arrival
labels: two departures (or two arrivals) of one coordinate would enclose a
positive run shorter than \(d+1\).

Fix a maximal positive run \(R\).  If its entry transition is \(p\) and
its departure transition is \(u\), then

\[
                     L(R)=u-p.                       \tag{2.1}
\]

The arrival \(\beta_p\) occurs in the second block of (0.4) at the shifted
source index \(p+d+1\), while the equal departure \(\alpha_u\) occurs in
the first block at index \(u\).  Their distance in those two aligned
source-index blocks is

\[
                 h_R=u-(p+d+1)=L(R)-d-1\ge0.         \tag{2.2}
\]

### Theorem 2.1 (exact overlap census)

For every \(1\le q\le d+1\),

\[
 \sum_{j\in\mathbb Z_W}
 \left|
 \{\alpha_j,\ldots,\alpha_{j+q-1}\}
 \cap
 \{\beta_{j-d-1},\ldots,\beta_{j+q-d-2}\}
 \right|
 =\sum_{R\in{\cal R}}(q-h_R)_+.                    \tag{2.3}
\]

Consequently (0.5) holds, and every physical \(q\)-cell satisfies

\[
 \left|\bigcup_{h=j}^{j+q-1}A_h\right|
 \ge 2q-|\text{the two collar blocks intersect}|.   \tag{2.4}
\]

### Proof

For a fixed run, its aligned arrival and departure positions are two points
at forward cyclic distance \(h_R\) in the source-index line.  The opposite
distance is larger than \(d+1\): a coordinate occurs in only
\({k-1\choose r-1}=rW/k\) carrier owners altogether, so one positive run
cannot leave an opposite gap shorter than any \(q\le d+1\).  A cyclic
interval of length \(q\) therefore contains both in exactly \(q-h_R\)
positions when \(h_R<q\), and in none otherwise.  Distinct runs give distinct
arrival/departure incidences, so summing gives (2.3).  Both blocks have
size \(q\), hence inclusion--exclusion gives (0.5).  Finally (0.4) gives
(2.4). \(\square\)

For \(q=1\), (2.4) reads

\[
 |A_j|\ge
 \begin{cases}
 1,&\alpha_j=\beta_{j-d-1},\\
 2,&\alpha_j\ne\beta_{j-d-1}.
 \end{cases}                                            \tag{2.5}
\]

Equality of the two labels says that the coordinate enters between
\(T_{j-d-1}\) and \(T_{j-d}\), remains present through \(T_j\), and
leaves immediately afterward.  This is exactly the minimum run (0.7),
proving (0.6).

### Corollary 2.2 (near-minimum-run capacity inequalities)

Choose one physical witness for every strict-lower target represented by
the cyclic factor, and let \(n_{s,q}\) be the number of chosen rank-\(s\)
targets whose chosen witness uses exactly \(q\) consecutive source letters,
where \(1\le q\le d\).  Then, for every \(q\),

\[
 \boxed{
 \sum_{s=1}^{r-1}(2q-s)_+\,n_{s,q}
 \le
 \sum_{R\in{\cal R}}
       \bigl(q-(L(R)-d-1)\bigr)_+.}                 \tag{2.6}
\]

If the factor itself supplies every strict-lower target, the variables also
satisfy

\[
                    \sum_{q=1}^{d}n_{s,q}={k\choose s}
                    \qquad(1\le s<r).               \tag{2.7}
\]

Thus any integral one-copy rotor must solve the finite allocation system
(2.6)--(2.7) against its **labelled near-minimum run spectrum**.  The scalar
short-interval count alone omits these inequalities.

#### Proof

Put

\[
 o_{j,q}:=
 \left|
 \{\alpha_j,\ldots,\alpha_{j+q-1}\}
 \cap
 \{\beta_{j-d-1},\ldots,\beta_{j+q-d-2}\}
 \right|.                                           \tag{2.8}
\]

If the \(q\)-cell at \(j\) has value \(S\) of rank \(s\), then its
mandatory collar has size \(2q-o_{j,q}\) and lies in \(S\).  Hence

\[
                         o_{j,q}\ge(2q-s)_+.         \tag{2.9}
\]

Distinct chosen targets use distinct physical cells: one cell has only one
union value.  Summing (2.9) over all selected \(q\)-cells and then bounding
by the sum over all \(W\) positions gives the left side of (2.6) at most
\(\sum_j o_{j,q}\).  Theorem 2.1 identifies that total with the right side.
Equation (2.7) is just the census of all rank-\(s\) targets. \(\square\)

For \(q=1\), the right side of (2.6) is exactly the number of positive
runs of length \(d+1\).  Taking singleton witnesses of minimum physical
length recovers the scalar part of Corollary 4.1.  For larger \(q\), (2.6)
requires clusters of several aligned near-minimum arrivals/departures; it
is the higher-rank analogue of the singleton minimum-run gate.

## 3. Exact maximal erosion and simultaneous pins

The next statement is the arbitrary-depth cyclic form of the earlier
depth-three run-boundary theorem.

### Theorem 3.1 (maximal erosion factor)

Assume every positive carrier run has length at least \(d+1\).  Then

\[
                         T_i=\bigcup_{j=i}^{i+d}E_j. \tag{3.1}
\]

### Proof

Fix a coordinate whose positive carrier run is the cyclic interval
\([s,t]\), of length at least \(d+1\).  Equation (0.8) places that
coordinate in the erosion positions \([s+d,t]\).  For every
\(i\in[s,t]\), the interval \([i,i+d]\) meets \([s+d,t]\): use
\(s+d\) near the left end and \(t\) near the right end.  Thus every
required owner occurrence is supplied.  Conversely, (0.8) prevents a
coordinate outside \(T_i\) from entering the union in (3.1). \(\square\)

### Theorem 3.1A (exact individual q-cell aperture)

For \(1\le q\le d\), put

\[
 E_{j,q}:=\bigcup_{h=j}^{j+q-1}E_h.
\]

Then

\[
 \boxed{
 E_{j,q}=\bigcap_{i=j+q-1-d}^{j}T_i.}               \tag{3.2a}
\]

Every value \(S\) of the physical \(q\)-cell beginning at \(j\) obeys the
exact carrier-only aperture

\[
                         K_{j,q}\subseteq S\subseteq E_{j,q}. \tag{3.2b}
\]

Conversely, every nonempty set \(S\) satisfying (3.2b) is individually
realizable: there is a depth-\(d\) factor equal to the maximal erosion
factor outside \([j,j+q-1]\), whose union on that block is exactly \(S\).

#### Proof

Every \(E_h\) in the displayed union is contained in every owner whose
window contains all of \([j,j+q-1]\), giving the forward inclusion in
(3.2a).  Conversely, suppose coordinate \(x\) occurs throughout the owner
interval \([j+q-1-d,j]\).  In the positive run \([s,t]\) containing that
interval, one has

\[
                         s+d\le j+q-1,
 qquad                  t\ge j.
\]

Hence the erosion support \([s+d,t]\) meets \([j,j+q-1]\), so \(x\in E_h\)
for some \(h\) in that block.  This proves (3.2a).  The lower inclusion in
(3.2b) is the mandatory-collar theorem, and the upper inclusion follows
because the cell lies in every owner window containing it.

For the converse, write

\[
                         F_h=\{\alpha_h,\beta_{h-d-1}\}.
\]

For every \(x\in S\), choose one \(h\in[j,j+q-1]\) with \(x\in E_h\), and
put \(x\) into the new letter at \(h\); also put all of \(F_h\) there.
This yields nonempty sets \(A_h\subseteq S\cap E_h\) whose block union is
\(S\).  Use \(A_h=E_h\) outside the block.

No extraneous owner coordinate is introduced.  If a required owner
occurrence of coordinate \(x\) were lost, all of its erosion suppliers in
one length-\((d+1)\) owner window would lie inside the pinned block, which
has length at most \(d\), and all would omit \(x\).  The supplier interval
cannot then avoid both of its global endpoints: otherwise it contains the
whole owner window, of length \(d+1\), inside a block of length at most
\(d\).  At an erosion-support endpoint, however, \(x\) is respectively the
forced arrival \(\beta_{h-d-1}\) or forced departure \(\alpha_h\), and so
belongs to \(F_h\subseteq A_h\), a contradiction.  The modified letters
therefore remain a factor. \(\square\)

Theorem 3.1A defines a canonical carrier-only bipartite graph: a lower
target \(S\) is adjacent to a physical slot \((j,q)\) precisely when
\(K_{j,q}\subseteq S\subseteq E_{j,q}\).  Every edge is individually
realizable, while every simultaneous lower compiler must be a matching in
this graph.  Hence all of its Hall cuts are genuine integral rotor
obstructions; the only information they omit is interference among several
simultaneous block pins.

### Theorem 3.2 (exact simultaneous-pin criterion)

Let \(J\subseteq\mathbb Z_W\), and prescribe nonempty \(S_j\) satisfying
(0.9).  Put

\[
 A_j=\begin{cases}S_j,&j\in J,\\E_j,&j\notin J,
 \end{cases}                                             \tag{3.2}
\]

and, for each coordinate \(x\),

\[
 Z_x=\{j:x\in E_j,\ j\notin J\text{ or }x\in S_j\}. \tag{3.3}
\]

Then (3.2) is a depth-\(d\) factor of \((T_i)\) if and only if

\[
 [i,i+d]\cap Z_x\ne\varnothing
 \qquad(i\in\mathbb Z_W,\ x\in T_i).                 \tag{3.4}
\]

In particular, (3.4) is automatic if distinct positions of \(J\) have
cyclic distance at least \(d+1\).

### Proof

Every \(A_j\subseteq E_j\), so no extraneous coordinate is introduced.
For fixed \((i,x)\), the right side of (3.4) says exactly that at least one
of the \(d+1\) source positions of owner window \(i\) still supplies
\(x\).  This is necessary and sufficient for (0.2).

For one pin, (0.9) is sufficient.  Indeed, if deleting
\(x\in E_j-S_j\) destroyed an owner occurrence, the erosion support of
that coordinate would meet one length-\((d+1)\) window only at \(j\).
That makes \(j\) one of the two support endpoints, so \(x\) is respectively
\(\alpha_j\) or \(\beta_{j-d-1}\), contrary to (0.9).  If selected
positions are \((d+1)\)-separated, every owner window contains at most one
pin, and the one-pin argument applies independently. \(\square\)

## 4. The exact singleton gate

Let \(X\subseteq[k]\) be the coordinates whose singleton targets must be
supplied by the cyclic factor, and define

\[
 P_x=\{j:\alpha_j=\beta_{j-d-1}=x\}.                 \tag{4.1}
\]

Thus \(P_x\) is the set of terminal positions of minimum positive
\(x\)-runs.

### Corollary 4.1 (necessary labelled minimum runs)

If the factor contains the singleton value \(\{x\}\), then \(P_x\ne
\varnothing\).  Consequently exact coverage of all singleton targets in
\(X\) requires

\[
                         |P_x|\ge1\qquad(x\in X).     \tag{4.2}
\]

This is stronger than the scalar inequality
\(\sum_x|P_x|\ge|X|\): the run label must agree with the target label.

### Corollary 4.2 (separated singleton-packing theorem)

If

\[
               |P_x|\ge(2d+1)(|X|-1)+1
                    \qquad(x\in X),                  \tag{4.3}
\]

then there are positions \(p_x\in P_x\), one for every \(x\in X\), whose
pairwise cyclic distances are at least \(d+1\).  Pinning

\[
                         A_{p_x}=\{x\}                \tag{4.4}
\]

and taking \(A_j=E_j\) elsewhere is a literal factor realizing all
singleton targets in \(X\) simultaneously.

### Proof

Choose the positions greedily.  Each previously chosen position forbids at
most \(2d+1\) cyclic positions for the next coordinate.  Bound (4.3)
therefore leaves an available candidate at every step.  The selected pins
are separated, and Theorem 3.2 applies. \(\square\)

### Corollary 4.3 (one equivariant minimum run closes the singleton orbit)

Suppose

\[
                         W=kN,
 \qquad T_{i+N}=\rho^vT_i,                            \tag{4.5}
\]

where \(\rho\) is the cyclic rotation of the \(k\) coordinates and
\(\gcd(v,k)=1\).  If one quotient position \(j\) has

\[
                         \alpha_j=\beta_{j-d-1}=x,   \tag{4.6}
\]

then the \(k\) positions

\[
                         j,j+N,\ldots,j+(k-1)N       \tag{4.7}
\]

are minimum-run positions labelled respectively by

\[
                         x,\rho^vx,\ldots,
                         \rho^{(k-1)v}x.             \tag{4.8}
\]

If \(N\ge d+1\), the maximal erosion factor may therefore be pinned
simultaneously by

\[
                  A_{j+\ell N}=\{\rho^{\ell v}x\}
                  \qquad(0\le\ell<k),               \tag{4.9}
\]

and these \(k\) source letters realize every singleton target exactly once.

#### Proof

Taking set differences in (4.5) gives

\[
 \alpha_{i+N}=\rho^v\alpha_i,
 \qquad
 \beta_{i+N}=\rho^v\beta_i.                         \tag{4.10}
\]

Iterating (4.6) and (4.10) proves (4.7)--(4.8).  Coprimality makes the
labels in (4.8) the complete coordinate orbit.  Consecutive positions in
(4.7), including the cyclic last-to-first gap, have distance \(N\); hence
\(N\ge d+1\) makes them pairwise admissibly separated.  Apply Theorem 3.2
with the singleton pins (4.9). \(\square\)

Thus, on a coprime-voltage strict spiral, the complete rank-one lower row
does **not** require \(k\) unrelated local repairs.  Its exact remaining
carrier gate is only

\[
 \boxed{\text{produce one positive quotient run of length exactly }d+1.}
                                                               \tag{4.11}
\]

This statement concerns the singleton row only; the same orbit pins still
have to coexist with the higher lower-target assignment, upper decks and
the terminal compiler.

## 5. Linear words and additive sidecars

For a linear factor \(A_1,\ldots,A_{W+d}\), the same proof gives

\[
 F_j=
 (\{\alpha_j\}\text{ when }j\le W-1)
 \cup
 (\{\beta_{j-d-1}\}\text{ when }j\ge d+2).          \tag{5.1}
\]

There are exactly \(2(d+1)\) boundary positions at which only one of the
two terms is present.  Every other one-coordinate-capable position is the
terminal position of a minimum run of length \(d+1\).  Therefore a linear
word whose central factor must supply \(s\) distinct singleton targets
satisfies

\[
 \boxed{\#\{\text{internal minimum runs of length }d+1\}
                  \ge s-2(d+1).}                    \tag{5.2}
\]

If \(C\) extra sidecar cells are allowed to supply singleton targets
directly, the right side weakens by at most \(C\).

For \(d=3\), (5.1)--(5.2) recover the authenticated eight-boundary and
minimum-four-run theorem.  The new content here is the arbitrary-depth
form, the all-\(q\) collar identity (0.5), and the exact separated
simultaneous-pinning consequence.

## 6. Consequence for integral coloured-rotor fusion

The stationary pull-clock theorem constructs same-owner rational
circulations and proves the required rank marginals.  It has no selected
one-copy owner order, hence no physical transition labels
\((\alpha_i,\beta_i)\).  Equations (0.3)--(0.5) show that those labels are
not dispensable bookkeeping: they force literal subsets inside every
physical lower cell.  In particular, rank-one exactness forces the labelled
minimum-run transversal (4.2).

Thus denominator clearing, an aggregate age-semigroup rounding, or an
owner/target matching which forgets the lag-\((d+1)\) collars cannot prove
one-copy rotor fusion.  A valid positive theorem must choose jointly:

1. the owner/coatom Johnson order;
2. its minimum and near-minimum run bank;
3. the target-to-cell matching inside the mandatory intervals
   \(K_{j,q}\subseteq S\subseteq E_{j,q}\); and
4. the simultaneous run-hitting constraints of Theorem 3.2.

This is a sharp invariant obstruction to rounding the proved stationary
fractional trace circulation *as such*.  It does not rule out a global
moving-core construction, and it does not prove or disprove
\(\nu(k)=B(k)+O(1)\).
