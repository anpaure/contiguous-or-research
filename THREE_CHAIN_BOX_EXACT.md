# Exact reconnaissance for the three-chain box problem

## 1. Local problem and a useful normalization

Let

\[
P(p,q,r)=[0,p]\times[0,q]\times[0,r].
\]

The point `(x,y,z)` is represented by the first `x`, first `y`, and first
`z` increments in three disjoint chains.  Write `g_3(p,q,r)` for the least
length of a word whose nonempty contiguous joins contain every nonzero point
of `P(p,q,r)`.

The entries may initially be arbitrary subsets of the `p+q+r` increments,
but this extra freedom is illusory.

### Prefix-closure lemma

Every word can, without increasing its length or destroying a box-point
witness, be replaced by a word all of whose entries are themselves box
points.

For an entry `X`, let `cl(X)` be the least box point containing `X`: in each
coordinate chain, fill all increments below the highest increment of `X`.
If an interval has join equal to a box point `T`, every entry `X` in that
interval satisfies `X subseteq T`; hence `cl(X) subseteq T`.  Replacing every
entry by its closure leaves that interval join equal to `T`.  Zero entries
can be deleted in the nonzero problem.

Consequently, `g_3` is exactly the shortest sequence of triples

\[
             a_i=(x_i,y_i,z_i)\in P(p,q,r)\setminus\{(0,0,0)\}
\]

such that every nonzero triple is the coordinatewise maximum of one
contiguous interval.

This normalization is both mathematically useful and built into the exact
solver `three_box_exact_sat.cpp`.

## 2. Box rank-slack bound

Let

\[
m_s=[z^s](1+\cdots+z^p)(1+\cdots+z^q)(1+\cdots+z^r),
\qquad L_s=\sum_{j=1}^{s-1}m_j.
\]

The interval-slack proof applies verbatim to this graded poset:

\[
g_3(p,q,r)\ge B_\Box(p,q,r)
 :=\max_s(m_s+\tau_s),
\]

where `tau_s` is the least nonnegative `t` satisfying

\[
                  L_s\le t m_s+{t+1\choose2}.                 \tag{2.1}
\]

For the even cube `p=q=r=2a`, the middle layer has

\[
M_a=3a^2+3a+1,
\qquad
L_a={ (2a+1)^3-M_a\over2}-1.
\]

The middle-rank delay in (2.1) is **exactly**

\[
                         \tau_{3a}=\left\lceil{4a\over3}\right\rceil. \tag{2.2}
\]

This follows by substituting `a=3u,3u+1,3u+2`.  If
`d=ceil(4a/3)` and `F(d)=dM_a+d(d+1)/2`, the two positive gaps are:

| `a` | `F(d)-L_a` | `L_a-F(d-1)` |
|---|---:|---:|
| `3u` | `(7u^2+3u+2)/2` | `(47u^2+23u)/2` |
| `3u+1` | `(43u^2+49u+16)/2` | `(11u^2+13u+2)/2` |
| `3u+2` | `(25u^2+45u+22)/2` | `(29u^2+53u+22)/2` |

For the first three even cubes, direct evaluation of every rank gives

| side `2a` | width `M_a` | full `B_Box` |
|---:|---:|---:|
| 2 | 7 | 9 |
| 4 | 19 | 22 |
| 6 | 37 | 41 |

Thus a `width+O(side)` local theorem has the correct possible order, but
equality with the rank-slack expression is already false in the smallest
cube.

## 3. First exact values

The proof-equivalent SAT model and an independent interval enumerator give:

| `(p,q,r)` | width | `B_Box` | `g_3` |
|---|---:|---:|---:|
| `(1,1,1)` | 3 | 4 | 4 |
| `(1,1,2)` | 4 | 5 | 5 |
| `(1,1,3)` | 4 | 6 | 7 |
| `(1,1,4)` | 4 | 6 | 8 |
| `(1,2,2)` | 5 | 7 | 7 |
| `(1,2,3)` | 6 | 8 | 9 |
| `(1,2,4)` | 6 | 8 | 11 |
| `(1,3,3)` | 7 | 9 | 11 |
| `(2,2,2)` | 7 | 9 | **10** |
| `(2,2,3)` | 8 | 10 | 12 |

The non-cubic rows currently have solver UNSAT logs plus independently
verified SAT words.  The `(2,2,2)` row additionally has a checked DRAT
certificate, described next.

All displayed upper words are preserved in
`three_box_certificates/small_words/` and pass the independent verifier.

## 4. Certified theorem: `g_3(2,2,2)=10`

Use bits `0,1`, `2,3`, `4,5` for the three two-step chains.  The word

```text
4 12 20 48 1 16 3 5 13 21
```

or, in triple notation,

```text
(0,1,0) (0,2,0) (0,1,1) (0,0,2) (1,0,0)
(0,0,1) (2,0,0) (1,1,0) (1,2,0) (1,1,1)
```

covers all 26 nonzero points.  Shortest witnesses are:

| target | interval | target | interval |
|---|---:|---|---:|
| `(1,0,0)` | `[5,5]` | `(2,0,0)` | `[7,7]` |
| `(0,1,0)` | `[1,1]` | `(1,1,0)` | `[8,8]` |
| `(2,1,0)` | `[7,8]` | `(0,2,0)` | `[2,2]` |
| `(1,2,0)` | `[9,9]` | `(2,2,0)` | `[7,9]` |
| `(0,0,1)` | `[6,6]` | `(1,0,1)` | `[5,6]` |
| `(2,0,1)` | `[6,7]` | `(0,1,1)` | `[3,3]` |
| `(1,1,1)` | `[10,10]` | `(2,1,1)` | `[6,8]` |
| `(0,2,1)` | `[2,3]` | `(1,2,1)` | `[9,10]` |
| `(2,2,1)` | `[6,9]` | `(0,0,2)` | `[4,4]` |
| `(1,0,2)` | `[4,5]` | `(2,0,2)` | `[4,7]` |
| `(0,1,2)` | `[3,4]` | `(1,1,2)` | `[3,5]` |
| `(2,1,2)` | `[3,7]` | `(0,2,2)` | `[2,4]` |
| `(1,2,2)` | `[2,5]` | `(2,2,2)` | `[2,7]` |

### Proof-producing lower certificate

For length nine the generator creates Boolean entry-bit variables and one
witness variable for every target/interval pair.  A witness implication:

1. forbids every bit outside the target on the interval; and
2. requires every bit inside the target to occur somewhere on the interval.

Every target has an at-least-one-witness clause.  Prefix-closure and nonzero
clauses are justified by Section 1.  Safe witness-length pruning follows
from the rank-slack theorem: a target below rank `s` cannot use an interval
longer than `n-m_s`.

Hence the CNF is satisfiable iff a length-nine box word exists.  It contains
786 variables and 6,524 clauses.  Kissat produced a 5,734,982-byte DRAT
refutation.  `drat-trim` checked it independently:

```text
c parsing input formula with 786 variables and 6524 clauses
c detected empty clause; start verification via backward checking
c 92577 of 135328 lemmas in core using 8142521 resolution steps
s VERIFIED
```

Artifacts are in `three_box_certificates/cube_2/`.  The uncompressed proof
hash is recorded in the remote log; local hashes are:

```text
7da69eafc5c4c4d3778f5c0134d5ddb36d63bb59d51e2f3430e47abbf12f6a0f  cube222_n9.cnf
bd9693db493ded033995cf5433c81077cb4fe0ee590cfabe8dfaf6a1bea64d62  cube222_n9.drat.gz
ea1d7e9b7c72f46df3e4aca948207d1407cda8d66a76102515ea336295a74fbb  2_2_2_n10.word
```

## 5. The first geometric pattern: an inward hexagonal spiral

The seven middle-rank targets, ordered by the left endpoints of their
shortest witnesses, are

\[
\begin{aligned}
&(0,2,1),(0,1,2),(1,0,2),(2,0,1),\\
&(2,1,0),(1,2,0),(1,1,1).
\end{aligned}
\]

The first six form the boundary hexagon of the middle slice; the final point
is its center.  Consecutive points exchange one unit between two coordinates.
The selected witness intervals are

```text
[2,3] [3,4] [4,5] [6,7] [7,8] [9,9] [10,10]
```

so, relative to the sorted index `i`, the monotone band states are

```text
12 12 12 23 23 33 33.
```

This gives a canonical all-side candidate ordering.  For side `2a`, center
the middle slice at `(a,a,a)` and visit the hexagonal rings of radii
`a,a-1,...,1,0` inward.  On a radius-`h` ring start at `(-h,h,0)` and use
the six directions

```text
(0,-1,+1), (+1,-1,0), (+1,0,-1),
(0,+1,-1), (-1,+1,0), (-1,0,+1).
```

The end of each ring is adjacent to the beginning of the next.  This is a
Hamilton path through the middle layer, with exactly
`1+6(1+...+a)=3a^2+3a+1` vertices.

The pattern is real but not by itself a construction: Kissat returned UNSAT
when this exact central order was forced at side four and length 23.  A DRAT
proof was not retained for that much larger exploratory instance, so this is
a computational rejection of the ansatz rather than a new formal theorem.
Thus the innermost/outermost ring phases, the shell order, or the selected
central witnesses must be modified.  The simple unchanged spiral does not
recursively lift.

Every deletion and every adjacent contraction of the ten-term side-two word
loses at least one target.  The observed recursion is therefore in the
middle-layer shell ordering, not in literal deletion of a word position.

## 6. Structural warning: a fixed derivative row cannot work

For an even cube of side `2a`, the three top increments each occur in exactly
`a+1` middle-layer points, and no middle point contains two of them.  If a
permutation `T` of the middle layer factored as `T=D^t A`, every internal
coordinate run would have length at least `t+1`.  For `t>=a+1`, each of the
three rare, pairwise-disjoint supports would therefore have to touch one of
only two row boundaries—impossible.

The rank-slack delay always satisfies `t>=a+1`.  Hence a near-bound word must
use variable central witness lengths (a monotone-band/flagged construction),
not one fixed window row.  The side-two certificate demonstrates exactly
this: its central witnesses have both lengths one and two and occupy three
different band states.

## 7. Current computational status

All substantive solving was run remotely in visible `tmux` sessions.  No
heavy search was run on the Mac.

For side four:

* `B_Box(4,4,4)=22`;
* an unconstrained length-22 search reached its time limit without a result;
* Kissat rejects the unchanged inward-spiral ansatz at length 23 (exploratory;
  no retained DRAT certificate);
* the search priority is now a feasible near-bound word with variable shell
  phases/flags, rather than a large unrestricted optimality run.

The exact source, decoder, verifier, rank table, shortest-witness printer, and
word analyzer are all in `three_box_exact_sat.cpp`.

## 8. Shadow pattern of the Hamilton hex spiral

For the genuine outer-to-inner Hamilton spiral (with adjacent ring seams),
direct enumeration at sides 2, 4, and 6 gives a remarkably rigid pattern.

* Every consecutive-union shadow at every rank above the middle is complete.
* The consecutive-intersection shadows below the middle miss precisely

\[
 \{(0,y,z):1\le y\le 2a,\ 0\le z\le a-1\}.          \tag{8.1}
\]

Thus the numbers of missed lower points are `2,8,18=2a^2`.  Although this is
quadratic, (8.1) is a two-chain rectangle and has its own contiguous-join word
of length only

\[
                         2a+(a-1)=3a-1.              \tag{8.2}
\]

This pattern is verified data for `a<=3`, not yet a proved all-`a` theorem.
It explains why a hexagonal construction remains attractive: the upper half
is already perfect and the lower shadow defect has linear encoding cost.
The unresolved step is realizing the intersection shadows as actual OR
windows of one factor; envelope coverage alone is not pin labelability.

## 9. Closed radial band: exact failure decomposition

The closed radial shadow row repeats the starting corner at the end of every
ring.  It has

\[
L=M_a+a
\]

central occurrences.  A radius-`s` occurrence is assigned
`I_i=[i,i+s]`, giving factor length `L+a`; initially one additional boundary
slot was proposed.

The audit separates three gates.

1. **Central factorability passes.**  Coordinatewise interval stabbing has
   zero failures for the tested `a`.
2. **Positive-envelope containment is too weak.**  Matching a target `S` to
   an interval `J` merely because `S` lies in the OR of the maximal envelopes
   ignores bits that the central windows force somewhere inside `J`.
3. **Central-witness avoidance is the correct cardinal gate.**  Any
   below-middle witness must avoid containing an entire `I_i`.

For the closed row,

\[
 \sum_i s_i=\sum_{s=1}^a s(6s+1)
            ={a(a+1)(4a+3)\over2}.                  \tag{9.1}
\]

With `q` free boundary positions, the total avoidance capacity is at most

\[
              \sum_i s_i+{a+q+1\choose2}.           \tag{9.2}

At `a=2,q=1`, this is

\[
                    33+{4\choose2}=39<52,
\]

so the proposed side-four band is cardinally impossible before any pinning
question.

At `a=1,q=1`, the capacity count does not rule it out, but exact pinning does.
The central constraints together with only four lower targets

\[
                         \{x_1,y_1,z_1,x_1z_1\}
\]

are already inconsistent.  The forced central labels include

\[
 A_2=x_1x_2,\ A_3=x_1y_1,\ A_4=y_1y_2,\
 A_5=y_1z_1,\ A_6=z_1z_2,
\]

with `A_1` containing `z_1`, `A_7` containing `x_1`, and `A_8` containing
`x_1x_2`.  The three atom targets therefore force the only free tail to be
`y_1`, force `A_1=z_1`, and force `A_7=x_1`.  No interval can then equal
`x_1z_1`: the middle route contains a forbidden higher or `y` bit, `A_8`
contains `x_2`, and the tail contains `y_1`.

Two free tail slots do make the `a=1` band SAT, at length 11.  Therefore the
closed band is a useful shadow scaffold but does not attain the proposed
`M+2a+1` formula.

A second family, alternating singleton and adjacent-pair states at ring
corners, was exhaustively tested at `a=1` over 84 phase/orientation/state-cut
variants.  Every instance was solver-UNSAT.  No DRAT certificates were
retained for this exploratory family, so this is evidence rejecting that
specific ansatz, not a general theorem about all variable bands.

## 10. Exact band-capacity objective and central-order search

For a central order `T_0,...,T_(M-1)`, write

\[
 I_i=[i+\alpha_i,i+\beta_i],\qquad
 0\le\alpha_0\le\cdots\le\alpha_{M-1}\le D,
\]

with the analogous monotonicity for `beta` and `alpha_i<=beta_i`.  Every
internal coordinate run `[u,v]` imposes

\[
                   \beta_{u-1}-\alpha_{v+1}\le v-u. \tag{10.1}
\]

Put `alpha_{-1}=0`.  The exact number of physical intervals of length at most
`D` that contain no selected central witness is

\[
 C(\alpha,\beta)=
 \sum_{i=0}^{M-1}\sum_{t=\alpha_{i-1}}^{\alpha_i}(\beta_i-t)
 +{D-\alpha_{M-1}+1\choose2}.                       \tag{10.2}

Formula (10.2), rather than just the number of maximum-length witnesses, is
the correct first objective for central-order discovery.

`three_box_band_opt.cpp` generates an exact integer optimization model for
(10.1)--(10.2).  At `a=2,D=3`, where 52 lower targets must be accommodated,
the current exact fixed-order results are:

| Hamilton order | max avoidance `C` | full-length witnesses | gap sum |
|---|---:|---:|---:|
| outer-to-inner hex spiral | **43** | 7 | 37 |
| row snake | 30 | 6 | 24 |
| sector weave | 20 | 4 | 14 |
| heuristic order optimized for full block | 32 | 8 | 26 |

The last row is instructive: it reaches the crude defect requirement of eight
full-length witnesses but has avoidance capacity only 32.  Full-count and
gap-sum proxies are therefore insufficient; future order search must optimize
(10.2) itself.

Random Hamilton 2-opt/3-edge/backbite search produced saved checkpoint orders
for `a=2,3,4`.  Their last proxy statistics were respectively:

```text
a=2: full block 8, short-run penalty 22
a=3: full block 13, short-run penalty 48
a=4: full block 17, short-run penalty 227
```

Only the `a=2` checkpoint was subsequently evaluated by the exact capacity
model, giving the fourth row of the table.  The `a=3,4` figures are heuristic
proxy scores, not capacity bounds and not existence/nonexistence results.
Artifacts are stored in `three_box_order_checkpoints/`.

## 11. Clean stopping ledger

Rigorous new result:

* `g_3(2,2,2)=10`, with checked DRAT lower certificate and explicit verified
  word.

Solver-supported but not proof-certificate-retained local data:

* the remaining small table in Section 3;
* rejection of the unchanged side-four spiral and the 84 corner-band variants.

Conclusive mathematical eliminations:

* one fixed derivative row at rank-slack delay;
* the closed radial band at `a=2,q=1` by avoidance capacity;
* the closed radial band at `a=1,q=1` by the four-target pin conflict.

Still open:

* the three-chain surface-error theorem;
* a central Hamilton order and variable band with avoidance capacity matching
  the lower volume;
* exact `g_3(3,3,3)`.  Here the full box rank-slack bound is 15 (the upper of
  the two middle ranks strengthens the lower-middle value 14).  Both exact
  length-15 SAT runs timed out, and the best local-search candidate covered
  58 of 63 targets; neither SAT nor UNSAT is claimed.

All remote `three_box_*` search sessions launched in this pass were stopped
after their checkpoints and logs were saved.
