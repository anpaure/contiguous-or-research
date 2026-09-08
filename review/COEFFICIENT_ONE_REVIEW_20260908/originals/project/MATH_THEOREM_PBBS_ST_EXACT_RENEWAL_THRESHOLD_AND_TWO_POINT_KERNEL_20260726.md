# PBBS Gaussian returns: the exact renewal threshold and two-point Pascal kernel

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil ,
\tag{0.1}
\]

where \(A>0\) is fixed. Let \(E_H\) be the set of normalized PBBS
quotient roots on cycles longer than \(H+1\) which start a consecutive
omitted-coordinate return of residence at most \(H\), and write

\[
 R_H=|E_H|,\qquad
 \mathcal C_H=\sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|.
\tag{0.2}
\]

This note gives a complete one-pruning-level renewal formula for both
quantities. It sharpens the former passage sum in two ways.

1. Above a nonempty pruned root \(E\), all short parent returns are
   controlled by one integer threshold \(Z_H(E)\). If the inverse
   peak-deletion fibre is represented by a weak composition of free leaf
   mass \(y\) into \(K=2d+1\) slots, then a parent starts a short return
   if and only if its terminal coordinate is at most \(Z_H(E)\).

2. The two-point function is exactly an intersection of two transported
   threshold cylinders. When the transport takes terminal slots to
   individual slots, this intersection has an explicit stars-and-bars
   formula. Uniformly in the Pascal saddle and for all thresholds at
   most \(3\log m\), two distinct transported slots are asymptotically
   independent, while a repeated slot changes the answer by at most the
   sharp factor \(4/3+o(1)\).

Consequently, on every coordinate-transport sector, outer Pascal sheets
preserve the bounded-versus-divergent short-lag clustering alternative:

\[
 \boxed{
 \left({9\over16}-o(1)\right){T_H\over S_H}
 \le {\mathcal C_H^{\rm cell}\over R_H^{\rm cell}}
 \le \left({4\over3}+o(1)\right){T_H\over S_H}.}
\tag{0.3}
\]

Here \(S_H\) is the complete-fibre-weighted number of active reduced
phases and \(T_H\) is its complete-fibre-weighted short-lag pair count;
the definitions are in Section 5. Formula (0.3) includes every terminal
value \(z\le3\log m\), not only the terminal-zero sector. (Terminal
occupancy equals winding on the mountain rotor, but that identity is not
asserted for a general core.)

This proves a rigorous decision boundary, but not \((ST_A)\). At critical
one-point mass, bounded \(T_H/S_H\) would refute \((ST_A)\) through the
Caro--Wei bound, whereas \((ST_A)\) requires \(T_H/S_H\to\infty\).
The exact one-level renewal kernel supplies neither global behavior.
The raw terminal-singleton statement excludes one prescribed return of
one parent vector; it does not by itself prove that the other reduced
threshold cylinders are empty.  The calibrated minimal-expansion audit in
MATH_AUDIT_ST_A_REDUCED_PREDECESSOR_PHASE_DEGREE_20260726.md repairs
this when \(H=s+1\), producing actual long-period Pascal-saddle cores with
reduced degree at most two.  Their complete deterministic-collar mass is,
however, only
\[
 (B_m/H)e^{-\Theta(\sqrt m)}.
\]
Thus the remaining theorem is genuinely the **critical-mass** reduced
predecessor-passage phase process (and, outside coordinate transport, the
dense-reframing cylinder intersection), not another Pascal marginal
estimate.

## 1. One return threshold above a pruned core

Let \(D\in\mathcal D_m\) and let

\[
 E=\partial D\in\mathcal D_d,
 \qquad k=\operatorname {pk}(E),
 \qquad y=m-d-k,
 \qquad K=2d+1.
\tag{1.1}
\]

After putting one mandatory new leaf at every old leaf, the inverse
peak-deletion fibre over \(E\) is canonically the weak-composition set

\[
 \mathcal W_{K,y}
 =\{(n_0,\ldots,n_{K-1})\in\mathbb Z_{\ge0}^K:
                  n_0+\cdots+n_{K-1}=y\}.
\tag{1.2}
\]

The distinguished terminal root slot is denoted by \(\star(E)\). Let

\[
 0<B_1(E)<B_2(E)<\cdots
\tag{1.3}
\]

be the positive selection times of the immediate predecessor of the
distinguished equality particle, with the leader having already returned,
as in the exact predecessor-passage theorem. Before the outer
circumference, terminal occupancy \(z\) gives the first parent return at

\[
                       G(D)=B_{2z+2}(E).
\tag{1.4}
\]

Define

\[
 Z_H(E)=\max\{z\ge0:B_{2z+2}(E)\le2H-1\},
\tag{1.5}
\]

with \(Z_H(E)=-1\) if the set is empty. Since the times in (1.3) are
strictly increasing, the active terminal values form exactly the initial
interval

\[
                         \{0,1,\ldots,Z_H(E)\}.
\tag{1.6}
\]

### Theorem 1.1 (exact threshold criterion)

Assume \(2H-1<N\). A parent \(D\) above the nonempty core \(E\) starts a
return of residence at most \(H\) if and only if

\[
                    n_{\star(E)}(D)\le Z_H(E).
\tag{1.7}
\]

The return is the first consecutive return; its terminal value indexes the
\((2z+2)\)-nd predecessor selection in (1.4).

#### Proof

The exact predecessor-passage theorem says that a parent with terminal
occupancy \(z\) has its next repeated physical coordinate at the unique
time \(B_{2z+2}(E)\), provided this time is below the outer circumference.
The no-overtaking proof in that theorem also proves consecutiveness. Thus
the cutoff is precisely (1.5). Strict increase of the selection times
gives (1.6), and hence (1.7). \(\square\)

The number of parents above \(E\) which satisfy (1.7) is therefore

\[
 \begin{aligned}
 \mathsf K(y,K;Z)
 &=\sum_{z=0}^{\min(y,Z)}
      \binom{y-z+K-2}{K-2}\\
 &=\binom{y+K-1}{K-1}
   -\binom{y-Z+K-2}{K-1},
 \end{aligned}
\tag{1.8}
\]

where the second binomial is zero when its upper argument is smaller than
\(K-1\), and \(\mathsf K(y,K;-1)=0\). The second equality is the hockey
stick identity.

### Corollary 1.2 (exact one-point renewal formula)

Let \(R_H^{\rm all}\) count all normalized roots, before short quotient
cycles are deleted. Apart from the completely pruned one-root boundary,

\[
 \boxed{
 R_H^{\rm all}
 =\epsilon_m(H)+
   \sum_{d=1}^{m-1}\ \sum_{E\in\mathcal D_d}
     \mathsf K(m-d-\operatorname {pk}(E),\,2d+1;\,Z_H(E)),}
\tag{1.9}
\]

where \(\epsilon_m(H)\in\{0,1\}\). Moreover, for every fixed \(L\),

\[
 R_H=R_H^{\rm all}+o(B_m/m^L).
\tag{1.10}
\]

#### Proof

Inverse peak-deletion fibres partition \(\mathcal D_m\), so summing (1.8)
proves (1.9). The established voltage-itinerary bound gives at most

\[
 (2H+2)N^{2H+2}=\exp(O_A(\sqrt m\log m))
\]

roots on quotient cycles of length at most \(H+1\). This is
\(o(B_m/m^L)\) for every fixed \(L\), proving (1.10). \(\square\)

Formula (1.9) is equivalent to the former triple sum over
\((E,z,B_{2z+2})\), but makes its renewal content explicit: the only
dynamic datum left at one pruning level is the threshold \(Z_H(E)\).

## 2. The exact transported two-point formula

Peak deletion semiconjugates the PBBS quotient map:

\[
                         \partial\tau=\tau\partial.
\tag{2.1}
\]

Fix a reduced quotient cycle \(C=(E_i)_{i\in\mathbb Z/\ell\mathbb Z}\),
where \(\ell>H+1\), and fix an invariant inverse rank/peak-profile cell
above it. Let \(\Omega_i\) be its parent fibre over \(E_i\). The time
\(t\) PBBS map gives a bijection

\[
                  \Theta_{i,t}:\Omega_i\longrightarrow\Omega_{i+t}.
\tag{2.2}
\]

The fibre cardinality is independent of \(i\): rank is fixed and peak
count is invariant under the PBBS quotient permutation (equivalently, the
number of equality particles is invariant).

Define the active threshold cylinder

\[
 \mathcal A_i=
 \{x\in\Omega_i:n_{\star(E_i)}(x)\le Z_H(E_i)\},
\tag{2.3}
\]

with \(\mathcal A_i=\varnothing\) when \(Z_H(E_i)=-1\).

### Theorem 2.1 (exact one- and two-point fibre ledger)

The contribution of this cell to (0.2) is

\[
 \boxed{
 R_H(C)=\sum_i|\mathcal A_i|,}
\tag{2.4}
\]

\[
 \boxed{
 \mathcal C_H(C)=
 \sum_{t=1}^{H+1}\sum_i
 |\mathcal A_i\cap\Theta_{i,t}^{-1}\mathcal A_{i+t}|.}
\tag{2.5}
\]

#### Proof

Theorem 1.1 identifies \(\mathcal A_i\) with the parent roots over phase
\(i\) which start an eligible return. This proves (2.4). A root
\(x\in\Omega_i\) contributes to the lag-\(t\) intersection precisely when
both \(x\in\mathcal A_i\) and
\(\Theta_{i,t}x\in\mathcal A_{i+t}\), which is the summand in (2.5).
Summing over phases and lags proves the result. \(\square\)

Equation (2.5) is exact without any stability hypothesis. It also marks
the precise limitation of every one-column Pascal count: the marginal
sizes \(|\mathcal A_i|\) do not determine their transported
intersections.

## 3. Two bounded-coordinate cylinders

For \(Z\ge-1\), put

\[
 A_a(Z)=\{\mathbf n\in\mathcal W_{K,y}:n_a\le Z\}.
\tag{3.1}
\]

The case \(Z=-1\) is empty. Let

\[
                         P(y,K)=\binom{y+K-1}{K-1}.
\tag{3.2}
\]

### Lemma 3.1 (exact two-threshold kernel)

For \(Z,Z'\ge0\) and two distinct coordinates \(a\ne b\),

\[
 \boxed{
 \begin{aligned}
 |A_a(Z)\cap A_b(Z')|
 ={}&P(y,K)
 -\binom{y-Z+K-2}{K-1}
 -\binom{y-Z'+K-2}{K-1}\\
 &+\binom{y-Z-Z'+K-3}{K-1}.
 \end{aligned}}
\tag{3.3}
\]

For \(a=b\),

\[
 \boxed{|A_a(Z)\cap A_a(Z')|
        =\mathsf K(y,K;\min\{Z,Z'\}).}
\tag{3.4}
\]

#### Proof

For (3.3), use inclusion--exclusion. The number with
\(n_a\ge Z+1\) is obtained by subtracting \(Z+1\) from that coordinate,
and is

\[
 \binom{y-(Z+1)+K-1}{K-1}
 =\binom{y-Z+K-2}{K-1}.
\]

Imposing both lower bounds subtracts \(Z+Z'+2\) units and gives the final
binomial in (3.3). Equation (3.4) is immediate. \(\square\)

It is useful to normalize the formulas. Define

\[
 q(y,K;u)
 ={\binom{y-u+K-1}{K-1}\over P(y,K)}
 ={(y)_{\underline u}\over(y+K-1)_{\underline u}},
 \qquad u\ge0,
\tag{3.5}
\]

with \(q=0\) when \(u>y\). Thus

\[
 {\mathsf K(y,K;Z)\over P(y,K)}=1-q(y,K;Z+1).
\tag{3.6}
\]

For distinct coordinates, (3.3) divided by \(P(y,K)\) is

\[
 1-q(y,K;Z+1)-q(y,K;Z'+1)
   +q(y,K;Z+Z'+2).
\tag{3.7}
\]

## 4. Uniform Pascal-saddle asymptotics

Assume the usual fixed saddle tube

\[
 d={m\over2}+O(\sqrt{m\log m}),
 \qquad
 k={m\over6}+O(\sqrt{m\log m}).
\tag{4.1}
\]

Then

\[
 K=2d+1=m+O(\sqrt{m\log m}),
 \qquad
 y=m-d-k={m\over3}+O(\sqrt{m\log m}),
\tag{4.2}
\]

and hence

\[
                         \rho_m={y\over y+K-1}={1\over4}+o(1).
\tag{4.3}
\]

### Lemma 4.1 (uniform falling-factorial estimate)

Uniformly for \(0\le u\le6\log m+2\),

\[
 \boxed{q(y,K;u)=\rho_m^u
       \left(1+O\left({u^2\over m}\right)\right).}
\tag{4.4}
\]

#### Proof

From (3.5),

\[
 \log q(y,K;u)
 =u\log\rho_m+
   \sum_{j=0}^{u-1}
   \left[\log\left(1-{j\over y}\right)
   -\log\left(1-{j\over y+K-1}\right)\right].
\]

Both denominators are \(\Theta(m)\), uniformly in (4.1). Taylor's
formula makes the sum \(O(u^2/m)\). Exponentiation proves (4.4).
\(\square\)

Write

\[
 p_Z=1-\rho_m^{Z+1}.
\tag{4.5}
\]

### Theorem 4.2 (uniform low-slot two-point neutrality)

Uniformly for \(0\le Z,Z'\le3\log m\):

* for two distinct transported slots,

  \[
  { |A_a(Z)\cap A_b(Z')|\over P(y,K)}
  =p_Zp_{Z'}+o(1);
  \tag{4.6}
  \]

* for the same transported slot,

  \[
  p_Zp_{Z'}-o(1)\le
  { |A_a(Z)\cap A_a(Z')|\over P(y,K)}
  \le\left({4\over3}+o(1)\right)p_Zp_{Z'}.
  \tag{4.7}
  \]

In particular, every active one-phase density lies in

\[
                         {3\over4}-o(1)\le p_Z\le1.
\tag{4.8}
\]

#### Proof

Equation (4.6) follows from (3.7) and Lemma 4.1, since

\[
 \rho_m^{Z+Z'+2}
 =\rho_m^{Z+1}\rho_m^{Z'+1}.
\]

For the same coordinate, suppose without loss of generality that
\(Z\le Z'\). Equation (3.4) has normalized value \(p_Z+o(1)\). This is
at least \(p_Zp_{Z'}-o(1)\), and its ratio to the product is
\(1/p_{Z'}\le4/3+o(1)\) by (4.8). Finally, the smallest active threshold
is \(Z=0\), for which \(p_0=1-\rho_m=3/4-o(1)\). \(\square\)

The upper constant \(4/3\) is sharp at the saddle: take two identical
terminal-zero conditions, for which the intersection density tends to
\(3/4\) while the product of the marginal densities tends to \(9/16\).

## 5. The phase process is the entire remaining two-point datum

Work in a coordinate-transport cell: after pulling every fibre back to a
reference weak-composition set, each threshold cylinder in (2.3) is a
single-coordinate set \(A_{a_i}(Z_i)\). Assume (4.1) and
\(Z_i\le3\log m\), which is exactly the retained low-slot normal form.
Let \(P_C\) be the complete fibre size, constant on the reduced cycle, and
put

\[
 J_C=\{i:Z_H(E_i)\ge0\}.
\tag{5.1}
\]

Define

\[
 S_H(C)=P_C|J_C|,
 \qquad
 T_H(C)=P_C\sum_{t=1}^{H+1}|J_C\cap(J_C-t)|.
\tag{5.2}
\]

For a union of such cells, sum (5.2) over the cells and denote the results
by \(S_H,T_H\).

### Theorem 5.1 (sharp one-level clustering preservation)

Uniformly over every union of saddle, low-slot, coordinate-transport
cells,

\[
 {3\over4}S_H-o(S_H)\le R_H^{\rm cell}\le S_H,
\tag{5.3}
\]

\[
 {9\over16}T_H-o(T_H)\le
 \mathcal C_H^{\rm cell}\le T_H.
\tag{5.4}
\]

Consequently, whenever \(S_H>0\),

\[
 \boxed{
 \left({9\over16}-o(1)\right){T_H\over S_H}
 \le {\mathcal C_H^{\rm cell}\over R_H^{\rm cell}}
 \le \left({4\over3}+o(1)\right){T_H\over S_H}.}
\tag{5.5}
\]

#### Proof

Apply (4.8) to every active phase and sum, proving (5.3). For every
ordered active phase pair counted by \(T_H\), Theorem 4.2 bounds the
intersection density between \(9/16-o(1)\) and one. Summation gives
(5.4). Dividing the lower bound in (5.4) by the upper bound in (5.3),
and the upper bound in (5.4) by the lower bound in (5.3), gives (5.5).
\(\square\)

Thus an outer Pascal sheet cannot turn a bounded reduced phase degree into
divergent clustering, nor can it regularize a divergent reduced phase
degree. This conclusion now includes every retained terminal value
\(z\le3\log m\), so positive winding in the low-slot normal form is not a
separate Pascal loophole.

## 6. Implication for \((ST_A)\)

For the full active set, the conflict-graph bound is

\[
 \overline\nu_H\ge{R_H^2\over R_H+2\mathcal C_H}.
\tag{6.1}
\]

Suppose a union of the cells in Theorem 5.1 has

\[
                         S_H\ge c_A B_m/H.
\tag{6.2}
\]

If \(T_H/S_H=O_A(1)\), then (5.3)--(5.5) and (6.1), applied to this
subfamily alone, give

\[
                         \overline\nu_H=\Omega_A(B_m/H),
\tag{6.3}
\]

and \((ST_A)\) is false. Conversely, if \((ST_A)\) holds while (6.2)
holds, then necessarily

\[
                         T_H/S_H\longrightarrow\infty.
\tag{6.4}
\]

Equations (6.3)--(6.4) are a decision boundary, not a decision. The exact
renewal threshold \(Z_H(E)\) is a dynamic statistic of the reduced PBBS
predecessor itinerary. Neither the Narayana--Pascal cell mass nor the
outer slot kernel estimates its weighted short-lag phase degree.

There are rigorous calibrations in both directions.

* The one-defect mountain rotor has \(T_H/S_H=\Theta(H)\), hence divergent
  clustering, but its retained Gaussian-rank mass is subcritical.
* The terminal-singleton construction has a selected duration-\(s\)
  parent conflict graph of degree at most two, but this does not prove
  \(T_H/S_H=O(1)\) for the reduced active support.  If \(x\) is the
  selected parent vector, rejection at phase \(t\) gives only
  \(x_{a_t}>Z_H(E_t)\); reduced inactivity would require the stronger
  statement \(Z_H(E_t)=-1\).  Its deterministic collar also costs
  \(\Theta(\sqrt m)\) rank and makes its selected-parent mass
  \(e^{-\Theta(\sqrt m)}B_m/H\).

  After calibrating \(H=s+1\) and replacing each first-pruned core by its
  minimal expansion, the height-gap theorem removes every alternative
  duration and the terminal rotor gives genuine reduced degree at most
  two.  The Narayana comparison
  \[
    \operatorname {Nar}(d-3p+3,k-2)/
    \operatorname {Nar}(d,k)
    =\exp[-(6\log(3/2)+o(1))p]
  \]
  shows that the complete collar class is still \(o(B_m/H)\).

Therefore both local behaviors are compatible with every exact formula in
this note. Settling \((ST_A)\) still requires one genuinely global theorem:
either critical weighted mass with bounded reduced phase degree (which
refutes \((ST_A)\)), or divergent reduced phase degree together with a
packing upper bound (which can prove it). In the densely reframing sector,
one must additionally control the exact intersections (2.5), because the
transported terminal condition need not remain a single-coordinate
threshold.

## 7. Audit and scope

1. The threshold criterion uses the already proved exact
   predecessor-passage theorem; it does not use the retracted implication
   \(d(D)=1\Rightarrow\) short return.
2. Formula (1.9) counts roots, not quotient cycles or physical lifts.
   The short-cycle deletion in (1.10) is made explicitly.
3. Formula (2.5) is valid for arbitrary fibre transport. Sections 3--5
   apply only when that transport is by individual slot coordinates.
4. The same-slot case is retained. It is exactly the source of the sharp
   factor \(4/3\); treating all two-point constraints as independent would
   be false.
5. The low-slot uniformity is logarithmic. The error in (4.4) is
   \(o(1)\) uniformly for \(Z,Z'\le3\log m\).
6. No lower bound such as (6.2) is inferred from a capacity envelope.
   It is displayed as a separate hypothesis.
7. The theorem neither proves nor refutes \((ST_A)\). It proves that one
   peak-deletion level, including all low terminal occupancies, is
   quantitatively neutral for the clustering ratio. The missing datum is
   the actual reduced predecessor-passage phase process.
