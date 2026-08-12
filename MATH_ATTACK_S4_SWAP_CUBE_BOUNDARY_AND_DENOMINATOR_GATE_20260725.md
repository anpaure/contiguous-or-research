# Four-antichain quarantine and the exact swap-cube boundary lemma

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

In the adjacent-switch catalogue, fixing the carrier labelling and the
non-switch decorations leaves a Boolean swap cube

\[
 \mathcal C_d\cong\{0,1\}^d,
 \qquad d=\Theta(M).
 \tag{0.1}
\]

Dynamic four-antichain quarantine deletes at most an

\[
 \eta=m^{-4+o(1)}
 \tag{0.2}
\]

fraction of the full catalogue in every nonexceptional fibre.  The exact
cube lemma below shows that, for every

\[
 t\le(4-\varepsilon)\log_2m,
 \tag{0.3}
\]

all but (m^{-\varepsilon/2+o(1)}) of the surviving cube vertices lie in
at least a (1-m^{-\varepsilon/2+o(1)}) fraction of completely undeleted
(t)-faces through them.  Each such face supplies (2^t) integral local
swap alternatives.

This is a genuine denominator reservoir and is much stronger than merely
retaining a (1-\eta) fraction of the catalogue.  It is, however, not a
complete hereditary lower-degree theorem.  A deleted set of density
(2^{-t}) may be one entire codimension-(t) face, so a residual rule
which deterministically forces that particular face can still have zero
degree.  The exact remaining condition is **face diffusion**: the
owner/priority history must not concentrate its forced local swap face on
the exceptional (O(2^t\eta)) fraction of hit faces.

Combined with the two-link branching parameter

\[
 \beta={g\over m}(C\log m)^6=m^{-1/2+o(1)},
 \tag{0.4}
\]

this reduces the denominator issue to a logarithmic-face witness-tree
estimate.  That estimate is not proved here.

## 1. Exact face counts

Let (Z\subseteq\mathcal C_d) be deleted, with

\[
 |Z|=\eta2^d.
 \tag{1.1}
\]

A (t)-face is obtained by choosing (t) free coordinates and fixing
the other (d-t).  Hence

\[
 N_t=2^{d-t}\binom dt
 \tag{1.2}
\]

is the number of (t)-faces.  Every vertex lies in exactly

\[
 \binom dt
 \tag{1.3}
\]

such faces.

### Theorem 1.1 (global cube boundary)

Let (mathcal H_t(Z)) be the family of (t)-faces meeting (Z).  Then

\[
 \boxed{
 { |\mathcal H_t(Z)|\over N_t}
 \le\min\{1,2^t\eta\}.}
 \tag{1.4}
\]

More generally, if (mathcal H_{t,\theta}(Z)) is the family of
(t)-faces having deleted density greater than (	heta), then

\[
 \boxed{
 {|\mathcal H_{t,\theta}(Z)|\over N_t}
 \le {\eta\over\theta}.}
 \tag{1.5}
\]

#### Proof

Count incidences ((z,F)) with (z\in Z\cap F).  Their number is

\[
 |Z|\binom dt=\eta2^d\binom dt.
 \tag{1.6}
\]

Every hit face contributes at least one incidence, giving

\[
 |\mathcal H_t(Z)|
 \le\eta2^d\binom dt
 =2^t\eta N_t.
\]

Every face in (mathcal H_{t,\theta}(Z)) contributes more than
(	heta2^t) incidences.  Divide (1.6) by this quantity to obtain
(1.5).  \(\square\)

## 2. Local faces through a typical vertex

For (x\in\mathcal C_d), put

\[
 q_t(x)=
 {\#\{t\hbox{-faces }F\ni x:F\cap Z\ne\varnothing\}
  \over\binom dt}.
 \tag{2.1}
\]

### Theorem 2.1 (local all-good face reservoir)

For every (delta>0), all but a

\[
 {2^t\eta\over\delta}
 \tag{2.2}

fraction of the cube vertices satisfy

\[
 \boxed{q_t(x)\le\delta.}
 \tag{2.3}
\]

In particular, with (delta=\sqrt{2^t\eta}), all but a
(sqrt{2^t\eta}) fraction of vertices lie in at least a

\[
 1-\sqrt{2^t\eta}
 \tag{2.4}

fraction of completely undeleted (t)-faces through them.

#### Proof

The incidence graph between vertices and (t)-faces is biregular.
Therefore

\[
 {1\over2^d}\sum_xq_t(x)
 ={ |\mathcal H_t(Z)|\over N_t}
 \le2^t\eta
 \tag{2.5}
\]

by Theorem 1.1.  Markov's inequality gives (2.2)--(2.3), and the stated
choice of (delta) gives (2.4).  \(\square\)

### Corollary 2.2 (the (s=4) scale)

If (eta=m^{-4+o(1)}) and

\[
 t\le(4-\varepsilon)\log_2m,
 \tag{2.6}
\]

then

\[
 \sqrt{2^t\eta}=m^{-\varepsilon/2+o(1)}.
 \tag{2.7}

Thus almost every candidate lies in almost every logarithmic-dimensional
swap face through it which is wholly preserved by quarantine.

For example, at (t=2\log_2m), every all-good face contains (m^2)
integral switch alternatives, while the exceptional vertex and face
fractions are both at most (m^{-1+o(1)}).

## 3. Disjoint unions of catalogue cubes

A fibre is a disjoint union of swap cubes indexed by the carrier
labelling and the decorations not involved in the adjacent switches.
Suppose quarantine deletes at most an (eta)-fraction of the whole fibre.
Apply Theorems 1.1 and 2.1 to the disjoint union: the face-incidence graph
remains biregular, so the same conclusions hold without first requiring
that every individual cube have deletion density at most (eta).

Equivalently, the total number of hit (t)-faces throughout the fibre is
at most

\[
 2^t\eta\times
 (\hbox{total number of }t\hbox{-faces in the fibre}).
 \tag{3.1}
\]

This is the form needed after the deterministic dynamic-quarantine
ledger, which controls a full fibre but not every phase-labelling cube
separately.

## 4. A sharp limitation: a forced face can be dead

The factor (2^teta) in (1.4) is sharp.  Let (F_0) be one fixed
(t)-face and take

\[
 Z=F_0.
 \tag{4.1}
\]

Then (eta=2^{t-d}).  The residual rule which forces exactly the face
(F_0) has no surviving candidate, even though the deleted fraction of
the ambient cube is exponentially small.

At the catalogue scale, the analogous construction deletes a union of
rare faces selected by a structured owner/priority history.  Therefore
Theorem 2.1 cannot by itself supply a deterministic lower bound for every
conditional residual fibre.

## 5. The exact face-diffusion gate

Let (mathsf F_s) be the random (t)-face of local swaps left free by
the owner/priority constraints at sequential time (s).  Let
(mathrm{Unif}_t) denote the uniform distribution on all (t)-faces of
the relevant fibre.  A sufficient face-diffusion condition is

\[
 \Pr(\mathsf F_s\in\mathcal A\mid\mathcal F_s)
 \le\chi_s\,\mathrm{Unif}_t(\mathcal A)
 \tag{5.1}
\]

for every family of faces (mathcal A).  Theorem 1.1 then gives

\[
 \boxed{
 \Pr(\mathsf F_s\cap Z\ne\varnothing\mid\mathcal F_s)
 \le\chi_s2^t\eta.}
 \tag{5.2}
\]

Thus any

\[
 \chi_s=m^{o(1)},\qquad
 t\le(4-\varepsilon)\log_2m
 \tag{5.3}
\]

makes the quarantine obstruction negligible.

Condition (5.1) is far weaker than pointwise diffusion over the full
exponential candidate catalogue.  It asks only that the logarithmic local
swap face retain subpolynomial density distortion.

### Theorem 5.1 (free-coordinate escape; no diffusion needed)

There is a deterministic alternative to (5.1).  Fix a surviving cube
vertex (x), and suppose a set (R_x\subseteq[d]) of (L) switch coordinates
is **jointly free**: toggling an arbitrary subset of (R_x) preserves all
owner/priority constraints before quarantine.  Thus (x) lies in one
feasible (L)-face.

If

\[
 \frac{\binom Lt}{\binom dt}>q_t(x),
 \tag{5.4}
\]

then the feasible (L)-face contains a completely undeleted (t)-face
through (x).

#### Proof

Exactly (\binom Lt) of the (t)-faces through (x) use only coordinates in
(R_x), and every one of them is feasible before quarantine.  Fewer than
(q_t(x)\binom dt) of all (t)-faces through (x) meet the quarantine set.
Inequality (5.4) leaves at least one feasible face which is wholly
undeleted.  \(\square\)

Take (z=1/\log m), and suppose

\[
 L\ge zd/2.
 \tag{5.5}
\]

For (t=o(zd)),

\[
 \frac{\binom Lt}{\binom dt}
 \ge\left(\frac z3\right)^t.
 \tag{5.6}
\]

Choose

\[
 t=\left\lfloor
 (2-\varepsilon)\frac{\log m}{\log\log m}
 \right\rfloor.
 \tag{5.7}
\]

Then the right side of (5.6) is

\[
 m^{-2+\varepsilon+o(1)},
 \tag{5.8}
\]

whereas Theorem 2.1, with (\eta=m^{-4+o(1)}), gives

\[
 q_t(x)\le\sqrt{2^t\eta}=m^{-2+o(1)}
 \tag{5.9}
\]

for all but (m^{-2+o(1)}) of the cube vertices.  Therefore every typical
vertex satisfying (5.5) lies in an intact feasible face of size

\[
 2^t=\exp\left((2-\varepsilon+o(1))
 {\log2\,\log m\over\log\log m}\right)=m^{o(1)}.
 \tag{5.10}
\]

Thus face diffusion can be replaced by the following still weaker local
condition:

> enough current candidates have at least (zd/2) jointly free adjacent
> switch coordinates.

For disjoint adjacent switches, owner feasibility is coordinatewise, so
the owner-compatible vertices inside one swap cube are either empty or a
face; its dimension is exactly the number of coordinates for which both
local owner alternatives remain unused.  The unresolved content is a
lower bound on that face dimension for enough of the currently relevant
cubes.  This is a one-star/free-toggle statement, rather than full
candidate point-mass diffusion.

### Corollary 5.2 (an averaged swap-edge condition suffices)

Let (\mathcal A) be the current owner-compatible candidates in one fibre,
before quarantine, and let (L(x)) be the number of jointly free adjacent
switches at (x).  Because feasibility inside each swap cube is a face,
(L(x)) is exactly the degree of (x) in the induced swap graph.  Put

\[
 \overline L=
 {1\over|\mathcal A|}\sum_{x\in\mathcal A}L(x)
 ={2e_{\rm swap}(\mathcal A)\over|\mathcal A|}.
 \tag{5.11}
\]

If

\[
 \boxed{\overline L\ge zd,}
 \tag{5.12}
\]

then at least a (z/(2-z)\ge z/2) fraction of current candidates satisfy

\[
 L(x)\ge zd/2.
 \tag{5.13}
\]

#### Proof

If a fraction (p) satisfies (5.13), then, using (L(x)\le d),

\[
 \overline L
 \le pd+(1-p)zd/2.
\]

Combine this with (5.12) and solve for (p).  \(\square\)

Since (z/2\gg m^{-2+o(1)}) at (z=1/\log m), the quarantine-atypical
vertices from (5.9) cannot exhaust the rich candidates.  Therefore
(5.12), together with Theorem 5.1, gives an intact logarithmic swap face
in every fibre satisfying the averaged swap-edge condition.

The denominator problem has consequently been reduced to the single
first-order lower-link inequality (5.12).  It asks for the induced
adjacent-switch edge density of the current candidate set, not for
pointwise diffusion or a full higher-codegree hierarchy.

### 5.3 The unweighted Johnson baseline is automatic

There is no set-level obstruction to (5.12).  Let

\[
 \mathcal O_U\subseteq\binom Um,qquad |U|=M=m+H,
 \tag{5.14}
\]

have density (\zeta).  The Johnson graph (J(M,m)) has degree (mH) and
smallest eigenvalue (-H).  The standard least-eigenvalue expansion gives

\[
 \boxed{
 {2e_{J(M,m)}(\mathcal O_U)\over|\mathcal O_U|}
 \ge mH\zeta-H(1-\zeta).}
 \tag{5.15}
\]

#### Proof

Write the indicator of (\mathcal O_U) as
(\zeta\mathbf1+f), with (f\perp\mathbf1).  If (A_J) is the Johnson
adjacency matrix, then

\[
\begin{aligned}
 2e(\mathcal O_U)
 &=\zeta^2\,|V|mH+\langle f,A_Jf\rangle\\
 &\ge\zeta^2\,|V|mH-H\|f\|_2^2\\
 &=|V|\bigl(\zeta^2mH-H\zeta(1-\zeta)\bigr).
\end{aligned}
\]

Divide by (|\mathcal O_U|=\zeta|V|).  \(\square\)

Thus a uniformly sampled local Johnson neighbour of an unused owner is
unused with average probability at least

\[
 \zeta-\frac{1-\zeta}{m}.
 \tag{5.16}
\]

The disjoint adjacent-switch diamonds are coordinate-transitive over
these local Johnson edges before conditioning on the other phases of the
path.  Therefore (5.15) supplies exactly the desired (z-o(z)) free-toggle
fraction in the **unweighted local-diamond measure**.

What is not automatic is preservation of (5.15) after weighting a local
diamond by the number of full currently feasible path extensions through
it.  That extension bias is another form of the weighted two-link/bow-tie
gate.  Hence the remaining theorem may be stated even more narrowly:

> prove that feasible-extension weights do not move a linear proportion
> of their mass from the internal Johnson edges in (5.15) onto its
> boundary.

The exact (L^2) threshold is elementary.

### Proposition 5.3 (weighted Johnson expansion)

Let (\mu) be the uniform probability measure on oriented local Johnson
edges whose tail lies in (\mathcal O_U), and let

\[
 I(e)=\mathbf1_{\{\text{head}(e)\in\mathcal O_U\}}.
 \tag{5.17}
\]

Let (w(e)\ge0) be feasible-extension weights, normalized by

\[
 \mathbb E_\mu w=1,
 \qquad
 \mathbb E_\mu(w-1)^2\le\sigma^2.
 \tag{5.18}
\]

Then the weighted internal-edge fraction satisfies

\[
 \boxed{
 \mathbb E_\mu[wI]
 \ge
 \zeta-\frac{1-\zeta}{m}-\sigma.}
 \tag{5.19}
\]

#### Proof

Equation (5.16) gives

\[
 \mathbb E_\mu I\ge\zeta-(1-\zeta)/m.
\]

By Cauchy--Schwarz,

\[
 |\mathbb E_\mu[(w-1)I]|
 \le\|w-1\|_2\|I\|_2\le\sigma.
\]

Add the two identities.  \(\square\)

At the stopping density (\zeta=z=1/\log m), any

\[
 \sigma=o(1/\log m)
 \tag{5.20}
\]

gives the averaged swap-edge lower bound (5.12), with room to spare.
The variance in (5.18) is exactly a two-extension/common-link square, so
Proposition 5.3 identifies the quantitative target for the bow-tie
martingale rather than introducing a new kind of obstruction.

## 6. Pairing with the two-link census

In the four-antichain architecture, every selected/candidate intersection
has width at most three.  The two-link common-neighbour expansion has raw
successive-span ratio

\[
 \beta={g\over m}(Cw)^6,
 \qquad w\le\log m,
 \tag{6.1}
\]

and hence

\[
 \beta=m^{-1/2+o(1)}.
 \tag{6.2}
\]

The formal witness-tree route is now:

1. use an intact logarithmic swap face to provide a local denominator;
2. charge every failure of face diffusion to a two-link witness branch;
3. sum the witness trees with branching factor (\beta);
4. use (\beta\log\log m=o(1)) over the effective nibble time.

Steps 1 and 3 have the exact numerical room required.  Step 2—the map
from a concentrated forced face to a two-link witness—is the remaining
unproved combinatorial lemma.

Equivalently, let (w_s(e)) be the number of currently feasible full path
extensions through an oriented local diamond (e), normalized to mean one
under the uniform diamond measure.  The single quantitative estimate
which would close the above chain is

\[
 \boxed{
 \mathbb E\bigl[(w_s-1)^2\bigr]
 \le C\beta\log\log m
 =m^{-1/2+o(1)}.}
 \tag{6.3}
\]

Indeed, (6.3) gives

\[
 \sigma=m^{-1/4+o(1)}=o(1/\log m),
 \tag{6.4}
\]

so Proposition 5.3 gives the free-toggle average, Corollary 5.2 gives many
rich candidates, and Theorem 5.1 supplies intact local swap faces.

For independently sampled obstacles, (6.3) follows by expanding the
second moment: the covariance multiplier is the common-neighbour
four-walk and the width-three two-link census has branching factor
(\beta).  What is not proved is the comparison from the actual adaptive
matching history to that independent-obstacle expansion.

## 6.1 An exact stopped-CV bootstrap

The probabilistic normalization can be separated completely from the
catalogue geometry.  Fix one oriented-diamond fibre with uniform measure
(\mu).  Let (W_s(e)) be its feasible-extension count at the beginning of
bite (s), put

\[
 \overline W_s=\mathbb E_\mu W_s,
 \qquad
 w_s=W_s/\overline W_s,
 \qquad
 \sigma_s^2=\mathbb E_\mu(w_s-1)^2.
 \tag{6.5}
\]

Let (\rho_s) be the reference one-bite contraction.  Write the normalized
conditional drift and centered fluctuation as

\[
 b_s(e)=
 {\mathbb E[W_{s+1}(e)\mid\mathcal F_s]-\rho_sW_s(e)
  \over\rho_s\overline W_s},
 \tag{6.6}
\]

\[
 \xi_s(e)=
 {W_{s+1}(e)-\mathbb E[W_{s+1}(e)\mid\mathcal F_s]
  \over\rho_s\overline W_s}.
 \tag{6.7}
\]

Bars below denote (\mu)-averages.  Stop the fibre at the first time

\[
 \sigma_s>z_s/4
 \tag{6.8}
\]

or its mean degree leaves the prescribed reference interval.

### Lemma 6.1 (abstract CV recursion)

Suppose that before the stop,

\[
 \|b_s-\bar b_s\|_2^2
 \le C\alpha^2\beta_s(1+\sigma_s^2),
 \tag{6.9}
\]

and

\[
 \mathbb E[\|\xi_s-\bar\xi_s\|_2^2\mid\mathcal F_s]
 \le C\alpha\sqrt{\beta_s}(1+\sigma_s^2),
 \tag{6.9a}
\]

and the common normalization obeys

\[
 |\bar b_s+\bar\xi_s|\le C\alpha\sqrt{\beta_s}
 \tag{6.10}
\]

on the retained outcome (with outcomes violating (6.10) charged to the
ordinary mean-degree exception ledger).  Then

\[
 \boxed{
 \mathbb E[\sigma_{s+1}^2\mid\mathcal F_s]
 \le(1+C'\alpha\sqrt{\beta_s})\sigma_s^2
 +C'\alpha\sqrt{\beta_s}.}
 \tag{6.11}
\]

#### Proof

From (6.5)--(6.7),

\[
 w_{s+1}
 ={w_s+b_s+\xi_s\over1+\bar b_s+\bar\xi_s}.
 \tag{6.12}
\]

Subtract one, square in (L^2(\mu)), and use (6.10) to expand the
denominator by a factor (1+O(\alpha\sqrt{\beta_s})).  The cross term involving
(\xi_s-\bar\xi_s) has conditional expectation zero.  Apply
(2\langle u,v\rangle\le\alpha\sqrt{\beta_s}\|u\|_2^2+
(\alpha\sqrt{\beta_s})^{-1}\|v\|_2^2) to the drift cross term and then
(6.9).
Use (6.9a) for the fluctuation square.  This gives (6.11).  \(\square\)

If (\beta_s\le\beta=m^{-1/2+o(1)}) and

\[
 \alpha R=O(\log\log m),
 \tag{6.13}
\]

iteration of (6.11) gives

\[
 \boxed{
 \mathbb E\sigma_{R\wedge\tau}^2
 =O(\sqrt\beta\log\log m)=m^{-1/4+o(1)}.}
 \tag{6.14}
\]

Since (z_s\ge z_*=1/\log m), optional stopping and Markov give

\[
 \Pr(\tau\le R)
 \le O\left({\sqrt\beta\log\log m\over z_*^2}\right)
 =m^{-1/4+o(1)}.
 \tag{6.15}
\]

The total accounting weight of these oriented-diamond/tag fibres is
(O(W)), not (O(QW)).  Hence (6.15) costs (o(W)).

Equation (6.9) is the centered one-link mean drift.  Equation (6.9a) is
**exactly** the two-link common-neighbour quadratic variation: after
expanding (\xi_s), it is the kernel (6.3) of
`MATH_ATTACK_CATALOGUE_PAIR_SQUARE_AND_BOWTIE_GATE_20260725.md`.
The following elementary three-tilt lemma supplies the required upgrade
from a raw operator bound.

### Lemma 6.2 (three stopped tilts)

Let (\mu,\nu) be probability measures on candidates (P) and tentative
chunks (E), and let (0\le h(P,E)\le1).  Define

\[
 H(P,P')=\mathbb E_{E\sim\nu}h(P,E)h(P',E).
 \tag{6.16}
\]

Assume (\|H\|_{L^2(\mu)\to L^2(\mu)}\le\beta).  If (f) and (g) are
probability densities with respect to (\mu) and (\nu), with CVs
(\sigma_f,\sigma_g), then

\[
 \boxed{
 \mathbb E_{E\sim\nu}g(E)
 \left(\mathbb E_{P\sim\mu}f(P)h(P,E)\right)^2
 \le
 \beta(1+\sigma_f^2)
 +\sigma_g\sqrt{\beta(1+\sigma_f^2)}.}
 \tag{6.17}
\]

#### Proof

Put (I(E)=\mathbb E_\mu[f(P)h(P,E)]).  The raw common-link operator
bound gives

\[
 \mathbb E_\nu I^2=\langle f,Hf\rangle
 \le\beta\|f\|_2^2=\beta(1+\sigma_f^2).
\]

Also (0\le I\le\mathbb E_\mu f=1), so

\[
 \|I^2\|_2=(\mathbb E I^4)^{1/2}
 \le(\mathbb E I^2)^{1/2}.
\]

Cauchy--Schwarz applied to (\mathbb E[(g-1)I^2]) gives (6.17).
\(\square\)

Before the stop, (\sigma_f,\sigma_g\le1/4).  Thus (6.17) is
(O(\sqrt\beta)); multiplying by the activation probability (\alpha)
is exactly (6.9a).  The centered one-link drift is the corresponding
linear operator.  Its norm is at most (\sqrt\beta\sigma_g), so after the
factor (\alpha) its squared norm satisfies (6.9).

Therefore the stopped bootstrap closes once the raw width-three census
is upgraded only to the operator statement

\[
 \boxed{
 \|H_s\|_{2\to2}\le\beta_s=m^{-1/2+o(1)}.}
 \tag{6.18}
\]

The raw Schur row sums from the width-three two-link census have the
correct value (\beta_s).  Because (H_s) is nonnegative and symmetric,
the same row bound gives (6.18) by Schur's test.  Thus, once the exact
factorial priority loss is dominated by the width-three interaction
kernel used in that census, the three adaptive tilts themselves cause no
further gap.

## 7. Exact status

Proved here:

* the global and local cube-face boundary formulas (1.4), (1.5), (2.3);
* an (m^{4-\varepsilon})-sized local swap reservoir through almost every
  candidate under (s=4) dynamic quarantine;
* the extension from one cube to the full disjoint union of catalogue
  cubes;
* the sharp forced-face obstruction;
* the precise face-diffusion criterion (5.1)--(5.2).

Still unproved:

* subpolynomial face diffusion (5.3) for the actual owner/priority
  history;
* or, alternatively, the free-toggle lower bound (5.5) on enough current
  candidates;
* equivalently, the averaged swap-edge lower bound (5.12);
* equivalently, the witness map in Step 2 of Section 6.
* equivalently, the extension-weight variance estimate (6.3) for the
  actual adaptive history.

Thus the cube boundary supplies the missing raw denominator reservoir but
does not, on its own, prove hereditary lower-degree control.
