# Equivariant graded compilers: an exact quotient-Hall reduction at `k=15`

Date: 2026-07-29

Status: proved sufficient theorem, exact weighted quotient reduction, and
boundary-localization lemma.  This note does **not** prove that the required
Hall inequalities hold for the Merino--Mička--Mütze carrier.  It proves that,
for the depth-three regime containing `k=15`, the lower common-word SAT gate
can be replaced by a much smaller ordinary matching gate after one additional
grading choice.

## 1. Setup

Let

\[
 k=2m+1,\qquad r=m+1,\qquad W={k\choose r},\qquad
 N=W/k=\operatorname {Cat}_m,
\]

and index cyclic sequences by `Z_W`.  Write

\[
 (DX)_i=X_i\cup X_{i+1}.
\]

Suppose `T=(T_i)` is a cyclic Johnson Hamilton cycle on the rank-`r`
sets.  Let `d=d(k)` and suppose `T` is cyclically `d`-resident.  Its maximal
cyclic depth-`d` erosion is denoted by `P`; thus

\[
 P_i=\bigcap_{a=0}^{d}T_{i-a}
 \quad\hbox{(up to a harmless cyclic shift)},
 \qquad D^dP=T.                                           \tag{1.1}
\]

Put

\[
 h=r-d.                                                   \tag{1.2}

Assume `h>=1`; this is automatic in every finite instance used below and is
needed only to guarantee that the unmatched envelope letters are nonempty.
\]

Residence and Johnson adjacency imply that every `D^jP` entry has rank
`h+j`; a proof is given in Lemma 1.1 below.  Assume the **graded shadow
condition**

\[
 \{(D^jP)_i:i\in\mathbb Z_W\}
 \supseteq { [k]\choose h+j}
 \qquad(1\le j\le d).                                   \tag{1.3}
\]

For `j=d`, this is equality because `D^dP=T`.  At depth three, the only
nonautomatic condition in (1.3) is cyclic lower-`q=2` coverage by `DP`:
lower-`q=1` is the rainbow middle-level property, and `D^3P=T` is the
middle layer.  There is **no separate lower-`q=3` carrier gate**.  The
rank-`h` sets are included among the literal targets of the Hall graph, so
their degree condition is exactly the needed `q=3` support test.

### Lemma 1.1 (intersection tower and its ranks)

Write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\]

For `0<=q<=d`, every intersection of `q+1` consecutive carrier sets has
rank `r-q`.  Moreover, with consistent cyclic indexing,

\[
 D^jP_i=\bigcap_{a=0}^{d-j}T_{i-a},
 \qquad |D^jP_i|=h+j.                                   \tag{1.4}
\]

#### Proof

In any block of at most `d` transitions, the deleted coordinates are
distinct, and no deleted coordinate was inserted earlier in the same
block.  Otherwise a coordinate would be reinserted and deleted again after
at most `d` carrier positions, creating an internal positive run of length
at most `d`, contrary to `d`-residence.  Thus `q` successive transitions
delete `q` distinct members of the first carrier set from the consecutive
intersection, proving rank `r-q`.

Let `I_i^(q)=T_i intersect ... intersect T_(i+q)`.  Both `I_i^(q)` and
`I_(i+1)^(q)` lie in `I_(i+1)^(q-1)`.  The first contains the coordinate
deleted at the last boundary and the second contains the coordinate inserted
at the first boundary; residence makes these two boundary contributions
distinct.  Hence their union has rank `r-q+1`, equal to the rank of
`I_(i+1)^(q-1)`, and therefore

\[
 I_i^{(q)}\cup I_{i+1}^{(q)}=I_{i+1}^{(q-1)}.
\]

Starting from `P`, which is the `q=d` intersection row, and iterating this
identity proves (1.4).  \(\square\)

### Lemma 1.2 (the top lower row is forced cyclically)

Assume the rank-`(r-1)` row `D^(d-1)P` is a bijection onto
`binom([k],r-1)`.  If `A<=P`, `D^dA=T`, and the cyclic word `A` covers every
rank-`(r-1)` target, then

\[
 D^{d-1}A=D^{d-1}P.                                     \tag{1.5}
\]

#### Proof

Every interval of width at least `d+1` contains a width-`(d+1)` subinterval
whose union is a rank-`r` member of `T`; hence it cannot realize a
rank-`(r-1)` target.  For `j<d-1`, every `D^jA` cell lies in a
rank-`(h+j)` envelope and
therefore has rank at most `r-2`.  Thus every rank-`(r-1)` target must
occur in row `D^(d-1)A`.  That cyclic row has exactly `W` cells and there
are exactly `W` targets.  Moreover its `i`th cell is contained in the
rank-`(r-1)` set `(D^(d-1)P)_i`.  Covering all `W` distinct targets forces
every containment to be equality.  \(\square\)

For a linear word the same count has one additional boundary cell.  This is
the familiar one-spare lower-`q=1` flag.  The stronger grading used below,
`DA=DP`, fixes all rows above the source row, not just the forced top one.

## 2. One derivative freezes the whole upper part of the compiler

### Definition 2.1 (one-core)

A one-core of `P` is a cyclic sequence `C` satisfying

\[
 C_i\subseteq P_i,\qquad DC=DP.                          \tag{2.1}
\]

One-cores always exist: `C=P` is one.  Much sparser one-cores are obtained
coordinatewise.  For a coordinate `x`, choose binary values `c_i(x)` with

\[
 c_i(x)\le {\mathbf 1}_{x\in P_i},\qquad
 c_i(x)\vee c_{i+1}(x)
 ={\mathbf 1}_{x\in P_i\cup P_{i+1}}.                   \tag{2.2}
\]

This is a vertex-cover problem on a disjoint union of paths (or on a cycle
in the all-one case), with the vertices outside the support of `P` forbidden.
It is feasible because the full support of `P` is itself a cover.

For a fixed one-core `C`, form the bipartite graph

\[
 \mathcal G_C=(\mathcal S_h,\mathbb Z_W;E),              \tag{2.3}
\]

where

\[
 \mathcal S_h=\{S\subseteq[k]:1\le |S|\le h\},
\]

and

\[
 S\sim i\quad\Longleftrightarrow\quad
 C_i\subseteq S\subseteq P_i.                           \tag{2.4}
\]

### Theorem 2.2 (graded compiler matching theorem)

If `G_C` has a matching saturating `S_h`, then there is a nonempty cyclic
word `A=(A_i)_(i in Z_W)` such that

\[
 D^jA=D^jP\qquad(1\le j\le d),                           \tag{2.5}
\]

and every nonempty set of rank at most `h` occurs literally as one letter
of `A`.  Consequently (1.3) implies that rows

\[
 A,DA,\ldots,D^dA                                      \tag{2.6}
\]

cover every nonempty set of rank at most `r`.

#### Proof

For every matched edge `S~i`, put `A_i=S`.  At an unmatched position put
`A_i=P_i`.  Equation (2.4) gives

\[
 C\subseteq A\subseteq P.
\]

Monotonicity of `D` and (2.1) now give the pointwise sandwich

\[
 DP=DC\subseteq DA\subseteq DP,
\]

so `DA=DP`.  Iterating proves (2.5).  Every letter is nonempty: matched
letters belong to `S_h`, and unmatched letters have rank `h`.  The matching
places every member of `S_h` literally in `A`; (1.3) and (2.5) supply all
remaining ranks through `r`.  \(\square\)

This is the key simplification.  The exact common-word obstruction from a
general multirow compiler disappears because every flexible target is put
in a **single** physical letter.  Negative requirements from different
target intervals never overlap.  The one-core is precisely the common
positive protection needed to keep all higher rows fixed.

### Proposition 2.3 (exact scope of the reduction)

Within the graded subclass `DA=DP`, a compiler of the form in Theorem 2.2
exists if and only if there is some one-core `C` for which `G_C` has a
saturating matching.

#### Proof

The forward word `A` is itself a one-core, because `A<=P` and `DA=DP`.
Choose one literal occurrence of each target in `S_h`; these distinct
positions give a matching in `G_A`.  The reverse implication is Theorem
2.2.  \(\square\)

The proposition does not say that a successful arbitrary depth-`d`
compiler must satisfy `DA=DP`.  This is an intentionally stronger grading
which buys the ordinary matching theorem.

## 3. Rotation symmetry makes the Hall test a weighted quotient test

Assume now that `T` is a strict spiral of voltage `v`, with `gcd(k,v)=1`:

\[
 T_{i+N}=\rho^vT_i.                                      \tag{3.1}
\]

Then `P` has the same symmetry.  An equivariant one-core exists.  Indeed,
choose any solution of (2.2) for coordinate zero over its full cyclic trace
and translate it by

\[
 (i,x)\longmapsto(i+N,x+v).                              \tag{3.2}
\]

Because `v` is a unit, this defines the other coordinate traces, and after
`k` translations both the position and the coordinate return to their
starting values.

Fix such an equivariant `C`.  The cyclic group acts by automorphisms on
`G_C`.  Its action on the right positions is free, with `N` orbits of size
`k`; target orbits on the left may be shorter when `k` is composite.
The equivariance includes the twisted quotient seam, namely

\[
 P_{i+N}=\rho^vP_i,\qquad C_{i+N}=\rho^vC_i,
\]

and in particular the closing edge equation between positions `N-1` and
the appropriately rotated position zero.  Internal quotient-path equations
without this seam do not define an automorphism of the physical Hall graph.

Let `O` run over rotation orbits in `S_h`, give it weight

\[
 w(O)=|O|,                                                \tag{3.3}
\]

and let `J` run over the `N` position orbits, each of weight `k`.  Join
`O` to `J` if any (equivalently, some phased) physical candidate edge joins
the two orbits.

### Theorem 3.1 (exact weighted quotient Hall criterion)

The physical graph `G_C` has a matching saturating every target if and only
if, for every collection `X` of target orbits,

\[
 \boxed{\quad
   \sum_{O\in X}w(O)\ \le\ k\,|N_{\rm quot}(X)|.
 \quad}                                                   \tag{3.4}
\]

Thus a strict-spiral carrier plus an equivariant one-core reduces the whole
graded lower compiler to a weighted Hall problem on the quotient.

#### Proof

For a target family `A`, put

\[
 \delta(A)=|A|-|N(A)|.
\]

The neighborhood identities imply that `delta` is supermodular:

\[
 \delta(A\cup B)+\delta(A\cap B)
 \ge\delta(A)+\delta(B).                                 \tag{3.5}
\]

Consequently unions and intersections of maximum-deficiency shores are
again maximum-deficiency shores.  Unioning all rotations of one maximizer
produces a rotation-invariant maximizer.  Hence Hall fails physically if
and only if it fails on a union of complete target orbits.  The neighborhood
of such a union is a union of complete right orbits, so its physical sizes
are exactly the two sides of (3.4).  \(\square\)

The matching produced by (3.4) need not be equivariant.  This is useful,
not a defect: at composite `k`, a short target orbit can use only part of a
`k`-position orbit, leaving the remaining phases for other targets.  The
carrier and the core retain their symmetry while the final source word is
allowed to break it.  A saturated quotient flow proves existence; its
aggregate flow is not itself a phase-resolved matching.  To emit a word one
must recover an ordinary matching in the physical occurrence-labelled graph,
as the implementation and the `k=11` calibration do.

## 4. The `k=15`, `d=3` specialization

Here

\[
 (k,r,d,h,W,N)=(15,8,3,5,6435,429).                      \tag{4.1}
\]

Let `T` be a strict-spiral rainbow Johnson Hamilton cycle satisfying
depth-three residence.  Its shadow rows are

\[
 P\quad(\text{rank }5),\qquad
 DP\quad(\text{rank }6),\qquad
 D^2P\quad(\text{rank }7),\qquad
 D^3P=T\quad(\text{rank }8).                             \tag{4.2}
\]

Perfect lower-`q=1` rainbow gives the rank-seven row, and cyclic
lower-`q=2` coverage gives the rank-six row.  Rank five and below are all
assigned literally by the matching.  In particular, cyclic lower-`q=3`
coverage is not a separate carrier prerequisite: it is exactly the
positive-degree part of the rank-five portion of the Hall graph.  Therefore
Theorems 2.2 and 3.1 apply exactly as stated.

The flexible target side has

\[
 \sum_{s=1}^{5}{15\choose s}=4943                       \tag{4.3}
\]

physical targets and `6435` physical letter positions, a slack of `1492`.
After quotienting, it has only

\[
 1+7+31+91+201=331                                      \tag{4.4}
\]

target orbits against `429` position orbits.  Their exact orbit-size
profiles are

\[
\begin{array}{c|c}
\text{rank}&\text{orbit sizes}\ \\ \hline
1&15^1\\
2&15^7\\
3&15^{30},5^1\\
4&15^{91}\\
5&15^{200},3^1.
\end{array}                                               \tag{4.5}
\]

Accordingly the remaining lower gate is not the old `16383`-target
shared-variable SAT instance.  For each equivariant one-core it is the
weighted `331 x 429` quotient Hall problem (3.4).  A passing matching emits
`A` directly and preserves `DP,D^2P,D^3P` by the sandwich proof; no second
SAT completion is needed.

This is a sufficient route, not an automatic consequence of the shadow
tests.  The choice `C=P` is an equivariant one-core, but when `h>1` it gives
no singleton candidate at all.  Sparse one-core choice is therefore real
mathematical content.  Even after every target orbit has positive degree,
a multi-orbit weighted Hall shore may remain deficient.

The published canonical symmetric cycle is not already a passing carrier.
The lightweight audit `python3 scratch/audit_knuth_symmetric_middle_k15.py
15 1` gives:

```text
minimum cyclic residence run       2      (need 4)
lower q2 coverage                  4455 / 5005
lower q3 coverage                  2475 / 3003
all upper targets                  8611 / 9949
strict spiral voltage              1
```

Thus the Merino--Mička--Mütze theorem solves the central symmetric
Hamilton/rainbow base, including composite `k=15`, but the extension-edge
choices still have to be redesigned for residence and lower-`q=2` (as well
as the upper shadows) before the quotient Hall theorem can be consumed.
The lower-`q=3` deficit shown above will be tested, and potentially repaired,
inside Hall rather than as an eager carrier constraint.

## 5. Cutting creates no lower defect after a cyclic compiler

Suppose Theorem 2.2 has produced a cyclic word `A` of length `W`.  Rotate it
at any desired cut and form the linear word

\[
 A'=A_0,A_1,\ldots,A_{W-1},A_0,A_1,\ldots,A_{d-1}.       \tag{5.1}
\]

### Lemma 5.1 (prefix closure)

Every cyclic cell of `D^jA`, `0<=j<=d`, occurs exactly once among the first
`W` cells of `D^jA'`.  In particular,

\[
 D^dA'=T                                                    \tag{5.2}
\]

in the chosen linear order, and no lower target is lost at the cut.

#### Proof

A cyclic cell of row `j` is a block of `j+1<=d+1` consecutive source
letters.  The appended prefix contains every wraparound block of these
lengths.  Starts `0,...,W-1` therefore reproduce the cyclic row exactly.
\(\square\)

Thus the lower compiler is cut-independent in this route.  The cut still
has to be chosen for **upper** nonwrapping coverage; cyclic upper-orbit
coverage alone does not settle that separate gate.

There is a related localization statement for a quotient implementation
which temporarily drops its twisted closing constraints.

### Lemma 5.2 (replicated quotient-seam cone)

Suppose a fundamental quotient path of length `N` is lifted through `k`
sheets without enforcing its twisted last-to-first constraint.  The physical
lift has `k` block seams.  At derivative row `j`, at most `kj` cyclic cells
cross those seams.  Across rows `1,...,d`, at most

\[
 k{d+1\choose2}                                          \tag{5.3}
\]

cells are affected, and all affected source positions lie in an
`O(kd)` collar.

#### Proof

For one seam, exactly `j` starts of a length-`j+1` block cross it.  Sum over
the `k` replicated seams and then over `j`.  \(\square\)

Equation (5.3) is a localization theorem, not a repair theorem: a unique
shadow witness or a tight Hall shore can make even one affected cell
essential.  Enforcing the twisted quotient boundary from the start removes
the entire collar; solving only the quotient path leaves a finite
`O(kd)`-position / `O(kd^2)`-cell repair problem.

## 6. Exact calibration on the fresh strict `k=11` carrier

The audit

```text
python3 scratch/audit_k11_equivariant_graded_quotient_hall.py
```

reconstructs Claude's fresh voltage-two carrier from

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/equi2_k11_rnd34.json
```

and applies Theorems 2.2 and 3.1 without a compiler SAT call.  Here

```text
(k,r,d,h,W,N) = (11,6,3,3,462,42).
```

The canonical coordinatewise depth-one core is equivariant and has

```text
rank histogram(C) = 1^55 2^220 3^187,
DC = DP.
```

The physical Hall graph has `231` targets and `462` positions.  Its exact
candidate-degree histogram is

```text
1^22 2^33 3^77 4^33 5^33 6^22 9^11,
```

and it has a `231`-edge saturating matching.  On the quotient this is a
weighted max flow of `231/231` on only `21` target orbits and `42` position
orbits.

The matched word satisfies `DA=DP`; its cyclic derivative rows have ranks

```text
3^462, 4^462, 5^462, 6^462
```

and distinct counts

```text
165, 330, 462, 462.
```

Cut zero is upper-safe.  Appending the three-letter prefix produces the new
word

```text
scratch/k11_equivariant_graded_hall.word.txt
```

of length `465`, SHA-256

```text
7b5ad0529c4e6354664e46d1cf42b02982e0787fead4edf9ba680dc5b63031cb
```

and the independent exhaustive verifier reports all `2047` nonempty masks,
an exact rank-six middle row, and status `VERIFIED_OPTIMAL`.  The frozen
audit is

```text
scratch/k11_equivariant_graded_hall.audit.json.
```

This calibration is important: the quotient-Hall collapse is not merely a
formal sufficient condition.  On a freshly reconstructed strict carrier it
actually replaces the old lower SAT compiler and emits a different exact
optimal certificate.

## 7. General range and the exact caveat

The one-letter grading needs the elementary capacity condition

\[
 \sum_{s=1}^{h}{k\choose s}\le W,
 \qquad h=r-d.                                            \tag{6.1}
\]

It holds in the depth-three regime for `k=11,13,15,17`, but fails for
`k=19,21`.  It also fails at `k=9` (by three physical slots).  Therefore
Theorem 2.2 is a serious `k=15` simplification and a reusable theorem on
part of every depth plateau, but it is not by itself the all-odd-`k`
construction.

When (6.1) fails, at least one additional derivative row must carry flexible
targets.  Assigned intervals then overlap in source letters, and the exact
common-word positive/negative compatibility reappears.  Rotation still
reduces any **fixed invariant candidate graph** to weighted quotient Hall,
but ordinary containment Hall alone no longer implies one common source
word.

The precise `k=15` next target is now:

> Find, on a Merino--Mička--Mütze strict-spiral carrier with cyclic
> residence and `q=2` lower coverage, an equivariant one-core `C` whose
> `331 x 429` weighted quotient graph satisfies (3.4), together with an
> upper-safe physical cut.

This separates three facts cleanly:

1. the published symmetric middle-level cycle supplies the strict-spiral
   central/rainbow base even for composite `k=15`;
2. cyclic `q=2` coverage and residence supply the nonautomatic fixed
   maximal row, while rank-five `q=3` support is absorbed into Hall; neither
   makes lower Hall automatic; and
3. after the one-core grading, the compiler gate is a true quotient Hall
   problem rather than the former shared-variable SAT problem.
