# Pair-omission tokens: a zero-boundary run atlas and the exact priority-refresh charge

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or
long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad L=2m-1,
 \qquad R_m=\frac1L\binom{2m-1}{m-1}=\operatorname{Cat}_{m-1}.
\tag{0.1}
\]

This note closes the row-run-boundary ledger for two explicit
common-base token operations.

First, every maximal selected interval in the first-avoided-pair spine has
two canonical central matchings: attach every lower token to its predecessor
middle window, or attach every lower token to its successor middle window.
The choices are independent over all selected intervals.  Every corner is
an integral lower-saturating matching, and every corner has **exactly the
same selected source positions**.  Consequently

\[
 \boxed{J(M_\varepsilon)=J(M_0)\quad\hbox{for every corner }\varepsilon.}
\tag{0.2}
\]

Thus an arbitrary number of contractions inside this run-orientation atlas
creates no new physical row boundary at all.  The flag displacement is
computed exactly in (3.4) below; it is supported only at the two ends of the
run, vanishes at depth one, and vanishes at every depth on a full cyclic row.

Second, interchange two adjacent pairs in the first-avoided priority order,
at positions \(j,j+1\).  The old and new matchings differ only on lower sets
which meet every earlier pair and avoid both interchanged pairs.  In each of
the two affected local factors this difference occupies at most \(2j\)
cyclic intervals per source row.  Hence its exact carrier charge is at most

\[
 \boxed{b_j\le
 \min\{4jR_m,\,2|\mathcal D_j|\}.}
\tag{0.3}
\]

If the two affected factors are paired by the coordinate involution
\(\vartheta\) interchanging the adjacent omitted pairs, these carrier
intervals may themselves be chosen independently.  Every corner remains a
matching, packetization loses no individual variance, and the joined Gram
is the nonnegative explicit collision excess

\[
 \left\|\sum_Iz_I\right\|_w^2-\sum_I\|z_I\|_w^2
 =2\sum_{q=1}^Hw_q
   \sum_{U:\,U\cap B\ne\varnothing}\mu_q(U)(\mu_q(U)-1).
\tag{0.3a}
\]

Uniformly over all priority positions \(j\),

\[
 b_j=O\!\left(\frac{W\log m}{m}\right)=o(W/H)
\tag{0.3b}
\]

whenever \(H=o(m/\log m)\).

In particular, every permutation of the first \(t\) priority pairs can be
reached from the original matching through adjacent-priority alternating
components with cumulative carrier charge

\[
 \boxed{B_t<2R_mt^3.}
\tag{0.4}

For \(t=\lceil20\log m\rceil\),

\[
 B_t=O\!\left(\frac{W\log ^3m}{m}\right)=o(W/H)
 \quad\text{whenever}\quad H=o(m/\log ^3m).
\tag{0.5}
\]

This includes every fixed Gaussian window \(H=\lceil A\sqrt m\rceil\),
with exact ratio

\[
 \frac{B_t}{W/H}
 <\frac{Ht^3(m+1)}{(2m+1)(2m-1)}=o_A(1).
\tag{0.6}
\]

Therefore the row-boundary cost does not obstruct a contraction theorem
based on the run-orientation cube, nor a contraction using one logarithmic
priority-refresh atlas.  More generally, \(K_m\) such refreshes cost
\(o(W/H)\) provided \(K_mHt^3/m\to0\).  The remaining question is the
energy/Gram strength of these explicit cells, not their physical run cost.

## 1. An exact boundary calculus

Throughout the theorem statements, \(J\) denotes the physical cyclic run
count, with a nonempty full cyclic row counted as one run.  The following
linear-cut formula is a convenient proof device.  Its cyclic analogue is
obtained by joining the two ends and is the version used in the carrier
bounds below.

Fix a linear cut in every cyclic source row and write its binary selection
word as

\[
 x=(x_0,\ldots,x_{L-1})\in\{0,1\}^L.
\]

Its number of selected linear runs is

\[
 J(x)=x_0+\sum_{i=1}^{L-1}(1-x_{i-1})x_i.
\tag{1.1}
\]

Adjoin zeros at the two ends.  Then

\[
 2J(x)=|x_0|+\sum_{i=1}^{L-1}|x_i-x_{i-1}|+|x_{L-1}|.
\tag{1.2}
\]

### Lemma 1.1 (XOR boundary inequality)

For two selection words \(x,y\), put \(d=x\mathbin\triangle y\),
coordinatewise.  Then

\[
 \boxed{|J(y)-J(x)|\le J(d).}
\tag{1.3}
\]

The same assertion holds for cyclic run counts, with a full cyclic word
counted as one run.

#### Proof

On every edge of the zero-extended line, the boundary indicator of \(y\)
is the XOR of the boundary indicators of \(x\) and \(d\).  Its absolute
value is therefore at most their sum.  Equation (1.2) gives
\(J(y)\le J(x)+J(d)\).  Interchanging \(x,y\) gives (1.3).

On a circle the identical argument applies to the cyclic edge boundary.
If none of the three words is full, half the cyclic boundary is exactly the
run count.  The exceptional full/empty cases satisfy the displayed
inequality directly: a nonconstant word and its complement have the same
positive number of cyclic runs. \(\square\)

Thus the correct charge of a token exchange is the number of rowwise
intervals in its carrier, not the number of changed tokens.  For a sequence
of exchanges with carriers \(d_s\),

\[
 J(x_T)-J(x_0)\le\sum_sJ(d_s).
\tag{1.4}
\]

This is a worst-case pathwise bound; cancellations can make the final
increase smaller.

## 2. The first-avoided spine

Fix ordered disjoint coordinate pairs

\[
 P_1,\ldots,P_m
\]

and one unused coordinate.  For every \(j\), fix an exact central wreath
factor \(F_j\) on \(Q_j=[n]\setminus P_j\).  In a row

\[
 \pi=(x_0,\ldots,x_{L-1})
\]

put, with cyclic indices,

\[
 S_i=I_\pi(i,m-1),\qquad X_i=I_\pi(i,m).
\tag{2.1}
\]

Select position \(i\) in \(F_j\) exactly when

\[
 \kappa(S_i)=j,
\tag{2.2}
\]

where \(\kappa\) is the first pair avoided by the set.  The selected
positions in every source row split into maximal cyclic intervals.  The
proof of Theorem 5.1 in
`PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md` gives

\[
 J_0=O\!\left(\frac{W\log ^2m}{m}\right).
\tag{2.3}
\]

Both middle windows adjacent to \(S_i\) contain it:

\[
 S_i=X_{i-1}\cap X_i.
\tag{2.4}
\]

Call the edges \((S_i,X_{i-1})\) and \((S_i,X_i)\) respectively the
predecessor and successor token at position \(i\).

Formally, the source token graph chooses the predecessor orientation as one
section.  Here we use its physical two-orientation lift: an unoriented
wreath row may be traversed in either direction, so the successor edge is
the predecessor token of the reversed cyclic order.  Different maximal
selected intervals may choose their directions independently because each
interval receives its own standard initialization collar.  This lift adds
no row, owner, or boundary; it only records the two literal traversals
already available on every physical row segment.

## 3. The zero-boundary run-orientation atlas

For every maximal selected interval \(I=[a,b]\) in one source row, choose
one of the following two matchings:

\[
 \{(S_i,X_{i-1}):i\in I\},
 \qquad
 \{(S_i,X_i):i\in I\}.
\tag{3.1}
\]

The union of the two edge sets is the alternating path

\[
 X_{a-1}-S_a-X_a-S_{a+1}-\cdots-S_b-X_b.
\tag{3.2}
\]

It may be made a literal alternating cycle by adjoining one private dummy
lower vertex at the two exposed middle endpoints.  Deleting that dummy
recovers exactly the original token switch and changes no physical flag or
boundary count.

### Theorem 3.1 (independent run atlas)

Choose predecessor or successor orientation independently on every maximal
selected interval of the first-avoided spine.  Every choice is a matching
which saturates every lower target exactly once, and

\[
 J(M_\varepsilon)=J_0.
\tag{3.3}
\]

#### Proof

The lower endpoints are unchanged, so lower saturation is automatic.  In
one source row, two distinct maximal selected intervals have at least one
unselected position between them.  Shifting either interval's middle-index
set from \(I-1\) to \(I\) cannot make it meet the shifted middle-index set
of another interval.  Thus all chosen middle endpoints in that row are
distinct.  Different rows of one \(F_j\) own disjoint middle windows.

Finally, if \(S_i\) has category \(j\), then both \(X_{i-1}\) and \(X_i\)
avoid \(P_j\) and meet every earlier pair, because they contain \(S_i\).
They therefore also have category \(j\).  Middle endpoints used in
different phases are disjoint.  This proves the matching assertion.

The selected source positions were never changed.  Their maximal intervals,
and hence their number, are exactly the same at every corner. \(\square\)

The complete two-parent flag displacement is also explicit.  For a cyclic
index interval \(I\) and a window length \(r\), write

\[
 E_{\pi,r}(I)=\sum_{i\in I}{\bf1}_{I_\pi(i,r)}.
\]

At signed depth \(q\), successor minus predecessor orientation on \(I\)
has displacement

\[
 \boxed{
 \begin{aligned}
 z^-_{I,q}
 &=E_{\pi,m-q}(I)-E_{\pi,m-q}(I+q-1),\\
 z^+_{I,q}
 &=E_{\pi,m+q}(I-q)-E_{\pi,m+q}(I-1).
 \end{aligned}}
\tag{3.4}
\]

Indeed, the predecessor flags at position \(i\) are

\[
 I_\pi(i+q-1,m-q),\qquad I_\pi(i-1,m+q),
\]

whereas the successor flags are

\[
 I_\pi(i,m-q),\qquad I_\pi(i-q,m+q).
\]

In particular

\[
 z^-_{I,1}=z^+_{I,1}=0.
\tag{3.5}
\]

If \(I\) is the full cyclic row, both vectors vanish for every \(q\).
For \(q\le H<L/2\), every window in (3.4) is proper except possibly the
upper window at \(q=m-1\).  Proper cyclic windows have distinct starts, and
shifting an interval by \(q-1\) changes at most \(2(q-1)\) positions.  In
the exceptional full-window case the corresponding displacement is zero.
Consequently

\[
 \boxed{
 \|z^-_{I,q}\|_2^2\le2(q-1),\qquad
 \|z^+_{I,q}\|_2^2\le2(q-1).}
\tag{3.6}
\]

For arbitrary nonnegative signed depth weights \(w_q^\pm\), this gives

\[
 \|z_I\|_w^2
 \le2\sum_{q=2}^H(q-1)(w_q^-+w_q^+).
\tag{3.7}
\]

Formula (3.4) is also an exact joined-owner cross-Gram formula: the inner
product of two run innovations is the signed number of coincidences among
their four shifted endpoint strips, with the prescribed depth weights.
No abstract owner variance remains in this atlas.

### Corollary 3.2 (boundary-free contraction iteration)

Let \(\mathcal E_H\ge0\) be any weighted multidepth defect on the corners
of the atlas.  Suppose an endpoint-stable kernel on these corners has, above
a threshold \(T_m\), conditional drift

\[
 \mathbb E[\mathcal E_H(M')\mid M]
 \le(1-\lambda_m)\mathcal E_H(M)+\lambda_mT_m,
 \qquad 0<\lambda_m\le1.
\tag{3.8}
\]

Then for every \(R\ge0\) there is a deterministic sequence of atlas corners
such that

\[
 \mathcal E_H(M_R)
 \le T_m+(1-\lambda_m)^R
       (\mathcal E_H(M_0)-T_m)_+,
\tag{3.9}
\]

while

\[
 \boxed{J(M_R)=J_0\quad\text{for every }R.}
\tag{3.10}
\]

Thus, for any positive \(\eta_m\to0\), if \(T_m=o(W)\) and

\[
 R\ge \lambda_m^{-1}
 \log^+\!\frac{(\mathcal E_H(M_0)-T_m)_+}{\eta_mW},
\]

then \(\mathcal E_H(M_R)\le T_m+\eta_mW=o(W)\), with zero boundary
increase.  The conclusion is
independent of the number of iterations.

#### Proof

At each step above \(T_m\), some corner in the kernel support is no worse
than its conditional expectation.  Once the defect is at most \(T_m\), keep
the current corner fixed; this also obeys the affine recurrence.  Iterating
that recurrence proves (3.9).
Equation (3.10) is Theorem 3.1. \(\square\)

## 4. Adjacent-priority refreshes

The run atlas keeps the selected lower token positions fixed.  A second
explicit operation changes the spine itself while retaining a sharp
boundary charge.

Fix the local factors \(F_P\) for all pairs in the priority list.  Let
\(A,B\) occupy adjacent positions \(j,j+1\), and interchange them.  A lower
set changes its assigned factor if and only if it lies in

\[
 \mathcal D_j=\{S:S\cap P_h\ne\varnothing\ (h<j),\quad
                    S\cap A=S\cap B=\varnothing\}.
\tag{4.1}
\]

### Lemma 4.1 (exact change domain)

Outside \(\mathcal D_j\) the old and new first-avoided assignments agree.
Every \(S\in\mathcal D_j\) moves from factor \(F_A\) to factor \(F_B\).
Moreover,

\[
 |\mathcal D_j|
 =\sum_{\ell=0}^{j-1}(-1)^\ell\binom{j-1}{\ell}
   \binom{2m-3-2\ell}{m-1},
\tag{4.1a}
\]

where an out-of-range binomial coefficient is zero.

#### Proof

If \(S\) avoids both \(A,B\), their interchange changes which of them is
first.  If it avoids exactly one, that same pair is first in both orders.
If it meets both, neither can be first.  The earlier-pair conditions in
(4.1) are exactly the assertion that the first avoided pair is one of
\(A,B\).  After deleting the four coordinates of \(A\cup B\), apply
inclusion--exclusion to the \(j-1\) requirements that \(S\) meet an earlier
pair.  Deleting \(\ell\) selected earlier pairs leaves
\(2m-3-2\ell\) available coordinates, proving (4.1a). \(\square\)

For a coordinate pair \(C\subset Q_P\), the starts in a cyclic row of
\(F_P\) whose length-\((m-1)\) window avoids \(C\) form at most two cyclic
intervals: omission of one coordinate is one circular arc of starts, and
the desired set is the intersection of two such arcs.

### Lemma 4.2 (rowwise carrier bound)

In every source row of \(F_A\), the positions representing sets in
\(\mathcal D_j\) form at most \(2j\) cyclic intervals.  The same is true in
every source row of \(F_B\).

#### Proof

Inside \(F_A\), membership in \(\mathcal D_j\) says: avoid \(B\), and do
not avoid any of the \(j-1\) earlier pairs.  The first condition has at most
two cyclic components.  The union of the earlier-pair avoidance sets has at
most \(2(j-1)\) components.  If \(j=1\), there is no earlier condition and
the desired set has at most two components directly.  If \(j\ge2\), the
complement of that union is either empty or has at most \(2(j-1)\)
components.  On a circle, intersecting a set with \(r\) components and a
set with \(s\) components has at most \(r+s\) components, because every
resulting component begins at a boundary point of one of the two sets.
The asserted \(2j\) bound follows.  The proof in \(F_B\), with \(A\) in
place of \(B\), is identical. \(\square\)

Each local factor has exactly \(R_m\) rows.  Lemmas 1.1 and 4.2 therefore
give the promised charge.

The floor at the first upper rank needs separate notation because it is
zero.  Every lower-saturating matching has exactly

\[
 T=\binom n{m-1}
\tag{4.1b}
\]

tokens, hence exactly \(T\) flags at every signed depth.  Put

\[
 N_q^\pm=\binom n{m\pm q},\qquad
 \frac{T}{N_q^\pm}=c_q^\pm+\theta_q^\pm,\qquad
 c_q^\pm=\left\lfloor\frac{T}{N_q^\pm}\right\rfloor.
\tag{4.1c}
\]

Since \(N_1^+=\binom n{m+1}=W\) and

\[
 \frac{T}{W}=\frac{m}{m+2}<1,
\]

one has

\[
 \boxed{c_1^+=0.}
\tag{4.1d}
\]

Accordingly no expression below divides by \(c_q^\pm\).  For arbitrary
positive finite weights \(w_q^\pm\), the exact floor polynomial is

\[
 \mathcal Q_w
 =\sum_{q,\pm}w_q^\pm\sum_R
  (\mu_{q,R}^\pm-c_q^\pm)(\mu_{q,R}^\pm-c_q^\pm-1).
\tag{4.1e}
\]

If \(f_{q,R}^\pm=\mu_{q,R}^\pm-T/N_q^\pm\), direct expansion gives

\[
 \mathcal Q_w=\|f\|_w^2-
 \sum_{q,\pm}w_q^\pm N_q^\pm
       \theta_q^\pm(1-\theta_q^\pm).
\tag{4.1f}
\]

At \(q=1,+\), the summand in (4.1e) is literally
\(\mu(\mu-1)\).  Thus the zero floor causes no singularity and every Gram
identity below transfers exactly to floor-energy differences.

There is a particularly useful common-base version.  Write

\[
 A=\{a_1,a_2\},\qquad B=\{b_1,b_2\},\qquad
 \vartheta=(a_1\ b_1)(a_2\ b_2),
\tag{4.2}
\]

and choose the two local factors compatibly:

\[
 F_B=\vartheta F_A.
\tag{4.3}
\]

If \(S\in\mathcal D_j\), then \(\vartheta S=S\).  Its token in \(F_B\)
is therefore the \(\vartheta\)-image of its token in \(F_A\).

### Theorem 4.3 (independent adjacent-pair run atlas and exact Gram)

Assume (4.3), and group the positions representing \(\mathcal D_j\) into
maximal cyclic intervals in the paired rows \(\pi\in F_A\) and
\(\vartheta\pi\in F_B\).  Independently for every such interval, use all
its \(F_A\)-tokens or all its \(F_B\)-tokens.  Then:

1. every corner is an integral lower-saturating matching;
2. every corner satisfies
   \[
    [J(M_\varepsilon)-J(M_A)]_+
    \le\min\{4jR_m,\,2|\mathcal D_j|\};
   \tag{4.4}
   \]
3. if \(d_S\) is the flag displacement of the \(F_A\)-token to the
   \(F_B\)-token, then, for every \(q\le H\),
   \[
    d^-_{S,q}=0,
    \qquad
    d^+_{S,q}={\mathbf 1}_{\vartheta U_q(S)}
              -{\mathbf 1}_{U_q(S)};
   \tag{4.5}
   \]
4. for arbitrary nonnegative upper-depth weights \(w_q\),
   \[
    \boxed{
    \langle d_S,d_T\rangle_w
    =2\sum_{q=1}^Hw_q\,
      {\bf1}_{\{U_q(S)=U_q(T),\ U_q(S)\cap B\ne\varnothing\}}
    \ge0.}
   \tag{4.6}
   \]

Here \(w_q=w_q^+\) from (4.1e); the lower-depth contribution is identically
zero by (4.5).  Thus (4.6) includes the exact floor-corrected energy even
though \(c_1^+=0\).

If \(H\le m-2\), the innovations belonging to distinct starts in one
source row are orthogonal.  Hence, if \(I\) ranges over the maximal
\(\mathcal D_j\)-intervals and \(z_I=\sum_{S\in I}d_S\), then

\[
 \boxed{
 \sum_I\|z_I\|_w^2=\sum_{S\in\mathcal D_j}\|d_S\|_w^2,}
\tag{4.7}
\]

and the joined coherence left after run packetization is exactly

\[
 \boxed{
 \left\|\sum_Iz_I\right\|_w^2-
 \sum_I\|z_I\|_w^2
 =2\sum_{q=1}^Hw_q
   \sum_{\substack{U:\ U\cap B\ne\varnothing}}
        \mu_q(U)(\mu_q(U)-1),}
\tag{4.8}
\]

where \(\mu_q(U)=|\{S\in\mathcal D_j:U_q(S)=U\}|\).

#### Proof

For \(S\in\mathcal D_j\), let \(Y_A(S)\) be its middle endpoint in
\(F_A\); its alternative endpoint is \(Y_B(S)=\vartheta Y_A(S)\).  Suppose
\(Y_A(S)=Y_B(T)\).  The left side avoids \(A\), while the right side avoids
\(B\); their common value avoids both pairs and is therefore
\(\vartheta\)-fixed.  It follows that \(Y_A(S)=Y_A(T)\), and injectivity of
the middle windows of \(F_A\) gives \(S=T\).  The same argument with
\(A,B\) interchanged handles the other mixed orientation.  Thus arbitrary
tokenwise choices, and hence arbitrary runwise choices, have distinct
middle endpoints among the changed lower sets.

They also avoid every unchanged middle endpoint.  Indeed,
\(Y_B(S)=\vartheta Y_A(S)\) avoids \(B\) and meets every pair preceding
\(A\).  If it meets \(A\), it has old category \(B\), and injectivity of
the middle windows inside \(F_B\) separates it from every unchanged
category-\(B\) token.  If it avoids \(A\), then it avoids \(A\cup B\), is
\(\vartheta\)-fixed, and equals \(Y_A(S)\); uniqueness in the original
matching separates it from all other endpoints.  Its category precludes a
collision with any remaining phase.  This proves item 1.

There are at most
\(\min\{2jR_m,|\mathcal D_j|\}\) run bits: Lemma 4.2 gives the first
bound, while every nonempty run contains a distinct member of
\(\mathcal D_j\).  Switching one bit
toggles one interval in its \(F_A\)-row and the paired interval in its
\(F_B\)-row.  Its carrier charge is at most two.  Lemma 1.1 gives (4.4).

Every lower flag is a subset of \(S\), which is fixed by \(\vartheta\),
so the lower displacement is zero.  Every upper flag is carried to its
\(\vartheta\)-image, proving (4.5).  Both \(U_q(S)\) and \(U_q(T)\) avoid
\(A\).  A mixed equality \(\vartheta U_q(S)=U_q(T)\) would avoid both
\(A,B\), hence would be fixed by \(\vartheta\), and would force
\(U_q(S)=U_q(T)\).  Expanding the four terms in the inner product now gives
(4.6): when the common target avoids \(B\), the two signed vectors vanish;
when it meets \(B\), their inner product is two.

For \(q\le m-2\), upper cyclic windows in one source row are proper and
have distinct starts.  Thus (4.6) is zero for distinct starts in that row,
which proves (4.7).  Finally expand the square of the total innovation and
use (4.6).  The ordered unequal pairs with common target \(U\) are counted
by \(\mu_q(U)(\mu_q(U)-1)\), proving (4.8). \(\square\)

This is the required positive-along-rows correlation: a whole physical
interval is one Haar bit, but packetization loses none of the individual
variance.  At the same time all cross-packet Gram terms have the favourable
sign and are the explicit collision excess (4.8).

### Corollary 4.4 (iteration in one adjacent-pair atlas)

Suppose an endpoint-stable kernel on the corners of the atlas in Theorem
4.3 satisfies the affine defect contraction (3.8), with threshold
\(T_m=o(W)\).  Then deterministic iteration reaches defect \(o(W)\) while,
at every intermediate and final corner,

\[
 J(M)\le J(M_A)+\min\{4jR_m,2|\mathcal D_j|\}.
\tag{4.9}
\]

Uniformly for every \(1\le j<m\), the added term is
\(O(W\log m/m)=o(W/H)\) when \(H=o(m/\log m)\).  There is no
multiplication by the number of contraction rounds.

#### Proof

The deterministic energy iteration is exactly Corollary 3.2.  Every
iterate remains one corner of the same fixed atlas, so (4.4), rather than
a stepwise triangle inequality, applies directly to it.

For the uniform asymptotic, use the first bound in (4.4) when
\(j\le u=\lceil20\log m\rceil\).  When \(j>u\), the category-tail estimate
(5.10) of the source theorem applies because
\(\mathcal D_j\) is contained in category \(j\):

\[
 |\mathcal D_j|
 \le C_0\sqrt m\binom{2m-1}{m-1}(3/4)^{j-1}.
\tag{4.9a}
\]

The two ranges give

\[
 \min\{4jR_m,2|\mathcal D_j|\}
 =O(W\log m/m)
\]

uniformly in \(j\).  In the first range this follows from (5.2); in the
second, \((3/4)^u=O(m^{-5})\).  Dividing by \(W/H\) gives
\(O(H\log m/m)=o(1)\).  For reference, in the first range the exact
ratio before taking the maximum is

\[
 \frac{4jR_m}{W/H}
 =\frac{2Hj(m+1)}{(2m+1)(2m-1)}=O(Hj/m).
\]

This tends to zero under the displayed hypothesis. \(\square\)

### Theorem 4.5 (global adjacent-priority alternating-component charge)

Let \(M,M'\) be the two first-avoided token matchings before and after the
adjacent interchange at positions \(j,j+1\).  Their union outside common
edges decomposes into alternating even cycles and alternating paths whose
two endpoints lie on the middle side.  After privately dummy-closing the
paths, this is a common-base alternating-cycle cell.  Switching all its
components gives \(M'\), and

\[
 \boxed{[J(M')-J(M)]_+
 \le\min\{4jR_m,\,2|\mathcal D_j|\}.}
\tag{4.10}
\]

#### Proof

Both matchings saturate the lower side, and both have middle degree at most
one.  Hence every nontrivial component of their two-coloured union is an
alternating cycle or a path with endpoints on the middle side.  Private
dummy closure is as in Section 3.

By Lemma 4.1, the source-position XOR carrier lies only in \(F_A,F_B\).
Lemma 4.2 bounds it by \(2jR_m\) intervals in each factor, while the total
number of toggled positions is \(2|\mathcal D_j|\).  Take the smaller
bound and apply Lemma 1.1 row by row. \(\square\)

Theorem 4.5 deliberately switches the whole adjacent-priority difference.
Choosing its alternating components independently can fragment a carrier
interval if component labels interlace along that interval; no such
independence is needed for the priority-refresh operation.

## 5. A logarithmic permutation atlas

Restrict attention to the first \(t\) priority pairs.  Any permutation of
them is obtainable by at most \(t(t-1)/2\) adjacent interchanges, all at
positions at most \(t\).  The sum of the charges (4.10) is therefore less
than

\[
 4R_m\,t\,{t(t-1)\over2}<2R_mt^3.
\tag{5.1}
\]

This proves (0.4).  The exact ratios

\[
 \frac{\binom{2m-1}{m-1}}W=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{R_m}{W}
 =\frac{m+1}{2(2m+1)(2m-1)}
\tag{5.2}

give

\[
 \frac{2R_mt^3}{W/H}
 =\frac{Ht^3(m+1)}{(2m+1)(2m-1)}.
\tag{5.3}

Thus (0.5)--(0.6) follow without suppressing a floor or a divisibility
term.

If \(K_m\) logarithmic priority-refresh atlases are used along an iterative
descent, their total carrier charge is at most

\[
 2K_mR_mt^3.
\tag{5.4}

Consequently

\[
 K_mHt^3/m\longrightarrow0
\tag{5.5}

is sufficient for total added row-run boundary \(o(W/H)\).  Between these
refreshes, any number of run-orientation contractions is free by (3.10).

There is also a stronger endpoint statement which does not charge repeated
global refreshes at all.

### Theorem 5.1 (uniform low-run bound over every priority order)

There is an absolute constant \(C_0\) such that, for every ordering
\(\prec\) of the \(m\) disjoint pairs and every integer \(1\le u\le m\),
the corresponding first-avoided matching satisfies

\[
 \boxed{
 J(M_\prec)\le
 R_m u(u+1)+4C_0\sqrt m\binom{2m-1}{m-1}(3/4)^u.}
\tag{5.6}
\]

In particular, with \(u=\lceil20\log m\rceil\),

\[
 \sup_\prec J(M_\prec)
 =O\!\left(\frac{W\log ^2m}{m}\right)=o(W/H)
\tag{5.7}
\]

uniformly for \(H=o(m/\log ^2m)\).  Therefore an arbitrarily long sequence
of *completed global* adjacent-priority refreshes has row-run count
\(o(W/H)\) at every endpoint, independently of the number of refreshes.

#### Proof

The component argument in the source Section 5 is independent of the names
and order of the disjoint pairs.  If \(N_j^\prec\) is the number of lower
sets having category \(j\), it gives

\[
 J_j\le\min\{N_j^\prec,2jR_m\},
\qquad
 N_j^\prec\le C_0\sqrt m\binom{2m-1}{m-1}(3/4)^{j-1}.
\tag{5.8}
\]

Sum the first bound for \(j\le u\).  Sum the geometric second bound for
\(j>u\).  This gives

\[
 \sum_{j\le u}2jR_m+
 C_0\sqrt m\binom{2m-1}{m-1}
 \sum_{j>u}(3/4)^{j-1},
\]

which is exactly (5.6).  Equations (5.2) and
\((3/4)^{20\log m}=m^{20\log(3/4)}=O(m^{-5})\) imply (5.7).
\(\square\)

The distinction is useful.  Formula (5.4) controls the sum of carrier
charges during an explicit adjacent-swap compilation.  Formula (5.7)
controls the actual physical run count at every completed priority
matching, even if the priority walk revisits orders.  For contraction
inside one independently switchable run atlas, Corollary 4.4 controls all
intermediate corners as well.

## 6. Proved boundary and remaining quantitative input

The following are unconditional.

1. The predecessor/successor run cube is a genuine common-base integral
   matching atlas with exactly constant row-run count.
2. Its complete two-parent innovations are the explicit endpoint-strip
   vectors (3.4), so its joined-owner Gram is a signed target-collision
   count rather than an unspecified variance.
3. One adjacent-priority refresh at position \(j\) has carrier charge at
   most \(4j\operatorname{Cat}_{m-1}\).
4. A full permutation atlas on the first \(\lceil20\log m\rceil\) pairs has
   cumulative charge \(O(W\log ^3m/m)=o(W/H)\) on every fixed Gaussian
   window.
5. Every completed first-avoided priority matching, under any ordering, has
   \(O(W\log ^2m/m)=o(W/H)\) runs; this remains true along arbitrarily many
   global priority refreshes.
6. Any defect contraction satisfying (3.8) inside the run cube iterates to
   \(o(W)\) with **zero** additional boundary cost.

What is not asserted here is that the endpoint-strip Gram in (3.4) spans
every multidepth defect direction.  That is a separate numerical inequality.
The present theorem proves that, if it does, no boundary term is lost under
iteration.  If a priority refresh is needed to expose new directions, the
exact allowable refresh count is (5.5).
