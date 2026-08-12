# Pair-token adjacent-priority atlas: exact chronology and nonnegative joined Gram

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or
long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad T=\binom n{m-1},\qquad W=\binom nm,
 \qquad H=O(\sqrt{m\log m}).
\]

Fix disjoint coordinate pairs \(P_1,\ldots ,P_m\), one unpaired
coordinate, and one exact local wreath factor \(F_P\) on
\([n]\setminus P\) for every pair \(P\).  Every ordering of the pairs
gives the first-avoided lower-saturating token matching of
`PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md`, Section 5.

This note constructs a common-base alternating atlas between the two
matchings obtained by interchanging two adjacent pairs in the priority
order.  Its conclusions are as follows.

1.  The changed lower targets have an exact inclusion-exclusion count.
    In the two affected local factors they occupy a total of

    \[
      K_j\le \min\{4j\operatorname {Cat}_{m-1},\,2|D_j|\}
      =o(W/H)
      \tag{0.1}
    \]

    cyclic intervals, uniformly in the adjacent position \(j\).

2.  The symmetric difference consists of alternating paths as well as
    cycles.  After the harmless standard dummy completion, join its
    elementary alternating components whenever they meet the same one of
    the \(K_j\) physical intervals.  Every resulting macro-corner is a
    lower-saturating matching and

    \[
       J(M_{\eta})\le J(M)+K_j=o(W/H).
       \tag{0.2}
    \]

    Hence every corner has literal two-parent flags and word cost
    \(T+o(W)\).  In particular its predecessor conditional probability is
    \(1-o(1/H)\), exactly as required by the token-polytope audit.

3.  Join further any two components having oppositely signed occurrences
    of one common flag target.  This extra joining cannot hurt (0.2).  For
    the resulting bundles the joined-owner cross-Gram is not abstract: it
    is exactly the number of equal-target same-sign token pairs in distinct
    bundles.  Thus

    \[
       \boxed{A-V\ge0.}
       \tag{0.3}
    \]

    The complete floor-corrected Haar interpolation identity is

    \[
      \boxed{
      \mathbb E\mathcal Q_w(M_\eta)
      ={\mathcal Q_w(M)+\mathcal Q_w(M')\over2}
       -{A-V\over4}
      \le {\mathcal Q_w(M)+\mathcal Q_w(M')\over2}.}
      \tag{0.4}
    \]

    This holds simultaneously for every positive system of Gaussian-window
    rank weights and with all adjacent-integer floors exact.

Consequently adjacent-priority interpolation has no chronology cost and no
negative Gram curvature.  The statement still needed for constant one is
a quantitative lower bound for the same-sign collision term in (0.3), or
an independent proof that one endpoint of a priority swap has smaller
weighted defect.  Neither follows merely from biregularity.  No
constant-one conclusion is claimed here.

## 1. Exact token conventions and two small audits

Let \(P\) be omitted, let

\[
 \pi=(x_0,\ldots ,x_{2m-2}),\qquad
 X_i=I_\pi(i,m),\qquad S_i=I_\pi(i,m-1),
 \tag{1.1}
\]

with cyclic indices.  Then

\[
 S_i=X_{i-1}\cap X_i.
 \tag{1.2}
\]

The oriented start token used below is

\[
 e(P,\pi,i)=(S_i,X_{i-1}).
 \tag{1.3}
\]

Its two signed depth-\(q\) flags are exactly

\[
 L_q(e)=I_\pi(i+q-1,m-q),\qquad
 U_q(e)=I_\pi(i-1,m+q).
 \tag{1.4}
\]

For completeness, the first-avoided construction really is a matching
with this predecessor convention, although the source report proved the
successor convention explicitly.  If \(P\) is the first pair avoided by
\(S_i\), then \(S_i\subset X_{i-1}\subseteq[n]\setminus P\), so
\(X_{i-1}\) also meets every earlier pair and avoids \(P\).  Thus it has
the same category as \(S_i\).  The length-\(m\) windows in one local factor
are all distinct, and middle owners in different categories are disjoint.
Hence the predecessor owners are distinct.

There is also a correction to the last paragraph of
`PAIR_OMISSION_CLUSTERED_TOKEN_REDUCTION_20260725.md`.  Two matchings which
saturate \(V_-\) need not have symmetric difference equal to a union of
cycles, because

\[
 |V_0|-|V_-|={2W\over m+2}>0.
 \tag{1.5}
\]

Their symmetric difference is a disjoint union of even alternating cycles
and alternating paths whose endpoints lie in \(V_0\).  Every whole path is
nevertheless a legal matching switch.  Equivalently, add
\(2W/(m+2)\) dummy left vertices and match them to the unused middle
owners; then all components become even cycles.  No flag is attached to a
dummy edge.  We freely use this completion below.

## 2. The exact carrier of an adjacent priority swap

Fix a priority order and let

\[
 A=P_j,\qquad B=P_{j+1}.
\]

Let \(M\) be its first-avoided matching and \(M'\) the matching after
interchanging \(A,B\), leaving all local factors and all other priorities
fixed.  Define

\[
 D_j=\left\{S\in\binom{[n]}{m-1}:
 S\cap A=S\cap B=\varnothing,
 \ S\cap P_h\ne\varnothing\ (h<j)\right\}.
 \tag{2.1}
\]

### Lemma 2.1 (exact changed set)

The matchings \(M,M'\) use the same token at every lower target outside
\(D_j\).  At \(S\in D_j\), \(M\) uses its token in \(F_A\), while
\(M'\) uses its token in \(F_B\).  Moreover

\[
 \boxed{
 |D_j|=\sum_{h=0}^{j-1}(-1)^h\binom{j-1}{h}
             \binom{2m-3-2h}{m-1}.}
 \tag{2.2}
\]

#### Proof

If \(S\) avoids both \(A,B\), their relative order decides which is first.
If it avoids only one, that same pair is first in either order; if it
avoids neither, neither can be first.  This proves the first assertion.

After deleting \(A\cup B\), there are \(2m-3\) available coordinates.
Inclusion-exclusion over failure to meet any chosen subfamily of the
\(j-1\) earlier disjoint pairs gives (2.2).  \(\square\)

### Lemma 2.2 (physical interval count)

Put

\[
 R_m={1\over2m-1}\binom{2m-1}{m-1}
     =\operatorname {Cat}_{m-1}.
 \tag{2.3}
\]

Its comparison with the global middle layer is exact:

\[
 {R_m\over W}={m+1\over2(2m-1)(2m+1)}.
 \tag{2.3a}
\]

In one row of \(F_A\), the starts representing \(D_j\) have at most
\(2j\) cyclic components.  The same holds in one row of \(F_B\).
Consequently their total number \(K_j\) of nonempty cyclic intervals
satisfies

\[
 \boxed{K_j\le\min\{4jR_m,\,2|D_j|\}.}
 \tag{2.4}
\]

#### Proof

For any fixed coordinate pair \(C\), the starts at which a cyclic
length-\((m-1)\) window avoids \(C\) form the intersection of two circular
arcs, hence have at most two cyclic components.  In a row of \(F_A\), the
set (2.1) is the avoid-\(B\) set with the avoid-\(P_h\) sets, \(h<j\),
removed.  Beginning with at most two components, removal of one set having
at most two components increases the component count by at most two.  The
result has at most \(2+2(j-1)=2j\) components.  Interchange \(A,B\) for
the other factor.

There are \(R_m\) rows in either exact local factor.  This proves the first
bound.  Each nonempty interval contains a changed target; every target of
\(D_j\) occurs once in either factor, proving the second.  \(\square\)

### Lemma 2.3 (uniform Gaussian estimate)

Uniformly for \(1\le j<m\),

\[
 \boxed{K_j=o(W/H)}
 \tag{2.5}
\]

whenever \(H=O(\sqrt{m\log m})\).

#### Proof

Choose a uniform \((m-1)\)-subset of the \(2m-3\) coordinates outside
\(A\cup B\).  Before conditioning on its size, include coordinates
independently with probability

\[
 p={m-1\over2m-3}.
\]

The events of meeting the earlier pairs are independent and each has
probability

\[
 1-(1-p)^2
 =1-\left({m-2\over2m-3}\right)^2\le {8\over9}
 \qquad(m\ge3).
\]

The probability of the conditioning event is at least \(c m^{-1/2}\)
for an absolute \(c>0\).  Therefore

\[
 |D_j|\le C\sqrt m\binom{2m-3}{m-1}
 \left({8\over9}\right)^{j-1}.
 \tag{2.6}
\]

Let \(t=\lceil20\log m\rceil\).  For \(j\le t\), (2.4) and
\(R_m=\Theta(W/m)\) give

\[
 {HK_j\over W}=O\left({H\log m\over m}\right)=o(1).
\]

For \(j>t\), (2.4)--(2.6), \(\binom{2m-3}{m-1}\le W\), and
\(20\log(9/8)>2\) give

\[
 {HK_j\over W}
 \le C H\sqrt m\,m^{-20\log(9/8)}=o(1).
\]

Both estimates are uniform in their displayed ranges.  \(\square\)

## 3. Common-base interval-joined alternating atlas

Let \(\mathcal C\) be the elementary alternating paths and cycles of
\(M\triangle M'\).  Initially declare two members of \(\mathcal C\)
equivalent whenever their changed token edges meet the same one of the
physical intervals counted by \(K_j\), in either \(F_A\) or \(F_B\), and
take transitive closure.  Call the resulting unions interval bundles.

For any set of interval bundles, switch all elementary alternating
components in the chosen bundles.  Denote the resulting matching by
\(M_\eta\).

### Theorem 3.1 (literal low-boundary common base)

Every \(M_\eta\) saturates \(V_-\), uses distinct middle owners, and

\[
 \boxed{J(M_\eta)\le J(M)+K_j=o(W/H).}
 \tag{3.1}
\]

All its flags (1.4) are literal with total word cost

\[
 T+O(HJ(M_\eta))=T+o(W).
 \tag{3.2}
\]

#### Proof

Switching a union of whole alternating components preserves degree one at
every lower vertex and degree at most one at every middle vertex.  Thus the
central matching constraints hold at every corner.

In an \(F_A\) row, a \(D_j\)-interval is entirely selected by \(M\); in
an \(F_B\) row it is entirely unselected by \(M\).  The interval joining
forces all token switches on that interval to use one common bit.  Hence a
corner is obtained from \(M\) by deleting some whole \(D_j\)-intervals in
the \(F_A\) rows and adding some whole \(D_j\)-intervals in the \(F_B\)
rows.  Deleting an all-one cyclic interval, or adding an all-zero cyclic
interval, increases the number of selected cyclic runs by at most one.
This proves the first inequality in (3.1).  The original first-avoided
bound is

\[
 J(M)=O(W\log ^2m/m)=o(W/H),
\]

and Lemma 2.3 handles \(K_j\).

Finally each selected source-row component is a consecutive segment of a
genuine pair-omission row.  Adding its standard \(H\)-entry collar realizes
all flags (1.4), including endpoint flags, at cost \(O(H)\) per run.
This proves (3.2).  \(\square\)

If a selected token is sampled uniformly from a corner, at most
\(J(M_\eta)\) selected tokens have an unselected predecessor in their
source row.  Thus Theorem 3.1 also gives the exact conditional estimate

\[
 \Pr(\hbox{predecessor selected}\mid\hbox{token selected})
 \ge1-{J(M_\eta)\over T}=1-o(1/H).
 \tag{3.3}
\]

This is the positive-along-rows condition (4.7) of
`PAIR_OMISSION_TOKEN_POLYTOPE_AUDIT_20260725.md`, now simultaneously valid
at every atlas corner rather than only at its two endpoints.

## 4. Exact floor ledger and the explicit joined Gram

For \(\epsilon\in\{-,+\}\), put

\[
 r_q^-=m-q,\qquad r_q^+=m+q,\qquad
 N_q^\epsilon=\binom n{r_q^\epsilon}.
\]

Every lower-saturating token matching has exactly \(T\) flags at every
signed depth.  Write

\[
 {T\over N_q^\epsilon}=c_q^\epsilon+\theta_q^\epsilon,
 \qquad c_q^\epsilon=\left\lfloor{T\over N_q^\epsilon}\right\rfloor,
 \qquad0\le\theta_q^\epsilon<1.
 \tag{4.1}
\]

This includes the exceptional first upper rank: \(c_1^+=0\), and its
floor polynomial is simply \(\mu(\mu-1)\).

Fix arbitrary positive weights \(w_q^\epsilon\), and define

\[
 \mathcal Q_w(M)=
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}w_q^\epsilon
 \sum_{|R|=r_q^\epsilon}
 (\mu_{q,R}^\epsilon-c_q^\epsilon)
 (\mu_{q,R}^\epsilon-c_q^\epsilon-1).
 \tag{4.2}
\]

If \(f_{q,R}^\epsilon=\mu_{q,R}^\epsilon-T/N_q^\epsilon\), direct expansion
using \(\sum_Rf_{q,R}^\epsilon=0\) gives the exact identity

\[
 \boxed{
 \mathcal Q_w(M)=\|f(M)\|_w^2-\beta_w,
 \qquad
 \beta_w=\sum_{q,\epsilon}w_q^\epsilon
 N_q^\epsilon\theta_q^\epsilon(1-\theta_q^\epsilon).}
 \tag{4.3}
\]

The baseline is independent of the matching.

We now refine the interval bundles once more.  If two elementary
alternating components contain, respectively, a new token and an old
token carrying the same signed depth target, join them.  Do this for all
\(q\le H\), both signs, and take transitive closure together with the
interval joins of Section 3.  Call the final macro-bundles \(\mathscr K\).
Further joining leaves Theorem 3.1 unchanged.

For \(K\in\mathscr K\), set

\[
 \Delta_{K,q}^\epsilon(R)=
 \#\{e\in(M'\setminus M)\cap K:F_q^\epsilon(e)=R\}
 -\#\{e\in(M\setminus M')\cap K:F_q^\epsilon(e)=R\},
 \tag{4.4}
\]

and let \(z_K\) be this stacked vector with the weights from (4.2).
Write

\[
 Z=\sum_Kz_K=f(M')-f(M),\qquad
 A=\|Z\|_w^2,\qquad V=\sum_K\|z_K\|_w^2.
 \tag{4.5}
\]

For distinct bundles \(K,L\), define

\[
 C_{KL,q}^{\alpha\beta,\epsilon}
 =\#\{(e,g):e\in E_K^\alpha,\ g\in E_L^\beta,
             \ F_q^\epsilon(e)=F_q^\epsilon(g)\},
 \tag{4.6}
\]

where \(E^+=M'\setminus M\) and \(E^-=M\setminus M'\).
Here \(E_K^\alpha=E^\alpha\cap K\).

### Theorem 4.1 (computed joined-owner curvature)

For distinct final bundles, opposite-sign collision counts vanish:

\[
 C_{KL,q}^{+-,\epsilon}=C_{KL,q}^{-+,\epsilon}=0.
 \tag{4.7}
\]

Consequently

\[
 \boxed{
 \begin{aligned}
 A-V
 &=2\sum_{K<L}\langle z_K,z_L\rangle_w\\
 &=2\sum_{q,\epsilon}w_q^\epsilon
   \sum_{K<L}
   \left(C_{KL,q}^{++,\epsilon}+C_{KL,q}^{--,\epsilon}\right)
 \ge0.
 \end{aligned}}
 \tag{4.8}
\]

At the first lower depth the stronger componentwise cancellation holds:

\[
 \Delta_{K,1}^-(S)=0\qquad(K\in\mathscr K, S\in V_-).
 \tag{4.9}
\]

#### Proof

If a new token in \(K\) and an old token in \(L\) have the same flag
target, the defining closure joins \(K,L\).  Thus (4.7) holds when they
remain distinct.  Expanding the inner product of the signed incidence
vectors (4.4) now leaves precisely the two same-sign counts in (4.8).
They are nonnegative.

For (4.9), the old and new edge incident with a changed lower target \(S\)
belong to the same elementary alternating component, while
\(L_1(e)=S\) for both.  Their contributions cancel inside the same
bundle.  \(\square\)

The counts in (4.8) are literal pair-row counts, not unspecified owner
effects.  Using (1.4), for example, the lower equality tested in
\(C_{KL,q}^{\alpha\beta,-}\) is exactly

\[
 I_{\pi_e}(i_e+q-1,m-q)
 =I_{\pi_g}(i_g+q-1,m-q),
 \tag{4.10}
\]

and the upper equality is

\[
 I_{\pi_e}(i_e-1,m+q)
 =I_{\pi_g}(i_g-1,m+q).
 \tag{4.11}
\]

Thus (4.8) is an explicit collision census in the actual local rows.

### Corollary 4.2 (floor-exact nonexpansive Haar interpolation)

Choose each macro-bundle independently with probability \(1/2\), and
switch precisely the chosen bundles.  Then (0.4) holds.

#### Proof

If \(\eta_K\in\{0,1\}\) are independent fair bits, then

\[
 f(M_\eta)=f(M)+\sum_K\eta_Kz_K.
\]

Independence gives

\[
 \mathbb E\|f(M_\eta)\|_w^2
 ={\|f(M)\|_w^2+\|f(M')\|_w^2\over2}
  -{A-V\over4}.
\]

Subtract the common baseline (4.3) and apply (4.8).  \(\square\)

## 5. Exact proved boundary

The construction supplies the requested common base, keeps every mixed
corner physically clustered, and resolves the sign of its formerly
abstract joined-owner Gram.  It does not by itself give a quantitative
positive lower bound in (4.8): the final closure may produce one macro-
bundle, or distinct bundles may have no same-sign flag collision.  In that
case \(A=V\), and (0.4) is an equality when the two priority endpoints
have equal energy.

Accordingly the next exact statement is one of the following two
equivalent forms.

* Prove that whenever \(\mathcal Q_w(M)\) exceeds the permitted
  \(o(W)\) defect, some adjacent priority swap has a lower-energy endpoint.
* Or prove that for some adjacent swap the explicit same-sign census in
  (4.8) is quantitatively larger than the endpoint energy rise.

All matching, path-versus-cycle, floor, run-boundary, and negative
cross-Gram issues have been removed from that statement.
