# Profile pair spread closes the stopped whole-arm factorial estimate

Date: 2026-07-27

Scope: the genuine vertex-induced compensated promotion-frame process,
with complete physical-union normalization.

## Subsequent pair-stop progress

`MATH_THEOREM_PAIR_PROFILE_STOP_UNDER_TRIPLE_FIBRE_AND_NEXT_BOUNDARY_20260727.md`
proves that PPS itself has $o(W)$ stopped incidence before the natural
$u^{-2}$ triple-profile stop, uniformly down to
$u=m^{-1/2}(\log m)^B$.  Its quadratic variation is closed by the
physical theta kernel.  The remaining boundary is now the stopped
incidence of the triple-profile condition, not PSF or the pair profile
below that condition.

## 0. Result and exact remaining boundary

Let $r=(1+o(1))m$ be the catalogue edge size, let $D_0$ be the initial
maximum resource degree, and put

\[
                         u_t=e^{-t/r},\qquad z=m^{-1/20}.
\]

For physical resources $x\ne y$, write

\[
 q_2(x,y)={d_0(x,y)\over D_0}.                              \tag{0.1}
\]

Run inside the ordinary degree stop

\[
 c_DD_0u_t^{r-1}\le\Delta_t\le C_DD_0u_t^{r-1}.           \tag{Deg}
\]

Assume the **profile**, rather than maximum, pair-spread stop

\[
 \boxed{
 d_t(x,y)\le A_2u_t^{-1}q_2(x,y)\Delta_t
 \quad\text{for every active }x\ne y,}                    \tag{PPS}
\]

where $A_2=L^{C_2}$ and $L=C_1(\log m)^2$.  The companion natural
triple-fibre stop is

\[
 d_t(x,y,w)le A_3u_t^{-2}{d_0(x,y,w)\over D_0}\Delta_t,  \tag{PFS}
\]

but PFS is not needed for the whole-arm estimate once PPS is available.

Then the incidence-weighted stopped factorial whole-arm estimate is
proved.  If $F,F'$ are equality-resolved displayed arms and
$C_t(F,F')$ is the family of active future edges meeting both exclusive
shores, then, outside stopped marked incidence $o(W)$,

\[
 \boxed{
 |C_t(F,F')|
 \le {C A_H\Delta_t\over m u_t},}                          \tag{0.2}
\]

where $A_H=L^{C_H}$ may be chosen with $C_H$ arbitrarily large relative
to the polynomial arm multiplicity.  Consequently, for every
$1\le h\le J=C_0\log m$,

\[
 \boxed{
 \sum_{F,F'}w_t(F,F')\bigl(|C_t(F,F')|\bigr)_h
 \le
 \left({C A_H\Delta_t\over m u_t}\right)^h
 \sum_{F,F'}w_t(F,F'),}                                  \tag{PSF}
\]

for the owner/root marked-incidence weights of the top-strip
observable.  This includes all overlapping and non-square equality
shapes because no tuple decomposition is used.

The corresponding common-event clock mass is

\[
 \beta_t(F,F')\le {C A_H\over m^2u_t},                    \tag{0.3}
\]

and hence, for $p=O(L)$ displayed arms,

\[
 \int_0^T\binom p2\beta_t\,dt
 \le {C A_HL^2\over mz}=o(1).                            \tag{0.4}
\]

Thus PSF and the whole-arm/HCE part of the pair-safe stop are closed
conditional on PPS.  The only remaining dynamic gate is now the
incidence-weighted propagation of PPS itself (and PFS if it is used to
prove PPS).  The arbitrary edge-deletion pair star is not a
vertex-induced obstruction to this theorem, and no genuine induced
obstruction to PPS is currently known.

## 1. Two static profile sums

The proof uses the exact time-zero frame influence profile, not a
maximum pair codegree.

### Lemma 1.1 (one-frame internal pair mass)

For every catalogue edge $G$,

\[
 \boxed{
 \sum_{\{x,y\}\subseteq V(G)}q_2(x,y)\le {C\over m}.}    \tag{1.1}
\]

### Lemma 1.2 (two-frame cross pair mass)

For every equality-resolved pair of catalogue edges $F,F'$,

\[
 \boxed{
 \sum_{x\in F\setminus F'}
 \sum_{y\in F'\setminus F}q_2(x,y)\le {C\over m}.}       \tag{1.2}
\]

#### Proof

Fix one owner resource $x$ and one frame $G$.  The exact cyclic-distance
pair table and the endpoint count in the deck of $G$ give

\[
 \sum_{\substack{y\in V(G)\\y\ne x}}d_0(x,y)
 \le {CD_0\over m^2}.                                    \tag{1.3}
\]

There are $r=(1+o(1))m$ possible $x$ in a frame.  Summing (1.3) and
dividing by two proves (1.1).  Summing the same fixed-owner inequality
over $x\in F\setminus F'$ proves (1.2).  The top--owner terms are
$m^{-\omega(1)}D_0$ in the Gaussian regime and distinct top resources
have codegree zero.  Resolving resources already common to $F,F'$ can
only decrease the cross sum.  \(\square\)

These are exactly the profile statements lost when (1.2) is replaced by
the crude maximum-pair bound $r^2\Delta_2$.

## 2. PPS controls every active edge hazard

For an active resource set $S$, recall

\[
 J_t(S)=\sum_{x\in S}d_t(x)-|\mathcal E_t(S)|
 =\sum_g(|g\cap S|-1)_+                                  \tag{2.1}
\]

and

\[
                         \Lambda_t(S)={|S|\over r}
                                      -{J_t(S)\over r\Delta_t}.
\tag{2.2}
\]

Pair domination and PPS give, for every active catalogue edge $G$,

\[
 \begin{aligned}
 J_t(V(G))
 &\le\sum_{\{x,y\}\subseteq V(G)}d_t(x,y)\\
 &\le A_2u_t^{-1}\Delta_t
       \sum_{\{x,y\}\subseteq V(G)}q_2(x,y)\\
 &\le {CA_2\Delta_t\over m u_t}.
 \end{aligned}                                           \tag{2.3}
\]

Consequently every active edge has the statewise hazard lower bound

\[
 \boxed{
 \Lambda_t(V(G))\ge1-\varepsilon_t,
 \qquad
 \varepsilon_t={CA_2\over mr u_t}.}                       \tag{2.4}
\]

Uniformly for $u_t\ge z$,

\[
                         \varepsilon_t\le {1\over r}      \tag{2.5}
\]

for all sufficiently large $m$, because
$A_2/(mu_t)=m^{-19/20+o(1)}$.  This is the decisive gain over
maximum pair spread: the internal cyclic profile saves an additional
factor $m^{-1}$.

## 3. The whole-arm score

Fix equality-resolved arms $F,F'$ and put

\[
 \mathcal Q(F,F')=(F\setminus F')\times(F'\setminus F).
\tag{3.1}
\]

Define the physical-union marked score

\[
 X_{F,F'}(t)
 =I_{F\cup F'}(t)
   \sum_{(x,y)\in\mathcal Q(F,F')}d_t(x,y).               \tag{3.2}
\]

All shared physical resources occur once in $I_{F\cup F'}$.  In
particular, compensation coins introduce no cross-fibre correction.

Expand (3.2) over active future edges:

\[
 X_{F,F'}(t)
 =\sum_{(x,y)\in\mathcal Q(F,F')}
   \sum_{G\supseteq\{x,y\}} I_{F\cup F'\cup G}(t).        \tag{3.3}
\]

One summand in (3.3) dies at rate
$\Lambda_t(F\cup F'\cup G)$, which is at least
$\Lambda_t(V(G))$.  Therefore (2.4) and linearity of the generator give
the exact stopped inequality

\[
 \boxed{
 \mathcal G_tX_{F,F'}(t)
 \le-(1-\varepsilon_t)X_{F,F'}(t).}                       \tag{3.4}
\]

Terminal death of either displayed arm only strengthens (3.4); it is
not dropped against a negative prefix reference.

At time zero, Lemma 1.2 gives

\[
                         X_{F,F'}(0)\le {CD_0\over m}.     \tag{3.5}
\]

Put

\[
 B_H(t)={CD_0\over m}u_t^{r-2}.                           \tag{3.6}
\]

Since

\[
 -{d\over dt}\log B_H(t)={r-2\over r}
 \le1-\varepsilon_t,                                    \tag{3.7}
\]

equations (3.4)--(3.7) show that

\[
                         {X_{F,F'}(t)\over B_H(t)}         \tag{3.8}
\]

is a nonnegative stopped supermartingale.  Notice that the reference
$u^{r-2}$ deliberately includes the two-endpoint conditioning loss; no
marginal products have been used.

## 4. Incidence-weighted maximal stopping

Mark one current owner or root incidence in every displayed arm-pair
occurrence.  Its death is terminal and favorable, so the marked version
of (3.4) is unchanged.  Let a top-strip state contain at most $p=O(L)$
nonprivate physical arms and define its score to be the sum of (3.8)
over its equality-resolved arm pairs.

Stop that marked occurrence at the first time its score exceeds $A_H$.
Doob's maximal inequality and (3.5) give

\[
 \mathbb E[\text{stopped marked incidence}]
 \le {C p^2\over A_H}
       [\text{total marked incidence}].                   \tag{4.1}
\]

Choose, for example,

\[
                         A_H=L^{10}.                       \tag{4.2}
\]

Then $p^2/A_H=O(L^{-8})=o(1)$.  After summing the
$\exp[O(s\log(s+1))]$ compressed top types with their existing
$\alpha^s$ weights, the same calculation used in the top-strip
quarantine gives

\[
             \boxed{\text{whole-arm stopped incidence}=o(W).} \tag{4.3}
\]

No union bound over physical resource pairs is taken.  Pair occurrences
are summed first into the one whole-arm score (3.2), which is why the
factor $r^2$ does not reappear.

## 5. PSF follows pointwise

Every genuinely new common event $G\in C_t(F,F')$ contains at least one
ordered cross pair

\[
             x\in F\setminus F',\qquad y\in F'\setminus F.
\]

Hence, on a retained marked occurrence,

\[
 |C_t(F,F')|\le X_{F,F'}(t)\le A_HB_H(t).                 \tag{5.1}
\]

By (Deg),

\[
 B_H(t)le {C\Delta_t\over m u_t}.                        \tag{5.2}
\]

This proves (0.2).  Since $(n)_h\le n^h$ for every integer $n\ge0$,

\[
 \bigl(|C_t(F,F')|\bigr)_h
 \le\left({CA_H\Delta_t\over m u_t}\right)^h.           \tag{5.3}
\]

Multiplication by arbitrary nonnegative retained incidence weights and
summation proves PSF.  Intersections among the $h$ future edges can only
decrease the falling factorial relative to the right side, so Ferrers,
theta, repeated-edge, and all other equality shapes are already
included.

Finally, multiplying (5.1) by the edge-clock rate
$\nu_t=(r\Delta_t)^{-1}$ gives (0.3), and integration gives (0.4).

## 6. Coin fibres

For complete physical-union normalization the compensation part of the
hazard is

\[
                         \sum_{x\in U}\chi_t(x)
\]

for the physical union $U$.  This is exactly the actual union coin
hazard.  Therefore

\[
                         \boxed{C_\circ^{\rm union}=0.}    \tag{6.1}
\]

Thus no coin-fibre hypothesis is used in Sections 2--5.

## 7. Status

Unconditional inside the degree and PPS stops:

1. the edge-hazard estimate (2.4);
2. the whole-arm supermartingale (3.8);
3. $o(W)$ incidence at the whole-arm stop;
4. all factorial PSF orders through $J$ (indeed all orders); and
5. exact disappearance of coin fibres under physical-union
   normalization.

Still open:

\[
 \boxed{
 \text{prove }o(W)\text{ incidence for the profile pair-spread stop
 PPS itself, or construct a genuine vertex-induced PPS obstruction}.}
\]

The natural triple threshold PFS is the first auxiliary condition for a
future PPS proof, but it is not part of the now-closed PSF gate.
