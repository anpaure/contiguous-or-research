# Lane W: cyclic boundary moments for the survival-packet gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, random
experiment, solver, or long-running computation is used.  The exact-factor
and survival-packet definitions are the previously audited ones.  Every new
claim below is proved here.  The canonical private-component rectangle used
in Section 8 is explicitly identified as an imported audited lemma.

## 0. Verdict and exact boundary

Fix (A>0), and put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 t=\frac Wn=\operatorname {Cat}_m,\qquad
 K_A=\lceil A\sqrt m\rceil .
\tag{0.1}
\]

This report does **not** prove \((\mathrm{SPC}_A)\).  It also does not prove
that every exact factor has packet value larger than (O_A(t/m)).  The
unrestricted existential problem remains open.

The theorem-level advance is a new, literal cyclic obstruction.  For every
exact factor (F), every controlled depth (q), and every balanced quota,
the actual shorter cyclic distances of coordinate pairs in the rows of
(F) form a matrix (H_q(F)).  An exact identity gives

\[
 \sum_{|S|=m-q}(\mu_q^F(S)-c_q)\mathbf1_S\mathbf1_S^{\mathsf T}
 =a_qJ+b_qI+H_q(F).
\tag{0.2}
\]

Every positive-semidefinite negative mode of (b_qI+H_q(F)), orthogonal to
the all-ones vector, forces packet mass.  Precisely, if (Q\succeq0),
(Q\mathbf1=0), then for every balanced common multidepth quota system

\[
 \boxed{
 \vartheta(F,\beta)
 \ge
 \frac{[-\operatorname {Tr}Q(b_qI+H_q(F))]_+}
 {n(c_q+2)\max_{|S|=m-q}\mathbf1_S^{\mathsf T}Q\mathbf1_S}.}
\tag{0.3}
\]

This is uniform over the mobile high-quota positions and is proved by
turning an arbitrary fractional packet cover into one common fractional
quota-safe core.  It is not a histogram relaxation: (H_q(F)) is computed
from the physical cyclic rows, and its identity uses exact middle ownership.

The following consequences are proved.

1. A mesoscopic signed tail-distance mode on (s=O(q)) coordinates at
   (q\asymp\sqrt m) forces
   
   \[
   \vartheta(F,\beta)=\Omega_A(t/\sqrt m)=\omega(t/m),
   \]
   
   so every factor in that explicit class is excluded as a witness for
   \((\mathrm{SPC}_A)\).  The obstruction persists throughout a fixed
   positive-radius exact row-edit ball.
2. In every nonresonant Gaussian regime, a negative boundary-moment
   certificate must use (\Theta(q)) coordinates.  Constant-size local
   atoms and the projected (O(m^{-2})) star codegree cannot see it.
3. Exact middle ownership gives an entropy obstruction to such growing
   atoms: an (s)-coordinate, cyclic-placement-type-local architecture
   using only (\exp(o(s))) placement types occupies an exponentially
   negligible fraction of every exact factor.  At (s=\Theta(\sqrt m)), a
   positive-density architecture needs
   (\exp((\log2-o(1))s)) different placement types.
4. At depth one, the certificate becomes an exact boundary-matching Gram
   identity.  A perfectly balanced first shadow must make (tI+H_1)
   positive semidefinite on (\mathbf1^\perp).
5. For prime \(n\equiv1,11\pmod {12}\), the sharp equivariant
   collision-free Hall core cannot lift to literal \(n\)-cycles.  This is
   an exact symmetry-preserving cyclic obstruction, although only
   \(\Theta(n)\) row changes remove it.
6. The complete audited private (C_8)-component cube has packet value at
   least
   
   \[
   \frac{\operatorname {Cat}_{m-4}}{6n}
   =\left(\frac1{3072}+o(1)\right)\frac tm
   \]
   
   at every vertex of the cube.  Thus those genuine exact cyclic atoms can
   only transfer hard excess into hole debt; arbitrary dependence among
   their switching bits cannot produce (o(t/m)).  This proves sharpness of
   the target scale for that exact-factor class, not a global lower bound.

The independently audited boundary is therefore precise.  The results
exclude mesoscopically biased cyclic factors and low-entropy growing-atom
architectures.  They do not exclude a factor whose distance-tail matrices
have no negative modes and whose residual owner packets are concentrated by
more complicated, exponentially diverse cross-depth geometry.

## 1. Exact notation and the quota order statistics

All statements below are for sufficiently large (m), so
(K_A\le m-2).  Fix

\[
 1\le q\le K_A,\qquad r=m-q,\qquad
 N_q=\binom nr,\qquad
 \lambda_q=\frac W{N_q},\qquad
 c_q=\lfloor\lambda_q\rfloor,\qquad
 \rho_q=W-c_qN_q.
\tag{1.1}
\]

A balanced quota is

\[
 \beta_q(S)=c_q+\mathbf1_{\mathcal H_q}(S),\qquad
 |\mathcal H_q|=\rho_q.
\tag{1.2}
\]

Here (\mathcal H_q) denotes a high-quota family and must not be confused
with the cyclic distance matrix (H_q(F)) introduced in Section 2.

Let (F) be one exact factor.  For a target (S\in\binom{[n]}r), let

\[
 O_{q,S}=\{C\in F:S\text{ is a cyclic length-}r
 \text{ interval of }C\},\qquad h_{q,S}=|O_{q,S}|.
\tag{1.3}
\]

For row weights (x_C\ge0), write
(\operatorname {bot}_j(x;O)) for the sum of the (j) smallest weights in
(O), with value (+\infty) when (|O|<j).

### Lemma 1.1 (exact elimination of mobile quotas)

At one depth (q), there is a balanced quota (\beta_q) for which (x)
covers every survival packet if and only if

\[
 \operatorname {bot}_{c_q+2}(x;O_{q,S})\ge1
 \quad\text{for every }S,
\tag{1.4}
\]

and

\[
 \#\{S:\operatorname {bot}_{c_q+1}(x;O_{q,S})<1\}
 \le\rho_q.
\tag{1.5}
\]

The same (x) works simultaneously at several depths precisely when
(1.4)--(1.5) hold separately at every depth.  The high-quota families may
then be chosen independently by rank.

#### Proof

For one owner set, covering every (j)-subset is equivalent to requiring
that the sum of its (j) smallest weights be at least one.  A low quota has
packet size (c_q+1), while a high quota has packet size (c_q+2).
Consequently every target must satisfy the high condition (1.4), and every
failure of the low condition must receive a high quota.  This is possible
exactly when there are at most (\rho_q) failures.  Assign high quotas to
all failures and fill the unused high positions arbitrarily.  Quota choices
at distinct ranks are independent, while the row weights are common.
\(\square\)

Lemma 1.1 is an exact finite statement.  It does not construct the desired
factor or the desired weights.

## 2. The cyclic distance-tail matrix

For an unoriented cyclic row (C) and distinct coordinates (i,j), let

\[
 d_C(i,j)\in\{1,\ldots,m\}
\tag{2.1}
\]

be their shorter distance in the (n)-cycle.  Define the symmetric matrix
(H_q=H_q(F)) by

\[
 H_q(i,j)=\sum_{C\in F}(d_C(i,j)-r)_+\quad(i\ne j),\qquad
 H_q(i,i)=0.
\tag{2.2}
\]

Thus (H_q(i,j)) records only the tail event that (i,j) are farther apart
than a length-(r) interval can contain.

Put

\[
 K_q(F)=\sum_{S\in\binom{[n]}r}
   (\mu_q^F(S)-c_q)\mathbf1_S\mathbf1_S^{\mathsf T}.
\tag{2.3}
\]

Let (J=\mathbf1\mathbf1^{\mathsf T}), the unnormalised all-ones matrix.

### Theorem 2.1 (exact cyclic boundary-moment identity)

For every exact factor (F) and (1\le q\le m-2),

\[
 \boxed{K_q(F)=a_qJ+b_qI+H_q(F),}
\tag{2.4}
\]

where

\[
 a_q=\binom{n-2}{m-2}-qt-c_q\binom{n-2}{r-2},
\tag{2.5}
\]

and

\[
 \begin{aligned}
 b_q
 &=\frac{m+1}{2}t-c_q\binom{2m-1}{m-q-1}\\
 &=\frac{m+1}{2}t(1-c_qp_q),
 \qquad
 p_q=\prod_{j=1}^q\frac{m-j}{m+j}.
 \end{aligned}
\tag{2.6}
\]

In addition,

\[
 \boxed{H_q\mathbf1=q(q+1)t\,\mathbf1,}
\tag{2.7}
\]

\[
 \boxed{0\le H_q(i,j)\le\frac{qt}{2}\quad(i\ne j),}
\tag{2.8}
\]

and

\[
 \boxed{
 \lambda_qp_q=1-\frac{q(q+1)}{m(m+1)}.}
\tag{2.9}
\]

Consequently

\[
 \boxed{
 \frac{b_q}{t}
 =\frac{q(q+1)}{2m}
 +\frac{m+1}{2}p_q(\lambda_q-c_q),}
\tag{2.10}
\]

and in particular

\[
 \frac{q(q+1)t}{2m}\le b_q\le\frac{q(q+1)t}{2}.
\tag{2.11}
\]

#### Proof

In one cyclic row, the number of length-(r\le m) intervals containing a
fixed pair at shorter distance (d) is

\[
 (r-d)_+.
\tag{2.12}
\]

At the middle rank (r=m), exact ownership therefore gives, for every
distinct (i,j),

\[
 \sum_{C\in F}(m-d_C(i,j))
 =\binom{n-2}{m-2}
 =\frac{m-1}{2}t.
\tag{2.13}
\]

The elementary identity

\[
 (m-q-d)_+=(m-d)-q+(q-m+d)_+
\tag{2.14}
\]

now yields

\[
 \sum_{S\supseteq\{i,j\}}\mu_q^F(S)
 =\binom{n-2}{m-2}-qt+H_q(i,j).
\tag{2.15}
\]

For a diagonal entry, every coordinate belongs to exactly (r) cyclic
length-(r) intervals of each row, so

\[
 \sum_{S\ni i}\mu_q^F(S)=rt.
\tag{2.16}
\]

The complete rank-(r) incidence Gram matrix has off-diagonal entry
(\binom{n-2}{r-2}) and diagonal entry
(\binom{n-1}{r-1}).  Subtracting (c_q) times this matrix from
(2.15)--(2.16) proves (2.4)--(2.5), with

\[
 \begin{aligned}
 b_q
 &=rt-c_q\binom{n-1}{r-1}-a_q\\
 &=mt-\binom{n-2}{m-2}-c_q\binom{n-2}{r-1}\\
 &=\frac{m+1}{2}t-c_q\binom{2m-1}{m-q-1}.
 \end{aligned}
\tag{2.17}
\]

Since ((m+1)t/2=\binom{2m}{m}/2), cancellation of consecutive factorial
ratios gives

\[
 \frac{2\binom{2m-1}{m-q-1}}{\binom{2m}{m}}
 =\prod_{j=1}^q\frac{m-j}{m+j}=p_q,
\tag{2.18}
\]

which proves (2.6).

For a fixed (i), one row has two coordinates at every shorter distance
(d=1,\ldots,m).  Only (d=m-q+1,\ldots,m) contribute to (H_q), and
their contributions are (1,\ldots,q), twice each.  Thus one row has tail
degree (q(q+1)), proving (2.7).

For the entry bound, put (s_C=m-d_C(i,j)\in[0,m-1]).  By (2.13),

\[
 \sum_Cs_C=\frac{m-1}{2}t.
\tag{2.19}
\]

For (0\le s\le m-1),

\[
 (q-s)_+\le q\left(1-\frac{s}{m-1}\right).
\tag{2.20}
\]

Indeed, for (s\le q) the difference between the right and left sides is
(s(1-q/(m-1))\ge0), and for (s\ge q) the assertion is immediate.
Summing (2.20) and using (2.19) proves (2.8).

Finally,

\[
 \lambda_q
 =\prod_{j=1}^q\frac{m+1+j}{m+1-j}.
\tag{2.21}
\]

Multiplication by (p_q) telescopes to

\[
 \lambda_qp_q
 =\frac{m+q+1}{m+1}\frac{m-q}{m}
 =1-\frac{q(q+1)}{m(m+1)},
\tag{2.22}
\]

which gives (2.9)--(2.10).  The lower bound in (2.11) follows because
(\lambda_q-c_q\ge0).  For the upper bound, (c_q\ge1) and

\[
 1-p_q
 \le\sum_{j=1}^q\frac{2j}{m+j}
 \le\frac{q(q+1)}{m+1}.
\tag{2.23}
\]

Substitution into (2.6) proves the claim.  \(\square\)

### Corollary 2.2 (the floor trace is nonnegative and exact)

Let (P=I-J/n), the orthogonal projection onto (\mathbf1^\perp).  Then

\[
 \boxed{
 \operatorname {Tr}P(b_qI+H_q)
 =m(m+1)t\,p_q(\lambda_q-c_q).}
\tag{2.24}
\]

#### Proof

The eigenvalue of (H_q) on (\mathbf1) is (q(q+1)t), while
(\operatorname {Tr}H_q=0).  Hence

\[
 \operatorname {Tr}P(b_qI+H_q)=2mb_q-q(q+1)t.
\]

Use (2.10).  \(\square\)

Thus a negative mode is not forced by the trace: the exact fractional-part
term provides nonnegative spectral room.  At a resonant depth
(\lambda_q\in\mathbb Z), the trace on (\mathbf1^\perp) is zero.  If a
perfectly balanced factor exists there, all its nontrivial boundary-moment
eigenvalues must lie exactly at the positivity threshold.

## 3. From a packet cover to a fractional quota-safe core

The next lemma is the decisive step.  It remains inside one fixed integral
exact factor: only fractional weights on its physical rows are introduced,
and no ambient or unextendible near-factor is substituted for it.

### Lemma 3.1 (thresholded common fractional core)

Fix balanced quotas through any set of depths and let (x_C\ge0) be a
common fractional survival-packet cover.  Let (R) dominate every packet
size under consideration and set

\[
 y_C=(1-Rx_C)_+,\qquad
 D=\sum_{C\in F}(1-y_C).
\tag{3.1}
\]

Then

\[
 D\le R\sum_Cx_C,
\tag{3.2}
\]

and, at every controlled depth,

\[
 \mu_q^y(S):=\sum_{C\in O_{q,S}}y_C\le\beta_q(S)
 \qquad\text{for every }S.
\tag{3.3}
\]

#### Proof

Equation (3.2) follows termwise from

\[
 1-(1-Rx)_+=\min\{Rx,1\}\le Rx.
\]

Fix a target (S), put (k=\beta_q(S)+1\le R), and suppose that at least
(k) of its owners have positive (y)-weight.  Each of those owners has
(x_C<1/R\le1/k).  Those (k) owners form a survival packet of total
(x)-weight strictly below one, a contradiction.  Hence at most
(\beta_q(S)) owners have positive (y)-weight, and every (y_C\le1),
which proves (3.3).  The same (y) works at every depth.  \(\square\)

At a single depth (q), one may take the sharp value

\[
 R_q=c_q+2.
\tag{3.4}
\]

For one literal common fractional core at all depths one takes
(R_A=\max_{q\le K_A}(c_q+2)=O_A(1)).

## 4. The cyclic PSD obstruction

For a nonnegative weight vector (z(S)) on rank-(r) targets, write

\[
 \mathcal G(z)=\sum_Sz(S)\mathbf1_S\mathbf1_S^{\mathsf T}\succeq0.
\tag{4.1}
\]

### Theorem 4.1 (quota-uniform cyclic boundary-moment lower bound)

Fix an exact factor (F), a depth (q), and any balanced quota system
containing a depth-(q) quota.  For every (Q\succeq0) satisfying
(Q\mathbf1=0), put

\[
 M_q(Q)=\max_{S\in\binom{[n]}r}
 \mathbf1_S^{\mathsf T}Q\mathbf1_S.
\tag{4.2}
\]

If (M_q(Q)>0), then

\[
 \boxed{
 \vartheta(F,\beta)
 \ge
 \frac{[-\operatorname {Tr}Q(b_qI+H_q(F))]_+}
 {n(c_q+2)M_q(Q)}.}
\tag{4.3}
\]

The right side is independent of the positions of the (\rho_q) high
quotas.

#### Proof

Let (x) be any common packet cover.  Apply Lemma 3.1 at depth (q) with
(R_q=c_q+2), obtaining (y) and (D\le R_q\sum_Cx_C).  Put

\[
 \delta(S)=\mu_q^F(S)-\mu_q^y(S)\ge0,\qquad
 \gamma(S)=\beta_q(S)-\mu_q^y(S)\ge0.
\tag{4.4}
\]

Let (h(S)=\beta_q(S)-c_q\in\{0,1\}).  Then exactly

\[
 K_q(F)=\mathcal G(\delta)+\mathcal G(h)-\mathcal G(\gamma).
\tag{4.5}
\]

All three Gram matrices on the right are positive semidefinite.  Moreover,

\[
 \sum_S\gamma(S)
 =\sum_S\beta_q(S)-\sum_S\mu_q^y(S)
 =W-n\sum_Cy_C=nD.
\tag{4.6}
\]

Because (Q\succeq0),

\[
 \operatorname {Tr}Q\mathcal G(\delta)\ge0,\qquad
 \operatorname {Tr}Q\mathcal G(h)\ge0,
\]

while

\[
 \operatorname {Tr}Q\mathcal G(\gamma)
 =\sum_S\gamma(S)\mathbf1_S^{\mathsf T}Q\mathbf1_S
 \le nD M_q(Q).
\tag{4.7}
\]

Thus

\[
 \operatorname {Tr}QK_q(F)\ge-nD M_q(Q).
\tag{4.8}
\]

Theorem 2.1 and (Q\mathbf1=0) give

\[
 \operatorname {Tr}QK_q(F)
 =\operatorname {Tr}Q(b_qI+H_q(F)).
\]

Combine this with (D\le R_q\sum_Cx_C), then minimize over (x).
\(\square\)

Positivity of (Q) is indispensable.  Orthogonality to (\mathbf1) alone
does not permit the two positive Gram terms in (4.5) to be discarded.

### Corollary 4.2 (negative spectral mass)

Let (L_q) be the compression of (b_qI+H_q(F)) to
(\mathbf1^\perp), and let

\[
 \mathcal N_q(F)=\sum_{\xi<0}|\xi|
\tag{4.9}
\]

be the sum of the absolute values of its negative eigenvalues.  Then

\[
 \boxed{
 \vartheta(F,\beta)
 \ge\frac{\mathcal N_q(F)}{n(c_q+2)r}.}
\tag{4.10}
\]

#### Proof

Take (Q) to be the orthogonal projection onto the negative eigenspace of
(L_q).  Then (Q\succeq0), (Q\mathbf1=0), the numerator in (4.3) is
(\mathcal N_q(F)), and

\[
 \mathbf1_S^{\mathsf T}Q\mathbf1_S\le\|\mathbf1_S\|_2^2=r.
\]

Apply Theorem 4.1.  \(\square\)

### Corollary 4.3 (several depths do not amplify this certificate cone)

For tests (Q_q\succeq0), (Q_q\mathbf1=0), at any collection of depths,

\[
 \vartheta(F,\beta)
 \ge
 \frac{[-\sum_q\operatorname {Tr}Q_q(b_qI+H_q)]_+}
 {n\sum_q(c_q+2)M_q(Q_q)}.
\tag{4.11}
\]

The right side of (4.11) is at most the largest one-depth ratio (4.3).
Thus merely summing block-diagonal quadratic boundary moments gives no
common-depth amplification.  An amplification theorem must use
owner-specific cuts or genuine cross-rank row features.

#### Proof

Apply the proof of Theorem 4.1 separately at each depth to the same packet
cover (x), using (D_q\le(c_q+2)\sum_Cx_C), and sum the trace
inequalities.  For the last assertion, replace each signed numerator by its
positive part and compare a ratio of sums with the maximum of the individual
ratios.  \(\square\)

## 5. A mesoscopic signed cyclic obstruction

For disjoint coordinate sets (P,N\subset[n]), define

\[
 w_q(P)=\sum_{\{i,j\}\subset P}H_q(i,j),\qquad
 w_q(P,N)=\sum_{i\in P,j\in N}H_q(i,j).
\tag{5.1}
\]

### Theorem 5.1 (alternating tail-distance no-go)

Let (P,N) be disjoint, with

\[
 |P|=|N|=s/2,\qquad s\le2r.
\tag{5.2}
\]

Assume also (r+s/2\le n), so a rank-(r) set can contain all of one
side and none of the other.  If, for some (\gamma>0),

\[
 2\bigl[w_q(P,N)-w_q(P)-w_q(N)\bigr]
 \ge\bigl[b_q+\gamma q(q+1)t\bigr]s,
\tag{5.3}
\]

then every balanced quota system satisfies

\[
 \boxed{
 \vartheta(F,\beta)
 \ge\frac{4\gamma q(q+1)t}{n(c_q+2)s}.}
\tag{5.4}
\]

In particular, suppose along a sequence (m\to\infty) that

\[
 \frac q{\sqrt m}\to a\in(0,A],\qquad s\le Cq,
\tag{5.5}
\]

and (5.3) holds with fixed (C,\gamma>0).  Then

\[
 \boxed{
 \vartheta(F,\beta)
 \ge\left(\frac{2\gamma a}{C(c_q+2)}+o(1)\right)
 \frac t{\sqrt m}=\omega(t/m).}
\tag{5.6}
\]

Thus no factor sequence with this aggregate mesoscopic signed
tail-distance bias can witness \((\mathrm{SPC}_A)\).

#### Proof

Put (u=\mathbf1_P-\mathbf1_N) and (Q=uu^{\mathsf T}).  Then
(Q\succeq0), (Q\mathbf1=0), and

\[
 -u^{\mathsf T}(b_qI+H_q)u
 =2[w_q(P,N)-w_q(P)-w_q(N)]-b_qs.
\tag{5.7}
\]

Under the size assumptions, the largest value of
(|\langle u,\mathbf1_S\rangle|) over (|S|=r) is (s/2).  Hence

\[
 M_q(Q)=\frac{s^2}{4}.
\tag{5.8}
\]

Hypothesis (5.3) makes the numerator of (4.3) at least
(\gamma q(q+1)ts).  Equations (5.4)--(5.6) follow.  \(\square\)

Hypothesis (5.3) is a direct statement about the aggregate matrix of the
whole exact factor.  It is not inferred merely from a positive-density
subfamily of rows with one fixed antipodal placement.  That tempting
inference is generally false: exact ownership fixes the mean distance of
every coordinate pair at ((m+1)/2), so a strongly antipodal placement can
occur in at most (1/2+o(1)) of the rows, while an arbitrary remainder can
cancel its signed bias.  The theorem is therefore nonvacuous only when the
aggregate signed bias itself is established, or when the remainder is
separately controlled.

### Proposition 5.2 (edit robustness)

Suppose (Q\succeq0), (Q\mathbf1=0), and

\[
 \operatorname {Tr}Q(b_qI+H_q(F))
 \le-\gamma q(q+1)t\operatorname {Tr}Q.
\tag{5.9}
\]

If an exact factor (F') is obtained by replacing (k\le\gamma t/4)
rows of (F) by (k) rows, then

\[
 \operatorname {Tr}Q(b_qI+H_q(F'))
 \le-\frac\gamma2q(q+1)t\operatorname {Tr}Q.
\tag{5.10}
\]

#### Proof

The one-row tail matrix is symmetric, nonnegative, and
(q(q+1))-regular.  Its operator norm is therefore at most (q(q+1)).
Replacing (k) rows changes (H_q) by a sum of (k) new minus (k) old
one-row matrices, so

\[
 |\operatorname {Tr}Q(H_q(F')-H_q(F))|
 \le2kq(q+1)\operatorname {Tr}Q.
\]

Use (k\le\gamma t/4).  \(\square\)

Thus an actually exhibited negative mode would exclude a positive-radius
exact edit basin, not just a single representative.

## 6. Why the obstruction requires growing correlated atoms

### Theorem 6.1 (support threshold)

Let (Q\succeq0), (Q\mathbf1=0), be supported on a coordinate set
(U\subset[n]) of size (s).  Then

\[
 \boxed{
 \operatorname {Tr}Q(b_qI+H_q)
 \ge\left(b_q-\frac{(s-1)qt}{2}\right)\operatorname {Tr}Q.}
\tag{6.1}
\]

Consequently a negative boundary-moment certificate supported on (s)
coordinates requires

\[
 \boxed{s>1+\frac{2b_q}{qt}.}
\tag{6.2}
\]

Suppose (q/\sqrt m\to a>0) and, along the sequence,
(c_q=c) with

\[
 1-ce^{-a^2}>0.
\tag{6.3}
\]

Then every negative certificate satisfies

\[
 \boxed{
 \frac{s}{q}\ge
 \frac{1-ce^{-a^2}}{a^2}-o(1).}
\tag{6.4}
\]

For example, when (0<a<\sqrt{\log2}), one has (c=1), and every
certificate uses (\Theta(q)=\Theta(\sqrt m)) coordinates.

#### Proof

By (2.8), every row sum of the principal matrix (H_q[U]) is at most
((s-1)qt/2).  Its operator norm is at most that quantity, so

\[
 \operatorname {Tr}QH_q
 \ge-\frac{(s-1)qt}{2}\operatorname {Tr}Q.
\]

This proves (6.1)--(6.2).  Under the stated scaling,
(p_q=e^{-a^2+o(1)}), and (2.6) gives

\[
 \frac{2b_q}{qt}
 =\frac{m(1-ce^{-a^2}+o(1))}{q}
 =q\left(\frac{1-ce^{-a^2}}{a^2}-o(1)\right).
\]

This proves (6.4).  \(\square\)

At resonant values (ce^{-a^2}=1), the leading support threshold vanishes;
the exact floor term (2.10), not the nonresonant asymptotic, must then be
used.  No claim is made across such a resonance without checking the exact
fractional part (\lambda_q-c_q).

### Theorem 6.2 (exact-ownership entropy obstruction for type-local atoms)

Fix (U\subset[n]), (|U|=s), and a family
(\mathcal T\subseteq2^U).  Let (\mathcal C\subseteq F) be a row family
such that every middle interval (X) of every (C\in\mathcal C) satisfies

\[
 X\cap U\in\mathcal T.
\tag{6.5}
\]

Then

\[
 \boxed{
 \frac{|\mathcal C|}{t}
 \le\sum_{R\in\mathcal T}
 \frac{\binom{n-s}{m-|R|}}{\binom nm}
 \le|\mathcal T|
 \left(\frac{m+1}{n-s+1}\right)^s.}
\tag{6.6}
\]

Now let a rooted placement type record the cyclic positions of all
coordinates of (U), modulo rotation and reversal.  A single placement
type generates at most (n) traces (X\cap U) among its middle windows.
Consequently, if rows belonging to a catalogue of (L) placement types
form (\mathcal C), then

\[
 \boxed{
 \frac{|\mathcal C|}{t}
 \le Ln\left(\frac{m+1}{n-s+1}\right)^s.}
\tag{6.7}
\]

If (s=\Theta(\sqrt m)), a positive fixed fraction of an exact factor
therefore requires

\[
 \boxed{
 L\ge\frac1n\exp((\log2-o(1))s).}
\tag{6.8}
\]

In particular every polynomial or (\exp(o(s))) placement catalogue is
exponentially negligible.

#### Proof

The (n|\mathcal C|) middle windows in the rows of (\mathcal C) are all
distinct because (F) is exact.  For one fixed trace (R\subseteq U),
there are exactly

\[
 \binom{n-s}{m-|R|}
\]

middle sets with that trace, interpreted as zero if the lower argument is
inadmissible.  This proves the first inequality in (6.6).

Choose a uniform (m)-subset and reveal the required membership or
nonmembership status of the (s) coordinates of (U) sequentially.
After fewer than (s) revelations, the conditional probability of either
required status is at most

\[
 \frac{m+1}{n-s+1}.
\]

Multiplication proves the second inequality in (6.6).  A rooted cyclic
placement has only (n) middle-window starts, hence at most (n) traces.
Taking the union of the trace families of (L) types gives (6.7).

Finally, for (s=o(m)),

\[
 \left(\frac{m+1}{n-s+1}\right)^s
 =\exp[-(\log2-o(1))s].
\]

Rearrange (6.7).  \(\square\)

Theorems 6.1 and 6.2 compose into a genuine architecture no-go.  In a
nonresonant Gaussian window, a boundary-moment obstruction needs a growing
(\Theta(\sqrt m))-coordinate atom.  If that atom is local to only a
subexponential catalogue of cyclic placement types, exact ownership makes
it negligible.  A factor-wide mode must aggregate coherently across
exponentially many placement types.  This does not prove that such coherent
aggregation is impossible.

## 7. The exact first-shadow Gram condition and the local Hall relaxation

At depth one and (m\ge3),

\[
 c_1=1,\qquad \rho_1=\frac{2W}{m+2},\qquad
 a_1=\frac{m-4}{m+2}t,\qquad b_1=t.
\tag{7.1}
\]

### Theorem 7.1 (first-shadow boundary Gram identity)

Suppose an integral row set (B\subseteq F), (|B|=b), is deleted and the
remaining core has depth-one loads (\eta(S)\le\beta_1(S)).  Put

\[
 R_2=\{S:\eta(S)=2\},\qquad Z=\{S:\eta(S)=0\},
\tag{7.2}
\]

and let

\[
 P_B=\sum_{C\in B}\sum_{S\text{ a depth-one interval of }C}
 \mathbf1_S\mathbf1_S^{\mathsf T}.
\tag{7.3}
\]

Then

\[
 \boxed{
 a_1J+tI+H_1
 =\sum_{S\in R_2}\mathbf1_S\mathbf1_S^{\mathsf T}
 -\sum_{S\in Z}\mathbf1_S\mathbf1_S^{\mathsf T}+P_B,}
\tag{7.4}
\]

and

\[
 |Z|=|R_2|+nb-\rho_1\le nb.
\tag{7.5}
\]

In particular, if the full factor itself is perfectly balanced at depth
one, then

\[
 \boxed{
 a_1J+tI+H_1
 =\sum_{S:\mu_1(S)=2}\mathbf1_S\mathbf1_S^{\mathsf T}.}
\tag{7.6}
\]

Consequently (tI+H_1\succeq0) on (\mathbf1^\perp).

#### Proof

Subtract the all-one floor Gram matrix from the full load Gram matrix.  A
retained load two contributes (+1), a retained load zero contributes
(-1), a retained load one contributes zero, and every deleted occurrence
contributes through (P_B).  This proves (7.4).

The core has (W-nb) depth-one occurrences, so

\[
 |R_2|-|Z|=(W-nb)-N_1=\rho_1-nb.
\]

Every retained load-two target must occupy a high quota, so
(|R_2|\le\rho_1), proving (7.5).  For (b=0), quota safety and equality of
total masses force the full load vector to equal the quota vector, giving
(7.6) and the PSD conclusion.  \(\square\)

This is stronger than total load, point-margin, or ordinary Hall
arithmetic.  To show exactly where cyclicity enters, the following local
relaxation is useful.

Let

\[
 \mathcal L=\binom{[n]}m,\qquad
 \mathcal R=\binom{[n]}{m-1},\qquad
 X\sim S\Longleftrightarrow X\cap S=\varnothing.
\tag{7.7}
\]

The degrees of this bipartite graph are

\[
 \delta=\binom{m+1}{2}\quad(X\in\mathcal L),\qquad
 \Delta=\binom{m+2}{2}\quad(S\in\mathcal R).
\tag{7.8}
\]

For a disjoint pair (X,S), if
([n]\setminus(X\cup S)=\{a,b\}), the unique local odd-graph wedge centred
opposite (X) has neighbours (S\cup\{a\}) and (S\cup\{b\}).  Thus
(7.7) is the exact local angle-feasibility graph.

### Proposition 7.2 (all local Hall constraints attain perfect balance)

The graph (7.7) has:

1. a matching saturating every (S\in\mathcal R), hence an integral
   collision-free local angle core using (N_1) distinct centres and
   leaving exactly
   
   \[
   \rho_1=W-N_1=\frac{2W}{m+2}
   \tag{7.9}
   \]
   
   centres; and
2. an assignment of every (X\in\mathcal L) to a neighbouring target
   such that every target has load one or two, with exactly (\rho_1)
   targets of load two.

#### Proof

For (Y\subseteq\mathcal R), edge counting gives

\[
 \Delta|Y|\le\delta|N(Y)|,
\]

so Hall's condition holds and proves Part 1.

For Part 2, replace every right vertex by two clones.  For
(A\subseteq\mathcal L),

\[
 \delta|A|\le\Delta|N(A)|,\qquad
 \frac{2\delta}{\Delta}=\frac{2m}{m+2}\ge1,
\]

so the cloned graph has a matching saturating all left vertices.  This is
an assignment with right loads at most two.  Choose one maximizing the
number of used right targets.

If a target (S_0) were unused, follow alternating transfers: from a
reachable target (S), every adjacent centre (X) leads to its currently
assigned target.  If a load-two target were reached, shifting assignments
along the path would fill (S_0), leave the terminal target used, and
increase the support.  Hence no reachable target has load two.  If
(R_0) is the reachable target set and (L_0=N(R_0)), all centres in
(L_0) are assigned inside (R_0), while at least (S_0) is empty, so

\[
 |L_0|\le|R_0|-1.
\]

But all (\Delta|R_0|) incidences from (R_0) enter (L_0), and every
left vertex has degree (\delta), giving

\[
 \Delta|R_0|\le\delta|L_0|<\delta|R_0|,
\]

a contradiction.  Thus every target is used.  Conservation then forces
exactly (W-N_1=\rho_1) double targets.  \(\square\)

Proposition 7.2 is deliberately not promoted to an exact factor.  It does
not enforce mutual-neighbour reciprocity, decomposition into literal
(n)-cycles, or factorability of the middle leave.  It proves that local
wedge feasibility, ordinary Hall, total slots, and even the ideal (1/2)
histogram do not obstruct the SPC scale.  The Gram condition (7.6) and the
packet cuts live beyond this local relaxation.

There is already a genuine obstruction to the most symmetric attempted
lift of Part 1.

### Proposition 7.3 (prime equivariant cyclic-lift obstruction)

Assume

\[
 p=n=2m+1
\tag{7.10}
\]

is prime, and let a regular coordinate \(p\)-cycle act on the local graph
(7.7).  The quotient graph has a matching saturating all right orbits; its
lift is an equivariant collision-free local angle core covering every
depth-one target once.  It uses \(N_1\) centres and therefore would have

\[
 s=\frac{N_1}{p}=\frac{mt}{m+2}
\tag{7.11}
\]

wreath rows if it lifted to literal \(p\)-cycles.

Any equivariant partial wreath packing with \(s\) rows must satisfy

\[
 \boxed{s\bmod p\le m,}
\tag{7.12}
\]

where the left side is the least nonnegative residue.  For the quotient
Hall core,

\[
 t\equiv2(-1)^m\pmod p,\qquad
 s\equiv-\frac23(-1)^m\pmod p.
\tag{7.13}
\]

Its least residue exceeds \(m\) precisely in the prime congruence classes

\[
 \boxed{p\equiv1\ \text{or}\ 11\pmod {12}.}
\tag{7.14}
\]

Hence in those classes the sharp equivariant collision-free Hall core
cannot satisfy the literal \(p\)-cycle condition.

#### Proof

Every nonempty proper coordinate subset has a free orbit under a regular
action of the prime-order group.  Quotienting (7.7) therefore preserves its
biregular incidence count, with parallel quotient edges allowed.  The same
edge-count proof as in Proposition 7.2 gives a right-saturating quotient
matching, and lifting its edge orbits gives the asserted equivariant local
core.

The coordinate \(p\)-cycle permutes the row components of any equivariant
literal wreath packing in orbits of size one or \(p\).  A fixed wreath
support is determined by a step \(a\in\mathbb F_p^\times\): after numbering
its windows cyclically, the coordinate action advances them by \(a\), and
the successive leaving labels force the coordinate order to be the
corresponding arithmetic \(p\)-cycle.  Steps \(a\) and \(-a\) give the same
unoriented support.  Thus there are at most

\[
 \frac{p-1}{2}=m
\]

fixed wreath supports.  The number of components modulo \(p\) is the number
of fixed components modulo \(p\), proving (7.12).

Since

\[
 \binom{p-1}{m}\equiv(-1)^m\pmod p,\qquad
 m+1\equiv\frac12\pmod p,
\]

the Catalan number satisfies \(t\equiv2(-1)^m\pmod p\).  Also

\[
 \frac{m}{m+2}\equiv-\frac13\pmod p,
\]

which proves (7.13).  The four possible prime residues modulo \(12\) give

\[
\begin{array}{c|c}
p\bmod12& s\bmod p\\ \hline
1&(2p-2)/3\\
5&(p-2)/3\\
7&(p+2)/3\\
11&(2p+2)/3.
\end{array}
\tag{7.15}
\]

Only the first and fourth entries exceed \(m=(p-1)/2\).  This proves
(7.14).  \(\square\)

This obstruction is exact but deliberately narrow.  Changing the core row
count by only \(\Theta(p)\) removes the residue obstruction, negligible
beside the permitted \(O(t/m)\) exceptional scale.  Proposition 7.3 closes
the symmetry-preserving sharp collision-free lift, not unrestricted SPC.

## 8. A genuine exact-factor cube locked at the (t/m) scale

This section imports one already audited exact component fact and derives a
new packet consequence.

### Audited private-component input

For every (m\ge4), the canonical exact factor contains

\[
 L=\operatorname {Cat}_{m-4}
\tag{8.1}
\]

pairwise independent genuine (C_8) switch components, indexed by
(V\in\mathcal D_{m-4}).  Their depth-one four-cell supports are pairwise
disjoint, and on each support the switch changes the load profile

\[
 (3,1,1,1)\longmapsto(2,2,0,2).
\tag{8.2}
\]

This is Theorem 2.1 of
`MATH_ATTACK_P5_AFR_BRIDGE_SELECTION_20260725.md`; no unproved property of
the canonical factor is used here.

For a depth-one histogram (h), define

\[
 H_0(h)=|\{S:h(S)=0\}|,\qquad
 E_2(h)=\sum_S(h(S)-2)_+.
\tag{8.3}
\]

### Lemma 8.1 (exact mobile depth-one overload)

For every nonnegative integral depth-one histogram of total (W),

\[
 \boxed{O_1(h)=\max\{H_0(h),E_2(h)\},}
\tag{8.4}
\]

where (O_1) is overload minimized over all balanced (1/2)-valued
quotas.

#### Proof

Let (r_2=|\{S:h(S)\ge2\}|).  Starting from quota one everywhere, the
overload is

\[
 P=\sum_S(h(S)-1)_+=r_2+E_2.
\]

Since (W=N_1+\rho_1), conservation also gives

\[
 r_2+E_2=H_0+\rho_1.
\tag{8.5}
\]

The (\rho_1) upper quotas remove one overload unit on at most
(\min\{r_2,\rho_1\}) targets.  Therefore

\[
 O_1=P-\min\{r_2,\rho_1\}.
\]

If (r_2\ge\rho_1), this equals (H_0\ge E_2) by (8.5); if
(r_2<\rho_1), it equals (E_2>H_0).  \(\square\)

### Theorem 8.2 (private cyclic cube packet obstruction)

Switch an arbitrary subset (I\subseteq\mathcal D_{m-4}), put
(k=|I|), and let (F_I) be the resulting exact factor.  Then for every
balanced common multidepth quota system,

\[
 \boxed{
 \vartheta(F_I,\beta)
 \ge\frac{\operatorname {Cat}_{m-4}}{6n}.}
\tag{8.6}
\]

Consequently

\[
 \boxed{
 \vartheta(F_I,\beta)
 \ge\left(\frac1{3072}+o(1)\right)\frac tm.}
\tag{8.7}
\]

More exactly, if (H_0^0,E_2^0) are the canonical values, then

\[
 H_0(F_I)=H_0^0+k,\qquad
 E_2(F_I)=E_2^0-k.
\tag{8.8}
\]

Thus arbitrary grouping or dependence among all (L) component bits only
transfers hard-excess debt into hole debt.

#### Proof

The disjoint rectangle effect (8.2) creates one hole and removes one unit
of (E_2) per switched component, proving (8.8).  The (L) old load-three
cells are distinct, so

\[
 H_0(F_I)\ge k,\qquad E_2(F_I)\ge L-k.
\]

Lemma 8.1 gives

\[
 O_1(F_I)\ge\max\{k,L-k\}\ge L/2.
\tag{8.9}
\]

Now fix any balanced depth-one quota (\beta_1) and any fractional packet
cover (x).  On a violating target with (h) owners and packet size
(j=\beta_1(S)+1\le3), average all (j)-packet inequalities.  A fixed
owner belongs to a (j/h) fraction of the packets, so

\[
 \sum_{C\in O_{1,S}}x_C\ge\frac hj.
\tag{8.10}
\]

Also

\[
 h-\beta_1(S)\le h\le3\frac hj
 \le3\sum_{C\in O_{1,S}}x_C.
\tag{8.11}
\]

Summing over violating targets counts every row at most (n) times and
gives

\[
 O_{\beta_1}(F_I)\le3n\sum_Cx_C.
\tag{8.12}
\]

The optimized overload is no larger than (O_{\beta_1}), so (8.9)--(8.12)
prove (8.6).  Finally,

\[
 \frac{\operatorname {Cat}_{m-4}}{t}\longrightarrow\frac1{256},
 \qquad n\sim2m,
\]

which proves (8.7).  \(\square\)

The lower bound (8.7) is of the same order as the requested SPC upper
bound.  It rules out (o(t/m)) inside this whole genuine exact-factor cube,
but it does not rule out (O(t/m)), and therefore it is not a global
counterexample to \((\mathrm{SPC}_A)\).

## 9. Independent audit of the decisive step

The boundary-moment theorem and packet-to-PSD implication were audited
independently from the proof above.  The audit checked the following points.

1. The off-diagonal interval count is ((r-d)_+), with no ordered-pair
   factor.  The row sum of (H_q) is (q(q+1)t), not half that value.
2. Exact middle ownership gives
   
   \[
   \sum_C(m-d_C(i,j))=\binom{n-2}{m-2}=\frac{m-1}{2}t,
   \]
   
   and sharpens the naive entry bound (qt) to (qt/2).
3. The diagonal coefficient is
   
   \[
   b_q=\frac{m+1}{2}t-c_q\binom{2m-1}{m-q-1};
   \]
   
   the product formula and the exact floor correction (2.10) agree.
4. In Lemma 3.1 the inequality is strict: positive (y_C) implies
   (x_C<1/R), so (\beta+1) positive owners really contradict a packet
   inequality even when the packet size equals (R).
5. In Theorem 4.1, the quota slack has mass exactly (nD), and the sign in
   (4.5) is essential.  Both retained high-quota mass and deleted-row mass
   are positive Gram terms; only the quota slack is negative.
6. (Q\succeq0) is necessary.  The condition (Q\mathbf1=0) merely kills
   the (a_qJ) term.
7. For the two-block test, (M_q(Q)=(s/2)^2) requires the explicit size
   assumptions in Theorem 5.1.  Without them the exact value is
   (\min\{s/2,r\}^2), with a further outside-capacity condition if all of
   one sign is to be selected.
8. A fixed antipodal placement cannot be assumed on an arbitrary majority
   of an exact factor.  Accordingly, Theorem 5.1 assumes the aggregate
   signed (H_q)-bias directly and makes no invalid dominant-type
   inference.
9. Summing pair-moment certificates across depths yields only a ratio of
   sums and cannot exceed the best one-depth ratio.  This limitation does
   not apply to general owner-subset packet cuts.

No audit correction changes (0.3), (5.4), the support threshold, or the
type-entropy theorem.

## 10. Final proved/conditional boundary

### Proved unconditionally

1. The exact cyclic boundary-moment identity (2.4), including all floor
   constants, row sums, entry bounds, and the fractional-part trace.
2. The quota-uniform packet lower bound (4.3) for every exact factor.
3. The negative spectral-mass bound (4.10).
4. The exact support threshold (6.2) and its nonresonant Gaussian
   consequence (6.4).
5. The exact-ownership type-entropy obstruction (6.6)--(6.8).
6. The depth-one Gram identity (7.4)--(7.6).
7. The integral local Hall and cap-two relaxations of Proposition 7.2,
   together with their explicit failure to enforce cyclic reciprocity,
   (n)-cycle decomposition, or extendibility.
8. The prime equivariant literal-cycle obstruction of Proposition 7.3.
9. The private exact-component cube lower bound (8.6).

### Conditional only on an explicit property of the selected exact factor

If the aggregate signed distance-tail bias (5.3) holds on
(s=O(q)) coordinates at (q\asymp\sqrt m), then that factor and a fixed
positive-radius exact edit basin have packet value
(\Omega_A(t/\sqrt m)=\omega(t/m)).  No sequence of exact factors satisfying
this hypothesis can prove \((\mathrm{SPC}_A)\).

### Still unproved

There is no proof here that every exact factor has such a negative mode.
There is also no construction of an exact factor whose common multidepth
packet value is (O_A(t/m)).  A successful positive construction must evade
all negative cyclic moment modes, preserve exact middle ownership and
literal (n)-cycle rows, and concentrate the remaining owner packets on
(O_A(t/m)) rows.  A successful universal no-go must add an owner-specific
or cross-rank obstruction beyond the block-diagonal pair moments proved
here.

No labelled synchronization theorem, no constant-one contiguous-OR theorem,
and no literal OR word is claimed.
