# Cross-audit of aligned interval packets and exact floor energy

Date: 2026-07-25

## 0. Verdict

This note audits the interval packets in
`MATH_ATTACK_S11_ADJACENT_PRIORITY_ALIGNED_SWITCH_20260725.md` against
the rankwise-flat priority cube in
`PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md`.

The conclusions are as follows.

1. Every monotone threshold on one aligned open path is a legal integral
   token matching: every lower root is saturated once and no middle owner
   is repeated.  Thresholds may be chosen independently on all paths of
   all disjoint adjacent priority blocks.  The total extra physical-row
   boundary count is

   \[
   O\!\left(\frac{W\log ^2m}{m}\right)=o(W/H)
   \quad\text{whenever}\quad H=o(m/\log ^2m).
   \]

2. The two factor couplings used in the source reports are different.
   All-rank energy-flatness uses the orientation-preserving choice
   \(F_B=\tau F_A\).  Long *alternating paths* use
   \(F_B=\theta\operatorname{rev}F_A\).  Under the first choice the
   affected overlay has only parallel digons and one-lower-root open
   paths.  Crucially, this does **not** prevent grouping those independent
   components into one maximal physical \(D_j\)-interval packet.  Section
   7 proves that every such grouped packet is legal, costs at most two
   new selected-row runs (at most four raw \(0/1\) boundary edges), and
   has nonnegative Gram interaction at every upper depth.

3. There is nevertheless genuine overlap at the first upper depth.
   Reversal preserves the two-sided length-\((m+1)\) window.  Hence the
   *complete* reverse-correlated adjacent swap has the same depth-one
   floor energy at its two endpoints.  At every deeper signed rank the
   reversal changes the flag window, and no endpoint permutation or
   energy equality follows.

4. Interior occurrence cancellation is linear.  Floor-quadratic energy is
   not linear.  For packet increments \(d_K\), the exact missing term is

   \[
   \sum_{K<L}\langle d_K,d_L\rangle_w.
   \]

   The exact corridor remainder is the corresponding discrete-slope
   congestion term in (5.5) below.  Neither remainder can be discarded.

5. For the first adjacent block \(j=1\), the first-upper packet Gram
   entries are nonnegative.  Complete endpoint energy-flatness then gives
   a sharp dichotomy: either one whole aligned path strictly decreases the
   exact factorial floor excess, for at most two new runs, or
   the entire whole-path side cube is rankwise energy-flat.  The rigid
   alternative is characterized exactly in Theorem 4.1.

6. The analogous corridor dichotomy is also exact.  Either one whole path
   lowers first-upper support excess by at least one, in which case the
   base-16 all-depth geometric corridor drops by at least

   \[
   \frac{101}{225}
   \]

   for at most two new row boundaries, or the entire whole-path side cube
   is first-upper-corridor flat.  This does not prove small unweighted
   defect at every Gaussian depth.

Thus interval legality and the total boundary budget are closed.  For the
orientation-preserving grouped packets, the endpoint gap vanishes at all
ranks and the Gram term is nonnegative, yielding the exact descent/flatness
dichotomy in Section 7.  For the reverse-correlated long-path packets, the
remaining multidepth term is the explicit packet Gram/congestion term
together with the deeper-rank endpoint gap.

## 1. Exact legality of all interval thresholds

Let \(M\) and \(N\) be the two first-avoided token matchings before and
after swapping adjacent pairs \(A,B\).  They agree outside the changed
lower family \(D_j\).  Write an open component of their labelled overlay
as

\[
 y_0,S_1,y_1,S_2,\ldots,S_b,y_b,
\]

where the old edges are \(y_{i-1}S_i\) and the new edges are
\(S_i y_i\).

### Lemma 1.1 (threshold legality, including the unchanged matching)

For each \(r\in\{0,1,\ldots,b\}\), select the old edge at \(S_i\) for
\(i\le r\) and the new edge at \(S_i\) for \(i>r\).  This selection,
together with every edge on which \(M,N\) agree, saturates every lower
root once and is middle-simple.  Choices on distinct overlay components
are independent.

#### Proof

Every \(S_i\) receives exactly one edge.  At an internal owner \(y_i\),
the two potentially chosen edges are the new edge at \(S_i\), requiring
\(i>r\), and the old edge at \(S_{i+1}\), requiring \(i+1\le r\).
These conditions are incompatible.  The two endpoint owners have only
one incident overlay edge.

Distinct overlay components have disjoint middle vertices.  Finally, a
middle owner used by an unchanged edge cannot occur on an old changed
edge, by middle simplicity of \(M\), and cannot occur on a new changed
edge, by middle simplicity of \(N\).  Hence there is no hidden collision
with the unchanged part.  \(\square\)

For the reverse-correlated factors, each component is a maximal physical
\(D_j\)-interval in one old row and the reverse interval in one new row.
The threshold therefore deletes at most one selected interval from the
old row and inserts at most one interval into the new row.  Its extra run
cost is at most two.  Equivalently it toggles at most two physical
intervals and creates at most four raw \(0/1\) row-boundary edges.

The same legality holds simultaneously for disjoint adjacent blocks.  To
see the only point not covered by Lemma 1.1, define the middle-owner
stratum of the block at positions \(j,j+1\) by

\[
 \mathcal Y_j=\{Y:Y\cap P_h\ne\varnothing\ (h<j),\quad
 Y\cap P_j=\varnothing\text{ or }Y\cap P_{j+1}=\varnothing\}.
\tag{1.1}
\]

Every old or new owner above \(D_j\) belongs to \(\mathcal Y_j\).  If
\(j<k\), every member of \(\mathcal Y_k\) meets both pairs at positions
\(j,j+1\), whereas every member of \(\mathcal Y_j\) avoids one of them.
Thus

\[
 \mathcal Y_j\cap\mathcal Y_k=\varnothing.
\tag{1.2}
\]

So path thresholds in distinct disjoint priority blocks cannot collide at
a middle owner.

### Proposition 1.2 (total packet-boundary budget)

Let \(K_j\) be the number of aligned paths for the block at positions
\(j,j+1\), and take any family of disjoint adjacent blocks.  If

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1},
 \qquad
 A_m=\binom{2m-1}{m-1},
\]

then, with \(t=\lceil20\log m\rceil\),

\[
 \sum_jK_j
 \le R_m t(t+1)
   +4C\sqrt m\,A_m(3/4)^t
 =O\!\left(\frac{W\log ^2m}{m}\right),
\tag{1.3}
\]

where \(C\) is the absolute constant in the audited category-tail bound.
Every simultaneous threshold choice adds at most

\[
 2\sum_jK_j
 =O\!\left(\frac{W\log ^2m}{m}\right)
\tag{1.4}
\]

additional selected-row runs, and at most

\[
 4\sum_jK_j
 =O\!\left(\frac{W\log ^2m}{m}\right)
\tag{1.5}
\]

raw \(0/1\) row-boundary edges.

#### Proof

Use \(K_j\le2jR_m\) for \(j\le t\), and
\(K_j\le |D_j|\le C\sqrt m A_m(3/4)^{j-1}\) for \(j>t\).
Summing the first estimate over all positions gives
\(R_mt(t+1)\); summing the geometric tail gives the second term in
(1.3).  Equations (1.4)--(1.5) follow from the
two-run/four-raw-edge cost of one path.
Since

\[
 R_m=\frac{m+1}{2(2m+1)(2m-1)}W,
\]

(1.3) has the displayed order.  The hypothesis
\(H=o(m/\log ^2m)\) makes both (1.4) and (1.5) \(o(W/H)\).
\(\square\)

For the first adjacent block \(j=1\), there is exactly one reverse
exchange path in every \(F_A\)-row:

\[
 K_1=R_m.
\tag{1.6}
\]

Indeed, deleting the two \(B\)-positions from a cyclic row leaves two
common-coordinate arcs of total length \(2m-3\).  Exactly one arc has
length at least \(m-1\), so exactly one nonempty interval of
length-\((m-1)\) starts avoids \(B\).  Since

\[
 |D_1|=\frac m2R_m,
\]

the exact mean path length is \(m/2\), and at least half of the changed
tokens lie on paths of length at least \(m/4\).

## 2. Which endpoint cube is energy-flat?

Let \(R=[n]\setminus(A\cup B)\), and let
\(\theta:Q_A\to Q_B\) fix \(R\) and exchange the omitted pair names.

The pair-symmetric flat cube uses

\[
 F_B=\theta F_A.
\tag{2.1}
\]

The aligned interval construction uses

\[
 F_B=\theta\operatorname{rev}F_A.
\tag{2.2}
\]

These couplings cannot be identified.

### Lemma 2.1 (pair symmetry has no long affected component)

Under (2.1), every affected overlay component is either a parallel digon
on one lower root or an open path with one lower root.  In particular,
there is no open affected path with two or more lower roots.

#### Proof

Let \(f(S)\) be the old middle owner of \(S\in D_j\).  Pair symmetry
makes its new owner \(\theta f(S)\).  Suppose an old owner and a new owner
are shared:

\[
 Y=f(S)=\theta f(T).
\]

Every shared owner avoids \(A\cup B\), so \(\theta Y=Y\).  Hence
\(f(T)=\theta Y=Y=f(S)\), and injectivity of the old owner map gives
\(T=S\).  If \(f(S)\) also avoids \(B\), then it is fixed by \(\theta\)
and the two labelled edges form a parallel digon.  Otherwise the old and
new owners are distinct and exclusive, giving a one-lower-root open path.
\(\square\)

Thus all-rank pair-symmetric flatness and nontrivial long aligned paths do
not occur from the same factor coupling.

There is one important rank at which reversal disappears.

### Lemma 2.2 (first-upper reversal invariance)

Let

\[
 S_i=I_\pi(i,m-1)
\]

be a lower root in an old row.  Its first upper flag is

\[
 U_1^{\rm old}(S_i)=I_\pi(i-1,m+1).
\]

In the reversed \(\theta\)-row, the token over \(\theta S_i\) has

\[
 U_1^{\rm new}(\theta S_i)
 =\theta I_\pi(i-1,m+1).
\tag{2.3}
\]

Consequently the two complete adjacent-swap endpoints for (2.2) have
first-upper load vectors which differ only by the target permutation
\(\theta\) on the affected first-avoided stratum.  They have identical
factorial floor excess and identical floor corridor.  Their first lower
flags are identical rootwise.

#### Proof

The length-\((m+1)\) flag consists of \(S_i\) together with both cyclic
neighbors of this length-\((m-1)\) window.  Reversal exchanges those two
neighbors and leaves their union unchanged, proving (2.3).

The roots assigned to \(A\) before the priority swap are sent by
\(\theta\) to the roots assigned to \(B\) afterwards; the old \(B\)
stratum is similarly sent to the new \(A\) stratum.  Earlier and later
first-avoided strata are disjoint from this upper-target stratum.  Thus
the complete affected load is permuted, while the remaining load is
unchanged.  Finally \(L_1(S)=S\).  \(\square\)

For \(q\ge2\), the relevant windows are instead

\[
 U_q^{\rm old}=I_\pi(i-1,m+q),
 \qquad
 U_q^{\rm rev}=\theta I_\pi(i-q,m+q),
\tag{2.4}
\]

and

\[
 L_q^{\rm old}=I_\pi(i+q-1,m-q),
 \qquad
 L_q^{\rm rev}=\theta I_\pi(i,m-q).
\tag{2.5}
\]

These are not target permutations of one another rootwise or globally.
Their differences telescope only through interiors of consecutive
selected starts, leaving the audited boundary columns.  Thus the endpoint
energy-flat theorem applies to the reverse-correlated construction at
\(q=1\), not at the deeper signed ranks.

## 3. Exact floor-quadratic law for arbitrary thresholds

Fix one signed rank \(a\), with target set of size \(K_a\), total load
\(T_a\), and

\[
 T_a=c_aK_a+\delta_a,
 \qquad 0\le\delta_a<K_a.
\]

The factorial floor excess is

\[
 \Phi_a(x)
 =\frac12\sum_T(x_T-c_a)(x_T-c_a-1).
\tag{3.1}
\]

Equivalently, for \(\lambda_a=T_a/K_a\) and
\(B_a=\delta_a(K_a-\delta_a)/K_a\),

\[
 2\Phi_a(x)=\|x-\lambda_a\mathbf1\|_2^2-B_a.
\tag{3.2}
\]

For a path \(K\), choose any legal threshold and let \(d_{K,a}\) be its
load increment relative to the all-old endpoint.  It has rankwise mass
zero.  Let \(\mu_a\) be the old load and put

\[
 D_a=\sum_Kd_{K,a}.
\]

### Theorem 3.1 (exact deterministic packet energy)

For arbitrary simultaneous threshold choices and arbitrary nonnegative
rank weights,

\[
 \boxed{
 \Phi_w(\mu+D)-\Phi_w(\mu)
 =\sum_K A_K+\sum_{K<L}G_{KL},}
\tag{3.3}
\]

where

\[
 A_K=\sum_aw_a\left(
 \langle\mu_a,d_{K,a}\rangle
 +\frac12\|d_{K,a}\|_2^2\right),
\tag{3.4}
\]

and

\[
 G_{KL}=\sum_aw_a\langle d_{K,a},d_{L,a}\rangle.
\tag{3.5}
\]

There is no additional floor term in the difference.  The exact floor
constants cancel because every \(d_{K,a}\) has zero mass.

#### Proof

At one rank,

\[
 \Phi_a(\mu+D)-\Phi_a(\mu)
 =\langle\mu,D\rangle+\frac12\|D\|_2^2.
\]

Expand \(D=\sum_Kd_K\) and sum the signed ranks.  \(\square\)

After cancelling equal removed and inserted occurrences inside one packet,
its entries lie in \(\{-1,0,1\}\).  If \(\mathcal P_{K,a}\) and
\(\mathcal O_{K,a}\) are its inserted and removed targets and

\[
 r_{K,a}=|\mathcal P_{K,a}|=|\mathcal O_{K,a}|
 =\frac12\|d_{K,a}\|_2^2,
\]

then

\[
 A_K=\sum_aw_a\left(
 \sum_{T\in\mathcal P_{K,a}}\mu_T
 -\sum_{T\in\mathcal O_{K,a}}\mu_T+r_{K,a}\right).
\tag{3.6}
\]

For a complete long aligned path,

\[
 r_{K,(q,-)}=q-1,
 \qquad r_{K,(q,+)}=q+1,
\]

so the exact self term is \(2q\) at depth \(q\).  Thus a family of
packets is a strict floor-quadratic descent exactly when

\[
 \sum_{K,a}w_a\left(
 \sum_{T\in\mathcal O_{K,a}}\mu_T
 -\sum_{T\in\mathcal P_{K,a}}\mu_T\right)
 >\sum_{K,a}w_ar_{K,a}+\sum_{K<L}G_{KL}.
\tag{3.7}
\]

The last term is the missing congestion/cancellation term.

More explicitly, at one target let \(p_T\) packets insert and \(r_T\)
packets remove an occurrence.  Then

\[
 \sum_{K<L}d_K(T)d_L(T)
 =\binom{p_T}{2}+\binom{r_T}{2}-p_Tr_T.
\tag{3.8}
\]

At a sector in which insertion and removal supports are disjoint, (3.8)
is nonnegative and is exactly the same-sign boundary congestion.

There is also an exact independent-threshold expectation identity.  If
the threshold variables are independent, \(\bar d_K=\mathbb E d_K\),
and \(Q_w=2\Phi_w\), then

\[
 \boxed{
 \mathbb E Q_w
 =\left\|\mu+\sum_K\bar d_K-\lambda\right\|_w^2-B_w
 +\sum_K\left(
 \mathbb E\|d_K\|_w^2-\|\bar d_K\|_w^2\right).}
\tag{3.9}
\]

The first term in (3.9) can lie below zero because the mean load is
fractional.  This is precisely the integer-floor compensation seen in the
global priority cube; it is not permission to omit (3.5).

## 4. The sharp first-upper quadratic dichotomy

Now take the first adjacent block, \(j=1\), with reverse-correlated
factors.  Let \(\mathcal K\) be its maximal aligned paths.  For a whole
old-to-new side switch on path \(K\), write

\[
 z_K={\bf1}_{\mathcal P_K}-{\bf1}_{\mathcal O_K}
\]

at the first upper rank.  If the path has \(b_K\) lower roots, then

\[
 r_K:=|\mathcal P_K|=|\mathcal O_K|=\min\{b_K,2\},
 \qquad \|z_K\|_2^2=2r_K.
\tag{4.1}
\]

For \(b_K\ge2\), these are precisely the left- and right-endpoint
transfers.  A nonempty proper threshold suffix contains the right endpoint
but not the left endpoint, so at \(q=1\) it makes exactly one
removed-to-inserted transfer; the full side switch makes both.  When
\(b_K=1\), the two path ends belong to the same token and there is only
one transfer.  Thus the \(2+2\) boundary census applies to whole paths of
length at least two, not to singleton paths or proper threshold suffixes.

Every removed target meets \(B\) and avoids \(A\); every inserted target
meets \(A\) and avoids \(B\).  Therefore, for distinct paths,

\[
 G_{KL}:=\langle z_K,z_L\rangle
 =|\mathcal P_K\cap\mathcal P_L|
  +|\mathcal O_K\cap\mathcal O_L|\ge0.
\tag{4.2}
\]

Let \(\mu\) be the old first-upper load and define the exact one-path
factorial-floor change

\[
 \Delta_K
 :=\Phi_1^+(M\oplus K)-\Phi_1^+(M)
 =\sum_{T\in\mathcal P_K}\mu_T
  -\sum_{T\in\mathcal O_K}\mu_T+r_K.
\tag{4.3}
\]

### Theorem 4.1 (flat endpoint decomposes into descent or rigidity)

The complete adjacent swap satisfies

\[
 \boxed{
 0=\sum_{K\in\mathcal K}\Delta_K
   +\sum_{K<L}G_{KL}.}
\tag{4.4}

Consequently exactly one of the following holds.

1. Some whole aligned path has \(\Delta_K\le-1\).  Switching that one
   path strictly lowers the exact first-upper factorial floor excess and
   adds at most two row boundaries.
2. For every path \(K\),

   \[
   \Delta_K=0,
   \tag{4.5}
   \]

   and for every two distinct paths

   \[
   G_{KL}=0.
   \tag{4.6}
   \]

   In this case every whole-path side choice has exactly the same
   first-upper factorial floor excess as both endpoints.

#### Proof

Lemma 2.2 makes the two complete endpoint load histograms permutations,
so their floor excesses are equal.  Apply (3.3) to the complete family to
obtain (4.4).  Every \(G_{KL}\) is nonnegative.  If no \(\Delta_K\) is
negative, all terms in (4.4) are nonnegative and hence all vanish.  Under
(4.5)--(4.6), applying (3.3) to any subset of paths gives zero change.
The converse is immediate.  \(\square\)

Thus the exact rigid alternative says both that same-sign boundary targets
are disjoint between paths and that every path has the floor-corrected
endpoint balance

\[
 \sum_{T\in\mathcal O_K}\mu_T
 -\sum_{T\in\mathcal P_K}\mu_T=r_K.
\tag{4.7}
\]

For fair independent whole-side bits, put

\[
 V=\sum_K\|z_K\|_2^2,
 \qquad A=\left\|\sum_Kz_K\right\|_2^2.
\]

Then \(A-V=2\sum_{K<L}G_{KL}\ge0\), and for doubled floor excess
\(Q=2\Phi\),

\[
 \boxed{
 \mathbb E Q(\text{child})
 =Q(M)-\frac{A-V}{4}.}
\tag{4.8}
\]

Equation (4.8) is fully consistent with global endpoint flatness.  The
global priority cube has one bit for the whole block; (4.8) concerns the
strictly larger cube of individual aligned-path sides.

At \(q\ge2\), define \(\Delta_K^H\) and \(G_{KL}^H\) using all desired
signed-rank weights.  The exact identity is only

\[
 \Phi_H(N)-\Phi_H(M)
 =\sum_K\Delta_K^H+\sum_{K<L}G_{KL}^H.
\tag{4.9}
\]

The left side need not vanish and the deeper Gram entries need not be
nonnegative.  Equation (4.9), rather than zero, is the explicit remaining
multidepth term.

## 5. Exact corridor law and a floor-corrected geometric descent

For the exact floor \(c\), put

\[
 \psi_c(u)=(c-u)_++(u-c-1)_+,
 \qquad \mathcal C_c(\mu)=\sum_T\psi_c(\mu_T).
\tag{5.1}
\]

Define the forward discrete slope

\[
 s_c(u)=\psi_c(u+1)-\psi_c(u)
 =\begin{cases}
 -1,&u\le c-1,\\
 0,&u=c,\\
 1,&u\ge c+1.
 \end{cases}
\tag{5.2}
\]

For an integral net increment \(D\), define

\[
 g_c(u,D)=
 \begin{cases}
 \displaystyle\sum_{h=0}^{D-1}s_c(u+h),&D>0,\\[2mm]
 \displaystyle-\sum_{h=D}^{-1}s_c(u+h),&D<0,\\[2mm]
 0,&D=0.
 \end{cases}
\tag{5.3}
\]

Then the exact simultaneous corridor change is

\[
 \boxed{
 \Delta\mathcal C_c=\sum_Tg_c(\mu_T,D_T).}
\tag{5.4}
\]

If \(p_T\) packets insert and \(r_T\) packets remove at \(T\), the exact
remainder beyond the isolated packet marginals is

\[
 \boxed{
 R_{c,T}
 =\psi_c(\mu_T+p_T-r_T)-\psi_c(\mu_T)
 -p_T[\psi_c(\mu_T+1)-\psi_c(\mu_T)]
 -r_T[\psi_c(\mu_T-1)-\psi_c(\mu_T)].}
\tag{5.5}
\]

This is the corridor analogue of the Gram term.  It can be nonzero even
when every packet is individually a boundary-only move.

At the first upper rank, \(c=0\).  In the separated sectors of the first
block, let \(p_T\) denote insertions on a new-sector target and \(r_T\)
removals on an old-sector target.  Since \(r_T\le\mu_T\), (5.4) becomes

\[
 \boxed{
 \Delta\mathcal C_0
 =\sum_{T\in\mathrm{new}}
   \left(p_T-\mathbf1_{\{\mu_T=0,\ p_T>0\}}\right)
  -\sum_{T\in\mathrm{old}}
   \min\{r_T,\mu_T-1\}.}
\tag{5.6}
\]

For comparison, the exact factorial-floor change is

\[
 \boxed{
 \Delta\Phi_0
 =\sum_{T\in\mathrm{new}}
   \left(p_T\mu_T+\binom{p_T}{2}\right)
  -\sum_{T\in\mathrm{old}}
   \left(r_T(\mu_T-1)-\binom{r_T}{2}\right).}
\tag{5.7}
\]

Equations (5.6)--(5.7) display the exact restitution lost when several
packets use the same boundary target.

### Theorem 5.1 (first-upper corridor descent or flatness)

For the whole-path side cube of the first adjacent block, either

1. some single path switch decreases \(\mathcal C_1^+\) by at least one;
   or
2. every whole-path side choice has exactly the same
   \(\mathcal C_1^+\) as both complete endpoints.

For one path \(K\), its exact first-upper change is

\[
 \Delta_K\mathcal C_1^+
 =|\{P\in\mathcal P_K:\mu_P\ge1\}|
  -|\{O\in\mathcal O_K:\mu_O\ge2\}|.
\tag{5.8}
\]

#### Proof

Let

\[
 F(I)=\mathcal C_1^+\!\left(\mu+\sum_{K\in I}z_K\right)
       -\mathcal C_1^+(\mu).
\]

At each first-upper target all nonzero packet increments have one sign,
by the exclusive \(A/B\) sectors.  Since \(\psi_0\) is convex on the
integers, \(F\) is a normalized supermodular set function.  Therefore

\[
 F(\mathcal K)\ge\sum_KF(\{K\}).
\]

Lemma 2.2 gives \(F(\mathcal K)=0\).  If some singleton is negative, the
first alternative holds.  Otherwise every singleton is zero.  For every
\(I\), supermodularity gives \(F(I)\ge0\), while

\[
 F(I)+F(\mathcal K\setminus I)
 \le F(\mathcal K)+F(\varnothing)=0.
\]

Hence every \(F(I)=0\).  Formula (5.8) is the unit-step specialization of
(5.6).  \(\square\)

The first alternative has a literal all-depth consequence.  Define

\[
 \Lambda_H^{(16)}
 =\mathcal C_1^+
  +\sum_{q=2}^H16^{1-q}
    (\mathcal C_q^-+\mathcal C_q^+).
\tag{5.9}
\]

For one aligned path,

\[
 |\Delta(\mathcal C_q^-+\mathcal C_q^+)|\le4q.
\]

Thus a first-upper drop of one gives

\[
 \begin{aligned}
 \Delta\Lambda_H^{(16)}
 &\le-1+4\sum_{q=2}^{\infty}\frac q{16^{q-1}}\\
 &=-1+4\left(\frac1{(1-1/16)^2}-1\right)\\
 &=-\frac{101}{225}.
 \end{aligned}
\tag{5.10}
\]

The row-boundary increase is at most two.  If the stronger two-overload
to-two-hole condition holds, the source report's base-8 constant
\(-38/49\) remains valid.  One must not sum that stronger claim over
overlapping packets without either disjoint first-upper boundary supports
or sequential rechecking of the endpoint loads.

## 6. Precise proved and unproved boundary

The following points are now exact.

1. All aligned path thresholds, including simultaneous choices in
   disjoint adjacent blocks, are lower-saturating and middle-simple.
2. Their total extra row-boundary count is \(o(W/H)\) throughout the
   current Gaussian window.
3. The complete reverse-correlated swap is energy-flat at depth one but
   not at deeper signed ranks.
4. At first upper depth for \(j=1\), one obtains either a literal
   two-boundary floor-quadratic/corridor descent or the exact flat-cube
   rigidity in Theorems 4.1 and 5.1.
5. For arbitrary multidepth threshold choices, the exact remaining terms
   are (3.5), (4.9), and (5.5).  Histogram permutation of the two complete
   endpoints does not annihilate them.

For the reverse-correlated long-path construction, a standard-weight
multidepth descent remains unproved because the deeper-rank endpoint gap
in (4.9) has no favorable sign.  Section 7 gives an all-rank
descent/flatness dichotomy for a different, orientation-preserving grouped
packet family.  Its unresolved case is the flat alternative itself, which
may still have large defect.  The base-16 geometric corridor is also too
weak to imply \(o(W)\) unweighted defect separately at every Gaussian
depth.  No constant-one conclusion is drawn.

## 7. Orientation-preserving maximal-interval packets

There is a second packetization which retains the all-rank flat endpoint
theorem.  Take the orientation-preserving pair-symmetric factors

\[
 F_B=\tau F_A,
\tag{7.1}
\]

where \(\tau\) exchanges \(A,B\) and fixes
\(R=[n]\setminus(A\cup B)\) pointwise.  Although Lemma 2.1 says that the
labelled overlay components are only digons and one-root paths, those
components can be grouped without losing legality.

In every row of \(F_A\), partition the affected starts into maximal
physical \(D_j\)-intervals.  For such an interval \(K\), its paired row
in \(F_B\) is the coordinatewise image \(\tau\pi\).  Because every
affected root lies in \(R\), the same starts, in the same orientation,
form the corresponding interval in \(\tau\pi\).  Define the packet switch
on \(K\) by replacing the old token by the new token at every root of
that interval.

### Theorem 7.1 (arbitrary interval-packet choices are legal)

Every subset of the maximal \(D_j\)-interval packets gives an integral
lower-saturating, middle-simple token matching.  Each selected packet adds
at most two selected-row runs and at most four raw \(0/1\) boundary edges.
The assertion remains true
simultaneously over disjoint adjacent priority blocks.

#### Proof

It is enough to prove the stronger rootwise assertion.  Let \(f(S)\) be
the old owner of an affected root \(S\).  Its new owner is
\(\tau f(S)\).  If an old owner at \(S\) equals a new owner at \(T\),
then the common owner avoids \(A\cup B\).  It is fixed by \(\tau\), so

\[
 f(S)=\tau f(T)=f(T).
\]

Injectivity of the old owner map gives \(S=T\).  Thus no choices at two
different roots can collide.  At the same root exactly one of the two
tokens is selected, including when their owners coincide in a parallel
digon.  Unchanged owners are excluded exactly as in Lemma 1.1.  This
proves lower saturation and middle simplicity for arbitrary rootwise
choices, hence for interval packets.

Switching one whole interval deletes at most one selected interval in the
old row and inserts at most one in the paired new row, so its row-boundary
cost is at most two.  Distinct adjacent blocks have the disjoint owner
strata (1.2), completing the simultaneous assertion.  \(\square\)

The total number of these packets is exactly the interval count already
bounded in Proposition 1.2.  Hence the total boundary budget of an
arbitrary packet side choice is still

\[
 O\!\left(\frac{W\log ^2m}{m}\right)=o(W/H).
\tag{7.2}
\]

For the first block, the exact mass and interval bounds remain

\[
 |D_1|=\frac m2R_m,
 \qquad K_1\le2R_m.
\tag{7.2a}
\]

Thus these grouped packets have mean length at least \(m/4\), and at
least half of the affected roots lie in packets of length at least
\(m/8\).  This reconciles the two size statements: the labelled overlay
components are microscopic, but the legal physical interval packets are
macroscopic unions of those independent components.

### Lemma 7.2 (all-rank sector columns and nonnegative Gram)

For every affected root \(S\) and every depth \(q\),

\[
 L_q^{\rm new}(S)=L_q^{\rm old}(S),
 \qquad
 U_q^{\rm new}(S)=\tau U_q^{\rm old}(S).
\tag{7.3}
\]

Consequently every packet has zero lower-rank increment.  At an upper
rank, let \(a_{K,q}(T)\) be the number of old flags of packet \(K\) equal
to a target \(T\) which meets \(B\) and avoids \(A\).  Then

\[
 z_{K,q}
 =\sum_Ta_{K,q}(T)
   ({\bf e}_{\tau T}-{\bf e}_T),
\tag{7.4}
\]

where targets avoiding both pairs contribute zero.  Thus, for any two
packets and every upper depth,

\[
 \boxed{
 \langle z_{K,q},z_{L,q}\rangle
 =2\sum_Ta_{K,q}(T)a_{L,q}(T)\ge0.}
\tag{7.5}
\]

#### Proof

The two paired rows have the same orientation.  Their token flags are
coordinatewise \(\tau\)-images.  Every lower flag is a subset of
\(S\subseteq R\), proving the first part of (7.3).  An old upper flag
avoids \(A\).  If it also avoids \(B\), it is fixed by \(\tau\) and
cancels rootwise.  Otherwise it lies in the exclusive \(B\)-sector and
its image lies in the disjoint exclusive \(A\)-sector.  Aggregating equal
targets gives (7.4).  The two sectors are disjoint and \(\tau\) is a
bijection between them, giving (7.5).  \(\square\)

Let \(\Phi_w\) be any nonnegative weighted sum of the exact factorial
floor excesses over a fixed collection of signed depths.  Write

\[
 \delta_K
 =\Phi_w(M\oplus K)-\Phi_w(M)
 =\langle\mu,z_K\rangle_w+\frac12\|z_K\|_w^2,
\tag{7.6}
\]

and

\[
 G_{KL}=\langle z_K,z_L\rangle_w\ge0.
\tag{7.7}
\]

### Theorem 7.3 (all-rank interval-packet descent/flatness dichotomy)

For one pair-symmetric adjacent block,

\[
 \boxed{
 0=\sum_K\delta_K+\sum_{K<L}G_{KL}.}
\tag{7.8}
\]

Therefore exactly one of the following occurs.

1. Some single maximal-interval packet has \(\delta_K<0\).  It is a
   literal integral floor-quadratic descent for at most two new selected
   runs (four raw \(0/1\) boundary edges).
2. Every packet marginal and every packet Gram entry vanish:

   \[
   \delta_K=0\quad\text{for all }K,
   \qquad
   G_{KL}=0\quad\text{for all }K<L.
   \tag{7.9}
   \]

   In this case the entire maximal-interval packet cube is
   \(\Phi_w\)-flat.

If \(\Phi_w\) is an unweighted integer sum, a strict descent lowers
factorial floor excess by at least one, equivalently doubled floor energy
by at least two.

#### Proof

The complete set of interval packets is the bundled adjacent-priority
swap.  Pair symmetry permutes its upper load at every depth and fixes its
lower load, so its endpoint \(\Phi_w\)-difference is zero.  The exact
quadratic expansion (3.3) gives (7.8).  By (7.7), all Gram terms are
nonnegative.  If no marginal is negative, every term in (7.8) is
nonnegative, so all terms vanish.  Equation (3.3) then gives zero energy
change for every packet subset.  \(\square\)

For fair independent interval-packet bits, let

\[
 V=\sum_K\|z_K\|_w^2,
 \qquad
 A=\left\|\sum_Kz_K\right\|_w^2.
\]

Then \(A-V=2\sum_{K<L}G_{KL}\ge0\), and for doubled floor excess
\(Q_w=2\Phi_w\),

\[
 \boxed{
 \mathbb E Q_w(\text{child})
 =Q_w(M)-\frac{A-V}{4}.}
\tag{7.10}
\]

The single-packet conclusion in Theorem 7.3 is stronger than the mere
existence conclusion from (7.10).

Theorem 7.3 also holds verbatim for the union of the packet families from
all disjoint adjacent priority blocks.  Their lower increments vanish,
their upper first-avoided target strata are disjoint, and hence every
cross-block Gram entry is zero.  Selecting all packets gives the
all-block swapped corner of the pair-symmetric priority cube, whose
rankwise energies equal those of the base corner.  The total available
packet-boundary budget remains (7.2).

The same architecture has an exact corridor version.  At each target all
packet increments have one sign, so every nonnegative weighted sum of the
rankwise floor corridors is a normalized supermodular function of the
selected packet set.  Pair symmetry makes the two bundled endpoints
equal.  The proof of Theorem 5.1 therefore gives:

### Corollary 7.4 (all-rank corridor descent/flatness dichotomy)

For any nonnegative weighted sum of exact rankwise corridors, either one
maximal-interval packet strictly decreases that corridor objective, or
the whole interval-packet cube is corridor-flat.

This is an actual defect-reducing block switch outside the explicitly
classified flat alternative.  It does not show that the flat alternative
has small defect.  Pair-symmetric local factors can remain flat at a large
floor excess, so Theorem 7.3 by itself does not prove constant one.
