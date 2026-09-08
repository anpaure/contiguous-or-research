# `k=17`: full-static nine-attachment transition-cycle audit

**Date:** 2026-08-01  
**Lane:** A / residence-first compressed GKS chronology  
**Status:** exact obstruction for the frozen full-static flag certificate;
the abstract state-cycle implication is valid, but this certificate has no
such cycle

## 1. Verdict

The proposed compression is algebraically sound:

1. give each rank-eight root `Q_p` its nine incidence states
   `(p,alpha)`, where `alpha` is outside `Q_p`;
2. select one state per root and one state per rank-nine owner orbit;
3. order the selected states by literal changing-owner transitions through
   the old root.

Then the selected root--owner edges form a perfect matching `D`, and the
transition edges through the old roots form a second perfect matching `H`.
The fixed lower suffixes and the nine age-type masses are unchanged.

However, the frozen full-static flag certificate

```text
scratch/threadA_k17_gks_full_static_flags_20260801.tsv
SHA256 5fc20be6e76a5ca0336ce9bc51e252d2d597f2ec2ea9ff96a54264eb050cf886
```

does **not** admit such a transition cycle.  Exhausting all `12,870`
attachment states and every aligning rotation gives

```text
literal turn templates, including one packet loop       2457
labelled state arcs                                     19656
loop-free zero-out roots                                  738
loop-free zero-in roots                                   523
loop-free projected root matching number                  669
```

Thus even the projected successor graph has matching deficiency
`1430-669=761`.  A single zero row already suffices: root `p=0` has no
literal successor for any of its nine owner attachments.

This does not contradict the earlier `202`-row theorem.  That theorem used
a different flag partition certificate, of SHA prefix `908651cb`; moreover,
it already quantified over all nine attachments.  The `202` rows were not
an artefact of freezing one arbitrary attachment.

## 2. Exact state-cycle implication

Write the fixed flag at root `p` as

\[
 Q_p=C^p_0\mathbin{\dot\cup}C^p_1\mathbin{\dot\cup}C^p_2,
 \qquad |Q_p|=8.
\]

For `alpha` outside `Q_p`, the incidence state

\[
 s=(p,\alpha),\qquad T_s=Q_p\cup\{\alpha\}
\]

uses one of the nine possible rank-nine owners.  A **state transversal** is
a set `S` of `1430` states for which both maps

\[
 s\longmapsto p(s),\qquad s\longmapsto [T_s]
\]

are bijections onto the root and owner necklace orbits.

Let `s=(p,alpha)` and `t=(q,b)`.  A phase-labelled arc `s -> t` exists when
there are an entering label `beta != alpha` and a rotation `rho^delta` such
that

\[
 \rho^\delta(Q_q\cup\{b\})=Q_p\cup\{\beta\}.       \tag{2.1}
\]

Put

\[
 D_i=\rho^\delta C^q_i\quad(0\le i\le2),
 \qquad D_3=\{x\},
\]

where `x` is the unique label deleted from the next owner to obtain the
rotated target root.  Literal rotated age compatibility is exactly

\[
 D_{i+1}\subseteq C^p_i\quad(0\le i\le2),          \tag{2.2}
\]

and

\[
 D_0=\{\beta\}\mathbin{\dot\cup}
      (C^p_0-D_1)\mathbin{\dot\cup}
      (C^p_1-D_2)\mathbin{\dot\cup}
      (C^p_2-D_3).                                  \tag{2.3}
\]

These are necessary and sufficient: (2.2) carries the three survivor age
classes, and (2.3) is the new age-zero refresh partition.

### Proposition 2.1 (two perfect matchings)

Suppose a directed cycle uses one state from each root and owner orbit and
every arc satisfies (2.1)--(2.3).  Define

\[
 D(T_s)=Q_{p(s)}.
\]

For the arc from `s` to its successor `t`, define `H` by joining the old
root `Q_{p(s)}` to the aligned owner represented by `T_t` in (2.1).  Then
`D` and `H` are perfect incidence matchings.

#### Proof

The state-transversal conditions make `D` bijective on both shores.  Every
cycle vertex has one predecessor, so every selected owner is the head of
exactly one transition.  Every old root is the tail of exactly one
transition.  Equation (2.1) says precisely that the corresponding root and
owner are incident.  Hence `H` is also bijective on both shores. `square`

The lower rank-`2,...,8` suffixes depend only on
`C_0,C_1,C_2`, not on the selected fourth singleton.  Therefore the static
lower flags and the exact type masses survive automatically.  This
proposition does **not** by itself prove upper-turn coverage, residence,
deep shadows, or common-cap feasibility.

There is also a phase condition omitted by an unlabelled cycle statement.
If the quotient cycle has phase labels `delta_e`, its `Z_17` physical lift
is connected exactly when

\[
                       \sum_e\delta_e\ne0\pmod {17}. \tag{2.4}
\]

Thus a projected cycle is necessary but not sufficient for the desired
physical Hamilton chronology.

## 3. Why the old `202` rows were not frozen-attachment artefacts

The earlier dynamic certificate is

```text
scratch/threadA_k17_gks_dynamic_switched_seed2512_20260801.tsv
SHA256 908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451
```

Its exact constructor explicitly formed all `1430*9=12870` states.  Every
legal turn template was expanded to the eight source states
`alpha != beta`; the target attachment and aligning phase were also part of
the emitted row.  Its independently replayed census was

```text
turn templates                         3828
labelled state arcs                   30624
zero-out / zero-in roots            202 / 191
projected root matching number        1158.
```

Consequently the old zero-row set was attachment-independent on that fixed
flag catalogue.  What *was* later frozen was a particular transversal when
testing the stronger complement-dual successor `A^2`; that is a different
`1009`-failure statement.  It must not be conflated with the `202` universal
zero rows.

The new full-static certificate has the same roots and stored owners but
different age partitions.  Replaying the same all-state construction gives
the stronger `738`-row obstruction above.  The two zero sets overlap in
`165` roots; `37` old zero rows acquire a successor, while `573` new zero
rows appear.  Thus changing the low-rank flag assignment can repair
individual rows, but this particular globally exact assignment greatly
reduces chronological support.

The new zero rows by packet kind are

```text
pair_broken 198, pair_native 304, skip 224, triple 12,
```

and by age type `0,...,8` are

```text
(114,266,5,12,6,81,98,144,12).
```

## 4. A one-root explicit obstruction

For packet `p=0` in the full-static certificate,

\[
 (C_0,C_1,C_2)=(117,10,128),\qquad Q=255
\]

in decimal mask notation.  There are exactly `9*9=81` possible pairs:
choose the entering label `beta` outside `Q`, then delete one of the nine
labels of `Q+beta` to obtain the next root.  The next packet and its aligning
rotation are forced by that facet.

Let `S_i` denote failure of the `i`th containment in (2.2), and let `R`
denote failure of (2.3).  Exact evaluation of all 81 candidates gives

```text
failure set          multiplicity
S2+R                         2
S1+S2+R                      7
S1+S3+R                      1
S2+S3+R                     18
S1+S2+S3+R                  53
```

In particular every candidate fails the refresh identity.  Since the
source attachment `alpha` only excludes the one choice `beta=alpha`, no
choice of `alpha` can create an arc.  This one root is already a complete
obstruction to any spanning transition cycle.

## 5. Frozen replay artifacts and scope

```text
scratch/threadA_k17_fullstatic_attachment_audit_20260801/turns.tsv
  SHA256 c509eaaa43f4446ce429ec24284eea6b583d7854c02522041e7d954df8f0469d
scratch/threadA_k17_fullstatic_attachment_audit_20260801/generator.audit.json
  SHA256 1105b15fd0af39cbe41db6c3a479afe0ba68376c2280671aa39a706d8e0173af
scratch/threadA_k17_fullstatic_attachment_audit_20260801/independent.audit.json
  SHA256 eeabf03ddc6eaf57a4d18abd9cb1ba5f834412aa12fff283e2ace21aca44f85f
scratch/threadA_k17_fullstatic_attachment_audit_20260801/audit_zero_rows.py
  SHA256 a122f9b7396d253257a52e27d3bcccf51424a6a89344269dad8a1b44b977d403
scratch/threadA_k17_fullstatic_attachment_audit_20260801/zero_rows.audit.json
  SHA256 c31149e931581ca176c715145b309d0ced26e5bf552c3153a3fe9f099d4eab66
```

The generator is the pre-existing exhaustive literal constructor.  The
Python verifier independently rebuilds all turns, state arcs, suffix decks,
type masses and the projected Hopcroft--Karp value.  The concise comparison
audit independently rebuilds both old and new zero-row sets and packet
`0`'s 81 failure masks.

This is a no-go only for the frozen `5fc20be6...` full-static flag
assignment under the exact transition equations (2.1)--(2.3).  It does not
rule out jointly rechoosing the low-rank flag attachment and the transition
cycle, alternating GKS containment surgery, or a non-GKS rank-eight rooted
flag system.
