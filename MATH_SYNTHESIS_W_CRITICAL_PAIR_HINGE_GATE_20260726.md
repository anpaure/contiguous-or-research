# Constant one after the July 26 growing-port wave: the critical-pair hinge gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The current July 26 theorems do **not** assemble into a proof of MWB or
coefficient one.

They do isolate one nonvacuous surviving construction theorem. The first
potentially sufficient local scale is

\[
                         r=\Theta(\sqrt m).
\tag{0.1}
\]

At this scale one must construct two genuinely unrelated exact rooted
`D_r`-port factors, lift their full ownership overlay through the first
size-`r` fringe of the global Catalan factor, and prove a directed
balanced-hinge statement for one common all-depth component law. The law
must be rounded with a target-specific fluctuation bound computed from the
complete physical carrier and collar histograms.

The exact sufficient statement is formulated below as
`CRH_A` (critical root-scale hinge rounding). It is strictly more
structured than MWB: it demands a particular two-seed critical-scale
component cube, a common fractional law on that cube, and a quantitative
rounding certificate. It is not the empty-core completion statement which
can be satisfied by simply restating the desired overload bound.

The following implication is proved here:

\[
             \boxed{\mathrm{CRH}_A\text{ for every fixed }A
                    \Longrightarrow \mathrm{MWB}
                    \Longrightarrow \nu(k)=(1+o(1))W(k).}
\tag{0.2}
\]

No current construction proves `CRH_A`. The exact positive boundary is:

* full-overlay component choices are integral and port-legal;
* critical-scale first-fringe supply is asymptotically complete;
* the balanced-hinge dual and an exact zero-margin rounding inequality are
  available;
* no critical pair with directed low hinge and small targetwise rounding
  remainder has been constructed.

## 1. Global notation and the exact two-seed cube

Put

\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 B={W\over n}=\operatorname {Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil,
\tag{1.1}
\]

and, for `1<=q<=H_A`,

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor{W\over N_q}\right\rfloor .
\tag{1.2}
\]

For fixed `A`,

\[
                         1\le c_q\le C_A,
 \qquad
 \sum_{q\le H_A}{1\over c_q}=\Theta_A(\sqrt m).
\tag{1.3}
\]

A balanced quota at depth `q` is a vector

\[
 \beta_q(S)\in\{c_q,c_q+1\},\qquad
                         \sum_S\beta_q(S)=W.
\tag{1.4}
\]

Let `F^0,F^1` be two exact global rooted factors obtained by lifting two
exact rooted `D_r`-port factors through common literal contexts. Their
**full port-closed ownership overlay** uses every middle state and every
adjacent-union colour. Let `mathcal K` be its components. The common root
port edge proves that the two shores of a component have the same root
set. Consequently every vector

\[
                         \varepsilon\in\{0,1\}^{\mathcal K}
\tag{1.5}
\]

selecting one complete shore of every component gives one integral exact
rooted factor `F^epsilon`. This conclusion uses the full `X/Y` overlay,
not an `X`-only owner graph.

For every component `K`, depth `q`, and physical target `S`, let

\[
 u_{K,q}(S),\qquad v_{K,q}(S)
\tag{1.6}
\]

be its two complete occurrence histograms. They are taken **after** every
row/start-resolved carrier push-forward and include every crossing collar.
Let `ell_q` be the histogram of any rows fixed outside the displayed
components. Thus

\[
 \mu_q^\varepsilon
 =\ell_q+\sum_K\bigl((1-\varepsilon_K)u_{K,q}
                         +\varepsilon_Kv_{K,q}\bigr).
\tag{1.7}
\]

The same `epsilon_K` occurs at every depth.

## 2. An exact zero-margin component-rounding theorem

Let `mathbb P` be any probability law on the exact component children
(1.5). Put

\[
 t_K=\mathbb E\varepsilon_K,
\tag{2.1}
\]

and define the mean physical histogram

\[
 \overline\mu_q
 =\ell_q+\sum_K\bigl((1-t_K)u_{K,q}+t_Kv_{K,q}\bigr).
\tag{2.2}
\]

No independence is assumed. Define

\[
 \Phi_\beta(\mathbb P)
 =\sum_{q\le H_A}{1\over c_q}
      \sum_S(\overline\mu_q(S)-\beta_q(S))_+,
\tag{2.3}
\]

and the target-specific fluctuation remainder

\[
 \mathcal R_\beta(\mathbb P)
 ={1\over2}\sum_{q\le H_A}{1\over c_q}
       \sum_S\sqrt{\operatorname {Var}_{\mathbb P}
                         (\mu_q^\varepsilon(S))}.
\tag{2.4}
\]

### Theorem 2.1 (zero-margin hinge rounding)

Some integral exact child in the support of `mathbb P` satisfies

\[
 \boxed{
 \sum_{q\le H_A}{1\over c_q}\sum_S
       (\mu_q^\varepsilon(S)-\beta_q(S))_+
 \le \Phi_\beta(\mathbb P)+\mathcal R_\beta(\mathbb P).}
\tag{2.5}
\]

#### Proof

Fix `q,S` and put

\[
 a=\overline\mu_q(S)-\beta_q(S),\qquad
 Y=\mu_q^\varepsilon(S)-\overline\mu_q(S).
\]

Then `E Y=0`. The positive part is subadditive, so

\[
 (a+Y)_+\le a_++Y_+.
\tag{2.6}
\]

For a mean-zero random variable,

\[
 \mathbb EY_+={1\over2}\mathbb E|Y|
       \le {1\over2}\sqrt{\mathbb EY^2}.
\tag{2.7}
\]

Taking expectations in (2.6), summing with weights `1/c_q`, and using
(2.3)--(2.4) gives

\[
 \mathbb E\sum_{q,S}{1\over c_q}
       (\mu_q^\varepsilon(S)-\beta_q(S))_+
 \le\Phi_\beta(\mathbb P)+\mathcal R_\beta(\mathbb P).
\]

At least one support point is no larger than the expectation. Every support
point is an integral exact factor by the full-overlay component theorem.
\(\square\)

This theorem is deliberately a zero-margin statement. A balanced quota
has the same total mass as the factor, so a fractional mean cannot lie a
fixed positive distance below every quota coordinate. The proportional
slack inequality used for cap `2m+1` is therefore not a substitute for
(2.5) at the bounded MWB floors `c_q=O_A(1)`.

For independent Bernoulli component choices, (2.4) becomes

\[
 \mathcal R_\beta
 ={1\over2}\sum_{q,S}{1\over c_q}
 \sqrt{\sum_Kt_K(1-t_K)
        (v_{K,q}(S)-u_{K,q}(S))^2}.
\tag{2.8}
\]

A correlated law may reduce the variance in (2.4). Any such covariance
claim must be proved target by target; standard unsigned negative
dependence is neither assumed nor needed by Theorem 2.1.

## 3. The exact fractional hinge dual

The mean (2.2) depends only on the marginals `t_K`. Put

\[
 \Phi_\beta^*
 =\min_{0\le t_K\le1}
 \sum_{q,S}{1\over c_q}
 \left(\ell_q(S)+\sum_K[(1-t_K)u_{K,q}(S)
                 +t_Kv_{K,q}(S)]-\beta_q(S)\right)_+.
\tag{3.1}
\]

### Theorem 3.1 (protected-mass dual at balanced floors)

One has the exact identity

\[
\boxed{
\begin{aligned}
 \Phi_\beta^*
 =\max_{0\le z_q(S)\le1/c_q}\Bigg\{&
 \sum_{q,S}z_q(S)(\ell_q(S)-\beta_q(S))\\
 &+\sum_K\min\bigl(
       \langle z,u_K\rangle,
       \langle z,v_K\rangle\bigr)\Bigg\}.
\end{aligned}}
\tag{3.2}
\]

The inner product includes all depths and physical targets.

#### Proof

For every scalar `x`,

\[
 {1\over c_q}(x)_+
     =\max_{0\le z\le1/c_q}zx.
\tag{3.3}
\]

Substitute (3.3) into (3.1). The domains are finite-dimensional compact
convex sets and the resulting expression is bilinear in `t,z`, so minimax
interchanges minimum and maximum. For fixed `z`, each `t_K` independently
chooses the smaller of `inner(z,u_K)` and `inner(z,v_K)`. This gives
(3.2). \(\square\)

Thus the directed part of the missing theorem has a precise form: every
protected-mass dual vector `z` must lose almost all of its value against
one common two-shore choice. Point margins, component counts, and unsigned
variance do not imply (3.2) is small.

## 4. The single live lemma

### Critical root-scale hinge theorem `CRH_A` -- **UNPROVED**

For every fixed `A>0` and all sufficiently large `m`, construct the
following objects.

1. A scale
   \[
                    c_A\sqrt m\le r\le C_A'\sqrt m.
   \tag{4.1}
   \]
2. Two genuinely unrelated integral exact rooted `D_r`-port factors.
   Their complete first-size-`r` fringe lifts give two global exact factors
   and a full port-closed component cube as in Section 1.
3. Balanced quotas `beta_q`, `q<=H_A`, and one common law `mathbb P` on
   that exact component cube, such that
   \[
       \boxed{\Phi_\beta(\mathbb P)
                    +\mathcal R_\beta(\mathbb P)=o_A(W).}
   \tag{4.2}
   \]
4. Every histogram in (4.2) is the complete physical row/start histogram,
   with all parent carriers, crossing collars, overlapping contexts, and
   unaffected background already included.

To make this a genuinely new construction rather than a disguised endpoint
witness, the local pair must additionally pass the two known necessary bulk
tests:

* its active row-word change uses `Theta(r)` carrier positions on the
  positive-density part meant to repair the defect; and
* if the cube is built from the native MSW factor, its second seed has row
  distance at least
  \[
   \left({107897\over19784704}-o(1)\right)\operatorname {Cat}_r
  \tag{4.3}
  \]
  from the native invariant packet basin.

The last two clauses are not used in the formal implication below. They
exclude constructions already proved incapable of satisfying (4.2).

### Theorem 4.1 (`CRH_A` implies fixed-window MWB)

If `CRH_A` holds, there is one exact factor `F_(A,m)` such that

\[
 \sum_{q\le H_A}{O_q(F_{A,m})\over c_q}=o_A(W).
\tag{4.4}
\]

#### Proof

Apply Theorem 2.1 and choose the resulting exact child. For each depth,
the displayed balanced quota is an admissible competitor in the definition
of `O_q`. Hence

\[
 O_q(F_{A,m})
 \le\sum_S(\mu_q^{F_{A,m}}(S)-\beta_q(S))_+.
\tag{4.5}
\]

Sum (4.5) with weights `1/c_q` and use (4.2). \(\square\)

This is the single strongest live lemma after the July 26 audit. It is
not ordinary MWB phrased with new names: it requires a critical-scale,
unrelated, full-overlay two-seed realization and separately checkable
fractional and fluctuation certificates.

## 5. Completion of the implication to coefficient one

Assume `CRH_A` for every fixed positive integer `A`. Choose thresholds
`T_j` so that for `m>=T_j` the witness at `A=j` has weighted overload at
most `W/j`, and enlarge them so that `T_j>=j^8`. Put

\[
 a(m)=\max\{j:T_j\le m\},\qquad
 H_m=\lceil a(m)\sqrt m\rceil.
\tag{5.1}
\]

Then `a(m)->infinity`, `a(m)<=m^(1/8)`, and

\[
 H_m=o(m),\qquad {H_m\over\sqrt m}\longrightarrow\infty,
\tag{5.2}
\]

while one exact factor `F_m` satisfies

\[
                  \sum_{q\le H_m}{O_q(F_m)\over c_q}=o(W).
\tag{5.3}
\]

If `M_q(F_m)` is the number of missing depth-`q` lower targets, equality of
the load and quota masses gives

\[
                         M_q(F_m)\le {O_q(F_m)\over c_q}.
\tag{5.4}
\]

The literal central wreath word has length at most

\[
 W+{2H_m+1\over2m+1}W+2\sum_{q\le H_m}M_q(F_m).
\tag{5.5}
\]

The second term is `o(W)` by `H_m=o(m)`, and the third is `o(W)` by
(5.3)--(5.4). The audited product-SCD word covers both outer tails in
`o(W)` letters because `H_m/sqrt(m)->infinity`. Therefore

\[
                         \nu(2m+1)\le W+o(W).
\tag{5.6}
\]

The standard one-coordinate lift gives the even dimensions, and the width
lower bound gives

\[
             \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{5.7}
\]

This chain is unlabelled. It proves no common nested owner resolution and
uses no converse from MWB to labelled synchronization.

## 6. Why the other apparent endpoints are not the missing lemma

### 6.1 The newly stated completion hypothesis is vacuous as a reduction

In `MATH_THEOREM_GROWING_PORT_PATH_COMPLETION_TO_MWB_20260726.md`, the
hypothesis called `GPC_A` permits its rooted core `mathcal M` to be empty.
Take

\[
                         \mathcal M=\varnothing,
 \qquad \mathcal C=F.
\]

Then the residual capacity is `s_q=beta_q`, and its spill condition is

\[
 \sum_{q\le H_A}{1\over c_q}\sum_S
       (\mu_q^F(S)-\beta_q(S))_+=o_A(W),
\tag{6.1}
\]

which is exactly the fixed-window overload assertion at the chosen quotas.
Thus the stated `GPC_A` is sufficient but is not a smaller remaining
lemma. The meaningful stronger corollary is a quota-safe completable core
whose arbitrary completion has

\[
                         o_A(B/\sqrt m)
\tag{6.2}
\]

rows, or a genuinely structured spill theorem for a larger completion.

The exact survival-packet theorem gives a fractional version of (6.2).
For an exact factor and balanced quotas, let `O_(q,S)` be the owner set and
require

\[
 \sum_{E\in P}x_E\ge1
 \quad\text{for every }P\subseteq O_{q,S},
 \quad |P|=\beta_q(S)+1.
\tag{6.3}
\]

On a fixed Gaussian window every packet has rank

\[
                         R_A\le2+\max_{q\le H_A}c_q=O_A(1).
\tag{6.4}
\]

The threshold set `{E:x_E>=1/R_A}` is an integral common deletion family
of size at most `R_A sum_E x_E`. Hence a cover of mass

\[
                         o_A(B/\sqrt m)
\tag{6.5}
\]

proves the quota-core statement. No present critical pair supplies this
cover.

### 6.2 PPR is a direct hole route, not an MWB implication

The earlier PPR/PCap statistic uses the translation-orbit cap `2m+1` and
can control actual holes, so it remains a sufficient route to coefficient
one. It does not imply fixed-window MWB, whose capacities are the bounded
numbers `c_q=O_A(1)`. A histogram may have no holes and no cap-`2m+1`
overload while having `Theta_A(W)` balanced overload. `CRH_A` avoids this
scope error by using the actual balanced quotas (1.4).

### 6.3 Small edit variance is terminal, not the bulk counterbias

For two growing factors, let

\[
 e_{q,P}={1\over2}\|z^1_{q,P}-z^0_{q,P}\|_1,
 \qquad
 \Omega_H=\sum_{q\le H}{1\over c_q},
\tag{6.6}
\]

and let `Xi_H` be the size-weighted edit moment from the sparse-component
variance theorem. Since every nonempty component has size at least one,

\[
 \sum_{q\le H}{1\over c_q}\sum_Pe_{q,P}
       \le B\Omega_H\Xi_H.
\tag{6.7}
\]

At `H=A sqrt(m)`, the condition `Xi_H=o(sqrt(m))` therefore gives only
`o(W)` total weighted half-`L^1` action. Balanced overload is
one-Lipschitz in this metric. Consequently a one-shot small-`Xi` pair
cannot change an `Omega(W)` overload into `o(W)`. The variance theorem is
a valid terminal or iterative rounding lemma once directed counterbias has
already been supplied; it is not that counterbias.

The antipodal cube identity independently shows that unsigned component
sizes, edit moments, absolute Gram entries, or spectra cannot orient a
descent: fair drifts average to zero over the cube. The directed term
`Phi_beta`, equivalently the dual (3.2), is indispensable.

## 7. Audit against every current no-go

### 7.1 Exact path-factor interface

A local rooted factor is a vertex partition of the middle-levels inclusion
graph into paths

\[
 P=X_0\subset Y_0\supset\cdots\subset Y_{r-1}
       \supset X_r=[2r]\setminus P.
\tag{7.1}
\]

Equivalently it is an integral degree factor satisfying every labelled
complement-pair cut. Ordinary `D_r`-transversality, separate entrance and
exit matchings, or a degree factor alone are insufficient. An explicit
rank-three degree factor has wrong three-cycle monodromy, and the clean
rank-four path matrix has a determinant-two minor. `CRH_A` begins with two
already exact factors, so it assumes none of these false implications.

### 7.2 First-edge balance is automatic but not completion

Every completed rooted factor has

\[
 h_j=|\{P:b_1(P)=j\}|\le C_{r-1},\qquad
 h_{2r}=C_{r-1},\qquad h_1=0.
\tag{7.2}
\]

Thus coordinatewise first-edge balance at the first Catalan crossing is
not the missing theorem. Literal floor/ceiling balance over all `2r`
coordinates is actually impossible for `r>=3`, because deletion coordinate
`1` and insertion coordinate `2r` both have forced load `C_(r-1)`.

Even a clean optimally spread rank-three prefix fails a singleton residual
Hall cut by exactly one. Therefore the critical factors must be built with
residual Hall and labelled monodromy, not by rounding first-edge labels.

### 7.3 Four-cycles, six/eight-cycles, and twists

The middle-levels inclusion graph is `C_4`-free, so interior two-edge
splicing is nonexistent. Same-phase alternating `C_6` switches are
three-strand routers; clean `C_8` switches are odd four-strand routers;
folded `C_6` switches can be transpositions. A switch-stable connected
`C_6` atlas plus one odd router would correct arbitrary endpoint monodromy
while freezing protected prefixes. No growing positive-density atlas is
proved.

Nonidentity twisted packets are impossible in an ordinary fixed-exterior
\(r\)-step slab: for endpoints \(O\cup P\) and
\(O\cup(J\setminus\tau P)\), the Johnson distance is

\[
                         |P\cap\tau(P)|<r.
\]

Serial inverse or finite-order repetition cannot repair this, because
every contiguous subpath of a geodesic is geodesic. A twist remains a
possible local mechanism only after an exterior-moving packet is
constructed with

\[
 |O_L\setminus O_R|=|P\setminus\tau(P)|
\]

row by row and all crossing collars are rebuilt. Ordinary reversal also
reverses the antisymmetric carrier sign; complement-reversal preserves it
only under an additional lower-rainbow theorem. Thus no present twisted or
mirror construction supplies the critical pair.

### 7.4 Bounded seeds and separated growing packets

The fixed `D_4/H_4` library is exact but factor-coupled. Its full canonical
six-open hinge has maximum relief zero, including reflected reversal. The
`D_5` private-anchor lift has genuine nonzero parent action, but fixed
deployment covers only `7/128+o(1)` per boundary; even its maximal
row-disjoint two-boundary bank has limiting changed-row fraction

\[
                         {1743\over16384}.
\tag{7.3}
\]

Distinct exterior tags are not sufficient for disjoint physical cells;
the tags must be recoverable, or the push-forward images disjoint.

For separated literal size-`s` parent packets with `2s<=r`, the exact
maximum row-disjoint bank is

\[
                         N_{r,s}=2C_{r-s}-C_sC_{r-2s},
\tag{7.4}
\]

and

\[
 (2s+1){C_sN_{r,s}\over C_r}=O(s^{-1/2}).
\tag{7.5}
\]

Thus every `s->infinity` separated-boundary bank is occurrence-insufficient
even with perfect signs. This does not cover the overlapping regime
`s>r/2`, but it closes the literal separated amplification of a growing
seed.

### 7.5 The critical-scale locality threshold

If two lifted seeds differ only by reordering a common carrier block of
`b` positions, every component child satisfies

\[
 \sum_{q\le H}{1\over2}
       \|\mu_q^{\rm child}-\mu_q^{0}\|_1
 \le {2bH\over2m+1}W.
\tag{7.6}
\]

Therefore `bH=o(m)` is statewise incapable of changing an `Omega(W)`
defect. At `H=Theta(sqrt(m))`, every active block
`b=o(sqrt(m))` is closed. This includes a bounded active subhole hidden
inside a growing spectator carrier. Clause (4.1) and the `Theta(r)` active
word requirement place `CRH_A` exactly at the first scale not excluded by
(7.6).

### 7.6 Why critical supply itself is not the obstruction

The first size-`r` fringe classes cover all but a proportion

\[
 O\left(m^{3/2}\exp\left[-c{m\over r^{3/2}}\right]\right)
\tag{7.7}
\]

of the Catalan roots. For `r=Theta(sqrt(m))` this is `o(1)`. A local
full-overlay component lifts to an independent global component of the
same size. Thus critical-scale row supply is available; the missing facts
are a genuinely active local pair and the directed physical hinge.

There is concrete but subcritical evidence. The suspended pentagon gives
`C_(r-4)` independent five-row components, changes complete shadow and
coordinate-orbit mass, and has size-biased component moment tending to

\[
                         {69\over64}.
\tag{7.8}
\]

Its active carrier has only nine positions, so (7.6) makes every Gaussian
deployment `o(W)` in action. It proves that unrelatedness and fragmentation
are possible, not that `CRH_A` holds.

### 7.7 Operadic skeletons and coordinate components

The growing Catalan skeleton hypergraph has average degree
`~2^t/sqrt(pi t)`, but exceptional codegree `C_(t-2)` and literal
common-port incidence `O(C_s/t^(3/2))=o(C_s)`. It cannot supply the
critical pair through the proved shape-respecting suspension.

The first-two-cut Chung--Feller rectangles are exact but act on only

\[
                         2C_{s-2}=(1/8+o(1))C_s
\tag{7.9}
\]

roots. Coordinate-component routing is nonlaminar, and a transitive phase
comparison makes the full overlay connected rather than well fragmented.
`CRH_A` therefore asks for two direct unrelated factors, not an iteration
of the closed coordinate or operadic libraries.

### 7.8 Positive-radius native packet obstruction

Every child of a two-seed cube lies in the row ball determined by its two
endpoints. Around the native MSW cube, the invariant survival-packet bound
forces the extensive distance (4.3). Hence a tiny perturbation of MSW,
even one with vanishing component variance, cannot prove the theorem.
`CRH_A` records this necessary extensive-distance test explicitly.

### 7.9 Integrality, simultaneous depths, and literal realization

Every outcome in Theorem 2.1 is one exact factor because complete
port-closed component shores are selected. The same component vector is
used at every depth. Equations (1.6)--(1.7) are evaluated after literal
cyclic reconstruction and all carrier maps. Therefore the theorem does not
use fractional factors, separate depthwise signs, labelled common-owner
synchronization, or nonliteral shadow vectors.

## 8. Shortest viable proof route

The shortest route left by the audit is the following.

1. **Construct one critical unrelated pair.** Work directly at
   `r=Theta(sqrt(m))` in the middle-levels inclusion graph. Build both
   exact `D_r`-port factors using residual Hall plus labelled monodromy.
   A growing switch-stable `C_6/C_8` braid, or an exterior-moving twisted
   atlas satisfying the exact rowwise distance budget and full collars, is
   a possible mechanism. Uniform first-edge matching, fixed-exterior
   twisting, and pure mirror completion are closed.
2. **Make the pair extensive and root-active.** A positive density of
   root-matched rows must change `Theta(r)` carrier positions. The full
   `X/Y` overlay must remain fragmented; an `X`-only component theorem is
   insufficient. Check the native packet-distance bound before doing any
   cap calculation.
3. **Lift through first fringes.** The exact first-fringe partition then
   supplies `1-o(1)` global row coverage and transports every local
   port-closed component integrally.
4. **Prove the directed fractional hinge.** Use the exact dual (3.2).
   This is the decisive sign theorem: defeat every protected-mass vector
   `z` using one common all-depth marginal choice. First-edge or orbit-mass
   dispersion is not enough.
5. **Prove target-specific rounding.** Construct a product or correlated
   law with the same marginals and show (2.4) is `o(W)`. Generic unsigned
   edit variance is too weak at zero quota margin; the covariance must be
   routed on the actual target fibres.
6. **Invoke no further conjecture.** Theorem 2.1 gives one integral exact
   child, Theorem 4.1 gives fixed-window MWB, and Section 5 gives the
   literal central word, SCD tails, and both parities.

Steps 4--5 are the one missing theorem `CRH_A`; Steps 1--3 specify the only
currently unclosed construction scale and geometry. No shorter current
route survives all of the audited no-go theorems.

### 8.1 Ballot-cycle update

The later ballot theorem in Section 3.6 of
`MATH_THEOREM_TWISTED_PORT_MONODROMY_COMPOSITION_20260726.md` gives an
abstract supply statement. Every `D_r` port factor has at least

\[
 {r-1\over(r+1)(r+2)}C_r=(1/r+O(r^{-2}))C_r
\]

selected-edge-disjoint outgoing functional-cycle certificates. Under the
separately assumed local normalization `Theta(C_r/r^(3/2))`, this raw count
has a factor `Theta(sqrt(r))` of scalar slack.

The precise audit is in
`MATH_AUDIT_W_BALLOT_CYCLE_STRAND_CARRIER_EXTRACTION_20260726.md`.
The count does not guarantee a genuine full-factor circuit: a certificate
may use an old path-successor edge or repeat an old strand. More decisively,
even a clean nonidentity circuit cannot be installed in a fixed-exterior
`r`-step slab. The corrected narrow target is `EMCE_r`: extend a proved
clean bank to rowwise exterior-moving geodesic packets satisfying

\[
 |O_L\setminus O_R|=|P\setminus\tau(P)|,
\]

then prove joint switch stability, exact seams and collars, extensive
parent-visible action, and coherent full-carrier sign. Serial closure may
be used only after each constituent slab passes this local geodesic test.
The raw square-root ratio is not a universal demand calculation, and
`EMCE_r` does not remove the global balanced-hinge or target-specific
rounding obligations in Steps 4--5.

### 8.2 The all-adjacent-block conjugate pair

The explicit Lane N factor

\[
 G_r(P)=\eta_rF_r(\eta_rP),\qquad
 \eta_r=\prod_{i<r}(2i\ \ 2i+1),
\]

remains a literal identity-monodromy factor after the fixed-exterior twist
correction. It also differs from \(F_r\) in the first edge on exactly

\[
                         C_r-R_{r-1}
   =\left({8\over9}+o(1)\right)C_r
\]

root-matched rows. However its advertised \(1/9\) cap is only the
source-first-return-resolved maximum \(R_{r-1}\). After source labels are
forgotten, every exact component child has the forced raw endpoint load

\[
                         h(2r)=C_{r-1}\sim C_r/4.
\]

Moreover the common top/top core of size \(R_{r-1}\) survives in every
component child, so even perfect physical source separation cannot improve
the resolved \(1/9\) threshold.

The coordinate-automorphism classification

\[
 \operatorname{Aut}_{S_{2r}}({\cal D}_r)
   =\langle(2i\ \ 2i+1):1\le i<r\rangle
\]

shows that this is minimax over every fixed-port coordinate conjugate of
the canonical seed. It is not a minimax theorem over arbitrary exact
factors.

No theorem currently bounds the full \(X/Y\) component sizes for the
product conjugate. The single-transposition component hierarchies do not
compose to give that direct overlay. Nor is there a complete carrier/collar
mean-hinge or targetwise covariance estimate. The exact audit is in
MATH_AUDIT_W_ALL_ADJACENT_BLOCK_PAIR_CRH_20260726.md. Thus this explicit
pair narrows the construction search but does not satisfy
\(\mathrm{CRH}_A\).

The marked first-column obstruction by itself is only \(o(W)\) after
global critical-scale normalization. Therefore it does not rule out the
pair at coefficient scale; the unresolved full-profile component,
carrier-mean, and covariance calculations are genuinely decisive.

## 9. Exact proved/conditional boundary

### Proved

1. Full port-closed component shores give integral exact factors.
2. The zero-margin rounding inequality (2.5).
3. The balanced-floor protected-mass dual (3.2).
4. `CRH_A =>` fixed-window MWB with no hidden constants.
5. Fixed-window diagonalization, literal central-band repair, product-SCD
   tails, and parity lift.
6. The critical scale `r=Theta(sqrt(m))` is the first scale not excluded
   by carrier locality, and its first-fringe row reservoir is
   asymptotically complete.

### Unproved

1. Existence of the critical unrelated pair.
2. A growing positive-density monodromy-router atlas preserving the needed
   carrier direction.
3. The directed dual estimate `Phi_beta=o(W)` on that pair.
4. The common all-depth target-specific rounding estimate
   `mathcal R_beta=o(W)`.

Accordingly no MWB or coefficient-one theorem is claimed unconditionally.
The surviving gate is not a bounded-seed conveyor, an operadic matching,
first-edge balance, unsigned component expansion, or a renamed overload
statement. It is the critical root-scale directed hinge-and-rounding
theorem `CRH_A`.
