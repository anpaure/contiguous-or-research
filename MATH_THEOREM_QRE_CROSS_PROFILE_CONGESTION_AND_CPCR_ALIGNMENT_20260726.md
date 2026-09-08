# QRE cross-profile congestion and exact alignment with CPCR

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Fix \(A>0\) and

\[
                         q=A\sqrt m+O(1).
\tag{0.1}
\]

For the independent-local-rank-matching atlas, global raw QRE_A is
**not proved or refuted** here. The following statements are proved.

1. After an \(o(N_q)\) quarantine, every raw family contained in one
   safe diffuse ordered target profile expands, on either sign, by

   \[
                          K_q=(3/2)^q.
   \tag{0.2}
   \]

2. Every global Hall-deficient family must therefore use more than
   \(K_q\) ordered profiles. More sharply, its profilewise neighborhoods
   must overlap on common middle owners with weighted average
   multiplicity greater than \(K_q\).

3. The full ordered-profile score has no entropy advantage over
   cross-profile competition. A typical single middle owner is adjacent
   to

   \[
             (1-o(1))\binom{2b+q-1}{q},
             \qquad b=m/d+O(1),\quad d=\Theta(\log m),
   \tag{0.3}
   \]

   predecessor profiles, with the same
   \((A/2+o(1))\sqrt m\log m\) leading entropy as the full score.
   The certified full-score bound
   \(\binom{\lfloor\rho b\rfloor}{q}(7/6)^q\) is smaller by
   \(\exp(\Theta_A(\sqrt m))\). By contrast, the cruder factor
   \((3/2)^q\) in (0.2) is smaller by
   \(\exp(\Theta_A(\sqrt m\log m))\).

4. A common parallel packet-axis selector through \(H=o(R)\) adds only
   \(O(W/\sqrt R)=o(W)\) aggregate raw Hall loss beyond the maximal
   source-normalized harmonic deficit, simultaneously in all depths and
   both signs.

5. The diverse-order compiler removes all within-packet repeats. In the
   authoritative CPCR state space, the floor energy is exactly twice
   the excess, above its integer minimum, of the number of colliding
   unordered packet-occurrence pairs. Every such pair is cross-parent.

6. As a convex certificate, raw QRE is strictly weaker than CPCR. QRE
   controls unit demand and ungrouped source capacity. CPCR controls the
   exact \(c_q/c_q+1\) quotas in one common legal all-depth packet
   resolution. This is an abstract certificate separation, not a
   constructed actual atlas satisfying QRE and failing CPCR.

Thus the minimum unresolved raw statement is a weighted
**cross-profile common-source inequality** for the independent-rank
atlas. Even if that is proved, the remaining coefficient-one statement
is still the grouped cross-parent floor-covariance theorem CPCR. Once a
legal state is fixed, no separate common-order, payload, seam, or
within-packet term survives in the energy. Those conditions still
constrain which states are legal.

## 1. Raw graphs and the Hall dual

Let

\[
 \mathcal T_q^-=\binom{[2m]}{m-q},\qquad
 \mathcal T_q^+=\binom{[2m]}{m+q},\qquad
 \mathcal O_m=\binom{[2m]}m .
\tag{1.1}
\]

Write \(G_q^\epsilon\) for either maximal rank-twisted compatibility
graph, with target shore \(\mathcal T_q^\epsilon\) and source shore
\(\mathcal O_m\). Every lower edge has \(T\subset X\), every upper edge
has \(X\subset U\), and the edited coordinates are intrinsic split
endpoints in the source-rank local matchings.

For a nonnegative target weight \(y\), put

\[
                         M_X(y)=\max\{y_T:T\sim X\},
\tag{1.2}
\]

with an empty maximum equal to zero. The weighted Hall inequality is

\[
                         \sum_XM_X(y)\ge\sum_Ty_T.
\tag{1.3}
\]

It is equivalent to ordinary Hall. Indicators give necessity. If Hall
holds, a matching saturating the target shore sends each \(y_T\) to a
distinct adjacent source, proving sufficiency.

Partition the retained target shore into exact ordered half-rank
profiles \(\tau\), and define

\[
 a_{\tau X}(y)=\max\{y_T:T\in\tau,\ T\sim X\}.
\tag{1.4}
\]

Then

\[
                         M_X(y)=\max_\tau a_{\tau X}(y).
\tag{1.5}
\]

## 2. Weighted within-profile expansion

The audited overlap-component theorem gives, on every retained safe
diffuse profile \(\tau\),

\[
                         |N(\mathcal A)|\ge K_q|\mathcal A|
\tag{2.1}
\]

for every raw \(\mathcal A\subseteq\tau\), on both signs. Its relative
exception is at most \(2qe^{-cd}\). With \(d=C\log m\), \(C\) chosen
large enough, these exceptions, the unsafe profiles, and the nondiffuse
profiles have total mass \(o(N_q)\).

### Lemma 2.1 (weighted profile inequality)

For every nonnegative \(y\) supported on a retained profile \(\tau\),

\[
                 \sum_Xa_{\tau X}(y)
                    \ge K_q\sum_{T\in\tau}y_T.
\tag{2.2}
\]

#### Proof

For \(s\ge0\), put
\(\mathcal A_s=\{T\in\tau:y_T>s\}\). Layer cake and (2.1) give

\[
\begin{aligned}
 \sum_Xa_{\tau X}(y)
 &=\int_0^\infty |N(\mathcal A_s)|\,ds\\
 &\ge K_q\int_0^\infty|\mathcal A_s|\,ds
 =K_q\sum_{T\in\tau}y_T.
\end{aligned}
\]

\(\square\)

No randomness of the local rank matchings enters Lemma 2.1. Randomness
is relevant only to the unresolved alignment of different profiles on
the same raw sources.

## 3. Cross-profile congestion

For \(M_X(y)>0\), define

\[
 \mu_X(y)=\frac{\sum_\tau a_{\tau X}(y)}{M_X(y)};
\tag{3.1}
\]

put \(\mu_X(y)=0\) when \(M_X(y)=0\).

### Theorem 3.1 (profile-spreading and congestion)

For every nonnegative weight \(y\) supported on the retained target
shore,

\[
 \boxed{
 \sum_X M_X(y)\mu_X(y)
 =\sum_{X,\tau}a_{\tau X}(y)
 \ge K_q\sum_Ty_T.}
\tag{3.2}
\]

Consequently:

1. if \(y\) is supported on at most \(p\) ordered profiles, then

   \[
        \sum_XM_X(y)\ge \frac{K_q}{p}\sum_Ty_T;
   \tag{3.3}
   \]

2. for \(y=\mathbf1_{\mathcal A}\), \(\mu_X(y)\) is exactly the number
   of profiles \(\tau\) for which
   \(X\in N(\mathcal A\cap\tau)\); and
3. if, for some \(0\le\varepsilon<1\),

   \[
         \sum_XM_X(y)<(1-\varepsilon)\sum_Ty_T,
   \tag{3.4}
   \]

   then

   \[
    \frac{\sum_XM_X(y)\mu_X(y)}{\sum_XM_X(y)}
       >\frac{K_q}{1-\varepsilon}.
   \tag{3.5}
   \]

In particular, a Hall-deficient family must meet more than \(K_q\)
profiles and must align their neighborhoods with average active-profile
multiplicity greater than \(K_q\).

#### Proof

Sum (2.2) over the target profiles to get (3.2). If at most \(p\)
profiles are active, then \(\mu_X\le p\), giving (3.3). For an
indicator, every nonzero \(a_{\tau X}\) equals one. Finally divide
(3.2) by (3.4) to obtain (3.5). \(\square\)

### Corollary 3.2 (a sufficient cross-profile gate)

If, uniformly for every nonnegative \(y\),

\[
 \sum_{X,\tau}a_{\tau X}(y)
 \le (1+o(1))K_q\sum_XM_X(y),
\tag{3.6}
\]

then

\[
                         \sum_XM_X(y)
 \ge(1-o(1))\sum_Ty_T.
\tag{3.7}
\]

Thus (3.6), or a sharper component-indexed analogue, proves QRE_A.
The weight \(y\) may depend adversarially on the whole realized
permutation array; annealed profile symmetry does not prove (3.6).

There is no hidden counting advantage in \(K_q\).

### Theorem 3.3 (predecessor-profile entropy is sharp)

Let \(\kappa=((a_j,c_j))_{j\le b}\) be a central ordered middle
profile. The exact lower and upper predecessor-profile counts are

\[
\begin{aligned}
 P_q^-(\kappa)
 &=[z^q]\prod_{j=1}^b
   (1+z+\cdots+z^{a_j})(1+z+\cdots+z^{c_j}),\\
 P_q^+(\kappa)
 &=[z^q]\prod_{j=1}^b
   (1+z+\cdots+z^{d-a_j})(1+z+\cdots+z^{d-c_j}).
\end{aligned}
\tag{3.8}
\]

Consequently

\[
 \binom{2b}{q}\le P_q^\epsilon(\kappa)
 \le P_{b,q}:=\binom{2b+q-1}{q},
\tag{3.9}
\]

and

\[
 \log P_{b,q}
 =q\log\frac{2eb}{q}+O(q^2/b+\log q)
 =\left(\frac A2+o(1)\right)\sqrt m\log m.
\tag{3.10}
\]

For a raw owner \(X\in\kappa\), let \(p_j,s_j\) be its two singleton-side
counts in block \(j\), measured in its source-rank matching. The number
of predecessor profiles literally visible from \(X\) is

\[
 V_q(X)=[z^q]\prod_{j=1}^b
       (1+z+\cdots+z^{p_j})(1+z+\cdots+z^{s_j}).
\tag{3.11}
\]

For all but \(o(1)\) of the raw owners in every retained central
profile,

\[
                         V_q(X)=(1-o(1))P_{b,q}.
\tag{3.12}
\]

For the certified constant \(\rho=1/13\),

\[
 K_q^{\rm cert}=\binom{\lfloor\rho b\rfloor}{q}(7/6)^q
\]

satisfies

\[
 \log\frac{P_{b,q}}{K_q^{\rm cert}}
 =q\log\frac{12}{7\rho}+O(q^2/b+\log q)=\Theta(q).
\tag{3.13}
\]

#### Proof

An ordered predecessor is uniquely specified by its \(2b\) nonnegative
half-rank decrements, giving (3.8). Removing the caps gives the
stars-and-bars upper bound in (3.9); restricting every decrement to zero
or one gives the lower bound. Stirling's formula gives (3.10).

Equation (3.11) is the same count with the actual singleton-side caps.
On the central core, hypergeometric lower tails give fixed
\(c_0,c_1>0\) such that \(p_j,s_j\ge c_0d\) in every block outside an
\(O(be^{-c_1d})=o(1)\) owner family. If \(N=2b\) and \(L=c_0d\), the
fraction of weak \(N\)-part compositions of \(q\) violating at least
one cap is at most

\[
                         N(q/N)^L
 =\exp[-\Theta((\log m)^2)]=o(1).
\]

This proves (3.12). A final Stirling comparison gives (3.13).
\(\square\)

At the balanced collision-free benchmark, the score
\(2^q\binom bq\) exactly equals the one-edit-per-block predecessor
count of a central owner. Thus unweighted expansion and incoming
congestion match at their natural scale. Any proof of QRE must exploit
the weighted component ratios and common capacities.

The cancellation persists at the first nontrivial normalized level.

### Conditional Theorem 3.4 (uniform predecessor averaging has a linear Gaussian deficit)

Restrict to allocations having at most two promotions in every
macroblock. On the central core, every middle profile has exactly

\[
                         D_{b,q}=[z^q](1+2z+3z^2)^b
\tag{3.14}
\]

predecessor profiles. For \(T\in\tau\), let

\[
 K_{\tau,2}(T)=\sum_{\kappa}^{(\le2)}R_{\tau\kappa}(T),
 \qquad
 H_{\tau,2}(T)=\frac{K_{\tau,2}(T)}{D_{b,q}},
\tag{3.15}
\]

where \(R_{\tau\kappa}(T)\) is the exact overlap-component ratio.
Assume the following uniform saddle lemma.

> **Unproved Uniform Saddle Lemma.** There is an explicitly measurable
> class of ordered target profiles of total mass \(1-o(1)\), uniform on
> which the tilted coefficient extraction in (3.19) has its local
> central-limit asymptotic through every real tilt in a fixed
> neighborhood of \(1\), with uniformly integrable exponential moments
> and total error \(o(1)\).

Then, on every profile in that class,

\[
 \log H_{\tau,2}(T)
 =C_\tau+2A Z_\tau(T)+o_{\mathbb P}(1),
 \qquad Z_\tau\Rightarrow N(0,1),
\tag{3.16}
\]

with exponential-moment convergence on fixed compact tilts. Moreover,

\[
 \frac1{N_q}\sum_T H_{\tau(T),2}(T)=e^{A^2+o(1)}.
\tag{3.17}
\]

Consequently

\[
 \boxed{
 \frac1{N_q}\#\{T:H_{\tau(T),2}(T)<1\}
 \ge
 \frac12\Phi\left(\frac{A^2-\log2}{2A}\right)-o(1)>0.}
\tag{3.18}
\]

Thus the uniform capacity \(1/D_{b,q}\) on every predecessor profile
fails the pointwise weighted-score criterion on a linear target family.

#### Proof

In one block there are one, two, and three allocation labels of sizes
zero, one, and two, proving (3.14). If

\[
 r_j(T)=e_j\left(\frac1{p_j+1}+\frac1{s_j+1}\right)
\]

is the exact one-promotion score and \(w_j(T)\) is the sum of the three
two-promotion ratios, then the overlap-component decomposition gives

\[
                         K_{\tau,2}(T)
 =[z^q]\prod_{j=1}^b(1+r_j(T)z+w_j(T)z^2).
\tag{3.19}
\]

The denominator saddle is
\(z_0=(Ad/(2\sqrt m))(1+o(1))\). On a typical profile, if \(f_j\) is
the full-edge overlap in the rank-\((a_j+c_j+1)\) matching, Taylor
expansion gives

\[
 r_j-\mathbb Er_j
 =\left(\frac{16}{d}+o(d^{-1})\right)
   (f_j-\mathbb Ef_j)+\xi_j,
\tag{3.20}
\]

where \(z_0\sum_j\xi_j=o_{\mathbb P}(1)\). Since
\(\operatorname {Var}f_j=d/16+o(d)\) on average over a typical
ordered profile,

\[
 z_0^2\sum_j\operatorname {Var}r_j=4A^2+o(1).
\tag{3.21}
\]

The block variables are independent and satisfy Lindeberg. Expanding
the logarithm of (3.19), the cubic remainder is

\[
                         O(bz_0^3)=O(d^2/\sqrt m)=o(1),
\]

and the centered quadratic term is \(o_{\mathbb P}(1)\). The unproved
Uniform Saddle Lemma upgrades these estimates to the uniform tilted
local central limit theorem and exponential-moment statement (3.16).

For every safe arc, overlap-component double counting gives

\[
                         \sum_{T\in\tau}R_{\tau\kappa}(T)
 =(1-o(1))|\kappa|.
\]

Every retained central owner profile has \(D_{b,q}\) predecessors.
Summing first over arcs and then over owner profiles yields

\[
                         \sum_TK_{\tau(T),2}(T)
 =(1-o(1))D_{b,q}W,
\]

which proves (3.17). Let
\(M_\tau=|\tau|^{-1}\sum_{T\in\tau}H_{\tau,2}(T)\).
By Markov, profiles of total target mass at least
\((1/2-o(1))N_q\) have \(M_\tau\le2e^{A^2+o(1)}\).
Equation (3.16) and exponential-moment convergence then imply
\(C_\tau\le\log2-A^2+o(1)\) on those profiles. Applying (3.16) once
more and summing their target masses proves (3.18). \(\square\)

For arbitrary \(y\ge0\), the exact component inequalities give

\[
 \sum_X\max_{T\sim X}y_T
 \ge
 \sum_\kappa\max_\tau
       \sum_{T\in\tau}y_TR_{\tau\kappa}(T).
\tag{3.22}
\]

Averaging the maximum over the predecessor profiles recovers
\(\sum_Ty_TH_{\tau(T),2}(T)\). Theorem 3.4 proves that this uniform
averaging cannot establish QRE. It is not a Farkas countercut:
nonuniform capacities \(c_{\tau\kappa}\), with
\(\sum_\tau c_{\tau\kappa}\le1\), may still repair the Gaussian tail.
That nonuniform weighted allocation is the exact unresolved gate.

## 4. Quotient slack does not control raw congestion

### Proposition 4.1 (sharp abstract alignment cut)

For every integer \(k\ge2\) and fixed \(0<\eta<1\), there is a
two-level graph in which every used profile arc is \(k\)-expanding on
every raw subset, every full target profile sees its entire adjacent
owner profile, and the quotient flow has slack \(\eta\), but a raw Hall
cut has neighborhood ratio \(1/2\).

#### Proof

Take \(p=2k\) target profiles

\[
                         L_i=A_i\mathbin{\dot\cup}B_i,
 \qquad |A_i|=|B_i|=n.
\]

Take one owner profile \(R=C\mathbin{\dot\cup}D\), with

\[
 |R|=\left\lceil\frac{2pn}{1-\eta}\right\rceil,
 \qquad |C|=kn.
\]

Join \(A_i\) completely to \(C\) and \(B_i\) completely to \(D\).
Since \(|D|\ge kn\), every subset of one \(L_i\) expands by at least
\(k\), and \(N(L_i)=R\). Sending the full mass \(2n\) of each \(L_i\)
to \(R\) uses at most \((1-\eta)|R|\). Nevertheless

\[
 N\left(\mathop{\dot\bigcup}_{i=1}^{p}A_i\right)=C,
 \qquad
 |C|=\frac12\left|\mathop{\dot\bigcup}_{i=1}^{p}A_i\right|.
\]

\(\square\)

### Proposition 4.2 (literal constant-rank Hall cut)

Use one fixed perfect matching of the \(2m\) coordinates at every local
rank. For every fixed \(A>0\), at \(q=A\sqrt m+O(1)\), both maximal
compatibility graphs have a target family of \(\Omega_A(N_q)\) vertices
whose neighborhood has size at most

\[
                         e^{-A^2/3}|\mathcal A|.
\tag{4.1}
\]

#### Proof for the lower sign

For an exact set \(F\) of \(f\) full matching edges, let
\(\mathcal A_F\) be the rank-\(m-q\) targets with full-edge set \(F\),
and let \(\mathcal X_F\) be the middle sources with the same full-edge
set. Compatible promotion preserves \(F\), and

\[
\begin{aligned}
 |\mathcal A_F|
   &=\binom{m-f}{f+q}2^{m-q-2f},\\
 |\mathcal X_F|
   &=\binom{m-f}{f}2^{m-2f},\\
 \frac{|\mathcal X_F|}{|\mathcal A_F|}
   &=r_f
    =\prod_{i=1}^{q}\frac{2(f+i)}{m-2f-i+1}.
\end{aligned}
\tag{4.2}
\]

Moreover \(N(\mathcal A_F)=\mathcal X_F\), and distinct \(F\)'s give
disjoint components. Put

\[
                         f_0=\left\lfloor
                         \frac{m-2q}{4}+\frac q{16}
                         \right\rfloor.
\tag{4.3}
\]

The product \(r_f\) is increasing in \(f\). Uniformly at
\(f=f_0+O(1)\),

\[
                         \log r_f=-\frac{q^2}{2m}+o(1)
                                      =-\frac{A^2}{2}+o(1).
\tag{4.4}
\]

Indeed, after expanding about the common scale \(m/2\), the sum of the
numerator-minus-denominator displacements is
\(-q^2/4+O(q)\), and the total quadratic remainder is
\(O(q^3/m^2)=o(1)\). Thus \(r_f\le e^{-A^2/3}\) for all \(f\le f_0\)
and all large \(m\).

For a uniform rank-\(m-q\) target, its number \(\mathbf F\) of full
matching edges satisfies

\[
 \mathbb E\mathbf F=\frac{m-2q}{4}+O_A(1),
 \qquad \operatorname {Var}\mathbf F=O(m).
\tag{4.5}
\]

The variance follows from the slice Poincaré inequality. Since
\(f_0-\mathbb E\mathbf F=q/16+O_A(1)\), Cantelli's inequality gives
\(\Pr\{\mathbf F\le f_0\}\ge c_A>0\). Unioning the components with
\(|F|\le f_0\) proves (4.1). Complementation gives the upper sign.
\(\square\)

This is not a counterexample to independent-rank QRE. It proves that
rank diversity is essential and that the profile theorems cannot be
glued without weighted cross-profile control.

## 5. Common parallel selectors add only \(o(W)\) raw Hall loss

Let the retained owner cells be \(C\cong Q_{S_C}\), of total owner mass
\(G\), and assume \(H=o(R)\). In every cell choose a uniform \(R\)-set
\(A_C\) of its split axes and partition it into parallel \(Q_R\)-fibres.
Put

\[
 \rho_q=\frac{N_q}{W},\qquad
 \Lambda_q^\epsilon(T)
   =\sum_{X\sim_{\rm max}T}\frac1{\binom{S(X)}q}.
\tag{5.1}
\]

### Theorem 5.1 (simultaneous selected-axis Hall transfer)

There is one deterministic choice of all \(A_C\), common to every
\(q\le H\) and both signs, such that

\[
 \boxed{
 \sum_{q\le H,\epsilon}\operatorname {def}
       G_{q,{\rm sel}}^\epsilon
 \le
 \sum_{q\le H,\epsilon,T}
       (1-\rho_q\Lambda_q^\epsilon(T))_+
       +O(W/\sqrt R).}
\tag{5.2}
\]

#### Proof

A fixed target is a physical \(q\)-face of a fixed parent cell in at
most one way; write \(D_C(T)\) for its direction set. Define

\[
 Z_q^\epsilon(T)
 =\frac{\rho_q2^q}{\binom Rq}
 \sum_{C:T\text{ a }q\text{-face of }C}
       \mathbf1_{\{D_C(T)\subseteq A_C\}}.
\tag{5.3}
\]

Every surviving face contains \(2^q\) sources, while every selected
source has \(\binom Rq\) signed \(q\)-faces. Hence

\[
 \operatorname {def}G_{q,{\rm sel}}^\epsilon
 \le\sum_T(1-Z_q^\epsilon(T))_+.
\tag{5.4}
\]

The face-retention probability is
\(\binom Rq/\binom{S_C}q\), so

\[
 \mathbb EZ_q^\epsilon(T)=\rho_q\Lambda_q^\epsilon(T)=:\mu_T,
 \qquad
 \operatorname {Var}Z_q^\epsilon(T)
       \le a_q\mu_T,\quad
 a_q=\frac{\rho_q2^q}{\binom Rq}.
\tag{5.5}
\]

Independence is used only between parent cells. Cauchy--Schwarz and
\(\sum_T\mu_T=\rho_qG\le N_q\) give

\[
 \mathbb E\sum_T(1-Z_q^\epsilon(T))_+
 \le\sum_T(1-\rho_q\Lambda_q^\epsilon(T))_+
       +W\sqrt{a_q}.
\tag{5.6}
\]

Since

\[
 \frac{2^{q+1}/\binom R{q+1}}{2^q/\binom Rq}
 =\frac{2(q+1)}{R-q}=o(1),
\]

we have \(\sum_{q\le H}\sqrt{a_q}=O(R^{-1/2})\). Sum (5.6) over
the depths and signs and average over the common selectors. \(\square\)

If omitted cells have owner mass \(L\), their depthwise baseline loss is
already contained in the harmonic term through
\(\sum_T\rho_q\Lambda_q(T)=\rho_q(W-L)\). Thus \(L=o(W/H)\)
contributes only \(o(W)\) in total.

For exact floor alignment, put

\[
 g_q=\frac G{N_q},\qquad c_q=\lfloor g_q\rfloor,\qquad
 \widetilde Z_q^\epsilon(T)
 =\frac{d_q^\epsilon(T)}{\binom Rq},\qquad
 Z_q^{G,\epsilon}(T)=\frac{N_q}{G}\widetilde Z_q^\epsilon(T),
\tag{5.7}
\]

where \(d_q^\epsilon(T)\) is the selected owner-degree. Then
\(\sum_TZ_q^{G,\epsilon}(T)=N_q\), and the same edge count gives

\[
 \operatorname {def}_{c_q}G_{q,{\rm sel}}^\epsilon
 \le\sum_T(c_q-\widetilde Z_q^\epsilon(T))_+
 \le g_q\sum_T(1-Z_q^{G,\epsilon}(T))_+.
\tag{5.8}
\]

If pointwise

\[
                         c_q\le\widetilde Z_q^\epsilon(T)\le c_q+1,
\tag{5.9}
\]

the uniform edge flow \(1/\binom Rq\), followed by bipartite
integrality, gives an exact raw floor-balanced assignment.

At fixed \(q=A\sqrt m+O(1)\), \(g_q=e^{A^2+o(1)}=O_A(1)\). Across
\(H=\sqrt m\,\omega(m)\), however, \(g_q\) can reach
\(e^{\omega(m)^2+o(1)}\). A fixed-window raw estimate cannot be summed
into CPCR without the corresponding \(g_q\)-weighted control.

Theorem 5.1 is a raw face-support theorem. It does not realize one legal
compiler image.

## 6. Diverse-order simplification and the CPCR pair ledger

Use the legal-state definition in
MATH_EXACT_REMAINING_CROSS_PARENT_COMPILER_RESOLUTION_20260726.md.
For every packet \(P\), sign \(\epsilon\), and \(q\le H\), the
diverse-order compiler gives an injective literal image

\[
                         I_{P,q}^\epsilon,\qquad
                         |I_{P,q}^\epsilon|=|P|=2^R.
\tag{6.1}
\]

Sibling packets in one parent product cell have disjoint images. Hence
every repeated occurrence pair is cross-parent.

For one depth and sign, write

\[
 L(T)=\#\{P:T\in I_{P,q}^\epsilon\},\qquad
 G=cN+r,\quad 0\le r<N,
\tag{6.2}
\]

where \(N=N_q\), \(c=\lfloor G/N\rfloor\). Let

\[
                         C(L)=\sum_T\binom{L(T)}2.
\tag{6.3}
\]

### Theorem 6.1 (floor energy equals cross-parent collision excess)

For every legal resolution state,

\[
 \boxed{
 \sum_T(L(T)-c)(L(T)-c-1)
   =2\bigl(C(L)-C_{\min}\bigr),}
\tag{6.4}
\]

where

\[
                         C_{\min}=N\binom c2+cr.
\tag{6.5}
\]

The minimum is attained exactly at \(r\) loads \(c+1\) and \(N-r\)
loads \(c\). Every pair counted by \(C(L)\) is cross-parent.

#### Proof

Since \(\sum_TL(T)=G\),

\[
\begin{aligned}
 \sum_T(L-c)(L-c-1)
 &=2C(L)-2cG+c(c+1)N\\
 &=2C(L)-c(c-1)N-2cr\\
 &=2(C(L)-C_{\min}).
\end{aligned}
\]

Integer convexity of \(z\mapsto\binom z2\) gives the equality case.
Packet injectivity and sibling disjointness give the cross-parent
assertion. \(\square\)

Thus CPCR is exactly

\[
 \sum_{q\le H,\epsilon}
       \bigl(C(L_q^\epsilon)-C_{q,\min}\bigr)=o(W).
\tag{6.6}
\]

There is no separate within-packet, common-order, payload, or seam term
in (6.6), once the legality of the resolution state has been imposed.

## 7. Exact logical relation between QRE and CPCR

### Theorem 7.1 (exact raw floor dual)

Let a raw owner--target graph have \(G=cN+r\) owners, every owner being
required to choose one adjacent target. Put

\[
 \mathcal B=\{c\mathbf1+u:0\le u_T\le1,\ \sum_Tu_T=r\}.
\tag{7.1}
\]

The raw assignment polytope contains a load vector in \(\mathcal B\) if
and only if, for every real target array \(\lambda\),

\[
 \boxed{
 \sum_X\min_{T\sim X}\lambda_T
 \le c\sum_T\lambda_T
       +\sum_{\text{\(r\) largest }T}\lambda_T.}
\tag{7.2}
\]

In particular, for every \(y\ge0\), floor feasibility requires

\[
 \boxed{
 \sum_X\max_{T\sim X}y_T
 \ge c\sum_Ty_T
       +\sum_{\text{\(r\) smallest }T}y_T.}
\tag{7.3}
\]

#### Proof

The convex hull of raw load vectors is the Minkowski sum, over owners
\(X\), of the simplices
\(\operatorname {conv}\{e_T:T\sim X\}\). Its minimum against
\(\lambda\) is the left side of (7.2). The support function of
\(\mathcal B\) is the right side. The two compact convex sets intersect
if and only if no strict separating functional exists. Bipartite total
unimodularity makes a fractional intersection integral. Substitute
\(\lambda=-y\) to get (7.3). \(\square\)

Unit-demand QRE asks only for

\[
                         \sum_X\max_{T\sim X}y_T
 \ge(1-o(1))\sum_Ty_T.
\tag{7.4}
\]

It omits \(c_q\), \(r_q\), and the positive-\(\lambda\) upper-capacity
half of (7.2). Whole-compiler CPCR is stronger still because every
packet chooses one common option across all depths and signs.

For completeness, the corresponding whole-compiler mean-load dual is
also exact. Freeze a scaffold on which the remaining choices are
independent whole-packet option sets \(\Omega_P\). For
\(c=(q,\epsilon)\), let

\[
 v_{P,\omega}
 =\bigl(\mathbf1_{\{T\in I_{P,c}^{\omega}\}}\bigr)_{c,T},
\qquad
 \mathcal B_c
 =\{c_q\mathbf1+u:0\le u_T\le1,\ \sum_Tu_T=r_q\},
\tag{7.5}
\]

and put \(\mathcal B=\prod_c\mathcal B_c\).

### Theorem 7.2 (whole-compiler mean floor dual)

A fractional choice of one option in every \(\Omega_P\) has mean load
in \(\mathcal B\) if and only if, for every real all-depth signed array
\(\lambda=(\lambda_{c,T})\),

\[
 \boxed{
 \sum_P\min_{\omega\in\Omega_P}
       \langle\lambda,v_{P,\omega}\rangle
 \le
 \sum_c\left(
 c_q\sum_T\lambda_{c,T}
 +\sum_{\text{\(r_q\) largest }T}\lambda_{c,T}
 \right).}
\tag{7.6}
\]

All depths and signs occur inside the same packetwise minimum.

#### Proof

The convex hull of mean compiler loads is the Minkowski sum
\(\sum_P\operatorname {conv}\{v_{P,\omega}:\omega\in\Omega_P\}\).
Its minimum against \(\lambda\) is the left side of (7.6). The support
function of \(\mathcal B\) is the right side. Separation proves the
equivalence. \(\square\)

If a slab trade couples several packets, those packets must be replaced
in (7.6) by one joint choice group. Treating them independently would
enlarge the legal polytope and is invalid.

Mean feasibility is not CPCR. If independent packet choices have an
integral balanced mean \(b_c(T)\in\{c_q,c_q+1\}\), then

\[
 \mathbb E\Phi
 =\sum_{c,T}\operatorname {Var}L_c(T)
 =\sum_{c,P,T}p_{P,c,T}(1-p_{P,c,T}).
\tag{7.7}
\]

Thus balanced mean together with the \(o(W)\) variance bound in (7.7)
is sufficient. In general, the exact remaining condition is the
cross-parent pair-covariance bound (6.6), not the mean dual (7.6).

### Proposition 7.3

CPCR gives \(o(W)\) aggregate missing targets and hence a raw
near-injection in its actual legal trace graphs. Raw QRE, even at every
fixed \(A\), does not by itself imply CPCR.

#### Proof

Put

\[
 D=\sum_T(c-L(T))_+,\qquad
 U=\sum_T(L(T)-c-1)_+.
\]

Writing \(D_T=(c-L(T))_+\) and
\(U_T=(L(T)-c-1)_+\), pointwise

\[
                         (L-c)(L-c-1)\ge2(D_T+U_T).
\tag{7.8}
\]

Thus CPCR gives \(\sum_{q,\epsilon}(D+U)=o(W)\). Since \(c_q\ge1\)
on the protected central band, every missing target contributes to
\(D\). Choose one occurrence of each nonmissing target; packetwise
injectivity and owner-disjoint packets give distinct starting owners.

Conversely, Hall controls support, not \(C(L)\). At the abstract load
level with \(G=2N\), the vector with load one on \(N/2\) targets and
load three on \(N/2\) targets has full support and admits an injection,
but its floor energy is \(N\). Therefore support Hall cannot imply CPCR
without a grouped covariance theorem. \(\square\)

The valid implication chain is therefore

\[
\text{CPCR}
\Longrightarrow
\text{near floor-balanced raw assignment}
\Longrightarrow
\text{unit raw Hall after \(o(W)\) quarantine},
\tag{7.9}
\]

while neither reverse implication is available.

## 8. Proved and unproved boundary

Unconditional:

1. weighted within-profile expansion by \(K_q=(3/2)^q\), after total
   \(o(N_q)\) quarantine, for both signs;
2. the profile-spreading/congestion theorem (3.2)--(3.5);
3. exclusion of every Hall countercut supported on fewer than \(K_q\)
   profiles;
4. the sharp predecessor-profile entropy and typical-owner visibility
   theorem (3.8)--(3.13);
5. the simultaneous parallel-selector transfer (5.2);
6. a literal linear Hall cut for constant-in-rank matchings, proving
   rank diversity essential;
7. the exact raw and whole-compiler floor duals (7.2), (7.6); and
8. the exact cross-parent CPCR collision identity (6.4).

Not proved:

1. (3.6), the weighted allocation-score inequality, or an equivalent
   common-source theorem for one independent-rank realization;
2. the Uniform Saddle Lemma needed to make the Gaussian deficit
   (3.18) unconditional;
3. global independent-rank QRE_A;
4. compiler-image realization of an ungrouped raw matching;
5. common all-depth cross-parent covariance cancellation; or
6. CPCR and coefficient one.

The smallest raw obstruction is adversarial weighted alignment of
exponentially many ordered-profile components on common sources. The
smallest final obstruction is stronger and exactly (6.6): construct one
legal resolution whose cross-parent collision count is integer-minimal
up to \(o(W)\), simultaneously at every protected depth and both signs.
