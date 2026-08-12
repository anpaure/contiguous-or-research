# Independent rank matchings: deterministic profile expansion and the raw-cut gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result

Partition the nonresidual coordinates into macroblocks

\[
 B_j=A_j\mathbin{\dot\cup}C_j,
 \qquad |A_j|=|C_j|=d,
 \qquad j=1,\ldots,b,qquad bd=m,                    \tag{0.1}
\]

and choose, independently and uniformly if desired, a bijection

\[
                 \pi_{j,k}:A_j\longrightarrow C_j
                 \qquad(0\le k\le2d).               \tag{0.2}
\]

Let `G_q^-` and `G_q^+` be the maximal lower and upper
allocation-overlap graphs at

\[
                         q=A\sqrt m+O(1),\qquad A>0, \tag{0.3}
\]

before retaining only `r` axes and before choosing a chronological packet
factor.

This note proves an exact normalized expansion theorem for the
macroblock-half-count profile quotient. In fact, that theorem is
deterministic: randomizing the matchings is not needed at this quotient.
For every fixed bijection, the aggregate number of compatible incidences
between two prescribed half-count profiles is the same.

Assume

\[
 d\to\infty,\qquad d^2=o(\sqrt m),\qquad
 {m\over d}e^{-c_0d}=o(1)                            \tag{0.4}
\]

for a sufficiently small absolute `c_0>0`.  Thus `d=C log m` with a
sufficiently large fixed `C` is admissible. After discarding `o(N_q)`
targets, the lower and upper profile quotients separately have a
fractional flow which saturates every retained target profile and uses at
most

\[
                  {\binom mq\over\binom{m+q}q}
                    \left(1+O_A(d^2/\sqrt m)\right)
                  =e^{-A^2}+o(1)<1                  \tag{0.5}
\]

of every owner-profile capacity. Equivalently, every nonnegative dual of
the aggregate half-count profile quotient has expansion factor

\[
                         e^{A^2}-o(1).               \tag{0.6}
\]

The proof keeps only allocations placing at most two of the `q`
promotions in any macroblock. Their loss is uniformly

\[
                         O_A(d^2/\sqrt m)=o(1).       \tag{0.7}
\]

All within-block collision corrections are retained exactly; none is
replaced by an independent-addition approximation.

This is not a raw source injection. A realized matching array is not
transitive inside a half-count profile, and the compatible degrees within
one such profile have a genuine Gaussian spread. An arbitrary raw target
family may select a thin part of a profile. The missing theorem is a
quenched within-profile Hall/cut-norm statement. Even that theorem would
still precede the selected-axis and common-chronology packet gates.

## 1. Exact probability for one prescribed inclusion

Fix one block, a lower inclusion `T subset X`, and put

\[
\begin{aligned}
 a&=|T\cap A|,&c&=|T\cap C|,\\
 \alpha&=|(X\setminus T)\cap A|,&
 \gamma&=|(X\setminus T)\cap C|,\\
 a'&=a+\alpha,&c'&=c+\gamma,
 \qquad \ell=\alpha+\gamma.
\end{aligned}                                        \tag{1.1}
\]

The source uses the rank-`a'+c'` matching. Every added `A`-coordinate
must be matched into `C setminus X`, and every added `C`-coordinate must
have its preimage in `A setminus X`. The two requirements use disjoint
domains and images. Hence, for a uniform local bijection,

\[
 \boxed{
 p_d(a,c;\alpha,\gamma)
 ={(d-c')_{\underline\alpha}
    (d-a')_{\underline\gamma}
   \over(d)_{\underline\ell}}.}                     \tag{1.2}
\]

This proves the exact single-inclusion formula. It also shows that merely
replacing every retained inclusion probability by `2^-ell` loses the
without-replacement terms which accumulate at Gaussian depth.

## 2. Exact aggregate profile incidence is deterministic

The key additional observation is that the aggregate profile count does
not depend on the identity of the bijection.

### Lemma 2.1 (one-block profile incidence)

For any fixed bijection `pi:A to C`, the number of compatible lower pairs
`T subset X` having the data (1.1) is exactly

\[
 \boxed{
 I_d(a,c;\alpha,\gamma)
 =\binom d{\alpha,\gamma,d-\ell}
   \binom{d-\ell}a\binom{d-\ell}c.}                 \tag{2.1}
\]

#### Proof

Choose `ell` matching edges and partition them into `alpha` edges on
which the source adds the `A` endpoint and `gamma` edges on which it adds
the `C` endpoint. The target contains neither endpoint of any selected
edge. On the remaining `d-ell` edges, choose its `a` occupied `A`
endpoints and its `c` occupied `C` endpoints independently. This is a
bijection with all compatible pairs of the prescribed type. \(\square\)

Let

\[
 J_d(a,c;\alpha,\gamma)
 =\binom da\binom dc
   \binom{d-a}\alpha\binom{d-c}\gamma              \tag{2.2}
\]

be the number of all, not necessarily compatible, inclusions of this
profile type. Equations (1.2) and (2.1) independently check each other:

\[
                         I_d=J_d p_d.                \tag{2.3}
\]

For ordered global profiles

\[
 \tau=((a_j,c_j))_{j\le b},
 \qquad
 \kappa=((a_j+\alpha_j,c_j+\gamma_j))_{j\le b},     \tag{2.4}
\]

where `sum_j(alpha_j+gamma_j)=q`, put

\[
\begin{aligned}
 w_T(\tau)&=\prod_j\binom d{a_j}\binom d{c_j},\\
 w_X(\kappa)&=\prod_j
   \binom d{a_j+\alpha_j}\binom d{c_j+\gamma_j},\\
 J_{\tau\kappa}&=\prod_jJ_d(a_j,c_j;\alpha_j,\gamma_j),\\
 I_{\tau\kappa}&=\prod_jI_d(a_j,c_j;\alpha_j,\gamma_j).
\end{aligned}                                        \tag{2.5}
\]

Here `J_(tau,kappa)` and `I_(tau,kappa)` count global ordinary and
compatible inclusions, respectively. They are exact for every matching
array. Independent random rank matchings change which raw pairs occur,
but not these profile totals.

The upper statement is identical after complementation and reindexing the
source ranks. In particular its aggregate profile counts are also
deterministic for every matching array.

## 3. A safe Gaussian profile core

Call a lower or upper half-count profile safe if

\[
                    {d\over4}\le a_j,c_j\le{3d\over4}
                    \qquad(j\le b).                 \tag{3.1}
\]

For a uniform rank-`m plus/minus q` set, the count in one fixed `d`-set
is hypergeometric with mean `d/2+O(d/sqrt(m))`. A standard
hypergeometric Chernoff bound gives

\[
 \Pr\left\{a_j\notin[d/4,3d/4]\right\}
 +\Pr\left\{c_j\notin[d/4,3d/4]\right\}
 \le 4e^{-c_0d}.                                    \tag{3.2}
\]

A union bound over `2b` halves and (0.4) show that unsafe profiles contain
`o(N_q)` targets, on both signs.

Now fix any lower target, and choose uniformly one of its

\[
                         D_T=\binom{m+q}q             \tag{3.3}
\]

middle supersets. Let `ell_j` be the number of added elements in block
`B_j`. Since at most `2d` available coordinates lie in one block,

\[
\begin{aligned}
 \Pr\{\max_j\ell_j\ge3\}
 &\le b\binom{2d}3{(q)_{\underline3}\over(m+q)_{\underline3}}\\
 &=O_A(d^2/\sqrt m)=:\varepsilon_m=o(1).             \tag{3.4}
\end{aligned}
\]

This bound is uniform in the target. The same calculation applies to the
`q` deletions from an upper target.

If a target profile is safe and `ell_j<=2`, then (2.1) is positive in
every block. More quantitatively, (1.2) gives

\[
                         p_d(a_j,c_j;\alpha_j,\gamma_j)
                              \ge c_1^{\ell_j}        \tag{3.5}
\]

for an absolute `c_1>0` and all large `d`. Hence

\[
                         {I_{\tau\kappa}\over J_{\tau\kappa}}
                              \ge c_1^q               \tag{3.6}
\]

on every retained profile arc. This lower bound will only be used to
check that profile mass can be supported by actual compatible incidences;
it is not used as a substitute for Hall.

## 4. Exact normalized flow on the profile quotient

The ordinary inclusion graph between ranks `m-q` and `m` is biregular.
Every target has degree `D_T` from (3.3), every source has reverse degree

\[
                         D_X=\binom mq,               \tag{4.1}
\]

and

\[
                         \rho_q={D_X\over D_T}
                         ={N_q\over W}
                         =e^{-A^2}+o(1).              \tag{4.2}
\]

For a safe target profile `tau`, let

\[
 r_\tau={1\over w_T(\tau)D_T}
   \sum_{\substack{\kappa:\,\ell_j\le2\\j\le b}}
                         J_{\tau\kappa}.             \tag{4.3}
\]

Equation (3.4) gives the uniform estimate

\[
                         r_\tau\ge1-\varepsilon_m.   \tag{4.4}
\]

Define the quotient flow

\[
 F_{\tau\kappa}
 ={J_{\tau\kappa}\over D_T r_\tau}                 \tag{4.5}
\]

on safe target profiles and allocations with `ell_j<=2`, and put it zero
elsewhere. Then exactly

\[
                         \sum_\kappa F_{\tau\kappa}=w_T(\tau).  \tag{4.6}
\]

For every owner profile `kappa`, restriction can only reduce the ordinary
inclusion inflow, so

\[
\begin{aligned}
 \sum_\tau F_{\tau\kappa}
 &\le {1\over1-\varepsilon_m}
       {1\over D_T}\sum_\tau J_{\tau\kappa}\\
 &= {\rho_q\over1-\varepsilon_m}w_X(\kappa).
                                                               \tag{4.7}
\end{aligned}
\]

Equations (4.2) and (3.4) prove the owner-load bound (0.5).

It remains to check that (4.5) is carried by actual compatible profile
incidences, not merely by the support symbol. Distribute
`F_(tau,kappa)` equally over the `I_(tau,kappa)` compatible raw pairs.
By (3.6), the weight placed on one pair is at most

\[
 {1\over D_T(1-\varepsilon_m)c_1^q}=o(1),           \tag{4.8}
\]

because

\[
                         D_Tc_1^q
 \ge\left({c_1m\over q}\right)^q\longrightarrow\infty. \tag{4.9}
\]

Thus no individual compatible incidence is asked to carry more than one
unit. This is an exact fractional flow on the profile quotient, realized
by edges of the actual maximal graph.

The qualification “on the profile quotient” is essential: (4.6)--(4.7)
control the sum of loads in each profile, not each raw vertex separately.

## 5. The profile-quotient dual

Let `y_tau>=0` be arbitrary on the retained target profiles. From the
flow above,

\[
\begin{aligned}
 \sum_\tau w_T(\tau)y_\tau
 &=\sum_{\tau,\kappa}F_{\tau\kappa}y_\tau\\
 &\le {\rho_q\over1-\varepsilon_m}
 \sum_\kappa w_X(\kappa)
       \max_{\tau:F_{\tau\kappa}>0}y_\tau.           \tag{5.1}
\end{aligned}
\]

This proves every weighted Hall inequality in the **aggregate profile
quotient**. It does not yet prove the corresponding raw-graph inequality
for a potential which is constant inside each half-count profile: an
aggregate-adjacent target profile need not be visible from every raw owner
in the source profile. In particular, for every family `P` of retained
target profile nodes, the quotient capacities satisfy

\[
 \sum_{\tau\in P}w_T(\tau)
 \le {\rho_q\over1-\varepsilon_m}
       \sum_{\kappa\in N(P)}w_X(\kappa).             \tag{5.2}
\]

Thus the quotient neighborhood is larger by the factor

\[
                         {1-\varepsilon_m\over\rho_q}
                         =e^{A^2}-o(1).              \tag{5.3}
\]

This is normalized expansion of the quotient relaxation. The raw
profile-compressed dual requires an additional uniform arc-visibility
lemma. That lift is supplied and audited separately in
`MATH_AUDIT_INDEPENDENT_RANK_MATCHING_PROFILE_HALL_AND_GROUPING_20260726.md`.

## 6. Why this does not prove an arbitrary raw cut

For a fixed local matching and fixed half counts `(a,c)`, the number of
full edges in a uniformly chosen local target is hypergeometric:

\[
 F\sim\operatorname{Hyp}(d,c,a),
 \qquad
 \operatorname{Var}F
 ={ac(d-a)(d-c)\over d^2(d-1)}.                     \tag{6.1}
\]

On central profiles this variance is `Theta(d)`. The empty-edge and
singleton counts, and hence even the depth-one compatible-extension count,
vary inside one half-count profile. Across `b=m/d` blocks, the centered
depth-one carrier sum has variance `Theta(m)`. Since the block summands are
independent under the uniform measure on one ordered profile and are
bounded by `d=o(sqrt(m))`, the Lindeberg theorem splits that profile into
positive-density Gaussian subfamilies whose carrier sums differ by
`Theta(sqrt(m))`.

This observation is deterministic for every matching array: changing the
bijection only permutes which raw local sets occupy the hypergeometric
classes. Independent random rank matchings can decorrelate the target
look-ahead class from the owner class on unpromoted blocks, but they do not
make a realized graph transitive inside a profile. No asymptotic formula
for the full depth-`q` degree is needed for this conclusion.

Consequently (5.1) cannot be applied to a dual potential which selects an
arbitrary subset inside one profile. Nor can one average such a potential
over the blockwise coordinate group: a realized array of independent
permutations is not invariant under that group.

The exact next raw theorem is therefore a quenched all-cuts statement.
For example, it would suffice to prove, after deleting `o(N_q)` targets and
`o(W)` owners, that

\[
                         |N(\mathcal A)|
                         \ge(1+\delta_A)|\mathcal A| \tag{6.2}
\]

for every raw target family `mathcal A`, with `delta_A>0`. Max-flow,
min-cut, and bipartite integrality would then give a raw injection. The
profile theorem proves (6.2) only when `mathcal A` is a union of retained
half-count profiles.

One random permutation `pi_(j,k)` is reused by exponentially many raw
vertices. Hence concentration of the `e^{o(m)}` profile totals is not a
union bound over the `2^{N_q}` raw target families. A valid lift requires
a within-profile cut-norm theorem, a compression theorem for minimum Hall
cuts, or a targetwise fractional certificate.

## 7. Correction to the Gaussian rank-one profile-flow argument

Suppose, in addition to the theorem proved above, one establishes a
refined positive edge census between Gaussian target-status cells `z` and
owner-status cells `y` of the form

\[
                         c_A\phi(z)\phi(y)e^{A(z-y)}. \tag{7.1}
\]

Full support of this kernel would indeed remove every fixed finite
Gaussian profile cut. The associated uniform-capacity flow, however, must
send target mass proportionally to the owner **vertex capacity**
`phi(y)`, not proportionally to the edge factor `phi(y)e^(-Ay)`. The
latter choice gives owner load proportional to `e^(-Ay)` and is not
constant.

Once every retained cell pair has sufficiently many actual edges, the
correct profile flow is simply

\[
                         F(z,y)
 = {n_T(z)n_X(y)\over W_{\rm good}},                 \tag{7.2}
\]

whose owner load is `N_q/W=e^(-A^2)+o(1)` uniformly. Thus a proved
full-support census would still yield the claimed conclusion, but the
displayed exponential-tilt routing requires this correction.

The present note avoids that unproved refined census entirely: Sections
2--5 give a deterministic, exact coarser profile flow.

## 8. Raw injection is still not packet/chronology grouping

Even a proof of (6.2) would choose one distinct middle source separately
for each target at one fixed sign and depth. It would not ensure that

1. the selected exposed axes lie among the `r` axes retained in the
   source's physical `Q_r` packet;
2. the required axes form a consecutive window of one packet factor;
3. lower and upper choices use the same owner occurrence; or
4. the choices are nested and common for every `q<=H`.

The logical implications remain only

\[
 \boxed{
 \text{packet/chronology assignment}
 \Longrightarrow
 \text{selected-axis raw injection}
 \Longrightarrow
 \text{maximal raw injection}
 \Longrightarrow
 \text{profile flow}.}                              \tag{8.1}
\]

Only the rightmost object is proved here.

There is also an exact whole-cell twirl in
`MATH_THEOREM_RANK_TWISTED_LITERAL_TWIRL_AND_WEIGHTED_HALL_KERNEL_20260726.md`.
Its target load is the particular source-normalized quantity

\[
             \Lambda_q(T)=\sum_{X\sim T}{1\over\binom{S(X)}q}.  \tag{8.2}
\]

The quotient flow (4.5) is allowed to choose different fractional weights
on compatible profile arcs; it does not prove `Lambda_q(T)>=1`
targetwise, nor does it round the mutually exclusive whole-cell twirl
options. Thus the deterministic profile expansion and the literal twirl
are complementary necessary ingredients, not interchangeable conclusions.

## 9. Audited boundary

Proved:

1. the exact single-inclusion probability (1.2);
2. the exact deterministic profile incidence count (2.1);
3. a uniform `O_A(d^2/sqrt(m))` truncation to at most two promotions per
   block;
4. normalized fractional profile expansion with owner load
   `e^(-A^2)+o(1)` on both signs;
5. every arbitrary weighted Hall inequality in the aggregate half-profile
   quotient; and
6. the strict separation between profile flow, raw injection, and grouped
   packet chronology.

Not proved:

1. a within-profile or arbitrary-subset Hall theorem for one realized
   random matching array;
2. a raw source injection;
3. survival under an `r`-axis selector; or
4. simultaneous lower/upper, all-depth packet completion.

Independent rank matchings therefore remove the coarse allocation-profile
capacity obstruction, but their only possible remaining advantage lies in
a quenched within-profile mixing theorem. Potential reachability and
profile totals alone do not supply that theorem.
