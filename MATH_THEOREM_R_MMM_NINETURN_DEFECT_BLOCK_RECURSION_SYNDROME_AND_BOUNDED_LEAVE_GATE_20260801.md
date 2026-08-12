# Standard MMM nine-turn defect blocks: exact recursion, block hypergraph,
# syndrome, and the bounded-leave gate

Date: 2026-08-01  
Lane: R, secondary additive-constant target  
Status: exact raw-defect recursion, exact padded-block hypergraph and lattice,
exact finite-state sufficient theorem, and a sharp no-go for a naive
four-copy recursion.  A uniform `O(1)` block leave is not proved.

## 0. Outcome

The finite sequence

\[
                D_4=3,\qquad D_5=22,\qquad D_6=117             \tag{0.1}
\]

has an exact Catalan explanation.  The raw canonical MMM missing turns are
cyclic three-forests whose three Dyck components are all nonempty.  If
`C(z)` is the Catalan generating function, then

\[
 D_n={2n+1\over3}[z^{n-1}](C(z)-1)^3
     ={2n+1\over n-1}\binom{2n-2}{n-4}.                        \tag{0.2}
\]

The padded nine-turn blocks form a canonical six-uniform hypergraph on the
two defect shores.  After complementing the upper shore, an edge is exactly
a partition

\[
 \Omega=H\mathbin{\dot\cup}G\mathbin{\dot\cup}
                Q_0\mathbin{\dot\cup}Q_1\mathbin{\dot\cup}Q_2,
 \qquad |H|=|G|=n-4,quad |Q_i|=3.                              \tag{0.3}
\]

It uses `H union Q_i` on the lower shore and `G union Q_i` on the
complemented upper shore.  This normal form gives exact degrees, codegrees,
a two-coordinate padding morphism, and a conserved coordinate vector over
`F_3`.

Let `nu_n` be the maximum number of disjoint blocks in the endpoint-induced
hypergraph.  Its balanced leave is

\[
                         \rho_n=D_n-3\nu_n.                    \tag{0.4}
\]

Thus the desired central statement is precisely `rho_n=O(1)`.  The frozen
audits prove

\[
                   \rho_4=0,\qquad \rho_5=1,qquad \rho_6\ge6, \tag{0.5}
\]

where the last row is only a lower bound: no `37`-block witness was frozen.
These values neither prove nor refute bounded leave.

Two exact positive reductions survive.

1. A uniform bound on the balanced block-free independence number implies
   `rho_n=O(1)` by a greedy maximal packing.
2. A finite family of padded residual states closes induction if every
   lifted state plus the newly born child defects has a block matching to a
   next state.  This is the exact finite residual-gadget criterion.

There is also a real recursive obstruction.  The exact ratio `D_(n+1)/D_n`
shows that the child defect is not four tagged parent copies plus `O(1)`
correction.  The discrepancy has magnitude asymptotic to `2D_n/n` and is
unbounded.  Any successful Pascal recursion must perform a macroscopic
cross-sector rebundling or carry a statefully normalized defect bank.

At service level, every block is a `3 by 3` crown in the lower--upper
containment graph.  Residual closure is ordinary augmenting-path matching;
the audited crossed rerouter is its shortest one-block move.  This supplies
a plausible finite **relational** basis, but not a uniform literal padded
packet basis.

All statements below concern turn-colour service unless an explicit
physical hypothesis is stated.  Residence, deeper windows, topology,
occurrence linkage, common cap, and compiler chronology do not follow from
the block hypergraph.

## 1. Exact raw MMM defect grammar

Use the paper parameter `n`: the middle-levels ground has size `2n+1`, and
the two missing turn palettes have ranks `n-1` and `n+2`.

The raw canonical MMM upper turns, up to cyclic rotation, are exactly

\[
                              1u1v1,                            \tag{1.1}
\]

where `u,v` are Dyck words of total semilength `n-1`.  Every binary cyclic
word of excess three has a cyclic three-forest form

\[
                              1a1b1c.                            \tag{1.2}
\]

The attained turns are those for which at least one of `a,b,c` is empty;
the missing turns are exactly those for which all three are nonempty.
Reverse-complementation gives the same grammar on the lower shore.

### Theorem 1.1 (closed defect count)

For every `n>=4`, the raw missing count on either shore is (0.2), equivalently

\[
 D_n=(2n+1){(n-2)(n-3)\over(n+1)(n+2)}\operatorname {Cat}_{n-1}.
\tag{1.3}
\]

#### Proof

Put `E(z)=C(z)-1=zC(z)^2`.  A missing word with a distinguished one of its
three cyclic separators is an ordered triple of nonempty Dyck words, so the
number of pairs `(labelled missing word, distinguished separator)` is both
`3D_n` and

\[
                  (2n+1)[z^{n-1}]E(z)^3.
\]

This gives the first expression in (0.2).  Since

\[
 [z^{n-4}]C(z)^6={3\over n-1}\binom{2n-2}{n-4},               \tag{1.4}
\]

the second follows.  Routine Catalan algebra gives (1.3).  \(\square\)

The component-size compositions explain the first cases directly:

\[
\begin{array}{c|c|c}
n&\text{positive semilength types}&D_n\\ \hline
4&(1,1,1)&3\\
5&(1,1,2)&22\\
6&(1,1,3),(1,2,2)&117.
\end{array}                                                    \tag{1.5}
\]

### Proposition 1.2 (peak-insertion recursion)

Inserting one adjacent Dyck peak `10` at any cyclic seam of a raw missing
word gives a raw missing word at parameter `n+1`.  Conversely, for `n>=4`,
every raw missing word at parameter `n+1` has a peak whose deletion leaves a
raw missing word at parameter `n`.

#### Proof

In the representation (1.2), any seam is inside a Dyck component or adjacent
to one of its separator symbols.  Inserted `10` may be concatenated to the
corresponding component on the appropriate side; it remains a nonempty Dyck
word.  Conversely the three component semilengths sum to `n`.  For `n>=4`,
one component has semilength at least two.  Deleting an adjacent peak from
that component leaves a nonempty Dyck word and does not change the other two.
\(\square\)

This is a recursive grammar for the **raw** defect bank.  A Hamiltonizing
pull changes turn occurrences, so the defect set of a glued endpoint is not
automatically the peak lift of a parent endpoint.

### Theorem 1.3 (exact count recurrence and four-copy obstruction)

For `n>=4`,

\[
 {D_{n+1}\over D_n}
 = {2(2n-1)(2n+3)(n-1)\over
             (n-3)(n+3)(2n+1)}.                              \tag{1.6}
\]

Consequently

\[
 D_{n+1}-4D_n
 =D_n{-4n^2+58n+42\over (n-3)(n+3)(2n+1)},                   \tag{1.7}
\]

whose absolute value is asymptotic to `2D_n/n` and is unbounded.

Therefore a recursion whose child defect is four disjoint tagged copies of
the parent defect plus or minus only `O(1)` targets cannot reproduce the raw
MMM defect sequence while retaining bounded leave.

#### Proof

Divide the two consecutive closed forms in (0.2) to obtain (1.6); subtract
four to obtain (1.7).  Since `D_n` is exponential and the rational factor in
(1.7) is `-2/n+O(n^-2)`, its magnitude diverges.  The final assertion is a
counting contradiction.  \(\square\)

The last statement is deliberately scoped to a four-tagged-copy recursion.
It does not obstruct a repaired child lift with macroscopic cross-sector
trades.

## 2. Exact complement-side block hypergraph

Let

\[
 \mathcal L_n\subseteq\binom\Omega{n-1},\qquad
 \mathcal U_n\subseteq\binom\Omega{n+2}                       \tag{2.1}
\]

be the lower and upper defect banks of one chosen endpoint, of common size
`D`.  Replace the upper bank by

\[
             \mathcal C_n=\{\Omega\setminus U:U\in\mathcal U_n\}
                         \subseteq\binom\Omega{n-1}.           \tag{2.2}
\]

### Lemma 2.1 (five-cell partition normal form)

A padded nine-turn block is exactly a partition (0.3) for which

\[
                  H\cup Q_i\in\mathcal L_n,
 \qquad           G\cup Q_i\in\mathcal C_n
                  \qquad(i=0,1,2).                            \tag{2.3}
\]

#### Proof

The original lower colours are `A_i=H union Q_i`.  Its upper colours are

\[
 B_{ij}=H\cup Q_i\cup Q_j.
\]

The unused part of the ground is a set `G` of size `n-4`, and

\[
                 \Omega\setminus B_{ij}=G\cup Q_k,
                 \qquad\{i,j,k\}=\{0,1,2\}.                  \tag{2.4}
\]

This proves both directions.  \(\square\)

For fixed disjoint cores `H,G`, put

\[
 \mathcal E_{H,G}=\{Q\in\tbinom{\Omega\setminus(H\cup G)}3:
       H\cup Q\in\mathcal L_n, G\cup Q\in\mathcal C_n\}.   \tag{2.5}
\]

The remaining ground has size nine.  A block on `(H,G)` is exactly a
three-edge perfect matching of this local three-graph.  This is the smallest
exact local recognition problem.

### Theorem 2.2 (unrestricted ambient counts)

If both shores contain every rank-`(n-1)` set, the block hypergraph has

\[
 |\mathcal B_n^{\rm all}|
 =\frac{(2n+1)!}{(n-4)!^2(3!)^3,3!},                         \tag{2.6}
\]

and every vertex has degree

\[
 d_n=10\binom{n-1}{3}\binom{n+2}{6}
    ={1\over2}\binom{n-1}{3}^2\binom{n+2}{3}.                \tag{2.7}
\]

Two vertices on one shore have codegree `binom(n-1,3)` exactly when their
intersection has size `n-4`, and zero otherwise.  A left/right pair has
codegree

\[
 \begin{cases}
  \binom{n-1}{3}^2,&|A\cap C|=0,\\
  10,&|A\cap C|=3,\\
  0,&\text{otherwise}.
 \end{cases}                                                \tag{2.8}
\]

In particular the maximum normalized pair-codegree is `O(n^-3)`.

#### Proof

Count the unordered partition (0.3) to obtain (2.6).  For a fixed left
vertex, choose its active triple, choose `G` from the complement, and split
the remaining six coordinates into two unordered triples; this gives the
first expression in (2.7), equivalent to the second.

Two same-shore vertices in one block must share the core `H`; their third
active triple can be any three-subset of the `n-1` remaining coordinates.
For a cross-shore pair, either the two vertices use distinct active triples
and are disjoint, or they use the same active triple and meet in exactly
three coordinates.  These choices give (2.8).  Division by (2.7) gives the
last assertion.  \(\square\)

The endpoint-induced hypergraph need not inherit any of this regularity.
The frozen `n=6` endpoints already have block-isolated defect vertices.
Thus ambient nibble or design theorems cannot be invoked without a new
induced-degree/expansion theorem.

## 3. Exact packing, padding, and bounded-state criteria

Let `nu(B_n)` be the matching number of the six-uniform induced block
hypergraph.  Every block removes three vertices from each shore, proving
(0.4).

### Definition 3.1 (balanced independence)

Let `alpha_bal(B_n)` be the largest integer `t` for which there are
`X subset L_n`, `Y subset C_n`, with `|X|=|Y|=t`, such that no block is
contained in `X union Y`.

### Theorem 3.2 (greedy bounded-leave criterion)

Every inclusion-maximal block packing leaves at most
`alpha_bal(B_n)` vertices on each shore.  In particular, a uniform bound

\[
                         \alpha_{\rm bal}(\mathcal B_n)\le C  \tag{3.1}
\]

proves `rho_n<=C`.

#### Proof

A matching removes equally many vertices from the two equal shores, so its
leave is balanced.  If the leave contained a block, the matching was not
maximal.  Apply Definition 3.1.  \(\square\)

This is a strong but checkable supersaturation target.  Minimum degree alone
does not imply it.

### Lemma 3.3 (two-coordinate padding morphism)

Adjoin new coordinates `a,b`.  The maps

\[
 A\longmapsto A\cup\{a\},qquad
 C\longmapsto C\cup\{b\}                                  \tag{3.2}
\]

send every abstract block at parameter `n` to a block at parameter `n+1`:
replace `H,G` by `H+a,G+b` and leave the three `Q_i` unchanged.  In original
upper notation both the lower and upper masks acquire `a`.

This is a hypergraph embedding whenever the displayed padded vertices
belong to the chosen child defect banks.  Proposition 1.2 supplies such a
raw-defect embedding when `a,b` are inserted as a common peak; a glued MMM
endpoint requires a separate provenance theorem.

### Theorem 3.4 (finite residual-state induction)

Fix an absolute `C` and a finite set `S` of residual types.  Suppose that for
every dimension and every reachable `s in S` there are balanced residual
banks

\[
                         R_{n,s}=(R^-_{n,s},R^c_{n,s}),
 \qquad |R^-_{n,s}|=|R^c_{n,s}|\le C,                         \tag{3.3}
\]

and a padding embedding `iota_n` with the following transition property.
If a parent packing leaves `R_(n,s)`, then the child vertices not covered by
the lifted parent matching—namely the newly born child vertices together
with `iota_n(R_(n,s))`—have a block matching leaving `R_(n+1,s')` for some
`s' in S`.

Then every descendant dimension has a block packing with leave at most `C`.

#### Proof

Lift every parent block by Lemma 3.3.  These lifted blocks cover precisely
the padded images of the parent vertices outside its residual.  By
hypothesis, a disjoint transition matching covers the complementary birth
bank and padded old residual outside the declared next state.  Their union
is the required child matching.  Induct from any supplied base state.
\(\square\)

This is the exact finite-gadget-basis theorem.  The substantive missing row
is existence of the transition matching; (1.7) proves that it must rebundle
a macroscopic birth bank rather than make only bounded corrections.

There is a separate limitation on a **literal** finite padded basis.  For a
residual shore `R`, put

\[
             a(R)=\left|\bigcup_{S\in R}S-\bigcap_{S\in R}S\right|. \tag{3.4}
\]

### Lemma 3.5 (active-diameter test for literal padded gadgets)

A coordinate-padded copy of a fixed gadget on `a` active coordinates can
service only residual shores with `a(R)<=a`.  Consequently a finite literal
padded gadget family has one uniform active-diameter bound.  Residual states
of unbounded active diameter would require either several independently
placed gadgets or a genuinely relational/nonliteral packet family.

#### Proof

Outside the active coordinates every mask in one padded shore has the same
fixed membership.  Hence every coordinate in the displayed union-minus-
intersection lies in the active set.  Take the maximum over a finite family.
\(\square\)

The distinct reduced `n=5` and `n=6` crossed-rerouter orbits refute one
particular padded orbit, but do not prove unbounded active diameter.

## 4. The block lattice and residual syndrome

For a balanced bank `X=(X_L,X_C)`, define

\[
 \Sigma(X)=\sum_{A\in X_L}{\mathbf 1}_A-
             \sum_{C\in X_C}{\mathbf 1}_C
             \quad\in\mathbb F_3^\Omega.                      \tag{4.1}
\]

### Theorem 4.1 (exact `F_3` block invariant)

Every block has syndrome zero.  Consequently every packing leave `R`
satisfies

\[
 \Sigma(R)=\Sigma(\mathcal L_n,\mathcal C_n),qquad
 |R_L|\equiv|\mathcal L_n|,\quad
 |R_C|\equiv|\mathcal C_n|\pmod3.                            \tag{4.2}
\]

#### Proof

For the partition (0.3), the sum of its three left incidence vectors minus
the sum of its three right incidence vectors is

\[
                         3({\mathbf 1}_H-{\mathbf 1}_G),        \tag{4.3}
\]

zero over `F_3`.  A packing subtracts a sum of such vectors.  Each edge also
has three vertices on each shore.  \(\square\)

Thus a finite residual basis must carry every reachable syndrome.  Blocks
alone can transform one residual into another only when their syndromes
agree.

There are also integer, not merely modular, coordinate cuts.  In original
upper notation let `d_j^-,d_j^+` be the full defect degrees of coordinate
`j`, and let `r_j^-,r_j^+` be its residual degrees.  Then every packing obeys

\[
\begin{aligned}
 &(d_j^+-r_j^+)-(d_j^--r_j^-)\ge0,\\
 &2(d_j^--r_j^-)-(d_j^+-r_j^+)\in 3\mathbb Z_{\ge0}.         \tag{4.4}
\end{aligned}

Indeed a block contributes respectively one on every active `Q` coordinate
and three on every `H` coordinate.  In particular

\[
 |R^-|\ge\max_j(d_j^--d_j^+)_+,qquad
 |R^+|\ge\max_j(d_j^+-2d_j^-)_+.                              \tag{4.5}
\]

For the six best audited `n=5` endpoints, after one common coordinate
normalization, the lower degree vector is constant `8`, while the upper
degree vector is

\[
                         (14,15,13,14,\ldots,14).              \tag{4.6}
\]

The unique one-pair leave carries syndrome `e_1-e_2`.  For the canonical
and best one-glue `n=6` fixtures the lower vector is constant `45` and the
upper vector is

\[
                         (72,74,70,72,\ldots,72),              \tag{4.7}
\]

so the syndrome is `2(e_1-e_2)`.  Together with the zero `n=4` state these
three rows suggest, but do not prove, the phase law
`(n-4)(e_1-e_2) mod 3`.  Syndrome and count congruence permit a three-pair
leave at `n=6`; the exact no-`38`-block result shows that a further nonlinear
matching cut is active.

## 5. Relational residual closure by containment flow

Let `G_n` be the bipartite containment graph

\[
 L\in\mathcal L_n,quad U\in\mathcal U_n,qquad
                         L\sim U\iff L\subset U.               \tag{5.1}
\]

Every nine-turn block induces the `3 by 3` crown `C_6`: each lower
`H+Q_i` is contained in the two upper pairwise unions using `Q_i`.  Choosing
one crown matching in every packed block gives a bulk service matching.

### Proposition 5.1 (exact augmenting-path residual criterion)

Relative to any bulk crown matching `M`, complete service exists if and only
if the unmatched defect vertices can be joined by the vertex-disjoint
`M`-alternating augmenting paths occurring in the symmetric difference with
some perfect matching of `G_n`.  The number of unserviceable lower targets
in a maximum service matching is exactly

\[
 \delta(G_n)=\max_{X\subseteq\mathcal L_n}(|X|-|N(X)|).       \tag{5.2}
\]

#### Proof

This is Berge's symmetric-difference decomposition and Hall's deficiency
formula applied to `G_n`.  \(\square\)

The audited crossed four-by-four rerouter is precisely the shortest move in
which one unmatched pair is routed through one crown.  It closes every
audited `n=5` one-pair block leave and the named nonnested `n=6` isolated
pair at service level.  The currently exposed relational templates are

1. a nine-turn crown;
2. a nested unit edge; and
3. a crossed crown-plus-residual augmenting path.

The `n=5` and `n=6` crossed rows are distinct reduced coordinate orbits.
Thus one fixed literal padded crossed gadget is not a universal basis.  A
uniform bound on `delta(G_n)` or on the required augmenting-path state would
still give a finite **relational** residual theorem; neither is proved.

## 6. Finite evidence and exact scope

The frozen finite results are:

* `n=4`: two labelled gluing-tree endpoints; one has one block and leave
  zero.
* `n=5`: all `112` labelled gluing-tree selections that pass the Hamilton
  audit have `22` defects per shore.  Exactly six have a unique seven-block
  packing, leaving one nonnested pair.  The crossed rerouter gives complete
  service for each of those six.
* `n=6`: the canonical endpoint has `117` defects and `274` candidate
  blocks.  A block-isolated lower hole and two block-isolated upper holes
  occur, and an exact search excludes `38` blocks, proving leave at least
  six.  All `56` one-glue Hamilton selections retain isolated vertices; the
  best has `275` candidates and still no `38`-block packing.  No
  `37`-block witness is part of the certificate.

The counts `112` and `56` are counts of labelled tree selections passing the
Hamilton test; physical edge-set injectivity between all selections is not
needed and is not asserted.

The grammar of Section 1 is the raw canonical factor grammar.  The complete
`n=4,5` and scoped `n=6` endpoint audits do not establish one recursive
family of defect **sets**.  Equality of their scalar defect counts is not a
block-hypergraph recursion theorem.

Finally, “nine-turn” is a signed palette width, not a physical chronology
width.  One translated block uses three `C_10` circuits and replaces fifteen
old factor seams before any exterior gluing.  A valid simultaneous packing
must additionally supply private old patches, compatible factor topology,
the augmented occurrence matching, residence, protected deeper witnesses,
negative-provider reserve, and one common-cap compiler.  The first physical
crossed compound exists at active ground eleven but has many short runs; the
separate eleven-coordinate full reset passes all guards but requires a
private reset socket whose recursive supply is open.

Therefore an `O(1)` block or service leave would be enough for the terminal
palette charge in a `B(k)+O(1)` theorem only after the physical spine exports
all other carried defects in a bounded state.  The present theorem proves
the exact combinatorial target and the failure of the naive recursion, not
an unconditional additive-constant upper bound.

## 7. Sharp remaining alternatives

Any one of the following would close the central bounded-leave row.

1. **Balanced supersaturation:** prove
   `alpha_bal(B_n)<=C` for a prospectively selected endpoint family.
2. **Finite-state cover-down:** exhibit residual templates and transition
   matchings satisfying Theorem 3.4, with their `F_3` syndromes included in
   the state.
3. **Relational service:** prove `delta(G_n)<=C` and physically realize a
   bounded family of augmenting-path packets.

A no-go would follow from an unbounded lower bound on the block-isolated
vertices, the minimum syndrome-representative length, `alpha_bal`, or
`delta(G_n)`.  None is presently proved for a recursively selected MMM
endpoint family.
