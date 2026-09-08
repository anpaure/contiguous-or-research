# Catalan two-rail switches: exact Hall--SCC criterion and the Aharoni--Haxell barrier

Date: 2026-07-31  
Status: proved conditional matching theorems and sharp abstract obstructions;
the all-dimension existence hypothesis is not proved

## 0. Result and scope

Throughout let \(m\ge2\), and put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname {Cat}_m .
\]

For a fixed saturating cycle and a fixed cap-two host injection, the
one-of-two switch problem in
`MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md`
is exactly a labelled perfect-matching problem with two options per omitted
facet.  It has an exact implication-graph criterion.  There are also two
genuine coefficient-one Hall sufficient conditions, one using an
endpoint-safe orientation schedule and one using cyclically nonadjacent
hosts.

After fixing the \(K\)-block host bank and its residual palette, the direct
Aharoni--Haxell route is structurally incapable of certifying the exact
Catalan transversal: on the full family its matching number is at most
\(K\), whereas the rank-two and rank-three Aharoni--Haxell hypotheses
demand respectively more than \(2(K-1)\) and \(3(K-1)\).  This fails for
every \(K\ge2\), hence for every \(m\ge2\).  This capacity argument does
not rule out an augmented construction that keeps all \(N=mK\) hosts live
and encodes the signed palette equations simultaneously.

Under the additional hypothesis that the complete split lower-colour
multiset already has profile \(1^{N-K}2^K\), the exact matching graph has
maximum degree two on both shores.  Its only choices are alternating flips
on even cycles, and the opposite-cut condition is an exact 2-SAT instance
on those cycle bits.  This lower-floor hypothesis is additional: cap two on
the upper blocks does not imply it.

Nothing below proves protected upper shadows, connectivity, residence, or
the common compiler.  Those remain separate from this lower-q1 switch gate.

## 1. Exact local data

Write the saturating cycle cyclically as

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0,             \tag{1.1}
\]

where the \(U_i\) are all \((m+1)\)-sets, the \(C_i\) are distinct
\(m\)-sets, and \(C_i,C_{i+1}\subset U_i\).  Put

\[
 {\cal E}=\binom{[2m]}m\setminus\{C_i:i\in\mathbb Z_N\},
 \qquad |{\cal E}|=K,                                    \tag{1.2}
\]

and let

\[
 {\cal L}=\binom{[2m]}{m-1},\qquad
 b_i=C_i\cap C_{i+1}.                                    \tag{1.3}
\]

Thus \(|{\cal L}|=N\).  The Catalan identities used below are exact:

\[
 M=(m+1)K,\qquad N=mK.                                   \tag{1.4}
\]

If \(X\in{\cal E}\) is hosted in \(U_i\), its two records are

\[
\begin{array}{c|c|c}
 \sigma&\text{retained lower colour }\lambda_{Xi}^{\sigma}
       &\text{opposite cut endpoint }J_i^{\sigma}\\ \hline
 0&X\cap C_{i+1}&C_i\\
 1&X\cap C_i&C_{i+1}.
\end{array}                                               \tag{1.5}
\]

The two retained colours in one hosted block are distinct.  Indeed write

\[
 C_i=U_i\setminus\{p\},\quad
 C_{i+1}=U_i\setminus\{q\},\quad
 X=U_i\setminus\{c\}.
\]

The three facets are distinct, so \(p,q,c\) are distinct, and the two
colours are \(U_i\setminus\{c,p\}\) and
\(U_i\setminus\{c,q\}\).

## 2. A joint signed provider formulation

The following formulation is useful because it does not presuppose a good
host bank or a good cap-two injection.

For every legal record \((X,i,\sigma)\), meaning \(X\subset U_i\), introduce
\(x_{Xi\sigma}\in\{0,1\}\).  For \(L\in{\cal L}\), write

\[
 d_L=|\{i:b_i=L\}|.                                      \tag{2.1}
\]

### Theorem 2.1 (exact joint switch system)

There is a host injection and a one-of-two choice satisfying the complete
rainbow condition (2.2) of the two-rail reduction if and only if the
following integral system is feasible:

\[
 \sum_{i,\sigma:X\subset U_i}x_{Xi\sigma}=1
       \qquad(X\in{\cal E}),                              \tag{2.2}
\]

\[
 \sum_{X,\sigma}x_{Xi\sigma}\le1
       \qquad(i\in\mathbb Z_N),                           \tag{2.3}
\]

\[
 \sum_{X,i,\sigma:J_i^\sigma=C_j}x_{Xi\sigma}\le1
       \qquad(j\in\mathbb Z_N),                          \tag{2.4}
\]

and

\[
 d_L-
 \sum_{X,i,\sigma:b_i=L}x_{Xi\sigma}
 +\sum_{X,i,\sigma:\lambda_{Xi}^\sigma=L}x_{Xi\sigma}
 =1
       \qquad(L\in{\cal L}).                             \tag{2.5}
\]

There are exactly \(2mK\) record variables and \(K+3N=(3m+1)K\)
displayed rows.

#### Proof

Every \(m\)-set has exactly \(m\) containing \((m+1)\)-sets in
\([2m]\), and the \(U_i\) enumerate them all.  Each legal host has two
sides, giving \(2mK\) records.  Equations (2.2) choose one hosted side for
each omitted facet; (2.3) is precisely host injectivity; and (2.4) is
precisely distinctness of the opposite cuts.

Before hosting, block \(i\) contributes the default marked lower colour
\(b_i\).  Hosting and switching that block removes this default
contribution and replaces it by the retained colour
\(\lambda_{Xi}^{\sigma}\).  Hence the left side of (2.5) is the exact
final multiplicity of \(L\).  Requiring it to be one for every \(L\) is
the disjoint-union identity in (2.2) of the reduction.  This proves both
directions. \(\square\)

The signed rows (2.5) explain why the raw problem is not an ordinary
unstructured matching before the unmatched-block palette is fixed.

## 3. Fixed host injection: exact labelled matching and 2-SAT

Fix an injection

\[
 \phi:{\cal E}\longrightarrow\{U_i:i\in\mathbb Z_N\},
 \qquad X\subset\phi(X),                                  \tag{3.1}
\]

and put \(H=\operatorname{im}\phi\), identifying \(H\) with its block
indices.

The \(N-K\) unavoidable colours

\[
 F_\phi=\{b_i:i\notin H\}                                 \tag{3.2}
\]

must be pairwise distinct.  If they are not, no switch can repair their
repetition because their blocks are unmatched.  When they are distinct,
put

\[
 D_\phi={\cal L}\setminus F_\phi,\qquad |D_\phi|=K.       \tag{3.3}
\]

Build a bipartite graph \(A_\phi\) with shores \({\cal E}\) and
\(D_\phi\).  For \(X\) hosted in \(U_i\), retain the edge

\[
 X\lambda_{Xi}^{\sigma}
\]

exactly when \(\lambda_{Xi}^{\sigma}\in D_\phi\), and label that edge by
\(J_i^\sigma\).  Every left degree is at most two.

### Theorem 3.1 (exact labelled-perfect-matching criterion)

The fixed injection \(\phi\) admits a valid split-switch choice if and only
if \(A_\phi\) has a perfect matching whose \(J\)-labels are pairwise
distinct.

#### Proof

A valid switch chooses one retained colour at every \(X\).  The fixed
colours already occupy \(F_\phi\), so every chosen colour must lie in
\(D_\phi\).  The \(K\) choices are pairwise distinct if and only if they
form a perfect matching from \({\cal E}\) to the \(K\)-set \(D_\phi\).
The edge label is exactly the opposite endpoint cut on the unmarked rail,
so simultaneous switch legality is exactly label distinctness. \(\square\)

### Corollary 3.2 (exact implication-SCC criterion)

Give each \(X\) one Boolean variable for its side.  Add

1. a unit clause forbidding side \(\sigma\) whenever
   \(\lambda_{Xi}^{\sigma}\notin D_\phi\); and
2. for any two distinct targets and sides whose records have equal retained
   colour or equal \(J\)-label, the clause forbidding those two sides
   simultaneously.

Then \(\phi\) admits a valid switch if and only if this 2-CNF is
satisfiable, equivalently if and only if no literal and its complement lie
in the same strongly connected component of its implication digraph.

#### Proof

Exactly one side is represented by the Boolean value of each target.  The
unit clauses remove precisely the colours already occupied by fixed blocks.
The binary clauses are precisely the two possible failures of Theorem 3.1:
a repeated retained colour or a repeated opposite cut.  The final statement
is the standard implication-graph characterization of 2-SAT. \(\square\)

There is additional cyclic structure.  Write a side bit as zero when its
cut points to the left endpoint \(C_i\) of block \(i\), and one when it
points to the right endpoint \(C_{i+1}\).  For two consecutive hosted
blocks \(i,i+1\), the only endpoint collision is the pattern \(10\) at
their common endpoint \(C_{i+1}\).  Since \(K<N\), the hosted blocks split
into linear cyclic runs, and the endpoint-safe words on every run are
exactly

\[
                         0^*1^*.                          \tag{3.4}
\]

Thus an implication bicycle, not marginal endpoint Hall, is the exact
remaining obstruction after \(\phi\) is fixed.

## 4. The fixed-bank Aharoni--Haxell capacity barrier

The fixed-injection provider family for \(X\) is the graph

\[
 {\cal P}_X=\{\{\lambda,J\}:X\lambda\in E(A_\phi)\}.      \tag{4.1}
\]

The rank-two Aharoni--Haxell theorem would require

\[
 \nu\!\left(\bigcup_{X\in S}{\cal P}_X\right)
                    >2(|S|-1)                            \tag{4.2}
\]

for every nonempty \(S\subseteq{\cal E}\).  For
\(S={\cal E}\), however,

\[
 \nu\!\left(\bigcup_X{\cal P}_X\right)\le|D_\phi|=K.    \tag{4.3}
\]

For \(K\ge2\), (4.3) cannot be strictly larger than \(2(K-1)\).

The same barrier survives if only a host bank \(H\), \(|H|=K\), with
distinct outside default colours is fixed and the injection is co-designed.
Put \(D_H={\cal L}\setminus\{b_i:i\notin H\}\), and for every omitted
facet define the 3-uniform typed family

\[
 {\cal G}_X(H)=
 \left\{
   \{i,\lambda_{Xi}^{\sigma},J_i^\sigma\}:
   i\in H,\ X\subset U_i,\ \lambda_{Xi}^{\sigma}\in D_H,\
   \sigma\in\{0,1\}
 \right\}.                                               \tag{4.4}
\]

### Proposition 4.1 (exact fixed-bank hypergraph)

There is a co-designed host injection with image \(H\) and a valid switch
if and only if the families \(({\cal G}_X(H):X\in{\cal E})\) have a
disjoint transversal.

#### Proof

The three resources of a record are its host block, retained lower colour,
and opposite cut.  Disjointness in the first shore gives a host injection;
because \(K\) records use a \(K\)-set \(H\), its image is all of \(H\).
Disjointness in the second shore gives all \(K\) elements of \(D_H\), and
disjointness in the third gives distinct opposite cuts.  These conditions
are also plainly necessary. \(\square\)

Thus a record uses the three typed resources

\[
       (i,\lambda_{Xi}^{\sigma},J_i^\sigma)\in
       H\times D_H\times\{C_j\},                          \tag{4.5}
\]

with \(X\) as the family index.  A disjoint transversal is exactly the
desired host, retained-colour, and cut choice.  Its full union has matching
number at most \(|H|=|D_H|=K\), whereas rank-three Aharoni--Haxell asks for
more than \(3(K-1)\).  This too is impossible for every \(K\ge2\).

More quantitatively, the shore cap \(K\) allows (4.2) for a serviced
subfamily of size \(s\) only if

\[
 K>2(s-1),\qquad s\le\lceil K/2\rceil.                   \tag{4.6}
\]

The rank-three form similarly permits at most

\[
                         s\le\lfloor(K+2)/3\rfloor.       \tag{4.7}
\]

Consequently a single direct Aharoni--Haxell stage followed by an
\(o(K)\)-sized absorber cannot solve this zero-slack problem: it leaves a
linear-in-\(K\) residue.  This does not rule out a genuinely iterative
absorber with changing resources.

The qualification “fixed bank” is essential.  If all \(N=mK\) blocks are
left available, the raw host shore has size \(N\), so the bound
\(\nu\le K\) used above is no longer valid.  On the other hand, raw
host/lower/cut triples are not yet equivalent to the switch problem:
selecting a host also deletes its default colour \(b_i\), exactly as in the
signed equation (2.5).  No Aharoni--Haxell encoding of that larger signed
system is proved or refuted here.

For reference, before host-bank filtering the record catalogue has the
following exact upper bounds:

\[
 |{\cal G}^{\rm raw}_X|=2m,\quad
 \deg(i)\le2(m-1),\quad
 \deg(L)\le\binom{m+1}{2},\quad
 \deg(C_j)\le2(m-1),                                     \tag{4.8}
\]

and typed pair codegrees

\[
 \deg(i,L)\le1,qquad
 \deg(i,C_j)\le m-1,qquad
 \deg(L,C_j)\le2.                                       \tag{4.9}
\]

#### Proof of (4.8)--(4.9)

A fixed \(X\) has exactly \(m\) one-element extensions in \([2m]\), and
each host has two sides.  A block \(U_i\) has \(m+1\) middle facets, of
which \(C_i,C_{i+1}\) are not omitted; hence it supports at most
\(m-1\) possible \(X\)'s and at most \(2(m-1)\) records.

A fixed cut \(C_j\) is an endpoint only of blocks \(j-1,j\).  In each
block the cut fixes the side and leaves at most \(m-1\) possible omitted
facets, proving its degree bound and also
\(\deg(i,C_j)\le m-1\).

For a fixed lower colour \(L\), there are
\(\binom{m+1}{2}\) upper sets \(U\supset L\).  In a fixed block
\(U_i\), write \(U_i\setminus L=\{a,b\}\).  A record retaining \(L\)
must delete one of \(a,b\) to form its retained seam facet and the other to
form \(X\).  There is at most one such omitted \(X\): if both deletion
labels \(a,b\) were the two boundary labels, the resulting \(X\) would be
one of \(C_i,C_{i+1}\), not an omitted facet.  This proves both
\(\deg(i,L)\le1\) and the stated bound on \(\deg(L)\).  Finally a pair
\((L,C_j)\) can arise only in blocks \(j-1,j\), at most once in each, so
its codegree is at most two.  \(\square\)

These bounds do not overcome (4.3).

## 5. Positive coefficient-one expansion theorems

### Theorem 5.1 (Hall plus matching-proper cut labels)

Suppose \(F_\phi\) is distinct and

\[
 |N_{A_\phi}(S)|\ge|S|\qquad(S\subseteq{\cal E}).         \tag{5.1}
\]

For a cut label \(J\), let \(A_\phi[J]\) be the subgraph consisting of
edges carrying that label.  If

\[
                  \nu(A_\phi[J])\le1\qquad\text{for every }J,             \tag{5.2}
\]

then a valid switch exists.

#### Proof

Hall's theorem gives a perfect matching of \(A_\phi\).  If it used one
label twice, the two equally labelled matching edges would form a
two-edge matching in \(A_\phi[J]\), contradicting (5.2).  Theorem 3.1
finishes the proof. \(\square\)

Since a fixed \(J=C_j\) can occur only from the two blocks incident with
\(C_j\), its label class has at most two edges.  Thus (5.2) is local: when
two such records exist, it says that they share their retained-colour
endpoint.  A crude degree-only sufficient form of (5.1) is

\[
 0<\max_{d\in D_\phi}\deg(d)
       \le\min_{X\in{\cal E}}\deg(X),                     \tag{5.3}
\]

because edge counting gives
\(|N(S)|\ge \min_X\deg(X)|S|/\max_d\deg(d)\).

### Theorem 5.2 (oriented-bank Hall theorem)

Fix a host bank \(H\subseteq\mathbb Z_N\), \(|H|=K\), for which the
unmatched colours \(b_i\), \(i\notin H\), are distinct, and put

\[
 D_H={\cal L}\setminus\{b_i:i\notin H\}.                 \tag{5.4}
\]

Suppose there are

1. an endpoint-safe side schedule \(\epsilon:H\to\{0,1\}\), equivalently
   a threshold word \(0^*1^*\) on every consecutive run of \(H\);
2. a bijection \(\psi:{\cal E}\to D_H\) with
   \(\psi(X)\subset X\) for every \(X\); and
3. Hall expansion in the bipartite graph \(B_{\psi,\epsilon}\) from
   \({\cal E}\) to \(H\), where

\[
 X\sim i
 \quad\Longleftrightarrow\quad
 X\subset U_i\ \text{ and }\
 \lambda_{Xi}^{\epsilon_i}=\psi(X):
 \qquad
 |N_{B_{\psi,\epsilon}}(S)|\ge|S|\quad(S\subseteq{\cal E}).              \tag{5.5}
\]

Then a valid split-switch choice exists.

#### Proof

Hall gives a containment bijection \(\phi:{\cal E}\to H\).  Its retained
colours are the prescribed bijection \(\psi\), hence exactly \(D_H\).
The threshold condition makes the opposite endpoints pairwise distinct.
The fixed colours outside \(H\) together with \(D_H\) are exactly
\({\cal L}\). \(\square\)

### Corollary 5.3 (independent-host Hall theorem)

Suppose a containment injection \(\phi:{\cal E}\to\{U_i\}\) has a host
set \(H\) containing no two cyclically consecutive blocks.  If
\(F_\phi\) is distinct and the retained-colour graph \(A_\phi\) satisfies
Hall (5.1), then a valid switch exists.

#### Proof

The possible cut labels in block \(i\) are \(C_i,C_{i+1}\).  These
two-element sets are disjoint for nonconsecutive blocks, so every perfect
matching of \(A_\phi\) is automatically label-rainbow. \(\square\)

There is no cardinality obstruction to an independent bank:
\(N=mK\) and therefore

\[
                         K\le\lfloor N/2\rfloor
                         \qquad(m\ge2).                   \tag{5.6}
\]

Containment, distinct unmatched colours, and (5.1), however, are not
implied by this count.

## 6. Extra lower-floor hypothesis: alternating paths and cycles

Assume now, in addition to cap two on the upper blocks, that the complete
split \(C\)-rail lower-colour multiset has exact profile

\[
                         1^{N-K}2^K.                      \tag{6.1}
\]

Let \(D^{(2)}\subseteq{\cal L}\) be its \(K\) duplicated colours.  At a
hosted \(X\), switching cuts the edge \(XJ\).  Build the **cut graph**
\(A_\phi^{\rm cut}\) with shores \({\cal E}\) and \(D^{(2)}\), putting an
edge \(Xq\), labelled \(J\), when

\[
                         q=X\cap J\in D^{(2)}.             \tag{6.2}
\]

### Theorem 6.1 (degree-two alternating-component criterion)

The cut graph satisfies

\[
 \deg(X)\le2,qquad \deg(q)\le2,qquad
 |\{e:\operatorname{label}(e)=J\}|\le2.                 \tag{6.3}
\]

The lower palette can be repaired if and only if
\(A_\phi^{\rm cut}\) has a perfect matching.  Equivalently every path
component has positive even order and has its two endpoints on opposite
shores; in particular, there are no isolated vertices.  Every such balanced
path has a unique perfect matching and every even cycle has exactly two
alternating perfect matchings.

After fixing the path matchings and giving each cycle one alternating-state
bit, repeated \(J\)-labels produce only fixed contradictions, unit clauses,
or binary clauses between cycle states.  Conditional on the preceding
path-balance condition, a full split-switch exists if and only if this
2-CNF has no cycle bit and its complement in one implication SCC.

#### Proof

The full rail has \(K\) colours of multiplicity two and all other colours
of multiplicity one.  Cutting one marked edge at each of the \(K\) hosted
facets leaves every colour once exactly when the cut colours are the
elements of \(D^{(2)}\), once each.  This is a perfect matching in the cut
graph.  Each \(X\) has two incident split edges.  Each duplicated colour has
only two physical occurrences in the full rail, so its cut-graph degree is
at most two.  A seam endpoint \(C_j\) is incident with only blocks
\(j-1,j\), proving the label bound.

A bipartite graph of maximum degree two is a disjoint union of paths and
even cycles.  A path has a perfect matching precisely when its shores are
balanced, and that matching is unique; a cycle has its two alternating
matchings.  Every label collision is a forbidden pair of component states,
which gives the asserted 2-CNF.  The SCC criterion is exact by 2-SAT.
\(\square\)

The alternating-cycle flips in this theorem are the exact augmenting moves;
no generic hypergraph absorber is needed after (6.1) is available.

## 7. Sharp obstructions and audit calibration

### 7.1 Marginal expansion is insufficient

Even with two legal sides per task, maximum resource degree two, pair
codegree one, and all three pairwise projections Hall-positive, the joint
choice may fail.  An abstract three-task table is

\[
\begin{array}{c|cc}
 &0&1\\ \hline
 X_1&(v_0,a)&(v_1,b)\\
 X_2&(v_1,c)&(v_2,b)\\
 X_3&(v_2,c)&(v_3,a).
\end{array}                                               \tag{7.1}
\]

The first coordinate is the cut endpoint and the second the retained
colour.  The colour-rainbow words are exactly \(010,101\), whereas the
endpoint-injective words along the three-block run are exactly
\(000,001,011,111\).  Their intersection is empty.  Every two-task
subinstance is feasible.

This is a sharp labelled-incidence obstruction to marginal Hall,
degree, or codegree criteria.  It is **not** asserted to be realized by
Boolean deletion labels: adjacent Johnson blocks impose additional
same-side intersection restrictions.  Those restrictions, or an exact SCC
argument exploiting them, are what an all-dimension proof must use.

Even in the abstract degree-two regime of Section 6, lower Hall and
componentwise endpoint feasibility need not compose.  Five consecutive
host positions with component pattern \(A,B,A,B,A\) can have alternating
state words

\[
 A:(1,0,1)\leftrightarrow(0,1,0),\qquad
 B:(0,0)\leftrightarrow(1,1).                             \tag{7.2}
\]

Writing their state bits as \(a,b\), the combined host word is

\[
                         (1-a,b,a,b,1-a).                 \tag{7.3}
\]

For the four assignments to \((a,b)\), a forbidden endpoint descent occurs
at one of the four successive boundaries.  This is precisely an implication
bicycle.  Again, (7.2) is an abstract labelled graph obstruction, not a
claimed Boolean-rail counterexample.

### 7.2 Verified physical \(m=3\) failure

The exact six-coordinate instance in
`MATH_AUDIT_CATALAN_RAINBOW_NOT_AUTOMATIC_K6_20260731.md` satisfies the
extra lower-floor profile (6.1), with

\[
 D^{(2)}=\{12,18,24,33,36\}.                              \tag{7.4}
\]

The hosted facet \(X=7\) has cut colours \(6,3\), and \(X=42\) has cut
colours \(34,10\).  Neither pair meets \(D^{(2)}\).  Thus both left vertices
are isolated in \(A_\phi^{\rm cut}\), and Hall fails before endpoint labels
are considered.  This is a physical counterexample only to the claim that
an arbitrary cap-two/lower-floor injection is automatically switchable; it
does not prove that the same saturating cycle has no better injection.

## 8. Exact remaining all-dimension lemma

The strongest proved replacement for the proposed Aharoni--Haxell step is:

> For every \(m\), construct a saturating cycle together with one host
> injection \(\phi\) for which the unmatched lower colours are distinct and
> the exact 2-CNF of Corollary 3.2 is satisfiable.

Either Theorem 5.1, Theorem 5.2, or Corollary 5.3 is a stronger sufficient
way to discharge that lemma.  Under the extra lower-floor hypothesis,
Theorem 6.1 reduces it to alternating-component bits and implication
bicycles.

What is now closed is the normalized black-box route: after fixing the
host bank or injection and its residual palette, direct Aharoni--Haxell,
separate marginal Hall conditions, and degree/codegree dispersion alone
cannot prove the exact zero-slack transversal.  An augmented all-\(N\)-host
signed construction is not excluded.  The concrete remaining route is
geometric expansion or bicycle exclusion for the actual deletion-label
incidence, followed independently by protected upper cuts, component
splicing, residence, and literal compiler compatibility.
