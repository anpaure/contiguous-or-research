# The exact Q2-associator birth--death operator and the three-halves visibility gate

Date: 2026-07-26

Method: pure mathematics only.  No search, computation, solver, or web input is
used.

## 0. Outcome

Fix a perfect matching of the (2m) ordinary coordinates and, when working in
the literal odd ground set, fix the remaining coordinate (infty).  The exact
pair-frame (Q_2) associator has normalized lower type polynomial

\[
 \phi(z)={16+8z\over24}={2+z\over3}
\]

on its old shore and polynomial (1) on its recoupled shore.  Thus one
effective forward recoupling erases exactly one
\({\rm Bernoulli}(1/3)\) full-pair contribution.  Its reciprocal reinstates
that contribution.  Tensoring gives an exact pure-death chain, and its
reciprocal closure is an explicit reversible birth--death chain with binomial
stationary law.

The type law of a genuinely uniform rank deletion is governed by a different
exact chain.  At paired-rank defect (a), its death probability from type (f)
is

\[
                         {2f\over m-a}.
\]

In the Gaussian band this is (1/2+O(m^{-1/2})), whereas one effective
associator layer has mean drift (1/3).  Consequently the number of visible
associator layers required by depth (q) is

\[
 \boxed{
 L^*_{\varepsilon,q}
 =3(\mu_\varepsilon-\mu_{\varepsilon+q})
 ={3q(2m-2\varepsilon-q-1)\over2(2m-1)}
 ={3q\over2}+O_A(1)
 }
\]

uniformly for (q\le A\sqrt m) and
\(\varepsilon\in\{0,1\}\).  Moreover

\[
 L^*_{\varepsilon,q+1}-L^*_{\varepsilon,q}
 ={3(m-\varepsilon-q-1)\over2m-1}
 ={3\over2}+O_A(m^{-1/2}).
\]

This gives a sharp architectural verdict.

* In the audited disjoint tensor packet, a depth-(q) window sees at most
  (q) associator blocks.  Its largest possible mean displacement is (q/3),
  while the target displacement is (q/2+O_A(1)).  At
  (q=x\sqrt m+o(\sqrt m)), its symmetric maximal-drift law stays a positive
  total-variation distance at least
  \(2\Phi(x/3)-1-o(1)\) from the uniform target type law.
* There is no Gaussian type-law obstruction to an overlapping construction
  which makes (L^*_{\varepsilon,q}) layers visible by depth (q).  After
  rounding (L^*), the associator process and the true target law have the
  same limiting normal law, uniformly through every fixed Gaussian window.
  Thus the exact remaining physical requirement is average overlap
  multiplicity (3/2) per new window direction, together with literal
  completion and long-cycle compatibility.

The second statement is a fractional/type-law statement.  It does not prove
individual labelled target quotas, outer-packet collision control, or that
overlapping local factor trades compose.

## 1. The exact uniform-deletion type chain

On the (2m) paired coordinates, let defect (a) mean rank (m-a).  A type
(f) set then has

\[
 f\text{ full pairs},\qquad f+a\text{ empty pairs},\qquad
 m-a-2f\text{ split pairs}.
\]

Its normalized type law is

\[
 \pi_a(f)=
 {1\over\binom{2m}{m-a}}
 {m!\,2^{m-a-2f}\over
 f!(f+a)!(m-a-2f)!}.
\tag{1.1}
\]

Choose one of the (m-a) present coordinates uniformly and delete it.  A
full pair supplies (2f) present coordinates, and deleting either changes
type (f) to (f-1).  A split pair supplies one present coordinate and its
deletion leaves (f) unchanged.  Hence the exact kernel is

\[
 \boxed{
 K_a(f,f-1)={2f\over m-a},\qquad
 K_a(f,f)={m-a-2f\over m-a}.}
\tag{1.2}
\]

Direct counting, or the construction itself, gives

\[
                         \pi_aK_a=\pi_{a+1}.
\tag{1.3}
\]

The reverse insertion kernel is

\[
 \boxed{
 K_a^*(g,g+1)={m-2g-a-1\over m+a+1},\qquad
 K_a^*(g,g)={2(g+a+1)\over m+a+1}.}
\tag{1.4}
\]

Indeed a defect-(a+1), type-(g) set has
\(m-2g-a-1\) split pairs whose missing endpoint completes a full pair and
\(g+a+1\) empty pairs, contributing two missing endpoints each.  Uniform
deletion flags prove the cross-rank detailed-balance identity

\[
 \pi_a(f)K_a(f,g)=\pi_{a+1}(g)K_a^*(g,f).
\tag{1.5}
\]

Consequently (H_a=K_aK_a^*) is a birth--death chain on the defect-(a)
types, reversible with stationary law (pi_a).  Its two off-diagonal
probabilities are

\[
 H_a(f,f-1)
 ={4f(f+a)\over(m-a)(m+a+1)},
\tag{1.6}
\]

\[
 H_a(f,f+1)
 ={(m-a-2f)(m-a-2f-1)\over(m-a)(m+a+1)}.
\tag{1.7}
\]

These formulas give the requested exact stationary/reversible operator; no
entropy approximation is involved.

## 2. Drift, variance, and the odd infinity sectors

If (F_a\sim\pi_a), then

\[
 \boxed{
 \mu_a:=\mathbb EF_a
 ={(m-a)(m-a-1)\over2(2m-1)}.}
\tag{2.1}
\]

This follows either by summing (1.2) or by writing (F_a) as the sum of the
indicators that the two endpoints of each pair are selected.  More precisely,
with (k=m-a),

\[
 A_k={(k)_2\over(2m)_2},\qquad B_k={(k)_4\over(2m)_4},
\]

\[
 \boxed{
 \operatorname{Var}F_a
 =mA_k(1-A_k)+m(m-1)(B_k-A_k^2).}
\tag{2.2}
\]

For (a=O_A(\sqrt m)), this is (m/16+o_A(m)).  The one-step conditional
drift and noise are

\[
 \mathbb E(F_{a+1}-F_a\mid F_a=f)=-{2f\over m-a},
\tag{2.3}
\]

\[
 \operatorname{Var}(F_{a+1}-F_a\mid F_a=f)
 ={2f\over m-a}\left(1-{2f\over m-a}\right).
\tag{2.4}
\]

The literal odd middle layer has two sectors.  If (infty) is absent, the
paired part starts at defect (\varepsilon=0); if it is present, it starts at
defect (\varepsilon=1).  Associators avoiding (infty) preserve this bit,
and a depth-(q) paired deletion therefore changes
\(pi_\varepsilon\) to (pi_{\varepsilon+q}).  Its exact mean displacement is

\[
 \boxed{
 \Delta_{\varepsilon,q}
 :=\mu_\varepsilon-\mu_{\varepsilon+q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}.}
\tag{2.5}
\]

If a window uses (infty), separate that one step; it changes the paired
defect by (q-1), so all Gaussian conclusions below change by only one
bounded layer.

Complementation gives the identical formulas for upper shadows when their
type is indexed by the number of empty old-frame pairs.  Thus the
three-halves count below is two-sided; only the names "full" and "empty" are
interchanged.

For (q=x\sqrt m+o(\sqrt m)) and fixed (\varepsilon), Stirling's formula
gives

\[
 {F_{\varepsilon+q}-m/4\over\sqrt m}
 \Longrightarrow N(-x/2,1/16).
\tag{2.6}
\]

Equivalently, along the coupled deletion process,

\[
 F_{\varepsilon+q}
 =F_\varepsilon-{q\over2}+O_p(m^{1/4}+1).
\tag{2.7}
\]

The (O_p(m^{1/4})) term is the accumulated Bernoulli noise from
(O(\sqrt m)) deletions; it vanishes after division by (sqrt m).

## 3. The exact Q2 associator operator

For the old and recoupled shores of the exact pair-frame associator, the
lower type ledgers relative to the old matching are

\[
                         16f_0+8f_1,qquad 24f_0.
\tag{3.1}
\]

After adjoining an outside core of type (C), (3.1) says exactly

\[
 C+B\longmapsto C,qquad B\sim{\rm Bernoulli}(1/3),
\tag{3.2}
\]

when occurrences are normalized uniformly on the 24-state packet.  The same
identity holds at every depth at which the window touches one or both local
directions; an untouched block has identical old and new ledgers.

Let

\[
 b_N(j)=\binom Nj(1/3)^j(2/3)^{N-j}.
\]

Deleting a uniformly chosen old local contribution gives

\[
 \boxed{
 D_N(j,j-1)={j\over N},\qquad D_N(j,j)=1-{j\over N},}
\tag{3.3}
\]

and (b_ND_N=b_{N-1}).  The reciprocal insertion is

\[
 \boxed{
 U_N(j,j+1)={1\over3},\qquad U_N(j,j)={2\over3},}
\tag{3.4}

and (b_{N-1}U_N=b_N).  The two kernels satisfy the exact cross-size
detailed-balance identities

\[
 b_N(j){N-j\over N}={2\over3}b_{N-1}(j),
\qquad
 b_N(j){j\over N}={1\over3}b_{N-1}(j-1).
\tag{3.5}
\]

The fixed-(N) heat-bath closure (Q_N=D_NU_N) is therefore reversible
with stationary law (b_N).  Explicitly,

\[
 Q_N(j,j-1)={2j\over3N},\qquad
 Q_N(j,j+1)={N-j\over3N},
\tag{3.6}
\]

and the remaining probability stays at (j).  Its conditional drift and
second moment are

\[
 \boxed{
 \mathbb E(\Delta j\mid j)={1\over3}-{j\over N},
\qquad
 \mathbb E((\Delta j)^2\mid j)={N+j\over3N}.}
\tag{3.7}
\]

This is the ordinary random-scan Bernoulli heat bath.  Its eigenvalues on
degree-(ell) Krawtchouk modes are (1-\ell/N); in particular its gap is
(1/N).  This spectral observation concerns the symmetrized type operator,
not the unproved physical composition of overlapping factor trades.

For (r) tensor slots and (t) effective forward shore changes, the exact
normalized type polynomial in a packet with outside core (C) is

\[
 z^C\left({2+z\over3}\right)^{r-t}.
\tag{3.8}
\]

Thus

\[
 F_t=C+{\rm Bin}(r-t,1/3),
\tag{3.9}
\]

and, in the natural coupling,

\[
 F_0-F_t\sim{\rm Bin}(t,1/3),qquad
 \mathbb E(F_0-F_t)={t\over3},qquad
 \operatorname{Var}(F_0-F_t)={2t\over9}.
\tag{3.10}
\]

At the coefficient level, if (eta) is the type law of the core together
with the other slots, one forward layer has the exact signed divergence

\[
 \nu^{\rm new}_f-\nu^{\rm old}_f
 ={1\over3}(\eta_f-\eta_{f-1}).
\tag{3.11}
\]

This is the orbit-level form of the associator's signed drift.

### 3.1 Wreath-symmetrized frame incidence

There is no hidden change from (1/3) to (1/2) after averaging over all
placements of one local frame.  Fix a defect-(a), type-(f) owner and put

\[
                         s=m-a-2f.
\]

For an eligible associator embedding, the two reservoir pairs must be split.
The two special old-frame pairs are either one full and one empty, which is
the type-decreasing local state, or two further split pairs, which is the
neutral local state.  Up to role-label constants common to both cases, the
numbers of incidences are

\[
 H_{a,f}=f(f+a)\binom{s}{2},
 \qquad
 L_{a,f}=\binom{s}{2}\binom{s-2}{2}.
\tag{3.12}
\]

Consequently a uniformly chosen eligible frame incidence is decreasing with
exact probability

\[
 \boxed{
 p_{a,f}={f(f+a)\over f(f+a)+\binom{s-2}{2}}.}
\tag{3.13}
\]

At the Gaussian center write

\[
 f={m\over4}-{a\over2}+z\sqrt m,
 \qquad a=O_A(\sqrt m),\quad z=O_A(1).
\]

Then direct expansion of (3.13) gives

\[
 p_{a,f}={1\over3}+{32z\over9\sqrt m}+O_A(m^{-1}).
\tag{3.14}
\]

Thus uniform wreath-incidence symmetrization changes the drift only by
(O_A(m^{-1/2})) per layer throughout the Gaussian band.  Over
(O_A(\sqrt m)) layers this contributes only (O_A(1)) to the unscaled
mean and cannot replace the missing factor (3/2).  Formula (3.13) by itself
does not rule out a nonuniform state-adaptive incidence choice.  The robust
fact for literal trades is instead (3.1): every completed selected packet
ties eight decreasing starts to sixteen neutral starts and hence has aggregate
per-start drift exactly (1/3).  Turning a desired incidence weighting into one
simultaneous factor trade still requires a regular integral packing.

## 4. The disjoint-tensor ceiling

In the sibling-block recursive cycle factor, every depth-(q) window with
(q\le r) touches exactly (q) distinct local blocks and at most one
direction in each.  A local shore change is invisible when its block is
untouched.  Hence even if every touched block is put on the forward
recoupled shore,

\[
                         t\le q.
\tag{4.1}
\]

By (3.10), the maximum symmetric mean displacement is (q/3).  By (2.5),
the required displacement exceeds it whenever (q<(2m-2\varepsilon-1)/3),
and the exact gap is

\[
 \boxed{
 \Delta_{\varepsilon,q}-{q\over3}
 ={q(2m-6\varepsilon-3q-1)\over6(2m-1)}
 ={q\over6}+O_A(1).}
\tag{4.2}
\]

For (q=x\sqrt m+o(\sqrt m)), the all-touched-new tensor law has limiting
scaled type distribution

\[
 N(-x/3,1/16),
\tag{4.3}
\]

whereas the uniform target law has limit (2.6).  Taking the fixed threshold
midway between the two limiting means proves

\[
 \boxed{
 \liminf {1\over2}\|\mathcal L_{\rm tensor}-\pi_{\varepsilon+q}\|_1
 \ge 2\Phi(x/3)-1>0.}
\tag{4.4}
\]

Equation (4.4) applies to the symmetric maximal-drift tensor operator.  The
mean ceiling (4.2) applies to every disjoint tensor selection.  A fully
state-adaptive nonsymmetric selection requires a separate concentration
argument before upgrading the mean ceiling to the same explicit
total-variation constant.

## 5. The three-halves overlap criterion

To match the target mean exactly, the effective visible-layer count must be

\[
 L^*_{\varepsilon,q}=3\Delta_{\varepsilon,q}
 ={3q(2m-2\varepsilon-q-1)\over2(2m-1)}.
\tag{5.1}
\]

For all (q\le A\sqrt m), this is monotone and its one-depth increments are

\[
 L^*_{\varepsilon,q+1}-L^*_{\varepsilon,q}
 ={3(m-\varepsilon-q-1)\over2m-1}.
\tag{5.2}
\]

Thus rounding the cumulative sequence permits an integral schedule with one
or two new visible layers at each physical depth and average multiplicity
(3/2+o_A(1)).  A convenient fractional schedule mixes the two adjacent
integers so that its expectation is exactly (5.1).

Let (widehat L_{\varepsilon,q}) be any integer rounding with error at most
one.  Coupling the erased local bits gives, uniformly for (q\le A\sqrt m),

\[
 \sup_{q\le A\sqrt m}
 {1\over\sqrt m}
 \left|
 {\rm Bin}(\widehat L_{\varepsilon,q},1/3)
 -\Delta_{\varepsilon,q}
 \right|\ \longrightarrow_p\ 0.
\tag{5.3}
\]

Indeed the rounding error is bounded and the maximal centered partial sum
has variance (O_A(\sqrt m)), so Doob's inequality makes (5.3) immediate.
Combining (5.3) with the source central limit theorem yields the same limiting
law (2.6) at every Gaussian depth.  Therefore a (3/2)-overlap atlas has no
remaining Gaussian full-pair-type capacity obstruction.

What (5.3) does not supply is precisely the physical gate: one must construct
completed exact factor trades in which a physical window direction is visible
to one or two overlapping associators according to the schedule (5.2), while
the ownership overlap stays in long cycles and the added interfaces have
subcritical seam cost.  The disjoint tensor bank cannot do this, but the
birth--death calculation does not obstruct such an overlapping bank.
