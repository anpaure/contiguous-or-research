# Candidate29 balanced-outward `C8 x C12`: exact terminal algebra and provider gate

Date: 2026-08-01  
Status: **complete exact candidate29 no-go, independently replayed, in the stated terminal shell**

This is the balanced-outward specialization of
`MATH_THEOREM_THREAD_D_CANDIDATE29_SUPPORT10_TWO_CIRCUIT_TERMINAL_GATE_20260801.md`.

## 1. Scope and notation

Fix the literal candidate29 factor.  Its quotient successor is the one-cycle

\[
                 P=\bar H^{-1}\bar D,
\]

with voltage `3 mod 17`, upper hole `u=0x0355f`, and lower hole
`l=0x0062f`.  This note concerns the two balanced-outward shells

\[
       H4\times D6 \qquad\hbox{and}\qquad H6\times D4,
\]

where the integers are assignment-cycle lengths; physically these are
`H-C8 x D-C12` and `H-C12 x D-C8`.

Only terminal matching validity, rank-10/rank-7 palette completeness,
quotient connectedness, and `Z17` voltage are in scope.

Let `alpha` be the D assignment cycle and `beta` the H assignment cycle, with
supports

\[
 A=\operatorname{supp}(\alpha),\qquad
 B=\operatorname{supp}(\beta),\qquad \{|A|,|B|\}=\{4,6\}.
\]

Every raw nonloop literal incidence is retained, including an incidence equal
to the opposite base matching.  Equal complete side terminal maps, and only
those maps, are deduplicated.

## 2. Exact terminal map and pair rescue

The terminal endpoint maps and quotient successor are

\[
 \bar D'=\bar D\alpha,\qquad
 \bar H'=\bar H\beta,\qquad
                 P'=\beta^{-1}P\alpha.                 \tag{2.1}
\]

Define the isolated opposite-base conflicts

\[
 C_D=\{x\in A:d'_x=h_x\},\qquad
 C_H=\{x\in B:h'_x=d_x\}.                              \tag{2.2}
\]

### Lemma 2.1 (pair rescue)

The raw pair is terminal incidence-disjoint if and only if

\[
 C_D\cup C_H\subseteq A\cap B                           \tag{2.3}
\]

and `d'_x != h'_x` for every `x in A cap B`.

Consequently

\[
             |C_D\cup C_H|\le |A\cap B|\le4.           \tag{2.4}
\]

In particular every raw atom with at least five opposite-base obligations is
unusable in this shell.  The condition is exact: containment alone does not
exclude a new collision at an overlap owner.

## 3. Palette currents and overlap correction

Put

\[
 r_-=|A\cap B|,
 \qquad
 r_+=|\bar D(A)\cap\bar H(B)|.                          \tag{3.1}
\]

The numbers of changed lower and upper rows are respectively

\[
                  n_-=10-r_-,\qquad n_+=10-r_+.         \tag{3.2}
\]

For either shore, delete every changed base turn once and insert every literal
terminal turn once.  If `a_T=d_T-g_T` is the resulting deletion current, then
the terminal shore is complete exactly when

\[
 a_h\le-1,
 \qquad
 a_T\le\mu(T)-1\quad(T\ne h),                           \tag{3.3}
\]

where `h` is the corresponding base hole.  Also `sum_T a_T=0`.

At an owner/facet overlap, form the four-term square first in the free group
on all trace ranks and then project to the required rank palette:

\[
 \kappa=\operatorname{pr}\bigl([R]-[P]-[Q]+[B]\bigr).   \tag{3.4}
\]

This order matters for pair-rescued atoms: an isolated $P$ or $Q$ can be
off-rank.  The projected positive mass is nevertheless at most two, since
its positive part is contained in $[R]+[B]$.  Hence every palette-exact pair
satisfies

\[
 \operatorname{Def}(\nu_-)\le2r_-,
 \qquad
 \operatorname{Def}(\nu_+)\le2r_+.                     \tag{3.5}
\]

Here $\nu_\pm$ is the required-rank projection of the base palette plus the
two isolated side columns, and

\[
                  \operatorname{Def}(\nu)
                  =\sum_T(1-\nu(T))_+.
\]

This is a sound projected-current cut, not a sufficient test; negative square
terms can create new holes.

If `s` changed base turns have load one and the `n` new turns have collision
excess `chi`, the exact protected-singleton count also gives

\[
                         n-s\ge1+\chi.                  \tag{3.6}
\]

## 4. Exact provider clauses

For each shore, the named hole must be created by one of exactly three kinds
of witness:

1. an unmixed D provider outside the owner/facet overlap;
2. an unmixed H provider outside the overlap; or
3. a literal mixed terminal pair on the overlap.

The lower clause is indexed by owners and the upper clause by facets.  These
clauses are necessary and sufficient for creation of the two named targets;
the full current inequalities (3.3) are still required to protect old colours.

### Lemma 4.1 (support-four gap rule)

Suppose both named holes are witnessed by unmixed upper/lower provider arcs on
the same assignment 4-cycle.  Then the two provider arcs are antipodal: their
two directed intermediate-arc gaps are exactly

\[
                              (1,1).                    \tag{4.1}
\]

#### Proof

The frozen provider audit proves that no lower-provider head is an
upper-provider tail and no upper-provider head is a lower-provider tail.
Thus the two provider arcs cannot be consecutive in either direction.  Two
distinct arcs on a directed 4-cycle have two intermediate-gap counts summing
to `4-2=2`.  Both counts are positive, so both equal one.  ∎

This is a sound branch rule only when both witnesses are unmixed and assigned
to the same support-four atom.  It cannot be imposed when one witness lies on
the support-six atom, the two witnesses lie on different atoms, or either is
mixed.  For comparison, the corresponding support-six same-atom possibilities
are `(1,3),(2,2),(3,1)`.

## 5. Topology and parity

Equation (2.1) is the full successor identity.  A convenient changed-tail set
is

\[
 S=A\cup\alpha^{-1}P^{-1}(B),\qquad |S|\le10.            \tag{5.1}
\]

Cut the base outgoing arcs at `S`, reconnect them by their literal terminal
heads, and sum the intervening base segment lengths and voltages.  This gives
the exact contracted topology.  No naive `A union B` identification is needed.

Both assignment cycles have even length and therefore odd sign.  Hence

\[
 \operatorname{sgn}(P')
 =\operatorname{sgn}(\beta)\operatorname{sgn}(P)
  \operatorname{sgn}(\alpha)
 =\operatorname{sgn}(P).                                \tag{5.2}
\]

Since `P` is a 1430-cycle, every terminal quotient factor has an odd number of
components.  At most ten changed ports occur, so the only possible component
counts are

\[
                         1,3,5,7,9.                     \tag{5.3}
\]

Parity does not obstruct a connected factor.  A connected row must also have
nonzero literal voltage modulo 17.

## 6. Complete finite test and implementation plan

For both orientations:

1. enumerate every raw simple directed assignment 4-cycle and 6-cycle;
2. deduplicate by the complete sorted `(owner,new incidence)` side map;
3. precompute opposite-obligation count and unmixed upper/lower provider
   positions for every atom;
4. apply the exact rescue-containment cut (2.3), then the final overlap
   inequalities;
5. optionally apply the proved three-way provider clauses, using the `(1,1)`
   rule only on its guarded support-four branch;
6. compute exact pointwise currents (3.3), including all cross squares;
7. compute topology from (2.1)/(5.1) and literal voltage; and
8. fully replay every one-palette-safe row, every strict running minimum, and
   every terminal-safe row from all 1430 literal turns.

The frozen Cartesian execution used the rescue-containment prefilter but did
not use the optional provider/gap pruning; it therefore exhausts a superset
of the rows surviving those proved cuts.

The independently certified raw banks are

| bank | unique literal maps | base-valid |
|---|---:|---:|
| H4 | 1,386 | 802 |
| D4 | 1,377 | 797 |
| H6 | 46,287 | 20,504 |
| D6 | 46,171 | 20,425 |

Thus

\[
 |H4\times D6|=63,993,006,
 \qquad
 |H6\times D4|=63,737,199,                          \tag{6.1}
\]

for `127,730,205` raw pairs total.  The raw census is

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  support10_two_circuit_raw_census.audit.json
SHA 5617dc61cf85668a718cf7fc2a5b2fbd633b0700b93b5b3e3d4fbf66fcaec2fb
```

## 7. Exact finite verdict

The complete literal Cartesian execution gives:

| orientation | terminal-valid | connected nonzero | upper-safe | lower-safe | both |
|---|---:|---:|---:|---:|---:|
| H4 x D6 | 16,441,089 | 3,026,977 | 556 | 97 | 0 |
| H6 x D4 | 16,401,849 | 2,923,439 | 47 | 47 | 0 |

The minimum connected-nonzero total debt is three in each orientation.
Every one-palette-safe row and every strict running/final minimum was fully
replayed from all 1430 literal upper and lower turns (`660+103` full replays).
Component counts are exactly among the odd values in (5.3), and connected
voltage agrees with the additive literal current in every connected row.

The original-hole current is also insufficient.  In `H4 x D6`, exactly
`1,609` terminal-valid rows fill both original holes; their minimum new debt
is `3`, attained once.  In `H6 x D4`, the corresponding count is `682` and
the minimum new debt is `5`, attained twice.  Thus all `2,291`
both-original-hole-filling rows eject other colours; their witnesses need not
be a single mixed provider.

Therefore no simultaneous candidate29 `C8 x C12` row preserves both q1
palettes, even without topology.  In particular none is an immediate
palette-exact physical repair.

An implementation independent of the primary evaluator regenerated all four
raw banks and scanned both Cartesian products without the primary rescue
prefilter.  It directly rebuilt terminal literal maps, pointwise currents,
the changed-tail successor $\beta^{-1}P\alpha$, component lengths, and
literal voltages.  It exactly matches every displayed count, the complete
joint-hole, component-count, and connected-voltage histograms, and both
minimum rows.  It fully replayed all `653` and `94` one-palette-safe rows
from all 1430 owners and facets.

The strongest reusable dimension-free filters exposed by this shell remain:

* at most four opposite obligations can be pair-rescued;
* overlap deficiency is bounded by twice owner/facet overlap;
* repeat-release must pay every protected singleton plus the new hole;
* named-hole creation obeys the exact three-way provider clauses; and
* an unmixed two-hole support-four witness is forced into gap `(1,1)`.

Frozen execution:

```text
scratch/threadD_k17_candidate29_c8_c12_20260801/
  audit_candidate29_c8_c12.cpp
SHA f4c5b566c19c2394a036488fdc377c6a035842f2731f0bef7f305f48e11e6db5

  audit.json
SHA 0b27666c03a2d7bf5ff6a8c437b907901b4634da5a55b474a537347b6922f10e

  audit_candidate29_c8_c12_independent.cpp
SHA 4aadfb2e4925cec3dfc88ac686dc93c7d7a9e3b8f8a532af604b00b8ad542234

  independent.audit.json
SHA ce9f3a40ed577de0b9fc44a0e2a0eaffd5073cb3260892122d97e3ec03692391
```

The H100 O3 execution exited normally in `256.21s`, with maximum RSS
`34,964 KiB` under the two-GiB cap.  The independent H100 O3 execution exited
normally in `157.21s` CPU / `157.23s` wall, with maximum RSS `24,868 KiB`
under the same cap.  A preceding warning-fatal compile chain launched no
checker and made no mathematical inference.

This no-go makes no q2, residence, source, or compiler claim and does not
cover `C6 x C14`, triple circuits, or `C30`.
