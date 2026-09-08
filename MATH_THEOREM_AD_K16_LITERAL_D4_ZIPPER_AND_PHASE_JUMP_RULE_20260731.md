# The exact `k=15 -> 16` facet substitution is a literal `D^4` zipper

Date: 2026-07-31  
Lane: AD  
Status: unconditional theorem for the promoted `k=15` and `k=16` words;
dimension-free local zipper lemma; conditional component-absorption rule;
no all-`k` recurrence or new value of `nu(k)` is claimed

## 0. Verdict

The frozen shifted-chunk theorem identifies the 49 mixed-rank entries of
the exact `k=16` depth-three row as the lower facets of one four-edge path
and one 45-edge cycle.  The present theorem supplies the missing literal
chronology.

Each of those 49 tagged `D^3` facet windows has a one-cell extension which
is exactly one of the 49 omitted tagged rank-nine owners.  The resulting
occurrence-labelled `D^4` extension graph has 96 edges and is

\[
                         P_8\ \dot\cup\ P_{90}.       \tag{0.1}
\]

It therefore has a unique perfect matching.  This upgrades the previously
known 128-edge containment matching from a marginal allocation statement to
49 literal nested interval witnesses in the actual word.

The complete first band now has a transparent decomposition:

* plain `D^3` and `D^4` windows cover every untagged rank-eight and
  rank-nine target;
* tagged `D^2` windows together with the 49 low `D^3` bridge windows cover
  every tagged rank-eight target;
* the 6386 high tagged `D^3` windows together with the 49 matched tagged
  `D^4` windows cover every tagged rank-nine target.

The two conspicuous numbers have exact but different meanings:

\[
 45=15\cdot3
\]

is the whole short parent component, while

\[
 49=45+(3+1)                                             \tag{0.2}
\]

is that component plus the four depth-three windows crossing the pinned
singleton.  The affine shift jump is 45 because global indexing skips the
same short component.  None of these facts proves that a comparable short
component exists in every dimension.

## 1. Notation and authenticated input

For a word `A=(a_0,...,a_(n-1))`, write

\[
 D^qA_i=\bigcup_{j=0}^{q}a_{i+j},\qquad 0\le i<n-q.  \tag{1.1}
\]

Let

\[
 A^{15}=\texttt{answers/k15.word},\quad
 A^{16}=\texttt{answers/k16.word},\quad
 T=D^3A^{15},\quad z=2^{15}.                         \tag{1.2}
\]

The answer-word SHA-256 values are

```text
k15  f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
k16  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

The frozen anatomy theorem proves that `T` is a lower-rainbow Johnson
two-factor with directed component intervals

\[
 C_L=T[0:6390],\qquad C_S=T[6390:6435],              \tag{1.3}
\]

and that the 49 low tagged entries of `D^3 A16` occur at starts

\[
 6386,6387,6388,6389,12825,\ldots,12869.             \tag{1.4}
\]

They replace precisely

\[
 \mathcal O_L=T[5109:5113],\qquad
 \mathcal O_S=T[6390:6435].                         \tag{1.5}
\]

All indices in this note are zero-based and all intervals of word positions
are inclusive unless written as Python half-open slices.

## 2. The exact literal zipper

### Theorem 2.1 (four forward rows and 45 backward rows)

For `0<=i<4`, the following two literal identities hold:

\[
 D^3A^{16}_{6386+i}
 =z\cup\bigl(T_{5108+i}\cap T_{5109+i}\bigr),       \tag{2.1}
\]

\[
 D^4A^{16}_{6386+i}=z\cup T_{5109+i}.               \tag{2.2}
\]

Thus the four-cell interval `[6386+i,6389+i]` is a tagged lower facet,
and extending it one cell to the right gives the omitted owner on the
five-cell interval `[6386+i,6390+i]`.

For `0<=r<45`, put

\[
 a_r=6390+((35+r)\bmod45),\qquad
 b_r=6390+((36+r)\bmod45).                          \tag{2.3}
\]

Then

\[
 D^3A^{16}_{12825+r}
 =z\cup(T_{a_r}\cap T_{b_r}),                       \tag{2.4}
\]

\[
 D^4A^{16}_{12824+r}=z\cup T_{a_r}.                \tag{2.5}
\]

Thus each tail facet is extended one cell to the left.  As `r` varies,
the indices `a_r` enumerate all 45 vertices of `C_S`.  Equations (2.1)--
(2.5) therefore give 49 distinct, literal, five-cell witnesses for exactly
the 49 omitted tagged upper owners in (1.5).

#### Proof

The audit evaluates every displayed OR directly from `A16`.  The four
targets in (2.2) are `T[5109:5113]`.  The map `r -> 35+r mod 45` is a
permutation, so the targets in (2.5) are exactly `C_S`.  Distinctness follows
also from the fact that `T` contains every parent rank-eight owner once.
No cyclic interval of `A16` is used: even the last witness is the honest
linear interval `[12868,12872]`.  \(\square\)

### Theorem 2.2 (the chronological graph is `P8 + P90`)

Let the left shore consist of the 49 occurrence-labelled low `D^3` rows
`(p,F)` in (1.4), and let the right shore be the 49 omitted owners in
(1.5).  Define the **chronological one-cell extension graph** `Xi` by

\[
 (p,F)\sim R
 \quad\Longleftrightarrow\quad
 D^4A^{16}_{p-1}=z\cup R
 \text{ or }
 D^4A^{16}_{p}=z\cup R,                            \tag{2.6}
\]

where an out-of-range derivative is simply unavailable.

Then `Xi` has 96 edges.  Both shore-degree profiles are

\[
                         1^2 2^{47},                 \tag{2.7}
\]

and its connected components have 8 and 90 vertices.  Each component is a
path, so

\[
                         \Xi=P_8\dot\cup P_{90}.     \tag{2.8}
\]

In particular, `Xi` has a unique perfect matching, namely the four right
extensions in (2.2) and the 45 left extensions in (2.5).

By comparison, the unlabelled containment graph

\[
                         F\sim R\iff F\subset R      \tag{2.9}
\]

has 128 edges and shore-degree profiles

\[
 1^1 2^{17}3^{31},\qquad 1^1 2^{18}3^{29}4^1.       \tag{2.10}
\]

Thus containment Hall is strictly weaker than literal chronology in this
very certificate, even though both graphs happen to have perfect matchings.

#### Proof

Every chronological edge is tested by the two possible five-cell intervals
in (2.6).  The audit obtains 96 edges and (2.7).  Breadth-first search gives
component orders 8 and 90.  In each component all degrees are at most two,
there are exactly two degree-one vertices, and the edge count is one less
than the vertex count; hence each is a path.  An even path has one perfect
matching, forced successively from an endpoint.  The explicit matching of
Theorem 2.1 is therefore the unique one.  The 128-edge census is recomputed
independently from (2.9).  \(\square\)

## 3. The complete literal first band

### Theorem 3.1 (rank eight and rank nine decompose into four decks)

Let `Omega=[15]`.  In the fixed word `A16`, all rank-eight and rank-nine
targets on `Omega union {z}` are covered by the following selected literal
interval families.

| child shore | selected intervals | distinct old projections |
|---|---|---:|
| rank 8, no `z` | plain rank-eight `D^3` | 6435 |
| rank 8, with `z` | tagged rank-eight `D^2` outside the bridge, plus the 49 low tagged `D^3` rows | `6386+49=6435` |
| rank 9, no `z` | plain rank-nine `D^4` | 5005 |
| rank 9, with `z` | 6386 high tagged rank-nine `D^3` rows, plus the 49 matched `D^4` rows of Theorem 2.1 | `6386+49=6435` |

More exactly, the set of old rank-seven projections supplied by tagged
rank-eight `D^2` rows has size 6388.  Its intersection with the 49 bridge
facets is

\[
                     \{\mathtt{0x5b06},\mathtt{0x730c}\}.     \tag{3.1}
\]

Consequently the 6386 `D^2` projections outside the bridge, together with
all 49 bridge facets, are a disjoint copy of the complete rank-seven layer.
The high tagged `D^3` projections and the 49 matched `D^4` projections are
disjoint and their union is the complete parent rank-eight layer.

#### Proof

The four assertions are set equalities, not just cardinality checks.  The
audit compares each projected set against the corresponding Boolean layer
on 15 coordinates.  The two tagged-middle sets have sizes 6388 and 49,
intersection (3.1), and union size 6435.  Removing the intersection from
the `D^2` side gives `6386+49` distinct selected occurrences.  The tagged
upper equality is Theorems 2.1--2.2 together with the frozen identity that
the high `D^3` rows are exactly the other 6386 parent owners.  Finally,
Pascal partitions each child layer according to absence or presence of
`z`.  \(\square\)

This theorem is a literal first-band cover and selected-occurrence
decomposition.  It is stronger than the slot-counting facet substitution,
but it is not a common-cap compiler and says nothing yet about ranks beyond
nine or about a common lower-envelope schedule.

## 4. Dimension-free local lemmas

### Lemma 4.1 (exact one-cell facet-repair criterion)

Let `W` be any linear word on `Omega union {z}` and fix integers `d>=0` and
`r>=1`.  Suppose there are `b` occurrence-labelled low rows

\[
                         D^dW_{p_i}=z\cup F_i,
 \qquad F_i\in\binom{\Omega}{r-1},                  \tag{4.1}
\]

and a bank `O` of `b` omitted owners in `binom(Omega,r)`.  Form the graph
`Xi_W` by the analogue of (2.6).

There exists a degree-exact one-step repair which uses each low occurrence
once, each omitted owner once, and only a one-cell left or right extension
if and only if `Xi_W` has a perfect matching.

#### Proof

A matching edge is already an actual nested pair of intervals in the one
fixed word:

\[
                         z\cup F_i\subset z\cup R.   \tag{4.2}
\]

Selecting a perfect matching gives the required bijection with no further
compatibility condition, because the intervals may overlap.  Conversely,
each pair in a repair of the stated subclass is an edge of `Xi_W`; using
every occurrence and owner once gives a perfect matching.  \(\square\)

The qualification “of the stated subclass” is essential.  Ordinary target
coverage need not use bridge slots bijectively, and a target may have a
longer or remote witness.  Conversely, `F subset R` alone does not create an
edge of `Xi_W`: either adjacent cell may add a contaminating coordinate.

### Lemma 4.2 (directed path/cycle zipper)

Let `V_0,...,V_t` be a directed rank-`r` Johnson path with distinct lower
edge colours `F_i=V_(i-1) intersect V_i`.  If consecutive low `D^d` cores
are `z union F_i` and their right one-cell extensions are `z union V_i`,
then they form a slot-preserving forward zipper for the `t` nonroot path
owners.

Let `V_0,...,V_(s-1)` be a directed rank-`r` Johnson cycle with distinct
lower edge colours.  If consecutive low cores are
`z union (V_i intersect V_(i+1))` and their left extensions are
`z union V_i`, then they form a slot-preserving backward zipper for every
cycle owner.

#### Proof

The displayed extensions themselves give the required bijections.  The
distinct-edge-colour hypothesis ensures that the low cores are distinct and
therefore retain the path/cycle slot count.  \(\square\)

Lemma 4.2 is the literal upgrade of the frozen cycle/path facet-substitution
lemma.  The exact `k=16` bridge is one forward path zipper of length four
and one backward cycle zipper of length 45.

### Theorem 4.3 (first-band Pascal criterion)

Let `d>=1` and `|Omega|=2r-1`.  A single word on `Omega union {z}` covers the complete
child ranks `r` and `r+1` if the following four literal conditions hold.

1. Its `z`-free `D^d` intervals cover `binom(Omega,r)`.
2. Its `z`-free `D^(d+1)` intervals cover `binom(Omega,r+1)`.
3. Selected tagged `D^(d-1)` intervals and selected low tagged `D^d`
   intervals cover `z+binom(Omega,r-1)`.
4. Its high tagged `D^d` intervals and a chronological-extension matching
   for the omitted owners cover `z+binom(Omega,r)`.

If each family is bijective as stated, this is an exact selected occurrence
decomposition of the two layers.

#### Proof

Partition each Boolean layer according to whether it contains `z`:

\[
 \binom{\Omega\cup\{z\}}r
 =\binom\Omega r\ \dot\cup\
   \bigl(z+\binom\Omega{r-1}\bigr),                 \tag{4.3}
\]

\[
 \binom{\Omega\cup\{z\}}{r+1}
 =\binom\Omega{r+1}\ \dot\cup\
   \bigl(z+\binom\Omega r\bigr).                  \tag{4.4}
\]

The four hypotheses cover the four disjoint summands.  \(\square\)

## 5. Why the shifts are `5112,5157,36,6426`

### Lemma 5.1 (common-phase cut of a strict spiral)

Let a cyclic group of order `q` act by `R`, and let a strict `q`-sheet
spiral with base block `P` of length `n` be

\[
 P\,\Vert R^gP\,\Vert\cdots\Vert R^{(q-1)g}P.      \tag{5.1}
\]

Assume explicitly that `gcd(g,q)=1`, so these are all `q` sheets of one
strict orbit.

Suppose the desired clean subgroup displacement is `R^s`, and choose a
representative `0<=tau<q` satisfying

\[
                         g\tau\equiv s\pmod q.       \tag{5.2}
\]

Cutting before sheet `tau` rotates the linear spiral into chunks of lengths

\[
                         (q-\tau)n,\qquad \tau n.    \tag{5.3}
\]

If both chunks are required to be nonempty, assume `0<tau<q`.

#### Proof

There are `q-tau` sheets after the cut and `tau` before it, each containing
`n` entries.  Equation (5.2) is exactly the group displacement of the first
post-cut sheet.  \(\square\)

For the authenticated parent,

\[
 q=15,\qquad g=4,\qquad s=3,
\]

and the unique solution of `4 tau = 3 mod 15` is `tau=12`.  The quotient
component base lengths are 426 and 3.  Formula (5.3) gives

\[
 3\cdot426=1278,\quad12\cdot426=5112,
\]

\[
 3\cdot3=9,\quad12\cdot3=36,                       \tag{5.4}
\]

which are exactly the four plain-rail chunk lengths.  The actual parent
source starts are `5112,0,6426,6390`.  When each chunk is instead written
as `T[(j+delta) mod 6435]` using its global output index `j`, the four
affine shifts `delta` are `5112,5157,36,6426`, as in the frozen anatomy.

### Lemma 5.2 (component-skip phase jump)

Write a parent global order as one main component `C[0:L)` followed by a
reserved component bank of total length `S`; thus `W=L+S`.  Let the plain
main rotation start at `a`, put `alpha=a+1`, and omit `c` predecessor owners
from the tagged high copy.  Its retained high order is

\[
 C[\alpha:L)\ \Vert\ C[0:\alpha-c).                \tag{5.5}
\]

Assume

\[
 0\le a<L,\qquad 0\le c\le\alpha=a+1\le L,
\]

and regard all positions in `C` and in the reserved bank as distinct,
occurrence-labelled owners.  Index the retained high output (5.5) from
zero.  For two nonempty displayed chunks one further needs
`c<alpha<L`.

It has length `L-c`, and the omitted owner bank has size

\[
                              S+c.                  \tag{5.6}
\]

When the two chunks in (5.5) are expressed as affine functions of their
global output index modulo `W`, their shifts are

\[
                         \alpha,\qquad\alpha+S.      \tag{5.7}
\]

Their difference is therefore exactly `S`.

#### Proof

The lengths in (5.5) are `L-alpha` and `alpha-c`, summing to `L-c`.
The omitted owners are the `S` reserved-component owners and the `c` owners
`C[alpha-c:alpha)`.  At the first index of the second chunk, the global
output index is `L-alpha`; adding the proposed shift gives

\[
 (L-\alpha)+(\alpha+S)=L+S=W\equiv0\pmod W,
\]

so (5.7) is exact.  \(\square\)

For `k=16`,

\[
 L=6390,\quad S=45,\quad a=5112,\quad
 \alpha=5113,\quad c=4.                            \tag{5.8}
\]

Thus the high chunks have lengths `1277` and `5109`, their shifts are
`5113` and `5158`, and

\[
                  5158-5113=S=45,\qquad S+c=49.     \tag{5.9}
\]

So 45 is not an unexplained optimizer offset: it is the global-index toll
for jumping over the reserved short component.

## 6. Why the collar has four rows

In a linear word of length `n`, a cell at position `p` belongs to

\[
 \min(p,n-d-1)-\max(0,p-d)+1                       \tag{6.1}
\]

windows of `D^d` whenever this quantity is positive.  In particular, under
the precise interior condition

\[
                         d\le p\le n-d-1,
\]

there are exactly `d+1` such windows, with starts

\[
                         p-d,p-d+1,\ldots,p.         \tag{6.2}
\]

The exact word has

\[
                         A^{16}_{6389}=z.            \tag{6.3}
\]

The four depth-three windows containing this pinned singleton start at
`6386,6387,6388,6389`, exactly the four forward-zipper rows.  Hence the
fixture identity is

\[
 49=|C_S|+|\Gamma_3|=45+(3+1),                      \tag{6.4}
\]

where `Gamma_3` is the canonical crossing block of a depth-three splice.
The equality `c=d+1` follows here from the literal singleton collar.  It is
not asserted to be necessary for every possible even lift.

## 7. Conditional component-absorption rule and exact open gate

Combining Lemmas 4.1--5.2 gives the following reusable sufficient rule.

> Start with a directed lower-rainbow parent factor.  Reserve whole
> components of total trace-owner mass `S` as one contiguous post-main bank in
> the chosen global indexing, choose a main-component collar of `c` owners,
> impose the retained-high order (5.5), and rotate all strict spirals at one
> compatible sheet phase.
> If one child word realizes (i) a forward facet zipper on the collar,
> (ii) backward facet zippers on the reserved cycles, and (iii) the four
> first-band deck conditions of Theorem 4.3, then the child first band is
> literal and hole-free.  Its tagged high shifts differ by `S`, and its
> bridge bank has exactly `S+c` slots.

This statement neither requires nor supplies a Hamilton parent.  Retaining
a small component can be useful because it can become a complete cyclic
facet zipper if the required literal zipper chronology exists.

The exact all-dimension gate is now sharply separated into four questions.

1. Does an appropriate odd parent factor always have a reserved component
   bank with controllable mass `S` and compatible strict-spiral phase?
2. Can the abstract facet substitutions be realized simultaneously as
   overlapping derivative rows of one integral word?
3. Can the same zippers preserve every deeper upper shadow and redistribute
   residence runs?
4. Does the resulting chronology admit the integral common-cap lower
   compiler?

The present theorem closes the first-band literal chronology for the exact
`k=16` certificate only.  It does not answer these four uniform questions.
In particular, 45 is fixture-specific; the reusable formula is `S+c`, not
`45+d+1` and not `3q+d+1`.

## 8. Reproducibility

Run

```text
python3 scratch/audit_ad_k16_literal_d4_zipper_phase_rule_20260731.py
```

The audit reads only the promoted answer words.  It verifies every `D^3`
and `D^4` identity, reconstructs both graphs, proves the `P8 + P90`
decomposition and unique matching, and checks the four exact first-band set
equalities.  For the separately authenticated strict-spiral parameters
`q=15,g=4,s=3` and base lengths `426,3`, it checks the phase arithmetic; it
does not rediscover those parameters.  Its output is

```text
scratch/ad_k16_literal_d4_zipper_phase_rule_20260731.audit.json
```

The independent trace-level audit

```text
MATH_AUDIT_AD_K16_D3_TWO_SHIFT_AND_49_FACET_BRIDGE_20260731.md
```

separately authenticates the parent cycles, shifted chunks, facet order,
and 128-edge containment census.  It does not assume the search or compiler
model used to find either word.
