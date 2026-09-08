# Max-reward cyclic transitions: exact owner dual and tail-area audit

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
long-running computation is used.

## 0. Result

Fix one oriented exact factor and one common integral balanced quota flow.
At a transition (q), suppose that a monotone release set (E) has already
been chosen.  There is an exact max-reward transportation problem whose
unused reward arcs are the **minimum possible number of new actual owners**
which must be released at transition (q).  Its integral dual is

\[
 \boxed{
 \delta_q(E)=
 \max_{\lambda_R+\mu_S\ge0\ (S\subset R)}
 \left\{
  \sum_{X\notin E}
   \min\!\left(1,
      \lambda_{\Gamma_{q-1}(X)}+\mu_{\Gamma_q(X)}\right)
  -\sum_R b_{q-1}(R)\lambda_R
  -\sum_S b_q(S)\mu_S
 \right\}.}
 \tag{0.1}
\]

Integral potentials suffice.  Every floor remains inside

\[
 b_j(T)=c_j+\mathbf1_{H_j}(T),\qquad
 c_j=\left\lfloor\frac{W}{\binom{2m+1}{m-j}}\right\rfloor.
\]

Choosing an integral optimum successively at every transition gives one
monotone family

\[
 \varnothing=E_0\subseteq E_1\subseteq\cdots\subseteq E_K
\]

and one common nested resolution.  No owner labels are exchanged: a newly
released owner is still at its literal canonical parent, and integral
residual flow units are bijected to the actual active owners at that parent.
If (D_q=E_q\setminus E_{q-1}), then exactly

\[
 |D_q|=\delta_q(E_{q-1})
\]

and the resulting tail area is

\[
 \boxed{
 \sum_{t=1}^K\frac{|E_t|}{c_t}
 =\sum_{q=1}^K
   \delta_q(E_{q-1})
   \sum_{t=q}^K\frac1{c_t}.}
 \tag{0.2}
\]

This is an exact constructive min-cost formulation, but it does **not**
improve the quantitative gates \(\mathrm{MR}_A\) or WCOI.  The audited
extraction hypothesis controls only rankwise balanced overload (or its
density-weighted common-quota version).  That overload is obtained from
the special height-one potentials in (0.1), hence is a lower bound for
\(\delta_q\), not an upper bound.  The remaining potentials in (0.1) are
the actual cyclic compatibility term.  Moreover, the extraction premise
allows aggregate overload of order (KW), whereas (0.2) must be (o(W)).
Thus no (o(W)) tail-area conclusion follows from the extraction premise,
even before the additional cyclic potential is considered.

## 1. Exact transition network

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 V_j=\binom{[n]}{m-j},\qquad K=\lceil A\sqrt m\rceil.
\]

For every middle owner (X\in V_0), retain its literal canonical flag

\[
 \Gamma_0(X)\supset\Gamma_1(X)\supset\cdots\supset\Gamma_K(X).
\]

Fix balanced integer vectors belonging to one common feasible nested flow:

\[
 b_j(T)=c_j+\mathbf1_{H_j}(T),\qquad
 |H_j|=W-c_j|V_j|.
 \tag{1.1}
\]

Fix (q\ge1) and a set (E\subseteq V_0) already released before
transition (q).  The candidate owners are (U=V_0\setminus E).  Form the
following bipartite transportation network from (V_{q-1}) to (V_q).

* Parent (R) has supply (b_{q-1}(R)), and child (S) has demand
  (b_q(S)).
* For every Boolean inclusion (S\subset R), insert an uncapacitated
  generic arc (R\to S) of reward zero.  (Capacity (W) would define the
  same primal feasible flows, but the uncapacitated presentation gives the
  dual constraint below directly.)
* For every candidate owner (X\in U), insert one separate parallel arc
  
  \[
  e_X:\Gamma_{q-1}(X)\longrightarrow\Gamma_q(X)
  \]
  
  of capacity one and reward one.

The network is feasible because (b_{q-1},b_q) are consecutive marginals
of the fixed common quota flow.  Let (Z_q(E)) be its maximum reward and
put

\[
 \delta_q(E)=|U|-Z_q(E).
 \tag{1.2}
\]

### Theorem 1.1 — exact minimum number of new owners

The number (delta_q(E)) is the minimum (|D|) over
(D\subseteq V_0\setminus E) such that transition (q) can be completed
integrally while every owner outside (E\cup D) uses its literal canonical
edge.

#### Proof

The transportation constraint matrix becomes a directed node--arc incidence
matrix after multiplying all child equations by (-1).  It is totally
unimodular.  The supplies, demands, and capacities are integral, so an
integral maximum-reward flow exists.

Take such a flow.  Let (K_q\subseteq U) be the actual owner arcs used by
the flow and put (D=U\setminus K_q).  Then

\[
 |D|=|U|-|K_q|=|U|-Z_q(E)=\delta_q(E).
\]

The full transportation flow contains the canonical arc of every owner
outside (E\cup D).  Designate those units by their actual owner labels.
All remaining integral units constitute a residual inclusion flow.  Hence
the indicated (D) is feasible.

Conversely, suppose (D\subseteq U) is feasible.  Put one unit on the
special arc (e_X) for every (X\in U\setminus D), and put the residual
completion units on generic arcs.  This is a feasible transportation flow
of reward (|U|-|D|).  Therefore

\[
 Z_q(E)\ge |U|-|D|,
\]

or (delta_q(E)\le|D|).  Together with the integral optimum construction,
this proves equality.  \(\square\)

## 2. Exact dual

### Theorem 2.1 — cyclic transition potential

Formula (0.1) holds.  If all data are integral, the maximum may be taken
over integral potentials (lambda,mu).

#### Proof

Give the parent and child conservation equations free dual variables
(lambda_R,mu_S).  An uncapacitated generic zero-reward arc forces

\[
 \lambda_R+\mu_S\ge0\qquad(S\subset R).
 \tag{2.1}
\]

The capacity-one reward arc (e_X) contributes

\[
 \bigl(1-lambda_{\Gamma_{q-1}(X)}
          -mu_{\Gamma_q(X)}\bigr)_+
\]

to the max-flow dual.  Strong transportation duality gives

\[
 Z_q(E)=
 \min_{(2.1)}
 \left\{
  \sum_Rb_{q-1}(R)\lambda_R
  +\sum_Sb_q(S)\mu_S
  +\sum_{X\notin E}
    \bigl(1-lambda_{\Gamma_{q-1}(X)}
            -\mu_{\Gamma_q(X)}\bigr)_+
 \right\}.
 \tag{2.2}
\]

Subtract (2.2) from (|V_0\setminus E|) and use, for (u\ge0),

\[
 1-(1-u)_+=\min(1,u).
\]

This is exactly (0.1).  Total dual integrality of the transportation
system, with integral rewards, permits integral optimal potentials.
\(\square\)

The same proof gives the genuinely weighted version.  If releasing a
candidate owner (X) costs (w_X\ge0), replace its special-arc reward by
(w_X).  The minimum new release cost is

\[
 \boxed{
 \delta_q^w(E)=
 \max_{(2.1)}
 \left\{
  \sum_{X\notin E}
    \min\!\left(w_X,
      \lambda_{\Gamma_{q-1}(X)}+\mu_{\Gamma_q(X)}\right)
  -\sum_Rb_{q-1}(R)\lambda_R
  -\sum_Sb_q(S)\mu_S
 \right\}.}
 \tag{2.3}
\]

Thus common-owner incidence weights can be put into the transition problem
without fractional owner splitting.

## 3. Monotone concatenation with actual owner labels

Start with (E_0=\varnothing).  At transition (q), choose an integral
maximum-reward flow from Section 1 and set

\[
 D_q=(V_0\setminus E_{q-1})\setminus K_q,
 \qquad E_q=E_{q-1}\cup D_q.
 \tag{3.1}
\]

### Theorem 3.1 — the transition optima concatenate

There is one integral nested resolution (P) with load (b_q) at every
depth and

\[
 P_q(X)=\Gamma_q(X)\qquad(X\notin E_q).
 \tag{3.2}
\]

Moreover (|D_q|=\delta_q(E_{q-1})), and (0.2) holds exactly.

#### Proof

Proceed by induction on (q).  Assume the actual labelled paths have been
constructed through depth (q-1).  Every newly released owner
(X\in D_q) was outside (E_{q-1}); hence its actual current parent is

\[
 P_{q-1}(X)=\Gamma_{q-1}(X).
 \tag{3.3}
\]

Every owner outside (E_q) is also outside (E_{q-1}), and the chosen
transportation flow contains its designated literal canonical arc.  Remove
all these designated frozen units from the full flow.  At a parent (R),
the remaining number of outgoing units is

\[
 b_{q-1}(R)
 -|\{X\notin E_q:\Gamma_{q-1}(X)=R\}|.
 \tag{3.4}
\]

The actual active owners in (E_q) currently at (R) have exactly the same
multiplicity.  Indeed, the full depth-((q-1)) load is (b_{q-1}(R)), and
every owner outside (E_q) is canonical there; (3.3) accounts for the new
members of (E_q).  Thus the integral residual outgoing units at (R) can
be bijected to the **actual labelled active owners currently at (R)**.
Assign each such owner the child of its bijected residual unit.

At child (S), frozen canonical units plus residual units total (b_q(S)).
All assigned children lie inside their actual parents, so the paths remain
nested.  No earlier layer changes, and no owner label is swapped or reset.
This proves the induction and (3.2).

The equality (|D_q|=\delta_q(E_{q-1})) is Theorem 1.1.  Since the increments
(D_q) are disjoint, an owner first released at (q) belongs to every
(E_t) for (t\ge q).  Double counting owner--depth incidences gives

\[
 \sum_{t=1}^K\frac{|E_t|}{c_t}
 =\sum_{q=1}^K|D_q|\sum_{t=q}^K\frac1{c_t},
\]

which is (0.2).  \(\square\)

## 4. The exact term controlled by pointed extraction

For the fixed common quota at depth (q), define

\[
 \mathcal B_q=\{S:\ell_q(S)>b_q(S)\},
 \qquad
 D_q^b=\sum_S(\ell_q(S)-b_q(S))_+.
 \tag{4.1}
\]

In (0.1) with (E=\varnothing), take

\[
 \lambda_R=0,
 \qquad
 \mu_S=\mathbf1_{\mathcal B_q}(S).
\]

These potentials satisfy (2.1), and their value is exactly

\[
 \ell_q(\mathcal B_q)-b_q(\mathcal B_q)=D_q^b.
\]

Consequently

\[
 \boxed{D_q^b\le\delta_q(\varnothing).}
 \tag{4.2}
\]

More generally, for an already released (E), the same test with

\[
 \mathcal B_q(E)=
 \{S:\ell_q(S)-a_q^E(S)>b_q(S)\}
\]

gives

\[
 \boxed{
 \sum_S(\ell_q(S)-b_q(S)-a_q^E(S))_+
 \le\delta_q(E).}
 \tag{4.3}
\]

Equations (4.2)--(4.3) identify the extraction-controlled quantity inside
the exact transition dual: it is the height-one child-overload potential.
The other admissible potentials in (0.1) are precisely the extra cyclic
parent--child compatibility cost.

The original audited pointed-extraction premise controls the independently
optimized spill

\[
 \sum_{a\in\mathcal A}O_{\tau(a)}(F),
\]

while its common-quota density refinement controls a weighted sum of the
(D_q^b).  Since (O_q(F)\le D_q^b\le\delta_q(\varnothing)), neither is an
upper bound for the max-reward cost.  The common-owner overload incidence

\[
 J_q^\uparrow
 =\sum_{\ell_q(S)>b_q(S)}a_q^{E_q}(S)
\]

is likewise only a charged subset of (|E_q|); owners forced by the other
potentials can lie in nonoverloaded fibres and contribute zero to
(J_q^\uparrow) while contributing fully to tail area.

There is also an unavoidable scale mismatch.  Positive retained cap mass
allows the controlled overload sum to be of order (KW).  In contrast,
fixed-window alignment requires

\[
 \sum_t|E_t|/c_t=o(W),
\]

and already survival gives

\[
 \sum_t\frac{D_t^b}{c_t}
 \le \sum_t\frac{|E_t|}{c_t}.
 \tag{4.4}
\]

Thus even deleting every higher potential from (0.1) would not turn the
positive-mass extraction hypothesis into an (o(W)) tail-area estimate.

## 5. Precise boundary

The following are proved.

1.  Minimum additional release at one transition is an integral
    max-reward Boolean transportation problem on the actual canonical owner
    arcs.
2.  Formula (0.1) is its exact dual, with all quota floors and high-set
    corrections retained.
3.  Successive optimum flows concatenate into one nested resolution without
    owner relabelling, retroactive rerouting, or a further Hall condition.
4.  The tail area of the resulting monotone construction is exactly (0.2).
5.  Balanced overload is only the special dual test (4.2); extraction
    controls this lower-level term, not the full transition optimum.

There is no unconditional asymptotic improvement of \(\mathrm{MR}_A\) or
WCOI.  To improve \(\mathrm{MR}_A\), one must bound the successive full
potentials (0.1), with their common owner history, strongly enough that the
right side of (0.2) is (o(W)).  To improve WCOI, one may use the weighted
dual (2.3) with the exact density-weighted overload-incidence costs, but no
such uniform upper bound follows from the audited extraction theorem.
