# Audit of the disjoint adjacent interval layer

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Verdict

The tensorization theorem in
`PAIR_OMISSION_DISJOINT_INTERVAL_LAYER_20260725.md` is correct.  It holds
for every set

\[
 \Lambda\subseteq\{1,\ldots,m-1\},
 \qquad |j-k|\ge2\quad(j\ne k\in\Lambda),
\tag{0.1}
\]

and hence for either full parity layer.  For each \(j\in\Lambda\), put

\[
 A_j=P_j,qquad B_j=P_{j+1},
\]

let \(\theta_j\) exchange \(A_j,B_j\) coordinatewise, and choose

\[
 F_{j+1}=\theta_jF_j.
\tag{0.2}
\]

Every independent choice on every maximal physical carrier interval in
every block is simultaneously a lower-saturating, middle-injective token
matching.  Cross-block owner collisions and cross-block flag Gram terms
both vanish for exact first-avoided-category reasons.

If \(r_j\) is the number of interval packets in block \(j\), and

\[
 r_\Lambda=\sum_{j\in\Lambda}r_j,
\]

then

\[
 \boxed{
 r_j\le\min\{2j\operatorname{Cat}_{m-1},|\mathcal D_j|\},
 \qquad
 J(M_\varepsilon)-J(M_0)\le2r_\Lambda,}
\tag{0.3}
\]

and

\[
 r_\Lambda=O(W\log^2m/m).
\tag{0.4}
\]

For doubled factorial floor energy and finite nonnegative signed-depth
weights, define

\[
 \mathcal C_j=
 \sum_{q=1}^H w_q^+
 \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
 \binom{\mu_{j,q,U}}2.
\tag{0.5}
\]

The tensorized descent is exact:

\[
 \boxed{
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M_0)-\sum_{j\in\Lambda}\mathcal C_j.}
\tag{0.6}
\]

Thus one integral layer corner satisfies

\[
 \boxed{
 \mathcal Q_w(M_\varepsilon)
 \le\mathcal Q_w(M_0)-\mathcal C_\Lambda,
 \qquad
 \partial_{\rm new}(M_\varepsilon)\le4r_\Lambda,}
\tag{0.7}
\]

where \(\mathcal C_\Lambda=\sum_{j\in\Lambda}\mathcal C_j\) and
\(\partial_{\rm new}\) counts new physical run-boundary edges.

There is one decisive strengthening exposed by the audit and now
incorporated into the candidate:

\[
 \boxed{\mathcal C_{j,1}=0\quad\text{for every }j.}
\tag{0.8}
\]

Indeed every interval corner, not merely its expectation, has exactly the
same first-upper factorial floor energy as the coherent base.  Therefore
one disjoint odd/even layer cannot contract the first-upper defect at all.
All positive descent in (0.6) comes from \(q\ge2\).

The strongest unconditional one-layer coverage statement is

\[
 \boxed{
 \max\{\mathcal C_{\rm odd},\mathcal C_{\rm even}\}
 \ge\frac12\mathcal C_{\rm all},
 \qquad
 \mathcal C_{\rm all}=\sum_{j=1}^{m-1}\mathcal C_j.}
\tag{0.9}
\]

This is coverage of the explicit adjacent-visible collision charge, not
of the complete floor energy.  A positive iterative contraction still
requires a lower bound comparing \(\mathcal C_{\rm all}\) with the
\(q\ge2\) excess, either a \(q=1\) near-rainbow theorem or a joined
overlap charge, and recentering control after the fixed atlas has been
used.  The stronger
same-base overlapping legality is proved in
`MATH_ATTACK_PAIR_PRIORITY_OVERLAPPING_LAYER_JOINED_GRAM_20260725.md`.

## 1. Lower carriers and compatible factor choices

The affected lower carrier for block \(j\) is

\[
 \mathcal D_j=\left\{S\in\binom{[n]}{m-1}:
 S\cap P_h\ne\varnothing\ (h<j),\quad
 S\cap(P_j\cup P_{j+1})=\varnothing\right\}.
\tag{1.1}
\]

If \(j<k\), a set in \(\mathcal D_j\) avoids \(P_j\), whereas a set in
\(\mathcal D_k\) meets \(P_j\).  Hence

\[
 \mathcal D_j\cap\mathcal D_k=\varnothing.
\tag{1.2}
\]

For \(S\in\mathcal D_j\), \(\theta_jS=S\), so its two candidate tokens
satisfy

\[
 e_{j+1}(S)=\theta_je_j(S).
\tag{1.3}
\]

Every affected lower target receives exactly one candidate, and every
other lower target retains its base token.  This proves simultaneous lower
saturation.

The conjugacy hypotheses are compatible.  Starting with one exact
\(F_1\), recursively define

\[
 F_{j+1}=\theta_jF_j\qquad(1\le j<m).
\tag{1.4}
\]

Every image is an exact factor on the required omitted-pair universe.
Thus one fixed factor family supports either parity layer, though the
theorem below uses only the relations belonging to the chosen disjoint
layer.

## 2. Complete middle-owner audit

Write \(Y_j(S)\) for the middle owner of \(e_j(S)\).  We check all three
possible collision types.

### 2.1 One block

Same-side owners are distinct by exactness of \(F_j\) or \(F_{j+1}\).
If

\[
 Y_j(S)=Y_{j+1}(T)=\theta_jY_j(T),
\tag{2.1}
\]

then the common owner avoids both \(P_j,P_{j+1}\), hence is fixed by
\(\theta_j\).  Therefore \(Y_j(S)=Y_j(T)\), and injectivity of the
predecessor-owner map in \(F_j\) gives \(S=T\).  A corner chooses only one
token over that lower target, so this is not a collision.

### 2.2 Two changed blocks

Let \(j<k\) lie in \(\Lambda\).  Every owner chosen over
\(S\in\mathcal D_j\) avoids at least one of \(P_j,P_{j+1}\).  Every lower
target \(T\in\mathcal D_k\) meets both pairs, because \(k\ge j+2\), and
every owner over \(T\) contains \(T\).  Thus a block-\(k\) owner meets
both pairs and cannot equal a block-\(j\) owner.

Equivalently, with \(\kappa\) denoting first avoided category, a block
\(j\) owner has

\[
 \kappa(Y)\in\{j,j+1\};
\tag{2.2}
\]

these category pairs are disjoint across \(\Lambda\).

### 2.3 The genuinely unchanged background

Here the background must mean lower targets outside
\(\bigcup_{j\in\Lambda}\mathcal D_j\); changed tokens from another block
were handled in Section 2.2.  An old phase-\(j\) candidate coexists with
this background in \(M_0\).  Its conjugate phase-\((j+1)\) candidate
coexists with the same background in the coherent matching obtained by
globally swapping positions \(j,j+1\), since that coherent swap changes
exactly \(\mathcal D_j\).  Both coherent states are matchings.  Hence no
candidate collides with the true background, whose own owners are mutually
distinct in \(M_0\).

These cases exhaust all pairs and certify simultaneous middle injectivity.

## 3. Physical packet and endpoint accounting

For one coordinate pair, the starts at which a length-\((m-1)\) cyclic
window avoids the pair form at most two circular intervals and have at
most four boundary edges.  Membership in \(\mathcal D_j\) is a Boolean
combination of \(j\) such predicates.  Its boundary lies in their boundary
union, so one row contains at most \(2j\) maximal carrier intervals.

One local factor has

\[
 R_m=\operatorname{Cat}_{m-1}
 =\frac1{2m-1}\binom{2m-1}{m-1}
\tag{3.1}
\]

rows, proving the first inequality in (0.3).

Changing one packet removes one all-one interval from an \(F_j\)-row and
inserts its conjugate all-zero interval in an \(F_{j+1}\)-row.  Each
operation can increase the cyclic run count by at most one.  Blocks in one
layer use disjoint factor pairs.  Hence

\[
 J(M_\varepsilon)-J(M_0)\le2r_\Lambda,
 \qquad
 \partial_{\rm new}(M_\varepsilon)\le4r_\Lambda.
\tag{3.2}
\]

Let

\[
 A_m=\binom{2m-1}{m-1}
\]

and let \(N_j\) be the number of category-\(j\) lower targets.  After
conditioning a uniform lower target to avoid \(P_j\), it is a uniform
\((m-1)\)-subset of the remaining \(2m-1\) points.  Its probability of
meeting one fixed earlier pair is

\[
 p_m=1-\frac{\binom{2m-3}{m-1}}{\binom{2m-1}{m-1}}
 =\frac{3m-2}{4m-2}<\frac34.
\tag{3.3a}
\]

For disjoint pairs, the meeting events are negatively correlated.  Here
is the elementary induction.  Condition on the number of selected points
in the union of the first \(s-1\) pairs.  The conditional probability of
meeting those \(s-1\) pairs is nondecreasing in that number, whereas the
conditional probability of meeting pair \(s\) is nonincreasing.  Their
conditional covariance is therefore nonpositive.  Removing the last
pair and iterating gives

\[
 \Pr(X\cap P_h\ne\varnothing\text{ for every }h<j)
 \le p_m^{j-1}.
\]

Consequently

\[
 |\mathcal D_j|\le N_j
 \le A_m(3/4)^{j-1}.
\tag{3.3b}
\]

Splitting the sum of
\(\min\{2jR_m,|\mathcal D_j|\}\) at
\(t=\lceil20\log m\rceil\) now gives, without a hidden constant,

\[
 r_\Lambda
 \le R_mt(t+1)+4A_m(3/4)^t
 =O(W\log^2m/m),
\]

because
\[
 \frac{A_m}{W}=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{R_m}{W}=\frac{m+1}{2(2m-1)(2m+1)}.
\]
This proves (0.4).

For completeness, the category-\(j\) carrier in the coherent base has at
most \(2j\) runs per \(F_j\)-row and at most \(N_j\) runs in total.  The
same split therefore proves

\[
 J(M_0)=O(W\log^2m/m),
\]

every layer corner obeys

\[
 2J(M_\varepsilon)\le2J(M_0)+4r_\Lambda
 =O(W\log^2m/m).
\tag{3.4}
\]

At \(H=\lceil L\sqrt m\rceil\), fixed \(L\), this total physical
run-endpoint count is \(o(W/H)\), and

\[
 HJ(M_\varepsilon)
 =O_L(W\log^2m/\sqrt m)=o(W).
\tag{3.5}
\]

## 4. Disjoint upper strata and additive Gram

Every lower innovation is zero.  Let \(U_{j,q}(S)\) be the old upper flag
of a changed token.  Its innovation is

\[
 d_{j,S,q}=\delta_{\theta_jU_{j,q}(S)}-\delta_{U_{j,q}(S)}.
\tag{4.1}
\]

If this vector is nonzero, then \(U_{j,q}(S)\) avoids \(P_j\), meets
\(P_{j+1}\), and meets every earlier pair.  Thus

\[
 \kappa(U_{j,q}(S))=j,
 \qquad
 \kappa(\theta_jU_{j,q}(S))=j+1.
\tag{4.2}
\]

Consequently

\[
 \operatorname{supp}d_{j,S,q}
 \subseteq\{U:\kappa(U)\in\{j,j+1\}\}.
\tag{4.3}
\]

The category pairs in (4.3) are disjoint for distinct
\(j\in\Lambda\).  Therefore all cross-block Gram products vanish exactly.

Within one block, the conjugate-pair unit-vector identity gives

\[
 \langle d_{j,S},d_{j,T}\rangle_w
 =2\sum_{q=1}^H w_q^+
 \mathbf1_{\{U_{j,q}(S)=U_{j,q}(T),\,
               U_{j,q}(S)\cap P_{j+1}\ne\varnothing\}}.
\tag{4.4}
\]

Distinct starts in one physical row have distinct proper upper windows for
\(q\le m-2\).  Packetization therefore loses no variance.  If \(z_{j,I}\)
is the innovation of packet \(I\), then

\[
 \left\|\sum_Iz_{j,I}\right\|_w^2
 -\sum_I\|z_{j,I}\|_w^2
 =4\mathcal C_j.
\tag{4.5}
\]

Summing (4.5) over \(\Lambda\) introduces no cross terms.

## 5. Exact factorial-floor tensorization

Tie all interval bits inside each block to one global block bit.  These
coherent corners are the first-avoided matchings obtained by disjoint
adjacent priority swaps.  At every upper depth, a global block flip merely
permutes the load on its disjoint category-pair stratum by \(\theta_j\).
Lower loads are unchanged, and middle loads remain zero-one.  Hence all
coherent corners have the same factorial floor energy, rank by rank.

The fair coherent-block ensemble and the fair independent-interval
ensemble have the same midpoint.  Their Haar variances differ by one
quarter of (4.5).  Every corner has the same rankwise total mass, so the
linear and exact adjacent-integer floor terms cancel.  This proves (0.6).

The proof uses arbitrary finite weights and never divides by a floor
quotient.  In particular it includes the autonomous first-upper token
floor

\[
 c_1^+=0,
 \qquad
 Q_1^+(x)=\sum_Ux_U(x_U-1).
\tag{5.1}
\]

## 6. The first-upper layer is pointwise flat

Fix one block \(j\), and suppose two distinct old token occurrences have
the same first-upper target \(U\).  If their lower endpoints are \(S,T\),
then the two collars

\[
 C_S=U\setminus S,
 \qquad C_T=U\setminus T
\tag{6.1}
\]

have size two.  For one occurrence, the two sets

\[
 U\setminus\{c\}\qquad(c\in C_S)
\]

are precisely its two adjacent rank-\(m\) windows.  If
\(C_S\cap C_T\ne\varnothing\), deleting a common collar point gives one
rank-\(m\) target among the two window starts attached to each token.
Exactness makes that window occurrence unique.  Therefore the two token
starts lie in the same row and differ by at most one.  If they differ by
one, however, their proper length-\((m+1)\) cyclic windows are distinct;
if they differ by zero, they are the same occurrence.  Consequently two
distinct occurrences of one \(U\) have disjoint collars.

If both \(S,T\in\mathcal D_j\) and \(U\cap P_{j+1}\ne\varnothing\), then
both lower endpoints avoid \(P_{j+1}\).  Hence

\[
 \varnothing\ne U\cap P_{j+1}\subseteq C_S\cap C_T,
\]

a contradiction.  Thus

\[
 \boxed{
 \mu_{j,1,U}\le1,
 \qquad
 \mathcal C_{j,1}=0.}
\tag{6.2}
\]

There is a stronger pointwise conclusion.  Nonfixed changed targets form
disjoint two-point orbits \(\{U,\theta_jU\}\), with exactly one moving
occurrence per orbit.  Let the complete base loads on one such orbit be
\((a,b)\).  The coherent endpoint identity

\[
 x+Z_j=\theta_jx
\]

and the innovation \((-1,+1)\) give \(a=b+1\).  An arbitrary tokenwise
choice merely exchanges

\[
 (b+1,b)\longleftrightarrow(b,b+1).
\tag{6.3}
\]

Every coordinate-separable factorial floor energy is invariant under this
exchange.  Because the orbits are disjoint, every simultaneous interval
corner in the whole layer has exactly the same \(q=1\) floor energy as
\(M_0\).

## 7. Charged coverage of one parity layer

Construct the recursively conjugate factors (1.4), so every adjacent
index has a valid individual charge \(\mathcal C_j\).  Odd and even
indices partition \(\{1,\ldots,m-1\}\); therefore (0.9) is exact.

There is also a literal multiplicity lower bound.  For \(q\ge2\), put

\[
 a_{j,q}=
 \sum_{U:\,U\cap P_{j+1}\ne\varnothing}\mu_{j,q,U},
 \qquad
 K_{j,q}=|\{U:\mu_{j,q,U}>0,\ U\cap P_{j+1}\ne\varnothing\}|.
\tag{7.1}
\]

If \(K_{j,q}>0\), Cauchy--Schwarz gives

\[
 \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
 \binom{\mu_{j,q,U}}2
 \ge\frac12\left(\frac{a_{j,q}^2}{K_{j,q}}-a_{j,q}\right).
\tag{7.2}
\]

Consequently one of the two legal parity layers satisfies

\[
 \boxed{
 \mathcal C_\Lambda
 \ge\frac14\sum_{j=1}^{m-1}\sum_{q=2}^H w_q^+
 \left(\frac{a_{j,q}^2}{K_{j,q}}-a_{j,q}\right),}
\tag{7.3}
\]

with zero terms understood when \(K_{j,q}=0\).

Let

\[
 r_{\rm all}=r_{\rm odd}+r_{\rm even}.
\]

Choosing the parity layer with the better charge-to-packet ratio gives

\[
 \boxed{
 \max_{\Lambda\in\{\mathrm{odd},\mathrm{even}\}}
 \frac{\mathcal C_\Lambda}{4r_\Lambda}
 \ge\frac{\mathcal C_{\rm all}}{4r_{\rm all}},}
\tag{7.4}
\]

omitting a zero-denominator layer.  This is the exact guaranteed descent
per new physical boundary edge.  Counting all run endpoints of the final
corner instead gives

\[
 \boxed{
 \frac{\mathcal Q_w(M_0)-\mathcal Q_w(M_\varepsilon)}
      {2J(M_\varepsilon)}
 \ge
 \frac{\mathcal C_\Lambda}
      {2J(M_0)+4r_\Lambda}.}
\tag{7.5}
\]

The denominator in (7.5) is \(O(W\log^2m/m)=o(W/H)\) for fixed Gaussian
\(H\).

## 8. Exact iterative boundary

The lower bound (7.3) concerns only visible changed-occurrence
collisions.  It gives no fixed positive fraction of the complete floor
energy.  Collisions are uncharged if their target avoids the designated
partner pair, if one lower endpoint already meets that pair, or if they
belong to the final category.  Most decisively, Section 6 shows that the
entire \(q=1\) energy is invariant.

The recursively chained factors in fact support all overlapping adjacent
blocks simultaneously at this same base; this stronger theorem is proved
in `MATH_ATTACK_PAIR_PRIORITY_OVERLAPPING_LAYER_JOINED_GRAM_20260725.md`.
It does not by itself renew a fresh atlas after the fixed cube has been
optimized.  Suppose the following two additional statements were proved at
every renewable coherent base:

\[
 \mathcal C_{\rm all}
 \ge\gamma_m\bigl(\mathcal Q_{\ge2}-R_m^*\bigr),
\tag{8.1}
\]

and a descended odd/even corner could be re-encoded as the next coherent
base without losing the descent or the run budget.  Then one parity layer
would give

\[
 \mathcal Q_{\ge2}'-R_m^*
 \le\left(1-\frac{\gamma_m}{2}\right)
       (\mathcal Q_{\ge2}-R_m^*).
\tag{8.2}
\]

After \(t\) renewable layers,

\[
 \mathcal Q_{\ge2}^{(t)}-R_m^*
 \le\left(1-\frac{\gamma_m}{2}\right)^t
       (\mathcal Q_{\ge2}^{(0)}-R_m^*).
\tag{8.3}
\]

If run boundaries accumulated at the worst one-layer rate, the physical
budget would still allow

\[
 t=o(\sqrt m/\log^2m)
\tag{8.4}
\]

for \(H=\Theta(\sqrt m)\).  Neither (8.1) nor the required renewability is
currently proved.  Moreover a separate theorem forcing
\(\mathcal Q_1=o(W)\) is unavoidable, since the layer circuit leaves
\(\mathcal Q_1\) unchanged at every step.

Thus the candidate tensorization is valid, but by itself it is a one-layer
contraction of only the explicitly charged \(q\ge2\) sector.  No
constant-one conclusion follows.

## 9. Patch record

The audited candidate has been patched in place as follows.

1. The multidepth range \(1\le H\le m-2\) is now explicit.
2. “Unchanged background” now excludes every changed carrier; collisions
   with another changed block are handled by Section 2.2.
3. The upper-support claim now explicitly uses the disjoint strata
   \(\{j,j+1\}\), so additivity is an exact orthogonality statement.
4. The depth-one collar proof now treats the possible adjacent-start case
   before invoking properness of the length-\((m+1)\) windows.
5. The total, rather than merely incremental, run-endpoint bound is stated.
6. Malformed display delimiters and the missing \(\le\) in (3.4) were
   corrected.

None of these changes alters the tensorization theorem.  Item 4 closes a
gap in the written proof of the stronger depth-one flatness assertion.
