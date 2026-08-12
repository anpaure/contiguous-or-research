# Independent rank matchings and the allocation-overlap Hall profile

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

In every macroblock \(B_j=A_j\dot\cup C_j\), choose the local-rank
matchings

\[
                  \pi_{j,k}:A_j\longrightarrow C_j
                  \qquad(0\le k\le2d)                              \tag{0.1}
\]

independently and uniformly. This changes none of the owner-tiling
arguments: every rank layer is still partitioned by its status cells, and
the product-cube leave remains \(2^{m+o(m)}\).

For

\[
                         d\asymp\log m,\qquad
                         q=A\sqrt m,\quad A>0,                     \tag{0.2}
\]

independence does remove the known fixed-allocation Gaussian obstruction
at the level of the allocation-overlap **profile quotient**.

The exact mechanism is simple. Conditional on one local set \(R\), the
full-pair counts measured in \(\pi_{j,k}\) and \(\pi_{j,k+1}\) are
independent hypergeometric variables. Thus, on the \(1-o(1)\) fraction of
unpromoted blocks, the target's look-ahead carrier profile and the owner's
actual status profile are independent. The \(q\) promoted blocks occupy
only

\[
                              {q\over m/d}=O(d/\sqrt m)=o(1)       \tag{0.3}
\]

of all blocks.

After centering, the lower and upper profile kernels both converge to

\[
 {\cal K}_A(z,y)
     =c_A\phi(z)\phi(y)e^{A(z-y)}
     =c_A'\phi(z-A)\phi(y+A),                                     \tag{0.4}
\]

with full support. Here \(z\) is the target carrier fluctuation and \(y\)
the owner status fluctuation. Since

\[
             {W\over N_q}
             ={\binom{2m}m\over\binom{2m}{m-q}}
             =e^{A^2+o(1)},                                      \tag{0.5}
\]

every cut in the finite Gaussian profile quotient has constant Hall slack.
The fixed-allocation diagonal kernel, by contrast, has ratio
\(\exp(2Az-A^2)\) and is deficient on \(z<A/2\).

This proves the following precise statement:

> With probability \(1-o(1)\), independent rank matchings eliminate every
> positive-density Hall cut which is measurable in the macro-rank,
> half-rank, and Gaussian empty/full status profiles.

It does **not** yet prove a raw source injection. A target family contained
inside one profile cell could still have an abnormally small neighborhood.
The missing raw theorem is a quenched within-profile cut-norm or normalized
expansion estimate. If that estimate is proved, the profile flow lifts to
a fractional matching, and bipartite integrality immediately gives a raw
injection.

Even that raw injection would remain strictly weaker than packet
completion: it chooses sources separately at one depth and one sign, and
does not enforce the retained \(r\) axes, whole-packet ownership, a cyclic
direction order, or common choices across depths.

The independent audit
MATH_ATTACK_RANK_TWISTED_ALLOCATION_OVERLAP_HALL_GATE_20260726.md
adds two qualifications.  First, after adjoining the owner's look-ahead
carrier, the uniform-edge kernel is nearly diagonal; the rank-one kernel
(0.4) is its projection after that carrier is forgotten and is not by
itself a neighborhood theorem.  The audit proves the positive-density
profile conclusion instead by a score-reservoir argument over deliberately
chosen one-hit allocations.  Second, a legal localized retained-axis rule
still gives an explicit \(\Omega(W)\) physical Hall cut on both signs.

## 1. Owner tiling is unchanged

Fixing an arbitrary perfect matching on every local rank layer partitions
that layer into disjoint zero/singleton/full status cells. The proof never
uses a relation between the matchings on two different ranks. Therefore
the independent choice (0.1) preserves:

1. the exact local status partition;
2. the product \(Q_S\)-cell partition;
3. the subdivision of every \(Q_S\), \(S\ge r\), into parallel \(Q_r\)'s;
4. the fact that every physical direction crosses \(A_j\) to \(C_j\); and
5. the low-dimension leave \(2^{m+o(m)}\).

The status enumerator is also deterministic:

\[
 \sum_Xx^{|X|}y^{S(X)}
       =(1+x)^\rho(1+2xy+x^2)^N,                                  \tag{1.1}
\]

where \(N=d\lfloor m/d\rfloor=m-O(d)\) is the number of nonresidual
coordinate pairs and \(\rho=2m-2N<2d\).

Thus random rank matchings alter incidences but not owner counts or the
split-axis census.

## 2. Exact maximal compatibility graph

The graph in this note is the maximal status-atlas graph, before retaining
only \(r\) axes of a \(Q_S\)-cell.

For a lower target \(T\), write

\[
                         T_j=T\cap B_j,\qquad t_j=|T_j|.           \tag{2.1}
\]

If \(\ell_j\) coordinates are promoted in block \(j\), the source rank is
\(k_j=t_j+\ell_j\), so the relevant matching is \(\pi_{j,t_j+\ell_j}\).
Let

\[
 e_{j,k}(T_j)
   =\#\{a\in A_j:a\notin T_j,\ \pi_{j,k}(a)\notin T_j\}.           \tag{2.2}
\]

Then

\[
 \boxed{
 D_q^-(T)=[z^q]\prod_j
 \left(
   \sum_{\ell=0}^d
      2^\ell\binom{e_{j,t_j+\ell}(T_j)}{\ell}z^\ell
 \right).}                                                       \tag{2.3}
\]

For an upper target \(U\), with \(u_j=|U\cap B_j|\), put

\[
 f_{j,k}(U_j)
   =\#\{a\in A_j:a\in U_j,\ \pi_{j,k}(a)\in U_j\}.                 \tag{2.4}
\]

Then

\[
 \boxed{
 D_q^+(U)=[z^q]\prod_j
 \left(
   \sum_{\ell=0}^d
      2^\ell\binom{f_{j,u_j-\ell}(U_j)}{\ell}z^\ell
 \right).}                                                       \tag{2.5}
\]

For a middle owner \(X\), if \(S(X)\) is its number of singleton edges in
the intrinsic matchings \(\pi_{j,|X_j|}\), then its degree on either sign
is exactly

\[
                              d_R(X)=\binom{S(X)}q.                \tag{2.6}
\]

Consequently

\[
 \sum_TD_q^\pm(T)=\sum_X\binom{S(X)}q
 =2^q\binom Nq\binom{2m-2q}{m-q}.                                \tag{2.7}
\]

Equations (2.3)--(2.7) are valid for every realization of the independent
matchings.

## 3. Exact local random-matching law

Fix a local set \(R\subseteq A\cup C\), and put

\[
              \alpha=|R\cap A|,\qquad \gamma=|R\cap C|.           \tag{3.1}
\]

For a uniform random matching \(\pi:A\to C\), its number \(F\) of full
edges on \(R\) is hypergeometric:

\[
 F\sim\operatorname{Hyp}(d,\gamma,\alpha),\qquad
 \mathbb EF={\alpha\gamma\over d},                                \tag{3.2}
\]

\[
 \operatorname{Var}F
 ={\,\alpha\gamma(d-\alpha)(d-\gamma)\over d^2(d-1)}.             \tag{3.3}
\]

The number of empty edges is

\[
 E=d-\alpha-\gamma+F,\qquad
 \mathbb EE={(d-\alpha)(d-\gamma)\over d}.                        \tag{3.4}
\]

Most importantly, if \(k\ne k'\), then the variables measured in
\(\pi_{j,k}\) and \(\pi_{j,k'}\) are independent conditional on \(R\).
This exact conditional independence replaces the correlated cyclic-shift
identities.

For later reference, fix an inclusion \(T_j\subset X_j\). Let
\(\ell_A=|(X_j\setminus T_j)\cap A_j|\) and
\(\ell_C=|(X_j\setminus T_j)\cap C_j|\), and put
\(\alpha=|X_j\cap A_j|\), \(\gamma=|X_j\cap C_j|\). Its exact lower
retention probability under a uniform \(\pi_{j,|X_j|}\) is

\[
 p_j^-(T_j,X_j)
 ={(d-\gamma)_{\underline{\ell_A}}\over
    d_{\underline{\ell_A}}}
  {(d-\alpha)_{\underline{\ell_C}}\over
    (d-\ell_A)_{\underline{\ell_C}}}.                             \tag{3.5}
\]

For an upper inclusion \(X_j\subset U_j\), where
\(\ell_A=|(U_j\setminus X_j)\cap A_j|\) and similarly for \(C_j\),

\[
 p_j^+(X_j,U_j)
 ={\gamma_{\underline{\ell_A}}\over
    d_{\underline{\ell_A}}}
  {\alpha_{\underline{\ell_C}}\over
    (d-\ell_A)_{\underline{\ell_C}}}.                             \tag{3.6}
\]

On central half profiles with \(\ell_A+\ell_C=o(\sqrt d)\), both are
\(2^{-\ell_A-\ell_C}\exp(o(1))\).

### The fixed-allocation control

Freezing one allocation also freezes one product matching. If a lower
target has \(E\) empty and \(U\) singleton edges in that matching, the
target and source degrees inside the preserved status profile are

\[
                         2^q\binom Eq,\qquad
                         \binom{U+q}q.                             \tag{3.7}
\]

At the Gaussian center,

\[
 E={m\over4}+{q\over2}+{z\sqrt m\over4}+o(\sqrt m),
 \qquad U={m\over2}+o(\sqrt m),
\]

and therefore

\[
 \log\left(
 {2^q\binom Eq\over\binom{U+q}q}
 \right)=2Az-A^2+o(1).                                           \tag{3.8}
\]

The profiles \(z<A/2-\varepsilon\) have a positive-mass deficit. This
calculation is unchanged by randomizing the matching: randomness changes
which raw targets occupy the profile, not its fixed-allocation ratio. The
only possible repair is overlap between different allocations and
independent rank frames.

## 4. Half-rank profiles create no Gaussian deficit

The mean first lower coefficient in block \(j\) is

\[
 w_j^-(T)
   =2\,{(d-\alpha_j)(d-\gamma_j)\over d},                         \tag{4.1}
\]

and the mean first upper coefficient is

\[
 w_j^+(U)
   =2\,{\alpha_j\gamma_j\over d}.                                 \tag{4.2}
\]

Write \(\alpha_j=d/2+x_j\), \(\gamma_j=d/2+y_j\). Then

\[
\begin{aligned}
 w_j^-&={d\over2}-(x_j+y_j)+{2x_jy_j\over d},\\
 w_j^+&={d\over2}+(x_j+y_j)+{2x_jy_j\over d}.
\end{aligned}                                                     \tag{4.3}
\]

At fixed global target rank, \(\sum_j(x_j+y_j)\) is deterministic up to
the \(O(d)\) residual coordinates. Moreover

\[
                         \operatorname{Var}
            \left({2\over d}\sum_jx_jy_j\right)=O(m/d).           \tag{4.4}
\]

Hence, outside \(o(N_q)\) targets,

\[
 \sum_jw_j^\pm={m\over2}+O(\sqrt m)+O(\sqrt{m/d}\,\omega_m),      \tag{4.5}
\]

for any \(\omega_m\to\infty\) sufficiently slowly. The last fluctuation
changes the logarithm of the \(q\)-coefficient by only

\[
                         O(q/\sqrt{md})=o(1).                     \tag{4.6}
\]

Thus macro-rank and half-rank profiles do not reproduce the fixed-frame
constant deficit. The only order-one profile fluctuation comes from the
random matching status itself.

## 5. Allocation saddle

Let \(b=N/d\sim m/d\). Under the coefficient saddle in (2.3) or (2.5),

\[
 {q^2\over b}=\Theta(d),\qquad
 {q^3\over b^2}=o(1).                                             \tag{5.1}
\]

Thus:

* \(q-O(d)\) blocks receive one promotion;
* \(O(d)\) blocks receive two promotions; and
* blocks receiving three or more promotions have total contribution
  \(o(1)\).

The saddle is

\[
                              z_*={2A\over\sqrt m}(1+o(1)).       \tag{5.2}
\]

The doubly promoted blocks contribute an order-one deterministic
second-saddle correction. Independence of the rank-\((t+2)\) matchings
makes the random fluctuation of that correction \(O(d/\sqrt m)=o(1)\).
Thus it does not create another Gaussian profile variable. The Gaussian
part of a lower target degree is controlled by

\[
 Z^-(T)
 ={4\over\sqrt m}\sum_j
 \left(
 e_{j,t_j+1}(T_j)
 -{(d-\alpha_j)(d-\gamma_j)\over d}
 \right),                                                        \tag{5.3}
\]

and the upper analogue is

\[
 Z^+(U)
 ={4\over\sqrt m}\sum_j
 \left(
 f_{j,u_j-1}(U_j)-{\alpha_j\gamma_j\over d}
 \right).                                                        \tag{5.4}
\]

Conditional on the target, the summands are independent, centered, and
bounded by \(d\), with total variance \(m/16+o(m)\) on central profiles.
The Lindeberg theorem gives

\[
                              Z^\pm\Rightarrow N(0,1).            \tag{5.5}
\]

On profile \(Z^\pm=z\), the target degree has the saddle tilt

\[
                              D_q^\pm(T)=D_0^\pm(T)e^{Az+o(1)},   \tag{5.6}
\]

where \(D_0^\pm\) depends only on the non-Gaussian macro profile and is
constant to \(e^{o(1)}\) on the good core from Section 4.

## 6. Independence from the owner profile

For a middle owner \(X\), define its centered full-pair profile

\[
 Y(X)={4\over\sqrt m}\sum_j
 \left(
 f_{j,|X_j|}(X_j)-{|X_j\cap A_j|\,|X_j\cap C_j|\over d}
 \right).                                                        \tag{6.1}
\]

The singleton count satisfies

\[
                              S(X)=S_0(X)-{\sqrt m\over2}Y(X),    \tag{6.2}
\]

with \(S_0(X)=m/2+o(\sqrt m)\) on the good half-rank core. Therefore

\[
                              \binom{S(X)}q
                  =D_R^0(X)e^{-AY(X)+o(1)}.                       \tag{6.3}
\]

For a lower incidence, every unpromoted block compares
\(\pi_{j,t_j+1}\), used in \(Z^-(T)\), with \(\pi_{j,t_j}\), used in
\(Y(X)\). These matchings are independent. Promoted blocks occupy the
fraction (0.3), and their total normalized covariance is \(o(1)\).
The same statement holds above with ranks \(u_j-1\) and \(u_j\).

Consequently the joint Gaussian edge profile satisfies

\[
                              (Z^\pm,Y)\Rightarrow
                              N(0,1)\otimes N(0,1).                \tag{6.4}
\]

Combining the vertex densities with the degree tilts (5.6) and (6.3)
gives the rank-one edge kernel (0.4).

This is the exact Gaussian advantage of independent rank matchings.
For one frozen allocation the status profile is diagonal and deficient;
after summing allocations, independent adjacent-rank frames replace that
diagonal by a product kernel.

There is a hidden source variable which this statement intentionally
forgets.  Define the lower source look-ahead carrier by evaluating
\(\pi_{j,|X_j|+1}\) on every unpromoted block, and define the upper
look-behind carrier analogously.  On all but the \(q=o(b)\) promoted
blocks this carrier is literally the target carrier.  Hence the edge
kernel augmented by this variable is nearly diagonal.  Formula (0.4)
is correct as a \((Z,Y)\)-marginal, but first moments in that marginal do
not control source unions.  The score-reservoir theorem in the independent
audit shows that nonuniformly choosing \(q\) promotion blocks can tune the
hidden carrier and is the additional reason the full coarse profile cut
has enough neighbors.

## 7. Profile-compressed fractional Hall

Choose \(K_m\to\infty\) slowly and divide \([-K_m,K_m]\) into intervals
of width \(\eta_m\to0\), also slowly. Add the finitely many typical
macro-rank and half-rank classes from Section 4. The resulting number of
profile cells is \(\exp(\operatorname{polylog}m)=\exp(o(m/d))\).

For independent rank matchings, block concentration and the conditional
central limit theorem imply, simultaneously for all retained profile-cell
pairs, that their normalized edge census is

\[
 (1+o(1))c_A\phi(z)\phi(y)e^{A(z-y)}.                             \tag{7.1}
\]

The discarded target and owner mass is \(o(W)\). Every entry of (7.1) is
positive, and its raw edge multiplicity is much larger than either
profile-cell vertex capacity.

To justify the simultaneous statement, encode one block by its normalized
bivariate status polynomial, marking its local rank, half-ranks, carrier
count, and owner singleton count. For fixed marks these polynomials are
independent across \(j\), have coefficients bounded by \(4^d\), and their
logarithms at the saddle (5.2) have uniformly bounded exponential moments.
Bernstein concentration over \(b=m/d+O(1)\) blocks is
\(\exp(-\Omega(m/d))\). The number of retained histogram cells and saddle
grid points is \(\exp(\operatorname{polylog}m)=\exp(o(m/d))\), so a union
bound is valid. Uniform coefficient extraction then gives (7.1).

### Theorem 7.1 (profile Hall)

With probability \(1-o(1)\), the lower and upper allocation-overlap graphs
separately admit a fractional flow on their profile quotients which
saturates every retained target profile cell and uses at most

\[
                              e^{-A^2}+o(1)<1                     \tag{7.2}
\]

of every retained owner profile capacity.

#### Proof

After the exponential tilts, (7.1) is a positive rank-one kernel. Send
each target profile proportionally to the owner factor
\(\phi(y)e^{-Ay}\). This saturates the target side. Its total owner load is
the ratio of the two shore sizes,

\[
                              {N_q\over W}=e^{-A^2+o(1)},         \tag{7.3}
\]

and the product form makes this load the same on every owner profile.
The \(o(1)\) census error is absorbed by the constant slack in (7.2).
\(\square\)

Equivalently, every dual cut whose potential is constant on these profile
cells has nonnegative slack, with a constant margin unless it is the zero
cut.

This is a flow in the compressed quotient only.  It must not be lifted by
distributing a cell-to-cell flow over its raw incidences without proving
row and column expansion inside that pair of cells.  For whole
positive-density carrier cells, the allocation score-reservoir theorem
cited above supplies an actual neighborhood-capacity proof.  Arbitrary
subsets of one cell remain exactly the QRE gate below.

## 8. The exact raw expansion gate

Theorem 7.1 is not yet a fractional matching on individual targets and
owners. To lift it, one needs the following quenched statement for the
realized random atlas.

### QRE\(_A\) (quenched rank expansion)

After deleting \(o(N_q)\) targets and \(o(W)\) owners, every target family
\(\mathcal A\) satisfies

\[
                         |N(\mathcal A)|
                              \ge(1+\delta_A)|\mathcal A|,        \tag{8.1}
\]

for some fixed \(\delta_A>0\). Equivalently, after replacing
\(\delta_A\) by \(\delta_A/(1+\delta_A)\), the normalized incidence matrix
admits target row sums \(1\) and owner column sums at most
\(1/(1+\delta_A)<1\).

A sufficient analytic form is a within-profile cut estimate

\[
 e(\mathcal A,\mathcal B)
 =(1+o(1))
 {d(\mathcal A)d(\mathcal B)\over
  \sum_Xd(X)}                                                    \tag{8.2}
\]

uniformly for profile-contained sets above the inverse-degree scale,
together with the corresponding minimum-degree bound for smaller sets.

If QRE\(_A\) holds, max-flow/min-cut gives a fractional matching saturating
all retained raw targets. The bipartite matching polytope is integral, so
there is an actual injection of those targets into distinct middle
sources.

The independent matching model makes QRE\(_A\) plausible, but Theorem 7.1
does not prove it. The unresolved issue is that all targets in one profile
cell reuse the same \(O(m)\) random local matchings; ordinary concentration
of the profile census does not control every one of the
\(2^{N_q}\) target subfamilies. A proof needs either:

1. a cut-norm theorem for products of independent random permutation
   kernels;
2. a compression theorem showing every minimum Hall cut is a union of the
   profiles used above; or
3. a direct normalized-matching theorem for the random local inclusion
   operators.

No linear deficit survives in the proved profile dual, but raw Hall is not
claimed.

## 9. Separation from packets and chronology

Even QRE\(_A\) would prove only a raw one-depth injection in the maximal
status atlas. It would not choose:

* the \(r\) retained axes inside each \(Q_S\)-cell;
* one \(Q_r\) subpacket for each owner;
* a cyclic direction word;
* the same source for lower and upper signs; or
* one common selection for all \(q\le H\).

Those are additional integral constraints. In logical order, the remaining
gates are

\[
\boxed{
\text{profile Hall}
\ \Longrightarrow\
\text{QRE}_A
\ \Longrightarrow\
\text{raw injection}
\ \Longrightarrow\
\text{packet/chronology grouping}.}                              \tag{9.1}
\]

Only the first implication target is proved here: independent rank
matchings remove every profile-compressed Gaussian Hall deficit. The raw
injection and packet grouping remain separate theorems.  In particular,
the maximal-atlas result does not license an arbitrary deterministic
\(r\)-axis selector: the localized-selector cut in the independent audit
misses \((1-o(1))N_q\) lower and upper targets regardless of the compiler.
