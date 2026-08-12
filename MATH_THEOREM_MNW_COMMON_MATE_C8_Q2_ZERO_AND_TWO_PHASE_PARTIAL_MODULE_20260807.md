# A common untouched mate makes the MNW phase-creator `C_8` exactly q2-neutral

**Date:** 2026-08-07  
**Method:** literal turn telescoping and coloured partial-matching audit; no
computation or search  
**Status:** unconditional local algebra.  It removes the unit q2 casualty
of the canonical phase creator under one explicit common-mate condition.
The natural candidate is the lifted marked coordinate `z`.  Extension of
the resulting partial ordered two-SDR with the required connector/socket
interface remains open.

## 1. General detour cycle

Let `K` be a rank-four set, let `a,b,x` be distinct labels outside `K`,
and choose `s in K`.  Put

\[
\begin{aligned}
 X&=K+a,& X_x&=K+x,\\
 R&=K+a+b,& Q&=K+a+x,& M&=K+b+x,\\
 Y_1&=K-s+a+b,&Y_2&=K-s+b+x,\\
 S&=K-s+a+b+x.
\end{aligned}                                      \tag{1.1}
\]

The Boolean incidence graph contains the simple cycle

\[
 \boxed{
 C_s=X-R-Y_1-S-Y_2-M-X_x-Q-X.}                    \tag{1.2}
\]

Use the alternating orientation with old edges

\[
 O_s=\{XR,;Y_1S,;Y_2M,;X_xQ\}                  \tag{1.3}
\]

and new edges the complementary four edges of (1.2).

For the concrete MNW boundary take

\[
 K=0010001101,quad (a,b,x)=(1,2,9),quad s=3.     \tag{1.4}
\]

Then (1.2) is exactly the unique leaf-boundary detour creator already
proved alternating in the gamma--alpha state.

## 2. Common-mate telescope

Choose one further label

\[
                         c\notin K\cup\{a,b,x\}.    \tag{2.1}
\]

At the four lower owners of (1.2), retain the four mate incidences

\[
 X(X+c),\quad
 Y_1(Y_1+c),\quad
 Y_2(Y_2+c),\quad
 X_x(X_x+c).                                      \tag{2.2}
\]

These incidences form a matching: their lower endpoints are distinct and
their upper endpoints are distinct.

### Theorem 2.1 (exact q2-zero common-mate switch)

If the four incidences (2.2) are the untouched factor mates at the four
owners while `C_s` is switched from (1.3) to its complementary edge set,
then the complete signed q2 turn current is zero.

### Proof

At `X`, the old and new turns are

\[
 K+a+b+c
   \longmapsto
 K+a+x+c.                                         \tag{2.3}
\]

At `Y_1`, they are

\[
 K-s+a+b+x+c
   \longmapsto
 K+a+b+c.                                         \tag{2.4}
\]

At `Y_2`, they are

\[
 K+b+x+c
   \longmapsto
 K-s+a+b+x+c.                                     \tag{2.5}
\]

At `X_x`, they are

\[
 K+a+x+c
   \longmapsto
 K+b+x+c.                                         \tag{2.6}
\]

Every value appearing positively in (2.3)--(2.6) appears once
negatively in the next row.  Hence their signed sum is zero. \(\square\)

This is equality of occurrence multiplicities, not merely support safety.
It is independent of the old multiplicities of the four targets.

## 3. The marked-coordinate realization

In the ten-prefix-bit MNW module there is one lifted coordinate `z`
outside the prefix support.  Setting

\[
                         c=z                         \tag{3.1}
\]

turns (2.2) into the four vertical incidences

\[
                         O\subset O+z                \tag{3.2}
\]

at the affected owners.  The creator never toggles these incidences, so
they are literal protected mates if the ordered two-SDR host selects them.

Theorem 2.1 then proves that the creator is q2-neutral even though the
same `C_8` with the canonical z-free mates has current

\[
 [1010101111]-[1100101111].                         \tag{3.3}
\]

Thus the unit `J` casualty is a mate-choice defect, not an invariant of
the incidence `C_8`.

The assertion here is conditional on selecting all four vertical mates.
It does not assert that every one of them belongs to the previously fixed
closure matching or that the higher connector interface leaves them free.

## 3.1 A smaller endpoint-price realization inside the ten-bit half

For the concrete creator (1.4), the fresh prefix label `c=5` gives the
four mates

```text
1010101101  1100101101  0100101111  0010101111.
```

The first is the already-selected untouched mate at `X`.  The second is
the already-selected untouched mate at `Y_1`: its current selected
additions are exactly `5,9`.  Thus no phase change is needed at those two
internal owners.

The owners `Y_2=0100001111` and `X_x=0010001111` are respectively the
reverse and forward z-free endpoints used in the leaf construction.  The
last two incidences above add a second z-free edge at precisely those two
owners.  Therefore choosing `c=5` has the exact physical price

\[
 \boxed{\text{promote two old z-free endpoints to internal owners and
 export two replacement endpoints elsewhere}.}                 \tag{3.4}
\]

It does not require four new vertical closure edges.  A connector-faithful
module may therefore use `c=5` provided its socket permutation relocates
the two displaced vertical closures.  This two-endpoint relocation is an
explicit remaining topology row; q2 remains identically zero by Theorem
2.1.

## 4. Coloured partial ordered-SDR module

Give the fused contextual source cycle `C_src` phase zero and the detour
creator `C_s` phase one.  At their only common colour `M`, their old edges
are distinct:

\[
                         X_2M\in O^0,qquad
                         Y_2M\in O^1.                \tag{4.1}
\]

Place the four common mates (2.2) in phase zero.  None meets an old
phase-zero source edge in the concrete ten-bit pattern, and their upper
colours are distinct from the four source-cycle colours.  Therefore the
declared phase-zero and phase-one old banks are partial matchings.

After switching, the phase-zero source new bank and phase-one creator new
bank are again partial matchings; at `M` they use the two distinct edges

\[
                         (01O_2)M,qquad X_xM.         \tag{4.2}

### Corollary 4.1 (q2-transparent local two-phase module)

There is no local degree, edge-colour, or q2-current obstruction to
placing the source `C_8` in phase zero and the unique detour creator in
phase one while retaining the four common `z` mates in phase zero.

If one global ordered two-SDR extends these partial banks, avoids their
new edges initially, and realizes the required socket order, then the
simultaneous two-phase switch:

1. preserves degree two;
2. performs the source and boundary phase changes;
3. leaves every common mate selected; and
4. has zero q2 current from the phase creator.

The source B8 current is of course still present and must be completed by
the remaining B8 faces; the claim is only that the phase creator adds no
extra q2 debt.

## 5. Revised finite gate

The earlier terminal `J` hole is no longer part of the minimal local
algebra.  The finite ten-bit problem has narrowed to one coloured host:

> Extend the phase-zero source bank, the phase-one detour bank, and the
> four common mates (either the vertical `z` bank or the `c=5` bank with
> its two endpoint relocations) to an ordered two-SDR which also contains
> the remaining annulus phases and inherited connector/socket marks.

The remaining risk is now genuinely global.  The four vertical mates may
conflict with the standard marked closure or higher MNW attachments, and
the partial successor permutation still needs one common extension.  No
claim about those rows follows from q2 telescoping alone.
