# Bidirectional rolling resets: an orbit-balanced SCD trade and its exact `G_0` gate

Date: 2026-08-01

Status: unconditional local/all-depth phase theorem, exact quotient-chain
reduction, and finite `k=17` audit.  The construction preserves the complete
cyclic OR deck, every high-suffix inventory, full ordered rail balance, and
the owner inventory.  It does not prove the residual representative-state
Hall/rainbow condition, a connected carrier, or the lower compiler.

## 0. Verdict

Put

\[
 k=2m+1,\qquad 2\le d\le m,\qquad N=2(d+1).
\]

There is an explicit bank of `N` rank-`m` roots carrying two phases:

* a forward rolling reset;
* the same reset run backwards.

The two phases use exactly the same:

1. roots;
2. suffix-target multiset at every depth `1,...,d-1`;
3. complete ordered prefix/suffix rail boundary;
4. rank-`(m+1)` owner multiset; and
5. cyclic contiguous-OR deck at every width.

Both phases are literal legal flag cycles and require no extra owner slot.
Taking every ground-set translate gives an orbit-balanced protected bank.

At depth three, replacing the reverse bank by the forward bank therefore
preserves the necklace-SCD target selector and rail balance exactly.  In the
representative state graph `G_0`, however, only the graph induced outside
the eight protected root-orbit vertices is unchanged.  Cross incidences
through a protected tail or head can change.  Freezing the eight reset edges
reduces the remaining chronology gate exactly to one complementary rainbow
perfect matching in that common residual graph.

For `k=17`, the two residual quotient-chain Hall systems pass exactly, but
one deterministic common residual completion has representative-state
matching number only `1018/1430`.  Thus the reset and static SCD selector do
coexist; state Hall remains genuinely correlated and is not repaired by an
arbitrary chain completion.

## 1. The anchored bank

Identify the ground set with `Z_k`.  Assume first

\[
                         m\ge 2d+2.                 \tag{1.1}
\]

Put

\[
 X=\{x_0,\ldots,x_{N-1}\}=\{0,1,\ldots,N-1\},
 \qquad
 K=\{N,N+1,\ldots,m+d+1\}.                         \tag{1.2}
\]

Indices on the `x`'s are read modulo `N`, not modulo `k`.  Then

\[
 |K|=m-d,qquad |K\cup X|=m+d+2\le k.               \tag{1.3}
\]

For a cyclic interval of private coordinates write

\[
 X[a,a+s-1]=\{x_a,x_{a+1},\ldots,x_{a+s-1}\}.
\]

Define the `N` roots

\[
                         q_a=K\cup X[a,a+d-1].       \tag{1.4}
\]

They all have rank `m`.

### Lemma 1.1 (free and separated necklaces)

Every set

\[
                         K\cup X[a,a+s-1],
       \qquad 1\le s\le d+1,                       \tag{1.5}
\]

has trivial `C_k` stabilizer.  Two sets in (1.5) with the same rank are in
one rotation orbit only when they are literally equal.

#### Proof

In the cyclic binary word on `Z_k`, the consecutive block `K` has length

\[
                         m-d\ge d+2.                 \tag{1.6}
\]

Any run contained wholly in `X[a,a+s-1]` has length at most `d+1`.
If the private interval contains a suffix of `X`, that suffix merely extends
`K` to the left; the resulting run is still the unique longest run and its
right endpoint is always `m+d+1`.  The unused interval following `K` has
length `m-d-1>0`, so this run does not wrap around the ground-set cycle.

A rotation carrying one set in (1.5) to another must carry the unique
longest run to the unique longest run and hence fix its right endpoint.
The rotation is zero.  The two sets are then equal.  Taking the two sets to
be the same also proves freeness. `square`

This applies simultaneously to every root, suffix target, and owner used
below.

## 2. The two phases

At root `q_a`, define the forward flag

\[
 F_a=(q_a;x_a,x_{a+1},\ldots,x_{a+d-2})             \tag{2.1}
\]

and the reverse flag

\[
 R_a=(q_a;x_{a+d-1},x_{a+d-2},\ldots,x_{a+1}).      \tag{2.2}
\]

Each is a legal depth-`d` flag: its deletion word consists of `d-1`
distinct elements of `q_a`.

### Theorem 2.1 (bidirectional rolling-reset phase trade)

The banks `F={F_a}` and `R={R_a}` satisfy all of the following.

1. `F_a -> F_(a+1)` is a legal literal turn and the owner is

   \[
             O_a^+=K\cup X[a,a+d].                 \tag{2.3}
   \]

2. `R_a -> R_(a-1)` is a legal literal turn and the owner is

   \[
             O_a^-=K\cup X[a-1,a+d-1].             \tag{2.4}
   \]

3. Each phase has zero complete ordered rail boundary.
4. At every depth `1<=j<d`, the two banks offer the identical target
   multiset.
5. The owner multisets in (2.3)--(2.4) are identical.

Consequently either phase is an `N`-root rolling-reset cycle, and replacing
one phase by the other preserves roots, every named high-target row, full
rail balance, and owner colours with zero additional owner slots.

#### Proof

For the forward phase,

\[
 q_{a+1}=q_a-\{x_a\}+\{x_{a+d}\}.                  \tag{2.5}
\]

The deletion rail shifts left, and the new last deleted coordinate is
`x_(a+d-1)`, the unique noncore member of the bottom of `F_a`.  This is the
literal shift law, and adjoining the new coordinate gives (2.3).  The
reverse calculation is

\[
 q_{a-1}=q_a-\{x_{a+d-1}\}+\{x_{a-1}\},            \tag{2.6}
\]

with the reversed rail shift and owner (2.4).

The forward rail suffix of `F_a` is the forward rail prefix of `F_(a+1)`.
The reverse rail suffix of `R_a` is the reverse rail prefix of `R_(a-1)`.
Thus each bank is a directed circulation on the complete ordered
`(d-2)`-word states, proving item 3.

After `j` deletions, the two targets are

\[
 \begin{aligned}
  T^+_{a,j}&=K\cup X[a+j,a+d-1],\\
  T^-_{a,j}&=K\cup X[a,a+d-j-1].
 \end{aligned}                                               \tag{2.7}
\]

As `a` runs around `Z_N`, both rows of (2.7) are exactly the family of all
cyclic private intervals of length `d-j`.  This proves item 4.  Finally,

\[
                         O_a^+=O_{a+1}^-              \tag{2.8}
\]

proves item 5. `square`

By Lemma 1.1 the `N` root orbits are distinct.  Translating the whole bank
through `C_k` therefore gives `Nk` distinct flags, grouped either into `k`
forward reset rings or `k` reverse reset rings.  The translated bank remains
an exact ordered-word circulation; no averaging or denominator clearing is
being used.

## 3. The complete cyclic OR deck is phase invariant

Consider the cyclic source words

\[
 \begin{aligned}
 W^+&=(K+x_0,K+x_1,\ldots,K+x_{N-1}),\\
 W^-&=(K+x_0,K+x_{N-1},K+x_{N-2},\ldots,K+x_1).
 \end{aligned}                                               \tag{3.1}
\]

They are dihedral reversals of the same cyclic word.

### Theorem 3.1 (all-width cyclic transparency)

For every interval length `ell`, the multisets of cyclic contiguous unions
of `W^+` and `W^-` agree.  For `1<=ell<N`, this common multiset is

\[
          \{K\cup X[a,a+\ell-1]:a\in Z_N\},          \tag{3.2}
\]

and for `ell>=N` every value is `K union X`.

In particular the source-letter, root, owner, immediate-upper, and every
longer internal cyclic OR inventory are phase invariant.

#### Proof

An interval in either orientation is exactly `ell` consecutive private
letters together with the permanent core `K`.  Reversal bijects cyclic
intervals.  Formula (3.2) and the full-support case follow. `square`

This is stronger than the suffix/owner accounting in Theorem 2.1.  The
qualification **cyclic** is essential after the block is opened.

## 4. Exact quotient-SCD coexistence

For `0<=j<d`, let `P_j` be the `N` necklace orbits of the sets

\[
             K\cup X[a,a+d-j-1],\qquad a\in Z_N.     \tag{4.1}
\]

Thus `P_0` is the root bank and `P_j` is the common depth-`j` target bank.
All these orbits are free and distinct by Lemma 1.1.

Let `Gamma_j` be the quotient containment graph from rank `m-j` necklace
orbits to rank `m-j+1` necklace orbits.  Delete `P_j` from its lower shore
and `P_(j-1)` from its upper shore, obtaining

\[
                         \Gamma_j^0.                 \tag{4.2}
\]

### Theorem 4.1 (common residual-chain criterion)

Inside the adjacent-level quotient-chain-factor architecture, the forward
and reverse banks coexist with one identical residual exact named-target
selector if and only if, for every `1<=j<d`, `Gamma_j^0` has a matching
saturating its remaining lower shore.

#### Proof

At interface `j`, either phase supplies a matching between `P_j` and
`P_(j-1)`: equation (2.7) shows that the endpoint sets are identical, while
the two phases merely pair them in opposite cyclic orders.  Removing those
endpoints leaves exactly (4.2) in both phases.

If `Gamma_j^0` has a saturating matching, adjoining the phase matching gives
a saturating quotient containment matching at that interface.  Do this
independently at every rank.  Their union is a quotient chain forest, which
lifts to one equivariant flag orbit per middle-root orbit.  A target with
stabilizer `h` is offered `h` times per named translate; mark one occurrence,
as in the necklace-SCD lifting theorem.  Hence every named target is marked
once.

Conversely, a quotient chain factor containing either fixed phase restricts,
after its `P_j` endpoints are deleted, to a saturating matching of
`Gamma_j^0`. `square`

The theorem is an exact Hall reduction, not an assertion that every
`Gamma_j^0` passes automatically.  Its main gain is that the residual
problem is literally common to both phases.

## 5. The representative `G_0` effect at depth three

At `d=3`, reindex the eight roots as

\[
                         q_i=K+\{x_i,x_{i+1},x_{i+2}\}. \tag{5.1}
\]

Then

\[
 F_i=(q_i;x_i,x_{i+1}),\qquad
 R_i=(q_i;x_{i+2},x_{i+1}).                         \tag{5.2}
\]

The forward phase contributes the eight legal turns `F_i -> F_(i+1)`;
the reverse phase contributes `R_i -> R_(i-1)`.  Their eight owner-orbit
colours are the common distinct family

\[
              [K+\{x_i,x_{i+1},x_{i+2},x_{i+3}\}].   \tag{5.3}
\]

Let `G_0^+` and `G_0^-` be the owner-coloured representative state graphs
of two equivariant flag tables which agree outside this bank and use the
two phases inside it.  Let `B_L,B_R` be the eight protected vertices on the
tail and head shores.

### Theorem 5.1 (exact protected-interface statement)

The colour-preserving identity

\[
 G_0^+[L-B_L,R-B_R]
 =G_0^-[L-B_L,R-B_R]                              \tag{5.4}
\]

holds.  No stronger isolation statement is automatic: edges from a bank
tail to an exterior head and from an exterior tail to a bank head can
change under the phase switch.

If the eight internal forward (respectively reverse) ring edges are frozen,
the resulting equivariant table has an owner-exact cycle cover containing
the protected rings if and only if the common residual graph in (5.4) has a
perfect matching whose colours are exactly the owner orbits outside (5.3).

#### Proof

A literal turn and its owner are functions only of its two endpoint flags.
Two exterior flags are unchanged, proving (5.4).  A protected flag changes
its deletion order and bottom core, and its state-zero normalization may
also change, so no equality is forced on incident cross edges.

Each phase's eight internal turns form a matching of the protected tail and
head vertices and use (5.3) once.  After freezing them, all remaining tails,
heads and owner colours must be used exactly once.  This is precisely the
stated complementary rainbow perfect matching.  Conversely, adjoining such
a residual matching to the eight frozen edges gives the required quotient
matching, whose translates use every named owner once. `square`

Ordinary Hall in (5.4) is necessary but not sufficient for the coloured
statement.  On a functional owner-attachment face where the residual colour
is a bijective function of one shore, it becomes sufficient and the gate is
ordinary bipartite Hall.

Thus the phase switch is an isolated orientation flip only **after both
copies of the protected bank are deleted**.  It is not an isolated flip in
the full `G_0` incidence graph.

## 6. What opening destroys

For a linear occurrence of a block `W=(A_0,...,A_(N-1))`, put

\[
 P_j(W)=A_0\cup\cdots\cup A_{j-1},\qquad
 S_j(W)=A_{N-j}\cup\cdots\cup A_{N-1}.              \tag{6.1}
\]

Reversal gives

\[
                         P_j(W^{rev})=S_j(W),\qquad
                         S_j(W^{rev})=P_j(W).         \tag{6.2}
\]

Let `L_a` be a suffix union of the left exterior and `R_b` a prefix union of
the right exterior.  Apart from internal intervals and intervals spanning
the whole block, the crossing values are exactly

\[
             L_a\cup P_j(W),\qquad S_j(W)\cup R_b.    \tag{6.3}
\]

The spanning values

\[
                         L_a\cup\bigcup W\cup R_b     \tag{6.4}
\]

are orientation independent.  Therefore the entire exterior failure of
cyclic transparency is the prefix/suffix swap (6.2) inside the two product
families (6.3).

More precisely, write `e_Z` for one unit of multiset mass at value `Z`.
The signed boundary current of a forward-to-reverse change is

\[
 \begin{aligned}
 \Delta_W({\cal L},{\cal R})
 ={}&\sum_{a,j}
    \bigl(e_{L_a\cup S_j}-e_{L_a\cup P_j}\bigr)\\
   &+\sum_{b,j}
    \bigl(e_{P_j\cup R_b}-e_{S_j\cup R_b}\bigr).
 \end{aligned}                                               \tag{6.5}
\]

### Corollary 6.1 (exact two-block cancellation criterion)

Two simultaneous block reversals preserve their combined exterior deck if
and only if their currents (6.5) sum to zero.

In particular, suppose the two blocks have literally identical prefix and
suffix union ladders, or those ladders have been identified by an
equality-preserving ambient construction.  If their exterior ladders are
mirror copies--the left ladder of one is the right ladder of the other and
conversely--then their currents are opposite and cancel.

Mirror exterior contexts alone do not suffice when the two blocks have
different literal ladders.  Even in the sufficient identical-ladder face,
this is only an OR-deck identity: it does not assert that the four new
physical seams are legal Johnson turns or preserve owner colours.  Literal
duplication of one block would itself be incompatible with an owner-exact
factor, so a useful application needs a nontrivial equality-preserving
identification rather than two copies of the same owners.

## 7. The smallest splice obstruction

A two-cut cross-splice of two directed components would be a nontrivial
`2 <-> 2` exchange of ordered Boolean diamonds.

### Lemma 7.1 (no nondegenerate two-edge owner-preserving splice)

Two distinct owner-exact Johnson edges cannot be cross-reconnected while
preserving the two tail roots, two head roots, and the owner-colour multiset.

#### Proof

Let the old owner colours be distinct rank-`(m+1)` sets `O_1,O_2`.  In one
possible colour assignment after swapping the heads, both old tails must be
rank-`m` subsets of both `O_1` and `O_2`; in the other assignment, both old
heads must be.  Since two distinct rank-`(m+1)` sets have at most one common
rank-`m` subset, the two corresponding tails or heads coincide.  That makes
the exchange degenerate.  If `O_1=O_2`, owner exactness was already
violated. `square`

Hence mirror-pair deck cancellation does not by itself produce a two-ring
component splice.  Support at least three is necessary.  The known ternary
Boolean hexagon is the first central four-resource possibility, but no
embedding is presently proved that also preserves the complete reset rail,
all suffix inventories, and the exterior product families (6.3).  A
genuine regenerating cross-splice remains open at exactly that lifted
support-three gate.

## 8. Finite `k=17,d=3` audit

For `m=8`, use

\[
 K=\{8,9,10,11,12\},\qquad X=\{0,1,\ldots,7\}.       \tag{8.1}
\]

The standalone H100 O3 audit constructs all necklace orbits at ranks
`6,7,8,9`, installs the eight forced bank endpoints, solves both residual
quotient containment matchings, builds one deterministic common residual
flag table, and then constructs `G_0` literally.  It reports

```text
PASS_K17_D3_RESET_SCD_G0
orbits(B,A,Q,O)=728,1144,1430,1430
residual_chain_match=720,1136
g0_edges_old_new=3846,3889
g0_match_old_new=1018,1018
g0_reset_frozen_residual=1010/1422
protected_edges=8 protected_owner_colors=8
```

Thus:

* both residual static Hall systems pass exactly;
* the protected reset edges and their eight distinct owner colours occur;
* this particular independently completed selector fails state Hall by
  `412`, in either orientation;
* freezing the reset isolates the identical residual deficiency `412`.

The last two numbers are a scoped counterexample to **independent residual
chain completion**, not a no-go for another jointly selected necklace-SCD
completion.

The all-depth symbolic replay

```text
PASS_TWO_QUEUE_ORBIT_BALANCED_PHASE_TRADE
cases=153 d=2..10 m=2d+2..30
```

checks the two legal directions, every suffix-depth multiset, full ordered
rail balance, owner equality, and orbit separation.  A separate range audit
checks the explicit depth-three anchor through `m=200` and finds the sharp
start `m=8` for that displayed interval core.

## 9. Secondary whole-layer design and divisibility

Ignore the high-target coverage constraints and let one unoriented reset
ring be a block on its `N` roots and `N` owners.  The block hypergraph on

\[
 \binom{[k]}m\ \dot\cup\ \binom{[k]}{m+1}            \tag{9.1}
\]

has

\[
 |E|={k!\over 2N(m-d)!(m-d-1)!}                     \tag{9.2}
\]

blocks.  It is regular on both shores, with common degree

\[
 D={1\over2}
   {m!\over(m-d)!}
   {(m+1)!\over(m-d-1)!}.                            \tag{9.3}
\]

For an incident root-owner pair `q subset O`, the codegree is

\[
 \lambda_{RO}
 =\binom md\binom m{d+1}d!(d+1)!
 ={2D\over m+1}.                                    \tag{9.4}
\]

For two Johnson-adjacent roots, the codegree is

\[
 \lambda_{RR}(1)
 =\binom{m-1}{d-1}\binom m{d+1}(d-1)!(d+1)!
 ={2D\over m(m+1)}.                                 \tag{9.5}
\]

The interval-position count shows that pairs at larger Johnson distance
have no larger codegree under `m>=2d+2`; the owner-owner formula is the
complementary copy of (9.5).  Thus the dominant pair-codegree ratio is
`2/(m+1)`.  This is favourable for approximate matching, but the uniformity
`2N=Theta(d)` grows with `m`, and no exact absorber theorem is invoked here.

An exact root/owner decomposition has the unavoidable divisibility

\[
                         N\mid \binom{2m+1}m.         \tag{9.6}

\]

At `k=17,d=3`, `N=8` and

\[
                         \binom{17}8\equiv6\pmod8,   \tag{9.7}

\]

so a full reset-ring decomposition is impossible; any non-equivariant
packing leaves at least six roots and six owners.  If the packing is a union
of free ground-rotation orbits of blocks, it consumes roots in multiples of
`Nk`.  Since `Cat_8=1430=6 mod 8`, an equivariant packing at `k=17` leaves at
least

\[
                         6\cdot17=102                \tag{9.8}

\]

roots.  Thus an all-but-`O(d)` physical tiling, if it exists, must break
rotation symmetry in this first unresolved case.  High-target coverage and
the compiler impose further constraints not represented by (9.1).

## 10. Exact remaining theorem

The local and static rows are now closed.  The shortest surviving global
statement is:

> Choose the common residual quotient chain factor so that the coloured
> residual graph in (5.4) has the complementary rainbow perfect matching;
> then join its components by a support-at-least-three exchange whose whole
> rail and exterior boundary currents vanish.

The bidirectional reset supplies a reusable protected circulation.  The
unproved content is the correlated residual `G_0` choice and the lifted
ternary-or-larger splice, not residence, named-target bookkeeping, or cyclic
OR transparency inside the reset bank.
