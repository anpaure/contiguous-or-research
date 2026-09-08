# Core-pinned wide gaps force a full optional core inside the wall

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional asymptotic structural reduction.  It does not
eliminate the optional core.

## 0. Outcome

The one-coordinate wall can be coinstantiated with the depth-wide
forbidden-bank refinement.  For the resulting protected path bank, every
surviving optional co-small obstruction contains a second sharp-shadow
core entirely in the wall.

More precisely, put

\[
 D=d-3.
\]

Fix the pinned coordinate `q_0`.  If `B^-` is a positive canonical
optional core and `Q` is its positive-owner family, write

\[
 B_i=\{x\in B^-:\mathbf1_{q_0\in x}=i\},\qquad
 Q_i=\{U\in Q:\mathbf1_{q_0\in U}=i\}.
\]

Then, for all sufficiently large `m`,

\[
 |Q_0|\le |B_0|,
 \qquad
 |Q_1|>|B_1|,
\tag{0.1}
\]

and every member of `Q_1` contains at least `D` members of `B_1`.
Consequently

\[
 \boxed{|B_1|\ge {2d-7\choose d-4}+1,}
\tag{0.2}
\]

and, after deleting the common pinned coordinate,

\[
 \boxed{
 \left|\bigcup_{x\in B_1}(x-\{q_0\})
       \setminus
       \bigcap_{x\in B_1}(x-\{q_0\})\right|
 \ge 2d-6.}
\tag{0.3}
\]

Thus a coordinate wall does not compress the obstruction to a bounded
collar.  If an obstruction survives, it reproduces the entire
`4^d/sqrt d`-scale core on the protected side of the wall.

## 1. Coinstantiating pinning with the stronger forbidden bank

Use the notation

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad
 |K|=m-1,\quad |E|=m,
\]

of the core-pinned reservoir, with `q_0 in K`.  For an owner `U`, put

\[
 h(U)=|U\cap K|.
\]

Define the one-unit-enlarged forbidden lower bank

\[
 \mathcal F_{<d+1}
 =\{L:L\subset U\text{ for some owner }U
              \text{ with }h(U)<d+1\}.
\tag{1.1}
\]

### Lemma 1.1 (pinned depth-wide avoidance)

For all sufficiently large `m`, the core-pinned complete upper-cone
reservoir can be selected so that every non-top protected lower colour
avoids `mathcal F_(<d+1)`.

#### Proof

The number of members of the new forbidden bank is at most

\[
 m\sum_{h=0}^{d}{m-1\choose h}{m\choose h}=2^{o(m)},
\tag{1.2}
\]

because `d=O(sqrt m)`.

A pinned low noninterval path has external trace size at most
`m-d-2`.  A lower facet of an owner with `h(U)<=d` has external trace
size at least `m-d-1`.  Therefore the explicit low paths already avoid
the bank.

For the high-tail paths, add (1.1) to the forbidden lower-resource list
in the existing greedy construction.  The stabilizer-of-`q_0` resource
denominators remain `2^(2m-o(m))`, whereas both (1.2) and the total
previously occupied resource bank are `2^(m+o(m))`.  The same union bound
is still `2^(-m+o(m))<1`.  Thus every high path can be chosen while
avoiding (1.1), without changing owner, lower-colour, upper-colour,
clipped-residence, or upper-cone coverage properties.  The deterministic
top bank is retained. \(\square\)

For an owner containing `q_0`, let

\[
 g_U^{(1)}
 =|\{x\subset U:|x|=m-1, q_0\in x, x\notin Z_P\}|
\tag{1.3}
\]

be its optional gap *inside* the wall.

### Lemma 1.2 (wall gap)

Every owner `U` containing `q_0` satisfies

\[
 \boxed{g_U^{(1)}\ge d-2.}
\tag{1.4}
\]

#### Proof

If `h(U)<d+1`, Lemma 1.1 leaves only deterministic top colours among the
protected facets of `U`.  At most one comes from deleting a `K`
coordinate with unchanged external trace, and at most two come from
deleting an `E` coordinate: adjoining one point to a cyclic interval has
at most two endpoint choices.  Thus at most three wall facets are
protected, and

\[
 g_U^{(1)}\ge(m-1)-3=m-4\ge d-2.
\]

Now suppose `h(U)>=d+1`, and put `e=|U cap E|=m-h(U)`.
The `e` facets obtained by deleting an external coordinate have distinct
external traces.  Among facets obtained by deleting a `K` coordinate,
the same-trace adjacency theorem permits at most two protected colours.
The facet obtained by deleting `q_0` is not protected at all, because
every protected lower colour contains `q_0`.  Hence at most `e+2` of the
`m-1` wall facets are protected, and

\[
 g_U^{(1)}\ge(m-1)-(e+2)=h(U)-3\ge d-2.
\]

This proves (1.4). \(\square\)

## 2. The off-wall positive owners cannot balance their shore

Let `B^-` be the inclusion-minimal positive optional maximizer and let

\[
 Q=\{U:a_U>0\}
\]

be its positive-capacity owner family.  The exact optional-core ledger
gives

\[
 \sum_Ua_U>2|B^-|,
 \qquad a_U\le2,
\]

so

\[
 |Q|>|B^-|.
\tag{2.1}
\]

The near-shadow localization also gives

\[
 |B^-|\le |Z_P\cup B^-|=O(m^2 2^m).
\tag{2.2}
\]

### Lemma 2.1 (off-wall imbalance)

For all sufficiently large `m`,

\[
 |Q_0|\le |B_0|.
\tag{2.3}
\]

If one of the two sides is nonempty, the inequality is strict.

#### Proof

An owner `U` not containing `q_0` contains no protected physical vertex.
Therefore

\[
 d_P(U)=0,\qquad z_U=0,\qquad g_U=m,qquad c_U=2.
\]

Positivity says

\[
 b_U(B^-)\ge g_U-c_U+1=m-1.
\]

Every facet of such an owner also avoids `q_0`, so every member of `Q_0`
has at least `m-1` facets in `B_0`.

If `|Q_0|>=|B_0|` and `Q_0` is nonempty, apply the sharp one-sided
partial-shadow theorem to `(B_0,Q_0)` with threshold `m-1`.  It gives

\[
 |B_0|\ge {2m-3\choose m-2}.
\tag{2.4}
\]

But (2.4) is `2^(2m-o(m))`, contradicting (2.2), which is
`2^(m+o(m))`.  If `B_0` is empty, the displayed degree condition forces
`Q_0` to be empty as well.  This proves the lemma. \(\square\)

Combining (2.1) and (2.3) gives

\[
 \boxed{|Q_1|>|B_1|.}
\tag{2.5}
\]

## 3. A full sharp-shadow core remains inside the wall

### Lemma 3.1 (wall owner degree)

Every `U in Q_1` contains at least `D=d-3` members of `B_1`.

#### Proof

Write `g_U=g_U^(1)+1`: the additional optional facet is the unique facet
`U-{q_0}` outside the wall.  Since `a_U>0` and `c_U<=2`,

\[
 b_U(B^-)\ge g_U-c_U+1\ge g_U-1=g_U^{(1)}.
\]

At most one counted member of `B^-` is the off-wall facet.  Therefore

\[
 |B_1\cap N(U)|\ge g_U^{(1)}-1\ge d-3=D
\]

by Lemma 1.2. \(\square\)

Strip `q_0` from `B_1` and `Q_1`.  They become families in two adjacent
Boolean ranks, (2.5) is strict side imbalance, and Lemma 3.1 is the
threshold-`D` hypothesis.  The sharp optional threshold-shadow theorem
therefore gives (0.2).

Apply the coordinate-span corollary to the stripped fixed-rank family.
Its strict `+1` lower bound gives free span at least `2D=2d-6`, proving
(0.3).

The same argument gives the following aperture-cover obstruction: if the
stripped `B_1` is covered by `t` Boolean intervals of free dimension at
most `D+C`, with fixed `C`, then

\[
 \boxed{t\ge2^{d-C+O(1)}.}
\tag{3.1}
\]

## 4. Exact scope

This theorem is a genuine localization, not an extension theorem.
It proves that the wall removes every balanced off-wall positive-owner
system, but it also proves that a surviving obstruction can concentrate
on the wall while retaining the full sharp-shadow size and coordinate
span.  Therefore neither one pinned coordinate nor a bounded collection
of deadline-sized apertures can close the co-small row by itself.

The remaining route must either:

1. prove that the actual occurrence-labelled damage inside the wall is
   covered by fewer than the lower bound (3.1);
2. construct a balanced residual factor inside the wall; or
3. use additional correlated walls whose top section cannot host the
   reproduced core.

## 5. Dependencies

- `MATH_THEOREM_CORE_PINNED_THREE_RING_RESERVOIR_AND_COORDINATE_WALL_PULL_COMPLETION_20260804.md`
- `MATH_THEOREM_CO_SMALL_WIDE_GAP_BOOTSTRAP_CORE_AND_COMPRESSION_BARRIER_20260804.md`
- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`
- `MATH_COROLLARY_OPTIONAL_CORE_COORDINATE_SPAN_AND_LOCAL_CUBE_COVER_20260804.md`
- `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`

