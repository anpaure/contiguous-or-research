# A Gaussian Packet Selector and a Density-Scale Energy Certificate

Date: 2026-09-05. Independent scratch work, suffix `c7e42`.

## 0. Status and Scope

The full asymptotic conjecture is not proved here. This note gives an
unconditional positive selector, its literal words, and a quantitative
conditional strengthening:

1. A finite, deterministic conditional-expectation algorithm selects phase
   packets with a prescribed number of blocks and an exact residual-profile
   bound. It requires no disjointness or matching theorem.
2. For every fixed `c>0`, the algorithm constructs nonempty words on `2b`
   coordinates of length at most `c W(2b)` with hole density at most

   \[
   \eta(c)+o(1),\qquad
   \eta(c)=\frac1{\sqrt\pi}\int_{\mathbb R}
                  \exp(-x^2-c e^{x^2})\,dx.                 \tag{0.1}
   \]

3. At `c=1`, this is coverage at least
   `(0.7607312156...-o(1)) 4^b`. The weaker explicit bound
   `1-1/(e sqrt(2))>2/pi` needs no numerical quadrature.
4. Independent packet selection actually has hole density tending to
   `eta(c)`, even after all extra within-block and cross-block interval
   unions are counted. This statement does not assert an optimality bound
   on dependent selectors.
5. A floor-corrected pair-energy certificate reduces density-one coverage
   to one explicitly specified integral quadratic optimization. It includes
   the Gaussian capacity deficit, permits skipping `o(sqrt(b))` ranks, and
   invokes the proved cylinder completion only after an actual word exists.

The elementary floor-energy idea is already present in the older project
notes; it is not claimed as a new general inequality. The contributions
here are the literal exact-budget positive selector and Gaussian profile,
the bound on all undesignated interval unions, and the explicit
density-scale, packet-pair formulation with its full cost ledger. The
all-band microbank extension in the existing microbank notes is also not
counted as new work.

No conclusion is drawn from a generic growing-uniformity nibble. The
unresolved estimate is stated in Section 8.

## 1. Literal Phase-Packet Blocks

Let `b>=3`, let `Omega=[2b]`, and choose an integer

\[
  1\le H\le b-2,\qquad
  \ell=b-H,\quad u=b+H,\quad L=b+1,\quad D=L+2H.
                                                               \tag{1.1}
\]

Parity of `b` is irrelevant in this note. Write

\[
 W=\binom{2b}{b},\qquad N_s=\binom{2b}{s}.
\]

A labelled packet consists of an omitted coordinate `v` and an ordered
list `z=(z_0,...,z_{2b-2})` of the other coordinates. There are exactly
`(2b)!` labels. Extend `z` periodically, with period `2b-1`. For each
`ell<=s<=u`, designate the `L` sets

\[
 S_s(z)=\left\{\{z_a,\ldots,z_{a+s-1}\}:0\le a<L\right\}.
                                                               \tag{1.2}
\]

All these windows are clean. They are distinct at each rank: a proper arc
in a directed cycle with distinct labels has exactly one directed edge
entering it from its complement, so its set determines its start. Here
`s<=2b-2` and `L<=2b-1`.

The literal output block of this packet is

\[
 B(z)=(B_0,\ldots,B_{D-1}),\qquad
 B_j=\{z_j,\ldots,z_{j+\ell-1}\}.                      \tag{1.3}
\]

Every letter is a nonempty `ell`-set. The needed singleton source prefix
has exactly `L+u-1=2b+H` letters. For each designated `a,s`,

\[
 \bigcup_{j=a}^{a+s-\ell}B_j
       =\{z_a,\ldots,z_{a+s-1}\}.                       \tag{1.4}
\]

Indeed the source intervals overlap consecutively, have first coordinate
position `a`, and last coordinate position `a+s-1`. The final block index
is at most `L-1+u-ell=D-1`. Thus (1.4) is a literal internal witness,
not a queue or shadow interpretation.

For a list of `t>=1` packets, concatenate their blocks, with no separators or
connectors. Its length is exactly `tD`. Every designated witness remains
inside its own block.

## 2. Exact Control of Undesignated Intervals

For the concatenated word, let `U_s` be its distinct rank-`s` interval
unions and let `V_s` be the union of the designated supports (1.2).

### Lemma 2.1

For every `ell<=s<=u`,

\[
 0\le |U_s|-|V_s|
 \le t(u-s)+(t-1)(s-\ell+1)
 \le t(2H+1).                                         \tag{2.1}
\]

#### Proof

An interval of `r` letters inside one block is a cyclic source window of
length `ell+r-1`. Until this length reaches `2b-1`, its union has exactly
that cardinality. At and beyond `2b-1`, its union is all of
`Omega-{v}`, of rank `2b-1>u`. Consequently a within-block rank-`s`
interval has exactly `r=s-ell+1` letters. There are

\[
 D-r+1=L+u-s
\]

possible starts, only `u-s` more than the designated `L` starts. Summing
over blocks gives the first term in (2.1).

Now consider an interval crossing a block boundary and ending at position
`j`, numbered starting from one, of the last block it meets. It contains
the whole prefix of `j` letters of that block. That prefix has rank
`min(ell+j-1,2b-1)`. Therefore a rank-`s` crossing interval must have
`j<=s-ell+1`. This remains true if the interval crosses several boundaries.
For any fixed ending position, all interval unions are nested, so at most
one distinct rank-`s` target can use it. There are at most
`(t-1)(s-ell+1)` eligible endings outside the first block. This proves
(2.1). No cleanliness across a join was assumed. QED.

Put

\[
 X=\sum_{s=\ell}^u(N_s-|V_s|),\qquad
 F=\sum_{\substack{1\le s\le2b\\s\notin[\ell,u]}}N_s.
\]

If `g` is the actual number of nonempty holes of the word, Lemma 2.1 gives

\[
 X-t(2H+1)^2\le g\le X+F.                              \tag{2.2}
\]

The lower bound can be negative and is used only as an asymptotic error
estimate. This lemma makes statements about the selected windows
transferable to the actual word in both directions.

## 3. A Deterministic Profile-Aware Selector

Uniformly sample a packet label. Permutation invariance and transitivity
on the rank-`s` layer, together with `|S_s(z)|=L`, imply

\[
 p_s:=\Pr(T\in S_s(z))=\frac L{N_s}
       \quad\text{for every rank-}s\text{ target }T.     \tag{3.1}
\]

Let `R_s` be any specified residual target family at rank `s`. It need not
be random, regular, or a matching residual.

### Theorem 3.1

For every integer `t>=0`, a deterministic list of `t` packets exists for
which

\[
 \sum_{s=\ell}^u
 \left|R_s\setminus\bigcup_{i=1}^t S_s(z_i)\right|
 \le \sum_{s=\ell}^u |R_s|(1-L/N_s)^t.                 \tag{3.2}
\]

Concatenating their literal blocks costs exactly `tD` positions. If an old
word already covers the complement of the specified residuals, append
these blocks; all old witnesses are retained.

#### Proof and Algorithm

After choosing `j` packets, let `R_s^(j)` be the targets still uncovered
by these packets. Define

\[
 \Phi_j=\sum_{s=\ell}^u
      |R_s^{(j)}|(1-p_s)^{t-j}.                         \tag{3.3}
\]

For each possible next label `z`, compute

\[
 \sum_{s=\ell}^u
      |R_s^{(j)}\setminus S_s(z)|(1-p_s)^{t-j-1}.
\]

Its average over the `(2b)!` labels is exactly `Phi_j`, by (3.1) and
linearity of expectation. Choose a minimizing label, breaking ties by
lexicographic order. Then `Phi_(j+1)<=Phi_j`. After `t` choices,
`Phi_t` is the left side of (3.2), while `Phi_0` is its right side.
Equation (1.4) proves the word and cost assertion. QED.

This is a finite exact algorithm, not an efficiency claim. Rational
arithmetic suffices throughout. The selected packets may overlap and may
repeat; all such costs are counted. The theorem does not promise separate
rankwise inequalities for the same deterministic family, only the stated
simultaneous aggregate inequality.

## 4. Gaussian Coverage at an Exact Width Budget

For sufficiently large `b`, set

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,
 \qquad t=\left\lfloor\frac{cW}{D}\right\rfloor,
 \qquad M=Lt,\qquad c>0\text{ fixed}.                  \tag{4.1}
\]

Then `H<=b-2`, `t>=1`, and the constructed word is nonempty, with exact
length `tD<=cW`. Also

\[
 \frac MW\longrightarrow c,
 \qquad
 \frac{t(2H+1)^2}{4^b}
        =O\left(\frac{\log b}{\sqrt b}\right)=o(1).     \tag{4.2}
\]

For `Y` binomial with parameters `(2b,1/2)`,
`E exp(lambda(Y-b))=(cosh(lambda/2))^(2b)<=exp(b lambda^2/4)`.
Optimizing the exponential Markov bound on each tail gives

\[
 \frac F{4^b}\le2e^{-H^2/b}\le\frac1{2b^2}.            \tag{4.3}
\]

### Theorem 4.1

The selector in Theorem 3.1, applied to all band targets, gives words with

\[
 \limsup_{b\to\infty}\frac g{4^b}\le\eta(c),
 \qquad
 \eta(c)=\frac1{\sqrt\pi}\int_{\mathbb R}
                    e^{-x^2-ce^{x^2}}\,dx.            \tag{4.4}
\]

For independent uniform packet labels, the actual hole density converges
in probability to `eta(c)`.

#### Gaussian Limit

For independent labels the exact expected designated deficit is

\[
 \mathbb E X=\sum_{h=-H}^H
 N_{b+h}\left(1-\frac L{N_{b+h}}\right)^t.             \tag{4.5}
\]

For every fixed `A<infinity`, the elementary adjacent-binomial product
gives, uniformly for `|h|<=A sqrt(b)`,

\[
 \frac{N_{b+h}}W
   =\exp\left(-\frac{h^2}b+o(1)\right),
 \qquad \frac{\sqrt b W}{4^b}\longrightarrow\frac1{\sqrt\pi}.
                                                               \tag{4.6}
\]

For example, for `h>=0` the ratio is
`product_(i=0)^(h-1) (b-i)/(b+i+1)`; taking logarithms and using
`sum_(i<h)(2i+1)=h^2` proves the uniform assertion. Negative offsets
follow by symmetry. The second assertion is the central-binomial
Stirling estimate.

On this compact range `L/N_(b+h)` is exponentially small,

\[
 tL/N_{b+h}\longrightarrow c e^{x^2},\qquad
 t(L/N_{b+h})^2\longrightarrow0,
       \quad h/\sqrt b\longrightarrow x.
\]

Thus the corresponding portion of (4.5), divided by `4^b`, tends to

\[
 \frac1{\sqrt\pi}\int_{-A}^A e^{-x^2-ce^{x^2}}\,dx.
\]

The omitted summands are at most the binomial mass outside
`|h|<=A sqrt(b)`, bounded by `2 exp(-A^2+o(1))`. Let `A` tend to infinity.
This proves `E X/4^b -> eta(c)`. Theorem 3.1 and (2.2), (4.3) give the
deterministic upper bound.

#### Concentration and Literal Holes

Replacing one packet changes `X` by at most `K=(2H+1)L`. At each rank,
adding or deleting one packet can change the union's size by at most `L`;
replacing it changes that size by a number in `[-L,L]`.

Expose the independent labels successively and use the conditional
expectations of `X` as a martingale. Each increment has absolute value at
most `K`: fixing all preceding labels, two values of the next label alter
the conditional expectation by at most `K`, by coupling the same future
labels. Distinct martingale increments are orthogonal in expectation.
Consequently

\[
 \operatorname{Var}X\le tK^2,
 \qquad
 \Pr(|X-\mathbb E X|>\varepsilon4^b)
 \le\frac{tK^2}{\varepsilon^2 16^b}
 =O\left(\frac{b^{3/2}\log b}{\varepsilon^2 4^b}\right)=o(1).
                                                               \tag{4.7}
\]

Equations (2.2), (4.2), and (4.3) then give
`g/4^b -> eta(c)` in probability for the actual word. QED.

The same compact-range argument shows that at Gaussian offset
`s=b+floor(x sqrt(b))` the expected covered fraction of that layer tends
to `1-exp(-c exp(x^2))`. It is not permissible to choose different
families at different offsets; (4.5) used one common family throughout.

### Numerical and Analytic Calibration

At `c=1`, elementary quadrature gives

\[
  \eta(1)=0.239268784392\ldots,
  \qquad 1-\eta(1)=0.760731215608\ldots.                 \tag{4.8}
\]

These decimals are numerical, not used in the proof. Since
`exp(x^2)>=1+x^2`, there is the analytic estimate

\[
 \eta(c)\le\frac{e^{-c}}{\sqrt{1+c}}.                  \tag{4.9}
\]

In particular the guaranteed coverage at width is at least
`1-1/(e sqrt(2))`, strictly larger than `2/pi`, the density of the old
narrow deterministic bridge word. The stronger value in (4.8) follows
from the integral, not from (4.9).

This improves that particular density benchmark; it does not improve
the known universal-word coefficient or prove that a dependent selector
cannot do better. The random selector has a positive limiting hole
density. Applying sublinear dimension extension to that selector does
not meet the vanishing-density antecedent.

The positive bound extends to every dimension, not only even ones. If
`A=(A_1,...,A_n)` is the nonempty even-dimensional word, use the literal
one-bit lift

\[
 A_1,\ldots,A_n,\{z\},A_1\cup\{z\},\ldots,A_{n-1}\cup\{z\}.
\]

Every old witness persists. Its union with `z` uses its lifted copy if
it ends before `n`, or the old suffix followed by the bridge `{z}` if
it ends at `n`. The bridge covers `{z}`. Thus the lifted word has at most
`2g` holes and length `2n`, and

\[
 \frac{2W(2b)}{W(2b+1)}=1+\frac1{2b+1}.
\]

Consequently, for every sufficiently large dimension `k`, the construction
has length at most `(c+o(1))W(k)` and covers at least
`(1-eta(c)-o(1))2^k` nonempty targets.

## 5. A Sharp Scalar Integer-Energy Bound

This section records the floor correction explicitly so the selector
problem need not assign a separate quota to every target.

Let `a_1,...,a_N` be nonnegative integers with sum `M`, let

\[
 q=\lfloor M/N\rfloor,\qquad
 Q=\sum_{j=1}^N a_j(a_j-1),
 \qquad Q_{\min}=2qM-q(q+1)N,
\]

\[
 E=Q-Q_{\min},\qquad
 d(q)=\begin{cases}2,&q=0,\\q(q+1),&q\ge1.\end{cases}  \tag{5.1}
\]

### Lemma 5.1

If `h` of the `a_j` vanish, then

\[
 E\ge0,\qquad
 h\le (N-M)_++\frac E{d(q)}.                           \tag{5.2}
\]

Moreover `Q_min` is the exact minimum of `Q` over all integer load vectors
of total `M`.

#### Proof

For every integer `a>=0`, `(a-q)(a-q-1)>=0`. Summing gives

\[
 \sum_j(a_j-q)(a_j-q-1)=Q-2qM+q(q+1)N=E.              \tag{5.3}
\]

Loads in `{q,q+1}`, with exactly `M-qN` ceiling loads, have this sum zero,
proving both nonnegativity and the exact minimum.

When `q>=1`, a zero load contributes `q(q+1)` to (5.3), and every other
contribution is nonnegative. Also `M>=N`, so (5.2) follows.

When `q=0`, `E=Q`. The exact identity

\[
 h=N-M+\sum_j(a_j-1)_+
\]

and the integer inequality `(a-1)_+<=a(a-1)/2` give (5.2).
Both branches are sharp for load vectors supported respectively on
`{0,q,q+1}` and on `{0,1,2}`, whenever the prescribed mean allows those
loads. QED.

The integer floor correction matters. Subtracting `M^2/N` or insisting
that all raw pair collisions be small would be wrong when `M/N>1`.
Conversely, small energy is sufficient but not necessary for few holes:
at mean two, half the loads one and half three have no holes but `E=N`.

## 6. The Exact Packet-Pair Optimization

For an arbitrary chosen list of `t` packets, let `a_s(T)` count its
designated rank-`s` occurrences. Then `sum_T a_s(T)=M=Lt`. Each packet
has no same-rank internal repetition. Therefore

\[
 Q_s:=\sum_T a_s(T)(a_s(T)-1)
   =\sum_{i\ne j}|S_s(z_i)\cap S_s(z_j)|.              \tag{6.1}
\]

Define

\[
 q_s=\lfloor M/N_s\rfloor,\quad
 E_s=Q_s-2q_sM+q_s(q_s+1)N_s,\quad
 \mathcal E=\sum_{s=\ell}^u\frac{E_s}{d(q_s)}.           \tag{6.2}
\]

Every `E_s` is nonnegative. Lemma 5.1 and the literal compiler prove the
following finite assertion, without any distributional assumption:

### Theorem 6.1

For `t>=1`, the actual word of length exactly `tD` satisfies

\[
 g\le F+\sum_{s=\ell}^u(N_s-M)_+ +\mathcal E.            \tag{6.3}
\]

No internal middle matching, adjacent disjointness, target-specific
quota choices, or cross-block cleanliness is required.

This is an explicit quadratic optimization over nonnegative integral
packet multiplicities. If `x_z` is the multiplicity of label `z`, put
`sum_z x_z=t`. Then

\[
 Q_s=\sum_{z,z'}x_zx_{z'}|S_s(z)\cap S_s(z')|-Lt.        \tag{6.4}
\]

The diagonal subtraction is important, including when a label is selected
more than once: (6.1) counts distinct packet instances, not distinct labels.

For completeness the full one-packet same-rank pair census is also closed
form. Put `n=2b-1` and, for `1<=d<=b`,

\[
 r_s(d)=s-(s-d)_+-(s-(n-d))_+.
\]

For `r>=1`, define

\[
 A_{s,r}=2\sum_{d=1}^b(L-d)\mathbf1_{\{r_s(d)=r\}}.
                                                               \tag{6.5}
\]

Two arcs whose start indices differ by `d` have the two possible overlap
lengths `(s-d)_+` and `(s-(n-d))_+`. There are `2(L-d)` ordered pairs of
designated starts at ordinary separation `d`. This proves (6.5). If
fixed rank-`s` targets `T,U` have Johnson distance `r`, permutation
transitivity consequently gives

\[
 \Pr(T,U\in S_s(z))
   =\frac{A_{s,r}}{N_s\binom sr\binom{2b-s}r}.          \tag{6.6}
\]

These formulas specify the rank-dependent packet kernel, rather than
replacing it by one maximum codegree. They do not prove a near-minimizing
integral choice in (6.4).

## 7. Capacity, Skipped Ranks, and Cylinder Completion

Now take `c=1` in (4.1). Let

\[
 \delta=1-M/W.
\]

Since `t=floor(W/D)`,

\[
 0\le\delta\le\frac{2H}{D}+\frac L W=O(H/b).            \tag{7.1}
\]

### Lemma 7.1

For `delta<=1/2`,

\[
 \sum_{s=\ell}^u(N_s-M)_+
     \le (4\sqrt{b\delta}+1)\delta W.                 \tag{7.2}
\]

#### Proof

For `0<=h<=b`,

\[
 \frac{N_{b+h}}W
 =\prod_{i=0}^{h-1}\left(1-\frac{2i+1}{b+i+1}\right)
 \le e^{-h^2/(2b)}.                                    \tag{7.3}
\]

If `N_(b+h)>(1-delta)W`, then
`h^2/(2b)<-log(1-delta)<=2delta`, hence
`|h|<2 sqrt(b delta)`. There are at most `4 sqrt(b delta)+1`
such integer offsets; each deficit is at most `delta W`. QED.

As a cube density this capacity term is

\[
 O(\delta^{3/2}+\delta/\sqrt b)=o(1),                   \tag{7.4}
\]

not the old `o(W)` requirement. In particular, Theorem 6.1 gives the
conditional implication

\[
 \boxed{\mathcal E=o(4^b)
 \quad\Longrightarrow\quad
  |B|\le W,\qquad g=o(4^b).}                           \tag{7.5}
\]

Here `B` is the actual nonempty concatenated word, not a fractional
incidence object.

There is a further optional weakening. For any set `J_b` of skipped band
ranks, put

\[
 \mathcal E_{\mathrm{keep}}=
       \sum_{s\in[\ell,u]\setminus J_b}\frac{E_s}{d(q_s)}.
\]

Counting all skipped targets as holes gives

\[
 \frac g{4^b}
 \le O\left(b^{-2}+\frac{|J_b|}{\sqrt b}
                  +\delta^{3/2}+\frac\delta{\sqrt b}\right)
       +\frac{\mathcal E_{\mathrm{keep}}}{4^b}.          \tag{7.6}
\]

Thus it suffices that `|J_b|=o(sqrt(b))` and
`E_keep=o(4^b)`. In particular all ranks with `N_s>M` can be omitted:
by the proof of Lemma 7.1 their number is

\[
 O(\sqrt{b\delta}+1)=O(\sqrt H+1)
   =O(b^{1/4}(\log b)^{1/4})=o(\sqrt b).                \tag{7.7}
\]

Then every retained `q_s` is at least one. The no-skipping estimate (7.4)
is quantitatively better but demands energy control on those ranks too.

To spell out the final conditional cost, let the right side of (7.6) be
bounded by `eta_b=o(1)`. The handoff's proved nonempty linear cylinder
completion, applied with

\[
 a_b=\left\lceil 2b\eta_b^{2/3}+\sqrt{2b}\right\rceil=o(b),
\]

constructs a universal word on `2b+a_b` coordinates with length at most

\[
 \left(1+O(\eta_b^{2/3}+b^{-1/2})\right)W(2b+a_b).      \tag{7.8}
\]

It uses `a_b` literal top-bit lifts of the already constructed word and
one isolated fiber block per old hole, so its exact pre-asymptotic cost is
`2^(a_b) |B| + g (nu(a_b)+1)`. Nonemptiness holds for all sufficiently
large `b`. The bases `2b` range over all sufficiently large even
dimensions; the relatively dense interpolation in Section 3.9 then gives
all dimensions. Nothing in (7.8) supplies the hypothesis `E_keep=o(4^b)`.

## 8. What Is Still Missing

The sufficient positive selector statement left by this note is:

> Choose `t=floor(W/(b+1+2H))` phase-packet labels, allowing arbitrary
> overlaps and repetitions, so that the weighted excess pair energy in
> (6.2), summed outside any `o(sqrt(b))` skipped ranks, is `o(4^b)`.

Equivalently, the total weighted pair intersection in (6.4) must approach
the sum of the rankwise integer minima to this density-scale accuracy.
The uniform fractional loads do not imply that those separate minima are
jointly integrally attainable.

For comparison, independent sampling has the exact formula

\[
 \mathbb E Q_s=t(t-1)L^2/N_s,                           \tag{8.1}
\]

not `Q_min,s+o(N_s)` throughout the Gaussian band. Its actual holes have
the positive limit in Theorem 4.1. The deterministic algorithm of
Section 3 is only proved to achieve the bound (3.2); it may do better,
but no vanishing-density estimate for it has been established here.

One must therefore prove a genuinely correlated integral selection, or
replace the sufficient energy condition by a weaker constructible
coverage condition. This note provides neither a global near-minimizer
nor a proof of coefficient one. It does provide actual exact-budget
words and a fully specified, Gaussian-normalized pair objective rather
than another unsupported growing-rank promotion.

## 9. Reproducible Checks

Run:

```sh
python3 scratch/gate_c_gaussian_packet_selector_energy_20260905_c7e42.py
```

The dependency-free checker verifies literal internal witnesses, the
undesignated-interval bound including joins, all-rank pair census (6.5),
the quadratic identities including repeated labels, the scalar energy
inequality on exhaustive small integer vectors, and an exact rational
conditional-expectation selector on six coordinates. It also evaluates
the Gaussian integral numerically and the exact expectation (4.5) in
larger dimensions. Finite tests corroborate the proofs and do not replace
the missing integral energy estimate.

Observed results: 60 literal concatenations, 19,530 exhaustive scalar load
vectors, and 598 all-rank pair censuses passed. The exact rational selector
at `b=3,H=1` chose three blocks of total length 18, against width 20, and
had 15 designated band holes versus the proved bound `4966/225`; the actual
word had 19 nonempty holes across all ranks. The larger-dimensional
expectations decrease toward (4.8), with substantial finite guard overhead:
at `b=2501`, `M/W=0.858024691...` and the exact designated expected hole
density is `0.285851693...`. These finite values are not evidence of
vanishing density.
