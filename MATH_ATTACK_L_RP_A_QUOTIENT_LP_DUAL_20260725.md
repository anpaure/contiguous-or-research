# Lane L: the RP_A quotient packing LP and its Dyck-statistic duals

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computation is used.

## 0. Outcome

Put

\[
 N=2m+1,
 \qquad B=\operatorname{Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\to\infty\). After removing the negligible
short quotient cycles, the quotient short-return packing has the finite LP

\[
 \max\sum_Ix_I,
 \qquad
 \sum_{I\ni D}x_I\le1,
\]

and its dual is

\[
 \min\sum_Dy_D,
 \qquad
 \sum_{D\in I}y_D\ge1.
\]

The precise RP normalization is

\[
 \boxed{\sum_Dy_D=o_A(B/N).}
 \tag{0.1}
\]

Equivalently, the lifted physical dual has cost

\[
 N\sum_Dy_D+NZ_H=o_A(B).
 \tag{0.2}
\]

Thus an unlifted quotient dual of cost merely \(o_A(B)\) does **not** prove
RP_A.

The following statements are proved below.

1. The reciprocal-height weight

   \[
   y_{\rm ht}(D)=
   \frac{\mathbf1_{\{\operatorname{ht}(D)\le H-1\}}}
        {\operatorname{ht}(D)+2}
   \tag{0.3}
   \]

   is dual feasible and has exact fixed-window scale

   \[
   \sum_Dy_{\rm ht}(D)=\Theta_A(B/\sqrt m).
   \tag{0.4}
   \]

2. If \(d(D)\) is the positive odd suffix deficit, then

   \[
   y_{\rm wind}(D)=\frac{d(D)-1}{N-H+2}
   \tag{0.5}
   \]

   covers every positive-winding return. The exact integer floor \(d\ge1\)
   has been subtracted, and

   \[
   cB\sqrt m
   \le\sum_D(d(D)-1)
   \le CB\sqrt m\log ^2m.
   \tag{0.6}
   \]

3. Combining the centered suffix deficit with a terminal first-maximum
   charge gives an explicit dual for **all** short returns. For

   \[
   T_m=\frac{m}{\log ^8m},
   \tag{0.7}
   \]

   define

   \[
   y_T(D)=
   \frac{d(D)-1}{T_m}
   +\mathbf1_{\{\delta(D)\le H-1+T_m\}}.
   \tag{0.8}
   \]

   Then

   \[
   \sum_Dy_T(D)
   =O_A\!\left(\frac{B\log ^{10}m}{\sqrt m}\right)
    +o(B/N)
   =o_A(B).
   \tag{0.9}
   \]

   This is a genuine quotient dual of sub-Catalan cost, but its physical
   lift is still much too expensive for (0.2).

4. Iterated simultaneous peak deletion gives a new exact return-chain
   invariant. If a root of height \(h\) starts a return of gap
   \(2s+1<N\), and

   \[
   \partial^{h-1}D=(10)^p,
   \]

   then

   \[
   \boxed{h+p\le s+1.}
   \tag{0.10}
   \]

   More precisely, there is an exact nonnegative slack identity (7.5)
   below.

5. There is an all-depth suffix--winding--chronology dual obtained from
   peak deletion. However, the retained integral floor \(d_j\ge1\) forces
   every height-homogeneous nonnegative additive synthesis of these
   certificates to cost

   \[
   \Omega_A(B/\sqrt m).
   \tag{0.11}
   \]

   The reciprocal-height dual is pointwise optimal in this entire positive
   ledger cone. Centering removes the floor, but a genuine mountain return
   has centered deficit exactly zero at every deletion level.

6. Within the one-potential architecture (6.2), the coboundary may be
   arbitrary but cannot remove the floor. Every dual in that displayed
   global suffix--coboundary--endpoint template has cost at least

   \[
   \frac{B-o(B/N)}{N-3},
   \tag{0.12}
   \]

   already of the forbidden \(B/N\) order.

Consequently RP_A is not proved. The exact surviving problem is a
chronology- and Pascal-slot-sensitive dual for centered, zero-winding
deletion towers. It must have quotient cost \(o_A(B/N)\). The marginal
height/suffix constructions, the one-potential template (6.2), and the
height-homogeneous nonnegative iterated-deletion cones (8.5) and (8.8) are
rigorously insufficient. No no-go is claimed for arbitrary localized or
phase-varying LP weights.

## 1. Exact quotient coordinates and the interval support

Let \(\mathcal D_m\) be the set of Dyck words of semilength \(m\). Thus

\[
 |\mathcal D_m|=B.
\]

If the first up-step attaining the maximum of \(D\) is displayed as

\[
 D=P1Q,
\]

put

\[
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q,0\,\overline P,
 \qquad
 \tau=\phi^2.
 \tag{1.1}
\]

Refine the first-maximum factorization uniquely to

\[
 D=P1R0S,
 \tag{1.2}
\]

where the displayed zero is the first subsequent return to height zero.
The suffix \(S\) is Dyck. If \(\sigma(D)\) is its semilength, define

\[
 d(D)=|S|+1=2\sigma(D)+1.
 \tag{1.3}
\]

The exact two-step PBBS skew product is

\[
 (u,D)\longmapsto (u-d(D)\pmod N,\tau D).
 \tag{1.4}
\]

Suppose the omitted physical coordinate at normalized root \(D\) next
returns after the odd gap

\[
 g=2s+1.
\]

Writing \(D_t=\tau^tD\), the complete return equation is

\[
 \boxed{
 \sum_{t=0}^{s-1}d(D_t)=\delta(D_s)+Na(D,s),
 \qquad a(D,s)\in\mathbb Z_{\ge0}.}
 \tag{1.5}
\]

The return is consecutive precisely when the analogous congruence fails at
every proper prefix.

There is a harmless but important indexing shift between a return root and
the projected transition which inserts its omitted coordinate. In this
report, \(e_D\) denotes that preceding insertion transition. With this edge
indexing, the full cut support of the return is

\[
 \boxed{
 Q(D,s)=\{e_D,e_{\tau D},\ldots,e_{\tau^{s+1}D}\}.}
 \tag{1.6}
\]

It contains exactly

\[
 |Q(D,s)|=s+2=\frac{g+3}{2}
 \tag{1.7}
\]

quotient transition edges. The deficit core in (1.5) consists only of
\(D_0,\ldots,D_{s-1}\); \(D_s\) is the terminal \(\delta\)-state, and
\(D_{s+1}\) is the second boundary edge.

If quotient edges are instead indexed by their projected source root, the
same support is

\[
 \{e_{\phi^{-1}D},e_{\phi^{-1}\tau D},\ldots,
   e_{\phi^{-1}\tau^{s+1}D}\}.
\]

Thus (1.6) is a fixed bijective reindexing, not a change in the physical
interval.

The residence cutoff \(s+1\le H\) is exactly

\[
 1\le s\le H-1.
 \tag{1.8}
\]

For \(m\ge2\), gap three is absent, but allowing the empty \(s=1\) class
does not affect any statement below.

## 2. The primal and dual LPs, with exact normalization

Delete every \(\tau\)-cycle of length at most \(H+1\). Let \(V_H\) be the
remaining quotient edge set, and let \(Z_H=B-|V_H|\). Every interval
(1.6) on \(V_H\) is then a proper, nonrepeating circular interval.

Let \(\mathcal R_H\) be the set of eligible consecutive-return pairs
\(\rho=(D,s)\), with \(D\in V_H\) and \(s\le H-1\). The exact integral
quotient packing number is

\[
 \overline\nu_H=
 \max\left\{
  \sum_{\rho\in\mathcal R_H}x_\rho:
  x_\rho\in\{0,1\},\quad
  \sum_{\rho:E\in Q(\rho)}x_\rho\le1
  \quad(E\in V_H)
 \right\}.
 \tag{2.1}
\]

Its fractional relaxation is

\[
 p_H^*=
 \max\left\{
  \sum_{\rho\in\mathcal R_H}x_\rho:
  x_\rho\ge0,\quad
  \sum_{\rho:E\in Q(\rho)}x_\rho\le1
  \quad(E\in V_H)
 \right\},
 \tag{2.2}
\]

with dual

\[
 d_H^*=
 \min\left\{
  \sum_{E\in V_H}y_E:
  y_E\ge0,\quad
  \sum_{E\in Q(\rho)}y_E\ge1
  \quad(\rho\in\mathcal R_H)
 \right\}.
 \tag{2.3}
\]

Finite LP duality gives

\[
 p_H^*=d_H^*.
 \tag{2.4}
\]

### Theorem 2.1 (factor-two integral equivalence)

\[
 \boxed{
 \overline\nu_H\le d_H^*\le2\overline\nu_H.}
 \tag{2.5}
\]

#### Proof

The first inequality is weak duality applied to an integral primal
solution. On one active quotient cycle, the circular-interval transversal
number is at most \(\nu_C+1\): cut one point lying in a short interval and
apply the exact line-interval packing--transversal theorem to the remaining
intervals. Since an active cycle has \(\nu_C\ge1\), this is at most
\(2\nu_C\). Summing over active cycles gives an integral transversal of
size at most \(2\overline\nu_H\). Its indicator is dual feasible, proving
the second inequality. \(\square\)

The voltage-itinerary bound gives

\[
 Z_H\le(2H+2)N^{2H+2}.
 \tag{2.6}
\]

For fixed \(A\),

\[
 \log(NZ_H)=O_A(\sqrt m\log m)=o(m),
\]

whereas

\[
 B\ge\frac{4^m}{(m+1)(2m+1)}.
\]

Consequently

\[
 NZ_H=o_A(B),
 \qquad
 Z_H=o_A(B/N).
 \tag{2.7}
\]

Every quotient interval has all \(N\) spatial lifts. Lifting a quotient
dual assigns weight \(y_E\) to every physical edge over \(E\), at total
cost \(N\sum_Ey_E\). Conversely, averaging a physical fractional dual
under cyclic ground rotation makes it constant on each \(N\)-edge fibre
without changing its cost or feasibility. Therefore the long-cycle
physical fractional optimum is exactly \(Nd_H^*\).

Assume from now on that

\[
 2H-1<N,
 \qquad H\log N=o(m).
\]

These conditions hold for fixed \(A\) and all sufficiently large \(m\).
Combining the preceding observation, (2.5), and the deck packing theorem
then gives

\[
 \boxed{
 \nu_H(P_m)=o_A(B)
 \iff
 \overline\nu_H=o_A(B/N)
 \iff
 d_H^*=o_A(B/N).}
 \tag{2.8}
\]

This proves the normalization asserted in (0.1)--(0.2).

## 3. The exact reciprocal-height dual

### Lemma 3.1 (height is a quotient-orbit invariant)

\[
 \operatorname{ht}(\phi D)=\operatorname{ht}(D).
 \tag{3.1}
\]

#### Proof

Let \(h=\operatorname{ht}(D)\), and write \(D=P1Q\) at the first step
reaching height \(h\). Along \(Q\), the old path descends from \(h\) to
zero without exceeding \(h\). Hence \(\overline Q\), read from zero, stays
nonnegative and ends at height \(h\). The following zero lowers the height
to \(h-1\). Every prefix of \(P\) had old height at most \(h-1\), so
\(\overline P\), read from height \(h-1\), stays nonnegative, never exceeds
\(h-1\), and ends at zero. Thus \(\phi D=\overline Q0\overline P\) has
height exactly \(h\). \(\square\)

In particular height is constant on every \(\tau\)-cycle. The height-gap
theorem and (1.7) give, for every eligible return,

\[
 h(D)\le s,
 \qquad
 |Q(D,s)|=s+2\ge h(D)+2.
 \tag{3.2}
\]

### Theorem 3.2 (reciprocal-height dual and its sharp scale)

Define

\[
 y_{\rm ht}(D)=
 \frac{\mathbf1_{\{h(D)\le H-1\}}}{h(D)+2}.
 \tag{3.3}
\]

Then \(y_{\rm ht}\) is feasible for (2.3), and there are constants
\(c_A>0\) and an absolute \(C<\infty\) such that, for all sufficiently
large \(m\),

\[
 \boxed{
 c_A\frac B{\sqrt m}
 \le
 \sum_{D\in V_H}y_{\rm ht}(D)
 \le
 C\frac B{\sqrt m}.}
 \tag{3.4}
\]

#### Proof

Feasibility follows immediately from (3.2), since every edge of a return
interval has the same height:

\[
 \sum_{E\in Q(D,s)}y_{\rm ht}(E)
 =\frac{s+2}{h(D)+2}\ge1.
\]

Let \(M_{m,h}\) denote the number of semilength-\(m\) Dyck paths of height
at most \(h\). The path-graph spectral formula is

\[
 M_{m,h}
 =\frac2{h+2}\sum_{j=1}^{h+1}
  \sin^2\frac{\pi j}{h+2}
  \left(2\cos\frac{\pi j}{h+2}\right)^{2m}.
 \tag{3.5}
\]

For \(2\le h\le\sqrt m\), pairing the two symmetric eigenvalues and using
the elementary sine and cosine bounds gives absolute constants \(c,C>0\)
with

\[
 M_{m,h}
 \le C\frac{4^m}{h^3}
       \exp\!\left(-c\frac m{h^2}\right).
 \tag{3.6}
\]

Group exact heights into dyadic intervals. For a dyadic endpoint
\(u\le\sqrt m\), the contribution of paths with height in \((u/2,u]\)
is at most

\[
 \frac{2M_{m,u}}u
 \le C\frac{4^m}{u^4}
       e^{-cm/u^2}.
\]

Since \(B\asymp4^m/m^{3/2}\), the ratio of this expression to
\(B/\sqrt m\) is \(O(x^4e^{-cx^2})\), where \(x=\sqrt m/u\). Its dyadic
sum is bounded. Heights at least \(\sqrt m\) contribute at most
\(B/\sqrt m\). This proves the upper bound.

For the lower bound, take

\[
 h_0=\left\lfloor\frac{A\sqrt m}{2}\right\rfloor.
\]

Retaining the two extremal terms in (3.5) yields

\[
 M_{m,h_0}
 \ge\frac4{h_0+2}\sin^2\frac\pi{h_0+2}
 \left(2\cos\frac\pi{h_0+2}\right)^{2m}
 \ge c_AB.
 \tag{3.7}
\]

Every one of these roots has dual weight at least \(1/(H+1)\). Removing
the \(Z_H=o(B/N)\) short-cycle roots changes the sum negligibly. This proves
the lower bound. \(\square\)

Thus height alone gives an honest \(o_A(B)\) quotient dual, but it is a
factor \(\Theta_A(\sqrt m)\) above (0.1).

## 4. Suffix deficit and positive winding

For \(d(D)=2\sigma(D)+1\), put

\[
 \mathscr D_m=\sum_{D\in\mathcal D_m}d(D).
 \tag{4.1}
\]

The raw positive-winding dual \(d(D)/(N+1)\) retains the unavoidable
baseline \(d\ge1\). The correct floor-retaining centered identity is

\[
 \sum_{t=0}^{s-1}(d(D_t)-1)
 =\delta(D_s)+Na-s.
 \tag{4.2}
\]

If \(a\ge1\) and \(s\le H-1\), its right side is at least

\[
 N+1-(H-1)=N-H+2.
\]

Hence (0.5) covers every positive-winding interval.

More generally, for every real \(c\ge0\) satisfying

\[
 \Lambda_{H,c}=N+1-c(H-1)>0,
\]

the thresholded suffix weight

\[
 \boxed{
 y_c^+(D)=\frac{(d(D)-c)_+}{\Lambda_{H,c}}}
 \tag{4.3}
\]

covers every positive-winding interval, because

\[
 \begin{aligned}
 \sum_{t<s}(d(D_t)-c)_+
 &\ge \sum_{t<s}d(D_t)-cs\\
 &=\delta(D_s)+Na-cs\\
 &\ge N+1-c(H-1).
 \end{aligned}
\]

Thus its exact quotient cost is bounded by

\[
 C_{H,c}=
 \frac{\sum_D(d(D)-c)_+}{N+1-c(H-1)}.
 \tag{4.4}
\]

### Theorem 4.1 (two-sided centered suffix mass)

There are absolute constants \(c,C>0\) such that

\[
 \boxed{
 cB\sqrt m
 \le \mathscr D_m-B
 =\sum_D(d(D)-1)
 \le CB\sqrt m\log ^2m.}
 \tag{4.5}
\]

#### Proof

Let \(b_{m,j}\) be the number of roots for which the suffix \(S\) in
(1.2) has semilength \(j\). Write \(D=A S\), so \(A\) has semilength
\(m-j\). Since \(S\) follows the first primitive component attaining the
global maximum,

\[
 \operatorname{ht}(S)\le\operatorname{ht}(A).
\]

Consequently

\[
 b_{m,j}
 \le\#\{(A,S)\in\mathcal D_{m-j}\times\mathcal D_j:
          \operatorname{ht}(S)\le\operatorname{ht}(A)\}.
 \tag{4.6}
\]

If \(j\le m/2\), the standard two-sided Catalan coefficient bounds give

\[
 \frac{\operatorname{Cat}_{m-j}\operatorname{Cat}_j}{B}
 \le\frac C{(j+1)^{3/2}}.
 \tag{4.7}
\]

Therefore

\[
 \sum_{j\le m/2}j b_{m,j}=O(B\sqrt m).
 \tag{4.8}
\]

Now let \(j>m/2\) and put \(\ell=m-j\). If

\[
 j/\ell\le C_0\log ^4m,
\]

then \(\ell\ge c m/\log ^4m\), and the symmetric form of (4.7) gives

\[
 \sum j b_{m,j}=O(B\sqrt m\log ^2m)
 \tag{4.9}
\]

over this range.

It remains to treat \(j/\ell>C_0\log ^4m\). Put

\[
 t=(j\ell)^{1/4}.
\]

For independent uniform Dyck paths \(A\in\mathcal D_\ell\) and
\(S\in\mathcal D_j\), reflection after the first hit of level \(t\),
together with the Catalan coefficient bounds, gives

\[
 \Pr(\operatorname{ht}(A)\ge t)
 \le \operatorname{poly}(m)
       \exp\!\left(-c\frac{t^2}{\ell}\right).
 \tag{4.10}
\]

The path spectrum gives

\[
 \Pr(\operatorname{ht}(S)\le t)
 \le \operatorname{poly}(m)
       \exp\!\left(-c\frac{j}{(t+2)^2}\right).
 \tag{4.11}
\]

Both exponents are \(\Omega(\sqrt{j/\ell})\). Choosing the absolute
constant \(C_0\) sufficiently large makes the probability that
\(\operatorname{ht}(S)\le\operatorname{ht}(A)\) at most \(m^{-10}\).
Finally,

\[
 \sum_{\ell=0}^m
 \operatorname{Cat}_\ell\operatorname{Cat}_{m-\ell}
 =\operatorname{Cat}_{m+1}
 =O(B).
\]

Thus this final range contributes \(o(B)\) even after multiplication by
\(j\le m\). Since

\[
 \mathscr D_m-B=2\sum_j j b_{m,j},
\]

(4.8)--(4.11) prove the upper bound.

For the lower bound, fix a sufficiently small absolute \(\kappa>0\) and
put \(L=\lfloor\kappa\sqrt m\rfloor\). For every integer

\[
 \lceil m/3\rceil\le j\le\lfloor m/2\rfloor,
 \qquad n=m-j-1,
\]

choose

\[
 E\in\mathcal D_n,
 \quad \operatorname{ht}(E)\ge L,
 \qquad
 S\in\mathcal D_j,
 \quad \operatorname{ht}(S)\le L-1,
\]

and form

\[
 D=1E0S.
 \tag{4.12}
\]

The first primitive component has height at least \(L+1\), whereas the
suffix has height at most \(L-1\). It is therefore the first component
attaining the global maximum, and

\[
 d(D)=2j+1\ge2m/3.
\]

The lower spectral term in (3.5) gives, uniformly for \(j\asymp m\),

\[
 \#\{S\in\mathcal D_j:\operatorname{ht}(S)\le L-1\}
 \ge c_\kappa\operatorname{Cat}_j.
\]

Conversely, (3.6) and a sufficiently small fixed \(\kappa\) give,
uniformly for \(n\asymp m\),

\[
 \#\{E\in\mathcal D_n:\operatorname{ht}(E)\ge L\}
 \ge\frac12\operatorname{Cat}_n.
\]

The construction (4.12) is injective, and different \(j\)'s have different
canonical suffix lengths. Stirling's Catalan bounds give

\[
 \operatorname{Cat}_n\operatorname{Cat}_j
 \ge c\frac B{m^{3/2}}
\]

throughout this range. Summing over \(\Theta(m)\) choices of \(j\) gives
at least \(cB/\sqrt m\) distinct roots, each contributing at least
\(2m/3-1\) to \(d(D)-1\). This proves the lower bound in (4.5). \(\square\)

Deleting the short-cycle roots changes \(\sum(d-1)\) by at most
\(NZ_H=o(B)\), since \(d(D)-1<N\). Thus the same two-sided orders hold on
\(V_H\).

Taking \(c=1\) in (4.3) now gives

\[
 c_A\frac B{\sqrt m}
 \le \sum_Dy_{\rm wind}(D)
 \le C_A\frac{B\log ^2m}{\sqrt m}
 =o_A(B).
 \tag{4.13}
\]

It covers positive winding only, and remains far above \(B/N\).

## 5. A full centered dual using the terminal first maximum

For \(1\le L\le m\), put

\[
 \Delta_{m,L}=\#\{D\in\mathcal D_m:\delta(D)\le L\}.
\]

### Lemma 5.1 (small first-maximum bound)

There are absolute constants \(c,C>0\) such that

\[
 \boxed{
 \Delta_{m,L}
 \le C(L+1)^3 4^m
       \exp\!\left[-c\sqrt{\frac m{L+1}}\right].}
 \tag{5.1}
\]

#### Proof

Suppose the first global maximum has height \(h\) and is reached at time
\(t\le L\). Ignoring positivity and first-attainment conditions, the number
of possible prefixes is at most

\[
 2^t\exp\!\left(-\frac{h^2}{2t}\right)
 \tag{5.2}
\]

by the binomial Chernoff bound. The remaining walk has length \(2m-t\),
starts at height \(h\), ends at zero, and is confined to
\(\{0,1,\ldots,h\}\). The path-graph spectral radius gives the upper bound

\[
 (h+1)2^{2m-t}
 \exp\!\left(-c_0\frac{2m-t}{(h+2)^2}\right).
 \tag{5.3}
\]

Since \(t\le L\le m\), the exponent in the product of (5.2)--(5.3) is at
least

\[
 c_1\left(\frac{h^2}{L}+\frac m{(h+2)^2}\right)
 \ge c_2\sqrt{\frac m{L+1}}.
\]

Summing over \(1\le h,t\le L\) proves (5.1). \(\square\)

### Theorem 5.2 (a sub-Catalan full dual)

Let \(T>0\) satisfy \(T\le N-H+2\), and define

\[
 y_T(D)=
 \frac{d(D)-1}{T}
 +\mathbf1_{\{\delta(D)\le H-1+T\}}.
 \tag{5.4}
\]

Then \(y_T\) covers every eligible short-return interval.

#### Proof

For positive winding, (4.2) is at least \(N-H+2\ge T\), so the first term
alone sums to at least one.

For zero winding,

\[
 \sum_{t<s}(d(D_t)-1)=\delta(D_s)-s.
 \tag{5.5}
\]

If this is at least \(T\), again the first term covers the interval. If it
is smaller than \(T\), then

\[
 \delta(D_s)<s+T\le H-1+T.
\]

The terminal edge \(D_s\) belongs to the full support (1.6), and its
indicator term is one. \(\square\)

Take

\[
 T=T_m=m/\log ^8m.
\]

For sufficiently large \(m\), \(T_m\le N-H+2\). By (4.5), the first-term
cost is

\[
 O_A\!\left(\frac{B\log ^{10}m}{\sqrt m}\right).
 \tag{5.6}
\]

For \(L=H-1+T_m\),

\[
 \sqrt{m/(L+1)}=\Theta(\log ^4m).
\]

Equations (5.1) and \(B\asymp4^m/m^{3/2}\) therefore give

\[
 \Delta_{m,L}=o(B/N).
 \tag{5.7}
\]

This proves (0.9). Notice the precise scope: (5.4) solves the weak
\(o(B)\) quotient-cost problem, but not the RP cost (0.1).
Indeed, the lower bound in (4.5) gives the explicit obstruction

\[
 \sum_Dy_T(D)
 \ge c\frac{B\sqrt m}{T_m}
 =c\frac{B\log ^8m}{\sqrt m},
 \tag{5.8}
\]

which is larger than \(B/N\) by a factor tending to infinity.

## 6. A one-potential suffix--coboundary no-go

The preceding dual used the centered deficit \(d-1\). Without that exact
floor subtraction, the following broad but specific one-potential template
cannot reach little-oh at the \(B/N\) scale.

For \(m\ge2\),

\[
 \boxed{\max_{D\in\mathcal D_m}\delta(D)=N-3.}
 \tag{6.1}
\]

Indeed, a height-one path first reaches its maximum at time one. If the
height is \(h\ge2\), at least \(h\) down-steps remain after the first visit
to height \(h\), so \(\delta(D)\le2m-h\le2m-2=N-3\). Equality is attained
by \((10)^{m-2}1100\).

Let \(F:V_H\to\mathbb R\) be arbitrary and let \(\alpha\ge0\). Define

\[
 \begin{aligned}
 Y_{\alpha,F}(D)
 ={}&[\alpha d(D)+F(\tau D)-F(D)]_+\\
 &+[F(D)]_+
  +[1-\alpha\delta(D)-F(D)]_+.
 \end{aligned}
 \tag{6.2}
\]

### Theorem 6.1 (global potential floor)

The weight (6.2) is dual feasible, but every such weight obeys

\[
 \boxed{
 \sum_{D\in V_H}Y_{\alpha,F}(D)
 \ge\frac{|V_H|}{N-3}
 =\frac{B-o(B/N)}{N-3}.}
 \tag{6.3}
\]

#### Proof

On a return core, the first summand gives, after dropping positive parts,

\[
 \alpha(\delta(D_s)+Na)+F(D_s)-F(D_0).
\]

Use the second summand at \(D_0\) and the third at \(D_s\). The resulting
lower bound is

\[
 \alpha(\delta(D_s)+Na)+F(D_s)-F(D_0)
 +[F(D_0)]_+
 +[1-\alpha\delta(D_s)-F(D_s)]_+
 \ge1.
\]

Thus (6.2) is feasible.

Because \(V_H\) is a union of complete \(\tau\)-cycles, the coboundary
telescopes globally. Since \(d(D)\ge1\),

\[
 \sum_{D\in V_H}
 [\alpha d(D)+F(\tau D)-F(D)]_+
 \ge\alpha|V_H|.
 \tag{6.4}
\]

Also, pointwise,

\[
 [F(D)]_++[1-\alpha\delta(D)-F(D)]_+
 \ge[1-\alpha\delta(D)]_+
 \ge[1-\alpha(N-3)]_+.
 \tag{6.5}
\]

Hence the total cost is at least

\[
 |V_H|\left(\alpha+[1-\alpha(N-3)]_+\right).
\]

The minimum over \(\alpha\ge0\) is \(1/(N-3)\), attained at
\(\alpha=1/(N-3)\). This proves (6.3). \(\square\)

The potential \(F\) may be an arbitrary function of height, suffix
deficit, the entire iterated peak-deletion profile, or any other quotient
statistic. Therefore these features cannot succeed merely by being inserted
into one global nonnegative coboundary cancellation.

## 7. Exact nested returns under iterated peak deletion

Let \(\partial D\) be simultaneous deletion of all Dyck peaks. Under the
plane-tree contour bijection this is simultaneous deletion of all leaves.
For nonempty \(D\),

\[
 \operatorname{ht}(\partial D)=\operatorname{ht}(D)-1.
 \tag{7.1}
\]

The equality-particle PBBS gives the semiconjugacy

\[
 \partial(\tau D)=\tau(\partial D),
 \tag{7.2}
\]

where the \(\tau\) on the right is the canonical step-two PBBS map at the
smaller rank.

### Theorem 7.1 (complete nested return chain)

Suppose \(D\) has height \(h\) and starts a consecutive omitted-coordinate
return of gap

\[
 g_0=2s_0+1<N.
\]

For \(0\le j<h\), put

\[
 D^{(j)}=\partial^jD.
\]

Then there are consecutive return gaps \(g_j=2s_j+1\) for \(D^{(j)}\)
such that

\[
 g_{j+1}\le g_j-2,
 \qquad
 s_{j+1}\le s_j-1.
 \tag{7.3}
\]

If

\[
 D^{(h-1)}=(10)^p,
\]

then

\[
 g_{h-1}=2p+1,
 \qquad
 s_{h-1}=p.
 \tag{7.4}
\]

Consequently the exact slack identity is

\[
 \boxed{
 s_0=p+(h-1)
     +\sum_{j=0}^{h-2}(s_j-s_{j+1}-1),}
 \tag{7.5}
\]

and every summand in the final sum is a nonnegative integer. In particular,

\[
 \boxed{h+p\le s_0+1.}
 \tag{7.6}
\]

#### Proof

At level \(j\), the equality particles evolve as the canonical PBBS whose
normalized root is \(D^{(j+1)}\). The equality particle selected at time
zero moves into the physical edge associated with the returned coordinate.
Before that physical coordinate can reappear at time \(g_j\), this particle
must be selected again. If a different particle makes the final entry, the
initial particle must first vacate; if the same particle makes the entry,
then it must have been selected earlier in order to complete a full lap.

Let \(g_{j+1}\) be its first reselection time. In the reduced PBBS this is
the next occurrence of the same omitted particle label, hence a consecutive
return. It occurs strictly before \(g_j\). Both same-label gaps are odd, so
\(g_{j+1}\le g_j-2\). This proves (7.3) and permits iteration all the way
to height one; no small-circumference exception is needed.

This statement concerns only the nested **same-label** return. The stronger
claim that the final entrant is the immediate predecessor, together with
the prescribed Pascal-slot identity, does require the return gap to be
smaller than the current child circumference and may stop at an earlier
deletion level.

The only height-one Dyck word of semilength \(p\) is \((10)^p\). It is fixed
by \(\phi\), and its spatial voltage is one. Its first omitted-coordinate
return is therefore the full circumference \(2p+1\), proving (7.4).
Telescoping

\[
 s_j=s_{j+1}+1+(s_j-s_{j+1}-1)
\]

gives (7.5), and (7.6) follows. \(\square\)

For an outer residence-\(H\) return, (7.6) gives the sharpened eligibility
condition

\[
 h(D)+p(D)\le H.
 \tag{7.7}
\]

This is stronger than the height-gap theorem, but Section 9 shows that its
marginal statistic is still Catalan-dense.

## 8. The all-depth cocycle dual and its exact floor

For \(0\le j<h(D)\), let

\[
 m_j(D)=\text{semilength}(\partial^jD),
 \qquad N_j(D)=2m_j(D)+1,
\]

and define

\[
 d_j(D)=d(\partial^jD),
 \qquad
 \delta_j(D)=\delta(\partial^jD).
 \tag{8.1}
\]

Write \(\tau_j\) for the canonical step-two PBBS map at rank \(m_j(D)\).
The semiconjugacy (7.2) gives

\[
 \partial^j(\tau D)=\tau_j(\partial^jD).
\]

In particular, height and every deletion rank \(m_j(D)\) are constant on
an outer \(\tau\)-cycle, so \(\tau_j\) is consistently defined along that
cycle.

By (7.2), the quantity

\[
 c_j(D)=d_j(D)+\delta_j(D)-\delta_j(\tau D)
 \tag{8.2}
\]

is a literal pulled-back suffix--chronology cocycle.

At level \(j\), the nested return equation gives

\[
 \sum_{t=0}^{s_j-1}d_j(\tau^tD)
 =\delta_j(\tau^{s_j}D)+N_ja_j,
 \qquad a_j\ge0.
\]

Therefore

\[
 \begin{aligned}
 \sum_{t=0}^{s_j-1}c_j(\tau^tD)
 &=\delta_j(D)+N_ja_j\\
 &\ge\delta_j(D)\\
 &\ge h(D)-j.
 \end{aligned}
 \tag{8.3}
\]

The nested prefix has \(s_j\le s_0-j\), so it lies inside the outer support
(1.6).

### Theorem 8.1 (all-depth positive cocycle dual)

For each height \(1\le h\le H-1\), choose numbers

\[
 \alpha_{h,j}\ge0
 \quad(0\le j<h)
\]

satisfying

\[
 \sum_{j=0}^{h-1}\alpha_{h,j}(h-j)\ge1.
 \tag{8.4}
\]

Then

\[
 \boxed{
 y_\alpha(D)=
 \mathbf1_{\{h(D)\le H-1\}}
 \sum_{j=0}^{h(D)-1}\alpha_{h(D),j}[c_j(D)]_+}
 \tag{8.5}
\]

is quotient-dual feasible.

#### Proof

For an outer return of height \(h\), sum the \(j\)-th term over the nested
prefix supplied by Theorem 7.1 and use (8.3). Summing over \(j\) gives at
least the left side of (8.4). All omitted terms are nonnegative. \(\square\)

For example, the genuinely all-depth choice

\[
 \alpha_{h,j}=\frac2{h(h+1)}
 \tag{8.6}
\]

is feasible, because \(\sum_{j<h}(h-j)=h(h+1)/2\). The level-zero choice
\(\alpha_{h,0}=1/h\) is also feasible.

### Theorem 8.2 (orbit-floor no-go)

Every height-homogeneous weight (8.5) obeys

\[
 \boxed{
 \sum_{D\in V_H}y_\alpha(D)
 \ge
 \sum_{\substack{D\in V_H\\h(D)\le H-1}}
 \frac1{h(D)}
 =\Omega_A(B/\sqrt m).}
 \tag{8.7}
\]

#### Proof

On a complete outer \(\tau\)-cycle \(C\) of height \(h\), the
\(\delta_j\)-coboundary telescopes even if the image under \(\partial^j\)
has smaller period. Hence

\[
 \sum_{D\in C}c_j(D)=\sum_{D\in C}d_j(D)\ge|C|,
\]

where the last inequality is the retained integer floor \(d_j(D)\ge1\).
Thus

\[
 \sum_{D\in C}[c_j(D)]_+\ge|C|.
\]

It follows that the cost on \(C\) is at least

\[
 |C|\sum_j\alpha_{h,j}.
\]

Since \(h-j\le h\), (8.4) forces

\[
 \sum_j\alpha_{h,j}\ge1/h.
\]

Summing over cycles proves the first inequality. The spectral lower bound
(3.7) and \(Z_H=o(B/N)\) prove the final estimate. \(\square\)

The same conclusion holds on any chosen union of complete \(\tau\)-cycles:
iteration cannot improve the \(1/h\) floor on the mass to which it is
applied. It could still be useful after a separate theorem localizes every
active return to a union of only \(o(B/\sqrt m)\) quotient edges. Proving
such localization is essentially the missing RP clustering theorem.

There is a slightly broader floor statement which does not use
coboundaries. Consider a height-homogeneous nonnegative ledger

\[
 y(D)=u_h+\sum_{j=0}^{h-1}v_{h,j}d_j(D),
 \qquad u_h,v_{h,j}\ge0,
 \tag{8.8}
\]

whose feasibility is certified only from

\[
 |Q(D,s)|\ge h+2,
 \qquad
 \sum_{E\in Q(D,s)}d_j(E)\ge h-j.
\]

The sufficient coefficient condition is

\[
 (h+2)u_h+\sum_j(h-j)v_{h,j}\ge1.
 \tag{8.9}
\]

Since every \(d_j(D)\ge1\), (8.9) implies pointwise

\[
 \boxed{y(D)\ge\frac1{h+2}.}
 \tag{8.10}
\]

Indeed, multiply (8.8) by \(h+2\) and use \(h-j\le h+2\). Therefore the
reciprocal-height dual is pointwise optimal inside the full uncentered
positive-ledger cone (8.8)--(8.9).

## 9. Why centering and peak profiles still do not close RP_A

Centering \(d_j\) at its exact floor is necessary to avoid (8.7)--(8.10),
but it creates genuine null returns.

Let

\[
 E_p=1^p0^p.
\]

Then

\[
 \phi(E_p)=E_p,
 \qquad
 \delta(E_p)=p,
 \qquad
 d(E_p)=1.
 \tag{9.1}
\]

Its first return has gap \(2p+1\), so \(s=p\), winding \(a=0\), and

\[
 \boxed{
 \sum_{t=0}^{p-1}(d(E_p)-1)
 =\delta(E_p)-p=0.}
 \tag{9.2}
\]

Moreover every nonempty deletion core of a mountain is again a mountain,
so every centered iterated deficit is zero. The terminal mountain-tower
families in the existing PBBS reduction lift this null core to growing-rank
short returns; the nullity is not a finite-rank artefact.

The strengthened eligibility statistic \(p\) in (7.6) is also not
marginally sparse.

### Lemma 9.1 (Catalan-dense primitive unique-top profiles)

For every fixed \(A>0\), there is \(c_A>0\) such that at least \(c_AB\)
Dyck roots of semilength \(m\) are primitive, have a unique maximum peak,
and have height at most \(H\). For every such root,

\[
 p(D)=1,
 \qquad
 d_j(D)=1
 \quad(0\le j<h(D)).
 \tag{9.3}
\]

#### Proof

Take a Dyck path \(F\) of semilength \(m-2\) and height at most
\(\lfloor A\sqrt m/3\rfloor\). Form the primitive path \(1F0\). At its
first highest peak, replace the local peak \(10\) by \(1100\). The result
has semilength \(m\), remains primitive, and its newly inserted inner peak
is the unique global maximum. Its height is at most \(H\) for all
sufficiently large \(m\).

The construction is injective: the unique maximum identifies the inserted
\(1100\), whose contraction recovers \(1F0\), hence \(F\). The spectral
lower bound (3.7), with \(A/3\) in place of \(A\), gives

\[
 \#\{F\}\ge c_A\operatorname{Cat}_{m-2}\ge c_A'B.
\]

In the plane tree, primitivity means that the root has one child; leaf
pruning preserves this until the tree disappears. A unique maximum peak is
a unique deepest leaf, which remains unique under pruning. This proves
(9.3). \(\square\)

Lemma 9.1 does not assert that all these roots start short returns. It proves
the precise marginal no-go: the entire tuple

\[
 h\le H,
 \qquad p=1,
 \qquad d_j=1\text{ at every level}
\]

is Catalan-dense. Any successful centered dual must therefore use actual
same-row return chronology, not merely eligibility thresholds in these
statistics.

Finally, the exact one-step peak-deletion fibre explains why a core-only
charge loses the needed information. If \(E\in\mathcal D_d\) has \(k\)
peaks and \(d\ge1\), then

\[
 \boxed{
 \#\{D\in\mathcal D_m:\partial D=E\}
 =\binom{m+d-k}{2d}.}
 \tag{9.4}
\]

If the final root-slot occupancy is prescribed to equal an integer
\(0\le z\le m-d-k\), the number of parents is

\[
 \boxed{
 \binom{m+d-k-z-1}{2d-1}.}
 \tag{9.5}
\]

Indeed, after the one mandatory new child at each of the \(k\) old leaves,
the remaining \(m-d-k\) new leaves form a weak composition among the
\(2d+1\) ordered child slots. Prescribing one slot leaves \(2d\) slots.
Thus iterated deletion must retain the Pascal slot vector, or an equivalent
chronology-sensitive packet. The pruned core alone has exponentially
unbounded congestion.

## 10. Exact proved boundary

The quotient LP has now isolated three different scales.

1. **Sub-Catalan quotient scale.** The explicit weights (3.3) and (5.4)
   have cost \(o_A(B)\). This answers the weak, unlifted reading of “dual
   cost \(o_A(\operatorname{Cat}_m)\).”

2. **Physical RP scale.** The deck lift multiplies quotient cost by
   \(N\). Therefore RP_A requires the strictly stronger quotient estimate

   \[
   d_H^*=o_A(B/N).
   \]

   None of the constructed weights has this cost.

3. **Positive-ledger obstruction.** The exact floor \(d_j\ge1\) forces the
   height-homogeneous positive additive syntheses (8.5) and (8.8) to cost
   at least \(\Omega_A(B/\sqrt m)\), while the separate one-potential
   construction (6.2) has the absolute floor \((1+o(1))B/N\). Centering is
   compulsory inside these architectures, but mountain returns make every
   centered iterated deficit vanish. Arbitrary localized or phase-varying
   duals are not covered by these no-go statements.

The smallest remaining theorem is therefore the following.

> **Chronology-sensitive centered-tower dual — UNPROVED.** For every fixed
> \(A>0\), find nonnegative quotient weights \(y^0,y^+\) such that \(y^0\)
> covers every zero-winding short-return interval, including every iterated
> mountain-null tower and its Pascal-slot lifts, \(y^+\) covers every
> positive-winding interval, and
> \[
>   \sum_D(y^0_D+y^+_D)=o_A(B/N).
> \]
> A localized version of (4.3) is one possible source for \(y^+\). The
> weights must exploit genuine phase-varying same-row chronology or a
> proved sparse interval packetization; a global nonnegative function of
> marginal deletion statistics cannot suffice.

This structured statement is sufficient for RP_A. The unrestricted
full-dual condition (2.3) with cost \(o_A(B/N)\) is, by Theorem 2.1,
equivalent to RP_A up to the exact factor-two circular-interval integrality
gap. No constant-one conclusion is claimed in this report.
