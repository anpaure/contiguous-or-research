# Catalan collars: exact protected-Ore mean, principal-star aperture, and the cut-entropy barrier

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional identities and reductions.  The note proves the
exact all-edge mass of the protected transition test, shows that an
isotropic Catalan collar law has a factor-`Theta(m^{-1/2})` fractional
margin against every protected-Ore cut, proves deterministic safety of all
one-coordinate principal stars, and gives an exact weighted-hypergeometric
tail theorem for thinning a collar bank.  It also proves that the presently
available generic connected-cut entropy bound cannot close the argument:
at collar-block resolution it loses a factor equal to the collar length,
while connected positive-defect cuts with `sigma(A)<6|A|` exist.  A
low-slack stability/container theorem or an edge-resolution collar MGF is
still required.  No protected factor extension is claimed.

## 0. Setting

Put

\[
 n=2m-1,\qquad
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}m,\qquad
 W=|\mathcal L|=|\mathcal U|.
\tag{0.1}
\]

Let `J_U=J(n,m)` be the Johnson graph on `mathcal U`.  Every edge
`e=UV` has the unique lower colour

\[
                         q(e)=U\cap V\in\mathcal L.             \tag{0.2}
\]

For `A subseteq mathcal L`, write

\[
 N=N(A)=\{U\in\mathcal U:\exists x\in A,\ x\subset U\},
 \qquad \delta(A)=|N(A)|-|A|.                                  \tag{0.3}
\]

The protected-Ore slack is

\[
 \sigma(A)=\sum_{U\in\mathcal U}\min\{2,a_U\}-2|A|,
 \qquad a_U=|\{x\in A:x\subset U\}|.                          \tag{0.4}
\]

Retain the clique-closure defect

\[
 \beta(A)=\sum_{U:2\le a_U\le m-1}(m-a_U).                    \tag{0.5}
\]

The frozen shadow identity is

\[
 \boxed{(m-1)\sigma(A)=(m-2)\delta(A)+\beta(A).}               \tag{0.6}
\]

Define the transition test requested here by

\[
 w_A(UV)=\mathbf 1_{\{U\cap V\notin A\}}
          \bigl(\mathbf 1_{\{U\in N(A)\}}
                +\mathbf 1_{\{V\in N(A)\}}\bigr).             \tag{0.7}
\]

If `P` is a family of palette-disjoint Johnson paths and every selected
Johnson edge is lifted through its lower colour, then

\[
 c_P(A)=\sum_{e\in P}w_A(e)                                   \tag{0.8}
\]

is exactly the protected crossing count from `N(A)` to
`mathcal L-A`.  The exact protected loss satisfies

\[
                         \lambda_P(A)\le c_P(A),                \tag{0.9}
\]

with the known one-neighbour rebates accounting for the difference.

Throughout, a collar has `ell` Johnson transitions, where
`ell=Theta(sqrt(m))`.  In the odd Catalan bank the number of collars is

\[
 C={W\over 2m-1}=\operatorname{Cat}_{m-1},
 \qquad b=C-1.                                                  \tag{0.10}
\]

## 1. Exact total transition mass

### Theorem 1.1 (Johnson transition identity)

For every lower cut `A subseteq mathcal L`,

\[
 \boxed{
 \sum_{e\in E(J_U)}w_A(e)=m(m-1)\delta(A).}
\tag{1.1}
\]

Since `J_U` has degree `m(m-1)` and

\[
                         |E(J_U)|={Wm(m-1)\over2},              \tag{1.2}
\]

a uniformly random Johnson edge satisfies

\[
 \boxed{\mathbb E w_A(e)={2\delta(A)\over W}.}                 \tag{1.3}
\]

#### Proof

The Johnson edges of lower colour `q in mathcal L` form the complete graph
on the `m` upper extensions of `q`.  If `q notin A`, summing the endpoint
indicators in (0.7) over that clique gives

\[
 (m-1)d_N(q),\qquad
 d_N(q)=|\{U\in N:q\subset U\}|,                               \tag{1.4}
\]

because every upper endpoint occurs in exactly `m-1` clique edges.  Thus

\[
 \sum_e w_A(e)=(m-1)e_{ML_m}(N,\mathcal L-A).                  \tag{1.5}
\]

Every incidence out of `A` ends in `N(A)`, so regularity of the
middle-levels graph gives

\[
 e_{ML_m}(N,\mathcal L-A)
 =m|N|-m|A|=m\delta(A).                                        \tag{1.6}
\]

Equations (1.5)--(1.6) prove (1.1), and division by (1.2) proves (1.3).
\(\square\)

### Corollary 1.2 (fractional Catalan margin)

Let `B` be a random `ell`-edge collar law for which every edge occurrence
is marginally uniform on `E(J_U)`.  Then

\[
 \mathbb E w_A(B)={2\ell\delta(A)\over W}.                     \tag{1.7}
\]

For `b` such collars (independence is not needed for this expectation),

\[
 \mu_A:=\mathbb E c_P(A)
 \le \vartheta_m\sigma(A),
 \qquad
 \vartheta_m={2b\ell(m-1)\over W(m-2)}.                        \tag{1.8}
\]

At Catalan scale,

\[
 \boxed{
 \vartheta_m
 <{2\ell(m-1)\over(2m-1)(m-2)}
 =\Theta(m^{-1/2}).}
\tag{1.9}
\]

#### Proof

Sum (1.3) over the `ell` edge occurrences and then over the `b` collars.
Equation (0.6) gives

\[
 \delta(A)\le {m-1\over m-2}\sigma(A),                         \tag{1.10}
\]

which proves (1.8).  Substitute (0.10) and `ell=Theta(sqrt(m))` to obtain
(1.9). \(\square\)

Thus there is no fractional protected-Ore obstruction: an isotropic collar
bank uses only an `O(m^{-1/2})` fraction of the available cut slack,
uniformly in the cut.

## 2. Global relabelling cannot create cut-thinness

The word *isotropic* in Corollary 1.2 must concern the construction law,
not a random global relabelling of one already chosen bank.

### Proposition 2.1 (orbit invariance no-go)

For every coordinate permutation `pi in S_n`,

\[
 w_{\pi A}(\pi e)=w_A(e),\qquad
 \sigma(\pi A)=\sigma(A).                                     \tag{2.1}
\]

Consequently

\[
 \boxed{
 \max_A\bigl(c_{\pi P}(A)-\sigma(A)\bigr)
 =\max_A\bigl(c_P(A)-\sigma(A)\bigr).}
\tag{2.2}
\]

In particular, applying one random coordinate permutation to a fixed
three-palette collar bank cannot improve its all-cut protected-Ore status.

#### Proof

Coordinate permutations preserve containment, intersection, Johnson
adjacency, upper shadows, and all cardinalities in (0.4).  This proves
(2.1).  The substitution `A=pi A'` is a bijection on all lower cuts and
gives (2.2). \(\square\)

This rules out the tempting but invalid inference

\[
 \text{uniform orbit mean for each fixed }A
 \quad\Longrightarrow\quad
 \text{one relabelled bank works for every }A.                  \tag{2.3}
\]

Independent or regenerating collar choices, or a deterministic cut-spread
construction, are genuinely necessary.

There is nevertheless an exact orbitwise sparsity consequence for every
fixed bank.

### Theorem 2.2 (orbit-average cut thinness)

Let `P` be any Johnson-edge bank with `E=|E(P)|`.  For every lower cut
`A`, averaging over its coordinate orbit gives

\[
 \boxed{
 {1\over n!}\sum_{\pi\in S_n}c_P(\pi A)
 ={2E\delta(A)\over W}
 \le \Theta_P\sigma(A),}
\tag{2.4}
\]

where

\[
                         \Theta_P={2E(m-1)\over W(m-2)}.         \tag{2.5}
\]

Consequently, in every coordinate-isomorphism orbit of cuts, the fraction
violating the sufficient inequality `c_P(A)<=sigma(A)` is strictly less
than `Theta_P`.  For the Catalan collar bank `E=b ell`,

\[
                         \Theta_P=\Theta(m^{-1/2}).              \tag{2.6}
\]

#### Proof

By (2.1),

\[
 c_P(\pi A)=\sum_{e\in P}w_A(\pi^{-1}e).                       \tag{2.7}
\]

The Johnson graph is edge-transitive, so `pi^{-1}e` is uniform on its edge
set.  Theorem 1.1 makes the expectation of each summand
`2delta(A)/W`, proving the equality in (2.4).  Equation (0.6) proves the
inequality.  Since `sigma` is constant on the orbit, Markov's inequality
gives the exceptional fraction. \(\square\)

Thus every bank is automatically cut-thin on a `1-O(m^{-1/2})` fraction
of **each** cut orbit.  The hard issue is eliminating the exceptional
representatives simultaneously; orbit averaging alone cannot do so by
Proposition 2.1.  Indeed the number of coordinate orbits of lower cuts is
at least

\[
                              {2^W\over n!},                     \tag{2.8}
\]

because every orbit has size at most `n!`.  Therefore even one exceptional
representative per orbit leaves a doubly exponential family.  A stability
theorem must bound the exceptional **orbit types**, not just their density
inside each orbit.

## 3. Exact thinning tail at collar-block resolution

Let `mathscr B={B_1,...,B_M}` be any deterministic family of collars, and
put

\[
 z_i(A)=\sum_{e\in B_i}w_A(e),\qquad
 C_{\mathscr B}(A)=\sum_{i=1}^M z_i(A).                         \tag{3.1}
\]

Always `0<=z_i(A)<=2ell`.  Choose exactly `b` collars uniformly without
replacement, put `p=b/M`, and let `P` denote their union.

### Theorem 3.1 (weighted exact-thinning bound)

For every cut `A` and every `y\ge pC_{\mathscr B}(A)`,

\[
 \boxed{
 \Pr\{c_P(A)\ge y\}
 \le
 \left({e\,pC_{\mathscr B}(A)\over y}\right)^{y/(2\ell)}.}
\tag{3.2}
\]

More generally, `2ell` in (3.2) may be replaced by any valid uniform
aperture bound `z_i(A)<=L_A`.

#### Proof

The indicators of an exact-size sample are negatively associated.  Hence,
for `theta>=0`,

\[
 \mathbb E\exp\!\left(\theta\sum_i z_iI_i\right)
 \le\prod_i(1-p+pe^{\theta z_i}).                              \tag{3.3}
\]

For `0<=z<=L`, convexity of the exponential gives

\[
 e^{\theta z}-1\le {z\over L}(e^{\theta L}-1).                 \tag{3.4}
\]

Using `1+x<=e^x` in (3.3),

\[
 \mathbb E e^{\theta c_P(A)}
 \le \exp\!\left({pC_{\mathscr B}(A)\over L}
                   (e^{\theta L}-1)\right).                    \tag{3.5}
\]

The exponential Markov inequality, optimized at
`e^{\theta L}=y/[pC_{\mathscr B}(A)]`, gives the Poisson tail

\[
 \exp\!\left[-{y\over L}\log{y\over pC_{\mathscr B}(A)}
              +{y-pC_{\mathscr B}(A)\over L}\right]
 \le\left({e\,pC_{\mathscr B}(A)\over y}\right)^{y/L}.        \tag{3.6}
\]

Take `L=2ell`, or the sharper cut-specific aperture. \(\square\)

### Corollary 3.2 (conditional isotropic-bank tail)

Suppose a large bank has the cut-energy domination

\[
 pC_{\mathscr B}(A)\le\vartheta\sigma(A)                       \tag{3.7}
\]

for every cut in a family `\mathcal A`, where `e\vartheta<1`.  Then

\[
 \boxed{
 \Pr\{c_P(A)>\sigma(A)\}
 \le(e\vartheta)^{\sigma(A)/L_A}.}
\tag{3.8}
\]

At the ideal isotropic value (1.9), the logarithmic reserve in (3.8) is

\[
 \log{1\over e\vartheta_m}={1\over2}\log m+O(1).              \tag{3.9}
\]

Theorem 3.1 is exact enough for a future stability/container proof.  It
also exposes precisely what the present prospective collar theorem does
not give: local owner/facet loads do not imply the global energy inequality
(3.7).

## 4. Principal-star aperture and an unconditional safe family

For `R subseteq[n]`, `|R|=j`, define the principal lower star

\[
 \mathcal A_R=\{x\in\mathcal L:R\subseteq x\}.                  \tag{4.1}
\]

Assume `1<=j<=m-2`.  Then

\[
 |\mathcal A_R|={n-j\choose m-1-j},\qquad
 |N(\mathcal A_R)|={n-j\choose m-j}=:N_j.                      \tag{4.2}
\]

Every owner in the shadow has `m-j>=2` selected facets, and therefore

\[
 \boxed{
 \delta(\mathcal A_R)={j\over m}N_j,
 \qquad
 \sigma(\mathcal A_R)={2j\over m}N_j.}
\tag{4.3}
\]

### Lemma 4.1 (star transition aperture)

For a Johnson edge `e=UV`,

\[
 w_{\mathcal A_R}(e)=1                                      \tag{4.4}
\]

exactly when, for one `z in R`, the shared lower colour contains
`R-{z}` but not `z`, and the exchange `U triangle V` uses `z`.  In all
other cases its weight is zero.

Consequently, if a generalized balanced geodesic collar exchanges every
coordinate on at most two of its Johnson transitions, then

\[
 \boxed{w_{\mathcal A_R}(B)\le\min\{2j,4\}.}                   \tag{4.5}
\]

#### Proof

If `q=U cap V` lies in `mathcal A_R`, the leading indicator in (0.7)
vanishes.  If `q` misses at least two elements of `R`, neither one-element
extension can contain `R`, so both endpoint indicators vanish.  If `q`
misses exactly `z in R`, precisely the endpoint obtained by adding `z`
belongs to the upper shadow.  This proves (4.4).  Charge such a transition
to `z`.  Summing the at-most-two exchange occurrences of every `z in R`
gives the `2j` bound.

For the constant bound, observe more directly that

\[
 w_{\mathcal A_R}(UV)
 =\left|\mathbf1_{\{R\subseteq U\}}
       -\mathbf1_{\{R\subseteq V\}}\right|.                    \tag{4.5a}
\]

Along the internal geodesic

\[
 M_t=Q\cup\{\lambda_{t+1},\ldots,\lambda_h\}
          \cup\{\rho_1,\ldots,\rho_t\},                       \tag{4.5b}
\]

the indices with `R subseteq M_t` form an interval: provided every other
member of `R` lies in `Q`, they are exactly the integers satisfying

\[
 \max\{i:\rho_i\in R\}\le t<
 \min\{i:\lambda_i\in R\};                                   \tag{4.5c}
\]

with the maximum of the empty set interpreted as `-infinity` and the
minimum as `+infinity`; otherwise the interval is empty.  A binary interval has total variation
at most two.  Adjoining the single left and right seam owners adds at most
one transition at each end.  Hence the whole collar has variation at most
four. \(\square\)

The balanced collars of the three-palette bank have the required
exchange-multiplicity property: every internal rail label is exchanged
once, each seam label is exchanged once, and only the first entering label
can occur on both the left seam and the first internal edge.

There is also an exact aggregate identity which makes the remaining
higher-order discrepancy explicit.

### Lemma 4.2 (rank-`j` principal-star mass)

For every Johnson edge `e` and `1<=j<=m-1`,

\[
 \boxed{
 \sum_{R\in\binom{[n]}j}w_{\mathcal A_R}(e)
 =2{m-1\choose j-1}.}
\tag{4.6}
\]

Consequently every `ell`-edge collar has total rank-`j` principal-star
mass `2ell binom(m-1,j-1)`, independently of its labels, and every collar
bank `P` satisfies

\[
 \boxed{
 \sum_{R\in\binom{[n]}j}c_P(\mathcal A_R)
 =2|E(P)|{m-1\choose j-1}.}
\tag{4.7}
\]

The corresponding slack sum is

\[
 \boxed{
 \sum_{R\in\binom{[n]}j}\sigma(\mathcal A_R)
 =2W{m-1\choose j-1}.}
\tag{4.8}
\]

Hence, deterministically for every bank,

\[
 {\sum_R c_P(\mathcal A_R)\over
   \sum_R\sigma(\mathcal A_R)}={|E(P)|\over W}
 ={b\ell\over W}=\Theta(m^{-1/2}).                \tag{4.9}
\]

#### Proof

Write `e=UV`, `q=U cap V`, and `U triangle V={a,b}`.  By Lemma 4.1, a
rank-`j` set charged at the `U` endpoint is uniquely

\[
                         R=\{a\}\cup T,
 \qquad T\in{q\choose j-1},                        \tag{4.10}
\]

and the sets charged at the `V` endpoint are obtained in the same way with
`b`.  The two families are disjoint because neither `a` nor `b` lies in
`q`.  This proves (4.6); summation proves (4.7).

Equation (4.8) follows from (4.3) and

\[
 {n\choose j}{n-j\choose m-j}=W{m\choose j},
 \qquad {j\over m}{m\choose j}={m-1\choose j-1}.    \tag{4.11}
\]

This proves (4.8)--(4.9). \(\square\)

Thus every bank has the correct **average** higher-order principal-star
charge.  The unresolved issue is its maximum charge over `R`; this is a
finite-coordinate discrepancy problem, not a missing scalar count.

### Corollary 4.3 (only a vanishing fraction of principal cuts can fail)

At every fixed rank `j`, the number of sets `R` for which the sufficient
cut-thinness inequality

\[
                         c_P(\mathcal A_R)>\sigma(\mathcal A_R)
\tag{4.12}
\]

holds is strictly smaller than

\[
 \boxed{
 {b\ell\over W}{n\choose j}=O(m^{-1/2}){n\choose j}.}
\tag{4.13}
\]

#### Proof

The slack in (4.3) depends only on `j`, so every failing `R` contributes
more than that common value to the left numerator of (4.9).  Markov's
inequality and (4.9) give (4.13). \(\square\)

This is an exact global sparsity statement for the unresolved principal
cuts.  It cannot be upgraded by a common coordinate relabelling, by
Proposition 2.1; the exceptional sets must be prevented or repaired during
co-selection.

### Corollary 4.3a (principal-upset thinning closes from isotropic energy)

Let `mathscr B` be a large collar bank and suppose that, for every nonempty
`R` of rank at most `m-1`, its exact `b`-collar thinning satisfies the
pre-thinning energy bound

\[
 pC_{\mathscr B}(\mathcal A_R)
 \le\vartheta\sigma(\mathcal A_R),
 \qquad \vartheta=O(m^{-1/2}).                                 \tag{4.13a}
\]

Then, for all sufficiently large `m`, some exact thinning satisfies

\[
                         c_P(\mathcal A_R)\le\sigma(\mathcal A_R)
 \qquad(1\le|R|\le m-1)                                       \tag{4.13b}
\]

simultaneously.

#### Proof

Lemma 4.1 gives aperture at most four.  Theorem 3.1 therefore bounds the
failure probability of one row by

\[
                         (e\vartheta)^{\sigma(\mathcal A_R)/4}. \tag{4.13c}
\]

For `|R|<=m-2`, (4.3) gives `sigma>=m-2` (the sharp middle-shadow bound
also gives this directly); for `|R|=m-1`, `A_R` is a singleton and its
slack is exactly `m-2`.  There are fewer than `2^n` choices of `R`.
Hence the total failure probability is at most

\[
 2^n(e\vartheta)^{(m-2)/4}=o(1),                              \tag{4.13d}
\]

because `\log(1/(e\vartheta))=(1/2)\log m+O(1)`. \(\square\)

Thus all principal optional cuts reduce to one concrete prospective-bank
condition, (4.13a).  The existing low-star theorem proves many of these
rows after thinning but not the short-rank transition-energy bound in full.

### Theorem 4.4 (one-coordinate stars are automatically safe)

Let `P` be **any palette-disjoint** family of
`b=C-1=\operatorname{Cat}_{m-1}-1` generalized balanced collars; no randomness or
star-spread hypothesis is needed.  For every coordinate `z`,

\[
 \boxed{
 c_P(\mathcal A_{\{z\}})\le2b
 <2C
 =\sigma(\mathcal A_{\{z\}}).}
\tag{4.14}
\]

Hence every one-coordinate principal-star cut passes the exact protected
Ore inequality.

#### Proof

Lemma 4.1 gives at most two units per collar.  By (4.3),

\[
 \sigma(\mathcal A_{\{z\}})
 ={2\over m}{n-1\choose m-1}
 ={2W\over2m-1}=2C.                                           \tag{4.15}
\]

Now use `b=C-1` and (0.9). \(\square\)

This closes the literal full principal-star cut without probability.  The
stronger residual cut `mathcal A_{\{z\}}-Z`, where the protected lower
colours are removed, is closed by the exact added-label identity in
`MATH_THEOREM_PROTECTED_FACTOR_TWO_MATCHING_COORDINATE_CUT_OBSTRUCTION_20260805.md`;
the same at-most-two exchange count supplies its sharp two-unit reserve.
For larger `j`, (4.5) remains a useful cut-specific aperture, but the
deterministic comparison need not hold; global spread is still needed.

### Remark 4.5 (why a global invariant is indispensable)

The same protected-factor obstruction theorem constructs
three-palette-disjoint path banks with both local exposure parameters
`o(m)` which nevertheless fail on a one-coordinate residual cut.  Thus
local owner-star and forced-facet loads cannot imply (6.1).  Balanced
geodesic collars avoid that example only because their added-label charge
in every coordinate is at most `2b`.  A successful theorem must retain a
global transition invariant of this kind at higher-order cuts.

The constant aperture persists for every bounded union of principal stars.

### Theorem 4.6 (multi-centre aperture)

Let

\[
                         A=\bigcup_{i=1}^g\mathcal A_{R_i}       \tag{4.19}
\]

be a union of `g` principal lower stars, with centres of arbitrary ranks at
most `m-1`.  Every generalized balanced collar satisfies

\[
                         \boxed{w_A(B)\le4g.}                    \tag{4.20}
\]

#### Proof

For an owner `U`, put `f_i(U)=1_{R_i subseteq U}`.  On one edge `UV`, if
`q=U cap V` belongs to `A`, then `w_A(UV)=0`.  Otherwise, every centre
contained in `U` is absent from `V` (if it were in both, it would lie in
`q`), and conversely.  Choose one centre witnessing each endpoint which
belongs to `N(A)`.  This gives the pointwise charge

\[
 w_A(UV)\le
 \sum_{i=1}^g|f_i(U)-f_i(V)|.                                  \tag{4.21}
\]

For each fixed centre, the proof of Lemma 4.1 shows that `f_i` is an
interval on the internal geodesic and has total variation at most four
after adjoining the two seams.  Sum (4.21) over the collar. \(\square\)

### Corollary 4.7 (bounded-centre container implication)

Suppose the pre-thinning isotropic energy inequality (3.7) holds on every
union of at most `g=g(m)` principal stars, with
`vartheta=O(m^{-1/2})`.  If

\[
                              g^2=o(\log m),                     \tag{4.22}
\]

then some exact thinning is cut-thin on all those unions simultaneously.

#### Proof

There are at most `(2^n)^g` ordered descriptions.  Cuts whose complement
has size at most `m-2` are automatically safe for every protected bank of
maximum degree two.  Every remaining nonempty cut has `sigma>=m-2` by the
sharp middle-shadow bound.  Theorem 3.1 and (4.20) bound the total failure
probability by

\[
 2^{ng}(e\vartheta)^{(m-2)/(4g)}.                              \tag{4.23}
\]

Its logarithm is `O(mg)-Omega(m log(m)/g)`, which tends to `-infinity`
under (4.22). \(\square\)

In particular, the connected two-centre partial-colex obstruction used in
Section 5 has aperture at most eight.  Its role is to refute scalar
size-stratum counting, not to create a long correlated jump inside one
collar.

## 5. Why the current generic cut count does not close the proof

The whole-collar aperture in Theorem 3.1 is not merely an artefact of a
crude estimate.

### Lemma 5.1 (the `2ell` collar aperture is attained)

Let a generalized balanced collar have internal geodesic length `h>=2`
and hence `ell=h+2` Johnson transitions.  If `m` is large enough relative
to `h`, there are a support `S` of size `m+h` and a collar `B` such that,
for the connected equality cut

\[
                         A={S\choose m-1},                       \tag{5.0a}
\]

one has

\[
                         \boxed{w_A(e)=2\quad(e\in B),
                         \qquad w_A(B)=2\ell.}                   \tag{5.0b}
\]

#### Proof

Choose `y notin S`.  Take `M_0` to consist of `y` and `m-1` elements of
`S`.  Choose all deletion labels, all internal entering labels, both seam
deletion labels, and the fresh right entering label inside `S`, in the
standard generalized balanced-collar pattern.  The `h` internal entering
labels together with the fresh right label fit because
`|S-M_0|=h+1`; the fixed core supplies the seam deletion labels.

Every owner on the collar then has the form

\[
                         \{y\}\cup T,\qquad T\in{S\choose m-1}. \tag{5.0c}
\]

Every lower colour on a collar edge has the form

\[
                         \{y\}\cup Q,\qquad Q\in{S\choose m-2}. \tag{5.0d}
\]

Thus no lower colour belongs to `A`, while both owner endpoints belong to
`N(A)` (delete `y` to obtain a member of `A`).  Equation (0.7) gives weight
two on every transition. \(\square\)

Hence no universal argument based only on geodesicity can replace the
block jump `2ell` by a constant.  Any edge-resolution MGF must use the
rarity of collars aligned with the particular low-slack support, or a
switching operation which moves them out of that support.

The protected-Ore functional and loss split over the Johnson-connected
components of `A`.  It is therefore enough to test connected cuts.  The
frozen connected-set estimate says that the number `C_t` of connected
`t`-vertex cuts is at most

\[
 C_t\le W\Delta^{2(t-1)},\qquad \Delta=m(m-1).                  \tag{5.1}
\]

Assume optimistically that the global bank energy (3.7) holds with the
isotropic value `vartheta=Theta(ell/m)`.  Combining (3.8)--(3.9) with
(5.1), the generic union bound at size `t` has logarithm at most

\[
 O(m)+4t\log m
 -\left({\sigma(A)\over4\ell}+o\!\left({\sigma(A)\over\ell}\right)
  \right)\log m.                                               \tag{5.2}
\]

Thus this particular pair of estimates can close a size stratum only at
the scale

\[
                         \sigma(A)>(16+o(1))\ell t.             \tag{5.3}
\]

That condition is false for genuine connected positive-defect cuts.  The
frozen two-level partial-colex family `A_q` at `m=4q` is connected, has
positive clique-closure defect, and satisfies

\[
                         \sigma(A_q)<6|A_q|.                    \tag{5.4}
\]

Since `ell=Theta(sqrt(m))`, (5.4) is separated from (5.3) by an unbounded
factor.

### Theorem 5.2 (sharp scope of the entropy obstruction)

The following three ingredients, by themselves, do **not** yield an
all-cut union-bound proof:

1. the exact isotropic first moment (1.8);
2. collar-block concentration using only `0<=w_A(B)<=2ell`; and
3. the generic connected-set count (5.1).

More precisely, their resulting sufficient inequality is (5.3), while the
explicit connected cuts (5.4) violate it for all large `m`.

This is a no-go for that proof package, not a counterexample to random
collar cut-thinness.  The count (5.1) is enormously wasteful on the
structured low-slack family (5.4), which is a two-centre Hamming-one union
of principal stars.  A successful proof may still proceed in either of two
ways:

* prove a low-`sigma` stability/container theorem whose entropy is
  `o(sigma log(m)/ell)`; or
* prove a collar switching/MGF estimate at edge rather than whole-collar
  resolution, removing the factor `ell` from the exponent.

For the audited three-palette bank, the newer sublinear-exposure theorem
already closes both cardinality tails: any residual obstruction and its
optional complement have size `2^{2m-o(m)}`.  It also leaves an optional
middle core, and an explicit coordinate-cut construction proves that this
middle window is real for generic locally spread path banks.  Therefore the
live application of Theorem 1.1 is precisely to that nonprincipal optional
middle core.  The partial-colex example (5.4) diagnoses the insufficiency
of generic connected-set counting; it is not asserted to survive the
sublinear-exposure tail theorem for the actual collar bank.

### Proposition 5.3 (ordinary approximate-junta stability is too coarse)

For a fixed protected bank of maximum degree two, put

\[
                         F_P(A)=c_P(A)-\sigma(A).                \tag{5.5}
\]

If two lower cuts differ in `t` vertices, then

\[
 \boxed{|F_P(A)-F_P(A')|\le(3m+4)t.}                            \tag{5.6}
\]

Consequently an approximation to `A` with symmetric-difference error
`epsilon W` controls the exact Ore margin only to additive error
`O(m epsilon W)`.  Since a failed integral cut can have margin one, a
generic slice junta theorem giving only `epsilon W` Hamming error would
have to be used at the exponentially tiny scale

\[
                         \epsilon=O((mW)^{-1}).                  \tag{5.7}
\]

Its resulting junta bound is far too large.  The required stability input
must therefore preserve the exact cut or provide a margin-sensitive
container; ordinary constant-error Friedgut--Wimmer approximation does not
close the gate.

#### Proof

It is enough to toggle one lower vertex `x`.  Its upper neighbourhood has
`m` owners.  Therefore `N(A)` changes by at most `m` owners, each of
protected degree at most two, while the term `D_P(A)` changes by at most
two.  The crossing identity `c_P(A)=D_P(N(A))-D_P(A)` gives

\[
                         |\Delta c_P|\le2m+2.                    \tag{5.8}
\]

In (0.4), at most `m` capped owner terms change, each by at most one, and
the term `-2|A|` changes by two.  Hence

\[
                         |\Delta\sigma|\le m+2.                 \tag{5.9}
\]

Add (5.8)--(5.9) and telescope over the symmetric difference. \(\square\)

## 6. Exact remaining cut-thinness target

The clean positive target exposed by the preceding results is the
following.

### Protected collar cut-spread lemma

Construct a three-palette-disjoint Catalan collar bank `P` such that

\[
 \boxed{
 \sum_{e\in P}w_A(e)\le\sigma(A)
 \qquad(A\subseteq\mathcal L).}
\tag{6.1}
\]

Then `lambda_P(A)<=sigma(A)` for every cut, so the protected incidence
lift extends to a spanning two-factor.

The exact full-graph identity proves that (6.1) has fractional density
margin `Theta(sqrt(m))`.  The one-coordinate equality/stability core is
already safe by Theorem 4.2.  What remains is not another local star-load
estimate: it is a correlated rounding theorem for the low-slack shifted
containers, or an edge-resolution switching theorem for random geodesic
collars.

## 7. Scope

This note does not prove that the three-palette Catalan bank extends.  It
proves:

1. the exact all-edge transition identity;
2. a uniform `Theta(m^{-1/2})` fractional protected-Ore margin;
3. a rigorous exact-thinning tail theorem;
4. deterministic safety of all one-coordinate principal stars; and
5. a sharp explanation of why current generic connected-cut entropy loses
   the entire collar-length factor.

No conclusion about connectedness of the completed factor, residence,
deeper upper shadows, or the common-cap compiler is implicit.

## 8. Dependencies

* `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`
* `MATH_THEOREM_PROTECTED_ORE_JOHNSON_COMPONENT_REDUCTION_20260804.md`
* `MATH_THEOREM_CAPPED_LOWER_SHADOW_COMPRESSION_AND_PARTIAL_COLEX_OBSTRUCTION_20260804.md`
* `MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md`
* `MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`
* `MATH_THEOREM_PROTECTED_FACTOR_TWO_MATCHING_COORDINATE_CUT_OBSTRUCTION_20260805.md`
