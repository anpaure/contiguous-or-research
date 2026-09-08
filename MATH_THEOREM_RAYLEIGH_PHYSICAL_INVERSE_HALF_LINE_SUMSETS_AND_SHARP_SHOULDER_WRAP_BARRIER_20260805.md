# Physical Bellman inverses on the half-line, mixed sumsets, and the sharp shoulder-wrap barrier

**Date:** 2026-08-05  
**Method:** pure mathematics; generalized inverses, one-dimensional
sumsets, and an explicit Bellman family; no computation, search, or solver  
**Status:** unconditional theorem and sharp no-go.  The generalized-inverse
method extends exactly from a formal Apéry clock to its physical Bellman
minorant on the half-line.  Periodizing the physical inverse fails only at
wrapped sums, with the availability shoulder as the canonical error term.
The corresponding mixed formal/physical sumset inequality is exact but
one-sided.  A direct finite-prefix analogue of the cyclic variance theorem
is false, even for saturated first-minimum Bellman tables; the counterfamily
also shows why the missing theorem must retain the sign change of the
Rayleigh kernel rather than use an unsigned moment bound.

## 0. Normalized setting

Let

\[
 0=A_0\le A_1\le A_2\le\cdots,
 \qquad A_{i+j}\ge A_i+A_j,
 \qquad A_n\le n                                      \tag{0.1}
\]

be a normalized physical Bellman clock.  In the Rayleigh application

\[
                         A_n={V_n\over\lambda},       \tag{0.2}
\]

where \(\lambda\) is the maximum denomination density.  Let
\(\bar A_n=U_n/\lambda\) be its formal Apéry clock.  Thus

\[
 A_n\le\bar A_n,
 \qquad A_n=\bar A_n\quad(n\ge C),                   \tag{0.3}
\]

and, for the normalized residue period \(g\),

\[
                  \bar A_{n+g}=\bar A_n+g.           \tag{0.4}
\]

Define left generalized inverses on the nonnegative half-line by

\[
 \begin{aligned}
 B(t)&=\min\{n\ge0:A_n\ge t\},\\
 \bar B(t)&=\min\{n\ge0:\bar A_n\ge t\},
 \end{aligned}                                      \tag{0.5}
\]

and their equal-work discrepancies

\[
 u(t)=B(t)-t,
 \qquad \bar u(t)=\bar B(t)-t.                      \tag{0.6}
\]

The clocks tend to infinity, so the minima exist.  Endpoint conventions
affect only a null set in every integral below.

## 1. The physical inverse is subadditive on the half-line

### Theorem 1.1 (half-line inverse theorem)

The function \(B\) is nondecreasing, both \(B,u\) are measurable, and

\[
 \boxed{
 B(s+t)\le B(s)+B(t),
 \qquad u(s+t)\le u(s)+u(t)
 }
 \quad(s,t\ge0).                                    \tag{1.1}
\]

Moreover

\[
                         B(t)\ge t,\qquad u(t)\ge0.  \tag{1.2}
\]

The same statements hold for \(\bar B,\bar u\), and (0.3) implies

\[
                         u(t)\ge\bar u(t).           \tag{1.3}
\]

#### Proof

Monotonicity and measurability follow from the definition.  Since

\[
 A_{B(s)+B(t)}\ge A_{B(s)}+A_{B(t)}\ge s+t,
\]

minimality of \(B(s+t)\) gives the first inequality in (1.1).  Subtract
\(s+t\) to get the second.  If an integer \(n<t\), then
\(A_n\le n<t\); hence it cannot reach level \(t\).  This proves (1.2).
Finally, \(A\le\bar A\) makes every formal hitting time no later than the
corresponding physical hitting time, proving (1.3). \(\square\)

Thus the connected-sumset mechanism survives physical availability on
the half-line.  What is lost is degree-one periodicity at the finite head.

## 2. Exact tail translation and the inverse shoulder

Choose a multiple \(N\) of \(g\) with \(N\ge C\).  Then for every
\(t\ge0\),

\[
 \boxed{
 B(t+N)=N+\bar B(t),
 \qquad u(t+N)=\bar u(t).}                         \tag{2.1}
\]

#### Proof

For \(m\ge0\), (0.3)--(0.4) give

\[
 A_{N+m}=\bar A_{N+m}=N+\bar A_m.
\]

Thus \(N+\bar B(t)\) reaches level \(N+t\).  No index \(n<N\) can
reach it, because \(A_n\le n<N\le N+t\).  Among indices at least \(N\),
minimality is exactly the formal inverse problem after subtracting \(N\).
This proves (2.1). \(\square\)

Put

\[
                  \eta(t)=u(t)-\bar u(t)\ge0.       \tag{2.2}
\]

Then \(\eta\) has bounded support.  It is the inverse-coordinate form of
the finite availability shoulder.  More precisely, the standard area
identity for two ordered graphs gives

\[
 \boxed{
 \int_0^\infty\eta(t)\,dt
   =\sum_{n\ge0}(\bar A_n-A_n)
   ={1\over\lambda}\sum_{n\ge0}(U_n-V_n).}         \tag{2.3}
\]

#### Proof

Away from clock atoms,

\[
 B(t)=\#\{n:A_n<t\},
 \qquad
 \bar B(t)=\#\{n:\bar A_n<t\}.
\]

Since \(A_n\le\bar A_n\), their difference is the sum over \(n\) of
the indicator of the interval between \(A_n\) and \(\bar A_n\).
Only finitely many such intervals are nonempty.  Tonelli's theorem gives
(2.3). \(\square\)

## 3. Periodic padding fails exactly at the shoulder interface

Periodize the physical inverse head of length \(N\):

\[
                         u_N(x)=u(x\bmod N).         \tag{3.1}
\]

If \(0\le x,y<N\) and \(x+y<N\), Theorem 1.1 gives

\[
                         u_N(x+y)\le u_N(x)+u_N(y). \tag{3.2}
\]

If \(x+y=N+z\), \(0\le z<N\), then (1.1), (2.1), and (2.2) give

\[
 \boxed{
 u_N(z)
 \le u_N(x)+u_N(y)+\eta(z).}                      \tag{3.3}
\]

Indeed,

\[
 \bar u(z)=u(N+z)=u(x+y)\le u(x)+u(y),
\]

and \(u(z)=\bar u(z)+\eta(z)\).  Thus every nonwrapped sum is honestly
subadditive, while the only missing term at a wrapped output is its inverse
availability shoulder.  The bound need not be an equality for every
representation; Section 7 gives a Bellman family where it is attained at
every defective output.

There is an equivalent index formulation.  Put

\[
 e_n=n-A_n,
 \qquad d_n=n-\bar A_n,
 \qquad \delta_n=e_n-d_n\ge0.                     \tag{3.4}
\]

For \(r+s=N+z\), ordinary half-line subadditivity of \(e\) and formal
periodicity give

\[
 \boxed{
 e_z\le e_r+e_s+\delta_z.}                        \tag{3.5}
\]

This is the exact algebraic location of the failed cyclic inequality.

## 4. Connected-sumset inequalities that remain valid

For \(q\ge0\), define the inverse block

\[
 u_q(x)=u(qg+x),\qquad 0\le x<g,                   \tag{4.1}
\]

and its sublevel set and distribution

\[
 C_q(a)=\{x\in[0,g):u_q(x)\le a\},
 \qquad F_q(a)=|C_q(a)|.                           \tag{4.2}
\]

### Theorem 4.1 (two-block connected-sumset inequality)

Whenever the two sublevel sets have positive measure,

\[
 \boxed{
 F_q(a)+F_r(b)
 \le F_{q+r}(a+b)+F_{q+r+1}(a+b).}                \tag{4.3}
\]

More generally, for \(p\) positive-measure sublevel sets,

\[
 \boxed{
 \sum_{i=1}^pF_{q_i}(a_i)
 \le
 \sum_{j=0}^{p-1}F_{Q+j}(a_1+\cdots+a_p),
 \qquad Q=\sum_iq_i.}                             \tag{4.4}
\]

#### Proof

For \(x\in C_q(a)\) and \(y\in C_r(b)\), half-line subadditivity says

\[
 u((q+r)g+x+y)\le a+b.
\]

If \(x+y<g\), the output phase belongs to \(C_{q+r}(a+b)\); if
\(x+y\ge g\), its translate by \(-g\) belongs to
\(C_{q+r+1}(a+b)\).  Hence the ordinary real sumset
\(C_q(a)+C_r(b)\subset[0,2g)\) lies in the two displayed output strips.
The one-dimensional Brunn--Minkowski inequality gives

\[
 |C_q(a)+C_r(b)|\ge F_q(a)+F_r(b),
\]

which proves (4.3).  Iterating the same argument proves (4.4). \(\square\)

Once one input and all possible outputs are in the formal tail, addition
may instead be taken on the connected circle.  Write \(F_\infty\) for
the formal one-period distribution.  Then

\[
 \boxed{
 F_\infty(a+b)
 \ge\min\{g,F_q(a)+F_\infty(b)\}.}                \tag{4.5}
\]

Equivalently, for increasing generalized quantiles and \(x+y\le1\),

\[
 \boxed{
 Q_\infty(x+y)\le Q_q(x)+Q_\infty(y).}           \tag{4.6}
\]

The proof is the same, after translating the formal input by sufficiently
many periods and reducing the output modulo \(g\); connected-circle Kneser
then gives (4.5).

### Exact limitation of the mixed inequality

Because \(u_q\ge u_\infty\) on every preconductor block, one has

\[
 C_q(a)\subseteq C_\infty(a),
 \qquad Q_q(x)\ge Q_\infty(x).                    \tag{4.7}
\]

Consequently (4.5)--(4.6) are already implied by the formal circle
inequality

\[
 Q_\infty(x+y)\le Q_\infty(x)+Q_\infty(y).
\]

They are exact structural identities, but they are one-sided and do not
upper-bound the raised physical quantiles.  The genuinely new finite
information is (4.3)--(4.4), which couples consecutive physical blocks;
even it supplies no reverse inequality by itself.

## 5. Exact finite inverse moments

Suppose \(A_N=N\), and put \(e_n=n-A_n\) for \(0\le n\le N\).  Then
\(e_0=e_N=0\).  On every nonempty inverse cell

\[
                         A_n<t<A_{n+1},
\]

one has \(B(t)=n+1\), hence

\[
                         u(t)=n+1-t.               \tag{5.1}
\]

Telescoping the cell integrals gives

\[
 \boxed{
 {1\over N}\int_0^N u(t)\,dt
   ={1\over2}+{1\over N}\sum_{n=0}^{N-1}e_n,}     \tag{5.2}
\]

\[
 \boxed{
 {1\over N}\int_0^N u(t)^2\,dt
   ={1\over3}+{1\over N}\sum_{n=0}^{N-1}(e_n+e_n^2),} \tag{5.3}
\]

and therefore

\[
 \boxed{
 \operatorname {Var}_{[0,N]}(u)
   ={1\over12}+\operatorname {Var}_{0\le n<N}(e_n).} \tag{5.4}
\]

These are the exact finite-prefix analogues of the formal phase moment
identities.  They require no cyclic subadditivity.  The next section shows
that the cyclic variance bound itself does not survive.

## 6. A sharp finite-prefix sublevel inequality

The defect sequence \(e_n=n-A_n\) is subadditive on \(\mathbb N\).  Put

\[
 S_M(a)=\{0\le n\le M:e_n\le a\},
 \qquad G_M(a)=|S_M(a)|.                            \tag{6.1}
\]

Then

\[
 S_M(a)+S_L(b)\subseteq S_{M+L}(a+b).
\]

The torsion-free sumset inequality on the integers yields

\[
 \boxed{
 G_{M+L}(a+b)
 \ge G_M(a)+G_L(b)-1.}                             \tag{6.2}
\]

Equivalently, if \(e^{(M)}_1\le\cdots\le e^{(M)}_{M+1}\) are the
ordered prefix defects, then

\[
 \boxed{
 e^{(M+L)}_{i+j-1}
 \le e^{(M)}_i+e^{(L)}_j.}                         \tag{6.3}
\]

This is the natural finite-prefix quantile theorem.  Its horizon expands
from \((M,L)\) to \(M+L\); identifying the output back with one input
horizon is exactly the wrap step, and Section 3 shows that this costs the
availability shoulder.

## 7. Sharp Bellman no-go to an unsigned finite-circle variance proof

Fix integers

\[
                         2\le M,qquad N\ge2M,       \tag{7.1}
\]

and put \(\lambda=\zeta/N\).  Define a finite saturated table by

\[
 c_j=
 \begin{cases}
 0,&1\le j<M,\\
 \lambda j,&M\le j\le N.
 \end{cases}                                       \tag{7.2}
\]

### Theorem 7.1 (triangular availability shoulder)

The table (7.2) is nonnegative, nondecreasing, internally superadditive,
has its first \(\zeta\)-crossing at \(N\), and is already saturated there.
Its maximum density is \(\lambda\), its critical gcd is one, and hence its
formal clock is

\[
                         U_n=\lambda n.             \tag{7.3}
\]

Its physical Bellman clock is

\[
 V_n=
 \begin{cases}
 0,&0\le n<M,\\
 \lambda n,&n\ge M.
 \end{cases}                                       \tag{7.4}
\]

Consequently the normalized complete defects are

\[
 e_n=
 \begin{cases}
 n,&0\le n<M,\\
 0,&n\ge M.
 \end{cases}                                       \tag{7.5}
\]

#### Proof

Monotonicity is clear.  If \(i+j<M\), all three relevant values are zero.
If \(i+j\ge M\), then

\[
 c_{i+j}=\lambda(i+j)\ge c_i+c_j,
\]

because either input below \(M\) contributes zero and every input at least
\(M\) contributes its linear value.  Thus the table is internally
superadditive.  Every proper displayed value is below
\(\lambda N=\zeta\), while \(c_N=\zeta\).  Since

\[
 N=M+(N-M),qquad M,N-M\ge M,
\]

this proper partition already has value \(\lambda N=\zeta\); hence the
endpoint is saturated.

All indices \(M,M+1,\ldots,N\) are critical, so their gcd is one and the
formal clock is (7.3).  The physical clock is zero below \(M\).  Every
capacity in \([M,N]\) is an available critical denomination.  For a
capacity larger than \(N\), repeatedly subtract \(M\) until the remainder
lies in \([M,N]\); this is possible because \(N\ge2M\).  Thus every
capacity at least \(M\) is a sum of critical denominations and has value
\(\lambda n\).  This proves (7.4)--(7.5). \(\square\)

For the prefix of length \(N\), put

\[
 \mu_N={1\over N}\sum_{n=0}^{N-1}e_n
       ={M(M-1)\over2N}.                            \tag{7.6}
\]

A direct symbolic simplification gives

\[
 \operatorname {Var}_N(e)
 \le {\mu_N(\mu_N+1)\over3}
 \quad\Longleftrightarrow\quad N\le M.             \tag{7.7}
\]

Indeed, writing

\[
 S_1={M(M-1)\over2},
 \qquad S_2={M(M-1)(2M-1)\over6},
\]

the proposed inequality is equivalent to

\[
 N(S_2-S_1/3)\le{4S_1^2\over3},
\]

which reduces to \(N\le M\).  Since (7.1) has \(N\ge2M\), the finite
cyclic variance inequality fails sharply.

The periodic wrap defect is also attained exactly.  For
\(1\le z<M\), choose

\[
                         r=M,qquad s=N-M+z.
\]

Then \(r,s\in[M,N)\), so \(e_r=e_s=0\), while

\[
                         e_{r+s-N}=e_z=z.            \tag{7.8}
\]

Thus the failed wrapped subadditivity is precisely the physical shoulder,
not a proof artifact.

Finally, every shoulder term in this family is favorable for the Rayleigh
functional:

\[
 \Phi(V)-\Phi(U)
 =\sum_{m=1}^{M-1}\bigl(K(0)-K(\lambda m)\bigr)>0.  \tag{7.9}
\]

Indeed

\[
 0<\lambda m<\lambda M\le\zeta/2<\zeta,
\]

and \(K\) is strictly decreasing on \([0,\zeta]\).  Hence the physical
point moved to zero has larger kernel value than its formal point.

This proves the sharp methodological boundary:

> An unsigned finite-prefix variance extension is false even on the exact
> saturated Bellman class, and its failure may consist entirely of
> favorable sub-minimum shoulder mass.  Any valid shoulder theorem must
> retain the location of the inverse defect relative to \(\zeta\), or an
> equivalent signed layer-cake quantity.

## 8. Exact surviving target

The inverse-circle theorem closes the periodic tail.  The present theorem
closes the generalized-inverse and connected-sumset bookkeeping for the
physical head, and rules out the direct finite-variance shortcut.  The
remaining analytic statement is now explicitly two-sided and signed:

> **Signed shoulder transport target.**  Bound the part of
> \(\eta=u-\bar u\) (equivalently of the index deficits \(\delta_n\))
> lying above the Rayleigh minimum by the favorable sub-minimum part plus
> the strict formal Fourier reserve, using the expanding-horizon inequalities
> (4.3)--(4.4) or (6.2), together with the exact Bellman slack recursion.

Neither the mixed circle inequality nor unsigned shoulder area can prove
this: (4.7) makes the former weaker than the already-known formal theorem,
and Theorem 7.1 makes the latter arbitrarily large while remaining wholly
favorable.

This note proves no all-price positivity claim and no OR-word upper bound.

## 9. Dependencies

1. `MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`;
3. `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md`;
4. the one-dimensional Brunn--Minkowski inequality and its integer
   torsion-free analogue.
