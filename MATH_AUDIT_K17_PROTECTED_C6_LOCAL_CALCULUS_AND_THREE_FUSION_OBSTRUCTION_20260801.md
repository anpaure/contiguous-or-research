# The protected k=17 factor has an exact local C6 calculus, but no static three-C6 loose hypertree can fuse its seven components

**Date:** 2026-08-01  
**Status:** exact finite theorem for the authenticated factor
`scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`, SHA-256
`7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`.
In addition to the static obstruction, complete dynamic replay closes every
three-step sequence in which each merger is individually q1-safe, and a
separate complete sweep closes one individually q1-safe component-neutral
preparation followed by a static three-fusion loose hypertree.  It does not
exclude a sequence which is only net-q1-safe, more than one preparatory
move, a higher-support connector, or a different factor.

The literal census supersedes the even-component-delta claims in Section 3
of `MATH_THEOREM_K17_PROTECTED_C6_COUPLED_OBJECTIVES_AND_LOOSE_HYPERTREE_20260801.md`
and Section 2 of
`MATH_THEOREM_A_K17_PROTECTED_C6_LOCAL_DELTA_AND_LOOSE_HYPERTREE_GATE_20260801.md`.
Their q1, run-locality, witness-locality and serial final-replay principles
remain usable; only the false opposite-shore stub assumption and its parity
consequences are withdrawn.

## 1. Literal toggle

Let `C` be a rank-seven set and let `a,b,c` be three labels outside `C`.
Put

\[
 l_a=C+a,\quad l_b=C+b,\quad l_c=C+c
\]

and

\[
 o_{ab}=C+a+b,\quad o_{bc}=C+b+c,\quad o_{ca}=C+c+a.
\]

The Boolean incidence hexagon has the two alternating matchings

\[
 E_0=\{l_ao_{ab},l_bo_{bc},l_co_{ca}\},\qquad
 E_1=\{l_ao_{ca},l_bo_{ab},l_co_{bc}\}.                 \tag{1.1}
\]

A directed toggle is legal in the frozen factor `F` precisely when

\[
 E_i\subseteq F,\qquad E_{1-i}\cap F=\varnothing,
 \qquad E_i\cap P_{52}=\varnothing,                     \tag{1.2}
\]

where `P_52` is the authenticated protected-incidence bank.  Replacing
`E_i` by `E_(1-i)` preserves every rank-eight and rank-nine degree and all
52 protected incidences.

For each `l_x`, let `p_x` be its other selected rank-nine neighbour.  In the
projected owner two-factor, (1.1) is exactly the three-edge replacement

\[
 p_xo_i(x)\longmapsto p_xo_{1-i}(x),\qquad x=a,b,c.      \tag{1.3}
\]

Thus all effects can be audited without reconstructing any unselected
incidence.

## 2. Component calculus

Delete the three old projected edges in (1.3).  Their six endpoints are
paired in two ways:

1. by the three surviving path fragments of the old factor; and
2. by the three new edges.

The number of alternating cycles in the union of these two pairings is the
number of new affected components.  Subtracting the number of old affected
components gives the exact component delta.

The surviving path pairing is an arbitrary perfect matching on the six
stubs.  It need not pair an owner-shore stub with a lower-shore stub: a
retained path may have even length and end on the same shore.  Therefore it
cannot in general be encoded by a permutation in `S_3`.  In particular the
component delta is not restricted to even values; all five values

\[
                         -2,-1,0,1,2                    \tag{2.1}
\]

occur in the authenticated census.  Any argument obtaining only
`{-2,0,2}` by composing a three-cycle with an owner-to-lower permutation
has silently assumed the false opposite-shore property.

In particular, if the three old edges lie in three distinct components,
the deletion leaves three paths and (1.3) joins them into one cycle.  Hence

\[
                         \Delta c=-2.                    \tag{2.2}
\]

Only this forward implication is used below.  The general component test is
the arbitrary perfect-stub-matching union-cycle formula above, not a
classification by the number of old components met.

## 3. Residence and upper-witness locality

Only the three projected adjacencies in (1.3) change.  A positive coordinate
run of length at most three whose status changes must cross one of those
adjacencies.  Equivalently, its start lies within directed distance at most
three of a changed endpoint.  Therefore the exact `run1,run2,run3` delta is
a junction-local calculation.  The retained audit also performs a complete
cycle replay as an independent equality check.

Likewise, an old or new interval witness differs only if it crosses a
changed adjacency.  For ranks 11--13 one extends each of the six directed
seam rays only until its union first has rank above 13; monotonicity of OR
then proves that no later interval can return to the audited ranks.  Comparing
these seam inventories against the global occurrence counts gives, for each
rank, the number of newly opened holes, healed holes and their net difference.

These deltas are exact for one toggle.  They are not blindly additive across
several toggles: a final compound candidate must be replayed because a new
interval may cross two changed seams.

## 4. Exact census

The frozen factor has

\[
 c=7,\qquad (R_1,R_2,R_3)=(0,3073,2710),\qquad
 (H_{11},H_{12},H_{13})=(1502,295,9).                   \tag{4.1}
\]

Exhausting every rank-seven core, every three-label choice and both
orientations of (1.1) gives

```text
protected-safe directed C6 toggles             46818
three-component fusions                         3379
q1-hole-free toggles                            5710
three-component and q1-hole-free                 405
q1-hole-free fusions nonincreasing run<4         257
q1-hole-free fusions nonincreasing deep holes    262
```

The TSV records the literal six incidences, old component triple, exact
component delta, q1 hole count, all three run deltas, and for ranks 11--13
the new-hole, healed-hole and net-hole deltas for every q1-hole-free move.
The full component-delta distributions are

\[
\begin{array}{c|rrrrr}
\Delta c&-2&-1&0&1&2\\ \hline
\text{all protected-safe}&3379&15875&21708&4462&1394\\
\text{q1-hole-free}&405&1967&2642&527&169.
\end{array}                                               \tag{4.2}
\]

Across the 5,710 q1-hole-free moves, the total run delta ranges from `-6`
to `+5`, the total rank-11--13 hole delta from `-6` to `+6`, and no move
creates a singleton run.  Three useful q1-hole-free fusion witnesses on
components `{0,1,2}` are:

\[
\begin{array}{c|c|c|c|c}
\text{TSV id}&(C;a,b,c;i)&(\Delta R_1,\Delta R_2,\Delta R_3)
 &(\Delta H_{11},\Delta H_{12},\Delta H_{13})&\text{totals}\\ \hline
33068&(76425;6,14,15;1)&(0,-1,-5)&(1,0,0)&(-6,+1)\\
26651&(59909;1,12,16;0)&(0,-2,-2)&(0,0,0)&(-4,0)\\
17416&(36449;1,12,13;0)&(0,-2,-1)&(-1,-2,0)&(-3,-3).
\end{array}                                               \tag{4.3}
\]

Thus useful local fusions are abundant; the obstruction in Section 5 is
not a lack of improving individual moves, but their component incidence.

## 5. Sharp static three-fusion obstruction

Number the seven frozen components in their retained factor order; their
owner sizes are

\[
             14305,8615,1362,18,4,3,3.                  \tag{5.1}
\]

Ignoring q1, residence and deeper-upper constraints entirely, the 3,379
three-component C6 fusions meet only the following ten component triples:

\[
\begin{array}{c|r}
\{0,1,2\}&3293\\
\{0,1,3\}&44\\
\{0,2,3\}&5\\
\{1,2,3\}&3\\
\{0,1,4\}&10\\
\{0,2,4\}&5\\
\{0,1,5\}&8\\
\{0,2,5\}&1\\
\{0,1,6\}&9\\
\{0,2,6\}&1.
\end{array}                                             \tag{5.2}
\]

Every triple containing one of the four peripheral components
`3,4,5,6` contains no other member of that four-set.  Consequently any
family of component triples covering all four peripheral components has at
least four members.

### Theorem 5.1 (no static three-C6 loose hypertree)

There do not exist three pairwise support-disjoint C6 toggles already legal
in the frozen factor whose component triples form a spanning loose
three-uniform hypertree on all seven components.  Hence the standard static
three-toggle schedule cannot realize

\[
                         7\longrightarrow5\longrightarrow3
                           \longrightarrow1.              \tag{5.3}
\]

#### Proof

A static three-C6 loose hypertree is, by definition, formed from three
initial toggles whose deleted edges lie on three distinct old components
and whose component triples have union size seven.  But a three-member
subfamily of (5.2) covers at most three of `3,4,5,6`.  It therefore misses
at least one component, a contradiction. \(\square\)

This obstruction is stronger than failure of the coupled objective: it
holds before q1, residence or ranks 11--13 are imposed.  It is also sharply
scoped.  It does not rule out:

* a dynamic three-toggle sequence whose first toggle creates a new literal
  C6 occurrence;
* a longer sequence with neutral/splitting preparatory moves;
* a support-four or higher-arity connector; or
* a different protected q1-complete factor.

## 6. Retained artifacts

```text
scratch/audit_k17_protected_c6_local_calculus_20260801.cpp
  SHA 93dcd1a38148b46f0f361f21f8a93cc5e1c2926e9f628298ed3a00672336a958

scratch/k17_protected_c6_local_calculus_20260801.tsv
  SHA f2c948de733a5286f4d21c3ba3cd2507831e2b061ca59f7fe82ace5c11b55d67

scratch/audit_k17_protected_c6_local_calculus_20260801.out
  SHA 7efac1586e378b271e3a433d958494e98c0a28b4e792b9fdc9c15238661b0535

scratch/audit_k17_protected_c6_local_calculus_20260801.log
  SHA 36cab32c6fd6baac77eefdd8cce508a53a9b52205af3221e6cc3fcc5c537d769
```

The executable was compiled with `g++ -std=c++20 -O3 -DNDEBUG` and run on
H100 pinned to one CPU core.  No local heavy enumeration or Python solver
was used.

## 7. Complete individually-safe dynamic regeneration

The 405 q1-safe three-component mergers were next treated as first moves,
not as a frozen static catalogue.  For every first child the factor was
rebuilt literally, its complete protected individually-q1-safe
three-component C6 catalogue was regenerated, and every resulting
three-component grandchild was regenerated once more.

Exactly five first children admit a safe `5 -> 3` move:

\[
 171,\ 172,\ 239,\ 248,\ 362,                         \tag{7.1}
\]

with respectively `2,2,3,3,2` second moves, for twelve total.  Complete
third-generation regeneration on all twelve states gives zero protected
individually-q1-safe `3 -> 1` moves.  Thus there is no serial sequence

\[
             7\longrightarrow5\longrightarrow3\longrightarrow1 \tag{7.2}
\]

of three incidence C6s in which every prefix retains the complete rank-ten
palette.  This conclusion is dynamic: the second and third catalogues are
not inherited from the baseline.

The literal best first merger is safe-catalogue row 144, corresponding to
full-catalogue id 17416,

\[
 (C;a,b,c;i)=(36449;1,12,13;0).                         \tag{7.3}
\]

It gives five components and

\[
 (R_2,R_3,H_{11},H_{12},H_{13})
   =(3071,2709,1501,293,9),\qquad \Phi=7583.             \tag{7.4}
\]

Its own complete second-generation safe merger catalogue is empty; the
five live branches arise from the other first moves in (7.1).  The best
two-move descendants have \(\Phi=7587\), but none has a safe final merger.
An independent clean replay reproduces all 405 children, the same five live
children, the same twelve second moves and zero third moves.

```text
scratch/threadA_k17_c6_dynamic2_20260801/sweep.audit.json
  SHA 26c3694f511e9d7ae470c40f54ae643f2fc6f3d66089dbe7b2a90894f9cf8bdf

scratch/threadA_k17_c6_dynamic2_20260801/sweep.children.tsv
  SHA 922f8e03cea9ade87c681d6fc71c01714cfb5b5c0ba998c4c97fa87e487c7964

scratch/threadA_k17_c6_dynamic2_20260801/sweep.moves.tsv
  SHA cb2bb168c197c95bbcbf4e143cd218e4d4bab72e0132616908b5aafbfd47110d

scratch/threadA_k17_c6_dynamic2_20260801/sweep.independent.audit.json
  SHA 4d308e77eba795856b9748762eb90fd9b236e857d2942b113d8eae9419ffe6b9
```

## 8. Complete one-neutral-preparation obstruction

The complete q1-safe component-neutral catalogue contains 2,642 moves, with
best \(\Delta\Phi=-8\).  For every one of these preparations, the complete
protected individually-q1-safe three-component fusion catalogue was
regenerated.  Every prepared state has at least one such fusion, and there
are 968,086 fusion rows in total.  Nevertheless, zero prepared states have
three supported component triples forming a spanning loose hypertree.
Hence one safe neutral C6 cannot prepare a static three-fusion
`7 -> 1` contraction.

This obstruction occurs before incidence-support compatibility or final
deck replay: there are zero component-mask patterns to instantiate.  An
independent endpoint/component/q1-only regeneration matches all per-state
fusion counts and again finds zero patterns.  Across all prepared states
only nine fusion rows even use a component triple containing component 4;
none combines with two other supported triples to span a loose tree.

```text
scratch/threadA_k17_c6_prep2642_20260801/prep.best.audit.json
  SHA 01a2d506ececc304edbcb88481cfbd4358a3f6f448bec5bbfda9a9335c0b788e

scratch/threadA_k17_c6_prep2642_20260801/prep.summary.tsv
  SHA ec2ffeb563391b1caecc8f9d66c1d96df4ff52c49a109960161bd6fc77387757

scratch/threadA_k17_c6_prep2642_20260801/prep.independent.audit.json
  SHA 1d8f51dadad116bfc4a6dfc1c303b4d46d87ccf2506c9026b585e697c3539733

scratch/threadA_k17_c6_prep2642_20260801/verify_k17_c6_prep2642_component_masks.cpp
  SHA 7f9e8f5cfd6dca1657dac0dfdbc2fa34e6816a7a2b73d69b86a8c178652e20cc
```

The remaining nearest C6 face is a dynamic three-merger sequence whose
intermediate factors may lose rank-ten colours but whose final aggregate
rank-ten multiplicities are positive.  The static version is already
impossible by Section 5, independently of its q1 ledger.
