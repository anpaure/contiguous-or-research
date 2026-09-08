# Independent audit of the first-exit type obstruction and threshold Hall theorem

**Date:** 2026-08-03  
**Status:** pure-mathematical line audit.  The direct type obstruction, the
empty literal acceptance graph, the exact threshold-Ferrers deficiency, and
the exit-distance histogram are valid.  One scope statement was corrected:
the `H(t)-2` lower bound applies only to the selected two-wrap set, not to a
larger unavailable set containing additional background seams.  No
computation or finite search is used.

## 0. Files audited

The principal file is

`MATH_THEOREM_FIRST_EXIT_TYPE_OBSTRUCTION_AND_THRESHOLD_HALL_20260803.md`.

It was checked against the following source theorems.

```text
25dc0c20f14254a9f9419caa41912c5fdc480f6fb3178e20822a6e6cd8a89ab0
  MATH_THEOREM_DIAGONAL_FIRST_EXIT_SECOND_TERMINAL_BANK_20260803.md
d5da9f8698cda6c4dde9c588ae104efe45124ba92ac42755d54b16690f087839
  MATH_THEOREM_FIRST_EXIT_PAIRED_BANK_SINGLE_HALL_AND_TWO_WRAP_RESET_20260803.md
7090a0622a03af5cab9944803d8d3dd8880f820cad9cfccee8dd32c21a58cba2
  MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md
69b3469d2148820a260bb5564dd0e7f6418b142cba2a4c3554bfd92060ce3f0d
  MATH_THEOREM_R_FOLDED_C8_ADDRESSED_OCCURRENCE_BIJECTION_AND_ZERO_CHARGE_SCREEN_20260801.md
108c4b0ad2adc99d9e9c91df9f1bfdb9f816494670f7473c51e7751f134177cc
  MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md
```

After the scope correction, the principal theorem has SHA-256

```text
6ceb2e483fa2d9e8a278e388a91e9d70c1a4ab1715fc6b8def3bd595da146a7b
  MATH_THEOREM_FIRST_EXIT_TYPE_OBSTRUCTION_AND_THRESHOLD_HALL_20260803.md
```

## 1. Direct value-type obstruction

The first-exit theorem supplies, at every seam, two same-phase interval
occurrences with Boolean values

\[
                         R_i\subset V_i,
             \qquad |V_i\setminus R_i|=1.             \tag{1.1}
\]

Thus their values are comparable and form one Boolean Hasse edge.

For `1<=j<d`, one canonical folded-C8 antidiagonal has values

\[
 X=B_3\cup F[1,j],\qquad
 Y=B_3\cup F[j+1,d],                                   \tag{1.2}
\]

where the two filler intervals are nonempty and disjoint.  Hence

\[
 X\setminus Y=F[1,j]\ne\varnothing,
 \qquad
 Y\setminus X=F[j+1,d]\ne\varnothing.                 \tag{1.3}
\]

The second antidiagonal is identical with base `B_1`.  Therefore both
canonical pairs are incomparable.  A permutation of Boolean coordinates is
a Boolean-lattice automorphism, so it preserves comparability.  It cannot
map either ordered orientation of (1.2) to either orientation of (1.1).

This proves the claimed obstruction for coordinate relabellings and, a
fortiori, for direct occurrence lifts which preserve the two Boolean values.
It does not forbid a protected packet which changes the values and proves a
new compiler semantics.  The theorem is correctly scoped to the direct
value-preserving face.

## 2. Independent phase obstruction and exact literal deficiency

The addressed folded-C8 audit places the two coordinates of

\[
 P_0(j)\longleftrightarrow S_1(j+1)
 \quad\hbox{and}\quad
 P_1(j)\longleftrightarrow S_0(j+1)                    \tag{2.1}
\]

in opposite phase words.  A first-exit pair `(w_i,v_i)` belongs to one
fixed q1 phase bundle.  Hence a map preserving occurrence phase cannot
identify (2.1) with the first-exit pair even if Boolean values are ignored.

On the face which requires both literal value preservation and phase
preservation, every canonical ticket is therefore a loop in the
ticket-by-seam graph.  The two antidiagonals contain `d-1` tickets each and
their shores are disjoint, so the logical ground set has size `2(d-1)`.
Its maximum matching has size zero and its exact deficiency is

\[
                              2d-2.                    \tag{2.2}
\]

This is an exact statement only on the direct-lift face.  It is not a
negative theorem about all possible value-changing type converters.

## 3. What first-exit geometry does not imply

The complete terminal Rado/gammoid theorem forms physical menus only after
the cap, phase, occurrences, flags, endpoints, guards, background
reservation, and terminal type are fixed.  The exit numbers `h_i` alone do
not restrict which ticket types accept which complete seam bundles.

At this abstract interface one may formally filter the seam bundles by any
bipartite edge set.  Therefore no interval, convex, laminar, or Hall
expansion property follows from the first-exit geometry alone.  This is a
logical nonimplication statement.  It does **not** assert that every such
artificial filter is physically realizable by the canonical compiler.  The
principal theorem was patched to state this distinction explicitly.

## 4. Exact threshold-Ferrers deficiency

Assume the additional converter theorem says that ticket `x`, of integer
requirement `a_x>=2`, accepts exactly the available seams satisfying
`h_i>=a_x`.  Put

\[
 I_t=\{x:a_x\ge t\},\qquad
 E_t=\{i\notin Z:h_i\ge t\}.                           \tag{4.1}
\]

The seam sets are nested.  For any nonempty ticket family `X`, let
`t=min_{x in X} a_x`.  The union of its neighborhoods is exactly `E_t`, and
`X subseteq I_t`.  Thus

\[
 |X|-|N(X)|\le |I_t|-|E_t|.                            \tag{4.2}
\]

Conversely, if requirement `t` is attained, the family `I_t` contains a
ticket whose neighborhood is `E_t`; all other members have smaller nested
neighborhoods.  Hence

\[
                         N(I_t)=E_t.                    \tag{4.3}
\]

If `t` is unattained, `|I_t|=|I_{t+1}|` and
`|E_t|>=|E_{t+1}|`, so its candidate cannot exceed the next one.  Iterating
reaches an attained requirement or the empty family.  Therefore the exact
Hall deficiency is

\[
 \boxed{
 \delta=\max_{t\ge2}
 \left(|I_t|-|E_t|\right)_+
 =\max_{t\ge2}\left(A(t)-H_Z(t)\right)_+.}             \tag{4.4}
\]

The empty ticket family contributes zero, resolving the otherwise undefined
minimum requirement.  Requirements larger than `r+1` are also covered:
their seam neighborhood is empty and (4.4) detects them.

In particular, if all requirements equal two, every ticket accepts every
available seam, because every first-exit distance is at least two.  A
perfect matching then exists exactly when

\[
                              |I|\le W-|Z|.             \tag{4.5}
\]

## 5. Exit-distance histogram

In a maximal constant run of the upper word of length `L`, the run identity
from the paired-bank theorem gives the successive first-exit distances

\[
                              L+1,L,\ldots,2.           \tag{5.1}
\]

Consequently the number at least `t` in that run is
`(L-t+2)_+`, and over all runs

\[
                  H(t)=\sum_{j=1}^{J}(L_j-t+2)_+.      \tag{5.2}
\]

The special values are

\[
 H(2)=W,
 \qquad H(3)=\sum_j(L_j-1)=W-J.                        \tag{5.3}
\]

If the immediate-upper word is surjective, each of its

\[
                         U={2r-1\choose r+1}
\]

values contributes at least one maximal run, so `J>=U`.  Since

\[
 {U\over W}={r-1\over r+1},
 \qquad W-U={2W\over r+1},                             \tag{5.4}
\]

we obtain, for every `t>=3`,

\[
             H(t)\le H(3)=W-J\le {2W\over r+1}.        \tag{5.5}
\]

The direction is important: this is an upper bound on long-exit supply.
Surjectivity supplies no positive lower bound on `H(3)`, because repeated
upper values may occur in separated singleton runs.

## 6. Scope correction for unavailable seams

For an arbitrary unavailable seam set `Z`, at most `|Z|` members of any
histogram level are removed.  The universally valid bound is

\[
                     H(t)-|Z|\le H_Z(t)\le H(t).       \tag{6.1}
\]

The paired-bank opening theorem proves the existence of a selected cut
whose wrap-loss set `Z_wrap` has cardinality exactly two.  If no further
background seams are unavailable, (6.1) specializes to

\[
              H(t)-2\le H_{Z_{\rm wrap}}(t)\le H(t).   \tag{6.2}
\]

The original principal draft used (6.2) with `Z` already described as a
wrap/**background** unavailable set.  That was too broad: additional
background deletions can remove more than two seams.  The theorem has been
patched to distinguish (6.1) from (6.2).  Its threshold deficiency formula
(4.4) was already written with the correct actual set `Z` and is unchanged.

## 7. Final proof-safe implication

The audit supports exactly the following chain.

1. The first-exit theorem supplies `W` deterministic same-phase nested Hasse
   pairs, and a selected linear opening loses exactly two of them.
2. These pairs do not directly instantiate the canonical folded-C8 cross
   tickets: Boolean order type and phase type both disagree.
3. A protected converter is therefore a genuine theorem premise.
4. If that converter has exact threshold acceptance, all terminal Hall cuts
   collapse to the scalar ledger (4.4), using the actual unavailable set.
5. The run histogram is exactly (5.2), but upper surjectivity alone does not
   guarantee enough long exits for requirements at least three.

Accordingly, the first-exit bank closes raw paired-address capacity.  It
does not close typed canonical acceptance or prove an additive-constant
construction without the missing protected converter and background-safe
Hall bound.
