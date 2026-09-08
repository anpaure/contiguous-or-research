# Cyclic-interval nibble: local Johnson mass is harmless, but parity holonomy is a statewise trap

Date: 2026-07-26

## 0. Outcome

Put

\[
 v=2m,\qquad r=m-a\sqrt m+O(1),\qquad s=v-r,
\]

with fixed \(a>0\), and let \(\mathcal H_r\) be the \(v\)-uniform
hypergraph on \(\binom{[v]}r\) whose edges are the \(v\) cyclic
\(r\)-intervals of an unoriented cyclic order.  Write

\[
 D={r!s!\over2}
\]

for its degree and \(d(X,Y)\) for a pair codegree.

This note gives both the positive and negative conclusions of a direct
growing-uniformity nibble audit.

1.  The large distance-one codegree is benign in its correct local norm.
    For every packet \(e\),

    \[
      {1\over D}\sum_{\{X,Y\}\subset e}d(X,Y)
        ={4+o(1)\over m}.                                      \tag{0.1}
    \]

    Moreover one marked packet changes the link degree of any target not
    in that packet by at most \((4+o(1))D/m\).  A fresh nibble bite
    therefore has Bernstein fluctuations on relative scale \(m^{-1/2}\),
    not constant scale.  Thus the two Johnson neighbours per packet do
    **not** obstruct a first bite, and a maximum-codegree black box loses
    the decisive geometry.

2.  Arbitrary residual regeneration nevertheless fails, even after one
    records the exact coordinate balance automatically preserved by every
    packet matching.  For every \(r\), there is a set

    \[
      U\subseteq\binom{[2m]}r,
      \qquad |U|\ge\left({1\over3}-e^{-\Theta(m)}\right)\binom{2m}r,
                                                                  \tag{0.2}
    \]

    which is an exact \(1\)-design on the ground coordinates but for which

    \[
                         \mathcal H_r[U]=\varnothing.             \tag{0.3}
    \]

    For even \(r\), the obstruction is parity of intersection with a
    fixed balanced half of the ground set and has density \(1/2-o(1)\).
    For odd \(r\), the same construction works modulo three and has
    density \(1/3+o(1)\).  It is a global finite-character holonomy of
    the cyclic window sequence, invisible to density, one-coordinate
    marginals, and the time-zero all-\(j\) codegree envelope.

Consequently the specialized random-greedy route remains possible, but
its missing theorem is now sharper: one must prove that the *particular*
random-greedy trajectory stays character-uniform (or otherwise excludes
all window-holonomy traps).  A hereditary theorem for every dense,
coordinate-balanced residual is false.

## 1. Exact packet-local pair mass

For distinct \(X,Y\), put

\[
 t=|X\setminus Y|=|Y\setminus X|.
\]

The exact codegrees are

\[
 {d(X,Y)\over D}
 =p_t:={2\over\binom rt\binom st}\quad(1\le t<r),
 \qquad
 p_r={v-2r+1\over\binom sr}.                                \tag{1.1}
\]

Fix a packet \(e\).  Relative to any \(X\in e\), there are exactly two
members of \(e\) at Johnson distance \(t\), for \(1\le t<r\), and
exactly \(v-2r+1\) disjoint members.  Hence

\[
 \begin{aligned}
 \Lambda(e)
 &:= {1\over D}\sum_{\{X,Y\}\subset e}d(X,Y)\\
 &=2v\sum_{t=1}^{r-1}{1\over\binom rt\binom st}
   +{v(v-2r+1)^2\over2\binom sr}.                           \tag{1.2}
 \end{aligned}
\]

The \(t=1\) term is \(2v/(rs)=(4+o(1))/m\).  More explicitly,
the earlier quantity

\[
 \sigma(e)={1\over vD}\sum_{\{X,Y\}\subset e}d(X,Y)
\]

equals

\[
 2\sum_{t=1}^{r-1}{1\over\binom rt\binom st}
 +{(v-2r+1)^2\over2\binom sr}.
\]

Thus

\[
 \boxed{
 {1\over D}\sum_{\{X,Y\}\subset e}d(X,Y)
 =v\sigma(e)={4+o(1)\over m}.}                              \tag{1.3}
\]

Indeed each distance \(1\le t<r\) occurs in exactly \(v\) unordered
packet pairs.  All \(t\ge2\) terms total \(O(m^{-3})\), and the
disjoint term is \(\exp[-\Theta(\sqrt m\log m)]\).

Equation (1.3) is the relevant replacement for
\(\binom v2\Delta_2/D=\Theta(1)\): the actual packet contains only
\(v\) distance-one pairs, not \(\Theta(v^2)\) extremal pairs.

## 2. Bounded influence in one nibble bite

Mark every packet independently with probability

\[
                         p={\gamma\over vD},\qquad 0<\gamma\le1.
                                                                  \tag{2.1}
\]

Fix a target \(X\).  For a packet \(g\not\ni X\), let

\[
 a_X(g)=|\{f\ni X:(f\setminus\{X\})\cap g\ne\varnothing\}|.
                                                                  \tag{2.2}
\]

The union bound and the exact maximum pair codegree give

\[
 a_X(g)\le\sum_{Y\in g}d(X,Y)
           \le v\Delta_2
           =\left({4+o(1)\over m}\right)D=:B.               \tag{2.3}
\]

There is also the exact first-moment ledger

\[
 \sum_g a_X(g)
 \le\sum_g\sum_{Y\in g}d(X,Y)
 =D\sum_{Y\ne X}d(X,Y)
 =D^2(v-1).                                                  \tag{2.4}
\]

Let \(\xi_g\) be the marking indicators and put

\[
                         Z_X=\sum_{g\not\ni X}a_X(g)\xi_g.
                                                                  \tag{2.5}
\]

This overcounts the number of packets in the link of \(X\) destroyed by
marked packets not containing \(X\).  From (2.3)--(2.4),

\[
 \operatorname {Var}Z_X
 \le p\sum_ga_X(g)^2
 \le pB\sum_ga_X(g)
 \le\left({4\gamma+o(1)\over m}\right)D^2.                 \tag{2.6}
\]

Bernstein's inequality therefore yields, uniformly for \(0<\eta\le1\),

\[
 \boxed{
 \Pr\bigl(|Z_X-\mathbb EZ_X|>\eta D\bigr)
 \le2\exp\left[-c,{m\eta^2\over\gamma+\eta}\right]}     \tag{2.7}
\]

for an absolute \(c>0\) and all sufficiently large \(m\).

This proves a genuine growing-rank one-bite concentration statement.
It also pinpoints the remaining difficulty: (2.7) does not, by itself,
show that the nonlinear residual after \(\Theta(v\log(1/\rho))\) bites
avoids global structured traps.

### 2.1 Finite-character balance is cheap in one raw bite

The traps below are not evidence that a random trajectory is likely to
enter one.  In fact all finite-character counts can be controlled
simultaneously in one raw marking round.

Let \(f:\binom{[v]}r\to[-1,1]\), and define

\[
 Y_f=\sum_e\xi_e\sum_{X\in e}f(X).                          \tag{2.8}
\]

Regularity gives

\[
 \mathbb EY_f=pD\sum_Xf(X),
 \qquad
 \operatorname {Var}Y_f
 \le p\sum_e v\sum_{X\in e}f(X)^2
 \le\gamma\binom vr.                                       \tag{2.9}
\]

Since one summand in (2.8) has absolute value at most \(v\), Bernstein
gives

\[
 \Pr(|Y_f-\mathbb EY_f|>t)
 \le2\exp\left[-{t^2\over
        2\gamma\binom vr+(2/3)vt}\right].                  \tag{2.10}
\]

Consequently (2.10) holds simultaneously, with error \(o(\binom vr)\),
for every member of any test family of size \(\exp(O(v))\).  This
includes every balanced-half parity or fixed-modulus residue test below.
Deleting colliding marked packets changes any such count by at most
\(v\) times the number of rejected marks; the latter is an
\(O(\gamma)\) fraction of all marks in expectation.  Thus taking
\(\gamma=o(1)\) also makes the isolation correction negligible for one
bite.

The obstruction below therefore says that finite-character control is a
*necessary trajectory invariant*, not that this particular invariant is
hard to maintain.  Availability of complete packets is a higher-order
condition still missing from the iteration.

### 2.2 Product residuals do regenerate: an exact common-prefix moment

There is a stronger positive statement.  Let \(U_z\) retain every target
independently with probability \(z\), and condition on a fixed target
\(X\) being retained.  Write

\[
 d_z(X)=|\{e\ni X:e\setminus\{X\}\subseteq U_z\}|,
 \qquad \mu_z=Dz^{v-1}.                                    \tag{2.11}
\]

For every fixed \(a>0\), uniformly when
\(r=m-a\sqrt m+O(1)\) and \(z\ge1/\log m\),

\[
 \boxed{
 {\operatorname {Var}d_z(X)\over\mu_z^2}
 =O\left({(\log m)^5\over m^2}\right)+o(1).}               \tag{2.12}
\]

In particular, with
\(\varepsilon_m=(\log m)^3/m=o(1)\), all but \(o(\binom vr)\)
retained targets have available degree
\((1\pm\varepsilon_m)\mu_z\), with probability \(1-o(1)\).

#### The common-prefix renewal

Anchor and orient a packet through \(X\).  It is represented by an
ordering of the \(r\) elements of \(X\) and an independent ordering of
the \(s\) exterior elements.  Relative to one fixed packet, a second
uniform packet through \(X\) is therefore represented by independent
uniform permutations of these two ordered blocks.

For one fixed choice of left/right endpoint on each packet, let \(K_0\)
be the number of nontrivial endpoint depths at which both the removed
prefix set in \(X\) and the inserted prefix set in its complement agree.
For \(R\le S\), put

\[
 F_{R,S}(u)=\mathbb E u^{K_0}.                              \tag{2.13}
\]

Expanding \(u^{K_0}=\prod_t[1+(u-1){\bf1}_{\{t\text{ is a
common cut}\}}]\) and conditioning on the first common cut gives the
exact renewal

\[
 F_{R,S}(u)=1+(u-1)\sum_{d=1}^{R-1}
 {F_{R-d,S-d}(u)\over\binom Rd\binom Sd}.                  \tag{2.14}
\]

Indeed, prescribed common cuts
\(0<t_1<\cdots<t_k<R\) occur with probability

\[
 {\prod_{i=1}^k(t_i-t_{i-1})!^2\,(R-t_k)!(S-t_k)!
       \over R!S!},\qquad t_0=0,                            \tag{2.15}
\]

which is exactly the iterated kernel in (2.14).

The elementary kernel bound

\[
 \sum_{d=1}^{R-1}{1\over\binom Rd\binom Sd}
 \le {3\over RS}                                           \tag{2.16}
\]

follows by separating \(d=1,R-1\); for
\(2\le d\le R-2\), use
\(\binom Rd\ge\binom R2\) and
\(\binom Sd\ge\binom S2\).  In the present application
\(S-R=s-r=\Theta(\sqrt m)\).  Hence, uniformly over every tail state
\((R,S)=(R,R+s-r)\) with \(R\ge2\),

\[
 (u-1){3\over RS}=o(1)                                     \tag{2.17}
\]

whenever \(u\le(\log m)^5\).  Induction in (2.14) first gives
\(F_{R,S}(u)\le2\), and then

\[
                         F_{r,s}(u)=1+O\left({u\over m^2}\right).
                                                                  \tag{2.18}
\]

#### The four endpoints and disjoint windows

Let \(K(e,f)=|(e\cap f)\setminus\{X\}|\).  Every common non-disjoint
target belongs to one of four left/right endpoint comparisons.  H\"older's
inequality and (2.18), with \(u=z^{-1}\), give

\[
 \mathbb E u^{K_{\rm nondis}(e,f)}
 \le\prod_{i=1}^4(\mathbb E u^{4K_i})^{1/4}
 =1+O\left({u^4\over m^2}\right).                          \tag{2.19}
\]

For a uniform second packet through \(X\), the expected number of common
disjoint targets is

\[
 { (v-2r+1)^2\over\binom sr}.                               \tag{2.20}
\]

There are at most \(v-2r+1=O(\sqrt m)\) such targets.  Thus, even after
using H\"older with exponent five,

\[
 \mathbb E u^{5K_{\rm dis}(e,f)}
 \le1+u^{5(v-2r+1)}{(v-2r+1)^2\over\binom sr}
 =1+e^{-\Theta(\sqrt m\log m)}.                            \tag{2.21}
\]

Combining the four endpoint terms and the disjoint term with exponent
five yields

\[
 \boxed{\mathbb E u^{K(e,f)}
       =1+O\left({u^5\over m^2}\right)}                    \tag{2.22}
\]

for \(1\le u\le\log m\).

Finally, conditional on \(X\in U_z\), two packets \(e,f\ni X\) survive
together with probability

\[
 z^{2(v-1)-K(e,f)}.
\]

The diagonal contribution to the normalized second moment is
\(1/\mu_z=o(1)\), since

\[
 \log\mu_z
 =\log D-(v-1)\log\log m
 =(2+o(1))m(\log m-\log\log m-1)\to\infty.                 \tag{2.23}
\]

Equation (2.22) now proves (2.12).  Chebyshev and averaging over \(X\)
give the last assertion.

This closes **degree regeneration in \(L^1\)** for a product residual at
the density needed for an \(o(N)\) leave.  It does not extract a spanning
regular core after the exceptional targets are removed, and it does not
construct a matching.  What remains unproved is that the dependent
residual created by repeated isolated bites has the same common-prefix
moment (and that its small exceptional set can be quarantined without
destroying the regenerated degrees).

## 3. A balanced parity-holonomy trap

Fix a balanced bipartition

\[
                         [2m]=A\sqcup B,\qquad |A|=|B|=m.
                                                                  \tag{3.1}
\]

For \(\varepsilon\in\{0,1\}\), define

\[
 U_\varepsilon(A)=
 \{S\in\tbinom{[2m]}r:|S\cap A|\equiv\varepsilon\pmod2\}.
                                                                  \tag{3.2}
\]

### Theorem 3.1 (window-parity classification)

If all cyclic \(r\)-intervals of an order \(\pi\) lie in one
\(U_\varepsilon(A)\), then \(r\) is even and

\[
                         \varepsilon\equiv r/2\pmod2.       \tag{3.3}
\]

Conversely, for even \(r\), orders attaining (3.3) exist.  Therefore

\[
             \boxed{\mathcal H_r[U_{1-r/2\pmod2}(A)]=\varnothing}
                                                                  \tag{3.4}
\]

for every even \(r\).  For odd \(r\), neither parity class contains an
entire packet.

#### Proof

Write

\[
 a_i={\bf1}_{\{\pi_i\in A\}},\qquad
 y_j=\sum_{h=0}^{r-1}a_{j+h}\pmod2 .                        \tag{3.5}
\]

If every packet target has parity \(\varepsilon\), then \(y_j\) is
constant.  Taking consecutive differences in (3.5) gives

\[
                         a_{j+r}=a_j\quad(j\in\mathbb Z_{2m}).
                                                                  \tag{3.6}
\]

Put \(g=\gcd(2m,r)\).  The shift by \(r\) has \(g\) orbits, each of
length \(2m/g\).  Equation (3.6) says that the positions occupied by
\(A\) are a union of whole shift-orbits.  Since there are \(m\) such
positions, the number of chosen orbits is \(g/2\).  Thus \(g\), and
hence \(r\), must be even.

The shift-orbits are the residue classes modulo \(g\).  Every interval
of length \(r\) contains \(r/g\) representatives of each residue class,
so it contains

\[
                         {r\over g}{g\over2}={r\over2}       \tag{3.7}
\]

members of \(A\).  This proves the necessity of (3.3).  Conversely,
place the labels of \(A\) in any \(g/2\) shift-orbits and the labels of
\(B\) in the others; then (3.7) holds for every window.  \(\square\)

### Theorem 3.2 (density and exact coordinate balance)

For even \(r=m+O(\sqrt m)\), the forbidden class

\[
                         U=U_{1-r/2\pmod2}(A)               \tag{3.8}
\]

satisfies

\[
 |U|={1\over2}\left[\binom{2m}r-\binom m{r/2}\right]
    =\left({1\over2}-e^{-\Theta(m)}\right)\binom{2m}r,      \tag{3.9}
\]

and every ground coordinate belongs to exactly \(r|U|/(2m)\) members of
\(U\).

#### Proof

The signed parity enumerator is

\[
 \sum_{S\in\binom{[2m]}r}(-1)^{|S\cap A|}
 =[z^r](1-z)^m(1+z)^m
 =(-1)^{r/2}\binom m{r/2}.                                  \tag{3.10}
\]

This gives the first equality in (3.9); Stirling gives the second.
Finally

\[
                         (S_A\times S_B)\rtimes C_2          \tag{3.11}
\]

acts transitively on the \(2m\) ground coordinates.  Because \(r\) is
even, swapping \(A\) and \(B\) preserves the parity in (3.2).  Hence
the action preserves \(U\), so its coordinate degrees are equal.  Their
common value follows by double counting incidences.  \(\square\)

### Theorem 3.3 (odd ranks: a mod-three balanced trap)

Suppose \(r\) is odd.  Let \(c\in\mathbb Z_3\) be the unique residue
satisfying

\[
                             2c\equiv r\pmod3,              \tag{3.12}
\]

and put

\[
 U_c^{(3)}(A)=
 \{S\in\tbinom{[2m]}r:|S\cap A|\equiv c\pmod3\}.           \tag{3.13}
\]

Then

\[
 \boxed{\mathcal H_r[U_c^{(3)}(A)]=\varnothing,\qquad
 |U_c^{(3)}(A)|=\left({1\over3}+e^{-\Theta(m)}O(1)\right)
                         \binom{2m}r,}                       \tag{3.14}
\]

and \(U_c^{(3)}(A)\) is an exact ground-coordinate \(1\)-design.

#### Proof

If all \(r\)-window intersection counts are congruent to \(c\) modulo
three, consecutive differences again give

\[
                         a_{j+r}\equiv a_j\pmod3.           \tag{3.15}
\]

Because \(a_j\in\{0,1\}\), congruence in (3.15) is equality.  Thus the
positions of \(A\) are a union of orbits of the shift by \(r\).  Here
\(g=\gcd(2m,r)\) is odd, so every orbit has length \(2m/g\), and exactly
\(g/2\) orbits would be required to obtain \(m\) positions.  This is
impossible.  Hence (3.13) contains no packet.

The hypergeometric random variable \(|S\cap A|\), for uniform
\(S\in\binom{[2m]}r\), is equidistributed modulo three up to
\(e^{-\Theta(m)}\).  This follows directly from the roots-of-unity
filter applied to

\[
                         (1+z)^m(1+\omega z)^m,
 \qquad \omega=e^{2\pi i/3},                                \tag{3.16}
\]

and the standard central coefficient bound, uniformly for
\(r=m+O(\sqrt m)\).  This proves the size assertion.

Finally, swapping \(A\) and \(B\) sends an intersection count \(j\) to
\(r-j\).  Equation (3.12) says that the residue class \(c\) is fixed by
this involution.  Thus the transitive group
\((S_A\times S_B)\rtimes C_2\) preserves (3.13), and all coordinate
degrees are equal.  \(\square\)

## 4. Consequence for a custom nibble theorem

Every cyclic packet is itself an exact ground-coordinate \(1\)-design:
each coordinate occurs in exactly \(r\) of its \(2m\) interval targets.
Thus the uncovered set after **any** packet matching is automatically
coordinate-balanced.  Theorem 3.2 shows that this deterministic invariant
does not imply regeneration, even at density one half.

Accordingly, none of the following data can be a sufficient hereditary
hypothesis:

* residual density bounded below;
* exact one-coordinate balance;
* the time-zero all-\(j\) codegree envelope;
* deterministic accounting of the two Johnson neighbours in each packet.

The fresh-bite estimates (1.3) and (2.7) leave one viable route: analyze
the actual random-greedy trajectory and prove that it remains far from
every parity-holonomy class (and from its higher-modulus analogues) until
the residual density is \(o(1)\).  That is a trajectory theorem, not an
arbitrary-residual regeneration theorem.

The present result does **not** obstruct an almost-perfect matching in
\(\mathcal H_r\).  It does identify a genuine statewise obstruction to
the proposed generic regeneration step, while proving that the visible
distance-one codegree is locally too dispersed to be the obstruction.
