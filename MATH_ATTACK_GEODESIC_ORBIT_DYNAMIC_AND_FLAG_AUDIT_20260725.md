# Dynamic and flag audit of geodesic-orbit TRP pruning

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, web search, or
matching black box is used.

## 0. Corrected outcome

The static calculations in
MATH_ATTACK_GEODESIC_ORBIT_TRP_OVERLAP_PRUNING_20260725.md survive:

\[
 \Psi_j(P)
 \le(2+o(1)){\ell\over\binom m{j-1}^{\,2}},
\tag{0.1}
\]

\[
 \sup_{1/\log m\le z\le1}\mathcal K_z(P)
 \le(2+o(1)){\ell\over m^2},
\tag{0.2}
\]

and the simple-support degree still tends to infinity after division by
\((\log m)^{A\ell}\) for every fixed \(A\). Moreover, even the corrected
conflict-neighbourhood static series satisfies

\[
 \sup_{1/\log m\le z\le1}
 \sum_{j=2}^{\ell}\Psi_j(P)(c/z)^j
 =O\left({\ell(\log m)^2\over m^2}\right),
\tag{0.2a}
\]

whose product with \(\ell\log\log m\) tends to zero. Thus the correction is
not a failure of the initial numerical hierarchy; it is specifically a
failure to prove hereditary propagation.

The asserted owner near-factor does **not** follow from these static
statements. The wasteful nibble requires the normalized degree and
conflict-link estimates in every adaptively generated residual. No
martingale or hereditary theorem proving this for the geodesic orbit is
currently available. The assertion

\[
 L_O=o(W),\qquad L_C=o(W/\ell)
\tag{0.3}
\]

has therefore been retracted and is now only conditional on the dynamic
propagation gate.

The flag audit gives an additional exact limitation. For a monotone
geodesic owner path, all but \(q\) lower and \(q\) upper depth-\(q\) flags
are already determined by the owner support. Hidden rotor decorations
control only two collars. At depth one,

\[
 L_1(t)=X_t\cap X_{t+1},\qquad
 U_1(t+1)=X_t\cup X_{t+1}
\tag{0.4}
\]

for every internal transition. Thus selecting hidden decorations cannot
repair a macroscopic failure of the two-sided rainbow edge labels. It can
change only \(O(W/\ell)=o(W)\) depth-one occurrences.

So the corrected frontier has two gates:

1. hereditary residual propagation for the geodesic owner nibble; and
2. a joint matching of geodesic owner supports with their deterministic
   interior lower/upper flag rows.

## 1. The exact dynamic quantity

Let \(G_t\) be a current residual of the tagged geodesic hypergraph, let
\(D_t\) be its reference degree, and mark residual edges with probability

\[
 p_t={h\over rD_t},\qquad r=\ell+1.
\tag{1.1}
\]

For an edge \(e\), write

\[
 \Gamma_t(e)=\{g\in G_t:g\cap e\ne\varnothing\}.
\]

If \(I_e\) is the event that no marked edge meets \(e\), then exactly

\[
 \Pr(I_e=1)=(1-p_t)^{|\Gamma_t(e)|},
\tag{1.2}
\]

and

\[
 {\Pr(I_e=I_f=1)\over\Pr(I_e=1)\Pr(I_f=1)}
 =(1-p_t)^{-|\Gamma_t(e)\cap\Gamma_t(f)|}.
\tag{1.3}
\]

The covariance is therefore controlled by residual conflict-neighbourhood
intersections, not by the initial owner intersection \(|e\cap f|\) alone.
The deterministic comparison is

\[
 |\Gamma_t(e)\cap\Gamma_t(f)|
 \le
 \sum_{x\in e}\sum_{y\in f}d_t(x,y).
\tag{1.4}
\]

To turn (1.4) into the desired exponential owner-overlap majorant one
already needs, in the current residual,

\[
 d_t(x)=(1+o(1))D_t
\tag{1.5}
\]

for almost every current vertex and

\[
 r^2{\Delta_{2,t}\over D_t}\log\log m=o(1).
\tag{1.6}
\]

These are propagation conclusions, not consequences of (0.1).

## 2. Why the static hierarchy is not hereditary

For a surviving edge \(e\), define the residual normalized moments

\[
 \Psi_{j,t}(e)
 ={1\over D_t}
 \sum_{\substack{f\in G_t\\
                  \operatorname{tag}(f)\ne\operatorname{tag}(e)}}
 \binom{|e\cap f|}{j}.
\tag{2.1}
\]

The static theorem bounds the initial numerator by \(D_0\Psi_{j,0}(e)\).
After deletions one knows only that the numerator decreases. If the
reference degree has fallen to its product benchmark

\[
 D_t\asymp D_0z^{r-1},
\tag{2.2}
\]

the deterministic consequence is merely

\[
 \Psi_{j,t}(e)
 \le z^{-(r-1)}\Psi_{j,0}(e).
\tag{2.3}
\]

At \(z=1/\log m\), the multiplier in (2.3) is

\[
 (\log m)^{\ell+O(1)},
\tag{2.4}
\]

which destroys (0.2). To recover the useful bound, one must prove that
every overlap numerator thins at essentially the same rate as \(D_t\).

The nibble does not perform independent vertex thinning. It removes unions
of marked geodesic chunks. If two candidate chunks share a long geodesic
core, conditioning that the core survives makes both chunks survive
together. Formula (1.3) records this bias exactly. The initial factorial
rarity in (0.1) is encouraging, but without a martingale estimate it does
not show that the rare family cannot become a large fraction of a residual
link.

In particular, the following two statements remain unproved:

\[
 \sum_{v\in V(G_t)}
 \left({d_t(v)\over D_t}-1\right)^2=o(|V(G_t)|),
\tag{2.5}
\]

and, uniformly for every surviving edge,

\[
 \sum_{j\ge2}\Psi_{j,t}(e)(c/z_t)^j
 =o\left({1\over r\log\log m}\right).
\tag{2.6}
\]

Equations (2.5)--(2.6), together with (1.6), are the exact dynamic gate.
No proof of them is contained in the static orbit census.

## 3. The martingale calculation that would be needed

For completeness, fix a current vertex \(v\), put

\[
 E_t(v)=\{g\in G_t:v\in g\},
\]

condition that no edge of \(E_t(v)\) is marked in one bite, and write

\[
 Z_v=\sum_{e\ni v}
 \mathbf 1\{\Gamma_t(e)\setminus E_t(v)
             \hbox{ contains no mark}\}.
\tag{3.1}
\]

Let

\[
 B_e=\Gamma_t(e)\setminus E_t(v),\qquad e\ni v.
\]

Conditional on the displayed event, the remaining edge marks are still
independent. Denote the summand indexed by \(e\) in (3.1) by \(Y_e\); it
is the indicator that \(B_e\) contains no mark. Hence

\[
 {\Pr(Y_e=Y_f=1)\over\Pr(Y_e=1)\Pr(Y_f=1)}
 =(1-p_t)^{-|B_e\cap B_f|}.
\]

Whenever \(p_t\max_{e,f}|B_e\cap B_f|\le1\), the elementary bound
\(e^x-1\le Cx\) for \(0\le x\le2\), together with
\(-\log(1-p_t)\le2p_t\), gives

\[
 \operatorname {Var}(Z_v\mid v\hbox{ untouched})
 \le
 C\left(D_t+\frac{h}{rD_t}
 \sum_{g\not\ni v}A_g(v)^2\right),
\tag{3.2}
\]

where

\[
 A_g(v)=\#\{e\ni v:e\cap g\ne\varnothing\}.
\]

Indeed,

\[
 \sum_{e,f\ni v}|B_e\cap B_f|
 =\sum_{g\not\ni v}A_g(v)^2,
\]

which proves (3.2), after absorbing the diagonal variances and degree
flatness into \(CD_t\). The initial weighted-overlap and tag--owner
estimates are designed to make this right-hand side small. For iteration
one also needs the analogous residual pair-link martingale. For owners
\(u,v\), it contains

\[
 {h\over rD_t}
 \sum_{g\not\ni u,v}A_g(u,v)^2,
\tag{3.3}
\]

where

\[
 A_g(u,v)
 =\#\{e\supset\{u,v\}:e\cap g\ne\varnothing\}.
\]

Expanding (3.3) introduces residual triple and higher links. Even for the
geodesic orbit, endpoints at distance two have a specified geodesic
midpoint on exactly a \(1/4\) fraction of their initial link, by the four
orders of the two departures and two arrivals. The normalized endpoint
codegree has the small static factor \(\binom m2^{-2}\), but proving that
every such
conditional cluster stays harmless over
\(\Theta(r\log\log m/h)\) bites is precisely the missing martingale
argument.

A self-contained proof would have to establish a stopped supermartingale
for the combined potential

\[
 \Phi_t=
 \sum_v\left({d_t(v)\over D_t}-1\right)^2
 +\sum_{j\ge2}\alpha_{j,t}
   \sum_{\mathcal S:|\mathcal S|=j}
   \left({d_t(\mathcal S)\over D_t}\right)^2,
\tag{3.4}
\]

with weights \(\alpha_{j,t}\) compensating the factor
\((1-p_t)^{-|\Gamma_t(e)\cap\Gamma_t(f)|}\). No choice of weights with a
verified negative drift has yet been proved. Consequently there is no
self-contained dynamic theorem to report.

## 4. Hidden decorations of a geodesic owner support

Write a selected geodesic support as

\[
 X_t=C+\{a_{t+1},\ldots,a_g\}
        +\{b_1,\ldots,b_t\},
\qquad0\le t\le g.
\tag{4.1}
\]

### Proposition 4.1 (decoration rigidity)

For every \(1\le q\le Q\), the owner support (4.1) determines the
\(\ell-q\) interior entries in each signed depth-\(q\) row. Among the
displayed flags, changing the hidden rotor realization can affect only the
two \(q\)-entry collars (4.7)--(4.8).

#### Proof

For every \(q\le Q\) with \(t+q\le g\), the owner chronology forces the
next \(q\) departures to be

\[
 a_{t+1},a_{t+2},\ldots,a_{t+q}.
\tag{4.2}
\]

For \(t\ge q\), it records the previous \(q\) departures in the upper half
of the queue in the order

\[
 a_t,a_{t-1},\ldots,a_{t-q+1}.
\tag{4.3}
\]

Therefore, whenever \(t+q\le g\),

\[
 \boxed{
 L_q(t)
 =X_t\cap X_{t+q}
 =C+\{a_{t+q+1},\ldots,a_g\}
    +\{b_1,\ldots,b_t\},}
\tag{4.4}
\]

and, whenever \(t\ge q\),

\[
 \boxed{
 U_q(t)
 =X_{t-q}\cup X_t
 =C+\{a_{t-q+1},\ldots,a_g\}
    +\{b_1,\ldots,b_t\}.}
\tag{4.5}
\]

Thus the owner support fixes

\[
 \ell-q
\tag{4.6}
\]

flags on each signed depth-\(q\) row.

The explicit realization in Proposition 3.1 of the pruning note retains
the following hidden choices:

* an ordered initial upper queue selected from the \(H-g\) unused outside
  coordinates; and
* \(Q\) post-chunk scheduled departures selected from the unused core.

They affect only

\[
 U_q(0),\ldots,U_q(q-1)
\tag{4.7}
\]

and

\[
 L_q(g-q+1),\ldots,L_q(g),
\tag{4.8}
\]

respectively. These are the two \(q\)-column collars. The initial
upper-queue order and the post-chunk core choices enter only these boundary
positions. This proves the proposition. \(\square\)

## 5. Depth one is already rigid

### Corollary 5.1 (depth-one bulk obstruction)

At \(q=1\), equations (4.4)--(4.5) reduce to

\[
 L_1(t)=X_t\cap X_{t+1},
\qquad0\le t<g,
\tag{5.1}
\]

and

\[
 U_1(t+1)=X_t\cup X_{t+1},
\qquad0\le t<g.
\tag{5.2}
\]

Only \(U_1(0)\) and \(L_1(g)\) depend on hidden decorations. Hence a family
of \(S\) selected chunks has only \(S\) adjustable depth-one occurrences
on either signed side.

Any selected owner-matching with owner leave \(o(W)\) necessarily has

\[
 S=(1+o(1)){W\over\ell},
\tag{5.3}
\]

because every chunk contains \(\ell\) distinct owners. Hence its total
adjustable depth-one mass is

\[
 O(W/\ell)=o(W).
\tag{5.4}
\]

Let \(h_1^-\) and \(h_1^+\) be the holes left by the fixed internal
intersection and union labels in (5.1)--(5.2). Whatever hidden decorations
are selected, the final holes obey

\[
 H_1^-\ge h_1^- -S,\qquad
 H_1^+\ge h_1^+ -S.
\tag{5.5}
\]

Thus hidden decorations can produce \(o(W)\) final depth-one holes only if

\[
 h_1^-+h_1^+=o(W)
\tag{5.6}
\]

already holds for the selected geodesic owner supports.

Equations (5.1)--(5.2) are exactly the two-sided rainbow edge labels of the
Johnson graph: a transition \(X_tX_{t+1}\) is labelled below by its
intersection and above by its union. An owner matching does not control
these labels. Distinct owners can use the same lower facet or upper
cofacet, so owner-disjointness does not imply (5.6).

## 6. Higher-depth collar capacity

At signed depth \(q\), a selected chunk has \(q\) decoration-controlled
positions and \(\ell-q\) owner-determined positions. Across \(S\) chunks,
the maximum number of new targets which collar choices can add is at most

\[
 qS=(1+o(1)){qW\over\ell}
\tag{6.1}
\]

per side. If the deterministic interior row has \(h_q^\pm\) holes, then

\[
 H_q^\pm\ge h_q^\pm-qS.
\tag{6.2}
\]

The total collar occurrence mass through depth \(Q\) is

\[
 2S\sum_{q=1}^{Q}q
 =(1+o(1)){Q(Q+1)W\over\ell}.
\tag{6.3}
\]

Although the ordered collars have substantial entropy, they cannot alter
the bulk

\[
 2S\sum_{q=1}^{Q}(\ell-q)
\tag{6.4}
\]

of the flag incidence. In particular, collar selection is a secondary
balancing problem; it cannot replace a joint interior-flag matching.

## 7. Correct frontier

The audited conclusions are now:

1. The geodesic orbit is an explicit coordinate-symmetric,
   repetition-free, rotor-realizable owner catalogue.
2. Its static owner degrees, codegrees, overlap hierarchy, and entropy
   calculations are correct.
3. Those static bounds do not prove hereditary residual degree or link
   control. The owner near-factor remains conditional.
4. Hidden rotor decorations control only the two boundary collars
   (4.7)--(4.8).
5. The internal depth-one flags are the fixed intersection/union labels
   (5.1)--(5.2), so decoration selection cannot solve the two-sided
   rainbow problem.

The next valid coefficient-one theorem must jointly select geodesic owner
supports so that:

* the owner residual martingales remain flat through the nibble;
* the deterministic interior rows (4.4)--(4.5) have aggregate \(o(W)\)
  holes; and
* the two hidden collars are then balanced without adding more than
  \(o(W)\) holes.

No such joint dynamic theorem is currently proved.
