# AD17: negative-interval diagonal braids and the cyclic-comb obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact outcome

This report attacks the proposed in-place replacement of a cut cluster of
baseline length \(S\) by one literal word of length \(S+O(H)\). The input is
the exact negative-interval description of the depth-\(H\) erosion word.

The outcome has a positive and a negative part.

1. If a coordinate has a maximal positive owner run \([\alpha,\beta]\),
   then its positions in the depth-\(H\) erosion word are exactly

   \[
      [\alpha,\beta-H].
   \]

   Thus long runs have honest erosion intervals and short runs have empty,
   or reversed, intervals. The usual erosion--dilation identities recover
   exactly the coordinates belonging to long runs; the entire defect is the
   short-run support.

2. A reversed interval cannot be inserted into an unchanged baseline
   position while retaining all canonical owner intervals. More exactly,
   if the owner \(X_i\) must still be represented by the fixed word interval
   \([i-H,i]\), every coordinate written at position \(p\) must lie in all
   owners \(X_p,\ldots,X_{p+H}\). Hence every such letter is contained in
   the old erosion letter. Circularizing the baseline does not change this
   obstruction.

3. There is nevertheless a genuine global rerouting theorem. Along the
   east-before-south Pareto path, let the time support of each coordinate be
   decomposed into intervals. If these support intervals are proper
   (their left and right endpoints can be ordered simultaneously), then all
   floor-correct lower intersections and all consecutive upper owner unions
   in the chart have one literal word of length

   \[
      \boxed{
      \frac{\tau+B_0}{2}+\mathbf 1_{C\ne\varnothing}
      \ \le\
      \frac{T+B_0}{2}+\mathbf 1_{C\ne\varnothing}},
      \tag{0.1}
   \]

   where \(T\) is the number of Pareto edges, \(\tau\le T\) is the number
   of edges on which the intersection letter actually changes, \(C\) is the
   common core, and \(B_0\) counts support components meeting exactly one
   end of the path.
   For an actual-cut cluster of span \(S\), \(T=2(H+S-1)\). For the
   virtual-cut chart which also restores the deleted negative erosion
   prefixes,

   \[
      \boxed{T=2(S+2H-2).}                         \tag{0.2}
   \]

   Thus the upper bound in (0.1) is \(S+O(H)\) when \(B_0=O(H)\).

4. The proper-support hypothesis can be localized. Cut the Pareto path
   into proper-support cells. An internal support crossing any number of
   cut vertices costs only one additional token: all intermediate full-cell
   restrictions are absorbed into the cell cores. If
   \(C_{\rm hit}(Q)\) counts internal closed supports meeting at least one
   cut vertex, counted once per support, then

   \[
      \boxed{
      |Z_Q|\le
      \frac T2+\frac{B_0}{2}+C_{\rm hit}(Q)
      +2(|Q|+1).}                                  \tag{0.3}
   \]

   This gives an exact, directly testable positive gate for a blockwise
   coefficient-one fusion.

5. The gate is not automatic. For every \(R\ge5\) and
   \(m\ge2R-3\), there is a cyclic rank-\((m+1)\) Johnson trajectory of
   length \(S=2R\), with integral vertex-simple odd-graph lift and globally
   two-sided-rainbow first band, for which every arbitrary linear or
   circular literal word covering the owners and the first two lower bands
   has length at least

   \[
      \boxed{2R+\left\lceil\frac R3\right\rceil
      =S+\left\lceil\frac S6\right\rceil.}         \tag{0.4}
   \]

   All noncore coordinate runs in this example are reversed for growing
   \(H\). Taking \(R=\lfloor m/4\rfloor\) gives \(S\gg H=A\sqrt m\) and
   still satisfies the multi-cut corridor \(3H+S\le m+1\) for all large
   \(m\). Thus there is no universal \(S+O(H)\) diagonal or circular
   compiler based only on Johnson legality, floor correctness, the
   negative-interval characterization, first-band rainbowness, and the
   corridor inequality.

The precise open boundary is PBBS-specific. The obstruction is not shown
to occur with positive density in the canonical PBBS factor, while the
proper-cell statistic in (0.3) is not shown to be \(o(W)\) there. Therefore
this report neither claims coefficient one nor refutes it. It proves the
strongest general compiler found in this lane and a sharp local obstruction
to removing its support-order hypothesis.

## 1. Literal words and owner runs

Let \(\Omega\) be a finite ground set. A literal OR word is a finite sequence

\[
   Z=(Z_1,\ldots,Z_L),\qquad
   \varnothing\ne Z_j\subseteq\Omega.
\]

It represents \(A\subseteq\Omega\) if \(A\) is the union of a contiguous
subword. In a circular word the witness may be a cyclic interval.

Let

\[
   X_i\in\binom{\Omega}{k},\qquad
   |X_i\triangle X_{i+1}|=2,                       \tag{1.1}
\]

be a linear or cyclic Johnson owner trajectory. A maximal positive run of
a coordinate \(x\) is a maximal integer interval \([\alpha,\beta]\) on
which \(x\in X_i\).

Fix \(H\ge1\). Whenever the indicated owners exist, define the erosion
letters

\[
   D_p=\bigcap_{h=0}^{H}X_{p+h}.                   \tag{1.2}
\]

In the cyclic case, assume \(H\) is smaller than the period and read every
proper, non-full positive run in a nonwrapping integer lift. A coordinate
positive on the whole cycle is treated separately: it belongs to every
erosion letter.

### Lemma 1.1 (exact negative-interval characterization)

For a maximal positive run \([\alpha,\beta]\) of \(x\),

\[
   \boxed{x\in D_p\iff p\in[\alpha,\beta-H].}      \tag{1.3}
\]

Consequently the erosion support is nonempty exactly when the run contains
at least \(H+1\) owners, equivalently \(\beta-\alpha\ge H\). If
\(\beta-H<\alpha\), the displayed interval is reversed and \(x\) occurs in
no erosion letter through that run.

#### Proof

The condition \(x\in D_p\) is exactly

\[
   [p,p+H]\subseteq[\alpha,\beta],
\]

which is equivalent to \(\alpha\le p\le\beta-H\). \(\square\)

The following identities isolate the defect without assuming that all runs
are long.

### Lemma 1.2 (exact durable dilation)

Let \(a\le b\) and \(b-a\le H\), all read in one unwrapped index range.
Assume that every erosion index below is defined, either physically or by
specified endpoint padding. Then

\[
\begin{aligned}
 \bigcup_{p=b-H}^{a}D_p
   =\{x\in\bigcap_{i=a}^{b}X_i:\;&
       \text{the positive run containing }[a,b]\\
      &\text{has at least }H+1\text{ owners}\},                 \tag{1.4}
\end{aligned}
\]

and

\[
\begin{aligned}
 \bigcup_{p=a-H}^{b}D_p
   =\{x\in\bigcup_{i=a}^{b}X_i:\;&
       \text{some positive run meeting }[a,b]\\
      &\text{has at least }H+1\text{ owners}\}.                 \tag{1.5}
\end{aligned}
\]

#### Proof

Suppose first that a run \([\alpha,\beta]\) contains \([a,b]\) and has
length at least \(H+1\). The two integer intervals

\[
   [\alpha,\beta-H],\qquad [b-H,a]
\]

intersect: \(\alpha\le a\), \(\alpha\le\beta-H\),
\(b-H\le a\), and \(b-H\le\beta-H\). A point in their intersection gives
an erosion window contained in the run and containing \([a,b]\).
Conversely, if \(p\in[b-H,a]\), then
\([a,b]\subseteq[p,p+H]\), proving (1.4).

For (1.5), a long run meeting \([a,b]\) has

\[
   [\alpha,\beta-H]\cap[a-H,b]\ne\varnothing,
\]

because \(\alpha\le b\) and \(\beta-H\ge a-H\). Conversely every
\([p,p+H]\) with \(p\in[a-H,b]\) meets \([a,b]\). \(\square\)

Thus the straight erosion word recovers precisely the durable support. A
global braid has to reroute, rather than merely dilate, the reversed
intervals.

## 2. Fixed-baseline rigidity

The first possible interpretation of an in-place braid is to retain the
canonical owner witnesses and decorate their positions. This is impossible
for short runs.

### Theorem 2.1 (no reversed-run decoration of fixed owner intervals)

Let \(P\) be an integer interval of word positions, and suppose letters
\(Z_p\subseteq\Omega\), \(p\in P\), are required to satisfy

\[
   X_i=\bigcup_{p=i-H}^{i}Z_p                      \tag{2.1}
\]

for every \(i\) for which \([i-H,i]\subseteq P\). If \(p\) is an interior
position participating in all \(H+1\) such owner intervals, then

\[
   \boxed{Z_p\subseteq\bigcap_{i=p}^{p+H}X_i=D_p.} \tag{2.2}
\]

In particular no coordinate belonging only to a positive run of at most
\(H\) owners can be placed at \(p\). On a circular baseline of length
greater than \(H\), (2.2) holds at every position.

#### Proof

If \(x\in Z_p\), then every fixed owner witness whose interval contains
\(p\) also contains \(x\). Those owners are exactly

\[
   X_p,X_{p+1},\ldots,X_{p+H}.
\]

Therefore \(x\) lies in their intersection, proving (2.2). A circular
position also lies in exactly those \(H+1\) cyclic owner intervals. \(\square\)

This theorem permits arbitrary changes and deletions inside the baseline
letters; it does not assume \(D_p\subseteq Z_p\). The conclusion is that
the fixed family of owner intervals itself forbids every new short-run
coordinate. Only \(O(H)\) linear boundary positions escape the full
constraint. Hence a successful \(S+O(H)\) replacement must globally
reroute the owner witnesses.

## 3. The Pareto support path

We now describe an exact rerouting which does not preserve the old owner
intervals position by position.

For an endpoint point \(z=(u,v)\), put

\[
   W_z=\bigcap_{i=-u}^{v}X_i.                      \tag{3.1}
\]

To a positive run \([L,R]\) attach the point \((-L,R)\), with the standard
upper clipping and below-rectangle deletion used in the global dominance
chart.

Let

\[
   \Gamma=(z_0,z_1,\ldots,z_T),\qquad
   z_t=(u_t,v_t),                                  \tag{3.2}
\]

be the east-before-south unit staircase through the Pareto-minimal run
points, from the northwest to the southeast corner of the endpoint
rectangle. Assume the nonzero corridor condition, so every \(W_{z_t}\) is
nonempty, and set

\[
   Y_t=W_{z_t}.                                    \tag{3.3}
\]

### Lemma 3.1 (one-coordinate monotonicity)

On every edge,

\[
\begin{array}{lll}
Y_{t+1}\subseteq Y_t,\quad |Y_t\setminus Y_{t+1}|\le1,
  &\text{for an east edge},\\[2mm]
Y_t\subseteq Y_{t+1},\quad |Y_{t+1}\setminus Y_t|\le1,
  &\text{for a south edge}.
\end{array}                                                       \tag{3.4}
\]

In particular, if

\[
   \tau=\#\{t\in\{0,\ldots,T-1\}:Y_{t+1}\ne Y_t\},               \tag{3.5}
\]

then \(\tau\le T\), and every changing edge toggles exactly one coordinate.

#### Proof

An east step replaces \(u\) by \(u+1\), so it adds the single owner
\(X_{-u-1}\) to the intersection (3.1). Since
\(X_{-u-1}\) and \(X_{-u}\) are Johnson-adjacent and
\(Y_t\subseteq X_{-u}\), intersecting with \(X_{-u-1}\) can delete at most
the unique coordinate of \(X_{-u}\setminus X_{-u-1}\). This proves (3.4).
A south step removes the last owner \(X_v\); the enlarged intersection can
gain at most the unique coordinate of \(X_{v-1}\setminus X_v\), proving
the south case of (3.4). \(\square\)

For each coordinate \(x\), decompose

\[
   \{t:x\in Y_t\}                                  \tag{3.6}
\]

into maximal integer interval components. A component
\(\rho=[s_\rho,e_\rho]\) is labelled by its coordinate \(x(\rho)\). Put

\[
   C=\bigcap_{t=0}^{T}Y_t.                         \tag{3.7}
\]

Remove the full support components belonging to \(C\), and let
\(\mathcal R\) be the remaining component family. Let \(B_0\) be the
number of components of \(\mathcal R\) which contain exactly one of the
endpoints \(0,T\). All other members of \(\mathcal R\) are internal.

The family is **proper** if its members can be ordered
\(\rho_1,\ldots,\rho_N\) so that

\[
   s_{\rho_1}\le\cdots\le s_{\rho_N},\qquad
   e_{\rho_1}\le\cdots\le e_{\rho_N}.              \tag{3.8}
\]

Equivalently, there is no reversed start/end pair. Ties may be broken in
either compatible way.

### Theorem 3.2 (proper-support Pareto compiler)

Assume \(\mathcal R\) is proper. Assume also the proved global dominance
property for the requested floor-correct query points:

\[
   W_q=\bigcup_{t:z_t\ge q}Y_t.                    \tag{3.9a}
\]

Define

\[
   E_j=C\cup\{x(\rho_j)\},\qquad 1\le j\le N.       \tag{3.9}
\]

Emit \(E_1,\ldots,E_N\), together with one additional letter \(C\) if
\(C\ne\varnothing\). Then the resulting literal word represents:

1. every nonempty union \(\bigcup_{t=u}^{v}Y_t\);
2. every nonempty intersection \(\bigcap_{t=u}^{v}Y_t\);
3. every floor-correct lower query in the dominance chart; and
4. every consecutive upper union of owners whose singleton and adjacent
   depth-one query points lie in the endpoint rectangle.

Its exact length is

\[
   \boxed{
   |Z|=\frac{\tau+B_0}{2}+
          \mathbf 1_{C\ne\varnothing}
       \le
       \frac{T+B_0}{2}+
          \mathbf 1_{C\ne\varnothing}.}            \tag{3.10}
\]

#### Proof

At a fixed time \(t\), the active supports satisfy

\[
   s_{\rho_j}\le t\le e_{\rho_j}.                  \tag{3.11}
\]

The first inequality selects a prefix of the order (3.8), and the second
selects a suffix. Thus the active supports form one index interval and
the OR of the corresponding \(E_j\)'s is exactly \(Y_t\).

A support meets \([u,v]\) exactly when

\[
   s_{\rho_j}\le v,\qquad e_{\rho_j}\ge u,         \tag{3.12}
\]

again a prefix intersected with a suffix. Its contiguous \(E\)-block has
OR \(\bigcup_{t=u}^{v}Y_t\). A support contains \([u,v]\) exactly when

\[
   s_{\rho_j}\le u,\qquad e_{\rho_j}\ge v,         \tag{3.13}
\]

which proves the intersection assertion. If no noncore support is needed,
the extra \(C\)-letter is the witness.

For a floor-correct lower query \(q\), (3.9a) applies. The first coordinate
of \(z_t\) is nondecreasing and the second is
nonincreasing, so the selected times form one interval. This proves the
lower claim.

For an owner \(X_i\) in the rectangle, let \(I_i\) be its selected time
interval in (3.9a). Consecutive intervals \(I_i,I_{i+1}\) overlap: their
intersection is the selected set for \(X_i\cap X_{i+1}\), which is a
nonempty rank-\((k-1)\) floor-correct target. Hence
\(\bigcup_{i=a}^{b}I_i\) is one time interval, and (3.12) represents
\(\bigcup_{i=a}^{b}X_i\).

Finally, Lemma 3.1 says that each changing path edge toggles one
coordinate. An internal support component accounts for two changes and a
one-ended component for one. If \(N_{\rm int}\) is the number of internal
components, then

\[
   \tau=2N_{\rm int}+B_0,\qquad
   N=N_{\rm int}+B_0=\frac{\tau+B_0}{2}.           \tag{3.15}
\]

This proves (3.10). \(\square\)

### 3.3 Relation to owner-run endpoints

For a positive owner run \(I=[L,R]\), its contribution to (3.6) is

\[
   A_I=\{t:u_t\le-L,\ v_t\le R\}.                  \tag{3.16}
\]

This is a time interval: the first condition is a prefix and the second a
suffix. Larger \(R\) makes the support enter earlier, while smaller \(L\)
makes it leave later. Therefore strict containment

\[
   L<L',\qquad R>R'                                \tag{3.17}
\]

induces the reversed support order

\[
   s(A_I)\le s(A_{I'}),\qquad
   e(A_I)\ge e(A_{I'}),                            \tag{3.18}
\]

with strict inequalities when neither endpoint is clipped or tied.
Properness is exactly the absence of reversed order in the induced support
components. It is not equivalent merely to the absence of short runs:
shortness creates the negative erosion defect, while containment between
different runs creates the possible braid-order defect.

For a cut cluster of actual span \(S\), the two coordinate ranges of the
endpoint rectangle are \(H+S-1\). Thus

\[
   T=2(H+S-1),                                     \tag{3.19}
\]

and Theorem 3.2 gives the upper bound

\[
   |Z|\le S+H-1+\frac{B_0}{2}
             +\mathbf 1_{C\ne\varnothing}.         \tag{3.20}
\]

When the actual cuts are enlarged by the \(H\)-long virtual-cut intervals
needed to replace all omitted negative erosion prefixes, their span is
\(S+H-1\). Therefore the correct full-restoration constant is

\[
   T=2\bigl(H+(S+H-1)-1\bigr)
    =2(S+2H-2).                                    \tag{3.21}
\]

This corrects the tempting but false use of (3.19) for the virtual chart.
Owner unions are covered only for singleton points inside the chosen
rectangle. An outer owner halo must be included by enlarging the rectangle
or handled by a separately proved boundary splice.

## 4. Cutting to proper cells

The global support family need not be proper. Its obstruction can be
measured exactly after cutting the time path.

Choose internal cut vertices

\[
   Q=\{q_1<\cdots<q_{K-1}\}\subseteq\{1,\ldots,T-1\},
\]

put \(q_0=0,q_K=T\), and use the overlapping closed cells

\[
   J_r=[q_{r-1},q_r],\qquad 1\le r\le K.           \tag{4.1}
\]

Their vertex sets overlap at cut points, but their edge sets partition the
\(T\) Pareto edges.

Restrict each global support component to a cell. If a restriction equals
the whole cell, absorb its coordinate into the cell core

\[
   C_r=\bigcap_{t\in J_r}Y_t.                      \tag{4.2}
\]

Every other nonempty maximal restriction is a cell token. Call \(Q\)
**admissible** if the nonfull token supports form a proper family in every
cell.

Let

\[
 C_{\rm hit}(Q)=
 \#\{\rho:\rho\text{ is globally internal and }
                [s_\rho,e_\rho]\cap Q\ne\varnothing\}.           \tag{4.3}
\]

This is a hit-once count. A cut equal to \(s_\rho\) or \(e_\rho\) counts;
“strictly inside” would be incorrect.

### Theorem 4.1 (hit-once proper-cell compiler)

For every admissible cut set \(Q\), there is a literal word \(Z_Q\) which
represents every nonempty union \(\bigcup_{t=u}^{v}Y_t\), and
hence every lower dominance query and upper owner union covered in
Theorem 3.2. Its length satisfies

\[
   \boxed{
   |Z_Q|\le
   \frac{\tau+B_0}{2}+C_{\rm hit}(Q)+2K
   \le
   \frac{T+B_0}{2}+C_{\rm hit}(Q)+2K.}             \tag{4.4}
\]

#### Proof

In cell \(J_r\), order the nonfull tokens properly and emit

\[
   C_r,\ E_{r,1},\ldots,E_{r,N_r},\ C_r,           \tag{4.5}
\]

where

\[
   E_{r,j}=C_r\cup\{x(\rho_{r,j})\}.               \tag{4.6}
\]

Omit both displayed core portals when \(C_r=\varnothing\). Concatenate
the cell words in chronological order.

Inside a cell, a time prefix is represented by its left core portal and an
\(E\)-prefix; a time suffix by an \(E\)-suffix and its right portal; an
interior time interval by one \(E\)-block, or one core portal if only the
core is needed; and the whole cell by its whole word. Therefore a global
time interval is represented literally as

\[
   \text{suffix of its first cell};\quad
   \text{whole intermediate cell words};\quad
   \text{prefix of its last cell}.                 \tag{4.7}
\]

Duplicating a shared cut vertex introduces only coordinates already in the
target and hence no contamination.

It remains to count tokens. A globally internal support missed by \(Q\)
gives one nonfull cell token. If it meets one or many cut vertices, its
first and last restricted pieces are the only nonfull pieces; every piece
between successive cuts is a full-cell support absorbed into \(C_r\). It
therefore gives exactly two tokens. This remains true when a cut equals a
support endpoint: the singleton piece in the adjacent closed cell is one of
the two endpoint pieces. A globally one-ended support always gives exactly
one token, and a full support gives none. Thus

\[
   \sum_{r=1}^{K}N_r
    =\frac{\tau+B_0}{2}+C_{\rm hit}(Q).            \tag{4.8}
\]

There are at most two nonzero core portals per cell, proving (4.4).
\(\square\)

Define the exact braid statistic

\[
\begin{aligned}
 \Xi(\Gamma)=\frac{B_0}{2}+
   \min_{Q\ {\rm admissible}}
      \{C_{\rm hit}(Q)+2(|Q|+1)\}.                 \tag{4.9}
\end{aligned}
\]

Cutting at every internal vertex is admissible, so the minimum is defined.
The theorem says

\[
   \boxed{|Z|\le T/2+\Xi(\Gamma).}                 \tag{4.10}
\]

When the whole family is proper, Theorem 3.2 is sharper than (4.10): it
needs only one common-core portal rather than two.

### Theorem 4.2 (periodic circular version)

Let \(Y_t\), \(t\in\mathbb Z_T\), be a genuinely periodic Pareto-support
sequence in which every edge changes at most one coordinate, and let
\(\tau^\circ\) be the number of changing edges. Decompose every
nonconstant coordinate support into circular arc components. Choose a
nonempty set \(Q\) of cut vertices. In every closed circular cell, absorb
full-cell restrictions into the core and require the remaining restriction
components to be proper; as in Theorem 4.1, omit both core portals when the
cell core is empty. Let \(C_{\rm hit}^{\circ}(Q)\) count support arcs
containing at least one cut point, once per arc. Then one circular literal
word covers every nonempty circular time union and has length at most

\[
   \boxed{
   \frac{\tau^\circ}{2}+C_{\rm hit}^{\circ}(Q)+2|Q|
   \le
   \frac T2+C_{\rm hit}^{\circ}(Q)+2|Q|.}           \tag{4.11}
\]

#### Proof

Every nonconstant circular support arc has two toggle endpoints, so their
number is \(\tau^\circ/2\). An unhit arc creates one nonfull token. A hit
arc creates two endpoint tokens; all cell restrictions between them are
full and absorbed. This remains true if the arc contains all cut points:
in the one cell containing its complementary gap, the restriction has two
maximal endpoint pieces. The two-portal chronology proof of Theorem 4.1
now runs cyclically. \(\square\)

One may therefore define

\[
   \Xi^{\circ}(\Gamma)=
   \min_Q\{C_{\rm hit}^{\circ}(Q)+2|Q|\}.           \tag{4.12}
\]

This circular statement requires actual periodicity. It does not license
identifying two unequal endpoints of a finite chart.

### Corollary 4.3 (exact blockwise sufficient gate)

Suppose a baseline portion of total length \(W_0\) is partitioned into
\(M\) central blocks of spans \(S_1,\ldots,S_M\), with
\(\sum_rS_r=W_0\). Assign every required depth-\(H\) query to a block whose
virtual-cut endpoint rectangle contains the query and its required owner
singleton points. If \(Q_r\) is admissible in the resulting chart, then
the charts have total length at most

\[
   \boxed{
   W_0+M(2H-2)+\sum_{r=1}^{M}\Xi(\Gamma_r),}        \tag{4.13}
\]

before any additional outer-halo enlargement. If block \(r\) is enlarged,
let \(\widehat\Gamma_r\) be the enlarged chart and let \(\delta_r\) be the
increase of its endpoint-rectangle half-perimeter. Reapplying Theorem 4.1
to the enlarged charts gives

\[
   |Z|\le
   W_0+M(2H-2)+\sum_r\delta_r+
                    \sum_r\Xi(\widehat\Gamma_r).                  \tag{4.13a}
\]

The statistic \(\Xi\) must be recomputed after enlargement; adding only
the half-perimeter increase to the old statistic is not justified.

Consequently, at a block scale \(b\gg H\), if

\[
   M=O(W_0/b),\qquad
   \sum_r\Xi(\widehat\Gamma_r)=o(W_0),              \tag{4.14}
\]

and \(\sum_r\delta_r=O(MH)\), then the integrated
replacement length is \(W_0+o(W_0)\).

#### Proof

For the virtual-cut chart of block \(r\), (3.21) gives

\[
   T_r/2=S_r+2H-2.
\]

Sum (4.10), using the enlarged form (4.13a) when necessary. Under (4.14),
\(MH=O(W_0H/b)=o(W_0)\), proving the last claim. \(\square\)

This is a conditional literal fusion theorem, not an arbitrary substring
splice. Its hypotheses require every old target to be reassigned to a
specified chart interval. In particular, external ambient intervals are
preserved only through that explicit reassignment.

## 5. The tight east--south corner

The local mechanism behind failure of properness can already be seen at
one east--south turn.

### Lemma 5.1 (exact corner deletion criterion)

Suppose three consecutive endpoint vertices are

\[
   A=(u-1,v),\qquad B=(u,v),\qquad C=(u,v-1).      \tag{5.1}
\]

Then

\[
   \boxed{W_B=W_A\cap W_C.}                        \tag{5.2}
\]

Every integer dominance query \(q\le B\), \(q\ne B\), is dominated by at
least one of \(A,C\). The vertex \(B\) is the unique path vertex dominating
\(B\) itself. Hence deleting the \(B\)-letter from the canonical Pareto
word preserves all canonical dominance witnesses except possibly the query
\(B\). That query can be transferred to an adjacent letter without
contamination exactly when

\[
   \boxed{W_A=W_B\quad\text{or}\quad W_C=W_B.}     \tag{5.3}
\]

The two exact contamination fringes are

\[
 W_A\setminus W_B
  =\{x:\text{some run point }p\text{ of }x
          \text{ has }p_1=u-1,\ p_2\ge v\},        \tag{5.4}
\]

\[
 W_C\setminus W_B
  =\{x:\text{some run point }p\text{ of }x
          \text{ has }p_1\ge u,\ p_2=v-1\}.        \tag{5.5}
\]

#### Proof

The owner intervals defining \(W_A\) and \(W_C\) are respectively
\([-u+1,v]\) and \([-u,v-1]\). Their union is \([-u,v]\), proving (5.2).
If \(q\le B\) is a different integer point, either its first coordinate is
at most \(u-1\) or its second is at most \(v-1\), so \(A\ge q\) or
\(C\ge q\). Monotonicity of the staircase makes \(B\) the only vertex with
both coordinates at least those of \(B\). Since \(W_B\subseteq W_A,W_C\),
an adjacent replacement is exact precisely in (5.3). Finally, membership
in \(W_A\setminus W_B\) means that the coordinate is present from
\(-u+1\) through \(v\) but absent at \(-u\), giving (5.4); (5.5) is dual.
\(\square\)

Both fringes can be nonempty under exact Johnson legality and floor
correctness. For example, let \(|G|=k-4\), take all displayed coordinates
distinct outside \(G\), and use

\[
\begin{aligned}
X_{-3}&=G\cup\{n,f,y_1,y_2\},\\
X_{-2}&=G\cup\{n,\rho,y_1,y_2\},\\
X_{-1}&=G\cup\{n,\rho,\lambda,y_2\},\\
X_0&=G\cup\{n,\rho,\lambda,z\},\\
X_1&=G\cup\{n,\lambda,z,w\},\\
X_2&=G\cup\{n,z,w,g\},\\
X_3&=G\cup\{j,z,w,g\}.
\end{aligned}                                      \tag{5.6}
\]

Every step is Johnson-adjacent. At

\[
   A=(1,1),\quad B=(2,1),\quad C=(2,0),
\]

one has

\[
   W_A=G\cup\{n,\lambda\},\quad
   W_B=G\cup\{n\},\quad
   W_C=G\cup\{n,\rho\}.                            \tag{5.7}
\]

The query \(B\) has four owners and rank \(k-3\), exactly its floor. Both
adjacent transfers contaminate it. The run of \(n\) has six owners, so for
\(H\ge6\) it is itself a reversed depth-\(H\) erosion interval.

The next section shows that this corner toll can be forced at positive
linear density even after abandoning the Pareto word entirely.

## 6. The cyclic-comb obstruction

### Theorem 6.1 (integral two-sided-rainbow comb)

Let

\[
   R\ge5,\qquad m\ge2R-3,
\]

and let \(\Omega=[2m+1]\). Choose pairwise disjoint sets

\[
   |K|=m-2,\qquad
   \{b_t:t\in\mathbb Z_R\},\qquad
   \{x_t:t\in\mathbb Z_R\}.                       \tag{6.1}
\]

Define rank-\(m\) facets

\[
   A_t=K\cup\{b_t,b_{t+1}\},\qquad
   E_t=K\cup\{b_t,x_t\},                           \tag{6.2}
\]

and rank-\((m+1)\) owners

\[
\begin{aligned}
   L_t&=K\cup\{b_{t-1},b_t,x_t\},\\
   R_t&=K\cup\{b_t,x_t,b_{t+1}\}.
\end{aligned}                                      \tag{6.3}
\]

Order them cyclically as

\[
   L_0,R_0,L_1,R_1,\ldots,L_{R-1},R_{R-1}.        \tag{6.4}
\]

Then:

1. (6.4) is a cyclic Johnson trajectory, with

   \[
      L_t\cap R_t=E_t,\qquad
      R_t\cap L_{t+1}=A_t.                         \tag{6.5}
   \]

2. Every three-owner intersection is floor-correct of rank \(m-1\). Its
   distinct values are

   \[
      D_t=K\cup\{b_t\},                            \tag{6.6}
   \]

   and

   \[
   R_{t-1}\cap L_t\cap R_t=D_t
     =L_t\cap R_t\cap L_{t+1}.                     \tag{6.7}
   \]

3. The depth-one lower colours \(A_t,E_t\) are globally distinct. The
   depth-one upper colours are

   \[
   L_t\cup R_t
    =K\cup\{b_{t-1},b_t,b_{t+1},x_t\},             \tag{6.8}
   \]

   \[
   R_t\cup L_{t+1}
    =K\cup\{b_t,b_{t+1},x_t,x_{t+1}\},             \tag{6.9}
   \]

   and are globally distinct. Thus the first band is globally
   two-sided-rainbow.

4. Every three-owner upper union has rank \(m+3\), its floor-correct upper
   size.

5. Every linear literal word representing all \(2R\) owners and all
   depth-one and depth-two lower intersections has length

   \[
      \boxed{|Z|\ge2R+\left\lceil\frac R3\right\rceil.} \tag{6.10}
   \]

   The same inequality holds for a circular literal word with cyclic-arc
   witnesses.

#### Proof of the structural assertions

Equations (6.5) and (6.7) follow by direct intersection. The \(A_t\)'s are
distinguished by their cyclic adjacent \(b\)-pairs, the \(E_t\)'s by their
unique \(x_t\), and the two families by the presence of an \(x\)-coordinate.
The colours (6.8) are distinguished by their one \(x\)-coordinate, the
colours (6.9) by their adjacent \(x\)-pairs, and the two families by one
versus two \(x\)-coordinates. A direct union of either kind of three
consecutive owners contains \(K\) and five active coordinates, so its size
is \((m-2)+5=m+3\).

#### Proof of the literal lower bound

Let

\[
   \Sigma=\{b_t,x_t:t\in\mathbb Z_R\},\qquad
   \pi(Y)=Y\cap\Sigma.                             \tag{6.11}
\]

From a witness for \(D_t\), select a word position \(P_t\) whose letter
contains \(b_t\). Exactness forces

\[
   \pi(Z_{P_t})=\{b_t\}.                           \tag{6.12}
\]

From a witness for \(E_t\), select a position \(Q_t\) whose letter contains
\(x_t\). Then

\[
   x_t\in\pi(Z_{Q_t})\subseteq\{b_t,x_t\}.         \tag{6.13}
\]

All \(2R\) positions \(P_t,Q_t\) are pairwise distinct.

Fix \(t\), and put

\[
   \Lambda_t=\{b_{t-1},b_t,b_{t+1},x_t\}.         \tag{6.14}
\]

We claim that there is a nonanchor position \(p\) such that

\[
   \varnothing\ne\pi(Z_p)\subseteq\Lambda_t.       \tag{6.15}
\]

Assume not. Delete from the order every letter contained wholly in \(K\).
A \(\Sigma\)-empty letter containing any unused coordinate outside \(K\) is
not deletable: it is a blocker. Under the assumption, every remaining
nonanchor is a blocker for all targets contained in \(K\cup\Lambda_t\).

Write

\[
   a=b_{t-1},\qquad b=b_t,\qquad c=b_{t+1},
   \qquad x=x_t.
\]

Exact witnesses for

\[
   A_{t-1}=K\cup\{a,b\},\qquad
   A_t=K\cup\{b,c\}                                \tag{6.16}
\]

force \(P_{t-1},P_t,P_{t+1}\) to be consecutive in the reduced linear
order, with \(P_t\) in the middle. Indeed, each pair must be joined by an
interval containing no blocker, and under the assumption there is no
other usable occurrence of either required active coordinate.

The position \(Q_t\) lies outside this triple. If it lies on the
\(P_{t-1}\)-side, every interval representing the owner
\(R_t=K\cup\{b,c,x\}\) crosses the forbidden \(a\)-position. If it lies on
the \(P_{t+1}\)-side, every interval representing
\(L_t=K\cup\{a,b,x\}\) crosses the forbidden \(c\)-position. This proves
(6.15) in a linear word.

For a circular word, (6.16) forces the reduced-circle adjacencies

\[
   P_{t-1}-P_t-P_{t+1}.                            \tag{6.17}
\]

The \(L_t\)-witness forces \(Q_t\) to be the other neighbor of
\(P_{t-1}\), and the \(R_t\)-witness forces it to be the other neighbor of
\(P_{t+1}\). The reduced circle would therefore be exactly the four-cycle

\[
   Q_t-P_{t-1}-P_t-P_{t+1}-Q_t.                   \tag{6.18}
\]

Since \(R\ge5\), another nonempty anchor exists, a contradiction. Thus
(6.15) also holds circularly.

A fixed nonanchor can satisfy (6.15) for at most three values of \(t\). If
its projection contains \(x_j\), only \(t=j\) is possible. If it contains
only \(b\)-coordinates, even a singleton \(b_j\) belongs to only
\(\Lambda_{j-1},\Lambda_j,\Lambda_{j+1}\), and adding further
\(b\)-coordinates cannot increase the number. Covering all \(R\) values
of \(t\) therefore needs at least \(\lceil R/3\rceil\) nonanchors. Together
with the \(2R\) anchors this proves (6.10). \(\square\)

### 6.2 Reversed intervals and the diagonal corridor

Index the owners by

\[
   X_{2t}=L_t,\qquad X_{2t+1}=R_t.                 \tag{6.19}
\]

The maximal positive run of \(x_t\) is

\[
   [2t,2t+1],                                      \tag{6.20}
\]

so its depth-\(H\) erosion interval is

\[
   [2t,2t+1-H],                                    \tag{6.21}
\]

reversed for every \(H\ge2\). The run of \(b_t\) is

\[
   [2t-1,2t+2],                                    \tag{6.22}
\]

and its erosion interval is reversed for \(H\ge4\). Thus, for
\(4\le H<2R\), every erosion letter is just \(K\). Nonetheless

\[
   E_t=D_t\cup\{x_t\},                             \tag{6.23}
\]

and the two neighboring three-owner intersections both equal \(D_t\).
This is the tight corner spike of Section 5, now repeated cyclically.

The lower bound (6.10) permits a completely arbitrary new word, not merely
decoration of the erosion positions. It therefore proves the genuinely
strong local obstruction

\[
   |Z|-S\ge\left\lceil\frac S6\right\rceil.        \tag{6.24}
\]

Take \(R=\lfloor m/4\rfloor\) and \(H=\lceil A\sqrt m\rceil\), for fixed
\(A\). Then \(S=2R=\Theta(m)\), \(S/H\to\infty\), and for all sufficiently
large \(m\),

\[
   3H+S\le m+1.                                    \tag{6.25}
\]

Every query used in the lower-bound proof has depth at most two and hence
lies inside the diagonal corridor \(u+v\le H\). Therefore an \(O(H)\)
halo or endpoint duplication cannot absorb (6.24).

### 6.3 Integral odd-graph lift

Let \(\overline L_t,\overline R_t\) be the complements of the owners in
\(\Omega=[2m+1]\). The alternating sequence

\[
   \overline L_t,\ E_t,\ \overline R_t,\ A_t,\
   \overline L_{t+1}                               \tag{6.26}
\]

forms a cycle in \(KG(2m+1,m)\): each facet is contained in each adjacent
owner and hence disjoint from its complement. It is vertex-simple. The
facets are all distinct; the owners are all distinct; and every facet
contains the nonempty core \(K\), while every owner complement avoids
\(K\), so no cross-type collision is possible.

Thus the obstruction remains fully integral inside one exact,
vertex-simple odd-graph cycle. What is not proved is that this cycle is a
component of the canonical PBBS factor.

## 7. Proved and conditional boundary

The following statements are proved with exactly their stated hypotheses
and no hidden extra assumptions.

1. The negative-interval identity (1.3), durable dilation identities
   (1.4)--(1.5), and fixed-baseline rigidity (2.2).
2. The proper-support compiler, including literal lower and upper
   chronology and exact length (3.10).
3. The hit-once cell ledger (4.4): incidence with many cuts is not charged
   repeatedly.
4. The periodic circular version (4.11).
5. The cyclic-comb lower bound (6.10), its first-band two-sided rainbowness,
   corridor compatibility, and vertex-simple odd-graph lift.

The following statements remain unproved and are not imported.

1. **PBBS proper-cell estimate.** For canonical PBBS charts on blocks
   \(b\gg H\), it is not known that cuts can be chosen with

   \[
      \sum_{\rm blocks}\Xi(\Gamma_B)=o(W).         \tag{7.1}
   \]

   In particular, neither \(B_0=O(H)\) nor
   \(C_{\rm hit}(Q)=o(S)\) is currently proved.

2. **Canonical exclusion of comb forks.** The residence and corridor
   ledgers do not exclude the local comb, but no positive-density embedding
   of it in the canonical PBBS factor is proved.

3. **External witness reuse.** The block lower bound does not rule out a
   global PBBS word which represents a block target using physical letters
   assigned outside that block. Such reuse would need a separate global
   theorem.

4. **Outer-halo splice.** The upper chronology theorem covers owner points
   in the chosen endpoint rectangle. Enlarging the rectangle by an
   \(O(H)\) halo preserves the base half-perimeter scale, but \(\Xi\) must
   be recomputed; an exact global splice must specify those enlarged
   endpoints and target assignments.

Accordingly, the universal circular/diagonal compiler proposed in the
question is closed: reversed intervals alone do not admit an \(S+O(H)\)
replacement. The surviving positive route is the strictly stronger
PBBS-specific assertion (7.1), or an equally strong cross-block witness
reuse theorem. Either would compose with the existing baseline and tail
ledgers into coefficient one; neither is claimed here.

## 8. Independent audit record

The decisive steps were independently audited. The audit confirmed:

1. the factor \(2R+\lceil R/3\rceil\) in both the linear and circular comb
   arguments;
2. pairwise distinct anchors and the fact that one helper position serves
   at most three centers;
3. vertex simplicity and the two-sided-rainbow upper colours;
4. the proper-support active/meeting/containing interval argument;
5. the two-portal literal chronology across closed overlapping cells; and
6. the hit-once, rather than cut-incidence, congestion constant.

The audit also forced seven scope corrections incorporated above:

1. a \(\Sigma\)-empty word letter is erasable only if its entire support lies
   in \(K\); otherwise it is a blocker;
2. endpoint contact with a closed support counts in \(C_{\rm hit}(Q)\);
3. virtual-cut endpoint restoration uses \(T=2(S+2H-2)\), not
   \(2(H+S-1)\); and
4. upper chronology outside the endpoint rectangle needs enlargement or a
   separate splice;
5. the truncated Pareto path can have zero-change edges, so the exact
   component identity uses the actual toggle count \(\tau\), with only
   \(\tau\le T\) available universally;
6. cyclic erosion intervals require a nonwrapping lift, while a full-cycle
   coordinate has full rather than finite interval support; and
7. after enlarging a chart, its \(\Xi\)-statistic must be recomputed rather
   than inherited from the smaller chart.

No coefficient-one conclusion is asserted.
