# Plateau truncation: valid orbit-floor theorem and the unresolved tail

Date: 2026-07-26

Method: pure mathematics only.

## 1. Exact truncated orbit-floor inequality

Fix a depth `q`.  Put

\[
 N=N_q,\qquad \lambda={W\over N}>1,
\]

and let `mu` be the canonical load vector, of total mass `W`.  For an
integer `b>=1`, set

\[
 g(S)=\min\{\mu(S),b\},\qquad
 D=\sum_S(\mu(S)-b)_+=W-\|g\|_1,
\]

\[
 \bar\lambda={\|g\|_1\over N},\qquad
 \delta=g-\bar\lambda\mathbf1.
\tag{1.1}
\]

For a prime coordinate cycle `sigma`, write `Pi_sigma` for orbit
averaging and `mathfrak D_sigma(mu)` for the relaxed orbit-mass hole
floor.

### Theorem 1.1 (truncated one-sided smoothing)

For every `sigma`,

\[
 \boxed{
 \mathfrak D_\sigma(\mu)
 \le D+\min\left\{
       \sqrt N\,\|\Pi_\sigma\delta\|_2,
       {\|\Pi_\sigma\delta\|_2^2\over4(\lambda-1)}
                         \right\}.}
\tag{1.2}
\]

For a uniformly random prime coordinate cycle,

\[
 \boxed{
 \mathbb E_\sigma\|\Pi_\sigma\delta\|_2^2
 ={1\over n}\left(
       \|\delta\|_2^2-\|\Pi_1\delta\|_2^2\right)
 \le {bW\over n}.}
\tag{1.3}
\]

#### Proof

Since `g<=mu` coordinatewise, its mass on every target orbit is no larger,
and therefore

\[
                  \mathfrak D_\sigma(\mu)
                  \le\mathfrak D_\sigma(g).
\tag{1.4}
\]

The centered Cauchy estimate, with the possible loss of mean written
separately, gives

\[
 \mathfrak D_\sigma(g)
 \le (N-\|g\|_1)_++\|\Pi_\sigma\delta\|_1
 \le D+\sqrt N\,\|\Pi_\sigma\delta\|_2.
\tag{1.5}
\]

For the surplus estimate, add the constant
`u=lambda-bar(lambda)>=0` to every coordinate of `g`.  The resulting
formal vector has total mass `W` and the same centered deviation `delta`.
The scalar inequality

\[
                  (1-x)_+\le u+(1-x-u)_+
\]

costs `Nu=D` after summation.  Lemma 4.1 of the prime-cycle smoothing
note then gives

\[
 \mathfrak D_\sigma(g)
 \le D+{\|\Pi_\sigma\delta\|_2^2\over4(\lambda-1)}.
\tag{1.6}
\]

This proves (1.2).  The conjugacy-class identity

\[
 K_n=\Pi_0-{1\over n-1}\Pi_1
\]

applied to the arbitrary zero-mean vector `delta` proves the equality in
(1.3).  Finally

\[
 \|\delta\|_2^2\le\|g\|_2^2
                 \le b\|g\|_1\le bW,
\]

proving the last inequality. \(\square\)

### Corollary 1.2 (valid conditional multidepth criterion)

For truncation levels `b_q`, one common prime coordinate cycle satisfies

\[
 {1\over W}\sum_{q\le H}\mathfrak D_{\sigma,q}
 \le C\sum_{q\le H}\left[
   \Psi_q(b_q)+
   \min\left\{\sqrt{b_q/n},
               {b_q\over n(\lambda_q-1)}\right\}
                         \right],
\tag{1.7}
\]

where

\[
                  \Psi_q(b)={1\over W}
                    \sum_S(\mu_q(S)-b)_+.
\]

In the shallow Gaussian range,
`n(lambda_q-1)>=c q^2`, so the second entry in the minimum is
`O(b_q/q^2)`.  Thus the proposed truncation criterion is a correct
**conditional theorem about the relaxed missing-target orbit floor**.

It is not a theorem about MWB balanced overload: excessive multiplicity
is free in `mathfrak D` but is one of the two terms measured by `O_q`.
It also does not realize the orbit floor by one legal exact factor; the
simultaneous integral lift remains a separate gate.

## 2. What Section 19 of the selector note actually proves

The pointed-subtree estimate

\[
 {1\over W}\sum_{r\ge R}A_{m,r}=O(R^{-1/2})
\tag{2.1}
\]

counts recursive nodes whose *own* invisible block has size at least
`R`.  In particular, taking `R=q` gives the observed `q^{-3/2}` mass for
the special event that the whole depth-`q` zero window is one recursive
subtree.

It does **not** imply

\[
                         \Psi_q(B)=O(q^{-3/2})
\tag{2.2}
\]

for an absolute constant `B`.  A fixed size-`r` invisible subtree remains
invisible inside every larger zero window containing it.  Moreover a zero
window can contain several maximal interior blocks, and their Catalan
filling multiplicities multiply.  Neither phenomenon is counted by
setting `R=q` in (2.1).

The exact completed-block decomposition proves only:

1. exterior blocks are target-forced;
2. maximal interior blocks are freely Catalan-filled;
3. the residual address data lie on two boundary spines.

To establish (2.2), or any substitute adequate in (1.7), one still needs
a theorem controlling the **total product of all interior Catalan
fillings per target**, including mergers of several boundary skeletons.
No such theorem has yet been proved.

In fact (2.2) is false for every absolute `B`.

### Theorem 2.1 (fixed invisible blocks persist through larger windows)

Fix `r` with `d=Cat_r>B`.  Uniformly for `r<=q<=m`,

\[
 \boxed{
 \Psi_q(B)\ge
 {H_{m,r}(d-B)\over W(1+d\lfloor q/r\rfloor)},
 \qquad
 H_{m,r}={1\over2}\binom{2(m-r)}{m-r}.}
\tag{2.3}
\]

Consequently, for fixed `r` and `q=o(m)` tending to infinity,

\[
                         \boxed{\Psi_q(B)\ge {c_{r,B}\over q}}
\tag{2.4}
\]

with `c_(r,B)>0`.  In particular `Psi_q(B)=O(q^(-3/2))` is impossible.

#### Proof

Take any aligned one-hole context of hole size `r`, counted by
`H_(m,r)`.  If its block occupies pair positions
`[s,s+r-1]`, choose canonically

\[
                         i=\max\{0,s+r-q\}.
\]

Because `q>=r` and `s+r<=m`, one has
`0<=i<=s` and `i+q<=m`; hence the length-`q` zero window beginning at
`i` contains the whole block.  Lemma 19.1 of the selector note shows that
the `d=Cat_r` fillings of the hole give `d` distinct rooted windows with
one common physical target.  Call this a context group.

A fixed rooted length-`q` window can belong to at most `floor(q/r)` such
groups.  Indeed, its responsible size-`r` recursive nodes have blocks
contained in the zero interval; distinct tree nodes of the same size are
disjoint, and each consumes `r` pair positions.  Therefore the
intersection graph of the context groups has maximum degree at most
`d floor(q/r)-1`: each group has `d` occurrences and every occurrence
lies in at most `floor(q/r)` groups.

Greedy selection gives at least

\[
                    {H_{m,r}\over1+d\lfloor q/r\rfloor}
\]

groups with pairwise disjoint occurrence sets.  If `k` selected groups
have the same target, its full load is at least `kd`, and

\[
                         (kd-B)_+\ge k(d-B).
\]

Summing over targets proves (2.3).  Finally

\[
                         {H_{m,r}\over W}
                         \longrightarrow {1\over4\,4^r}
\]

for fixed `r`, which proves (2.4). \(\square\)

The canonical choice of one containing window in this proof discards a
factor of order `q`.  Keeping all containing windows cancels the overlap
denominator and strengthens (2.4) to a constant lower bound.

### Theorem 2.2 (constant fixed-cutoff plateau tail)

Under the hypotheses of Theorem 2.1, uniformly for `2r<=q=o(m)`,

\[
 \boxed{
 \Psi_q(B)\ge(1-o_m(1))
 {(q-r+1)H_{m,r}(d-B)
  \over W(1+d\lfloor q/r\rfloor)}.}
\tag{2.5}
\]

Consequently

\[
 \boxed{
 \liminf_{m\to\infty}\ \inf_{2r\le q=o(m)}\Psi_q(B)
 \ge c_{r,B}>0.}
\tag{2.6}
\]

#### Proof

A fixed aligned size-`r` hole is contained in `q-r+1` aligned
length-`q` zero windows.  In the cyclic pointed model this is exact.  In
the linear rooted normalization only contexts within `O(q)` positions of
the cut can lose a placement; cyclic pointing, or averaging the cut,
shows that these form an `o_m(1)` fraction for `q=o(m)`.  Thus the number
of context--window groups is

\[
 G=(1-o_m(1))(q-r+1)H_{m,r}.
\tag{2.7}
\]

The occurrence-degree argument of Theorem 2.1 is unchanged: one rooted
window belongs to at most `floor(q/r)` groups, so the group-intersection
graph has maximum degree at most `d floor(q/r)-1`.  Greedy selection now
gives at least

\[
 {G\over1+d\lfloor q/r\rfloor}
\]

token-disjoint groups.  Each contributes `d-B` to the truncated tail,
even when several selected groups share one target, because
`(kd-B)_+>=k(d-B)`.  This proves (2.5).

Finally `H_(m,r)/W -> 1/(4 4^r)`, while
`(q-r+1)/q>=1/2` for `q>=2r`.  For instance one may take

\[
 c_{r,B}={r(d-B)\over16d\,4^r}>0,
\]

which proves (2.6). \(\square\)

Thus a constant truncation level is impossible.  Theorem 2.2 does not
rule out a growing cutoff.  Choosing `r` minimally with `Cat_r>B` gives
a lower bound of approximate order

\[
 {1\over B\sqrt{\log(B+2)}},
\tag{2.8}
\]

which must be balanced against the valid smoothing penalties in (1.7).

There is a stronger boundary-service version.  It avoids both the
`q-r+1` window multiplicity and the `q/r` overlap denominator.

### Theorem 2.3 (growing-cutoff boundary tail)

Let `b>=1`, and choose `r` minimally so that

\[
                         d=\operatorname{Cat}_r\ge4b.       \tag{2.9}
\]

Then `d<16b` and `r=Theta(log(b+2))`.  Uniformly for

\[
                         r\le q\le m/2,qquad r=o(m),
\]

one has

\[
 \boxed{
 \Psi_q(b)\ge {H_{m,r}(d/2-b)\over W}
             \ge {c\over(\log(b+2))^{3/2}}.}               \tag{2.10}
\]

#### Proof

Let an aligned size-`r` block occupy pair positions `[s,s+r-1]`.  If
`s+q<=m`, choose the length-`q` zero window beginning at `s`; the block is
its left boundary block.  Otherwise choose the window ending at `s+r`.
Its start is `s+r-q>=0`, because `s>m-q`, `q<=m/2`, and `r>=1`.  Thus every
one of the `H_(m,r)` contexts supplies a canonical boundary-served
length-`q` group of `d` fillings with one target.

A rooted length-`q` occurrence belongs to at most two such groups: its
responsible size-`r` recursive block must be the unique block beginning at
the left window boundary or the unique block ending at the right boundary.
For one target `S`, if `h_S` context groups land there, their total
group--occurrence incidence is `d h_S`; hence their union contains at least
`d h_S/2` distinct occurrences.  Therefore

\[
 (\mu_q(S)-b)_+
 \ge \left({dh_S\over2}-b\right)_+.
\]

Summing over occupied targets, using
`sum_S h_S=H_(m,r)` and at most `H_(m,r)` occupied targets, gives

\[
 \sum_S(\mu_q(S)-b)_+
 \ge H_{m,r}(d/2-b).
\]

Minimality in (2.9) and `Cat_r/Cat_(r-1)<4` give `d<16b` and
`r=Theta(log(b+2))`.  Finally

\[
 {H_{m,r}d\over W}
 \asymp4^{-r}\operatorname{Cat}_r
 \asymp r^{-3/2},
\]

uniformly for `r=o(m)`.  Since `d/2-b>=d/4`, this proves (2.10).
\(\square\)

Thus scalar coordinatewise truncation cannot make the plateau tail decay
with the window length: once `q` contains the logarithmic-size boundary
block, the lower bound depends only polylogarithmically on `b`.  This is
why Sections 5--7 cap each fibre's useful phase mass at `p` and retain it,
rather than deleting all load above one scalar height.

### Corollary 2.4 (no scalar cutoff can satisfy the smoothing criterion)

Let `n=2m+1` tend to infinity and let `b_q>=1` be arbitrary integer
cutoffs.  On the interval

\[
 I_n=\left[\left\lceil{n^{1/4}\over8}\right\rceil,
           \left\lfloor{n^{1/4}\over4}\right\rfloor\right]\cap\mathbb Z
\]

one has

\[
 \boxed{
 \sum_{q\in I_n}\left[
   \Psi_q(b_q)+
   \min\left\{\sqrt{b_q/n},{b_q\over2q^2}\right\}
                    \right]
 \ge {c n^{1/4}\over(\log n)^{3/2}}.}                     \tag{2.11}
\]

In particular the scalar criterion (1.7) cannot be `o(1)`, even on one
fixed Gaussian window.

#### Proof

For `q in I_n`,

\[
                         {4q^4\over n}<1.
\]

Thus, for every `b>=1`, the smaller smoothing branch is
`sqrt(b/n)`.  If `b>n`, this branch is greater than one.  If `b<=n`, let
`r` be minimal with `Cat_r>=4b`.  Then `r=O(log n)=o(q)`, so Theorem 2.3
applies and gives

\[
                         \Psi_q(b)\ge {c\over(\log n)^{3/2}}.
\]

Hence every summand in (2.11) is at least the smaller of a positive
constant and `c(log n)^(-3/2)`.  Since `|I_n|=Theta(n^(1/4))`, summing
proves (2.11). \(\square\)

This is a no-go for **coordinatewise scalar deletion**, not for the
component decomposition of Sections 5--7: those sections retain up to one
full orbit of useful mass from every invisible fibre and center the fibre
supports separately.

There is, however, a stronger phase-capacity consequence which applies to
every coordinate-cycle lift of the canonical factor, independently of how
the fibres are decomposed.

### Theorem 2.5 (phase capacity rules out every canonical row-power lift)

Let `F_MSW` be the canonical factor and let `sigma` be any coordinate
`p`-cycle, where `p=2m+1` is prime.  Assign arbitrary exponents
`a(C) in Z_p` to its rows; the shifted rows need not preserve exact middle
ownership.  Let `H'_q` be the number of missing depth-`q` targets in the
shifted row family.  Then, uniformly for

\[
             p^{1/4}/8\le q\le p^{1/4}/4,
\]

\[
 \boxed{
 H'_q\ge {cW\over(\log p)^{3/2}}.}                         \tag{2.12}
\]

Consequently

\[
 \boxed{
 \sum_{p^{1/4}/8\le q\le p^{1/4}/4}H'_q
 \ge {cWp^{1/4}\over(\log p)^{3/2}},}                     \tag{2.13}
\]

so no row-power lift of the canonical MSW factor can satisfy the weak
vertical-wreath lemma, and hence it cannot establish the constant-one
theorem through this architecture.

#### Proof

Fix a depth and a source target `S`.  Its `mu_q(S)` occurrences belong to
distinct rows.  After arbitrary row powers, all of their images lie among
the `p` translates of `S`.  (The orbit has exactly `p` members because
`0<|S|<p` and `p` is prime.)  Thus those occurrences can cover at most
`min(mu_q(S),p)` targets.  In fact distinctness of the owning rows is not
needed for this upper bound: repeated occurrences controlled by one row
would only reduce their phase freedom.  Taking the union over all source
targets gives

\[
 \#\{\text{covered targets after the lift}\}
 \le\sum_S\min\{\mu_q(S),p\}
 =W-\sum_S(\mu_q(S)-p)_+ .                                 \tag{2.14}
\]

This remains an upper bound when images coming from different source
targets coincide.  Therefore

\[
 H'_q\ge
 \sum_S(\mu_q(S)-p)_+-(W-N_q)
 =W\Psi_q(p)-(W-N_q).                                      \tag{2.15}
\]

Choose `r` minimally with `Cat_r>=4p`.  Then `r=Theta(log p)`, and
Theorem 2.3 gives

\[
                         \Psi_q(p)\ge {c\over(\log p)^{3/2}}
\]

throughout the displayed `q`-interval.  On the same interval,

\[
 {W-N_q\over W}=1-{1\over\lambda_q}=O(q^2/m)=O(p^{-1/2}),
\]

which is negligible relative to `(log p)^(-3/2)`.  This proves (2.12),
and summing over `Theta(p^(1/4))` depths proves (2.13). \(\square\)

For clarity, all constants here are uniform.  Minimality of `r` and
`Cat_r/Cat_(r-1)<4` give `4p<=Cat_r<16p`, while

\[
 {H_{m,r}\operatorname{Cat}_r\over W}\asymp r^{-3/2}
\]

uniformly for `r=O(log p)`.  Also `r=o(p^(1/4))`, so Theorem 2.3 applies
simultaneously at every depth in the displayed interval for all
sufficiently large `p`.

Theorem 2.5 is stronger than the scalar-truncation no-go: it allows each
row to choose its phase adversarially and does not impose middle legality.
The obstruction is simply that a source spike of height `d` has only `p`
possible translated targets.  Component-wise smoothing cannot restore the
discarded `d-p` units.  A successful proof must therefore change the
underlying middle factor (or use non-row-power trades which change these
source fibres), rather than merely rephase the canonical MSW rows.

The phase-capacity part is seed-independent; only the Catalan lower bound
used to evaluate it is specific to the canonical seed.

### Proposition 2.6 (the exact seed-level phase-capacity criterion)

For an arbitrary exact middle factor `F`, define

\[
 K_q(F)=\sum_S(\mu_q^F(S)-p)_+,
\qquad
 \operatorname{PCap}_H(F)=
 \sum_{q\le H}\bigl(K_q(F)-(W-N_q)\bigr)_+.               \tag{2.16}
\]

Every row-power lift `F_a` of `F`, legal or not, satisfies

\[
 \boxed{
 \sum_{q\le H}H_q(F_a)\ge \operatorname{PCap}_H(F).}       \tag{2.17}
\]

Consequently

\[
 \boxed{
 \operatorname{PCap}_H(F)=o(W)}                            \tag{2.18}
\]

is a necessary seed-level condition for a row-power proof of the weak
vertical-wreath lemma.  The stronger pointwise condition `K_q(F)=0` is
sufficient to remove this particular obstruction, but it is **not
necessary**: the unavoidable surplus `W-N_q` can absorb that much source
phase waste, and an `o(W)` aggregate error is allowed.

#### Proof

The union-capacity argument (2.14)--(2.15) used no property of the MSW
factor, so for every `q`,

\[
                         H_q(F_a)\ge K_q(F)-(W-N_q).
\]

Taking positive parts and summing proves (2.17). \(\square\)

Condition (2.18) is only necessary.  It neither constructs phases which
cover the available slots nor ensures that those phases preserve exact
middle ownership.  Thus the construction problem does not reduce solely
to finding a factor with zero cap tail.

### Corollary 2.7 (zero overload above \(p\) is not the exact target)

For a cutoff \(Q\), define

\[
             \operatorname {OV}_Q(F)=\max_{q\le Q}K_q(F). \tag{2.19}
\]

The condition \(\operatorname {OV}_Q(F)=0\) is sufficient to make the
scalar phase-capacity lower bound vanish, but it is not necessary.  If a
row-power lift has zero missing targets at each depth, the exact capacity
necessity is only

\[
                         K_q(F)\le W-N_q\qquad(q\le Q),    \tag{2.20}
\]

and for an \(o(W)\) aggregate hole target it is precisely the weaker
condition \(\operatorname {PCap}_Q(F)=o(W)\) from (2.18).  The positive
quantity \(W-N_q\) is the duplicate budget forced by having \(W\)
occurrences and only \(N_q\) targets.

Nor is \(\operatorname {OV}_Q(F)=0\) sufficient for the complete
construction: it supplies neither a common covering phase assignment nor
exact middle legality.  If genuine trades or a multi-seed switch are
allowed before rephasing, the necessary statement is that **some
reachable exact state** \(G\) satisfy
\(\operatorname {PCap}_Q(G)=o(W)\); the common-core, row-space, and lattice
obstructions of Proposition 12.4 may prevent even that.

A \(\nu\)-dependent twisted interleaving can therefore be a complete
target only if it proves the exact middle-cover equations and either
directly has \(o(W)\) cyclic band holes, or also supplies a common legal
phase lift realizing them.  Merely proving
\(\operatorname {OV}_Q=0\) settles only one scalar obstruction.  A twist
which merely rephases the unchanged canonical source fibres remains ruled
out by Theorem 2.5; a genuine twist which moves those fibres is not ruled
out.

## 3. Consequence for the architecture

The raw quadratic target is conclusively false, and Theorem 1.1 shows
that a one-sided inequality is mathematically available.  Theorems
2.3--2.5 now show more: neither scalar truncation nor **any** row-power
phase assignment can overcome the canonical MSW plateau on the required
multidepth window.

Thus the current status is

\[
 \boxed{
 \text{the canonical MSW + prime-cycle row-power architecture is ruled out;}\
 \text{a successful route must alter the middle factor's source fibres by}\
 \text{genuine trades or construct a different exact seed.}}
\tag{3.1}
\]

The plateau has not disproved the constant-one theorem, and the general
component inequalities in Sections 5--8 remain valid tools for a different
seed.  What is no longer open is whether a clever legal choice of cyclic
row powers can rescue the canonical seed: Theorem 2.5 says it cannot.

## 4. Ramsey does not remove orientation frustration

Relative endpoint-orientation signs form a signed complete graph.
Reversing one endpoint cycle switches all incident signs.  Hence the sign
product around a triangle is switching-invariant.  An all-negative
monochromatic triangle has product `-1` and cannot be converted into an
all-positive triangle by reversing representatives.  Therefore
`R(3,3)=6` returns exactly the existing dichotomy--a balanced positive
triangle or a frustrated negative triangle--and does not close the affine
gate.

There is a weaker genuine consequence.  An all-negative clique has size
at most five: for a fixed member, its pairwise shared-edge cores with the
other members are disjoint, each of size at least `(p-1)/4`.  Ramsey then
gives a positive coherent clique of order at least a fixed power of `p`,
but the circuit-pencil theorem currently permits such a sublinear clique.
This does not yet yield a contradiction.

## 5. Direct one-sided smoothing of a spike decomposition

Truncating the whole load at one scalar height throws away precisely the
Catalan plateau mass which can fill a complete phase orbit.  A better
one-sided estimate keeps that mass, caps it only at the orbit capacity,
and centers the **supports of multiplicity classes** separately.

Let `X` be one target rank, `|X|=N`, and let a prime coordinate cycle
`sigma` partition `X` into `M=N/p` orbits of size `p`.  For a nonnegative
vector `v` write

\[
 v(O)=\sum_{S\in O}v(S),\qquad
 \mathfrak D_\sigma(v)=\sum_O(p-v(O))_+ .                    \tag{5.1}
\]

Suppose that

\[
                         w=\sum_{j\in J}w_j\le\mu           \tag{5.2}
\]

coordinatewise.  Put

\[
 g_j=\|w_j\|_1,qquad h_j=\|w_j\|_2^2,qquad
 G=\sum_jg_j,                                                \tag{5.3}
\]

and define the orbit-support collision and orbit variance

\[
\begin{split}
 C_{\sigma,j}
   &=\sum_O\sum_{\{S,T\}\subset O}w_j(S)w_j(T),\\
 V_{\sigma,j}
   &=\sum_O\left(w_j(O)-{pg_j\over N}\right)^2\\
   &=h_j+2C_{\sigma,j}-{pg_j^2\over N}.                     \tag{5.4}
\end{split}
\]

### Theorem 5.1 (capped first-moment orbit bound)

For every prime cycle `sigma`,

\[
 \boxed{
 \mathfrak D_\sigma(\mu)
 \le (N-G)_+
   +{1\over2}\sqrt{N\over p}
        \sum_{j\in J}\sqrt{V_{\sigma,j}}.}                 \tag{5.5}
\]

For a uniformly random prime coordinate cycle,

\[
 \boxed{
 \mathbb E_\sigma V_{\sigma,j}
 =h_j-{g_j^2\over N}-\|\Pi_1w_j\|_2^2
 \le h_j,}                                                  \tag{5.6}
\]

where `Pi_1` is the first nonconstant Johnson harmonic projection.
Consequently

\[
 \boxed{
 \mathbb E_\sigma\mathfrak D_\sigma(\mu)
 \le (N-G)_+
   +{1\over2}\sqrt{N\over p}\sum_j\sqrt{h_j}.}             \tag{5.7}
\]

#### Proof

The first inequality in (5.2) gives
`mathfrak D_sigma(mu)<=mathfrak D_sigma(w)`.  Put

\[
 L=\max\{G,N\},\qquad
 \theta_j={pg_j\over L},\qquad
 r=p-\sum_j\theta_j.
\]

Thus `r=0` when `G>=N`, while `r=p(1-G/N)` when `G<N`.  For every orbit,

\[
 \left(p-\sum_jw_j(O)\right)_+
 \le r+\sum_j(\theta_j-w_j(O))_+ .                           \tag{5.8}
\]

Moreover `theta_j<=pg_j/N`, the mean of `w_j(O)` over the `M=N/p`
orbits.  Hence

\[
\begin{split}
 \sum_O(\theta_j-w_j(O))_+
 &\le\sum_O\left({pg_j\over N}-w_j(O)\right)_+\\
 &= {1\over2}\sum_O
       \left|w_j(O)-{pg_j\over N}\right|\\
 &\le {1\over2}\sqrt{N\over p}\sqrt{V_{\sigma,j}}.        \tag{5.9}
\end{split}
\]

The total contribution of `r` over all orbits is `(N-G)_+`, proving
(5.5).

For (5.6), observe that

\[
 V_{\sigma,j}
   =p\|\Pi_\sigma w_j\|_2^2-{pg_j^2\over N}.
\]

The prime-cycle conjugacy identity, now applied to a vector of arbitrary
total mass, is

\[
 \mathbb E_\sigma\|\Pi_\sigma w_j\|_2^2
 ={g_j^2\over N}
 +{1\over p}\left(
      h_j-{g_j^2\over N}-\|\Pi_1w_j\|_2^2\right).
\]

Substitution proves (5.6).  Jensen's inequality in (5.5) gives (5.7).
\(\square\)

For a pure spike `w_j=d 1_A`, `|A|=a`, (5.4)--(5.6) become

\[
 V_{\sigma,j}=d^2\left(
       a+2C_\sigma(A)-{pa^2\over N}\right),                 \tag{5.10}
\]

and the exact random-cycle support-collision identity is

\[
 \boxed{
 \mathbb E_\sigma C_\sigma(A)
 ={1\over2}\left({(p-1)a^2\over N}
                  -\|\Pi_1\mathbf1_A\|_2^2\right).}        \tag{5.11}
\]

Thus plateau height enters (5.7) linearly as `d sqrt(a)`, rather than
quadratically as `d^2a`.  Formula (5.11) also identifies the only possible
improvement over the universal estimate: point-regular or otherwise
first-harmonic-rich supports have smaller orbit collision variance.

### Corollary 5.2 (spikes of height `d`)

Suppose

\[
                 \sum_d d\,\mathbf1_{A_d}\le\mu,
 \qquad |A_d|=a_d,
 \qquad G=\sum_dda_d,                                       \tag{5.12}
\]

where the supports may overlap.  Then

\[
 \boxed{
 \mathbb E_\sigma\mathfrak D_\sigma(\mu)
 \le (N-G)_+
 +{1\over2}\sqrt{N\over p}\sum_d d\sqrt{a_d}.}            \tag{5.13}
\]

If a spike height exceeds `p`, it may be replaced by `p` in
(5.12)--(5.13) without weakening the orbit-floor conclusion.  Thus
(5.13) is naturally a capped-first-moment theorem, not a tail-deletion
theorem.

#### Proof

Apply Theorem 5.1 with `w_d=d 1_(A_d)`.  Overlap of the supports causes
no difficulty because (5.2) is the only required relation and the proof
centers each component separately.  A single target contributes at most
`p` useful units to its orbit shortfall, which justifies the final cap.
\(\square\)

## 6. Canonical interior-forest fibres and dyadic plateau classes

At one depth `q`, apply Lemma 19.1 of the selector note to every intrinsic
rooted window.  Delete the freely filled maximal interior blocks but retain
the two-boundary skeleton and all physical addresses.  This partitions the
occurrences into canonical fibres `F`.  If the maximal interior block sizes
are `r_1,...,r_s`, then

\[
                         d_F=\prod_{a=1}^s\operatorname{Cat}_{r_a}          \tag{6.1}
\]

is the fibre size, and all `d_F` fillings have one target `S_F`.  Complete
the partition of the full canonical depth-`q` load by treating every
remaining occurrence family in the same way, with singleton fibres when
no larger canonical fibre is available.

The useful contribution of one fibre to its phase orbit is at most `p`.
Accordingly put

\[
 b_F=\min\{d_F,p\},
 \qquad
 \mathcal F_{q,k}=\{F:2^{k-1}<d_F\le2^k\},
 \qquad
 B_k=\min\{2^k,p\}.                                         \tag{6.2}
\]

Define

\[
\begin{split}
 w_{q,k}(S)&=\sum_{F\in\mathcal F_{q,k}:S_F=S}b_F,\\
 A_{q,k}&=|\mathcal F_{q,k}|,\\
 \Xi_{q,k}&=
   \#\{\{F,F'\}\subset\mathcal F_{q,k}:S_F=S_{F'}\},\\
 G_q&=\sum_Fb_F.                                             \tag{6.3}
\end{split}
\]

Since the fibre occurrence sets partition the load,

\[
             \sum_kw_{q,k}\le\mu_q,qquad
 \|w_{q,k}\|_2^2
       \le B_k^2(A_{q,k}+2\Xi_{q,k}).                        \tag{6.4}
\]

The cap in (6.2) is not a deletion of useful orbit mass: more than `p`
members of a fibre cannot cover more than the `p` translates of its one
base target.

### Corollary 6.1 (dyadic plateau orbit bound)

For a uniformly random prime cycle,

\[
 \boxed{
 \mathbb E_\sigma\mathfrak D_{\sigma,q}(\mu_q)
 \le (N_q-G_q)_+
 +{1\over2}\sqrt{N_q\over p}
   \sum_k B_k\sqrt{A_{q,k}+2\Xi_{q,k}}.}                    \tag{6.5}
\]

Hence one common prime cycle has total relaxed orbit floor `o(W)` on a
band `q<=H` provided

\[
 \boxed{
 \sum_{q\le H}(N_q-G_q)_+=o(W).}                            \tag{6.6}
\]

and

\[
 \boxed{
 \sum_{q\le H}\sqrt{N_q\over p}
    \sum_kB_k\sqrt{A_{q,k}+2\Xi_{q,k}}=o(W).}               \tag{6.7}
\]

These are one-sided conditions.  They do not ask for a small quadratic
energy of the original load and do not discard fibres of height greater
than the cutoff.

### Proposition 6.2 (the exact aligned Catalan ledger is diagonally small)

For the aligned whole-window fibres of Section 18 of the selector note,

\[
 d_r=\operatorname{Cat}_r,qquad
 A_r=H_{m,r}={1\over2}\binom{2(m-r)}{m-r}.                  \tag{6.8}
\]

Let `b_r=min(Cat_r,p)`.  Uniformly for `H=o(m)`, their diagonal contribution
to (6.5), summed over `r<=H`, is

\[
 \boxed{
 {1\over W}\sum_{r\le H}\sqrt{N_r\over p}\,b_r\sqrt{H_{m,r}}
 =O((\log p)^{-3/4})=o(1).}                                 \tag{6.9}
\]

#### Proof

For `r=o(m)`, one has `N_r<=W` and

\[
                         {H_{m,r}\over W}\le C4^{-r}.
\]

Thus the left side of (6.9) is at most

\[
 {C\over\sqrt p}\sum_{r\le H}b_r2^{-r}.                   \tag{6.10}
\]

Let `R` be the largest integer with `Cat_R<=p`.  Catalan estimates give
`R=Theta(log p)` and

\[
 {1\over\sqrt p}\sum_{r\le R}\operatorname{Cat}_r2^{-r}
 \le {C\over R^{3/4}},
 \qquad
 {1\over\sqrt p}\sum_{r>R}p2^{-r}
 \le {C\over R^{3/4}}.                                     \tag{6.11}
\]

This proves (6.9). \(\square\)

If `Xi_r` counts pairs of aligned contexts of size `r` having the same
physical target, the corresponding unresolved merger contribution is

\[
 {C\over\sqrt{pW}}\sum_{r\le H}b_r\sqrt{\Xi_r}.             \tag{6.12}
\]

Thus the isolated whole-window Catalan diagonal is small.  It does **not**
show that the complete canonical plateau is harmless: Theorem 2.5 proves
that the repeated embedded blocks make the available phase capacity
insufficient.  In the language here, capped first-moment sufficiency
(6.6) fails after all fibres based at the same source target are pooled.
The remaining merger and product-fibre terms cannot repair a deficit of
useful phase mass.  Conditions (6.6)--(6.7) remain a correct abstract
criterion for a different seed, but they are not satisfiable by a mere
row-power rephasing of the canonical MSW load.

The window-service caveat remains explicit: a pointed subtree may occur in
many larger zero windows and at many depths.  The fibre partition is unique
only after `(q,i)` and the entire maximal interior forest are retained.
Accordingly the quantities in (6.6)--(6.7) must be summed at every depth;
(2.1) cannot be reused to pay the same pointed node only once.

## 7. The separate legal-lift condition

The orbit floor in Sections 5--6 permits mass to be rearranged freely
inside every target orbit.  A coordinate phase applied to a physical row
acts simultaneously at every depth and must preserve exact middle
ownership.  Neither Theorem 5.1 nor the Catalan ledger constructs such a
phase choice.

Here is a strongest clean sufficient condition.  Fix one prime cycle
`sigma`.  Assign one exponent `a(C) in Z_p` to every physical middle row
`C`.  Call the assignment a **plateau-rainbow legal lift** if

1. the shifted rows `sigma^(a(C))C` still form an exact middle factor;
2. the same exponent is used for every occurrence of `C` at every depth;
3. for every depth `q` and target orbit `O`, the translated occurrences
   belonging to all canonical fibres based in `O` occupy at least
   \[
      \min\left\{p,\sum_{F:S_F\in O}\min(d_F,p)\right\}
                                                                    \tag{7.1}
   \]
   distinct targets of `O`, apart from a total of `o(W)` declared
   exceptions over the protected band.

Condition (7.1) says equivalently that each fibre is phase-rainbow until
it saturates its orbit, and that the phase sets of different fibres in the
same orbit are disjoint until that orbit is saturated.

### Lemma 7.1 (legal lift attains the capped orbit floor)

If (6.6)--(6.7) hold and a plateau-rainbow legal lift exists, then the
shifted exact factor has `o(W)` missing targets over the protected band.

#### Proof

Row shifts preserve every target-orbit mass.  By (7.1), the number of
covered targets in `O` is at least the capped fibre mass there, truncated
at `p`.  Hence its missing count is at most the relaxed orbit shortfall of
the vector `sum_kw_(q,k)`, plus the declared exceptions.  Corollary 6.1
chooses a common `sigma` for which the sum of those shortfalls is `o(W)`.
Summing the exceptional allowance proves the claim. \(\square\)

This lemma is deliberately conditional.  Independent rainbow phase maps
inside individual Catalan fibres are not enough: the exponents must be
consistent for rows shared across depths, must pack together inside each
target orbit, and must preserve exact middle ownership.  Those three
requirements are the remaining integral lift/deck-circuit gate.
For the canonical source over the full required window, Theorem 2.5 shows
that no assignment can meet this condition: pooled source spikes already
exceed the available `p` phases before middle legality is imposed.

## 8. A universal all-context rainbow labelling (middle legality excluded)

One part of the lift gate can be discharged explicitly.  Write a Dyck
root `x` as its binary word

\[
                 x=x_0x_1\cdots x_{2m-1},\qquad x_i\in\{0,1\},
\]

and, for a prime `p=2m+1`, put

\[
                 a_2(x):=\sum_{i=0}^{2m-1}x_i2^i\pmod p.   \tag{8.1}
\]

### Lemma 8.1 (simultaneous small-subtree rainbow hash)

Let `C[ ]` be any one-hole ordered-binary-tree context whose hole has
semilength `r`.  If `4^r<p`, then

\[
             u\longmapsto a_2(C[u])
\]

is injective on all `Cat_r` Dyck fillings of the hole.  The assertion holds
simultaneously for every ambient size-`m` context and every
`r<(1/2)log_2 p`.

#### Proof

The word of a rooted subtree is a contiguous block in the Dyck word of the
ambient tree.  If the block starts at position `s`, then for two distinct
fillings `u,v`,

\[
 a_2(C[u])-a_2(C[v])
     =2^s\bigl(\operatorname{bin}(u)-\operatorname{bin}(v)\bigr)\pmod p.
\]

The integer in parentheses is nonzero and has absolute value strictly less
than `2^(2r)=4^r<p`.  It is therefore nonzero modulo `p`; multiplication by
`2^s` is invertible modulo the odd prime `p`.  This proves injectivity.
The same proof covers a reflected or reverse-complemented local convention,
because that convention merely bijects the set of length-`2r` binary
blocks. \(\square\)

Thus consistency across different depths and different one-hole contexts
is not by itself an obstruction: one common row label makes every marked
small-subtree fibre rainbow.  In particular, after using the canonical
first-variable-subtree partition rather than the full product fibre, the
same label works for every serviced window of that marked subtree.

This does **not** yet define a legal phase lift.  The shifted rows
`sigma^(a_2(x))C(x)` need not retain exact middle ownership, and phase sets
belonging to different fibres in one target orbit need not be disjoint.
Consequently the remaining gate has been narrowed to

\[
 \boxed{\text{modify or realize the hash (8.1) inside the middle-factor
 legality polytope, with inter-fibre packing.}}               \tag{8.2}
\]

The lemma must not be quoted as a construction of the desired factor; it
solves only the simultaneous intra-fibre rainbow constraint.

There is also no need to demand the exact inter-fibre disjointness in
(7.1).  A summed collision estimate suffices.

### Lemma 8.2 (inter-fibre Bonferroni ledger)

Fix one depth and one target orbit `O`.  Let `P_F subseteq Z_p` be the set
of phases occupied after shifting the rows in a family of marked fibres
based in `O`, and assume each fibre is internally rainbow, so
`|P_F|=d_F<=p`.  Put

\[
 G_O=\sum_Fd_F,\qquad
 J_O=\sum_{F<F'}|P_F\cap P_{F'}|.
\]

Then

\[
 \boxed{
 p-\left|\bigcup_FP_F\right|
 \le (p-G_O)_+ +J_O.}                                     \tag{8.3}
\]

Consequently, an exact-middle legal realization of the hash (8.1) covers
all but `o(W)` protected targets if the capped orbit-mass floor and the
total inter-fibre collision ledger both sum to `o(W)` over the protected
depths.

#### Proof

Bonferroni gives

\[
 \left|\bigcup_FP_F\right|
 \ge\sum_F|P_F|-\sum_{F<F'}|P_F\cap P_{F'}|
 =G_O-J_O.
\]

If `G_O<=p`, rearrangement proves (8.3).  If `G_O>p`, the same inequality,
or simply counting all repeated phase incidences, gives
`J_O>=G_O-|union P_F|>=p-|union P_F|`, which is (8.3) because the first
term on its right is zero.  Summation over target orbits and depths proves
the final assertion. \(\square\)

Thus the surviving lift problem has three sharply separated clauses:

1. intra-fibre rainbowness -- solved for `4^r<p` by Lemma 8.1;
2. inter-fibre collisions -- the explicit nonnegative ledger `sum J_O`;
3. exact middle ownership -- the phase-free partition equations (or an
   equivalent positive wreath-trade realization).

## 9. The phase-free rainbow-kernel obstruction

Lemma 8.1 does not merely leave middle legality unchecked.  Legality has
an exact first obstruction which a binary hash cannot be repaired around
by component phases.

Fix the prime cycle `sigma`.  For a middle necklace `O` and factor row
`C`, let

\[
                         B_\sigma(O,C)=|P_{C,O}|
\tag{9.1}
\]

be the row--necklace multiplicity matrix.  Its bipartite support graph is
the quotient graph `Q_sigma(F)`.  Call a vector `c` **component-constant**
if it is constant on the row shore of every connected component of this
graph.

### Theorem 9.1 (binary-hash legality gate)

Let `e(C) in F_p` be any middle-admissible exponent assignment.

1. One necessarily has

   \[
                            \boxed{B_\sigma e=0
                            \quad\text{over }\mathbb F_p.}
   \tag{9.2}
   \]

2. For every component-constant vector `c`,

   \[
             \boxed{e\text{ is middle-admissible}
             \iff e+c\text{ is middle-admissible}.}
   \tag{9.3}
   \]

   In particular, component phases cannot repair a failure of (9.2), or
   any higher exact partition equation.

3. If a quotient component `K` has `b_K` rows and

   \[
             \operatorname{rank}_{\mathbb F_p}B_\sigma[K]=b_K-1,
   \tag{9.4}
   \]

   then every middle-admissible exponent assignment is constant on `K`.
   Consequently no canonical marked fibre containing two rows of `K` can
   be internally rainbow under any legal row-power lift.

#### Proof

For one necklace, exact ownership before and after shifting gives equality
of every power sum on `F_p`.  The linear power sum is exactly (9.2); this
is also the first cyclotomic derivative of the nonzero-frequency Fourier
equation.

Every necklace belongs to one quotient component.  Adding the common
value `c_K` to all its adjacent row exponents translates the entire
post-shift multiset in that necklace by `c_K`.  Being a permutation of
`F_p` is invariant under a common translation.  This proves (9.3), in
both directions.

Under (9.4), equation (9.2) makes `e` constant on `K`.  Equivalently one
may apply the `p`-rank rigidity theorem.  Two rows in the same component
therefore receive the same phase and cannot be rainbow. \(\square\)

For the particular label in Lemma 8.1, write

\[
                         h(C(x))=a_2(x).
\tag{9.5}
\]

The theorem gives the immediate necessary condition

\[
                         \boxed{B_\sigma h=0.}
\tag{9.6}
\]

Thus replacing `h` by `h+c` for arbitrary component phases never helps:
the derivative (9.6) is unchanged, and (9.3) says the full legality status
is unchanged as well.

There is a useful phase-free formulation for any desired family of
serviced fibres.  Let `mathscr P` be the set of row pairs which occur
together in one such fibre and put

\[
 H_{CD}=\{z:z_C=z_D\}\subseteq\mathbb F_p^F.
\tag{9.7}
\]

### Corollary 9.2 (rainbow-kernel gate)

A necessary condition for a phase-free legal rainbow assignment is

\[
 \boxed{
 \ker_{\mathbb F_p}B_\sigma
 \not\subseteq
 \bigcup_{\{C,D\}\in\mathscr P}H_{CD}.}
\tag{9.8}
\]

For the literal binary hash, the stronger point condition is

\[
 h\in\ker B_\sigma\setminus
 \bigcup_{\{C,D\}\in\mathscr P}H_{CD}.
\tag{9.9}
\]

In particular, if all quotient components are `p`-rank rigid, every
serviced fibre must meet each component in at most one row.

#### Proof

Equation (9.2) places every legal assignment in the displayed kernel.
Rainbowness says that it avoids every equality hyperplane belonging to a
pair in the same fibre.  Lemma 8.1 supplies that avoidance for `h` when
`4^r<p`.  The final assertion is Theorem 9.1(3). \(\square\)

Condition (9.8) is only the first derivative; higher phase moments may
still exclude every vector that survives it.  It nevertheless shows that
the legal-lift issue is not an inter-fibre collision estimate.  Before
Bonferroni can be used, one needs a root-valued Fourier-kernel vector whose
restriction avoids a prescribed family of equality hyperplanes.

There is an exact pairwise test for the phase-free gate.  Write `u_C` for
the coordinate unit vector at row `C`.

### Lemma 9.3 (row-space obstruction and the sub-`p` union criterion)

For two rows `C,D`, the following are equivalent.

1. Every vector in `ker_(F_p)B_sigma` has `z_C=z_D`.
2. `u_C-u_D` belongs to the row space of `B_sigma`.

Consequently, if `|mathscr P|<p` and no difference `u_C-u_D` for
`{C,D} in mathscr P` belongs to the row space, then there is a vector

\[
 z\in\ker B_\sigma\setminus
 \bigcup_{\{C,D\}\in\mathscr P}H_{CD}.
\tag{9.10a}
\]

#### Proof

The annihilator of `ker B_sigma` under the standard pairing is the row
space of `B_sigma`, proving the equivalence.  Under the stated pairwise
condition, every `H_(CD) cap ker B_sigma` is a proper hyperplane of the
kernel and hence contains exactly a `1/p` fraction of it.  Fewer than `p`
such hyperplanes cannot cover the kernel. \(\square\)

This criterion is phase-free only: the vector in (9.10a) need not satisfy
the nonlinear root-of-unity partition equations.  It does identify a
checkable obstruction stronger than component membership.  For a single
small fibre with `binom(d,2)<p`, derivative-level rainbow feasibility is
equivalent to the absence of the displayed row-space obstruction on each
of its pairs.

For a semilength-`r` Catalan fibre, `d=Cat_r<4^r`.  Hence the elementary
hyperplane argument reaches the range

\[
                         \boxed{16^r<2p,}
\tag{9.10b}
\]

roughly `r<(1/4)log_2 p`, provided every row pair is individually
separable by the kernel.  Lemma 8.1 itself reaches twice that logarithmic
range.  The gap is real: beyond (9.10b), avoiding the equality
hyperplanes requires a structured kernel vector such as the literal hash,
not a union bound inside `ker B_sigma`.

The separation can be quantified exactly over coordinate cycles.  Let
`T=|F|`, let

\[
 n_t=|\{C:h(C)=t\}|,
\qquad
 v_\xi(h)_C=\zeta^{\xi h(C)},
\tag{9.10}
\]

and let `M_(sigma,xi)` be the Fourier signature matrix of the prime-cycle
rigidity theorem.

### Theorem 9.4 (mean Fourier defect of a fixed hash)

For every fixed exponent label `h:F->F_p`,

\[
 \boxed{
 \mathbb E_\sigma\sum_{\xi=1}^{p-1}
 \|M_{\sigma,\xi}v_\xi(h)\|_2^2
 =p^2\left(T-{1\over T}\sum_{t\in\mathbb F_p}n_t^2\right).}
\tag{9.11}
\]

The right side vanishes exactly when `h` is constant.  If one serviced
fibre already contains `d` rows with distinct hash values, then

\[
 \mathbb E_\sigma\sum_{\xi\ne0}
 \|M_{\sigma,\xi}v_\xi(h)\|_2^2
 \ge p^2{(d-1)(2T-d)\over T}.
\tag{9.12}
\]

#### Proof

The exact mean Gram identity gives, for each nonzero `xi`,

\[
 \mathbb E_\sigma\|M_{\sigma,\xi}v_\xi(h)\|_2^2
 =p\left(T-{1\over T}
 \left|\sum_C\zeta^{\xi h(C)}\right|^2\right).
\tag{9.13}
\]

Character orthogonality gives

\[
 \sum_{\xi=1}^{p-1}
 \left|\sum_C\zeta^{\xi h(C)}\right|^2
 =p\sum_tn_t^2-T^2.
\]

Substitution proves (9.11).  Subject to at least `d` nonempty hash
classes, `sum_t n_t^2` is maximized by the profile
`(T-d+1,1,...,1)`.  This gives (9.12). \(\square\)

Equation (9.11) is not a nonexistence theorem: an exceptional cycle may
still put the fixed hash in every Fourier kernel.  It does prove that the
universal context-rainbow property supplies no average middle legality.
For a nonconstant hash, exact legality is a cycle-dependent zero of a
strictly positive averaged defect.  A successful construction must
therefore prove (9.9) and all higher moment equations for one specially
correlated cycle, or replace the literal hash by a genuinely nonconstant
vector in the legal kernel while preserving the fibre inequalities.

The full middle condition also has a direct collision form, which makes
clear why ordinary hash injectivity is not the right local property.

### Proposition 9.5 (exact middle gain-avoidance ledger)

For an exponent vector `e`, define

\[
 \Lambda_O^{\rm mid}(e)=
 \sum_{C<D}
 |(P_{C,O}+e(C))\cap(P_{D,O}+e(D))|,
\qquad
 \Lambda^{\rm mid}(e)=\sum_O\Lambda_O^{\rm mid}(e).
\tag{9.14}
\]

Then

\[
 \boxed{e\text{ is middle-admissible}
 \iff \Lambda^{\rm mid}(e)=0.}
\tag{9.15}
\]

More precisely, if

\[
 h_O(t)=\sum_C\mathbf1_{P_{C,O}+e(C)}(t),
\]

then

\[
 \boxed{
 \sum_t(h_O(t)-1)^2=2\Lambda_O^{\rm mid}(e).}
\tag{9.16}
\]

Equivalently, for every two rows incident with `O`, legality requires

\[
 \boxed{
 e(D)-e(C)\notin P_{C,O}-P_{D,O}.}
\tag{9.17}
\]

On the transversal core, write `P_(C,O)={phi_O(C)}`.  Condition (9.17)
becomes the one-forbidden-gain rule

\[
 \boxed{
 e(C)-e(D)\ne\phi_O(D)-\phi_O(C).}
\tag{9.18}
\]

#### Proof

Every shifted signature family has total mass `p`.  Pairwise disjointness
is therefore equivalent to being a partition of `F_p`, which proves
(9.15) and (9.17).  Also

\[
 \sum_t\binom{h_O(t)}2=\Lambda_O^{\rm mid}(e).
\]

Using `sum_t h_O(t)=p` gives

\[
 \sum_t(h_O(t)-1)^2
 =\sum_th_O(t)^2-p
 =2\sum_t\binom{h_O(t)}2,
\]

which is (9.16).  The singleton specialization is immediate. \(\square\)

If `a=|P_(C,O)|` and `b=|P_(D,O)|`, Cauchy--Davenport gives

\[
 |P_{C,O}-P_{D,O}|\ge\min(p,a+b-1).
\tag{9.19}
\]

Hence a legal phase difference for this row pair has at most

\[
                         p-a-b+1
\tag{9.20}
\]

possible values when `a+b<=p`.  The original difference zero is one of
them because the old signatures are disjoint.  Thus high-mass signature
pairs force almost equal phases; in the two-piece case `a+b=p`, zero is
the only allowed difference, recovering two-phase rigidity locally.

For the literal binary hash, Lemma 8.1 controls differences of hashes on
rows in one **lower-shadow fibre**.  Proposition 9.5 instead forbids
specific differences on pairs meeting one **middle necklace**.  These are
different incidence graphs.  Hash injectivity only rules out difference
zero; on a transversal necklace the forbidden difference in (9.18) is
nonzero.  Therefore the exact additional target is

\[
                         \boxed{\Lambda^{\rm mid}(a_2)=0,}
\tag{9.21}
\]

while Lemma 8.2 asks that the lower-shadow collision ledger `sum J_O` be
small.  A successful phase assignment must make the first collision
ledger exactly zero and the second asymptotically small with the same row
differences.

Combining (9.16) with Fourier Parseval and Theorem 9.4 gives an exact
average for the first ledger.

### Corollary 9.6 (mean middle-collision count of the hash)

For every fixed exponent label `h`,

\[
 \boxed{
 \mathbb E_\sigma\Lambda^{\rm mid}(h)
 ={p\over2}\left(T-{1\over T}\sum_tn_t^2\right).}
\tag{9.22}
\]

In particular, if the hash classes are asymptotically equidistributed,
the expected number of colliding shifted row pairs at middle targets is
`(1/2+o(1))W`.

#### Proof

The exact Fourier defect identity is

\[
 \sum_{\xi\ne0}\|M_{\sigma,\xi}v_\xi(h)\|_2^2
 =p\sum_{O,t}(h_O(t)-1)^2
 =2p\Lambda^{\rm mid}(h).
\]

Take expectations and use (9.11). \(\square\)

Again, (9.22) does not rule out a specially correlated zero-collision
cycle.  It does rule out treating the binary hash as approximately legal:
at a generic cycle its exact-middle defect is linear, even though its
small-subtree lower-shadow fibres are perfectly rainbow.

## 10. Exact-factor overlays which genuinely change source fibres

Row powers preserve the canonical source fibres.  To change them while
retaining middle legality, start with two genuinely different exact factors
`F,G`.  Their ownership overlay is the bipartite multigraph whose shores
are the rows of `F` and `G`, with one edge for every middle target joining
its two owners.  Every vertex has degree `p`.  In each connected component
`C`, the two row packets have equal size and cover the same middle support.
Consequently, replacing the `F` packet by the `G` packet on any collection
of components produces another exact factor.

At depth `q`, let `u_(q,C)` and `v_(q,C)` be the target histograms of the
two packets and put `d_(q,C)=v_(q,C)-u_(q,C)`.  Switching a component set
`I` gives the exact simultaneous load formula

\[
 \boxed{
 \mu_q^{F_I}=\mu_q^F+\sum_{C\in I}d_{q,C}.}                 \tag{10.1}
\]

The same `I` occurs at every depth, so (10.1) is automatically a legal
multidepth operation.

### Proposition 10.1 (exact cap-tail potential)

Define

\[
 K_q(H)=\sum_S(\mu_q^H(S)-p)_+,
 \qquad
 \Gamma_q(H)=\sum_S\min\{\mu_q^H(S),p\}.                   \tag{10.2}
\]

Then, for every component choice `I`,

\[
\boxed{
\begin{split}
 K_q(F_I)-K_q(F)
 &=\sum_S\left[
 \left(\mu_q^F(S)+\sum_{C\in I}d_{q,C}(S)-p\right)_+
                 -(\mu_q^F(S)-p)_+\right]\\
 &=-\bigl(\Gamma_q(F_I)-\Gamma_q(F)\bigr).
\end{split}}                                                \tag{10.3}
\]

Equivalently,

\[
 K_q(F_I)=\sum_{t\ge p+1}
             |\{S:\mu_q^{F_I}(S)\ge t\}|.                 \tag{10.4}
\]

The identities remain exact after arbitrary nonnegative depth weights are
applied and summed.

#### Proof

Equation (10.1) gives the first line.  Every exact factor has total
depth-`q` mass `W`, and pointwise
`(x-p)_+=x-min(x,p)`.  This proves the second line.  The integer
layer-cake identity proves (10.4). \(\square\)

Thus cap-tail descent is exactly capped-coverage gain.  No quadratic
surrogate is needed.

### Proposition 10.2 (statewise common-core obstruction)

Put

\[
                     c_q(S)=\sum_C
                       \min\{u_{q,C}(S),v_{q,C}(S)\}.       \tag{10.5}
\]

Every switch child satisfies `mu_q^(F_I)(S)>=c_q(S)`, and hence

\[
 \boxed{
                 \min_IK_q(F_I)
                 \ge\sum_S(c_q(S)-p)_+.}                   \tag{10.6}
\]

In particular, a source plateau contained in one overlay component cannot
be repaired if both component states retain more than `p` occurrences at
its target.  Fragmentation into many components is likewise ineffective
when the two states share the same high common core componentwise.

#### Proof

Component `C` contributes either `u_(q,C)(S)` or `v_(q,C)(S)`, and hence
at least their minimum.  Sum over components and use monotonicity of the
cap-tail function. \(\square\)

If the ownership overlay is connected, it has only one switch component
and hence only the two children `F,G`.  In that case

\[
                         \min_IK_q(F_I)=\min\{K_q(F),K_q(G)\}. 
                                                                  \tag{10.6a}
\]

Thus a connected overlay supplies no source-fibre mixing at all.

### Theorem 10.3 (two-seed anti-plateau criterion)

Choose every ownership component independently from its `F`- or `G`-state
with probability `1/2`.  Set

\[
 \bar\mu_q(S)={\mu_q^F(S)+\mu_q^G(S)\over2},
 \qquad
 V_q(S)={1\over4}\sum_Cd_{q,C}(S)^2.                        \tag{10.7}
\]

Then

\[
 \boxed{
 \mathbb E_IK_q(F_I)
 \le\sum_S(\bar\mu_q(S)-p)_+
       +{1\over2}\sum_S\sqrt{V_q(S)}.}                    \tag{10.8}
\]

A margin-sensitive version is

\[
\boxed{
\begin{split}
 \mathbb E_IK_q(F_I)
 \le{}&\sum_S(\bar\mu_q(S)-p)_+\\
 &+{1\over2}\sum_{S:\bar\mu_q(S)>p/2}\sqrt{V_q(S)}
 +{1\over2p}\sum_{S:\bar\mu_q(S)\le p/2}V_q(S).
\end{split}}                                                \tag{10.9}
\]

Consequently, for arbitrary nonnegative weights `omega_q`, some exact
switch child has `sum_q omega_q K_q(F_I)=o(W)` whenever the corresponding
weighted sum of the right side of (10.8), or (10.9), is `o(W)`.

#### Proof

Write the component choices as independent signs `epsilon_C`.  Then

\[
 \mu_q^{F_I}(S)=\bar\mu_q(S)+Y_q(S),
 \qquad
 Y_q(S)={1\over2}\sum_C\epsilon_Cd_{q,C}(S).               \tag{10.10}
\]

This random variable is symmetric, has mean zero, and variance `V_q(S)`.
Thus

\[
 \mathbb E(Y_q(S))_+
 ={1\over2}\mathbb E|Y_q(S)|
 \le{1\over2}\sqrt{V_q(S)}.
\]

Together with `(a+y)_+<=a_++y_+`, this proves (10.8).  If
`bar(mu)_q(S)<=p/2`, put `gamma=p-bar(mu)_q(S)>=p/2` and use

\[
                    (y-\gamma)_+\le{y^2\over4\gamma}
                                      \le{y^2\over2p}.
\]

This proves (10.9).  Expectation commutes with the weighted depth sum, so
one legal component choice is no worse than its expectation. \(\square\)

The two terms in (10.8) express the required anti-plateau theorem exactly:
the seed average must move plateaus to different targets, and each target
imbalance must be fragmented among sufficiently many small overlay
components.  Exactness of `F,G` alone implies neither condition;
Proposition 10.2 is the opposite statewise possibility.

## 11. Multi-seed component systems

Suppose more generally that every ownership component `C` has `L`
alternative row packets `R_(C,1),...,R_(C,L)`, all covering the same
middle support, and that choosing one packet independently in every
component always gives an exact factor.  Let `u_(q,C,l)` be the depth-`q`
histogram and define

\[
\begin{split}
 \bar u_{q,C}&={1\over L}\sum_{\ell=1}^Lu_{q,C,\ell},\\
 \bar\mu_q&=\sum_C\bar u_{q,C},\\
 V_q(S)&=\sum_C{1\over L}\sum_{\ell=1}^L
     (u_{q,C,\ell}(S)-\bar u_{q,C}(S))^2.
\end{split}                                                 \tag{11.1}
\]

Uniform independent component states satisfy

\[
 \boxed{
 \mathbb E K_q
 \le\sum_S(\bar\mu_q(S)-p)_++\sum_S\sqrt{V_q(S)}.}         \tag{11.2}
\]

On targets with `bar(mu)_q(S)<=p-gamma_q(S)`, their contribution improves
to `V_q(S)/(4 gamma_q(S))`.  Conversely, the exact multi-state common core

\[
 c_q^{(L)}(S)=\sum_C\min_{1\le\ell\le L}u_{q,C,\ell}(S)     \tag{11.3}
\]

forces

\[
 \boxed{
                         K_q\ge\sum_S(c_q^{(L)}(S)-p)_+.}   \tag{11.4}
\]

Thus extra seeds help only when their component states genuinely move the
source fibres.  Coordinate copies of one unchanged source leave (11.3)
large.  For arbitrary exact seeds a canonical common multiway component
decomposition is in fact automatic; the additional issue is whether its
components are small.  The exact construction and the full state space are
given next.

## 12. The exact multi-seed switching complex

Let `U` be the middle layer, `|U|=W`, and let

\[
                    F_1,\ldots,F_L
\tag{12.1}
\]

be exact factors, regarded as partitions of `U` into `T=W/p` rows of
size `p`.  Equal geometric rows occurring in two seeds are tagged by their
seed; this changes none of the exact-cover equations.

Construct the **ownership hypergraph** `O(F_1,...,F_L)` as follows.  Its
vertices are the tagged rows in the disjoint union of the `F_l`.  For every
middle target `x in U`, put one `L`-edge

\[
 e_x=\{R_1(x),\ldots,R_L(x)\},
\tag{12.2}
\]

where `R_l(x)` is the unique row of `F_l` which owns `x`.  This is an
`L`-partite, `L`-uniform, `p`-regular multihypergraph.  Repeated edges are
kept, since they represent different middle targets.

### Theorem 12.1 (balanced-component normal form)

Let `C` range over the connected components of the ownership hypergraph,
and let `U_C` be the middle targets whose edges lie in `C`.  Then:

1. `U_C` is a union of rows of every `F_l`.  Moreover
   
   \[
       |U_C|=p b_C,\qquad
       |V(C)\cap F_l|=b_C
       \quad(1\le l\le L) .                              \tag{12.3}
   \]

2. The sets `U_C` are exactly the minimal nonempty subsets of `U` which
   are unions of rows in every seed.  Equivalently, they are the blocks of
   the join of the `L` partition equivalence relations.

3. Put
   
   \[
    X_C=\left\{z\in\{0,1\}^{V(C)}:
         \sum_{R\ni x}z_R=1\quad(x\in U_C)\right\}.       \tag{12.4}
   \]
   
   The complete set of exact factors using rows from the tagged catalogue
   `F_1 union ... union F_L` is the Cartesian product
   
   \[
                         \boxed{X=\prod_C X_C.}            \tag{12.5}
   \]
   Every state in `X_C` uses exactly `b_C` rows.  Equivalently, it is a
   perfect matching of the local `p`-uniform row hypergraph on `U_C`, or
   an independent set of size `b_C` in the local row-intersection graph.

4. For every `l`, selecting the whole packet `V(C) cap F_l` is an element
   of `X_C`.  Consequently every collection of exact seeds automatically
   contains the legal canonical switching cube
   
   \[
                         [L]^{\{C\}}\subseteq X:           \tag{12.6}
   \]
   independently choose one seed packet on every ownership component.

#### Proof

Every tagged row has its `p` incident target-edges in one ownership
component.  Conversely, every target-edge in that component has one owner
from each seed in the same component.  Hence the `F_l`-rows in `C`
partition `U_C`; double counting their incidences proves (12.3).

Two middle targets are connected precisely when one can pass between them
through a sequence in which consecutive targets lie in a common row of
one of the seeds.  This is exactly the equivalence relation generated by
the `L` partition relations, proving part 2.

A row selection covers every middle target exactly once precisely when it
satisfies (12.4).  No row crosses two sets `U_C`, so these equations split
as the Cartesian product (12.5).  Summing the equations in one component
gives

\[
 p\sum_{R\in V(C)}z_R=|U_C|=pb_C,
\]

so every local state uses `b_C` rows.  Pairwise disjointness of `b_C`
local rows is equivalent to covering their `pb_C=|U_C|` targets, proving
the matching and intersection-graph descriptions.  Finally, the packet
from any one seed partitions `U_C`, proving (12.6). \(\square\)

The full local state space `X_C` may be strictly larger than the `L`
canonical colour states.  In particular, unlike the two-seed case,
connectedness does not imply rigidity when `L>=3`: a connected union of
three one-factorizations may have additional perfect matchings.  Thus
(12.5), rather than merely (12.6), is the exact characterization.

### Corollary 12.2 (fragmentation is a common block-system condition)

Let `k_L` be the number of canonical cube coordinates and
`b=max_C b_C`.  Then

\[
                         k_L\ge {T\over b}.                \tag{12.7}
\]

Adding another seed can only merge ownership components.  Consequently
`k_(L+1)<=k_L`, and the largest balance parameter `b_C` can only increase.
In particular, many canonical independent switches exist if and only if
all seeds preserve a common partition of the middle layer into many small
balanced supports.

#### Proof

The components partition each seed's `T` rows, so `sum_C b_C=T`, proving
(12.7).  Adding a seed adds generators to the join of the partition
relations and therefore coarsens its block partition. \(\square\)

This is an exact tension specific to the multi-seed proposal: more seeds
can disperse the average lower load, but they never create more canonical
switch coordinates.  Unless the new seed is aligned with the existing
common block system, it merges them.

There is a second, opposite tension.  A component with `b_C=1` is
geometrically frozen: every seed packet is the same middle row `U_C`
(with only its tag changed), so all of its lower histograms agree.  More
generally a component moves anything only if its local row hypergraph has
at least two distinct perfect matchings.  Thus every nontrivial small atom
required below is exactly a small multiway wreath trade.  Small atoms give
low variance, but singleton atoms give zero useful variance.

### Theorem 12.3 (small-atom anti-plateau theorem)

At every depth `q`, assume that one row contributes `p` distinct targets.
For component `C` and seed `l`, let `u_(q,C,l)` be its lower-target
histogram, as in Section 11.  Choose one seed packet independently and
uniformly on each ownership component, and let `F_*` be the resulting
exact factor.

Suppose `b_C<=b` for every component and, for numbers `alpha_q>0`,

\[
 \bar\mu_q(S)={1\over L}\sum_{l=1}^L\mu_q^{F_l}(S)
                  \le (1-\alpha_q)p
 \qquad\hbox{for every target }S.                         \tag{12.8}
\]

Then, for arbitrary nonnegative depth weights `omega_q`, some canonical
switch child satisfies

\[
 \boxed{
 \sum_q\omega_q K_q(F_*)
 \le {1\over4}\left(\sum_Cb_C^2\right)
                    \sum_q{\omega_q\over\alpha_q}
 \le {bW\over4p}\sum_q{\omega_q\over\alpha_q}.}          \tag{12.9}
\]

In particular, if

\[
                    b\sum_q{\omega_q\over\alpha_q}=o(p), \tag{12.10}
\]

then the weighted cap tail is `o(W)` in one exact integral factor.

Equivalently, (12.9) may be used as a direct construction theorem without
first naming global seeds.  Partition a base factor into disjoint packets
of at most `b` rows; on the middle support of every packet supply `L`
alternative wreath partitions, and require their aggregate lower-load
mean to satisfy (12.8).  Independent choice of one local partition is an
exact factor and obeys (12.9).  Thus the concrete structural target is a
packing of many disjoint, small, mean-dispersing **multiway wreath
trades**.

#### Proof

For a fixed lower target `S`, write

\[
 X_S=\mu_q^{F_*}(S)=\bar\mu_q(S)+Y_S,\qquad
 \mathbb EY_S=0.
\]

Independence across ownership components gives

\[
 \operatorname {Var}Y_S
 =V_q(S)=\sum_C {1\over L}\sum_l
       (u_{q,C,l}(S)-\bar u_{q,C}(S))^2.                  \tag{12.11}
\]

Equivalently, the variance is the average pairwise packet separation,

\[
 V_q(S)={1\over2L^2}\sum_C\sum_{l,l'}
             (u_{q,C,l}(S)-u_{q,C,l'}(S))^2.              \tag{12.11a}
\]

Put `gamma_S=p-bar(mu)_q(S)>=alpha_q p`.  The scalar inequality

\[
                         (y-\gamma)_+\le {y^2\over4\gamma}
\tag{12.12}
\]

therefore yields

\[
                 \mathbb E(X_S-p)_+
                 \le {V_q(S)\over4\alpha_qp}.            \tag{12.13}
\]

Now `0<=u_(q,C,l)(S)<=b_C`, while
`sum_S u_(q,C,l)(S)=pb_C`.  Hence

\[
\begin{split}
 \,\sum_SV_q(S)
 &\le\sum_C{1\over L}\sum_l\sum_Su_{q,C,l}(S)^2\\
 &\le\sum_C b_C{1\over L}\sum_l\sum_Su_{q,C,l}(S)
  =p\sum_Cb_C^2
  \le pbT=bW .                                           \tag{12.14}
\end{split}
\]

Sum (12.13), then sum over depths with weights.  The expectation obeys
the first bound in (12.9), so at least one exact child does also.  The
second bound follows from `sum_Cb_C=T=W/p`. \(\square\)

Theorem 12.3 isolates a concrete use for three or more seeds.  If a
source plateau of height `p` is concentrated in only a small fraction of
the seeds at each target, their average acquires a fixed margin below
`p`; the only remaining quantitative requirement is that the common join
atoms be `o(p)` after the weighted number of depths is included.

The uniform margin can be replaced by a weaker mean-tail condition.  For
`0<a<p`, put

\[
 D_{q,a}=\{S:\bar\mu_q(S)>p-a\},\qquad
 \bar K_q=\sum_S(\bar\mu_q(S)-p)_+ .                      \tag{12.14a}
\]

The same random canonical child satisfies

\[
 \boxed{
 \mathbb EK_q(F_*)
 \le \bar K_q+{W\over2}\sqrt{b\over p-a}+{bW\over4a}.}  \tag{12.14b}
\]

Indeed, `|D_(q,a)|<=W/(p-a)`.  On this exceptional set use

\[
 \mathbb E(\bar\mu+Y-p)_+
 \le(\bar\mu-p)_++{1\over2}\sqrt{\operatorname {Var}Y},
\]

where the factor `1/2` follows from `EY=0`; off it use (12.12).
Cauchy--Schwarz and (12.14) prove (12.14b).  Taking `a=p/2` gives

\[
 \mathbb EK_q(F_*)
 \le\bar K_q+W\sqrt{b\over2p}+{bW\over2p}.               \tag{12.14c}
\]

Thus at one depth it is enough that the **average seed histogram** have
`o(W)` cap tail and that `b=o(p)`.  Over a weighted family of depths of
total weight `Omega`, the same argument costs
`O(Omega sqrt(b/p) W)`; the fixed-margin theorem (12.9) is sharper by one
power of `Omega` when its hypothesis is available.

### Proposition 12.4 (exact obstructions for all mixed states)

The common-core obstruction can be strengthened from the canonical cube
to the entire catalogue.  Let `A` be the middle-incidence matrix of all
tagged catalogue rows, let `B_q` be the depth-`q` incidence matrix, and
write a legal mixed state as

\[
                  x\in\{0,1\}^{\mathcal R},qquad Ax=\mathbf1,
                  \qquad\mu_q=B_qx.                       \tag{12.15}
\]

For each component define

\[
 \kappa_{q,C}(S)=\min_{x_C\in X_C}(B_{q,C}x_C)(S).        \tag{12.16}
\]

Then every legal mixed factor, including every noncanonical local state,
satisfies

\[
 \boxed{
 K_q\ge\sum_S\left(\sum_C\kappa_{q,C}(S)-p\right)_+.}   \tag{12.17}
\]

There is also an exact linear-invariant certificate.  If vectors `eta,y`
satisfy

\[
       0\le\eta\le\mathbf1,qquad B_q^T\eta=A^Ty,         \tag{12.18}
\]

then every legal mixed state obeys

\[
 \boxed{
 K_q(B_qx)\ge
       \langle y,\mathbf1\rangle-p\langle\eta,\mathbf1\rangle.}
                                                                  \tag{12.19}
\]

Thus a positive right side is a statewise obstruction which no number of
seeds, no component randomization, and no noncanonical local perfect
matching can remove.  Moreover (12.18), without the inequalities on
`eta`, characterizes all linear functionals of the lower load which are
constant on the affine middle fibre `Ax=mathbf1`.

#### Proof

Every global state restricts to some `x_C in X_C`, so its contribution at
`S` is at least (12.16).  This proves (12.17).

For (12.19), the cap-tail dual inequality gives, for every
`0<=eta<=1`,

\[
 K_q(B_qx)=\sum_S((B_qx)_S-p)_+
 \ge\langle\eta,B_qx-p\mathbf1\rangle.
\]

Under (12.18) this equals

\[
 \langle y,Ax\rangle-p\langle\eta,\mathbf1\rangle
 =\langle y,\mathbf1\rangle-p\langle\eta,\mathbf1\rangle.
\]

Finally, a functional `eta^TB_qx` is constant on `Ax=mathbf1` exactly
when `B_q^Teta` annihilates `ker A`, equivalently when it belongs to
`(ker A)^perp=rowspan(A^T)`. \(\square\)

Proposition 12.4 is the exact statewise audit required before searching
for a favorable family of seeds: the variance criterion can only exploit
directions in `B_q ker A`; every componentwise forced core and every
row-space invariant survives the whole multi-seed switching complex.

There is also an integral obstruction invisible to real variance.  Fix
one legal state `x_0` and put

\[
 \Lambda_q=B_q\{z\in\mathbb Z^{\mathcal R}:Az=0\}
              \subseteq\mathbb Z^{N_q}.                  \tag{12.20}
\]

Every legal lower load lies in the single lattice coset

\[
                         \boxed{B_qx_0+\Lambda_q.}         \tag{12.21}
\]

Thus, if this coset is disjoint from the cap-safe load region, cap repair
is impossible even when the real common core and every real row-space
certificate vanish.  Equivalently, for any modulus `d`, integer vectors
`eta,y` satisfying

\[
                       B_q^T\eta\equiv A^Ty\pmod d        \tag{12.22}
\]

give the statewise congruence

\[
                   \langle\eta,B_qx\rangle
                   \equiv\langle y,\mathbf1\rangle\pmod d. \tag{12.23}
\]

These integral invariants, and whether a desired balanced load meets the
coset, are determined exactly by the Smith normal form of the middle
incidence lattice.  They are the multi-seed analogue of the parity
obstructions encountered by local selector trades.

## 13. Correct specification for a replacement seed

The cap-tail theorem isolates a useful seed statistic, but it must not be
overstated.  The exact necessary quantity is `PCap_H(F)` from (2.16), not
the pointwise demand `K_q(F)=0`.  Moreover a good cap tail removes only the
phase-capacity obstruction; it does not supply a legal phase assignment or
lower-shadow coverage.

Let `D_m` be the `Cat_m` Dyck roots.  A proposed twisted construction is a
map

\[
                         c^*:D_m\longrightarrow
                         \operatorname{Cyc}([p]).          \tag{13.1}
\]

It is an exact middle factor if and only if

\[
 \boxed{
 \sum_{x\in D_m}\sum_{j\in\mathbb Z_p}
 \mathbf1_{\{I_{c^*(x)}(j,m)=S\}}=1
 \quad\text{for every }S\in\binom{[p]}m.}                 \tag{13.2}
\]

This is the load-bearing condition.  Injectivity of `x -> c^*(x)` does
not imply (13.2): two distinct cyclic orders may share middle windows,
while other middle sets remain uncovered.

The binary label (8.1) supplies only `p` values and separates a subtree
fibre only in the range `4^r<p`.  The phase-capacity obstruction in
Theorem 2.5 deliberately chooses `r` with `Cat_r>=4p`, outside that range.
Consequently a `nu`-dependent interleaving can evade the no-go only if it
moves different fillings through **different target orbits**, rather than
merely assigning the `p` cyclic phases of one old target.  Even complete
separation of every one-hole fibre would not by itself bound mergers of
unrelated contexts.

The precise post-MSW construction package is therefore:

1. prove the exact-cover equations (13.2);
2. prove `PCap_H(F^*)=o(W)` for the resulting seed;
3. prove a relaxed target-orbit floor of `o(W)` for one common coordinate
   cycle (or obtain direct lower-shadow coverage);
4. realize that floor by an exact-middle legal assignment, equivalently
   make the middle collision ledger (9.14) zero while the lower-shadow
   ledger (8.3) is `o(W)`.

Clauses 2--4 may be bypassed if the seed itself already has `o(W)` total
missing targets.  Otherwise all are genuinely additional to the absence
of excursion blindness.  This is narrower than the original problem, but
it is not a single local-injectivity lemma.

The `m=4` balanced certificate does satisfy the proposed zero-cap test,
but this gives no evidence for the asymptotic seed problem.  Here `p=9`
and `p^(1/4)<2`, so the test sees only `q=1`.  At depth one every exact
factor satisfies

\[
                         \mu_1(R)\le\left\lfloor{m+2\over2}\right\rfloor<p:
\]

in the Johnson-graph normal form, the factor edges inside the extension
clique `K_R` form a matching.  Hence `K_1(F)=0` for **every** factor, not
only for the balanced fourteen-row certificate.  The first informative
finite test must reach a depth at which loads can exceed `p`.

More generally, simplicity of the endpoint-fan `q`-graph gives the
universal pointwise bound

\[
             (q+1)\mu_q(R)\le\binom{m+q+1}{q}.             \tag{13.3}
\]

Thus the first prime case in which the window `q<=p^(1/4)` even permits a
cap violation is `m=8,p=17,q=2`: the right side of (13.3), divided by
three, is `55/3>17`.  Tests below that dimension cannot discriminate
candidate seeds by phase capacity.

## 13A. Position-dependent MSW switches and the exact local gate

There is a nontrivial exact replacement rule.  In fact a parent-context
switch can split a nested invisible Catalan fibre at every depth.  The
reason this does not contradict Lemma 18.1 of the selector note is that
the switch is closed only at the parent boundary: relative to the nested
hole it imports one parent coordinate.

First record the exact local condition.  Put

\[
                    \Omega=[2m]\mathbin\sqcup\{\infty\}.
\]

Write the part of one minimum odd cycle avoiding `infinity` as

\[
 X_0,X_1,\ldots,X_m,qquad
 X_t\in\binom{[2m]}m,qquad
 X_t\sim_JX_{t+1},qquad
 X_m=\overline{X_0}.                                      \tag{13A.1}
\]

For `0<=t<m`, put

\[
 Y_t=X_t\cup X_{t+1},\qquad
 Z_t=\{\infty\}\cup\bigl([2m]\setminus Y_t\bigr).         \tag{13A.2}
\]

Then

\[
                 X_0,Z_0,X_1,Z_1,\ldots,Z_{m-1},X_m       \tag{13A.3}
\]

is a `C_(2m+1)` in `KG(2m+1,m)`.

### Lemma 13A.1 (the two exact ownership ledgers)

A collection of traces (13A.1) is an exact `C_(2m+1)`-factor if and only
if, as multisets,

\[
 \biguplus_{u}\biguplus_{t=0}^{m}\{X_t(u)\}
       =\binom{[2m]}m,
 \qquad
 \biguplus_{u}\biguplus_{t=0}^{m-1}\{Y_t(u)\}
       =\binom{[2m]}{m+1}.                                \tag{13A.4}
\]

#### Proof

The first equality says that every factor vertex avoiding `infinity` is
owned once.  Complementation in `[2m]` is a bijection from the
`(m+1)`-sets `Y` to the `(m-1)`-sets `[2m]\setminus Y`; adjoining
`infinity` then gives every factor vertex containing `infinity` exactly
once.  Thus the second equality is precisely ownership of those vertices.
Conversely every vertex of (13A.3) is of one of these two types, so an
exact factor forces both equalities. \(\square\)

Consider now a phase slab `a,...,b` in a set `U` of rows, with all other
states fixed.  Let `X'_t(u)` be a proposed replacement and keep the two
boundary states fixed row by row.  Define the two local discrepancies

\[
\begin{aligned}
 \Delta_0(S)
   &=\sum_{u\in U}\sum_{t=a}^{b}
       \left(\mathbf1_{\{X'_t(u)=S\}}-
             \mathbf1_{\{X_t(u)=S\}}\right),\\
 \Delta_\infty(T)
   &=\sum_{u\in U}\sum_{t=a}^{b-1}
       \left(\mathbf1_{\{X'_t(u)\cup X'_{t+1}(u)=T\}}-
             \mathbf1_{\{X_t(u)\cup X_{t+1}(u)=T\}}\right).
                                                               \tag{13A.5}
\end{aligned}
\]

### Theorem 13A.2 (exact local replacement criterion)

The slab replacement extends to an exact factor if and only if

1. every consecutive pair `X'_t(u),X'_(t+1)(u)` is a Johnson edge;
2. `Delta_0(S)=0` for every `m`-set `S`; and
3. `Delta_infinity(T)=0` for every `(m+1)`-set `T`.

For the position-dependent interleaving

\[
                         X'_t(u)=X_t(f_t(u)),               \tag{13A.6}
\]

with `f_a=f_b=id`, condition 2 holds automatically whenever every `f_t`
is a permutation of `U`.  In this phasewise ownership class, the remaining
condition is exactly

\[
 \boxed{
 \biguplus_{t=a}^{b-1}\biguplus_{u\in U}
 \{X_t(f_tu)\cup X_{t+1}(f_{t+1}u)\}
 =
 \biguplus_{t=a}^{b-1}\biguplus_{u\in U}
 \{X_t(u)\cup X_{t+1}(u)\}.}                              \tag{13A.7}
\]

Equality is required only after aggregation over the slab; demanding it
separately at every transition is unnecessarily strong.

#### Proof

The fixed boundary states glue the replacement to the unchanged pieces.
Condition 1 gives legal rows.  Conditions 2 and 3 are exactly the two
multiset equalities of Lemma 13A.1 restricted to the entries which changed,
so they are necessary and sufficient.  If each `f_t` is a permutation,
then the state multiset at phase `t` is merely permuted, proving the last
assertion. \(\square\)

The first useful switch is the semilength-two rectangle.  In the shorthand
`124={1,2,4}`, the two MSW traces are

\[
\begin{array}{c|ccc}
1100&12&14&34\\
1010&13&23&24.
\end{array}                                                \tag{13A.8}
\]

Swapping the two phase-one states gives

\[
                 12,23,34,\qquad 13,14,24.                \tag{13A.9}
\]

All four new adjacencies are Johnson edges, while the adjacent-union
multiset is, before and after,

\[
                         \{123,124,134,234\}.               \tag{13A.10}
\]

Thus (13A.9) is an exact local switch, not merely a middle-state switch.

The same rectangle gives a scalable parent-context trade.  Fix `r>=2`,
put `s=r+1`, and consider the two semilength-`s` Dyck roots

\[
 C_r=1100(10)^{r-1},\qquad E_r=(10)^{r+1}.                 \tag{13A.11}
\]

Let

\[
                         R=\{5,7,\ldots,2s-1\}.
\]

The first three states in their canonical MSW traces are

\[
\begin{array}{c|ccc}
C_r&12R&14R&34R\\
E_r&13R&23R&24R.
\end{array}                                                \tag{13A.12}
\]

Replace only phase one by swapping `14R` and `23R`.  Formula (13A.10),
with the spectator set `R` adjoined, proves (13A.7); all later states and
both endpoints are unchanged.  Hence this is an exact
`C_(2s+1)`-factor trade.  By coordinate relabelling it embeds in any
aligned size-`s` one-hole context of a larger MSW factor.

### Theorem 13A.3 (a parent trade splits every-depth invisible fibre)

For every `r>=2`, the exact size-`r+1` trade (13A.11)--(13A.12) splits an
aligned size-`r` Catalan fibre contained in that parent context.

#### Proof

The rows

\[
                         F_v=10v,\qquad v\in D_r,           \tag{13A.13}
\]

form one size-`r` one-hole context.  In the recursion (14.3) of the
selector note, the block for `v` starts in permutation position three,
so it is aligned.  Its `r` exchanges occupy phases `1,...,s`.  Before the
trade, coordinate `2` is present throughout these states, while the
`2r` coordinates of the child block are all exchanged.  Consequently

\[
                         \bigcap_{t=1}^{s}X_t(F_v)=\{2\}
                         \quad(v\in D_r).                  \tag{13A.14}
\]

The row `E_r` is the member with `v=(10)^r`.  After the switch its phase-one
state is `14R`; from phase two onward its states are unchanged.  Coordinate
`4` is present in every one of those states.  Coordinate `2` is absent at
phase one, coordinate `1` is absent at phase two, every odd coordinate in
`R` is removed later, and every even coordinate at least six is absent at
phase two.  Therefore

\[
                  \bigcap_{t=1}^{s}X'_t(E_r)=\{4\},         \tag{13A.15}
\]

whereas all other rows in (13A.13) retain target `{2}`.  Under an ambient
context, the common exterior set is simply adjoined to both targets.
Thus the invisible fibre is genuinely split inside an exact factor.
\(\square\)

There remains a sharp same-hole no-go which explains the mechanism.

### Proposition 13A.4 (closed substitutions cannot split their own hole)

Let `J` be the `2r` coordinates of a size-`r` hole and `O` the exterior
coordinates fixed throughout its slab.  Suppose every replacement row
keeps its own boundary states

\[
                         O\cup P_u,qquad O\cup(J\setminus P_u),
                         \qquad |P_u|=r,                   \tag{13A.16}
\]

and changes only coordinates of `J` between them.  Then, for every legal
replacement path,

\[
                         \bigcap_t X'_t(u)=O.               \tag{13A.17}
\]

In particular no closed one-hole substitution, even one satisfying the
exact ledgers (13A.5), can split that hole's invisible Catalan fibre.

#### Proof

Every coordinate of `O` remains present.  Each coordinate of `J` is absent
from one of the two complementary boundary states in (13A.16), so none can
belong to the intersection.  This proves (13A.17).  If the slab has exactly
`r` Johnson edges, it is additionally a geodesic: every coordinate of
`P_u` is removed once and every coordinate of `J\setminus P_u` is inserted
once. \(\square\)

Theorem 13A.3 escapes Proposition 13A.4 precisely because it changes the
entrance state of the nested size-`r` hole: coordinate `1` from the parent
is imported and coordinate `2` is displaced.  Thus recursive interleaving
is a viable seed line, but it must use trades one context level above the
fibre being dispersed.  The construction proves that the fibre obstruction
of Theorem 2.3 is not invariant under exact context trades; it does not yet
show that overlapping parent trades can be packed so as to disperse all
large fibres simultaneously.

## 14. The top-level certified MSW trade family is too sparse

The top-level concatenation family in `MSW_MULTIRANK_LOCAL_TRADES.md`
contains `Cat_(m-1)` two-for-two trades.  They are genuine exact-middle
moves, so they are the first natural candidate for implementing a twisted
interleaving.  Their exact all-rank formula, however, makes this particular
family quantitatively too small.  Recursively embedded copies form a
larger family and are treated separately in Section 15.

### Theorem 14.1 (top-level-trade cap-tail no-go)

Let `F'` be obtained from the canonical factor by any support-feasible
simultaneous choice among these top-level trades.  For every
`2<=q<=m-2`,

\[
 \boxed{
 \|\mu_q^{F'}-\mu_q^{F_{MSW}}\|_1
 \le8\operatorname{Cat}_{m-1}=O(W/p).}                   \tag{14.1}
\]

Consequently, uniformly on
`p^(1/4)/8<=q<=p^(1/4)/4`,

\[
 \boxed{
 K_q(F')\ge {cW\over(\log p)^{3/2}},\qquad
 H_q(F')\ge {cW\over(\log p)^{3/2}}.}                    \tag{14.2}
\]

The same lower bound survives every subsequent cyclic row-power lift of
`F'`, up to changing the absolute constant.  Thus neither this top-level
trade cube nor a binary selection of its position-dependent
interleavings can produce the required replacement seed.

#### Proof

At rank `m-q`, the signed histogram of one local trade has eight distinct
entries of magnitude one.  The total number of certified trade occurrences
over all Dyck concatenation boundaries is exactly `Cat_(m-1)`.  The
triangle inequality proves (14.1), whether or not all occurrences can be
selected simultaneously.

The function `x -> (x-p)_+` is one-Lipschitz, so

\[
 |K_q(F')-K_q(F_{MSW})|
 \le\|\mu_q^{F'}-\mu_q^{F_{MSW}}\|_1.
\]

Theorem 2.3 with cutoff `p` gives the canonical lower bound
`cW/(log p)^(3/2)`, while

\[
 {\operatorname{Cat}_{m-1}\over W}
 ={1\over p}{\operatorname{Cat}_{m-1}\over\operatorname{Cat}_m}
 =O(1/p).
\]

This proves the first assertion in (14.2).  Proposition 2.6 with the
identity phase gives
`H_q(F')>=K_q(F')-(W-N_q)`; the last term is `O(W/sqrt p)` on this
window, proving the second.  Applying Proposition 2.6 once more after
arbitrary row powers proves the final assertion. \(\square\)

This result does not exclude nested, larger, or iterated trades.  It says
that a viable `nu`-twist must change `Omega(W/(log p)^(3/2))` lower-rank
occurrences, whereas the top-level concatenation trade family
changes only `O(W/p)` of them at one depth.

There is a corresponding seed-distance statement which applies to every
successful factor, not only to the certified trade cube.

### Corollary 14.2 (any good seed is multidepth-far from canonical MSW)

Let

\[
 I_p=[p^{1/4}/8,p^{1/4}/4]\cap\mathbb Z.
\]

If an exact factor `G` satisfies

\[
                         \sum_{q\in I_p}H_q(G)=o(W),       \tag{14.3}
\]

then

\[
 \boxed{
 \sum_{q\in I_p}
 \|\mu_q^G-\mu_q^{F_{MSW}}\|_1
 \ge {cWp^{1/4}\over(\log p)^{3/2}}.}                    \tag{14.4}
\]

#### Proof

For every factor,

\[
                         K_q(G)\le H_q(G)+(W-N_q),         \tag{14.5}
\]

which is (2.15) with the identity phase rearranged.  On `I_p`, summing the
second term gives `O(Wp^(-1/4))=o(W)`.  Hence (14.3) implies
`sum_(q in I_p)K_q(G)=o(W)`.

The cap-tail potential is one-Lipschitz in histogram `L^1`, while
Theorem 2.3 gives

\[
 K_q(F_{MSW})\ge {cW\over(\log p)^{3/2}}
 \qquad(q\in I_p).
\]

Sum the resulting triangle inequalities over the
`Theta(p^(1/4))` depths. \(\square\)

Thus absence of hereditary blindness is not a perturbative modification
of MSW: in the relevant multidepth metric every successful replacement
seed lies at the explicit distance (14.4).  Any proposed construction
whose total lower-histogram action is smaller is ruled out before its
exact-cover equations are considered.

## 15. A bulk fixed-scale family of nested rectangle trades

Section 13A used one right-comb filling only.  The spectator tail in that
argument may be an arbitrary Dyck root, which changes the count by a
Catalan factor and reaches exactly the scale of the plateau lower bound.

Fix

\[
                  2\le r\le m-2,\qquad s=r+1,
\]

and let `C` be an aligned size-`s` one-hole context.  For every
`R in D_(r-1)`, use the two fillings

\[
                         A_R=1100R,\qquad B_R=1010R.       \tag{15.1}
\]

If the deletion-coordinate set of `R`, shifted past the first four local
coordinates, is `Q_R`, the first three local middle states are

\[
\begin{array}{c|ccc}
A_R&12Q_R&14Q_R&34Q_R\\
B_R&13Q_R&23Q_R&24Q_R.
\end{array}                                                \tag{15.2}
\]

The exterior state of the ambient context is common and is suppressed in
(15.2).  Swap the two phase-one states `14Q_R` and `23Q_R`.

### Theorem 15.1 (exact simultaneous nested family)

For a fixed `r`, all switches (15.1)--(15.2), over every aligned
size-`r+1` context and every `R in D_(r-1)`, can be performed
simultaneously.  The result is an exact `C_(2m+1)`-factor.

The number of elementary switches is exactly

\[
 \boxed{
 T_{m,r}
 =H_{m,r+1}\operatorname{Cat}_{r-1}
 ={1\over2}\binom{2(m-r-1)}{m-r-1}
             \operatorname{Cat}_{r-1}.}                  \tag{15.3}
\]

Moreover these switches retarget `T_(m,r)` distinct marked depth-`r`
occurrences: in each parent context they move the
`Cat_(r-1)` members

\[
                         10(10R),\qquad R\in D_{r-1},      \tag{15.4}
\]

of the nested `Cat_r` fibre from its old target to a different target.

#### Proof

For one `R`, (15.2) is the rectangle (13A.8) with the common spectator
set `Q_R` adjoined.  Its four adjacent-union colours are

\[
               123Q_R,\quad124Q_R,\quad134Q_R,\quad234Q_R,
\]

and the switch merely permutes them.  The middle states are also merely
transposed.  The exact local criterion, Theorem 13A.2, therefore proves
legality and both ownership equations.

For distinct `R` in one context, the two pairs of fillings in (15.1) are
disjoint, so their phase-one transpositions are disjoint.  Now compare two
distinct aligned size-`s` contexts.  If a full Dyck root belongs to both,
the corresponding size-`s` nodes of its ordered recursion tree are
distinct.  Two distinct tree nodes of the same size cannot be nested, so
their permutation blocks, and hence their phase slabs, are disjoint.  A
switch changes only the state one phase after the start of its block and
the two adjacent edges.  Since `s>=3`, even adjacent size-`s` blocks have
disjoint affected edges.  Thus at every global phase the switches are a
product of disjoint row transpositions, and switches sharing a row act in
disjoint slabs.  Their local ownership ledgers consequently add without
interference.  This proves simultaneous exactness.

There are `H_(m,r+1)` aligned parent contexts by (18.3), and each contains
`Cat_(r-1)` row-disjoint switches, proving (15.3).  Inside the parent, the
rows `10v`, `v in D_r`, form the aligned right-child fibre.  The members
with `v=10R` are exactly (15.4).  The proof of Theorem 13A.3, with `Q_R`
in place of the odd spectator set, shows that each selected member loses
the parent coordinate labelled `2` from its common intersection and gains
the coordinate labelled `4`.  Distinct marked parent contexts have
distinct rooted windows, so (15.3) marked occurrences are retargeted.
\(\square\)

### Corollary 15.2 (the family has fatal-scale marked-token mass)

Uniformly for `r^2/m=o(1)`,

\[
 {T_{m,r}\over W}
 ={\operatorname{Cat}_{r-1}\over16\,4^r}
   \exp\!\left(O\!\left({r^2\over m}+{1\over m}\right)\right)
 ={1+o(1)\over64\sqrt\pi\,r^{3/2}}.                      \tag{15.5}
\]

If `r` is minimal with `Cat_r>=4p`, then `r=Theta(log p)` and

\[
                         \boxed{T_{m,r}
                         =\Theta\!\left({W\over(\log p)^{3/2}}\right).}
                                                               \tag{15.6}
\]

Within each parent context the moved fraction is

\[
 {\operatorname{Cat}_{r-1}\over\operatorname{Cat}_r}
 ={r+1\over2(2r-1)}={1\over4}+O(r^{-1}).                  \tag{15.7}
\]

In particular `Cat_(r-1)>p` at the cutoff used in Theorem 2.3.  Thus the
distinguished nested arm of one parent packet moves more than `p` marked
tokens.  This is only raw capacity: the other three arms of every
four-letter trade, and interactions between switches in one row, must be
included before asserting any decrease of the full cap excess.

#### Proof

The binomial ratio used after (18.4), with `r+1` in place of `r`, gives

\[
 {H_{m,r+1}\over W}
 ={1\over4\,4^{r+1}}
   \exp\!\left(O\!\left({r^2\over m}+{1\over m}\right)\right).
\]

Multiply by
`Cat_(r-1)=(1+o(1))4^(r-1)/(sqrt(pi)r^(3/2))` to obtain
(15.5).  The minimal-cutoff bounds `4p<=Cat_r<16p` give (15.6), and the
exact Catalan quotient gives (15.7). \(\square\)

This family is not the `Cat_(m-1)` top-level cube bounded in Theorem 14.1.
It consists of recursively embedded copies at one fixed subtree scale.  At
the fatal scale,

\[
 {T_{m,r}\over\operatorname{Cat}_{m-1}}
                      =\Theta\!\left({p\over r^{3/2}}\right),             \tag{15.8}
\]

so the sparse-cube count does not apply.

The marked intrinsic ledger has a telescoping correction.  In local
coordinates, the `B_R` window on phases `1,...,s` moves from target `2`
to target `4`, while the `A_R` window on the same phases moves from target
`4` to target `3`.  Thus, if

\[
 S_C=O_C\cup\{2\},\qquad U_C=O_C\cup\{3\},
\]

the marked packet change is

\[
 \operatorname{Cat}_{r-1}
       \sum_C\left(e_{U_C}-e_{S_C}\right).                \tag{15.9}
\]

The intermediate target `O_C union {4}` cancels once negatively and once
positively for every `R`.

### Lemma 15.2A (the two boundary Catalan profiles)

Inside one aligned parent context of size `s=r+1`, let the local target
outside the parent block be `O`.  For `1<=j<=s`, put

\[
                         w_j=\operatorname{Cat}_{j-1}
                              \operatorname{Cat}_{s-j}.   \tag{15.9a}
\]

Among the depth-`r` intrinsic windows on phases `1,...,s`, target
`O union {2j}` has multiplicity exactly `w_j`, and every odd local target
has multiplicity zero.  The opposite boundary windows on phases
`0,...,r` give the odd copy: target `O union {2j-1}` has multiplicity
`w_j`.

In particular the canonical loads at local targets `2,3,4` are

\[
                   d=\operatorname{Cat}_r,\qquad
                   e=\operatorname{Cat}_{r-1},\qquad e,  \tag{15.9b}
\]

respectively.  After the complete packet (15.1), these three marked loads
are

\[
                              d-e,\qquad2e,\qquad e.      \tag{15.9c}
\]

#### Proof

Write a parent filling in first-return form `x=1u0v`, with `u` of
semilength `j-1`.  The first entry of its MSW permutation is
`a_0=2j`.  Formula (17.2), with window start one and length `s-1`, selects
only `a_0`; there are `Cat_(j-1)Cat_(s-j)` choices of `u,v`.  This proves
the even profile.

For the start-zero window, (17.2) selects only the last deletion entry
`b_(s-1)`.  Let `L_s(j)` count size-`s` roots whose last permutation entry
is `2j-1`.  If `x=1u0v` and `v` is empty, that last entry is `1`, giving
`L_s(1)=Cat_(s-1)`.  If `v` is nonempty and `u` has semilength `h`, the
last entry is `2h+2` plus the last entry for `v`.  Induction therefore
gives, for `j>=2`,

\[
\begin{aligned}
 L_s(j)
 &=\sum_{h=0}^{j-2}\operatorname{Cat}_h
       L_{s-1-h}(j-h-1)\\
 &=\operatorname{Cat}_{s-j}
       \sum_{h=0}^{j-2}\operatorname{Cat}_h
                           \operatorname{Cat}_{j-2-h}\\
 &=\operatorname{Cat}_{j-1}\operatorname{Cat}_{s-j}=w_j.
\end{aligned}
\]

This proves the odd profile.

For the three values in (15.9b), the rows are explicit.  All `10v`,
`v in D_r`, give target `2`.  The `A_R=1100R` give target `4`.  Finally

\[
                              D_R=101R0,qquad R\in D_{r-1},
\]

give target `3` in the start-zero window: the last entry of
`pi(10(1R0))` is `3`.  The packet changes `A_R:4 -> 3` and
`B_R:2 -> 4`, proving (15.9c). \(\square\)

At the fatal cutoff, `d>=4p` and
`e=d(r+1)/(2(2r-1))>p`, while `d-e>p`.  Hence the marked intrinsic cap
excess on these three targets is exactly invariant:

\[
 \begin{aligned}
 &(d-p)+(e-p)+(e-p)\\
 &\qquad=(d-e-p)+(2e-p)+(e-p).                            \tag{15.9d}
 \end{aligned}
\]

The same conclusion holds in the presence of additional background load,
because the transfer in (15.9) runs between targets which stay strictly
above the cap.  Thus the distinguished intrinsic packet supplies no
cap-tail decrease.  This statement does **not** determine the change of
the full depth-`r` potential: the other three cyclic arms in (15.10) can
decrease, preserve, or increase it, and their canonical loads have not
yet been controlled.

The profile does contain genuinely sub-cap classes.  Standard Catalan
bounds give

\[
 {w_j\over\operatorname{Cat}_r}
 \le C{r^{3/2}\over
          j^{3/2}(r+1-j)^{3/2}}.                          \tag{15.9e}
\]

Thus, when `j` and `r+1-j` are both `Omega(r)`, minimality
`Cat_r<16p` implies `w_j<p` for all sufficiently large `r`.  The failure
of (15.1) is not absence of low-load destinations: its net marked move
stops at the already saturated boundary class `w_2=Cat_(r-1)`.

This is not the full lower-shadow change.  Let `e=(C,R)` be one elementary
switch, let `beta_e,gamma_e` be its transposed coordinates, and put

\[
                  \partial_e K
                  =e_{K\cup\{\gamma_e\}}-e_{K\cup\{\beta_e\}}.
\]

After cyclically rotating its omitted-label word, let
`mathsf E_e,mathsf O_e` be the two parity lists of the common tail, as in
(2.5) of `MSW_MULTIRANK_LOCAL_TRADES.md`.  For depth `q`, put
`ell=m-q-1`.  If this switch is applied in isolation, its exact full
rank-`m-q` vector is

\[
\boxed{
 d_{q,e}={}
   \partial_e\operatorname{suf}_{\ell}(\mathsf O_e)
  +\partial_e\operatorname{suf}_{\ell}(\mathsf E_e)
  -\partial_e\operatorname{pre}_{\ell}(\mathsf E_e)
  -\partial_e\operatorname{pre}_{\ell}(\mathsf O_e).}     \tag{15.10}
\]

Indeed the two new local traces are the coordinate-transposed old traces,
in the opposite row order, so the universal four-letter identity applies
after the ambient affine relabelling.  For
`2<=m-q<=m-2`, the four cores in (15.10) are distinct and

\[
                         \|d_{q,e}\|_1=8:                 \tag{15.11}
\]

there are four negative and four positive targets.  The move displayed in
(15.9) is only one distinguished occurrence-level arm; the other three
arms can offset its cap-tail gain.

For one isolated switch, or for any additive subfamily below, the hinge
potential can change in absolute value by at most four:

\[
 \left|K_q(F+e)-K_q(F)\right|
       \le\sum_S(d_{q,e}(S))_+=4.                         \tag{15.11a}
\]

Consequently a whole row-disjoint parent packet has full
`Delta K_r` between `-4Cat_(r-1)` and `4Cat_(r-1)`.  Its marked intrinsic
part is exactly zero by (15.9d); no sign is presently proved for the other
three arms.

For one fixed parent context the four-arm sum has a sharper exact form.
Put `c=Cat_(r-1)` and `k=m-r-1`.  After rotating every omitted word at the
parent block, the common tail consists of the embedded permutation of `R`
followed by the `2k+1` exterior symbols.  Hence its two length-`k` suffix
cores, call them `A_C,B_C`, are independent of `R`; let
`P^E_(C,R),P^O_(C,R)` be the two prefix cores.  Summing (15.10) gives

\[
 \boxed{
 Z_C=c\,\partial_C(A_C+B_C)
       -\sum_{R\in D_{r-1}}\partial_C
          \bigl(P^E_{C,R}+P^O_{C,R}\bigr).}              \tag{15.11b}
\]

Here notation is linear, so `partial_C(A+B)` means
`partial_C A+partial_C B`.  In particular

\[
                         \|Z_C\|_1\le8c,
 \qquad \sum_S(Z_C(S))_+\le4c.                          \tag{15.11c}
\]

The distinguished fixed arm `partial_C A_C` is the telescoping intrinsic
move (15.9): its negative endpoint has canonical preload at least
`Cat_r`, and its positive endpoint has preload at least `c` by Lemma
15.2A.  Since both remain above `p`, this arm contributes exactly zero to
`Delta K_r`.  Therefore all full cap change comes from the other three
arms and

\[
                              |\Delta K_r(C)|\le3c.        \tag{15.11d}
\]

No sign follows from (15.11b).  There is also an exact within-packet Haar
obstruction.  With arbitrary coefficients `epsilon_R`,

\[
 \sum_R\epsilon_Rd_{r,(C,R)}
 =\left(\sum_R\epsilon_R\right)\partial_C(A_C+B_C)
  -\partial_C\sum_R\epsilon_R(P^E_{C,R}+P^O_{C,R}).       \tag{15.11e}
\]

A zero-sum commutator cancels both fixed arms, including the desired drain;
a nonzero coefficient on that drain forces the identical coefficient on
the fixed collateral arm `partial_C B_C`.  Thus cancellation internal to
one packet cannot isolate the marked flow.

There is a second, separate nonlinearity.  Let `F^star` be the factor after
all fixed-scale switches and define the interaction remainder

\[
 \mathcal R_q=\mu_q^{F^\star}-\mu_q^{F_{MSW}}
                         -\sum_e d_{q,e}.                 \tag{15.12}
\]

The exact-factor proof of Theorem 15.1 does not imply
`mathcal R_q=0`.  One row may contain several disjoint switched slabs, and
a cyclic rank-`m-q` interval can meet modifications associated with two
of them.  Its resulting target need not equal the sum of the two isolated
changes.  At `q=r`, no *intrinsic marked window* in (15.4) contains two
swapped state cells, because distinct size-`r+1` blocks in one row are
separated by at least `r+1` phases.  This proves additivity of (15.9), but
not of the full cyclic histogram (15.12).

The interaction can nevertheless be removed at constant cost.

### Lemma 15.3 (boundary locality of one rectangle)

In either modified row, a depth-`q` intersection window can change only
when the switched phase is one of its two boundary phases.

#### Proof

Suppress the common set `Q`.  In the first row the unchanged neighbours,
old state, and new state are

\[
             L=12Q,\qquad M=14Q,\qquad M'=23Q,\qquad R=34Q.
\]

In the second row they are

\[
             L=13Q,\qquad M=23Q,\qquad M'=14Q,\qquad R=24Q.
\]

In both cases

\[
                         L\cap M\cap R
                         =L\cap M'\cap R=Q.              \tag{15.13}
\]

If the switched phase is strictly inside a consecutive intersection
window, that window contains `L,M,R`; replacing `M` by `M'` therefore
does not change its intersection.  If the phase is outside the window it
also has no effect.  Only the left- and right-boundary cases remain.
\(\square\)

For a serviced depth `q`, form a conflict graph on the `T_(m,r)`
elementary switches.  Join two switches when they use a common row and
their switched phases are the two boundaries of one depth-`q` window.
Each switch uses two rows.  In either row there is at most one switch at
the phase `q` steps to its left and at most one at the phase `q` steps to
its right.  Hence

\[
                            \Delta(G_q)\le4.              \tag{15.14}
\]

### Corollary 15.4 (constant-density additive subfamily)

For every fixed scale `r` and serviced depth `q`, at least

\[
                              {T_{m,r}\over5}              \tag{15.15}
\]

of the elementary switches may be applied so that the full lower-histogram
change is exactly the sum of their isolated four-arm vectors (15.10).
In particular their interaction remainder (15.12) is zero.

At the matched depth `q=r`, all `T_(m,r)` switches are additive; no
factor-five thinning is needed.

#### Proof

Greedy colouring, or the standard maximal-independent-set bound, gives an
independent set of size at least `|V(G_q)|/5`.  Apply only those switches.
By Lemma 15.3, switches strictly inside a given depth-`q` window do not
alter its target.  Independence says that its two boundary phases cannot
both be switched.  Thus every changed window is charged to its unique
boundary switch and has exactly the target change it has when that switch
is applied alone.  Summing over windows proves additivity.  Every subset
of the switches remains exact by Theorem 15.1.  Finally, two distinct
size-`r+1` blocks in one row have switched phases separated by at least
`r+1`, whereas the two boundaries of a depth-`r` window are separated by
exactly `r`.  Thus `G_r` has no edges. \(\square\)

Consequently interaction costs only an absolute factor and the sharp
remaining lemma is now purely a four-arm congestion problem: select or
orient a constant fraction of the additive vectors (15.10) so that their
four positive prefix/suffix arms do not refill the overloaded targets
emptied by their four negative arms.  Controlling only the distinguished
map `C -> (S_C,T_C)` in (15.9) is insufficient.

The count (15.6) shows that a constant-factor loss is affordable.  No loss
of order `p` is affordable.  Exact middle ownership, fixed-scale slab
compatibility, and lower-window interaction are solved; simultaneous
four-arm target routing is not.

## 16. The certified leaf rotations do not generate a Catalan conveyor

The rewrite underlying (15.1) resembles a Tamari rotation, but it is only
the special rotation in which two of the three hanging subtrees are empty.
That distinction prevents the present exact trades from implementing an
arbitrary permutation, or even from moving the central first-return
classes.

Write an ordered binary tree as `N(L,R)`, let `emptyset` denote the empty
tree, and put

\[
                         \bullet=N(\varnothing,\varnothing).
\]

Under the MSW tree bijection, the local replacement is

\[
 \boxed{
 N(\bullet,R)\quad\longleftrightarrow\quad
 N(\varnothing,N(\varnothing,R)).}                       \tag{16.1}
\]

Let `mathcal L_r` be the graph on `D_r` obtained by allowing (16.1) in an
arbitrary one-hole tree context.  This deliberately enlarges the certified
generator graph, because a literal middle-state rectangle is presently
proved only when its local permutation block is aligned.  A no-go for
`mathcal L_r` is therefore also a no-go for the certified subgraph.

### Theorem 16.1 (leaf-rotation component invariant)

Orient (16.1) from left to right.  Every tree has a unique normal form,
obtained by removing every occurrence of a node whose left child is
`bullet`.  Two Dyck fillings lie in the same component of `mathcal L_r`
if and only if they have the same normal form.

Consequently `mathcal L_r` is disconnected for every `r>=3`.  If `f_r`
is its number of components, then

\[
 F(z)=\sum_{r\ge0}f_rz^r
      =1+z\bigl(F(z)-z\bigr)F(z),                         \tag{16.2}
\]

so

\[
                         f_0,f_1,f_2,f_3,f_4,f_5,\ldots
                         =1,1,1,2,5,13,\ldots.            \tag{16.3}
\]

The edge transpositions of this enlarged leaf-rotation graph generate
exactly

\[
                         \prod_{K\in\pi_0(\mathcal L_r)}
                         \operatorname{Sym}(K),           \tag{16.4}
\]

not `Sym(D_r)`.  The currently certified aligned rotations generate a
subgroup of (16.4).

#### Proof

Let `c(T)` count nodes of `T` whose left child is exactly `bullet`.
The forward rule in (16.1) removes its root redex and creates no new such
node.  It preserves `R` unchanged; a redex inside `R` is merely moved two
addresses deeper.  A redex in a disjoint subtree is untouched.  Thus
`c(T)` decreases by one, so forward rewriting terminates.

Nested redexes can occur only inside the displayed `R`.  Rewriting the
outer redex and a redex inside `R` commutes, while disjoint rewrites plainly
commute.  Hence the terminating system is confluent and its normal form is
unique.  A forward or reverse edge preserves that normal form.  Conversely
two trees with the same normal form are joined by following their forward
reduction paths, one in reverse.  This proves the component statement.

A normal tree is empty, or is `N(L,R)` with `L,R` normal and `L` not equal
to `bullet`.  The singleton tree `bullet` contributes `z`, so the
ordinary generating function is exactly (16.2), whose first coefficients
give (16.3).  Finally, edge transpositions of a connected graph generate
the full symmetric group on its vertex set.  Applying this independently
to every component gives (16.4). \(\square\)

There is an even sharper phase obstruction.  For a root
`x=1u0v`, put `j=|u|_s+1`; Lemma 15.2A places its long-window target in
the even class `2j`.  A root application of (16.1) connects only
`j=2` to `j=1`.  An application strictly below the root preserves the size
of the root's left subtree and hence preserves `j`.  Therefore no sequence
of certified rectangles can transport any class `j>=3` toward a central
sub-cap class, or conversely.

Full Tamari rotations do connect `D_r`, and their edge transpositions
would generate `Sym(D_r)`.  They are not currently legal factor trades:
one still needs an exact replacement preserving both ledgers (13A.5) when
the three hanging subtrees are nonempty.  Such a larger rotation theorem,
not connectivity of the associahedron by itself, is the missing Catalan
conveyor lemma.

The most direct two-bracketing associator theorem is in fact false.

### Proposition 16.2 (the first nonempty associator packet is not legal)

Take hanging-subtree sizes `(a,b,c)=(1,1,0)`.  The packet
`Cat_a Cat_b Cat_c` contains only the two bracketings, whose MSW traces are

\[
\begin{array}{c|ccccc}
L&1245&1258&1268&1678&3678\\
R&1256&1456&3456&3458&3478.
\end{array}                                                \tag{16.5}
\]

There is no nonidentity phasewise interleaving of these two rows which
fixes both endpoints and remains a Johnson path.  Hence no exact
associator packet using only these two bracketings exists, even before the
adjacent-union ledger is imposed.

#### Proof

A phasewise permutation of two rows is a bit `epsilon_t`, with
`epsilon_0=epsilon_4=0`; the bit changes at transition `t` only if both
cross pairs `L_t--R_(t+1)` and `R_t--L_(t+1)` are Johnson edges.  From
(16.5), both cross pairs are edges at transition zero.  At transitions
one, two, and three their symmetric-difference sizes are respectively

\[
                         (6,4),\qquad(6,6),\qquad(4,4),
\]

instead of `(2,2)`.  Thus the bit can change only at transition zero and
can never return to zero.  The endpoint condition forces it to remain
zero throughout. \(\square\)

This does not rule out an associator with auxiliary bracketings or extra
rows.  It does rule out the naive commuting-grid packet consisting solely
of all `Cat_a Cat_b Cat_c` choices in the two endpoint bracketings.  Any
legal full-Tamari conveyor must enlarge the packet or use a multi-stage
route through additional tree shapes.

The extra-row alternative is now realized at the first nonleaf root scale.
There is a support-feasible four-for-four packet of length-four wreath
paths with identical aggregate \(X\) and adjacent-union \(Y\) ledgers.  Its
distinguished traces are

\[
 (1245,1258,1268,1678,3678)
 \quad\longleftrightarrow\quad
 (1245,1256,1268,1678,3678).                         \tag{16.6}
\]

Thus the new first edge is the root Tamari rotation
\(1245\longrightarrow1256\), starting from the primitive first-return
class \(j=4\).  The corresponding intrinsic intersection changes exactly
from \(\{8\}\) to \(\{6\}\).  Three auxiliary paths cancel the displaced
\(X\) state and all changed \(Y\) colours.  The complete four-by-five
tables and direct ledger proof are in the four-row Tamari associator note.

This closes the complete-wreath associator gate, but not the stronger
row-labelled open-slab gate: one auxiliary path changes its complementary
endpoint pair.  Hence the packet may replace four complete wreaths in an
exact factor, while insertion into a slab with four individually frozen
boundary pairs still needs an endpoint-routing identity.  Together with
Proposition 16.2, the minimum complete-wreath packet size is currently
known only to lie between three and four rows.

### Theorem 16.3 (even-pair conjugation still has a Motzkin invariant)

Let

\[
 H_r=\langle(2\ 3),(4\ 5),\ldots,(2r-2\ 2r-1)\rangle. \tag{16.7}
\]

Every element of `H_r` preserves every Chung--Feller layer, so it may be
used to conjugate the enlarged leaf-rotation graph `mathcal L_r`.  Even
after adjoining all these conjugate edges, the resulting graph on `D_r`
is disconnected for every `r>=4`.

Write a Dyck word as

\[
 1\;(x_2x_3)(x_4x_5)\cdots(x_{2r-2}x_{2r-1})\;0         \tag{16.8}
\]

and encode each displayed pair by

\[
 11\mapsto U,\qquad00\mapsto D,\qquad10,01\mapsto L.    \tag{16.9}
\]

This is a Motzkin path of length `r-1`.  Let `rho(w)` be the word obtained
from its uncoloured Motzkin encoding by replacing every adjacent `UD` by
`LL`.  Then `rho` is invariant under `H_r` and under every
`H_r`-conjugate of every embedded leaf rotation (16.1).

#### Proof

At the boundaries of the pairs in (16.8), Dyck height is odd.  Dividing
the height above zero by two identifies (16.9) with a Motzkin path;
swapping the two entries of one pair only exchanges the two colours of a
level step and leaves its uncoloured skeleton fixed.

An occurrence `1100 <-> 1010` beginning at an odd position changes
`10 <-> 01` inside one pair, so again it changes only a level colour.  If
it begins at an even position, its two affected pairs change as

\[
                         11,00\longleftrightarrow10,10,
\]

which is exactly `UD <-> LL`.  Conjugating by `H_r` can choose the two
level colours but cannot change this uncoloured relation.

Orient `UD -> LL`.  Different occurrences of `UD` are disjoint, and
performing one replacement creates no new `UD` at either boundary.
Hence the reduction terminates after one simultaneous sweep and has a
unique normal form.  Both sides of `UD <-> LL` have the same normal form,
so `rho` is invariant under every allowed edge.

For `r>=4`, the two valid Motzkin paths

\[
                         L^{r-1},\qquad UL^{r-3}D        \tag{16.10}
\]

contain no adjacent `UD` and are distinct.  Their corresponding Dyck
words therefore lie in different components. \(\square\)

The rooted pentagon at `r=3` is consistent with this theorem: its
Motzkin paths have length two, and the sole nonflat skeleton `UD` reduces
to `LL`.  Its transitivity is a genuine improvement over the old leaf
normal form, but bounded pentagon substitutions and even-pair conjugates
do not by themselves give a full Catalan conveyor.

There is a complete refinement of this invariant.  Retain the two colours
\(10,01\) on every Motzkin level step.  In the \(UD\)-free normal form,
call a level position rigid when it is isolated and its previous step is
\(D\), or its next step is \(U\).  Two roots lie in the same component if
and only if their uncoloured normal forms agree and their colours agree at
every rigid position.  Hence, if \(g_r\) is the component count,

\[
 \boxed{
 g_r=\sum_{\substack{M\text{ Motzkin excursion}\\
                     |M|=r-1,\ UD\not\subset M}}
          2^{\rho(M)},}                                  \tag{16.11}
\]

where \(\rho(M)\) counts rigid levels.  The first values are

\[
                         g_1,g_2,g_3,g_4,g_5
                         =1,1,1,2,6.                     \tag{16.12}
\]

The proof is in the \(H_r\)-conjugated leaf-graph component note.  Its two
local moves are \(UD\leftrightarrow LL\), with arbitrary colours on the
two levels, and a single-level colour flip precisely when the previous
step is not \(D\) and the next step is not \(U\).  Adjacent level runs and
all nonrigid isolated levels are therefore flexible; exactly the displayed
rigid colours survive.

The five-row \(D_3\) pentagon itself is a complete port-transversal factor
trade: both sides exhaust all twenty \(X\)-states and fifteen \(Y\)-colours,
fix all five Dyck/complement ports, and have intrinsic displacement
\(2e_3+e_5-e_4-2e_2\).  Its exact certificate and contextual PCap capacity
audit are in the \(D_3\)-port-pentagon note.

## 17. A port-transversal local factor is an exact context substitute

The failure of a two-row associator does not force one to rewire the
canonical local paths.  One may replace the complete odd-graph factor
inside a recursive hole.  There is a precise and very small interface
condition for doing so.

Let `J` be a set of `2r` local coordinates and let `infinity` be one
additional coordinate.  Let `G` be an exact `C_(2r+1)`-factor of
`KG(J union {infinity},r)`.  Let `D` be the `Cat_r` local boundary
`r`-sets supplied by the canonical Dyck fillings of a size-`r` hole
(after the affine relabelling inherited from its outer context).

Call `G` **`D`-transversal** when every wreath of `G` contains exactly
one member of `D` among its middle windows.

For a wreath `C`, let `partial_infinity(C)` be the two length-`r`
windows on `J` which are adjacent to `infinity` in the cyclic order.
Equivalently, these are the endpoints of the block of the `r+1`
consecutive length-`r` windows avoiding `infinity`.  Call `G`
**`D`-port-transversal** when

\[
                 |D\cap\partial_\infty(C)|=1
                 \qquad\hbox{for every wreath }C\in G.       \tag{17.0}
\]

The port qualification is essential.  Ordinary `D`-transversality does
not force the distinguished set to be an endpoint of the local Johnson
geodesic.

### Proposition 17.0 (ordinary transversality is insufficient)

Let `r=2`, `J={1,2,3,4}`, and `infinity=0`.  The two cyclic orders

\[
                 (0,1,2,3,4),\qquad(0,2,4,1,3)              \tag{17.0a}
\]

form an exact middle factor on the ten two-subsets.  For the affine Dyck
family

\[
                         D=\{23,24\},                       \tag{17.0b}
\]

the first wreath contains exactly `23` and the second exactly `24`, so
the factor is `D`-transversal.  However the core windows of the first
wreath are

\[
                         12,23,34,                           \tag{17.0c}
\]

and its ports are `12,34`.  Thus its distinguished Dyck set `23` is an
interior state.  No orientation makes the core-avoiding block a geodesic
from `23` to its complement `14`.  Hence the original transversal-only
form of Theorem 17.1 is false. \(\square\)

### Theorem 17.1 (port-transversal context-substitution theorem)

If `G` is `D`-port-transversal, then the canonical MSW traces inside any
aligned size-`r` hole may be replaced by the traces of `G`, rooted at
their unique `D`-ports.  The replacement keeps every outer boundary state
fixed and preserves both exact ownership ledgers (13A.4).

Consequently it extends to another exact middle wreath factor in the
ambient dimension.  Different `D`-port-transversal local factors may be chosen
independently in phase-disjoint holes.

#### Proof

Fix one wreath `C` of `G`, and let `P` be the unique member of
`D` in `partial_infinity(C)`.  Orient the wreath so that the block of
vertices avoiding `infinity` starts at `P`.  Those vertices form a
Johnson geodesic

\[
                         P=X_0,X_1,\ldots,X_r=J\setminus P.
                                                               \tag{17.1}
\]

Indeed a cyclic order on `J union {infinity}` has exactly `r+1`
length-`r` windows avoiding `infinity`; read in order, consecutive such
windows exchange one coordinate, while the first and last are the two
complementary length-`r` blocks of `J` separated by `infinity`.

Between `X_t` and `X_(t+1)` the odd cycle has the unique vertex containing
`infinity`, namely

\[
 Z_t=\{\mathord{infinity}\}\cup
           \bigl(J\setminus(X_t\cup X_{t+1})\bigr).      \tag{17.2}
\]

Equivalently its adjacent-union colour is

\[
                         Y_t=X_t\cup X_{t+1}.             \tag{17.3}
\]

As `C` ranges over `G`, all core `r`-sets occur exactly once among the
states in (17.1), because `G` is an exact factor.  All `(r+1)`-sets occur
exactly once among the colours in (17.3), because complementation in `J`
and adjoining `infinity` bijects them with the `infinity`-containing
vertices in (17.2), which are also owned exactly once by `G`.

Port-transversality assigns the `Cat_r` rooted paths bijectively to the
canonical boundary sets `P in D`.  Indeed the selected ports are distinct
middle sets, and their number is `|G|=|D|=Cat_r`.  The opposite port is
`J minus P`, so (17.1) fixes both boundary states row by row.  After
adjoining the common exterior coordinates of the ambient hole, the two
preceding paragraphs say exactly that the `X`-state and adjacent-`Y`
multisets in (13A.5) are unchanged.  Theorem 13A.2 proves exact ambient
ownership.  Phase-disjoint substitutions have disjoint state and edge
slabs, so their ledgers add. \(\square\)

### Corollary 17.2 (the replacement-seed problem is local)

For every growing scale `r`, it is enough to construct a library of
`D_(r+1)`-port-transversal exact local factors on the **parent** holes and
to choose their members so that their **full affected-window histograms**
satisfy the required simultaneous residual-capacity inequalities.  Every
such choice produces a global exact seed without a new middle-completion
problem.

For one parent `C`, one library member `G`, and one serviced depth `q`,
let `u_(C,G,q)` count all windows meeting an interior phase of `C`,
including both crossing collars, and let `beta_q` be the load of all
unaffected windows.  The literal local cap defect is

\[
 \sum_S\bigl(u_{C,G,q}(S)-(p-\beta_q(S))_+\bigr)_+.     \tag{17.3a}
\]

Thus a usable library must lower the sum of (17.3a), with one common
integral choice serving every protected depth, while retaining the
targets supported only by the old parent packet.  The exact identities
and weighted fractional dual are in the parent residual-capacity note.

Merely requiring the two distinguished child-window target maps to have
fibres of size at most `p` is neither sufficient nor the correct
floor-aware statement: the other `2r-2` crossing starts and the ambient
background `beta_q` remain.  This distinction is part of the theorem,
not a later routing detail.

The parent qualification is necessary.  A `D_r`-port-transversal replacement
made strictly inside the same size-`r` hole fixes its two boundary states,
so Proposition 14.4 says that the full-hole intersection remains the old
exterior target.  Theorem 17.1 solves exact completion; it does not by
itself split the hole in which it is installed.

This is a sufficient architecture, not a library theorem.  The canonical
MSW factor is one `D_r`-port-transversal member.  The boundary-closed
rectangles of Sections 13A and 15 already give noncanonical parent members
which preserve the parent Dyck port matching and change selected child
profiles.  The open finite gate is whether one can build a sufficiently
rich port-transversal library whose full affected-window profiles satisfy
the residual-capacity and exclusive-support conditions above.  In
particular, either side of the known `r=4`
nonlocal Haar circuit would require a separately proved admissible
re-embedding which preserves the prescribed port matching; ordinary Dyck
transversality and shadow cancellation are not enough.

### Theorem 17.3 (middle-levels path-factor normal form)

Let `M(J)` be the bipartite inclusion graph whose two vertex classes are
the `r`- and `(r+1)`-subsets of `J`.  There is a bijection between

1. `D`-port-transversal exact local odd-graph factors on
   `J union {infinity}`; and
2. vertex partitions of `M(J)` into `Cat_r` paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r=J\setminus P,qquad P\in D,             \tag{17.4}
\]

where every path has length `2r` and the initial vertices run through
`D` exactly once.

Under this bijection the `X`-states and `Y`-colours in the local
replacement criterion are literally the two vertex classes of `M(J)`.
Thus the remaining local construction problem is an exact rooted
complement-path-factor problem in the middle-levels graph.

#### Proof

Given a port-transversal odd cycle, orient its `infinity`-avoiding block
from its `D`-port `P`.  Equations (17.1)--(17.3) give the alternating path

\[
 X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r.
\]

Its other port is `J minus P`.  Exact middle ownership says that the
`X`-vertices over all cycles partition the `r`-subsets of `J`; ownership
of the `infinity`-containing odd-graph vertices says, by (17.2), that the
`Y`-vertices partition the `(r+1)`-subsets.  Hence the paths partition
all vertices of `M(J)`.

Conversely, start with a path factor (17.4) and put

\[
             Z_t=\{\mathord{infinity}\}\cup(J\setminus Y_t).
                                                               \tag{17.5}
\]

Then `X_t` is disjoint from `Z_t`, and `Z_t` is disjoint from
`X_(t+1)`, because both `X_t` and `X_(t+1)` are contained in `Y_t`.
Also `X_r=J minus X_0`, so

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{r-1},X_r                  \tag{17.6}
\]

closes to a `(2r+1)`-cycle in the odd graph.  The paths partition all
`r`-sets avoiding `infinity`; the bijection (17.5) makes their `Y`-sets
partition all `r`-sets containing `infinity`.  Thus (17.6) over all
paths is an exact odd-graph factor.  Its two ports are `P` and
`J minus P`, so it is `D`-port-transversal.  The two constructions are
inverse. \(\square\)
