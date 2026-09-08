# The `k=17` protected factor: exact one-copy Hall contraction and a 3,807-edge residence obstruction

**Date:** 2026-08-01  
**Status:** unconditional factor/rounding reduction and exact finite audit.
The combined `h=2` reset plus twin-Ferrers bank is treated as the fixed
protected seed.  The note gives an exact sufficient-and-necessary Hall
criterion for an owner-rainbow flag circulation relative to one alternating
owner attachment, and proves that the frozen seven-component factor itself
is at least 3,807 old adjacencies away from any depth-three resident
rethreading.  It does **not** construct the required flag selector or a
`k=17` word.

## 0. Input and outcome

The authenticated factor

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

is a spanning two-factor of the containment graph between rank-eight and
rank-nine subsets of `[17]`.  It has seven components of owner sizes

```text
14305, 8615, 1362, 18, 4, 3, 3,
```

contains all 52 incidences of the three protected owner paths, and has
complete lower- and upper-`q1` palettes.

Two conclusions follow.

1. Alternating the factor gives a completely explicit functional owner
   attachment.  Relative to any selected depth-three flag table, extension
   of the protected paths to an integral owner-rainbow cycle cover is exactly
   one contracted bipartite Hall problem.  No rounding of the rational pull
   block coefficients is involved.
2. The frozen factor cannot itself carry a depth-three source.  Its 5,783
   short coordinate runs have circular interval transversal number 3,807,
   even when all 26 protected internal `q1` gaps are forbidden as cuts.
   Hence every resident rethreading of these same owners must delete at least
   3,807 old factor adjacencies.  This is a sharp obstruction to a local or
   bounded-edit rounding around the new seed.

## 1. A two-factor already supplies the owner bijection

Let `L` be the rank-eight shore and `O` the rank-nine shore.  Alternately
colour every component of the two-factor as two perfect matchings

\[
                         M_0,\ M_1:L\longrightarrow O.          \tag{1.1}
\]

Orient each protected owner path in the direction induced by this colouring;
path reversal is allowed because its interval deck is reversal-closed.
Define

\[
             \theta(q)=M_0(q),\qquad
             \pi(p)=M_0^{-1}(M_1(p)).                         \tag{1.2}
\]

### Lemma 1.1 (owner-rainbow factor permutation)

The triples

\[
                    (p,\pi(p),M_1(p)),\qquad p\in L,           \tag{1.3}
\]

use every tail root, head root and rank-nine owner exactly once.  Moreover

\[
             M_1(p)=p\cup\pi(p).                              \tag{1.4}
\]

Their directed cycles are precisely the seven alternating factor cycles.

#### Proof

Both `M_0` and `M_1` are bijections.  Thus `pi` is a permutation of `L`,
and the owner colours `M_1(p)` are all distinct.  The two roots `p` and
`pi(p)` are the two distinct rank-eight neighbours of `M_1(p)` in the
simple factor.  They are distinct facets of one rank-nine set, so their
union is that owner.  Alternating around a bipartite factor component gives
exactly one cycle of `pi`.  \(\square\)

This is already an integral one-copy owner/`q1` object.  Its failure is not
owner divisibility; it is compatibility with one common depth-three flag
table and, later, residence and deeper shadows.

## 2. Exact protected functional-Hall criterion

Fix one depth-three flag `f_p` at every rank-eight root `p`.  For roots
`p,q`, retain the directed edge `p q` exactly when the literal flag
transition `f_p -> f_q` is legal and has owner `theta(q)=M_0(q)`.  Call the
resulting bipartite predecessor graph

\[
                         B_{F,M_0}=(L_{\rm tail},L_{\rm head};E_F). \tag{2.1}
\]

The owner is not a free edge colour in this graph: it is the fixed bijective
head attachment `M_0`.

Let `R` be any prescribed matching of legal turn edges induced by the three
protected paths, including whatever endpoint socket edges have been fixed.
Delete from (2.1) the tails and heads already used by `R`; write the residual
graph as `B_{F,M_0}/R`.

### Theorem 2.1 (protected one-copy Hall contraction)

The selected flag table has an owner-exact directed cycle cover extending
`R` and using the functional attachment `M_0` if and only if

\[
 \boxed{
 |N_{B_{F,M_0}/R}(X)|\ge |X|
 \quad\text{for every residual tail family }X.}               \tag{2.2}
\]

For a fixed table `F`, (2.2) is decided by one bipartite maximum matching;
a failed residual min-cut returns an exact violated shore.

#### Proof

Necessity is Hall's theorem.  Conversely, (2.2) gives a residual perfect
matching.  Add the prescribed edges `R`.  Every tail and head is then used
once.  Since `M_0` is a bijection from heads to owners, every owner is also
used once.  Every selected triple is literal by the definition of
`B_(F,M_0)`, so their union is an owner-rainbow directed permutation of the
flags containing the protected paths.  \(\square\)

There is a useful attachment-variable form when `M_0` is not frozen.  Let
`A` be the residual aligned head--owner columns, and for a tail set `X` put

\[
 A_X=\{a\in A:\text{the selected predecessor list of }a
                    \text{ meets }X\}.                         \tag{2.3}
\]

For a head--owner perfect matching `u`, the predecessor neighbourhood is
exactly

\[
                         |N_u(X)|=\sum_{a\in A_X}u_a.           \tag{2.4}
\]

Hence the exact common-owner expansion rows are

\[
 \boxed{
 \sum_{a\in A_X}u_a\ge |X|
 \quad(X\subseteq L_{\rm tail}^{\rm residual}).}               \tag{2.5}
\]

Equations (2.5), together with the ordinary head and owner degree-one rows,
are necessary and sufficient for a functional owner-rainbow completion.
They are separated by alternating between a head--owner assignment and the
predecessor matching/min-cut oracle.  This is the exact checkable expansion
condition requested by the one-copy problem.

The stationary pull clock proves that the unrestricted literal trace system
has a rational balanced circulation.  The protected SCD theorem supplies an
integral named-target flag table containing a bounded prescribed bank.  They
combine integrally once the **same** table satisfies (2.2), or equivalently
admits a functional attachment satisfying (2.5).  Neither marginal theorem
implies these common rows.

## 3. Short runs are circular cut intervals

Consider one owner cycle

\[
                         C=(T_0,\ldots,T_{n-1}).                 \tag{3.1}
\]

Gaps are indexed cyclically: gap `i` lies between `T_i` and `T_(i+1)`.
For a coordinate `x`, let

\[
                         T_a,T_{a+1},\ldots,T_{b-1}             \tag{3.2}
\]

be a maximal positive run of cyclic length `ell=b-a<=3`.  Associate the
circular gap interval

\[
                         I_x=\{a-1,a,\ldots,b-1\}.               \tag{3.3}
\]

It contains the entering boundary, every internal gap and the leaving
boundary.

### Lemma 3.1 (exact circular stabbing criterion)

A gap set `D` cuts the cycle into depth-three-factorable owner paths if and
only if

\[
                         D\cap I_x\ne\varnothing                \tag{3.4}
\]

for every positive run of length at most three.

#### Proof

If `D` misses `I_x`, the complete run (3.2), including both non-`x`
boundary adjacencies, remains internal to one resulting path.  It is a
forbidden internal run of length at most three.

Conversely, if every interval is hit, every short old run is clipped at a
new path boundary or split into boundary runs.  Any run internal to a new
piece was an internal run of the original cycle and has length at least
four.  The coordinatewise residence criterion therefore gives a depth-three
antecedent on every piece.  Four consecutive rank-nine Johnson owners have
intersection rank at least six, so every maximal source letter is nonempty.
\(\square\)

For circular intervals, the minimum is exact by conditioning on one selected
point of a first interval.  After fixing that point, every remaining interval
is linear; process them by increasing right endpoint and select the rightmost
allowed point of the first unhit interval.  Trying every allowed point of
the first interval gives the circular optimum.  The same proof permits a
set of forbidden protected gaps.

## 4. Exact cut census for the protected seven-factor

The factor has

\[
       3073\text{ runs of length }2,qquad
       2710\text{ runs of length }3,qquad
       0\text{ runs of length }1.                            \tag{4.1}
\]

Applying Lemma 3.1 componentwise gives:

| owner component size | short runs | minimum cuts | minimum with protected gaps forbidden |
|---:|---:|---:|---:|
| 14,305 | 3,404 | 2,244 | 2,244 |
| 8,615 | 2,049 | 1,349 | 1,349 |
| 1,362 | 317 | 208 | 208 |
| 18 | 3 | 2 | 2 |
| 4 | 4 | 2 | 2 |
| 3 | 3 | 1 | 1 |
| 3 | 3 | 1 | 1 |
| **total** | **5,783** | **3,807** | **3,807** |

All 26 factor gaps whose two incidences belong to the protected packet or
twin banks were forbidden in the last column.  They cause zero additional
cut cost.

### Corollary 4.1 (global-rethread distance)

Let `C'` be any depth-three-resident two-regular chronology on the same
24,310 owner vertices.  If it retains an old factor adjacency, count that
adjacency as unchanged.  Then `C'` deletes at least

\[
                              \boxed{3807}                    \tag{4.2}
\]

old factor adjacencies.  The same bound holds if all protected internal
adjacencies must remain.

#### Proof

If every adjacency in one interval (3.3) were retained, those edges would
still form the same path with the same non-`x` boundaries inside `C'`.
The old short run would remain an internal short run.  Thus the set of
deleted old adjacencies hits every interval, and Section 4 gives the lower
bound.  \(\square\)

This is not a no-go for `nu(17)=B(17)`.  It says the newly closed factor is
a valid protected **seed**, but an integral pull-clock/flag rounding cannot
be a bounded local perturbation of its unprotected bulk.  At least 3,807
factor edges must participate in the rethreading before the later deep-upper
and compiler rows are even meaningful.

## 5. Reproducible audit

The exact C++20 audit is

```text
scratch/audit_k17_h2_factor_min_residence_cuts_20260801.cpp
SHA256 bb09aa293759f15926ddc888882497dd9aedeea1ae835900606d3f75086d055d
```

and its retained output is

```text
scratch/k17_h2_factor_min_residence_cuts_20260801.out
SHA256 e8a358b1b49ece670764343e157857b8d0e36841dcd16ea19eff4e3904571ef8
```

It reconstructs all seven cyclic owner components from the authenticated
factor, rebuilds every coordinate run, solves the circular interval
transversal both with and without the 26 protected gaps, and checks the
previously authenticated run histogram.  It was compiled and run on H100
with `g++ -std=c++20 -O3 -DNDEBUG`; no local heavy computation or Python was
used.  Its final line is

```text
PASS_K17_H2_FACTOR_MIN_RESIDENCE_CUTS
```

## 6. Exact remaining gate

The fixed factor has already solved one integral projection:

\[
 \text{owners}+\text{lower }q1+\text{upper }q1
 \quad\text{with the complete protected bank}.               \tag{6.1}
\]

The pull clock has solved the stationary fractional trace projection, and
the protected SCD theorem has solved the integral named-target projection.
The next common theorem is now precisely:

> Choose a rethreaded depth-three flag table retaining the 52 protected
> incidences and at least 3,807 changed old adjacencies, such that the
> contracted functional expansion rows (2.2)/(2.5) hold.

Once those rows hold, Theorem 2.1 performs the one-copy owner-rainbow
rounding exactly.  Connectivity, deeper upper targets, the linear opening
and the terminal compiler remain separate later gates.
