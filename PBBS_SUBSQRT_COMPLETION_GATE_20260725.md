# A sub-square-root ambient-completion gate for coefficient one

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The corrected linear-seam ledger needs only

\[
 \nu_{\lceil A\sqrt r\rceil}(P_r)=o_A(B_r\sqrt r),
 \qquad B_r=\operatorname{Cat}_r,
\tag{0.1}
\]

or equivalently the quotient estimate

\[
 \overline\nu_{\lceil A\sqrt r\rceil}
 =o_A(B_r/\sqrt r).
\tag{0.2}
\]

Consequently the ambient-completion criterion for simple fixed-core
sectors does not need the formerly proposed pointwise \(O_A(1)\) tail
load.  The strictly weaker estimate

\[
 \boxed{\sup_X\Lambda_X(\mathcal P)=o_A(\sqrt r)}
\tag{SC_A}
\]

for every projected-edge-disjoint simple-sector family already proves
coefficient one.

This note proves that implication exactly.  It also shows that every
fixed, and indeed every \(o(\sqrt r)\), collection of the first core-tail
layers contributes only \(o(\sqrt r)\).  Thus a counterexample to
\((SC_A)\) must place its congestion in growing, genuinely mixed-core
completion layers.  The mixed-core estimate is not proved here.

## 1. The exact completion load

Let \(N=2r+1\).  A simple sector of step-two residence at most
\(H=\lceil A\sqrt r\rceil\) has active halves

\[
 Z=U\mathbin{\dot\cup}A,
 \qquad |U|=s,\quad |A|=s+1,
\]

and cores \(K,K'\) of common size \(q=r-s\).  Choose independent uniform
orders of \(K,K'\) and complete the open sector to an ambient wreath.

For a middle vertex \(X\), let \(\Lambda_X(\mathcal P)\) be the expected
number of these completed wreaths which contain \(X\), summed over
\(I\in\mathcal P\).  The exact kernel is

\[
 \begin{aligned}
 \Lambda_X(\mathcal P)={}&
 \#\{I:X\text{ is in the fixed open segment of }I\}\\
 &+\sum_{I:X\cap Z_I=A_I}
 {1\over\binom{q_I}{i_I}\binom{q_I}{i_I-1}}\\
 &+\sum_{I:X\cap Z_I=U_I}
 {1\over\binom{q_I}{i_I}^2},
 \end{aligned}
\tag{1.1}
\]

with the endpoint conventions from the audited completion law.  The
fixed open term is at most four.

## 2. Sub-square-root congestion implies the linear-seam target

### Theorem 2.1

Assume that for every fixed \(A>0\), every projected-edge-disjoint family
\(\mathcal P\) of simple physical PBBS sectors of residence at most
\(\lceil A\sqrt r\rceil\) satisfies

\[
 \sup_{X\in\binom{[N]}r}\Lambda_X(\mathcal P)
 =o_A(\sqrt r).
\tag{2.1}
\]

Then

\[
 \nu_{\lceil A\sqrt r\rceil}(P_r)=o_A(B_r\sqrt r),
\tag{2.2}
\]

and hence the contiguous-OR coefficient-one theorem follows from the
corrected linear-seam reduction.

#### Proof

Every completed wreath contains exactly \(N\) middle vertices.  Double
counting expected sector--vertex incidences gives

\[
 N|\mathcal P|
 =\sum_{X\in\binom{[N]}r}\Lambda_X(\mathcal P)
 \le \binom Nr\sup_X\Lambda_X(\mathcal P).
\tag{2.3}
\]

Since \(\binom Nr=NB_r\), (2.1) gives

\[
 |\mathcal P|=o_A(B_r\sqrt r).
\tag{2.4}
\]

Every projected-edge-disjoint return family contains a simple-return
subfamily of at least half its size.  Therefore the same little-oh bound,
up to the harmless factor two, holds for the unrestricted physical
packing number.  This is (2.2).  The established linear-seam theorem then
gives coefficient one. \(\square\)

Thus the former bounded-congestion conjecture was stronger than necessary
by a full factor \(\sqrt r\).

## 3. Both endpoint windows of \(o(\sqrt r)\) layers are harmless

Fix \(X\), put \(q_*=r-H\), and allow all sector sizes \(s\le H\)
simultaneously.  For the even-tail kernel at index \(i\), endpoint
throughput and the exact Johnson-level count give

\[
 |\mathcal P_i^E(X)|
 \le4\binom r{i-1}\binom{r+1}i.
\tag{3.1}
\]

The factor four allows shared endpoints.  Since \(q_I=r-s_I\ge q_*\)
and \(\binom qi\) is increasing in \(q\) for fixed \(i\), its weighted
contribution is at most

\[
 4R_i^E(r,q_*),\qquad
 R_i^E(r,q_*)=
 {\binom r{i-1}\binom{r+1}i
  \over\binom {q_*}{i-1}\binom {q_*}i}.
\tag{3.2}
\]

The analogous first-side odd-tail bound is

\[
 4R_i^O(r,q_*),\qquad
 R_i^O(r,q_*)=
 {\binom ri\binom{r+1}i\over\binom {q_*}i^2}.
\tag{3.3}
\]

### Lemma 3.1

Let \(K=K(r)=o(\sqrt r)\).  Uniformly for

\[
 H\le A\sqrt r,\qquad q_*=r-H,\qquad1\le i\le K,
\]

one has

\[
 R_i^E(r,q_*)+R_i^O(r,q_*)=O_A(1).
\tag{3.4}
\]

Consequently all indices \(1\le i\le K\), over both displayed tail
types, contribute \(o_A(\sqrt r)\) to \(\Lambda_X\).

#### Proof

For \(0\le j\le K\),

\[
 {\binom rj\over\binom {q_*}j}
 =\prod_{a=0}^{j-1}{r-a\over r-H-a}.
\tag{3.5}
\]

Because \(H=O_A(\sqrt r)\) and \(j=o(\sqrt r)\),

\[
 \log {\binom rj\over\binom {q_*}j}
 \le C_A\left({j\over\sqrt r}+{j^2\over r}\right)=o_A(1)
\tag{3.6}
\]

uniformly.  Replacing \(r\) by \(r+1\) changes only the constant.
Substitution in (3.2)--(3.3) proves (3.4).  Summing \(O_A(1)\) over
\(K=o(\sqrt r)\) indices proves the last assertion. \(\square\)

There is an exact symmetric charge at the opposite boundary.  Put
\(k=q_I-i_I\).

For an even-tail occurrence, \(X\cap Z=A\) and
\[
 |X\cap K|=k,\qquad |X\cap K'|=q-k-1.
\tag{3.7}
\]
The initial fixed open owner is
\[
 A_0=K\cup U,
\]
and therefore
\[
 |X\cap A_0|=k.
\tag{3.8}
\]
Endpoint throughput bounds the number of such sectors by
\[
 4\binom rk\binom{r+1}{k+1}.
\tag{3.9}
\]
Their common kernel weight is
\[
 {1\over\binom qk\binom q{k+1}}.
\tag{3.10}
\]

For an odd-tail occurrence, \(X\cap Z=U\) and
\[
 |X\cap K|=q-k.
\]
Hence the same initial owner satisfies
\[
 |X\cap A_0|=r-k,
\]
so the number of sectors is at most
\[
 4\binom rk\binom{r+1}k,
\tag{3.11}
\]
while the kernel weight is \(1/\binom qk^2\).

Exactly the estimate (3.5)--(3.6), now with \(j=k\), proves:

### Corollary 3.2 (two-sided endpoint disposal)

For every \(K=o(\sqrt r)\), the total completion load from odd-tail
sectors with
\[
 \min\{i_I,q_I-i_I\}\le K
\tag{3.12}
\]
and even-tail sectors with

\[
 \min\{i_I-1,q_I-i_I\}\le K
\tag{3.12a}
\]

is \(o_A(\sqrt r)\), uniformly in \(X\).

The choice of endpoint is essential.  Charging the far-end indices to the
terminal owner introduces one unnecessary Johnson-level factor of order
\(r\); charging them to \(A_0\) gives the matching pair of binomial
denominators in (3.10)--(3.11).

There is also a quantitative fixed-\(\varepsilon\) form.  For
\(K=\lfloor\varepsilon\sqrt r\rfloor\), the proof of (3.6) gives

\[
 \boxed{
 \Lambda_X^{\rm end}(\varepsilon)
 \le C_A\varepsilon
       e^{C_A(\varepsilon+\varepsilon^2)}\sqrt r.
 }
\tag{3.13}
\]

Thus, after normalizing by \(\sqrt r\), the two endpoint windows can be
made arbitrarily small by first choosing \(\varepsilon\downarrow0\).

## 4. Exact remaining subproblem

By Theorem 2.1 and Corollary 3.2, coefficient one follows if one proves that,
uniformly over fixed \(A\), fixed middle vertices \(X\), and
projected-edge-disjoint simple PBBS sectors, the contribution from the
genuinely mixed-core indices.  More precisely, it is enough to prove,
for every fixed \(\varepsilon>0\), that the contribution from

\[
 \min\{i_I,q_I-i_I\}\ge\varepsilon\sqrt r
\]

in the odd kernel and

\[
 \min\{i_I-1,q_I-i_I\}\ge\varepsilon\sqrt r
\]

in the even kernel is

\[
 \boxed{o_A(\sqrt r).}
\tag{4.1}
\]

Every contributing sector is an alternating omitted-label segment across
\((X,X^c)\).  Equivalently, its two owner parities are opposite unit-slope
monotone staircases in the scalar process

\[
 h_X(Y)=|X\cap Y|.
\]

Thus (4.1) is a sub-square-root weighted packing theorem for paired
monotone PBBS staircases.  The local tiled-sector construction shows that
the required little-oh cannot follow from fixed-core geometry and
edge-disjointness alone.  It must exploit the canonical PBBS chronology
of the staircase starts.

Conversely, if \((SC_A)\) fails, then (3.13) implies a saturation
localization: there are constants \(\varepsilon,\delta>0\), middle
vertices \(X_r\), and packed simple sectors with

\[
 \min\{i_I,q_I-i_I\}\ge\varepsilon\sqrt r
\]

in the odd case (with the shifted even analogue) whose total
reciprocal-binomial completion load is at least
\(\delta\sqrt r\).  Hence no boundary-core phenomenon can obstruct the
new gate; every obstruction is macroscopically mixed in both cores.

## 5. Status

Proved:

* sub-square-root, rather than bounded, completion congestion is enough;
* \(o(\sqrt r)\) layers at **both** core boundaries are automatically
  harmless.

Unproved:

* the mixed-core tail estimate (4.1);
* the equivalent vanishing improvement over reciprocal-height trace
  saturation;
* coefficient one.
