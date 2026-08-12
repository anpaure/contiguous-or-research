# Reduced-scale short paths: exact endpoint degrees, the coloured H-queue circulation, and the long-component gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 H=\left\lfloor\sqrt{m\log\log m}\right\rfloor,
 \qquad M=m+H,
\]

\[
 W=\binom{2m}{m},\qquad
 N=N_H=\binom{2m}{m-H},\qquad
 \lambda={W\over N},
\tag{0.1}
\]

and take

\[
 r=\lfloor\lambda\rfloor,qquad t=r-1.
\tag{0.2}
\]

Then

\[
 \lambda=\log m+o(1),qquad
 r=\log m+O(1),qquad
 N=(1+o(1)){W\over\log m}.
\tag{0.3}
\]

This report settles the endpoint/circulation audit at this scale as
follows.

1. The reduced-scale rooted owner-path hypergraph has the exact degrees
   and codegrees already isolated in the independent short-path audit.
   Its attractive scalar satisfies

   \[
    (r+1){\Delta_2\over D_R}\log(W+N)
       =(4\log2+o(1)){\log m\over m}=o(1).
   \tag{0.4}
   \]

   This is **not** a published matching theorem. The genuine audited
   growing-uniformity condition contains

   \[
                 e^{2(r+1)}{\Delta_2\log D_R\over D_R}=o(1),
   \tag{0.5}
   \]

   whereas the left side is \(\Theta(\log D_R)\to\infty\) for the
   canonical floor choice. Thus even the supply of \(N-o(N)\)
   owner-disjoint short paths remains conditional on an object-specific
   nibble or absorber.

2. Before owner selection, the complete oriented short-path catalogue
   has a large exact endpoint degree. If \(P\) is a fixed
   \(t\)-transition geodesic, then the number of oriented
   \(t\)-transition geodesics \(Q\) which can follow \(P\) through one
   direct Johnson seam while the whole \((2t+1)\)-transition string
   remains geodesic is

   \[
       \boxed{D_t=(m-t)^2(m-t-1)_t^2.}
   \tag{0.6}
   \]

   Every such owner path has exactly

   \[
       \boxed{\rho_{m,H,t}={(m-t)!^2\over(m-H)!}}
   \tag{0.7}
   \]

   rooted full-frame decorations. Hence the decorated degree is
   \(D_t\rho_{m,H,t}\). For two paths with distinct terminal owners,
   the common decorated outdegree is at most

   \[
       (2m-2)(m)_t^2\rho_{m,H,t},
   \tag{0.8}
   \]

   and its ratio to (0.6)--(0.7) is at most
   \((2+o(1))/m\).

3. These complete-catalogue degrees do not survive projection to an
   arbitrary owner-disjoint selected family. Such a family can have
   zero endpoint degree. Even positive minimum degree plus (0.8) closes
   only explicitly bounded Hall cuts; it does not provide the large-cut
   or long-cycle theorem automatically.

4. More decisively, an ordinary endpoint cycle cover is the wrong
   physical object. Two adjacent \(r\)-owner blocks determine only

   \[
                         2r^2
   \tag{0.9}
   \]

   signed seam-crossing incidences, whereas one genuine radius-\(H\)
   seam belongs to

   \[
                         H(H+1)
   \tag{0.10}
   \]

   signed incidences. Their ratio tends to zero. There are three literal
   geodesic blocks for which both adjacent splices are geodesic, but a
   coordinate inserted in the first block is deleted in the third less
   than \(H\) transitions later. The resulting three-block word has a
   wrong-rank spanning trace. Thus pairwise-safe endpoint matching,
   even supplemented by a cycle voltage equation, is not an all-depth
   physical certificate.

5. The exact replacement is an ordered radius-\(H\) queue lift. Its
   states are

   \[
      (X;i_1,\ldots,i_H;d_1,\ldots,d_H),
   \tag{0.11}
   \]

   and its directed indegree and outdegree are both exactly

   \[
                         \boxed{(m-H)^2.}
   \tag{0.12}
   \]

   Every queue arc emits all its literal lower and upper targets through
   depth \(H\). This gives an exact coloured circulation formulation.
   However every middle owner has \((m)_H^2\) queue lifts. A regular
   queue cycle factor therefore does not produce an owner-simple,
   one-root physical section.

6. Voltage is an additional cycle coboundary, not a degree count. For a
   selected block permutation \(\pi\), one-pass zero monodromy is
   equivalent to

   \[
    \sum_{P\in\mathcal C}
       \bigl(\omega(P)+\omega(P,\pi(P))\bigr)=0
   \tag{0.13}
   \]

   on every selected cycle \(\mathcal C\), modulo only a declared
   stabilizer. Equivalently there must be one sheet potential per block.
   Raw endpoint degrees sum over voltage fibres and imply neither
   (0.13) nor the existence of those potentials.

7. Suppose conditionally that \(N-o(N)\) owner-disjoint \(r\)-paths have
   been supplied and an exact coloured queue circulation joins them into
   \(C\) components. The literal ledger is

   \[
      L_{\rm word}
      \le T+2HC+K_{\rm conn}+\mathfrak H,
   \tag{0.14}
   \]

   where \(T=(1+o(1))W\), \(K_{\rm conn}\) is declared connector
   installation length, and \(\mathfrak H\) is the complete remaining
   target-hole ledger. Consequently coefficient-one collar cost requires

   \[
       {N\over C}=\omega\!\left({H\over r}\right)
       =\omega\!\left({\sqrt{m\log\log m}\over\log m}\right).
   \tag{0.15}
   \]

   Constant-length direct seams cost only \(O(N)=o(W)\); an \(H\)-cost
   repair at every seam would be fatal.

8. There is an exact long-cycle obstruction. Let \(B_i\) be the largest
   number of atomic paths in any certified owner-simple, target-capacitated,
   zero-voltage radius-\(H\) cycle containing atom \(i\). Every physical
   cycle cover satisfies

   \[
                         \boxed{C\ge\sum_i{1\over B_i}.}
   \tag{0.16}
   \]

   Hence short strongly connected classes, endpoint Hall failure, or a
   voltage-coset exclusion can rule out collar amortization exactly. A
   complementary two-switch theorem shows that a ledger-neutral,
   zero-voltage cross-cycle switch bank would merge down to the desired
   component scale with only \(O(N)=o(W)\) installation cost.

The decision is therefore sharp. Ordinary endpoint circulation is
rigorously insufficient. The surviving object is a voltage-resolved,
target-capacitated, owner-simple section of the ordered \(H\)-queue
circulation whose cycles contain on average
\(\omega(H/r)\) selected short paths. No theorem constructing that
section, and no global lower bound excluding it, is proved here.

## 1. Calibration and the owner-path supply audit

The exact ratio is

\[
 \lambda
 =\prod_{j=1}^{H}{m+j\over m-j+1}.
\tag{1.1}
\]

Taylor expansion gives

\[
 \log\lambda
 ={H^2\over m}
 +O\!\left({H^2\over m^2}+{H^4\over m^3}\right)
 =\log\log m+o(1).
\tag{1.2}
\]

The floor error in \(H\) is \(O(H/m)=o(1/\log m)\), and the error in
(1.2), after multiplication by \(\log m\), still tends to zero. Hence

\[
                         \lambda=\log m+o(1),
\tag{1.3}
\]

which proves (0.3).

For reference, the simple rooted short-path hypergraph has one root and
\(r\) consecutive promotion owners in every edge. Its physical
presentation multiplicity is

\[
                 \mu_r=2(H-r+1)!(m-r+1)!.
\tag{1.4}
\]

Its root and owner degrees are

\[
 D_R={M!\over\mu_r},
 \qquad
 D_O={r(m!)^2\over(m-H)!\mu_r},
 \qquad
 {D_O\over D_R}={r\over\lambda}=:\rho.
\tag{1.5}
\]

For owners \(X,Y\) at Johnson distance \(d\),

\[
 {d(X,Y)\over D_O}
 =
 \begin{cases}
 \displaystyle {2(r-d)\over r\binom md^2},&1\le d<r,\\[2mm]
 0,&d\ge r.
 \end{cases}
\tag{1.6}
\]

The maximum is at \(d=1\), and

\[
 {\Delta_2\over D_R}
 ={2\rho(r-1)\over rm^2}
 ={2+o(1)\over m^2}.
\tag{1.7}
\]

Equations (1.4)--(1.7) are imported from the independently audited
reduced-scale short-path theorem. They also follow directly by recovering
the oriented owner path and observing the two invisible coordinate blocks
of sizes \(H-r+1\) and \(m-r+1\).

The scalar (0.4) now follows from

\[
 \log(W+N)=2m\log2+O(\log m).
\]

It is tempting, but invalid, to call (0.4) a variable-rank nibble
theorem. The audited ABKV condition is (0.5). Here

\[
 \log D_R=(1+o(1))H\log{m\over H},
 \qquad
 \log\log D_R=\left({1\over2}+o(1)\right)\log m.
\tag{1.8}
\]

For \(r=\lfloor\lambda\rfloor\),

\[
 2e^{-o(1)}\log D_R
 \le
 e^{2(r+1)}{\Delta_2\log D_R\over D_R}
 \le
 (2e^2+o(1))\log D_R.
\tag{1.9}
\]

Thus (0.5) fails. The same theorem's displayed residual factor is

\[
 (r+1)
 \left({\Delta_2\log(1+\Delta_2)\over D_R}\right)^{1/r}
 =(e^{-3/2}+o(1))\log m,
\tag{1.10}
\]

which is nonvanishing. Consequently all results below that begin with
\(N-o(N)\) owner-disjoint paths are explicitly conditional on a new
catalogue-specific matching theorem.

If such a matching has size \(N-s\), its exact uncovered middle-owner
count is

\[
                   W-r(N-s)=N(\lambda-r)+rs.
\tag{1.11}
\]

Thus \(s=o(N)\) would give \(o(W)\) owner leave with the correct floor
baseline.

## 2. Exact safe-splice criterion and complete-catalogue degree

An oriented \(t\)-transition Johnson geodesic is

\[
                   P=(B_0,B_1,\ldots,B_t).
\]

Put \(B=B_t\), and define its inserted and departed sets

\[
 I_P=B_t\setminus B_0\subset B,
 \qquad
 O_P=B_0\setminus B_t\subset B^c.
\tag{2.1}
\]

Both have size \(t\). Let

\[
                  Q=(C_0,C_1,\ldots,C_t)
\]

be another oriented \(t\)-geodesic, with

\[
 L_Q=C_0\setminus C_t,
 \qquad
 E_Q=C_t\setminus C_0.
\tag{2.2}
\]

Suppose the seam is

\[
                         C_0=B-x+y.
\tag{2.3}
\]

### Theorem 2.1 (exact two-block splice test)

The concatenation

\[
                  P,\ (B,C_0),\ Q
\]

is a Johnson geodesic of \(2t+1\) transitions if and only if

\[
 x\notin I_P,qquad y\notin O_P,
\tag{2.4}
\]

\[
 L_Q\cap(I_P\cup\{y\})=\varnothing,
 \qquad
 E_Q\cap(O_P\cup\{x\})=\varnothing.
\tag{2.5}
\]

#### Proof

A Johnson walk is geodesic precisely when all departure labels are
distinct, all arrival labels are distinct, and no label inserted during
the walk is later deleted. The first condition in (2.4) says that the seam
does not delete an earlier insertion; the second says that it does not
reinsert an earlier departure. The two conditions in (2.5) make the same
assertions for the transitions inside \(Q\). All remaining cross-pairs
are disjoint automatically because a departure of \(Q\) lies in \(C_0\)
and an arrival of \(Q\) lies outside \(C_0\). This proves necessity and
sufficiency. \(\square\)

### Corollary 2.2 (exact endpoint degree)

For fixed \(P\), the number of safe seam choices is

\[
                         (m-t)^2,
\tag{2.6}
\]

and the number of complete oriented \(Q\)'s satisfying Theorem 2.1 is

\[
                         D_t=(m-t)^2(m-t-1)_t^2.
\tag{2.7}
\]

#### Proof

There are \(m-t\) choices for
\(x\in B\setminus I_P\) and \(m-t\) choices for
\(y\in B^c\setminus O_P\). Once the seam is fixed, the allowed departure
alphabet of \(Q\) is

\[
 C_0\setminus(I_P\cup\{y\}),
\]

of size \(m-t-1\), and its allowed arrival alphabet has the same size.
Choose and order \(t\) distinct labels from each alphabet. The two ordered
lists uniquely determine \(Q\), proving (2.7). \(\square\)

### Lemma 2.3 (exact rooted decoration multiplicity)

Every fixed oriented \(t\)-geodesic has exactly

\[
                       \rho_{m,H,t}={(m-t)!^2\over(m-H)!}
\tag{2.8}
\]

full promotion-frame decorations with its phase interval and orientation
fixed.

#### Proof

The path intersection has size \(m-t\). Choose its root of size \(m-H\),
or equivalently choose the remaining \(H-t\) initial-window labels, in

\[
                         \binom{m-t}{H-t}
\]

ways. Order those \(H-t\) labels after the already forced \(t\) departure
labels, and order the \(m-t\) unused tail labels. The product is

\[
 \binom{m-t}{H-t}(H-t)!(m-t)!
 ={(m-t)!^2\over(m-H)!}.
\]

No further order is free. As a check, the exact double count is

\[
 W(m)_t^2\rho_{m,H,t}=NM!.
\tag{2.9}
\]

\(\square\)

Thus the complete decorated outdegree is

\[
                         D_t\rho_{m,H,t}.
\tag{2.10}
\]

This is an uncoloured, preselection degree. Different decorations of the
same owner path can have different deep histories, ports, and voltage.

## 3. Common endpoint neighbours and the loss under selection

Two distinct middle owners at Johnson distance at least three have no
common Johnson neighbour. At distance two they have exactly four; at
distance one they have exactly \(2(m-1)\).

Indeed, for distance two a common neighbour chooses one of the two
departures and one of the two arrivals. For adjacent owners with common
\((m-1)\)-set \(S\), a common neighbour is either

\[
 S-\{s\}+\{a,b\}\quad(s\in S)
\]

or

\[
 S\cup\{c\}\quad(c\notin S\cup\{a,b\}),
\]

giving \(2(m-1)\).

For a common start owner \(C\), the exact common number of future
\(t\)-geodesics for two histories is

\[
 \rho_{m,H,t}
 \bigl(m-|I\cup I'\cup\{y,y'\}|\bigr)_t
 \bigl(m-|O\cup O'\cup\{x,x'\}|\bigr)_t,
\tag{3.1}
\]

provided both seam tests hold, and zero otherwise. Summing over at most
\(2m-2\) common starts gives

\[
 \Delta_2^{\rm end}
 \le(2m-2)(m)_t^2\rho_{m,H,t}.
\tag{3.2}
\]

Together with (2.7)--(2.8),

\[
 {\Delta_2^{\rm end}\over D_t\rho_{m,H,t}}
 \le {2+o(1)\over m}.
\tag{3.3}
\]

The restriction to distinct terminal owners is essential. Parallel
history or decoration clones with one terminal owner may have almost the
same neighbourhood.

Now freeze an owner-disjoint family \(\mathcal F\) of physical paths.
At most one member of \(\mathcal F\) begins at a prescribed middle owner,
so two terminal owners have at most \(2m-2\) common outneighbours inside
\(\mathcal F\). There is nevertheless no unconditional lower bound on a
terminal's degree: (2.10) counts paths outside \(\mathcal F\), and the
selected start-owner set may avoid its whole Johnson neighbourhood.

There is a useful exact small-cut consequence if a separate argument
provides minimum degree. Suppose a subgraph retains exactly \(d\)
outneighbours at every left vertex and every two left vertices have at
most \(c=2m-2\) common neighbours. For \(X\) on the left, write \(a_v\)
for the number of edges from \(X\) to \(v\in N(X)\). Then

\[
 \sum_va_v=d|X|,
 \qquad
 \sum_v\binom{a_v}{2}\le c\binom{|X|}{2}.
\]

Cauchy--Schwarz gives

\[
 \boxed{
 |N(X)|\ge
 { |X|d^2\over d+c(|X|-1)}.}
\tag{3.4}
\]

Thus Hall holds for

\[
 |X|\le1+{d^2-d\over2m-2}.
\tag{3.5}
\]

At the independent-density benchmark \(d\asymp m^2/r\), this closes cuts
only through order \(m^3/r^2\), still negligible beside the exponential
number \(N\) of selected paths. Endpoint transitivity before selection
therefore does not settle the selected large cuts.

## 4. The projected endpoint and voltage circulation

Condition on a finite family of atomic paths indexed by \(i\in I\). Let
\(\mathcal O_i\) be its allowed orientations or local shores. For an
oriented atom \((i,a)\), let \(\mathcal E^+(i,a)\) and
\(\mathcal E^-(i,a)\) be its declared outgoing and incoming seam options.
Use binary variables

\[
 z_{i,a},\qquad y_e.
\]

The endpoint degree equations are

\[
 \sum_{a\in\mathcal O_i}z_{i,a}=1,
\tag{4.1}
\]

\[
 \sum_{e\in\mathcal E^+(i,a)}y_e=z_{i,a}
 =\sum_{e\in\mathcal E^-(i,a)}y_e.
\tag{4.2}
\]

An integral solution is exactly an oriented directed cycle cover of the
atoms in the **projected pairwise endpoint graph**. If every component is
required to contain at least \(L\) atoms, add

\[
 \sum_{e\in\delta^+(S)}y_e\ge1
 \qquad
 (\varnothing\ne S\subset I,\ |S|<L).
\tag{4.3}
\]

For a cycle cover, (4.3) is necessary and sufficient: a component of
size below \(L\) violates its own cut, while a set smaller than \(L\)
cannot be a union of components when all components have size at least
\(L\).

### Voltage

Let the deck-voltage group be \(G\), written additively. Give an oriented
atom an internal voltage \(\omega(i,a)\), and a seam \(e:(i,a)\to(j,b)\)
a voltage \(\omega(e)\). A selected base cycle \(\mathcal C\) is one-pass
zero-monodromy precisely when

\[
 \sum_{(i,a)\in\mathcal C}\omega(i,a)
 +\sum_{e\in\mathcal C}\omega(e)=0.
\tag{4.4}
\]

Equivalently, there are sheet potentials \(g_{i,a}\in G\) such that on
every selected seam

\[
 g_{j,b}=g_{i,a}+\omega(i,a)+\omega(e).
\tag{4.5}
\]

The implication from (4.5) to (4.4) follows by telescoping; conversely,
choose one potential on each cycle and propagate it. If a declared
stabilizer \(K\le G\) is allowed, replace zero by membership in \(K\), or
work in \(G/K\).

An unrestricted circulation on the full sheet lift is not enough: it may
project several sheet laps onto one nonzero-voltage base cycle. Exact
one-pass lifting chooses one sheet copy of each selected oriented atom and
enforces (4.5).

Equations (4.1)--(4.5) are still only a projection. They know neither the
radius-\(H\) transition history nor the seam-crossing target loads.

## 5. Exact crossing colours and the failure of pairwise safety

Consider one direct seam which deletes \(x\) and inserts \(y\). For a
window using \(s\) transitions on the left, the seam, and \(u\)
transitions on the right, put

\[
                         s+u+1=q.
\tag{5.1}
\]

Let \(D_s^-\) and \(E_s^-\) be the sets of the last \(s\) departures and
arrivals before the seam, and let \(D_u^+\) and \(E_u^+\) be the first
\(u\) departures and arrivals after it. If the whole window is geodesic,
its literal targets are

\[
 \boxed{
 \Phi^-_{q,s}
 =B\setminus(E_s^-\cup\{x\}\cup D_u^+),}
\tag{5.2}
\]

\[
 \boxed{
 \Phi^+_{q,s}
 =B\cup D_s^-\cup\{y\}\cup E_u^+.}
\tag{5.3}
\]

They have ranks \(m-q\) and \(m+q\). These formulas are a seam ledger,
not merely an endpoint label.

Two adjacent \(r\)-owner blocks contain \(2r\) owner positions. The number
of \(q\)-transition windows crossing their seam and contained in those
two blocks is

\[
 n_q=
 \begin{cases}
 q,&1\le q\le r,\\
 2r-q,&r<q\le2r-1,\\
 0,&q\ge2r.
 \end{cases}
\tag{5.4}
\]

Therefore the number of signed incidences determined by the two-block
pair is

\[
                 2\sum_qn_q=2r^2.
\tag{5.5}
\]

In a long radius-\(H\) word, one interior seam belongs to \(q\) windows
of depth \(q\). Its complete signed incidence count is

\[
                 2\sum_{q=1}^Hq=H(H+1).
\tag{5.6}
\]

At the present scale,

\[
 {2r^2\over H(H+1)}
 =O\!\left({(\log m)^2\over m\log\log m}\right)=o(1).
\tag{5.7}
\]

Most crossing targets therefore depend on a chain of
\(\Theta(H/r)\) endpoint choices.

### Theorem 5.1 (three-block obstruction to pairwise endpoint circulation)

For all sufficiently large \(m\), there are three rooted, fully
decorable oriented \(t\)-geodesic blocks \(P_0,P_1,P_2\) and two direct
seams such that:

1. \(P_0\), its seam, and \(P_1\) form a geodesic of \(2t+1\)
   transitions;
2. \(P_1\), its seam, and \(P_2\) form a geodesic of \(2t+1\)
   transitions;
3. the complete three-block concatenation is not radius-\(H\) safe and
   has a wrong-rank spanning trace.

Consequently no system consisting only of pairwise endpoint legality,
degree equations, subtour cuts, and cycle-total voltage equations is an
exact all-depth physical formulation.

#### Proof

Since \(t=O(\log m)\) and \(H/\log m\to\infty\), one has

\[
                         t+4<H
\tag{5.8}
\]

for all sufficiently large \(m\). Start with an arbitrary middle owner.
Use fresh departure and arrival labels for every transition below except
for one label \(z\). Insert \(z\) on the last transition of \(P_0\).
Keep it throughout the first seam, all transitions of \(P_1\), and the
second seam. Delete \(z\) on the first transition of \(P_2\). Fill every
other transition of the three blocks and both seams with mutually fresh
labels. There is ample room because only \(O(t)\) labels are prescribed.

The first two-block concatenation sees the insertion of \(z\) but no
later deletion, and all its other labels are fresh; it is geodesic. The
second two-block concatenation begins with \(z\) already present, sees its
single deletion but no insertion, and is likewise geodesic. Thus both
seams pass Theorem 2.1.

Across all three blocks, however, \(z\) is inserted and then deleted
within \(t+4<H\) transitions. In the spanning interval, one nominally
new arrival is also a later departure. Its union has one fewer element
than a geodesic interval of the same length, and the corresponding
intersection/union trace fails the required rank. Each individual
\(t\)-geodesic is promotion-decorable by Lemma 2.3. This proves the
claim. \(\square\)

The obstruction is geometric and precedes PBBS authorization. It does
not assert that the three particular blocks belong to a narrower PBBS
trade bank. It proves that pairwise endpoint data, even when accompanied
by an independently satisfied voltage equation, cannot certify the
literal all-depth word.

## 6. The exact ordered H-queue lift

Let \(\mathcal Q_H\) have states

\[
 q=(X;i_1,\ldots,i_H;d_1,\ldots,d_H),
\tag{6.1}
\]

where

\[
 X\in\binom{[2m]}m,
\]

the \(i_j\)'s are distinct elements of \(X\), and the \(d_j\)'s are
distinct elements of \(X^c\). They record, from oldest to newest, the
labels inserted and deleted in the last \(H\) transitions.

For

\[
 x\in X\setminus\{i_1,\ldots,i_H\},
 \qquad
 y\in X^c\setminus\{d_1,\ldots,d_H\},
\tag{6.2}
\]

there is an arc to

\[
 \bigl(X-x+y; i_2,\ldots,i_H,y; d_2,\ldots,d_H,x\bigr).
\tag{6.3}
\]

### Theorem 6.1 (queue regularity and exact colours)

The queue digraph has

\[
               W(m)_H^2
\tag{6.4}
\]

states and is exactly \((m-H)^2\)-in-regular and
\((m-H)^2\)-out-regular. Its arc (6.2)--(6.3) emits, for every
\(1\le q\le H\),

\[
 L_q
 =X\setminus\bigl(\{i_{H-q+2},\ldots,i_H\}\cup\{x\}\bigr),
\tag{6.5}
\]

\[
 U_q
 =X\cup\{d_{H-q+2},\ldots,d_H\}\cup\{y\},
\tag{6.6}
\]

where the historical set is empty for \(q=1\). These have exact ranks
\(m-q\) and \(m+q\). A middle-owner walk lifts to \(\mathcal Q_H\) if and
only if every interval of at most \(H\) transitions is geodesic; after
one initial queue is fixed, the lift is unique.

#### Proof

The state count is immediate. Equation (6.2) leaves \(m-H\) choices on
each side, proving the outdegree. Reversing (6.3) gives the same number
of predecessors, proving the indegree.

For a window of \(q\) transitions ending with the displayed arc, the
last \(q-1\) inserted labels were absent at the beginning of the window,
so they and the final departure \(x\) are absent from the intersection.
This is (6.5). Dually, the last \(q-1\) departed labels and the final
arrival \(y\) occur in the union, giving (6.6). The queue exclusions make
all these labels distinct, so the ranks are exact.

Conversely, if every \(H\)-transition interval is geodesic, its last
\(H\) arrivals lie in the current owner and its last \(H\) departures lie
outside it, with both lists injective. They define (6.1), and every next
transition obeys (6.2). Uniqueness is forced by the chronological lists.
\(\square\)

The number of outgoing queue walks of length \(r\) from a fixed state is

\[
                         (m-H)^{2r}.
\tag{6.7}
\]

This regularity yields a cycle factor of the complete queue state space,
but that is not the required physical selection. Every middle owner has
exactly \((m)_H^2\) queue-state lifts. The physical rows require, among
other things,

* at most one selected occurrence of each middle owner;
* the prescribed rooted short-path occurrences;
* one legal shore or orientation per selected atom;
* target capacities for every value in (6.5)--(6.6);
* all port, resource, and voltage rows.

Parallel queue contexts over one owner can have almost identical
neighbourhoods. Projecting a regular queue factor to owners therefore
destroys the low-codegree conclusion. This is the exact
history-lift/physical-section gate.

## 7. Exact coloured circulation and whole-seam ledger

There are two equivalent exact formulations.

### 7.1 State-expanded circulation

Take the product of \(\mathcal Q_H\) with the finite automaton which
records:

1. the selected atomic path and its current internal position;
2. its allowed orientation or shore;
3. physical provenance and port state;
4. the deck sheet or one-pass sheet potential.

Every transition variable is linked diagonally to its atom-selection
variable. Impose:

\[
 \hbox{flow conservation and indegree/outdegree at most one,}
\tag{7.1}
\]

\[
 \hbox{one selected automaton route for every selected atom,}
\tag{7.2}
\]

\[
 \hbox{owner, root, port, carrier, exclusivity, and resource rows,}
\tag{7.3}
\]

\[
 \mu^-_{q,T}
 =\sum_{e:L_q(e)=T}z_e,qquad
 \mu^+_{q,T}
 =\sum_{e:U_q(e)=T}z_e,
\tag{7.4}
\]

with the required capacities or explicit defect variables, and the
one-pass potential equations (4.5). Equation (7.4) includes every
crossing window; there is no separate seam projection.

To demand components of at least \(L\) atomic paths, impose the projected
cuts (4.3), or retain an atom counter in the state-expanded subtour rows.

### 7.2 Component-closed master columns

Alternatively, let one column be one complete certified queue cycle. It
records every atom, owner, root, queue arc, target in (6.5)--(6.6), port,
voltage, seam, and connector cost of that cycle. Select component-disjoint
columns, cover every required atom once, and impose all resource and target
rows. This formulation is exponentially large but integral and literal by
definition. It is the safe whole-packet form of the same circulation.

Pairwise variables (4.1)--(4.2) are only the projection of either exact
system. Theorem 5.1 proves that this projection has spurious integral
points.

## 8. Exact component and literal-cost theorem

Let \(\mathcal F\) be a family of pairwise owner-disjoint atomic paths.
Write \(w_i\) for the number of principal middle positions in atom \(i\),
and put

\[
                         T=\sum_iw_i.
\tag{8.1}
\]

Let an integral solution of Section 7 have \(C\) output components,
total connector installation length \(K_{\rm conn}\), and complete
missing-target count \(\mathfrak H\).

### Theorem 8.1 (literal compilation of a coloured queue circulation)

The selected solution emits a literal word of length

\[
 \boxed{
 L_{\rm word}
 \le T+2HC+K_{\rm conn}+\mathfrak H.}
\tag{8.2}
\]

If \(|\mathcal F|=(1+o(1))N\), \(w_i=r+O(1)\), every component has at
least

\[
 L={H\over r}\,\omega_m
 \qquad(\omega_m\to\infty)
\tag{8.3}
\]

atoms, \(K_{\rm conn}=o(W)\), and \(\mathfrak H=o(W)\), then

\[
                         L_{\rm word}=W+o(W).
\tag{8.4}
\]

#### Proof

Open each selected queue cycle once and emit its principal atom routes and
declared connectors. Repeating at most the first \(2H\) queue positions
exposes every cyclic lower and upper interval through depth \(H\). All
internal seam targets are already in (7.4). Append each remaining target
once. This proves (8.2).

The number of components is at most \(|\mathcal F|/L\). Hence

\[
 2HC
 \le {2H|\mathcal F|\over L}
 ={2r|\mathcal F|\over\omega_m}
 ={2+o(1)\over\omega_m}W=o(W).
\tag{8.5}
\]

Also \(T=W+o(W)\) under the conditional near-perfect owner supply, by
(1.11). The remaining hypotheses now give (8.4). \(\square\)

In particular, one \(O(1)\)-length connector per atom costs

\[
                         O(N)=O(W/\log m)=o(W).
\tag{8.6}
\]

More generally, average connector cost \(o(r)\) is harmless. What is not
harmless is paying an \(H\)-collar or \(\Theta(H)\) new holes at every
one of the \(N\) internal seams.

## 9. Positive fusion by certified two-switch descent

Suppose an exact coloured queue cycle cover contains arcs

\[
                         i\to i',\qquad j\to j'
\]

on two distinct components. Call the pair **fully fusible** when replacing
them by

\[
                         i\to j',\qquad j\to i'
\tag{9.1}
\]

has all of the following certified properties:

1. both new seams lift to the ordered \(H\)-queue and all newly spanning
   windows emit the declared targets;
2. the complete owner, root, port, carrier, and resource rows remain
   legal;
3. the change in total cycle voltage is zero, or is cancelled by a
   declared ledger-neutral seam variant;
4. the total new target-hole-plus-repeat defect is at most \(\delta\);
5. the added implementation length is at most \(\kappa\).

### Theorem 9.1 (correlated component descent)

Fix \(L\ge1\). Suppose every certified cover with more than
\(|\mathcal F|/L\) components contains a fully fusible cross-component
pair. Then repeated switches produce a certified cover with

\[
                         C\le{|\mathcal F|\over L}
\tag{9.2}
\]

after fewer than \(|\mathcal F|\) switches. The total added
implementation length is less than \(\kappa|\mathcal F|\), and the total
declared target defect is less than \(\delta|\mathcal F|\).

In particular, at the reduced scale, if \(\kappa,\delta=O(1)\) and
\(L=(H/r)\omega_m\), the switch costs and the collar in Theorem 8.1 are
all \(o(W)\).

#### Proof

A directed two-switch between two distinct cycles merges them into one
directed cycle. Full fusibility preserves every other constraint by
hypothesis, so each step decreases the number of components by one. Fewer
than \(|\mathcal F|\) steps are possible. Summing the two declared costs
proves the result, and

\[
 O(|\mathcal F|)=O(N)=o(W).
\]

\(\square\)

This is a genuine integral packet theorem. Its unproved hypothesis is the
positive-density supply of cross-cycle, full-history fusible switches.
Greedy improvement by uncoloured endpoint energy is not enough.

## 10. The harmonic long-cycle obstruction

For an atom \(i\), let \(B_i\) be the maximum number of atoms in a
certified owner-simple, target-capacitated, zero-voltage queue cycle which
contains \(i\). Put \(1/B_i=+\infty\) if no such cycle exists.

### Theorem 10.1 (component harmonic bound)

Every certified cycle cover satisfies

\[
                         \boxed{C\ge\sum_i{1\over B_i}.}
\tag{10.1}
\]

More generally, let \(w_i>0\) be the principal literal mass of atom
\(i\), and let \(B_i^{\rm lit}\) be the maximum principal mass of a
certified cycle containing \(i\). Then

\[
                         \boxed{C\ge\sum_i{w_i\over B_i^{\rm lit}}.}
\tag{10.2}
\]

#### Proof

Let \(Q\) be one component of a certified cover. Since \(Q\) itself is
an admissible cycle containing each \(i\in Q\),

\[
                         B_i\ge|Q|.
\]

Therefore

\[
                         \sum_{i\in Q}{1\over B_i}\le1.
\]

Sum over components to obtain (10.1). If
\(w(Q)=\sum_{i\in Q}w_i\), then
\(B_i^{\rm lit}\ge w(Q)\) for every \(i\in Q\), so

\[
 \sum_{i\in Q}{w_i\over B_i^{\rm lit}}
 \le {1\over w(Q)}\sum_{i\in Q}w_i=1.
\]

This proves (10.2). \(\square\)

Consequences include the following.

* If a positive fraction of the atomic mass has
  \(B_i=O(H/r)\), then \(C=\Omega(W/H)\). The standard independent
  radius-\(H\) opening budget is then \(\Omega(W)\), so this architecture
  cannot obtain an \(o(W)\) collar by component amortization.
* If an atom lies in no certified zero-voltage cycle, then the exact
  circulation is infeasible.
* If the physical endpoint/queue graph has closed strongly connected
  classes of circumference \(O(H/r)\) on positive atom mass, (10.1)
  gives the same obstruction.
* If every projected cycle through an atom has voltage in a coset which
  excludes zero modulo the permitted stabilizer, then \(B_i=0\).

Injective \(2H\)-memory alone forces a direct cycle to have at least
\(\Omega(H/r)\) atoms. That is only the constant-factor scale. Coefficient
one needs the strict strengthening \(\omega(H/r)\), exactly as in
(0.15).

## 11. Precise proved and conditional boundary

### Proved

1. The reduced calibration \(\lambda=\log m+o(1)\) and
   \(N=(1+o(1))W/\log m\).
2. The exact short-path degree and codegree ledger (1.4)--(1.7), including
   the attractive scalar (0.4).
3. Failure of the genuine audited ABKV condition and nonvanishing of its
   displayed residual factor.
4. The exact two-block safe-splice criterion, endpoint degree (0.6), and
   decoration multiplicity (0.7).
5. The distinct-endpoint common-neighbour bound (0.8), the selected-family
   small-cut estimate (3.4), and the absence of any inherited minimum
   degree after selection.
6. The exact projected endpoint/subtour/one-pass-voltage equations.
7. The full crossing-colour formulas (5.2)--(5.3), the incidence ratio
   (5.7), and the literal three-block counterexample to pairwise
   endpoint sufficiency.
8. The exact ordered \(H\)-queue lift, its degree (0.12), and all-depth
   target emission.
9. The literal long-component sufficiency theorem, the fully fusible
   two-switch descent theorem, and the harmonic component obstruction.

### Not proved

1. A matching of \(N-o(N)\) rooted short paths. The favourable static
   degrees do not satisfy the currently audited published
   growing-uniformity theorem.
2. A positive minimum endpoint degree, large-cut Hall theorem, or long
   cycle cover after the paths have been selected owner-disjointly.
3. An owner-simple, one-root section of the regular \(H\)-queue factor.
4. One-pass voltage cancellation on a long selected queue cycle bank.
5. Target capacities with aggregate all-depth holes and repeats \(o(W)\).
6. A full-history fusible two-switch bank satisfying Theorem 9.1.
7. Coefficient one.

The exact remaining gate is:

> Construct a target-capacitated, owner-simple, voltage-resolved section
> of the ordered \(H\)-queue circulation which uses the required rooted
> short paths and whose average component contains
> \(\omega(H/\log m)\) atoms; or prove through (10.1) that every such
> section has too many short certified cycles.

Ordinary endpoint degrees and ordinary zero-monodromy cycle equations do
not solve this gate, because the missing information spans
\(\Theta(H/\log m)\) consecutive atom choices.
