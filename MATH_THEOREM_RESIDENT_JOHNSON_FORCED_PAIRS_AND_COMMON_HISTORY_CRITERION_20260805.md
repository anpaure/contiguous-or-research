# Exact forced pairs and a length-`d` common-history criterion for resident Johnson traces

**Date:** 2026-08-05  
**Method:** coordinatewise interval hitting; no computation or search  
**Status:** unconditional.  Antecedents of a cyclic `d`-resident Johnson
trace are exactly bounded-gap hitting sets inside the maximal coordinate
carrier intervals.  As a consequence, two components admit a common
literal history of length `d` precisely when the union of their two forced
coordinates at every aligned position lies in both maximal letters.  This
reduces zero-charge component splicing to explicit set containments; it does
not prove those containments for the PBBS braid and residual components.

## 1. Event notation

Let

\[
                         T=(T_i)_{i\in\mathbb Z_L}
\]

be a simple cyclic rank-`r` Johnson trace.  Write

\[
 T_{i+1}=T_i-\{D_i\}+\{I_i\}.                    \tag{1.1}
\]

Fix `d<r`, and assume every nonconstant positive coordinate run in `T` has
length at least `d+1`.  Also assume the component length is at least
`d+1`; this is automatic in the PBBS application.  Its maximal depth-`d`
antecedent is

\[
                         P_j=\bigcap_{h=0}^{d}T_{j-h}.          \tag{1.2}
\]

For any antecedent `A` with `D^dA=T`, write

\[
                         Q_x=\{j:x\in A_j\}                    \tag{1.3}
\]

for the source support of coordinate `x`.

## 2. One coordinate is an interval-hitting problem

Unwrap one nonconstant positive run of coordinate `x` as the owner interval

\[
                         [a,b],
 \qquad                  b-a+1\ge d+1.                       \tag{2.1}
\]

Thus `x` is inserted on edge `a-1` and deleted on edge `b`.

### Lemma 2.1 (maximal carrier interval)

The positions at which an antecedent letter may contain `x` are exactly

\[
                         E_x=[a+d,b].                          \tag{2.2}

#### Proof

By (1.2), `x in P_j` exactly when all owners
`T_(j-d),...,T_j` lie in the positive run `[a,b]`.  This is equivalent to
\(a+d\le j\le b\).  Every antecedent satisfies
\(A_j\subseteq P_j\).  \(\square\)

### Theorem 2.2 (bounded-gap support characterization)

A subset \(Q_x\subseteq E_x\) supplies coordinate `x` to every owner in the
run (2.1) if and only if

1. `a+d in Q_x` and `b in Q_x`; and
2. consecutive members of `Q_x`, in increasing order, differ by at most
   `d+1`.

#### Proof

Owner `T_a` can receive `x` only from its source window `[a,a+d]`, whose
intersection with `E_x` is the singleton `{a+d}`.  Likewise the last owner
`T_b` forces position `b`.  This proves the endpoint necessity.

Between two consecutive support positions `u<v`, a source window of length
`d+1` misses both precisely when it can lie strictly between them.  Such a
window exists exactly when `v-u>=d+2`.  Thus every owner window is hit
exactly when every support gap is at most `d+1`.  The forced endpoints deal
with the two boundary windows.  \(\square\)

Constant-one coordinates may be handled by the same statement on the
whole cyclic carrier interval: their support must cyclically hit every
length-`d+1` source window.  Constant-zero coordinates occur nowhere.  The
component-length hypothesis ensures that a block of at most `d` altered
positions never deletes the entire cyclic carrier of a constant-one
coordinate.

## 3. The two forced coordinates of one letter

Define

\[
                         F_j=\{D_j,I_{j-d-1}\}.                \tag{3.1}

The set may have one element when a run has length exactly `d+1`.

### Corollary 3.1 (exact forced-letter set)

Every antecedent `A` with `D^dA=T` satisfies

\[
                         F_j\subseteq A_j\subseteq P_j.        \tag{3.2}

Moreover no coordinate outside `F_j` is forced into position `j` by the
owner equations alone.

#### Proof

Coordinate `D_j` has a positive run ending at owner `j`; Theorem 2.2 forces
its terminal carrier position `j`.  Coordinate `I_(j-d-1)` begins its run
at owner `j-d`; Theorem 2.2 forces the initial carrier position
`(j-d)+d=j`.  This proves the left inclusion, and the right inclusion is
maximality of `P`.

If `x in P_j-F_j`, then `j` is not an endpoint of `E_x`.  Use the maximal
support `E_x` with position `j` deleted.  The only newly created support
gap has size two, at most `d+1`; Theorem 2.2 shows that all owners remain
covered.  Hence `x` is not individually forced at `j`.  \(\square\)

## 4. Altering one block of at most `d` positions

Let

\[
                         B=[c,c+s-1],
 \qquad                  1\le s\le d.                        \tag{4.1}

Choose arbitrary nonempty letters `H_j` on `B` satisfying

\[
                         F_j\subseteq H_j\subseteq P_j.        \tag{4.2}

Outside `B`, retain the maximal letters:

\[
 A_j=
 \begin{cases}
  H_j,&j\in B,\\
  P_j,&j\notin B.
 \end{cases}                                                \tag{4.3}

### Theorem 4.1 (short-block freedom)

The word (4.3) remains a depth-`d` antecedent of `T`:

\[
                         D^dA=T.                              \tag{4.4}

#### Proof

Fix a coordinate run.  Outside `B` its source support remains the complete
carrier interval `E_x`.  Inside `B` some support positions may be removed.
If an endpoint of `E_x` belongs to `B`, condition (4.2) retains it by
Corollary 3.1.  Every new internal gap is bounded by the two nearest retained
carrier positions and crosses at most the `s` altered positions, so its
length is at most `s+1<=d+1`.  Theorem 2.2 shows that every owner containing
`x` is still hit.  Coordinates constant on the cycle obey the same cyclic
gap estimate.  Therefore every owner equation survives.  \(\square\)

The bound `s<=d` is sharp for this argument: deleting a coordinate from
`d+1` consecutive nonforced positions can create a support gap `d+2`.

## 5. Exact two-component common-history criterion

Let `T^(1),T^(2)` be two cyclic `d`-resident simple Johnson traces, with
maximal letters `P_j^(ell)` and forced sets `F_j^(ell)`.  Choose a cut and
orientation on each component, and align `d` consecutive source positions
as

\[
                         j=0,1,\ldots,d-1.                     \tag{5.1}

### Theorem 5.1 (common literal history)

There are antecedents of the two traces whose aligned length-`d` histories
are literally identical if and only if

\[
 \boxed{
 F_j^{(1)}\cup F_j^{(2)}
       \subseteq P_j^{(1)}\cap P_j^{(2)}
 \quad(0\le j<d).}
\tag{5.2}

When (5.2) holds, one may take the common history letters to be

\[
                         H_j=F_j^{(1)}\cup F_j^{(2)}.           \tag{5.3}

#### Proof

Necessity follows from (3.2) in both components: a common letter must
contain both forced sets and lie in both maximal envelopes.

Conversely, (5.2) makes (5.3) a nonempty letter satisfying (4.2) for each
trace.  Apply Theorem 4.1 separately, retaining each trace's maximal
antecedent outside the aligned block.  Both resulting antecedents induce
their original owner components and have the common history (5.3).  \(\square\)

### Corollary 5.2 (zero-position de Bruijn source fusion)

Under (5.2), the two labelled owner components serialize into one cyclic
source word using every owner window once and adding no source position.

#### Proof

Regard each `(d+1)`-letter owner trace as a labelled edge in the order-`d`
de Bruijn graph of literal histories.  Each component antecedent is an
Euler circuit, and the common `d`-history (5.3) is a shared vertex.  Traverse
the first circuit back to that vertex and then the second circuit.  This is
one Euler circuit in their union and uses every labelled owner edge once.
Its spelled cyclic source word has length equal to the sum of the two owner
component lengths, so the fusion has zero positional charge.  \(\square\)

This is a statement about the order-`d` source/de Bruijn graph.  The two
new cross-component adjacencies in the resulting owner order need not be
Johnson edges: their entering and leaving screen letters may differ in more
than one coordinate even though the `d`-history is common.  Consequently
Corollary 5.2 alone does not preserve the selected owner-intersection q1 or
owner-union upper palettes, path topology, or any occurrence guard tied to
the old component edges.  On the other hand, the common-vertex short-deck
fusion theorem proves that the literal source subword multiset through width
`d+1` is preserved exactly; in particular the source-side strict-lower
compiler transports without a separate q1 seam condition.  A guarded
carrier fusion may still need the two cross screens to form the required
typed Johnson transitions (or a separate boundary packet) when those
owner-edge palettes themselves are part of the retained interface.

Thus the bare zero-charge **source** overlap problem has no residual flow or
Hall condition.  After cuts are chosen, it is exactly `d` explicit set
containments.  Source-cell assignments through width `d+1` survive by the
short-deck theorem.  Guarded carrier fusion may still fail because the cross
screens need not be Johnson-compatible and because longer upper witnesses
or typed cap routes can depend on the altered history positions.

## 6. PBBS application boundary

The maximal braid and residual antecedents of the rigid full-rotation
factor share no literal letter under any cuts or rotations, so maximal
histories cannot splice.  Theorem 5.1 identifies the precise nonmaximal
escape: find cuts for which the two event schedules satisfy (5.2).  Both
the braid and residual event rails contain long slope-minus-one segments,
so maximal-letter shape incompatibility does not decide this smaller forced
pair problem.

The next PBBS calculation is therefore finite-symbolic rather than
variational:

1. substitute the explicit braid and residual formulas for `D_j,I_j`;
2. compute \(P_j^{(1)}\cap P_j^{(2)}\) on an aligned `d`-block; and
3. solve the phase congruences imposed by (5.2).

If those congruences have a solution, the bare source histories join at
zero added positions.  If they do not, any successful `O(1)` join must use
a compound boundary packet which changes the owner trace itself.

## 7. Dependencies

The maximal-antecedent criterion is in

`MATH_THEOREM_AD_FAILCLOSED_FLAT_SOURCE_COMPILER_PIPELINE_20260802.md`.

The explicit terminal component event schedules are in

`MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_EXACT_BIRESIDENCE_20260805.md`
and
`MATH_THEOREM_PBBS_RIGID_ROTATION_RESIDUAL_EXACT_RESIDENCE_20260805.md`.

The maximal braid--residual overlap no-go is

`MATH_THEOREM_PBBS_RIGID_ROTATION_MAXIMAL_ANTECEDENT_OVERLAP_NOGO_20260805.md`.
