# The Catalan braid hidden in the two-coordinate lift

Date: 2026-07-27

This note isolates what the two-coordinate diamond lift really has to do.
It proves the block-count identities, records a universal averaging lemma,
and checks the resulting normal form against the stored central paths at
`k=7,9,11`.  It also proves a one-hole obstruction for the purely
chronological lift.  Thus the old construction is not failing because of
residence: residence-compatible batching is already present.  At `k=11` the
remaining defect is twelve upper colours plus one forced boundary hole.

## 1. Four sectors

Let the old ground set have size `2m+1`, and add two points `x,y`.  Put

\[
 W=\binom{2m+1}{m}=\binom{2m+1}{m+1},\qquad
 N=\binom{2m+1}{m+2}=\frac{m}{m+2}W.
\]

The new middle layer, of rank `m+2`, has four sectors

\[
\begin{array}{c|c|c}
\text{sector}&\text{vertex}&\text{count}\\ \hline
A& R+xy,\quad |R|=m&W\\
X& T+x,\quad |T|=m+1&W\\
Y& T+y,\quad |T|=m+1&W\\
U& V,\quad |V|=m+2&N.
\end{array}
\tag{1.1}
\]

For a Hamilton path `P` in this layer, let `b_S` be the number of maximal
blocks of sector `S`, let `epsilon_S` be the number of the two path endpoints
that lie in `S`, and let `e_ST` count transitions between distinct sectors.
Write `t=e_XY`.

The possible sector transitions and their immediate lower/upper colours are

\[
\begin{array}{c|c|c}
\text{edge}&\text{intersection}&\text{union}\\ \hline
AA&(m-1)+xy&(m+1)+xy\\
AX&m+x&(m+1)+xy\\
AY&m+y&(m+1)+xy\\
XX&m+x&(m+2)+x\\
YY&m+y&(m+2)+y\\
XU&m+1&(m+2)+x\\
YU&m+1&(m+2)+y\\
UU&m+1&m+3\\
XY&m+1&(m+1)+xy.
\end{array}
\tag{1.2}
\]

Here the number before `+x`, etc., is the rank on the old ground set.  An
`XY` edge is possible only between `T+x` and `T+y` with the same `T`.
There is no `AU` edge.

## 2. The Catalan block inequalities

There are `W-b_A` internal `AA` edges.  They are the only edges that can
realise lower colours containing both new points.  There are `N` such
colours.  Therefore

\[
 H_A^-\ \ge\ \bigl(N-(W-b_A)\bigr)^+
       =\bigl(b_A-(W-N)\bigr)^+.
\tag{2.1}
\]

The lower colours containing neither new point are realised by `UU`, `XU`,
`YU`, and `XY`.  Since

\[
 e_{XU}+e_{YU}=2b_U-\epsilon_U,
\]

their total number of edge slots is

\[
 (N-b_U)+(2b_U-\epsilon_U)+t=N+b_U+t-\epsilon_U.
\]

Consequently

\[
 H_U^-\ \ge\
 \bigl((W-N)-b_U-t+\epsilon_U\bigr)^+.
\tag{2.2}
\]

Likewise the only sources for the `x`-only and `y`-only lower colours give

\[
 H_X^-\ge(b_X-e_{AX})^+,
 \qquad
 H_Y^-\ge(b_Y-e_{AY})^+.
\tag{2.3}
\]

The critical block count is

\[
 \boxed{b:=W-N=\frac{2W}{m+2}=C_{m+1}.}
\tag{2.4}
\]

The last equality follows from

\[
 C_{m+1}=\frac1{m+2}\binom{2m+2}{m+1}
        =\frac2{m+2}\binom{2m+1}{m}.
\]

Thus the phrase *Catalan batching* is literal.  At the no-waste lower
threshold, the `A` sector is a forest of exactly `C_{m+1}` paths and its
`N` internal edges use every old rank-`m-1` colour once.

## 3. Catalan centering is universal

The occurrence of the number `C_{m+1}` is not special to the stored paths.

### Lemma 3.1 (pair-block average)

Let `P` be any Hamilton path through the rank-`r` layer of `[K]`, where
`K=2r-1`, and let `M=binom(K,r)`.  For a pair `{x,y}`, let `b_{xy}` be the
number of maximal path blocks in which both coordinates occur.  Then

\[
 \frac1{\binom K2}\sum_{\{x,y\}}b_{xy}
 =\frac MK+\frac{r/2-1}{K}.
\tag{3.1}
\]

In particular, for `K=2m+3`, `r=m+2`,

\[
 \frac1{\binom K2}\sum b_{xy}
 =C_{m+1}+\frac{m}{2(2m+3)}<C_{m+1}+\frac14,
\tag{3.2}
\]

so some coordinate pair has `b_A<=C_{m+1}`.

#### Proof

The initial set starts `binom(r,2)` pair-blocks.  At each Johnson step one
new coordinate is inserted.  It starts a co-presence block with each of the
`r-1` retained coordinates, and starts no other pair-block.  Hence

\[
 \sum_{\{x,y\}}b_{xy}=\binom r2+(M-1)(r-1).
\]

Since `binom(K,2)=K(r-1)`, division gives (3.1).  Also `M/K=C_{m+1}` in the
specified parameters.  QED.

Thus every central Hamilton path has a pair whose `A` sector contains enough
internal edge slots to cover the complete both-new lower sector.  The open
part is rainbow selection, not block capacity.

The stored odd paths do substantially better than this averaging guarantee.
Their complete pair-block distributions are

\[
\begin{array}{c|c|c}
k&C_{m+1}&\text{distribution of }b_{xy}\\ \hline
7&5&5^{18},6^3\\
9&14&14^{30},15^6\\
11&42&42^{45},43^{10}.
\end{array}
\tag{3.3}
\]

Thus every pair is at the integer floor or ceiling.  The number of ceiling
pairs is exactly

\[
 \binom{m+1}{2},
\tag{3.4}
\]

which is forced by (3.2), because

\[
 \binom{2m+3}{2}\frac{m}{2(2m+3)}=\frac{m(m+1)}2.
\]

This *pair-run balance* is a new common invariant of all three stored odd
paths.  In particular, the good pair is not exceptional: at `k=11`, 45 of
the 55 coordinate pairs have the exact Catalan block count.

In fact this stronger statement follows from the one-hole lower-rainbow
property.

### Lemma 3.2 (one missing lower colour forces the complete block profile)

Let `K=2r-1`, and suppose a Hamilton path in the rank-`r` layer has distinct
immediate intersections and these intersections comprise every
rank-`r-1` set except `C_*`.  Then, for every coordinate pair `{x,y}`,

\[
 \boxed{b_{xy}=C_{r-1}+\mathbf 1_{\{x,y\}\subseteq C_*}.}
\tag{3.5}
\]

#### Proof

Let `V_xy` be the number of path vertices containing both `x,y`, and let
`E_xy` be the number of path edges whose two endpoints both contain them.
In the binary co-presence word of the pair, a run of length `ell` contributes
`ell` to `V_xy` and `ell-1` to `E_xy`.  Hence

\[
 b_{xy}=V_{xy}-E_{xy}.
\]

Hamiltonicity gives

\[
 V_{xy}=\binom{K-2}{r-2}.
\]

The edge intersections are the full rank-`r-1` layer minus `C_*`, so

\[
 E_{xy}=\binom{K-2}{r-3}
       -\mathbf 1_{\{x,y\}\subseteq C_*}.
\]

For `K=2r-1`, the difference of the two binomial coefficients is
`C_{r-1}`.  This proves (3.5).  QED.

For the stored paths, the exceptional coordinate cliques are

\[
\begin{array}{c|c}
k&C_*\\ \hline
7&\{1,5,7\}\\
9&\{2,4,6,8\}\\
11&\{1,2,3,4,5\}.
\end{array}
\tag{3.6}
\]

Thus the boundary flag and the Catalan batching profile are not two
coincidences: the former algebraically forces the latter.  Any pair not
contained in the terminal missing colour automatically has exactly the
no-waste number of `A` blocks.

### Corollary 3.3 (the `AA` forest is automatically rainbow)

Under Lemma 3.2, choose `{x,y}` not contained in `C_*`.  Then `b_A=C_{r-1}`,
and the `W-b_A=N` internal `AA` edges realise every both-new lower colour
exactly once.

Indeed, the global path-edge intersections are all distinct and omit only
`C_*`.  No lower colour containing both `x,y` is omitted, and such a colour
can only be realised by an `AA` edge.  Thus the Catalan path forest and its
rainbow property are both free consequences of the one-flag path target;
they do not require an additional selection theorem.

The same argument is not special to pairs.

### Lemma 3.4 (complete ballot-block profile)

Under Lemma 3.2, fix any `t`-set `Q`, and let `b_Q` be the number of
maximal path blocks whose central vertices all contain `Q`.  Then

\[
 \boxed{
 b_Q=B_{r,t}+\mathbf 1_{Q\subseteq C_*},\qquad
 B_{r,t}:=\frac tr\binom{2r-1-t}{r-t}.}
\tag{3.7}
\]

#### Proof

Exactly as for pairs,

\[
 b_Q=V_Q-E_Q
 =\binom{K-t}{r-t}-\binom{K-t}{r-1-t}
  +\mathbf 1_{Q\subseteq C_*}.
\]

With `K=2r-1`, the binomial difference is
`(t/r) binom(2r-1-t,r-t)`.  QED.

The induced `Q`-containing sector is therefore a path forest with precisely
the ballot number `B_{r,t}` components (or one more for `Q subset C_*`).
Its internal edges have distinct lower colours and cover every lower colour
containing `Q`, except `C_*` itself when applicable.  Thus one-hole
lower-rainbowness produces a simultaneous rainbow forest decomposition in
*every coordinate section*, not only in the two-coordinate diamond split.

Two specializations explain additional finite data:

\[
 B_{r,1}=B_{r,2}=C_{r-1}.
\]

Hence both individual-coordinate 1-run counts and pair co-presence block
counts take the same Catalan floor, with the exceptional coordinates/subsets
forming exactly the downset of `C_*`.  At `k=11` the predicted `t=3`
distribution is `28^155,29^10`, since the ten exceptional triples are those
inside the five-set `C_*`.

For `t=1`, summing the block counts gives an instructive residence ledger.
Since `K C_{r-1}=M` and `|C_*|=r-1`, the total number of coordinate 1-runs is

\[
 M+r-1,
\]

while their total length is `rM` (each of the `M` central vertices contains
`r` coordinates).  Hence their average length is

\[
 \frac{rM}{M+r-1}=r-o(1).
\tag{3.8}
\]

Similarly, for a nonexceptional pair the average all-present block length is

\[
 \frac{\binom{2r-3}{r-2}}{C_{r-1}}=\frac r2.
\tag{3.9}
\]

The desired OR-factor delay is only `Theta(sqrt(r))`.  Thus residence has a
large *average* margin inside every one-hole lower-rainbow path; the issue is
equitable block lengths, not block supply.  The factorable stored path and
the nonfactorable q1 overlay certificate have the same forced run counts but
very different minima.  This isolates the k=11 repair as a run-balancing
problem under upper-colour moves.

There is a useful dual identity for absence blocks.  Let `z_Q` be the number
of maximal path blocks whose vertices avoid a fixed `t`-set `Q`, and let
`mu^+(U)` be the multiplicity of the upper colour `U` among path edges.  Then

\[
 \boxed{
 z_Q=\binom{K-t}{r}
      -\sum_{\substack{|U|=r+1\\U\cap Q=\varnothing}}\mu^+(U).}
\tag{3.10}
\]

Indeed, `z_Q` is again vertices minus internal edges; an edge avoids `Q`
exactly when its union colour does.  Thus the upper-load vector is the exact
disjointness transform of the zero-block profile.  Summing over all `Q`
gives the universal identity

\[
 \sum_{|Q|=t}z_Q
 =M\binom{r-1}{t}-(M-1)\binom{r-2}{t}.
\tag{3.11}
\]

For `t=1`, there are `M+r-2` coordinate zero-runs in total, with average
length `(r-1)M/(M+r-2)=r-1-o(1)`.  Consequently q1 upper-colour balancing and
longer-depth zero-excursion control are not separate objectives: (3.10)
couples them exactly.  CPCR is useful because it controls this transform's
input, while the run-spectrum penalty controls its local arrangement.

Two calibrations delimit the statement.

* The stored `k=5` word does not have the central normal form: its second
  derivative has ten entries but only nine distinct middle sets and only
  seven Johnson adjacencies.  It is therefore not a meaningful test of
  Lemma 3.2.
* The `k=12` central path is Hamiltonian, but its 923 immediate intersections
  cover 792 lower colours with 131 repetitions.  Its pair-block counts range
  from 49 to 79 (mean `70.1515...`), rather than taking two adjacent values.
  This is consistent with the proof: repeated lower colours alter `E_xy`, so
  the rigid clique formula is special to the odd one-hole rainbow path.

## 4. Residence has an exact block formulation

For the new coordinate `x`, its `1`-runs are precisely the maximal contiguous
subsequences of sector blocks using only `A` and `X`; their lengths are the
sums of the constituent block sizes.  Similarly, the `1`-runs of `y` are
the maximal `A/Y` subsequences.  Therefore delay-`d` factorability in the two
new coordinates is exactly

\[
 \begin{aligned}
 &\text{every internal maximal `A/X` block-subsequence has total size at
 least }d+1,\\
 &\text{every internal maximal `A/Y` block-subsequence has total size at
 least }d+1.
 \end{aligned}
\tag{4.1}
\]

This explains the correct braid macro

\[
 U\text{-block},\quad Y\text{-block},\quad A\text{-block},
 \quad X\text{-block},\quad U\text{-block}.
\tag{4.2}
\]

The `y`-run is `Y+A` and the `x`-run is `A+X`.  An `A` block of size one is
therefore harmless when its adjacent lane block has size at least `d`.
The earlier isolated insertion `X-A-X` was bad only because it made the
other new coordinate's run have length one.

## 5. The exact stored braid census

The following was recomputed directly from the stored central paths.  The
chosen coordinate pairs are one-based.

\[
\begin{array}{c|c|c|c|c|c|c}
k&\{x,y\}&C_{m+1}&(b_A,b_X,b_Y,b_U)&e_{XY}
 &\min(1\text{-runs})&(H_1^-,H_1^+)\\ \hline
7&\{1,4\}&5&(5,5,5,4)&1&(3,3)&(1,0)\\
9&\{1,9\}&14&(14,14,14,12)&2&(3,3)&(1,0)\\
11&\{6,10\}&42&(42,41,43,36)&5&(4,4)&(1,12).
\end{array}
\tag{5.1}
\]

At `k=7` the internal-sector edge counts are

\[
 (AA,XX,YY,UU)=(5,5,5,1),
\]

and at `k=9` they are

\[
 (AA,XX,YY,UU)=(21,21,21,9).
\]

At `k=11`, for the pair `{6,10}`, they are

\[
 (AA,XX,YY,UU)=(84,85,83,48).
\tag{5.2}
\]

The `84` internal `AA` edges cover all `84` both-new lower colours exactly
once.  The `48` internal `UU` edges cover all `36` neither-new upper colours.
The sole lower hole lies in the neither-new sector.  The twelve upper holes
split as

\[
 (H_A^+,H_X^+,H_Y^+,H_U^+)=(3,4,5,0).
\tag{5.3}
\]

So the first delay-three case has already solved all of the following:

1. the exact Catalan `A`-forest count;
2. a rainbow `AA` forest;
3. the delay-four residence floor in both new coordinates;
4. the outer `UU` upper sector;
5. all but one immediate lower colour.

The unresolved content of this lift is twelve upper colours.  This is much
smaller and more specific than “find a residence-compatible lift.”

The executable census is `scratch/analyze_k11_sector_pairs.py`.  The `k=7`
and `k=9` rows were checked by the same direct calculation.

## 6. A sharp boundary obstruction for the chronological ladder

Let

\[
 T_0,T_1,\ldots,T_{W-1}
\]

be an old central Hamilton path.  Suppose its immediate lower colours

\[
 C_i=T_i\cap T_{i+1}\quad(0\le i<W-1)
\]

are all distinct and miss only `C_*`, with `C_* subset T_{W-1}`.  Append
`C_*` to the lower-colour path.  Assume the final edge

\[
 C_{W-2}C_*
\]

is the unique chronological `AA` edge whose intersection is `R_*`.

Consider the *pure chronological diamond graph*: its `XX` and `YY` edges are
only the old consecutive `T_iT_{i+1}` edges; its `AA` edges are only the
consecutive edges in

\[
 C_0,C_1,\ldots,C_{W-2},C_*;
\]

and its cross edges are the containment edges supplied by these diamonds.

### Lemma 6.1 (one boundary hole is forced)

No Hamilton path in the pure chronological diamond graph can simultaneously
cover the three lower colours

\[
 R_*+xy,\qquad C_*+x,\qquad C_*+y.
\tag{6.1}
\]

#### Proof

The colour `R_*+xy` can only come from an `AA` edge.  By hypothesis its only
available witness is `A(C_{W-2})A(C_*)`, so that edge must be used.

The old `X` and `Y` spines have no edge of lower colour `C_*`, because the
old path misses `C_*`.  Hence `C_*+x` must be witnessed by an `A(C_*)X`
edge, and `C_*+y` by an `A(C_*)Y` edge.  These are three distinct required
edges incident with `A(C_*)`, contradicting path degree at most two.  QED.

For the stored `k=9` path,

\[
 C_*=\{2,4,6,8\},\qquad R_*=\{2,4,6\},
\]

and the final `AA` edge is indeed the unique chronological witness of
`R_*`.  A bounded SAT check that selects exactly one chronological `AA` edge
per old rank-three colour becomes UNSAT when `A(C_*)` is forced isolated;
Lemma 6.1 explains that result without computation.

The obstruction is local and sharp.  One reservoir `XX` or `YY` edge with
intersection `C_*` removes it.  Equivalently, the central path may retain one
boundary lower hole, which the extra factor cell is designed to absorb.
This is exactly the one-flag phenomenon seen at `k=7` and `k=9`.

## 7. The strengthened lift target

The useful target is now the following.

> Construct a four-sector Hamilton braid with `b_A=C_{m+1}`, a rainbow
> `AA` forest, residence condition (4.1), and complete upper colours, allowing
> the one boundary hole of Lemma 6.1.

At `k=11`, the stored near-path already meets every clause except upper
completeness, where it misses exactly twelve colours.  A successful local
move should therefore preserve the `84`-edge rainbow `AA` forest and the
run floor, while replacing duplicated upper witnesses in the `A/X/Y`
sectors.  Searching the raw alternating diamond chronology is the wrong
state space; searching Catalan braids is the right one.

The all-depth run identity adds the final design rule: after satisfying the
hard one-run cooldown, minimize short internal zero excursions.  Those are
exactly the source of upper-rank loss in longer windows.  Thus a natural
objective for a recursive compiler is

\[
 \text{rainbow `AA` forest}
 +\text{ Catalan block count}
 +\text{ hard one-run floor}
 +\text{ weighted zero-run penalty}.
\]
