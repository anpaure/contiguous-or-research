# Root-port flag matchings: exact alternating switches, component coalescence, and the chronology gate

**Date:** 2026-07-27  
**Status:** exact packet-valid switch calculus and conditional component-coalescence theorem.  A fixed-carrier switch obstruction and the remaining global circuit/chronology conditions are proved.  Existence of enough positive zero-boundary circuits is not asserted.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad L_0=n-M=m-H,                    \tag{0.1}
\]

and let

\[
 \mathfrak F=\{(U,x):U\in\binom{[n]}M,\ x\in U\}.          \tag{0.2}
\]

The six-uniform root-port flag hypergraph has shores
\(\mathfrak F^+\sqcup\mathfrak F^-\).  Its edge associated with an
oriented three-top packet is given explicitly in (1.2) below.  A
near-perfect matching in this hypergraph gives, at each top, a directed
partial permutation: a disjoint union of directed paths and cycles.

This note proves the following facts.

1. The ordinary directed two-switch at one top is **not** itself a packet
   switch.  Replacing
   \[
   x\to y,\quad u\to v
   \qquad\hbox{by}\qquad
   x\to v,\quad u\to y                                  \tag{0.3}
   \]
   leaves four exact signed flag defects on four companion tops.  Their
   identities are (2.4).

2. A collection of such cells is a genuine global matching switch if and
   only if its signed companion boundary vanishes and its old/new packet
   shores are conformal.  This is Theorem 3.1.  Thus an “alternating
   cycle” must be a zero-boundary cycle in the packet complex, not merely
   an alternating cycle in one top's arc graph.

3. A cross two-switch between a directed path and a directed cycle merges
   them into one directed path while preserving the path's two holes.
   Consequently a supply of gain-positive zero-boundary circuits removes
   every directed cycle without consuming new flag holes; see Theorem 4.2.

4. Gain-positive circuits first merge cycle--cycle pairs and absorb every
   cycle at a top already having a path.  Any final top consisting of one
   cycle and no path is opened by deleting one selected packet.  At most
   \(N\) such deletions are needed, costing \(6N=o(MN)\) flags.  The total
   number of remaining path components is then bounded by the number of
   unmatched incoming flags, hence is \(o(MN)\) for a near-perfect flag
   matching.

5. Zero-boundary cycles do not merge two directed paths: the crossed
   switch only exchanges their suffixes.  Reaching exactly one trail per
   top additionally requires open augmenting packet chains which consume
   endpoint holes.  Their exact boundary is stated in (4.7).

6. The smallest exact four-label packet trade is rigid.  On a tetrahedral
   carrier there are exactly two flag-perfect packet states; they reverse
   every local triangle and have identical undirected direction graphs.
   They cannot merge components.  Hence the desired switches must use a
   growing, cross-cell carrier.

7. Even a one-path-per-top flag state need not possess one global packet
   chronology.  The local path orders induce a precedence digraph on
   packets, and a common chronology exists exactly when this digraph is
   acyclic.  Literal collar-neutral validity further requires the common
   core-order/gap test at every scheduled packet.  Neither condition is
   implied by flag matching or by zero flag boundary.

The result is therefore a sharp reduction.  Component coalescence is an
exact alternating-circuit problem with an explicit local generator.
What remains is to pack gain-positive zero-boundary circuits whose new
packet shores are conformal, precedence-acyclic, and compatible with one
common-core word chart.

## 1. Packets and the induced directed graphs

Let \(U\in\binom{[n]}M\), let \(x,y\in U\) be distinct, and let
\(a\notin U\).  Write

\[
 V_x=U-x+a,\qquad V_y=U-y+a.                              \tag{1.1}
\]

The oriented packet \(P_U(x,y;a)\) has the six flag resources

\[
 \boxed{
 \begin{aligned}
 P_U(x,y;a)=\{&
 (U,x)^+,(U,y)^-,\\
 &(V_x,y)^+,(V_x,a)^-,\\
 &(V_y,a)^+,(V_y,x)^-\}.
 \end{aligned}}                                           \tag{1.2}
\]

Indeed its common core is \(C=U-\{x,y\}\), and its three top transitions
are

\[
 U:x\longrightarrow y,\qquad
 C+ya:y\longrightarrow a,\qquad
 C+ax:a\longrightarrow x.                                \tag{1.3}
\]

Let \(\mathcal M\) be a flag matching.  At a fixed top \(U\), every
selected packet using \(U\) supplies one directed arc \(x\to y\).
Flag-disjointness says

\[
 d_U^+(x)\le1,\qquad d_U^-(x)\le1                         \tag{1.4}
\]

for every \(x\in U\).  Hence the selected arc graph \(D_U(\mathcal M)\)
is a disjoint union of directed paths, directed cycles, and isolated
labels.

If \(h_U^+\) and \(h_U^-\) are the numbers of uncovered outgoing and
incoming flags on \(U\), then they are equal, and the number of nontrivial
directed path components is at most \(h_U^+=h_U^-\).  Every directed
cycle consumes no hole.

## 2. The exact local two-switch and its counterboundary

Fix four distinct labels \(x,u,y,v\in U\) and one \(a\notin U\).  Define
the formal packet cell

\[
 \begin{aligned}
 \Delta(U;a;x,u\mid y,v)
 :=\;&P_U(x,y;a)+P_U(u,v;a)\\
    &-P_U(x,v;a)-P_U(u,y;a).
 \end{aligned}                                            \tag{2.1}
\]

The positive shore in (2.1) contains the old arcs
\(x\to y,u\to v\); the negative shore contains the crossed arcs
\(x\to v,u\to y\).

For a formal packet sum \(Z\), let

\[
 \partial^+Z,\qquad \partial^-Z                           \tag{2.2}
\]

be its signed outgoing- and incoming-flag incidence vectors.

### Lemma 2.1 (counterboundary identity)

The central \(U\)-flags in (2.1) cancel, and

\[
 \boxed{
 \begin{aligned}
 \partial^+\Delta={}&
 e^+_{(U-x+a,y)}-e^+_{(U-x+a,v)}\\
 &+e^+_{(U-u+a,v)}-e^+_{(U-u+a,y)},                       \tag{2.3}\\[1mm]
 \partial^-\Delta={}&
 e^-_{(U-y+a,x)}-e^-_{(U-y+a,u)}\\
 &+e^-_{(U-v+a,u)}-e^-_{(U-v+a,x)}.                       \tag{2.4}
 \end{aligned}}
\]

In particular, one projected two-switch is never an exact flag trade.

#### Proof

Use (1.2).  In the outgoing shore, the central flags \(x,u\) agree on
the two sides of (2.1).  The flags with port \(a\), on
\(U-y+a\) and \(U-v+a\), also agree.  The remaining four terms are
(2.3).  On the incoming shore, the central heads \(y,v\) agree, as do
the two flags with head \(a\) on \(U-x+a,U-u+a\); the four remaining
terms are (2.4). \(\square\)

Equations (2.3)--(2.4) are the exact counterterm omitted by a switch
performed only in \(D_U(\mathcal M)\).  The plus boundary is a
\(2\times2\) rectangle on the two replacement tops \(U-x+a,U-u+a\)
and ports \(y,v\).  The minus boundary is the transposed rectangle on
\(U-y+a,U-v+a\) and ports \(x,u\).

## 3. Zero-boundary circuits are exactly the packet-valid switches

A **cell circuit** is a finite signed sum

\[
 Z=\sum_{i=1}^s\epsilon_i
 \Delta(U_i;a_i;x_i,u_i\mid y_i,v_i),
 \qquad \epsilon_i\in\{+1,-1\}.                           \tag{3.1}
\]

After collecting coefficients, write

\[
 Z=\mathcal A-\mathcal B,                                 \tag{3.2}
\]

where \(\mathcal A,\mathcal B\) are nonnegative packet multisets with
disjoint support.

### Theorem 3.1 (global toggle lemma)

Let \(\mathcal M\) be a flag matching.  Suppose:

1. \(\partial^+Z=\partial^-Z=0\);
2. every packet of \(\mathcal A\) belongs to \(\mathcal M\);
3. the packets of \(\mathcal B\) are pairwise flag-disjoint and avoid
   every packet of \(\mathcal M\setminus\mathcal A\); and
4. all coefficients in \(\mathcal A,\mathcal B\) are one.

Then

\[
 \mathcal M'=(\mathcal M\setminus\mathcal A)\cup\mathcal B \tag{3.3}
\]

is a flag matching and covers exactly the same outgoing and incoming
flags as \(\mathcal M\).

Conversely, if two flag matchings differ by packet multisets
\(\mathcal A,\mathcal B\) and cover the same flags, then
\[
 \partial^+(\mathcal A-\mathcal B)
 =\partial^-(\mathcal A-\mathcal B)=0.                    \tag{3.4}
\]

#### Proof

The zero-boundary equations say coefficientwise that the old and new
packet shores use every signed flag equally often.  Conditions 2--4 turn
this equality of multisets into a conformal \(0\)-\(1\) replacement.
Thus (3.3) is a matching with the same covered flag set.  The converse
is immediate by subtracting the two incidence vectors. \(\square\)

The theorem distinguishes three notions which must not be conflated:

- a projected alternating cycle in one \(D_U\);
- an integral zero-boundary relation among packet columns; and
- a **conformal** zero-boundary relation which can actually be toggled
  from the present matching.

Only the third is a matching switch.

### Corollary 3.2 (rectangle-circuit test)

A sum of local cells (2.1) is packet-valid precisely when every signed
rectangle in (2.3) and every signed rectangle in (2.4) cancels
coefficientwise, followed by the conformality test in Theorem 3.1.

Thus the search for alternating switches is the intersection of two
ordinary integral circulation kernels, one on outgoing replacement
flags and one on incoming replacement flags.  The kernels are linear;
conformality is the nonlinear positivity condition.

## 4. What a valid circuit does to components

Let \(c_U(\mathcal M)\) be the number of nontrivial components of
\(D_U(\mathcal M)\), and put

\[
 \Phi(\mathcal M)=\sum_U c_U(\mathcal M).                 \tag{4.1}
\]

### Lemma 4.1 (path--cycle splice)

Suppose \(x\to y\) lies on a directed path and \(u\to v\) lies on a
different directed cycle of \(D_U(\mathcal M)\).  Replacing these arcs by
\(x\to v,u\to y\) produces one directed path on the union of the old
path and cycle.  It preserves the missing incoming flag at the beginning
of the old path and the missing outgoing flag at its end.  Hence
\[
 c_U\longmapsto c_U-1.                                    \tag{4.2}
\]

The same crossed switch merges two distinct directed cycles into one
directed cycle.

#### Proof

Deleting \(x\to y\) cuts the path into a prefix ending at \(x\) and a
suffix beginning at \(y\).  Deleting \(u\to v\) opens the cycle into a
path beginning at \(v\) and ending at \(u\).  The new arcs concatenate
these three pieces in the order
\[
 \text{old prefix}\;x\to v\;
 \text{opened cycle}\;u\to y\;\text{old suffix}.
\]
The cycle--cycle statement is identical after opening both cycles.
\(\square\)

A crossed switch on two different directed paths generally leaves two
paths, merely exchanging their suffixes.  It does not reduce the number
of holes or path components.

Call a conformal zero-boundary circuit **gain-positive** at
\(\mathcal M\) if, after all its local arc changes are collected,
\[
 \Phi(\mathcal M')<\Phi(\mathcal M).                      \tag{4.3}
\]

### Theorem 4.2 (conditional cycle elimination)

Let \(\mathcal M_0\) be a flag matching.  Suppose that whenever a top has
either two directed cycles, or one directed cycle and a directed path,
there is a conformal zero-boundary circuit whose toggle merges such a
pair, is gain-positive, and does not increase the total number of directed
path components.

Then finitely many toggles leave, at every top, either no directed cycle
or one directed cycle and no path.  Delete one selected packet from each
remaining cycle, counting a packet only once if it is chosen by several
tops.  At most \(N\) packet deletions are needed, they create at most
\(6N=o(MN)\) uncovered flags, and the resulting matching
\(\mathcal M_*\) has no directed cycle.  Moreover,
\[
 \sum_U c_U(\mathcal M_*)
 \le\sum_U h_U^-=\sum_U h_U^+.                            \tag{4.4}
\]

Consequently, if \(\mathcal M_0\) misses \(o(MN)\) flags, then after
seeding and switching,
\[
 \sum_U c_U(\mathcal M_*)=o(MN).                          \tag{4.5}
\]

#### Proof

Every gain-positive toggle decreases the nonnegative integer
\(\Phi\), so the switching procedure terminates.  Its terminal condition
has the stated form: a remaining cycle can coexist with neither a path
nor a second cycle.  Deleting one arc opens each such cycle into a path,
and deleting further arcs on companion tops cannot create a cycle.
Every nontrivial component is then a path,
and every path has a distinct uncovered incoming flag and a distinct
uncovered outgoing flag.  This proves (4.4).  Since \(N=o(MN)\), the
near-perfect estimate gives (4.5). \(\square\)

The theorem gives the exact useful target.  It is unnecessary to merge
different path components: their aggregate number is already bounded by
the flag leave.  The switches only need to absorb cycles into paths while
reusing the same holes.

### 4.1 Why cycles alone do not give one trail per top

Let \(A_1,A_2\) be two distinct directed paths and choose internal arcs
\(x\to y\) in \(A_1\), \(u\to v\) in \(A_2\).  Removing them and adding
\(x\to v,u\to y\) produces two directed paths: the prefix of \(A_1\)
is joined to the suffix of \(A_2\), and the prefix of \(A_2\) is joined
to the suffix of \(A_1\).  The number of paths and the four endpoint
holes are unchanged.

Thus every zero-boundary circuit preserves the total outgoing and incoming
hole sets and cannot, by local successor exchanges alone, force several
paths into one.  To concatenate a path ending at \(t\) with a path
beginning at \(h\), one must cover the two currently unused flags

\[
 (U,t)^+,\qquad (U,h)^-.                                  \tag{4.6}
\]

For packet multisets \(\mathcal A\subseteq\mathcal M\) and
\(\mathcal B\cap\mathcal M=\varnothing\), put
\(Z=\mathcal A-\mathcal B\) as before.  An **open augmenting chain**
for the two paths has boundary

\[
 \partial^+Z=
 -\sum_{\xi\in H^+_{\rm fill}}e^+_\xi
 +\sum_{\xi\in H^+_{\rm new}}e^+_\xi,\qquad
 (U,t)\in H^+_{\rm fill},
                                                                    \tag{4.7a}
\]

\[
 \partial^-Z=
 -\sum_{\xi\in H^-_{\rm fill}}e^-_\xi
 +\sum_{\xi\in H^-_{\rm new}}e^-_\xi,\qquad
 (U,h)\in H^-_{\rm fill}.                                \tag{4.7b}
\]

Here \(H^\pm_{\rm fill}\) are old holes covered by the new shore and
\(H^\pm_{\rm new}\) are newly created holes, possibly on companion tops.
If no new holes are created and
\(|\mathcal B|=|\mathcal A|+1\), this is an ordinary hypergraph
augmentation: it increases the matching by one packet and covers six
previous holes, three outgoing and three incoming.  More generally,
(4.7a)--(4.7b) transport hole pairs while concatenating focal paths.

Consequently the exact one-trail target has two stages:

1. zero-boundary gain-positive circuits eliminate directed cycles;
2. conformal open augmenting chains route and consume all but one endpoint
   pair at each retained top.

A near-perfect six-uniform matching supplies only \(o(MN)\) total holes.
It does not imply that every top has at most one hole pair; two holes on
every top already cost only \(2N=o(MN)\).  Hence the first stage proves
the aggregate \(o(MN)\) component target, while the literal one-trail
claim needs a separate endpoint-routing theorem.

## 5. The smallest carrier does not merge components

The natural first candidate is a tetrahedral four-label switch.  It is
rigid.

Fix an \((M-3)\)-set \(B\) and four labels
\(\{1,2,3,4\}\cap B=\varnothing\).  Let
\[
 T_i=B+\bigl(\{1,2,3,4\}\setminus\{i\}\bigr)              \tag{5.1}
\]
be the four tops.  For each \(i\), a packet with core \(B+i\) is an
oriented cycle on the other three labels and uses exactly the three tops
\(T_j\), \(j\ne i\).

### Proposition 5.1 (tetrahedral rigidity)

There are exactly two packet matchings which cover all \(24\) signed
flags \((T_i,x)^\pm\), \(x\in T_i\setminus B\), using only packets in
this four-label cell.  They reverse all four packet orientations.
At every \(T_i\), both states have the same three undirected direction
edges, namely the complete triangle on \(T_i\setminus B\).  Therefore the
unique tetrahedral toggle changes no component count.

#### Proof

Four packets are required.  Let \(k_i\) be the number whose core is
\(B+i\).  Top \(T_j\) is used by every core type except \(j\), so flag
coverage gives
\[
 \sum_{i\ne j}k_i=3\quad(j=1,2,3,4),\qquad
 \sum_i k_i=4.
\]
Hence \(k_i=1\) for every \(i\).

At a top \(T_j\), the three incident packets supply the three edges
opposite their core labels.  Covering every outgoing and incoming flag
once forces these three arcs to be a directed triangle rather than a
transitive tournament.  Once one packet orientation is fixed, this
condition propagates uniquely across the four tops and fixes the other
three orientations.  Reversing every orientation gives the second
solution.  These are the only two, and reversal does not change the
underlying direction edges. \(\square\)

Thus no composition confined to disjoint tetrahedral cells can coalesce
the direction components created by those cells.  The switch carrier
must cross cell boundaries and grow with \(m\).

## 6. Global chronology is a separate exact condition

Assume all directed cycles have been removed.  Every top now has one or
more directed packet paths.  Along each path, consecutive arcs prescribe
an order on their packet events.  Let \(\mathcal P\) be the selected
packet set and define its **precedence digraph**
\[
 \mathscr D(\mathcal P)                                   \tag{6.1}
\]
as follows: its vertices are packets, and \(P\to Q\) is an edge whenever
the arc of \(P\) immediately precedes the arc of \(Q\) on one top path.

### Theorem 6.1 (chronology criterion)

The local top paths admit one common linear packet chronology if and only
if \(\mathscr D(\mathcal P)\) is acyclic.

#### Proof

Any common chronology must respect every immediate top-path precedence,
so a directed cycle is impossible.  Conversely, if
\(\mathscr D(\mathcal P)\) is acyclic, any topological ordering respects
every path order and is the required common chronology. \(\square\)

An alternating toggle can reduce \(\Phi\) and still create a directed
cycle in \(\mathscr D\).  Therefore a switch used in Theorem 4.2 is
**chronology-safe** only if the new precedence digraph remains acyclic.
A sufficient local certificate is that all changed packets occupy one
interval of an existing topological order and the new path pieces admit
an order inside that interval compatible on every touched top.

There is one further physical condition.  At the scheduled time of
\[
 P_U(x,y;a),                                               \tag{6.2}
\]
the three current cyclic words on
\[
 U,\quad U-x+a,\quad U-y+a                               \tag{6.3}
\]
must have the same deleted-core order and the same two admissible
insertion gaps.  This is the literal \(\omega/\eta/\eta\) source test.
The flag boundary records only \(x\to y,y\to a,a\to x\); it does not
record (6.3).

Hence a zero-boundary circuit preserves packet validity at three
successively stronger levels:

1. **flag-valid:** Theorem 3.1;
2. **chronology-valid:** Theorem 6.1 after the toggle;
3. **word-valid:** every new packet passes (6.3) in that chronology.

Only the third level is a literal coefficient-one packet switch.

## 7. Exact remaining merging theorem

The fixed-six near-perfect matching settles flag supply but not the
following assertion.

> **Gain-positive circuit packing (GPCP).**  Starting from a near-perfect
> root-port flag matching after \(O(N)\) path-seeding deletions, every
> remaining directed cycle belongs to a conformal cell circuit \(Z\)
> satisfying:
>
> 1. \(\partial^+Z=\partial^-Z=0\);
> 2. toggling \(Z\) decreases \(\Phi\) and creates no new path component;
> 3. the new precedence digraph is acyclic; and
> 4. the new packets possess a common-core word chart at their scheduled
>    times.

Under GPCP, Theorems 3.1, 4.2, and 6.1 give a packet family with
\[
 \sum_Uc_U=o(MN),                                         \tag{7.1}
\]
one common global chronology, and literal root-port recurrence.  If the
flag leave is distributed with one incoming/outgoing hole on almost every
top, the same argument gives one long directed trail on almost every top.

For the unconditional one-trail conclusion one additionally needs:

> **Endpoint-pair routing (EPR).**  Whenever a retained top has two
> directed path components, there is a conformal open chain
> (4.7a)--(4.7b) which concatenates them, preserves at least one endpoint
> pair on that top, does not increase the total path count elsewhere, and
> remains chronology- and word-valid.

GPCP plus EPR reduces every retained top to one directed path, except for
the \(o(N)\) tops deliberately discarded with the flag leave.

What the present note rules out is the tempting shortcut:
\[
 \text{near-perfect six-uniform matching}
 +\text{independent per-top two-switches}.                 \tag{7.2}
\]
Equation (2.4) shows the switches are not independent, Proposition 5.1
shows fixed tetrahedral cells cannot merge them, and Theorem 6.1 shows
that even flag-valid coalescence does not automatically produce a global
chronology.

The next constructive object must therefore be a growing-carrier packing
of the zero-boundary rectangle circuits (2.3)--(2.4), with positivity and
word-chart constraints built in from the start.
