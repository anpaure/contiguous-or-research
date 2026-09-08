# Fixed Gaussian annuli: the coherent forced-tail weighted Hall obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, web input, random
selection, or entropy argument is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and fix

\[
 0<a<b,\qquad q_0=\lceil a\sqrt m\rceil,
 \qquad H=\lfloor b\sqrt m\rfloor.
\tag{0.2}
\]

For one full SCD \(\mathcal D\), retain the

\[
 \Omega=\mathcal D_{\ge q_0},\qquad |\Omega|=N_{q_0},
\tag{0.3}
\]

annular providers.  The surviving coefficient-one gate asks for one
annular-compatible bridge-one path cover of \(\Omega\) with

\[
 p=o(W/H).
\tag{0.4}
\]

The separate top-tag and full-top cuts are correct, but they do not use
the fact that one path forest must satisfy every protected tag threshold
simultaneously.  This note proves the coherent version.

For a chain \(C\) and \(q_0<j\le\min\{\rho(C),H\}\), let

\[
 t_j(C)=(\delta_j(C),\eta_j(C))
\tag{0.5}
\]

be its forced lower/upper SCD tail pair.  For distinct \(C,C'\), put

\[
 d(C,C')=\min\{\rho(C),\rho(C'),H\},
\tag{0.6}
\]

and define their forced-tail overlap weight by

\[
 \boxed{
 w(C,C')=\max\left\{
 s:0\le s\le(d(C,C')-q_0-1)_+,\ 
 t_{q_0+i}(C')=t_{q_0+i+1}(C)\ (1\le i\le s)
 \right\}.}
\tag{0.7}
\]

Thus \(w\) is the number of consecutive forced pair shifts supported by
the two chains; it is automatically zero when one tag is at most
\(q_0+1\).

Let \(\Lambda_{\rm tail}(\mathcal D)\) be the maximum total \(w\)-weight
of a directed vertex-disjoint linear forest on \(\Omega\).  This is an
SCD-only relaxation: it remembers all forced outer tails but forgets the
free inner ports and every further bridge equation.

### Main theorem

Every annular-compatible bridge-one path cover with \(p\) paths forces

\[
 \boxed{
 \Lambda_{\rm tail}(\mathcal D)
 \ge
 \sum_{q=q_0+2}^{H}
       (2N_q-N_{q_0}-p)_+.}
\tag{0.8}
\]

Consequently, if (0.4) holds, then

\[
 \boxed{
 \Lambda_{\rm tail}(\mathcal D)
 \ge(\Psi_{a,b}+o_{a,b}(1))W\sqrt m,}
\tag{0.9}
\]

where

\[
 \boxed{
 \Psi_{a,b}
 =\int_a^{\min\{b,\sqrt{a^2+\log2}\}}
       \bigl(2e^{-x^2}-e^{-a^2}\bigr)\,dx>0.}
\tag{0.10}
\]

Since one edge has weight at most

\[
 H-q_0-1=(b-a+o(1))\sqrt m,
\]

the same SCD must contain one forced-tail-compatible linear forest with
at least

\[
 \boxed{
 \left({\Psi_{a,b}\over b-a}+o_{a,b}(1)\right)W}
\tag{0.11}
\]

positive-weight edges.  Thus a positive-density coherent outer-tail bank
is necessary for **every** fixed annulus \(a<b\), including the wide
range in which the old binary top-tag run cut is silent.

### Moving-entrance corollary

The same exact inequality gives a stronger form suited to the
one-baseline flag-coherent reduction.  Suppose

\[
 q_0=o(\sqrt m),\qquad {H\over\sqrt m}\longrightarrow\infty,
 \qquad p=o(W/H).
\tag{0.12a}
\]

Fix any constant \(0<b<\sqrt{\log2}\), and truncate every forced-tail
weight at

\[
                         B=\lfloor b\sqrt m\rfloor.
\]

Precisely, on the actual path forest put

\[
 w_B(C,C')
 :=\min\{w(C,C'),(B-q_0-1)_+\}.
\tag{0.12b'}
\]

Equivalently, \(w_B(C,C')\) counts the thresholds
\(q_0+2\le q\le B\) for which both endpoints have radius at least
\(q\).  This equivalence uses the initial-segment form of the forced
tail equalities in (0.7).

Put

\[
 \kappa_b=\int_0^b(2e^{-x^2}-1)\,dx>0.
\tag{0.12b}
\]

Then the actual path forest must have truncated total tail weight at
least

\[
 \boxed{(\kappa_b-o(1))W\sqrt m.}
\tag{0.12c}
\]

In particular it contains at least

\[
 \boxed{\left({\kappa_b\over2b-\kappa_b}-o(1)\right)W}
\tag{0.12d}
\]

edges whose forced lower/upper tail agreement has length at least

\[
                         {\kappa_b\over2}\sqrt m.
\tag{0.12e}
\]

Indeed, apply the actual-forest identity (3.3)--(3.4), restricted to
\(q_0+2\le q\le B\).  Uniformly for \(0\le q\le b\sqrt m\),

\[
 {N_q\over W}=e^{-q^2/m}+o(1).
\]

Also \(N_{q_0}/W\to1\).  Since
\(2e^{-b^2}-1>0\), all the terms before subtracting \(p\) have a
fixed positive \(W\)-scale margin, and \(p=o(W/H)=o(W)\); hence the
positive parts in (3.3) may be removed for all sufficiently large
\(m\).  The resulting Riemann sum gives

\[
 \sum_{q=q_0+2}^{B}(2N_q-N_{q_0}-p)
  =(\kappa_b+o(1))W\sqrt m.
\]

Here the accumulated \(p\)-term is
\(O(\sqrt m\,p)=o(W)\), because
\(p=o(W/H)\) and \(H/\sqrt m\to\infty\).  This proves (0.12c).

For completeness, let \(X\) be the number of forest edges with
\(w_B(e)\ge (\kappa_b/2)\sqrt m\).  The forest has at most
\(N_{q_0}\le W\) edges, while

\[
 w_B(e)\le B-q_0-1=(b+o(1))\sqrt m.
\]

Consequently

\[
 \sum_{e\in F}w_B(e)
 \le {\kappa_b\over2}W\sqrt m
   +X\left(b-{\kappa_b\over2}+o(1)\right)\sqrt m.
\]

Comparison with (0.12c) yields

\[
 X\ge\left({\kappa_b\over2b-\kappa_b}-o(1)\right)W,
\]

which proves (0.12d).  In particular, the previously stated weaker
constant \(\kappa_b/(2b)\) is also valid.

Thus the moving-entrance theorem cannot be obtained from a bank of merely
short compatible seams.  It requires a positive-density matching of SCD
chains with genuinely Gaussian-length shifted flag tails.

There is also an exact top-tag histogram projection.  On
\(\Omega_H=\mathcal D_{\ge H}\), define the length-
\((H-q_0-1)\) prefix and suffix tail words

\[
P(C)=(t_{q_0+1}(C),\ldots,t_{H-1}(C)),
\]

\[
 S(C)=(t_{q_0+2}(C),\ldots,t_H(C)).
\tag{0.12}
\]

If \(p_\tau,s_\tau\) are their multiplicities, then every successful
cover satisfies

\[
 \boxed{
 {1\over2}\sum_\tau|p_\tau-s_\tau|
 \le N_{q_0}-N_H+p.}
\tag{0.13}
\]

Finally, the coherent tail requirement, the exact full-top fibre cut,
and the top-tag run cut admit one common weighted ordered-Hall support
functional.  This prevents them from being certified by three unrelated
forests.

No noncanonical SCD meeting these conditions is constructed here.  The
advance is a stronger universal, SCD-only obstruction and its exact
weighted Hall dual.

## 1. Forced annular tails

Write a symmetric chain \(C\) of radius \(d\) as

\[
 D_d(C)\subset\cdots\subset D_0(C)=X(C)
 =E_0(C)\subset\cdots\subset E_d(C).
\tag{1.1}
\]

For \(1\le j\le d\), define

\[
 \delta_j(C)=D_{j-1}(C)\setminus D_j(C),
 \qquad
 \eta_j(C)=E_j(C)\setminus E_{j-1}(C).
\tag{1.2}
\]

The labels with \(j\le q_0\) may be reordered by changing the invisible
annular middle corner and its two inner port orders.  The labels with
\(j>q_0\) are fixed by the SCD targets themselves.  These are precisely
the pairs \(t_j(C)\) in (0.5).

The following is the only bridge fact needed below.

### Lemma 1.1 (forced-tail shift)

Let one annular-compatible bridge-one arc join distinct selected states
of \(C,C'\in\Omega\), and put

\[
 r=\min\{\rho(C),\rho(C'),H\}.
\]

Then

\[
 \boxed{
 t_j(C')=t_{j+1}(C)
 \quad(q_0+1\le j<r).}
\tag{1.3}
\]

Equivalently, the arc has tail weight exactly

\[
 (r-q_0-1)_+.
\tag{1.4}
\]

#### Proof

Truncate both full collar states to any radius \(q\) with

\[
 q_0+2\le q\le r.
\]

The two chains have distinct lower and upper rank-
\((m\mp q)\) SCD masks.  In the bridge-one classification, identity and
the promotion regimes preserving either of those masks are therefore
impossible.  After absorbing the outer collar, the surviving transition
is a genuine radius-\(q\) rotor.  Its deletion and insertion words shift
by one position.  At positions strictly outside the free inner
\(q_0\)-blocks those words are the forced labels (1.2), hence

\[
 \delta_j(C')=\delta_{j+1}(C),\qquad
 \eta_j(C')=\eta_{j+1}(C)
\]

for \(q_0+1\le j<q\).  Take \(q=r\).  There are exactly
\(r-q_0-1\) resulting pair equalities. \(\square\)

The point is that (1.3) is independent of every legal inner annular-port
permutation.  It therefore survives optimization over the entire port
transversal.

## 2. The exact top-tag overlap histogram

Assume \(m\) is sufficiently large that \(H-q_0\ge2\).  For a top
provider \(C\in\Omega_H\), use the words \(P(C),S(C)\) in (0.12).  Make
the split overlap graph \(B_H^{\rm tail}\) with left and right copies of
\(\Omega_H\), and put

\[
 C_LC'_R\in E(B_H^{\rm tail})
 \quad\Longleftrightarrow\quad S(C)=P(C').
\tag{2.1}
\]

The equalities in one tail word use distinct SCD increment labels, so
\(P(C)=S(C)\) is impossible.  Thus (2.1) has no diagonal loop.

For a word \(\tau\), put

\[
 s_\tau=|\{C:S(C)=\tau\}|,
 \qquad
 p_\tau=|\{C:P(C)=\tau\}|.
\tag{2.2}
\]

### Theorem 2.1 (exact split matching value)

The maximum matching size of the top-tail overlap graph is

\[
 \boxed{
 \nu(B_H^{\rm tail})
 =\sum_\tau\min(s_\tau,p_\tau)
 =N_H-{1\over2}\sum_\tau|s_\tau-p_\tau|.}
\tag{2.3}
\]

Consequently every annular-compatible bridge-one path cover with \(p\)
paths obeys (0.13).

#### Proof

The graph (2.1) is the disjoint union, over \(\tau\), of complete
bipartite graphs between the \(s_\tau\) source copies and the
\(p_\tau\) target copies.  Its matching number is therefore the first
quantity in (2.3).  Both histograms have total mass \(N_H\), giving the
second equality.

Mark the vertices of a full path cover according as they lie in
\(\Omega_H\).  The number of nonempty top runs is at most

\[
 (N_{q_0}-N_H)+p.
\]

Hence at least

\[
 2N_H-N_{q_0}-p
\tag{2.4}
\]

selected arcs have two top endpoints.  Lemma 1.1 puts them in (2.1), and
their split copies form a matching.  Thus

\[
 2N_H-N_{q_0}-p
 \le N_H-{1\over2}\sum_\tau|s_\tau-p_\tau|.
\]

Rearrangement gives (0.13). \(\square\)

Equation (0.13) is an explicit top-tag Hall witness which is invariant
under all invisible inner-port reorderings.  It is only necessary: the
matching in (2.3) may contain directed cycles and an overlap equality
does not by itself satisfy the complete bridge state equation.

## 3. Coherent summation over every protected tag

Let \(F\) be a directed path forest on \(\Omega\) with \(p\) components.
For \(q_0\le q\le H\), put

\[
 \Omega_q=\mathcal D_{\ge q},\qquad |\Omega_q|=N_q,
\tag{3.1}
\]

and let \(e_q(F)\) be the number of selected arcs with both endpoints in
\(\Omega_q\).

### Lemma 3.1 (exact threshold-run census)

For every \(q_0\le q\le H\),

\[
 \boxed{
 e_q(F)\ge(2N_q-N_{q_0}-p)_+.}
\tag{3.2}
\]

#### Proof

On each path mark a vertex \(\mathsf A\) when it lies in \(\Omega_q\)
and \(\mathsf B\) otherwise.  Across all paths, the number of nonempty
\(\mathsf A\)-runs is at most

\[
 (N_{q_0}-N_q)+p.
\]

Every \(\mathsf A\)-run on \(s\) vertices contributes \(s-1\) internal
arcs.  Hence

\[
 e_q(F)
 \ge N_q-(N_{q_0}-N_q+p)
 =2N_q-N_{q_0}-p.
\]

The left side is nonnegative, proving (3.2). \(\square\)

### Theorem 3.2 (coherent forced-tail obstruction)

If every edge of \(F\) is an annular-compatible bridge-one edge, then

\[
 \boxed{
 \sum_{e\in F}w(e)
 \ge
 \sum_{q=q_0+2}^{H}(2N_q-N_{q_0}-p)_+.}
\tag{3.3}
\]

In particular (0.8) holds.

#### Proof

For an edge \(e=CC'\), Lemma 1.1 says that it contributes one unit of
tail weight for every threshold

\[
 q_0+2\le q\le\min\{\rho(C),\rho(C'),H\}.
\]

Therefore

\[
 \sum_{e\in F}w(e)
 =\sum_{q=q_0+2}^{H}e_q(F).
\tag{3.4}
\]

Apply Lemma 3.1 term by term.  Since \(F\) itself is an admissible
linear forest in the SCD-only tail relaxation, its weight is at most
\(\Lambda_{\rm tail}(\mathcal D)\), proving (0.8). \(\square\)

This is stronger than maximizing a separate projected forest at every
radius: all threshold contributions in (3.3) are carried by one common
linear forest.

## 4. Gaussian evaluation

Uniformly for bounded \(x\) and \(q=x\sqrt m+O(1)\),

\[
 {N_q\over W}=e^{-x^2}+O_{a,b}(m^{-1/2}).
\tag{4.1}
\]

Put

\[
 c_{a,b}=\min\{b,\sqrt{a^2+\log2}\}.
\tag{4.2}
\]

Then a Riemann sum gives

\[
 \sum_{q=q_0+2}^{H}(2N_q-N_{q_0})_+
 =(\Psi_{a,b}+o_{a,b}(1))W\sqrt m,
\tag{4.3}
\]

with \(\Psi_{a,b}\) as in (0.10).  Its integrand is positive immediately
to the right of \(a\), so \(\Psi_{a,b}>0\) for every fixed \(a<b\).

For real \(u\) and \(p\ge0\),

\[
 (u-p)_+\ge u_+-p.
\]

There are at most \(H-q_0\) summands, so (0.4) gives

\[
 \sum_{q=q_0+2}^{H}(2N_q-N_{q_0}-p)_+
 \ge(\Psi_{a,b}+o(1))W\sqrt m-Hp
 =(\Psi_{a,b}+o(1))W\sqrt m.
\tag{4.4}
\]

This proves (0.9).  Finally \(w(e)\le H-q_0-1\); divide (0.9) by this
quantity to obtain (0.11). \(\square\)

## 5. Exact weighted ordered-Hall form

For a total order \(\prec\) on \(\Omega\), form the split bipartite graph
\(B_{\prec}^{\rm tail}(\mathcal D)\) whose edges are the pairs
\(C_LC'_R\) with

\[
 C\prec C',\qquad w(C,C')>0,
\]

and give such an edge weight \(w(C,C')\).  Let \(\nu_w\) denote maximum
matching weight.

### Theorem 5.1 (weighted ordered-Hall equality)

\[
 \boxed{
 \Lambda_{\rm tail}(\mathcal D)
 =\max_{\prec}\nu_w(B_{\prec}^{\rm tail}).}
\tag{5.1}
\]

For fixed \(\prec\), the exact dual is

\[
 \boxed{
 \nu_w(B_{\prec}^{\rm tail})
 =\min\left\{
  \sum_{C\in\Omega}u_C+\sum_{C\in\Omega}v_C:
  u_C+v_{C'}\ge w(C,C')
  \text{ on every forward edge},\ u,v\ge0
 \right\}.}
\tag{5.2}
\]

#### Proof

A directed linear forest has a topological order.  Its split edges form a
matching in the corresponding forward graph with the same total weight.
Conversely a matching of forward arcs gives indegree and outdegree at
most one, and strict increase in \(\prec\) excludes a directed cycle.
This proves (5.1).  Equation (5.2) is the standard linear-programming dual
of maximum-weight bipartite matching. \(\square\)

Thus a universal refutation of the SCD route would follow from proving
that every SCD and every order admit dual potentials in (5.2) of total
cost

\[
 <(\Psi_{a,b}-\varepsilon)W\sqrt m
\]

for some fixed \(\varepsilon>0\).  Conversely a large value in (5.1) is
only a necessary relaxation: it need not lift to one port transversal or
to literal bridge-one arcs.

## 6. One support functional for the tail, top-tag, and full-top cuts

Fix an annular port transversal \(\sigma\).  In its actual bridge-one
digraph, for an arc \(e=CC'\), let

\[
 f(e)=\mathbf1\{e\text{ is a genuine full-radius-}H\text{ rotor}\},
\]

\[
 h(e)=\mathbf1\{C,C'\in\Omega_H\}.
\tag{6.1}
\]

For \(\alpha,\beta\ge0\), define

\[
 W_{\alpha,\beta}(e)
 =w(e)+\alpha f(e)+\beta h(e),
\tag{6.2}
\]

and let \(\Lambda_{\alpha,\beta}(\mathcal D,\sigma)\) be the maximum
\(W_{\alpha,\beta}\)-weight of a directed linear forest in that actual
digraph.

### Theorem 6.1 (joint top support cut)

If the chosen transversal has a bridge-one path cover with \(p\) paths,
then for every \(\alpha,\beta\ge0\),

\[
 \boxed{
 \begin{aligned}
 \Lambda_{\alpha,\beta}(\mathcal D,\sigma)
 \ge{}&
 \sum_{q=q_0+2}^{H}(2N_q-N_{q_0}-p)_+\\
 &+\alpha(N_H-p)
 +\beta(2N_H-N_{q_0}-p)_+.
 \end{aligned}}
\tag{6.3}
\]

#### Proof

Use the successful path forest itself.  Theorem 3.2 gives its tail weight.
The exact full-top fibre cut gives at least \(N_H-p\) genuine full rotors.
Lemma 3.1 at \(q=H\) gives at least
\((2N_H-N_{q_0}-p)_+\) top-to-top arcs.  Such arcs are genuine full
rotors, but double counting them is intentional because (6.2) assigns
both bonuses.  Summing the three valid contributions proves (6.3).
\(\square\)

For fixed \((\sigma,\prec)\), the maximum in Theorem 6.1 is again a
maximum-weight forward matching and has the vertex-potential dual (5.2)
with \(W_{\alpha,\beta}\) in place of \(w\).  Hence (6.3) is a genuine
joint ordered-Hall obstruction: tail weight, full rotors, and top-to-top
rotors must occur in one common forest, not in three separately optimized
certificates.

Taking \(\alpha=\theta\sqrt m\), \(\beta=\kappa\sqrt m\) and using
\(p=o(W/H)\) yields

\[
 \boxed{
 \Lambda_{\theta\sqrt m,\kappa\sqrt m}
 \ge
 \left[
  \Psi_{a,b}+\theta e^{-b^2}
  +\kappa(2e^{-b^2}-e^{-a^2})_+
  +o_{a,b,\theta,\kappa}(1)
 \right]W\sqrt m.}
\tag{6.4}
\]

The \(\kappa\)-term is active exactly in the old narrow range
\(b^2-a^2<\log2\); the coherent tail and full-top terms remain positive
for every fixed annulus.

## 7. Proved boundary and remaining gate

Proved here:

1. the top-tail overlap graph has the exact histogram matching value
   (2.3), giving the port-invariant cut (0.13);
2. one path forest must carry the sum of all protected-threshold run
   demands, giving the coherent weighted obstruction (0.8);
3. its Gaussian value is \((\Psi_{a,b}+o(1))W\sqrt m\), with
   \(\Psi_{a,b}>0\) for every fixed \(a<b\);
4. consequently every successful SCD has a positive-density linear
   forest of nontrivial forced-tail overlaps, even for wide annuli;
5. the obstruction has the exact maximum-weight ordered-Hall dual
   (5.1)--(5.2); and
6. the coherent tail, full-top, and top-tag cuts combine into the single
   support inequality (6.3).

Not proved here:

1. a noncanonical SCD attaining these lower bounds;
2. a universal upper bound on \(\Lambda_{\rm tail}(\mathcal D)\) below
   (0.9);
3. a port transversal lifting a large tail forest to the actual bridge
   graph; or
4. the coefficient-one annulus theorem.

The construction target is therefore sharper than “many top-tag edges.”
One noncanonical SCD must arrange a single positive-density linear forest
whose chain tails form long suffix-prefix windows, while the same forest
contains the full-rotor mass required by the full-top fibre cut and has
ordered-Hall deficiency \(o(W/H)\).  Separate layerwise matchings do not
meet this gate.
