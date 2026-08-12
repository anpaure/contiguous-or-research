# Lane K7: dependent Catalan packet cuts and the exact multidepth NAE gate

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname{Cat}_m.
\]

Let \(F_m\) be the canonical MSW factor and let \(v_m\) be the maximum
number of pairwise root-disjoint contextual size-two packets from the audited
packet matching. Thus

\[
 v_m=\left(\frac{11}{72}+o(1)\right)B.                 \tag{0.1}
\]

This report proves that a *dependent* choice of the packet sides really does
escape the identity-region defect in the previous coarse-turnover theorem.
For \(m\ge5\), there exist a coordinate transposition \(\rho\) which lies
outside the full native contextual palette and an integral packet-cube
vertex for which the pulled-back fresh \(\rho\)-overlay has at least

\[
 \boxed{
 s_m\ge
 \frac{v_m(2n-4)m(m-4)}
      {4(2m^2+1)}
 =\left(\frac{11}{288}-o(1)\right)W
 }                                                        \tag{0.2}
\]

genuine switched-to-unswitched commutator seams.  These seams lie in fresh
components whose union contains at least

\[
 \boxed{
 |Z_m|\ge \frac{2s_m}{n-3}
 =\left(\frac{11}{144}-o(1)\right)B
 }                                                        \tag{0.3}
\]

left wreaths.  Every counted seam starts at a middle root genuinely moved by
the packet transposition; none is a singleton--singleton or fixed-root gauge
edge.  Both (0.2) and (0.3) are literal statements about integral exact
wreath factors.

The proof uses an oriented, pinned cut.  It is important not to confuse two
different packet facts.  The signed rank-\(r\) histogram of a packet has
support eight for most lower ranks because of cancellation among four rows.
The piecewise involution on the middle roots has support \(2n-4\), not eight.

The multidepth selection problem after (0.2) has an exact solution under a
checkable acyclicity hypothesis.  For any collection of lower and upper
ranks, the unresolved missing-target pairs form NAE clauses on the same fresh
component variables.  If deletion of clauses of total weight \(R\) makes the
clause--component incidence graph a forest, one integral component signing
satisfies every remaining clause.  There is also an exact floor-corrected
version: with unit component coefficients, one signing attains every
transposition-orbit parity floor off the deleted rows, and its excess is at
most

\[
 \frac12\sum_{a\in\mathcal R}w_a(L_a^2-\pi_a).          \tag{0.4}
\]

In particular, if the exact orbit-profile floors and the right side of (0.4),
with weights \(1/c_q\), are \(o(W)\), then the sum of missing targets in the
whole chosen depth band is \(o(W)\).  This is a quantitative lemma which
would compose into the coefficient-one transfer.

The new seam reservoir does **not** prove those hypotheses.  There is a sharp
counting obstruction to the most direct forest implementation.  A fresh
overlay has at most \(B\) component variables.  A forest incidence graph can
contain at most \(B-1\) clauses of width at least two.  Therefore, if
\(\delta W\) useful split clauses are to be treated in one round, every
feedback-row forest proof must discard at least

\[
 \delta W-B=(\delta-o(1))W                              \tag{0.5}
\]

of them.  Bounded congestion alone cannot replace acyclicity: replicated odd
cycles give width-two NAE systems of natural variable congestion \(2n\) with
an unavoidable one-third violated fraction.  This last example is a logical
obstruction to a degree-only inference, not an asserted exact-factor
counterexample.

Finally, for every prepared factor and every \(\rho\), only \(4B\) actual
\(\rho\)-owner incidences are directly aligned with their first-shadow cores.
Thus the \(\Theta(W)\) seams in (0.2) still require a genuinely nonlocal
component-containment theorem before they yield \(\Theta(W)\) useful
hole--duplicate clauses.  This is the precise proved/conditional boundary.

## 1. The exact middle-root support of a contextual packet

After the universal rotation and relabelling, one contextual packet has
omitted-label words

\[
\begin{array}{ll}
 C=(\delta,\beta,\gamma,\alpha,T),
 &D=(\beta,\alpha,\delta,\gamma,T),\\
 C'=(\delta,\gamma,\beta,\alpha,T),
 &D'=(\gamma,\alpha,\delta,\beta,T),
\end{array}                                             \tag{1.1}
\]

and its packet transposition is \(\tau=(\beta\ \gamma)\).  Thus
\(C'=\tau C\) and \(D'=\tau D\).

For an omitted-label word \(q=(q_0,\ldots,q_{n-1})\), the cyclic rank-\(r\)
intervals are the step-two windows

\[
 \{q_i,q_{i+2},\ldots,q_{i+2r-2}\}.                    \tag{1.2}
\]

Multiplication of positions by \(2^{-1}=m+1\pmod n\) turns (1.2) into
ordinary cyclic windows.  In \(C\), the positions of \(\beta,\gamma\) become
\(m+1,1\), at shorter cyclic distance \(m\).  In \(D\), they become
\(0,m+2\), at shorter cyclic distance \(m-1\).

Two points at shorter distance \(d\le m\) in an odd \(n\)-cycle are separated
by exactly \(2d\) cyclic \(m\)-windows.  Indeed, on each of the two boundary
arcs there are exactly \(d\) starting positions for which the window contains
one endpoint and not the other.  Therefore \(\tau\) moves

\[
 2m=n-1\quad\hbox{middle roots of }C,
 \qquad
 2(m-1)=n-3\quad\hbox{middle roots of }D.              \tag{1.3}
\]

The two rows of one exact factor own disjoint middle-root families.  Hence if
\(U_i\) is the complete \(2n\)-root cell of packet \(i\), then its moved set

\[
 M_i=\{X\in U_i:\tau_iX\ne X\}
\]

has the exact size

\[
 \boxed{|M_i|=2n-4.}                                   \tag{1.4}
\]

There are only four fixed roots.  The occasionally used loopless owner-degree
bound \(n-3\) is a different quantity: in the distance-\(m\) row, two moved
root incidences form one owner loop and are omitted from that degree.  It must
not be substituted for (1.4).

## 2. A directed dependent cut gives linearly many genuine seams

Take \(v=v_m\) pairwise root-disjoint packets.  Their cells \(U_i\) are
disjoint and \(\tau_iU_i=U_i\).  Every root outside their union belongs to a
unique unmatched row cell.  For packet bits
\(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_v)\), define the piecewise
involution of the middle layer

\[
 \alpha_\varepsilon X=
 \begin{cases}
  \tau_i^{\varepsilon_i}X,&X\in U_i,\\
  X,&X\notin\bigcup_iU_i.
 \end{cases}                                           \tag{2.1}
\]

Disjointness and cell invariance make (2.1) a bijective involution.  Choosing
the corresponding packet sides gives a literal integral exact factor
\(F_\varepsilon\).

Fix a packet \(i\) and a moved root \(X\in M_i\).  In the Johnson graph
\(J(n,m)\), the root \(X\) has degree

\[
 m(m+1).                                                \tag{2.2}
\]

At most \(2n-1\) of its neighbours lie in the same cell \(U_i\).  It therefore
has at least

\[
 d_*:=m(m+1)-(2n-1)=m^2-3m-1                           \tag{2.3}
\]

neighbours in other cells.  Assume \(m\ge4\), so \(d_*>0\).

Orient every such external edge away from the moved packet root.  Its endpoint
has the form \(\rho X\) for a unique coordinate transposition \(\rho\).  Let
\(A_\rho\) be the resulting set of directed arcs of colour \(\rho\).  Equations
(1.4) and (2.3) give

\[
 \sum_\rho |A_\rho|
 \ge v(2n-4)(m^2-3m-1).                                \tag{2.4}
\]

There are \(\binom n2=nm\) transpositions.  We require the new colour to lie
outside the full native contextual palette

\[
 \mathcal T_m=\{(2s+2\ \ 2s+3):0\le s\le m-2\},
 \qquad |\mathcal T_m|=m-1.                            \tag{2.5}
\]

For a fixed colour \(\rho\), every moved root is the tail of at most one directed
\(\rho\)-arc.  Consequently

\[
 |A_\rho|\le v(2n-4).                                  \tag{2.6}
\]

Deleting all native colours from (2.4) leaves at least

\[
 v(2n-4)m(m-4)                                        \tag{2.7}
\]

arcs on \(\binom n2-(m-1)=2m^2+1\) colours. Hence, for \(m\ge5\), some
\(\rho\notin\mathcal T_m\) satisfies

\[
 |A_\rho|\ge
 \frac{v(2n-4)m(m-4)}{2m^2+1}.                        \tag{2.8}
\]

Pin every unmatched cell to bit zero and choose the \(v\) packet bits
independently and fairly.  A directed arc from packet cell \(i\) to another
matched cell \(j\) is called active when

\[
 \varepsilon_i=1,\qquad \varepsilon_j=0.              \tag{2.9}
\]

It is active with probability \(1/4\).  An arc ending in an unmatched cell is
active when \(\varepsilon_i=1\), with probability \(1/2\).  Thus the expected
number of active arcs is at least \(|A_\rho|/4\).  Conditional expectation
gives a deterministic packet-side assignment with

\[
 s\ge |A_\rho|/4.                                     \tag{2.10}
\]

It remains to verify that these are real commutator seams, rather than a cut
in an artificial cell graph.  Identify every chosen child packet row with its
parent row.  The freshly recomputed \(\rho\)-owner relation then pulls back to

\[
 o_F(Y)\sim o_F(\theta_\varepsilon Y),
 \qquad
 \theta_\varepsilon=\alpha_\varepsilon\rho
                     \alpha_\varepsilon.             \tag{2.11}
\]

Consider an active arc \(X\to X'=\rho X\), with \(X\in M_i\).  Put
\(Y=\tau_iX\).  Since the source bit is one and the destination bit is zero,

\[
 \alpha_\varepsilon Y=X,
 \qquad
 \alpha_\varepsilon X'=X',
 \qquad
 \theta_\varepsilon Y=X'.                            \tag{2.12}
\]

The roots \(Y\) and \(X'\) lie in different cells.  Thus the edge in (2.12)
is loopless at the owner level.  It is also a genuine commutator seam:

\[
 \theta_\varepsilon Y=X'=\rho X\ne\rho Y,             \tag{2.13}
\]

because \(X\ne Y\).  Since the two roots are in different cells, their two
owners are distinct, so this is a loopless edge of the fresh owner graph.  If
both endpoints are moved packet roots, only the
orientation from bit one to bit zero is active.  Consequently two active arcs
cannot be the two orientations of one old orbit.  More generally,
\(\alpha_\varepsilon\) bijects the old \(\rho\)-orbits onto the fresh
\(\theta_\varepsilon\)-orbits, since

\[
 \theta_\varepsilon(\alpha_\varepsilon X)
 =\alpha_\varepsilon(\rho X).
\]

Thus distinct old orbits cannot collide after pullback.  Combining
(2.8)--(2.10)
proves (0.2), including its factor \(1/4\).

Let \(Z\) be the union of the left wreath sets of fresh \(\rho\)-components
which contain an active seam.  A row has loopless degree at most \(n-3\) in a
transposition overlay.  Every active seam contributes two distinct owner
incidences.  Therefore

\[
 2s\le(n-3)|Z|.                                        \tag{2.14}
\]

For completeness, the degree bound in (2.14) is exact at the needed level.
If the two labels of \(\rho\) have shorter cyclic distance \(d\le m\) in one
row, there are \(2d\) middle-root incidences moved by \(\rho\).  When
\(d\le m-1\), all possible loopless incidences are among these; when \(d=m\),
two incidences form one owner loop.  Hence the loopless degree is at most

\[
 2\min(d,m-1)\le2m-2=n-3.                              \tag{2.15}
\]

which proves (0.3).  More quantitatively, for every \(L\ge1\), either one
mixed fresh component contains more than \(L\) left rows, or there are at least

\[
 \left\lceil\frac{|Z|}{L}\right\rceil
\]

fresh mixed components.

This theorem removes the earlier possibility that every averaged crossing
edge is singleton--singleton identity turnover.  It does not say that the
fresh mixed components act nontrivially at a prescribed lower rank.

## 3. Exact multidepth NAE forest lemma

Let \(H\) be any exact factor and fix a coordinate transposition \(\rho\).
Write \(K\) for the genuine connected components of the middle-owner overlay
of \(H\) and \(\rho H\).  Choosing independently one side of every component
always gives another integral exact factor.

At any rank \(r\), put

\[
 x_{K,r}(S)=|\{C\in L_K:S\text{ is a cyclic }r
                         \text{-interval of }C\}|.     \tag{3.1}
\]

For a nonfixed target pair \(p=\{S,\rho S\}\), a component containing
occurrences on both sides covers both targets for every choice.  If no
component does so, every active component supplies occurrences to one side
only.  Its side choice is a literal, and both targets are covered exactly when
the effective component literals are not all equal.

Across an arbitrary collection \(\mathscr R\) of ranks, let \(\mathcal Q\)
be the set of these unresolved pairs having clause width at least two.  Use
the same component variables at every rank, and form the bipartite incidence
graph

\[
 \mathcal I=(\mathcal Q,\mathcal K;E),                 \tag{3.2}
\]

where \(pK\in E\) exactly when component \(K\) supplies one side of \(p\).

### Theorem 3.1 (dependent forest signing)

Suppose deleting a set \(\mathcal R\subseteq\mathcal Q\) of clause vertices
makes \(\mathcal I\) a forest.  Then there is one component-side assignment
which satisfies every NAE clause in \(\mathcal Q\setminus\mathcal R\)
simultaneously at all ranks.

#### Proof

Root each component of the remaining incidence forest at a variable vertex
and choose the root variable arbitrarily.  When a clause is first reached, its
parent variable is already assigned.  Its width is at least two, so it has a
child variable.  Choose one child so that its effective literal is opposite to
the parent's effective literal, and assign any other immediate children
arbitrarily.  The clause is now NAE-satisfied.  Continue away from the root.
No variable receives two assignments because the incidence graph is a forest.
This assigns all variables and satisfies every retained clause. \(\square\)

For rank \(r\), let

* \(H_{{\rm fix},r}\) be the number of \(\rho\)-fixed holes;
* \(P_{0,r}\) be the nonfixed pairs which are holes on both sides;
* \(L_{1,r}\) be the unresolved width-one pairs, each of which always leaves
  one hole.

With arbitrary nonnegative rank weights \(w_r\), Theorem 3.1 gives the exact
deterministic bound

\[
 \boxed{
 \sum_{r\in\mathscr R}w_rM_r(H_\eta)
 \le
 \sum_{r\in\mathscr R}w_r
       (H_{{\rm fix},r}+2|P_{0,r}|+L_{1,r})
 +\sum_{p\in\mathcal R}w_{r(p)}.
 }                                                       \tag{3.3}
\]

Every factor in (3.3) is literal and integral.  There is no rankwise choice of
different signs.

If \(V,E,\kappa\) are the vertex count, edge count, and component count of
\(\mathcal I\), its cyclomatic number is

\[
 \xi=E-V+\kappa.                                       \tag{3.4}
\]

Choose a spanning forest.  For every nonforest edge, mark its clause endpoint
and delete all marked clauses.  The remaining graph is a subgraph of the
spanning forest.  Hence one may always choose

\[
 |\mathcal R|\le\xi.                                   \tag{3.5}
\]

This is an exact, but useful only when \(\xi\) is small, feedback-row bound.

## 4. Exact floor-corrected forest lemma

Fix a depth \(q\), put \(r=m-q\), and write

\[
 N_q=\binom nr,\qquad W=c_qN_q+b_q,
 \qquad 0\le b_q<N_q.                                 \tag{4.1}
\]

For an integral rank histogram \(\mu_q\), define

\[
 f_c(t)=(t-c)(t-c-1),
 \qquad
 Q_q(\mu_q)=\sum_Sf_{c_q}(\mu_q(S)).                  \tag{4.2}
\]

This energy is nonnegative and vanishes exactly on the floor/ceiling loads
\(c_q,c_q+1\).

For a nonfixed \(\rho\)-pair \(p=\{S,T\}\), set

\[
 \ell_p=\mu_q(S)+\mu_q(T),
 \quad
 z_{pK}=x_{K,r}(S)-x_{K,r}(T),
 \quad
 \pi_p=\ell_p\bmod2.                                  \tag{4.3}
\]

Use signs \(\eta_K\in\{\pm1\}\), with plus denoting the left side.  Then

\[
 D_p(\eta)=\mu_{q,\eta}(S)-\mu_{q,\eta}(T)
           =\sum_K\eta_Kz_{pK}.                       \tag{4.4}
\]

The pair total \(\ell_p\) is invariant.  Direct substitution of
\((\ell_p\pm D_p)/2\) into (4.2) gives

\[
\begin{aligned}
 &f_{c_q}(\mu_{q,\eta}(S))
  +f_{c_q}(\mu_{q,\eta}(T))\\
 &\qquad=
 \frac{\ell_p^2+D_p(\eta)^2}{2}
 -(2c_q+1)\ell_p+2c_q(c_q+1).                         \tag{4.5}
\end{aligned}
\]

Because \(D_p\equiv\ell_p\pmod2\), the smallest arithmetically possible
square is \(\pi_p\).  Define the exact orbit-profile floor

\[
\begin{aligned}
 \mathcal B_{q,\rho}:={}&
 \sum_{\rho S=S}f_{c_q}(\mu_q(S))\\
 &+\sum_{p}
 \left[
  \frac{\ell_p^2+\pi_p}{2}
  -(2c_q+1)\ell_p+2c_q(c_q+1)
 \right],                                             \tag{4.6}
\end{aligned}
\]

where the second sum runs over nonfixed pairs.  Then the exact decomposition is

\[
 \boxed{
 Q_q(H_\eta)=\mathcal B_{q,\rho}
 +\frac12\sum_p(D_p(\eta)^2-\pi_p).
 }                                                       \tag{4.7}
\]

Now take any set of ranks, with nonnegative weights \(w_q\), and form the
single bipartite incidence graph whose row vertices are all \((q,p)\) with
\(z_{pK}\ne0\).  Assume

\[
 z_{pK}\in\{-1,0,1\}.                                  \tag{4.8}
\]

Let deletion of row set \(\mathcal R\) make this incidence graph a forest,
and put

\[
 L_{q,p}=\sum_K|z_{pK}|.                                \tag{4.9}
\]

On a forest, one common signing attains
\(D_p^2=\pi_p\) at every retained row.  To see this, root at a variable.  At a
row whose parent sign is fixed, choose its child signs so that the sum of its
unit signed coefficients is zero when its degree is even and \(\pm1\) when its
degree is odd.  Reversing all child choices if necessary matches the parent
contribution.  Acyclicity prevents conflicts.

At a deleted row, every signing obeys \(|D_p|\le L_{q,p}\).  Therefore some
integral exact factor satisfies

\[
 \boxed{
 \sum_qw_qQ_q(H_\eta)
 \le
 \sum_qw_q\mathcal B_{q,\rho}
 +\frac12\sum_{(q,p)\in\mathcal R}
     w_q(L_{q,p}^2-\pi_p).
 }                                                       \tag{4.10}
\]

This preserves all integer parity floors exactly.  No continuous rounding is
used.

The coefficient-one relevance is immediate and quantitative.  For an integer
\(t\),

\[
 f_c(t)\ge2(c-t)_+,
 \qquad
 f_c(t)\ge2(t-c-1)_+.                                  \tag{4.11}
\]

Every missing target contributes \(c_q\) to the first deficit.  Hence

\[
 \boxed{M_q(H_\eta)\le \frac{Q_q(H_\eta)}{2c_q}.}       \tag{4.12}
\]

Taking \(w_q=1/c_q\) in (4.10), if

\[
 \sum_q\frac{\mathcal B_{q,\rho}}{c_q}=o(W),
 \qquad
 \sum_{(q,p)\in\mathcal R}
       \frac{L_{q,p}^2-\pi_p}{c_q}=o(W),               \tag{4.13}
\]

then

\[
 \sum_qM_q(H_\eta)=o(W).                               \tag{4.14}
\]

The same statement applies to upper ranks, and to lower and upper ranks in
one common incidence graph.  Thus (4.13) is a genuine multidepth lemma which
composes quantitatively into the missing-window transfer.  Neither condition
in (4.13) is supplied by the seam count (0.2).

## 5. Why a forest or degree-only argument cannot finish one round

Let \(t\) be the number of fresh overlay components.  Since their nonempty
left row sets partition the \(B\) rows of an exact factor,

\[
 t\le B.                                                \tag{5.1}
\]

Suppose \(C\) useful split hole--duplicate pairs are represented as NAE
clauses, each incident with at least two component variables.  If their full
incidence graph is a forest, then

\[
 2C\le E\le C+t-1,
\]

and consequently

\[
 \boxed{C\le t-1\le B-1.}                              \tag{5.2}
\]

More generally, if deletion of \(R\) clause vertices makes it a forest, then

\[
 \boxed{R\ge C-t\ge C-B.}                              \tag{5.3}
\]

Thus a feedback-row forest proof cannot process \(C=\delta W\) useful pairs
with \(o(W)\) feedback loss in one overlay.  This does not say the NAE instance
is unsatisfiable; it says that near-acyclicity is quantitatively incompatible
with a linear useful-clause supply and only \(B=W/n\) component variables.

Nor does a natural bounded-congestion hypothesis imply near-perfect NAE
satisfiability.  Partition \(t=3a\) variables into triples.  On every triple,
place \(R_0\) copies of each of the three equal-literal width-two clauses

\[
 \varepsilon_1\ne\varepsilon_2,
 \qquad
 \varepsilon_2\ne\varepsilon_3,
 \qquad
 \varepsilon_3\ne\varepsilon_1.                       \tag{5.4}
\]

Every variable has clause congestion \(2R_0\), there are \(tR_0\) clauses,
and every assignment violates at least \(aR_0=(tR_0)/3\) clauses.  Equality is
attained by a two-against-one colouring of every triangle.  Taking
\(R_0=n\) gives \(\Theta(W)\) clauses on \(\Theta(B)\) variables, maximum
congestion \(2n\), and an unavoidable \(\Theta(W)\) residual.

The example (5.4) is an exact CSP/holonomy obstruction.  It is not claimed to
arise from a wreath factor.  Its implication scope is precise: component
count, clause width, and bounded incidence congestion alone cannot justify the
needed dependent selection.  One must prove an additional signed-cycle
consistency, near-bipartiteness, low-frustration, or genuine higher-width
property for the *actual* Catalan component incidence.

## 6. The remaining nonlocal leakage gate

For any exact factor and fixed \(\rho=(a\ b)\), a moved middle-root orbit has
the unique core form

\[
 \{S\cup\{a\},S\cup\{b\}\}.                            \tag{6.1}
\]

For the core \(S\) to occur as a first-shadow interval in the owner row of
\(S\cup\{a\}\), the coordinate \(a\) must be one of the two boundary labels
of that middle window.  In one cyclic row a fixed coordinate is a boundary
label of exactly two middle windows.  The same holds for \(b\).  Across all
\(B\) rows, at most

\[
 \boxed{4B}                                             \tag{6.2}
\]

actual \(\rho\)-owner incidences are directly aligned with their cores.

The active seams in (0.2) are actual edges of the prepared factor versus its
\(\rho\)-translate, so (6.2) applies unchanged before pullback.  Therefore a
linear seam supply does not directly give a linear useful first-shadow clause
supply.  At most \(O(B)=o(W)\) seam incidences can be read off through (6.1).
Any successful use of the remaining seams must prove that their fresh
components also contain lower-rank occurrences far from their defining middle
cores, and that these occurrences split hole--duplicate pairs with controlled
signed-cycle frustration simultaneously over all \(q\le A\sqrt m\).

The exact surviving theorem target is consequently:

> Starting from the packet assignment in Theorem 2, prove that the actual
> multidepth clause/component incidence has immutable weighted defect \(o(W)\)
> and either weighted NAE frustration \(o(W)\), or unit-coefficient
> orbit-profile and feedback penalties satisfying (4.13).

Theorems 2--4 prove every subsequent rounding and integrality step once that
geometric leakage/holonomy statement is available.  They do not prove the
statement itself, and no coefficient-one conclusion is claimed here.

## 7. Independent audit

An independent proof audit rederived the two step-two distances \(m,m-1\),
the moved-root count \(2n-4\), the external-neighbour subtraction
\(m(m+1)-(2n-1)=m^2-3m-1\), and the native-colour loss
\(hv(2n-4)\).  It also checked the pinned directed-cut factor \(1/4\), the
orbit injection under \(\alpha_\varepsilon\), and the owner-incidence bound
\(2s\le(n-3)|Z|\).  The resulting constants \(11/288\) in (0.2) and
\(11/144\) in (0.3) were recovered independently.

The audit found no substantive defect.  It emphasized the same implication
boundary as Section 6: (0.2) is a theorem about genuine fresh middle-owner
seams and component row mass, not a theorem that those components split any
specified lower-rank hole--duplicate pairs.
