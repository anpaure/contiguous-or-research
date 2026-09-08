# AB14: owner-fixed signed spikes and the exact global charged frame

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver,
web search, or long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom{2m+1}{m},
 \qquad
 T=\binom{2m+1}{m-1}=\frac{m}{m+2}W.
\]

This note audits
`PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_20260725.md`, including its lower
dual, and combines it with the simultaneously legal odd/even interval
layers.

The local owner-fixed calculation is correct.  If a token occurrence
\(e=(S,Y)\) is replaced by a conjugate row which fixes \(S\) and \(Y\)
setwise, then the central edge is literally unchanged.  A common upper or
lower spike of size \(t\) at depth \(q\ge2\) has

\[
 \boxed{\mathfrak A-\mathfrak V\ge w_q^\pm t(t-1).}
\tag{0.1}
\]

Thus its Haar credit is \((\mathfrak A-\mathfrak V)/4\) for squared norm,
equivalently for the doubled factorial-floor polynomial, and one half of
that for the ordinary collision polynomial \(\sum\binom\mu2\).  The
credit is below the average, or the larger, of the two coherent endpoints;
it is not automatically a descent from the prescribed old endpoint.

There are four audit corrections or scope restrictions.

1. Different occurrence-dependent conjugate rows generally belong to
   different labelled exact factors.  After a corner is chosen, its runs
   give a direct literal word.  It need not be one corner inside a single
   frozen local factor.
2. In a fixed one-factor-per-omitted-pair atlas, every repeated upper
   partner pair must use one globally fixed bijection.  The Gram bound is
   independent of that choice.
3. The lower dual has the exact range \(2\le q\le H\le m-2\) here; it
   requires a nonempty lower target from which to choose a surviving
   coordinate.
4. The upper theorem actually extends to \(q=1\) if the second exchanged
   coordinate is chosen outside the depth-\(H\) upper flag.  The report's
   assertion that owner-fixed upper spikes start exactly at depth two is
   therefore stronger than necessary.  The signed frame below is stated
   on \(2\le q\le H\), as requested.

The main new theorem is global and two-sided.  Fix any union of selected
token occurrences.  There is one coordinate \(a\) and one literal cube,
fixing every central edge pointwise, whose joined Gram satisfies

\[
 \boxed{
 \mathfrak A_a-\mathfrak V_a
 \ge
 2\frac{m-H}{2m+1}
 \sum_{q=2}^H
 \left(w_q^+C_q^+ + w_q^-C_q^-\right).}
\tag{0.2}
\]

Here \(C_q^\pm\) is the collision-pair census carried by the selected
tokens at signed depth \(q\).  The cube adds at most two source-row runs
per distinct selected token.  It is one all-depth cube, not a sum of
separate targetwise spike charts.

The construction is elementary.  For an upper token, use the first upper
entrant and switch only when the old target omits \(a\).  Every nonzero
old upper flag then omits \(a\), while its image contains \(a\).  For a
lower token, use the first deleted coordinate and switch only when the old
target contains \(a\).  Every nonzero old lower flag contains \(a\), while
its image omits \(a\).  All mixed old/image equalities are therefore
impossible, at every depth and across arbitrary source phases.  The two
signed sectors are orthogonal.

This yields a sharp heavy/light frame.  Let \(\Phi_w^\pm\) be the ordinary
factorial-floor excess of the token flags.  If \(K\) is a load threshold,
let \(C_K^\pm\) be the weighted collision census on targets of load at
least \(K\).  For \(H\le A\sqrt m\), put

\[
 C_A=\left\lceil e^{2(A+1)^2}\right\rceil,
 \qquad
 K=C_A+2+\lceil H\omega_m\rceil,
 \qquad \omega_m\longrightarrow\infty.
\tag{0.3}
\]

If the reciprocal floor weights are bounded below by \(w_*>0\) and
\(\Phi_w^++\Phi_w^-=O_A(W)\), then every heavy occurrence in every signed
depth can be placed in the one global marker cube with

\[
 \boxed{\Delta J=o(W/H).}
\tag{0.4}
\]

Let \(V\) be the complete upper collision census visible to the adjacent
priority layers, and let \(D_{\rm int}\ge V/2\) be the exact current-relative
descent of the better legal parity.  Let \(R_K^+\) be the floor-subtracted
upper interval-invisible census on targets of load below \(K\), and let
\(R_K^-\) be the complete floor-subtracted lower census on targets of load
below \(K\).  With

\[
 \lambda=\frac{m-H}{2m+1},
\]

the interval layer and the single signed heavy cube obey the exact frame
inequality

\[
 \boxed{
 D_{\rm int}+G_{\rm heavy}
 \ge
 \frac{\lambda}{2}
 \left(
  \Phi_w^+ + \Phi_w^-
  -R_K^+-R_K^-
 \right).}
\tag{0.5}
\]

The heavy credit \(G_{\rm heavy}\) is still relative to the larger coherent
endpoint.  Consequently (0.5) is a genuine integral, low-run frame theorem,
but not a current-relative contraction theorem.

Two further quantitative results locate the residual.

* A \(K_0\)-packet upper atlas, using \(K_0\) separated tail labels in
  every first-phase row, charges the exact fraction
  \((K_0q/(2m-1))^2\) of the depth-\(q\) collision census in expectation,
  with at most \(2K_0\operatorname{Cat}_{m-1}\) added runs.  At
  \(H=\Theta(\sqrt m)\), it reaches the required \(1/m\) charge with
  \(o(W/H)\) runs for every growing \(q\), but its certified accounting is
  critical, not little-oh, at fixed \(q\).
* Any aligned pointwise-central lower row block changes at most \(q-1\)
  depth-\(q\) flags.  If \(\Delta_q\) is the exact transport distance to
  the balanced floor and
  \(R_q=\max f_q-\min f_q-1\), then every adaptive sequence of \(B\)
  such blocks satisfies
  \[
   \boxed{
   B\ge\frac{\Delta_q}{q-1}
    \ge\frac{\Phi_q}{R_q(q-1)}.}
  \tag{0.6}
  \]

Finally, the current endpoint obstruction is exact.  At one signed rank,
if \(s_U\) selected old occurrences leave target \(U\), if their images
have multiplicities \(r_V\), and if \(f\) is the current load profile,
then fair bits give

\[
 \boxed{
 \begin{aligned}
 \mathbb E(\Phi_{\rm new}-\Phi_{\rm old})
 ={}&-\frac34\sum_U\binom{s_U}{2}
     -\frac12\sum_Us_U(f_U-s_U)\\
 &+\frac12\sum_Vr_Vf_V
     +\frac14\sum_V\binom{r_V}{2}.
 \end{aligned}}
\tag{0.7}
\]

The image-load term \(\sum_Vr_Vf_V\) is not bounded by positive Gram.
The exact surviving gates are therefore:

1. control the floor-subtracted light upper-invisible and lower residuals;
2. prove a current image-routing inequality which makes (0.7) negative;
3. control the choice-dependent completion collars when passing from the
   principal token ledger to the final literal \(W\)-owner word.

No constant-one conclusion is claimed.

## 1. Audit of the upper owner-fixed spike

Fix one token occurrence in a source row of an exact factor \(F_A\) on
\([n]\setminus A\):

\[
 e=(S,Y),\qquad S\subset Y,\qquad |S|=m-1,\qquad |Y|=m.
\]

Suppose its depth-\(q\) upper target is \(U\), and put

\[
 D=U\setminus Y,qquad |D|=q.
\]

For \(q\ge2\), choose a two-set \(B\subset D\), and let \(\theta\)
exchange the two coordinates of \(A\) with those of \(B\).  Since both
\(A\) and \(B\) avoid \(Y\),

\[
 \theta S=S,qquad \theta Y=Y.
\tag{1.1}
\]

Thus the row at the corresponding start in \(\theta F_A\) supplies the
same central edge.  Every lower flag is a subset of \(S\), hence is fixed.

Let \(U_p^{(i)}\) denote the old upper target of occurrence \(i\), and put

\[
 (d_i)_p^+=
 \delta_{\theta_iU_p^{(i)}}-\delta_{U_p^{(i)}}.
\]

All old targets avoid \(A\).  Whenever this column is nonzero, its image
meets \(A\).  Hence for two distinct occurrences the two negative cross
equalities are impossible.  Therefore

\[
 \left\langle(d_i)_p^+,(d_k)_p^+\right\rangle
 =
 \mathbf1_{\{U_p^{(i)}=U_p^{(k)}\}}
 +
 \mathbf1_{\{\theta_iU_p^{(i)}=\theta_kU_p^{(k)}\}}
 \ge0.
\tag{1.2}
\]

At the common depth \(q\), the first indicator is one.  Thus a spike of
size \(t\) gives

\[
 \mathfrak A-\mathfrak V
 =2\sum_{i<k}\langle d_i,d_k\rangle_w
 \ge w_q^+t(t-1).
\tag{1.3}
\]

This proof does not require the partner pairs \(B_i\) to be disjoint.
They may overlap or coincide.

### 1.1 Upper depth one also has an owner-fixed chart

The condition \(B\subset D\) is sufficient, not necessary.  Assume
\(1\le q\le H\le m-2\).  Choose

\[
 b\in U_q\setminus Y,
 \qquad
 z\in([n]\setminus A)\setminus U_H.
\]

The second choice exists because

\[
 |([n]\setminus A)\setminus U_H|=m-1-H\ge1.
\]

Exchange \(A\) with \(\{b,z\}\), pairing \(b\) with one fixed coordinate
of \(A\).  Both \(b,z\) avoid \(Y\), so the central edge is fixed.  The
coordinate \(z\) lies in no upper flag through depth \(H\).  From the
depth at which \(b\) enters onward, every nonzero image meets \(A\), and
the proof of (1.2)--(1.3) is unchanged.  This works at \(q=1\).

It does not contradict the exact depth-one flatness of the adjacent
common-pair interval charts.  It uses an occurrence-dependent second
coordinate outside the entire shallow upper chain and pays singleton
source-row fragmentation unless further packetized.

### 1.2 Exact source-label scope

For a fixed two-set \(B\), choose one bijection \(A\to B\) and install
the factor \(F_B=\theta_BF_A\).  Then every occurrence using this \(B\)
lies in one fixed exact factor.  If different occurrences use different
orientations for the same \(B\), they must instead be retained as labelled
copies in the direct literal construction.

The latter is still integral.  After a corner is chosen, split the selected
tokens into maximal consecutive runs inside their labelled exact rows and
emit the standard two-sided context for each run.  No abstract fractional
flag is used.

## 2. Audit of the lower dual

For \(2\le q\le H\), suppose \(t\) selected tokens have common lower
target

\[
 L_q(e_i)=L.
\]

Let

\[
 \{b_i\}=L_{q-1}(e_i)\setminus L,
 \qquad
 a_i\in L,
 \qquad
 \sigma_i=(a_i\ b_i).
\tag{2.1}
\]

Both coordinates lie in \(S_i\).  Therefore \(\sigma_i\) fixes
\(S_i\), \(Y_i\), the omitted source pair, and every upper flag setwise.
For the lower chain,

\[
 \sigma_iL_p(e_i)=
 \begin{cases}
 L_p(e_i),&p<q,\\
 (L-\{a_i\})\cup\{b_i\},&p=q,\\
 L_p(e_i),&p>q, a_i\notin L_p(e_i),\\
 (L_p(e_i)-\{a_i\})\cup\{b_i\},
       &p>q, a_i\in L_p(e_i).
 \end{cases}
\tag{2.2}
\]

For \(p\ge q\), every old nonzero target is contained in the common set
\(L\), while every image contains \(b_i\notin L\).  Thus the negative
cross equalities vanish and

\[
 \left\langle(d_i^-)_p,(d_k^-)_p\right\rangle\ge0.
\]

At depth \(q\), the old-old equality contributes one.  Hence

\[
 \boxed{
 \left\|\sum_i d_i^-\right\|_w^2
 -\sum_i\|d_i^-\|_w^2
 \ge w_q^-t(t-1).}
\tag{2.3}
\]

In general the rows \(\sigma_iF_A\) do not all lie in one frozen copy of
\(F_A\).  Equation (2.3) is an exact labelled-row, post-selected literal
construction.

### 2.1 Upper and lower bits on one central edge

An upper owner-fixed transposition has support outside \(Y_i\) (together
with coordinates of the omitted pair), while a lower transposition has
support inside \(S_i\subset Y_i\).  Their supports are disjoint, they
commute, and

\[
 L_p(\theta_i^\alpha\sigma_i^\beta e_i)
 =\sigma_i^\beta L_p(e_i),
 \qquad
 U_p(\theta_i^\alpha\sigma_i^\beta e_i)
 =\theta_i^\alpha U_p(e_i).
\tag{2.4}
\]

Thus the four source rows

\[
 F_A,\qquad \theta_iF_A,\qquad \sigma_iF_A,\qquad
 \theta_i\sigma_iF_A
\]

all supply the same central edge.  The signed innovations are orthogonal.
After choosing one of the four states, a switched token still costs at most
two added source-row runs, not four.

## 3. Exact Haar and run constants

For either sign, let

\[
 f^1=f^0+\sum_i d_i.
\]

A fair independent corner has

\[
 f^\varepsilon
 =\frac{f^0+f^1}{2}
 +\frac12\sum_i\varepsilon_i d_i.
\]

Therefore

\[
 \frac{\|f^0\|_w^2+\|f^1\|_w^2}{2}
 -\mathbb E\|f^\varepsilon\|_w^2
 =\frac14(\mathfrak A-\mathfrak V).
\tag{3.1}
\]

All corners have the same mass at every signed rank, so the linear and
integer-floor terms cancel.  Equation (3.1) is exact for the squared norm
and the doubled factorial-floor polynomial.  For
\(\Phi=\sum_R\binom{\mu_R}{2}\), it is divided by two.

Switching one token can split its old selected run once and create one new
run in its conjugate source row.  Thus, for \(t\) switched tokens,

\[
 \boxed{
 \Delta J\le2t,
 \qquad
 \partial_{\rm new}\le4t.}
\tag{3.2}
\]

These are safe upper bounds; adjacent tokens with the same source label
may merge and cost less.

Crucially, (3.1) only implies

\[
 \min_\varepsilon E(f^\varepsilon)
 \le
 \frac{E(f^0)+E(f^1)}2
 -\frac14(\mathfrak A-\mathfrak V).
\tag{3.3}
\]

Without equality or a bound between the coherent endpoint energies,
(3.3) need not improve \(f^0\).

## 4. Global signed fixed-marker theorem

We now remove the targetwise and phasewise product obstruction.

Let \(\mathcal T^+\) and \(\mathcal T^-\) be arbitrary selected token
unions.  For a token \(e\), let

\[
 \{b_e\}=U_1(e)\setminus Y_e,
 \qquad
 \{c_e\}=L_1(e)\setminus L_2(e).
\tag{4.1}
\]

The first coordinate \(b_e\) remains in every upper flag.  The first
deleted coordinate \(c_e\) is absent from every lower flag of depth at
least two.

Fix one global coordinate \(a\).  Define two disjoint token classes:

\[
 \mathcal U_a=\{e\in\mathcal T^+:a\notin Y_e\},
 \qquad
 \mathcal L_a=\{e\in\mathcal T^-:a\in S_e\}.
\tag{4.2}
\]

They are disjoint on an overlapping token because \(S_e\subset Y_e\).
On \(\mathcal U_a\), use \((a\ b_e)\).  On \(\mathcal L_a\), use
\((a\ c_e)\).  Identity transpositions are simply omitted.

### Theorem 4.1 (one global all-depth signed cube)

Every corner preserves the complete central matching.  All same-sign
cross-Gram entries are nonnegative across arbitrary source phases, targets,
and depths, and the two signs are orthogonal.  More precisely, if

\[
 C_q^+(a)=
 \sum_{U:a\notin U}
 \binom{\mu_{\mathcal T^+,q}^+(U)}2,
\]

\[
 C_q^-(a)=
 \sum_{L:a\in L}
 \binom{\mu_{\mathcal T^-,q}^-(L)}2,
\]

then

\[
 \boxed{
 \mathfrak A_a-\mathfrak V_a
 \ge
 2\sum_{q=2}^H
 \left(w_q^+C_q^+(a)+w_q^-C_q^-(a)\right).}
\tag{4.3}
\]

Moreover

\[
 \sum_{a\in[n]}C_q^+(a)
 =(m+1-q)C_q^+,
 \qquad
 \sum_{a\in[n]}C_q^-(a)
 =(m-q)C_q^-.
\tag{4.4}
\]

Consequently some \(a\) satisfies

\[
 \boxed{
 \mathfrak A_a-\mathfrak V_a
 \ge
 2\frac{m-H}{2m+1}
 \sum_{q=2}^H
 \left(w_q^+C_q^+ + w_q^-C_q^-\right).}
\tag{4.5}
\]

The run increase is at most

\[
 \boxed{\Delta J\le2|\mathcal T^+\cup\mathcal T^-|.}
\tag{4.6}
\]

#### Proof

For an upper token, \(b_e\) is in every \(U_p(e)\).  If
\(a\notin U_p(e)\), the transposition replaces \(b_e\) by \(a\); the old
target omits \(a\) and the image contains it.  Once \(a\) enters the nested
upper chain, both \(a,b_e\) are present and the target is fixed.  Hence
every nonzero old upper coordinate omits \(a\), while every image contains
\(a\).

For a lower token, \(c_e\notin L_p(e)\) for every \(p\ge2\).  If
\(a\in L_p(e)\), the image replaces \(a\) by \(c_e\); otherwise the
target is fixed.  Thus every nonzero old lower coordinate contains \(a\),
while every image omits it.

These marker separations kill both negative old/image equalities.  At a
common target satisfying the marker condition, the old-old equality
contributes one.  Expanding the coherent square gives (4.3).  A rank
\(m+q\) upper target omits exactly \(m+1-q\) coordinates, while a rank
\(m-q\) lower target contains exactly \(m-q\).  This proves (4.4), and
averaging proves (4.5).  Central fixity and (3.2) prove (4.6). \(\square\)

Theorem 4.1 is the decisive global legality upgrade.  The owner-fixed
spikes no longer need to be kept as separate targetwise menus, and no
all-depth signing or cross-phase Gram lemma remains unproved for the
selected token union.

## 5. Exact heavy-fiber capacity

Fix one signed depth and write

\[
 N=\binom{2m+1}{m\pm q},
 \qquad
 T=cN+\delta,
 \qquad 0\le\delta<N.
\]

The exact arithmetic collision floor is

\[
 p_{\min}=N\binom c2+c\delta.
\tag{5.1}
\]

For the load vector \(\mu\), put

\[
 \Phi=\sum_R\binom{\mu_R}{2}-p_{\min}.
\]

The following identity includes the hole terms exactly:

\[
 \boxed{
 \Phi=\sum_R\binom{\mu_R-c}{2},}
\tag{5.2}
\]

where \(\binom z2=z(z-1)/2\) for every integer \(z\).  Indeed, expanding
the right side and using \(\sum_R\mu_R=T\) gives (5.1).

For an integer \(K\ge c+2\), define

\[
 t_K=\sum_{\mu_R\ge K}\mu_R,
 \qquad
 C_K=\sum_{\mu_R\ge K}\binom{\mu_R}{2}.
\]

### Lemma 5.1 (sharp heavy occurrence bounds)

\[
 \boxed{
 t_K\le
 \frac{2K}{(K-c)(K-c-1)}\,\Phi,}
\tag{5.3}
\]

\[
 \boxed{
 C_K\le
 \frac{K(K-1)}{(K-c)(K-c-1)}\,\Phi.}
\tag{5.4}
\]

Both constants are pointwise sharp at load \(K\).

#### Proof

Write \(\mu=c+y\), where \(y\ge K-c\ge2\).  The ratios

\[
 \frac{c+y}{\binom y2},
 \qquad
 \frac{\binom{c+y}{2}}{\binom y2}
\]

decrease with \(y\ge2\).  Their values at \(y=K-c\) are exactly the
coefficients in (5.3)--(5.4).  Sum the pointwise inequalities and use
(5.2). \(\square\)

### 5.1 Uniform constants through \(A\sqrt m\)

For \(2\le q\le H\le A\sqrt m\), the token quotient satisfies

\[
 \frac{T}{N_q^+}
 =\prod_{r=2}^{q-1}\frac{m+r+1}{m+1-r},
 \qquad
 \frac{T}{N_q^-}
 =\prod_{r=2}^{q}\frac{m+r+1}{m+1-r}.
\tag{5.5}
\]

If \(m\ge4A^2\), then

\[
 \log\frac{T}{N_q^\pm}
 \le\sum_{r\le H}\frac{4r}{m}
 \le2(A+1)^2.
\]

Thus every integral floor parameter obeys

\[
 c_q^\pm\le
 C_A:=\left\lceil e^{2(A+1)^2}\right\rceil.
\tag{5.6}
\]

Assume every signed depth retained in the heavy union has
\(w_q^\pm\ge w_*>0\); zero-weight depths are omitted.  Summing (5.3)
over those heavy signed depths gives

\[
 \sum_{q,\pm}t_{q,K}
 \le
 \frac{2K}{w_*(K-C_A)(K-C_A-1)}
 \left(\Phi_w^++\Phi_w^-\right).
\tag{5.7}
\]

Let \(\mathcal T_K^\pm\) be the union of all occurrences belonging to a
load-at-least-\(K\) target at at least one depth.  A token occurring in
several heavy fibers is counted once in the union, so

\[
 |\mathcal T_K^+\cup\mathcal T_K^-|
 \le\sum_{q,\pm}t_{q,K}.
\]

Apply Theorem 4.1 to this union.  Its selected-run and endpoint costs obey

\[
 \boxed{
 \Delta J_{\rm heavy}
 \le
 \frac{4K}{w_*(K-C_A)(K-C_A-1)}
 \left(\Phi_w^++\Phi_w^-\right),}
\tag{5.8}
\]

\[
 \boxed{
 \partial_{\rm heavy}
 \le
 \frac{8K}{w_*(K-C_A)(K-C_A-1)}
 \left(\Phi_w^++\Phi_w^-\right).}
\tag{5.9}
\]

With \(K\) as in (0.3), \(K/H\to\infty\).  If the weighted floor excess
is \(O_A(W)\), (5.8)--(5.9) are \(o(W/H)\).  A threshold \(K=\Theta(H)\)
would give only \(O(W/H)\); the little-oh assertion genuinely needs a
super-\(H\) threshold unless a new packet compression is proved.

## 6. Exact interval--heavy frame identity

We use the common-base adjacent priority layers from
`MATH_ATTACK_PAIR_PRIORITY_LAYER_CHARGED_COVERAGE_FLOOR_RESIDUAL_20260725.md`.
Their simultaneous matching legality is exact for either index parity.

For completeness, the decisive owner check is short.  The changed lower
domains for distinct adjacent indices are disjoint.  Every candidate
middle owner in block \(j\) has first-avoided category \(j\) or \(j+1\).
Hence the candidate-owner strata of two indices of the same parity are
disjoint.  A candidate owner cannot meet the genuinely unchanged
background because it coexists with that background in one of the two
coherent endpoints of its individual block.  These observations exhaust
all collision types.  Every nonzero upper innovation of block \(j\) is
likewise supported on target strata \(j,j+1\), while every lower innovation
is zero.  Thus same-parity blocks are both matching-compatible and exactly
orthogonal in the flag Gram.

At an upper target \(U\), let \(\mu_U\) be its load and let \(a_U\) be
the multiplicity genuinely movable by its unique adjacent priority block.
Define the complete visible census

\[
 V=\sum_{q=2}^Hw_q^+\sum_U\binom{a_U}{2}.
\tag{6.1}
\]

The better legal parity has exact current-relative doubled-floor descent

\[
 \boxed{D_{\rm int}\ge\frac12V.}
\tag{6.2}
\]

The parity cube uses

\[
 O\!\left(\frac{W\log^2m}{m}\right)=o(W/H)
\]

run variables for \(H=O(\sqrt m)\).

Split the interval-invisible upper collision pairs according to whether
their target load is at least \(K\):

\[
 I^+=I_{\ge K}^++I_{<K}^+.
\]

For the lower side, split the complete collision census as

\[
 C^-=C_{\ge K}^-+C_{<K}^-.
\]

After summing the exact arithmetic floors with the weights, define the
signed residuals

\[
 R_K^+=I_{<K}^+-P_{\min}^+,
 \qquad
 R_K^-=C_{<K}^--P_{\min}^-.
\tag{6.3}
\]

Then, exactly,

\[
 \Phi_w^+=V+I_{\ge K}^++R_K^+,
 \qquad
 \Phi_w^-=C_{\ge K}^-+R_K^-.
\tag{6.4}
\]

The heavy marker cube charges the full heavy target census, so

\[
 C_K^+\ge I_{\ge K}^+,
 \qquad
 C_K^-=C_{\ge K}^-.
\]

By Theorem 4.1, its coherent-endpoint doubled-floor Haar credit is at
least

\[
 G_{\rm heavy}
 \ge\frac{\lambda}{2}(C_K^++C_K^-),
 \qquad
 \lambda=\frac{m-H}{2m+1}.
\tag{6.5}
\]

Combining (6.2), (6.4), and (6.5) proves

\[
 \boxed{
 D_{\rm int}+G_{\rm heavy}
 \ge
 \frac{\lambda}{2}
 \left(
 \Phi_w^++\Phi_w^--R_K^+-R_K^-
 \right).}
\tag{6.6}
\]

In particular one of the two frame members has credit at least

\[
 \frac{\lambda}{4}
 \left(
 \Phi_w^++\Phi_w^--R_K^+-R_K^-
 \right).
\tag{6.7}
\]

The residuals in (6.3) are signed because the arithmetic floor may exceed
the raw light census.  Replacing each by its positive part gives a weaker
but manifestly nonnegative obstruction statement.

Equation (6.6) is the sought global charged frame for the interval and
owner-fixed spike mechanisms.  It is not a contraction theorem: only
\(D_{\rm int}\) is known below the current coherent base.  The heavy term
is a larger-endpoint Haar credit.

### 6.1 Matching legality with the interval layer

A lower owner-fixed transposition is supported inside \(S\).  Every
adjacent upper interval transposition is supported outside its changed
lower root and fixes all lower flags.  The two operations commute, and the
lower transposition fixes either chosen upper-side owner because both
contain \(S\).  Thus lower owner-fixed bits tensor legally with a disjoint
parity interval cube, and their signed flag innovations are orthogonal.

For upper owner-fixed bits, the safest exact composition is to puncture
their selected heavy tokens out of the interval carriers.  The puncture
cost is \(O(|\mathcal T_K^+|)=o(W/H)\) by (5.7).  Alternatively, retain
the interval and heavy cubes as the two separate frame members in (6.6).
No simultaneous upper cross-Gram claim is needed for (6.6).

## 7. Diffuse upper packet theorem

The heavy theorem leaves targets below \(K\).  The following exact packet
construction handles all collision pairs in the full first phase at a
growing depth with the correct \(1/m\) density.

Fix the first omitted pair \(A=\{a_1,a_2\}\), and let \(F_A\) be the
exact factor on the cyclic ground of size

\[
 L=2m-1.
\]

For a row \(\pi\) and coordinate \(b\) in that row, put

\[
 I_H(\pi,b)=\{i:b\in U_H(i)\setminus Y_i\}.
\]

This is one cyclic interval of exactly \(H\) starts.  On it, the
transposition \((a_1\ b)\) fixes every central edge and every lower flag.

Choose in every row a set \(B_\pi\) of \(K_0\) cyclic positions whose
successive gaps are at least \(H\).  Such a set exists whenever

\[
 K_0H\le L.
\tag{7.1}
\]

The intervals \(I_H(\pi,b)\), \(b\in B_\pi\), are disjoint.  Give each
one an independent old/conjugate bit.

### Theorem 7.1 (separated-label packet coverage)

Let

\[
 C_q=\sum_U\binom{\mu_q(U)}2
\]

be the collision census among the full-start tokens of this phase.  There
is a deterministic choice of the separated label sets for which

\[
 \boxed{
 \mathfrak A-\mathfrak V
 \ge
 2\sum_{q=1}^H
 w_q^+
 \left(\frac{K_0q}{2m-1}\right)^2C_q.}
\tag{7.2}
\]

The cube has \(K_0\operatorname{Cat}_{m-1}\) block bits and

\[
 \boxed{
 \Delta J\le2K_0\operatorname{Cat}_{m-1}.}
\tag{7.3}
\]

#### Proof

Sample \(B_\pi\) independently in each row by a uniform cyclic rotation
of one fixed \(H\)-separated pattern.  Every coordinate has marginal
probability \(K_0/L\).  A depth-\(q\) upper tail is a cyclic interval of
\(q\le H\) coordinates and contains at most one selected label, so one
occurrence is active with exact probability \(K_0q/L\).

Two occurrences of the same depth-\(q\) target lie in different physical
rows, because \(m+q<2m-1\).  Their label choices are independent.  Thus
the pair is activated with probability \((K_0q/L)^2\).  Every active pair
has cross inner product at least one: old targets avoid \(A\), while every
image meets \(A\).  Expectation and deterministic averaging prove (7.2).
The disjoint carrier intervals and the two-run bound prove (7.3).
\(\square\)

The deterministic conclusion concerns the one preassigned weighted sum in
(7.2).  It does not assert targetwise simultaneous discrepancy control.

Using

\[
 \frac{\operatorname{Cat}_{m-1}}W
 =\frac{m+1}{2(2m-1)(2m+1)},
\tag{7.4}
\]

we obtain

\[
 \frac{2K_0\operatorname{Cat}_{m-1}}{W/H}
 =\frac{K_0H(m+1)}{(2m-1)(2m+1)}.
\tag{7.5}
\]

If \(H=\gamma\sqrt m+O(1)\), \(q=q(m)\to\infty\), and

\[
 K_0=\left\lceil\frac{\kappa\sqrt m}{q}\right\rceil,
\]

then (7.1) holds eventually,

\[
 \left(\frac{K_0q}{2m-1}\right)^2
 \ge\left(\frac{\kappa^2}{4}+o(1)\right)\frac1m,
\tag{7.6}
\]

and the ratio in (7.5) is at most

\[
 \frac{\kappa\gamma}{4q}+O(m^{-1/2})=o(1).
\tag{7.7}
\]

Thus this architecture reaches the contraction-scale \(1/m\) charge with
little-oh endpoints at every growing depth.  For fixed \(q\), its certified
worst-case accounting is only critical \(\Theta(W/H)\), not little-oh.
This is a limitation of the proved packet accounting, not a universal
lower bound on every favorable signing.

The endpoint-asymmetry in (3.3) remains present in Theorem 7.1.

## 8. Lower packet rigidity and floor transport

For consecutive central roots in one cyclic source row,

\[
 \boxed{
 L_q(i)=\bigcap_{h=0}^{q-1}S_{i+h}.}
\tag{8.1}
\]

Indeed the intersection is precisely the length-\((m-q)\) interval from
position \(i+q-1\) to the common right endpoint \(i+m-2\).

Suppose an alternate labelled row agrees with every central incidence on
one aligned block \([u,v]\).  Then its roots \(S_i\) agree there.  By
(8.1), every lower flag with

\[
 u\le i\le v-q+1
\]

is forced.  Hence one aligned pointwise-central alternate block changes at
most the final \(q-1\) depth-\(q\) occurrences.  This holds for an
arbitrary alternate exact row, not only a transposition row.

The assertion is adaptive.  If rows are recomputed after every step, each
new aligned block still moves at most \(q-1\) current occurrences.  Thus a
sequence of \(B\) blocks moves at most \((q-1)B\) flag units.

Let \(f\) be the current integral depth-\(q\) load profile and let

\[
 \Delta_q(f)=\frac12\min_{g\text{ at the exact balanced floor}}\|f-g\|_1.
\tag{8.2}
\]

Every exact floor repair must move at least \(\Delta_q(f)\) occurrences,
so

\[
 B\ge\frac{\Delta_q(f)}{q-1}.
\tag{8.3}
\]

Let \(\Phi_q\) be the ordinary factorial-floor excess and put

\[
 R_q=\max f-\min f-1.
\]

If \(\Phi_q>0\), a Robin-Hood transfer decreases the collision energy by
an integer in \([1,R_q]\).  A shortest transfer path uses exactly
\(\Delta_q(f)\) moves.  Therefore

\[
 \frac{\Phi_q}{R_q}\le\Delta_q(f)\le\Phi_q.
\tag{8.4}
\]

Equations (8.3)--(8.4) prove (0.6).  In particular, if
\(q\le H\), \(\Phi_q=\Omega(W)\), and the load spread is bounded, an
\(o(W/H)\) aligned pointwise-central lower atlas cannot reach the floor.
Occurrence-dependent singleton spikes evade (8.1) only by paying their
linear fragmentation; a cross-row or reordered braid is a genuinely new
operation.

At depth two, (8.1) says that one block changes at most one lower flag.
Thus a low-run depth-two correction already requires the exact support or
transport estimate which is absent from the present theory.

## 9. Exact current endpoint law

We now audit the missing energetic implication directly.

At one signed rank, let \(f\) be the current load.  Suppose the marker
cube selects \(s_U\) old occurrences at target \(U\), and let \(r_V\) be
the number whose image is \(V\).  Marker separation makes the selected old
target set disjoint from the image target set.

For ordinary collision energy \(\Phi=\sum\binom f2\), fair independent
bits have the following four pair types.

1. A selected-selected old pair survives with probability \(1/4\), giving
   \(-3\binom{s_U}{2}/4\).
2. A selected-unselected old pair survives with probability \(1/2\),
   giving \(-s_U(f_U-s_U)/2\).
3. A moved occurrence meets each current image-target occurrence with
   probability \(1/2\), giving \(r_Vf_V/2\).
4. An image-image pair is present with probability \(1/4\), giving
   \(\binom{r_V}{2}/4\).

Summation proves (0.7).  Multiply by the rank weight and by two for the
doubled factorial-floor polynomial.

For a complete old spike of load \(t\), moving a subset of size \(s\) to
images with multiplicities \(r_V\) and old sink loads \(b_V\) changes the
ordinary coherent collision energy by

\[
 \boxed{
 -s(t-1)+\binom s2
 +\sum_Vb_Vr_V+\sum_V\binom{r_V}{2}.}
\tag{9.1}
\]

If every available image has current load at least \(t-1\), the quantity
in (9.1) is nonnegative for every nonempty subset.  Thus even arbitrarily
large positive joined Gram does not imply a descending current corner.
An image-routing or endpoint-orientation theorem is logically necessary.

For the marker cube, (0.7) makes that theorem exact:

\[
 3\sum_U\binom{s_U}{2}
 +2\sum_Us_U(f_U-s_U)
 >
 2\sum_Vr_Vf_V+\sum_V\binom{r_V}{2}
\tag{9.2}
\]

is sufficient and necessary for the fair expected corner to improve at
that rank.  No term in (9.2) is hidden in a floor error.

## 10. A sharp light residual witness

The residual in (6.3) cannot be bounded from scalar multiplicity and
collar data alone.

At upper depth \(q=2\), choose disjoint triples

\[
 A=\{a_1,a_2,a_3\},
 \qquad
 B=\{b_1,b_2,b_3\},
\]

and an omitted pair \(C\), all disjoint.  Put

\[
 Q=[n]\setminus(A\cup B\cup C),
 \qquad |Q|=2m-7.
\]

For every \(R\in\binom Q{m-4}\), define

\[
 S_R=R\cup A,
 \qquad
 S_R'=R\cup B,
 \qquad
 U_R=R\cup A\cup B,
\]

\[
 Y_R=S_R\cup\{b_1\},
 \qquad
 Y_R'=S_R'\cup\{a_1\}.
\tag{10.1}
\]

The lower roots and middle owners are all distinct.  Prescribe the local
cyclic segment

\[
 b_1, S_R, b_2, b_3
\]

for the first token and the symmetric segment

\[
 a_1, S_R', a_2, a_3
\]

for the second.  For each prescribed row separately, some labelled
coordinate image of an exact factor on \([n]\setminus C\) contains that
row.  No one factor is asserted to contain all of them.  Both tokens have
depth-two upper target \(U_R\).
Their missing three-sets are \(B\) and \(A\), hence are disjoint.  No
common partner pair can move both occurrences.

There are

\[
 s=\binom{2m-7}{m-4}=\Theta(W)
\tag{10.2}
\]

resource-disjoint load-two targets.  At upper depth two,

\[
 N_2^+=\binom n{m+2}=T,
 \qquad c_2^+=1,qquad p_{2,\min}^+=0.
\]

Complete the abstract mass-\(T\) histogram by assigning the remaining
\(T-2s\) occurrences to distinct singleton targets.  Then

\[
 \Phi_2^+=s=\Theta(W),
 \qquad
 V_2=0,
 \qquad
 C_{K,2}^+=0\quad(K\ge3).
\tag{10.3}
\]

This is a literal root/owner-simple partial token family plus a complete
integer load profile.  It is not proved extendable to one full low-run
exact factor; the displayed literal realization uses singleton row pieces.
Accordingly, (10.3) is a rigorous no-go to any scalar or purely local
collar proof of the missing light-residual inequality, not a counterexample
to a theorem exploiting global low-run factor correlations.

## 11. Final proved and conditional boundary

### Proved

1. The upper and lower owner-fixed spike Gram constants, including every
   factor \(2,1/4,1/8\).
2. Pointwise central-edge legality, with overlapping partner pairs allowed.
3. Direct literal labelled-row realization and the exact \(2t\)-run,
   \(4t\)-endpoint bounds.
4. The upper depth-one helper-coordinate extension.
5. The commuting upper/lower same-edge product.
6. The one-coordinate, all-depth, all-phase, two-sign global marker cube,
   independently audited in both signs.
7. The exact heavy occurrence inequalities (5.3)--(5.4), with sharp
   constants.
8. The \(o(W/H)\) heavy-union run bound at threshold \(K/H\to\infty\).
9. The exact interval--heavy charged frame inequality (6.6).
10. The separated-label diffuse upper theorem and its growing-depth
    \(1/m\)-scale corollary.
11. The adaptive lower packet rigidity and floor-transport bound.
12. The exact current endpoint formula (0.7) and sink obstruction (9.1).

### Still unproved

1. A bound
   \[
   (R_K^+)_++(R_K^-)_+
   =o(W)+O_A(H\operatorname{Cat}_m)
   \]
   for the useful low-run exact matching.
2. A current image-load inequality implying (9.2), or an adaptive
   potential which makes the endpoint rises telescope.
3. An \(o(W/H)\) packetization of fixed-depth diffuse lower spikes.
4. A fixed-depth diffuse upper theorem beyond the critical certified
   \(\Theta(W/H)\) separated-label accounting.
5. Control of completion-collar flag changes in the final \(W\)-owner
   literal word at the same exact energy scale.
6. Constant one.

The principal advance is that the heavy signed sector is now globally
framed in one integral same-central cube.  Cross-phase signing, lower-dual
existence, and owner packing are no longer the obstruction.  The exact
remaining obstruction is the light floor residual together with coherent
image influx.
