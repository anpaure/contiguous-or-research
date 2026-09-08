# Audit of adjacent-priority LONG-BLOCK contraction

Date: 2026-07-25

Audited source:
MATH_ATTACK_W_ADJACENT_PRIORITY_LONG_BLOCK_CONTRACTION_20260725.md.

## 1. Verdict

The central and row-geometric core is correct.  In particular:

1. the affected-domain formula and its \(j=1\) constant are exact;
2. the generic alternating paths/cycles and the one-cut path state space
   are classified correctly;
3. the exact \(j=1\) common-owner count and \(p_1=R_m\) are correct;
4. same-orientation transport has singleton lower components and permits
   arbitrary block signs;
5. reverse transport has exactly one open exchange path per maximal
   physical changed interval;
6. both advertised two-boundary row estimates are valid; and
7. the positive-Gram contraction identity for same-orientation transport
   has the stated factor \(4\) in raw-square normalization.

Four corrections are required.

* All proper-window orthogonality and collar theorems must assume
  \(H\le m-2\), not \(H\le m-1\).
* A plus sign is missing in each of (5.6) and (5.7).
* The generic-interlacing example is an abstract obstruction to deduction
  from the current hypotheses, not a proved realization by exact local
  factors.
* The final literal-scope paragraph must distinguish “the same number of
  unused owners” from “the same unused owner set,” and distinguish
  unconditional \(W+o(W)\) literal skeleton length from the still
  conditional target-defect repair.

There is also a strengthening: for the same-orientation pair-symmetric
choice \(F_B=\tau F_A\), the two coherent endpoints have equal weighted
energy automatically, rank by rank.  A globally \(\tau\)-invariant
background is not needed.  Thus the \(p=1/2\) descent (5.11) is
unconditional within that factor class.

## 2. Central component audit

Let

\[
 \mathcal D_j=\{S:|S|=m-1,\ S\subseteq R,\ 
                    S\cap P_h\ne\varnothing\ (h<j)\}.
\]

The adjacent priority swap changes exactly these lower targets.  Deleting
the four coordinates of \(A\cup B\) and applying inclusion-exclusion to
the \(j-1\) earlier pairs gives

\[
 |\mathcal D_j|
 =\sum_{t=0}^{j-1}(-1)^t\binom{j-1}{t}
   \binom{2m-3-2t}{m-1}.
\]

For \(j=1\),

\[
 |\mathcal D_1|=\binom{2m-3}{m-1}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}W.
\]

These formulas and constants check.

For arbitrary endpoint owner injections \(f_A,f_B\), every common owner
avoids both \(A,B\).  The two-coloured overlay is therefore a union of
even paths with middle endpoints and even cycles.  Writing \(u_i=1\) for
the \(A\)-edge on a path, middle simplicity gives

\[
 u_i\ge u_{i+1}.
\]

Hence a path state is exactly \(1^r0^{k-r}\), while cyclic inequalities
force a constant cycle state.  This classification is necessary and
sufficient.

The path count is

\[
 p_j=|\mathcal D_j|
   -|f_A(\mathcal D_j)\cap f_B(\mathcal D_j)|.
\]

For \(j=1\), every \(m\)-set \(Y\subseteq R\) occurs in both images.  In
the unique \(F_A\)-occurrence of \(Y\), its predecessor lower window is a
facet of \(Y\), hence belongs to \(\mathcal D_1\); the same holds for
\(F_B\).  Conversely a common owner lies in \(R\).  Thus

\[
 |f_A(\mathcal D_1)\cap f_B(\mathcal D_1)|
 =\binom{2m-3}{m}
 =\frac{m-2}{m}|\mathcal D_1|
\]

and

\[
 p_1=\frac2m|\mathcal D_1|=R_m.
\]

The count is independent of the choice of local factors.

The source should, however, replace “can be arbitrarily interlaced” by:

> No exchange-order/physical-order alignment follows from the current
> endpoint run and component-count hypotheses; the abstract interlacing
> example shows that such data alone are insufficient.

No exact-factor realization of the extreme abstract interlacing was
proved.

## 3. Same-orientation transport

With \(F_B=\tau F_A\) in the same orientation,

\[
 f_B(S)=\tau f_A(S).
\]

If \(f_A(S)=f_B(T)\), the common owner avoids both swapped pairs and is
\(\tau\)-fixed.  Injectivity of \(f_A\) then gives \(S=T\).  Thus every
affected component has one lower vertex: a parallel two-cycle when its
owner lies in \(R\), otherwise a two-edge path.  Arbitrary tokenwise and
hence arbitrary blockwise choices are exact central matchings.

An alternative changed edge cannot collide with a common unchanged edge:
that alternative edge occurs in one coherent endpoint together with every
common edge, and that endpoint is a matching.  This observation should be
made explicit when passing from the affected overlay to the full matching.

The row estimate

\[
 J(M_\varepsilon)\le J(M_A)+2|\mathscr B|
\]

is correct.  One selected block removes one interval in an \(F_A\)-row and
inserts one in the paired \(F_B\)-row.  The block-count and asymptotic
consequences in (3.5)--(3.7) follow.

For \(q\le m-2\), distinct starts in one row have distinct proper upper
windows.  The token innovations

\[
 d_{i,q}=\mathbf e_{\tau U_{i,q}}-\mathbf e_{U_{i,q}}
\]

satisfy

\[
 \langle d_i,d_k\rangle_w
 =2\sum_qw_q^+
   {\bf1}_{\{U_{i,q}=U_{k,q},\ U_{i,q}\cap B\ne\varnothing\}}
 \ge0.
\]

Within one physical block the cross terms vanish.  Therefore

\[
 \|D\|_w^2-\sum_C\|D_C\|_w^2
 =4\mathcal C_{A,B},
\]

and the raw-square identity (5.4), including its coefficient \(4\), is
correct.

The proof displays (5.6)--(5.7) without addition signs.  They must read

\[
 \mathbb E Q_w(M_p)
 =\|\bar\mu-\lambda\|_w^2
 +p(1-p)\sum_C\|D_C\|_w^2,
\]

\[
 (1-p)Q_w(M_A)+pQ_w(M_B)
 =\|\bar\mu-\lambda\|_w^2
 +p(1-p)\|D\|_w^2.
\]

The final formula (5.4) already uses these corrected identities.

## 4. Automatic endpoint-energy equality

For the same-orientation coupling, \(Q_w(M_A)=Q_w(M_B)\) is automatic
for weights constant on every signed rank.

* The changed lower flags are subsets of the pointwise fixed lower target
  \(S\subseteq R\), so the complete lower load vector is unchanged.
* Middle loads are injective in both endpoints, so their square/factorial
  energies agree.
* At an upper rank, first-avoided phase residence separates earlier phases,
  the \(A/B\) stratum, and later phases into disjoint target supports.
* Inside the unchanged part of the \(A/B\) stratum, every
  avoid-\(A\)/meet-\(B\) token is paired by \(\tau\) with an
  avoid-\(B\)/meet-\(A\) token.  Its aggregate load is therefore
  \(\tau\)-invariant.
* The changed \(\mathcal D_j\)-load is carried from \(a\) to \(\tau a\).

Thus the whole \(A/B\) upper stratum is permuted by \(\tau\), while all
other strata are fixed and target-disjoint.  The endpoint energy is equal
rankwise.  This is also the content of Theorem 3.1 in
PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md.

Consequently the source's global-background condition after Corollary 5.2
is sufficient but unnecessarily strong.  Within the stated
pair-symmetric first-avoided construction one may take \(p=1/2\) and obtain

\[
 Q_w(M_*)\le Q_w(M_A)-\mathcal C_{A,B}.
\]

This remains only an activated-collar descent; it does not imply that
\(\mathcal C_{A,B}\) controls the total defect.

## 5. Reverse path converse and row count

Under opposite orientation,

\[
 f_A(S_i)=X_{i-1},\qquad f_B(S_i)=\tau X_i.
\]

If \(S_i,S_{i+1}\in\mathcal D_j\), then

\[
 X_i=S_i\cup S_{i+1}\subseteq R,
\]

so \(f_B(S_i)=X_i=f_A(S_{i+1})\).

Conversely, if \(\tau X_t=X_{s-1}\), the common set avoids both
\(A,B\), hence is fixed by \(\tau\).  Exact-factor uniqueness of every
middle window gives \(s=t+1\) in the same row.  Thus different physical
changed intervals cannot join.  A full changed cyclic row is impossible
because its lower windows would all avoid the two \(B\)-coordinates.
Every component is therefore exactly one open physical interval path.

The legal states are its old-prefix/new-suffix thresholds.  Relative to
the all-old endpoint, a threshold removes one suffix interval from the
old row and inserts one interval in the reversed transported row.  Hence

\[
 J(M_{\mathbf c})\le J(M_A)+2K_j
 \le J(M_A)+4jR_m.
\]

For \(j=1\), the two \(B\)-coordinates split the remaining
\(2m-3\) coordinates into arcs whose lengths sum to \(2m-3\).  Exactly
one arc has length at least \(m-1\), so there is exactly one nonempty
changed interval per row.  The claims

\[
 K_1=R_m,\qquad |\mathcal D_1|/R_m=m/2
\]

and the short-path bound (6.6) are correct.

## 6. Top-depth correction

The proper-window arguments require

\[
 \boxed{H\le m-2.}
\]

At \(q=m-1\), the upper window has length

\[
 m+q=2m-1=L
\]

and is the full local ground set at every start.  For a block \(K\),

\[
 z^+_{K,m-1}
 =|K|\bigl(\mathbf e_{Q_B}-\mathbf e_{Q_A}\bigr),
\qquad
 \|z^+_{K,m-1}\|_2^2=2|K|^2.
\]

Thus:

* same-row block orthogonality (4.4)--(4.5) fails at this depth;
* the curvature formula (5.8) counts internal block duplicates unless it
  is modified;
* the reverse bound \(\|z^+_{K,q}\|_2^2\le6q+2\) fails; and
* the claim that every innovation coordinate is \(0,\pm1\) fails.

The Gaussian/product-tail applications have \(H\ll m\), so replacing every
exact theorem scope by \(H\le m-2\) causes no asymptotic loss.

For \(q\le m-2\), the reverse formulas

\[
 z^-_{K,q}=E_{m-q}(K)-E_{m-q}(K+q-1),
\]

\[
 z^+_{K,q}=\tau E_{m+q}(K-q)-E_{m+q}(K-1)
\]

and the constants \(2(q-1)\), \(6q+2\), \(8q\), and \(4H(H+1)\) all
check.  The all-path estimate (7.9) and the corrected variance constant in
(7.11) also check.

## 7. Midpoint and literal scope

The path midpoint theorem is correct: a legal path word has
\(u_1\ge\cdots\ge u_k\); if every marginal is \(1/2\), then each
nonnegative difference has expectation zero, so all bits agree almost
surely.  The only such law is the fair endpoint coin.

The invariant-sector observations are correct as linear-algebra
statements.  The conclusion should be phrased as:

> Total energy alone cannot yield a descent theorem without an additional
> bound on its invariant projection or a charged-coverage theorem.

No exact-factor example concentrating arbitrary energy entirely in that
projection is supplied, so “impossible” should not be read as a separate
realizability theorem.

Every child has \(T=\binom n{m-1}\) selected tokens and \(T\) distinct
middle owners.  It therefore leaves the same **number**

\[
 W-T=\frac{2W}{m+2}
\]

of middle owners unused, but generally not the same unused set as either
endpoint.

The literal length ledger itself is unconditional.  The selected physical
runs cost

\[
 T+O(HJ),
\]

and adding isolated genuine flags for the \(W-T\) unused owners costs
\(O(H(W-T))\).  Thus

\[
 W+O\bigl(HJ+HW/m\bigr)=W+o(W)
\]

whenever \(J=o(W/H)\) and \(H=o(m)\).  What remains conditional on
multidepth defect \(o(W)\) is the target-repair/coverage conclusion and
hence constant one, not the existence or length of this literal skeleton.

## 8. First-upper reverse pair floor

The companion claim in
PAIR_OMISSION_REVERSE_LONG_BLOCK_SHADOW_ROUNDING_20260725.md also checks.
At \(q=1\), only the two collar coordinates outside \(S_i\) can meet \(B\).
Each \(B\)-coordinate occupies one of those two slots for at most two starts
per row, so at most

\[
 E_1\le4R_m
\]

old first-upper occurrences are movable anywhere in the reverse path cube.

Let \(\mu\) be the all-old load and let two corners remove respectively
\(d_0(T),d_1(T)\) old occurrences at target \(T\).  Additions only increase
the two-cover load, while

\[
 \sum_Td_h(T)\le E_1.
\]

For

\[
 \beta(u)=\left\lfloor\frac{(u-1)^2}{4}\right\rfloor
\]

one has \(\beta(u)\ge u/2-1\).  Therefore

\[
 \sum_T\beta(\mu^0(T)+\mu^1(T))
 \ge\sum_T(\mu(T)-1)_+
  -\frac12\sum_T(d_0(T)+d_1(T))
 \ge C_1(M_A)-E_1.
\]

The sharp correction is consequently \(-4R_m\), not \(-8R_m\).  This
first-upper floor obstruction is valid.
