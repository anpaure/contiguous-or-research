# Audit of the core-change zipper: sharp hypotheses and counterexamples

Date: 2026-08-02  
Status: proof audit of
`MATH_THEOREM_FACET_CORE_CHANGE_ZIPPER_AND_TWO_SEAM_FUSION_20260802.md`.
The local zipper is accepted under its stated hypotheses.  The unrestricted
claim "nearby cores can simply be spliced" is false without the repeated
tag, tag/core separation, and `P/H` phase conditions.  Global deeper-upper
and compiler conclusions remain out of scope.

## 1. Rank identity

For `h=q-1`, the input core has size

\[
 |X|=r-h-1,qquad |C|=r-h-2.
\]

A pure owner has one core point, `beta`, and `h` tags.  A mixed owner has
two core points, `beta`, and must therefore have exactly `h-1` distinct
tags.  The repeated boundary tag is not optional: it is the unique unit of
rank compensation for the core change.

The formulas (1.4), (2.2), and (2.3) of the theorem independently give
ranks `r`, `r-1`, and `r+1`.  Their consecutive symmetric differences are
exactly the three cases listed in (1.7).

## 2. Counterexample: no repeated boundary tag

If the last `X` tag and first `Y` tag are different and all `h` tags in a
mixed window are distinct, that window has

\[
 |C|+2+1+h=(r-h-2)+h+3=r+1.
\]

Thus an ordinary cross-edge between adjacent cores raises the owner rank.
The equality of the two boundary tags is necessary for this one-unit
core-change zipper.

## 3. Counterexample: a second active collision

The repeated seam tag must be the only collision visible in each mixed
window.  For example take `h=4` and use halos

\[
 \ell_0,\ell_1,u,z
 \quad\big|\quad
 z,u,\rho_2,\rho_3.
\]

The mixed window containing the last two left sources and first two right
sources sees tags `u,z,z,u`, hence only two distinct tags rather than
`h-1=3`.  Its rank is `r-1`.  This is exactly the failure excluded by
(1.3).  Merely saying that each side has no internal tag repetition is not
enough.

The strong pairwise-disjoint halo condition is sufficient but not
necessary.  A cross-equality `ell_i=rho_j` is harmless when the two
occurrences never coexist in a mixed window; the exact condition is
`j>=i`.  Formula (1.3) is the invariant statement.

## 4. Counterexample: a tag is a core point

If an old boundary tag equals `b`, the first purported exchange

\[
 O_0\longrightarrow O_1=O_0-\{\ell_0\}+\{b\}
\]

does not insert a new point.  The owner rank falls and the transition is
not a Johnson edge.  The analogous issue occurs when a new tag equals `a`
at the final transition, or when any tag lies in `C union {beta}`.
Therefore tag/core separation is structural, not cosmetic.

## 5. Counterexample: opposite cut phase

In two alternating even cycles, if the two deleted edges have opposite
ordered `P/H` phases, the two cross seams are `P-P` and `H-H`.  The fused
word is not alternating.  At the `P-P` seam the union of the two boundary
sources omits `beta`, so its rank is one below the prescribed length-two
marked rank.  When `h=2`, the mixed owner itself omits `beta` and has rank
`r-1`.

For `h>=3`, every owner may still happen to contain a nearby `H`, but the
lower age signature is already wrong.  Thus same-phase cuts are necessary
to remain in the unbuffered alternating primitive class, even where owner
rank alone does not detect the error.

## 6. Why two shared tags and `L>=h+2` are used

One 2-break has two new seams.  Cross-positioning two shared tags,

\[
 A_{\rm tail}=B_{\rm head}=z,
 \qquad B_{\rm tail}=A_{\rm head}=w,
\]

pays the rank compensation at both seams.  The inequality `L>=h+2`
ensures that `w` is absent from the `z` halo and `z` is absent from the `w`
halo.  Consequently the two mixed decks are separated by the literal
witnesses `z` and `w`.

If `L<=h+1`, the opposite seam tag can enter the halo.  Then a mixed window
may see two duplicated tags, or the two seam palettes may lose their
`z/w` separator.  No two-seam simplicity claim is valid in that range
without a separate direct audit.  The corrected reservoir lengths are
exactly `h+2` and `h+3`, so this issue does not arise there.

## 7. Palette scope

The theorem preserves **simplicity**, not palette identity.  The endpoint
lower colours reuse the unique proper `(h-1)`-interval colours exposed at
the deleted cuts.  The interior lower colours and every new upper colour
contain both `a,b` and are generally new literal targets.  Similarly, the
`h-1` mixed owners at each seam replace old same-core crossing owners.

Therefore it is invalid to infer any of the following without an additional
global ledger:

* that all middle owners are still covered exactly once;
* that every immediate upper target is still covered;
* that an old all-width upper witness survived;
* that the compiler matching transports through the zipper.

The theorem is directly usable in a reservoir whose socket halos are
reserved before target assignment, or in an ambient factor where the
changed named resources are charged explicitly.  It cannot be applied
post hoc to an exact carrier merely because its local owner/q1 rows remain
simple.

## 8. Verdict

The proposed local rank calculation is correct after replacing the phrase
"q-2 other tags" by the exact statement:

\[
 \boxed{\text{each mixed }h\text{-window has exactly }h-1=q-2
        \text{ distinct tags in total}.}
\]

Under the theorem's zipper and parity hypotheses, the owner row is a
Johnson geodesic, both immediate palettes are injective, and a same-phase
two-seam 2-break fuses the components with residence floor `h`.  The main
unproved all-dimensional step is now socket supply: the extracted cycle
bank must contain enough adjacent-core pairs with two cross-positioned
shared tags and compatible cut phases.  Deeper upper coverage and the
compiler remain independent gates.

## 9. Regeneration obstruction for the shortest cycles

The two-seam theorem is not, by itself, an iteration theorem.  After one
fusion an original cyclic core block becomes a linear block of length `L`.
To use a second pure-core cut inside that block, the new cut needs `h`
sources of that core immediately before it and `h` immediately after it.
Those two halos are disjoint on the fused linear chronology, so necessarily

\[
                         L\ge2h.                          \tag{9.1}
\]

The corrected shortest cycles have

\[
 L=h+2\quad(h\text{ even}),\qquad
 L=h+3\quad(h\text{ odd}).                              \tag{9.2}
\]

For every `h>=4`, (9.2) is strictly smaller than `2h`.  Hence a shortest
cycle whose only socket was used in one fusion does not automatically
export another pure-core zipper socket.  Repeatedly applying Theorem 3.1
can at most pair components unless one proves an overlapping mixed-core
zipper, plants longer socket-rich cycles, or embeds the pair into an
external host with a fresh pure halo.

Taking `L>=2h` removes this elementary halo-length obstruction and permits
two cut edges at cyclic distance at least `h`, but it still does not prove
iterative fusion: every later zipper deck must avoid all earlier mixed
decks, and the successive adjacent-core unions must be controlled.  Thus a
global connector theorem needs both socket regeneration and a named
resource-freshness invariant.
