# Independent audit: Macaulay interval erosion and common-root runs

**Date:** 2026-08-04  
**Verdict:** **INDEPENDENT GO AFTER TWO EXACT CORRECTIONS.**  The canonical
Macaulay decomposition, occurrence-level protected-current identities,
quantitative block-margin reduction, head--tail erosion inequality,
common-root run current, and uniform localized-run closure are valid at
the final hashes below.  The audit found and corrected (i) a false claim
that three block shadows can share a facet, and (ii) the missing exclusion
of the isolated full-shore endpoint from the common-root pivot
parametrization.

This is a pure mathematical audit.  No finite search, optimization, or
solver result is used.

## 1. Audited final artifacts

| artifact | final SHA-256 |
|---|---|
| `MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md` | `77253694d02d6d11c41a21b9875af843ede525d1751bca7d2463ac014b174cec` |
| `MATH_THEOREM_COMMON_ROOT_MACAULAY_RUN_EXACT_CURRENT_20260804.md` | `83db1a8e67e359025a03b0d704feb5aad81aaaae49a3e4f5339eb948edbfd189` |

The initially supplied first hash was
`c2b7156bb810306738086392238c5fb047b083b4885083a93827bb6ef16df23c`.
The supplied second hash `1fdbd655...` did not match the live artifact;
the live pre-audit file was
`00bd9db3dbfd987c039af4bf796a43b7a4598388a5e8f91a88fde34e6b353bb1`.
Neither pre-audit hash should be cited for the corrected statements.

## 2. Canonical decomposition and the corrected overlap theorem

At Macaulay index `j`, the fixed pivot set has size `m-j` and is

\[
 Q_j=\{p_{j+1},\ldots,p_m\}.
\]

Thus the canonical colex section is exactly

\[
 \mathcal B_j=Q_j+\binom{[c_j]}j.
\]

Complementation sends it bijectively to the rank-`m-1` interval between

\[
 C_j=[n]\setminus(Q_j\cup[c_j])
 \quad\text{and}\quad
 S_j=[n]\setminus Q_j,
\]

and hence gives `|I_j|=binom(c_j,j)=b_j`.  If a lower set contains `C_j`
but violates the upper cap, it contains some higher pivot `p_l`; the exact
relation

\[
 C_l\subseteq C_j\cup\{p_l\}
\]

moves it to a higher clause.  Iteration proves the principal-star DNF.

For `j<l`, a common facet must be a boundary facet of `B_j` obtained by
deleting `p_l`, and it is then an internal facet of `B_l`.  This gives

\[
 \partial\mathcal B_j\cap\partial\mathcal B_l
 =\{(Q_j-\{p_l\})\cup H:H\in\tbinom{[c_j]}j\},
\]

of cardinality `b_j`, with degrees one and `rho_l` respectively.

The original text then asserted that triple intersections can occur.  They
cannot.  A common `(j,l)` facet contains every higher pivot except `p_l`
and omits both `p_j,p_l`.  It cannot lie in an intermediate or later block
because it contains that block's forbidden pivot, and it cannot lie in an
earlier block because an earlier block facet can omit at most one of
`p_j,p_l`.  Hence every shared facet belongs to exactly one pair.  The
correct exact ledger is therefore

\[
 \sum_{D:|J(D)|\ge2}(|J(D)|-1)
 =\sum_{j=s}^{m-1}(m-j)b_j.
\]

This correction strengthens, rather than weakens, the later block-margin
bound.

## 3. Exact protected gluing and block margins

At a shared facet there is one boundary singleton fibre and one terminal
fibre of size `rho_l`.  Re-deriving the local truncated-shadow and
protected-loss table gives precisely the six rows of `chi_P(D)` in (3.2).
In particular:

* for `rho_l>=2`, the costs at protected degree `0,1,2` are respectively
  `1`, `1-tau_D`, and `0`;
* for `rho_l=1`, the costs are `0`, `1-t_D`, and `0`.

Summing proves the exact occurrence-level identity (3.3).  The corrected
pairwise ledger above gives its displayed global upper bound.

For one interval block, internal facets number
`binom(c_j,j-1)=(j/rho_j)b_j`, while boundary facets number
`(m-j)b_j`.  Therefore

\[
 \sigma(\mathcal I_j)=
 \begin{cases}
 (m-2)b_j,&\rho_j=1,\\
 (m-j-2+2j/\rho_j)b_j,&\rho_j\ge2.
 \end{cases}
\]

Charging its exact possible boundary ledger leaves

\[
 \beta_jb_j=
 \begin{cases}
 (j-2)b_j,&\rho_j=1,\\
 2(j/\rho_j-1)b_j,&\rho_j\ge2,
 \end{cases}
\]

which verifies the quantitative block-margin reduction.  Under the
two-sided interval parametrization, the outside width is `u=m-j`, the
aperture is `rho_j`, and the interval size is `b_j`; substituting these
values into the frozen exact two-sided current proves (3.7).  The endpoint
claims are also correct: `(j,rho)=(2,1)` has zero credit, while `(1,1)` is
already contained in the nonpositive regime `rho>=j`.

## 4. Head--tail erosion

Insert residual singleton fibres one at a time at one owner.  The local
gluing loss is at most one per insertion; the first insertion costs zero
when the head fibre is empty.  Hence the crude charge `m|R|` saves one at
every residual internal facet.  Internal facets of distinct Macaulay
blocks are disjoint, and no higher-index head block contains one.  The
total gluing charge is therefore at most

\[
 m|R|-\sum_{j=s}^r\binom{c_j}{j-1}.
\]

Each residual singleton has margin at least `m-12`, and

\[
 \binom{c_j}{j-1}={j\over\rho_j}\binom{c_j}j.
\]

These identities give exactly (4.2)--(4.3).  The one-interval head at
index `m` is a two-sided Boolean interval; its singleton and full-shore
endpoints are separately covered by the cited frozen results.  No hidden
endpoint remains in the erosion argument.

## 5. Common-root runs and the corrected endpoint

On a constant-aperture run, `c_j=j+rho-1` and `p_j=j+rho`.  When
`c_b<n`, the pivots are genuine ground-set coordinates and direct
complementation gives

\[
 C_j=R\cup\{p_j\},
 \qquad
 \mathcal D(R,X)=\{L:R\subseteq L,\ L\cap X\ne\varnothing\}.
\]

The pre-audit statement omitted the case `c_m=n`.  In that isolated
full-shore case the formal pivot is `p_m=n+1`, so the displayed
common-root parametrization is meaningless.  The final theorem excludes
it explicitly.  Its complement is the complete lower shore, with scalar
slack and protected loss both zero, so this correction loses no case.

For every nontrivial run, `|R|=m-rho-1` and the outside ground set has
size `N=m+rho`.  An active owner containing exactly one point of `X` has
fibre `rho`; with at least two it has fibre `rho+1`.  This independently
verifies (2.2)--(2.5).  Pascal telescoping gives

\[
 {\sigma\over2}
 =\sum_{t=0}^{h-1}{m-\rho-t\over\rho}
   \binom{m+\rho-t-1}{\rho-1},
\]

so (2.6) is exact even when later summands are negative.

For `rho>=2`, a protected unselected incidence either deletes a root
coordinate, or occurs at a unique-hit owner and deletes its unique active
coordinate.  These alternatives are disjoint and exhaustive, proving
`lambda=xi+eta`.  On each resident owner path the all-root positions form
one interval, and each active-coordinate occurrence set forms one
interval.  This gives at most two root exits and at most two exits per
active coordinate, establishing (3.4)--(3.9).  The clause-wise alternative
bound is valid because every union-loss incidence is a loss incidence for
at least one active principal-star clause.

## 6. Uniform closure and scope

The owner-fibre cap `rho+1` yields

\[
 \sigma\ge {2(m-\rho-1)\over\rho+1}|\mathcal D|.
\]

For `rho<=m/10`, this coefficient is at least sixteen for all sufficiently
large `m`; the one-clause endpoint is already safe, and two or more clauses
have size exceeding `2m`.  The frozen all-cut bound closes this range.

For `m/10<=rho<=m/2` and `h<=rho`, all terms through `h-1` in the
telescoping sum are nonnegative.  Its first term has exponential rate

\[
 (1+\alpha)\log_2(1+\alpha)-\alpha\log_2\alpha,
\]

while `N_rho` has rate at most `H_2(alpha)`.  Their difference

\[
 (1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha)
\]

is uniformly positive on `[1/10,1/2]`.  This verifies Theorem 4.1.  Under
small-side localization, a top aperture at least `m/2` would force
binomial rate `(3/2)H_2(1/3)>1`; apertures are nondecreasing with the
Macaulay index, and a run lying in `j<=rho` has width at most `rho`.
Corollary 4.2 follows.

The final scope is honest.  These theorems do not prove protected Ore for
arbitrary shifted families or for gluing across strict aperture jumps.
They prove the exact block/run reductions and close every localized
constant-aperture run in the intrinsic broad regime.  On that corrected
scope the verdict is **INDEPENDENT GO**.
