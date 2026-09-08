# Adjacent-priority necklace interpolation: aligned exact paths, positive-Gram interval rounding, and the remaining capacity obstruction

Date: 2026-07-25

## 0. Result and precise boundary

Let

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 T=\binom{n}{m-1},\qquad L=2m-1,
\]

and let

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
\]

be the number of necklace rows in one exact local factor.  Consider two
adjacent omitted pairs (A=P_j,B=P_{j+1}) in the first-avoided priority
order, and keep the local factor attached to each omitted pair fixed while
interchanging the priorities of (A) and (B).

Throughout the report,

\[
 1\le H\le m-2.
\tag{0.1}
\]

This contains (H=\lceil A\sqrt m\rceil) for every fixed (A) and all
sufficiently large (m).  The restriction is essential for the displayed
length-independent constants: at (q=m-1), an upper window is the entire
local universe and distinct-start simplicity is false.

The following statements are proved below.

1. The changed lower targets are exactly
   \[
   \mathcal D_j={S:|S|=m-1, S\cap(A\cup B)=\varnothing,
    S\cap P_h\ne\varnothing (h<j)},
   \]
   and
   \[
   |\mathcal D_j|
   =\sum_{t=0}^{j-1}(-1)^t\binom{j-1}{t}
     \binom{2m-3-2t}{m-1}.
   \]
   In particular
   \[
   |\mathcal D_1|
   =\frac{m(m+1)}{4(2m-1)(2m+1)}W
   =\left(\frac1{16}+O(m^{-1})\right)W.
   \]

2. For arbitrary fixed local factors, the exact central hybrids are not
   arbitrary component signs.  An alternating cycle has only its two
   endpoint orientations, while an alternating path has exactly one cut:
   an old prefix followed by a new suffix.  Low endpoint run count does not
   control the physical fragmentation of such a cut.

3. There are two explicit correlated choices of (F_B) from (F_A).

   * If (F_B) is a coordinate transport of (F_A) with the **same** row
     orientation, every affected lower target is a one-vertex exchange
     component.  Consequently arbitrary signs on long physical interval
     blocks preserve exact middle ownership.  All lower flags agree, and
     the upper difference vectors have an exact nonnegative Gram matrix.
     Independent block signs give the exact raw-square contraction
     \[
       \mathbb E Q_w(M_p)
       =(1-p)Q_w(M_A)+pQ_w(M_B)
        -4p(1-p)\mathcal C_{A,B},
     \]
     where \(\mathcal C_{A,B}\) is the weighted number of duplicate
     activated upper targets.  Every outcome adds at most two runs per
     interval block.  This is an unconditional, integral energy
     contraction relative to the endpoint interpolation.  The two
     pair-symmetric endpoints have equal energy rank by rank, so fair
     interval signs decrease raw energy by exactly
     \(\mathcal C_{A,B}\) in expectation.

   * If the transported (B)-rows are given the **opposite** orientation,
     every maximal physical \(\mathcal D_j\)-interval is exactly one open
     alternating path.  Its legal children are exactly its old-prefix / 
     new-suffix thresholds.  Every threshold adds at most two runs per
     path, and the complete flag displacement between any two thresholds
     satisfies, for every (q\),
     \[
       \|z^-_q\|_2^2\le2(q-1),\qquad
       \|z^+_q\|_2^2\le6q+2.
     \]
     Thus an arbitrarily long physical block has at most (4H(H+1))
     unweighted multidepth square action, independent of its length.

4. The preceding results do **not** prove constant one.  Same-orientation
   transport changes only pair-collar upper occurrences.  At depth one it
   changes at most (4R_m=O(W/m)) occurrences, so it cannot repair a
   linear first-upper collision defect.  Opposite orientation has signed
   endpoint-strip Grams from depth (2) onward, and its audited variance
   toll is
   \[
     O\!\left(
       K_j\sum_{q\le H}(q-1)(w_q^-+w_q^+)
       +R_m\sum_{q\le H}(q+1)w_q^+
     \right),
   \]
   which is (O_A((j+1)W)), not (o(W)), for
   (H=\lceil A\sqrt m\rceil) and bounded Gaussian weights.  Moreover, a midpoint-preserving law on
   one nontrivial exchange path is forced to use only the two endpoints.

The actual advance is therefore exact and nontrivial: the exchange-order
versus physical-order obstruction can be removed by an explicit factor
coupling, and one orientation gives a rigorous positive energy
contraction per (O(1)) new boundaries.  The missing theorem is now a
charged-coverage statement showing that these pair-collar atlases see a
sufficient fraction of the total multidepth defect, or a signed
endpoint-strip discrepancy theorem beating the critical (O(W)) toll.

No claim of MWB, SPC, or the constant-one contiguous-OR theorem is made.

## 1. Token convention and flags

Partition (2m) coordinates into ordered disjoint pairs

\[
 P_1,\ldots,P_m
\]

and leave one coordinate unpaired.  For a rank-((m-1)) set (S), put

\[
 \kappa(S)=\min\{h:S\cap P_h=\varnothing\}.
\]

Fix an exact local necklace factor (F_P) on
(Q_P=[n]\setminus P) for every omitted pair (P).  In an oriented row

\[
 \pi=(x_i)_{i\in\mathbb Z_L}
\]

of (F_P), write

\[
 S_i=I_\pi(i,m-1),\qquad X_i=I_\pi(i,m).
\]

We use the predecessor-owner token

\[
 e_P(S_i)=(S_i,X_{i-1}).
\]

Its literal signed depth-(q) flags are

\[
 L^P_q(i)=I_\pi(i+q-1,m-q),
 \qquad
 U^P_q(i)=I_\pi(i-1,m+q),
 \qquad 1\le q\le H.
\tag{1.1}
\]

Selecting the token for (S) in (F_{P_{\kappa(S)}}) covers every lower
target once.  Since its middle owner contains (S) and avoids the omitted
pair, it has the same category as (S).  Hence all selected middle owners
are distinct.  This is an exact lower-saturating, middle-simple matching.

The first-avoided interval argument gives

\[
 J_0=O\!\left(\frac{W\log^2m}{m}\right)
\tag{1.2}
\]

physical runs.  Thus its selected-token predecessor proportion is

\[
 1-\frac{J_0}{T}=1-O\!\left(\frac{\log^2m}{m}\right).
\tag{1.3}
\]

In particular it is (1-o(1/H)) whenever

\[
 H\log^2m=o(m).
\tag{1.4}
\]

All later switches retain the complete token (1.1).  No flag is detached
from its physical row, and no fractional token is used.

## 2. Exact affected set and arbitrary overlay

Let

\[
 A=P_j,\qquad B=P_{j+1},\qquad
 R=[n]\setminus(A\cup B).
\]

Compare the first-avoided matching (M_A) in the order

\[
 P_1,\ldots,P_{j-1},A,B,P_{j+2},\ldots
\]

with the matching (M_B) obtained by interchanging (A,B), without
changing which local factor is attached to each omitted pair.

### Theorem 2.1 (affected lower targets)

The two matchings differ precisely on

\[
 \boxed{
 \mathcal D_j={S:|S|=m-1, S\subseteq R,
                     S\cap P_h\ne\varnothing (h<j)}.}
\tag{2.1}
\]

Moreover

\[
 \boxed{
 d_j:=|\mathcal D_j|
 =\sum_{t=0}^{j-1}(-1)^t\binom{j-1}{t}
   \binom{2m-3-2t}{m-1}.}
\tag{2.2}
\]

#### Proof

A set missing an earlier pair is assigned before either (A) or (B) in
both orders.  A set missing exactly one of (A,B) is assigned to that same
pair in both orders.  A set meeting all earlier pairs and missing both
(A,B) is assigned to whichever of (A,B) is first.  This proves (2.1).
Inclusion-exclusion over the (j-1) earlier pairs gives (2.2).  ∎

For (j=1),

\[
 d_1=\binom{2m-3}{m-1}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}W.
\tag{2.3}
\]

Let

\[
 f_A,f_B:\mathcal D_j\longrightarrow\binom{[n]}m
\]

be the two injective middle-owner maps.  Form the two-coloured bipartite
overlay with left side \(\mathcal D_j\), right side
(f_A(\mathcal D_j)\cup f_B(\mathcal D_j)), and the two edges
((S,f_A(S))), ((S,f_B(S))) at each lower vertex.

### Lemma 2.2 (shared owners avoid both omitted pairs)

If

\[
 f_A(S)=f_B(T)=Y,
\]

then (Y\subseteq R).

#### Proof

An (A)-owner lies in (Q_A) and therefore avoids (A).  A (B)-owner
avoids (B).  A common owner avoids both.  ∎

The overlay is a disjoint union of even alternating paths and cycles.  Its
paths have both endpoints on the middle side.

### Theorem 2.3 (exact central state space)

Orient an alternating path as

\[
 y_0-S_1-y_1-S_2-\cdots-S_k-y_k
\]

so that the (A)-edge of (S_i) is (S_i y_{i-1}) and its (B)-edge is
(S_i y_i).  A set of overlay edges saturates every lower vertex and is
middle-simple if and only if:

* on each path there is a unique (r\in\{0,\ldots,k\}) for which it uses
  the (A)-edges of (S_1,\ldots,S_r) and the (B)-edges of
  (S_{r+1},\ldots,S_k);
* on each alternating cycle it uses either all (A)-edges or all
  (B)-edges.

#### Proof

Let (u_i=1) mean that the (A)-edge at (S_i) is chosen.  At the
internal middle vertex (y_i), the pattern (u_i=0,u_{i+1}=1) would
select both incident edges.  Thus

\[
 u_i\ge u_{i+1}.
\]

On a path this forces (u=1^r0^{k-r}).  Cyclic inequalities force a
constant word on a cycle.  Every such state is visibly lower-saturating and
middle-simple.  ∎

The number of open paths is exactly

\[
 p_j=d_j-|f_A(\mathcal D_j)\cap f_B(\mathcal D_j)|.
\tag{2.4}
\]

For (j=1), every rank-(m) subset (Y\subseteq R) belongs to both
images: its unique (A)-preimage and unique (B)-preimage are facets of
(Y), hence lie in \(\mathcal D_1\).  Conversely every common owner lies
in (R).  Therefore

\[
 |f_A(\mathcal D_1)\cap f_B(\mathcal D_1)|
 =\binom{2m-3}{m}=\frac{m-2}{m}d_1,
\]

and

\[
 \boxed{p_1=\frac{2d_1}{m}=R_m.}
\tag{2.5}
\]

No bound on the number or lengths of alternating cycles follows for
arbitrary local factors.  Nor does (2.5) align path order with physical
row order.  The stated hypotheses do not preclude arbitrary interlacing;
abstract two-matching instances with low-run endpoints and a linearly
fragmented interior path cut exist.  Realization of that worst-case
interlacing by exact local necklace factors is not asserted.  Thus the
endpoint run bound and component count alone do not prove predecessor
correlation for an interior hybrid.

### Lemma 2.4 (physical changed intervals)

In every (F_A)-row, the starts belonging to \(\mathcal D_j\) have at
most (2j) cyclic components.  Hence their total interval count (K_j)
satisfies

\[
 \boxed{K_j\le\min\{d_j,2jR_m\}.}
\tag{2.6}
\]

#### Proof

For one fixed coordinate pair, the starts whose length-((m-1)) window
avoids both coordinates form at most two cyclic intervals.  Membership in
\(\mathcal D_j\) requires avoidance of (B) and nonavoidance of each of
the (j-1) earlier pairs.  Every boundary of the resulting Boolean
intersection is a boundary of one of these (j) pair conditions.  There
are at most (4j) boundary points and therefore at most (2j) cyclic
components.  Summing over the (R_m) rows gives (2.6).  ∎

## 3. Same-orientation transport: singleton components and long blocks

Write

\[
 A=\{a_1,a_2\},\qquad B=\{b_1,b_2\},
\]

and let

\[
 \tau=(a_1\ b_1)(a_2\ b_2)
\tag{3.1}
\]

fix every coordinate of (R).  Choose

\[
 F_B=\tau F_A
\tag{3.2}
\]

with transported rows given the same orientation and root.  Thus the
(B)-token corresponding to (S_i\in\mathcal D_j) is the transport of
the (A)-token:

\[
 f_B(S_i)=\tau f_A(S_i)=\tau X_{i-1}.
\tag{3.3}
\]

### Theorem 3.1 (singleton-component coupling)

Every connected component of the affected overlay contains exactly one
lower vertex.  If (f_A(S)\subseteq R), the two token edges are parallel
and form a two-edge alternating cycle.  Otherwise they form a two-edge
alternating path with distinct middle endpoints.  Consequently an
arbitrary choice of (A)-token or (B)-token for every
(S\in\mathcal D_j) is lower-saturating and middle-simple.

#### Proof

Suppose (f_A(S)=f_B(T)).  Lemma 2.2 makes the common owner a subset of
(R), so it is fixed by \(\tau\).  Equation (3.3) then gives

\[
 f_A(S)=\tau f_A(T)=f_A(T).
\]

The (A)-owner map is injective, so (S=T).  This proves that distinct
lower vertices never meet in the overlay.  The two stated cases follow
according as (f_A(S)) is or is not \(\tau\)-fixed.  Finally, tokens outside
\(\mathcal D_j\) are common to the two endpoints.  Every chosen
\(A\)-alternative is compatible with them because \(M_A\) is
middle-simple, and every chosen \(B\)-alternative is compatible with them
because \(M_B\) is middle-simple.  Thus a mixed child cannot collide with
an unchanged owner.  ∎

Partition each maximal physical \(\mathcal D_j\)-interval into consecutive
blocks.  Let \(\mathscr B\) be the resulting block family.  Assign one bit
to each block and use its (A)-tokens or its (B)-tokens throughout.
Theorem 3.1 proves exact central legality for every bit string.

### Proposition 3.2 (deterministic row bound)

Every block child (M_\varepsilon) satisfies

\[
 \boxed{J(M_\varepsilon)\le J(M_A)+2|\mathscr B|.}
\tag{3.4}
\]

If blocks are formed with target length (b), with at most one shorter
remainder per maximal interval, then

\[
 |\mathscr B|\le \frac{d_j}{b}+K_j,
\tag{3.5}
\]

and hence

\[
 \frac{HJ(M_\varepsilon)}W
 =O\!\left(
   \frac{H\log^2m}{m}+\frac Hb+\frac{jH}{m}
 \right).
\tag{3.6}
\]

Thus every outcome has predecessor correlation (1-o(1/H)) provided

\[
 H\log^2m=o(m),\qquad H=o(b),\qquad jH=o(m).
\tag{3.7}
\]

#### Proof

Relative to (M_A), choosing the (B)-side of one block removes one
consecutive block from its (A)-row and inserts the paired consecutive
block in its (B)-row.  Toggling one interval can increase the number of
runs by at most one in each row.  This proves (3.4).  Splitting an interval
of length \(\ell\) uses at most \(\ell/b+1\) blocks, proving (3.5).
Equations (1.2), (2.6), and (3.5) give (3.6).  ∎

This is the required long-block predecessor correlation.  It is obtained
without independent vertex rounding: all bits act on complete physical
interval columns.

## 4. Same-orientation flag span and exact positive Gram

For (S_i\in\mathcal D_j), the transported (B)-flags are

\[
 L^{B}_q(i)=\tau I_\pi(i+q-1,m-q),
 \qquad
 U^{B}_q(i)=\tau I_\pi(i-1,m+q).
\]

Every lower flag is a subset of (S_i\subseteq R), so

\[
 \boxed{L^B_q(i)=L^A_q(i)\quad(1\le q\le H).}
\tag{4.1}
\]

Put

\[
 U_{i,q}=I_\pi(i-1,m+q),\qquad
 d_{i,q}=\mathbf e_{\tau U_{i,q}}-\mathbf e_{U_{i,q}}.
\tag{4.2}
\]

Then (d_{i,q}=0) unless (U_{i,q}\cap B\ne\varnothing).

### Theorem 4.1 (positive-Gram law)

For affected tokens (i,k),

\[
 \boxed{
 \langle d_i,d_k\rangle_w
 =2\sum_{q\le H}w_q^+
   \mathbf1_{\{U_{i,q}=U_{k,q},\ U_{i,q}\cap B\ne\varnothing\}}
 \ge0.}
\tag{4.3}
\]

If (i\ne k) lie in the same physical row, then

\[
 \langle d_i,d_k\rangle_w=0.
\tag{4.4}
\]

Consequently, for every interval block (C\in\mathscr B),

\[
 \left\|\sum_{i\in C}d_i\right\|_w^2
 =\sum_{i\in C}\|d_i\|_w^2.
\tag{4.5}
\]

#### Proof

At a fixed depth,

\[
 \langle \mathbf e_{\tau U}-\mathbf e_U,
          \mathbf e_{\tau V}-\mathbf e_V\rangle
 =2\mathbf1_{\{U=V\}}
  -\mathbf1_{\{\tau U=V\}}
  -\mathbf1_{\{U=\tau V\}}.
\]

If (U\cap B=\varnothing), then \(\tau U=U\) and the difference is zero.
If (U\cap B\ne\varnothing), then \(\tau U\) contains a coordinate of
(A), whereas every old (A)-upper target lies in (Q_A) and avoids
(A).  Hence the two negative coincidences are impossible among old
targets.  This proves (4.3).  Distinct proper cyclic windows of one row are
distinct, proving (4.4) and (4.5).  ∎

The movable flags are collar-scale.  For a fixed coordinate (b\in B),
there are exactly (q+1) cyclic starts for which (S_i) avoids (b) but
(U_{i,q}) contains (b): the coordinate is either the one predecessor
of (S_i) or one of its (q) successors in (U_{i,q}\setminus S_i).
Therefore, writing

\[
 E_q=|\{i\in\mathcal D_j:U_{i,q}\cap B\ne\varnothing\}|,
\]

we have

\[
 \boxed{E_q\le2(q+1)R_m,}
\tag{4.6}
\]

and

\[
 \sum_{i\in\mathcal D_j}\|d_i\|_w^2
 \le4R_m\sum_{q\le H}(q+1)w_q^+.
\tag{4.7}
\]

## 5. Exact energy contraction per interval block

For every signed depth let (\mu_q^\pm(M)) be the flag-load vector and let
(\lambda_q^\pm) be its forced uniform mean.  Give the coordinates
nonnegative depth weights (w_q^\pm), and define the raw square energy

\[
 Q_w(M)=\sum_{q\le H}\sum_{\sigma\in\{-,+\}}
 w_q^\sigma\|\mu_q^\sigma(M)-
 \lambda_q^\sigma\mathbf1\|_2^2.
\tag{5.1}
\]

Every child has the same total load at every signed depth.  Therefore the
balanced factorial excess differs from (Q_w/2) by a constant independent
of the child.  Explicitly, if

\[
 \lambda_q^\sigma=a_q^\sigma+\theta_q^\sigma,
 \qquad 0\le\theta_q^\sigma<1,
\]

then

\[
 \Phi_w(M)
 =\frac12\left(
 Q_w(M)-
 \sum_{q,\sigma}w_q^\sigma N_q^\sigma
 \theta_q^\sigma(1-\theta_q^\sigma)
 \right).
\tag{5.2}
\]

For an old upper target (U), let

\[
 \nu_q(U)=|\{i\in\mathcal D_j:U_{i,q}=U\}|,
\]

and define the activated duplicate curvature

\[
 \boxed{
 \mathcal C_{A,B}
 =\sum_{q\le H}w_q^+
   \sum_{U:U\cap B\ne\varnothing}\binom{\nu_q(U)}2.}
\tag{5.3}
\]

### Theorem 5.1 (biased long-block contraction)

Choose the (B)-side of each interval block independently with probability
(p\), and otherwise choose its (A)-side.  Every outcome is an integral,
lower-saturating, middle-simple token matching and satisfies (3.4).  Its
raw energy obeys the exact identity

\[
 \boxed{
 \mathbb E Q_w(M_p)
 =(1-p)Q_w(M_A)+pQ_w(M_B)
 -4p(1-p)\mathcal C_{A,B}.}
\tag{5.4}
\]

Consequently some deterministic block child satisfies the same upper
bound.  In factorial normalization,

\[
 \mathbb E\Phi_w(M_p)
 =(1-p)\Phi_w(M_A)+p\Phi_w(M_B)
 -2p(1-p)\mathcal C_{A,B}.
\tag{5.5}
\]

#### Proof

Put

\[
 D_C=\sum_{i\in C}d_i,qquad
 D=\sum_{C\in\mathscr B}D_C,qquad
 \bar\mu=(1-p)\mu(M_A)+p\mu(M_B).
\]

The independent-block mean-plus-variance identity gives

\[
 \mathbb E Q_w(M_p)
 =\|\bar\mu-\lambda\|_w^2
 +p(1-p)\sum_C\|D_C\|_w^2.
\tag{5.6}
\]

The endpoint interpolation is

\[
 (1-p)Q_w(M_A)+pQ_w(M_B)
 =\|\bar\mu-\lambda\|_w^2
 +p(1-p)\|D\|_w^2.
\tag{5.7}
\]

By Theorem 4.1, a block contains no repeated activated old upper target,
and positive and negative target sectors are disjoint.  Hence

\[
 \|D\|_w^2-\sum_C\|D_C\|_w^2
 =2\sum_{q,U}w_q^+\nu_q(U)(\nu_q(U)-1)
 =4\mathcal C_{A,B}.
\tag{5.8}
\]

Subtract (5.6) from (5.7).  Equation (5.5) follows from (5.2).  ∎

This proves a literal energy contraction per (O(1)) new boundaries: the
only random atoms are complete physical interval blocks, every atom costs
at most two new runs, and all cross curvature removed by independence is
nonnegative.

There is also an exact descent criterion relative to the better endpoint.

### Corollary 5.2 (gap-versus-curvature descent)

Let

\[
 \Delta=|Q_w(M_B)-Q_w(M_A)|,qquad
 Q_{\min}=\min\{Q_w(M_A),Q_w(M_B)\}.
\]

If

\[
 0\le\Delta<4\mathcal C_{A,B},
\tag{5.9}
\]

then an integral block child satisfies

\[
 \boxed{
 Q_w(M_*)\le Q_{\min}
 -\frac{(4\mathcal C_{A,B}-\Delta)^2}
 {16\mathcal C_{A,B}}.}
\tag{5.10}
\]

If the endpoints have equal energy, one may take (p=1/2), and

\[
 Q_w(M_*)\le Q_w(M_A)-\mathcal C_{A,B}.
\tag{5.11}
\]

#### Proof

Orient the notation so (M_A) is the lower endpoint.  Subtracting
(Q_w(M_A)) from (5.4) gives

\[
 p\Delta-4p(1-p)\mathcal C_{A,B}.
\]

Its minimum on ([0,1]) occurs at

\[
 p=\frac{4\mathcal C_{A,B}-\Delta}
 {8\mathcal C_{A,B}}
\]

under (5.9), and has value equal to the negative term in (5.10).  ∎

For the pair-symmetric construction of this section, equal endpoint energy
is automatic; no globally \(\tau\)-invariant background hypothesis is
needed.  At upper depth (q), define the invariant adjacent stratum

\[
 \mathcal U_{j,q}=\{U:U\cap P_h\ne\varnothing\ (h<j),
                    \ U\text{ avoids at least one of }A,B\}.
\]

Every upper flag has the same first-avoided pair as its lower token.
Therefore phases before (j) and after (j+1) occupy target strata
disjoint from \(\mathcal U_{j,q}\) and are identical in the two endpoints.
On \(\mathcal U_{j,q}\), the coordinate exchange \(\tau\), together with
\(F_B=\tau F_A\), maps the complete selected (A/B)-token family in one
priority orientation bijectively to the complete selected (A/B)-token
family in the other orientation, flags included.  Thus the two upper load
vectors on this stratum are coordinate permutations and have equal energy.
The lower load vectors are identical by (4.1), and middle loads are simple
in both endpoints.  Hence

\[
 \boxed{Q_w(M_A)=Q_w(M_B)}
\tag{5.12a}
\]

separately at every signed depth.  Consequently (5.11) is unconditional
for the same-orientation pair-symmetric atlas.

This endpoint flatness does not extend to refined interval corners: a
mixed interval corner is not the image of either endpoint under one global
coordinate permutation.  Formula (5.8) is exactly the positive
cross-interval curvature removed by that refinement.

The contraction has an exact capacity limitation.  By (4.6), at (q=1)
only

\[
 E_1\le4R_m=O(W/m)
\tag{5.12}
\]

upper occurrences can change.  Replacing one occurrence changes the
duplicate excess

\[
 C(\mu)=\sum_U(\mu(U)-1)_+
\]

by at most one.  At (q=1), opposite orientation has the same two upper
targets as same orientation, because its predecessor and successor formulas
both reduce to (I_\pi(i-1,m+1)) before applying \(\tau\).  Hence any two
children from either transported atlas satisfy

\[
 |C_{U_1}(M)-C_{U_1}(M')|\le4R_m.
\tag{5.13}
\]

Here (E_1) counts movable token replacements.  The symmetric difference
of the two incidence vectors may contain (2E_1\le8R_m) coordinates; this
does not change the one-unit Lipschitz bound per replacement used in
(5.13).

Thus a pre-existing (\Theta(W)) first-upper defect cannot be repaired by
one adjacent-pair atlas.  The theorem contracts exactly the
changed--changed activated duplicates; it does not assert that these
duplicates constitute a fixed positive fraction of the full energy.

## 6. Opposite orientation: exchange paths are physical intervals

Retain (F_B=\tau F_A), but orient every transported (B)-row oppositely.
For an (A)-row \(\pi), the two affected owner maps become

\[
 \boxed{f_A(S_i)=X_{i-1},\qquad f_B(S_i)=\tau X_i.}
\tag{6.1}
\]

### Theorem 6.1 (exact path alignment)

Every maximal cyclic interval

\[
 [a,b]\subseteq\{i:S_i\in\mathcal D_j\}
\]

is exactly one open alternating path

\[
 X_{a-1}-S_a-X_a-S_{a+1}-\cdots-S_b-\tau X_b.
\tag{6.2}
\]

Distinct intervals do not join, and there are no alternating cycles.  Its
exact central children are indexed by a unique threshold

\[
 c\in\{a-1,a,\ldots,b\},
\]

using (A)-tokens on ([a,c]) and (B)-tokens on ([c+1,b]).

#### Proof

If (i,i+1\in\mathcal D_j), then

\[
 X_i=S_i\cup S_{i+1}\subseteq R,
\]

so \(\tau X_i=X_i=f_B(S_i)=f_A(S_{i+1})\).  Conversely, suppose
(f_A(S_s)=f_B(S_t)).  The common owner lies in (R), hence is
\(\tau)-fixed.  Equation (6.1) gives

\[
 X_{s-1}=X_t.
\]

The middle windows of one exact local row family are globally injective,
so (s=t+1) in the paired row.  Therefore the only overlay adjacency is
between consecutive starts of the same \(\mathcal D_j\)-interval.  Its
endpoints are private.  The set \(\mathcal D_j\) cannot fill a row because
every row contains the two coordinates of (B), while its selected lower
windows avoid both.  Thus no component closes cyclically.  The threshold
description follows from Theorem 2.3.  ∎

### Corollary 6.2 (uniform predecessor bound)

Every simultaneous threshold child satisfies

\[
 \boxed{J(M_{\mathbf c})\le J(M_A)+2K_j
 \le O\!\left(\frac{W\log^2m}{m}\right)+4jR_m.}
\tag{6.3}
\]

Thus every threshold corner has predecessor correlation (1-o(1/H))
whenever

\[
 H(\log^2m+j)=o(m).
\tag{6.4}
\]

Indeed, the (A)-prefix is one physical interval in its (A)-row and the
(B)-suffix is one physical interval in the oppositely oriented paired
(B)-row.

For (j=1), the two (B)-coordinates split a cyclic row into two arcs of
(R)-coordinates whose lengths sum to (2m-3).  Exactly one arc has
length at least (m-1).  Therefore every row contains exactly one
nonempty \(\mathcal D_1\)-interval.  In agreement with (2.5), there are
exactly (R_m) paths, and

\[
 \frac{d_1}{R_m}=\frac m2.
\tag{6.5}
\]

For every \(\ell\ge1\), the total number of affected lower vertices on
paths of length less than \(\ell\) is less than

\[
 \ell R_m=\frac{2\ell}{m}d_1.
\tag{6.6}
\]

Hence a (1-o(1)) fraction of the phase-one swap domain lies on paths
longer than any \(\ell=o(m)\).

## 7. Exact multidepth threshold telescope

Read all intervals below in the original (A)-row orientation.  The
oppositely oriented (B)-token has flags

\[
 \boxed{
 L^B_q(i)=I_\pi(i,m-q),
 \qquad
 U^B_q(i)=\tau I_\pi(i-q,m+q).}
\tag{7.1}
\]

The (A)-flags remain those in (1.1).  For a set of consecutive indices
(K), define

\[
 E_r(K)=\sum_{i\in K}\mathbf e_{I_\pi(i,r)}.
\]

Switching precisely the consecutive block (K) from (A) to (B)
changes the flags by

\[
 \boxed{
 z^-_{K,q}=E_{m-q}(K)-E_{m-q}(K+q-1),}
\tag{7.2}
\]

\[
 \boxed{
 z^+_{K,q}=\tau E_{m+q}(K-q)-E_{m+q}(K-1).}
\tag{7.3}
\]

The block (K) may be arbitrarily long.

### Theorem 7.1 (length-independent flag action)

For (1\le q\le H\le m-2),

\[
 \boxed{\|z^-_{K,q}\|_2^2\le2(q-1),}
\tag{7.4}
\]

\[
 \boxed{\|z^+_{K,q}\|_2^2\le6q+2,}
\tag{7.5}
\]

and hence

\[
 \boxed{\|z^-_{K,q}\|_2^2+\|z^+_{K,q}\|_2^2\le8q.}
\tag{7.6}
\]

In particular the unweighted stacked square action through depth (H) is
at most

\[
 \boxed{\sum_{q=1}^H8q=4H(H+1).}
\tag{7.7}
\]

#### Proof

Put (d=q-1).  The two intervals in (7.2) are translates by (d).
All proper cyclic windows in one row are distinct, so cancellation on their
overlap gives

\[
 \|z^-_{K,q}\|_2^2
 =2(|K|-|K\cap(K+d)|)\le2d.
\]

For the upper vector, put (G=K-q) and
(T_h=I_\pi(h,m+q)).  Then (K-1=G+d), and

\[
 z^+_{K,q}=\tau E_{m+q}(G)-E_{m+q}(G+d).
\]

Both families (T_h) and \(\tau T_h) are simple.  A transported target
\(\tau T_h) can equal an old target (T_{h'}\) only if (T_h) avoids
(B), in which case \(\tau T_h=T_h\) and injectivity forces (h'=h).
Therefore the exact identity is

\[
\begin{aligned}
 \|z^+_{K,q}\|_2^2
 ={}&2(|G|-|G\cap(G+d)|)\\
 &+2|\{h\in G\cap(G+d):T_h\cap B\ne\varnothing\}|.
\end{aligned}
\tag{7.8}
\]

The first term is at most (2(q-1)).  Since every switched start has
(S_i\cap B=\varnothing), a fixed coordinate of (B) can enter
(T_{i-q}\) only in the (q) predecessor positions or the one successor
position outside (S_i).  Thus at most (q+1) indices occur for each of
the two (B)-coordinates.  The second term is at most (4(q+1)), proving
(7.5).  ∎

This is the desired multidepth flag-span theorem: the difference of two
long threshold states is an endpoint strip, plus the unavoidable
(A/B)-relabel collar.  It is not proportional to the block length.

There is a sharper all-path sum.  For any simultaneous choice of one
threshold displacement per path,

\[
 \boxed{
 \sum_I\bigl(\|z^-_{I,q}\|_2^2+
              \|z^+_{I,q}\|_2^2\bigr)
 \le4(q-1)K_j+4(q+1)R_m.}
\tag{7.9}
\]

Indeed the two translate-strip contributions give at most
(4(q-1)K_j), while, over one source row, a (B)-coordinate has only
(q+1) eligible collar starts in the disjoint path blocks.

### Corollary 7.2 (integral threshold rounding with exact toll)

On every path choose any monotone fractional profile

\[
 1\ge p_a\ge p_{a+1}\ge\cdots\ge p_b\ge0.
\]

It is the marginal profile of a random threshold.  Choose thresholds
independently between paths.  Every outcome is an integral exact central
matching satisfying (6.3).  If \(\bar\mu\) is its mean flag load, then

\[
 \mathbb E Q_w(M)
 =Q_w(\bar\mu)+
  \sum_I\mathbb E\|Z_I-\mathbb EZ_I\|_w^2.
\tag{7.10}
\]

Moreover the variance term is at most

\[
\boxed{
 K_j\sum_{q\le H}(q-1)(w_q^-+w_q^+)
 +2R_m\sum_{q\le H}(q+1)w_q^+.}
\tag{7.11}
\]

Here (7.11) uses the two-copy variance identity

\[
 \operatorname{Var}Z=\frac12\mathbb E\|Z-Z'\|^2
\]

and (7.9).

For bounded weights and (H=\lceil A\sqrt m\rceil), (7.11) is only

\[
 O_A(jW),
\tag{7.12}
\]

not (o(W)).  For (H=\sqrt m\,\omega(m)), it is
(O(jW\omega(m)^2)).  Thus ordinary independent threshold rounding is
critical at the Gaussian scale even though it is exact and has perfect
long-block physical correlation.

At (q=1), (7.2) vanishes and (7.3) is exactly the same transported
upper innovation as in the same-orientation construction.  Consequently
fair whole-path coins have the positive duplicate contraction of Theorem
5.1 at the first upper depth.  Starting at (q=2), the lower endpoint
strips and the upper orientation coboundaries have signed cross Grams; no
positivity theorem for their sum is proved.

For one deterministic threshold displacement (z), the exact raw-energy
change is

\[
 Q_w(M+z)-Q_w(M)
 =2\langle\mu(M)-\lambda,z\rangle_w+\|z\|_w^2.
\tag{7.13}
\]

Theorem 7.1 controls the curvature term by (O(H^2)) per path and the run
toll by (O(1)), but it gives no sign for the first term.  The missing
signed endpoint-strip theorem is precisely a statement that selects common
thresholds for which the negative linear signal dominates this audited
curvature.

There is nevertheless an exact parity-sharp correlated theorem after two
candidate thresholds have been fixed on every path.

### Theorem 7.3 (parity-sharp threshold-pair rounding)

For each opposite-orientation path (I), choose two legal thresholds with
flag incidence vectors (a_I^0,a_I^1), and put

\[
 z_I=a_I^1-a_I^0.
\]

Let (a_{\rm fr}) be the unchanged flag contribution and define the
coordinatewise pair sum

\[
 t=2a_{\rm fr}+\sum_I(a_I^0+a_I^1).
\]

For a target class \(\alpha\), write its fixed total load as

\[
 T_\alpha=c_\alpha N_\alpha+\rho_\alpha,
 \qquad0\le\rho_\alpha<N_\alpha,
\]

and set

\[
 b_c(t)=\min_{u+v=t}\{e_c(u)+e_c(v)\}
 =\left\lfloor\frac{(t-2c-1)^2}{4}\right\rfloor.
\]

Define

\[
 B_w=\sum_{\alpha,T}w_\alpha b_{c_\alpha}(t_\alpha(T)),
 \qquad
 O_w=\sum_{\alpha,T}w_\alpha
       \mathbf1_{\{t_\alpha(T)\ {\mathrm{odd}}\}},
\tag{7.14}
\]

and

\[
 D_w=\min_{\varepsilon_I\in\{\pm1\}}
 \left\|\sum_I\varepsilon_Iz_I\right\|_w^2.
\tag{7.15}
\]

Then one integral threshold corner satisfies

\[
 \boxed{
 \Phi_w(M)\le\frac{B_w}{2}+\frac{D_w-O_w}{8}.}
\tag{7.16}
\]

Every corner in (7.16) obeys the deterministic run bound (6.3), and

\[
 D_w\ge O_w,
 \qquad
 D_w\le\sum_I\|z_I\|_w^2.
\tag{7.17}
\]

#### Proof

For a sign vector \(\varepsilon\), the two complementary legal corners
have loads

\[
 \mu^\varepsilon
 =\frac12\left(t+\sum_I\varepsilon_Iz_I\right),
 \qquad
 \mu^{-\varepsilon}
 =\frac12\left(t-\sum_I\varepsilon_Iz_I\right).
\]

For integers (d\equiv t\pmod2), direct expansion gives

\[
 e_c\!\left(\frac{t+d}{2}\right)
 +e_c\!\left(\frac{t-d}{2}\right)
 =b_c(t)+\frac{d^2-\mathbf1_{\{t\ {\mathrm{odd}}\}}}{4}.
\tag{7.18}
\]

Apply (7.18) coordinatewise, choose a sign minimizing (7.15), and then
choose the better complementary corner.  Parity gives (D_w\ge O_w).
Independent fair signs give the second inequality in (7.17).  ∎

The theorem has a concrete collar-overlap sufficient condition.  Since
Theorem 7.1 gives (z_I(\gamma)\in\{-1,0,1\}) for every target-depth
coordinate \(\gamma\), put

\[
 r_\gamma=|\{I:z_I(\gamma)\ne0\}|,
 \qquad
 \Gamma_w=\sum_\gamma w_\gamma\binom{r_\gamma}{2}.
\]

Then

\[
 D_w-O_w\le2\Gamma_w.
\tag{7.19}
\]

Indeed the independent-sign action minus its forced parity is

\[
 \sum_\gamma w_\gamma
 \bigl(r_\gamma-(r_\gamma\bmod2)\bigr)
 \le2\Gamma_w.
\]

Thus

\[
 \boxed{B_w=o(W),\qquad\Gamma_w=o(W)}
\tag{7.20}
\]

is a fully explicit sufficient condition for an integral low-run corner
with factorial excess (o(W)).  Neither estimate in (7.20) is proved by
the adjacent-swap geometry.

The first upper rank supplies a sharp necessary preparation condition.
Let

\[
 C_1(M_A)=\sum_U(\mu_1^+(U)-1)_+.
\]

For any two corners (M^0,M^1) from either transported atlas, define

\[
 B_1^+(M^0,M^1)
 =\sum_U b_0(\mu_1^0(U)+\mu_1^1(U)).
\]

Since at most (E_1\le4R_m) old first-upper occurrences can move in
each corner,

\[
 \boxed{
 B_1^+(M^0,M^1)\ge C_1(M_A)-4R_m.}
\tag{7.21}
\]

To prove (7.21), let (d_h(U)) count old occurrences removed at (U) in
corner (h\).  Additions only increase pair sums, so

\[
 \mu_1^0(U)+\mu_1^1(U)
 \ge2\mu_1^A(U)-d_0(U)-d_1(U).
\]

The function

\[
 b_0(t)=\left\lfloor\frac{(t-1)^2}{4}\right\rfloor
\]

is nondecreasing and satisfies (b_0(t)\ge t/2-1).  Summing over targets
with \(\mu_1^A(U)\ge1), and using
\(\sum_Ud_h(U)\le4R_m\), proves (7.21).

Consequently a necessary condition for the threshold-pair floor in
(7.16) to be (o(W)) is

\[
 \boxed{C_1(M_A)=o(W).}
\tag{7.22}
\]

This obstruction is stronger than orbit-mean uniformity: coordinate orbit
averaging can make the fractional mean uniform while preserving the
duplicate energy of every integral member.

## 8. Midpoint rigidity and invariant sectors

The new path thresholds do not furnish a nontrivial rounding of the exact
endpoint midpoint marginals.

### Theorem 8.1 (path midpoint rigidity)

Let (u_1\ge\cdots\ge u_k) be the (A)-edge indicators of a random legal
state on one nontrivial exchange path.  If

\[
 \mathbb Eu_i=\frac12\qquad(1\le i\le k),
\]

then almost surely

\[
 u_1=\cdots=u_k,
\]

and the law is the fair coin on the two endpoint states.

#### Proof

Every (u_i-u_{i+1}\) is nonnegative, while its expectation is zero.
Hence (u_i=u_{i+1}) almost surely for every (i).  The common bit has
mean (1/2).  ∎

Thus an interior long-block threshold can be used only by moving the
fractional mean away from the endpoint midpoint, or by coupling different
paths through an additional shadow-twin theorem.  The balanced-point
convex decomposition alone does not supply that theorem.

There are also exact invariant target sectors for a single adjacent swap.

* Every changed lower flag is a subset of (S\subseteq R).  Hence all
  lower target coordinates meeting (A\cup B) are fixed.
* Every old upper flag avoids (A), and every new upper flag avoids (B).
  Hence every upper target meeting both (A) and (B) is fixed.
* The entire outgoing lower load (L_1) is fixed pointwise.

Therefore the span of the adjacent-swap vectors is a proper subspace of
the full multidepth target space.  Hence a negative-step theorem cannot be
deduced from the size of the **total** collision energy without also
bounding its invariant orthogonal projection.  This is a linear-algebraic
obstruction; no separate exact-factor example concentrating arbitrary
energy in that projection is asserted.  A valid descent theorem must
measure the defect charged to the activated pair-collar or combine many
pair atlases and prove a coverage inequality.

## 9. Audited implication scope

The decisive geometry and constants were checked independently in two
audits.  The following corrections and scope restrictions are essential.

1. On an open alternating path, exact central children are thresholds, not
   merely the two component sides.  On a cycle there are only the two
   sides.  Earlier cube formulations that treat an open path as one binary
   component discard valid integral states.

2. Low-run endpoints do not imply low-run generic component cuts.  The
   positive row bound here uses the proved same-orientation singleton
   structure or the proved opposite-orientation equality between exchange
   order and physical interval order.

3. The constants
   \[
   2(q-1),\qquad6q+2,
   \qquad4H(H+1)
   \]
   in Theorem 7.1 were checked from the exact window-overlap identity
   (7.8), including (q=1) and length-one paths.

4. The contraction (5.4) is for the raw square energy.  The corresponding
   balanced factorial gain is exactly half as large, as in (5.5).  No
   floor term changes because all children have identical total slot
   counts.

5. For the same-orientation pair-symmetric construction
   (F_B=\tau F_A), endpoint energy equality is automatic rank by rank.
   The reason is first-avoided upper-stratum separation, not invariance of
   every unrelated local factor.  Thus (5.11) is unconditional in this
   factor class.  Formula (5.9) remains the correct robust statement if
   this exact pair symmetry is perturbed.

6. The first-upper edit capacity is (O(W/m)), not (O(W)).  Hence this
   one adjacent switch cannot repair an arbitrary linear first-upper
   defect, even though \(|\mathcal D_1|=(1/16+o(1))W\).

7. Opposite orientation proves exact integrality, predecessor correlation,
   and an (O(H^2)) length-independent flag diameter.  It does not prove a
   simultaneous all-depth energy contraction: the signed endpoint-strip
   Gram theorem is still unproved, and the available variance bound is
   critical (O(W)) at (H=\Theta(\sqrt m)).

8. Every child contains exactly (T) selected tokens and exactly (T)
   distinct middle owners, leaving the same **number**
   (W-T=2W/(m+2)) of middle owners unused as the endpoints; the unused
   set itself may depend on the thresholds.  It is therefore an integral literal
   row construction, not a fractional or labelled synchronization.  It is
   not being called a perfect middle factor on all (W) owners.  After
   cutting its (J) selected runs and emitting their genuine (H)-collars,
   its core word cost is (T+O(HJ)).  Adding genuine singleton collars for
   the unused owners gives total length
   \[
     W+O\!\left(HJ+\frac{HW}{m}\right)=W+o(W)
   \]
   whenever (J=o(W/H)) and (H=o(m)).  Thus the literal skeleton length is
   unconditional in the stated range;
   proving that this skeleton covers the required multidepth targets, or
   repairing its holes within (o(W)), still requires the explicitly
   unproved defect bound.

## 10. Final proved/conditional boundary

The following theorem-level advance is unconditional.

> **Aligned adjacent-pair rounding theorem.**  For every exact local
> factor (F_A), the transported factor (F_B=\tau F_A) can be oriented
> in either of two ways.  Same orientation yields an exact atlas of
> independently signable physical interval blocks with the positive-Gram
> contraction (5.4).  Opposite orientation yields one exact exchange path
> per maximal changed physical interval, every threshold corner has the
> run bound (6.3), and every threshold displacement satisfies
> (7.4)--(7.9).  All resulting objects are integral, middle-simple, and
> retain literal complete flags from their source rows.

What is not proved is either of the following sufficient statements.

* **UNPROVED charged coverage:** the activated duplicate curvature
  \(\mathcal C_{A,B}\), averaged or summed over a quota-safe family of
  adjacent pairs, dominates the non-invariant collision energy up to
  (o(W)), while the first-upper starting defect is already (o(W)).

* **UNPROVED signed strip routing:** the opposite-orientation path strips
  admit a common correlated threshold law whose mean reaches the required
  fractional cancellation and whose parity-corrected covariance toll is
  (o(W)), not merely (O(W)).

Either statement would compose with the already audited literal repair
machinery.  Neither follows from projected star codegree, ordinary negative
dependence, endpoint low-run bounds, or the balanced orbit decomposition.
