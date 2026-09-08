# The positive B8 macro passes H0 and stops at one H1 owner

**Date:** 2026-08-07  
**Method:** exact touching-step phases and q2 turn replay; no computation or
search  
**Status:** unconditional in the gamma-alpha plus closed endpoint-packet
state.  Direct destination switching removes the need for an annulus at H0,
but H1 has one explicit double-unselected owner.  A unique C8 repairs that
phase and creates one unit q2 casualty.

## 1. H0 is literally alternating

Prefix the four-hex B8 relay by positive context `10`.  Its first hex H0
has lower owners

```text
1010001101  1010001011  1011001001.
```

Mirror gamma had prepared the third owner exactly.  The leaf face changes
the first owner from the mirror-gamma facet `1110001101` to the required
positive facet `1010001111`, retaining its mate.  The middle owner is in the
required canonical phase.  The companion hex `H_*` starts with `11` on all
its owners and colours and is disjoint.

Therefore positive H0 is alternating after the closed endpoint packet.
Its exact ownerwise turn current is

\[
\begin{aligned}
1010101111&\longmapsto1011101101,\\
1111001011&\longmapsto1110001111,\\
1011011101&\longmapsto1011011011.
\end{aligned}                                       \tag{1.1}
\]

In particular H0 directly recreates the first relay's missing target
`1011101101`.

## 2. H1 has one exact phase defect

After H0, the positive H1 owners are

```text
1010001011  1010000111  1011000011.
```

The first owner has the H0-propagated phase required by H1.  At the second,
the selected pair is `{2,4}`; its required cycle edge is addition four and
is selected, while the opposite cycle edge is unselected.

At the third owner

\[
                         O=1011000011,               \tag{2.1}
\]

the exact touching-step pair is `{2,6}`.  H1 needs addition seven selected
and addition eight unselected.  Both H1 cycle incidences are therefore
unselected.  None of gamma-alpha, H0, the leaf face, or `H_*` touches this
owner.  Thus positive H1 is not alternating.

This disproves the shortcut "toggle the positive four-hex macro directly."

## 3. Unique C8 phase repair

Retain addition six at `O` and replace selected addition two by required
addition seven.  Put

\[
 S=O+2=1111000011,\qquad D=O+7=1011001011.          \tag{3.1}
\]

Every simple C8 through `OS,OD` has the Johnson-detour normal form with

\[
 s\in O=\{1,3,4,9,10\},\qquad x\in\{5,6,8\}.       \tag{3.2}
\]

The three alternating conditions leave exactly `(s,x)=(3,6)`.  Its vertex
row is

```text
1011000011 1011001011 1001001011 1001011011
1001010011 1101010011 1101000011 1111000011
```

and its status word is `01010101`.  Toggling it installs `OD`, so H1 becomes
literally alternating.

## 4. The C8 is a q2 hole relay

At the repaired owner `O`, the turn changes

\[
                         1111010011
                 \longmapsto1011011011.             \tag{4.1}
\]

The negative target

\[
                         L_0=1111010011              \tag{4.2}
\]

has the unique inverse witness `(2,6)`, at `O` itself.  Hence the C8 removes
its sole canonical occurrence.  The later H1 switch advances the new turn
again and does not restore `L_0` at this owner.

Thus the direct destination route has been reduced to a new exact relay:
H0 is solved, H1 phase is solved by one unique C8, and the remaining local
q2 target is `1111010011`.

## 5. Scope

All statements tensor under Dyck suffixing.  No claim is made yet about a
companion restoring `L_0`, the H2/H3 phases, or the component action of the
combined packet.

