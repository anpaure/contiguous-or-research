# Pair-profile stopping under the triple-fibre threshold

Date: 2026-07-27

Scope: the genuine vertex-induced compensated promotion-frame process.

## Subsequent all-order audit

`MATH_NOGO_ALL_ORDER_PROFILE_ENERGY_CONSECUTIVE_SPINE_20260727.md`
shows that the profile-order boundary cannot be removed by any positive
scalar weights $a_k$.  The exact aggregate child kernel changes from
$\Theta(1/m)$ to $\Theta(1)$ at $k=H$; absorption over
$T=\Theta(m\log m)$ then forces weights whose initialized consecutive-
spine term is $\exp[(1+o(1))m\log\log m]$.  Thus the remaining boundary
requires a non-scalar/two-shore energy or cancellation of the $+1$
shift, not another choice of one-index weights.

## 0. Outcome

Write

\[
 q_s(S)={d_0(S)\over D_0},\qquad u_t=e^{-t/r},
\]

and assume the ordinary degree stop

\[
 c_DD_0u_t^{r-1}\le\Delta_t\le C_DD_0u_t^{r-1}.          \tag{Deg}
\]

Let $A_2,A_3=(\log m)^{O(1)}$.  Consider the profile stops

\[
 d_t(x,y)\le A_2u_t^{-1}q_2(x,y)\Delta_t,                 \tag{PPS}
\]

and

\[
 d_t(x,y,w)\le A_3u_t^{-2}q_3(x,y,w)\Delta_t.            \tag{PFS$_3$}
\]

Then, before PFS$_3$ and uniformly down to

\[
                         u_t\ge z_*=m^{-1/2}(\log m)^{B}, \tag{0.1}
\]

with $B$ larger than the fixed polylogarithmic constants, the PPS
crossing probability in every marked owner/root incidence is

\[
 \boxed{
 \Pr(\text{PPS crossing before PFS$_3$})
 \le
 \exp\!\left[-{c(A_2-2)^2\over V_*+b_*A_2}\right],}       \tag{0.2}
\]

where

\[
 b_*\le {L^C\over mz_*}=o(1),\qquad
 V_*\le L^C\left({1\over mz_*}+{1\over m^2z_*^3}\right)
 =o(1).                                                    \tag{0.3}
\]

Consequently PPS crossings occurring before PFS$_3$ have total expected
marked incidence $o(W)$.  Combined with
`MATH_THEOREM_PROFILE_PAIR_SPREAD_CLOSES_STOPPED_WHOLE_ARM_PSF_20260727.md`,
this closes PSF and the whole-arm top strip on that event.

The triple threshold does not finish the trajectory by itself.  Its own
first-moment maximal estimate loses the number of possible fourth
fibres.  Repeating the argument for PFS$_3$ requires the fourth-profile
threshold

\[
 d_t(S\cup\{w\})le A_4u_t^{-3}q_4(S\cup\{w\})\Delta_t.   \tag{0.4}
\]

Thus the exact remaining alternative is:

\[
 \boxed{
 \begin{array}{c}
 \text{either prove a joint all-fibre energy which absorbs the
 profile-order boundary,}\\
 \text{or construct a vertex-induced residual in which PFS$_3$
 carries nonnegligible incidence.}
 \end{array}}                                             \tag{0.5}
\]

No such vertex-induced residual is supplied by the existing pair-star
construction, which is only an arbitrary edge-deletion subhypergraph.

## 1. Static fibre inputs

Fix a physical pair $S=\{x,y\}$ with $q_2(S)>0$.  The exact
distance-one/fixed-endpoint table and the proved theta kernel give the
following three estimates.

### Lemma 1.1 (one fibre)

For every third physical resource $a$,

\[
                         q_3(S\cup\{a\})
 \le {CL^C\over m^2}q_2(S).                               \tag{1.1}
\]

### Lemma 1.2 (one frame of fibres)

For every catalogue edge $G$,

\[
 \sum_{a\in V(G)\setminus S}q_3(S\cup\{a\})
 \le {CL^C\over m}q_2(S).                                \tag{1.2}
\]

### Lemma 1.3 (theta fibre form)

After resolving resource equalities and retaining the physical
disjointness conditions,

\[
 \boxed{
 \sum_{a\ne b}q_2(a,b)
 q_3(S\cup\{a\})q_3(S\cup\{b\})
 \le {CL^C\over m^2}q_2(S)^2.}                            \tag{1.3}
\]

#### Justification

Equation (1.1) is the fixed-third-resource diffusion estimate in a
pair link.  Summing it over the $r=(1+o(1))m$ resources of one frame
gives (1.2).  Formula (1.3) is the equality-resolved subdivided
$K_{2,3}$, equivalently theta, mixed diagram: the two $q_3$ branches
share the fixed endpoints $S$, and the column $q_2(a,b)$ joins their
free endpoints.  The missing endpoint factor in this diagram is exactly
the factor $m^{-2}$ proved by the physical theta-kernel theorem.  All
three statements are within logarithmic physical order.

## 2. Pair-link drift

Put

\[
                         N_S(t)=d_t(S),qquad
 \mu_S(t)=q_2(S)D_0u_t^{r-2}.                              \tag{2.1}
\]

Events deleting either endpoint of $S$ terminate $N_S$ and are
favorable.  For an active edge $E\supseteq S$, pair domination and the
profile bound PPS give

\[
 \begin{aligned}
 J_t(V(E))-J_t(S)
 &\le\sum_{\substack{\{a,b\}\subseteq V(E)\\
                       \{a,b\}\not\subseteq S}}d_t(a,b)\\
 &\le {CL^CA_2\Delta_t\over m u_t}.
 \end{aligned}                                           \tag{2.2}
\]

Hence the external loss rate of one member of the pair link is at least

\[
 {r-2\over r}-{CL^CA_2\over mr u_t}.                      \tag{2.3}
\]

Since

\[
 \int_0^{T_*}{L^CA_2\over mr u_t}\,dt
 \le {L^CA_2\over mz_*}=o(1),                            \tag{2.4}
\]

the predictable drift of $N_S/\mu_S$ is at most an $o(1)$
multiplicative error before the stops.

## 3. Nonterminal jump sizes

For an external resource $a$, put

\[
                         A_a(t)=d_t(S\cup\{a\}).          \tag{3.1}
\]

A compensation deletion of $a$ removes at most $A_a$ members of the
pair link.  A selected edge $G$ avoiding the prefix $S$ removes at most

\[
                         K_G(t)=\sum_{a\in V(G)}A_a(t).    \tag{3.2}
\]

By PFS$_3$, Lemma 1.2, and (Deg),

\[
 \begin{aligned}
 K_G(t)
 &\le A_3u_t^{-2}\Delta_t
       \sum_{a\in V(G)}q_3(S\cup\{a\})\\
 &\le {CL^CA_3\over m u_t}\mu_S(t).
 \end{aligned}                                           \tag{3.3}
\]

Thus every nonterminal normalized jump is at most

\[
                         b(t)={CL^CA_3\over m u_t},
 \qquad b_*:=\sup_{t\le T_*}b(t)le {CL^CA_3\over mz_*}=o(1).
\tag{3.4}
\]

Prefix-killing jumps send the observable to zero and cannot cause an
upper crossing; they may be omitted from the one-sided quadratic
variation.

## 4. Exact quadratic variation

For one selected edge $G$, use

\[
 K_G^2
 \le\sum_{a,b\in V(G)}A_aA_b.                            \tag{4.1}
\]

After summing its clock rate $\nu_t=(r\Delta_t)^{-1}$ over active
selected edges, the diagonal part is at most

\[
 {1\over r}\sum_aA_a^2.                                  \tag{4.2}
\]

The compensation clocks contribute at most another
$r^{-1}\sum_aA_a^2$.  Before PPS,

\[
                         \sum_aA_a=(r-2)N_S
                         \le CL^CA_2r\mu_S.               \tag{4.3}
\]

Moreover PFS$_3$ and Lemma 1.1 give

\[
                         \max_aA_a
 \le {CL^CA_3\over m^2u_t}\mu_S.                         \tag{4.4}
\]

Therefore the normalized diagonal quadratic-variation rate is at most

\[
                         {CL^CA_2A_3\over m^2u_t}.         \tag{4.5}
\]

For the off-diagonal selected-edge part, reverse summation:

\[
 \nu_t\sum_G\sum_{a\ne b\in G}A_aA_b
 ={1\over r\Delta_t}
   \sum_{a\ne b}d_t(a,b)A_aA_b.                           \tag{4.6}
\]

Apply PPS, PFS$_3$, (Deg), and Lemma 1.3.  After division by
$\mu_S(t)^2$, (4.6) is at most

\[
                         {CL^CA_2A_3^2\over m^3u_t^3}.     \tag{4.7}
\]

Integrating (4.5)--(4.7), using $dt=-r\,du/u$, yields

\[
 \boxed{
 V_*le
 CL^C\left({A_2A_3\over mz_*}
       +{A_2A_3^2\over m^2z_*^3}\right)=o(1).}           \tag{4.8}
\]

This is the point at which the theta factor in (1.3) is indispensable.
Using only maximum pair and triple codegrees would give a divergent
$z_*^{-1}$ bound.

## 5. Freedman and incidence weighting

Multiply $N_S/\mu_S$ by the deterministic integrating factor from
(2.4), stop it at PPS, PFS$_3$, the degree stop, or endpoint death, and
subtract its predictable drift.  The result is a local martingale whose
nonterminal jump magnitudes are at most $b_*$ and whose predictable
quadratic variation is at most $V_*$.  One-sided Freedman therefore
gives

\[
 \Pr\left(sup_{t\le T_*}{N_S(t)\over\mu_S(t)}\ge A_2,
              \ t<\tau_{\rm PFS_3}\right)
 \le
 \exp\!\left[-{c(A_2-2)^2\over V_*+b_*A_2}\right].       \tag{5.1}
\]

The same calculation holds after marking one current owner or root
incidence: its deletion is terminal and favorable.  Sum (5.1) over the
marked pair occurrences in the top-strip physical-union catalogue,
rather than taking a union bound over all ambient resource pairs.  The
right side is $o(1)$, uniformly over the polynomial arm positions and
compressed types.  Hence

\[
 \boxed{
 \mathbb E[\text{PPS-stopped incidence before PFS$_3$}]=o(W).}
\tag{5.2}
\]

## 6. Why the triple stop is a genuine remaining boundary

For a fixed triple $S$, its link has natural reference

\[
                         q_3(S)D_0u_t^{r-3}.              \tag{6.1}
\]

The first-moment maximal inequality gives a factor $A_3^{-1}$ for one
fixed triple.  It does not pay the full family of possible fourth
resources in that triple link.  The quadratic-variation calculation for
the triple link contains

\[
 d_t(S\cup\{a\}),qquad
 \sum_{a,b}d_t(a,b)d_t(S\cup\{a\})d_t(S\cup\{b\}),       \tag{6.2}
\]

and controlling (6.2) dynamically requires the fourth-profile analogue
(0.4).  The same algebra then repeats with the same two small parameters
$(mz_*)^{-1}$ and $(m^2z_*^3)^{-1}$.

Thus PFS$_3$ is not a terminal scalar condition.  Claiming its stopped
incidence is $o(W)$ from first moments alone would repeat the finite
boundary error of the original ordered-column tower.  A proof must
either sum all profile orders in one weighted energy or establish a
finite top boundary by a new argument.

## 7. Status

Proved:

1. PPS has $o(W)$ stopped incidence before the triple-profile stop;
2. the proof is uniform to
   $u=m^{-1/2}(\log m)^B$ for sufficiently large fixed $B$;
3. the quadratic variation uses exactly the physical theta kernel and
   no marginal products; and
4. conditional on PFS$_3$, the whole-arm PSF/top-strip gate is closed.

Not proved, and not refuted by a genuine induced example:

\[
 \boxed{
 \text{$o(W)$ stopped incidence for PFS$_3$ itself.}}
\]

This is now the sole profile-order boundary.
