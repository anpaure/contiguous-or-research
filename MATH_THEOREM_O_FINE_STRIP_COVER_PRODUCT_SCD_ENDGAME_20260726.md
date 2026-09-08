# Fine strip cover plus product-SCD tail: the complete constant-one endgame

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 W=W_m=\binom{2m}m,
 \qquad
 N_1=\binom{2m}{m-1}=\frac m{m+1}W.                  \tag{0.1}
\]

Let `tau_(m,H,h)` be the integral labelled owner-recycling strip-cover
optimum from
`MATH_SYNTHESIS_FINE_STRIP_COVER_CONSTANT_ONE_20260726.md`.  Its exact
fractional value is

\[
 \boxed{
 \tau^*_{m,H,h}=W+\frac HhN_1.}                       \tag{0.2}
\]

Put

\[
 \varepsilon_m=
 \frac{\tau_{m,H,h}-\tau^*_{m,H,h}}W\ge0.            \tag{0.3}
\]

For every `1<=H<h<m`, the factor-blind product-SCD theorem gives the exact
finite implications

\[
 \boxed{
 \nu(2m)\le\tau_{m,H,h}+L_m(m-H-1),}                  \tag{0.4}
\]

and

\[
 \boxed{
 \nu(2m+1)\le2\tau_{m,H,h}+2L_m(m-H-1).}              \tag{0.5}
\]

Here one word of length `L_m(m-H-1)` already covers **both** even tails.
Only the trimmed odd lift produces the second factor `2`.

There is an absolute constant `C_0` for which

\[
 \frac{L_m(m-H-1)}W
 \le C_0e^{-H^2/(8m)}.                                 \tag{0.6}
\]

Consequently

\[
 \boxed{
 \frac{\nu(2m)}W
 \le1+\frac m{m+1}\frac Hh+\varepsilon_m
       +C_0e^{-H^2/(8m)}.}                             \tag{0.7}
\]

Thus the three conditions

\[
 \frac H{\sqrt m}\longrightarrow\infty,
 \qquad
 \frac Hh\longrightarrow0,
 \qquad
 \varepsilon_m\longrightarrow0                       \tag{0.8}
\]

imply

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.        \tag{0.9}
\]

An explicit admissible growing-window choice is

\[
 H_m=\left\lceil\sqrt{m\log m}\right\rceil,
 \qquad
 h_m=2^{\lceil(3/4)\log_2m\rceil}.                    \tag{0.10}
\]

If the strip-cover estimate is known only for each fixed Gaussian constant
`A`, a slow diagonal choice `H_m=ceil(A(m)sqrt(m))` is required instead;
this quantifier distinction is proved in Section 6.

The implication has no hidden seam, singleton, owner, Hall, or residual
cycle step.  Every selected strip and every singleton is already charged in
`tau`.  A cycle left outside that objective is **not** free: in the
owner-recycling architecture it costs its full literal length, not merely a
collar.  Section 8 states the precise residual-cycle alternatives.

## 1. The exact physical input

A cyclic `h`-strip on a `2m`-element ground set has middle states

\[
 X_t=K\cup I_z(t,h),
 \qquad t\in\mathbb Z/(2h),                            \tag{1.1}
\]

where `|K|=m-h` and `z_0,...,z_(2h-1)` are distinct active coordinates.
For `0<=q<=H<h`, its lower and upper targets are

\[
 L_t^q=K\cup I_z(t+q,h-q),
 \qquad
 U_t^q=K\cup I_z(t,h+q).                              \tag{1.2}
\]

The exact factor letters are

\[
 A_t=\bigcap_{j=0}^{H}X_{t+j}
    =K\cup I_z(t+H,h-H).                              \tag{1.3}
\]

They satisfy

\[
 \bigcup_{s=0}^{r}A_{t+s}
 =K\cup I_z(t+H,h-H+r)
 \qquad(0\le r\le2H).                                 \tag{1.4}
\]

Therefore the linear block

\[
 A_0,\ldots,A_{2h-1},A_0,\ldots,A_{2H-1}             \tag{1.5}
\]

has exact length

\[
                              2h+2H                   \tag{1.6}
\]

and literally realizes every target of that strip through depth `H`.
Every witness stays inside (1.5); no relation between two selected strips
is needed.

The integral cover program chooses whole strips with variables `x_C` and
literal central singletons with variables `z_S`.  Its exact objective is

\[
 (2h+2H)\sum_Cx_C+\sum_Sz_S.                          \tag{1.7}
\]

The constraints say that every target in ranks

\[
                              [m-H,m+H]                \tag{1.8}
\]

is contained in a chosen strip column or is selected as its own singleton.
Thus an integral feasible solution is already a literal central word.  The
same middle owner may occur in several chosen strips; this causes no logical
problem because every copy is paid for in (1.7).

## 2. Independent audit of the fractional normalization

Write

\[
 X=\sum_Cx_C,
 \qquad
 A=2hX,
 \qquad
 Z=\sum_Sz_S,
 \qquad
 \alpha=\frac Hh.                                     \tag{2.1}
\]

Here `A` is middle-owner **occurrence mass**, not the number of distinct
owners.  The exact integral objective is

\[
                              (1+\alpha)A+Z.            \tag{2.2}
\]

Summing the cover constraints over the middle layer and the two signed
depth-one layers gives

\[
 Z_0+A\ge W,
 \qquad
 Z_1^-+A\ge N_1,
 \qquad
 Z_1^++A\ge N_1.                                      \tag{2.3}
\]

Consequently every fractional solution has objective at least

\[
 (1+\alpha)A+(W-A)_++2(N_1-A)_+.                     \tag{2.4}
\]

For `0<=A<=N_1` the slope is `alpha-2<0`; for
`N_1<=A<=W` it is `alpha>0`; above `W` it remains positive.  Hence the
minimum is at `A=N_1` and equals

\[
                              W+\alpha N_1.            \tag{2.5}
\]

The transitive orbit solution attains it: give the strip orbit total cycle
weight `N_1/(2h)`, saturating each signed first-shadow target.  Deeper signed
layers are overcovered, while every middle target has load `N_1/W` and
receives singleton weight `1-N_1/W`.

The ledger at the optimum is therefore exactly

\[
 \underbrace{2h\frac{N_1}{2h}}_{N_1}
 +\underbrace{2H\frac{N_1}{2h}}_{(H/h)N_1}
 +\underbrace{(W-N_1)}_{W/(m+1)}
 =W+\frac HhN_1.                                      \tag{2.6}
\]

This proves all three delicate normalizations:

\[
 N_1=\frac m{m+1}W,
 \qquad
 W-N_1=\frac W{m+1},
 \qquad
 \text{collar}=\frac HhN_1.                           \tag{2.7}
\]

There is no missing factor `2` in the collar: one cycle has collar `2H`,
but the optimum has cycle mass `N_1/(2h)`.

## 3. What near-optimality forces

Suppose

\[
                 \tau_{m,H,h}\le W+\alpha N_1+\varepsilon_mW. \tag{3.1}
\]

Choose an optimal integral solution and use `A,Z` from (2.1).  Equations
(2.2)--(2.4) give

\[
 \boxed{
 (2-\alpha)(N_1-A)_+\le\varepsilon_mW.}               \tag{3.2}
\]

Also `Z>=0` gives

\[
 A\le\frac{W+\alpha N_1+\varepsilon_mW}{1+\alpha}
 \le W+\varepsilon_mW.                                \tag{3.3}
\]

If `epsilon_m->0`, then, since `N_1=W-W/(m+1)`,
(3.2)--(3.3) imply

\[
                              A=W+o(W).                 \tag{3.4}
\]

For `alpha<=1`, use the lower bound
`A>=N_1-epsilon_m W/(2-alpha)` in (2.2).  It gives

\[
 \boxed{
 Z\le\frac W{m+1}
 +\left(1+\frac{1+\alpha}{2-\alpha}\right)
   \varepsilon_mW
 \le\frac W{m+1}+3\varepsilon_mW.}                   \tag{3.5}
\]

Thus, when `epsilon_m->0`, every singleton repair—at every central rank,
not only the middle one—has total count `o(W)`.  If in addition
`alpha=H/h->0`, the total internal collar is independently

\[
 2HX=\alpha A=o(W).                                    \tag{3.6}
\]

These conclusions are audits, not extra hypotheses.  The finite endgame
below needs only the total objective bound (3.1), because that objective
already charges both the base cycle letters and every singleton.

## 4. Exact even compiler and the tail-rank audit

For completeness, retain the exact notation of the factor-blind tail
theorem.  If

\[
 A_m(a)=\binom ma-\binom m{a-1},
 \qquad
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}                                          \tag{4.1}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\[1mm]
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0,
 \end{cases}                                          \tag{4.2}
\]

then

\[
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).                                \tag{4.3}
\]

The product-SCD construction is a single word of this length and covers
both families

\[
                    |S|\le r
 \qquad\hbox{and}\qquad
                    |S|\ge2m-r.                      \tag{4.4}
\]

Take

\[
                              r=m-H-1.                 \tag{4.5}
\]

The lower exterior ends at rank `m-H-1`; the central strip cover starts at
rank `m-H`.  The central cover ends at rank `m+H`; the upper exterior starts
at

\[
                    2m-r=m+H+1.                       \tag{4.6}
\]

Thus the rank intervals are adjacent, with neither a gap nor a necessary
overlap:

\[
 [0,m-H-1]\ \dot\cup\ [m-H,m+H]\ \dot\cup\
 [m+H+1,2m].                                          \tag{4.7}
\]

The empty set in the first interval is immaterial because the definition
of `nu` asks only for nonempty masks.

Choose an optimal integral strip-cover solution.  Concatenate all of its
strip blocks (1.5) and singleton blocks, obtaining a central word `Q` of
length exactly `tau_(m,H,h)`.  Let `T` be the product-SCD exterior word of
length `L_m(m-H-1)`.  Every advertised witness lies wholly inside one
strip block, one singleton block, or one product-SCD gadget.  Consequently
the literal concatenation `Q || T` is universal; no separator letter and
no cross-seam witness is used.  This proves the exact finite statement

\[
 \boxed{
 \nu(2m)\le\tau_{m,H,h}+L_m(m-H-1).}                  \tag{4.8}
\]

The uniform product-SCD estimate is

\[
 L_m(m-H-1)
 \le C_0W\exp\!\left(-\frac{H^2}{8m}\right),         \tag{4.9}
\]

for an absolute `C_0`, with no moderate-deviation upper restriction on
`H`.  Substituting (0.2)--(0.3) into (4.8) gives

\[
 \boxed{
 \frac{\nu(2m)}W
 \le1+\frac m{m+1}\frac Hh+\varepsilon_m
      +C_0e^{-H^2/(8m)}.}                             \tag{4.10}
\]

This rank audit also identifies a common off-by-one error: choosing
`r=m-H` would make the tail overlap the two boundary ranks and is harmless
but weaker; choosing `r=m-H-2` would leave ranks `m-H-1` and `m+H+1`
uncovered.  The exact complementary index is (4.5).

## 5. An explicit admissible growing window

Set

\[
 H_m=\left\lceil\sqrt{m\log m}\right\rceil,
 \qquad
 h_m=2^{\lceil(3/4)\log_2m\rceil}.                   \tag{5.1}
\]

For all sufficiently large `m`,

\[
 m^{3/4}\le h_m<2m^{3/4}<m,
 \qquad
 1\le H_m<h_m,                                       \tag{5.2}
\]

and

\[
 \frac{H_m}{h_m}
 =O\!\left(m^{-1/4}\sqrt{\log m}\right)=o(1),
 \qquad
 \frac{H_m}{\sqrt m}\longrightarrow\infty.          \tag{5.3}
\]

Furthermore `H_m^2/m>=log m`, so (4.9) yields

\[
                 \frac{L_m(m-H_m-1)}W
                 \le C_0m^{-1/8}.                    \tag{5.4}
\]

Hence, if the owner-recycling strip theorem proves

\[
 \tau_{m,H_m,h_m}
 \le W+\frac{H_m}{h_m}N_1+\varepsilon_mW,
 \qquad \varepsilon_m\longrightarrow0,              \tag{5.5}
\]

then the completely explicit even conclusion is

\[
 \boxed{
 \nu(2m)\le W\left[
 1+\varepsilon_m
 +O\!\left(m^{-1/4}\sqrt{\log m}\right)
 +O(m^{-1/8})\right].}                               \tag{5.6}
\]

The dyadic choice of `h_m` is convenient if the strip construction needs
dyadic recursion.  Nothing in the compiler needs dyadicity; any integral
`h` satisfying `H/h=o(1)` and `h<m` gives the same implication.

## 6. The fixed-`A` quantifier and its diagonalization

There are two different hypotheses which must not be conflated.

The growing-window hypothesis directly supplies (5.5).  A weaker theorem
may instead say that, for every fixed positive integer `A`, with

\[
 H_{m,A}=\lceil A\sqrt m\rceil,
 \qquad h_m=2^{\lceil(3/4)\log_2m\rceil},             \tag{6.1}
\]

one has

\[
 \varepsilon_{m,A}:=
 \frac{\tau_{m,H_{m,A},h_m}
       -\tau^*_{m,H_{m,A},h_m}}W
 \longrightarrow0
 \quad(m\longrightarrow\infty)                      \tag{6.2}
\]

for that fixed `A`.  Statement (6.2) does not license substituting
`A=sqrt(log m)` into a nonuniform error term.  It does, however, imply the
needed result by diagonalization.

For each integer `j>=1`, choose increasing thresholds `M_j` so large that
whenever `m>=M_j`,

\[
 \varepsilon_{m,j}\le\frac1j,
 \qquad
 \lceil j\sqrt m\rceil<h_m.                           \tag{6.3}
\]

Define

\[
 A(m)=\max\{j\ge1:M_j\le m\text{ and }j\le m^{1/8}\},
 \qquad
 H_m=\lceil A(m)\sqrt m\rceil,                        \tag{6.4}
\]

using `A(m)=1` before the set becomes nonempty.  Every fixed `j` eventually
belongs to the set, so `A(m)->infinity`; by construction

\[
 \varepsilon_{m,A(m)}\le\frac1{A(m)}=o(1).            \tag{6.5}
\]

Also

\[
 \frac{H_m}{h_m}=O(A(m)m^{-1/4})=O(m^{-1/8})=o(1),   \tag{6.6}
\]

while

\[
 \frac{L_m(m-H_m-1)}W
 \le C_0e^{-A(m)^2/8}=o(1).                           \tag{6.7}
\]

Thus the fixed-`A` theorem, with no asserted uniformity in `A`, is enough.
What is essential is the order of quantifiers in (6.2) followed by the
explicit slow diagonal (6.4).

## 7. Odd parity: exact lift, normalization, and boundary halves

Let `Q=(Q_1,...,Q_N)` be any word on a `2m`-set and let `z` be a new
coordinate.  Its trimmed lift is

\[
 Q_1,\ldots,Q_N,\{z\},
 Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}.              \tag{7.1}
\]

It has exactly `2N` letters, not `2N+1`.  An old witness not ending at
`Q_N` translates to the final block.  If its witness is `Q_i,...,Q_N`,
then that suffix followed by `{z}` realizes its union with `z`.  Old
witnesses remain in the first copy, and `{z}` realizes itself.  Hence the
trimmed lift of a universal even word is a universal odd word.

Apply this to the complete even word `Q || T` from Section 4.  Its length is

\[
 \boxed{
 \nu(2m+1)\le
 2\tau_{m,H,h}+2L_m(m-H-1).}                          \tag{7.2}
\]

The same conclusion follows by lifting `Q` and `T` separately, but then a
rank-boundary detail must be recorded.  The lifted central word covers

* `z`-free ranks `m-H,...,m+H`, and
* `z`-containing ranks `m-H+1,...,m+H+1`.

Thus it does not by itself cover the `z`-containing half of rank `m-H` or
the `z`-free half of rank `m+H+1`.  These are precisely, respectively,

\[
 \{R\cup\{z\}:|R|=m-H-1\},
 \qquad
 \{R:|R|=m+H+1\},                                    \tag{7.3}
\]

of total size `2 binom(2m,m-H-1)`, and each is covered by the lifted even
exterior word.  This is why the correct odd proof lifts the complete even
construction (or both of its pieces), rather than invoking only a coarse
odd-rank slogan.

Let

\[
 W^{\rm odd}_m=\binom{2m+1}m
 =\frac{2m+1}{m+1}W=2W-\frac W{m+1}.                 \tag{7.4}
\]

Equations (0.2), (0.3), and (7.2) give the exact excess ledger

\[
 \boxed{
 \nu(2m+1)-W^{\rm odd}_m
 \le\frac W{m+1}
 +2\frac HhN_1+2\varepsilon_mW
 +2L_m(m-H-1).}                                      \tag{7.5}
\]

Equivalently,

\[
 \boxed{
 \frac{\nu(2m+1)}{W^{\rm odd}_m}
 \le\frac{2(m+1)}{2m+1}
 \left(
 1+\frac m{m+1}\frac Hh+\varepsilon_m
 +C_0e^{-H^2/(8m)}
 \right).}                                           \tag{7.6}
\]

The leading prefactor is `1+1/(2m+1)`.  Therefore either parameter regime
of Sections 5--6 gives `nu(2m+1)=(1+o(1))W_m^(odd)`.

Expanding (7.6), the exact normalized excess is bounded by

\[
 \frac1{2m+1}
 +\frac{2m}{2m+1}\frac Hh
 +\frac{2(m+1)}{2m+1}
  \left(\varepsilon_m+\frac{L_m(m-H-1)}W\right).      \tag{7.7}
\]

This displays separately the parity normalization, collar, integral-gap,
and product-tail terms.

## 8. Seams, singleton repairs, and residual cycles

### 8.1 Seams and singletons in the strip architecture

There are no unpaid seams.  A target is certified inside one physical
strip block or one singleton block; the exterior targets are certified
inside product-SCD gadgets.  Concatenating the blocks never destroys an
existing interval witness.  The seam charge in (4.8) is therefore exactly
zero.

All central holes, at all `2H+1` ranks, are variables of the same literal
singleton family in (1.7).  Their total number is `Z`, already paid in
`tau`.  Under near-optimality, (3.5) proves the audited quantitative bound

\[
 Z\le\frac W{m+1}+3\varepsilon_mW=o(W).               \tag{8.1}
\]

There is no later Hall matching or owner synchronization condition: an
integral feasible cover is itself a literal word, and repeated use of an
owner merely creates repeated paid letters.

### 8.2 The exact residual-cycle rule for owner recycling

In the owner-recycling strip program, a selected `2h`-strip costs its full
block length `2h+2H`.  Hence every strip—including one called
"residual" by an auxiliary construction—must either

1. occur among the variables counted by `tau`, at full cost `2h+2H`; or
2. be omitted, with all targets not otherwise covered repaired by the
   singleton variables counted by `tau`.

There is no third, free residual term.  If a purported proof of (5.5)
leaves `z` additional strips outside the objective and then appends their
blocks, the corrected finite bound has the extra term

\[
                         z(2h+2H).                    \tag{8.2}
\]

Since `H<h`, a sufficient and essentially exact count condition is

\[
                              hz=o(W).                 \tag{8.3}
\]

The weaker condition `Hz=o(W)` is not enough here: it pays only the
collars and omits the base `2hz` letters.

### 8.3 Why the exact-factor residual formula looks different

For comparison, in an owner-disjoint exact middle factor the baseline
`W` has already paid every middle owner once.  Only in that different
ledger may a retained residual cycle of owner mass `r_i` be charged merely
its `2H` collar.  The floor baseline in that statement is the following
exact one.  For `1<=q<=H`, put

\[
 N_q=\binom{2m}{m-q},
 \qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,
 \qquad
 S_H=\sum_{q=1}^H\frac1{c_q}.                         \tag{8.4}
\]

A balanced quota at signed depth `q` takes values in `{c_q,c_q+1}` and has
total mass exactly `W`.  If `mu_q^+` and `mu_q^-` are the two integral
occurrence histograms of the full pre-deletion factor, both of total mass
`W`, define

\[
 O_q^\pm=
 \min_{b_q}\sum_S(\mu_q^\pm(S)-b_q(S))_+,
 \qquad
 J_H=\sum_{q=1}^H\frac{O_q^-+O_q^+}{c_q},             \tag{8.5}
\]

where the minimum is over those balanced quotas.  Uniformly in `H<=m`,

\[
 S_H\le\frac{4^m}{W}-1=(\sqrt\pi+o(1))\sqrt m.       \tag{8.6}
\]

If the complete pre-deletion factor is `H`-safe and `J_H=o(W)`, the
factor-blind residual alternative is

\[
 2\sum_{i=1}^z\min\{H,r_iS_H\}
 \le2\min\{Hz,rS_H\},
 \qquad r=\sum_i r_i.                                 \tag{8.7}
\]

Thus that architecture may retain when `Hz=o(W)`, or delete when
`r=o(W/sqrt(m))`.  Without the balanced-floor
certificate, raw deletion costs at most `2Hr`, requiring
`r=o(W/H)`.  The collar-only alternative (8.7) cannot be imported into the
recycling objective without first identifying where its base owner mass
was paid.

Likewise, a bare uncertified recoupling cut can lose

\[
                       H(H+1)                         \tag{8.8}
\]

two-sided positive-depth shadow occurrences, besides its factor letters.
Thus a raw support-only estimate needs `b=o(W/H^2)` for `b` such cuts; a
balanced-floor transfer bounds the weighted damage by `O(mb)` and needs
`b=o(W/m)`.  A post-recoupling direct deficit measurement needs no separate
cut term.  If one instead transports a pre-recoupling overload certificate
across `s` changed successors, the factor-blind transfer charge is at most
`2ms`.

For a direct odd `X/Y` exact-factor construction, the corresponding
component choice is

\[
 \sum_i\min\{2H+1,r_i(1+2S_H)\};                     \tag{8.9}
\]

deletion includes the missing middle-shore term `r_i`.  The primary proof
of Section 7 does not use this direct odd architecture: it lifts the
complete even word.  Therefore every genuine even residual cost is simply
doubled, and no additional odd residual hypothesis is hidden.

## 9. Complete plug-in theorem and precise boundary

### Theorem 9.1 (owner-recycling strip cover implies constant one)

For each sufficiently large `m`, choose integers `1<=H_m<h_m<m`.  Assume
that the optimum of the integral labelled owner-recycling strip-cover
program of Section 1 satisfies

\[
 \tau_{m,H_m,h_m}
 \le W_m+\frac{H_m}{h_m}\binom{2m}{m-1}
       +\varepsilon_mW_m,                             \tag{9.1}
\]

where

\[
 \varepsilon_m\to0,
 \qquad
 \frac{H_m}{h_m}\to0,
 \qquad
 \frac{H_m}{\sqrt m}\to\infty.                      \tag{9.2}
\]

Then

\[
 \nu(2m)=(1+o(1))\binom{2m}m,
 \qquad
 \nu(2m+1)=(1+o(1))\binom{2m+1}m.                   \tag{9.3}
\]

The same conclusion holds if (9.1) is known for each fixed Gaussian
window and `H_m` is chosen by the diagonal construction of Section 6.

#### Proof

The exact upper bounds are (4.8) and (7.2).  Conditions (9.2), (4.9), and
(9.1) make every excess term in (4.10) and (7.6) `o(1)` after width
normalization.

For the reverse inequality, consider any universal word and choose one
witness interval for every set in a largest Boolean layer.  Two distinct
sets of that layer cannot have the same right endpoint: intervals with a
common right endpoint are nested, hence their unions are comparable,
whereas two distinct same-size sets are incomparable.  Therefore the word
has at least as many positions as that layer.  This gives

\[
 \nu(k)\ge\binom{k}{\lfloor k/2\rfloor}               \tag{9.4}
\]

for both parities and completes (9.3).  \(\square\)

### Audited logical boundary

The theorem above is a complete endgame implication, not a proof of the
strip-cover hypothesis (9.1).  Its premise is exactly the integral gap

\[
       \tau_{m,H,h}-\tau^*_{m,H,h}=o(W_m)              \tag{9.5}
\]

along an admissible growing window, or along the diagonal extracted from
fixed windows.  Fractional optimality alone does not prove (9.5).

Subject to that premise, every subsequent interface is now literal and
finite:

* `N_1=mW/(m+1)` and the fractional collar is exactly `(H/h)N_1`;
* the central strip word has exact objective length `tau`;
* the even tail begins at the exact index `r=m-H-1` and costs one `L_m`;
* all concatenation seams cost zero;
* all central singletons are already in `tau` and total `o(W)`;
* the trimmed odd lift costs exactly twice the complete even word;
* residual strips outside `tau` require the explicit correction (8.2).

Consequently there is no remaining parity, tail, seam, singleton, or
normalization gap after (9.5).  The only unproved mathematical gate in this
plug-in is the owner-recycling integral strip-cover bound itself.
