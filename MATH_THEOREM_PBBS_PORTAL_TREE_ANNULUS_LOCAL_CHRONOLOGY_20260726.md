# PBBS portal-tree chronology: unconditional local repair of the Gaussian annulus

Date: 2026-07-26

Method: pure mathematics only.  The audited PBBS orbit divisibility and
all-depth fan-support theorems are used as named inputs.

**Literal-word correction.**  The theorem below is a Johnson-walk theorem
only.  Consecutive intersections and unions of owner states are not, by
themselves, literal contiguous ORs.  The delay-\(H\) factorization claimed
in the original interpretation is retracted.  See
`MATH_AUDIT_PBBS_PORTAL_TREE_CHRONOLOGY_NOT_LITERAL_WORD_20260726.md` and
the successor
`MATH_THEOREM_PBBS_PORTAL_LITERAL_DELAY_EQUIVALENCE_AND_TWO_POINT_NO_GO_20260726.md`.

> **Correction.** This note proves the Johnson-walk chronology theorem,
> but not a literal contiguous-OR word of the same length. Consecutive
> intersections in a Johnson walk are not automatically ORs of literal
> factor letters, and the forward/backward portal excursions violate
> delay-\(H\) safety. The coefficient-one annulus claim is retracted; see
> `MATH_AUDIT_PBBS_PORTAL_TREE_CHRONOLOGY_NOT_LITERAL_WORD_20260726.md`.

## 0. Outcome

The earthmover obstruction rules out polishing an arbitrary
lower-complete Hamilton cycle across a Gaussian repeat--hole gap.  A PBBS
base avoids that problem by selecting the chronology before imposing one
component.

Put

\[
 n=2m+1,\qquad
 \mathcal M=\binom{[n]}m,\qquad
 W=|\mathcal M|,
 \qquad
 B={W\over2m+1}=\operatorname {Cat}_m.              \tag{0.1}
\]

Let \(f\) be the canonical PBBS permutation and \(g=f^2\).  The edges

\[
                         A--gA\qquad(A\in\mathcal M) \tag{0.2}
\]

form the canonical PBBS spanning \(2\)-factor \(F_{\rm P}\) of
\(J(2m+1,m)\).  Every component has length divisible by \(2m+1\), so its
number \(c_m\) of components satisfies

\[
                         c_m\le B.                  \tag{0.3}
\]

For every integer \(H<m\), there is an explicit closed Johnson walk
\(\mathscr W_H\) with

\[
 \boxed{
 |\mathscr W_H|
   \le W+2(c_m-1)+8H(c_m-1)
   \le W+(8H+2)B.}                                  \tag{0.4}
\]

It contains, as a consecutive subwalk, every directed PBBS window

\[
                         (A,gA,\ldots,g^qA)          \tag{0.5}
\]

for every \(A\in\mathcal M\) and every \(1\le q\le H\).

Consequently the intersection and union targets of \(\mathscr W_H\) have
complete support at every depth \(q\le H\):

\[
 \boxed{
 \begin{aligned}
 \left\{\bigcap_{i=0}^qX_i:
       (X_0,\ldots,X_q)\subset\mathscr W_H\right\}
     &\supseteq\binom{[n]}{m-q},\\
 \left\{\bigcup_{i=0}^qX_i:
       (X_0,\ldots,X_q)\subset\mathscr W_H\right\}
     &\supseteq\binom{[n]}{m+q}.
 \end{aligned}}                                    \tag{0.6}
\]

At Gaussian depth \(H=\lfloor A\sqrt m\rfloor\), with fixed \(A>0\),

\[
                         |\mathscr W_H|
                   =W+O_A(W/\sqrt m)=W+o(W).        \tag{0.7}
\]

Thus PBBS annulus defects are unconditionally locally transportable in a
single legal Johnson chronology: they occur only at \(O(B)\) component
portals, and one radius-\(H\) closed excursion at each portal repairs all
depths \(q\le H\) simultaneously.  There is no multiplication by the
number of depths and no Gaussian-distance target transport.

The scope is exact.  The chronology is a closed Johnson **walk**, not a
Hamilton cycle: bridge edges and repair blocks are revisited.  If simple
Hamilton ownership is mandatory, the unresolved PBBS paired-matching
connector theorem remains necessary.  For chronology length only, where
\(o(W)\) repeated owners are allowed, (0.7) closes the base-selection
annulus gate.  It does not close the coefficient-one literal-word gate.

## 1. The PBBS factor and its complete fan support

The PBBS map \(f\) is a permutation of \(\mathcal M\), and consecutive
states \(A,fA\) are disjoint.  Its square satisfies the Johnson update

\[
                         gA=A-\{b(A)\}+\{a(A)\}.     \tag{1.1}
\]

Hence (0.2) is a Johnson edge.  The permutation cycles of \(g\) give a
simple spanning \(2\)-factor \(F_{\rm P}\).

The audited PBBS site-homomesy theorem implies that every \(f\)-orbit has
length divisible by \(n=2m+1\).  The same lower bound \(n\) holds for every
\(g\)-component in the centered Johnson factor.  Since the components
partition \(W\) owners, this gives (0.3).

For a directed \(q\)-edge window of one \(g\)-cycle, put

\[
 \Theta_q^-(A)=\bigcap_{i=0}^qg^iA,
 \qquad
 \Theta_q^+(A)=\bigcup_{i=0}^qg^iA.                \tag{1.2}
\]

The audited all-depth PBBS corridor theorem gives, for every
\(1\le q\le m\),

\[
 \{\Theta_q^-(A):A\in\mathcal M, |\Theta_q^-(A)|=m-q\}
       =\binom{[n]}{m-q},                            \tag{1.3}
\]

and the exact cross-shore identity gives

\[
 \{\Theta_q^+(A):A\in\mathcal M, |\Theta_q^+(A)|=m+q\}
       =\binom{[n]}{m+q}.                            \tag{1.4}
\]

Only support, not a multiplicity bound, is needed below.

## 2. Connecting the PBBS components by doubled portals

Contract every component of \(F_{\rm P}\) to one vertex.  Because the host
Johnson graph \(J(2m+1,m)\) is connected, the resulting component quotient
is connected.  Choose a spanning tree \(T\) of that quotient.

For every tree edge \(CC'\), choose one physical Johnson edge

\[
                         x_{CC'}y_{CC'},
 \qquad x_{CC'}\in C,\quad y_{CC'}\in C'.          \tag{2.1}
\]

Take every PBBS factor edge once and take two parallel copies of every
chosen bridge (2.1).  The resulting multigraph \(G_T\) is connected.  Every
owner has even degree: it has its two PBBS factor incidences, and every
incident tree bridge contributes two more incidences.  Therefore \(G_T\)
has an Euler circuit.

More concretely, root \(T\).  Traverse the root PBBS cycle in its directed
order.  At the portal of a child component, cross the bridge, recursively
traverse the child subtree, cross the same bridge back, and continue around
the parent cycle.  This gives a closed Johnson walk \(\mathscr E_T\) of
length

\[
                         |\mathscr E_T|=W+2(c_m-1). \tag{2.2}
\]

Every PBBS factor edge occurs once.  The only PBBS consecutive windows which
may fail to occur consecutively in \(\mathscr E_T\) are those crossing a
vertex at which a bridge excursion was inserted.

Call such a vertex a portal.  Each tree bridge has two endpoints, so the
number \(p_T\) of distinct portals satisfies

\[
                         p_T\le2(c_m-1).             \tag{2.3}
\]

Several bridges sharing one endpoint only reduce this count.

## 3. One local excursion restores every depth at one portal

Fix a portal \(v\) on a directed PBBS component.  Since every PBBS
component has length at least \(2m+1>2H\), there is a well-defined directed
PBBS block

\[
 P_v=(v_{-H},v_{-H+1},\ldots,v,\ldots,v_H)         \tag{3.1}
\]

of \(2H\) edges, centred at \(v\).

At any visit to \(v_{-H}\) in the current closed walk, insert the closed
excursion

\[
                         P_v\,P_v^{-1}.              \tag{3.2}
\]

This is a legal Johnson walk, begins and ends at the same owner, and adds
exactly \(4H\) edge steps.  Its forward half contains every directed PBBS
window of length at most \(H\) which crosses the portal \(v\).

Perform (3.2) once for every distinct portal.  The resulting walk is
\(\mathscr W_H\), and (2.2)--(2.3) give

\[
\begin{aligned}
 |\mathscr W_H|
 &\le W+2(c_m-1)+4Hp_T\\
 &\le W+2(c_m-1)+8H(c_m-1),                         \tag{3.3}
\end{aligned}
\]

which is (0.4).

### Theorem 3.1 (simultaneous window restoration)

Every directed PBBS window of every length \(q\le H\) occurs consecutively
in \(\mathscr W_H\).

#### Proof

Take a PBBS window \(Q=(A,gA,\ldots,g^qA)\).

If its interior crosses no portal insertion, the recursive traversal of its
PBBS component follows the original directed cycle order throughout \(Q\),
so \(Q\) already occurs in \(\mathscr E_T\).

If it crosses a portal \(v\), then all its vertices lie between
\(v_{-H}\) and \(v_H\), because \(q\le H\).  Hence \(Q\) occurs in the
forward half of the repair excursion (3.2). \(\square\)

One excursion repairs the entire nested family of depths at its portal.
Charging a separate length-\(q\) repair at every depth would incorrectly
introduce an \(H^2c_m\) cost.

## 4. Complete annulus support

Apply Theorem 3.1 to the PBBS witnesses in (1.3)--(1.4).  Every witness
window survives either in the main portal-tree traversal or in one of the
local repair excursions.  This proves (0.6).

For fixed \(A>0\), set \(H=\lfloor A\sqrt m\rfloor\).  From (0.3)--(0.4),

\[
\begin{aligned}
 |\mathscr W_H|-W
 &\le(8H+2){W\over2m+1}\\
 &=O_A(W/\sqrt m)=o(W),                              \tag{4.1}
\end{aligned}
\]

which proves (0.7).

The construction is uniform over every fixed Gaussian annulus
\(q\le A\sqrt m\).  A slowly growing \(A=A(m)\) is also allowed whenever

\[
                         A(m)=o(\sqrt m),             \tag{4.2}
\]

because then \(H=o(m)\) and the relative overhead remains \(O(A/\sqrt m)\).

## 5. Relation to paired-matching Hamiltonization

The portal-tree walk solves chronology coverage but repeats bridge and
repair owners.  If a simple Hamilton cycle is required, return to the PBBS
paired-matching factor.  A component-merging alternating switch preserves
the upper ledger exactly.  If it changes the second matched facet at an
upper slot \(U\), the old and new lower colours are

\[
 f_0(U)\cap f_1(U),
 \qquad
 f_0(U)\cap f_1'(U).                                 \tag{5.1}
\]

Both are \((m-1)\)-subsets of the same middle owner \(f_0(U)\), so their
lower-layer Johnson distance is at most one.  Thus every changed paired
slot carries a literal radius-one lower-defect transport certificate, while
upper defects remain zero.

If the missing PBBS connector atlas supplies a Hamiltonization changing
\(k=O(B)\) slots, the same portal-neighbourhood argument gives an alternative
simple-base chronology with only

\[
                         O(Hk)=O_A(W/\sqrt m)         \tag{5.2}
\]

Gaussian-window repairs.  This is conditional only because sparse
Hamiltonization of the PBBS factor is not currently proved.

The unconditional walk construction avoids that gate by doubling the
component-tree bridges.  It is therefore the correct moving-frame fallback
when coefficient-one length, rather than exact Hamilton simplicity, is the
objective.

## 6. Quantitative obstruction boundary

For this construction the exact overhead parameter is the number of
portals, not the distance between target defects.  A base factor with
\(c\) components and minimum component length greater than \(2H\) has the
same portal-tree construction with cost

\[
                         W+O(Hc).                    \tag{6.1}
\]

Thus the sharp sufficient scale for coefficient one is

\[
                         Hc=o(W).                    \tag{6.2}
\]

PBBS satisfies this throughout every fixed Gaussian window because

\[
                         Hc_m\le H{W\over2m+1}
                              =O_A(W/\sqrt m).       \tag{6.3}
\]

Therefore no component-count or Gaussian-annulus obstruction exists for
PBBS-type bases at the level of closed Johnson chronologies.  Any remaining
obstruction must explicitly demand simple Hamilton ownership, or must concern
target conditions not represented by consecutive PBBS fan intersections
and unions.
