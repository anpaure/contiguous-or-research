# Phase-dense ternary carry as a direct contiguous-OR compiler: exact theorem and audit

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 W=\binom{2m}m.
\]

There is an exact factor-blind compiler for the long ternary-carry
components. If the good middle owners are partitioned into `K` cyclic
components of common length

\[
                         \lambda=2h3^t,                \tag{0.1}
\]

if the components satisfy the corrected delay condition through depth
`d`, and if

\[
 \Delta_d=\sum_{q=1}^d(M_q^-+M_q^+)                 \tag{0.2}
\]

is their actual aggregate signed hole count, then

\[
 \boxed{
 \nu(2m)\le
 W+2dK+\Delta_d+L_m(m-d-1).}                         \tag{0.3}
\]

For the ternary components,

\[
 \boxed{
 2dK={d\over h3^t}G,}                                \tag{0.4}
\]

where `G` is the good middle-owner mass. Thus the collar is paid once per
fused `2h3^t`-cycle, not once per `2h` phase lap. There is no middle-leave
penalty: appending the `W-G` omitted middle owners changes the retained base
length `G` to exactly `W`.

The complete-word trimmed lift gives

\[
 \boxed{
 \nu(2m+1)\le
 2\bigl[W+2dK+\Delta_d+L_m(m-d-1)\bigr].}            \tag{0.5}
\]

There is no second even-tail copy, no intercomponent seam, and no extra odd
singleton.

There is, however, an exact terminology trap.

* If cyclic `H`-geodesic means geodesic for every window of at most `H`
  transitions, it is one transition too weak for the advertised
  `lambda+2H` delay word.
* The full-depth formula needs the positive-dwell condition in Section 2;
  geodesicity through `H+1` transitions is a convenient stronger
  sufficient hypothesis.
* Ordinary cyclic `H`-geodesicity always permits the safe retreat `d=H-1`.
  Therefore it still gives

  \[
   \boxed{
   \nu(2m)\le
   W+2(H-1)K+\Delta_{H-1}+L_m(m-H).}                 \tag{0.6}
  \]

  When `H/sqrt(m)->infinity`, this one-depth retreat has no asymptotic
  cost.

Repeated directions on distant laps are not themselves a defect. Only a
physical coordinate return inside the protected dwell window can invalidate
the OR atoms. The current saved ternary-carry reports certify distinct
touched blocks through `q<=t`, with `H<=t`. This proves the full dwell
condition when `H<t`; the equality case `H=t` leaves the `H+1`-transition
endpoint unproved. One may use (0.6), or choose the protected depth strictly
below `t`.

Finally, the actual canonical first-`t` ternary carry does **not** satisfy
the hypothetical input (0.2). At

\[
 q_* = \lceil2\log_2h\rceil\le H,                    \tag{0.7}
\]

the audited all-target cut gives

\[
 M_{q_*}^-=W-o(W),
 \qquad
 M_{q_*}^+=W-o(W),                                   \tag{0.8}
\]

and hence `Delta_H>=2W-o(W)`. Thus the literal compiler is sound after the
one-step correction, but the present ternary atlas is not a constant-one
input. Its decisive failure is shadow support, not component length or
collar accounting.

## 1. The exact product-SCD exterior input

For later normalization define

\[
 A_m(a)=\binom ma-\binom m{a-1},                     \tag{1.1}
\]

\[
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}                                         \tag{1.2}
\]

and

\[
 C_m(s)=
 \begin{cases}
 0,&s<0,\\[1mm]
 \displaystyle\binom m{\min(s,\lfloor m/2\rfloor)},&s\ge0.
 \end{cases}                                         \tag{1.3}
\]

The factor-blind product-SCD word has exact length

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).}                               \tag{1.4}
\]

One such word covers both even-dimensional families

\[
                         |S|\le r
 \qquad\hbox{and}\qquad
                         |S|\ge2m-r.                  \tag{1.5}
\]

Moreover, for an absolute constant `C_0`,

\[
 \boxed{
 {L_m(m-d-1)\over W}
 \le C_0\exp\!\left(-{d^2\over8m}\right)}           \tag{1.6}
\]

uniformly for `0<=d<=m-1`. The leading `2` in (1.4) comes from the two
sides of a chain-pair gadget; it is already the length of one word covering
both tails.

At `r=m-d-1`, (1.5) is exactly

\[
 |S|\le m-d-1
 \qquad\hbox{or}\qquad
 |S|\ge m+d+1.                                       \tag{1.7}
\]

These are the two ranks exterior to the central band `[m-d,m+d]`.

## 2. The exact cyclic OR condition

Let

\[
 C=(X_i)_{i\in\mathbb Z/\lambda\mathbb Z},
 \qquad X_i\in\binom{[2m]}m,                          \tag{2.1}
\]

be an oriented cyclic Johnson row. For `0<=q<=d` write

\[
 L_{i,q}=\bigcap_{s=0}^qX_{i+s},
 \qquad
 U_{i,q}=\bigcup_{s=0}^qX_{i+s}.                     \tag{2.2}
\]

Two local conditions must be distinguished.

1. `G_d`: every cyclic segment of at most `d` transitions is a Johnson
   geodesic. Equivalently,

   \[
   |L_{i,q}|=m-q,
   \qquad |U_{i,q}|=m+q
   \quad(0\le q\le d).                               \tag{2.3}
   \]

2. `P_d`: in the cyclic binary row
   `(1_(x in X_i))_i`, every nonconstant positive run of every ground
   coordinate `x` has at least `d+1` states.

Condition `P_d` is the exact positive-dwell condition for the canonical
intersection atoms. The stronger statement that no coordinate changes
twice among any `d+1` consecutive transitions implies both `G_d` and
`P_d`, but also controls short zero-runs which the OR identity itself does
not need.

Define cyclic atoms

\[
                         B_j=\bigcap_{s=0}^dX_{j-s}.   \tag{2.4}
\]

### Lemma 2.1 (exact cyclic delay identities)

Assume `P_d`. For every `i` and every `0<=q<=d`,

\[
 \boxed{
 X_i=\bigcup_{j=i}^{i+d}B_j,}                         \tag{2.5}
\]

\[
 \boxed{
 L_{i,q}=\bigcup_{j=i+q}^{i+d}B_j,}                  \tag{2.6}
\]

and

\[
 \boxed{
 U_{i,q}=\bigcup_{j=i}^{i+q+d}B_j.}                  \tag{2.7}
\]

Conversely, the middle identities (2.5) for every `i` force `P_d`.

#### Proof

Fix a coordinate `x`. If `x` belongs to `X_i`, its positive run has at
least `d+1` states. That run therefore contains a block of `d+1`
consecutive one-states containing `i`; its right endpoint is some
`j in [i,i+d]`. Hence `x in B_j`. Conversely every atom in the right
side of (2.5) uses a defining window containing `i`. This proves (2.5)
coordinatewise.

Suppose next that `x` belongs throughout `[i,i+q]`. Its positive run again
contains a `d+1`-state subinterval which contains this entire shorter
interval. The right endpoint of such a subinterval can be chosen in
`[i+q,i+d]`. Every defining window with endpoint in this range contains
`[i,i+q]`. This proves (2.6).

Finally take the union of (2.5) over the states
`X_i,...,X_(i+q)`. The union of the atom-index intervals
`[i+s,i+s+d]` is `[i,i+q+d]`, proving (2.7).

For necessity, if a positive coordinate run has length at most `d`, no
`d+1`-state defining window inside that run contains the coordinate.
Thus no `B_j` contains it, while some `X_i` does, contradicting (2.5).
\(\square\)

Assume now `G_d` as well. Then every atom (2.4) has rank `m-d` and is
nonempty because `d<m`. If `lambda>2d`, the linear word

\[
 \boxed{
 \mathcal W_d(C)=
 B_0,B_1,\ldots,B_{\lambda-1},B_0,B_1,\ldots,B_{2d-1}}             \tag{2.8}
\]

has exact length

\[
                              \lambda+2d.             \tag{2.9}
\]

The longest witness in (2.5)--(2.7) has `2d+1` atoms. The copied prefix
therefore turns every cyclic witness into an ordinary contiguous interval.
There is no cut exception and no internal lap seam.

### The off-by-one counterexample

Ordinary `G_H` does not imply `P_H`. Take `H` disjoint coordinate pairs
`{a_i,b_i}` and a fixed core `K` of size `m-H`. In the associated
isometric `Q_H`, follow the cyclic direction word

\[
                         1,2,\ldots,H,1,2,\ldots,H.   \tag{2.10}
\]

This is a physical `C_(2H)` in the middle layer. Every `H` consecutive
transitions use each direction once, so every segment of at most `H`
transitions is geodesic. Yet each active coordinate has a positive run of
exactly `H` states. Consequently every atom

\[
                    \bigcap_{s=0}^HX_{j-s}
\]

equals the fixed core `K`; their unions cannot recover even one middle
owner. Thus a proof which inserts only `G_H` into the `lambda+2H` atom
word is false.

On the other hand, `G_H` forces every positive run to have at least `H`
states. Therefore

\[
                         G_H\Longrightarrow P_{H-1}.  \tag{2.11}
\]

Together with `G_(H-1)`, this proves the safe one-depth retreat used in
(0.6).

## 3. Exact factor-blind cycle compiler

The next statement permits arbitrary component lengths and even middle
overload. Let \(\mathcal C\) be a multiset of cycles satisfying `G_d` and
`P_d`, with `lambda_C>2d` for every component. Put

\[
 P=\sum_{C\in\mathcal C}\lambda_C,
 \qquad K=|\mathcal C|.                              \tag{3.1}
\]

Let `mu_0(S)` be the middle occurrence multiplicity and define

\[
 M_0=|\{S\in\tbinom{[2m]}m:\mu_0(S)=0\}|,
 \qquad
 E_0=\sum_{|S|=m}(\mu_0(S)-1)_+.                     \tag{3.2}
\]

Mass conservation gives

\[
                         P=W-M_0+E_0.                 \tag{3.3}
\]

For `1<=q<=d`, let `M_q^-` and `M_q^+` be the actual numbers of targets in
ranks `m-q` and `m+q`, respectively, absent from all cyclic flags (2.2),
and define `Delta_d` by (0.2).

### Theorem 3.1 (exact finite cycle/tail compiler)

Under the preceding hypotheses,

\[
 \boxed{
 \begin{aligned}
 \nu(2m)
 &\le P+2dK+M_0+\Delta_d+L_m(m-d-1)\\
 &=W+E_0+2dK+\Delta_d+L_m(m-d-1).
 \end{aligned}}                                      \tag{3.4}
\]

#### Proof

Use (2.8) for every cycle. Their total literal length is `P+2dK` and they
cover every represented flag in ranks `[m-d,m+d]`, including their middle
owners. Append every missing middle owner once, at cost `M_0`, and append
every missing signed target once, at cost `Delta_d`. All central ranks are
now covered. Append the one product-SCD word from Section 1. It covers
both exterior tails.

Every advertised witness lies wholly within one cycle word, one singleton,
or one product-SCD gadget. Concatenation preserves all of them, so the
interblock and central-tail seam cost is exactly zero. Equation (3.3)
gives the second line of (3.4). \(\square\)

This formula exposes an important scope point. A holes-only hypothesis is
not sufficient for an owner-recycling multicover: one must also have
`E_0=o(W)`. Doubling an exact factor has no middle holes but has
`E_0=W`, and indeed costs leading constant two. In the ternary-carry
application the good cycles are owner-disjoint, so `E_0=0`.

### Corollary 3.2 (owner-disjoint near-factor)

Suppose the cycles partition `G=W-u` distinct middle owners. Then

\[
 P=G,
 \qquad M_0=u,
 \qquad E_0=0,                                       \tag{3.5}
\]

and hence

\[
 \boxed{
 \nu(2m)\le
 W+2dK+\Delta_d+L_m(m-d-1).}                         \tag{3.6}
\]

The cancellation

\[
                         G+u=W                       \tag{3.7}
\]

is exact. In particular, the middle leave never costs `du`; all
positive-depth damage caused by that leave is already measured in the
actual holes `Delta_d`.

For common ternary length (0.1),

\[
 K={G\over2h3^t},
 \qquad
 \boxed{2dK={d\over h3^t}G}.                         \tag{3.8}
\]

The fused component is cut once. Cutting separately at all `3^t` phase
laps would replace the correct collar `2dK` by an unnecessarily larger
ledger and is not part of the construction.

Arbitrary safe residual cycles require no new theorem. If the main cycles
have common length `2h3^t` and `z` additional owner-disjoint safe cycles are
retained, their exact collar contribution is `2dz`; hence the total collar
is

\[
                  {d\over h3^t}G_{\rm main}+2dz.      \tag{3.9}
\]

The count-only sufficient condition is `dz=o(W)`. If a residual cycle is
deleted, append its middle owners once; their base mass again cancels, while
every lost positive-depth target is charged in the recomputed `Delta_d`.

## 4. Constant-one consequence and both parities

### Theorem 4.1 (conditional ternary-carry plug-in)

Suppose, for every sufficiently large `m`, that an owner-disjoint family of
ternary-carry cycles has good mass `G`, common length `2h3^t`, and is safe
through depth `d` in the sense `G_d+P_d`. Assume

\[
 {d\over\sqrt m}\longrightarrow\infty,
 \qquad
 {d\over h3^t}\longrightarrow0,
 \qquad
 {\Delta_d\over W}\longrightarrow0.                 \tag{4.1}
\]

Then

\[
 \nu(2m)=(1+o(1))W.                                  \tag{4.2}
\]

#### Proof

Equations (1.6), (3.6), and (3.8) give

\[
 {\nu(2m)\over W}
 \le1+{d\over h3^t}{G\over W}
       +{\Delta_d\over W}
       +C_0e^{-d^2/(8m)}
 =1+o(1).                                             \tag{4.3}
\]

The middle-layer endpoint injection gives the reverse inequality.
\(\square\)

For odd dimension, let `Q=(Q_1,...,Q_N)` be the entire even word furnished
by Theorem 3.1 and introduce a new coordinate `z`. The trimmed lift

\[
 Q_1,\ldots,Q_N,\{z\},
 Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}              \tag{4.4}
\]

has exactly `2N` letters. Old witnesses remain in the first block. A
translated witness not using `Q_N` lies in the last block; if an old witness
ends at `Q_N`, its suffix followed by `{z}` realizes the translated target.
Thus (4.4) is universal whenever `Q` is.

Writing

\[
 W_o=\binom{2m+1}m
 ={2m+1\over m+1}W
 =2W-{W\over m+1},                                   \tag{4.5}
\]

the exact odd ledger in the owner-disjoint case is

\[
 \boxed{
 \begin{aligned}
 \nu(2m+1)
 &\le2\bigl[W+2dK+\Delta_d+L_m(m-d-1)\bigr],\\
 \nu(2m+1)-W_o
 &\le {W\over m+1}+4dK+2\Delta_d+2L_m(m-d-1).
 \end{aligned}}                                      \tag{4.6}
\]

There is no `+1`: the central singleton `{z}` is offset by omitting the
last translated letter in (4.4). If central and tail pieces are lifted
separately, the lifted central word covers the `z`-free ranks
`[m-d,m+d]` and the `z`-containing ranks `[m-d+1,m+d+1]`. The lifted tail
supplies exactly the missing `z`-containing half of rank `m-d` and the
`z`-free half of rank `m+d+1`. Lifting the complete even word makes this
boundary audit automatic.

The largest-layer endpoint injection gives

\[
 \nu(k)\ge\binom{k}{\lfloor k/2\rfloor}.             \tag{4.7}
\]

Indeed, witness intervals with one right endpoint are nested, so their ORs
are comparable; two distinct sets in one largest layer are incomparable.
Combining (4.3), (4.6), and (4.7) proves constant one for both parities.

### Corollary 4.2 (what ordinary cyclic `H`-geodesicity suffices for)

Suppose only `G_H`, and suppose the aggregate physical holes through depth
`H` satisfy

\[
                         \Delta_H=o(W).               \tag{4.8}
\]

Apply Theorem 3.1 with `d=H-1`. By (2.11) the atom condition holds, and
`Delta_(H-1)<=Delta_H`. Therefore the exact finite bound is

\[
 \boxed{
 \nu(2m)\le
 W+{H-1\over h3^t}G
 +\Delta_{H-1}+L_m(m-H).}                            \tag{4.9}
\]

The tail is now the word with effective central half-width `H-1`, and

\[
 {L_m(m-H)\over W}
 \le C_0\exp\!\left(-{(H-1)^2\over8m}\right).        \tag{4.10}
\]

Thus `H/sqrt(m)->infinity`, `Delta_H=o(W)`, and
`(H-1)/(h3^t)=o(1)` still imply constant one. Ordinary cyclic
`H`-geodesicity is therefore enough for the asymptotic theorem, but not for
the literal full-depth `lambda+2H` identity.

## 5. Audit of the ternary-carry laps and collars

In the saved phase-dense construction,

\[
 t\text{ is a power of two},
 \qquad h=2t,
 \qquad H\le t<2H.                                   \tag{5.1}
\]

One canonical macrocell has `24^t` middle owners. The ternary odometer
fuses the static components into cycles of length

\[
                         2h3^t=4t3^t.                 \tag{5.2}
\]

The exact number of fused cycles in one macrocell is

\[
 {24^t\over4t3^t}={8^t\over4t},                      \tag{5.3}
\]

an integer because `t` is a power of two. Hence the global component
count on good mass `G` is exactly

\[
                         K={G\over2h3^t}.             \tag{5.4}
\]

The full collar is consequently

\[
 \boxed{
 2HK={H\over h3^t}G={H\over2t3^t}G.}                \tag{5.5}
\]

It is neither `(H/h)G` nor `(2H/h)G`. Those expressions treat every
phase lap as a separately cut component and discard the whole benefit of
ternary fusion.

The local OR proof never asks that a direction be globally fresh. It asks
only for `P_H`, a lower bound on the return time of a physical coordinate
to the opposite state. Thus a direction repeated after many laps is
harmless. A return which creates a positive run of length at most `H`
destroys (2.5), regardless of the total component length.

The cited carry facts say that every `q<=t` consecutive transitions touch
`q` distinct selected eight-blocks. Therefore:

* if `H<t`, every `H+1`-transition window touches distinct disjoint blocks,
  so no coordinate can change twice there and `P_H` is certified;
* if `H=t`, the cited theorem controls only `H` transitions. The next
  transition repeats a block, and the saved reports do not give the
  complete physical coordinate-return ledger needed to prove `P_H` after
  every possible ternary shore switch.

This is a genuine all-`m` endpoint gap in the unqualified inference from
cyclic `H`-geodesicity to the `2H` collar. It has two exact repairs:

1. retain the original parameters and use the `H-1` compiler (4.9); or
2. choose the protected depth strictly below the power `t`.

A third, less economical repair is to cut before every short positive run.
If `rho_H` cuts are needed, a support-blind ledger charges `H rho_H`
factor letters and at most

\[
             2\sum_{q=1}^Hq\,\rho_H=H(H+1)\rho_H    \tag{5.6}
\]

lost signed windows. The total correction is therefore

\[
                         (H^2+2H)\rho_H.              \tag{5.7}
\]

This is `o(W)` only under `rho_H=o(W/H^2)`. The saved carry theorem gives
no such short-run count, so a cut repair cannot be inserted silently.

For example, put

\[
 R_m=\left\lceil\sqrt{m\log m}\right\rceil,
 \quad
 t_m=2^{\lceil\log_2(R_m+1)\rceil},
 \quad
 H_m=t_m-1,
 \quad
 h_m=2t_m.                                            \tag{5.8}
\]

Then `t_m` is a power of two,

\[
 R_m\le H_m<t_m<2H_m,
 \qquad
 {H_m\over\sqrt m}\to\infty,
 \qquad h_m=o(m),                                    \tag{5.9}
\]

and

\[
 {H_m\over h_m3^{t_m}}\le{1\over2\,3^{t_m}}=o(1),
 \qquad
 {L_m(m-H_m-1)\over W}\le C_0m^{-1/8}.              \tag{5.10}
\]

Also `2h_m3^(t_m)=exp(o(m))`, so the component length is far below the
Boolean width scale. These are fully admissible compiler parameters if a
future transverse atlas supplies `Delta_(H_m)=o(W)`.

## 6. The actual logarithmic hole obstruction

It remains to check whether the present carry supplies that last premise.
It does not.

For one canonical macrocell \(\mathcal M\), every legal saved ternary-carry
menu alternative has physical signed depth-`q` image bounded by

\[
 |\operatorname{im}\tau_{q}^{\pm}|
 \le |\mathcal M|\,\eta_{h,q},
 \qquad
 \eta_{h,q}
 ={h\over2^q}
 +{3q(1-3^{-t})\over4h}.                             \tag{6.1}
\]

The first term is the common-order Hamming support; the second is the
largest possible new support created by the changed carry edges. At
`q_*` from (0.7),

\[
                         \eta_{h,q_*}
 =O\!\left({\log h\over h}\right)=o(1).              \tag{6.2}
\]

The good macrocells have total mass `G=W-u`, with
\(u\le e^{-cm}W=o(W)\) for some absolute `c>0`.
Summing (6.1) over them and allowing every bad owner to hit a new target
shows that the total hit set on either sign has size at most

\[
                         G\eta_{h,q_*}+u=o(W).         \tag{6.3}
\]

Since `q_*=O(log h)=o(sqrt(m))`,

\[
 {\binom{2m}{m-q_*}\over W}
 =\exp\!\left(-{q_*^2\over m}
       +O\!\left({q_*\over m}+{q_*^3\over m^2}\right)\right)
 =1-o(1).                                             \tag{6.4}
\]

Equations (6.3)--(6.4) prove independently that

\[
 \boxed{
 M_{q_*}^-=W-o(W),
 \qquad
 M_{q_*}^+=W-o(W),
 \qquad
 \Delta_H\ge2W-o(W).}                               \tag{6.5}
\]

Moving only depth `H` into the exterior by (4.9) cannot hide this defect,
because `q_*<H-1` for large `H`. Nor can the product tail cover this
interior logarithmic rank at `o(W)` cost: its layer itself has size
`(1-o(1))W`.

## 7. Precise proved/conditional boundary

The audit therefore separates three statements.

1. **Proved literal theorem.** Cyclic `G_d+P_d` components compile in
   exact length `sum_C(lambda_C+2d)`. With actual holes, middle leave, and
   product tails included, the exact finite bounds are (3.4), (3.6), and
   (4.6).

2. **Proved weak-geodesic repair.** Ordinary cyclic `H`-geodesicity
   compiles safely through `H-1`, giving (4.9). Hence a hypothetical
   aggregate-hole theorem `Delta_H=o(W)` would compose to constant one
   without any further seam or parity input.

3. **Refuted application to the current atlas.** The present canonical
   ternary carry has the exact middle factor, exponentially long fused
   components, and negligible collar, but (6.5) contradicts the required
   aggregate-hole premise. In addition, a full-depth `2H` collar claim at
   the equality parameter `t=H` needs a positive-dwell proof not present in
   the cited construction.

Thus there is no factor-blind compiler obstruction after the precise
one-depth correction. The surviving construction problem is a new
coordinate-transverse or trace-rainbow ternary atlas whose actual
consecutive signed target holes total `o(W)`.
