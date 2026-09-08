# The K16 equality word is a component jump plus a cap--facet bridge

Date: 2026-07-31  
Status: exact solver-free K15/K16 certificate identity and general
cap--facet accounting lemma; no all-dimension bridge or compiler theorem

## 0. Result

Let

\[
 T=D^3(\texttt{answers/k15.word}),\qquad
 E=D^3(\texttt{answers/k16.word}).
\]

The parent row `T` is a permutation of all `6435` old rank-eight sets.  The
child row `E` is not flat:

\[
 |E_i|=9\ (0\le i<6386),\qquad
 |E_i|=8\ (6386\le i<12870),                         \tag{0.1}
\]

and all `12870` entries are distinct.  Relative to the new bit `z=0x8000`,
the row consists of

\[
 6390\text{ tagged entries},\quad
 6435\text{ untagged entries},\quad
 45\text{ tagged entries}.                          \tag{0.2}
\]

Deleting `z` from the tagged entries exposes the exact construction law.

* `6386` entries are old rank-eight caps copied from `T` in two shifted
  chunks.
* The remaining `49` entries are rank-seven facets.
* The `6435` untagged entries are all of `T`, in four exact chunks.
* The missing `49` caps and the `49` facets have a `128`-edge containment
  graph with a perfect matching.  More strongly, the matching is the
  incoming-edge-colour map on one rooted four-edge path and one complete
  45-edge Johnson cycle.

The two shift parameters differ by `45` because the odd parent carrier has
cyclic components of orders `6390` and `45`; the tagged cap branch skips the
small component.  The number `49` is

\[
                 49=45+(3+1):                       \tag{0.3}
\]

the skipped component plus the four-owner `D^3` cut halo.  It is not the
three-cell closed-splice excess.  That excess is paid separately by
discarding two parent compiler halos and compiling both child shores against
one depth-three staircase.

This gives the correct candidate even recurrence: lift and braid the
**owner deck**, allow a cap/facet mixture in its maximal envelopes, then
solve one child common-cap compiler.  Literal deletion from two already
compiled parent words is the wrong normal form.

## 1. Exact raw identities

All indices in this section are zero based and intervals are half open.  Put

\[
                         W=6435.
\]

The authenticated inputs are

```text
answers/k15.word
  SHA f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
answers/k16.word
  SHA 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
  SHA c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

### Proposition 1.1 (the two parent cycles)

The rows

\[
 T[0:6390],\qquad T[6390:6435]                     \tag{1.1}
\]

are Johnson cycles of orders `6390` and `45`.  Every internal adjacency and
both displayed closure edges have symmetric difference two.  The linear
join `T[6389]--T[6390]` is also Johnson, while the whole-row wrap
`T[6434]--T[0]` is not.

This is the deck-level form of the two-component odd parent retained in the
three-primary spiral audit.

### Proposition 1.2 (the marked projection)

List the entries of `E` containing `z` in their original order and delete
`z`; call the resulting length-`W` sequence `M`.  Then

\[
 M_j=T_{j+5113\pmod W}\quad(0\le j<1277),          \tag{1.2}
\]

\[
 M_j=T_{j+5158\pmod W}\quad(1277\le j<6386).       \tag{1.3}
\]

The final `49` entries `M[6386:6435]` are distinct rank-seven facets, not
entries of `T`.  The cap indices absent from (1.2)--(1.3) are exactly

\[
 Q=[5109,5113)\ \dot\cup\ [6390,6435),             \tag{1.4}
\]

of sizes `4` and `45`.

The shift jump is literal:

\[
                         5158-5113=45.              \tag{1.5}
\]

### Proposition 1.3 (the unmarked projection)

List the entries of `E` omitting `z`; call the resulting sequence `A`.
Then `A` is all of `T`, once each, with the four formulas

\[
\begin{array}{c|c|c}
\text{global }j&\text{shift}&\text{parent indices}\cr\hline
[0,1278)&5112&[5112,6390)\cr
[1278,6390)&5157&[0,5112)\cr
[6390,6399)&36&[6426,6435)\cr
[6399,6435)&6426&[6390,6426).
\end{array}                                         \tag{1.6}
\]

Thus (1.6) is the large parent cycle opened at `5112`, followed by the small
parent cycle opened at `6426`.

### Proposition 1.4 (the exact lower-edge-colour bridge)

Join a missing cap `T_q`, `q in Q`, to a bridge facet `F` when

\[
                              F\subset T_q.          \tag{1.7}
\]

The resulting `49` by `49` bipartite graph has `128` edges and a perfect
matching.  It has a canonical block-respecting perfect matching.  Orient
both parent cycles as displayed.  The four halo facets are exactly

\[
 T_{5108+i}\cap T_{5109+i},\qquad 0\leq i<4,        \tag{1.8}
\]

the incoming lower edge colours of the rooted path
`T[5108:5113]`.  The remaining `45` facets are exactly the incoming lower
edge colours of the complete small cycle, in one cyclic rotation.  Thus the
four halo caps match the first four bridge facets, and the `45`
small-component caps match the remaining `45` facets.  The four halo pairs
are

```text
T[5109]=0x5b0e -> 0x5b06
T[5110]=0x538e -> 0x530e
T[5111]=0x53cc -> 0x538c
T[5112]=0x43ce -> 0x43cc.
```

Each arrow deletes one bit.  Combining this bridge matching with the
literal cap/facet containments at the other `6386` tagged owners gives a
perfect inclusion matching from all old rank-eight caps to all old
rank-seven facets.  The stronger edge-colour description explains why the
bridge retains the same number of chronology slots, rather than merely
giving a set-theoretic matching.

## 2. The physical construction schedule

The frozen rank-eight child carrier has `12870` owners.  With starts
`0,1,...,12869` and omitted deadlines

\[
                         \{0,1,6388\},              \tag{2.1}
\]

the authenticated physical word realizes every carrier owner literally.
The support spans are

\[
                         2^{6386}3^{6484}.           \tag{2.2}
\]

Relative to the carrier target and its maximal four-cell envelope:

\[
\begin{array}{c|c|c|c}
\text{shore/mode}&\text{count}&\text{target}&\text{maximal envelope}\cr\hline
A&6435&C&C\cr
B\text{ cap mode}&6386&z\cup F&z\cup C,\quad F\subset C\cr
B\text{ facet mode}&49&z\cup F&z\cup F.
\end{array}                                         \tag{2.3}
\]

The `B` targets in (2.3) enumerate all old rank-seven facets, while the `A`
targets enumerate all old rank-eight caps.  Hence they are exactly all
rank-eight targets on sixteen coordinates.

The first `6386` cap-mode envelopes are the rank-nine block in (0.1).  The
four large-component bridge facets, the two `A` blocks, and the `45`
small-component bridge facets form the rank-eight block.  The unique
rank transition is a containment step `9 -> 8`; all same-rank transitions
are Johnson.

The independently extracted *first-middle* staircase of the final word has
the alternative omitted-deadline set `{0,2,6389}`.  That is not a
contradiction: (2.1) is the construction ownership schedule, whereas a
physical word may deliver some rank-eight targets earlier than their
prescribed owner.  The derivative row (0.1) is independent of this choice.

## 3. Why the shifts differ by 45 and why the bridge has 49 rows

The arithmetic is a general component/cut identity.  Let a parent deck have
total order

\[
                         W=n+s,                     \tag{3.1}
\]

with a large cyclic component indexed `[0,n)` and a small component indexed
`[n,W)`.  Open the large `A` copy at `c`.  Its parent-index order is

\[
                         [c,n)\,[0,c).              \tag{3.2}
\]

When (3.2) is written as `T_(j+shift mod W)`, its two shifts are

\[
                         c,\qquad c+s,              \tag{3.3}
\]

and therefore differ by `s`.

For a depth-`d` cap-mode `B` copy in the observed one-step shifted-cut
normal form, replace the rooted owner path

\[
                         H=[c-d,c]                  \tag{3.4}
\]

by exact facets and omit the small component from cap mode.  The remaining
cap order is

\[
                         [c+1,n)\,[0,c-d).          \tag{3.5}
\]

Its shifts are

\[
                         c+1,\qquad c+s+1,          \tag{3.6}
\]

again differing by `s`, and its bridge set has size

\[
                         h=s+d+1.                   \tag{3.7}
\]

The root is the preceding cap `T[c-d-1]`, so (3.4) has `d+1` nonroot
vertices and exactly `d+1` incoming lower edge colours.  At word level the
`d` cross-cut depth-`d` windows account for `d` of these rows and the
one-step shore offset accounts for the endpoint row.  Hence `s+d+1` is
forced inside this literal shifted-cut normal form.  This is not a lower
bound for arbitrary even lifts: a general lift can use different ports,
more cuts, or a different compiler, and still has to realize every facet
value and deeper shadow physically.

For K16,

\[
 n=6390,\quad s=45,\quad c=5112,\quad d=3.         \tag{3.8}
\]

Equations (3.3), (3.6), and (3.7) give respectively

\[
 5157-5112=45,qquad 5158-5113=45,qquad h=45+4=49,
\]

which are exactly (1.2)--(1.6).

The number `45` is consequently not a universal collar constant.  It is the
order of the second cyclic component of this odd parent.  In the genuine
four-filter seed it also appears as the rank-seven tail after the unique
deficient triple-OR row at index `6390`.

For this parent, even the component order has a quotient explanation.  Both
parent cycles are free \(\mathbb Z_{15}\)-lifts of quotient cycles with
voltage `+4`: their quotient orders are 426 and 3.  A quotient cycle of
order `a` and voltage `v` over a free cyclic group of order `g` has lifted
component order

\[
                         a g/\gcd(g,v).             \tag{3.9}
\]

Indeed, one quotient circuit adds `v` to the fibre coordinate.  Here
\(g=15\), \(v=4\), and the voltage is primitive, so the small component has
order `3*15=45`.  Combined with the one-step depth-three rooted path, this
gives `h=3*15+(3+1)=49`.  The quotient order three and voltage four are
properties of the chosen K15 factor, not an all-dimension guarantee.

### Lemma 3.1 (cyclic quotient normal form)

Let `g=2r-1`.  Cyclic rotation acts freely on the rank-`r` caps and on the
rank-`r-1` facets, and the number of cap orbits is

\[
             \frac{1}{g}\binom{g}{r}=\operatorname{Cat}_{r-1}. \tag{3.10}
\]

Consequently, whenever a lower-rainbow Johnson factor is chosen
equivariantly under this rotation, each quotient cycle of order `a` and
voltage `v` lifts to `gcd(g,v)` physical components, each of order

\[
                         a g/\gcd(g,v).             \tag{3.11}
\]

#### Proof

A set fixed by a nonidentity rotation is a union of rotation orbits whose
common size is a nontrivial divisor of `g`.  That divisor would divide its
rank, impossible because both `gcd(g,r)` and `gcd(g,r-1)` are one.  Hence
the action is free, and the Catalan identity in (3.10) is immediate.  One
trip around a quotient cycle translates the fibre by `v`; this translation
has `gcd(g,v)` orbits, each of length `g/gcd(g,v)`, which proves (3.11).
\(\square\)

Lemma 3.1 is a genuine all-dimension reduction.  Proposition 4.3 below
shows that the rainbow factor can in fact be chosen equivariantly.  What it
does not control is the quotient cycle partition, its voltages, or any
physical ports.

## 4. General cap--facet substitution lemma

Let `V` have size `2r-1`, let `z` be new, and put

\[
                         W={2r-1\choose r}.
\]

Let `C` be the rank-`r` sets of `V`, let `F` be the rank-`r-1` sets, and
let

\[
                         \phi:C\longrightarrow F    \tag{4.1}
\]

be a perfect inclusion matching:

\[
                         \phi(C)\subset C.          \tag{4.2}
\]

Choose any exceptional set \(Q\subseteq C\), of size `h`.  Define the child
middle targets and proposed maximal envelopes by

\[
\begin{array}{c|c|c}
\text{owner}&\text{target}&\text{envelope}\cr\hline
A_C&C&C\cr
B_C&z\cup\phi(C)&z\cup C,\quad C\notin Q\cr
B_C&z\cup\phi(C)&z\cup\phi(C),\quad C\in Q.
\end{array}                                         \tag{4.3}
\]

### Theorem 4.1 (two-rank deck identity)

The targets in (4.3) enumerate every rank-`r` subset of \(V\cup\{z\}\)
exactly once.  Every target is contained in its envelope, all envelopes are
distinct within each of the three rows of (4.3), and their rank census is

\[
 \boxed{
  \#\operatorname{rank}r=W+h,qquad
  \#\operatorname{rank}(r+1)=W-h.}                 \tag{4.4}
\]

#### Proof

The `A` targets are exactly the rank-`r` sets omitting `z`.  Since `phi` is
bijective, the `B` targets are exactly `z` joined to the rank-`r-1` sets of
`V`.  These are the two disjoint shores of the child middle layer.
Containment is (4.2).  The `A` envelopes omit `z`; cap-mode `B` envelopes
contain `z` and have rank `r+1`; facet-mode `B` envelopes contain `z` and
have rank `r`.  Injectivity inside each row follows from injectivity of `C`
or `phi`.  Counting the rows gives (4.4).  \(\square\)

### Lemma 4.2 (rainbow Johnson-factor specialization)

Let `J` be an oriented spanning two-factor of the Johnson graph on the
rank-`r` subsets of `V`.  For each cap `C`, let `pred(C)` be its predecessor
on its oriented component and define its incoming lower edge colour by

\[
                     \lambda(C)=\operatorname{pred}(C)\cap C.
\]

If the colours `lambda(C)` are pairwise distinct, then `lambda` is a
perfect inclusion matching from the rank-`r` layer to the rank-`r-1`
layer.  Moreover, let `Q` be a disjoint union of complete oriented cycles
of `J` and directed path blocks

\[
                    C_1,C_2,\ldots,C_t
\]

with roots `C_0=pred(C_1)` outside the corresponding block.  Replacing the
slots `C_i` by \(\lambda(C_i)=C_{i-1}\cap C_i\) gives `t` vertices of a
rank-`r-1` Johnson path (and hence `t-1` lower-path edges), preserving the
`t` nonroot slots.  Replacing all slots of a selected cycle gives a
rank-`r-1` Johnson cycle of the same length.

#### Proof

There are equally many rank-`r` and rank-`r-1` subsets of a `(2r-1)`-set,
so pairwise distinctness makes `lambda` bijective.  Inclusion is immediate.
Consecutive incoming colours are two distinct `(r-1)`-subsets of the common
rank-`r` cap `C_i`, hence differ by one exchange and are Johnson adjacent.
The same argument includes the last--first pair on a cycle.  The number of
incoming edges equals the number of selected nonroot vertices.  \(\square\)

### Proposition 4.3 (unconditional equivariant rainbow-factor supply)

For every \(r\ge2\) and every ground set `V` of size `2r-1`, a spanning
lower-rainbow Johnson two-factor as in Lemma 4.2 exists.  After cyclically
labelling `V`, it can be chosen equivariantly under coordinate rotation.

#### Proof

Form the bipartite inclusion graph between the rank-`r` caps and the
rank-`r-1` facets.  It is balanced and `r`-regular.  By Lemma 3.1, cyclic
rotation acts freely on both shores and hence also on its edges.  The
quotient is therefore a balanced `r`-regular bipartite **multigraph**: an
edge orbit incident to one vertex orbit contributes one unit of quotient
degree.

A regular bipartite multigraph has a one-factorization.  Choose two
edge-disjoint quotient perfect matchings.  The full rotation orbit of one
chosen quotient edge is a perfect matching between its two endpoint orbits;
therefore the two quotient matchings lift to two edge-disjoint invariant
perfect matchings of the full inclusion graph.  Their union is a disjoint
union of alternating even cycles.  Project each such cycle onto its cap
vertices.  Consecutive caps meet in the intervening facet and are Johnson
adjacent.  Every cap occurs once, and every intervening facet occurs once
globally, so the projected cycles form the required equivariant
lower-rainbow two-factor.

There is no projected two-cycle: a physical inclusion four-cycle would
require two distinct rank-`r-1` facets inside the intersection of the same
two distinct rank-`r` caps, which is impossible.  \(\square\)

This closes both abstract and equivariant parent-factor supply.  It gives no
control of quotient component sizes or voltages, prescribed roots, cut
ports, residence, deeper shadows, or the physical compiler.  In particular
it does not imply that a component of bounded order, or one of order `45`,
exists in general.

For K16, the parent two-factor is rainbow, and the exceptional set `Q` is
the whole 45-cycle together with the four nonroot vertices following
`T[5108]`.  Lemma 4.2 therefore supplies the perfect matching in Theorem
4.1 and the exact internal chronology of both substituted blocks.  Port
compatibility between blocks, realization as a derivative row, and all
deeper shadows remain separate physical conditions.  In the literal child
row the four path facets and the 45 cycle facets are separate physical
blocks, with the whole plain rail between them; no adjacency between the
last path facet and the first cycle facet is asserted.

### Lemma 4.4 (adjacent-row owner recovery)

For an oriented lower-rainbow cycle `C_0,...,C_(s-1)`, put

\[
                         F_i=C_i\cap C_{i+1}
\]

with cyclic indices.  Then

\[
                         F_{i-1}\cup F_i=C_i.       \tag{4.5}
\]

Consequently a derivative row containing the consecutive marked facets
\(z\cup F_i\) automatically contains every marked owner \(z\cup C_i\) one
derivative later.  If an unmarked `C_0` is placed immediately before
\(z\cup F_0\), their typed seam supplies \(z\cup C_0\), so an entire cycle
can be facetified without changing its number of slots.

For a rooted path, the same union identity recovers every internal parent
vertex.  Its boundary owners require explicit typed seams or external
ports.  Conversely, placing the owners in one row does not by itself force
the facets one row earlier; that direction requires a tight physical
erosion identity.

#### Proof

The two facets in (4.5) are distinct rank-`r-1` subsets of the rank-`r`
set `C_i`, so they omit different elements and their union is `C_i`.  The
derivative and seam assertions are literal OR identities.  \(\square\)

This adjacent-row exchange is the other half of the slot rule.  Lemma 4.2
gives the canonical facet-to-head matching and internal chronology; Lemma
4.4 shows why a facet-mode component reconstructs its omitted owner deck.
It still does not provide the external ports, tight erosions on owner-mode
arcs, or the common lower compiler.

For K16, `h=49`, so (4.4) is

\[
              6435+49=6484,\qquad6435-49=6386.      \tag{4.6}
\]

The observed rank imbalance is `2h=98`.  It records shore composition, not
the three saved compiler cells.  More generally, `h` cancels from the total
slot count in Theorem 4.1; it need not be uniformly bounded for the deck
algebra.  Boundedness may still matter for constructing ports and a physical
compiler.

### Lemma 4.5 (the scalar one-switch schedule)

Let \(d\ge1\), put `q=W-h`, and set `L=2W+d`.  At owner start
`i=0,...,2W-1`, choose the inclusive physical interval

\[
 I_i=\begin{cases}
 [i,i+d-1],&0\le i<q,\\
 [i,i+d],&q\le i<2W.
 \end{cases}                                      \tag{4.7}
\]

The first `q` owners are therefore served at depth `d-1` and the remaining
`W+h` owners at depth `d`.  The unused physical starts are
`[2W,2W+d)`, and the omitted deadlines are exactly

\[
              \{0,1,\ldots,d-2\}\cup\{q+d-1\}.    \tag{4.8}
\]

All used deadlines are strictly increasing, and the union of every
consecutive owner family `I_a,...,I_b` is one physical interval.

#### Proof

The first deadline block is `[d-1,q+d-2]` and the second is
`[q+d,2W+d-1]`, giving exactly (4.8).  The first block is empty when `q=0`,
and `0,...,d-2` is empty when `d=1`.  Consecutive intervals overlap or
abut, so their union has no gap.  \(\square\)

Thus every bridge size `h` has a legal chain-aligned equality-length owner
schedule.  This is only chronology: it does not assert that the proper-prefix
lower-cell catalogue has enough scalar capacity.  That capacity row and the
integral common compiler remain part of the lower-coverage hypothesis.  The
other missing step is realizing all owner ORs simultaneously by nonzero
cells while preserving upper coverage.

### Corollary 4.6 (physical sufficient interface)

Suppose the envelopes (4.3) are ordered on a chain-aligned depth-`d` owner
schedule and have one common nonzero physical preimage.  If contiguous
unions of the owner targets or envelopes realize every upper target, and the
physical preimage realizes every lower target, then that preimage is a
universal word of length

\[
                         2W+d.                      \tag{4.9}
\]

This is the deadline-staircase transfer theorem applied to (4.3).  It is a
sufficient interface, not a proof that the order, preimage, or lower
compiler exists.

## 5. Halo fusion is what removes the closed-splice excess

Let the exact odd parent have length

\[
                         W+d_{\rm old}.
\]

The closed word splice duplicates the already compiled word and has length

\[
                         2W+2d_{\rm old}.            \tag{5.1}
\]

A deck lift of the form (4.3), followed by one child common compiler, has
the target length

\[
                         2W+d_{\rm new}=B(2r).       \tag{5.2}
\]

Thus the exact saving is

\[
                         q=2d_{\rm old}-d_{\rm new}.\tag{5.3}
\]

This is a **halo-fusion identity**: two old compiler halos are discarded and
one child halo is rebuilt.  It does not assign one local carrier event to
each saved cell.  In particular, at K16

\[
                         q=3,qquad h=49.            \tag{5.4}
\]

The facet bridge makes the child carrier physically admissible; the common
compiler pays the length saving.  Confusing `h`, `2h`, and `q` obscures the
mechanism.

The four solved even cases calibrate the distinction:

| child | old/new depth | closed-splice saving | final `D^d` row | certified mechanism |
|---:|:---:|---:|:---|:---|
| 10 | `2/2` | 2 | `rank5^252` | direct carrier; natural lift failed residence |
| 12 | `3/2` | 4 | `rank6^924` | repaired/six-piece full-facet carrier |
| 14 | `3/2` | 4 | `rank7^3432` | six-piece full-facet carrier |
| 16 | `3/3` | 3 | `rank9^6386 rank8^6484` | mixed cap/facet bridge plus common cap |

At K12 and K14 the favourable depth drop permits a flat child envelope row;
the adjacent-intersection shore is entirely in facet mode.  K16 has no
depth drop, so the large tagged block stays mostly in cap mode and only the
one-cut halo plus the small component move to facet mode.  K10 supplies no
automatic odd-to-even seed rule; it is evidence only for carrier/compiler
separation and the one-halo length accounting.

## 6. Exact conditional even recurrence

The preceding identities isolate a proof-safe all-dimension target.

### Theorem 6.1 (conditional deck-lift recurrence)

For each even `k=2r`, suppose one can supply:

1. a lower-rainbow oriented Johnson two-factor on the odd cap deck and an
   exceptional set `Q` made of complete components and rooted path blocks;
2. a port-compatible ordering of the cap/facet envelopes (4.3) which has a
   chain-aligned depth-`d_k` physical preimage;
3. at most `C` missing upper targets and at most `C'` missing lower targets
   after literal replay.

Then

\[
                         \nu(k)\le B(k)+C+C'.        \tag{6.1}
\]

If `C+C'` is bounded uniformly, this gives `B(k)+O(1)` on the even steps.
If both are zero, it gives exact even induction.

#### Proof

Theorem 4.1 supplies every middle target.  Chain alignment transfers every
certified upper owner interval to the physical word.  Append one singleton
letter for each remaining upper or lower target.  This adds at most `C+C'`
letters to (4.9).  \(\square\)

The theorem is unconditional as an implication, but its hypotheses are not
known in all dimensions.  In particular, the following remain open:

* a uniform component/cut and port rule producing the ordered cap/facet
  bridge (the abstract rainbow factor itself exists by Proposition 4.3);
* protected residence and upper shadows after the braid;
* a uniform integral common-cap compiler with bounded defect.

Therefore neither an unconditional `B(k)+O(1)` theorem nor exact even
induction is claimed here.

## 7. Solver evidence versus theorem

The identities in Sections 1--3 are direct deterministic replays of the
authenticated words.  Theorems 4.1 and 6.1, Lemmas 4.2 and 4.4, and
Proposition 4.3 are solver-independent.  The historical SAT/common-cap solve
is provenance for how the
K16 word was found, but universality and every number used here are checked
literally from the frozen word.

The reproducer is

```text
scratch/audit_even_k16_two_rank_facet_bridge_20260731.py
```

and writes

```text
scratch/even_k16_two_rank_facet_bridge_20260731.audit.json
```

The audit also compares the closed K15 splice with the exact K16 derivative.
The closed splice has `D^3` rank census

\[
 8^{6435}9^{6436}10^1 11^1
\]

with one duplicate; the equality word replaces a `51`-value splice-only set
by `49` new rank-eight values.  Hence the exact word rebuilds the owner deck;
it is not a three-row trim of the closed-splice derivative.
