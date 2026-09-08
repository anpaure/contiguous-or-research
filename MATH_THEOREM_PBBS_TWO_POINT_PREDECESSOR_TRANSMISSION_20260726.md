# PBBS two-point return correlation: exact predecessor transmission

Date: 2026-07-26

Method: pure mathematics only.  No computation, probabilistic occupancy
model, or web input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
 \qquad G=2H-1.
\]

Let \(\tau\) be the step-two PBBS permutation of the normalized Dyck
roots, discard its cycles of length at most \(H+1\), and let \(R_H\) and
\(\mathcal C_H\) be the one- and two-point quantities in
`PBBS_ST_TWO_POINT_CLUSTERING_DICHOTOMY_20260726.md`.

This note gives the exact two-point consequence of the predecessor kernel.
For a reduced root \(F\), let \(B_2(F)\) be the time of the second positive
selection of the immediate predecessor of the time-zero selected equality
particle.  Define the actual predecessor-active set

\[
 \mathscr A_H
 =\{F:B_2(F)\le G\}.                              \tag{0.1}
\]

If \(F\) has semilength \(d\) and \(k\) peaks, give it the inverse-fibre
weight

\[
 P_r(F)=\binom{r+d-k}{2d}.                         \tag{0.2}
\]

The two reduced statistics which survive are

\[
 \begin{aligned}
 S_{r,H}
   &=\sum_F P_r(F)\mathbf1_{\mathscr A_H}(F),\\
 K_{r,H}
   &=\sum_{u=1}^{H+1}\sum_F P_r(F)
     \mathbf1_{\mathscr A_H}(F)
     \mathbf1_{\mathscr A_H}(\tau^uF).
 \end{aligned}                                    \tag{0.3}
\]

The sums run over the nonempty cores which have rank-\(r\) inverse lifts,
that is, \(1\le d\le r-1\) and \(d+k\le r\).  Then

\[
 \boxed{
 \begin{aligned}
  (3/4-o(1))S_{r,H}-o(B_r/H)
      &\le R_H\le S_{r,H}+o(B_r/H),\\
  (1/2-o(1))K_{r,H}-o(B_r/H)
      &\le \mathcal C_H\le K_{r,H}+o(B_r/H).
 \end{aligned}}                                   \tag{0.4}
\]

All constants in (0.4) come from exact Pascal fibres.  In particular,
the lower two-point constant does not assume that two slot coordinates are
independent: it is the deterministic inequality

\[
 |A\cap A'|\ge |A|+|A'|-P
\]

inside one fibre of size \(P\).

Consequently, at the critical scale \(S_{r,H}=\Theta(B_r/H)\),

\[
 \boxed{
 R_H=\Theta(B_r/H),\qquad
 {\mathcal C_H\over R_H}\asymp {K_{r,H}\over S_{r,H}}.}
                                                               \tag{0.5}
\]

Thus inverse peak deletion neither creates nor destroys a divergent
two-point cluster: it transmits the actual reduced predecessor-active
autocorrelation up one rank scale with fixed positive constants.

This does **not** prove either requested asymptotic alternative.  The exact
predecessor kernel by itself proves neither

\[
 S_{r,H}=\Omega(B_r/H)
\]

nor a bound or divergence for \(K_{r,H}/S_{r,H}\).  The surviving theorem
is now a literal PBBS statement, not an occupancy surrogate:

\[
 \boxed{
 \text{control the short-lag autocorrelation under \(\tau\) of the roots
 whose actual predecessor has a second selection by time \(2H-1\).}}
                                                               \tag{0.6}
\]

In particular, the predecessor GF in
`MATH_ATTACK_R_PBBS_GAUSSIAN_RETURN_GF_PACKING_20260725.md` cannot by
itself choose between \(\mathcal C_H=O(R_H)\) and
\(\mathcal C_H/R_H\to\infty\).  It supplies the exact fibre multiplier;
the missing datum is the phase arrangement of (0.1) on the actual reduced
\(\tau\)-orbits.  The separate deletion in Section 5 handles short
**parent** cycles; a parent-long orbit may still project to a short reduced
orbit.

## 1. Exact one-phase support

Fix a nonempty reduced root

\[
 F\in\mathcal D_d,\qquad k=\operatorname {pk}(F).
\]

The inverse peak-deletion fibre \(\Omega_r(F)\) is obtained by distributing

\[
 y=r-d-k
\]

free leaves among

\[
 p=2d+1
\]

ordered slots.  Hence

\[
 |\Omega_r(F)|
 =\binom{y+p-1}{p-1}
 =P_r(F).                                         \tag{1.1}
\]

Let \(z_*\) be the free occupancy of the final root slot.  In the reduced
equality-particle PBBS, denote by

\[
 0<B_1(F)<B_2(F)<\cdots
\]

the positive selection times of the immediate predecessor of the
time-zero selected particle.  The exact no-overtaking predecessor theorem
states that the first outer physical return of a lift with \(z_*=a\) is

\[
 B_{2a+2}(F),                                     \tag{1.2}
\]

provided this time is less than \(N\).  Here \(G<N\) for all sufficiently
large \(r\).

Define

\[
 a_H(F)=\max\{a\ge0:B_{2a+2}(F)\le G\},           \tag{1.3}
\]

with value \(-1\) if the set is empty.  Since the occurrence times are
strictly increasing, the eligible lifts over \(F\) are exactly

\[
 \mathcal E_H(F)
 =\{D\in\Omega_r(F):z_*(D)\le a_H(F)\}.           \tag{1.4}
\]

In particular,

\[
 \mathcal E_H(F)\ne\varnothing
 \quad\Longleftrightarrow\quad
 B_2(F)\le G
 \quad\Longleftrightarrow\quad
 F\in\mathscr A_H.                                \tag{1.5}
\]

Stars and bars gives the exact size

\[
 |\mathcal E_H(F)|
 =P_r(F)-
   \binom{r+d-k-a_H(F)-1}{2d},                    \tag{1.6}
\]

where the second term is zero when its upper argument is below \(2d\).
If the fibre is active, it contains the entire terminal-zero hyperplane,
so

\[
 \boxed{
 \alpha_r(d,k)P_r(F)
 \le |\mathcal E_H(F)|\le P_r(F),
 \qquad
 \alpha_r(d,k)={2d\over r+d-k}.}                 \tag{1.7}
\]

This is the first important point.  A reduced phase does not contribute a
rare \(1/H\) fraction of its parent fibre.  It contributes no parent at
all, or at least the constant terminal-zero fraction (1.7).

## 2. Actual two-phase fibre transport

Peak deletion commutes with \(\tau\).  Therefore, for every \(u\), PBBS
evolution gives a bijection

\[
 \Sigma_F^{(u)}:
 \Omega_r(F)\longrightarrow\Omega_r(\tau^uF).     \tag{2.1}
\]

The exact number of parent roots over the phase pair
\((F,\tau^uF)\) which are eligible at both times is

\[
 J_u(F)=
 \left|
 \mathcal E_H(F)\cap
 (\Sigma_F^{(u)})^{-1}\mathcal E_H(\tau^uF)
 \right|.                                        \tag{2.2}
\]

The peak count is constant on a reduced PBBS orbit, so the two fibres in
(2.1) have the same size \(P_r(F)\).  If either reduced phase is not in
\(\mathscr A_H\), then \(J_u(F)=0\).  If both are active, (1.7) and
inclusion--exclusion inside \(\Omega_r(F)\) give

\[
 \boxed{
 (2\alpha_r(d,k)-1)P_r(F)
 \le J_u(F)\le P_r(F),}                           \tag{2.3}
\]

whenever the displayed lower coefficient is positive.

No description of \(\Sigma_F^{(u)}\) was used in (2.3).  It is valid for
the literal, topology-changing PBBS sector transport and for every amount
of fibre holonomy.

There is also a more explicit particle-gap description.  Label equality
particles in their preserved cyclic order.  Let \(j_u\) be the selected
particle after \(2u\) one-step updates and let \(j_u^-\) be its immediate
predecessor.  On compatible integer lifts put

\[
 C_j(s)=|\{0\le v<s:\kappa_v=j\}|.
\]

If

\[
 q_j={x_j(0)-x_{j^-}(0)-1\over2}

is the initial inserted-peak count in the particle gap, then at the even
phase \(u\)

\[
 \boxed{
 q_{j_u}^{(u)}
 =q_{j_u}
  +{C_{j_u}(2u)-C_{j_u^-}(2u)\over2}.}            \tag{2.4}
\]

The right side is integral because an even PBBS phase is again a Dyck-root
phase.  Equation (2.4) follows directly from

\[
 x_j(s)=x_j(0)+C_j(s).
\]

Thus, after subtracting the compulsory leaf in each compulsory slot, the
pullback of (1.4) is a one-coordinate upper-bound event in the initial
weak-composition simplex.  It is not an arbitrary occupancy event and it
does not rely on a random model.

For reference, if two pulled tests address distinct free coordinates and
give upper bounds \(a,b\ge0\), their exact intersection size is

\[
 \begin{aligned}
 V_{y,p}(a,b)
  ={}&\binom{y+p-1}{p-1}
  -\binom{y-a-1+p-1}{p-1}
  -\binom{y-b-1+p-1}{p-1}\\
  &+\binom{y-a-b-2+p-1}{p-1},                    \tag{2.5}
 \end{aligned}
\]

with the usual zero convention.  For the same coordinate it is

\[
 U_{y,p}(\min(a,b))
 =\binom{y+p-1}{p-1}
  -\binom{y-\min(a,b)-1+p-1}{p-1}.               \tag{2.6}
\]

At the Pascal saddle \(d=r/2+o(r)\), \(k=r/6+o(r)\), one has
\(p/(p+y)\to3/4\).  Hence, for fixed \(a,b\),

\[
 {U_{y,p}(a)\over P_r(F)}
   \longrightarrow1-4^{-(a+1)},                  \tag{2.7}
\]

and for distinct coordinates

\[
 {V_{y,p}(a,b)\over P_r(F)}
   \longrightarrow
   (1-4^{-(a+1)})(1-4^{-(b+1)}).                 \tag{2.8}
\]

In particular, two terminal-zero tests have limiting intersection
\(9/16\) when their coordinates differ and \(3/4\) when they coincide.
This confirms directly that the inverse-Pascal layer has no vanishing
two-point factor.

## 3. Exact untrimmed identities

Let \(\widetilde R_H\) and \(\widetilde{\mathcal C}_H\) denote the same
statistics as \(R_H,\mathcal C_H\), before deleting short parent
\(\tau\)-cycles.  Partitioning parent roots by their pruned roots gives

\[
 \boxed{
 \widetilde R_H=\sum_F|\mathcal E_H(F)|.}         \tag{3.1}
\]

Using semiconjugacy and transporting the second phase back to the first
fibre gives

\[
 \boxed{
 \widetilde{\mathcal C}_H
 =\sum_{u=1}^{H+1}\sum_FJ_u(F).}                 \tag{3.2}
\]

Equations (3.1)--(3.2) are identities for the actual PBBS dynamics.  They
are the two-point extension of the one-point predecessor GF.

## 4. Pascal saddle and the constants \(3/4,1/2\)

The total inverse-fibre mass in a cell \((d,k)\) is

\[
 \mathsf M_r(d,k)
 =\frac1d\binom dk\binom d{k-1}
  \binom{r+d-k}{2d}.                              \tag{4.1}
\]

Its unique entropy saddle is

\[
 d=r/2,\qquad k=r/6.                              \tag{4.2}
\]

Uniform Stirling expansion, followed by the quadratic tail bound, gives

\[
 \sum_{
   |d-r/2|+|k-r/6|>2\sqrt{r\log r}}
   \mathsf M_r(d,k)
 =o(B_r/N).                                       \tag{4.3}
\]

For completeness, the exponent in the central variables
\(x=k/r,y=d/r\) is

\[
 2y\,h(x/y)
 +(1+y-x)h\!\left({2y\over1+y-x}\right),         \tag{4.4}
\]

whose unique maximum is \(\log4\) at \((1/6,1/2)\).  In the normalized
variables \(u=(k-r/6)/\sqrt r\), \(v=(d-r/2)/\sqrt r\), the conservative
Gaussian bound is

\[
 {\mathsf M_r(d,k)\over B_r}
 \le {C\over r}
 \exp\!\left[-{\lambda_*\over4}(u^2+v^2)\right],
 \qquad
 \lambda_*={57-3\sqrt{73}\over4}.                \tag{4.4a}
\]

Outside the displayed \(L^1\)-tube,
\(u^2+v^2>2\log r\).  Since \(\lambda_*/2>3\), summing (4.4a) over at
most \(r^2\) cells is \(o(B_r/r)=o(B_r/N)\).  Uniform Taylor expansion is
valid throughout the tube because its cubic remainder is
\(O((\log r)^{3/2}/\sqrt r)=o(1)\); compactness supplies an exponential
gap outside a fixed neighbourhood of the saddle.  This proves (4.3) with
the scale needed below, and is the same Pascal moderate-deviation estimate
used in the one-point kernel audit.

Uniformly in the tube in (4.3),

\[
 \alpha_r(d,k)
 ={2d\over r+d-k}=3/4+o(1),                       \tag{4.5}
\]

and hence

\[
 2\alpha_r(d,k)-1=1/2+o(1).                       \tag{4.6}
\]

Applying (1.7) cell by cell to (3.1), and deleting the mass (4.3), gives

\[
 (3/4-o(1))S_{r,H}-o(B_r/N)
 \le\widetilde R_H\le S_{r,H}.                  \tag{4.7}
\]

Similarly, (2.3) and (3.2) give

\[
 (1/2-o(1))K_{r,H}-o(B_r/H)
 \le\widetilde{\mathcal C}_H\le K_{r,H}.        \tag{4.8}
\]

The error in (4.8) is \((H+1)o(B_r/N)=o(B_r/H)\), because
\(H^2=\Theta_A(r)\).

## 5. Long-cycle audit

Let \(Z_H\) be the number of parent quotient roots on \(\tau\)-cycles of
length at most \(H+1\).  The standard word-description bound is

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(r)).                 \tag{5.1}
\]

Deleting these roots changes the one-point count by at most \(Z_H\), and
changes the summed two-point count by at most

\[
 (H+1)Z_H.                                       \tag{5.2}
\]

Since \(B_r/H=\exp((\log4+o(1))r)\), both quantities in
(5.1)--(5.2) are \(o(B_r/H)\).  Combining this with
(4.7)--(4.8) proves (0.4).  Thus no short quotient cycle is being used to
manufacture either constant.

## 6. The precise surviving correlation gate

Write

\[
 a_H(F)=\mathbf1\{B_2(F)\le2H-1\}.               \tag{6.1}
\]

Then the remaining two-point term is literally

\[
 K_{r,H}
 =\sum_{u=1}^{H+1}\sum_F
   P_r(F)a_H(F)a_H(\tau^uF).                      \tag{6.2}
\]

The predicate in (6.1) is an actual statement about the selected-particle
itinerary: if \(-1\) denotes the immediate predecessor of the time-zero
particle, then

\[
 a_H(F)=1
 \quad\Longleftrightarrow\quad
 \#\{1\le s\le2H-1:\kappa_s(F)=-1\}\ge2.        \tag{6.3}
\]

The weight \(P_r(F)\) is \(\tau\)-invariant because the reduced rank and
peak count are invariant on a PBBS orbit.  Therefore (6.2) is a genuine
weighted short-lag autocorrelation on the actual reduced \(\tau\)-orbits.

Equations (0.4) imply the following exact decision boundary.

### Corollary 6.1 (equivalence at critical mass)

Along any subsequence on which \(S_{r,H}=\Theta(B_r/H)\):

1. \(R_H=\Theta(B_r/H)\);
2. \(\mathcal C_H=O(R_H)\) if and only if
   \(K_{r,H}=O(S_{r,H})\);
3. \(\mathcal C_H/R_H\to\infty\) if and only if
   \(K_{r,H}/S_{r,H}\to\infty\).

The implications use only the fixed positive constants in (0.4), so there
is no rounding or hidden uniform-integrability issue.

The first requested branch would follow from

\[
 S_{r,H}=\Omega(B_r/H),\qquad K_{r,H}=O(S_{r,H}). \tag{6.4}
\]

The second would follow, at critical mass, from

\[
 K_{r,H}/S_{r,H}\longrightarrow\infty.           \tag{6.5}
\]

Neither (6.4) nor (6.5) is a consequence of the predecessor occurrence
formula.  Formula (1.2) determines how many parent sheets lie over one
active reduced phase.  It gives no information about the positions of the
active phases (6.1) along a reduced \(\tau\)-cycle, and (6.2) depends
exactly on those positions.

The distinction is sharp.  The Pascal fibre does not wash out the phase
arrangement: (2.3) shows that every active reduced phase pair retains at
least half of the critical parent fibre.  Conversely, an isolated active
reduced phase creates no parent pair at a lag where the reduced phase is
inactive.  Hence neither an independence heuristic nor a claim of
automatic slot clustering can decide the sign.

## 7. Final audited boundary

Proved here:

1. the exact support equivalence
   \(\mathcal E_H(F)\ne\varnothing\iff B_2(F)\le2H-1\);
2. the exact cumulative Pascal count (1.6);
3. the actual two-phase transport identity (3.2);
4. the holonomy-independent overlap lower bound (2.3);
5. the saddle constants \(3/4\) and \(1/2\);
6. the long-cycle errors \(o(B_r/H)\); and
7. the equivalence (0.5) with the weighted reduced autocorrelation (6.2).

Not proved:

1. \(S_{r,H}=\Omega(B_r/H)\);
2. \(K_{r,H}=O(S_{r,H})\); or
3. \(K_{r,H}/S_{r,H}\to\infty\).

Accordingly, neither \(R_H=\Omega(B_r/H),\ \mathcal C_H=O(R_H)\) nor
\(\mathcal C_H/R_H\to\infty\) is presently justified.  The exact next
analytic object is (6.2), with the literal block-rotation/selected-particle
dynamics of \(\tau\).  Any proof that replaces (6.3) by independent
occupancy variables loses precisely the information still required.
