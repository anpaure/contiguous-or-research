# Parent-transversal replacement against exact residual capacities

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let `C` be an aligned parent hole of size `r+1`.  A
`D_(r+1)`-port-transversal exact local factor can be installed in `C` while
fixing the two parent boundary states and preserving the exact middle
ledgers.  At depth `r`, exactly `2r` rooted window slots per parent row
can depend on the installed local factor.  Since the parent packet has
`Cat_(r+1)` rows, its potential affected-window multiplicity is exactly

\[
                         L_r=2r\operatorname {Cat}_{r+1}.       \tag{0.1}
\]

Remove the old targets in these slots from the ambient depth-`r`
histogram and call the remaining load `beta`.  If `u_G` is the histogram
put back by a local factor `G`, then the new load is literally

\[
                              \mu^G=\beta+u_G.                   \tag{0.2}
\]

Thus the correct capacity available to `G` at a target `S` is not the
uniform cap `p`, but

\[
                              c_\beta(S)=(p-\beta(S))_+.         \tag{0.3}
\]

The cap overload and the direct missing-shadow count have the exact
forms

\[
 \boxed{
 K_r(F[C\leftarrow G])
 =K_p(\beta)+\sum_S(u_G(S)-c_\beta(S))_+,}               \tag{0.4}
\]

\[
 \boxed{
 M_r(F[C\leftarrow G])
 =|\{S:\beta(S)=0\}|-
   |\{S:\beta(S)=0,\ u_G(S)>0\}|.}                     \tag{0.5}
\]

Consequently a library must disperse the **full affected-window
profile** into the residual capacities (0.3), while retaining targets
which were covered only by the old parent packet.  Bounding only the
largest packet of distinguished child windows by `p` tests neither
condition.

The identities below also give a state-adaptive iteration theorem which
does not assume additivity of different parent replacements.

---

## 1. Setup and the exact affected-window count

Put

\[
 p=2m+1,\qquad W=\binom p m,\qquad
 \mathcal V_r=\binom{[p]}{m-r},\qquad N_r=|\mathcal V_r|. \tag{1.1}
\]

For an exact middle factor `F`, let

\[
 \mu_r^F(S)=
 \#\{\hbox{rooted depth-`r` windows of `F` with target }S\}. \tag{1.2}
\]

There is one rooted depth-`r` window per middle state, hence

\[
                              \sum_S\mu_r^F(S)=W.                \tag{1.3}
\]

Let `s=r+1`, and let `C` be an aligned size-`s` parent context.  Its
canonical packet has one row for each member of `D_s`, hence exactly
`Cat_s` rows.  Indeed a local exact factor on `2s+1` coordinates has

\[
 {1\over2s+1}\binom{2s+1}s=\operatorname {Cat}_s          \tag{1.4}
\]

wreaths.  If it is `D_s`-port-transversal, exact ownership and
`|D_s|=Cat_s` make the unique-root map a bijection from its wreaths to
`D_s`.  After choosing the compatible orientation, the local trace
rooted at `P in D_s` has the same two boundary states as the canonical
trace rooted at `P`.

Index the states in the parent slab by

\[
                              X_0,X_1,\ldots,X_s.                \tag{1.5}
\]

Only `X_1,...,X_(s-1)=X_r` may change.  A rooted depth-`r` target is the
intersection of `r+1` consecutive middle states.  A start `j` can see an
interior state exactly when

\[
                 [j,j+r]\cap[1,r]\ne\varnothing,
 \quad\hbox{equivalently}\quad 1-r\le j\le r.             \tag{1.6}
\]

There are exactly `2r` such starts.  They are distinct modulo `p`, since
`2r<p`.  Therefore the fixed set of potentially affected slots is

\[
 \mathcal I_C=D_s\times\{1-r,2-r,\ldots,r\},
 \qquad |\mathcal I_C|=2r\operatorname {Cat}_{r+1}.       \tag{1.7}
\]

Every rooted window outside `mathcal I_C` has exactly the same sequence
of middle states before and after the substitution.

For an oriented `D_s`-port-transversal factor `G`, define

\[
 u_G(S)=\#\{(P,j)\in\mathcal I_C:
       \hbox{the installed trace has depth-`r` target }S\}. \tag{1.8}
\]

Thus

\[
                         \sum_Su_G(S)=L_r                 \tag{1.9}
\]

for every library member, including the old local factor `G_0`.

### Lemma 1.1 (literal histogram substitution)

Define

\[
                         \beta(S)=\mu_r^F(S)-u_{G_0}(S). \tag{1.10}
\]

Then `beta(S)>=0` for every target and

\[
 \boxed{
 \mu_r^{F[C\leftarrow G]}(S)=\beta(S)+u_G(S)
 \quad(S\in\mathcal V_r).}                              \tag{1.11}
\]

#### Proof

The old slots `mathcal I_C` contribute `u_(G_0)` to the old histogram,
so (1.10) is the histogram of all remaining rooted windows.  Those
remaining windows are unchanged.  The same slots contribute `u_G` after
the substitution.  Adding the two disjoint occurrence sets proves
(1.11).  \(\square\)

---

## 2. Exact cap and shadow identities

For any nonnegative load `x`, write

\[
                              K_p(x)=\sum_S(x(S)-p)_+.    \tag{2.1}
\]

Put

\[
                              c_\beta(S)=(p-\beta(S))_+  \tag{2.2}
\]

and define the residual-capacity defect of a library member by

\[
                 E_\beta(G)=\sum_S(u_G(S)-c_\beta(S))_+. \tag{2.3}
\]

### Theorem 2.1 (residual-capacity identity)

For every oriented `D_(r+1)`-port-transversal substitute `G`,

\[
 \boxed{
 K_r(F[C\leftarrow G])=K_p(\beta)+E_\beta(G).}           \tag{2.4}
\]

In particular,

\[
 \boxed{
 K_r(F[C\leftarrow G])-K_r(F)
             =E_\beta(G)-E_\beta(G_0).}                 \tag{2.5}
\]

#### Proof

For nonnegative integers `a,x`, the scalar identity

\[
 (a+x-p)_+=(a-p)_+ +\bigl(x-(p-a)_+\bigr)_+             \tag{2.6}
\]

holds.  If `a>=p`, both sides equal `a+x-p`; if `a<p`, both
sides equal `(x-(p-a))_+`.  Apply (2.6) with
`a=beta(S)`, `x=u_G(S)`, and sum.  Equation (2.5) follows by using
`G=G_0` for the old factor.  \(\square\)

Let

\[
 B_r=W-N_r,\qquad
 P_r(F)=\bigl(K_r(F)-B_r\bigr)_+                         \tag{2.7}
\]

be the exact depth-`r` summand of `PCap_H`.

### Corollary 2.2 (the floor is retained exactly)

One has

\[
 \boxed{
 P_r(F[C\leftarrow G])
  =\bigl[K_p(\beta)+E_\beta(G)-B_r\bigr]_+.}            \tag{2.8}
\]

If `E_beta(G)<=E_beta(G_0)`, then

\[
 \boxed{
 P_r(F)-P_r(F[C\leftarrow G])
 =\min\{E_\beta(G_0)-E_\beta(G),\ P_r(F)\}.}            \tag{2.9}
\]

Moreover every subsequent assignment of powers of a coordinate
`p`-cycle obeys

\[
 \boxed{
 H_r\bigl((F[C\leftarrow G])_a\bigr)
 \ge\bigl[K_p(\beta)+E_\beta(G)-B_r\bigr]_+.}           \tag{2.10}
\]

#### Proof

Equation (2.8) is (2.4) and the definition (2.7).  If
`d=E_beta(G_0)-E_beta(G)>=0`, the scalar identity

\[
                              x_+-(x-d)_+=\min\{d,x_+\}  \tag{2.11}
\]

proves (2.9).  For (2.10), the occurrences of one source target can
cover at most `p` members of its translation orbit.  Hence at most

\[
                   \sum_S\min\{\mu_r(S),p\}=W-K_r       \tag{2.12}
\]

targets can be covered.  Subtract from `N_r`, take a positive part, and
use (2.4).  \(\square\)

Now let

\[
                              M_r(F)=|\{S:\mu_r^F(S)=0\}|. \tag{2.13}
\]

Define the targets supported exclusively by the old parent cylinder and
the old holes by

\[
\begin{aligned}
 P_0&=\{S:\beta(S)=0,\ u_{G_0}(S)>0\},\\
 Z_0&=\{S:\beta(S)=0,\ u_{G_0}(S)=0\}.
\end{aligned}                                             \tag{2.14}
\]

### Theorem 2.3 (exact created-hole/filled-hole ledger)

For every substitute `G`,

\[
\boxed{
\begin{aligned}
 M_r(F[C\leftarrow G])-M_r(F)
 ={}&|\{S\in P_0:u_G(S)=0\}|\\
    &-|\{S\in Z_0:u_G(S)>0\}|.
\end{aligned}}                                            \tag{2.15}
\]

Equivalently, if

\[
                 C_\beta(G)=|\{S:\beta(S)=0,\ u_G(S)>0\}|, \tag{2.16}
\]

then

\[
 \boxed{
 M_r(F[C\leftarrow G])
 =|\{S:\beta(S)=0\}|-C_\beta(G),}                       \tag{2.17}
\]

and the change is `C_beta(G_0)-C_beta(G)`.

#### Proof

A nonnegative sum `beta(S)+u_G(S)` vanishes exactly when both summands
vanish.  This proves (2.17).  Partition the set `\{beta=0\}` according
to whether `u_(G_0)` is positive or zero and subtract the old expression;
the two resulting terms are exactly (2.15).  \(\square\)

---

## 3. Sharp universal movement inequalities

Identify every slot in `mathcal I_C` before and after the substitution.
Let

\[
 T_G(S,T)=\#\{I\in\mathcal I_C:
       \text{old target }S,\ \text{new target }T\}       \tag{3.1}
\]

and put

\[
                 \operatorname {Mov}_C(G)
                    =\sum_{S\ne T}T_G(S,T).              \tag{3.2}
\]

The row and column sums of `T_G` are `u_(G_0)` and `u_G`; therefore

\[
 {1\over2}\|u_G-u_{G_0}\|_1
 \le\operatorname {Mov}_C(G)
 \le2r\operatorname {Cat}_{r+1}.                        \tag{3.3}
\]

### Proposition 3.1 (one-parent Lipschitz bounds)

For every substitute `G`,

\[
 \boxed{
 \begin{aligned}
 |K_r(F[C\leftarrow G])-K_r(F)|
      &\le {1\over2}\|u_G-u_{G_0}\|_1,\\
 |P_r(F[C\leftarrow G])-P_r(F)|
      &\le {1\over2}\|u_G-u_{G_0}\|_1,\\
 |M_r(F[C\leftarrow G])-M_r(F)|
      &\le {1\over2}\|u_G-u_{G_0}\|_1.
 \end{aligned}}                                           \tag{3.4}
\]

In particular every displayed quantity changes by at most
`2r Cat_(r+1)`.

#### Proof

Put `Delta=u_G-u_(G_0)`.  Its coordinate sum is zero.  Since the hinge
has slopes in `[0,1]`,

\[
 K_p(\mu+\Delta)-K_p(\mu)
 \le\sum_{\Delta(S)>0}\Delta(S)
 ={1\over2}\|\Delta\|_1.                                \tag{3.5}
\]

Interchanging the two loads gives the first bound.  The map
`x -> (x-B_r)_+` is one-Lipschitz, proving the second.  Every filled old
hole consumes a positive unit of `Delta`, and every newly created hole
consumes a negative unit.  Thus each of the two counts is at most one
half of `||Delta||_1`, and so is the absolute difference between them.
This proves the third bound.  Equation (3.3) completes the proof.
\(\square\)

Consequently every later row-power lift satisfies the completely
unconditional floor bound

\[
 H_r\bigl((F[C\leftarrow G])_a\bigr)
 \ge
 \left[K_r(F)-2r\operatorname {Cat}_{r+1}-(W-N_r)\right]_+ . \tag{3.6}
\]

---

## 4. What the local endpoint map controls

For a rooted local wreath `P in D_s`, write its oriented Johnson
geodesic as

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
       \cup\{b_1,\ldots,b_t\},\qquad 0\le t\le s,        \tag{4.1}
\]

where `(a_1,...,a_s)` orders `P` and `(b_1,...,b_s)` orders its
complement in the `2s` parent coordinates.  The two intrinsic depth-`r`
windows have exact local targets

\[
 \bigcap_{t=0}^{s-1}X_t=\{a_s\},\qquad
 \bigcap_{t=1}^{s}X_t=\{b_1\}.                           \tag{4.2}
\]

Indeed every `a_i` with `i<s` has already been deleted from the first
intersection, while `a_s` is still present; the second assertion is the
dual statement for the first inserted coordinate.

Thus a library's distinguished child-fibre profile is a restriction of
the two endpoint maps

\[
                              P\longmapsto a_s(P),\ b_1(P). \tag{4.3}
\]

This is useful but not the full profile `u_G`.  Even if both intrinsic
starts are controlled, there remain `2r-2` crossing starts per parent row
in (1.7).  Moreover the capacity at the physical target
`O_C union {i}` is `c_beta(O_C union {i})`, which may be strictly less
than `p` because of load from other contexts.

Therefore the condition

\[
 \max_i|\{P\text{ in a child fibre}:a_s(P)=i\}|\le p      \tag{4.4}
\]

(or its `b_1` analogue) is neither sufficient nor the correct
floor-aware statement.  The exact cap-safe condition for the whole
replacement is

\[
 \boxed{
                         u_G(S)\le c_\beta(S)
                         \quad\hbox{for every }S.}        \tag{4.5}
\]

The exact no-new-hole condition is

\[
 \boxed{
                         u_G(S)>0\quad\hbox{for every }S\in P_0.} \tag{4.6}
\]

Condition (4.5) is necessary and sufficient for cap safety, and (4.6)
is necessary and sufficient for setwise retention of every target
covered only by the old parent cylinder.  Together they imply

\[
 K_r(F[C\leftarrow G])=K_p(\beta),qquad
 M_r(F[C\leftarrow G])\le M_r(F).                        \tag{4.7}
\]

For mere numerical nonincrease of the hole count, (4.6) is stronger than
necessary.  By (2.15), the exact necessary and sufficient condition is

\[
 |\{S\in P_0:u_G(S)=0\}|
 \le |\{S\in Z_0:u_G(S)>0\}|.                            \tag{4.8}
\]

---

## 5. The exact library dispersion property

Let `mathscr L_C` be a library of oriented `D_(r+1)`-port-transversal local
factors containing the current member `G_0`.  For `theta>0`, define its
state-adaptive joint defect by

\[
\begin{aligned}
 \operatorname {Disp}_{\beta,\theta}(\mathscr L_C)
 =\min_{G\in\mathscr L_C}\Bigl[
 &E_\beta(G)\\
 &+\theta|\{S\in P_0:u_G(S)=0\}|
 \Bigr].                                                 \tag{5.1}
\end{aligned}
\]

### Theorem 5.1 (one-step dispersion inequality)

Some library member `G` satisfies

\[
\boxed{
\begin{aligned}
 K_r(F[C\leftarrow G])-K_r(F)
 &\le \operatorname {Disp}_{\beta,\theta}(\mathscr L_C)
                              -E_\beta(G_0),\\
 M_r(F[C\leftarrow G])-M_r(F)
 &\le {1\over\theta}
       \operatorname {Disp}_{\beta,\theta}(\mathscr L_C).
\end{aligned}}                                           \tag{5.2}
\]

If the first right side is `-d<=0`, the exact `PCap` descent is at least

\[
                              \min\{d,P_r(F)\}.           \tag{5.3}
\]

#### Proof

Choose a minimizer in (5.1).  Its first summand bounds `E_beta(G)`, and
Theorem 2.1 gives the first line of (5.2).  The second term in (2.15) is
nonnegative, so the missing-shadow increase is at most the number of old
exclusive targets missed by `G`; this number is at most the objective in
(5.1) divided by `theta`.  Formula (5.3) is Corollary 2.2. \(\square\)

This gives the exact answer to the local-library question.  A library is
useful at the current state precisely when its lower envelope in (5.1)
is smaller than the old residual defect `E_beta(G_0)`, with an acceptable
exclusive-support miss term.  For an iterative theorem this property must
hold for every **reachable** background `beta`, not merely for the
canonical background.

There is a useful sequential formulation.  Suppose legal parent
substitutions are made at steps `j=1,...,J`; contexts may have overlapping
depth-`r` influence.  Recompute `beta_j` immediately before step `j`.  If

\[
 E_{\beta_j}(G_j^{\rm new})
       \le E_{\beta_j}(G_j^{\rm old})-d_j,
 \qquad
 M_r(F_j)-M_r(F_{j-1})\le \ell_j,                        \tag{5.4}
\]

then no additivity assumption is needed:

\[
\boxed{
\begin{aligned}
 K_r(F_J)&\le K_r(F_0)-\sum_{j=1}^Jd_j,\\
 P_r(F_J)&\le
   \left[K_r(F_0)-\sum_{j=1}^Jd_j-(W-N_r)\right]_+,\\
 M_r(F_J)&\le M_r(F_0)+\sum_{j=1}^J\ell_j.
\end{aligned}}                                           \tag{5.5}
\]

These are telescoping consequences of (2.5), (2.8), and (2.15).

### The exact fractional cap criterion

For completeness, discard the shadow term temporarily and allow a
probability distribution `nu` on the library.  Put

\[
 \bar u_\nu=\sum_G\nu(G)u_G,
 \qquad
 E^{\rm frac}_\beta(\mathscr L_C)
  =\min_\nu\sum_S(\bar u_\nu(S)-c_\beta(S))_+.           \tag{5.6}
\]

Then finite-dimensional minimax gives the exact weighted dual

\[
 \boxed{
 E^{\rm frac}_\beta(\mathscr L_C)
 =\max_{0\le\alpha\le1}\left[
      \min_{G\in\mathscr L_C}\langle\alpha,u_G\rangle
      -\langle\alpha,c_\beta\rangle
                            \right].}                    \tag{5.7}
\]

Hence fractional defect at most `epsilon` is equivalent to

\[
 \boxed{
 \min_{G\in\mathscr L_C}\langle\alpha,u_G\rangle
 \le\langle\alpha,c_\beta\rangle+\epsilon
 \quad\hbox{for every }\alpha:\mathcal V_r\to[0,1].}    \tag{5.8}
\]

The minimizing `G` may depend on `alpha`.  Tests only on indicator
functions are not sufficient in general, because the same randomized
local choice must serve all level sets of a fractional `alpha`.

The integral gap

\[
 \operatorname {IG}_\beta(\mathscr L_C)
 =\min_GE_\beta(G)-E^{\rm frac}_\beta(\mathscr L_C)       \tag{5.9}
\]

is a separate quantity.  Thus the exact cap-dispersion package is
weighted residual-capacity dispersion (5.8) plus an integral rounding or
fragmentation theorem, together with the exclusive-support condition in
(5.1).

### A sufficient mean--variance--support certificate

For a distribution `nu`, let

\[
 \bar u(S)=\mathbb E_\nu u_G(S),\qquad
 v(S)=\operatorname {Var}_\nu u_G(S).                    \tag{5.10}
\]

Then for every `theta>0` some `G` satisfies

\[
\boxed{
\begin{aligned}
 E_\beta(G)+\theta|\{S\in P_0:u_G(S)=0\}|
 \le{}&\sum_S(\bar u(S)-c_\beta(S))_+\\
 &+{1\over2}\sum_S\sqrt{v(S)}\\
 &+\theta\sum_{S\in P_0}
            \Pr_\nu[u_G(S)=0].
\end{aligned}}                                           \tag{5.11}
\]

If instead `bar u(S)<=c_beta(S)-gamma(S)` with `gamma(S)>0` on every
target where `v(S)>0`, the first two terms on the right may be replaced
by

\[
                              \sum_S{v(S)\over4\gamma(S)}. \tag{5.12}
\]

#### Proof

Write `u_G=bar u+Y`, where `EY=0`.  The inequalities

\[
 (\bar u+Y-c)_+\le(\bar u-c)_++Y_+,
 \qquad \mathbb EY_+={1\over2}\mathbb E|Y|
                   \le{1\over2}\sqrt{\mathbb EY^2}      \tag{5.13}
\]

give the first two terms after summing.  The expectation of the
exclusive-support miss count is the last sum in (5.11).  Some library
member is no worse than the expectation of their combined objective.
Under the margin assumption use

\[
                              (Y-\gamma)_+\le{Y^2\over4\gamma} \tag{5.14}
\]

and take expectations.  \(\square\)

---

## 6. Common-core obstruction

Define the coordinatewise common profile of the library by

\[
                              \kappa(S)=\min_{G\in\mathscr L_C}u_G(S). \tag{6.1}
\]

Absorb it into the background:

\[
 \widetilde\beta=\beta+\kappa,
 \qquad \widetilde u_G=u_G-\kappa.                       \tag{6.2}
\]

All residual profiles are nonnegative and have equal total mass.  Theorem
2.1 applied to (6.2) gives

\[
 K_r(F[C\leftarrow G])
 =K_p(\widetilde\beta)
  +\sum_S\left(
      \widetilde u_G(S)-(p-\widetilde\beta(S))_+
            \right)_+.                                  \tag{6.3}
\]

In particular every library member obeys the statewise lower bound

\[
 \boxed{
                         K_r(F[C\leftarrow G])
                         \ge K_p(\beta+\kappa).}          \tag{6.4}
\]

Thus merely adding many local factors does not help if they retain a
large common affected-window profile on the same physical targets.

---

## 7. Fixed-scale accounting

There are exactly

\[
 H_{m,r+1}={1\over2}
       \binom{2(m-r-1)}{m-r-1}                           \tag{7.1}
\]

aligned size-`r+1` parent contexts.  Therefore the sum of potential
affected-slot incidences over a full fixed-scale layer is at most

\[
 A_{m,r}=2rH_{m,r+1}\operatorname {Cat}_{r+1}.            \tag{7.2}
\]

This is an incidence bound, so it remains valid when affected sets
overlap.  If a family of simultaneously legal substitutions is made at
this scale, Proposition 3.1 and a union bound give

\[
 \boxed{
 |\Delta K_r|,\ |\Delta P_r|,\ |\Delta M_r|
 \le A_{m,r}.}                                           \tag{7.3}
\]

Uniformly for `r^2/m=o(1)`,

\[
 {H_{m,r+1}\over W}
 ={1\over4\,4^{r+1}}
   \exp O\!\left({r^2\over m}+{1\over m}\right),        \tag{7.4}
\]

and

\[
 \operatorname {Cat}_{r+1}
 ={4^{r+1}\over\sqrt\pi(r+1)^{3/2}}
       \left(1+O(r^{-1})\right).                         \tag{7.5}
\]

Consequently

\[
 \boxed{
 {A_{m,r}\over W}
 ={1+o(1)\over2\sqrt\pi}
    {r\over(r+1)^{3/2}}
 =\left({1\over2\sqrt\pi}+o(1)\right)r^{-1/2}.}         \tag{7.6}
\]

At the fatal scale where `r` is minimal with `Cat_r>=4p`, one has
`r=Theta(log p)` and `Cat_(r+1)=Theta(p)`.  Hence

\[
 A_{m,r}=O\!\left({W\over\sqrt{\log p}}\right)=o(W).     \tag{7.7}
\]

Thus a full fixed-scale layer can create only `o(W)` direct depth-`r`
holes.  This is enough to make the raw shadow cost harmless at one
matched depth, but it gives no sign for the overload change.  The
certified plateau at this scale has order `W/r^(3/2)`, whereas the raw
movement budget (7.6) is larger by a factor of order `r`.  A successful
proof therefore needs the signed residual-capacity dispersion of Section
5, not a further cardinality estimate.

---

## 8. Proved boundary

The following points are rigorous.

1. A size-`r+1` port-transversal parent substitution has exactly
   `2r Cat_(r+1)` potentially affected depth-`r` slots.
2. Equations (2.4)--(2.5) give its exact cap-overload change against the
   true ambient residual capacities, including all boundary-crossing
   windows.
3. Equations (2.15)--(2.17) give its exact direct missing-shadow change.
4. Equation (2.8) keeps the unavoidable baseline `W-N_r` and its positive
   part exactly; (2.10) applies to every later row-power assignment.
5. The exact state-adaptive library property is (5.1).  Its fractional
   cap part is the all-weight dual (5.8), and its integral and
   exclusive-support parts are separate.
6. At `r=Theta(log p)`, the entire fixed-scale layer changes at most
   `O(W/sqrt(log p))=o(W)` depth-`r` targets, but no overload descent
   follows without (5.1).

What remains open is existence of a noncanonical `D_(r+1)`-port-transversal
library satisfying (5.1) uniformly for every reachable parent
background, or even satisfying its fractional weighted condition (5.8)
with sufficiently small integral gap.  The known parent rectangle
controls only a distinguished endpoint arm and does not establish this
full-profile property.  No constant-one conclusion follows at this
stage.
