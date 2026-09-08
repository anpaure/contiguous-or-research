# K17 exact \(\Phi/G_2\) evaluator and physical deadline-particle rethread

Date: 2026-08-02  
Lane: replacement V  
Heavy host: `h100`, CPU C++20 `-O3 -DNDEBUG -march=native`  
Unique root:
`/home/amodo/or15/work/v_k17_phi_absorber_rethread_20260802`

## 1. Result

This continuation supplies three reusable fail-closed C++ layers.

1. An arbitrary-physical-factor evaluator reconstructs the unique owner
   cycle, validates every rank-eight/rank-nine/rank-ten resource, optionally
   freezes protected edges against a reference factor, and computes exact
   \(G_2\) and the formal \(\Phi\) gate over both orientations and all 24,310
   cuts.
2. A complete physical cap-triangle C6 scan replaces short-run count by a
   deadline-particle distance objective.  Its optional `G2Q` mode first
   maximizes the exact all-cut length-two clean gap and then clusters both
   length-two and length-three runs into fixed early/late absorber bands.
3. A strict star-C8 catalogue rescorer applies the identical `Q` or `G2Q`
   objective while replaying every physical gate.

The authenticated seeds evaluate as follows.

| factor | cyclic \((N_1,N_2,N_3)\) | \(\max G_2\) | \(\Phi\) | best q1-safe \(\Phi\) |
|---|---:|---:|---:|---:|
| equivariant 4,199 | \((0,2312,1887)\) | 63 | 48,494 | 48,494 |
| non-equivariant 4,820 | \((0,2764,2056)\) | 41 | 48,538 | 48,538 |

The strongest new branch starts from the non-equivariant seed.  Fifty-four
accepted physical C6 rethreads raise \(G_2\) from 41 to 71 and lower exact
\(\Phi\) from 48,538 to 48,507, even though the raw short census increases
from 4,820 to 4,872.  This is a certified improvement of the intended
clustering functional, not a disguised short-count optimization.

The terminal branch is a complete single-C6 local minimum for `G2Q`.  Its
complete rank-seven-core star-C8 catalogue contains 59 connected cap-safe
candidates, none of which improves `G2Q`.  It is still very far from the
necessary \(\Phi\le7401\) row/middle gate, so no optimal word is claimed.

## 2. Exact reusable \(\Phi\) evaluator

Let an opening have internal length-two and length-three run starts.  Define

\[
 L_2(z)=\max(\{a:\ell=2,\ a\le z\}\cup\{0\}),\qquad
 L_3(z)=\max(\{a:\ell=3,\ a\le z\}\cup\{0\}).
\]

For \(0\le d\le W\), put

\[
 v_2(d)=L_2(W-d-3),\qquad v_3(d)=L_3(W-d-4),
\tag{2.1}
\]

with a negative cutoff interpreted as zero.  The integer endpoints in (2.1)
are exact: a length-two run has \(m=0\) iff
\(a\le W-d_1-3\), and a length-three run has \(m=0\) iff
\(a\le W-d_1-4\).

For fixed \(d_1\ge d_2\), Theorem V equations (4.3)--(4.5) become

\[
 A=v_2(d_1),\qquad
 C=\max\bigl(v_3(d_1),v_2(d_2)\bigr),
\tag{2.2}
\]

and the formal gate value at the cut is

\[
 d_1+v_2(d_1)+
 \min_{0\le d_2\le d_1}
 \left[d_2+\max\bigl(v_3(d_1),v_2(d_2)\bigr)\right].
\tag{2.3}
\]

The inner minimum is evaluated in amortized constant time.  Since \(v_2\)
is nonincreasing, let \(t\) be its first index with
\(v_2(t)\le v_3(d_1)\).  On \(d_2<t\), minimize the prefix array
\(d_2+v_2(d_2)\); on \(d_2\ge t\), the first index \(t\) is optimal and has
value \(t+v_3(d_1)\).  The transition \(t\) is nondecreasing as \(d_1\)
increases.  Thus every cut costs \(O(W+N_2+N_3)\), not \(O(W^2)\), and the
entire exact two-orientation audit takes about 6.8 seconds on one H100 CPU
core with roughly 11 MiB maximum RSS.

The program reports the minimizing cut, orientation,
\((A,C,d_1,d_2)\), q1-safe restriction, and q1-safe unprotected-wrap
restriction.  It also exports the canonical physical cycle, every short run,
and every cut result.

The label `phi_value` is deliberate.  Formula (2.3) is the exact
\(\Phi\le7401\) threshold gate.  Above threshold it need not equal full
crossing-inclusive Loss (2.7).  Every passing value forces deadline/start
separation, makes the crossing term zero, and yields an explicit legal
row/middle schedule.

## 3. Exact \(G_2\)

For each opening the evaluator uses

\[
 G_2=\max_{0\le x\le W}\bigl(x-L_2(x-3)\bigr),
\tag{3.1}
\]

which is Theorem V equation (5.1).  Over all cuts of a cyclic chronology this
also equals

\[
 \min\left(W,\ 2+\max_i(s_{i+1}-s_i)\right),
\tag{3.2}
\]

where the length-two starts \(s_i\) are cyclic and occurrences are retained.
Equation (3.2) is used in the hot C6/C8 loop; the final evaluator recomputes
(3.1) for every cut.  The two implementations agree on all frozen factors.

The two-gap theorem remains only a necessary gate:

\[
 \operatorname{Loss}\ge2W-2G_2,
 \qquad G_2\ge20610\text{ is necessary at slack }7401.
\tag{3.3}
\]

Length-three particles are therefore retained in `Q`; \(G_2\) is never used
as a sufficient objective.

## 4. The smallest count-free absorber objective

Carry a q1-safe opening and a budget-feasible schedule

\[
 \sigma=(A,C,d_1,d_2),\qquad
 0\le A\le C,\quad d_1\ge d_2\ge0,\quad
 A+C+d_1+d_2\le7401.
\tag{4.1}
\]

For a run write \(e=b+1=a+\ell\).  Under (4.1), the mixed length-two clause
from the general absorber theorem is impossible: its simultaneous conditions
\(a\le C\) and \(e\ge W-d_1\) would imply
\(C+d_1\ge W-2=24308>7401\).  Hence the exact fixed-schedule corridors reduce
to

\[
 \ell=2:\quad a\le A\ \text{or}\ e\ge W-d_2,
\tag{4.2}
\]

\[
 \ell=3:\quad a\le C\ \text{or}\ e\ge W-d_1.
\tag{4.3}
\]

Define distance to the nearer legal band by

\[
 v_2(r)=\min\bigl((a-A)_+,(W-d_2-e)_+\bigr),
\tag{4.4}
\]

\[
 v_3(r)=\min\bigl((a-C)_+,(W-d_1-e)_+\bigr).
\tag{4.5}
\]

Seam-crossing runs are boundary particles and are omitted.  The smallest
dense count-free objective used here is

\[
 Q_\sigma(T)=\left(\max_r v_r,\ \sum_r v_r\right)
\quad\text{lexicographically}.
\tag{4.6}
\]

It satisfies \(Q_\sigma=(0,0)\) iff this literal schedule absorbs every
internal short run.  It rewards position changes even when the number of
runs is unchanged or increases.  Squared distance and run censuses are only
deterministic diagnostics/tie breakers.

The `G2Q` portfolio order is

\[
 \left(-G_2,\ \max_r v_r,\ \sum_r v_r\right).
\tag{4.7}
\]

Exact \(\Phi\) is used only at checkpoints and for final certification.

## 5. Physical move and hard-gate scope

The C6 move is the smallest balanced physical three-segment rethread: three
old factor edges on a rank-ten cap triangle are replaced on the same three
rank-eight facet rows.  A candidate is retained only if it satisfies all of
the following literally.

1. No reference-protected physical edge changes.
2. Every replacement remains on the same rank-eight facet.
3. Every rank-nine owner retains degree two.
4. No loop or duplicate physical edge is created.
5. Every rank-ten cap load remains at least one.
6. The rank-nine factor remains one 24,310-owner component.
7. The carried seam is q1-safe and, in these runs, unprotected.

The full owner cycle is rebuilt for every retained candidate.  Thus a C6 or
C8 that reverses/reorders long path fragments moves all enclosed particles in
the score even when their local run lengths do not change.

The star-C8 layer replays every connected cap-safe row from the complete
rank-seven-core directed catalogue and applies the same gates and objective.
The present C8 certificate does not cover rank-six-core octahedral C8s,
paired modules, individually cap-debt modules, or compound exchanges.

## 6. Seed authentication

### 6.1 Equivariant 4,199

The factor is

`scratch/k17_c68b_double_fusion_residence_greedy_20260802/c68b.greedy48.factor.tsv`

with SHA-256

`b1343737cb0e3d99dec503e526e566521504478af1c5792c9a7949b6a5796616`.

It has 3,944 protected edges, one physical component, all 19,448 rank-ten
caps, and short census \((0,2312,1887)\).  Its 4,199 short runs form 247
coordinate-rotation orbits, so orbit-tied moves remain subject to the
equivariant no-go.  The search applies individual physical moves and breaks
that tie.

### 6.2 Non-equivariant 4,820

The factor is

`scratch/k17_marker58_upper_q1_quotient_audit_20260802/c68b.residence_greedy.factor.tsv`

with SHA-256

`f037fd236daf9eee231f0b35b46a8e1eecd7c0123eed96acc23524f71c676c0a`.

It is the deterministic 355-C6 endpoint rethread from the connected
equivariant marker58 base.  The original producer and its complete move log
are frozen in `producer4820/`.  Relative to the base, 1,001 rows are removed
and 1,001 added, no protected row changes, and one-step coordinate rotation
misses 172 selected edges.  Exact resources are:

| resource | value |
|---|---:|
| rank-eight facets | 24,310, each load one |
| rank-nine owners | 24,310, each degree two |
| rank-ten caps | 19,448, zero holes |
| cap loads 1/2/3/4/5 | 16,737 / 1,597 / 128 / 935 / 51 |
| protected edges | 3,944, unchanged from reference |
| owner components | one |

The new evaluator freezes the previously missing explicit cycle TSV.

## 7. Finite search results

The projected schedules used for hot-loop scoring were

| seed | anchor | \((A,C,d_1,d_2)\) | cost |
|---|---:|---:|---:|
| 4,199 | 20,988 | \((3469,3689,231,12)\) | 7,401 |
| 4,820 | 511 | \((967,2273,2733,1428)\) | 7,401 |

Both anchors retain a q1-safe unprotected wrap.  A symmetric
\((1850,1850,1851,1850)\) portfolio was also searched; it reached different
count-free local minima but did not change exact \(\Phi\) or \(G_2\).

The principal terminal comparison is

| branch | accepted C6 | \((N_1,N_2,N_3)\) | \(G_2\) | \(\Phi\) | \(\max v\) | \(\sum v\) |
|---|---:|---:|---:|---:|---:|---:|
| 4,199 seed | 0 | \((0,2312,1887)\) | 63 | 48,494 | 10,407 | 18,378,438 |
| 4,199 C6 local min | 52 | \((0,2344,1914)\) | 63 | 48,494 | 10,383 | 17,777,211 |
| 4,820 seed | 0 | \((0,2764,2056)\) | 41 | 48,538 | 10,943 | 21,429,419 |
| 4,820 `G2Q` local min | 54 | \((0,2777,2095)\) | 71 | 48,507 | 10,922 | 20,122,892 |

At the non-equivariant terminal factor, a final complete C6 scan has:

| counter | value |
|---|---:|
| raw cap-triangle triples | 2,333,760 |
| active alternating C6s | 48,366 |
| protected-blocked | 21,742 |
| cap-complete | 1,069 |
| connected and seam-safe | 542 |
| strict `G2Q` improvements | 0 |

The terminal star-C8 catalogue has 74,087 active directed rotations, 172
cap-complete candidates, and 59 connected candidates.  Strict replay finds
zero `G2Q` improvements.  The equivariant-derived C6 local minimum likewise
has zero improvements among 507 connected cap-safe C6s and 97 connected
star-C8s.

The improvement is real but quantitatively small:

\[
 41\longrightarrow71\ll20610,
 \qquad
 48538\longrightarrow48507\gg7401.
\]

This sharply redirects the next finite model toward compound/paired segment
modules capable of concatenating macroscopic clean gaps.  More single C6s or
rank-seven star-C8s under the frozen seams cannot advance the terminal
`G2Q` factors.

## 8. Downstream scope retained

A future \(\Phi\le7401\) incumbent would establish only the exact
no-singleton row-OR/scalar middle gate and its explicit deadline schedule.
It must then separately pass all of the following.

1. q1 boundary realization, including the removed rank-eight facet and
   repeated rank-ten cap witness;
2. ranks 11--17 consecutive-union replay;
3. the P/Q lower atlas and occurrence matching;
4. lower Hall and common-cap conditions;
5. source-letter assignment and protected traces;
6. the literal lower/common-cap compiler and final word verifier.

The present package validates physical rank 8/9/10 resources, connectivity,
protected-reference equality, chronology, \(G_2\), and \(\Phi\).  It makes no
claim for any item above and no SAT/UNSAT claim for the global compiler.

## 9. Frozen package and use

Package:

`scratch/v_k17_phi_absorber_rethread_20260802/`

Evaluator build and use:

```text
g++ -std=c++20 -O3 -DNDEBUG -march=native \
  evaluate_v_k17_physical_phi_g2_20260802.cpp -o evaluate_phi_g2

./evaluate_phi_g2 FACTOR.tsv OUTPUT_PREFIX [PROTECTED_REFERENCE_FACTOR.tsv]
```

C6 search:

```text
./search_c6_absorber FACTOR.tsv REFERENCE.tsv ANCHOR A C D1 D2 \
  REQUIRE_UNPROTECTED MAX_ITERS [G2Q] OUTPUT_PREFIX
```

Star-C8 rescoring:

```text
./rescore_star_c8 FACTOR.tsv REFERENCE.tsv VALID.tsv ANCHOR A C D1 D2 \
  REQUIRE_UNPROTECTED [G2Q] OUTPUT_PREFIX
```

`SHA256SUMS` binds every proof-safe source, factor, cycle, run/cut table,
search certificate, catalogue, and imported 4,820 producer artifact.

