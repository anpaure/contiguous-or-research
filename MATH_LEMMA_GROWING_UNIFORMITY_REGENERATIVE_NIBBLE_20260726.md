# A growing-uniformity packet nibble: exact bite rate and the residual-regeneration gate

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is used.

## 0. Scope and conclusion

This note separates two assertions which must not be conflated.

1. For a \(K\)-uniform, nearly \(D\)-regular hypergraph, a small normalized
   pair-codegree gives a quantitatively efficient **single isolated bite**.
2. The same pair-codegree hypothesis does not by itself regenerate the
   residual hypergraph through the \(O(K\log H)\) bites needed to leave
   \(o(1/H)\) of each slot part.

The first assertion is proved below with growing \(K\).  The second assertion
is made exact by a hereditary regeneration hypothesis and by an exact
residual-overlap kernel.  Under hereditary regeneration, the logarithmic
pair-cube pilot

\[
 r=\alpha\log _2m+O(1),\qquad 0<\alpha<1,\qquad
 H\le r/4,
\]

has the required numerical margin: with \(R=2^r=m^{\alpha+o(1)}\) and
\(K=(2H+1)R\), the full mixed census gives
\(\Delta_2/D=O(r/m)\), and hence

\[
 K\Delta _2/D=O(m^{\alpha-1}Hr)
 =O(m^{\alpha-1}(\log m)^2)=o(1).
\]

Taking residual density \(1/(H\log H)\) would then leave
\(O(W/(H\log H))=o(W/H)\) resources in every signed slot part and hence
only \(O(W/\log H)=o(W)\) aggregate mandatory-target holes.

This is a conditional pilot, not a proof of the packet theorem.  In fact,
ordinary product residuals fail the required hereditary hypothesis even on
the owner packet orbit.  Thus a positive application must establish a
packet-correlated residual law or a one-shot coloring/absorption theorem.

## 1. One isolated bite with growing edge size

Let \(\mathcal G=(V,\mathcal E)\) be a simple \(K\)-uniform hypergraph.  Suppose
that for some \(D>0\) and \(0\le\eta<1/4\),

\[
 (1-\eta)D\le d(v)\le(1+\eta)D\qquad(v\in V).       \tag{1.1}
\]

For an edge \(E\), define its normalized internal star overlap by

\[
 \sigma(E):={1\over KD}\sum_{\{u,v\}\subset E}d(u,v),
 \qquad \sigma:=\max_E\sigma(E).                       \tag{1.2}
\]

If \(\Delta _2\le\delta D\), then

\[
 \sigma\le {K-1\over2}\delta.                         \tag{1.3}
\]

The parameter \(\sigma\), rather than the cruder \(K\delta\), is the exact
quantity needed in the first-order conflict count.  This matters in a
multipartite packet lift, where owner--owner, owner--target, and
cross-depth target pairs have different codegrees.

### Lemma 1.1 (growing-\(K\) isolated bite)

Fix \(0<\gamma\le1\), and assume \(KD\ge2\).  Independently mark every edge
with probability

\[
 p={\gamma\over KD}.                                    \tag{1.4}
\]

Retain a marked edge if no other marked edge intersects it.  The retained
edges form a matching.  Put \(\beta=\gamma e^{-\gamma}\).  Uniformly in
\(K,D\), if

\[
 \xi:=\eta+\sigma+D^{-1}+(KD)^{-1}=o(1),                \tag{1.5}
\]

then every vertex is covered with probability

\[
 {\beta\over K}(1+O_\gamma(\xi)),                       \tag{1.6}
\]

and some outcome covers at least

\[
 {\beta\over K}(1-O_\gamma(\xi))|V|                    \tag{1.7}
\]

vertices.

#### Proof

Let \(N(E)\) be the number of edges other than \(E\) meeting \(E\).  The
union bound gives

\[
 N(E)\le\sum_{v\in E}(d(v)-1)\le K(1+\eta)D.            \tag{1.8}
\]

The first Bonferroni inequality and (1.2) give

\[
\begin{aligned}
 N(E)
 &\ge \sum_{v\in E}(d(v)-1)
       -\sum_{\{u,v\}\subset E}(d(u,v)-1)\\
 &\ge K(1-\eta)D-K-KD\sigma.                            \tag{1.9}
\end{aligned}
\]

Consequently

\[
 pN(E)=\gamma(1+O(\eta+\sigma+D^{-1})).                 \tag{1.10}
\]

Also \(p^2N(E)=O_\gamma((KD)^{-1})\).  Therefore

\[
 \Pr(E\text{ is retained})
 =p(1-p)^{N(E)}
 ={\gamma e^{-\gamma}\over KD}
   (1+O_\gamma(\xi)).                                   \tag{1.11}
\]

For a fixed vertex \(v\), the events that distinct edges through \(v\) are
retained are mutually exclusive.  Summing (1.11) over the \(d(v)\) edges
through \(v\), and using (1.1), proves (1.6).  Summing (1.6) over all
vertices proves the expectation corresponding to (1.7), so at least one
outcome attains (1.7). \(\square\)

No fixed-uniformity theorem is used here.  Notice that one bite covers
only \(\Theta(1/K)\) of the current vertices.  Reaching density
\(\varepsilon\) therefore requires \(\Theta(K\log(1/\varepsilon))\)
successful regenerated bites.

## 2. A self-contained regenerative nibble theorem

The following is the weakest deterministic iteration statement supplied by
Lemma 1.1.  It deliberately exposes, rather than hides, the residual gate.

Let \(V=V_1\dot\cup\cdots\dot\cup V_b\), with \(|V_i|=W\), and suppose every
edge contains exactly \(R\) vertices of every part.  Thus

\[
 K=bR.                                                   \tag{2.1}
\]

Deleting a matching leaves the same number of vertices in every part.

### Definition 2.1 (hereditary packet regeneration)

For \(0<\varepsilon<1\), say that \(\mathcal G\) has
\(\operatorname{HPR}(\varepsilon;\eta,\sigma_0)\) if every induced residual
\(\mathcal G[U]\) obtained by deleting the vertices of a matching, and
satisfying

\[
 |U\cap V_i|\ge\varepsilon W\quad(1\le i\le b),          \tag{2.2}
\]

has a scale \(D_U>0\) for which (1.1) holds on \(U\), and its parameter
(1.2), with \(D_U\) in place of \(D\), is at most \(\sigma_0\).

One may weaken this definition by requiring the property only for one
admissible outcome of each successive bite.  In that form, however, the
existence of the admissible outcome is itself the needed LLL-distribution
or martingale theorem and must be proved separately.

### Theorem 2.2 (explicit growing-uniformity iteration)

Assume \(\operatorname{HPR}(\varepsilon;\eta,\sigma_0)\), and assume

\[
 \xi_0:=\eta+\sigma_0+\sup_U D_U^{-1}=o(1).              \tag{2.3}
\]

Then \(\mathcal G\) has a matching leaving at most \(\varepsilon W\)
vertices in every part.  More precisely, for any fixed \(0<\gamma\le1\),
at most

\[
 T\le {K\over\gamma e^{-\gamma}(1-O_\gamma(\xi_0))}
       \log {1\over\varepsilon}+1                       \tag{2.4}
\]

isolated bites suffice.

#### Proof

Apply Lemma 1.1 to the current residual.  Choose an outcome covering at
least a fraction

\[
 c/K,\qquad c=\gamma e^{-\gamma}(1-O_\gamma(\xi_0)),     \tag{2.5}
\]

of its vertices.  Since each selected edge removes exactly \(R\) vertices
from each part and all residual part sizes are equal, the same fraction is
removed from every part.  The new residual again satisfies Definition 2.1
as long as (2.2) holds.  After \(t\) bites its common part size is at most

\[
 W(1-c/K)^t\le W e^{-ct/K}.                              \tag{2.6}
\]

Taking \(t\) as in (2.4) makes this at most \(\varepsilon W\).  The union
of the bite matchings is a matching because every later bite lies in the
uncovered residual. \(\square\)

### Corollary 2.3 (the numerical logarithmic-packet pilot)

Let

\[
 r=\alpha\log_2m+O(1),\quad 0<\alpha<1,\quad R=2^r,
 \quad H\to\infty,\quad H\le r/4,
\]

and use the \(b=2H+1\) owner-and-signed-slot parts of the full packet lift.
Suppose that after exact regularization all residuals down to

\[
 \varepsilon={1\over H\log H}                            \tag{2.7}
\]

satisfy HPR with \(\eta=o(1)\), \(\inf D_U\to\infty\), and

\[
 \sigma_0=o(1).                                         \tag{2.8}
\]

A sufficient, but not necessary, condition for (2.8) is that **every**
mixed pair type in every residual obey

\[
 {d_U(x,y)\over D_U}=O(r/m),                             \tag{2.9}
\]

because then

\[
 \sigma_0=O(Kr/m)
 =O(m^{\alpha-1}Hr)=o(1).                              \tag{2.10}
\]

The larger \(O(r/m)\) scale is genuinely needed in the physical lift:
although an incident owner--depth-one-target pair has normalized codegree
\(2/(m+1)\), adjacent same-sign depths can have normalized codegree up to
\(2r/(m-r)\).  Those pairs dominate the maximum-codegree estimate.

Theorem 2.2 gives a matching with common part leave

\[
 \ell\le {W\over H\log H}=o(W/H)                        \tag{2.11}
\]

after

\[
 T=O(K\log(H\log H))
  =O(m^\alpha H\log H)                                  \tag{2.12}
\]

bites.  Since there are \(2H\) signed target parts, their aggregate hole
count is at most

\[
 2H\ell=O(W/\log H)=o(W).                                \tag{2.13}
\]

Thus all numerical dependencies are favorable.  The time-zero mixed
owner--target and cross-depth target codegrees are computed in
MATH_LEMMA_LOG_PACKET_MIXED_CODEGREES_20260726.md and do satisfy (2.9).
What remains unproved is not a fixed-\(K\) technicality: it is hereditary
preservation of those estimates, together with the edge--edge overlap
distribution needed for HPR.

## 2A. The audited ABKV theorem is quantitatively inapplicable

This failure can be checked without dump tokens.  Consider the simple
strict-rainbow catalogue in which every decorated packet claims all \(R\)
distinct targets at every signed depth.  Its edge size is

\[
 K=(1+2H)R.                                             \tag{2A.1}
\]

Let \(D_0\) be its owner degree and \(D_q^\pm\) its degree on a signed
depth-\(q\) target part.  Coordinate transitivity and incidence counting
give

\[
 WD_0=N_qD_q^\pm,
\qquad
 {D_q^\pm\over D_0}={W\over N_q}=1+O(H^2/m).            \tag{2A.2}
\]

Thus this unthinned hypergraph is already
\((1+O(H^2/m))\)-regular.  Also

\[
 2\sum_{q\le H}(W-N_q)
 =O\!\left({W\over m}\sum_{q\le H}q^2\right)
 =O(H^3W/m)=o(W)                                       \tag{2A.3}
\]

when \(H=O(\log m)\).  Hence rank-size mismatch can be discarded at
negligible owner/target cost in this pilot; labelled dumps are not the
source of the obstruction below.

Through one owner there are

\[
 D_r=\binom mr^2r!
\]

physical frames.  On a fixed frame a directed cube factor is specified,
with a generous overcount, by choosing one of \(r\) outgoing directions
at each of its \(R\) owners.  Consequently the maximum degree \(D\) in
the strict simple catalogue satisfies

\[
 D_r\le D_0\le D\le (1+O(H^2/m))D_r r^R,
\qquad
 \log D=O(r\log m+R\log r).                             \tag{2A.4}
\]

Assume now \(H=\Theta(r)=\Theta(\log m)\), the simultaneous
\(c\log m\)-band pilot.  Then

\[
 {K\over\log D}
 \ge \Omega\!\left({H\over\log r}\right)\longrightarrow\infty. \tag{2A.5}
\]

The previously audited Alon--Bollobás--Kim--Vu matching theorem requires,
among other hypotheses,

\[
 K\le\tfrac12\log D,
\qquad
 e^{2K}{C_*\log D\over D}=o(1),                         \tag{2A.6}
\]

where \(C_*\) is the maximum pair codegree.  The first condition is
contradicted by (2A.5).  The second fails independently: the exact
owner--depth-one-target incidence gives

\[
 {C_*\over D}\ge {2+o(1)\over m},
\]

and therefore

\[
 e^{2K}{C_*\log D\over D}
 \ge e^{2K}{(2+o(1))\log D\over m}\longrightarrow\infty. \tag{2A.7}
\]

Finally, the theorem's displayed uncovered-vertex factor is

\[
 K\left({C_*\log(1+C_*)\over D}\right)^{1/(K-1)}.        \tag{2A.8}
\]

Since \(C_*\ge1\) and \(\log D=o(K)\), the parenthesized
\((K-1)\)-st root is at least

\[
 \left({\log2\over D}\right)^{1/(K-1)}=1-o(1).
\]

Thus (2A.8) is at least \((1-o(1))K\), so even its formal error expression
is vacuous here.  The ABKV failure is therefore audited separately from
the product-residual failure proved next.

## 3. Exact product-residual variance and the mixed-overlap kernel

Pair codegrees control one bite because only the union of edge stars is
being counted.  A deep residual asks a different question: how many whole
edges survive after many resources have disappeared?

Retain every vertex independently with probability \(0<\rho<1\).  Fix a
retained vertex \(v\), and let \(Z_v\) be its degree in the induced
residual.  For two distinct edges \(E,F\ni v\), put

\[
 j_v(E,F)=|(E\cap F)\setminus\{v\}|.                     \tag{3.1}
\]

Then

\[
 \mu_v:=\mathbb E(Z_v\mid v\text{ retained})
 =d(v)\rho^{K-1},                                        \tag{3.2}
\]

and the exact normalized overlap kernel is

\[
 \Omega_v(\rho)
 ={1\over d(v)^2}
   \sum_{\substack{E\ne F\\E,F\ni v}}
   \bigl(\rho^{-j_v(E,F)}-1\bigr).                       \tag{3.3}
\]

### Lemma 3.1 (exact residual second moment)

For a regular vertex \(d(v)=D\),

\[
 {\operatorname {Var}(Z_v\mid v\text{ retained})\over\mu_v^2}
 \le {1\over\mu_v}+\Omega_v(\rho).                     \tag{3.4}
\]

If \(\Delta_2\le\delta D\), then

\[
 \boxed{
 \Omega_v(\rho)
 \le \delta\bigl(\rho^{-(K-1)}-1\bigr).}               \tag{3.5}
\]

#### Proof

Write \(I_E\) for the indicator that all vertices of \(E\setminus\{v\}\)
survive.  Then

\[
 \mathbb E I_E=\rho^{K-1},\qquad
 \mathbb E(I_EI_F)=\rho^{2(K-1)-j_v(E,F)}.               \tag{3.6}
\]

Expanding the variance of \(Z_v=\sum_{E\ni v}I_E\) gives (3.4).

For the second assertion, first observe

\[
\begin{aligned}
 \sum_{E\ne F\ni v}j_v(E,F)
 &=\sum_{u\ne v}d(u,v)(d(u,v)-1)\\
 &\le \Delta_2\sum_{u\ne v}d(u,v)\\
 &=\Delta_2D(K-1)\le\delta D^2(K-1).                    \tag{3.7}
\end{aligned}
\]

Convexity, or the chord joining the endpoints \(0,K-1\), gives for every
\(0\le j\le K-1\)

\[
 \rho^{-j}-1
 \le {j\over K-1}\bigl(\rho^{-(K-1)}-1\bigr).           \tag{3.8}
\]

Substituting (3.7) into (3.3) proves (3.5). \(\square\)

Consequently product-residual degree concentration at one fixed vertex
follows from

\[
 D\rho^{K-1}\longrightarrow\infty,qquad
 \Omega_v(\rho)=o(1).                                   \tag{3.9}
\]

The pair-codegree bound alone proves the second condition only in the
near-full range

\[
 \delta\rho^{-(K-1)}=o(1).                              \tag{3.10}
\]

If successive bites each remove \((\beta+o(1))/K\) of the current
resources, then after \(t\) bites

\[
 \rho_t=\exp\{-(\beta+o(1))t/K\}.
\]

Thus the pair-codegree estimate (3.5) controls at most

\[
 t\le (1-o(1)){\log(1/\delta)\over\beta}                 \tag{3.10a}
\]

product-like rounds.  In the logarithmic pilot
\(\delta=O(r/m)\), this is only \(O(\log m)\) rounds and covers only
\(O(\log m/K)=o(1)\) of the resources.  By contrast, (2.12) needs
\(\Theta(K\log H)\) rounds.  This is an explicit quantitative reason that
the favorable value \(K\delta=o(1)\) settles the fresh bite but not the
trajectory.

At \(\rho\) close to \(1\), (3.3) can be evaluated from mixed pair overlap.
At small \(\rho\), its exponential weight distinguishes a pair of columns
sharing one resource from a pair sharing a long cross-depth trace.  Hence
the complete mixed calculation required for the pilot is the spectrum

\[
 A_{v,j}=|\{(E,F):E\ne F,\ E,F\ni v,\ j_v(E,F)=j\}|,
 \qquad 1\le j\le K-1,                                  \tag{3.11}
\]

or equivalently the polynomial

\[
 \sum_{j\ge1}A_{v,j}z^j.                                \tag{3.12}
\]

Maximum pair codegree records only a coarse first-moment bound on this
polynomial.  In particular, cross-depth target pairs cannot be omitted.

For simultaneous concentration at all resources, (3.9) is still not
enough: one needs a tail or local-lemma distribution strong enough to
survive the number of resources, or a quarantine theorem showing that the
total exceptional mass accumulated over the \(T\) rounds in (2.12) is
\(o(W/H)\).  This is the precise martingale/LLL hypothesis hidden by an
unqualified invocation of a fixed-uniformity nibble.

## 4. Product regeneration already fails on physical owner packets

The failure below is independent of target codegrees.  It occurs in the
owner projection.

For a pair-cube packet of dimension \(r\), put \(R=2^r\).  The exact number
of physical frames through a fixed middle owner is

\[
 D_r=\binom mr^2r!.                                      \tag{4.1}
\]

Retain middle owners independently with density \(\rho\), and condition on
retaining an owner \(X\).  A frame through \(X\) remains usable only if its
other \(R-1\) packet owners survive.  Therefore the expected number of
surviving physical frames through \(X\) is exactly

\[
 D_r\rho^{R-1}.                                          \tag{4.2}
\]

For \(r=\alpha\log_2m+O(1)\),

\[
 \log D_r
 \le2r\log(em/r)+r\log r=O((\log m)^2).                 \tag{4.3}
\]

At the density required in Corollary 2.3,

\[
 \rho={1\over H\log H},
\]

and for every \(H\to\infty\), \(H\le r/4\),

\[
 (R-1)\log(1/\rho)
 =m^{\alpha+o(1)}\log(H\log H)
 \gg(\log m)^2.                                         \tag{4.4}
\]

Equations (4.2)--(4.4) imply

\[
 D_r\rho^{R-1}=o(1).                                    \tag{4.5}
\]

This does not contradict the fact that many packets survive **globally**.
Indeed

\[
 |\mathscr P_r|={WD_r\over R},
\qquad
 \mathbb E|\mathscr P_r[U]|={WD_r\over R}\rho^R.         \tag{4.5a}
\]

For fixed \(0<\rho<1\), its logarithm is
\(\Theta(m)-\Theta(m^\alpha)\), so (4.5a) is exponentially large.
But the average surviving-frame degree of a retained owner is precisely
(4.2), which is \(o(1)\).  The surviving packets are concentrated on an
exceptional \(o(1)\)-fraction of retained owners and cannot support a
class-balanced continuation.

More generally, if \(\rho=1-\theta\) with \(\theta=o(1)\) and

\[
 \theta R\gg\log D_r=\Theta((\log m)^2),                 \tag{4.5b}
\]

then (4.2) is already \(o(1)\).  Thus a product-like trajectory loses
typical packet links after deleting only
\(\omega((\log m)^2/m^\alpha)\) of the owners, long before it reaches
constant density or the target density \(1/(H\log H)\).

By Markov's inequality, all but an \(o(1)\) fraction of retained owners
have no surviving physical packet through them.  Adding many local cycle
states to a frame does not change this conclusion: if one owner of the
physical packet is absent, none of those states is a surviving column.

Thus a product-thinned residual cannot satisfy HPR down to the desired
density.  This example also proves the exact methodological statement:

\[
 \boxed{K\Delta_2/D=o(1)\text{ does not imply hereditary residual
 regeneration.}}                                        \tag{4.6}
\]

It does **not** prove that a near-perfect packet matching is absent.  The
owner packet orbit even has deterministic exact factors inside a fixed
frame.  What (4.6) rules out is deriving the multiround theorem from
pair-codegree and marginal quasirandomness alone.

## 5. Audited conclusion boundary

The following are unconditional.

1. Lemma 1.1 gives an explicit growing-\(K\) isolated-bite rate under the
   internal overlap parameter (1.2).
2. Theorem 2.2 converts a hereditary regenerated bite into leave
   \(\varepsilon W\) in \(O(K\log(1/\varepsilon))\) rounds.
3. In the logarithmic pilot, \(K=m^{\alpha+o(1)}O(\log m)\), so normalized
   mixed codegrees \(O(r/m)\) give the favorable one-round scale
   \(K\Delta_2/D=o(1)\).
4. Lemma 3.1 gives the exact residual second moment and identifies the
   complete mixed intersection spectrum which must be audited.
5. Equation (4.5) proves that ordinary product residuals do not regenerate
   the physical packet links at the needed leave density.

The following is not proved.

1. HPR, or a weaker packet-correlated LLL-distribution invariant, for the
   owner-and-target packet lift.
2. The hereditary edge--edge intersection spectrum (3.11).  The
   time-zero resource-pair spectrum is now audited; it does not determine
   (3.11) after conditioning on many earlier bites.
3. A one-shot approximate edge-coloring or absorber which bypasses product
   residuals.

Accordingly, the logarithmic regime is a valid quantitative pilot for a
**correlated** growing-uniformity theorem, but \(K\Delta_2/D=o(1)\) alone is
not a license to cite a standard nibble.

An independent adversarial audit checked Lemma 1.1, Theorem 2.2,
the variance identity and convex-chord estimate (3.4)--(3.5), and the
strict-catalogue normalization in Section 2A.  All passed.
