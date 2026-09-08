# Adversarial audit of deterministic Stage B for rank-balanced partial blocks

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

There is a sharp constant-one sufficient theorem in the partial-block
language, but its Stage B hypothesis is an **integral shadow-support**
hypothesis.  Fractional rank balance is neither that hypothesis nor a way of
proving it by an ordinary flow.

For a fixed middle near-factor there is, in fact, no shadow-routing choice.
Every physical `(block,start,depth,sign)` slot has one immutable Boolean
colour.  A flow can select an occurrence of a colour which is already
present; it cannot create a missing colour.  If artificial per-block quotas
are imposed, max-flow gives an exact Hall criterion, but fractional rank
balance does not imply its cuts.

This failure is not merely formal.

1. A one-fixed-coordinate-pairing partial-block factor is a literal middle
   near-factor of locally geodesic blocks, yet a pair-type Hall cut forces
   `Omega(W)` missing shadows at one depth `q=c sqrt(m)`.
2. Averaging all coordinate-permutation translates of this bad factor gives
   exact rank-balanced fractional degrees at every rank.  Every integral
   factor in the averaging support remains bad by the same amount.  Thus an
   orbit average of literal middle near-factors, even after the standard
   normalization to exact fractional degree one, does not imply Stage B.
3. The physical block-incidence matrix already contains the unsigned
   triangle matrix of determinant two at depth one.  The shadow conflicts at
   successive depths cross in both directions, so there is no laminar
   family to which ordinary network-flow integrality applies.

The exact additional datum is a simultaneous collision/lower-tail bound,
equivalently the summed missing-shadow bound itself.  In a quota
formulation, the exact additional datum is the full family of Hall cuts.

## 1. Exact partial-block ledger

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{1.1}
\]

Let `R=2 ell`, and let `F` be a family of vertex-disjoint cyclic middle
blocks

\[
 B=(X_{B,t}:t\in\mathbb Z/R\mathbb Z),
 \qquad X_{B,t}\in\binom{[2m]}m.
\tag{1.2}
\]

Assume that every cyclic window of at most `H` transitions is a Johnson
geodesic.  For `1<=q<=H` define

\[
 L_{B,t,q}=\bigcap_{j=0}^{q}X_{B,t+j},\qquad
 U_{B,t,q}=\bigcup_{j=0}^{q}X_{B,t+j}.
\tag{1.3}
\]

Then `L_(B,t,q)` has rank `m-q` and `U_(B,t,q)` has rank `m+q`.  For the
standard partial pair-flip blocks the `R` lower colours, and separately the
`R` upper colours, are distinct at each fixed depth.  The deficit identity
below does not require this additional within-block injectivity.  Write

\[
 T=R|\mathcal F|,\qquad u=W-T
\tag{1.4}
\]

for the number of covered and uncovered middle sets.  For a target `S` at
depth `q` and sign `sigma`, let `n_q^sigma(S)` be its number of physical
occurrences among the selected blocks.  Put

\[
 \begin{aligned}
 M_q^\sigma
   &=|\{S:n_q^\sigma(S)=0\}|,\\
 C_q^\sigma
   &=\sum_S(n_q^\sigma(S)-1)_+.
 \end{aligned}
\tag{1.5}
\]

There are exactly `T` occurrences at every depth and sign.  Therefore the
following identity is exact:

\[
 \boxed{M_q^\sigma=N_q-T+C_q^\sigma.}
\tag{1.6}
\]

Thus Stage B is precisely a demand that the collision mass exceed its
unavoidable baseline `T-N_q` by only a summably negligible amount.  First
moments do not control the right side of (1.6).

## 2. The sharp self-contained sufficient theorem

The following is the strongest safe version of the partial-block reduction.
It deliberately states the physical support condition rather than a
fractional surrogate.

### Theorem 2.1 (partial-path constant-one criterion)

Suppose there are integer functions `H=H(m)` and `ell=ell(m)` and a family
`F=F_m` of vertex-disjoint middle **paths**, obtained for example by cutting
the blocks in Section 1, such that every internal window of at most `H`
transitions is geodesic.  Let `p=|F|`, let `u` be the number of middle masks
outside the paths, and define `M_q^sigma` from the actual internal path
windows.  Assume

\[
 H\longrightarrow\infty,\qquad
 H=o(\ell),\qquad \ell=o(m),
\tag{2.1}
\]

and

\[
 Hp=o(W),
\qquad
 \sum_{q=1}^{H}\sum_{\sigma\in\{-,+\}}M_q^\sigma=o(W).
\tag{2.2}
\]

Assume also that all ranks outside the band `[m-H,m+H]` have a literal OR
word of length `o(W)`.  Then

\[
 \nu(2m)\le W+o(W).
\tag{2.3}
\]

More quantitatively, endpoint-capped erosion of the middle paths gives

\[
 \nu(2m)
 \le
 W+Hp
 +\sum_{q=1}^{H}\sum_\sigma M_q^\sigma
 +L_{\rm tail},
\tag{2.4}
\]

where `L_tail` is the exterior-rank word length.

#### Proof

An `H`-geodesic middle path with `v` vertices has no internal coordinate
one-run of length at most `H`.  The endpoint-capped erosion identity therefore
turns it into a literal OR word of length exactly `v+H`, exposing every
internal lower intersection and upper union through depth `H`.  Summing over
the `p` paths costs `T+Hp`.  Append each of the `u=W-T` omitted middle masks
once, append each missing band mask once, and append the exterior-rank word.
This gives (2.4).  In particular, the middle leave costs `u` but cancels
exactly against the missing `u` terms in `T=W-u`; it does **not** require the
stronger condition `Hu=o(W)`.  Any shadow damage caused by the leave is
already present in the actual `M_q^sigma`.  `square`

For `R=2ell` blocks one has `p<=W/(2ell)`, so the seam condition follows
from `H=o(ell)`.  If the deficits are first measured cyclically, there are
two safe conversions.

* Cutting one edge of every cycle loses at most `q p` depth-`q` windows per
  sign.  Hence the total additional deficit is at most `H(H+1)p`.
* Repeating the first `H` middle states before erosion preserves all cyclic
  windows and gives the sharper general bound

  \[
  \nu(2m)\le W+2Hp+
  \sum_{q,\sigma}M_{q,\mathrm{cyc}}^\sigma+L_{\rm tail}.
  \tag{2.5}
  \]

Thus cyclic support needs only `H/ell=o(1)` when the repeated-prefix option
is used; it does not need `H^2/ell=o(1)`.

For the known tail construction one may take

\[
 H=\sqrt{m\,\omega(m)},\qquad
 \omega(m)\longrightarrow\infty,qquad H=o(m^{2/3}),
\tag{2.6}
\]

because its exterior cost is

\[
 O\!\left((1+H^2/m)\binom{2m}{m-H}\right)=o(W).
\tag{2.7}
\]

If literal repairs have nonunit costs `a_(q,sigma)>=1`, the sufficient
shadow hypothesis is the weighted condition

\[
 \sum_{q,\sigma}a_{q,\sigma}M_q^\sigma=o(W).
\tag{2.8}
\]

For ordinary one-letter literalization the sharp weights are all one.
Fractional rank balance does not occur in Theorem 2.1 because it is not
needed once the physical deficits in (2.2) are known.

## 3. Why Stage B is not a post-processing flow

Fix `F`, `q`, and one sign.  Form the bipartite graph whose left vertices
are the `T` occurrence slots `(B,t)` and whose right vertices are the
`N_q` target colours.  A slot is adjacent only to its actual colour.
Consequently this graph is a disjoint union of stars centred at targets.

### Proposition 3.1 (flow degeneracy)

A flow assigning one physical witness to every target exists if and only if
`M_q^sigma=0`.  More generally, its maximum number of covered targets is
exactly `N_q-M_q^sigma`.

#### Proof

A target with no occurrence has degree zero and cannot receive flow.  If a
target has an occurrence, choose any one of its incident slots.  Slots of
different targets are automatically distinct because every slot has one
colour.  `square`

Thus, after Stage A has fixed the blocks, an augmenting-path algorithm merely
reports their existing support.  It performs no rounding of fractional rank
balance.

If one imposes artificial quotas `b_B` and asks for distinct colours for the
quota slots of every block, Hall's theorem gives the exact condition

\[
 \left|\bigcup_{B\in\mathcal A}C_q^\sigma(B)\right|
 \ge\sum_{B\in\mathcal A}b_B
 \qquad(\mathcal A\subseteq\mathcal F),
\tag{3.1}
\]

where `C_q^sigma(B)` is the block's colour set.  If

\[
 r_q^\sigma=N_q-\sum_Bb_B\ge0
\tag{3.2}
\]

and

\[
 \delta_q^\sigma=
 \max_{\mathcal A\subseteq\mathcal F}
 \left(\sum_{B\in\mathcal A}b_B-
 \left|\bigcup_{B\in\mathcal A}C_q^\sigma(B)\right|
 \right)_+,
\tag{3.3}
\]

then the exact optimal quota leave is

\[
 r_q^\sigma+\delta_q^\sigma.
\tag{3.4}
\]

These quota flows may be solved independently for all depths and both
signs: using one physical window as a witness does not consume it for any
other rank.  Thus there is no hidden cross-rank capacity after `F` is fixed.
All cross-rank coupling lies earlier, in choosing the same block family
`F` whose immutable colour sets make every deficiency small.

Hence a quota-flow proof needs

\[
 \sum_{q,\sigma}(r_q^\sigma+\delta_q^\sigma)=o(W).
\tag{3.5}
\]

The scalar rank-balance equations control `r`, but they say nothing about
the exponentially many cut deficiencies `delta`.

## 4. A literal symmetrized counterexample to fractional averaging

Fix one perfect matching `P` of the `2m` coordinates.  The explicit
orientation-cube tiling gives, for a power-of-two

\[
 m^{3/4}\le\ell<2m^{3/4},
\tag{4.1}
\]

a vertex-disjoint family of `2ell` pair-flip blocks covering all but
`o(W/H)` middle masks for every `H=O(sqrt(m) omega(1))` with
`H=o(ell)`.  Every relevant block window is locally geodesic.

For a lower rank-`m-q` target, let `f` be its number of full `P`-pairs.  It
then has `f+q` empty pairs.  The exact number of targets of this type is

\[
 T_{f,q}=
 \frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
\tag{4.2}
\]

Every `P`-compatible witnessing window must start in the corresponding
middle source type, of which there are only

\[
 V_f=
 \frac{m!}{f!f!(m-2f)!}\,2^{m-2f}.
\tag{4.3}
\]

One source start can cover at most one target of this type.  Therefore the
type family is an exact Hall cut and gives

\[
 \boxed{M_q^-\ge\sum_f(T_{f,q}-V_f)_+.}
\tag{4.4}
\]

Complementation gives the same upper bound.  At

\[
 q=\lfloor c\sqrt m\rfloor
\tag{4.5}
\]

for a sufficiently large absolute constant `c`, the central type range has
positive target mass and satisfies `V_f/T_(f,q)<1/2`.  Since

\[
 N_q/W=e^{-c^2+o(1)},
\tag{4.6}
\]

there is an absolute `eta>0` such that every such fixed-pair block factor
has

\[
 M_q^-,M_q^+\ge\eta W.
\tag{4.7}
\]

This is a genuine positive-density physical obstruction, not an abstract
incidence-cycle example.

Now let `g` be uniform in `S_(2m)` and translate the whole bad factor to
`gF`.  All translated factors remain literal, middle-disjoint, locally
geodesic, and have the same missing counts (4.7).  On the other hand,
transitivity gives, for every middle set `X` and every depth-`q` target `S`,

\[
 \mathbb E_g\mathbf1_{X\in gF}=T/W,
 \qquad
 \mathbb E_g n_{gF,q}^\sigma(S)=T/N_q.
\tag{4.8}
\]

Scale the orbit average by `W/T`.  To keep the decoration nested, give a
block certification type `d in {0,...,H}` with the standard weights

\[
 p_0=1-\rho_1,\qquad
 p_d=\rho_d-\rho_{d+1}\ (1\le d<H),\qquad
 p_H=\rho_H,
\tag{4.9}
\]

and let a type-`d` block carry all shadows through depth `d`.  Since
`sum_(d>=q)p_d=rho_q`, every middle vertex and every shadow target has
weighted degree exactly one.  Thus this is the exact **typed**
rank-balanced fractional solution, not merely independent slot thinning.

Nevertheless every integral factor in the averaging support has the
positive-density defect (4.7).  Therefore:

### Theorem 4.1 (fractional balance does not imply Stage B)

Exact fractional rank balance, even when obtained by averaging literal
locally geodesic middle near-factors, does not imply that one factor in the
averaging support has `o(W)` shadow deficit.  No deterministic conditional-
expectation argument using only those first moments can prove Stage B.

The theorem does not rule out mixing individual blocks from different
translates.  It proves that such mixing is a new integral packing theorem,
not a consequence of the orbit average.

## 5. The physical constraint matrix is not a flow matrix

The failure of total unimodularity already occurs in one depth-one collar.
Fix an `(m+1)`-set `U` and three distinct elements `i,j,k in U`.  Put

\[
 A_i=U\setminus\{i\},\qquad
 A_j=U\setminus\{j\},\qquad
 A_k=U\setminus\{k\}.
\tag{5.1}
\]

The three Johnson edges

\[
 A_iA_j,\qquad A_jA_k,\qquad A_kA_i
\tag{5.2}
\]

are literal depth-one geodesic windows.  Each extends to a partial
`2ell`-block for every `2<=ell<=m`: take its exchanged pair as the first
active pair, then choose `ell-1` further departure coordinates from the
common intersection and `ell-1` arrivals outside `U`.  A partial block is
an induced cycle, so the extension of one edge contains neither of the
other triangle facets.

Restrict the block-versus-middle incidence matrix to the three rows
`A_i,A_j,A_k` and these three block columns.  Up to row and column order it
is

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad \det=2.
\tag{5.3}
\]

The local equations giving residual demand one at all three rows have the
fractional solution `(1/2,1/2,1/2)` and no integral solution, since summing
them gives twice an integer equal to three.  Thus the literal block matrix
is not totally unimodular and is not the incidence matrix of an ordinary
network flow.  This does not prove global infeasibility; it identifies the
necessary odd-set/blossom layer which scalar rank balance omits.

The correlation is stronger after shadows are included.  Choosing one
edge in (5.2) simultaneously fixes its two middle endpoints, upper colour
`U`, and lower colour `U\setminus\{r,s\}`.  Separate flows for these four
marginals need not select the same edge.

## 6. Successive shadow conflicts are nonlaminar

Local geodesicity does not make the depth constraints laminar.  Both
crossing directions occur in literal two-transition fragments.

First let `L` have size `m-1`, choose distinct `x,y in L`, and choose fresh
symbols outside `L`.  The paths

\[
 L+a,\quad L+b,\quad (L-x)+b+c
\tag{6.1}
\]

and

\[
 L+d,\quad L+e,\quad (L-y)+e+f
\tag{6.2}
\]

have the same depth-one lower shadow `L`, but their depth-two lower shadows
are `L-x` and `L-y`.

Conversely, let `K` have size `m-2` and choose fresh symbols.  The paths

\[
 K+a+b,\quad K+b+c,\quad K+c+d
\tag{6.3}
\]

and

\[
 K+e+f,\quad K+f+g,\quad K+g+h
\tag{6.4}
\]

have distinct depth-one lower shadows `K+b` and `K+f`, but the same
depth-two lower shadow `K`.  All four fragments are geodesic, and with
enough unused coordinates they extend to partial pair-flip blocks.

Hence the equivalence relation "has the same depth-`q` shadow" neither
refines nor coarsens its depth-`q+1` counterpart.  The lower and upper
relations cross similarly: two edges may have the same intersection and
different unions, or the same union and different intersections.  This
rules out an argument whose claimed flow integrality comes merely from
laminar nesting of the depth-conflict classes.  It does not rule out some
new Boolean-specific polymatroid representation.  The evident coverage
objective is submodular, but maximizing it subject to middle-block packing
is a set-packing/maximum-coverage integer problem, not by itself a min-cost
flow.

## 7. The sharp missing hypotheses

There are three equivalent safe ways to state what a positive Stage B proof
must add.

### 7.1 Physical support form

Directly prove

\[
 \sum_{q=1}^{H}\sum_\sigma M_q^\sigma=o(W).
\tag{7.1}
\]

By Theorem 2.1 this is exactly what the OR construction uses.

### 7.2 Collision form

Using (1.6), prove

\[
 \sum_{q=1}^{H}\sum_\sigma
 \bigl(C_q^\sigma-(T-N_q)\bigr)=o(W).
\tag{7.2}
\]

This is the sharp lower-tail strengthening of fractional rank balance.  It
requires almost-minimal collision at shallow depths; an ordinary Poisson or
independent selection has a constant-density defect there.

If a distribution on integral middle factors is constructed, the expected
version of (7.2) is sufficient by averaging.  First moments
`E n(S)=T/N_q` are not sufficient, as Theorem 4.1 shows.

### 7.3 Quota-Hall form

For a stronger quota resolution, prove (3.5), namely every block-family Hall
cut up to total `o(W)` deficiency.  Once those cuts are proved, deterministic
max-flow does finish the assignment.  The flow is the final clerical step;
the Hall inequalities are the missing theorem.

## 8. Audited boundary

Proved:

* the exact deficit identity (1.6);
* the quantitative constant-one reduction (2.4);
* degeneration of post-factor shadow flow to support counting;
* the exact quota-Hall deficiency (3.3)--(3.5);
* a physical fixed-pair Hall obstruction of size `eta W`;
* exact fractional rank balance obtained by symmetrizing those same bad
  literal factors;
* a determinant-two physical triangle minor; and
* nonlaminar crossing of consecutive-depth shadow conflicts.

Not proved:

* that a reservoir mixing coordinate pairings has an integral block
  near-factor satisfying (7.1);
* that the corresponding non-TU odd-set constraints all have slack; or
* any deterministic rounding theorem beyond the exact conditional Hall
  statement.

Accordingly, Stage B cannot presently be claimed from fractional rank
balance and local geodesicity.  The sharp positive target is a
Boolean-specific near-rainbow block-packing theorem establishing (7.1) or
(7.2).  No separate literal-leave hypothesis is needed: the leave cancels
in the baseline `W`.  Under a full Gaussian window, the support condition
itself necessarily forces the sharper capacity rate
`u=o(Wm^(-1/3))`; the older `u=o(W/H)` condition is merely a convenient,
generally stronger sufficient rate.

## 9. Final audit addendum after theorem patches

The companion theorem reports were re-audited after their final patches.
The verdict is **valid**, with the following precise clarifications now
incorporated there.

1. The pair-energy inverse distinguishes the exact variational integer
   quantity `K_ex` from the explicit balanced lower-envelope quantity
   `K_Phi`.  The ordering

   \[
        M\le N-K_{\rm ex}\le N-K_\Phi
   \]

   is correct.  This removes the former overstatement that the balanced
   envelope was an exact inverse for every prescribed integer energy.

2. The robust-flow capacity `ceil(R/a)` is asymptotically equal to the
   forced average load only when `a->infinity` and `a=o(R)`; the latter
   condition is needed to make the additive ceiling negligible.  The exact
   robust Hall theorem itself needs neither asymptotic condition.

3. The component-overlay theorem was checked independently.  Its exact
   product missing formula, Jensen lower bound, two-layer discrete bound,
   and singleton-leave seam ledger are all valid.  In particular, adjoining
   singleton leaves preserves a partition of the whole middle layer, and
   the identity `R b+(W-R b)=W` preserves the exact baseline cancellation.

4. The Gaussian forced-capacity constant is exactly `4/3` after summing the
   two signs.  The uniform rate

   \[
   O\!\left(W\delta+W\sqrt m\,\delta^{3/2}\right)
   \]

   and the `m^(-1/3)` capacity threshold are correct.

No further correction was found in the endpoint-capped erosion identities,
the collar constants, the literal one-copy leave repair, the max-flow cuts,
or the final implication scopes.
