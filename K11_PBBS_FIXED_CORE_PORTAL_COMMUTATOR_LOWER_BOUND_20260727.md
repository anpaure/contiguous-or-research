# The \(k=11\) portal needs at least three formal alphas

Date: 2026-07-27

Method: cyclic-parenthesis and integer-circuit analysis only; no computational
search.

## 0. Corrected outcome

Let \(F_{\rm P}^c\) be the complemented centered PBBS factor and let

\[
Z=\{1,3,5,7,9\}
\]

be an alternating lower row.

The following statements are proved.

1. The only initially executable \(K_4\) four-cycle trades touching the
   alternating component are the two reflected boundary transports obtained
   by deleting \(1\) or \(9\) from \(Z\).
2. Both transports are component-inert.
3. After either transport, no alpha chart and no second noninverse overlapping
   \(K_4\) chart uses either transported chord on the alternating route.
4. The boundary nearly-alpha cannot be completed by a second changing-core
   alpha through exactly one cancelled diamond.
5. A support-minimal portal whose negative rows all share one rank-four core
   cannot use only four negative rows. Hence every such one-core portal uses
   at least five negative rows.
6. No changing-core sum of two formal alphas has an entirely present
   surviving negative side containing the alternating chord.

Consequently every alpha-generated portal from the initial alternating
component uses at least three formal alphas.  The changing-core
classification is proved in
K11_PBBS_CHANGING_CORE_TWO_ALPHA_CLASSIFICATION_20260727.md, and the bound
is attained by the fork in
K11_PBBS_EXPLICIT_THREE_ALPHA_FORK_PORTAL_20260727.md.

The next unresolved mechanisms are therefore:

- an equivariant or residence-compatible version of the three-alpha fork;
- a noncanonical one-common-core \(K_5\)-supported circuit, necessarily using
  at least five negative rows.

## 1. Classification of initial \(K_4\) transports

For \(x\in Z\), put \(R_x=Z\setminus\{x\}\). The alternating chord at row
\(Z\) has endpoint pair \(\{0,10\}\). A \(K_4\) chart through this row must
therefore use

\[
Q_x=\{x,0,10,y\}
\tag{1.1}
\]

for one additional coordinate \(y\).

For an interior occupied coordinate \(1<x<9\), cyclic reduction gives

\[
\epsilon_{R_x}(0)=\epsilon_{R_x}(10)=\{x-1,x+1\}.
\tag{1.2}
\]

Both \(x-1\) and \(x+1\) would have to belong to \(Q_x\), but (1.1) has room
for only one of them. Thus no interior \(x\) supports a \(K_4\) chart.

For \(x=1\), let \(R=\{3,5,7,9\}\). The exact endpoint table is

\[
\begin{array}{c|cccc}
u&1&10&0&2\\ \hline
\epsilon_R(u)&\{0,10\}&\{0,2\}&\{1,2\}&\{1,10\}.
\end{array}
\tag{1.3}
\]

This is the directed four-cycle on \(Q=\{0,1,2,10\}\) audited in
K11_PBBS_PROPOSED_PORTAL_COMMUTATOR_AUDIT_20260727.md. The case \(x=9\)
is its reflection. Therefore

\[
\boxed{\text{exactly two boundary/reflection \(K_4\) families touch an
alternating row}.}
\tag{1.4}
\]

The external-port trace shows that both are component-inert: they move row
labels between the two local paths but preserve the contracted external
pairing.

## 2. Initial alpha charts: absent, but often only one edge short

No complete alpha chart of the initial PBBS factor contains the alternating
chord. It is important, however, to retain the exact amount of failure.

For every \(x>1\), the forward chart with common spare \(0\) and coordinate
set

\[
\{0,10,x,x-1\}
\]

has two present negative diamonds:

\[
Z:\{0,10\},
\qquad
R_x+(x-1):\{0,x\},
\tag{2.1}
\]

and one missing negative diamond:

\[
d_x=\bigl(R_x+10,\{0,x-1\}\bigr).
\tag{2.2}
\]

Reflection gives the corresponding common-spare-\(10\) family. Thus the
absence of an initial alpha proves that a one-alpha portal is impossible,
while the companion changing-core audit proves that no second chart can
insert \(d_x\) with all surviving negative diamonds present.

At the boundary \(x=1\), the nearly-alpha used in the original portal
proposal has present negative pairs

\[
Z:\{0,10\},
\qquad R+10:\{0,2\},
\tag{2.3}
\]

and missing diamond

\[
d=\bigl(R+2,\{0,1\}\bigr).
\tag{2.4}
\]

## 3. What is ruled out after one boundary transport

The exact one-\(K_4\) audit proves more than component-inertness. After the
boundary four-cycle reversal, the alternating route carries the transported
rows

\[
R+2=\{2,3,5,7,9\},
\qquad
R+10=\{3,5,7,9,10\}.
\]

Neither transported chord belongs to any post-switch alpha chart. Neither
supports a second noninverse overlapping \(K_4\): the original-core option is
the inverse trade, one apparent option splits into two transpositions, and
the remaining fourth-row condition fails. Hence

\[
\boxed{\text{one boundary \(K_4\) followed by one local alpha or one
noninverse overlapping \(K_4\) is not a portal}.}
\tag{3.1}
\]

This conclusion is local to the transported alternating route.  The global
changing-core two-alpha classification is supplied by the companion audit.

## 4. Boundary two-alpha completion is impossible

Let

\[
Y=R+2=\{2,3,5,7,9\}.
\]

To insert the missing boundary diamond \(d=(Y,\{0,1\})\), a second alpha with
core \(S=Y\setminus\{y\}\), \(y\in Y\), is forced to use common spare \(1\):
the current PBBS chord at \(Y\) is \(\{1,10\}\). In particular it requires

\[
\epsilon_S(10)=\{0,1\}.
\tag{4.1}
\]

Exact cyclic reduction gives

\[
\begin{array}{c|ccccc}
y&2&3&5&7&9\\ \hline
\epsilon_{Y-y}(10)
&\{0,2\}&\{3,4\}&\{4,6\}&\{6,8\}&\{1,8\}.
\end{array}
\tag{4.2}
\]

No entry is \(\{0,1\}\). Therefore the boundary nearly-alpha cannot be
completed by a second changing-core alpha through one cancelled diamond.
The reflected boundary case follows identically.

This is the boundary subcase.  The interior and double-cancellation subcases
are excluded in
K11_PBBS_CHANGING_CORE_TWO_ALPHA_CLASSIFICATION_20260727.md.

## 5. The one-common-core row-support lower bound

The fixed-core alpha-generation theorem states that every integral local
sigma-trade kernel is generated over \(\mathbb Z\) by ordinary
four-coordinate alpha trades. On four fixed-core lower rows, the
support-minimal simple circuits are precisely:

- alpha triangles;
- octahedral \(K_4\) four-cycles.

An alpha triangle containing the alternating chord is unavailable in the
initial PBBS factor, while the only executable \(K_4\) four-cycles touching
it are the component-inert boundary pair from (1.4). Consequently:

### Theorem 5.1

A support-minimal simple portal circuit touching the alternating component,
whose negative rows all have the form \(R+i\) for one rank-four core \(R\),
uses at least five distinct negative rows.

Equivalently, the first unresolved one-common-core support is \(K_5\).
By alpha-generation, such a \(K_5\) circuit is not a new lattice direction:
it must be a nonconformal sum of ordinary alphas. Its possible novelty is
entirely in intermediate executability and external-port topology.

## 6. Exact remaining finite targets

The two-alpha category is closed and the three-alpha lower bound is sharp.
The next audit has two branches.

### Branch A: compatibility of the explicit fork

Determine whether translated forks can be packed or orbit-summed while
preserving component gain, quotient voltage, wreath residence, and the
required depth-\(q\) shadows.  The labelled local portal itself is complete.

### Branch B: one-core \(K_5\)

Classify simple \(K_5\)-supported fixed-core circuits with at least five
present negative PBBS rows and compute their contracted external-port
pairings. The canonical pentagon has already been excluded in
K11_PBBS_K5_PENTAGON_PORTAL_AUDIT_20260727.md; a portal here would therefore
be a noncanonical \(K_5\) circuit.  Nonexistence would push that category to
\(K_6\).

These are genuine finite endpoint-map questions. No claim of existence or
nonexistence is made here.
