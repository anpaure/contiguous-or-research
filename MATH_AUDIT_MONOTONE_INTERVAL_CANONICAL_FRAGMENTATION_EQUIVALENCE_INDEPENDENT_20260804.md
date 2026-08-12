# Independent audit: monotone interval canonical fragmentation equivalence

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_MONOTONE_INTERVAL_CANONICAL_FRAGMENTATION_EQUIVALENCE_20260804.md`  
**Audited theorem SHA-256:**
`aa408b20958349cdf7472e23908c7f98d93409cad6e336c6d2730215ef738793`  
**Method:** independent line-by-line pure-mathematical replay and explicit
boundary-counterexample audit; no search, solver, or finite computation  
**Verdict:** **INDEPENDENT-GO after two exact ledger corrections.**  The
colour-passing equivalence, complete length-multiset preservation,
heterogeneous-capacity equivalence, corrected Boolean job ledger,
triangular-deletion monotonicity, and fractional configuration dual are
proof-safe at their stated scope.

The audit corrected:

1. the boxed finite configuration system now explicitly requires every
   fragment length to be at most the maximum socket capacity `D`; and
2. in the nonempty Boolean ideal, the first job multiplicity is
   `{k\choose1}=k`, rather than `{k\choose1}-{k\choose0}=k-1`.

The second correction is the exact one-unit effect of deleting the empty
set from the unique rank-zero symmetric chain.  Neither correction changes
the main equivalence or the remaining fragmentation gate.

## 1. Colour passing at every boundary

At the boundary before position `s`, write `C_s` for the intervals which
continue across the boundary.  Then

\[
 n_{s-1}=|C_s|+|E_s|,
 \qquad
 n_s=|C_s|+|B_s|,
\]

and hence

\[
                    |B_s|-|E_s|=n_s-n_{s-1}\ge0.
\]

Thus every colour released by an ending interval can be passed to a
distinct interval beginning at `s`.  The remaining beginnings receive the
new colours

\[
                    n_{s-1}+1,\ldots,n_s.
\]

If the active colours at `s-1` are `[n_{s-1}]`, the active colours at `s`
are exactly `[n_s]`: continuing intervals retain their colours, passed
colours replace the ending colours, and the excess beginnings carry the
new terminal block.  At `s=1`, there are no ending intervals and the rule
assigns `[n_1]` directly.  This proves the induction without requiring any
genericity of endpoints or distinctness of intervals; duplicate intervals
are simply distinct members of the input multiset.

Colour `a` first appears at

\[
                    s_a=\min\{s:n_s\ge a\}.
\]

Since the active sets `[n_s]` are nested, it remains active at every later
position.  Each time its current interval ends at `s-1`, its successor
begins at `s`.  Its intervals are therefore disjoint adjacent integer
pieces whose union is `[s_a,m]`.  No interval or endpoint is altered.

Conversely, fragmenting the canonical suffixes changes neither their union
nor their pointwise indicators.  Since exactly `n_s` suffixes contain
position `s`, the fragments have coverage vector `n`.  Theorem 1.1 is
exact in both directions.

## 2. Exact length-multiset preservation

The forward colouring partitions the existing intervals by colour and
does not modify them.  Consequently it preserves the full multiset of
their lengths, not merely total length or interval count.  For each colour,
the assigned lengths form a composition of `L_a`.

In the reverse direction, any composition of `L_a` can be placed in its
given order as consecutive pieces of `J_a`.  Hence every aggregate piece
multiset admitted by the canonical jobs gives an interval realization with
that same multiset.  Corollary 1.2 follows exactly.

## 3. Heterogeneous capacity matching

For fixed piece lengths, an injection into the capacity bins exists if and
only if

\[
 \#\{\text{pieces of length at least }q\}
 \le
 \#\{\text{bins of capacity at least }q\}
 \qquad(q\ge1).
\tag{3.1}
\]

Necessity is immediate.  For sufficiency, sort both lists decreasingly.  If
the `j`-th piece exceeded the `j`-th capacity, then at the threshold equal
to that piece length the left side of (3.1) would be at least `j` and the
right side at most `j-1`.  Therefore the sorted assignment is feasible.

Applying the colour-passing theorem to a capacity-compatible interval
realization retains its original injective bin assignment and yields
capacity-compatible compositions of all canonical jobs.  Conversely,
placing those compositions consecutively in the suffix jobs and retaining
their injected bin assignments gives the required interval realization.
Theorem 2.1 is exact.

### The overlong-piece correction

Before correction, the boxed system checked (3.1) only for `q<=D` but did
not state `ell<=D`.  The following one-line example passed that truncated
system incorrectly:

\[
 n=(1,1,1),\qquad L_1=3,qquad W=1,qquad c_1=D=2.
\]

The illegal one-part composition `(3)` obeys both displayed tail rows
`q=1,2`, yet no capacity-two bin accepts it.  The corrected theorem requires

\[
                     1\le\ell_{a,j}\le D,
\]

or equivalently extends (3.1) to all `q` with `K_q=0` above `D`.  With this
correction, the finite integer system is precisely equivalent to the
heterogeneous injection problem.

## 4. Exact Boolean job multiplicities

For the nonempty residual histogram

\[
 n_s={k\choose s},\qquad1\le s<t_0,
\]

the interval theorem uses `n_0=0`.  Therefore the number of jobs first
appearing at rank `b` is

\[
 \begin{cases}
 {k\choose1}=k,&b=1,\\[1mm]
 {k\choose b}-{k\choose b-1},&2\le b<t_0,
 \end{cases}
\]

and every such job has length `t_0-b`.

The originally stated value `k-1` at `b=1` would give only `k-1` rows
covering a first column of height `k`, so it could not be exact.  The SCD
interpretation gives the same correction.  Every SCD has one chain
beginning at the empty set and `k-1` chains beginning at rank one.  After
restriction below `t_0` and deletion of the empty set, the first chain has
length `t_0-1`, just like the rank-one chains.  Hence there are exactly `k`
jobs of that length.  At ranks `b>=2`, the usual symmetric-chain
multiplicity is unchanged.

If the empty set is retained, one instead has one bottom-zero job of
length `t_0` and the usual difference multiplicities at every positive
bottom rank.  The corrected theorem records both conventions and no longer
hides this finite unit as an asymptotic error.

## 5. Monotonicity after triangular deletions

Let

\[
                    \Delta_s={k\choose s}-{k\choose s-1}.
\]

For positive `Delta_s`, direct cancellation of adjacent binomial ratios
gives

\[
 {\Delta_{s+1}\over\Delta_s}\ge1
 \quad\Longleftrightarrow\quad
                    (k-2s)^2\ge k+2.
\tag{5.1}
\]

On the range needed to compare residual gaps,
`s<=t_0-2=r-D-2`.  Thus `k-2s` is at least `2D+3` in odd dimension and
`2D+4` in even dimension.  Since

\[
                    D^2=(\pi/8+o(1))k,
\]

condition (5.1) holds strictly for every sufficiently large `k`.  The
relevant positive gaps are therefore bounded below by
`Delta_1=k-1`.

If `B=sum_s b_s<=D(D+1)/2`, then for `s>=2`,

\[
 n_s-n_{s-1}
 =\Delta_s-b_s+b_{s-1}
 \ge(k-1)-B>0,
\]

because

\[
                    B=(\pi/16+o(1))k<k-1.
\]

At the first nonempty rank the correct convention is instead

\[
                    n_1-n_0=k-b_1\ge k-B>0.
\]

Thus arbitrary triangular deletions of the stated total size preserve
nondecreasingness for all sufficiently large `k`.  This proves only that
the canonical-fragmentation theorem remains applicable; it does not prove
the integer configuration system feasible.

## 6. Fractional configuration dual

For a job of length `L`, a socket-type vector
`p=(p_1,...,p_D)` is usable when

\[
                    \sum_{q=1}^D qp_q\ge L.
\]

One may restrict to vectors using at most `L` sockets.  If a cover uses
more, retain any `L` sockets; every capacity is at least one, so they still
cover `L`.  Conversely, if a cover has at most `L` sockets and total
capacity at least `L`, give each socket one unit and distribute the
remaining units within the aggregate spare capacity.  It therefore
corresponds to an actual positive integer fragmentation of the job.

Let `P_L` be the resulting finite configuration set.  A fractional
configuration packing exists exactly when the exact-capacity supply vector
`K^=` belongs to

\[
       \sum_a\operatorname{conv}(P_{L_a})+\mathbb R_{ge0}^D.
\tag{6.1}
\]

The set in (6.1) is a closed upward polyhedron.  Its separating normals may
be taken nonnegative.  For a fixed nonnegative normal `theta`, minimization
over the Minkowski sum separates by job and yields

\[
 \sum_a\min_{p\in P_{L_a}}\theta\mathbin{\cdot}p
 =\sum_a\psi_\theta(L_a).
\]

Therefore (6.1) holds if and only if

\[
 \sum_a\psi_\theta(L_a)
 \le\sum_{q=1}^D K_q^{=}\theta_q
 \qquad\text{for every }\theta\ge0.
\]

This verifies both necessity for every integral fragmentation and
sufficiency for the explicitly stated **fractional configuration LP**.  It
does not assert integrality of that LP.  The theorem correctly leaves a
possible integer residue absorber as an additional requirement.

## 7. Scope and surviving gate

The corrected theorem proves an anonymous rank-length equivalence:

\[
 \text{heterogeneous interval rows}
 \quad\Longleftrightarrow\quad
 \text{fragmented canonical suffix jobs}.
\]

On the complete nondecreasing Boolean layers, or when deletions and names
are selected adaptively, the cited normalized-matching theorem lifts an
interval schedule to named skipless Boolean chains.  This does not apply to
arbitrarily frozen punctured layers or prescribed physical socket roots;
those still require the named Hall ladder.  It also does not provide a
literal run serialization, owner chronology, upper deck, or a solution of
the integer fragmentation system itself.

Accordingly, the theorem safely identifies the remaining rank-only gate
but does not claim to close it.  **INDEPENDENT-GO at this corrected scope.**
