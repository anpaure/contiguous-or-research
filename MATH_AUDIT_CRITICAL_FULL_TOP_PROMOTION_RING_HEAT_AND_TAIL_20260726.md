# Critical full-top promotion rings: exact heat baseline, tag-census paths, and the negative-covariance gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad \lambda_q={W\over N_q}.
\tag{0.1}
\]

Let \(H\) be the greatest integer for which

\[
 \lambda_H\le M:=m+H.
\tag{0.2}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 T:=MN_H=W+E,\qquad 0\le E=O(WH/m)=o(W),
\tag{0.3}
\]

and

\[
 N_H=\Theta(W/m)=o(W/H).
\tag{0.4}
\]

For every top \(U\in\binom{[2m]}M\), the full-top catalogue contains all
promotion rings obtained from cyclic orders of \(U\).  One may attach a
tag \(d\in\{0,\ldots,H\}\) to a ring phase, with at most one tag \(H\)
per ring; the resulting symmetric chains are pairwise mask-disjoint inside
that ring.

This note gives a positive tag theorem and a negative heat theorem.

1. **The exact SCD tag census and the coherent forced-tail inequalities are
   simultaneously feasible inside the rings.**  Put
   \(\gamma_d=N_d-N_{d+1}\) for \(d<H\).  Across the \(N_H\) rings one
   can place exactly \(\gamma_d\) tags \(d\), exactly one tag \(H\) in
   every ring, and exactly \(E\) blank phases.  The nonblank phases of
   each ring can be made one promotion path.  Moreover, for every
   threshold \(q\), the high-tag vertices form one interval in each path,
   giving exactly

   \[
        e_q=N_q-N_H
   \tag{0.5}
   \]

   high--high promotion edges.  This termwise dominates the universal
   threshold-run demand

   \[
        (2N_q-W-N_H)_+.
   \tag{0.6}
   \]

   Thus neither the tag census nor the long forced-tail requirement is an
   obstruction to the tuned ring catalogue before cross-ring mask
   collisions are imposed.

2. **Independent ring heat has an exact fatal floor baseline.**  Fix any
   per-top tag words satisfying the census, and independently average the
   cyclic order in every top.  At signed depth \(q\), let
   \(a_{U,q}\) be the number of phases of top \(U\) whose tag is at least
   \(q\).  The exact one-top mean kernel is uniform on the appropriate
   subsets of \(U\).  If \(\Phi\) is the aggregate pair-collision energy,
   equivalently the square error above the load-one floor, then

   \[
   \boxed{
    \mathbb E\Phi
      =\mathcal T+\mathcal R,\qquad
    \mathcal T\ge0,\qquad
    \mathcal R=\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.}
   \tag{0.7}
   \]

   Here \(\mathcal T\) is the squared defect of the mean load from the
   uniform load one, and \(\mathcal R\) is the diagonal ring variance.
   The desired approximate SCD requires \(\Phi=o(W)\).  Thus the natural
   product heat misses the needed scale by a factor \(\Theta(\sqrt m)\),
   even in the ideal case \(\mathcal T=0\).

3. **The same obstruction applies to the adjacent-transposition heat.**
   Adjacent swaps connect all cyclic orders on a fixed top and preserve
   the promotion-ring and tag-path legality.  Their reversible stationary
   law is the uniform ring law used in (0.7).  A spectral gap can contract
   excess energy toward that equilibrium, but the equilibrium itself has
   \(\Theta(W\sqrt m)\) floor-correct energy.  Hence no Poincare/heat
   argument based only on independent top-ring blocks can prove the
   required \(o(W)\) packing.

4. **The precise surviving quantity is cross-top negative covariance.**
   For an arbitrary joint law on legal ring choices,

   \[
   \boxed{
      \mathbb E\Phi=\mathcal T+\mathcal R_{\mathbb P}+\mathcal C,}
   \tag{0.8}
   \]

   where \(\mathcal R_{\mathbb P}\) is its actual sum of one-top
   variances and \(\mathcal C\) is the sum of all cross-top covariances on
   literal target cells.  If the one-top marginals are the uniform ring
   marginals of the natural heat, then
   \(\mathcal R_{\mathbb P}=(\sqrt\pi/2+o(1))W\sqrt m\), and a successful
   correlated law with those marginals must have

   \[
      \boxed{\mathcal C=-\mathcal R+o(W),\qquad
             \mathcal T=o(W).}
   \tag{0.9}
   \]

   Product heat has \(\mathcal C=0\).  A rare deterministic selection has
   \(\mathcal R_{\mathbb P}=\mathcal C=0\), so (0.9) is not a universal
   statewise obstruction.  Rank-isolating rectangles give the correct
   signed local lattice, but no positive multi-top deployment is known
   which supplies (0.9) while retaining the uniform marginals.

This is a no-go for the natural heat proof, not for the promotion-ring
catalogue itself.  The exact next theorem is either a multi-top
alternating resolution with negative literal covariance of order
\(W\sqrt m\) under diffuse one-top marginals, or a direct exceptional
deterministic resolution outside that heat framework, while retaining the
tag-sorted promotion paths.  No coefficient-one conclusion is claimed
here.

## 1. The tagged full-ring model

For a top \(U\in\binom{[2m]}M\), choose a cyclic order

\[
 \pi_U=(u_0,\ldots,u_{M-1}).
\tag{1.1}
\]

The phase \(i\) full collar is the promotion-ring state from Theorem 3.6
of `MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md`.
If this phase has tag \(d\), its chain owns, at rank \(m+r\),
\(-d\le r\le d\), the mask

\[
 C_{U,i}(r)
 =U\setminus I_{\pi_U}(i+H+r,H-r),
\tag{1.2}
\]

where \(I_\pi(j,\ell)\) is the cyclic interval of length \(\ell\)
beginning at \(j\).  In particular, at depth \(q\), the lower mask omits
an interval of length \(H+q\), while the upper mask omits an interval of
length \(H-q\).

Use the covering-side calibration (0.2).  Its scalar consequences are

\[
 1\le {T\over W}={M\over\lambda_H}=1+O(H/m),
\tag{1.3}
\]

which is (0.3), and

\[
 {HN_H\over W}={H\over\lambda_H}=O(H/m)=o(1),
\tag{1.4}
\]

which proves (0.4) and the negligible one-path-per-top reset ledger.

Introduce one blank symbol \(\bot\), meaning that the corresponding ring
phase is omitted.  A **census-exact tagged ring selection** consists of:

* one cyclic order on every top;
* exactly one tag \(H\) in every top;
* exactly \(\gamma_d=N_d-N_{d+1}\) occurrences of tag \(d\), for
  \(0\le d<H\); and
* exactly \(E=T-W\) blanks.

The counts add correctly because

\[
 \sum_{d=0}^{H-1}\gamma_d+N_H=W,
 \qquad W+E=T=MN_H.
\tag{1.5}
\]

For every \(q\), the number of selected chains reaching either rank
\(m-q\) or rank \(m+q\) is therefore

\[
 \sum_{d=q}^{H-1}\gamma_d+N_H=N_q.
\tag{1.6}
\]

Thus load one is the exact floor at every controlled rank.

## 2. Exact tag-census paths and forced-tail agreement

### Theorem 2.1 (monotone ring-tag realization)

Every census-exact tag multiset admits a placement on the \(N_H\) rings
with the following properties.

1. In every ring the blanks form one cyclic interval.
2. The nonblank phases form one directed promotion path.
3. Along that path the tags are monotone, with its unique tag \(H\) at
   the high end.
4. For every \(1\le q\le H\), if \(e_q\) counts path edges whose two
   endpoint tags are at least \(q\), then

   \[
       \boxed{e_q=N_q-N_H.}
   \tag{2.1}
   \]
5. The retained tagged chains are pairwise mask-disjoint within each
   individual ring.

#### Proof

Give each ring one tag \(H\).  Distribute the lower tags and the \(E\)
blanks arbitrarily among the remaining \(M-1\) slots of the rings; the
total number of objects equals \(N_H(M-1)\) by (1.5).  In each ring put
all blanks consecutively, and put the nonblank tags in monotone order on
the complementary interval, ending with tag \(H\).  Deleting a nonempty
cyclic interval from a directed promotion cycle leaves one directed path.
If a ring has no blank, cut the cycle edge immediately before its
lowest-tag phase; this creates one path without deleting a state.

Let \(a_{U,q}\) be the number of tags at least \(q\) in ring \(U\).
It is positive because every ring contains a tag \(H\).  Monotonicity
makes those \(a_{U,q}\) vertices one terminal path interval, containing
exactly \(a_{U,q}-1\) internal edges.  Summing and using (1.6) gives

\[
 e_q=\sum_U(a_{U,q}-1)
     =N_q-N_H.
\]

The full-top promotion-ring theorem says that arbitrary phase tags give
pairwise mask-disjoint chains inside one ring provided at most one phase
has tag \(H\); deleting blank phases preserves that property.  This proves
the last assertion and completes the proof. \(\square\)

### Corollary 2.2 (the coherent forced-tail cut is passed)

Regard the selected ring paths as a bridge-one forest on the \(W\) tagged
chains.  It has

\[
 p=N_H=o(W/H)
\tag{2.2}
\]

components.  At every threshold \(q\),

\[
 e_q=N_q-N_H\ge(2N_q-W-N_H)_+.
\tag{2.3}
\]

For a truncation level \(B\le H\), the total forced-tail weight beyond
the free middle corner \(q_0=0\) is

\[
 \sum_{e}w_B(e)=\sum_{q=2}^{B}(N_q-N_H),
\tag{2.4}
\]

and it dominates term by term the universal coherent requirement

\[
 \sum_{q=2}^{B}(2N_q-W-N_H)_+.
\tag{2.5}
\]

#### Proof

Equation (2.2) is (0.4).  If the expression inside the positive part in
(2.3) is positive, subtracting it from the left side gives \(W-N_q\ge0\);
otherwise (2.3) is automatic.  A promotion-ring edge between tags
\(d,d'\) has the forced shifted lower/upper tails at precisely the
thresholds \(2\le q\le\min(d,d')\).  Summing first over edges and then
over thresholds gives (2.4).  Equation (2.5) follows from (2.3). \(\square\)

For example, if \(B=b\sqrt m+O(1)\) with fixed
\(0<b<\sqrt{\log2}\), then (2.4) is

\[
 \left(\int_0^b e^{-x^2}\,dx+o(1)\right)W\sqrt m,
\tag{2.6}
\]

whereas the necessary lower bound is

\[
 \left(\int_0^b(2e^{-x^2}-1)\,dx+o(1)\right)W\sqrt m.
\tag{2.7}
\]

The difference is positive.  Hence the long forced-tail theorem does not
close the tuned ring route.  Importantly, this conclusion uses one common
tag ordering at every threshold, not separately optimized forests.

More pointwise, for every fixed \(c>0\) and
\(L=\lfloor c\sqrt m\rfloor\), the same paths contain

\[
 e_L=N_L-N_H=(e^{-c^2}+o(1))W
\tag{2.8}
\]

edges whose two endpoints have forced shifted lower/upper tails of length
at least \(L-1\).  Thus the catalogue supplies a positive-density bank of
genuinely Gaussian-length tail agreements, rather than merely the correct
total weight.

## 3. Floor-correct collision energy

Fix a census-exact tagged ring selection.  For sign
\(\sigma\in\{-,+\}\) and \(0\le q\le H\), let
\(v_{U,q}^\sigma\) be the zero-one incidence vector of the masks at rank
\(m-q\) or \(m+q\) supplied by the active phases of top \(U\).  At
\(q=0\) the two signs are the same and are counted once.  Put

\[
 \mu_q^\sigma=\sum_Uv_{U,q}^\sigma.
\tag{3.1}
\]

By (1.6),

\[
 \|\mu_q^\sigma\|_1=N_q,
\tag{3.2}
\]

which is exactly the number of target coordinates in that rank.  Define

\[
 \Phi_q^\sigma
 =\sum_T\binom{\mu_q^\sigma(T)}2
 ={1\over2}\|\mu_q^\sigma-\mathbf1\|_2^2.
\tag{3.3}
\]

The equality follows from \(\sum_T\mu_q^\sigma(T)=N_q\).  If
\(h_q^\sigma\) is the number of holes, occurrence conservation gives

\[
 h_q^\sigma=\sum_T(\mu_q^\sigma(T)-1)_+\le\Phi_q^\sigma.
\tag{3.4}
\]

Thus

\[
 \Phi=\Phi_0+\sum_{q=1}^H(\Phi_q^-+\Phi_q^+)=o(W)
\tag{3.5}
\]

is a sufficient approximate-SCD packing target.  It is the correct
load-one floor energy; no raw second moment has been substituted for it.
Here “approximate” refers to the aggregate literal mask ledger.  The bound
\(\Phi=o(W)\) directly gives \(o(W)\) total holes, but it does not by
itself imply that deleting only \(o(W/H)\) whole chains makes the family
an exact SCD; that stronger chain-deletion conclusion would need a separate
collision-clustering theorem.

## 4. The exact one-ring mean kernel

Keep the tag positions in top \(U\) fixed and choose its cyclic coordinate
order uniformly.  Let

\[
 a_{U,q}=|\{i:d_{U,i}\ge q\}|.
\tag{4.1}
\]

The numbers of possible rank targets inside \(U\) are

\[
 B_q^- =\binom M{m-q}=\binom M{H+q},
 \qquad
 B_q^+ =\binom M{m+q}=\binom M{H-q}.
\tag{4.2}
\]

At \(q=0\), write \(B_0=\binom MH\).  For \(q=H\), one has
\(B_H^+=1\) and \(a_{U,H}=1\).

### Lemma 4.1 (uniform block kernel)

For a target \(S\) of the relevant rank,

\[
 \boxed{
 \bar v_{U,q}^\sigma(S)
 :=\mathbb E v_{U,q}^\sigma(S)
 =\begin{cases}
 a_{U,q}/B_q^\sigma,&S\subseteq U,\\
 0,&S\nsubseteq U.
 \end{cases}}
\tag{4.3}
\]

Moreover

\[
 \|v_{U,q}^\sigma\|_2^2=a_{U,q},\qquad
 \|\bar v_{U,q}^\sigma\|_2^2={a_{U,q}^2\over B_q^\sigma}.
\tag{4.4}
\]

#### Proof

For one fixed active phase, the omitted cyclic interval in (1.2) is a
uniform subset of \(U\) of its prescribed size under a uniform cyclic
order.  Hence its complementary mask is uniform among the
\(B_q^\sigma\) targets in \(U\).  Proper cyclic intervals at different
phases give different masks; at the exceptional full-top cell
\((q,\sigma)=(H,+)\), only the unique tag-\(H\) phase is active.  Summing
the \(a_{U,q}\) equal probabilities proves (4.3), and disjointness of the
incidences proves (4.4). \(\square\)

The formula depends only on the number of high tags, not their order.
Consequently restricting to the monotone long-tail tag words of Theorem
2.1 leaves the heat kernel below unchanged.

## 5. Exact product-heat decomposition

Choose the cyclic orders independently across tops, conditional on any
fixed census-exact collection of tag words.  Put

\[
 \bar\mu_q^\sigma=\sum_U\bar v_{U,q}^\sigma,
\tag{5.1}
\]

and define the mean-transport and diagonal-variance terms

\[
 \mathcal T_q^\sigma
 ={1\over2}\|\bar\mu_q^\sigma-\mathbf1\|_2^2,
\tag{5.2}
\]

\[
 \mathcal R_q^\sigma
 ={1\over2}\sum_U
 \left(a_{U,q}-{a_{U,q}^2\over B_q^\sigma}\right).
\tag{5.3}
\]

### Theorem 5.1 (exact floor-baseline identity)

At every signed rank,

\[
 \boxed{
 \mathbb E\Phi_q^\sigma
 =\mathcal T_q^\sigma+\mathcal R_q^\sigma.}
\tag{5.4}
\]

#### Proof

By (3.3),

\[
 \mathbb E\Phi_q^\sigma
 ={1\over2}\mathbb E
   \left\|\sum_Uv_{U,q}^\sigma-\mathbf1\right\|_2^2.
\]

Independence makes the centered vectors from distinct tops orthogonal in
expectation.  Therefore the last expression equals

\[
 {1\over2}\|\bar\mu_q^\sigma-\mathbf1\|_2^2
 +{1\over2}\sum_U
   \left(\mathbb E\|v_{U,q}^\sigma\|_2^2
              -\|\bar v_{U,q}^\sigma\|_2^2\right).
\]

Use (4.4). \(\square\)

This is already baseline-corrected: \(\mathcal T\) measures failure of
the mean to hit the load-one floor, while \(\mathcal R\) is variance above
that floor.

### Theorem 5.2 (critical variance asymptotic)

Summing the middle rank once and both signs at positive depths gives

\[
 \boxed{
 \mathcal R
 :=\mathcal R_0+
   \sum_{q=1}^H(\mathcal R_q^-+\mathcal R_q^+)
 =\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.}
\tag{5.5}
\]

In particular, uniformly over every exact distribution of the tag census
among the tops,

\[
 \mathbb E\Phi\ge
 \left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.
\tag{5.6}
\]

#### Proof

At every signed rank, \(0\le a_{U,q}\le M\), and (1.6) gives

\[
 \sum_Ua_{U,q}=N_q.
\tag{5.7}
\]

Thus the first terms in (5.3) sum to

\[
 {1\over2}\left(W+2\sum_{q=1}^HN_q\right).
\tag{5.8}
\]

We show that all square corrections are \(o(W\sqrt m)\).  On the lower
side, \(B_q^-\ge\binom MH\), so

\[
 \sum_{q=0}^H\sum_U{a_{U,q}^2\over B_q^-}
 \le {M\over\binom MH}\sum_{q=0}^HN_q=o(W).
\tag{5.9}
\]

For the upper side write \(j=H-q\).  The \(j=0\) term equals \(N_H\),
and the \(j=1\) term is at most \(N_{H-1}\); both are
\(O(W/m)=o(W\sqrt m)\).  For \(j\ge2\),
\(B_q^+=\binom Mj\ge\binom M2\), and hence

\[
 \sum_{q=0}^{H-2}\sum_U{a_{U,q}^2\over B_q^+}
 \le {M\over\binom M2}\sum_{q=0}^{H-2}N_q
 =O(W/\sqrt m)=o(W\sqrt m).
\tag{5.10}
\]

Finally, uniformly for \(q\le H=o(m^{2/3})\),

\[
 {N_q\over W}
 =\exp\left(-{q^2\over m}+o(1)\right),
\tag{5.11}
\]

and the error is uniform on the critical range.  Riemann summation yields

\[
 \sum_{q=1}^HN_q
 =\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m,
\tag{5.12}
\]

because \(H/\sqrt m\to\infty\).  Equations (5.3), (5.8)--(5.12)
prove (5.5).  Theorem 5.1 and \(\mathcal T\ge0\) prove (5.6).
\(\square\)

The desired scale \(o(W)\) is smaller by a factor tending to infinity.
Even the middle rank alone has diagonal baseline
\((1/2+o(1))W\), consistent with the exact \(e^{-1}\)-scale owner holes
under independent top choices.

### Corollary 5.3 (stationary shallow holes in the ideal mean-balanced case)

Fix \(b>0\).  Suppose, in addition, that the one-top means have been
balanced so that \(\bar\mu_q^\sigma(T)=1\) for every target at every
\(q\le b\sqrt m\).  Then, under independent ring choices,

\[
 \Pr\bigl(\mu_q^\sigma(T)=0\bigr)=e^{-1}+o(1)
\tag{5.13}
\]

uniformly on those ranks, and hence

\[
 \mathbb E\sum_{1\le q\le b\sqrt m}(h_q^-+h_q^+)
 =\left(2e^{-1}\int_0^b e^{-x^2}\,dx+o(1)\right)W\sqrt m.
\tag{5.14}
\]

#### Proof

For fixed \(T\), its load is a sum of independent Bernoulli variables,
one from each containing top, with total mean one.  By (4.3), the largest
success probability is at most

\[
 {M\over\min(B_q^-,B_q^+)}=o(1)
\]

uniformly for \(q\le b\sqrt m\), because
\(H-q\to\infty\).  Therefore

\[
 \log\Pr(\mu_q^\sigma(T)=0)
 =\sum_U\log(1-p_U)=-\sum_Up_U+o(1)=-1+o(1).
\]

Sum over targets and use the uniform Gaussian estimate for \(N_q\).
\(\square\)

Thus even replacing the quadratic Lyapunov function by the literal hole
count does not rescue product heat: its best symmetric equilibrium has a
macroscopic shallow occupancy defect.

## 6. Exact one-block drift and spectral scope

At one signed rank suppress \((q,\sigma)\) from the notation.  Suppose,
in the most favorable case, that the aggregate mean is exactly uniform:

\[
 \sum_U\bar v_U=\mathbf1.
\tag{6.1}
\]

For a deterministic ring selection put

\[
 \Phi={1\over2}\left\|\sum_Uv_U-\mathbf1\right\|_2^2,
 \qquad
 A=\sum_U\langle v_U,\bar v_U\rangle.
\tag{6.2}
\]

Resample the cyclic order of top \(U\) from its uniform ring law, leaving
all other tops fixed, and call the new energy \(\Phi^{(U)}\).

### Theorem 6.1 (summed heat drift)

\[
 \boxed{
 \sum_U\mathbb E(\Phi^{(U)}-\Phi)
 =-2\Phi+N_q-A.}
\tag{6.3}
\]

For the uniform block kernel,

\[
 A=\sum_U{a_{U,q}^2\over B_q^\sigma},
\tag{6.4}
\]

so the drift is toward the exact level

\[
 \boxed{
 \Phi_*={1\over2}\left(N_q-
              \sum_U{a_{U,q}^2\over B_q^\sigma}\right)
          =\mathcal R_q^\sigma,}
\tag{6.5}
\]

not toward zero.

#### Proof

Let \(w=\sum_Vv_V-\mathbf1\).  Replacing \(v_U\) by an independent
copy \(v'_U\) gives

\[
 \mathbb E(\Phi^{(U)}-\Phi)
 =\langle w,\bar v_U-v_U\rangle
  +a_{U,q}-\langle v_U,\bar v_U\rangle.
\tag{6.6}
\]

Sum over \(U\).  The first terms equal

\[
 \left\langle w,\sum_U\bar v_U-\sum_Uv_U\right\rangle
 =\langle w,-w\rangle=-2\Phi
\]

by (6.1).  The sum of \(a_{U,q}\) is \(N_q\).  Finally (4.3) is constant
on the support of \(v_U\), giving (6.4). \(\square\)

Thus whenever \(\Phi>\Phi_*\), some top has a negative expected
one-block move; but the certified descent stops once
\(\Phi\le\Phi_*\).  On every Gaussian bulk rank,
\(\Phi_*=(1/2+o(1))N_q\).

Adjacent transpositions generate the full cyclic-order space on a top.
The corresponding reversible adjacent-swap chain has the same uniform
stationary law as the full resampling kernel.  A Poincare or log-Sobolev
estimate can change the rate at which nonconstant modes approach
stationarity, but it cannot change (5.4)--(5.5), the stationary
floor-correct energy.  Therefore a spectral gap for the ring chain, by
itself, is not a coefficient-one contraction theorem.

## 7. Arbitrary joint laws and the exact covariance gate

Let \(\mathbb P\) now be any joint law on legal ring choices with the
fixed exact tag census; independence between tops is not assumed.  Keep
the one-top means \(\bar v_U=\mathbb Ev_U\), and define the actual
diagonal variance

\[
 \mathcal R_{\mathbb P,q}^\sigma
 ={1\over2}\sum_U
   \mathbb E\|v_{U,q}^\sigma-\bar v_{U,q}^\sigma\|_2^2
\tag{7.1a}
\]

and the cross-top covariance

\[
 \mathcal C_q^\sigma
 =\sum_T\sum_{U<V}
   \operatorname {Cov}\bigl(v_{U,q}^\sigma(T),
                             v_{V,q}^\sigma(T)\bigr).
\tag{7.1}
\]

### Theorem 7.1 (exact negative-covariance identity)

\[
 \boxed{
 \mathbb E\Phi_q^\sigma
 =\mathcal T_q^\sigma+\mathcal R_{\mathbb P,q}^\sigma
   +\mathcal C_q^\sigma.}
\tag{7.2}
\]

Consequently, if the one-top marginals remain the uniform ring marginals
of Section 4 and a joint law satisfies \(\mathbb E\Phi=o(W)\), then

\[
 \boxed{
 \sum_{q,\sigma}\mathcal T_q^\sigma=o(W),\qquad
 \sum_{q,\sigma}\mathcal C_q^\sigma
 =-\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m+o(W).}
\tag{7.3}
\]

#### Proof

 Expand the square in (3.3).  The diagonal variances give
 \(\mathcal R_{\mathbb P,q}^\sigma\), the square of the mean gives
 \(\mathcal T_q^\sigma\), and every unordered pair of distinct tops gives
 exactly the covariance in (7.1).  This proves (7.2).  Since
 \(\mathcal T={1\over2}\|\mathbb E\mu-\mathbf1\|_2^2
 \le\mathbb E\Phi\) by Jensen, a law with
 \(\mathbb E\Phi=o(W)\) has \(\mathcal T=o(W)\).  Theorem 5.2 and
 (7.2) then give the necessary cancellation (7.3). \(\square\)

For the uniform one-top ring marginals of Section 4,
\(\mathcal R_{\mathbb P,q}^\sigma=\mathcal R_q^\sigma\) from (5.3),
which is why Theorem 5.2 applies in (7.3).  Without that marginal
hypothesis there is no universal diagonal constant: for a deterministic
joint selection both \(\mathcal R_{\mathbb P}\) and \(\mathcal C\) are
zero.  Thus (7.3) is an obstruction to correlated rounding *with the
uniform one-top marginals*, not a statewise invariant against every rare
deterministic selection.

The required covariance is not a small correction: it must cancel the
entire diagonal scatter to relative error \(o(m^{-1/2})\).  This is the
literal near-parallel-class content of the problem.

There is a parallel exact statement for a two-seed owner-overlay heat.

### Theorem 7.2 (fair component heat: action equals scatter)

Suppose two legal ring resolutions of the same owner resources have been
overlaid and decomposed into independent legal switching components
\(C\), and suppose every component hybrid retains the exact global tag
census (hence exactly \(N_q\) incidences in each signed rank cell).
Let \(d_C\) be the complete signed all-rank target change produced by
switching component \(C\).  Choose every component shore independently
and fairly.  If \(\bar\mu\) is the resulting mean load vector, then

\[
 \boxed{
 \mathbb E\Phi
 ={1\over2}\|\bar\mu-\mathbf1\|_2^2
 +{1\over8}\sum_C\|d_C\|_2^2.}
\tag{7.4}
\]

Since every \(d_C\) is integral,

\[
 \sum_C\|d_C\|_2^2\ge
 \sum_C\|d_C\|_1.
\tag{7.5}
\]

Consequently a fair component heat with \(\Omega(W)\) total net literal
action has expected floor energy \(\Omega(W)\); to certify an
\(o(W)\) child by averaging, it must have only \(o(W)\) net action.

#### Proof

Write the contribution of component \(C\) as
\(\bar y_C+\varepsilon_Cd_C/2\), where the independent signs
\(\varepsilon_C\) are uniform on \(\{-1,1\}\).  Expanding
\(\Phi=\frac12\|\mu-\mathbf1\|_2^2\), all cross terms between different
components vanish in expectation and
\(\mathbb E\|\varepsilon_Cd_C/2\|_2^2=\|d_C\|_2^2/4\).
This proves (7.4).  For an integer \(z\), \(z^2\ge|z|\); summing proves
(7.5). \(\square\)

Thus replacing one-top product heat by a fair binary overlay does not by
itself solve the baseline problem.  Bounded local components are
variance-safe because they have subcritical action; components with the
linear action needed for repair carry a linear scatter charge.  A viable
switching theorem must orient components state-adaptively, use a highly
biased coupled law, or prove negative joined covariance before the fair
choice is taken.

## 8. What exact switches can and cannot supply

An adjacent transposition of two cyclic symbols in one top changes at most
two deleted and two inserted targets at every proper rank, and it preserves
the promotion-ring path and any fixed phase-tag word.  It therefore gives a
valid local direction, including under the monotone tag arrangement of
Theorem 2.1.

It is not, however, automatically an exact switch inside an already
owner-disjoint SCD selection: at the middle rank it changes literal
owners.  More sharply, when \(2H<M\), the **complete** unlabelled
middle-window family of one top determines its cyclic order up to rotation
and reversal.  Hence:

### Proposition 8.1 (no nontrivial one-top exact switch)

If two ring choices on one fixed top have the same complete middle-owner
family, then they have the same interval family at every rank.

#### Proof

Complement the length-\(m\) windows inside the \(M\)-set top.  They become
the length-\(H\) cyclic intervals.  Because \(2H<M\), joining two such
intervals when they meet in \(H-1\) points recovers the cycle of consecutive
windows.  Its singleton differences recover the cyclic coordinate order
up to direction and rotation.  All cyclic interval families are invariant
under those two ambiguities. \(\square\)

Thus complete-deck one-top heat has no nontrivial owner-preserving
direction.  In the blanked approximate-SCD model, Proposition 8.1 does not
classify switches which use the omitted phase reserve; such partial-deck
switches remain possible.  They must nevertheless charge every changed
selected middle owner, or coordinate their collateral with other tops.

There is an exact global closure law once two owner-simple ring selections
are available.

### Theorem 8.2 (owner-overlay component closure)

Let \(\mathcal F^-\) and \(\mathcal F^+\) use one ring segment at each top
in the same top family, with the same number of selected middle phases at
each corresponding top, and suppose both partition the same set
\(\mathcal O\) of middle owners.  Form a directed multigraph on the tops:
for each \(X\in\mathcal O\), draw the edge \(U\to V\) when the old segment
at \(U\) owns \(X\) and the new segment at \(V\) owns \(X\).

For a top set \(A\), replace old by new precisely on \(A\).  This is
owner preserving if and only if \(A\) is a union of weak connected
components of the full overlay multigraph.

#### Proof

For the owner edge \(U\xrightarrow{X}V\), the coefficient of \(X\) in
the proposed packet difference is

\[
 \mathbf1_A(V)-\mathbf1_A(U).
\]

All owner coefficients vanish exactly when no nonloop overlay edge crosses
the cut \(A\mid A^c\), which is equivalent to component closure. \(\square\)

Thus an Euler decomposition of the overlay into ordinary alternating
cycles is not a decomposition into legal ring trades: the other owner
edges incident with the same tops give a literal boundary counterterm.
The independent binary heat variables are the weak overlay components,
not individual owner cycles and not individual tops.

### Corollary 8.3 (bounded local ring trades have subcritical throughput)

Suppose every top participates in at most \(\kappa=O(1)\) adjacent-swap
rectangles.  At one isolated rank their total raw incidence variation is

\[
 O(\kappa N_H)=O(W/m)=o(W).
\tag{8.2}
\]

Allowing ordinary adjacent swaps, each affecting \(O(H)\) controlled
incidences, gives aggregate all-band variation at most

\[
 O(\kappa HN_H)=O(\kappa WH/m)=o(W).
\tag{8.3}
\]

Consequently bounded-congestion local switches cannot remove an
\(\Omega(W)\) collision defect.  For a linear defect at one fixed rank,
a useful component system must have long reassembly components with
\(\Omega(M)\) useful target change per active top on average.
Equivalently, adjacent-swap surgery needs average congestion
\(\Omega(m)\) in that case, and at least \(\Omega(m/H)\) to repair a
linear defect measured only after summing over the whole central band.

#### Proof

One rank-isolating rectangle has four nonzero target coefficients at its
active rank.  Summing over at most \(\kappa N_H\) atoms gives (8.2).
An adjacent swap changes at most four occurrences in each of \(O(H)\)
ranks, giving (8.3).  Hole or collision descent is bounded in absolute
value by raw incidence variation.  Finally use
\(N_H=\Theta(W/m)\) and \(H/m=o(1)\). \(\square\)

The two-adjacent-swap rectangle has a valuable signed property: when its
boundary cuts are separated by \(r\), its mixed second difference vanishes
at every rank except \(r\) and \(M-r\).  In the critical central band the
second exceptional rank lies outside the band, so rectangles span the
integer zero-point-marginal lattice rank by rank.  Their positive segment
implementation duplicates only \(O(H)\) endpoints per top, and

\[
 HN_H=O(WH/m)=o(W).
\tag{8.1}
\]

Thus rectangles remain a legitimate absorber candidate.  What they do
not supply is a positive **multi-top** semigroup realizing the covariance
in (7.3) while maintaining the middle packing.  Signed lattice spanning
does not imply that negative collateral can be charged within the
available owner reserve.

### 8.1 Relation to the existing invariant audits

Two previously proved obstructions do not strengthen the heat conclusion
to a global nonexistence theorem.

First, the finite-character holonomy theorem in
`MATH_THEOREM_PROMOTION_RING_CYCLE_NIBBLE_AND_CHARACTER_TRAP_20260726.md`
constructs positive-density residual middle layers containing no whole
promotion ring (for example when \(\gcd(m,H)=1\)).  It rigorously refutes
an *arbitrary-residual regeneration* hypothesis for an iterative nibble.
It does not say that a globally coordinated selection from the original
catalogue must enter such a residual, so it is not a dual certificate
against the initial resolution problem.

Second, the physical determinant-two minors in
`MATH_THEOREM_PROMOTION_RING_TAG_MATRIX_TU_CORE_AND_ROOT_ODD_MINORS_20260726.md`
show that the fixed-frame target matrix is not totally unimodular.  Their
currently proved support is only \(\Theta(N_H)\) phase columns, however,
and even an \(O(H)\) charge per affected ring totals

\[
                         O(HN_H)=o(W).
\tag{8.4}
\]

Thus those minors rule out a TU proof but not coefficient one.  Combined
with the present variance calculation, the exact surviving formulation is
the fibre-dense weighted root-transversal/negative-covariance problem of
`MATH_AUDIT_ROOTED_PROMOTION_RING_ARBITRARY_DUAL_NEAR_RESOLUTION_20260726.md`:
one needs a common multi-top resolution, not independent block heat and
not an arbitrary-residual nibble theorem.

## 9. Proved boundary

The following statements are now exact.

1. The critical ring inventory admits the full SCD tag census with only
   \(E=o(W)\) blanks and one promotion path per top.
2. One common monotone tag arrangement passes every coherent forced-tail
   threshold simultaneously, with the exact edge count \(N_q-N_H\).
3. Uniform one-ring resampling has the floor-correct decomposition
   \(\mathbb E\Phi=\mathcal T+\mathcal R\).
4. Its diagonal baseline is
   \((\sqrt\pi/2+o(1))W\sqrt m\), so neither full resampling nor the
   adjacent-swap spectral heat can establish \(o(W)\) aggregate holes.
5. A successful correlated law with the same one-top marginals requires
   negative cross-top covariance
   \(-\mathcal R+o(W)\).
6. Every complete-deck one-top middle-preserving switch is trivial.
   Partial-deck switches using the \(o(W)\) omitted reserve are not
   classified; a general exact contraction must coordinate their
   collateral or use multi-top moves.
7. Between two exact owner packings, legal binary hybrids are exactly
   unions of weak components of the full owner overlay; bounded-congestion
   adjacent swaps or rectangles have only \(o(W)\) total throughput.
8. The known finite-character residual trap blocks arbitrary-residual
   iteration but not the initial global resolution, while the known odd
   tag minors have only \(o(W)\) audited loss.  Neither supplies a global
   invariant obstruction beyond the heat/noise result proved here.

What is not proved is a statewise Hall obstruction against all correlated
ring selections.  The catalogue may still contain a rare approximate SCD.
The surviving constructive statement is precise:

> Build an owner/mask-disjoint multi-top alternating resolution of the
> promotion rings which either satisfies the diffuse-marginal covariance
> condition (7.3), or is constructed directly as an exceptional
> deterministic resolution outside that heat law, while retaining the
> monotone tag paths of Theorem 2.1; alternatively, give a nonnegative
> dual functional separating every such resolution.

That is a negative-covariance/resolution theorem, not a one-ring heat-gap
theorem and not an MSW component calculation.
