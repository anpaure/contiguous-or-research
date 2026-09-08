# The reusable six-piece odd-to-even intersection lift

Date: 2026-07-28

## 1. Exact finite theorem

Let `K=2r`, let `X` have size `K-1`, and let `z` be the new coordinate.
Put

\[
 W=\binom{K-1}{r}=\binom{K-1}{r-1},
 \qquad W_K=\binom Kr=2W,
 \qquad d=d(K).
\]

Let

\[
 A=(A_0,\ldots,A_{W-1})\subseteq\binom Xr,
 \qquad
 B=(B_0,\ldots,B_{W-1}),\quad
 B_i=\{z\}\cup C_i, C_i\in\binom X{r-1},
\]

enumerate their respective layers exactly once.  Choose

\[
 0\le a_0<a_1<W-1,qquad 1\le b,qquad b+d+1<W,
\]

and split

\[
\begin{aligned}
 A_1&=A[0,a_0],& A_2&=A[a_0+1,a_1],& A_3&=A[a_1+1,W-1],\\
 B_1&=B[0,b-1],& B_2&=B[b,b+d],& B_3&=B[b+d+1,W-1].
\end{aligned}
\]

Independently orient the six pieces and concatenate them in an alternating
`A/B` order, obtaining `T`.

For a middle path `R`, write

\[
 \mathcal U_q(R)=
 \left\{\bigcup_{j=0}^q R_{i+j}:0\le i<|R|-q\right\}.
\]

For the chosen six oriented pieces, let `I_q` be the union colours of the
length-`q+1` windows lying wholly inside one piece, and let `N_q` be those
crossing one of the five new seams.  Reversal does not change an internal
window's union, so the exact seam identity is

\[
 \boxed{\mathcal U_q(T)=I_q\cup N_q.}
\tag{1.1}
\]

Assume:

1. every new seam is a Johnson edge;
2. `T` is linearly depth-`d` resident, i.e. with
   \[
   E_j=\bigcap_{\max(0,j-d)\le i\le\min(j,W_K-1)}T_i
   \]
   one has
   \[
   T_i=E_i\cup\cdots\cup E_{i+d}\quad(0\le i<W_K);
   \tag{1.2}
   \]
3. for every `1<=q<=r`,
   \[
   \binom{X\cup\{z\}}{r+q}\subseteq I_q\cup N_q;
   \tag{1.3}
   \]
4. the depth-`d` lower compiler is feasible: there are nonzero
   `e_j subseteq E_j`, `0<=j<W_K+d`, such that
   \[
   e_i\cup\cdots\cup e_{i+d}=T_i
   \tag{1.4}
   \]
   and every nonempty mask of rank below `r` is a union of a contiguous
   interval of the `e_j`.

Then `e_0,...,e_(W_K+d-1)` is universal and

\[
 \boxed{\nu(K)=B(K)=W_K+d.}
\tag{1.5}
\]

Indeed, (1.4) covers the lower ideal and realizes the entire middle layer.
Every colour in (1.3) is the union of consecutive middle cells and hence of
one longer contiguous interval of the `e_j`.  The monotone-deadline theorem
is the matching lower bound.

This theorem is deliberately finite and fail-closed.  Conditions (1.1)--
(1.4) are exactly what the search and independent verifier check; no random
or asymptotic hypothesis is hidden in it.

## 2. Why two A cuts and one B ear are canonical

The `B` ear has length exactly `d+1`.  If it is internal in the braided path,
its two neighbouring pieces are `A` pieces, so the incidence word of `z`
has a maximal run of exactly `d+1`.  Its depth-`d` erosion has one `z` slot.
This is the unique local geometry capable of realizing the singleton `{z}`.
It is necessary but not sufficient: another coordinate can still be forced
into that slot, which is why the Hall/compiler check remains.

Cutting the ear removes precisely two first-upper colours,

\[
 U^-=(B_{b-1}\cup B_b)\setminus\{z\},\qquad
 U^+=(B_{b+d}\cup B_{b+d+1})\setminus\{z\}.
\tag{2.1}
\]

Both are rank-`r` subsets of `X`, so both occur as vertices of `A`.  The two
`A` cuts are taken immediately before or after those vertices.  If an exposed
vertex `U` is joined to `{z}\cup C` with `C subset U`, the seam is a Johnson
edge and its union is exactly `{z}\cup U`, restoring the lost `B` colour.
Thus the two B boundary colours determine the two A cut locations up to only
four side choices.  This collapses a nominal three-cut search from cubic to
linear size.

At depth one, the remaining exact condition is: every uniquely represented
colour lost at an A cut or at the original A/B seam has a surviving or new
witness.  At higher depths the same statement is precisely (1.1): only the
bounded collars of the old and new seams need be compared.

## 3. Intersection source and what it guarantees

Let `P=(P_0,...,P_(W-1))` be a Hamilton path through
`binom(X,r)` whose adjacent intersections are distinct.  They use `W-1` of
the `W` rank-`r-1` masks; call the missing one `L`.  If `L subset P_0` or
`L subset P_(W-1)`, orient `P` so `L subset P_(W-1)` and form

\[
 Q=(L,\ P_0\cap P_1,\ P_1\cap P_2,\ldots,
 P_{W-2}\cap P_{W-1})
\tag{3.1}
\]

(or its reverse).  Consecutive terms after `L` are distinct rank-`r-1`
subsets of the same `P_i`, hence Johnson adjacent; `L` and the adjacent
intersection are also distinct subsets of the endpoint.  Therefore `Q` is
a Hamilton path through `binom(X,r-1)`.  Consequently

\[
 A=P,\qquad B=\{z\}+Q
\tag{3.2}
\]

partition the even middle layer exactly.  These facts are automatic from a
lower-rainbow odd carrier with an endpoint-accessible hole.

Residence is not automatic.  On a coordinate incidence word, adjacent
intersection erodes every one-run by one.  Thus a clean sufficient condition
for `Q` to be depth-`d` resident is that all relevant one-runs of `P` have
length at least `d+2`, together with the endpoint check at the inserted `L`.
In particular, an odd depth-`d+1` carrier naturally feeds an even depth-`d`
lift.  An odd depth-`d` carrier does not naturally feed an even depth-`d`
lift.

The endpoint upper-hole family of `Q`, the nested flag that aligns it with
the suffix of a (possibly different) A source, the six Johnson seams, the
higher seam collars, and lower compiler feasibility are still existential.
Odd optimality alone guarantees none of them.

## 4. Parameterized algorithm

For every B-ear position:

1. compute the two lost colours (2.1);
2. look up their two positions in `A`;
3. try the four before/after choices for the A cuts;
4. try the 2304 alternating oriented six-piece templates, modulo whole-path
   reversal;
5. reject by the five endpoint tests, then residence, singleton capacity,
   upper collars, scalar Hall, and finally the exact compiler.

The outer search is `O(W)` times a fixed 2304-template catalogue, not
`O(W^3)`.  The implementation is
`scratch/search_odd_even_six_piece.cpp`; strict source construction is
`scratch/build_odd_even_intersection_carriers.py`; materialization is
`scratch/materialize_odd_even_six_piece.py`.

On the exact `k=14` source, the C++ search examines only 159 endpoint-passing
templates, 29 residence-passing templates, and one upper/Hall-perfect
template.  It takes about 0.06 seconds after compilation.  The lower compiler
takes 0.79 seconds.

## 5. Finite calibration

| lift | target depth | source used | intersection-sector audit | six-piece/compiler |
|---|---:|---|---|---|
| `5 -> 6` | 1 | exhaustive normalized lower-rainbow `k=5` paths | a resident source exists, but no strict upper-perfect A/B concatenation exists | SAT; exact length 21 |
| `7 -> 8` | 2 | exact `k=7` word | every one of 12 oriented Johnson completions is nonresident; minimum 26 failures | 175 endpoint-valid braids, zero resident braids |
| `9 -> 10` | 2 | exact `k=9` word | every one of 16 oriented Johnson completions is nonresident; minimum 68 failures | 186 endpoint-valid braids, zero resident braids |
| `11 -> 12` | 2 | two exact `k=11` carriers | 8 usable B carriers and 42 strict upper-perfect carriers | SAT; exact length 926 |
| `13 -> 14` | 2 | exact `k=13` carrier family | 100 calibrated strict carriers; 35 admit a six-piece braid | SAT; exact length 3434 |

The new `k=12` certificate is
`scratch/k12_intersection_sixpiece_hallpass_001.word`, SHA-256

`a29517e67dd3c9db5f773f5332b3e3e44197cfe79d3d8014ea0770c9bedeb482`.

It is built from cuts `[66,459]`, B cut `409`, and pieces

`A1R B1F A2R B2R A3F B3R`.

The compiler is SAT in 0.0306 seconds and an independent enumeration covers
all 4095 nonempty masks.

The `k=6` calibration is stronger than a replay of the known word.  Among
600 symmetry-normalized lower-rainbow `k=5` paths, a resident intersection
prelift exists.  The six-piece search repairs its non-perfect upper seam and
the compiler produces a length-21 word covering all 63 nonempty masks.  The
word is `scratch/k6_intersection_sixpiece_exact.word`, SHA-256

`036b9efb42d1feb3a3fcbf82af3cc10772264567647b31d705752466bf551b43`.

The failures at `7 -> 8` and `9 -> 10` are predicted by the unchanged depth:
`d(7)=d(8)=2` and `d(9)=d(10)=2`.  The successes at `11 -> 12` and
`13 -> 14` exploit `3 -> 2`.  The six-piece braid repairs seams; it cannot
repair dozens of residence failures lying inside B pieces.

## 6. Exact target for `15 -> 16`

Here `d(15)=d(16)=3`, so the favourable depth drop is absent.  A reusable
intersection lift needs two odd sources (which may be different):

1. an A source that is depth-three resident, lower-rainbow with an
   endpoint-accessible hole, and upper-complete;
2. a B source whose completed adjacent-intersection path is depth-three
   resident.  A clean sufficient condition is **depth-four residence of the
   B source**, i.e. relevant one-runs of length at least five;
3. a nested endpoint upper-hole family for the B source, alignable with an A
   suffix flag;
4. a length-four B ear whose two lost colours occur at two nondegenerate A
   cut positions;
5. an alternating orientation passing the Johnson, depth-three residence,
   and higher seam-collar identities;
6. the depth-three lower compiler.

The present `k=15` PBBS object does not satisfy item 1 yet: it is a 17-cycle
factor with 45 depth-three residence violations, reduced to a 38-segment
splice problem.  More decisively, a direct one-step-stronger audit finds
**1020 depth-four residence violations on eight physical cycles** (a greedy
cut cover already needs 533 cuts, versus 23 at depth three).  Thus item 2 is
not a small strengthening of the current 38-segment splice; it needs a
different B-source objective.  The useful refinement is that A and B need not
be the same source.  The old shared-tail route asked one chronology to be
bi-resident; the intersection route asks for one ordinary A chronology and
one one-sided over-resident B chronology, which is different and potentially
weaker.

Once such sources exist, the parameterized search already supports `K=16`,
`d=3`, and automatically uses a four-vertex ear.  The remaining unknown is
the source, not the braid enumerator.

## 7. Guaranteed versus existential

| property | follows from a suitable odd lower-rainbow carrier? |
|---|---|
| two target middle sectors partition exactly | yes |
| completed intersection row has every `(r-1)`-set once | yes, if the hole is endpoint-accessible |
| two B-ear lost q1 colours occur somewhere in A | yes |
| target-depth residence of A | only if assumed for A |
| target-depth residence of completed intersection row | only with one extra run unit / direct audit |
| nested endpoint upper-hole family | no |
| five new Johnson seams | no, finite search |
| higher upper seam identities | no, finite audit |
| singleton `{z}` | ear supplies the unique local slot; global pin freedom is not automatic |
| full lower compiler | no |

Thus the six-piece construction is now a genuine reusable finite lift, but
not an unconditional recurrence `nu(2r-1)=B -> nu(2r)=B`.
