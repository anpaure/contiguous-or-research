# The full `01 -> 10` annulus is an endpoint coboundary at every width

**Date:** 2026-08-07  
**Method:** signed incidence-chain telescoping, labelled chronology
conjugacy, and suffix projection; no computation or search  
**Status:** unconditional at the incidence-chain level.  The q2 and
all-width statements are exact under the stated turn/chronology-faithful
host hypotheses.  They prove that a complete annulus has no accumulating
interior current.  They also prove a sharp obstruction: neither wider-deck
damage nor a q2 hole can cancel between distinct Dyck suffix fibres.

## 1. General annulus coboundary

Let `Z` be a signed incidence circulation on base coordinates, and let

\[
 S_0,S_1,\ldots,S_t                                  \tag{1.1}
\]

be a Johnson path on disjoint context coordinates.  For the context edge
`S_i -> S_{i+1}`, let `A_i(Z)` be the signed sum of its transport
hexagons, with the convention of the context-transport theorem.  Then

\[
 A_i(Z)=Z_{S_{i+1}}-Z_{S_i}.                         \tag{1.2}
\]

Therefore the entire annulus satisfies the exact chain identity

\[
 \boxed{A_{0,t}(Z):=\sum_{i=0}^{t-1}A_i(Z)
                   =Z_{S_t}-Z_{S_0}.}               \tag{1.3}
\]

Every auxiliary owner rail and colour rail is internal to the left side
and cancels.  There is no interior incidence residue, regardless of the
length of the context path.

If one first toggles the source-boundary packet `Z_{S_0}` and then sweeps
the annulus, the complete current is simply

\[
 Z_{S_0}+A_{0,t}(Z)=Z_{S_t}.                         \tag{1.4}
\]

Thus every debt seen during a partial sweep is an intermediate boundary
term.  Only the destination copy can survive after the complete shell.

## 2. Exact q2 current of the B8 shell

For the four-hex B8 circulation, its base q2 current is

\[
\begin{aligned}
 \delta_2^B={}&+[11101101]+[11010111]\\
              &-[11100111]-[10111110].              \tag{2.1}
\end{aligned}
\]

Assume the annulus boundaries are turn-faithful: at each affected owner,
the untouched selected mate is the corresponding contextual copy of the
base mate.  Then the q2 functor commutes with (1.3).  For the one-step
context move `01 -> 10`, the shell current is

\[
 \boxed{\partial_2A_{01,10}(Z_B)
       =\iota_{10}\delta_2^B-\iota_{01}\delta_2^B,} \tag{2.2}
\]

namely

```text
+1011101101 +1011010111 +0111100111 +0110111110
-1011100111 -1010111110 -0111101101 -0111010111.
```

Here `iota_s` prefixes the disjoint two-bit context `s`.  Toggling the
natural `01` B8 packet first contributes `iota_01 delta_2^B`; adding (2.2)
leaves exactly

\[
 \boxed{
 +[1011101101]+[1011010111]
 -[1011100111]-[1010111110],}                       \tag{2.3}
\]

the desired positive-context B8 current.

Equation (2.2), rather than the currents of individual repair faces, is
the complete q2 ledger of the annulus.  In particular, any named unit
holes created by an initial segment must either cancel inside the
remaining shell or appear among the four terminal terms (2.3).  A partial
positive route cannot decide closure by pricing its local faces in
isolation.

## 3. Suffix fibres form a direct sum, not a telescope

Append a Dyck suffix `v` and its fixed up-set `U(v)` to every owner,
colour, and target.  Denote the resulting injection by `iota_{s,v}`.
For distinct Dyck words `v != w`, restriction to the suffix coordinates
distinguishes `U(v)` from `U(w)`.  Hence

\[
 \operatorname{im}\iota_{s,v}cap
 \operatorname{im}\iota_{s',w}=\varnothing          \tag{3.1}
\]

for every choice of prefix contexts `s,s'`.

Consequently the complete suffix-bank shell is the block-diagonal sum

\[
 \boxed{
 \partial_2A^{\rm bank}_{01,10}
 =\bigoplus_{v\in\mathcal D}
  (\iota_{10,v}\delta_2^B-
   \iota_{01,v}\delta_2^B).}                        \tag{3.2}
\]

There is no cancellation between different suffix states.  Terminal q2
support must therefore be certified fibre by fibre (or by a literal
provider theorem that tensors fibre by fibre).  Averaging over suffixes or
summing the Catalan bank cannot hide one bad base target.

## 4. The all-width endpoint-coboundary theorem

Let `F` be the selected path factor before a base switch and `F^Z` the
factor after it.  For width `q >= 2`, let

\[
 \delta_q^Z=\operatorname{Deck}_q(F^Z)-
             \operatorname{Deck}_q(F)               \tag{4.1}
\]

be the signed multiset current of contiguous owner-window OR values.

Call an annulus **chronology-faithful** when:

1. all interior rails return to their initial incidences;
2. the external half-edges at the two boundaries are identified in the
   same order; and
3. after that identification, the destination changed paths are the
   context-labelled copies of the base changed paths.

### Theorem 4.1

For a chronology-faithful annulus,

\[
 \boxed{
 \partial_qA_{S_0,S_t}(Z)
   =\iota_{S_t}\delta_q^Z-
    \iota_{S_0}\delta_q^Z
 \qquad(q\ge2).}                                    \tag{4.2}
\]

After toggling the source packet first, the complete carried packet has

\[
 \boxed{\partial_q(\text{source packet+annulus})
       =\iota_{S_t}\delta_q^Z.}                     \tag{4.3}
\]

#### Proof

Chronology faithfulness gives a position-preserving bijection between
every changed source path and its destination path.  A window union in a
common context is that context union the corresponding base window union.
Therefore every lost and gained q-window is carried by `iota_S`, with its
multiplicity and sign unchanged.  Subtract the source and destination
currents to obtain (4.2); adding the source current gives (4.3).  \(\square\)

### Corollary 4.2 (sharp wider-deck reduction)

Because the `01` and `10` target images are disjoint,

\[
 \partial_qA_{01,10}(Z)=0
 \quad\Longleftrightarrow\quad
 \delta_q^Z=0.                                      \tag{4.4}

Thus an annulus does not manufacture q3 or wider transparency.  It merely
transports the base current.  For B8, the all-dimensional q3+ question is
reduced exactly to the finite eight-coordinate base audit:

> Does the four-hex B8 macro have a support-safe `delta_q^B` for every
> relevant base width q?

If yes, every chronology-faithful suffix annulus inherits that result.  If
one base negative is a last provider, the same casualty occurs separately
in every suffix fibre and no cross-fibre telescoping can repair it.

## 5. Exact topology statement

Cut every changed base path at the incidences used by `Z`, and write
`pi_Z` for the induced pairing/permutation of the exposed half-edges.
Let `tau` be the boundary identification supplied by the annulus rails.

### Theorem 5.1

If the annulus is chronology-faithful, the destination switch induces

\[
                         \tau\pi_Z\tau^{-1}.          \tag{5.1}
\]

Therefore source and destination switches have the same cycle type and
the same component-count change.  The shell taking the already-switched
source factor to the switched destination factor is component-count
neutral.  The full carried packet inherits the component action of the
base packet.

For B8, the base four-hex macro joins six lifted wreath cycles into one.
Hence a topology-faithful carried B8 packet has component change

\[
                         -5                         \tag{5.2}
\]

per suffix fibre, while the annulus shell itself has net change zero.
Over a suffix bank this is `-5 |D|`.

#### Proof

The rails give the bijection `tau` between source and destination sockets.
Condition 2 in chronology faithfulness preserves their cyclic order, and
Condition 3 applies the same reconnection rule.  Relabelling the source
reconnection by `tau` gives (5.1).  Conjugate permutations have the same
cycle type.  \(\square\)

Without the ordered socket condition, incidence identity (1.3) alone does
not determine topology: different external pairings of the same exposed
half-edges can join two components or split one component while leaving
the local annulus chain unchanged.

## 6. What is proved and what remains

Proved unconditionally:

* the whole annulus incidence current is a boundary coboundary;
* all interior rail currents telescope exactly;
* suffix fibres are disjoint direct summands, not cancellation partners.

Proved under explicit, static host conditions:

* turn faithfulness gives the exact eight-term q2 shell current (2.2);
* chronology faithfulness gives the all-width law (4.2);
* ordered socket faithfulness makes the shell topology-neutral and carries
  the base `-5` component action.

Not proved by this theorem:

1. that the required rail phases and ordered sockets occur in one MNW
   hypertree;
2. that the finite B8 base macro is q3+-support-safe; or
3. that the two negative destination terms in (2.3) retain literal
   providers in the rethreaded positive boundary.

The decisive gain is that no separate all-dimensional audit of the many
transport faces is needed.  The remaining wider-width problem is finite
and base-local; the remaining infinite problem is the static planting of
one turn-, chronology-, and socket-faithful annulus in every disjoint
suffix fibre.
