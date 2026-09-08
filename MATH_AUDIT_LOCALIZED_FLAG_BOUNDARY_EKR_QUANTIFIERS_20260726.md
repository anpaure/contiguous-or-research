# Audit of the localized flag-boundary physical EKR theorem

Date: 2026-07-26

Audited files:

* `MATH_THEOREM_LOCALIZED_FLAG_BOUNDARY_ADAPTIVE_KERNEL_HIGH_COVER_EKR_20260726.md`;
* `MATH_THEOREM_FLAG_COMPRESSED_PHYSICAL_PORT_EKR_AND_HOLONOMY_GATE_20260726.md`;
* `MATH_AUDIT_KZ_SPREAD_APPROXIMATION_PHYSICAL_PORT_HIGH_COVER_20260726.md`;
* `MATH_THEOREM_PHYSICAL_PORT_EKR_HIGH_COVER_REDUCTION_20260726.md`.

## 0. Verdict

The localized theorem is valid under its displayed hypotheses.  In
particular, its Theorem A really proves, for one simultaneous exactly
target-regular port outcome,

\[
 \mathcal F\text{ pairwise intersecting and not contained in a target
 star}
 \quad\Longrightarrow\quad
 |\mathcal F|=o(D_1/\sqrt m).
\tag{0.1}
\]

Consequently, for every nonnegative weight vector supported on such a
family,

\[
 \sum_{C\in\mathcal F}y_C
 \le o(D_1/\sqrt m)\max_{C\in\mathcal F}y_C.
\tag{0.2}
\]

The earlier conclusion that global selected-port chart resolution remains
open is therefore obsolete as a statement about the **EKR/clique gate**.
The literal port-hole and chart-holonomy examples in that earlier file are
correct, but they obstruct only the particular flag-closure/gluing proof.
The localized proof does not assume selected flag closure and does not
transport charts around cycles.

This does **not** prove the fractional edge-colouring inequality for
arbitrary weighted supports.  The remaining gate is non-clique matching
decomposition, not high-cover EKR.

## 1. Why the two notes do not contradict one another

The older flag-compressed proof required a certificate closure
\(Q_\sigma\) contained in every selected edge of its link.  Exact
targetwise thinning need not preserve that closure, and three strips can
have nontrivial chart holonomy.  Those counterexamples remain literal.

The newer proof uses, for a co-occurring target label \(A\), only the
set-theoretic Boolean envelope

\[
 \mathcal B(A)=\{T:I(A)\subseteq T\subseteq U(A),\ 
                    m-H\le |T|\le m+H\}.
\tag{1.1}
\]

It never asserts \(\mathcal B(A)\subseteq e_C^\#\) for an edge containing
\(A\).  Instead:

1. \(|\mathcal B(A)|\le2^{\operatorname{sp}(A)}\);
2. if this set is smaller than the cover number of \(\mathcal F\), there
   is a witness edge \(E_A\in\mathcal F\) with
   \(e_{E_A}^\#\cap\mathcal B(A)=\varnothing\);
3. every actual collision target between the current branch and \(E_A\)
   is therefore **outside** the envelope and pays the conditional kernel.

Thus a zero-generator omission inside a raw chart never has to be
absorbed, and charts belonging to different nodes never have to be
identified.  This is a genuine bypass of PHCR, not an implicit proof of
PHCR.

## 2. Audit of the raw off-envelope kernel

Fix feasible nonempty \(A\), and write

\[
 I=\bigcap A,\qquad U=\bigcup A,\qquad Q=U\setminus I,
 \qquad |Q|=s.
\]

The group

\[
 G=\operatorname{Sym}(I)\times\operatorname{Sym}([2m]\setminus U)
\]

fixes every target in \(A\), not merely its rank: every member of \(A\)
contains all of \(I\), excludes all of \([2m]\setminus U\), and is
determined on the pointwise-fixed set \(Q\).  Hence the raw link of
\(A\) is \(G\)-invariant.

For \(T\notin\mathcal B(A)\), the two external defect counts

\[
 a=|I\setminus T|,\qquad b=|T\setminus U|
\]

are not both zero, and its orbit has exactly

\[
 \binom{|I|}{a}\binom{2m-|U|}{b}
\]

members.  The orbit double count in Lemma 2.1 is therefore exact.

The three cases used in summing a packet are exhaustive.

* If \(a=0,b=r\ge1\), then, after fixing \(T\cap Q\), a target of one
  witness strip is a fixed-length cyclic interval containing a fixed
  nonempty active subset with at most \(r\) slack positions.  There are
  at most \(r+1\) placements.  The band equations give
  \(r\le2H+s<h-H\), so the active-disjoint case cannot occur here.
  Complementation handles \(b=0,a=r\).
* If \(a,b\ge1\) and the active intervals overlap, the cyclic pair
  numerator is at most two, while both orbit factors are at least
  \(M_s=m-H-s\).
* In the active-disjoint case, cyclic geometry gives
  \(a,b\ge h-H-s\), producing the displayed superpolynomial tail.

Thus, for a packet \(P\) of at most \(K'\) targets from one raw strip,

\[
 \sum_{T\in P}\frac{d_0(A,T)}{d_0(A)}\le\eta_s(K')
\tag{2.1}
\]

whenever \(P\cap\mathcal B(A)=\varnothing\).  Importantly, (2.1) is a
sum of conditional link degrees; no independence among the targets in
\(P\) is asserted or needed.

## 3. Audit of selected-port conditioning

At each nonmiddle target, a uniform fixed-size set of incident strips is
selected, independently between distinct targets.  For fixed \(A\), the
indicators

\[
 Z_C(A)=\prod_{T\in A}X_{C,T}
\]

are negatively associated as \(C\) varies.  This follows from the
standard closure properties actually needed here:

1. fixed-size sampling is negatively associated;
2. independent unions of negatively associated coordinate families are
   negatively associated; and
3. coordinatewise increasing functions of disjoint coordinate blocks
   preserve negative association.

The coordinate blocks used by distinct strips are disjoint even though
the variables inside one target star are dependent.  Hence the lower and
upper Chernoff bounds used in Section 3 apply.

Every feasible target set of size at most four is a subset of the raw
target set of at least one strip.  Therefore

\[
 M\sum_{j=1}^{4}\binom{2h(2H+1)}j
\]

is a valid overcount for all labels requiring concentration.  The lower
mean bound applies to every bounded-span label, including mixed middle
and nonmiddle labels; using \(\theta_*^4\) is conservative.  Under (3.7)
its failure exponent dominates the logarithm of this catalogue.  The
additive upper-tail cutoff

\[
 \Lambda=C_1(\log M+hH)
\]

similarly makes all upper-link failures summable.

It follows that one port outcome can satisfy simultaneously:

* exact target degrees;
* the width bound;
* the all-order selected-codegree profile;
* the earlier pair and off-edge-star estimates; and
* the localized conditional kernel for **every** bounded-span label and
  every witness strip.

This last universal quantifier is what licenses adaptive witness choices:
the witnesses may depend on the realized port outcome and on the entire
previous branch history.

## 4. Audit of bounded span versus arbitrary span

The proof does not extrapolate the fixed-span kernel to large span.  It
stops large-span links.

Set

\[
 B=\frac{D}{mK^4},\qquad
 s_0=\left\lceil\frac{\log(4mK^4)}{\log(1/\alpha)}\right\rceil.
\]

The all-order selected-codegree estimate

\[
 d^\#(A)\le2D\alpha^{\operatorname{sp}(A)}+\Lambda
\]

and \(\Lambda\le B/2\) imply

\[
 d^\#(A)>B\quad\Longrightarrow\quad
 \operatorname{sp}(A)\le s_0.
\tag{4.1}
\]

For \(K=O(h\sqrt m)\), \(h=o(m^{7/8})\), and \(h=o(m)\), one has
\(s_0\le64\) eventually.  Thus the conditional kernel is invoked only
with one fixed choice \(s_*=64\).  Nodes of larger span have full-link
capacity at most \(B\) and are included in the stopped-node ledger.

This validates the transition from arbitrary labels to a bounded-span
calculation.  No hidden uniformity in a growing span parameter is used.

## 5. Audit of the adaptive four-level tree

Choose \(E_\varnothing\in\mathcal F\).  Assign every member of
\(\mathcal F\) to one selected target in its intersection with
\(E_\varnothing\).  The sum of full-link capacities of the depth-one
labels is at most \(KD\).

At an active node \(A\):

* (4.1) gives \(\operatorname{sp}(A)\le s_0\);
* \(|\mathcal B(A)|\le2^{s_0}<\tau(\mathcal F)\) supplies a witness
  \(E_A\) disjoint from the entire envelope;
* pairwise intersection ensures that every edge in the current branch
  meets \(E_A\);
* assigning an actual collision target \(T\in e_{E_A}^\#\) sends the
  branch to the link of \(A\cup\{T\}\); and
* because \(T\notin\mathcal B(A)\), the selected localized kernel bounds
  the **sum of all full child-link capacities**, even though different
  nodes use different witnesses.

Expansions occur only for labels of sizes one, two, and three, exactly
the range covered by the simultaneous kernel.  With

\[
 \gamma=4\max_{s\le s_0}\eta_s(K),
\]

three contractions produce \(KD\gamma^3\).  There are at most \(K^r\)
nodes at depth \(r\), so all stopped links contribute at most

\[
 B(K+K^2+K^3)\le\frac{3D}{mK}.
\]

The additive concentration errors contribute at most \(3K^4\Lambda\).
These are full-link overcounts, so overlaps between labels or between
different branch histories cannot invalidate the inequality.

The asymptotic ledger is also correct:

\[
 \eta_s(K)=O\!\left(\frac1m+\frac{h}{m^{3/2}}\right)+o(m^{-A})
 \quad(s\le64),
\]

and hence

\[
 K\gamma^3
 =O((h/m)^4)+o(m^{-1/2})=o(m^{-1/2})
\]

under \(h=o(m^{7/8})\).  Moreover
\(1/(mK)=o(m^{-1/2})\) and
\(K^4\Lambda=o(D/\sqrt m)\).

Therefore every family with cover number above \(2^{s_0}\) satisfies
(0.1).  The existing physical off-edge-star estimate gives

\[
 |\mathcal F|\le2\tau(\mathcal F)\widehat\rho_mD
\]

for \(2\le\tau(\mathcal F)\le2^{s_0}\), and
\(\widehat\rho_m\sqrt m=o(1)\).  Cover number one is precisely
containment in a target star.  These cases exhaust all intersecting
families.

## 6. Scope and remaining boundary

The following is now proved for the strengthened selected port outcome:

\[
 \boxed{\text{every non-star pairwise-intersecting support is }
        o(D_1/\sqrt m).}
\]

This includes genuinely distributed high-cover families and does not
require a common chart.  It supersedes PHCR as an EKR prerequisite.

It still does not imply

\[
 \chi_f'(\mathcal H^\#)
 \le D_1+o(D_1/\sqrt m).
\]

Clique inequalities are only part of the fractional matching/edge-colour
polytope.  Abstract non-clique obstructions remain possible, so an
additional physical matching-decomposition theorem is still required
for coefficient one.

