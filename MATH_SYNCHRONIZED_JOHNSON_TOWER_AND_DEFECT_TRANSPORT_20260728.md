# The synchronized Johnson tower and the exact defect-transport law

Date: 2026-07-28

Status: pure mathematics, with the final numerical table checked against the
frozen `k=15` Hall-29 carrier.  No `k=15` solution is claimed.

## 0. Why this is the right reconciliation

The lower shadows seen in the exact words are not independent set systems.
For a resident middle chronology, every lower row is a Johnson walk, the next
lower row is its edge-intersection colouring, and the preceding row is its
edge-union colouring.  Moreover, the point degrees of *all* lower-row defect
designs are determined by the immediate-shadow defect and the two boundary
ramps.

This explains three persistent observations at once:

1. one chronological choice serves every depth;
2. filling a hole at one depth usually relocates a defect rather than erasing
   it; and
3. large alternating-component moves succeed where isolated local moves do
   not: after the first shadow is fixed, deeper changes must be
   point-degree-preserving design trades simultaneously at every depth.

## 1. A tower of derived Johnson walks

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a Hamilton path in `J(k,r)`.  Write its transitions as

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\tag{1.1}
\]

Assume that every internal one-run of every coordinate in `T` has length at
least `d+1`.  For `0<=q<=d`, define

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h},
 \qquad 0\le i<W-q.
\tag{1.2}
\]

### Theorem 1.1 (synchronized Johnson tower)

For every `q<=d`,

\[
 |L_i^{(q)}|=r-q,
 \qquad
 L_i^{(q)}=T_i\setminus\{a_i,\ldots,a_{i+q-1}\}.
\tag{1.3}
\]

For `q<d`, consecutive terms are Johnson adjacent and

\[
 L_{i+1}^{(q)}=L_i^{(q)}-\{a_{i+q}\}+\{b_i\}.
\tag{1.4}
\]

The adjacent intersection and union recover the neighbouring levels:

\[
 L_i^{(q)}\cap L_{i+1}^{(q)}=L_i^{(q+1)},
\tag{1.5}
\]

\[
 L_i^{(q)}\cup L_{i+1}^{(q)}=L_{i+1}^{(q-1)}
 \qquad(q\ge1).
\tag{1.6}
\]

#### Proof

Within at most `d` successive transitions, no inserted coordinate can be
deleted: that would create an internal one-run of length at most `d`.
Likewise, the deleted coordinates are distinct, since deleting the same
coordinate twice would require an intervening insertion followed by such a
short internal run.  Hence the only coordinates lost from every set in the
window are the displayed `q` deletions, proving (1.3).

Moving the window one step expires the insertion `b_i` and introduces the
new terminal deletion `a_(i+q)`, which proves (1.4).  These two coordinates
are distinct and lie on opposite sides of `L_i^(q)`, so the two consecutive
sets are Johnson adjacent.  Their common part deletes both boundary tokens
and is (1.5); their union restores both and is (1.6).  \(\square\)

Thus `L^(q+1)` is literally the edge-colour sequence of `L^(q)` under the
intersection colouring of the Johnson graph.  This is the exact finite
counterpart of the correlated-depth phenomenon seen in PBBS: the rows form
one iterated path, not `d` occupancy experiments.

## 2. Boundary-corrected point degrees

For a coordinate `x`, let

* `t_x` be the number of one-runs of `x` in the linear word `T`;
* `M_x=#{i:x in T_i}`; and
* for `q>=1`,

\[
 \epsilon_{q,x}=\sum_{R}(q-|R|)^+,
\tag{2.1}
\]

where the sum runs over the one-runs `R` of `x`.

Internal runs have length at least `d+1`, so for `q<=d` only the initial and
terminal boundary runs can contribute to `epsilon_(q,x)`.

### Lemma 2.1 (run-to-trace identity)

The number of occurrences of `x` in the `q`th trace row is

\[
 \sum_i {\bf1}_{x\in L_i^{(q)}}
   =M_x-q t_x+\epsilon_{q,x}.
\tag{2.2}
\]

#### Proof

A one-run of length `ell` contains exactly `max(ell-q,0)` windows of length
`q+1`.  Since

\[
 \max(\ell-q,0)=\ell-q+(q-\ell)^+,
\]

summing over the runs proves (2.2).  \(\square\)

If `T` enumerates the whole rank-`r` layer, then

\[
 M_x=\binom{k-1}{r-1}
\tag{2.3}
\]

for every coordinate.

There is also an exact scalar boundary law.  At either end of a Johnson path,
the first `q-1` deletions, respectively the last `q-1` insertions, create one
boundary one-run of each length `1,...,q-1`.  Residence makes those tokens
distinct.  Therefore

\[
 \boxed{\sum_x\epsilon_{q,x}=q(q-1).}
\tag{2.4}
\]

Coordinates used at both ends may merge contributions pointwise, but the
total is fixed.

## 3. Defect designs at every depth

Let `mu_q(S)` be the load of an `(r-q)`-set `S` in `L^(q)`.  Define

\[
 \mathcal H_q=\{S:\mu_q(S)=0\}
\tag{3.1}
\]

and let `mathcal E_q` be the multiset containing `mu_q(S)-1` extra copies of
each set with positive load.  Thus, as signed incidence vectors,

\[
 \mu_q={\bf1}-{\bf1}_{\mathcal H_q}+{\bf1}_{\mathcal E_q}.
\tag{3.2}
\]

Write `deg_F(x)` for point degree, with multiplicity when `F` is a multiset.

### Theorem 3.1 (exact cross-depth defect transport)

Put

\[
 \Delta=\binom{k-1}{r-1}-\binom{k-1}{r-2}
\tag{3.3}
\]

and

\[
 \beta_q=\binom{k-1}{r-1}-\binom{k-1}{r-q-1}-q\Delta.
\tag{3.4}
\]

Then

\[
 \boxed{
 t_x=\Delta+\deg_{\mathcal H_1}(x)-\deg_{\mathcal E_1}(x)}
\tag{3.5}
\]

and, simultaneously for every `q<=d`,

\[
 \boxed{
 \deg_{\mathcal E_q}(x)-\deg_{\mathcal H_q}(x)
 =\beta_q
 -q\bigl(\deg_{\mathcal H_1}(x)-\deg_{\mathcal E_1}(x)\bigr)
 +\epsilon_{q,x}.}
\tag{3.6}
\]

The scalar multiplicity ledger is

\[
 |\mathcal E_q|-|\mathcal H_q|
   =W-q-\binom{k}{r-q}.
\tag{3.7}
\]

#### Proof

At depth `q`, counting occurrences containing `x` from (3.2) gives

\[
 \binom{k-1}{r-q-1}
 -\deg_{\mathcal H_q}(x)+\deg_{\mathcal E_q}(x).
\]

Equate this with (2.2)--(2.3).  At `q=1`, `epsilon_(1,x)=0`, which gives
(3.5).  Substitution gives (3.6).  Finally the trace row has `W-q`
occurrences, while the complete target layer has the displayed binomial
size, proving (3.7).  \(\square\)

For odd `k=2r-1`,

\[
 \Delta=\frac1r\binom{2r-2}{r-1}=C_{r-1}.
\tag{3.8}
\]

Hence the Catalan run count is not an independent design phenomenon.  It is
forced by the immediate lower rainbow.  In the ideal one-hole case
`H_1={H}`, `E_1=emptyset`,

\[
 t_x=C_{r-1}+{\bf1}_{x\in H}.
\tag{3.9}
\]

This recovers the ballot/Catalan block count directly from the path palette.

## 4. The marginal trade theorem

Suppose two resident middle chronologies have the same immediate defect
`(H_1,E_1)` and the same boundary correction vector `epsilon_q`.  Theorem
3.1 says that their signed depth-`q` defect designs have identical point
degrees.  Equivalently, their complete depth-`q` trace multisets have the
same point degrees.

### Theorem 4.1 (rankwise quadratic generation)

Any two multisets of `s`-subsets with the same cardinality and the same point
degrees are connected by a sequence of symmetric two-block exchanges

\[
 (A,B)\longmapsto
 (A-\{a\}+\{b\},\ B-\{b\}+\{a\}),
\tag{4.1}
\]

where `a in A\B` and `b in B\A`.

#### Proof

Label the block occurrences and view their incidence matrices as bipartite
graphs between block occurrences and points.  Both graphs have the same
degree sequence on both shores.  Their symmetric difference is a union of
alternating even cycles.  Successively shortcut an alternating cycle by a
`2 x 2` switch.  Each switch is exactly (4.1), and iteration transforms one
incidence matrix into the other.  Block labels may be forgotten at the end.
\(\square\)

This theorem says that there is no *marginal* mystery: at one fixed depth,
quadratic trades generate every allowed compensation.  The hard condition is
chronological synchronization.  One exchange of the middle transition word
must induce compatible exchanges in all rows of Theorem 1.1 while preserving
residence, upper coverage, and the owner matching.  The alternating-component
hybrid cubes observed computationally are chronology-level lifts of these
rankwise switches.

## 5. Complement-antipodal cycles collapse the two sides

For odd `k=2r-1`, let a Hamilton cycle of the middle-levels incidence graph
be written cyclically as

\[
 T_0,X_0,T_1,X_1,\ldots,T_{W-1},X_{W-1},
\tag{5.1}
\]

where `|T_i|=r`, `|X_i|=r-1`, and

\[
 X_i=T_i\cap T_{i+1}.
\tag{5.2}
\]

Assume set complementation preserves this cycle and acts on it as its
half-turn.  Since the half-turn moves `W` edges and swaps the two shores when
`W` is odd, there is an index shift `s` such that

\[
 [k]\setminus T_i=X_{i+s}
\tag{5.3}
\]

for every `i` (indices cyclic).

### Theorem 5.1 (one-sided tower identity)

For every `q>=0`,

\[
 \boxed{
 [k]\setminus\bigcup_{j=0}^{q}T_{i+j}
   =\bigcap_{j=0}^{q}X_{i+s+j}
   =\bigcap_{j=0}^{q+1}T_{i+s+j}.}
\tag{5.4}
\]

Consequently the upper depth-`q` load distribution of the `T` projection is
the complement image of its lower depth-`q+1` load distribution.  In
particular, upper depth `q` is complete if and only if lower depth `q+1` is
complete.

#### Proof

Complementation turns unions into intersections.  Apply (5.3) termwise to
the first expression.  The second equality follows from (5.2): intersecting
`X_(i+s),...,X_(i+s+q)` is the same as intersecting the `q+2` consecutive
upper vertices which define them.  Complementation is a bijection between
the two target ranks, proving the load and coverage statements.  \(\square\)

This is especially relevant at `k=15`.  Here `r=8` and `W=6435` is odd, so
the half-turn action is arithmetically possible; indeed `k=15` is the first
open dimension of the form `2^a-1`.  In this symmetry class the carrier's
entire upper audit is not a second family of constraints: it is the next row
of the same lower Johnson tower.  The remaining conditional construction is
therefore a complement-antipodal middle-levels cycle whose one lower tower is
complete and whose upper projection has the required residence and owner
compatibility.  Existence of such a decorated cycle is not proved here.

## 6. The Hall-29 carrier under the theorem

For the frozen `k=15` carrier,

\[
 k=15,\quad r=8,\quad d=3,\quad C_{r-1}=C_7=429.
\]

Its immediate lower defects are

```text
holes   = 5801, 7267, 8877, 13620
repeats = 17140, 3868, 4525
```

Formula (3.5) gives the run-count vector

```text
coordinate: 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
t_x:      431 430 428 429 428 431 429 429 428 429 431 429 431 431 428
```

The boundary corrections are

\[
 \sum_x\epsilon_{2,x}=2,
 \qquad
 \sum_x\epsilon_{3,x}=6,
\]

with two boundary length-one runs and two boundary length-two runs, exactly
as (2.4) predicts.  The constants in (3.6) are

\[
 \beta_2=572,\qquad\beta_3=1144.
\]

The measured deeper rows satisfy (3.6) coordinate by coordinate:

```text
depth q    holes    excess copies    degree(E_q)-degree(H_q)
1             4              3       forced by the displayed palette
2            21           1449       568..574, exactly formula (3.6)
3             4           3433       1138..1147, exactly formula (3.6)
```

For comparison, the exact `k=13` carrier has one immediate hole and no
repeat; its depth-two and depth-three holes are zero, and its excess designs
also satisfy (3.6) exactly.

The mathematical implication for `k=15` is sharp.  A move which holds the
immediate palette and endpoint flags fixed cannot simply insert one of the
21 missing rank-six or four missing rank-five targets.  It must perform a
point-degree-preserving design trade at that depth, and the same middle move
must realize the corresponding trades at the other depths.  A move which
improves the immediate palette changes the required point-degree vector at
depth `q` by `q` times the palette change.  This is the exact source of the
observed defect transport.

## 7. The remaining pure-math target

The finite problem is now naturally stated as follows.

> Construct a Hamilton path in `J(k,r)` whose synchronized Johnson tower is
> resident, upper-complete, and whose signed defect designs admit one common
> chronology-level trade to the boundary-compatible palette and the
> nested-owner matching.

Theorem 4.1 guarantees enough rankwise moves.  What is missing is a lifting
theorem saying that a compatible family of those rankwise symmetric
exchanges can be realized by one exchange of the middle transition word.
That is substantially narrower than an unstructured Hall-zero search and is
the mathematical form of the global-versus-local gap seen in the exact
certificates.
