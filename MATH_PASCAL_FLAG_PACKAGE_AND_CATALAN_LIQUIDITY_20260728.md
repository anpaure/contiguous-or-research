# Pascal flag packages, the Catalan liquidity hinge, and an induction target

Date: 2026-07-28

Status: pure mathematics.  This note proves structural reductions and a new
shadow-liquidity theorem.  It does **not** prove `nu(k)=B(k)` for all `k` and
does not claim a `k=15` construction.

## 0. Outcome

The exact words through `k=14`, the odd-to-even six-piece lift, the
four-sector `k -> k+2` deck, the `sigma` map, and the lower owner compiler are
different faces of one object: a **Pascal flag package**.

For a resident Johnson ordering `T` of the middle layer, put

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h},\qquad
 U_i^{(q)}=\bigcup_{h=0}^{q}T_{i+h}.
\]

The lower rows `L^(q)` are not independent shadows.  They are successive
edge-colour rows of one recursively nested Johnson path.  At every start
position they form one flag

\[
 L_i^{(d)}\subset\cdots\subset L_i^{(1)}\subset T_i
 \subset U_i^{(1)}\subset\cdots.
\]

Three exact consequences are proved below.

1. The odd-to-even deck is `T` together with a lifted completion of
   `L^(1)`.  The odd-to-odd four-sector deck is exactly

   \[
   xy+L^{(1)},\qquad x+T,\qquad y+T,\qquad U^{(1)}.
   \]

   Thus both lifts use the first Pascal neighbourhood of the parent, not
   unrelated constructions.

2. There is a scalar **shadow-prefix liquidity theorem**.  Natural
   lower-shadow occurrences are free compiler pins.  Duplicate occurrences
   in the higher rows and the nested boundary flags give a rigorous necessary
   prefix-capacity bound for a missing shadow before the next rank is reached.

3. In odd dimension `k=2r-1`, the first prefix slack is one and the second is

   \[
                         C_r+3.
   \]

   After removing the three triangular boundary cells, the bulk term is the
   same Catalan number which counts the components of the both-new flag
   forest in the `k -> k+2` lift.  The compiler prefix and the lift forest
   come from the same rank-`r-2` deficit.

For `k=15`, a one-path flat construction must have at most two internal
`q=1` holes and at most five internal `q=2` holes before labelled owner
constraints are even considered.  The current Hall-29 carrier has `(4,21)`;
the clean Hall-31 carrier has `(2,22)`.  Hence both are structurally far from
the necessary flag-prefix corridor, even though their unrestricted compiler deficiencies
are numerically small.

The resulting induction invariant is stated in Section 8.  The smallest
remaining compiler lemma is the **trace-two residual extension lemma** in
Section 9.  A separate carrier lemma is still required; calling their
conjunction one lemma would only rename the conjecture.

## 1. Lower bound and the exact scope of equality rigidity

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,\qquad
 W=\binom{k}{r},\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s}.
\]

Let `d=d(k)` be the least nonnegative integer such that

\[
                         \Lambda\le dW+\binom{d+1}{2},
\]

and put `B(k)=W+d`.

For a nonzero word of length `W+e`, let `f_i` be the number of initial cells
in column `i` whose rank is below `r`, and put `F_i=i+f_i`.  Shifted-cell
containment gives

\[
                         f_{i+1}\ge f_i-1,
 \qquad F_{i+1}\ge F_i.
\]

Two distinct middle-rank targets cannot have the same finite deadline
`F_i`: the later interval would be contained in the earlier one, and equal
rank would force equal labels.  The `W` middle targets therefore force

\[
                         f_i\le\min(e,W+e-i+1).
\]

Every lower target occurs in one of the first `f_i` cells of some column, so

\[
 \Lambda\le\sum_i f_i
 \le eW+\binom{e+1}{2}.
\]

This proves

\[
                         \boxed{\nu(k)\ge B(k)}.
\]

At `e=d`, define the arithmetic slack

\[
 \sigma_k=dW+\binom{d+1}{2}-\Lambda.
\]

The proof has the exact loss decomposition

\[
 \sigma_k=
 \sum_i\left(\min(d,W+d-i+1)-f_i\right)
 +\left(\sum_i f_i-\Lambda\right).
 \tag{1.1}
\]

Both summands are nonnegative.  Consequently `sigma_k=0` forces the first
`W` columns to have depth exactly `d`, forces the lower band to be bijective,
and forces row `d` to be the complete middle layer.  This explains the
rigidity at `k=6,9`.

Positive slack does **not** force flatness, rank grading, Johnson adjacency,
or bounded owner width.  Those are construction invariants selected by the
known optima.  This distinction is essential: the package below is an exact
sufficient normal form, but it is not a consequence of the bare equality
when `sigma_k>0`.

## 2. The recursive Pascal flag ladder

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a Johnson path in the rank-`r` layer.  Write

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
 \tag{2.1}
\]

Call `T` lower-`d`-fresh when every internal one-run of every coordinate has
length at least `d+1`.  This is the usual depth-`d` residence condition.

### Theorem 2.1 (Pascal flag ladder)

For `0<=q<=d`, define

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}
 \qquad(0\le i<W-q).
\]

Then

\[
 \boxed{L_i^{(q)}
 =T_i\setminus\{a_i,a_{i+1},\ldots,a_{i+q-1}\},}
 \tag{2.2}
\]

so `|L_i^(q)|=r-q`.  Moreover `L^(q)` is itself a Johnson path and

\[
 \boxed{L_i^{(q+1)}=L_i^{(q)}\cap L_{i+1}^{(q)}.}
 \tag{2.3}
\]

#### Proof

If `a_(i+h)` had been inserted after time `i`, it would be deleted within at
most `q<=d` transitions, contradicting residence.  Hence all displayed
deleted elements already lie in `T_i`.  They are distinct, because a second
deletion would require an intervening reinsertion followed by deletion within
`d` transitions.  This proves (2.2) and its rank.

Residence also gives `a_(i+q) in T_i` and
`b_i notin {a_(i+1),...,a_(i+q)}`.  Therefore the transition from
`L_i^(q)` to `L_(i+1)^(q)` deletes `a_(i+q)` and inserts `b_i`; it is a
Johnson edge.  Their intersection is exactly (2.2) with one further
deletion, proving (2.3).  \(\square\)

Thus the lower shadows form a path of paths:

\[
 T=L^{(0)}\longmapsto L^{(1)}\longmapsto\cdots\longmapsto L^{(d)},
\]

where every arrow takes consecutive edge intersections.  The deletion-chain
tableau and the lower Gray paths are the same object.

The upper rows always satisfy the formal recursion

\[
 U_i^{(q)}=\bigcup_{h=0}^{q}T_{i+h},\qquad
 U_i^{(q+1)}=U_i^{(q)}\cup U_{i+1}^{(q)}.
 \tag{2.4}
\]

If every internal zero-run also has length at least `d+1`, then the dual of
Theorem 2.1 makes `U^(q)` a rank-`r+q` Johnson path.  Upper universality does
not require this stronger grading: a returned coordinate can make a window
useful at a different depth.  We therefore use (2.4) without silently
assuming upper freshness.

At every start `i`, (2.2)--(2.4) give one two-sided nested flag.  This is the
common structural object seen in the exact words.

## 3. The `sigma` map is the first face of the flag ladder

Assume now that `k=2r-1` and use a cyclic carrier for notational simplicity.
The rank-`r-1` and rank-`r` layers both have size `W`.

Suppose the edge intersections

\[
                         X_i=T_i\cap T_{i+1}
\]

enumerate the rank-`r-1` layer.  Define

\[
                         \sigma(X_i)=T_i\cup T_{i+1}.
 \tag{3.1}
\]

Then `X subset sigma(X)` and `|sigma(X)\X|=2`.

### Proposition 3.1 (diamond-map equivalence)

Let `G_sigma` join `X` to the two intermediate rank-`r` sets between
`X` and `sigma(X)`.  Then `G_sigma` is exactly the alternating
rank-`r-1`/rank-`r` carrier.  In particular:

1. every lower vertex has degree two;
2. every middle vertex has degree two precisely when the carrier is a
   2-factor; and
3. the immediate upper shadow is complete precisely when `sigma` is
   surjective onto the rank-`r+1` layer.

#### Proof

The two intermediate sets are the endpoints `T_i,T_(i+1)` of the edge whose
lower colour is `X_i`.  Conversely, the union of those two intermediates is
the unique value in (3.1).  Degree and surjectivity are then literal.  \(\square\)

Hamiltonicity is only connectivity of this 2-factor.  The seam construction
at `k=13` shows that connectivity may be imposed after the labelled factor
is built.  The hard content of `sigma` is its simultaneous degree-two and
surjectivity property, not the number of components.

There is an important unconditional input here.

### Proposition 3.2 (the Middle Levels Theorem supplies the ideal lower face)

For every odd `k=2r-1`, there is a cyclic ordering of all rank-`r` sets
whose consecutive intersections enumerate the rank-`r-1` layer exactly.
After cutting the cycle, the resulting rank-`r` Hamilton path has exactly
one missing immediate-lower colour, and that colour is contained in the
appropriate endpoint.

#### Proof

Take a Hamilton cycle in the middle levels graph on ranks `r-1` and `r`.
Write it alternately as

\[
 X_0,T_0,X_1,T_1,\ldots,X_{W-1},T_{W-1},X_0.
\]

The two distinct rank-`r` neighbours of `X_(i+1)` have intersection exactly
`X_(i+1)`.  Hence the projection `T_0,...,T_(W-1)` is a Johnson cycle and
its edge intersections are `X_1,...,X_0`, each once.  Cutting one projected
edge removes one `X`; that `X` was incident with both cut endpoints in the
alternating cycle, so it is endpoint-accessible.  \(\square\)

Thus existence of the correct `q=1` lower palette is not open.  What is open
is finding a Middle Levels Hamilton cycle whose projection simultaneously
has:

* the required residence;
* a surjective upward map `sigma`; and
* the required second lower-shadow behaviour.

The last condition is especially concrete.  The rank-`r-1` sequence
`X_0,...,X_(W-1)` in the displayed Middle Levels cycle is itself a Johnson
cycle, and

\[
 X_i\cap X_{i+1}=T_{i-1}\cap T_i\cap T_{i+1}.
 \tag{3.2}
\]

So the `q=2` shadow of the projected middle chronology is exactly the
ordinary edge-colour palette of the lower shore of the same Hamilton cycle.
The first unresolved carrier property is therefore a two-level rainbow
condition on one classical object, not a new `q=1` cycle theorem.

### Lemma 3.2a (the lower shore determines the middle chronology)

In the notation of Proposition 3.2, assume consecutive lower vertices are
distinct.  Then

\[
 \boxed{T_i=X_i\cup X_{i+1}.}
 \tag{3.2a}
\]

Consequently

\[
 T_i\cup T_{i+1}=X_i\cup X_{i+1}\cup X_{i+2},
 \tag{3.2b}
\]

and

\[
 T_{i-1}\cap T_i\cap T_{i+1}=X_i\cap X_{i+1}.
 \tag{3.2c}
\]

#### Proof

The two distinct rank-`r-1` neighbours `X_i,X_(i+1)` of `T_i` are
distinct facets of the rank-`r` set `T_i`, so their union is `T_i`.  Taking
the union of two consecutive instances proves (3.2b).  Since
`X_i=T_(i-1) cap T_i` and `X_(i+1)=T_i cap T_(i+1)`, intersecting them
proves (3.2c).  \(\square\)

Thus the sharp odd carrier can be sought entirely on the lower shore.  It is
a rank-`r-1` Johnson cycle whose consecutive unions enumerate the middle
layer, whose consecutive intersections are almost rainbow one rank down,
and whose three-vertex unions cover the required rank-`r+1` layer.  The
middle chronology is recovered by (3.2a).  This is the precise bi-rainbow
path problem hidden inside the `sigma` formulation.

There is a sharper conditional route when the Middle Levels cycle is
complement-half-turn invariant.  This symmetry is arithmetically compatible
with the alternating levels when `W` is odd; in particular it is compatible
with `k=15`, where `W=6435`.

### Theorem 3.3 (complement duality collapses upper `q` to lower `q+1`)

Let `C` be a complement-half-turn invariant Hamilton cycle of the middle
levels graph, let `T` be its rank-`r` projection, and let `X` be its
rank-`r-1` shore.  For cyclic supports and every `q>=1`,

\[
 \boxed{
 \overline{\operatorname{supp} U_T^{(q)}}
 =\operatorname{supp} L_T^{(q+1)}.}
 \tag{3.3}
\]

In particular, for

\[
 \sigma(X)=\text{union of the two rank-`r` neighbours of }X,
\]

and

\[
 \delta(T)=\text{intersection of the two rank-`r-1` neighbours of }T,
\]

one has

\[
                         \boxed{\overline{\sigma(X)}=\delta(\bar X)}
 \tag{3.4}
\]

after the half-turn identification.  Consequently `sigma` is surjective if
and only if `delta` is surjective.

#### Proof

Complementation sends every block of `q+1` consecutive rank-`r` vertices
on `C` to `q+1` consecutive rank-`r-1` vertices on the opposite half of
`C`.  De Morgan's law turns their union into the intersection of those
lower-shore vertices.  Each lower-shore vertex between two consecutive
rank-`r` vertices is their intersection, so the intersection of `q+1`
consecutive lower-shore vertices is the intersection of the corresponding
`q+2` consecutive `T` vertices.  This proves (3.3).  The case `q=1` is
(3.4), and complementation bijects the two target layers.  \(\square\)

### Corollary 3.4 (a sharp conditional `k=15` carrier)

Suppose a complement-half-turn invariant Middle Levels Hamilton cycle has a
surjective `sigma`.  Choose a lower vertex `X_*` whose `sigma` value occurs
at least twice, and cut the projected `T` cycle at the edge coloured `X_*`.
Then the resulting path has

\[
 h_1=1,\qquad \text{no upper-`q=1` hole},\qquad h_2\le2.
 \tag{3.5}
\]

#### Proof

The cut deletes one lower edge colour, giving `h_1=1`.  Since `sigma` is a
surjection from `W` lower vertices onto only `W-C_r` upper targets, some
value is repeated; choosing `X_*` in a repeated fibre preserves every upper
target after the cut.  Theorem 3.3 makes the cyclic depth-two lower support
complete.  A cut destroys only the two cyclic triple windows crossing that
edge, so at most two depth-two lower targets are lost.  \(\square\)

For `k=15`, (3.5) is automatically inside both the refined `h_1=1` prefix
bound `h_2<=4` and the coarse prefix bound
`h_1<=2,h_2<=5`.  Therefore a complement-half-turn invariant Middle Levels
cycle with surjective `sigma`, depth-three residence, and the required deeper
dual shadow support, together with a repeated-`sigma` cut which preserves
that deeper support (or places its losses in the allowed collars), would
solve the **carrier** half of the current problem in one stroke.  The
residual trace-two compiler would still have to be supplied; no full `k=15`
word is claimed here.

Notice that “deeper dual shadow support” is one-sided data.  By (3.3), one
does not need to impose the upper tower separately: covering the appropriate
lower layers by the cyclic rows `L_T^(q+1)` is exactly equivalent, under
complementation, to covering the upper layers by `U_T^q`.  This removes one
whole family of constraints from the symmetric carrier search/theorem.

More generally, whenever `L_i^(q)` is unique, the pair

\[
                         L_i^{(q)}\subset U_i^{(q)}
\]

is a `2q`-diamond.  The maps at different `q` are not independent: they are
all projections of the same transition word.  This is the higher-depth
form of the `sigma` constraint.

## 4. Both known lifts are adjacent-row functors

The first Pascal neighbourhood gives the correct child deck before any
ordering is chosen.

### Theorem 4.1 (odd-to-even deck identity)

Let `k=2r-1` and adjoin `z`.  If `T` enumerates the rank-`r` layer and a
completion `\widehat L^(1)` enumerates the rank-`r-1` layer, then

\[
 \boxed{
 \binom{[k]\cup\{z\}}{r}
 =\{T_i\}_i\ \sqcup\ 
   \{\{z\}\cup X:X\in\widehat L^{(1)}\}.}
 \tag{4.1}
\]

#### Proof

A rank-`r` child set either avoids `z` and is a parent rank-`r` set, or
contains `z` and has an old rank-`r-1` trace.  \(\square\)

This is exactly the two-shore intersection lift.  The loss of one residence
unit on the second shore is also immediate from Theorem 2.1: a one-run of
length `ell` in `T` becomes a run of length `ell-1` in `L^(1)`.

### Theorem 4.2 (odd-to-odd four-sector identity)

Adjoin `x,y`.  Suppose `\widehat L^(1)` enumerates rank `r-1`, `T`
enumerates rank `r`, and choose one occurrence of every rank-`r+1` set from
the support of `U^(1)`.  Then

\[
\boxed{
\binom{[k]\cup\{x,y\}}{r+1}
= (\{x,y\}+\widehat L^{(1)})
\sqcup(\{x\}+T)
\sqcup(\{y\}+T)
\sqcup U_*,}
\tag{4.2}
\]

where `U_*` contains one copy of every parent rank-`r+1` set.

#### Proof

Partition a child set by its intersection with `{x,y}`.  Its old trace has
rank `r-1,r,r,r+1` in the four cases.  \(\square\)

Thus the `A,X,Y,U` sectors of the diamond lift are respectively the lower,
two central, and upper rows adjacent to the parent.  The old object supplies
the correct **labels**.  The unproved part is to rethread those labels with
common residence, upper windows, seams, and lower pins.  The exact `11 -> 13`
audit shows that this rethreading is genuinely off-spine, so an induction
must preserve a flag package, not a particular parent edge set.

### Proposition 4.3 (path-cover seam collar)

Let a middle-layer path cover have component lengths
`ell_1,...,ell_c`, summing to `W`.  The number of length-`q+1` windows
lying inside components is

\[
                         I_q=\sum_{j=1}^{c}(\ell_j-q)^+.
 \tag{4.3}
\]

If every component has length greater than `q`, then

\[
                         I_q=W-cq.
 \tag{4.4}
\]

A single Hamilton path has `W-q` such windows.  Hence joining the `c`
components creates exactly

\[
                         (c-1)q
 \tag{4.5}
\]

new seam-crossing windows at depth `q`.  Every changed witness is contained
in the `q`-collars of the cuts and joins.

#### Proof

A path of length `ell` has `(ell-q)^+` consecutive blocks of length
`q+1`, proving (4.3).  Under the length hypothesis, summation gives (4.4).
Subtracting from `W-q` gives (4.5).  A block unaffected by a cut or join has
the same ordered vertices, so only the displayed collars change.  \(\square\)

This is the exact reason connectivity was cheap at `k=13`: the labelled
factor was the hard object, while one seam modified only one bounded collar
at every fixed depth.  A path cover is therefore a legitimate induction
invariant provided it carries explicit seam ports and replacement witnesses.
Component count alone is neither an obstruction nor a proof of compatibility.

## 5. Natural shadows are free pins

Let `T` be lower-`d`-fresh and let `P` be its maximal depth-`d` erosion.  In
the interior, the intersection-tableau identity is

\[
                         (D^{d-q}P)_{i+q}=L_i^{(q)}.
 \tag{5.1}
\]

### Lemma 5.1 (free-shadow pin)

If a target `S` equals a cell `D^tP_j`, then prescribing

\[
                         D^tA_j=S
\]

does not shrink `P`: every source position of the cell already satisfies
`P_p subset S`, and its union is `S`.

#### Proof

Every member of a union is contained in that union, so `P_p subset D^tP_j`
throughout the cell.  The negative part of the pin removes no coordinate,
and the positive equality already holds in `P`.  \(\square\)

Consequently one may reserve one natural occurrence of every present lower
shadow target at zero owner cost.  The hard lower compiler consists only of

1. shadow holes which must spill into an earlier/higher envelope;
2. the deep ideal below rank `r-d`; and
3. competition among those non-natural pins.

This is the conceptual reason the shadow histogram predicts the compiler so
well.  The natural part of the matching is not merely easy; it is inert in
the coordinate realization.

## 6. The shadow-liquidity theorem

Assume that `A` is a length-`W+d` source word with
`D^d A=T`, where `T` is a one-path lower-`d`-fresh rank-`r` Johnson
chronology, and that `A` covers the lower ideal.  A cell longer than `d+1`
contains a complete central window `T_i`, so it has rank at least `r`.
Thus every lower target is witnessed in one of the top `d` short rows.

Let

\[
 N_q=\binom{k}{r-q},
\]

and, for `1<=q<=d`, let `h_q` be the number of rank-`r-q` targets missing
from the `W-q` internal cells `L_i^(q)`.  Let `c_q` be their repeat excess.
Since all internal cells have the correct rank, counting occurrences gives

\[
 \boxed{c_q-h_q=W-q-N_q.}
 \tag{6.1}
\]

We first isolate the boundary bookkeeping which is easy to miscount.

### Lemma 6.0 (boundary classification)

Let `P` be the maximal depth-`d` erosion of `T` and put

\[
                         C_{q,t}:=(D^{d-q}P)_t
 \qquad(0\le t<W+q).
\]

For a nominal lower depth `q`, the interior cells are exactly

\[
                         C_{q,t}=L_{t-q}^{(q)}.
 \tag{6.0a}
\]

for `q<=t<=W-1`.  The `q` left-boundary cells are exactly

\[
                         L_0^{(0)},L_0^{(1)},\ldots,L_0^{(q-1)},
 \tag{6.0b}
\]

and the right-boundary formula is

\[
 C_{q,W+s}=L_{W-q+s}^{(q-1-s)}
 \qquad(0\le s<q).
 \tag{6.0c}
\]

If one continues into deeper short rows, the descendants of these cells lie
on exactly `q` fixed-start inclusion chains at the left and `q` fixed-end
inclusion chains at the right.  Consequently these deeper boundary regions
can supply at most `2q` distinct new rank-`r-q` targets.

#### Proof

A maximal short cell is the intersection of all complete central windows
which contain it.  In the interior there are `q+1` consecutive such windows,
so (5.1) gives (6.0a).  At the left end there are only the first `t+1`
windows, giving (6.0b); reversal gives (6.0c).  Holding a truncated start
(respectively end) fixed while moving down the short triangle only shrinks
the source interval, so the actual OR cells form an inclusion chain.  There
are `q` truncated starts and `q` truncated ends.  An inclusion chain contains
at most one distinct set of a fixed rank, proving the final assertion.
\(\square\)

For `q>=0`, define the **prefix liquidity**

\[
 S_0=0,
 \qquad
 S_q=\sum_{j=1}^{q}(W+j)-\sum_{j=1}^{q}N_j.
 \tag{6.2}
\]

The first sum is the complete physical capacity of the top `q` short rows.

### Theorem 6.1 (shadow-prefix liquidity)

A necessary condition for such a resident flat-middle universal word is,
for every `q<=d`,

\[
 \boxed{S_q\ge0,\qquad h_q\le S_{q-1}+2q.}
 \tag{6.3}

Equivalently, the hole inequality is

\[
 \boxed{
 h_q+\sum_{j=1}^{q-1}N_j
 \le \sum_{j=1}^{q-1}(W+j)+2q.}
 \tag{6.4}

#### Proof

Every target in ranks `r-1,...,r-q` must be witnessed in the top `q` short
rows, apart from moving along their boundary chains; counting the whole rows
already includes those boundary cells.  Their total size is
`sum_(j<=q)(W+j)`, proving `S_q>=0`.

Now fix a rank-`r-q` target absent from its natural interior row.  It cannot
occur in an interior row below that row, whose maximal rank is smaller.
Thus all `h_q` such targets, together with **every** target in the higher
`q-1` ranks, must fit in the complete top `q-1` rows or in a boundary chain
of nominal depth at most `q`.  Lemma 6.0 gives exactly `2q` such
fixed-start/fixed-end chains, and each contributes at most one distinct
target of rank `r-q`.  This is
(6.4), which rearranges to the second part of (6.3).
\(\square\)

The theorem is a necessary rank-prefix bound, not a sufficiency claim.
Containment labels can reduce the usable prefix capacity, and the pointwise
intersection of all selected pin labels is the additional owner condition
treated in Section 7.

### Corollary 6.2 (the Catalan hinge in odd dimension)

Let `k=2r-1`, so `N_1=W`, and put

\[
                         b=W-N_2=\frac{2W}{r+1}=C_r.
\]

Then

\[
 \boxed{S_1=1,\qquad S_2=b+3,}
 \tag{6.5}
\]

and every resident flat-middle one-path construction necessarily satisfies

\[
                         \boxed{h_1\le2,\qquad h_2\le5.}
 \tag{6.6}

More precisely, once natural rank-`r-1` occurrences are reserved,

\[
                         \boxed{h_2\le c_1+4=h_1+3.}
 \tag{6.6a}

#### Proof

Equation (6.2) gives

 \[
 S_1=W+1-W=1.
\]

Also

\[
 S_2=(W+1)+(W+2)-(W+(W-b))=b+3.
\]

Condition (6.3) gives (6.6).  \(\square\)

For the refinement (6.6a), the first internal row has exactly `c_1`
duplicate cells left
after one natural occurrence of every present rank-`r-1` target is reserved.
This reservation is a charging device, not a hidden normal-form assumption:
if a present rank-`r-1` target is witnessed away from its chosen natural
occurrence, the alternative witness is either another natural occurrence
(charged to `c_1`) or lies on its endpoint fixed-start/fixed-end chain.  In
the latter case the freed chosen cell lies on the same chain and cannot
create a second distinct rank-`r-2` value beyond the chain's one.  Thus a
missing rank-`r-2` target can be charged only to one of the `c_1` off-chain
duplicate cells or to one of the four depth-two boundary chains.  Equation
(6.1) at `q=1` gives `c_1=h_1-1`.  \(\square\)

The significance is structural.  Before depth two, there is only one unit
of prefix slack, so the second lower shadow must be almost perfect.  After
the first two ranks, the scalar prefix slack is `b+3`: the Catalan bulk `b`
plus the three-cell triangular boundary contribution.  This is a capacity
bank, not yet a labelled or owner-compatible routing.

The raw exact chronologies lie inside these necessary bounds:

\[
\begin{array}{c|c|c}
k&d&(h_1,h_2,\ldots)\\ \hline
9&2&(1,1)\\
10&2&(0,0)\\
11&3&(1,1,0)\\
12&2&(0,0)\\
13&3&(1,0,0)\\
14&2&(0,0).
\end{array}
\tag{6.7}
\]

Thus the one-hole boundary flags in the solved odd cases are not decorative
features of their presentations.  They are the visible use of the single
unit of liquidity available before the Catalan release.

The completed `L^(1)` row has `W` vertices and the rank-`r-2` target layer
has `W-b` members.  If its edge intersections cover that layer, retaining
one edge of every colour leaves a forest with

\[
                         W-(W-b)=b
\]

components.  This is exactly the Catalan `A`-forest in the four-sector lift.
Thus the same equation `N_2=W-b` simultaneously explains:

* the Catalan bulk `b` in the depth-two compiler prefix slack `b+3`;
* the number of components in the both-new lift sector; and
* the amount `b` removed from `4W` in the child-width identity
  `W^+=4W-b`.

These are one phenomenon.

### Corollary 6.3 (`k=15` diagnosis before Hall)

For `k=15`, `r=8`, `W=6435`, `d=3`, and

\[
                         b=C_8=1430.
\]

Hence any resident flat-middle one-path optimum must have

\[
                         h_1\le2,\qquad h_2\le5.
\]

The Hall-29 carrier has `(h_1,h_2)=(4,21)`, so it exceeds the two scalar
prefix capacities by `2` and `16`.  The clean Hall-31 carrier has
`(2,22)`, so it passes the first gate but exceeds the second by `17`.
Neither chronology can compile at length `B(15)`, independently of any
particular matching algorithm or owner anchoring.

This does not lower-bound the full Hall deficiency by the sum of those
excesses: the same carried cells can participate in coupled Hall witnesses.
It does prove that the next carrier objective should explicitly enforce the
depth-two corridor, rather than optimize only the terminal all-lower
matching score.

## 7. The labelled reserve and owner meet dimension

Let a lower target `S` be assigned injectively to a short physical interval
`I_S`.  At source position `p`, let `E_p` be the maximal middle envelope and
let

\[
                         \mathcal O_p=\{S:p\in I_S\}.
\]

The final maximal source entry is

\[
                         A_p=E_p\cap\bigcap_{S\in\mathcal O_p}S.
 \tag{7.1}
\]

The owner meet dimension `kappa_p` is the minimum number of labels from
`O_p` whose intersection with `E_p` already equals (7.1).

### Proposition 7.1 (trace-two realization criterion)

Suppose every `kappa_p<=2`.  Choose active owners `O_p^1,O_p^2` (repeating
or omitting one when `kappa_p<2`) and put

\[
                         A_p=E_p\cap O_p^1\cap O_p^2.
\]

The pin family is realized with middle row `T` if and only if:

1. `A_p` is nonempty for every `p`;
2. `union_(p in [i,i+d]) A_p=T_i` for every middle window; and
3. `union_(p in I_S) A_p=S` for every assigned lower target.

#### Proof

Every source word respecting the fixed middle row and every negative pin is
contained in (7.1).  The chosen owners attain (7.1) by definition of
`kappa_p`.  The three displayed conditions are respectively nonzeroness,
central equality, and all positive/negative lower equalities.  They are
therefore necessary and sufficient.  \(\square\)

The exact normalized words have owner meet dimension at most one through
`k=13`; `k=14` uses dimension two at exactly five positions.  This says that
the labelled correction to Theorem 6.1 is locally very narrow even when its
target-to-cell assignment is globally nonlocal.

Combining Lemma 5.1 with Proposition 7.1 separates the compiler into a free
part and a paid part.  Natural shadow pins have no owner effect.  Only the
carried holes and the deep ideal contribute active owner cuts.

## 8. A common induction invariant

A **Pascal flag package of depth `d`** on `[k]` consists of:

1. a path cover of the rank-`r` layer and a specified seam order producing
   one middle chronology `T`;
2. lower-`d`-freshness of that chronology;
3. complete upper support among the consecutive unions of `T`;
4. completed endpoint flags for `L^(1),...,L^(d)`;
5. a labelled spill assignment satisfying the liquidity inequalities and
   containment Hall at every rank;
6. an injective assignment of the residual deep ideal whose pointwise owner
   meet dimension is at most two and which satisfies Proposition 7.1.

### Theorem 8.1 (package sufficiency)

If a Pascal flag package exists at depth `d=d(k)`, then

\[
                         \boxed{\nu(k)=B(k).}
\]

#### Proof

Use natural free pins for every retained shadow target, the spill pins for
the remaining near-middle targets, and the deep pins from item 6.  Proposition
7.1 produces a nonzero source word whose depth-`d` row is `T` and whose short
cells cover the complete lower ideal.  The middle chronology covers the
middle layer exactly, and item 3 covers the upper ideal because
`D^(d+q)A=D^qT`.  The word has length `W+d=B(k)`.  Section 1 supplies the
matching lower bound.  \(\square\)

This invariant reconciles the known cases without demanding a single cycle:

* `k=11` is a one-component package with one completed boundary flag;
* `k=13` begins with two perfect cycles and pays one seam; connectivity is
  secondary to the flag and owner data;
* `k=14` is a six-piece two-shore package, with five local width-two owner
  meets;
* the current `k=15` Hall-29 path is resident and upper-complete but is not a
  package because it fails the first two liquidity prefixes.

Theorem 4.1 says the odd-to-even lift braids two adjacent rows of a package.
Theorem 4.2 says the odd-to-odd lift braids four copies from its first Pascal
neighbourhood.  Hence a recursive proof should preserve the package, not a
specific Hamilton cycle, cyclic voltage, or parent edge set.

## 9. The genuinely open lemmas

The analysis leaves two mathematically different existence statements.

### Carrier lemma (open)

For every `k`, there is a lower-`d(k)`-fresh middle path cover with seam
ports such that its final chronology is upper-complete and its lower shadow
holes admit the labelled spill flow of Section 6.

In odd dimension, Proposition 3.2 supplies the ideal immediate-lower face
unconditionally.  The first nontrivial content is to choose or rethread that
   Middle Levels object so that the same projection has a surjective upward
`sigma`, the required residence, and the second-level corridor

\[
                         h_2\le5
\]

after a cut.  Equivalently, the completed first lower path must be almost
rainbow one level further down while its `sigma` map is surjective upward.
This is a sharper target than generic Hall minimization and is the immediate
pure-math lesson of `k=15`.

For `k=15` specifically, Corollary 3.4 reduces this carrier lemma further:
seek a complement-half-turn invariant Middle Levels Hamilton cycle with
surjective `sigma`, depth-three residence, and the deeper shadow support
required by the upper side, together with a repeated-`sigma` cut safe for
those deeper shadows.  The first two lower prefixes then close automatically
with `(h_1,h_2)=(1,<=2)`.

### Trace-two residual extension lemma (open)

After all natural flag pins and a labelled spill flow have been fixed, the
remaining deep lower ideal admits an injective short-interval assignment
such that:

1. every pointwise trace meet has dimension at most two;
2. every middle coordinate retains a private hit in its central window;
3. every target coordinate retains a private hit in its assigned interval;
4. every source position remains nonempty.

This is the smallest compiler lemma consistent with all exact data.  It is
strictly weaker than constructing the whole word: the middle chronology,
all upper targets, every natural near-middle target, and every spill target
have already been discharged.  It is also stronger than ordinary Hall,
because Hall does not imply the common pointwise meet conditions.

Both lemmas are needed.  Combining them into “every `k` has a Pascal flag
package” is a correct one-line sufficient theorem, but it does not make the
remaining mathematics one routine lemma.

## 10. Recommended mathematical direction

The exact Catalan hinge suggests the next proof should start at depth two,
not at the full compiler.

1. Start from a Middle Levels Hamilton cycle, so the lower edge colours are
   boundary-perfect for free.  Seek one whose completed lower path has at
   most three missing next-edge colours, whose upper `sigma` image is
   surjective, and whose projection has the required residence.
2. Forget connectivity until the labelled factor is built.  Path-cover seams
   cost collars; they do not change the Catalan liquidity identity.
3. Use the `b=C_r` components released at depth two as the port bank for the
   `A`-sector of the `k -> k+2` lift.
4. Prove the residual trace-two extension by a Boolean-lattice normalized
   matching argument plus a private-hit correction.  Natural shadow pins are
   already free, so only the deep residual family enters that theorem.

The central mathematical object is therefore not a Hamilton cycle and not a
standalone compiler matching.  It is a recursively nested, two-sided flag
path with a Catalan reserve and a locally width-two owner realization.
