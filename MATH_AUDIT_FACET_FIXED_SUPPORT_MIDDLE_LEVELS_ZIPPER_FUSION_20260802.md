# Audit of fixed-support Middle-Levels zipper fusion

Date: 2026-08-02  
Status: independent algebraic and finite symbolic audit.  The even-`k`
fixed-support fusion is accepted at owner/q1/residence scope.  The audit
does not promote it to an all-support carrier or a universal word.

## 1. Parameter identity

For `k=2r`, `h=d+1`, and core size `s=r-h-1`, deleting `2h` tags and one
refreshed point leaves

\[
 k-2h-1=2s+1.
\]

Hence the two middle shores on the outside ground have equal cardinality,
and a Middle Levels Hamilton cycle gives every `s`-core exactly once and
every `(s+1)` edge-union exactly once.  This equality is parity-specific:
for odd `k=2r-1`, the outside ground has size `2s`, and there are strictly
fewer `(s+1)`-sets than `s`-sets.  The even proof cannot be copied verbatim.

## 2. Socket arithmetic

With `u_i=i(h-1)` modulo `2h`, the tag halves

\[
 A_i=[u_i,u_i+h-1],\qquad B_i=V-A_i
\]

satisfy

\[
 A_i\cap A_{i+1}=\{u_i+h-1\},
 \qquad B_i\cap B_{i+1}=\{u_i-1\}.
\]

The order

\[
 (u_i,u_i+1,\ldots,u_i+h-1,
  u_i-1,u_i-2,\ldots,u_i+h)
\]

therefore has a wrap input socket and a midpoint output socket whose tags
are cross-positioned exactly as required by the core-change zipper.  The
two sockets are `h` edges apart, so both length-`h` halos are pure before
use.  This is the precise repair of the `L<2h` regeneration obstruction for
the shortest cycles.

## 3. Phase arithmetic

If the type at position zero is `epsilon_i`, the output edge has ordered
phase

\[
 (\epsilon_i+h-1)\to(\epsilon_i+h).
\]

The next input wrap has phase `(1-epsilon_(i+1))->epsilon_(i+1)`.
Setting `epsilon_(i+1)=epsilon_i+h mod 2` makes the tails equal and the
heads equal, hence both cross edges alternate.  Omitting this phase
recursion gives the `P-P/H-H` defect described in the base zipper audit.

## 4. Chronology replay

After all sequential fusions the source blocks have the nested order

\[
 A_0,A_1,\ldots,A_{M-1},
 B_{M-1},B_{M-2},\ldots,B_0.                             \tag{4.1}
\]

A length-`h` window can cross at most one boundary in (4.1), because every
block has length `h`.  At an `A_i|A_(i+1)` or `B_(i+1)|B_i` boundary it is
exactly one of the zipper windows; at the centre and cyclic exterior it is
a pure same-core window.  Thus there is no hidden three-core owner.

A direct symbolic replay was performed for every `2<=h<=9` on eight
successive adjacent cores with distinct edge unions.  For each case all
`16h` owners had rank `r`, all consecutive owner symmetric differences had
size two, all lower colours had rank `r-1`, all upper colours rank `r+1`,
and each of the three rows was injective.  The proof in the theorem is
general; this replay is only an indexing cross-check.

## 5. Collision invariant

Intersecting a named resource with the outside ground `G` gives one of two
types:

\[
 X_i\quad\text{(pure)},
 \qquad R_i=X_i\cup X_{i+1}\quad\text{(mixed)}.
\]

The types have different sizes, the `X_i` are all distinct, and the `R_i`
are all distinct.  This proves all cross-block collision statements except
the endpoint lower colours.  Those endpoint colours are the unique
proper `(h-1)` tag intervals at the socket being deleted; the old occurrence
is removed before the new occurrence is inserted.  The input and output
sockets of a block are different, so their endpoint colours are different.

This invariant is valid only inside one fixed support `V union {beta}`.
Different supports do not share a common outside-trace projection, and
must still be handled by clustered pruning or a new cross-support theorem.

## 6. Scale audit

The fixed-support reservoir has size

\[
 \binom{k-2h-1}{r-h-1}=\Theta(W/2^{2h}).
\]

This is exponentially smaller than the shortest-cycle fixed-support
reservoir, but the number of prospective supports grows by the reciprocal
factor.  Per unfused module the length-`2h` deck still has only
`O(hq)=O(q^2)` cylinders and `(2h+1)^2/k=Theta(1)`, so the scalar
`W/q^2` product count remains plausible.

There is a noncommutation caveat: ordinary clustered pruning deletes
individual modules, while the Middle-Levels fusion uses the complete core
path.  Deleting modules fragments that path.  Treating the entire fused
reservoir as one atom instead creates an `M`-times larger footprint.  Thus
bounded random-support moments alone do not prove a packing of the fused
components.  A path-preserving pruning or absorption theorem is still
needed.

## 7. Verdict

The even-dimensional fixed-support fusion theorem is proof-safe at its
stated scope.  It is the first literal construction in this branch that
simultaneously supplies:

* an adjacent-core connector for every core in a full fixed reservoir;
* regenerated pure `h`-halos after each sequential fusion;
* distinct core-union traces from a Middle Levels Hamilton cycle;
* exact P/H phase compatibility;
* owner/q1 simplicity and residence floor `h`.

It does not settle odd parity, inter-support component count, deeper upper
shadows, or the lower compiler.  Those are the exact remaining rows.
