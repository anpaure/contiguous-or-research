# Lane J: exact degree-two augmentation at the constant-one scale

Date: 2026-07-25

Method: pure mathematics only. No Python, SAT solver, web or literature
search, finite search, or long computation was used.

## 0. Outcome

This report does not prove the constant-one theorem. It proves a
target-scale integral augmentation theorem which removes two previously
separate losses inside an explicit genuine circuit chart:

1. every point of the continuous MSW two-switch cube rounds to one literal
   exact factor with floor-energy loss \(O(H\operatorname{Cat}_m)\);
2. greedy, always-applicable degree-two descent from any cube vertex ends
   within \(O(H\operatorname{Cat}_m)\) of the continuous cube optimum.

The exact constants are proved below. Therefore a continuous
\(O(H\operatorname{Cat}_m)\) point in this explicit cube would already
imply

\[
\nu(k)\le(1+o(1))W(k).
\]

No further integer selector, common completion, Markov connectivity, or
rounding lemma would be needed.

The report also proves two obstructions.

- A hereditary family of \(\operatorname{Cat}_{m-4}\) first-shadow holes
  is frozen throughout this degree-two cube. This forbids exact balance but
  costs only \(O(\operatorname{Cat}_m)\), below the allowed
  \(O(H\operatorname{Cat}_m)\) scale.
- On even \(m\), the known universal two-for-two circuits preserve an
  all-rank-invisible sign census. They therefore cannot be a whole-fibre
  Markov basis or define a unique energy normal form. Census-changing
  circuits are necessary for global connectivity.

The only remaining positive assertion for this chart is an explicit
continuous energy estimate, denoted \(\mathrm{FCE}_A\) in Section 5 and
marked **UNPROVED**.

## 1. Fixed-window floor energy

Put

\[
m\ge4,\qquad n=2m+1,\qquad
W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn.
\]

For \(1\le q\le H\le m-2\), put

\[
N_q=\binom n{m-q},
\qquad
W=c_qN_q+r_q,
\qquad
0\le r_q<N_q,
\tag{1.1}
\]

and

\[
\beta_q=\frac{r_q(N_q-r_q)}{N_q}.
\tag{1.2}
\]

For a genuine exact wreath factor \(F\), let

\[
\mu_q(F)=B_{m-q}\mathbf1_F,
\qquad
f_q(F)=\mu_q(F)-\frac W{N_q}\mathbf1.
\tag{1.3}
\]

Define the twice-half floor energy

\[
\begin{aligned}
Q_q(F)
&=
\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)\\
&=
\|f_q(F)\|_2^2-\beta_q,
\end{aligned}
\tag{1.4}
\]

and

\[
\mathcal Q_H(F)
=\sum_{q=1}^H\frac{Q_q(F)}{c_q},
\qquad
\Psi_H(F)=\frac12\mathcal Q_H(F).
\tag{1.5}
\]

At an integral load every summand in the first line of (1.4) is
nonnegative. If

\[
O_q(F)
=
\max\left\{
\sum_S(c_q-\mu_q(S))_+,
\sum_S(\mu_q(S)-c_q-1)_+
\right\},
\tag{1.6}
\]

then a deficit \(d\) or surplus \(e\) contributes respectively
\(d(d+1)\ge2d\) or \(e(e+1)\ge2e\). Hence

\[
\boxed{
\sum_{q=1}^H\frac{O_q(F)}{c_q}
\le\Psi_H(F)=\frac12\mathcal Q_H(F).}
\tag{1.7}
\]

For \(H=\lceil A\sqrt m\rceil\), all \(c_q\) are bounded above by a
constant depending only on \(A\).

## 2. Conflict-free universal circuit cubes

A universal two-for-two circuit has the four-order form

\[
\begin{aligned}
C&=(\delta,\gamma,E,\beta,\alpha,O),\\
D&=(\beta,\delta,E,\alpha,\gamma,O),\\
C'&=(\delta,\beta,E,\gamma,\alpha,O),\\
D'&=(\gamma,\delta,E,\alpha,\beta,O),
\end{aligned}
\tag{2.1}
\]

where the four displayed labels are distinct and the ordered lists \(E,O\)
partition the other labels with

\[
|E|=m-1,\qquad |O|=m-2.
\]

Put

\[
g=e_{C'}+e_{D'}-e_C-e_D.
\tag{2.2}
\]

For a core \(K\) avoiding \(\beta,\gamma\), write

\[
\partial K=e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}}.
\]

For an ordered list \(L\), \(\operatorname{pre}_sL\) and
\(\operatorname{suf}_sL\) denote its first and last \(s\) labels.

### Lemma 2.0 (exact four-letter cut profile)

The vector \(g\) is a genuine middle trade: \(B_mg=0\), and each of its
two signs is a middle packing. For \(2\le r\le m-1\),

\[
B_rg
=
\partial\operatorname{suf}_{r-1}O
+\partial\operatorname{suf}_{r-1}E
-\partial\operatorname{pre}_{r-1}E
-\partial\operatorname{pre}_{r-1}O.
\tag{2.3}
\]

Consequently

\[
\boxed{
\|B_{m-1}g\|_2^2=4,
\qquad
\|B_{m-q}g\|_2^2=8\quad(2\le q\le m-2).}
\tag{2.4}
\]

#### Proof

This is the universal cut identity established in
`MSW_MULTIRANK_LOCAL_TRADES.md`; the verification is included here.
Compare the four displayed cyclic words after cutting immediately before
each exceptional letter. An \(r\)-interval wholly inside \(E\) or wholly
inside \(O\) occurs with the same signed multiplicity on both sides. The
same cancellation holds for an interval crossing a cut but containing
either both or neither of \(\beta,\gamma\). The only survivors contain
exactly one of these two letters. At the four cuts adjacent to \(O,E,E,O\),
their old-minus-new cores are respectively

\[
\operatorname{suf}_{r-1}O,\quad
\operatorname{suf}_{r-1}E,\quad
\operatorname{pre}_{r-1}E,\quad
\operatorname{pre}_{r-1}O,
\]

with signs \(+,+,-,-\). This is exactly (2.3). The identical cut check at
\(r=m\) has no survivors, so \(B_mg=0\); inspecting the two rows on either
side during that check also shows that no middle target occurs twice on
one side. Thus both signs are middle packings.

For \(2\le r\le m-2\), the four ordered-list cores in (2.3) are distinct,
and adjoining \(\beta\) or \(\gamma\) gives eight distinct coordinates,
each with coefficient \(1\) or \(-1\). Thus the squared norm is eight.
For \(r=m-1\), the two \(O\)-cores are both all of \(O\) and cancel; the
two distinct \(E\)-cores give four distinct unit coefficients. This proves
(2.4). \(\square\)

Whenever \(C,D\) lie in one exact factor, the trade is applicable.

Let \(F\) be an exact factor. A conflict-free universal atlas based at
\(F\) is a family \(\mathscr J\) of applicable circuits (2.2) whose
negative pairs are pairwise disjoint subsets of \(F\). Write
\(d=|\mathscr J|\).

### Lemma 2.1 (a conflict-free atlas is an exact Boolean cube)

For every \(\varepsilon\in\{0,1\}^{\mathscr J}\),

\[
F_\varepsilon
=
F+\sum_{j\in\mathscr J}\varepsilon_jg_j
\tag{2.5}
\]

is a genuine exact factor. For every
\(t\in[0,1]^{\mathscr J}\),

\[
x(t)
=
\mathbf1_F+\sum_{j\in\mathscr J}t_jg_j
\tag{2.6}
\]

is a nonnegative fractional exact factor:

\[
B_mx(t)=\mathbf1.
\tag{2.7}
\]

Moreover \(d\le B/2\).

#### Proof

The negative rows of different circuits lie in the exact factor \(F\), so
their middle-target sets are disjoint. For each circuit, its positive pair
covers exactly the same middle-target set as its negative pair. Therefore
positive pairs belonging to different circuits are also middle-disjoint
from one another and from every untouched row of \(F\). Any independent
choice of old or new pair consequently covers every middle target exactly
once, proving (2.5).

Equation (2.6) is the coordinatewise convex interpolation in this product
cube. Every old coefficient is \(1-t_j\), every replacement coefficient is
\(t_j\), and untouched coefficients remain one, proving nonnegativity and
(2.7). Finally every circuit consumes two distinct rows of \(F\), so
\(2d\le|F|=B\). \(\square\)

Extend \(\mathcal Q_H\) and \(\Psi_H\) to the real cube (2.6) by the
quadratic formulas (1.3)--(1.5). Denote the extensions by
\(\widetilde{\mathcal Q}_H\) and \(\widetilde\Psi_H\).

Equip stacked lower-load space with

\[
\|z\|_H^2
=
\sum_{q=1}^H\frac{\|B_{m-q}z\|_2^2}{c_q}.
\tag{2.8}
\]

By (2.4), every coordinate circuit has the same squared profile

\[
\alpha_H
=
\frac4{c_1}
+8\sum_{q=2}^H\frac1{c_q}
\le8H-4.
\tag{2.9}
\]

Put

\[
D_H(\mathscr J)=d\alpha_H.
\tag{2.10}
\]

Since \(d\le B/2\),

\[
\boxed{
D_H(\mathscr J)\le(4H-2)B.}
\tag{2.11}
\]

## 3. Exact integral rounding

### Theorem 3.1 (target-scale Bernoulli rounding)

For every \(t\in[0,1]^{\mathscr J}\), there is an integral cube vertex
\(F_\varepsilon\) such that

\[
\boxed{
\mathcal Q_H(F_\varepsilon)
\le
\widetilde{\mathcal Q}_H(x(t))
+\frac14D_H(\mathscr J)}
\tag{3.1}
\]

and

\[
\boxed{
\Psi_H(F_\varepsilon)
\le
\widetilde\Psi_H(x(t))
+\frac18D_H(\mathscr J).}
\tag{3.2}
\]

In particular, the rounding losses are at most

\[
\left(H-\frac12\right)B
\quad\text{and}\quad
\left(\frac H2-\frac14\right)B,
\tag{3.3}
\]

respectively.

#### Proof

Choose independent Bernoulli variables \(X_j\) with
\(\mathbb EX_j=t_j\). Every outcome \(F_X\) is an integral exact factor by
Lemma 2.1. Its mean load is the load of \(x(t)\).

The floor correction \(-\sum_q\beta_q/c_q\) in
\(\widetilde{\mathcal Q}_H\) is constant. Orthogonality of independent
centered Bernoulli variables therefore gives the exact identity

\[
\mathbb E\mathcal Q_H(F_X)
=
\widetilde{\mathcal Q}_H(x(t))
+\sum_{j\in\mathscr J}
t_j(1-t_j)\|g_j\|_H^2.
\tag{3.4}
\]

Use \(t_j(1-t_j)\le1/4\) and
\(\|g_j\|_H^2=\alpha_H\). Some outcome is no larger than the expectation,
which proves (3.1). Division by two proves (3.2), and (2.11) gives (3.3).
\(\square\)

There is no hidden multicover or signed selector in this theorem. The
selected outcome is one squarefree exact factor, and every circuit is an
actual two-for-two replacement inside that factor cube.

## 4. Monotone degree-two augmentation

### Theorem 4.1 (local minima approximate the continuous cube optimum)

Let \(F_*\) be a vertex of the cube (2.5) which is locally minimal under
all individual coordinate switches. Then

\[
\boxed{
\mathcal Q_H(F_*)
\le
\min_{t\in[0,1]^{\mathscr J}}
\widetilde{\mathcal Q}_H(x(t))
+D_H(\mathscr J)}
\tag{4.1}
\]

and

\[
\boxed{
\Psi_H(F_*)
\le
\min_{t\in[0,1]^{\mathscr J}}
\widetilde\Psi_H(x(t))
+\frac12D_H(\mathscr J).}
\tag{4.2}
\]

If a cube vertex violates (4.1), one individual applicable degree-two
switch strictly decreases \(\mathcal Q_H\), equivalently \(\Psi_H\).
Consequently greedy strict coordinate descent terminates at a vertex
satisfying (4.1)--(4.2), and every intermediate state is a literal exact
factor.

#### Proof

At an arbitrary cube vertex \(F'\), orient \(h_j\) to be the coordinate
flip away from \(F'\). Thus \(h_j=g_j\) or \(-g_j\), and

\[
\|h_j\|_H^2=\alpha_H.
\]

Let \(f=(f_q(F'))_{q\le H}\). Local minimality says

\[
\begin{aligned}
0
&\le
\mathcal Q_H(F'+h_j)-\mathcal Q_H(F')\\
&=
2\langle f,h_j\rangle_H+\alpha_H,
\end{aligned}
\tag{4.3}
\]

so

\[
2\langle f,h_j\rangle_H\ge-\alpha_H.
\tag{4.4}
\]

Every point of the same real cube has a unique representation

\[
F'+\sum_j u_jh_j,
\qquad 0\le u_j\le1.
\]

Quadratic expansion and (4.4) give

\[
\begin{aligned}
\widetilde{\mathcal Q}_H
\left(F'+\sum_ju_jh_j\right)-\mathcal Q_H(F')
&=
2\sum_ju_j\langle f,h_j\rangle_H
+\left\|\sum_ju_jh_j\right\|_H^2\\
&\ge
-\alpha_H\sum_ju_j\\
&\ge-D_H(\mathscr J).
\end{aligned}
\tag{4.5}
\]

Minimizing the left side proves (4.1), and division by two gives (4.2).
The contrapositive proves the strict-improvement assertion. Finiteness of
the cube makes greedy strict descent terminate. \(\square\)

For fixed \(A\), choose an integer \(K_A\) with \(c_q\le K_A\) throughout
the window. Vertex energies lie in \(L_A^{-1}\mathbb Z_{\ge0}\), where

\[
L_A=\operatorname{lcm}(1,2,\ldots,K_A).
\]

Thus every strict step decreases energy by at least \(1/L_A\); one may
bound the number of steps by
\(L_A\mathcal Q_H(F_{\mathrm{start}})\). No path-length bound is needed for
the existential result.

### Corollary 4.2 (explicit canonical MSW degree-two cube)

Let \(F_m^{\mathrm{MSW}}\) be the canonical MSW factor and
\(\tau=(2\ 3)\). Its \(j=0\) ownership stratum supplies

\[
d_0=\operatorname{Cat}_{m-2}
\tag{4.6}
\]

independent applicable degree-two circuits, indexed by
\(R\in\mathcal D_{m-2}\). For this cube,

\[
\boxed{
D_H^{(0)}
=
\operatorname{Cat}_{m-2}
\left(
\frac4{c_1}
+8\sum_{q=2}^H\frac1{c_q}
\right)
\le(8H-4)\operatorname{Cat}_{m-2}.}
\tag{4.7}
\]

Therefore Bernoulli rounding loses at most \(D_H^{(0)}/4\), and greedy
degree-two descent terminates within \(D_H^{(0)}\) of the continuous
minimum. Since

\[
\frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
\longrightarrow\frac1{16},
\tag{4.8}
\]

for \(H=O(\sqrt m)\) one has

\[
D_H^{(0)}
\le\left(\frac12+o(1)\right)H\operatorname{Cat}_m.
\tag{4.9}
\]

Thus the full-energy Bernoulli toll is at most
\((1/8+o(1))H\operatorname{Cat}_m\), and the singleton-local-minimum gap
is at most \((1/2+o(1))H\operatorname{Cat}_m\), with no hidden dependence
on the number of lower-rank targets.

The same conclusion holds for every fixed contextual family

\[
P1100R\longleftrightarrow P1010R
\]

at one Dyck boundary \(p\): it contains

\[
\operatorname{Cat}_p\operatorname{Cat}_{m-p-2}
\]

independent degree-two coordinates, each with the profile (2.3).

## 5. Exact implication to constant one

For fixed \(A>0\), put

\[
H_A=\lceil A\sqrt m\rceil.
\]

The remaining continuous assertion for the explicit \(j=0\) cube is:

> **\(\mathrm{FCE}_A\) -- UNPROVED.** There is \(C_A<\infty\) such that,
> for all sufficiently large \(m\),
> \[
> \min_{t\in[0,1]^{\operatorname{Cat}_{m-2}}}
> \widetilde{\mathcal Q}_{H_A}
> \left(
> \mathbf1_{F_m^{\mathrm{MSW}}}
> +\sum_{R\in\mathcal D_{m-2}}t_Rg_R
> \right)
> \le C_AH_A\operatorname{Cat}_m.
> \tag{5.1}
> \]

### Theorem 5.1 (quantitative composition)

If \(\mathrm{FCE}_A\) holds for every fixed \(A\), then

\[
\boxed{\nu(k)\le(1+o(1))W(k).}
\tag{5.2}
\]

#### Proof

Apply Theorem 3.1 to a continuous point satisfying (5.1), or apply Theorem
4.1 after greedy exact descent. Equation (4.7) gives one genuine exact
factor \(F_A\) with

\[
\mathcal Q_{H_A}(F_A)
=O_A(H_A\operatorname{Cat}_m).
\tag{5.3}
\]

By (1.7),

\[
\sum_{q\le H_A}\frac{O_q(F_A)}{c_q}
=O_A(H_A\operatorname{Cat}_m).
\tag{5.4}
\]

Since \(W=n\operatorname{Cat}_m\),

\[
\frac{H_A\operatorname{Cat}_m}{W}
=\frac{H_A}{n}
=O_A(m^{-1/2})
=o(1).
\tag{5.5}
\]

Thus the fixed-window overload optimum is \(o(W)\) for every fixed \(A\).
The audited diagonalization chooses \(A=A(m)\to\infty\) slowly, giving the
overload form of MWB on a tail-killing window.

Every factor produced above is integral and exact. The audited exact
overload ledger and simultaneous integral nested deletion-flow theorem
therefore give a literal contiguous-OR word with central contribution
\(W+o(W)\). The factor-independent deep tail is \(o(W)\), and the standard
trimmed one-bit lift transfers the odd-dimensional result to all \(k\).
This proves (5.2). \(\square\)

This implication is unlabelled. It does not assert the stronger
common-owner synchronization theorem, and no false equivalence between
unlabelled histogram distance and a nearby labelled nested flow is used.

Theorem 5.1 shows exactly what has been achieved: integrality, common
applicability, bounded circuit support, monotone exact augmentation, and
the final constant-one ledger introduce only
\(O(H_A\operatorname{Cat}_m)\) loss. Only (5.1) remains for this chart.

## 6. A frozen hereditary obstruction inside the cube

The continuous criterion (5.1) cannot ask for perfect balance. A genuine
family of first-shadow holes is invariant throughout the entire \(j=0\)
cube.

Let

\[
T(V)=11101101\,V,
\qquad
V\in\mathcal D_{m-4},
\tag{6.1}
\]

be the established hereditary upper MSW holes, and let

\[
S(V)=\{n\}\cup([2m]\setminus T(V))
\tag{6.2}
\]

be their complementary lower rank-\((m-1)\) targets.

### Proposition 6.1 (persistent first-shadow holes)

For every \(R\in\mathcal D_{m-2}\) and
\(V\in\mathcal D_{m-4}\),

\[
B_{m-1}g_R(S(V))=0.
\tag{6.3}
\]

Consequently every integral or fractional point of the \(j=0\) cube has
load zero at all \(\operatorname{Cat}_{m-4}\) targets \(S(V)\). At every
integral cube vertex \(F_\varepsilon\),

\[
\boxed{
\mathcal Q_H(F_\varepsilon)
\ge
Q_1(F_\varepsilon)
\ge2\operatorname{Cat}_{m-4}}
\tag{6.4}
\]

and at every fractional point the displayed hole coordinates themselves
contribute exactly \(2\operatorname{Cat}_{m-4}\) to the rank-one floor
polynomial.

#### Proof

The exact first-shadow square of \(g_R\) has two targets omitting \(n\), and
two targets containing \(n\) together with respectively the label \(2\) or
the label \(3\). The fixed word \(11101101\) has ones in positions \(2\)
and \(3\). Therefore \(S(V)\) contains \(n\) but contains neither \(2\) nor
\(3\), so it lies outside every square support. This proves (6.3).

The targets (6.2) are holes of the starting MSW factor, hence their loads
remain zero throughout the real cube. Since \(c_1=1\), a zero load
contributes

\[
(0-1)(0-2)=2
\]

to \(Q_1\). Summing proves (6.4). \(\square\)

For a fractional point, other coordinates with loads strictly between one
and two can contribute negatively to the floor polynomial. Thus (6.4) is
asserted only for integral vertices; no false nonnegativity of the
fractional extension is used.

Because

\[
\operatorname{Cat}_{m-4}
=\left(\frac1{256}+o(1)\right)\operatorname{Cat}_m,
\]

this obstruction is only \(O(\operatorname{Cat}_m)\). It rules out exact
rank-one balance but remains smaller by a factor of order \(H_A\) than the
allowed target in (5.1). It is therefore not a counterexample to
\(\mathrm{FCE}_A\).

## 7. Definitive no-go for a universal-circuit whole-fibre normal form

The full proof is given in
MATH_ATTACK_J_UNIVERSAL_CIRCUIT_PARITY_NO_GO_20260725.md. We record the
theorem and its short algebraic core because it fixes the scope of the
augmentation result.

Assume \(m\ge4\) is even. Fix one unoriented cyclic order \(C_0\). If
\(C=\sigma C_0\), define

\[
\epsilon(C)=\operatorname{sgn}(\sigma).
\tag{7.1}
\]

This is well-defined because the dihedral stabilizer \(D_{2m+1}\) is
contained in the alternating group: rotations of odd length are even and a
reflection has sign \((-1)^m=1\).

### Theorem 7.1 (all-rank parity kernel and circuit census)

The sign vector satisfies

\[
\boxed{
B_r\epsilon=0
\qquad(0\le r\le n).}
\tag{7.2}
\]

Every universal circuit (2.2) preserves

\[
N_-(F)=|\{C\in F:\epsilon(C)=-1\}|.
\tag{7.3}
\]

Nevertheless there are genuine exact factors \(G\) and \(\pi G\), with
\(\pi\) a coordinate transposition, such that

\[
\boxed{
|N_-(\pi G)-N_-(G)|
\ge\operatorname{Cat}_{m-3}
=\left(\frac1{64}+o(1)\right)B,}
\tag{7.4}
\]

while their lower-load vectors differ only by coordinate permutation at
every rank. Hence all coordinate-symmetric floor energies and overloads
have exactly equal values at the two factors.

#### Proof

Fix an \(r\)-set \(S\), \(1\le r\le n-1\). At least one of \(S,S^c\)
contains two labels; transpose two labels within that part. This odd
permutation fixes \(S\), pairs all cyclic orders in which \(S\) is an
\(r\)-interval, and reverses \(\epsilon\). It has no fixed cyclic order
because a single transposition is not a nonidentity element of the odd
dihedral stabilizer. The row sum is therefore zero. The cases \(r=0,n\)
follow because the two sign classes have equal size. This proves (7.2).

For (2.1), the common transposition
\(\rho=(\beta\ \gamma)\) sends \(C,D\) to \(C',D'\). Relative to \(C\), the
position word of \(D\) has

\[
(m+1)+(m-1)+1=2m+1
\]

inversions, so \(C,D\) have opposite signs. The new pair also contains one
of each sign, proving census conservation.

By the established exact MSW component hierarchy, the \(j=1\) stratum has
\(\operatorname{Cat}_{m-3}\) independent three-for-three components, and
the right side of each component is the transposition image of its
three-row left side. If the left side has \(a\) negative rows, its right
side has \(3-a\), so switching the component changes the census by the
nonzero odd number \(3-2a\). Choose all smaller-census sides, then all
larger-census sides.
The resulting exact factors have census gap at least
\(\operatorname{Cat}_{m-3}\); one is at distance at least half this gap
from \(B/2\). Applying any odd coordinate permutation to that factor
reverses every sign, proving (7.4). Incidence equivariance gives equality
of all symmetric energy values. \(\square\)

There is an even stronger semigroup statement. If \(A_n\) is the
alternating group and

\[
X_G=\sum_{\sigma\in A_n}\mathbf1_{\sigma G},
\qquad
X_{\pi G}=\sum_{\sigma\in A_n}\mathbf1_{\sigma\pi G},
\]

then

\[
X_G-X_{\pi G}
=2n\bigl(B-2N_-(G)\bigr)\epsilon.
\tag{7.5}
\]

Indeed, \(A_n\) is transitive on each sign class and the stabilizer of a
cyclic order has size \(2n\). Hence the coefficient of a positive
respectively negative order in \(X_G\) is
\(2n(B-N_-(G))\) respectively \(2nN_-(G)\). The odd permutation \(\pi\)
interchanges these two coefficients, and subtraction gives (7.5).

Both sides are explicitly decomposed sums of genuine exact factors, their
loads agree at every rank by (7.2), and their difference is outside the
integer lattice generated by the universal circuits because that lattice
is killed by the census functional.

Thus the universal circuits cannot characterize or connect the whole
exact-factor fibre, even after every lower rank is observed. This is a
definitive method no-go. It does not contradict Theorems 3.1--4.1, which
operate inside one explicit census class, and it does not prove that the
continuous optimum in (5.1) is large.

## 8. Adversarial audit and exact remaining statement

1. **What is proved.** The rounding identity (3.4), local-minimum inequality
   (4.5), and exact norm profile (2.4) show that all integrality and
   monotone-augmentation losses in the explicit degree-two cube are
   \(O(HB)\). Every step is an applicable two-for-two trade and every state
   is one exact factor.

2. **What is not proved.** No estimate in this report upper-bounds the
   continuous minimum in (5.1). Signed lattice saturation does not imply
   (5.1), because its degree-two labels are based at different exact
   factors and need not form one nonnegative cube.

3. **Fractional does not mean nonphysical rounding.** The real point
   \(x(t)\) is used only as an analytic certificate. Theorem 3.1 immediately
   replaces it by a genuine integral exact factor with target-scale loss.

4. **The parity obstruction has exact scope.** Census conservation is
   proved for the known relabelled universal family, not for every possible
   degree-two wreath trade. Degree-three census-changing components exist
   in the MSW factor.

5. **Persistent holes do not refute constant one.** Proposition 6.1 gives
   only \(\Theta(B)\) forced energy, while the allowable error is
\(\Theta(HB)\) with \(H\asymp\sqrt m\).

6. **No labelled overclaim.** The final implication uses overload MWB and
   the audited integral deletion-flow/word construction. It does not infer
   a common labelled owner resolution from small unlabelled histogram
   distance.

## 9. Immutable-hole test for the continuous criterion

### Theorem 9.1 (immutable-hole lower bound for the continuous optimum)

Let \(M_q^{\mathrm{MSW}}\) be the number of rank-\((m-q)\) targets missed
by the canonical MSW factor. Put

\[
a_1=4,\qquad a_q=8\quad(q\ge2),
\qquad d_0=\operatorname{Cat}_{m-2},
\tag{9.1}
\]

and

\[
L_H
=
\sum_{q=1}^H
(c_q+1)
\bigl(M_q^{\mathrm{MSW}}-a_qd_0\bigr)_+.
\tag{9.2}
\]

Then every integral vertex of the \(j=0\) cube satisfies

\[
\boxed{\mathcal Q_H(F_\varepsilon)\ge L_H,}
\tag{9.3}
\]

and its continuous optimum satisfies

\[
\boxed{
\min_t\widetilde{\mathcal Q}_H(x(t))
\ge
L_H-\frac14D_H^{(0)}.}
\tag{9.4}
\]

Consequently \(\mathrm{FCE}_A\) can hold only if

\[
\boxed{
L_{H_A}=O_A(H_A\operatorname{Cat}_m).}
\tag{9.5}
\]

In particular it requires

\[
M_1^{\mathrm{MSW}}
=O_A(H_A\operatorname{Cat}_m)
=O_A(W/\sqrt m).
\tag{9.6}
\]

#### Proof

Let \(U_q\) be the union of rank-\((m-q)\) coordinates touched by the
effects of all \(d_0\) cube generators. The exact norm profile (2.4)
also gives their support sizes, so

\[
|U_q|\le a_qd_0.
\tag{9.7}
\]

Every load coordinate outside \(U_q\) is frozen throughout the whole cube.
At least \((M_q^{\mathrm{MSW}}-a_qd_0)_+\) canonical holes therefore remain
holes at every integral vertex. A zero load contributes

\[
(0-c_q)(0-c_q-1)=c_q(c_q+1)
\]

to \(Q_q\), hence \(c_q+1\) after division by \(c_q\). All other integral
contributions are nonnegative, proving (9.3).

For arbitrary \(t\), Theorem 3.1 supplies an integral vertex with

\[
\mathcal Q_H(F_\varepsilon)
\le
\widetilde{\mathcal Q}_H(x(t))+\frac14D_H^{(0)}.
\]

Combine this with (9.3) and minimize over \(t\) to obtain (9.4).
Equations (5.1) and (4.7) then imply (9.5). At \(q=1\),
\(a_1d_0=4\operatorname{Cat}_{m-2}=O(B)\), while
\(H_AB\gg B\), so (9.6) follows. \(\square\)

This is the strongest rigorous obstruction currently available for the
continuous cube criterion. It would definitively refute this chart if one
proved

\[
M_1^{\mathrm{MSW}}
=\omega(H_A\operatorname{Cat}_m)
\]

by a pure all-dimensional argument. No such lower bound is presently
proved; finite data are not used here.

The smallest remaining statement in this lane is precisely the continuous
inequality (5.1). If it is true, Theorems 3.1 and 5.1 give the complete
constant-one theorem with literal contiguous-OR realizability. If it is
false, any counterexample must have continuous energy
\(\omega(H\operatorname{Cat}_m)\) despite all
\(\operatorname{Cat}_{m-2}\) exact four-arm selector directions; the
\(\operatorname{Cat}_{m-4}\) frozen holes are too small to provide such a
counterexample.
