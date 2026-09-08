# The tensored four-row Tamari trade has a finite nested-rail chord current

## Status

The all-dimensional four-row trade in
`MATH_THEOREM_TENSORED_FOUR_ROW_TAMARI_WREATH_TRANSPORT_20260806.md`
preserves the two central shores and both immediate palettes.  This note
computes its remaining contiguous-path current.  The calculation is purely
algebraic.

Every chord whose two endpoints lie in the common tensor tail is fixed
pointwise.  Every chord crossing from the eight-coordinate packet into the
tail is one of three fixed finite currents adjoined to one of two nested
tail rails.  Thus tensoring does not create `Theta(r)` independent
all-width defects: it repeats six finite currents along nested rails.

This is a theorem about unions and intersections of contiguous blocks of
the rank-`r` complement geodesics.  It does not by itself prove that the
trade is plantable in one exact factor, that the six currents cancel in a
global packet, or that the eventual source-word compiler is feasible.

## 1. Endpoint reduction on a complement geodesic

Let

\[
             P=(P_0,P_1,\ldots,P_r)                  \tag{1.1}
\]

be a shortest Johnson path from an `r`-set to its complement in a
`2r`-set.  No deleted coordinate is reinserted and no inserted coordinate
is subsequently deleted.

### Lemma 1.1 (contiguous blocks are endpoint chords)

For every `0<=i<=j<=r`,

\[
 \bigcup_{t=i}^jP_t=P_i\cup P_j,
 \qquad
 \bigcap_{t=i}^jP_t=P_i\cap P_j.                    \tag{1.2}
\]

#### Proof

A coordinate present at an intermediate time but absent at time `i` was
inserted by time `j`, and hence belongs to `P_j`.  A coordinate present at
time `i` but removed before time `j` already belongs to `P_i`.  This proves
the union identity.  A coordinate belongs to both endpoints precisely
when it is neither removed nor inserted strictly between them, and then it
belongs to every intermediate state.  This proves the intersection
identity. \(\square\)

Consequently the complete contiguous union/intersection ledger of a
shortest wreath row is its chord ledger.

## 2. Tensor notation

Use the port-restored base trade

\[
             {\cal P}^-\longleftrightarrow {\cal P}^* \tag{2.1}
\]

from `MATH_ATTACK_E_FOUR_ROW_TAMARI_ASSOCIATOR_20260726.md`.  Its four
named rows are `A,L,C,D`, each with states `P_0,...,P_4`; the endpoints
`P_0,P_4` agree row by row in the two phases.

On a disjoint set `E` of size `2(r-4)`, fix a complement geodesic

\[
             S_0,S_1,\ldots,S_{r-4}=E-S_0.          \tag{2.2}
\]

The extended row is

\[
 P_0+S_0,\ldots,P_4+S_0,
 P_4+S_1,\ldots,P_4+S_{r-4}.                         \tag{2.3}
\]

For a signed multiset `Z` on subsets of `[8]` and a fixed set `R` disjoint
from `[8]`, write `Z+R` for the signed multiset obtained by adjoining `R`
to every term.

For `i=0,1,2,3`, define the finite endpoint currents

\[
\begin{aligned}
 U_i&=\sum_{R\in\{A,L,C,D\}}
   \bigl([P^*_{R,i}\cup P_{R,4}]-[P^-_{R,i}\cup P_{R,4}]\bigr),\\
 I_i&=\sum_{R\in\{A,L,C,D\}}
   \bigl([P^*_{R,i}\cap P_{R,4}]-[P^-_{R,i}\cap P_{R,4}]\bigr).
                                                               \tag{2.4}
\end{aligned}
\]

The common endpoints give `U_0=I_0=0`.

## 3. Exact finite currents

Literal inspection of the two four-row tables gives

\[
\begin{array}{c|l|l}
i&U_i&I_i\\ \hline
1&[1234578]-[1235678]&[6]-[4]\\
2&[123478]+[345678]-[123468]-[145678]
  &2[46]-[47]-[48]\\
3&[13478]-[34678]&[478]-[347].
\end{array}                                                \tag{3.1}
\]

Here, as in the base note, a digit string denotes the corresponding
subset of `[8]`.

For completeness, the only nonzero aggregate base chord currents after
grouping by chord length are at lengths two and three.  They are

\[
\begin{aligned}
 B^\cup_2={}&[124568]+[124678]+[345678]
              -[125678]-[123468]-[145678],\\
 B^\cap_2={}&[37]+[46]-[47]-[48],\\
 B^\cup_3={}&[1245678]+[1234578]
              -[1234567]-[1235678],\\
 B^\cap_3={}&[1]-[4].                                  \tag{3.2}
\end{aligned}
\]

Lengths zero and one vanish by the state and adjacent-palette identities
of the base packet, and length four vanishes because the row endpoints are
complementary and fixed.

### Lemma 3.1

Equations (3.1)--(3.2) are the exact base currents.

#### Proof

For (3.1), take in each displayed row the union and intersection of state
`i` with its fixed terminal state.  Cancelling common terms gives the
table.  For (3.2), apply the same operation to all pairs `(P_i,P_(i+2))`
and `(P_i,P_(i+3))` and cancel the common terms.  Lemma 1.1 identifies
these endpoint calculations with the corresponding contiguous-block
currents. \(\square\)

## 4. Complete tensor factorization

Put

\[
              R_t^+=S_0\cup S_t,
 \qquad       R_t^-=S_0\cap S_t.                    \tag{4.1}
\]

Because `S_0,...,S_(r-4)` is a complement geodesic, the `R_t^+` form an
increasing chain and the `R_t^-` form a decreasing chain.

### Theorem 4.1 (six nested cross-tail rails)

For every `1<=t<=r-4` and every base index `i=0,1,2,3`, the signed current of
the four extended chords from base position `i` to tail position `4+t`
is

\[
              U_i+R_t^+                              \tag{4.2}
\]

for unions and

\[
              I_i+R_t^-                              \tag{4.3}
\]

for intersections.

Every chord lying wholly in the common tail has zero current.  Every chord
lying wholly in the five-state base segment is the corresponding base
current adjoined to `S_0`.  Hence (3.1)--(3.2), together with (4.2)--(4.3),
is the complete contiguous union/intersection current of the tensored
trade.

#### Proof

For a crossing chord in row `R`, disjointness of the coordinate banks and
the fixed terminal state give

\[
\begin{aligned}
 (P_{R,i}+S_0)\cup(P_{R,4}+S_t)
   &=(P_{R,i}\cup P_{R,4})+(S_0\cup S_t),\\
 (P_{R,i}+S_0)\cap(P_{R,4}+S_t)
   &=(P_{R,i}\cap P_{R,4})+(S_0\cap S_t).
                                                               \tag{4.4}
\end{aligned}
\]

Subtracting the negative phase from the restored phase and summing over
the four rows proves (4.2)--(4.3).  If both endpoints lie in the tail,
both base projections equal the row's fixed `P_4`, so the chord is
literally unchanged.  If both lie in the base segment, both carry the
common `S_0`, and Lemma 1.1 reduces the calculation to (3.2) and the
already-zero lengths. \(\square\)

### Corollary 4.2 (dimension-independent all-width interface)

The number of independent finite current types created by tensoring is
bounded independently of `r`: three union endpoint currents, three
intersection endpoint currents, and the four finite internal currents in
(3.2).  The apparent linear number of tail defects is only the transport
of these six endpoint currents along two nested rails.

In particular, for a collection of trades using the same tail rails, it
is sufficient for complete chord-ledger cancellation that the signed sums
of each `U_i`, each `I_i`, and each of the four currents in (3.2) vanish.
This is a finite system of conditions independent of the ambient
dimension.

### Theorem 4.3 (constant symmetric-orbit cancellation)

Take one coordinate-conjugate copy of the tensored trade for every
permutation in `Sym([8])`, using the same tail geodesic (2.2) in every
copy.  Then the aggregate contiguous union/intersection current of all
`8!` trades is zero at every chord length.

More generally, the same conclusion holds for any finite permutation
group on `[8]` which is transitive on `s`-subsets for every rank `s`
appearing in (3.1)--(3.2).

#### Proof

Every one of the ten signed currents in (3.1)--(3.2) is supported on a
single subset rank and has total coefficient zero.  If a group is
transitive on that rank, every subset occurs equally often in the orbit of
each positive or negative term.  The orbit sum of the signed current is
therefore zero.

The full symmetric group is transitive on every subset rank.  It kills
the six endpoint currents and the four internal currents separately.
All copies use the same tail rails, so Theorem 4.1 then kills every lifted
cross-tail current as well as every wholly-base current.  Wholly-tail
currents were already pointwise zero. \(\square\)

Theorem 4.3 is a prospective algebraic packet of constant size independent
of `r`.  It does not assert that its `8!` negative packets are disjoint or
simultaneously present in one factor.  Its value is that no new
dimension-growing current invariant can obstruct a bounded associator
macro: only host planting and dynamic reachability remain.

### Corollary 4.4 (fifty-six conjugates suffice)

The `8!` copies in Theorem 4.3 may be replaced by `56` copies.

#### Proof

Identify `[8]` with the field `F_8` and take the affine group

\[
             G=\{x\longmapsto ax+b:a\in\mathbb F_8^*,\ b\in\mathbb F_8\},
\qquad |G|=8\cdot7=56.
\]

It is transitive on points and pairs.  It is also transitive on unordered
triples.  Indeed, `|G|=binom(8,3)`, and the stabilizer of a triple is
trivial.  A nonidentity translation has only two-element orbits and no
fixed point, so it cannot preserve a three-set.  Every affine map with
`a!=1` is conjugate to multiplication by `a`; since `F_8^*` has prime
order seven, it has one fixed point and one seven-cycle, and again cannot
preserve a three-set.

Thus `G` is transitive on subsets of ranks one, two, and three, and by
complementation on ranks seven, six, and five.  These are exactly the ranks
appearing in (3.1)--(3.2).  Apply the general form of Theorem 4.3. \(\square\)

This improves the prospective constant only.  It does not change the
simultaneous-host caveat.

## 5. Exact remaining gate

The four-row tensor therefore solves both the *shape* of the all-width
damage and its prospective bounded cancellation.  A complete transport
theorem must now realize a finite circuit of relabelled associators such
that

1. the required negative packets occur successively or disjointly in one
   literal factor;
2. their tail rails are aligned as in Theorem 4.3;
3. the net dynamic action exposes the desired inverse-pair slots rather
   than cancelling trivially; and
4. protected upper witnesses and lower compiler tickets survive the
   circuit.

The algebraic current problem is finite and has the symmetric-orbit
solution above.  The remaining conditions are the dynamic
slot-transitivity/host-extension problem and are not implied by prospective
coordinate symmetry.
