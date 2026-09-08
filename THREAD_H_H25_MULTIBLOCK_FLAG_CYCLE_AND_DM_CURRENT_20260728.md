# H25 multiblock flag cycles, fused seam current, and the residence obstruction

Date: 2026-07-28

Status: proved a general oriented-product-box fusion theorem, proved the
alternating-flag-cycle classification of immediate-shadow-neutral braids,
and completed an exact H25 audit of a connected four-movable-block `C10`
family.  In addition, the independently certified neutral-plus-improving
compounds pull back to direct seven-box braids: H25 descends to H24 and then
H23 while preserving the deck, residence, all upper supports, and four
immediate-lower holes.  No exact `k=15` word or coefficient-one theorem is
claimed.

## 1. Outcome and corrected frontier

Let `Q25` be the frozen 6,435-state rank-eight Johnson path in

```text
scratch/k15_segment_braid_hall25.json.
```

Its exact lower compiler graph has matching size `16358`, deficiency `25`,
and canonical Dulmage--Mendelsohn shore (S_ast) with

\[
 |S_\ast|=1320,
 \qquad |N(S_\ast)|=1295.                         \tag{1.1}
\]

The rank profile of (S_ast), in ranks four through seven, is

\[
                         (8,72,359,881),            \tag{1.2}
\]

and its target-list digest is

```text
89449e9fe9fb085c96ec911e3a9fad61f1e0409e4c6ef0133ed72677eb273e83.
```

The four verified descents `H29 -> H28 -> H27 -> H26 -> H25` all have
zero current on this final shore: its gap is `25` in every one of the five
graphs.  Therefore the next braid must create at least one genuinely new
right-cell occurrence on (S_ast).

There is one correction to the prior three-cut note.  H25 is a weak
one-move minimum, not a strict one.  The nonidentity move

\[
                         \operatorname{RF}(2612,3222,3766)        \tag{1.3}
\]

is resident and all-upper-safe and also has deficiency `25` and the same
seven zero targets.  It opens (S_ast) from gap `25` to `24`, but exposes
a different gap-25 shore.  Thus a portal on one displayed DM shore is
necessary but not sufficient.  The exact final criterion is contracted
occurrence capacity, or equivalently the current inequality on every shore.

The Hall-layer portal demanded by that criterion is now certified.  The
two moves

\[
 \operatorname{FR}(1512,2458,4103),\qquad
 \operatorname{FR}(2664,3491,6201)                 \tag{1.4}
\]

give `25 -> 25 -> 24`.  Pulled back to H25, their final word is the direct
seven-box braid

\[
 S_0,S_3,\overleftarrow S_1,S_5,S_2,
 \overleftarrow S_4,S_6,                            \tag{1.5}
\]

where the old cut positions are

\[
 1512,2125,2458,3610,4104,6202.                    \tag{1.6}
\]

Thus five interior boxes move in one final chronology.  Direct signature
cancellation leaves `58` old and `58` new profiles over a common graph of
rank `16323`, and contracted boundary capacity rises `35 -> 36`.

Starting at this H24 carrier, the pair

\[
 \operatorname{FF}(212,3732,4717),\qquad
 \operatorname{FF}(210,1501,4867)                  \tag{1.7}
\]

gives `24 -> 24 -> 23`.  Its direct seven-box order is

\[
 T_0,T_3,T_5,T_1,T_4,T_2,T_6                       \tag{1.8}
\]

for old cuts

\[
                         210,212,515,3732,4718,4868.\tag{1.9}
\]

The two-position block \(T_1\) makes this a genuinely fused macro-collar;
the individual seam collars overlap and cannot be charged independently.
The direct banks have only `29` profiles per side, and contracted capacity
rises `23 -> 24`.

## 2. Oriented block rethreading

Let

\[
                    Q=B_0B_1\cdots B_s             \tag{2.1}
\]

be a vertex-simple path in (J(n,r)), partitioned into nonempty contiguous
blocks.  Give each block either its forward or reverse orientation and
permute the oriented blocks.

### Theorem 2.1 (exact oriented-block criterion)

The resulting word (Q') is a vertex-simple Johnson path if and only if
each new join between two consecutive oriented blocks is a Johnson edge.
When this holds, the middle deck is exactly unchanged.  The endpoints are
unchanged if and only if the first and last oriented block endpoints are the
old endpoints.

#### Proof

Every old vertex occurs in exactly one retained block, so block permutation
and reversal preserve the deck and simplicity.  Every internal block edge is
retained, possibly traversed backwards.  The only unverified consecutive
pairs are the new joins.  This proves necessity and sufficiency, and the
endpoint assertion is immediate.  \(\square\)

It is useful to pair the two distant endpoints of each retained internal
block by a formal **block edge**.  No Johnson adjacency is asserted for a
block edge; the inherited path inside the block supplies the connection.
If (M_B) is this block matching and (M_+) is a proposed new seam
matching, then the rethreading is one path precisely when

\[
             M_B\cup M_+
\]

is one alternating path between the two exposed exterior ports.  A union of
cycles is not a physical word.

## 3. The exact multiscale trace coboundary

For (Phi\in\{\cap,\cup\}), let

\[
 T_{q,i}^{\Phi}(Q)
   =\Phi(Q_i,Q_{i+1},\ldots,Q_{i+q}),               \tag{3.1}
\]

and let (X_q^-), respectively (X_q^+), be the old, respectively new,
length-((q+1)) windows which are not contained in one retained oriented
block.

### Theorem 3.1 (fused trace identity)

For every target (Z),

\[
\begin{split}
 \mu_{q,Z}^{\Phi}(Q')-\mu_{q,Z}^{\Phi}(Q)
   ={}&\sum_{i\in X_q^+}{\bf1}[T_{q,i}^{\Phi}(Q')=Z]\\
     &-\sum_{i\in X_q^-}{\bf1}[T_{q,i}^{\Phi}(Q)=Z].              \tag{3.2}
\end{split}
\]

If there are (t) old and (t) new seams, then

\[
 |X_q^-|=|X_q^+|\le tq,
 \qquad
 \|\mu_q^{\Phi}(Q')-\mu_q^{\Phi}(Q)\|_1\le2tq.     \tag{3.3}
\]

#### Proof

Every window contained in one old block has one transported window in the
corresponding new oriented block.  Reversal changes entry order but not
union or intersection, so these windows cancel bijectively.  This gives
(3.2).  A fixed seam is crossed by at most (q) starts, hence the union
bound in (3.3).  Equality of (|X_q^-|) and (|X_q^+|) also follows from

\[
 |X_q|=(|Q|-q)-\sum_j\max\{|B_j|-q,0\},             \tag{3.4}
\]

which depends only on the multiset of block lengths.  The (L^1) bound is
the total mass of the two signed sums.  \(\square\)

Consequently, if the old upper layer at depth (q) is complete, the new
layer is complete if and only if

\[
 I_{q,Z}+N^+_{q,Z}\ge1                              \tag{3.5}
\]

for every upper target (Z), where (I_{q,Z}) counts occurrences internal
to retained blocks and (N^+_{q,Z}) counts new crossing occurrences.  This
is the exact last-witness test.  No separate reset is paid for the volume of
a moved block.

The same statement is genuinely multiscale.  If several intermediate
rethreadings are fused and only the initial and final words are retained,
their signed trace measures telescope.  The final cost is controlled by the
initial/final atomic seam set, not by the number of intermediate reset
words.

## 4. Immediate shadows are an alternating flag-cycle problem

For a Johnson edge (XY), define its flag

\[
                  \lambda(XY)=X\cap Y,
          \qquad \upsilon(XY)=X\cup Y.              \tag{4.1}
\]

This is an edge in the bipartite incidence graph between rank-((r-1)) and
rank-((r+1)) masks.  Conversely, an incident pair (L\subset U) with
(|U\setminus L|=2) determines the unique undirected Johnson edge whose two
states are (L\cup\{a\}) and (L\cup\{b\}), where
(U\setminus L=\{a,b\}).

### Theorem 4.1 (flag-cycle classification)

Colour old seams red and new seams blue.  The immediate lower and upper
multiplicity vectors are both preserved exactly if and only if red degree
equals blue degree at every lower and every upper flag vertex.  Equivalently,
the signed flag multigraph decomposes into alternating even cycles.

#### Proof

The multiplicity of a lower mask is its red or blue degree on the lower
shore, and similarly for upper masks.  Hence equality of both shadow vectors
is exactly equality of the two colours at every vertex.  In a finite
two-coloured balanced multigraph, begin with an unused red edge and
alternately take unused blue and red edges.  Colour balance prevents the walk
from stopping before it closes.  Delete the resulting alternating cycle and
iterate.  \(\square\)

This is a flag statement, not yet a deck statement.  A usable cycle must
also be **state-compatible**: its blue incidences must pair the same physical
boundary states used by the red seams.  Finally (M_B\cup M_+) must be one
path.  These two conditions are the exact global endpoint-sharing gate.

## 5. A connected four-movable-block wheel

Fix a rank-((r-2)) core (K) and six pairwise distinct coordinates

\[
                 a_0,a_1,a_2,a_3,a_4,c\notin K.     \tag{5.1}
\]

With indices modulo five, put

\[
 C_i=K\cup\{a_i,c\},
 \qquad
 P_i=K\cup\{a_i,a_{i+1}\}.                         \tag{5.2}
\]

The old and new seam matchings are

\[
 M_- =\{C_iP_i:0\le i<5\},
 \qquad
 M_+ =\{C_iP_{i-1}:0\le i<5\}.                    \tag{5.3}
\]

Every edge in (5.3) is Johnson.  Define

\[
 L_i=K\cup\{a_i\},
 \qquad
 U_i=K\cup\{a_i,a_{i+1},c\}.                       \tag{5.4}
\]

The old flags are ((L_i,U_i)), while the new flags are
((L_i,U_{i-1})).  Hence the signed flag graph is the connected cycle

\[
 L_0-U_0-L_1-U_1-\cdots-L_4-U_4-L_0,               \tag{5.5}
\]

and both immediate shadow multisets are exact.

### Theorem 5.1 (directed pentagonal braid)

Suppose the old path has the directed boundary factorization

\[
 A\,C_0\mid P_0 B_0^\circ P_1\mid
 C_1 B_1^\circ P_2\mid C_2 B_2^\circ P_3\mid
 C_3 B_3^\circ P_4\mid C_4 D.                       \tag{5.6}
\]

Then

\[
 A\,\overleftarrow B_3\,
   \overleftarrow B_1\,B_0B_2\,D                   \tag{5.7}
\]

is a same-endpoint, same-deck Johnson path.  It moves four inherited blocks,
and its new seams are exactly (M_+).

#### Proof

The chronological new seams are

\[
 C_0P_4,quad C_3P_2,quad C_1P_0,quad
 P_1C_2,quad P_3C_4,                               \tag{5.8}
\]

which are the five edges (C_iP_{i-1}).  Theorem 2.1 proves the path and
deck assertions; (5.4)--(5.5) prove the shadow assertion.  \(\square\)

The directed order (5.6) is sufficient, not necessary.  For arbitrarily
oriented old wheel edges, the exact necessary-and-sufficient replacement is
the block-matching test

\[
                         M_B\cup M_+\text{ is one path}.          \tag{5.9}
\]

This allows connected `C10` braids not expressible in the normal form
(5.6).  It also prevents the common error of accepting an unordered wheel
whose recoupling closes several block cycles.

The signed flag current in (5.5) is one `C10`, so it is not a disjoint union
of tetrahedral `C6` currents on the same support.  A factorization through
overlapping `C6` moves and additional intermediate seam flags is not ruled
out.

## 6. Residence is a separate collar constraint

Write a Johnson path as

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\}.              \tag{6.1}
\]

### Lemma 6.1 (exact depth-(d) run test)

Assume the retained blocks are depth-(d) resident internally.  The fused
path is depth-(d) resident if and only if

\[
                    \beta_i\ne\alpha_j              \tag{6.2}
\]

whenever (i<j), (j-i\le d), and the coordinate run from the insertion at
(i) to the deletion at (j) meets a new seam.  Equivalently, every
internally bounded positive coordinate run meeting a new seam has length at
least (d+1).

#### Proof

If (eta_i=\alpha_j=x), then (x) is present precisely from state
(i+1) through state (j), a run of length (j-i), unless that run extends
through an endpoint.  Thus (6.2) is exactly the exclusion of an internally
bounded run of lengths (1,\ldots,d).  All runs not meeting a seam are
transported old runs.  \(\square\)

Endpoint Johnson legality and the `C10` flag identity do not imply this
condition.  This is the decisive obstruction in the H25 common-hub family.

## 7. Product-box fusion and the exact Hall current

Let the compiler depth be (d), and let a row-(h) physical cell,
(0\le h<d), start at controller position (p).

### Theorem 7.1 (compiler seam locality)

The complete target-neighbourhood signature of this cell is determined by
the middle owners in

\[
                         [p-2d,\ p+h+d].             \tag{7.1}
\]

A cut between owners (a-1,a) can therefore affect at most

\[
                         3d+h                       \tag{7.2}
\]

row-(h) cells on one side of a comparison.  One seam owns at most

\[
 C_d=\sum_{h=0}^{d-1}(3d+h)
    ={7d^2-d\over2}                                  \tag{7.3}
\]

cell profiles per word.  Thus (t) old and (t) new seams leave at most

\[
                     t(7d^2-d)                       \tag{7.4}
\]

old-plus-new profiles before signature cancellation.  At (d=3,t=5), the
bounds are `150` old, `150` new, `300` combined.

#### Proof

The maximal erosion state at (p) uses owners in ([p-d,p]).  An owner
whose forced carrier can enter a row-(h) cell starts in ([p-d,p+h]), and
its full carrier test uses owners from (d) positions before through (d)
positions after that start.  This gives (7.1).  Its interval crosses the cut
only for

\[
                         a-h-d\le p\le a+2d-1,
\]

which contains (3d+h) integers.  Summing over (h) proves (7.3)--(7.4).
\(\square\)

If adjacent cuts are separated by at least (4d-1) states, these cell
collars are disjoint.  If blocks also have at least (H+1) states, no
depth-(q\le H) window crosses two seams.  Under these safe separation
hypotheses, both compiler profiles and trace currents are literal sums of
single-seam contributions.  Without separation, Theorems 3.1 and 7.1 still
give exact global union-of-collars identities, but a multi-seam window or
cell must be counted once rather than once per seam.

Now cancel old and new right cells having identical complete neighbourhood
signatures and write

\[
                    G^-=H\sqcup B^-,
             \qquad G^+=H\sqcup B^+.                \tag{7.5}
\]

For a target shore (X), put

\[
 n_F(X)=|\{c\in F:N(c)\cap X\ne\varnothing\}|,
 \qquad I_B(X)=n_{B^+}(X)-n_{B^-}(X).               \tag{7.6}
\]

### Theorem 7.2 (exact fused Hall criterion)

Let the old deficiency be (d_0), let

\[
 \sigma(X)=d_0-\bigl(|X|-|N_{G^-}(X)|\bigr).        \tag{7.7}
\]

Then

\[
 d(G^+)=d_0-
       \min_X\bigl(\sigma(X)+I_B(X)\bigr).          \tag{7.8}
\]

In particular, deficiency falls by at least one if and only if

\[
                     I_B(X)\ge1-\sigma(X)
                     \qquad\text{for every }X.       \tag{7.9}
\]

Equivalently, with

\[
 \operatorname{cap}_H(B)=\nu(H\sqcup B)-\nu(H),     \tag{7.10}
\]

one has descent if and only if

\[
 \operatorname{cap}_H(B^+)\ge
 \operatorname{cap}_H(B^-)+1.                       \tag{7.11}
\]

#### Proof

For each shore,

\[
 |X|-|N_{G^+}(X)|
   =d_0-\sigma(X)-I_B(X).
\]

Maximizing proves (7.8), and integrality gives (7.9).  Equation (7.11)
follows by writing both matching ranks relative to the common graph (H).
\(\square\)

For H25, (1.1) makes

\[
                         I_B(S_\ast)\ge1             \tag{7.12}
\]

necessary.  A five-seam depth-three braid has (|B^-|\le150), so only old
shores with slack at most `150` can block (7.9).  Condition (7.12) alone is
not sufficient: (1.3) opens (S_ast) but moves the obstruction to another
tight shore.  Thread A's exact compound example similarly opens
(S_ast) while the tight extension (S_ast\cup\{20654\}) stays at gap
`25`.

This is the precise product-box interpretation.  The useful resource is not
raw target incidence but the transversal-matroid rank of the fused boundary
bank after the inherited interior has been contracted.

## 8. A fixed-partition dual obstruction

Fix block orientations and assume the seam collars are disjoint.  Let
(w_{ij}(X)) be the number of local seam cells meeting a fixed shore (X)
when terminal port (i) is joined to initial port (j).  Any cycle-cover
relaxation chooses a permutation (pi) and has score

\[
                         \sum_i w_{i,\pi(i)}(X).     \tag{8.1}
\]

### Proposition 8.1 (assignment-dual no-go)

If numbers (alpha_i,eta_j) satisfy

\[
 \alpha_i+\beta_j\ge w_{ij}(X)
 \quad\text{for every allowed seam }ij,             \tag{8.2}
\]

and

\[
 \sum_i\alpha_i+\sum_j\beta_j
 \le \sum_iw_{i,\pi_0(i)}(X),                       \tag{8.3}
\]

where (pi_0) is the old seam assignment, then no reordering of this fixed
oriented partition has positive current on (X).  In particular, if (X)
is an old tight shore, no such reordering can lower Hall deficiency.

#### Proof

For every permutation,

\[
 \sum_iw_{i,\pi(i)}(X)
 \le\sum_i(\alpha_i+\beta_{\pi(i)})
 =\sum_i\alpha_i+\sum_j\beta_j,
\]

and (8.3) finishes the proof.  \(\square\)

Failure of this dual only produces a favourable cycle cover.  It does not
guarantee one alternating path, residence, upper last-witness coverage, or
the all-shore rank gain (7.11).

## 9. Exact H25 common-hub `C10` audit

The deterministic verifier

```text
scratch/audit_k15_h25_path_compatible_c10_wheels.py
```

enumerates the family without enumerating arbitrary block permutations.
For every old Johnson edge (X|Y), every (a\in X\cap Y), and each of the
two physical orientations, it records the unique data

\[
 K=(X\cap Y)\setminus\{a\},
 \qquad C=K+\{a,c\},
 \qquad P=K+\{a,b\}.                                \tag{9.1}
\]

Five records form an abstract wheel exactly when they have common
((K,c)) and their arcs (a\to b) form a simple directed five-cycle.  This
is a bijective encoding of (5.2)--(5.3).  The verifier then builds the actual
old block matching (M_B), retains the wheel precisely when (5.9) is one
path, materializes that unique signed block order, and checks the literal
word.

### Theorem 9.1 (common-hub wheel residence no-go at H25)

On the frozen H25 carrier:

1. there are `37` abstract simple common-((K,c)) five-wheels;
2. exactly `14` satisfy the physical alternating-path condition (5.9);
3. all `14` are same-deck Johnson paths;
4. all `14` preserve both immediate shadow multiplicity vectors exactly;
5. all `14` retain complete upper support at every depth (q=1,\ldots,7);
6. none is depth-three resident.

The minimum number of short positive runs is one, attained by exactly two
braids:

\[
\begin{array}{c|c|c|c|c}
K&c&(a_0,\ldots,a_4)&\text{cuts}&\text{unique bad run}\\ \hline
12504&1&(8,9,10,11,14)&(305,2305,3037,4715,5032)&(10,[1981,1982])\\
3157&3&(1,12,14,5,7)&(2052,2088,3504,3833,3862)&(12,[2052,2054]).
\end{array}                                          \tag{9.2}
\]

Coordinates and positions in (9.2) are zero-based.  Their signed block
orders are respectively

\[
 (B_2,B_1,\overleftarrow B_3,B_0),
 \qquad
 (\overleftarrow B_3,B_2,\overleftarrow B_0,
  \overleftarrow B_1).                              \tag{9.3}
\]

#### Proof

The encoding (9.1) is forced by the lower flag, the two exchanged
coordinates, and the physical orientation, so no member of the stated
family is omitted or duplicated except for cyclic rotation, which is
canonically quotiented.  The block matching test is Theorem 2.1 in its
alternating-path form.  The resulting fourteen materialized words are
checked against all 6,435 states, every consecutive Johnson edge, the two
complete depth-one multiplicity counters, every upper support counter
through depth seven, and the exact run criterion of Lemma 6.1.  The audit
asserts the six displayed totals and fails closed on any disagreement.
\(\square\)

The verifier and result hashes at writing time are

```text
c22aa06c667b32c40d102c3c3d6835e31bf96c0516fa107a7de68854121dedff
  scratch/audit_k15_h25_path_compatible_c10_wheels.py

7a05c7cd7ead649d9d0ebd5a6e65510ed76b13021b667054b48c6038a4e31b03
  scratch/k15_h25_path_compatible_c10_wheels_audit.json
```

The rigid directed normal form (5.6) has no H25 occurrence.  The fourteen
members above are more general: their arbitrary old seam orientations still
give the same connected red/blue `C10`, and (5.9) supplies their physical
signed block orders.

## 10. Exact proved/conditional boundary

The global endpoint algebra is no longer missing.  A connected
four-movable-block, deck-exact, immediate-shadow-neutral braid exists in
general, and fourteen such braids are physically present in H25 with the
entire upper support tower intact.

The common-hub `C10` family nevertheless cannot improve H25 because all
fourteen members fail residence before the lower compiler graph is defined.
This is a no-go for that family only.  It does not exclude:

* a state-compatible `C10` not having one common core and hub;
* a connected `C12` or larger flag cycle;
* overlapping cycles whose residence defects cancel;
* a collar surgery which lengthens one of the two runs in (9.2);
* a deck-changing compensated circuit.

The former H25 replacement lemma is now solved by the direct braid
(1.5)--(1.6), whose exact contracted capacity rises `35 -> 36`.  The same
mechanism repeats at H24 via (1.8)--(1.9), reaching H23.  Thus the
common-hub `C10` no-go identifies a failed primitive, not a barrier to
multiblock fusion.

At H23 the canonical DM shore is a disjoint union of 23 unit-defect
components.  The smallest current gate is to saturate any one component
while retaining a maximum matching on the other 22 and on the exterior.
The exact component-root diamond theorem and full census are in

```text
THREAD_H_H23_COMPONENT_ROOT_DIAMOND_PRODUCT_FUSION_20260728.md.
```

Even Hall 23 is only the projected lower Hall problem.  A final exact word
still needs the common physical controller/pin selection and all retained
owner constraints.  Hence this report does not prove the exact `k=15`
formula or asymptotic coefficient one.

## 11. Adversarial audit

1. A formal block edge joins distant endpoints of an inherited path; it is
   not asserted to be Johnson-adjacent.
2. An unordered `C10` of flags is insufficient.  State compatibility and
   the one-path condition (5.9) are both essential.
3. Exact depth-one multiplicities do not imply residence or any deeper
   layer.  The H25 census illustrates this sharply: deeper upper support
   survives, while residence fails.
4. The compiler estimates `150+150` are upper bounds before full-signature
   cancellation, not exact bank sizes.
5. Additive per-seam current requires disjoint dependency collars.  Without
   separation, use the global signed bank once.
6. Positive current on (S_ast) is only necessary.  All-shore current or
   contracted rank is the exact criterion.
7. The finite no-go is restricted to simple common-core/common-hub
   five-wheels.  No statement about every multiblock braid is made.
