# Second-wave AC: Graver suspension, positive thinning, and the exact obstruction

Date: 2026-07-24

No web search, finite search, or computational experiment is used in this report.  The explicit (m=4) circuit and its already proved three-target pointing obstruction are taken as certified mathematical inputs.  Every new argument below is symbolic.

## 1. Verdict

Let (B_r) be the rank-(r) cyclic-interval incidence map on cyclic orders of ([2m+1]).  The certified (m=4) nonlocal factor edge

\[
 w_4=\mathbf 1_{P_4}-\mathbf 1_{N_4}
\]

is a connected four-for-four exact-factor circuit with

\[
B_4w_4=B_3w_4=0,
\qquad
B_2w_4\ne0.
\tag{1.1}
\]

The second-wave conclusions are as follows.

1. **There is an exact all-dimensional signed suspension.**  If (P_j) is the antipodal all-pointings operator from dimension (j) to (j+1), then

   \[
   z_M=P_{M-1}\cdots P_4w_4
   \]

   is squarefree and satisfies, for every \(M\ge4\),

   \[
   B_Mz_M=B_{M-1}z_M=0,
   \qquad
   B_{M-2}z_M\ne0.
   \tag{1.2}
   \]

   Its support and surviving coefficient are explicit:

   \[
   |z_M^+|=|z_M^-|
   =4\prod_{j=4}^{M-1}(2j+1),
   \tag{1.3}
   \]

   and the old (B_2w_4) effect is multiplied by

   \[
   \prod_{j=4}^{M-1}(j-1)=\frac{(M-2)!}{2}.
   \tag{1.4}
   \]

   A conformal decomposition therefore produces, in every dimension, a squarefree Graver element of the **stacked** matrix

   \[
   \binom{B_M}{B_{M-1}}
   \]

   which still changes rank (M-2).  This is an abstract augmented-Graver theorem, not a positive exact-factor theorem.

2. **The first top-two-neutral positive gate fails completely.**  Put (z_5=P_4w_4).  There is no nonzero support-feasible \(h\sqsubseteq z_5\) with

   \[
   B_5h=B_4h=0.
   \]

   Thus no stacked or augmented top-two Graver summand conformal to the natural suspension is applicable at any exact-factor vertex.  More precisely, every conformal middle-kernel subrelation selects the same number (k) of pointings over every one of the eight seed rows; support feasibility forces (k=1), while the certified three-target obstruction proves that such a one-point section cannot preserve both displayed rows.  Ordinary \(B_5\)-Graver pieces which change \(B_4\) are not excluded.

3. **Literal preservation of the suspended deeper effect fails from the second step onward.**  Every middle packing in dimension (M) has the exact lower-load capacity

   \[
   \mu_{M-q}(T)
   \le
   \left\lfloor
   \frac1{q+1}\binom{M+q+1}{q}
   \right\rfloor.
   \tag{1.5}
   \]

   At depth two the twice-suspended (m=4) effect already cannot be the rank-four effect of **any** support-feasible trade in dimension (M=6).  For every \(M\ge7\), the single-coordinate inequality

   \[
   \frac{(M-2)!}{2}
   >
   \left\lfloor\frac{(M+3)(M+2)}6\right\rfloor
   \tag{1.6}
   \]

   gives the contradiction.  Hence an all-(m) positive suspension must disperse or renormalize the deeper effect; it cannot retain the multiplicative factor (m-1) at every step.

4. **A bounded support-feasible partial augmented-Graver packet does exist for all sufficiently large dimensions.**  For every

   \[
   m\ge510,
   \]

   there is an unconditional support-feasible six-for-six vector (Z) with

   \[
   B_mZ=B_{m-1}Z=0,
   \qquad
   B_{m-2}Z\ne0,
   \tag{1.7}
   \]

   and

   \[
   Z\in\operatorname{Gr}\binom{B_m}{B_{m-1}}.
   \tag{1.8}
   \]

   It is the minimal first-shadow cancellation packet of three disjoint two-for-two ordinary (B_m)-circuits.  Each component is separately realizable in an exact factor, but the three known completions are different.

5. **The sole missing positive statement for that bounded packet is exact common completion.**  It is unproved that its six negative rows lie together in one exact factor.  If they do, (Z) is an applicable lifted-Graver move and produces a literal exact-factor three-cube.  A common completion cannot fuse its three ordinary ownership components, so it remains ordinary-Graver decomposable and lifted-Graver indecomposable.

These results settle the structural question posed in this lane.  Graver primitivity itself is not the obstruction.  The obstruction is positivity inside one right-hand-side-one factor fibre.  The natural linear suspension has no conformal positive piece which preserves both top rows, and its raw deeper amplitude soon exceeds the capacity of every middle packing.  A successful all-dimensional theorem must reroute middle ownership, choose phases across different old owners, and renormalize the deeper signal while simultaneously proving exact completion.

Nothing here proves MWB, labelled synchronization, or the contiguous-OR width conjecture.

## 2. Definitions and the four levels of Graver status

Put

\[
n=2m+1.
\]

Let \(\Omega_m\) be the set of unoriented cyclic orders on ([n]), with rotation and reversal identified.  For \(C\in\Omega_m\), let

\[
B_re_C=\sum_{I\in\mathcal W_r(C)}e_I,
\]

where \(\mathcal W_r(C)\) is the family of cyclic (r)-intervals of (C).  The exact middle incidence matrix is

\[
A_m:=B_m.
\]

An exact factor is an indicator \(x\in\{0,1\}^{\Omega_m}\) with

\[
A_mx=\mathbf1.
\]

It has exactly

\[
\operatorname{Cat}_m
=\frac1{2m+1}\binom{2m+1}{m}
\]

rows.

A reduced signed vector

\[
p=\mathbf1_P-\mathbf1_N
\]

is **support feasible** when (P) and (N) are middle-wreath packings and

\[
A_m\mathbf1_P=A_m\mathbf1_N.
\]

It is **exact-factor realizable** when one residual packing (H) makes both

\[
H\mathbin{\dot\cup}N,
\qquad
H\mathbin{\dot\cup}P
\]

exact factors.  Support feasibility is necessary but not sufficient for exact-factor realizability.

For integer vectors, \(u\sqsubseteq v\) means that (u) and (v) lie in the same closed orthant and \(|u_i|\le|v_i|\) coordinatewise.  The Graver basis \(\operatorname{Gr}(M)\) consists of the nonzero conformally indecomposable vectors in \(\ker_{\mathbb Z}M\).

Three notions must be separated.

1. An **ordinary incidence Graver** lies in \(\operatorname{Gr}(A_m)\).
2. A **shallow-neutral stacked Graver** lies in

   \[
   \operatorname{Gr}
   \begin{pmatrix}
   A_m\\D
   \end{pmatrix},
   \]

   where (D) is a stack of lower-rank maps.
3. For

   \[
   \widehat A_D=
   \begin{pmatrix}
   A_m&0\\
   D&-I
   \end{pmatrix},
   \tag{2.1}
   \]

   an **augmented Graver** is an element of \(\operatorname{Gr}(\widehat A_D)\).

If (Dp=0), then

\[
p\in\operatorname{Gr}\binom{A_m}{D}
\quad\Longleftrightarrow\quad
(p,0)\in\operatorname{Gr}(\widehat A_D).
\tag{2.2}
\]

Indeed, conformality to a zero auxiliary block forces every conformal summand to have zero auxiliary part.

An abstract Graver vector need not be applicable at \(A_mx=\mathbf1\).  If a squarefree (p) is applicable at an exact factor, then (p^-) is a subpacking of that factor, and (A_mp^+=A_mp^-) forces (p^+) to be a packing as well.  Thus support feasibility is a necessary applicability test.

## 3. Ownership overlays and minimal cancellation packets

Let

\[
p=\mathbf1_P-\mathbf1_N
\]

be a reduced support-feasible middle trade.  Its **middle-ownership overlay** \(\Gamma(p)\) is the bipartite multigraph with vertices \(N\dot\cup P\); every middle target joins its unique negative and positive owners.

### Theorem 3.1 — overlay characterization of conformal middle moves

The nonzero vectors \(u\sqsubseteq p\) satisfying (A_mu=0) are exactly the unions of nonempty connected components of \(\Gamma(p)\).  Consequently,

\[
\boxed{
p\in\operatorname{Gr}(A_m)
\iff
\Gamma(p)\text{ is connected}.}
\tag{3.1}
\]

#### Proof

Because (p) is squarefree, \(u\sqsubseteq p\) selects subsets of the positive and negative order vertices.  For a middle target (S), the (S)-row of (A_mu=0) says that its negative owner is selected if and only if its positive owner is selected.  The selected vertex set is therefore closed under every overlay edge, hence is a union of connected components.

Conversely, every overlay component contains both endpoints of each of its incident target edges.  Its signed vertex indicator is therefore a middle-kernel vector.  This proves the first statement, and conformal indecomposability gives (3.1).  \(\square\)

The next theorem shows that, once a positive exact trade exists, extracting a controlled lifted Graver is automatic.

### Theorem 3.2 — minimal shallow-neutral packet extraction

Let (D) and (E) be arbitrary integer row maps on cyclic orders.  Let (p) be a support-feasible middle trade with ownership components

\[
p=p_1+\cdots+p_t.
\]

Assume

\[
Dp=0,
\qquad
Ep\ne0.
\tag{3.2}
\]

Partition \(\{1,\ldots,t\}\) iteratively into inclusion-minimal nonempty zero-sum blocks \(I_1,\ldots,I_s\), where

\[
D\sum_{i\in I_j}p_i=0.
\]

Put

\[
g_j=\sum_{i\in I_j}p_i.
\]

Then

\[
g_j\in\operatorname{Gr}\binom{A_m}{D},
\qquad
(g_j,0)\in\operatorname{Gr}(\widehat A_D).
\tag{3.3}
\]

At least one block also satisfies

\[
Eg_j\ne0.
\tag{3.4}
\]

If (p) is a difference of exact factors, every (g_j) is applicable at the negative endpoint.

#### Proof

The zero-sum blocks exist: choose an inclusion-minimal nonempty zero-sum subset, remove it, and repeat; the complement remains zero-sum.  By Theorem 3.1, every conformal (A_m)-kernel subvector of (g_j) is a union of ownership components indexed by a subset of (I_j).  If it is also in \(\ker D\), that subset is a nonempty zero-sum proper subblock, contrary to minimality.  Thus (g_j) is stacked-Graver.  Equation (2.2) gives the augmented statement.

Since

\[
Ep=\sum_jEg_j\ne0,
\]

one block satisfies (3.4).  Finally, between exact endpoints every component subset is a legal factor switch, so every (g_j) is applicable.  \(\square\)

For depth two, take

\[
D=B_{m-1},
\qquad
E=B_{m-2}.
\]

Thus every exact-factor-realizable depth-two trade contains an applicable first-shadow-neutral augmented Graver retaining a nonzero second-shadow effect.  No extra Graver theorem is needed after the positive endpoint has been constructed.

## 4. The certified (m=4) seed is already an applicable Graver circuit

The known seed has four negative and four positive orders, with a common ten-order completion to two exact fourteen-order factors.  Its exact profile is

\[
B_4w_4=B_3w_4=0
\]

and

\[
\begin{aligned}
B_2w_4={}&-e_{13}+e_{23}+e_{14}-e_{24}
        +e_{15}-e_{25}-e_{19}+e_{29}.
\end{aligned}
\tag{4.1}
\]

The four-for-four replacement is one connected interaction-component switch for the final transposition \(\tau=(1\ 2)\).  Therefore Theorem 3.1 gives

\[
w_4\in\operatorname{Gr}(A_4).
\tag{4.2}
\]

Since (B_3w_4=0), it also gives

\[
w_4\in\operatorname{Gr}\binom{B_4}{B_3},
\qquad
(w_4,0)\in
\operatorname{Gr}
\begin{pmatrix}
B_4&0\\B_3&-I
\end{pmatrix}.
\tag{4.3}
\]

This is a genuine applicable depth-two augmented Graver.  The issue is not existence at the seed dimension; it is stable positive suspension.

## 5. Exact all-dimensional signed suspension

Let \(C=(c_0,\ldots,c_{2m})\) be an oriented representative of an old cyclic order.  Number its gaps by \(\mathbb Z_{2m+1}\).  Add new labels (x_m,y_m).  Let \(E_{a,m}C\) be obtained by inserting (x_m) in gap (a) and (y_m) in gap (a+m).  Define

\[
P_me_C=\sum_{a\in\mathbb Z_{2m+1}}e_{E_{a,m}C}.
\tag{5.1}
\]

Choose one orientation for each old unoriented row.  Deleting (x_m,y_m) recovers the old row and the marked insertion gaps, so the descendants in (5.1) are distinct in the unoriented quotient.  Descendants of different old rows are also distinct.

The exact gap count gives the following depth-two identity.

### Lemma 5.1 — one-step antipodal shadow formula

If

\[
B_mz=B_{m-1}z=0,
\]

then

\[
B_{m+1}P_mz=B_mP_mz=0
\tag{5.2}
\]

and

\[
B_{m-1}P_mz
=(m-1)(\iota_{x_m}+\iota_{y_m})B_{m-2}z.
\tag{5.3}
\]

Here \(\iota_xe_U=e_{U\cup\{x\}}\).  The two one-new-label sectors are disjoint, so their sum is injective.

#### Proof

For insertion distance (m), the number of ordered insertion pairs lying inside an interval of \(\ell\) old gaps is

\[
h_m(\ell)=(\ell-m)_++(\ell-(m+1))_+.
\]

At new ranks (m+1) and (m), the zero-, one-, and two-new-label sectors use only old rows (m,m-1,m-2); the only potentially new (B_{m-2}) coefficient is \(h_m(m-1)=0\).  At new rank (m-1), the zero-new and two-new sectors vanish, while either one-new sector has coefficient

\[
(m-1)-h_m(m-2)=m-1.
\]

This gives (5.2)-(5.3).  \(\square\)

### Theorem 5.2 — iterated signed suspension with exact constants

For \(M\ge4\), use fresh pairs \(\{x_j,y_j\}\), \(4\le j<M\), and put

\[
z_4=w_4,
\qquad
z_{j+1}=P_jz_j.
\tag{5.4}
\]

Define

\[
D_M=\prod_{j=4}^{M-1}(2j+1),
\qquad
J_j=\iota_{x_j}+\iota_{y_j},
\tag{5.5}
\]

with empty product (D_4=1).  Then (z_M) is squarefree and

\[
|z_M^+|=|z_M^-|=4D_M,
\tag{5.6}
\]

\[
B_Mz_M=B_{M-1}z_M=0,
\tag{5.7}
\]

and

\[
\boxed{
B_{M-2}z_M
=\frac{(M-2)!}{2}
J_{M-1}\cdots J_4(B_2w_4)\ne0.}
\tag{5.8}
\]

#### Proof

Recursive deletion of the newest labelled pair recovers the unique parent and pointing.  Hence different insertion histories give different final cyclic orders, so coefficients remain in \(\{-1,0,1\}\) and (5.6) follows.

Equations (5.7)-(5.8) follow inductively from Lemma 5.1.  The scalar is

\[
\prod_{j=4}^{M-1}(j-1)
=3\cdot4\cdots(M-2)
=\frac{(M-2)!}{2}.
\]

The composite \(J_{M-1}\cdots J_4\) has \(2^{M-4}\) disjoint sectors, distinguished by choosing exactly one label from each new pair.  It is injective, and (4.1) is nonzero.  \(\square\)

### Corollary 5.3 — controlled augmented-Graver extraction in every dimension

For every \(M\ge4\), there is a squarefree

\[
g_M\in\operatorname{Gr}\binom{B_M}{B_{M-1}}
\]

such that

\[
g_M\sqsubseteq z_M,
\qquad
B_{M-2}g_M\ne0,
\tag{5.9}
\]

and

\[
|g_M^+|=|g_M^-|
\le4D_M.
\tag{5.10}
\]

Equivalently,

\[
(g_M,0)\in
\operatorname{Gr}
\begin{pmatrix}
B_M&0\\B_{M-1}&-I
\end{pmatrix}.
\]

#### Proof

Conformally decompose (z_M) in the kernel of \(\binom{B_M}{B_{M-1}}\).  Every summand is squarefree.  Since their (B_{M-2})-images sum to the nonzero vector (5.8), at least one is nonzero there.  Its support is bounded by that of (z_M).  Summing all middle rows shows that every middle-kernel vector has coefficient sum zero, hence equal positive and negative cardinalities.  \(\square\)

There is a second, different conclusion.  Decomposing (z_M) in \(\operatorname{Gr}(B_M)\) produces an ordinary (B_M)-Graver summand with nonzero (B_{M-2})-image, but that summand need not preserve (B_{M-1}).  Corollary 5.3 produces a first-shadow-neutral primitive, but it need not be an ordinary (B_M)-Graver or support feasible.  The two conclusions must not be merged.

## 6. Deletion projection and the complete \(m=4\to5\) top-two conformal obstruction

The all-pointings suspension has an exact projection back to the seed.

### Lemma 6.1 — exact deletion projection

On the descendant support define

\[
\pi(e_{E_{a,m}C})=e_C.
\]

For every old (m)-set \(S\subseteq V\), \(|V|=2m+1\), and every signed descendant vector (h),

\[
\boxed{
(B_m\pi h)_S
=(B_{m+1}h)_{S\cup\{x_m\}}
 +(B_{m+1}h)_{S\cup\{y_m\}}
 -(B_{m+1}h)_{V\setminus S}.}
\tag{6.1}
\]

In particular,

\[
B_{m+1}h=0
\quad\Longrightarrow\quad
B_m\pi h=0.
\tag{6.2}
\]

#### Proof

It is enough to check one descendant column.  If (S) is not an old middle interval, none of the three displayed new targets is a new middle interval.  If (S) is an old middle interval, the five possible relative pointing states have incidence triples

\[
(1,0,0),\quad(1,0,0),\quad(0,1,0),\quad
(0,1,0),\quad(1,1,1)
\]

on

\[
S\cup\{x_m\},\quad S\cup\{y_m\},\quad V\setminus S.
\]

In every case first plus second minus third is one.  Summing columns proves (6.1).  Reversal only interchanges the two one-new sectors, so the identity is orientation independent.  \(\square\)

### Lemma 6.2 — connected-overlay multiplicity propagation

Let

\[
w=\mathbf1_P-\mathbf1_N
\]

be a support-feasible old trade with connected ownership overlay, and let \(h\sqsubseteq P_mw\) satisfy \(B_{m+1}h=0\).  Then there is one integer

\[
k\in\{0,1,\ldots,2m+1\}
\]

such that (h) selects exactly (k) descendants above every old row on both signs.  If \(h\ne0\), then \(k\ge1\).  If (h) is support feasible, then (k=1).

#### Proof

For \(D\in P\), let \(\alpha_D\) be the number of selected descendants above (D); for \(C\in N\), let \(\beta_C\) be the corresponding negative count.  By Lemma 6.1, \(B_m\pi h=0\).  For an old middle target (S), whose unique owners are \(C\in N\) and \(D\in P\), its row gives

\[
\alpha_D=\beta_C.
\]

Connectivity propagates one common value (k) to all vertices.

Any two distinct antipodal descendants of the same old order share a new middle target.  Therefore a new middle packing contains at most one descendant above each old row, so support feasibility gives \(k\le1\).  \(\square\)

We now use the explicit three-target obstruction for the certified seed.  In ordinary interval order take

\[
C=(1,3,4,8,6,7,9,5,2),
\qquad
D=(1,5,9,7,6,8,4,3,2).
\]

Three common old middle targets start in (C,D) at

\[
(8,6),\qquad(7,7),\qquad(1,4).
\tag{6.3}
\]

For (m=4), the five middle-signature classes are

\[
\{0,1,2\},\quad\{3\},\quad\{4\},\quad
\{5,6,7\},\quad\{8\}.
\tag{6.4}
\]

The five-class map \(\kappa\) records four coordinates attached to one old middle target \(S\): the three new-middle targets

\[
S\cup\{x_4\},\qquad S\cup\{y_4\},\qquad V\setminus S
\]

and the target \(S\) itself in the new first-lower row \(B_4\).  Thus it records the simultaneous \(B_5/B_4\) signature, not \(B_5\) alone.

In the order of the five classes in (6.4), the four-coordinate values are

\[
(1,0,0,0),\quad
(1,0,0,1),\quad
(0,1,0,1),\quad
(0,1,0,0),\quad
(1,1,1,1).
\tag{6.4a}
\]

If \(a,b\in\mathbb Z_9\) are pointings of (C,D), put

\[
x=a-8,
\qquad
d=b-a.
\]

Equality of these simultaneous top-two signatures on the three old targets requires

\[
\kappa(x)=\kappa(x+d+2),
\quad
\kappa(x+1)=\kappa(x+d+1),
\quad
\kappa(x+7)=\kappa(x+d+4).
\tag{6.5}
\]

### Lemma 6.3 — the three equations have no solution

Equations (6.5) have no solution in \(\mathbb Z_9^2\).

#### Proof

Put (y=x+1).  The middle equation says \(\kappa(y)=\kappa(y+d)\), hence

\[
d\in\{0,\pm1,\pm2\}.
\]

- If (d=0), the first equation leaves \(x\in\{0,5\}\); the third compares respectively classes of ((7,4)) or ((3,0)), both unequal.
- If (d=1), then \(y\in\{0,1,5,6\}\); the first equation \(\kappa(y-1)=\kappa(y+2)\) fails in all four cases.
- If (d=2), then \(y\in\{0,5\}\); the first equation \(\kappa(y-1)=\kappa(y+3)\) fails.
- If (d=-2), then \(y\in\{2,7\}\); the third equation \(\kappa(y-3)=\kappa(y+1)\) fails.
- If (d=-1), then \(y\in\{1,2,6,7\}\); the third equation \(\kappa(y-3)=\kappa(y+2)\) fails.

These are all possibilities.  \(\square\)

### Theorem 6.4 — no conformal positive top-two extraction from (P_4w_4)

Let

\[
z_5=P_4w_4.
\]

There is no nonzero \(h\sqsubseteq z_5\) such that

\[
B_5h=B_4h=0
\]

and (h) is support feasible.  Consequently every stacked \(\binom{B_5}{B_4}\)-Graver summand, equivalently every zero-auxiliary top-two augmented-Graver summand, conformal to (z_5) is inapplicable at every exact-factor vertex.

#### Proof

The old seed overlay is connected.  Lemma 6.2 says that a nonzero support-feasible (h) must choose exactly one pointing above each of the eight seed rows.  For one descendant per old row, each sign is automatically a packing: equality of two new middle targets would project to equality of two old middle targets, contradicting the old packing property.

The simultaneous new middle and first-lower equations therefore reduce to the exact coarse top-two pointing conditions on the old occurrence pairs.  The particular pair (C,D) and the three targets in (6.3) would have to satisfy (6.5), contradicting Lemma 6.3.  \(\square\)

There is a useful exact refinement.  In any conformal stacked-kernel decomposition

\[
z_5=h_1+\cdots+h_t,
\]

Lemma 6.2 gives

\[
\pi h_i=k_iw_4,
\qquad
\sum_i k_i=9.
\]

Lemma 6.3 rules out (k_i=1), so \(k_i\ge2\) and

\[
t\le\left\lfloor\frac92\right\rfloor=4.
\tag{6.6}
\]

Every piece has

\[
8\le |h_i^+|=|h_i^-|=4k_i\le36
\tag{6.7}
\]

and is nonpacking.  Thus every stacked piece is inapplicable, while at least one changes \(B_3\).

For contrast, an ordinary \(B_5\)-Graver decomposition need not preserve \(B_4\) termwise.  Lemma 6.2 then gives only \(k_i\ge1\) and \(t\le9\); the present argument neither excludes \(k_i=1\) nor proves that every ordinary piece is nonpacking.

## 7. A universal lower-shadow capacity for middle packings

The factorial coefficient in (5.8) is not merely an aesthetic defect.  Every support-feasible trade has a polynomial coordinate cap at fixed depth.

### Theorem 7.1 — exact lower-load packing capacity

Let (F) be any middle-wreath packing in dimension (M), on (2M+1) labels.  Fix \(1\le q\le M-1\) and a target

\[
T\in\binom{[2M+1]}{M-q}.
\]

Then

\[
\boxed{
(B_{M-q}\mathbf1_F)_T
\le
L_{M,q}:=
\left\lfloor
\frac1{q+1}\binom{M+q+1}{q}
\right\rfloor.}
\tag{7.1}
\]

Consequently every support-feasible partial trade

\[
p=\mathbf1_P-\mathbf1_N
\]

satisfies

\[
\boxed{
|(B_{M-q}p)_T|\le L_{M,q}.}
\tag{7.2}
\]

The same bound holds, in particular, for every difference of exact factors.

#### Proof

Whenever (T) occurs as a cyclic ((M-q))-interval in one wreath (C), it has exactly (q+1) distinct cyclic middle extensions in (C): extend by (a) positions on the left and (q-a) on the right, for \(0\le a\le q\).

For two distinct rows of the middle packing, these ((q+1))-families are disjoint, because no middle target has two owners.  The total number of middle supersets of (T) is

\[
\binom{(2M+1)-(M-q)}q
=\binom{M+q+1}q.
\]

Dividing proves (7.1).  The two signed loads in a support-feasible trade both lie in \([0,L_{M,q}]\), so their difference lies in \([-L_{M,q},L_{M,q}]\), proving (7.2).  \(\square\)

At depth two,

\[
L_{M,2}
=\left\lfloor\frac{(M+3)(M+2)}6\right\rfloor.
\tag{7.3}
\]

### Theorem 7.2 — strict capacity obstruction from dimension seven

For every \(M\ge7\), no support-feasible trade (p) can have

\[
B_{M-2}p=B_{M-2}z_M,
\tag{7.4}
\]

where (z_M) is the raw iterated suspension in Theorem 5.2.

#### Proof

Choose any one of the eight targets (U) in (4.1), whose coefficient is \(\pm1\), and choose one label from each added pair.  The resulting target (T_M) in the corresponding sector of (5.8) has coefficient

\[
|(B_{M-2}z_M)_{T_M}|
=A_M:=\frac{(M-2)!}{2}.
\tag{7.5}
\]

At (M=7),

\[
A_7=60,
\qquad
L_{7,2}=15.
\]

Thereafter

\[
\frac{A_{M+1}}{A_M}=M-1\ge6,
\]

whereas the ratio of the unfloored capacities is

\[
\frac{M+4}{M+2}<2.
\]

Thus (A_M>L_{M,2}) for every \(M\ge7\), contradicting (7.2).  \(\square\)

The threshold can be sharpened to the second suspension step by using the four simultaneous saturated branches.

### Theorem 7.3 — the twice-suspended effect is already nonpositive at (M=6)

Let the two new pairs used in (P_5P_4) be

\[
A=\{x_4,y_4\},
\qquad
B=\{x_5,y_5\}.
\]

No support-feasible trade (p) in dimension (6) satisfies

\[
B_4p=B_4z_6.
\tag{7.6}
\]

#### Proof

Choose a base two-set (E) having coefficient (+1) in (B_2w_4); for example, (E=\{2,3\}).  For \(u\in A\), \(v\in B\), put

\[
R_{uv}=E\cup\{u,v\}.
\]

The four distinct rank-four targets (R_{uv}) all have coefficient

\[
(B_4z_6)_{R_{uv}}=12.
\tag{7.7}
\]

But (L_{6,2}=12).  If (7.6) held for \(p=\mathbf1_P-\mathbf1_N\), equality in the capacity bound would force

\[
(B_4\mathbf1_P)_{R_{uv}}=12,
\qquad
(B_4\mathbf1_N)_{R_{uv}}=0
\tag{7.8}
\]

for all four choices.

For a fixed (R_{uv}), its twelve occurrences on the positive side each supply three distinct middle extensions.  Equality in (7.1) means that these (36) extensions exhaust all

\[
\binom92=36
\]

middle supersets of (R_{uv}).

Now

\[
T=E\cup A\cup B
\]

is a six-set containing all four (R_{uv}).  Therefore the unique positive wreath owning the middle target (T) must contain all four (R_{uv}) as cyclic four-intervals.  Inside one cyclic six-interval, however, there are only

\[
6-4+1=3
\]

cyclic four-subintervals.  This contradiction proves the theorem.  \(\square\)

The same argument is seed-independent: any nonzero depth-two effect in dimension four, twice suspended by (P_4,P_5), has four branch coordinates of magnitude (12|a|).  If \(|a|\ge2\), one coordinate already violates capacity; if \(|a|=1\), the four-versus-three saturation contradiction applies.

### Corollary 7.4 — every fixed-depth raw suspension eventually leaves the support-feasible class

Let a seed in dimension (m_0) have its first nonzero lower row at depth \(q\), and suppose one coefficient there has magnitude \(a\ge1\).  Iterating the antipodal operator to dimension (M) creates branch coefficients of magnitude

\[
a\prod_{j=m_0}^{M-1}(j+1-q)
=a\frac{(M-q)!}{(m_0-q)!}.
\tag{7.9}
\]

For fixed (q), this is factorial in (M), while (L_{M,q}) in (7.1) is a polynomial of degree (q).  Hence the unrenormalized shadow recurrence is incompatible with support feasibility in all sufficiently large dimensions.

This corollary does not rule out a conformal Graver subrelation with much smaller surviving coefficients, nor a state-level suspension which spreads the old effect over many targets with cancellation.  It proves that such renormalization is mathematically necessary.

There is also a quantitative positive-decomposition consequence.  If the raw (z_M) is written as a sum of (s) support-feasible trades, then at the target (T_M) of (7.5), the triangle inequality and (7.2) give

\[
s\ge
\left\lceil\frac{A_M}{L_{M,2}}\right\rceil.
\tag{7.10}
\]

Thus even a decomposition into positive pieces must have factorial-over-quadratic length if it retains the raw suspended amplitude.

## 8. Conditional positive suspension and why the seed fails it

The obstruction above should be compared with the strongest honest positive one-step theorem.

For an old middle interval (S) occurring in a row (C), let (s_C(S)) be its start.  A pointing \(a_C\in\mathbb Z_{2m+1}\) is **bi-flat** when paired occurrences at ranks (m) and (m-1) satisfy

\[
a_C-s_C(S)=a_D-s_D(S)\pmod{2m+1}.
\tag{8.1}
\]

### Theorem 8.1 — conditional Graver-preserving suspension

Let \(w=\mathbf1_P-\mathbf1_N\) be a connected support-feasible trade with

\[
B_mw=B_{m-1}w=0,
\qquad
B_{m-2}w\ne0.
\]

Assume a bi-flat pointing exists.  For every common translate \(t\), choose the single descendant

\[
E_{a_C+t,m}C
\]

above every old row and let (w_t) be the resulting signed vector.  Then:

1. (w_t) is support feasible and

   \[
   B_{m+1}w_t=B_mw_t=0;
   \]

2. its new middle-ownership overlay is connected, so

   \[
   w_t\in\operatorname{Gr}(B_{m+1});
   \]

3. at least one translate satisfies

   \[
   B_{m-1}w_t\ne0.
   \]

#### Proof

Bi-flatness makes every paired old occurrence see the same exact relative offset, so the corresponding new middle and first-lower incidence decisions agree.  One descendant per old packing row is again a packing.  This proves the two top-row identities.

For every old overlay edge, the common relative state exposes at least one common new middle target.  Hence the lifted overlay contains a spanning copy of the connected old overlay.  Theorem 3.1 gives ordinary Graver connectedness.

Finally,

\[
\sum_{t\in\mathbb Z_{2m+1}}w_t=P_mw.
\]

Lemma 5.1 gives a nonzero (B_{m-1})-image for the right side, so at least one translate has nonzero image.  \(\square\)

If the negative packing of the deeper-effective translate lies in an exact factor, then the lift is an applicable exact-factor Graver move.  That completion is a separate condition.

The seed fails before this theorem can be used.

### 8.1 Exact-offset holonomy

Build the occurrence graph on old negative and positive rows and label a paired occurrence edge by

\[
\gamma(CD)=s_D(S)-s_C(S)\in\mathbb Z_{2m+1}.
\]

A bi-flat pointing is exactly a potential for this gain cochain, so it exists if and only if every closed-walk gain is zero.

For the certified seed, one moved middle-target edge has gain (1), while a fixed-target vertical edge has gain (0).  Their two-edge cycle is unbalanced in \(\mathbb Z_9\).  Therefore no bi-flat pointing exists.

More generally, let \(H\) be the subgroup generated by all closed-walk gains.  The exact-offset derived cover has \((2m+1)/|H|\) connected components, and every component contains exactly \(|H|\) pointings above every old row.  If \(H\ne0\), every component contains two descendants of one old row and is not a packing.  The seed has \(H=\mathbb Z_9\), so its derived cover is connected and contains all nine pointings above every seed row.

An owner- and start-preserving common-context embedding retains the gain-one cycle as gain \(1\pmod{2M+1}\) in every larger dimension.  Padding cannot remove the obstruction.  At least one occurrence on every inherited unbalanced cycle must be rerouted.

This is an obstruction to the translation-stable exact-offset ansatz.  It is not an obstruction to the coarser five-state pointing equations.  Theorem 6.4 separately rules out a coarse one-point lift preserving both new top rows for the chosen antipodal operator.

### 8.2 Phase erasure costs the full orbit

For a multiset (D) of pointing phases over one old row, let the multiset of five local states seen at old phase (s) be

\[
K_D(s)=\{\!\{\kappa(a-s):a\in D\}\!\}.
\]

If (K_D(s)) is independent of (s), the multiplicity of the singleton boundary state forces every residue to have the same multiplicity.  Thus

\[
D=c\,\mathbb Z_{2m+1}.
\tag{8.2}
\]

Every nonempty phase-oblivious orderwise gadget uses at least (2m+1) descendants of each old row, while a packing can use at most one.  For an old sign with (s) rows, a packing thinning of the raw orbit discards at least

\[
2ms
\tag{8.3}
\]

orbit columns.  For the four-row (m=4) seed sign this is (32) of the (36) descendants.  Thus the linear operator cannot be made positive by a small phase-symmetric correction.

## 9. Counting and metric obstructions to product or common-context lifts

### Theorem 9.1 — no uniform pure orderwise factor product beyond (m=4)

Suppose a pure orderwise suspension maps every row of an exact factor in dimension (m) to exactly (k) disjoint descendant rows, uses no auxiliary rows, and produces an exact factor in dimension (m+1).  Then

\[
k\operatorname{Cat}_m=\operatorname{Cat}_{m+1},
\]

so

\[
k=\frac{\operatorname{Cat}_{m+1}}{\operatorname{Cat}_m}
=\frac{2(2m+1)}{m+2}
=4-\frac6{m+2}.
\tag{9.1}
\]

The ratio is the integer (3) at (m=4), and is nonintegral for every \(m\ge5\).  Therefore no such uniform pure product can iterate beyond the first step.

If an old-coordinate-equivariant construction is used, transitivity of the symmetric group on cyclic orders forces the fibre size to be uniform, so (9.1) applies.  A nonuniform or auxiliary completion is indispensable.

There is an exact (3/4)-fibre refinement.  If every old row receives either three or four descendants and there are no auxiliary rows, then the number of four-fibre rows must be

\[
r_m
=\operatorname{Cat}_{m+1}-3\operatorname{Cat}_m
=\frac{m-4}{m+2}\operatorname{Cat}_m.
\tag{9.2}
\]

Thus the heavy/light choice is state dependent on a macroscopic number of old rows.  The extra fourth descendants form the fraction

\[
\frac{r_m}{\operatorname{Cat}_{m+1}}
=\frac{m-4}{4m+2}
\longrightarrow\frac14
\tag{9.3}
\]

of the new factor.  This cannot be treated as an (o(1)) auxiliary correction.

### Theorem 9.2 — linear dispersion is necessary for common contexts

For two unoriented cyclic orders let \(d_\circ(C,D)\) be cyclic adjacent-swap distance.  One adjacent swap changes at most two middle intervals, so

\[
|\mathcal W_m(C)\cap\mathcal W_m(D)|
\ge2m+1-2d_\circ(C,D).
\tag{9.4}
\]

Hence two distinct same-sign rows of a middle packing satisfy

\[
d_\circ(C,D)\ge m+1.
\tag{9.5}
\]

Suppose a lift from dimension (m_0) to (m_0+t) obeys

\[
d_\circ(\Phi_t(C),\Phi_t(D))
\le d_\circ(C,D)+e_t.
\]

Packing forces

\[
e_t\ge m_0+t+1-d_\circ(C,D).
\tag{9.6}
\]

If both lifted endpoints differ from a literal common-context embedding by at most (s_t) adjacent swaps, then \(e_t\le2s_t\), so

\[
s_t\ge
\left\lceil
\frac{m_0+t+1-d_\circ(C,D)}2
\right\rceil.
\tag{9.7}
\]

For the seed, the minimum same-sign distance is (7) and (m_0=4).  Thus

\[
e_t\ge t-2,
\qquad
s_t\ge\left\lceil\frac{t-2}{2}\right\rceil.
\tag{9.8}
\]

A distance-preserving literal common context (`e_t=0` in (9.6)) fails by
`t=3`, namely dimension `7`.  More generally, every indefinitely recursive
lift must create linearly growing order-dependent dispersion.  A tail which
is common in complement-geodesic **path time** need not be a distance-
preserving context in the induced cyclic-window order: it may split into
separate deletion and insertion banks and create the required dispersion.
See `MATH_AUDIT_TAMARI_TENSOR_VS_LINEAR_DISPERSION_20260806.md`.

## 10. A constant-support support-feasible partial lifted-Graver packet for every \(m\ge510\)

The failure of the seed suspension does not imply that abstract shallow-neutral Graver vectors must be mesoscopic.  In fact, a bounded support-feasible lifted-Graver exists in all sufficiently large dimensions.

### 10.1 Universal two-for-two circuits

Fix distinct labels \(\alpha,\beta,\gamma,\delta\).  Let (E,O) be ordered lists of the remaining labels with

\[
|E|=m-1,
\qquad
|O|=m-2.
\]

In ordinary cyclic-interval order put

\[
\begin{aligned}
C  &=(\delta,\gamma,E,\beta,\alpha,O),\\
D  &=(\beta,\delta,E,\alpha,\gamma,O),\\
C' &=(\delta,\beta,E,\gamma,\alpha,O),\\
D' &=(\gamma,\delta,E,\alpha,\beta,O),
\end{aligned}
\tag{10.1}
\]

and

\[
z(E,O)=e_{C'}+e_{D'}-e_C-e_D.
\tag{10.2}
\]

For a core (H) avoiding \(\beta,\gamma\), define

\[
\partial H=e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}.
\]

The universal four-letter cut table gives

\[
B_mz(E,O)=0,
\tag{10.3}
\]

and both signs in (10.2) are middle packings.  For \(2\le r\le m-1\), with \(\ell=r-1\),

\[
\boxed{
B_rz(E,O)
=\partial\operatorname{suf}_{\ell}(O)
 +\partial\operatorname{suf}_{\ell}(E)
 -\partial\operatorname{pre}_{\ell}(E)
 -\partial\operatorname{pre}_{\ell}(O).}
\tag{10.4}
\]

If

\[
E=(u,K,v),
\qquad |K|=m-3,
\]

then

\[
B_{m-1}z(E,O)
=f_v-f_u,
\qquad
f_t:=\partial(K\cup\{t\}).
\tag{10.5}
\]

The (2+2) ownership overlay of (z(E,O)) is connected.  Indeed, a disconnected (n)-regular bipartite overlay with two vertices on either side would split into two one-for-one components, forcing equality of an old and a new wreath column.  A middle column determines its unoriented cyclic order: two labels are adjacent exactly when they occur together in \(m-1\) of its middle intervals, the maximum possible pair co-occurrence.  The four rows in (10.1) are distinct, so equality is impossible.  Theorem 3.1 gives

\[
z(E,O)\in\operatorname{Gr}(B_m).
\tag{10.6}
\]

Moreover every such circuit is individually exact-factor realizable.  Choose one canonical two-wreath MSW component, interleave its arbitrary tail into its (E/O) lists, and map its four exceptional labels and every tail slot to the prescribed labels in (10.1).  The resulting coordinate permutation maps the canonical MSW exact factor to an exact factor containing (C,D), in which the replacement by (C',D') is legal.

Thus these are genuine applicable ordinary Graver moves with a uniformly bounded lower profile.  They do not preserve the first shadow.

### 10.2 The dispersed triangle

Put

\[
k=m-3.
\]

Partition the ground set as

\[
[2m+1]
=\{\beta,\gamma,x,y,z\}
\mathbin{\dot\cup}K
\mathbin{\dot\cup}Q_0,
\tag{10.7}
\]

where

\[
|K|=k,
\qquad
|Q_0|=m-1.
\]

For

\[
uv\in\{xy,yz,xz\},
\]

let (w) be the unused member of \(\{x,y,z\}\) and put

\[
Q_{uv}=Q_0\cup\{w\}.
\]

Independently for the three contexts, choose an ordering \(K_{uv}\) of (K), and an ordering of (Q_{uv}).  Call the first two entries of the latter \(\delta_{uv},\alpha_{uv}\), and call the remaining ordered list \(O_{uv}\).  Set

\[
E_{uv}=(u,K_{uv},v),
\qquad
z_{uv}=z(E_{uv},O_{uv}),
\]

using the common axes \(\beta,\gamma\), and define

\[
\boxed{Z=z_{xy}+z_{yz}-z_{xz}.}
\tag{10.8}
\]

Formula (10.5) gives

\[
\begin{aligned}
B_{m-1}z_{xy}&=f_y-f_x,\\
B_{m-1}z_{yz}&=f_z-f_y,\\
B_{m-1}(-z_{xz})&=f_x-f_z.
\end{aligned}
\tag{10.9}
\]

Therefore

\[
B_mZ=B_{m-1}Z=0.
\tag{10.10}
\]

### Theorem 10.1 — existence of a nonzero support-feasible triangle

For every

\[
\boxed{m\ge510,}
\]

the orderings in the preceding construction can be chosen so that both signs of (Z) are middle packings and

\[
B_{m-2}Z\ne0.
\tag{10.11}
\]

#### Proof

Choose the three \(K_{uv}\) orderings and three (Q_{uv}) orderings independently and uniformly.  In each of the twelve rows, the (K)-labels form one consecutive block.  The exact number (N_a) of middle intervals containing (a) labels from (K) is

\[
N_0=5,
\qquad
N_k=4,
\qquad
N_a=2\quad(1\le a\le k-1).
\tag{10.12}
\]

Across both global signs and different contexts there are exactly six (C/C), twelve (C/D), and six (D/D) row pairs.  One-sided exposure of the two independently ordered long blocks gives the audited collision bound

\[
\Pr(\text{one of the two signs is not a middle packing})
\le
\frac{504}{m}
+\frac{450}{\binom m2}
+\frac{384}{m(m-3)}.
\tag{10.13}
\]

For completeness, the three contributions are obtained as follows.

- For \(1\le a\le k-1\), the prescribed (K)-subset has probability \(\binom ka^{-1}\), and the independently exposed nontrivial (Q)-subset contributes at most (1/m).  Since

  \[
  \sum_{a=1}^{k-1}\binom ka^{-1}<\frac4k,
  \]

  all twenty-four cross-context row pairs contribute less than \(384/[m(m-3)]\).
- At (a=0), the five (C)-windows have (Q)-deficits (0,1,1,2,2), while the five (D)-windows have deficits (1,1,2,2,2).  The exact (C/C,C/D,D/D) contributions are respectively

  \[
  \frac8m+\frac{16}{\binom m2},
  \quad
  \frac6m+\frac{19}{\binom m2},
  \quad
  \frac4m+\frac{21}{\binom m2}.
  \]
- At (a=k), the corresponding contributions are (12/m,16/m,16/m).  Multiplying by the pair counts (6,12,6) yields the first two terms of (10.13).

Let (A_{uv},B_{uv}) be the first and last entries of (K_{uv}).  In (B_{m-2}Z), the only two displayed (E)-cores with outside endpoint (y) are

\[
+\partial((K\setminus\{A_{xy}\})\cup\{y\})
\]

and

\[
-\partial((K\setminus\{B_{yz}\})\cup\{y\}).
\]

All (O)-cores contain no (K)-labels, and the other (E)-cores have endpoint (x) or (z).  Thus

\[
B_{m-2}Z=0
\quad\Longrightarrow\quad
A_{xy}=B_{yz}.
\]

The two entries are independent uniform members of (K), so

\[
\Pr(B_{m-2}Z=0)\le\frac1{m-3}.
\tag{10.14}
\]

For \(m\ge510\),

\[
\frac{450}{\binom m2}\le\frac2m,
\quad
\frac{384}{m(m-3)}\le\frac1m,
\quad
\frac1{m-3}\le\frac2m.
\]

The total bad probability is at most

\[
\frac{509}{m}<1.
\]

Therefore a successful choice exists.  \(\square\)

No finite search is hidden here; this is a direct probabilistic existence proof with an explicit union bound.

### 10.3 Exact row count and ownership components

For a successful choice, all twelve cyclic-order rows are distinct even after quotienting by reversal.

Across different contexts, the set (K) is the unique maximal cyclic run consisting entirely of (K)-labels, and its unordered pair of outside neighbors is respectively

\[
\{x,y\},\qquad\{y,z\},\qquad\{x,z\}.
\]

Rotation and reversal preserve this invariant, so rows from different contexts cannot coincide.

Within one context, each old pair and new pair is a packing.  Also \(C'=\tau C\) and \(D'=\tau D\), where \(\tau=(\beta\ \gamma)\).  A coordinate transposition cannot stabilize an odd labelled cyclic order.  If, for example, (C=D'), then \(D=\tau C\); but every order (Q) and \(\tau Q\) share a middle target.  Indeed, the two transposed labels have total incidence (2m=(2m+1)-1) among the middle intervals, so some interval contains both or neither and is fixed by \(\tau\).  This contradicts the fact that (C,D) are a packing.  The other cross equalities are identical.

Thus a successful (Z) has **exactly six rows on each sign**; no cross-sign cancellation is needed.

Each (z_{uv}), with the sign in (10.8), has a connected two-for-two overlay by the argument after (10.6).  Global support feasibility makes their middle unions pairwise disjoint: an intersection would give the global positive sign two owners of the same middle target.  Hence these three circuits are exactly the three connected components of \(\Gamma(Z)\).

### Theorem 10.2 — the triangle is a bounded stacked and lifted Graver

For every successful (Z),

\[
\boxed{
Z\in\operatorname{Gr}
\begin{pmatrix}
B_m\\B_{m-1}
\end{pmatrix}.}
\tag{10.15}
\]

Equivalently,

\[
\boxed{
(Z,0)\in
\operatorname{Gr}
\begin{pmatrix}
B_m&0\\B_{m-1}&-I
\end{pmatrix}.}
\tag{10.16}
\]

More generally, if \(B_H=(B_{m-1},\ldots,B_{m-H})\), then for every \(1\le H\le m-2\),

\[
\boxed{
(Z,B_HZ)\in
\operatorname{Gr}
\begin{pmatrix}
B_m&0\\B_H&-I
\end{pmatrix}.}
\tag{10.17}
\]

#### Proof

The six targets supporting (f_x,f_y,f_z) in (10.9) are distinct.  Hence no nonempty proper subset of the three component effects sums to zero: a single effect is nonzero, and a two-effect sum is the negative of the remaining nonzero effect.

By Theorem 3.1, a conformal middle-kernel subvector of (Z) must be a union of the three ownership components.  Requiring zero first shadow therefore leaves only (0) and (Z).  This proves (10.15), and (2.2) proves (10.16).

For (10.17), the first-shadow block of the total auxiliary vector is zero.  Any conformal lifted submove must therefore have zero first-shadow block and hence must again be either (0) or all of (Z).  \(\square\)

This theorem rules out every claimed \(\Omega(m)\) support lower bound for **abstract** stacked or lifted Graver elements.  Mesoscopic necessity can only concern applicability at the exact right-hand-side-one fibre, or a restricted selector/suspension architecture.

### 10.4 Uniform lower-profile control

For each component and every \(2\le r\le m-2\), the four cores in (10.4) are distinct and each dipole has two entries.  Thus

\[
\|B_rz_{uv}\|_2^2=8.
\tag{10.18}
\]

Consequently

\[
\|B_rZ\|_1\le24,
\qquad
\|B_rZ\|_2^2\le72.
\tag{10.19}
\]

For a window \(2\le H\le m-2\), with positive floor weights \(c_q\ge1\),

\[
\sum_{q\le H}\frac{\|B_{m-q}Z\|_2^2}{c_q}
\le72\sum_{q=2}^H\frac1{c_q}
\le72(H-1).
\tag{10.20}
\]

This is a genuinely controlled augmented-Graver profile, independent of (m) at every fixed rank and linear in the number of covered depths.

## 11. The exact common-completion gate

Let \(N=N_{xy}\dot\cup N_{yz}\dot\cup P_{xz}\) be the six-row negative side of (Z), with the sign convention in (10.8).  Define the residual middle vector

\[
r_N=\mathbf1-B_m\mathbf1_N.
\tag{11.1}
\]

Because (N) is a packing, (r_N) is a (0/1) vector.  Let

\[
\mathcal S_m=B_m\mathbb Z_{\ge0}^{\Omega_m}
\]

be the middle-column affine semigroup.

### Proposition 11.1 — completion equivalence

The following are equivalent.

1. The triangle (Z) is applicable at some exact factor.
2. One exact factor contains all six rows of (N).
3. There is a residual packing (H) with

   \[
   B_m\mathbf1_H=r_N.
   \]

4. \(r_N\in\mathcal S_m\).

#### Proof

If \(F=H\dot\cup N\) is exact, replacing (N) by the positive side of (Z) preserves the middle vector, so (Z) is applicable.  Conversely, applicability contains (N) in the negative endpoint and its complement is the required (H).  The semigroup equation is exactly the nonnegative integral completion equation.  Since its right side is (0/1), every nonnegative solution is automatically a packing.  \(\square\)

The residual is always in the integer column lattice: take any known exact factor (F_0) and write

\[
r_N=B_m(\mathbf1_{F_0}-\mathbf1_N).
\]

It is not proved that (r_N) lies in the rational cone.  Therefore failure of completion would be either a cone obstruction or, if cone membership also held, a genuine semigroup hole.  It is not currently legitimate to call the unresolved residual a semigroup hole.

The exact missing statement is:

> **Unproved six-row extension lemma.**  For every sufficiently large (m), at least one successful dispersed triangle from Theorem 10.1 has \(r_N\in\mathcal S_m\).

This is the only unproved lemma needed to promote Theorem 10.2 to a bounded applicable depth-two lifted-Graver theorem.

### Proposition 11.2 — what a completion would create

If \(F=H\dot\cup N\) is a common completion, then for every subset \(S\subseteq\{xy,yz,xz\}\), switching precisely the selected two-for-two components gives an exact factor.  Thus the completion creates a literal exact-factor three-cube, and its full diagonal (Z) is first-shadow neutral and second-shadow active.

The common residual cannot fuse the three ordinary ownership components.  Their middle unions are pairwise disjoint, while (H) owns only the complementary targets.  Hence (Z) remains conformally decomposable into three ordinary (B_m)-Gravers even after completion; its primitivity is genuinely augmented.

Each component has an individual conjugate-MSW completion, but those three factors need not coincide.  The obvious attempt to place all three in one aligned canonical MSW factor is impossible: the audited fixed MSW component hierarchy has linearly independent first-shadow effects, so no nonempty component subset is first-shadow neutral.  Any common completion must use a different, prepared factor state.

## 12. Where mesoscopic necessity is true, and where it is false

Theorem 10.2 proves that no universal mesoscopic support lower bound can hold for abstract shallow-neutral Graver vectors: six rows per sign suffice for every \(m\ge510\).  Three different, precisely scoped mesoscopic statements do remain true.

1. **Selector-cell architecture.**  A connected, reduced, support-feasible composite of (s) coefficient-one Petr--Turek selector cells satisfies

   \[
   s\ge\left\lceil\frac{m+1}{2}\right\rceil.
   \tag{12.1}
   \]

   A selector cell has cyclic-order diameter at most two.  A connected (s)-cell union has diameter at most (2s), whereas two same-sign packing rows require distance at least (m+1) by (9.5).  If \(2s\le m\), each sign has at most one surviving row; equality of their middle columns makes the reduced trade zero.

2. **Common-context suspension.**  Equation (9.8) forces \(\Omega(t)\) order-dependent adjacent swaps after (t) suspension steps.

3. **Raw effect preservation.**  Equation (7.10) forces at least

   \[
   \left\lceil
   \frac{(M-2)!/2}{\lfloor(M+3)(M+2)/6\rfloor}
   \right\rceil
   \]

   support-feasible pieces to reproduce the literal iterated depth-two amplitude.

These are architecture-specific results.  They do not imply an \(\Omega(m)\) lower bound for arbitrary applicable nonlocal Graver moves.  Conversely, the bounded triangle does not refute a mesoscopic lower bound for **common exact completion**: its sole unresolved property is simultaneous containment in one factor.

## 13. Energy, MWB, and exact implication scope

The first-wave lifted-Graver descent theorem remains valid: if an exact factor \(x^\star\) has lower weighted floor energy than (x), a conformal augmented-Graver summand toward \(x^\star\) is applicable at (x) and decreases the energy by at least a \(1/\operatorname{Cat}_m\) fraction of the comparison gap.

The present constructions do not supply such a better endpoint.

- A nonzero (B_{m-2})-effect does not determine the sign of the weighted floor-energy change.  The two endpoints may even tie.
- Each universal two-for-two component is an applicable controlled Graver, but it changes the first shadow and need not decrease any chosen objective.
- The dispersed triangle is shallow neutral, but its common exact endpoint is unproved.
- The signed iterated suspension supplies lattice and Graver vectors, but Theorem 6.4 prevents positive conformal extraction which remains top-two neutral at the first step, and Theorems 7.2-7.3 prevent preservation of its raw deeper effect thereafter.

Thus no monotone descent from an arbitrary factor follows from this lane.  The comparison-based Graver theorem still needs a positive better factor, and the bounded triangle still needs a common completion.

All results here are unlabelled.  They do not construct a common balanced nested owner resolution.  They imply neither MWB nor labelled synchronization.  Even an all-dimensional depth-two factor circuit would be a local structural advance, not the fixed-Gaussian-window theorem required by the exact remaining synchronization brief.

## 14. Independent audit ledger

The decisive steps were independently rederived.  The following are the exact audit conclusions.

1. **Ordinary versus augmented Graver.**  For a squarefree support-feasible trade, conformal \(B_m\)-kernel subvectors are precisely ownership-component unions.  Connectedness is therefore equivalent to ordinary \(B_m\)-Graver status.  A disconnected union may nevertheless be stacked or lifted-Graver when its lower-row cancellation is subset-minimal.  The report never identifies these two notions.

2. **Iterated suspension constants.**  The support multiplier at the step \(j\to j+1\) is \(2j+1\), while the surviving depth-two coefficient multiplier is \(j-1\).  Thus (5.6) and the scalar \((M-2)!/2\) in (5.8) are exact.  The \(2^{M-4}\) one-label-per-pair sectors are disjoint.

3. **Deletion projection.**  The five possible top-row incidence triples are exactly

   \[
   (1,0,0),(1,0,0),(0,1,0),(0,1,0),(1,1,1),
   \]

   so the signs \(+,+,-\) in (6.1) are correct.  Connected old ownership then forces one common descendant multiplicity \(k\).

4. **The \(k=1\) seed obstruction.**  The direct five-case proof following (6.5) was checked separately.  It uses only the displayed three old target starts and the five \(\kappa\)-classes.  It is not a computer search.  Crucially, \(\kappa\) records the simultaneous \(B_5/B_4\) signature.  The proof rules out a one-point section preserving both rows for the fixed \(P_4\) orientation; it makes no claim about a \(B_5\)-kernel section which changes \(B_4\).

5. **Capacity constant.**  One occurrence of an \((M-q)\)-target supplies exactly \(q+1\) distinct middle supersets, not \(q\) or \(q+2\).  The total number of middle supersets is \(\binom{M+q+1}{q}\).  For a difference of two packing loads, the bound is \(L_{M,q}\), not \(2L_{M,q}\), because both loads lie in the same interval \([0,L_{M,q}]\).

6. **Dimension-six saturation.**  At \(M=6\), the raw coefficient is exactly the capacity \(12\).  Equality forces all \(36\) middle supersets of each branch target to be used.  The common six-set \(E\cup A\cup B\) therefore has one owner containing four distinct cyclic four-subintervals inside one cyclic six-interval, whereas only three exist.  This validates the sharper \(M=6\) obstruction.

7. **Dispersed triangle constants.**  The \(6,12,6\) cross-context row-pair counts, the collision bound

   \[
   \frac{504}{m}
   +\frac{450}{\binom m2}
   +\frac{384}{m(m-3)},
   \]

   and the deeper-vanishing probability \(1/(m-3)\) give the exact total \(509/m<1\) for \(m\ge510\).

8. **Triangle row distinctness.**  The unique full \(K\)-run and its outside-neighbor pair separate the three contexts even under reversal.  Within one context, transposition invariance or cross-equality would contradict the packing property.  Hence the successful vector is exactly six-for-six, and its three stated ownership components do not merge.

9. **Triangle primitivity.**  Its first-shadow effects are

   \[
   f_y-f_x,\qquad f_z-f_y,\qquad f_x-f_z
   \]

   on six distinct targets.  Empty and full are the only subset zero-sums.  Therefore (10.15)-(10.17) are valid.

10. **Applicability caveat.**  Support feasibility of the six-for-six packet is proved.  Common exact-factor completion is not.  The report marks the six-row extension lemma unproved and makes no endpoint, descent, MWB, or synchronization claim from it.

The audit also corrects five tempting overstatements.

- The all-dimensional \(g_M\) is Graver for the stacked top-two matrix; it is not proved ordinary-\(B_M\) Graver.
- The raw signed suspension is not a factor move.
- The lower-shadow amplitude obstruction rules out literal effect preservation, not every renormalized or adaptive suspension.
- The constant-support triangle refutes a universal mesoscopic bound for abstract lifted Gravers.
- Failure of residual completion is not called a semigroup hole unless rational-cone membership is separately proved.

## 15. Exact unproved ledger

Only the following mathematical gates remain open in this lane.

### U1. Six-row extension

For at least one successful dispersed triangle in every sufficiently large dimension, prove

\[
\mathbf1-B_m\mathbf1_N
\in B_m\mathbb Z_{\ge0}^{\Omega_m}.
\tag{U1}
\]

This would produce a bounded applicable first-shadow-neutral lifted-Graver for every \(m\ge510\).  It would not make the move an ordinary connected circuit.

### U2. Renormalized state-level suspension

Starting with a connected applicable depth-two circuit in dimension \(m\), construct in dimension \(m+1\) a support-feasible, exactly completable circuit or primitive packet which:

1. reroutes an old middle occurrence on every inherited unbalanced gain cycle;
2. chooses pointing phases jointly across different old owners;
3. creates the same-sign distance required by (9.5);
4. keeps every lower coordinate within the capacity (7.1), rather than multiplying it indefinitely by \(m-1\); and
5. preserves a nonzero primitive deeper signal.

No theorem in the current framework supplies these five properties simultaneously.  The natural antipodal orbit, its conformal Graver decomposition, a uniform product, a literal common context, and the fixed MSW component cube are all ruled out by the proved results above.

## Final conclusion

The signed incidence-lattice problem is solved as far as suspension and primitive extraction are concerned:

\[
\boxed{
\begin{gathered}
\text{the }m=4\text{ circuit suspends linearly to every }M,\text{ and every}\\
\text{suspended relation contains a depth-active top-two stacked Graver.}
\end{gathered}}
\]

The positive problem has an exact structural obstruction:

\[
\boxed{
\begin{array}{c}
P_4w_4\text{ has no nonzero conformal support-feasible top-two relation;}\\
\text{the twice-suspended raw depth-two effect is nonpositive already at }M=6;\\
\text{fixed-depth raw amplitudes thereafter grow factorially past packing capacity.}
\end{array}}
\]

There is nevertheless a bounded positive primitive at the partial-packing level:

\[
\boxed{
m\ge510
\Longrightarrow
\exists\,Z\text{ six-for-six},\
B_mZ=B_{m-1}Z=0,\
B_{m-2}Z\ne0,\
Z\in\operatorname{Gr}\binom{B_m}{B_{m-1}}.}
\]

Its common exact-factor completion is unproved.  Therefore the correct endpoint of this lane is not an all-\(m\) positive suspension theorem, but a sharp dichotomy:

\[
\boxed{
\text{Graver control is available; positive exact completion and
state-dependent owner rerouting are the remaining gates.}}
\]
