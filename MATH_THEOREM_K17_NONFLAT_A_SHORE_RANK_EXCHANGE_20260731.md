# The forced `K17` A-shore runs admit an exact nonflat rank exchange

Date: 2026-07-31  
Status: exact local theorem and literal finite audit; the independent modules
do not yet fit one optimal-length global schedule

## 0. Result

The fixed-parent obstruction consists of `165` A-shore patterns

\[
                         0\,111\,0                                      \tag{0.1}
\]

whose four incident rank-six colours have unique parent occurrences.  They
cannot be removed by changing the occurrence transversal.  They can,
however, be absorbed algebraically without changing the parent owners.

The exact operation is to advance the affected A-shore path by one derivative
row.  If

\[
 A_0,A_1,\ldots,A_{q-1}\in\binom{[17]}9
\]

is one consecutive A block and `L,R` are its two seam facets, then the mixed
depth-two block

\[
                    L,A_0,A_1,\ldots,A_{q-1},R                       \tag{0.2}
\]

has depth-three derivative

\[
 A_0, A_0\cup A_1,\ldots,A_{q-2}\cup A_{q-1}, A_{q-1}.            \tag{0.3}
\]

An internal `0,111,0` owner pattern therefore becomes four consecutive
positive cofacets.  The depth-two trace has a run of length three and the
depth-three trace has a run of length four: both are exactly legal.

On the authenticated parent and on the literal hex-optimized carrier:

* the `165` patterns lie in exactly `108` residual A blocks;
* advancing all `108` blocks absorbs all `165` patterns;
* the selected modules contain `1958` distinct A owners, `2066` distinct
  lower seam/internal facets, and `1850` distinct upper cofacets;
* every module is internally depth-two and depth-three resident; and
* the direct independent-block realization incurs an exact phase-boundary
  debt of `107` positions.

Thus the immutable-run obstruction is not an obstruction to a nonflat
compiler.  The missing object is now precise: share or compensate `107`
phase boundaries while preserving the literal palettes and the common cap.

There is a second exact formulation in terms of trace-edge actuators.  The
minimum number of physical trace edges meeting the four-edge support of every
forced pattern is

\[
                              \boxed{120}.                            \tag{0.4}
\]

If actuators are restricted to the entering or leaving edge, so every cut
exposes one length-three strand rather than splitting it into two shorter
strands, the exact minimum is

\[
                              \boxed{150}.                            \tag{0.5}
\]

Cutting an edge is not itself a repair.  It turns an immutable internal run
into an endpoint obligation; the exposed positive strand must then be glued
to a donor strand.  Deleting a positive coordinate from an owner instead
shortens the run and is the wrong operation.

## 1. The local owner/cofacet zipper

Let `V_0,...,V_(q-1)` be a Johnson path of rank-`r` owners.  Let

\[
 E_i=V_i\cap V_{i+1},\qquad H_i=V_i\cup V_{i+1}.                    \tag{1.1}
\]

Suppose `L` and `R` are distinct rank-`r-1` facets of `V_0` and
`V_(q-1)`, respectively.  In the K17 A block they are literally the X/A and
A/Y seam colours.

### Lemma 1.1 (one-row phase advance)

The derivative of

\[
                         L,V_0,\ldots,V_{q-1},R                      \tag{1.2}
\]

is

\[
                         V_0,H_0,\ldots,H_{q-2},V_{q-1}.             \tag{1.3}
\]

All values in (1.2) have rank `r-1,r,...,r,r-1`; the endpoints and internal
values in (1.3) have rank `r,r+1,...,r+1,r`.

#### Proof

Containment gives `L union V_0=V_0` and
`V_(q-1) union R=V_(q-1)`.  Every internal union is the definition of
`H_i`.  Johnson adjacency makes its rank `r+1`.  \(\square\)

There is also a lower zipper.  The consecutive facets

\[
 L, E_0,E_1,\ldots,E_{q-2}, R                                   \tag{1.4}
\]

have consecutive unions `V_0,...,V_(q-1)`.  This is the same identity

\[
              (V_{i-1}\cap V_i)\cup(V_i\cap V_{i+1})=V_i           \tag{1.5}
\]

used in the K16 facet/owner exchange.  Equations (1.3)--(1.5) are its
owner/cofacet dual one row higher.

### Lemma 1.2 (residence dilation)

Fix a coordinate `x`.  If its owner trace on `V_0,...,V_(q-1)` contains an
internal run `0,1^ell,0`, then its trace on the internal cofacets in (1.3)
contains `1^(ell+1)`.  In particular `ell=3` becomes four.

The lower-facet trace in (1.4) has length `ell-1`, the owner trace has length
`ell`, and the cofacet trace has length `ell+1`.  Hence, when every internal
owner run has length at least three, the three aligned rows satisfy exactly
the depth-one, depth-two, and depth-three residence thresholds `2,3,4`.

#### Proof

On consecutive owners the coordinate indicator in `E_i` is logical AND and
in `H_i` is logical OR.  On the edge-indexed trace, AND reduces a bracketed
positive run's length by one overall, while OR increases it by one.
\(\square\)

## 2. The minimum actuator theorem

For each forced pattern with positive owner starts `s,s+1,s+2`, put

\[
                         I_s=\{s-1,s,s+1,s+2\}\subset\mathbb Z_{6390}. \tag{2.1}
\]

These are its entering, two internal, and leaving trace edges.

### Theorem 2.1 (all-support optimum)

The transversal number of the 165 four-edge circular intervals is `120`.

#### Proof

Some point of `I_(s_0)` belongs to an optimum.  Condition on each of its four
possible values and cut the circle immediately after that point.  Every
remaining interval becomes an ordinary length-four interval.  The standard
right-endpoint greedy algorithm is optimal for intervals on a line.  All
four conditioned instances return `120`, and the emitted sets are replayed
against all `165` intervals.

One canonical optimum has edge-load profile

\[
                         1^{90}2^{15}3^{15}.                         \tag{2.2}
\]

Every forced interval is hit exactly once.  The selected edge is entering
for 16 patterns, the second internal edge for 30, and leaving for 119.
\(\square\)

### Theorem 2.2 (boundary-only optimum)

If only entering and leaving edges may be selected, the minimum is `150`.

#### Proof

Make a graph whose vertices are trace edges and whose 165 graph edges join
the entering and leaving edge of one pattern.  The literal graph is the
disjoint union of 135 single edges and 15 paths with two edges.  Its minimum
vertex cover therefore has size

\[
                           135+15=150.                               \tag{2.3}
\]

The audit emits and checks such a cover.  \(\square\)

The distinction is operational.  A boundary actuator exposes one positive
strand of length three and needs a donor prefix/suffix of capped length at
least one.  Cutting after one or two positive owners exposes two strands of
lengths `1+2`; they need two-sided donors of lengths at least `3+2` in the
appropriate orientation.  Rejoining the two old pieces directly recreates
the forbidden length-three run.

## 3. Why pointwise facet deletion is wrong

Replacing one positive owner by a facet which omits `x` changes
`0,111,0` into positive components of total length at most two.  To erase the
run entirely, all three positive owner positions would have to omit `x`.

Across the 165 forced patterns this gives 495 point-coordinate demands on
420 A owners.  Their exact profile is

\[
                              1^{345}2^{75}.                          \tag{3.1}
\]

A rank-eight facet of a rank-nine owner omits only one coordinate, so the 75
double-demand positions rule out the pointwise codimension-one deletion
scheme.  This does not rule out codimension-two faces, but those require a
different, two-row realization.  Phase advance avoids the conflict: it
keeps all positive owners and dilates their run in the next row.

## 4. Literal whole-macro audit

Every forced support lies strictly inside one retained A path.  Exactly 108
of the 1430 residual macros contain at least one forced pattern, with pattern
profile

\[
                       1^{77}2^9 3^{20}4^1 6^1.                     \tag{4.1}
\]

Advancing the whole A block in each of those macros is therefore the minimum
whole-macro selection: no unselected macro can repair a pattern internal to
another macro.  The 120-edge optimum lies in the same 108 macros, with
actuator profile

\[
                              1^{99}2^8 5^1.                          \tag{4.2}
\]

For every selected macro the audit reconstructs the X/A seam facet, all
internal A/A facets, the A/Y seam facet, all A owners, and all internal
cofacets directly from the frozen flow artifact.  It then checks (1.3)--
(1.5) literally.  The resulting selected occurrence counts are

\[
\begin{array}{c|r|r}
\text{row object}&\text{occurrences}&\text{distinct}\\ \hline
\text{lower seam/internal facets}&2066&2066\\
\text{A owners}&1958&1958\\
\text{internal cofacets}&1850&1850.
\end{array}                                                         \tag{4.3}
\]

Every one of the 165 forced patterns is replayed as four consecutive
positive cofacets.  There is no positive run below three strictly internal
to any selected mixed depth-two block and none below four strictly internal
to its depth-three derivative.  The macro paths are also verified to occur
contiguously, in one orientation or the other, in the literal hex-optimized
carrier.

## 5. Exact remaining realization and capacity conditions

The preceding theorem is local.  A global schedule at `B(17)=24313` must
satisfy all of the following simultaneously.

1. **Actuator hitting.**  Every forced support is phase-advanced or cut.  The
   exact marginal minima are 120 unrestricted or 150 boundary-only.
2. **Socket realization.**  Every cut support is assigned occurrence-labelled
   predecessor/successor ports.  A boundary length-three strand must receive
   one positive donor; an internal cut must satisfy both capped donor demands.
3. **Depth-two realization.**  After concatenation, every internal positive
   run in the mixed depth-two row has length at least three.  The local
   modules already pass; only their exposed prefix/suffix ports remain.
4. **Depth-three realization.**  The derivative has no internal positive run
   below four.  Again the local modules pass, so this is an exact capped
   strand-gluing condition at their ports.
5. **Row capacity.**  A module with `q` A owners replaces the `q+1` facet-rail
   tokens by the mixed `q+2` tokens in (0.2), a cost of one.  Installing 108
   modules independently costs 108 positions, whereas the linear opening of
   a cyclic `W`-token rail supplies only one.  The independent-block debt is

   \[
                                  108-1=107.                         \tag{5.1}
   \]

   Hence the modules must share phase boundaries, be paired with reverse
   rank exchanges, or be implemented by the 120-edge socket rethread rather
   than independently.
6. **Palette restitution.**  Every displaced rank-eight lower colour and
   every owner omitted from the flat depth-three row must retain a literal
   witness in an adjacent row.  The selected local facet, owner, and cofacet
   occurrences are injective, so there is no marginal collision obstruction.
7. **Common cap.**  One physical depth-zero assignment must realize the
   completed mixed rows and all remaining lower targets.  Separate row
   residence is necessary but not sufficient for this integral condition.

These seven conditions are the exact nonflat replacement for the failed
flat-residence CNF.  The new result closes the local algebra and the complete
forced-pattern ledger.  It does not close the global phase-boundary/common-cap
coupling.

## 6. Reproducibility

```text
python3 scratch/audit_k17_nonflat_a_shore_rank_exchange_20260731.py
python3 -m py_compile scratch/audit_k17_nonflat_a_shore_rank_exchange_20260731.py
```

Artifacts:

```text
scratch/audit_k17_nonflat_a_shore_rank_exchange_20260731.py
SHA-256 e4055e8a00af386e661891f7f16d086f4c7e52d4898a5984c023db114901199c

scratch/k17_nonflat_a_shore_rank_exchange_20260731.audit.json
SHA-256 723cd1b41444ec0e1ed5c6ff249a6bb26b89d1fe10f6c6e034f1516f744747b3
payload SHA-256 af3e5c82bba3c46a17a01e6bb6d368883343e192d5cedc563ab6ea9f785c8973
```

Authenticated dependencies:

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.flow.json
SHA-256 5d27dc9b0c31f7418a0393e4725cb76582fef9aa20bc0840092b814820f64d89

scratch/k17_parent_induced_macro_port_hexopt_20260731.cycle
SHA-256 37a36e4b335ef3efaa2667e558b8477cfae46f4beff3cafe5c98c232a1f6c45a

scratch/k17_macro_residence_20260731.map.json
SHA-256 1d16bf9453627528370cda64f71c4088f54c4bc8c0c2b23510f7e17ea905f224
```

No `K17` word or improved numerical upper bound is claimed.
