# Independent audit: sparse-top SCD flag rounding and the single-SCD barrier

**Date:** 2026-08-03  
**Audited theorem:**  
MATH_THEOREM_SPARSE_TOP_SCD_FLAG_ROUNDING_AND_SINGLE_SCD_BARRIER_20260803.md  
**Audited theorem SHA256:**  
f1381955ea94b2c5d86ec3af682d168228e86379a3dc66dad98b954388af89d1

**Verdict:** PASS after one exact \(O(1)\) census correction and two
presentation repairs. The sparse-top exact residual construction is valid.
The one-SCD deletion barrier remains \(\Omega(W)\).

No computation or finite experiment is used.

## 1. Corrections made during the audit

Three issues were repaired in the theorem file.

1. The display of (0.2) contained a missing TeX backslash before
   \(\mathtt{quad}\).
2. The display of (0.5) contained the control byte \(0x08\) where
   \(\backslash\mathrm{bigl}\) was intended.
3. Section 3 counted the empty set as a strict-lower target on the unique
   symmetric chain starting at rank zero. The correct nonempty count on
   that chain is \(r-1\), not \(r\). The resulting minimum flag count
   differs from the displayed telescoping sum by a number
   \(\theta_r\in\{0,1\}\). This is \(O(1)\), hence \(o(W)\), and does not
   affect the asymptotic limit or linear deletion conclusion.

The boundary-anchor paragraph was also made semantically explicit: a
deleted anchor is only a proof certificate. It is not a target, marked
prefix, compiler cell, or unit of owner capacity.

## 2. Exact chunk census

Fix a rank block \(B_j\) and write \(s_j=\max B_j<r\). A symmetric chain
is saturated. If it meets any rank \(t\in B_j\), its starting rank is at
most \(t\), and therefore it also meets every rank from \(t\) through
\(s_j\). Hence

\[
 C[B_j]\ne\varnothing
 \quad\Longleftrightarrow\quad
 C\text{ meets rank }s_j.
\tag{2.1}
\]

Every rank-\(s_j\) set lies on exactly one SCD chain, and that set is the
unique maximum of the corresponding chunk. Thus the nonempty chunks with
block label \(j\) are in literal bijection with

\[
 \binom{[2r]}{s_j},
\tag{2.2}
\]

so their number is exactly \(\binom{2r}{s_j}\). Since the blocks are
disjoint, their maxima are distinct ranks and no chunk is counted under
two block labels.

The total number of chunks is therefore

\[
 \sum_j\binom{2r}{s_j}
 =W\sum_jp_{s_j}\le W.
\tag{2.3}
\]

This is consistent with the requested injection into \(W\) middle owners.

## 3. Uniform containment matching

A chunk whose top is an \(s\)-set \(S\) is adjacent to exactly

\[
 D_s=\binom{2r-s}{r-s}
\tag{3.1}
\]

rank-\(r\) owners. Give each such incidence weight \(1/D_s\). Every chunk
has total incident weight one.

A fixed owner \(T\) contains \(\binom r{s_j}\) possible tops belonging to
block \(j\). Its total incoming weight is therefore

\[
 \sum_j{\binom r{s_j}\over\binom{2r-s_j}{r-s_j}}
 =\sum_j{\binom{2r}{s_j}\over\binom{2r}{r}}
 =\sum_jp_{s_j}\le1.
\tag{3.2}
\]

The middle identity follows by expanding both binomial ratios:

\[
 {\binom r s\over\binom{2r-s}{r-s}}
 ={(r!)^2\over s!(2r-s)!}
 ={\binom{2r}s\over\binom{2r}r}.
\tag{3.3}
\]

For completeness, the fractional assignment proves Hall directly. For
any set \(X\) of chunks,

\[
 |X|
 =\sum_{C\in X}\sum_{T\supseteq\operatorname{top}(C)}w(C,T)
 \le\sum_{T\in N(X)}1
 =|N(X)|.
\tag{3.4}
\]

Hence an integral matching saturates every chunk. Every member of a chunk
is below its top and thus below its assigned owner. Since the chunk is an
inclusion chain, ordering the successive set differences realizes every
one of its members as a literal prefix. The owner assignment is injective,
and each flag has at most \(|B_j|\le d\) targets.

This verifies the complete named-target statement, not merely a rank
histogram.

## 4. Parity blocks partition the residual ranks

Set

\[
 a=\left\lceil{7\over8}\sqrt r\right\rceil,\qquad
 u=r-a-1.
\]

For each parity, write the distance from its top uniquely as
\(2q\), and then write \(q=jd+h\) with \(j\ge0\) and
\(0\le h<d\). This proves that

\[
 B_{0,j}=\{u-2(jd+h):0\le h<d\},
\]

and

\[
 B_{1,j}=\{u-1-2(jd+h):0\le h<d\},
\]

after omitting nonpositive ranks, form a disjoint partition of
\(\{1,\ldots,u\}\). Every block has at most \(d\) members and is contained
in one parity class, so no block contains adjacent ranks. Its maximum is,
respectively,

\[
 u-2jd\quad\text{or}\quad u-1-2jd.
\tag{4.1}
\]

## 5. Sparse-top asymptotic sum

For the two top ranks at index \(j\), the deviations below the middle
rank \(r\) are

\[
 x_{0,j}=a+1+2jd,\qquad
 x_{1,j}=a+2+2jd.
\tag{5.1}
\]

Since

\[
 {a\over\sqrt r}\longrightarrow {7\over8},
\qquad
 {d\over\sqrt r}\longrightarrow{\sqrt\pi\over2},
\tag{5.2}
\]

for every fixed \(j\),

\[
 {x_{\nu,j}\over\sqrt r}
 \longrightarrow {7\over8}+\sqrt\pi\,j
 \qquad(\nu=0,1).
\tag{5.3}
\]

The central-binomial local ratio therefore gives

\[
 {\binom{2r}{r-x_{\nu,j}}\over\binom{2r}{r}}
 \longrightarrow
 \exp\left[-\left({7\over8}+\sqrt\pi\,j\right)^2\right].
\tag{5.4}
\]

The domination used in the theorem is valid. For \(0\le x\le r\),

\[
 {\binom{2r}{r-x}\over\binom{2r}{r}}
 =\prod_{t=0}^{x-1}{r-t\over r+t+1}
 \le\exp\left(-{x^2\over r+x}\right)
 \le\exp\left(-{x^2\over2r}\right).
\tag{5.5}
\]

For all sufficiently large \(r\), (5.2) makes the right side at
\(x=x_{\nu,j}\) at most \(e^{-c(1+j)^2}\) for an absolute \(c>0\).
This is summable uniformly in \(r\), including the truncated tail where
the top rank becomes nonpositive. Dominated convergence gives

\[
 \lim_{r\to\infty}
 \sum_{j\ge0}\left(p_{u-2jd}+p_{u-1-2jd}\right)
 =
 2\sum_{j\ge0}
 \exp\left[-\left({7\over8}+\sqrt\pi j\right)^2\right].
\tag{5.6}
\]

The elementary strict bound in the theorem is correct:

\[
 2e^{-49/64}< {15\over16},
\tag{5.7}
\]

because the first four exponential-series terms give
\(e^{49/64}>32/15\). Also \(\sqrt\pi>7/4\), so the first exponent for
\(j\ge1\) exceeds \(441/64\), while successive squared exponents differ
by more than \(49/4\). Hence

\[
 2\sum_{j\ge1}e^{-(7/8+\sqrt\pi j)^2}
 <{2e^{-441/64}\over1-e^{-49/4}}<{1\over16}.
\tag{5.8}
\]

Thus the limit is strictly below one, and the strict sparse-top inequality
holds for all sufficiently large \(r\).

## 6. Arbitrary boundary deletion and anchor semantics

Before deletion, every named target of every rank in
\(J=\{1,\ldots,u\}\) appears in exactly one chunk, and the chunks are
assigned to distinct owners. Therefore deleting an arbitrary prescribed
family \(\mathcal B_s\subseteq\binom{[2r]}s\) removes exactly
\(|\mathcal B_s|\) rank-\(s\) targets and leaves multiplicity

\[
 \binom{2r}s-|\mathcal B_s|.
\tag{6.1}
\]

Deletion cannot create a repeated target, owner collision, or failure of
nesting. If the old top is deleted while lower members survive, the
already selected owner and its ordering still contain and realize all
surviving members. The old top is needed only to certify why that owner
was selected; it is not retained in the mathematical flag and consumes no
capacity. If every member is deleted, discarding the empty flag releases
its owner.

Thus Corollary 1.2 is valid for arbitrary named deletion families within
the residual rank set \(J\), with no hidden anchor charge.

## 7. Exact one-SCD flag census

Let

\[
 c_j=\binom{2r}j-\binom{2r}{j-1}
\]

be the number of SCD chains beginning at rank \(j\). For \(j\ge1\), such a
chain has \(r-j\) nonempty strict-lower members. The unique \(j=0\) chain
has \(r-1\), because rank zero is empty.

Temporarily count the empty set on that root chain. The minimum number of
capacity-\(d\) flags needed without cross-chain merging is

\[
 \widetilde Q_r
 =\sum_{j=0}^r c_j\left\lceil{r-j\over d}\right\rceil.
\tag{7.1}
\]

Using

\[
 \left\lceil{L\over d}\right\rceil
 =\sum_{h\ge0}\mathbf1_{\{L>hd\}},
\]

and telescoping the \(c_j\),

\[
\begin{aligned}
 \widetilde Q_r
 &=\sum_{h\ge0}
   \sum_{0\le j\le r-hd-1}
   \left(\binom{2r}j-\binom{2r}{j-1}\right)\\
 &=\sum_{h\ge0}\binom{2r}{r-hd-1}.
\end{aligned}
\tag{7.2}
\]

Removing the empty set changes only the root-chain ceiling and hence

\[
 Q_r=\widetilde Q_r-\theta_r,\qquad
 \theta_r\in\{0,1\}.
\tag{7.3}
\]

For each fixed \(h\), the deviation is \(hd+1\), so

\[
 {\binom{2r}{r-hd-1}\over W}
 \longrightarrow e^{-\pi h^2/4}.
\tag{7.4}
\]

The same Gaussian domination as in Section 5 gives

\[
 {Q_r\over W}\longrightarrow
 \sum_{h\ge0}e^{-\pi h^2/4}
 >1+e^{-\pi/4}>1.
\tag{7.5}
\]

The correction \(\theta_r/W\) vanishes. Choose any fixed \(c_0>0\) smaller
than one quarter of the positive gap in (7.5). Then

\[
 Q_r\ge(1+2c_0)W
\]

for all sufficiently large \(r\).

If \(z_C\) targets are deleted from chain \(C\), its required number of
flags is \(\lceil(L_C-z_C)/d\rceil\), at least
\(\lceil L_C/d\rceil-z_C\). Summing over chains shows that \(z\) total
deletions reduce the required flag count by at most \(z\). Fitting the
remainder into at most \(W\) flags therefore forces

\[
 z\ge Q_r-W\ge2c_0W.
\tag{7.6}
\]

After weakening the constant, the asserted \(\Omega(W)\) barrier follows.
No adjacent-rank restriction was used.

## 8. Scope checks

1. The sparse-top theorem covers exactly the residual ranks
   \(1,\ldots,r-a-1\). It does not attach the top collar
   \(r-a,\ldots,r-1\).
2. The one-SCD barrier concerns the complete nonempty strict-lower ideal.
   It does not contradict the exact residual theorem, which deliberately
   leaves the collar unassigned.
3. The containment matching supplies one owner ordering per flag, but it
   does not serialize the owners into one physical word, prove upper-deck
   coverage, or solve the common-cap compiler.
4. The remaining collar attachment must respect both containment below
   the selected collar bottom and residual-plus-collar capacity. Those
   correlations are absent from the owner-only matching in Theorem 1.1.
5. The barrier forbids only refinements of one fixed SCD. Cross-SCD
   splicing, alternating exchanges, and a joint collar/residual matching
   remain live.

Within these boundaries, the theorem and its repaired proof are valid.
