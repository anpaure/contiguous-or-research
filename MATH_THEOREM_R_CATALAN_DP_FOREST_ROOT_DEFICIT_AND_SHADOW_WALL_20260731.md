# Delcourt--Postle side forests: exact rooted deficit and synchronized shadow expansion

Date: 2026-07-31

Status: exact finite identities; exact audit of the quantitative scope of
handoff item 2295ROOT; and an exact synchronized-\(Q\) theorem showing that
the full physical candidate graph has at most one anchor-free component.
No asymptotic palette-compatible rooted forest is claimed.

## 0. Verdict

Use

\[
 N=\binom{2n}{n-1},\qquad P=\binom{2n}{n-2},\qquad
 C=\operatorname {Cat}_{n+1},\qquad K=\operatorname {Cat}_n,
\]

and put

\[
 H=N-P=C-K,\qquad R=N-C=P-K.                         \tag{0.1}
\]

Let \(S\) be a spanning physical linear forest obtained after the cycle
deletions in item 2295ROOT, let

\[
                         |S|=P-\ell,
\]

and retain the side-anchor degree cap one.  If \(c_i\) is the number of
components of \(S\) containing exactly \(i\) anchors, then

\[
 \boxed{\quad
 c_0=R-r_{\widehat M/E_\rho}(S)=\ell-K+c_2.
 \quad}                                               \tag{0.2}
\]

Equivalently,

\[
 c_0=(\ell-K)_+
       +\left(c_2-(K-\ell)_+\right),                  \tag{0.3}
\]

and both summands on the right are nonnegative.  Thus:

1. no-empty support is possible only when \(\ell\le K\), and then it
   requires the extremal equality \(c_2=K-\ell\);
2. \(c_0=o(P/n)\) requires both
   \[
   (\ell-K)_+=o(P/n),\qquad
   c_2-(K-\ell)_+=o(P/n);                            \tag{0.4}
   \]
3. the statement \(\ell=o(P)\) by itself gives neither conclusion.

The full Delcourt--Postle coloring does not secretly supply (0.4).  Its
proved largest-class estimate has an order-\(8P/n\) density loss, an
unquantified \(P D_0^{-\alpha}\) coloring loss, and a fixed-cutoff cycle
deletion budget \(O(P/L)\).  Every selected physical cycle is anchor-free,
because an anchor has side degree at most one.  Breaking such a cycle
creates an empty path.  A slow diagonal \(L(n)\to\infty\) proves only
\(o(P)\), not \(o(P/n)\).

A first proposed counterexample based on puncturing the full shadow of
many nonanchors is **invalid for synchronized punctures**.  Every
nonanchor physical vertex \(y\) has a distinguished unpunctured facet:
if \(q_y\) is the unique child edge with \(U_{q_y}=y\), then
\(q_y\notin Q\), hence \(t_{q_y}\notin t(Q)\).  Lovász--Kruskal--Katona
then shows that an anchor-free component of the full candidate graph has
at least half of the central layer.  There can be at most one.

Thus the full-host rooted cut contributes only \(O(1)=o(P/n)\).  The
surviving obstruction is fragmentation inside a selected two-palette
forest, measured exactly by (0.2), not a small anchor-free component of
the full Boolean host.

Whole DP colour classes cannot be united: two \(P-o(P)\) classes repeat
\(P-o(P)\) resources.  The exact merge unit is a connected component of
their bipartite atom-conflict graph.  Such a toggle preserves palettes and
slots, but acyclicity and rooted gain remain separate tests.  For a private
bank of unit-gain toggles, partial Rado gives the exact residual-empty
min--max in Theorem 7.1.  Item 2295ROOT proves none of those rank cuts; an
explicit prime-field host shows that its numerical/coloring hypotheses
alone can remain \((7+o(1))P/n\) below the rooted cardinality scale.

## 1. Exact Catalan identities

Besides (0.1), factorial cancellation gives

\[
 H={3P\over n-1},\qquad
 K={P(n+2)\over n(n-1)},\qquad
 H-K={2P\over n},                                   \tag{1.1}
\]

and

\[
 {C\over P}={2(2n+1)\over n(n-1)}
            ={4+o(1)\over n}.                       \tag{1.2}
\]

Hence all three natural component scales \(H,C,K\) are
\(\Theta(P/n)\), not \(\Theta(P)\).

## 2. Exact leave--pairing decomposition

Adjoin a root \(\rho\) and the full root star

\[
                  E_\rho=\{\rho a:a\in A_Q\}
\]

to the physical graph on the \(N\) side vertices.  Write
\(\widehat M\) for its graphic matroid.

### Theorem 2.1

Let \(S\) be a spanning linear forest with \(P-\ell\) edges, where
\(0\le\ell\le P\).  Suppose every
physical vertex has degree at most two and every member of the
\(C\)-element anchor bank has degree at most one.  Then every component
contains zero, one, or two anchors and

\[
 \begin{aligned}
 c_0+c_1+c_2&=H+\ell,\\
 c_1+2c_2&=C.                                      \tag{2.1}
 \end{aligned}
\]

Consequently (0.2)--(0.3) hold and

\[
 \max\{0,\ell-K\}\le c_0
       \le \ell+\left\lfloor{P\over n}\right\rfloor. \tag{2.2}
\]

The lower bound is best possible using only these graph axioms.

#### Proof

A forest on \(N\) vertices with \(P-\ell\) edges has

\[
                         N-(P-\ell)=H+\ell
\]

components.  An anchor is a path endpoint or an isolated vertex, so a
component contains at most two anchors.  Counting components and anchors
gives (2.1).  Since \(C=H+K\),

\[
 c_0=H+\ell-C+c_2=\ell-K+c_2.                       \tag{2.3}
\]

Nonnegativity gives \(c_2\ge(K-\ell)_+\), proving (0.3) and the lower
bound.  Also \(c_2\le\lfloor C/2\rfloor\), and

\[
 \left\lfloor{C\over2}\right\rfloor-K
 =\left\lfloor{H-K\over2}\right\rfloor
 =\left\lfloor{P\over n}\right\rfloor,             \tag{2.4}
\]

which proves the upper bound.

For sharpness in the abstract graph class, take a complete ambient graph.
If \(\ell\le K\), prescribe

\[
 c_0=0,\qquad c_2=K-\ell,\qquad c_1=C-2K+2\ell.
\]

If \(\ell\ge K\), prescribe

\[
 c_0=\ell-K,\qquad c_2=0,\qquad c_1=C.
\]

In either case the component count is \(H+\ell\).  Partition the \(N\)
vertices into paths with the displayed anchor counts and distribute all
remaining nonanchors along them.  The forest has \(P-\ell\) edges and
obeys both degree caps.  This proves sharpness of the counting inequality,
not Boolean-diamond realizability. \(\square\)

### Theorem 2.2 (root-star contracted rank)

Under the hypotheses of Theorem 2.1,

\[
 r_{\widehat M/E_\rho}(S)=R-c_0=|S|-c_2.            \tag{2.5}
\]

#### Proof

After adding the full root star, all anchored components coalesce with
\(\rho\), while the \(c_0\) anchor-free components remain separate.  The
augmented graph on \(N+1\) vertices has \(c_0+1\) components, hence

\[
 r_{\widehat M}(S\cup E_\rho)=N-c_0.
\]

The root star has rank \(C\), so contraction gives

\[
 r_{\widehat M/E_\rho}(S)=N-c_0-C=R-c_0.
 \qquad\square
\]

The second equality in (2.5) follows as well from
\(R-c_0=P-K-(\ell-K+c_2)=|S|-c_2\).

This is exactly the contracted-rank row in the rooted-ear theorem.

### Corollary 2.3 (zero leave is not enough)

There are abstract cap-safe spanning linear forests with exactly \(P\)
edges and

\[
                  c_0=\left\lfloor{P\over n}\right\rfloor. \tag{2.6}
\]

Take \(c_2=\lfloor C/2\rfloor\) in (2.3).  Thus exact size,
acyclicity, and two abstract rainbow labels do not imply even
\(o(P/n)\) rooted defect.  One must force
\(c_2=K+o(P/n)\).

## 3. What item 2295ROOT quantitatively supplies

For a fixed forbidden-cycle cutoff \(L\), the largest conflict-free color
class in item 2295ROOT has a bound of the form

\[
 {\ell\over P}
 \le \delta_n+D_0^{-\alpha(L,\beta)}+O(1/L),         \tag{3.1}
\]

where

\[
 D_0=2(n+1)(n+2),\qquad
 \delta_n={2(2n+1)^2\over n(n+1)(n+2)}
          ={8\over n}+O(n^{-2}).                     \tag{3.2}
\]

No lower bound \(\alpha>1/2\) is part of the imported theorem.  The
proved fixed-\(L\) cycle deletion budget is \(O(P/L)\).  The diagonal argument
may send \(L\) to infinity slowly enough to obtain \(\ell=o(P)\), but it
does not yield

\[
                         \ell\le K+o(P/n).            \tag{3.3}
\]

Even eliminating the analytic error would leave the constant \(8\) in
(3.2), whereas \(K=(1+o(1))P/n\).

The cycle-breaking step has the wrong rooted sign.  A selected physical
cycle contains no anchor, because every cycle vertex has side degree two
and anchors have cap one.  Deleting one cycle edge produces one
anchor-free path, increasing both \(\ell\) and \(c_0\) by one.

Finally, the coloring partitions the atom set into alternative partial
matchings.  It contains no theorem about the distribution of anchors among
their physical components, and hence no control of \(c_2\).  Choosing the
largest class, choosing another class, or exchanging incidence components
between classes requires a new correlated-rank theorem.

The exact all-class deficiency/resource ledgers in handoff item 2300A are
consistent with this conclusion: they control palette and slot omissions
in aggregate, but contain no term measuring \(c_2\) or contracted-root
rank.

## 4. Exact repair cost

Let \(S'\) be obtained from \(S\) by adding \(t\) atoms without deleting
old atoms, while preserving palettes, capacities, and acyclicity.  Graphic
rank increases by at most \(t\), so

\[
                         c_0(S')\ge c_0(S)-t.          \tag{4.1}
\]

The same inequality holds for an equicardinal packet which removes \(t\)
old atoms and inserts \(t\) new atoms: deletion cannot increase contracted
rank and the insertions increase it by at most \(t\).  Thus a class merge
starting from rooted defect \(d\) must change or add at least
\(d-o(P/n)\) physical atoms to reach defect \(o(P/n)\).

For \(\ell>K\), at least \(\ell-K\) additions are unavoidable under every
anchor pairing.  When \(\ell\le K\), an equicardinal repair must reduce

\[
                         c_2-(K-\ell)=c_0.            \tag{4.2}
\]

At component level the elementary favorable move uncrosses one
double-anchor path and one empty path into two one-anchor paths.  Palette
preservation makes the supply of such moves an alternating-circuit/ear
matching problem.  It is not a consequence of the existence of all color
classes.

## 5. Synchronized punctures have no small full-host root cut

Fix the upper punctured shore.  Its physical vertices are

\[
 Y=\binom{[2n]}{n+1},\qquad |Y|=N.                   \tag{5.1}
\]

Write

\[
 T=t(Q)\subseteq\binom{[2n]}n,\qquad
 A=\{U_q:q\in Q\}\subseteq Y                         \tag{5.2}
\]

for the punctured lower labels and anchors.  The full candidate graph
\(\Gamma_Q\) has a Johnson edge \(xy\) precisely when

\[
 |x\triangle y|=2,\qquad x\cap y\notin T.            \tag{5.3}
\]

Every unpunctured \(D=x\cap y\) supplies this diamond and every physical
slot has positive capacity.  The child upper-colour map

\[
                         q\longmapsto U_q             \tag{5.4}
\]

is a bijection from the \(N\) child edges to \(Y\).  Denote its inverse at
\(y\) by \(q_y\).

### Lemma 5.1 (distinguished unpunctured facet)

Every nonanchor \(y\in Y\setminus A\) has a distinguished facet

\[
                         D_y=t_{q_y}\subset y         \tag{5.5}
\]

with \(D_y\notin T\).  The map \(y\mapsto D_y\) is injective.

#### Proof

If \(y\) is not an anchor, then the unique edge \(q_y\) is not in \(Q\).
Tail injectivity gives

\[
 q_y\notin Q\quad\Longrightarrow\quad
 t_{q_y}\notin t(Q)=T.                               \tag{5.6}
\]

The containment follows from \(t_{q_y}\subset U_{q_y}=y\), and tail
injectivity also proves injectivity of \(y\mapsto D_y\). \(\square\)

For \(\mathcal T\subseteq\binom{[2n]}n\), let

\[
 \Gamma^+(\mathcal T)=
 \left\{y\in\binom{[2n]}{n+1}:
 D\subset y\text{ for some }D\in\mathcal T\right\}.  \tag{5.7}
\]

### Theorem 5.2 (giant anchor-free component theorem)

Let \(W\) be an anchor-free connected component of \(\Gamma_Q\), and set

\[
                 \mathcal T_W=\{D_y:y\in W\}.         \tag{5.8}
\]

Then

\[
 |\mathcal T_W|=|W|,\qquad
 \Gamma^+(\mathcal T_W)=W,\qquad
 |W|\ge {1\over2}\binom{2n}{n}.                      \tag{5.9}
\]

Consequently \(\Gamma_Q\) has at most one anchor-free component.

#### Proof

The first equality is Lemma 5.1.  Fix
\(D=D_y\in\mathcal T_W\).  Since \(D\notin T\), every pair of
rank-\((n+1)\) supersets of \(D\) is a candidate physical edge.  Hence all
of \(\Gamma^+(\{D\})\) lies in the same component as \(y\), namely \(W\).
Taking the union gives \(\Gamma^+(\mathcal T_W)\subseteq W\).
Conversely every \(y\in W\) contains its distinguished
\(D_y\in\mathcal T_W\), so \(y\in\Gamma^+(\mathcal T_W)\).  Hence equality
holds and in particular

\[
 |\Gamma^+(\mathcal T_W)|\le|W|=|\mathcal T_W|.       \tag{5.10}
\]

Complementation maps \(\Gamma^+(\mathcal T_W)\) bijectively to the ordinary
lower shadow of the rank-\(n\) family

\[
 \overline{\mathcal T_W}
 =\{[2n]\setminus D:D\in\mathcal T_W\}.              \tag{5.11}
\]

Suppose

\[
 |\mathcal T_W|<{1\over2}\binom{2n}{n}
                =\binom{2n-1}{n}.                   \tag{5.12}
\]

Choose the unique real \(x\in[n,2n-1)\) with

\[
                         |\mathcal T_W|=\binom xn.    \tag{5.13}
\]

The Lovász form of Kruskal--Katona gives

\[
 |\Gamma^+(\mathcal T_W)|
 =|\partial^-\overline{\mathcal T_W}|
 \ge\binom{x}{n-1}.                                  \tag{5.14}
\]

But

\[
 {\binom{x}{n-1}\over\binom xn}
 ={n\over x-n+1}>1                                  \tag{5.15}
\]

because \(x<2n-1\), contradicting (5.10).  This proves the size bound.

Two anchor-free components would have total size at least
\(\binom{2n}{n}\), while

\[
 |Y|=N={n\over n+1}\binom{2n}{n}
      <\binom{2n}{n}.                                \tag{5.16}
\]

Thus at most one exists. \(\square\)

### Corollary 5.3 (full-host rooted deficit at most one)

Let \(b_Q\) be the number of anchor-free components of \(\Gamma_Q\).  Then

\[
                         b_Q\le1.                    \tag{5.17}
\]

Equivalently, the complete candidate edge ground has contracted graphic
rank at least \(R-1\).  Its pure graphic rooted defect is therefore
\(O(1)=o(P/n)\), uniformly for every synchronized \(Q\).

Indeed, after adjoining the root star, all components containing anchors
coalesce through \(\rho\), while the \(b_Q\) anchor-free components remain.
The augmented graph on \(N+1\) vertices has \(b_Q+1\) components and rank
\(N-b_Q\); subtracting the root-star rank \(C\) gives \(R-b_Q\).

The complement-dual proof applies verbatim to the lower shore, using the
unique child lower colour and its distinguished unpunctured cofacet.
Thus the bound one holds separately on both full candidate grounds for the
same synchronized \(Q\).

This does **not** prove a palette-compatible rooted side forest.  A
Delcourt--Postle color class is a sparse matching inside \(\Gamma_Q\), and
it can split one anchored host component into many anchor-free paths.
Theorem 5.2 removes only the full-support graphic cut.  It supplies neither
the leave bound nor the near-minimal \(c_2\) condition in (0.4).

## 6. What synchronization repairs and what remains

The numerical hypotheses in item 2295ROOT are edge-count, maximum-degree,
codegree, and conflict-degree inequalities.  By themselves they do not
encode rooted expansion: an abstract host could delete every atom incident
with \(\Theta(P/n)\) nonanchors inside the allowed \(\Theta(Pn)\)
edge-loss budget, while every upper degree bound only improves.

Theorem 5.2 proves that this abstract deletion is not induced by an actual
synchronized puncture.  The puncture and anchor banks are coupled through
the same child edge \(q_y\), so every nonanchor exports one unpunctured
facet.  This is a genuine positive correlation absent from the bare
coloring hypotheses.

The first possible obstruction is therefore a **selection cut**.  The
simultaneous two-palette matching may fail to use enough crossing edges
between the components of its own partial forest, even though the full
candidate graph has rooted deficit at most one.  Such a cut belongs to the
residual alternating-ear/cover-down system, not to \(\Gamma_Q\) alone.

### 6.1 Whole colour classes are not additive

Let \(A,B\) be two colour-class matchings with

\[
 |A|=P-\ell_A,\qquad |B|=P-\ell_B.                 \tag{6.1}
\]

Their used lower-palette sets intersect in at least

\[
                         P-\ell_A-\ell_B,            \tag{6.2}
\]

and the same holds upstairs.  Thus \(A\cup B\) has massive palette
repetition; any host matching extracted from the union must discard at
least the amount in (6.2).  Colour classes are alternative near-factors,
not additive banks.

There is one exact two-colour operation.  Form the bipartite atom-conflict
graph \(\Xi(A,B)\), joining \(a\in A\) to \(b\in B\) when they share any
host resource.  It has maximum degree at most four.  For a union \(Z\) of
connected components of \(\Xi(A,B)\), put

\[
 A^Z=(A\setminus(A\cap Z))\cup(B\cap Z).            \tag{6.3}
\]

Then \(A^Z\) is a host matching: a conflict between an inserted atom in
\(B\cap Z\) and a retained atom in \(A\setminus Z\) would join their two
components.  Both palettes and all slot capacities are preserved, and

\[
                         |A^Z|-|A|=|B\cap Z|-|A\cap Z|.           \tag{6.4}
\]

However, (6.3) can create a mixed physical cycle, and it has no automatic
contracted-rank gain.  A valid merge must separately pass ordinary graphic
independence and the root-star contracted-rank test.

### 6.2 The numerical coloring hypotheses have a sharp gap

### Proposition 6.1 (DP ledger does not imply rooted-scale cover-down)

Put

\[
 D_0=2(n+1)(n+2),\qquad
 f_n={n^3-5n^2-6n-2\over n(n+1)(n+2)},              \tag{6.5}
\]

and \(r_n=R/P=1-(n+2)/(n(n-1))\).  Then

\[
 r_n-f_n=
 {7n^3-5n^2-14n-6\over n(n-1)(n+1)(n+2)}
 ={7\over n}+O(n^{-2})>0.                           \tag{6.6}
\]

For every sufficiently large \(n\), there are four-partite four-uniform
hosts \(\mathcal H\), properly colored into \(D_0\) host matchings, such
that

\[
 |E(\mathcal H)|\ge D_0pf_n,\qquad
 \Delta(\mathcal H)\le D_0,\qquad
 \Delta_2(\mathcal H)\le1,                          \tag{6.7}
\]

but \(\nu(\mathcal H)<\lfloor r_np\rfloor\), where \(\nu(\mathcal H)\)
denotes the hypergraph matching number.  Thus even arbitrary global
mixing of every color class need not reach the rooted cardinality scale
from the numerical/coloring hypotheses alone.

#### Proof

Choose a prime \(p>D_0\), large enough that \((r_n-f_n)p>3\), and choose
\(S\subseteq\mathbb F_p\) of size \(D_0\).  Let \(V_0,V_1,V_2,V_3\) be
copies of \(\mathbb F_p\).  For \(s\in S,x\in\mathbb F_p\), take

\[
 e_{s,x}=(x,x+s,x+2s,x+3s)\in
 V_0\times V_1\times V_2\times V_3.                \tag{6.8}
\]

For fixed \(s\), these atoms form a perfect matching.  Two vertices in
distinct parts determine \(s\) uniquely, since their difference is
\((j-i)s\) and \(1,2,3\) are invertible modulo \(p\).  Hence the host is
\(D_0\)-regular, has codegree at most one, and coloring by \(s\) is proper.

Let \(z=\lfloor(1-f_n)p\rfloor\), choose a \(z\)-set
\(Z\subseteq\mathbb F_p\), and delete every \(e_{s,x}\) with \(x\in Z\).
The remaining host has \(|E|=D_0(p-z)\ge D_0pf_n\), and all degree and
codegree upper bounds persist.  Only \(p-z\) vertices in \(V_0\) are
nonisolated, so every matching has size at most

\[
 p-z\le f_np+1<\lfloor r_np\rfloor.                 \tag{6.9}
\]

Taking the forbidden-configuration system empty makes every configuration
degree condition vacuous. \(\square\)

This is an abstract four-resource counterexample, not a Boolean \(G_Q\).
Theorem 5.2 identifies the synchronized-inclusion geometry missing from it.
The proposition rules out only a formal deduction from the DP ledger and
full coloring.

## 7. Exact private-ear min--max criterion

### Theorem 7.1 (private root-ear Rado theorem)

Let \(M\) be a host matching whose physical projection is a linear forest,
let \(\mathcal U\) be a family of its anchor-free components, and let
\(\mathcal P_u\) be a finite menu of unit root-ear packets for every
\(u\in\mathcal U\).  Let \(\mathcal N\) be a matroid on
\(\mathcal P=\bigcup_u\mathcal P_u\).  Assume the following
simultaneous-realization axiom: a family of distinct representatives
\(p_u\in\mathcal P_u\), \(u\in I\subseteq\mathcal U\), is jointly
admissible **if and only if** it is independent in \(\mathcal N\); whenever
it is admissible, its packets

1. commute and give a host matching;
2. preserve both outer-palette injections and every physical/anchor cap;
3. have acyclic physical projection;
4. leave every unserved component's rooted status unchanged; and
5. raise \(r_{\widehat M/E_\rho}\) by exactly \(|I|\), rooting precisely
   the components indexed by \(I\).

Then the maximum number \(\nu\) of components which this catalogue can
root is

\[
 \nu=\min_{X\subseteq\mathcal U}
 \left(
 |{\mathcal U}\setminus X|+
 r_{\mathcal N}\left(\bigcup_{u\in X}\mathcal P_u\right)
 \right),                                           \tag{7.1}
\]

and the minimum residual empty count is

\[
 \boxed{
 |{\mathcal U}|-\nu=
 \max_{X\subseteq\mathcal U}
 \left(
 |X|-r_{\mathcal N}\left(\bigcup_{u\in X}\mathcal P_u\right)
 \right).
 }                                                   \tag{7.2}
\]

Hence the catalogue leaves at most \(s\) empty components if and only if

\[
 r_{\mathcal N}\left(\bigcup_{u\in X}\mathcal P_u\right)
 \ge |X|-s\qquad(X\subseteq\mathcal U).              \tag{7.3}
\]

#### Proof

Usable packet choices are exactly independent partial transversals of the
menus \((\mathcal P_u)\) in \(\mathcal N\).  The partial form of Rado's
theorem gives (7.1), equivalently by adjoining private dummy elements and
using the full theorem.  The simultaneous-realization axiom converts each
chosen representative into one unit of contracted-root rank without
collateral loss.  Subtracting (7.1) from \(|\mathcal U|\) gives (7.2), and
(7.3) follows. \(\square\)

For an occurrence-labelled equicardinal packet, item 2286AD gives the
local rooted test.  If it removes \(a_1,\ldots,a_t\) and inserts
\(b_1,\ldots,b_t\) in a rooted tree, put

\[
 K_{ij}=1\quad\Longleftrightarrow\quad
 a_i\text{ lies on the old-tree path joining the ends of }b_j.   \tag{7.4}
\]

The packet is rooted exactly when \(K\) is nonsingular over
\(\mathbb F_2\).  That is the local
test; (7.3) is the global packing test when packet interiors and resource
changes are private and their shared effects are represented by
\(\mathcal N\), typically a quotient graphic matroid.  A component of
\(\Xi(A,B)\) becomes an ear element only after passing (7.4), ordinary
graphic independence, and the declared privacy checks.

Thus the exact sufficient asymptotic condition for this certificate class
is

\[
 \max_{X\subseteq\mathcal U}
 \left(
 |X|-r_{\mathcal N}\left(\bigcup_{u\in X}\mathcal P_u\right)
 \right)=o(P/n),                                    \tag{7.5}
\]

together with \(\ell\le K+o(P/n)\).  A violated set in (7.3) is an exact
guarded ear-cut certificate.  The theorem is sufficient for private ears;
it is not asserted necessary for arbitrary overlapping multi-color
packets.

## 8. Correct remaining theorem

For fixed \(Q\) and cardinality \(m\), define

\[
 \eta_Q(m)=R-\max r_{\widehat M/E_\rho}(S),            \tag{8.1}
\]

where the maximum is over \(m\)-atom host matchings whose physical
projections are linear forests and hence preserve both outer injections
and all slot capacities.  Then \(\eta_Q(m)\) is exactly the minimum number
of anchor-free components at size \(m\).

Item 2295ROOT proves that the feasible set in (8.1) is nonempty for
\(m=P-o(P)\).  Theorem 5.2 proves the full-ground graphic relaxation has
defect at most one.  A palette-compatible asymptotic rooted upgrade still
requires

\[
 \boxed{
   \text{for every synchronized common }Q,\quad
   \text{there is }\ell\le K+o(P/n)
   \text{ with }\eta_Q(P-\ell)=o(P/n).
 }                                                     \tag{8.2}
\]

A sufficient color-reservoir theorem must provide both:

1. a cover-down reducing the palette leave to at most \(K+o(P/n)\); and
2. palette-preserving alternating ears reducing
   \(c_2-(K-\ell)_+\) to \(o(P/n)\) while retaining acyclicity.

In rooted-ear language, these operations must raise the contracted graphic
rank from \(R-c_0\) to \(R-o(P/n)\).  Theorem 5.2 removes the simplest
ambient graphic cut, but the two partition palettes and physical slot
capacities remain correlated constraints.  Theorem 7.1 resolves the
declared private-ear subclass exactly; without its simultaneous-realization
axiom, an ordinary one-matroid Rado inequality does not resolve the
overlapping packet system.

## 9. Audit ledger

The following points were independently checked against item 2295ROOT by
a separate audit lane:

1. the identity \(c_0=\ell-K+c_2\);
2. the absence of any hidden \(o(P/n)\) leave rate in the imported
   coloring theorem;
3. the proved fixed-\(L\) cycle-deletion budget \(O(P/L)\);
4. the fact that deleting a selected cycle creates an anchor-free path;
5. the absence of an anchor-component distribution theorem in the full
   coloring.

The initially proposed large full-shadow wall was adversarially rejected:
synchronization supplies the distinguished facet in Lemma 5.1.  The
Lovász--Kruskal--Katona proof above is the corrected exact host theorem.

The prime-field construction, the two-colour conflict-component toggle,
and the private-ear Rado formula were separately adversarially checked.
The scope distinction is load-bearing: Proposition 6.1 refutes an
inference from the analytic coloring hypotheses, whereas Theorem 5.2 is a
positive theorem for every actual synchronized Boolean host.

No finite search, SAT computation, or web lookup is used.
