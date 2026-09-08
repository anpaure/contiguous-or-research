# One full-context cache resets a PBBS split history, but adjacent heights overlap

**Date:** 2026-08-13  
**Status:** unconditional source/owner algebra for one isolated split
interface and an unconditional no-go for superposing these particular
caches on consecutive role-zero height-spine interfaces.  The cache repairs
the previously missed strict-lower cells which continue beyond the right
screen.  It does not by itself give an all-height role-zero replacement.

## 1. Abstract old fragment

Let the owner rank be `R` and the source depth be `d>=2`.  Let

\[
 I=(I_1,\ldots,I_d)
\tag{1.1}
\]

be an ordered nonempty partition of a rank-`R-2` set `H`.  Let `X,Y` be
two-element screens disjoint from `H`, and suppose

\[
 D=H\mathbin{\dot\cup}Y
\tag{1.2}
\]

is the old right endpoint owner.  Write the complete old right source
context as

\[
 (I_1,I_2,\ldots,I_d,Y,Q_1,Q_2,\ldots).
\tag{1.3}
\]

The first owner after `D` is

\[
 R_1=I_2\cup\cdots\cup I_d\cup Y\cup Q_1.
\tag{1.4}
\]

Because `D R_1` is a Johnson edge, there are unique labels

\[
 x\in I_1,\qquad z\in Q_1
\tag{1.5}
\]

such that

\[
 R_1=D-\{x\}+\{z\}.
\tag{1.6}
\]

In particular, every other member of `I_1` is absent from `Q_1`: equality
of the two rank-`R` sets in `(1.4)--(1.6)` forces

\[
 I_2\cup\cdots\cup I_d\cup Y=D-I_1,
 \qquad Q_1=(I_1-\{x\})\cup\{z\}.
\tag{1.7}
\]

Choose a fresh coordinate

\[
 p\notin D\cup\{z\}
\tag{1.8}
\]

and put

\[
 F=(I_1-\{x\})\cup\{p\}.
\tag{1.9}
\]

The replacement source fragment is

\[
 \boxed{(F,I_2,\ldots,I_d,Y,Q_1,Q_2,\ldots).}
\tag{1.10}
\]

Since every `I_j` is nonempty, `F` is nonempty even when `I_1={x}`: in
that case `F={p}`.

## 2. Exact owner and immediate-palette algebra

The first owner of `(1.10)` is

\[
 V=F\cup I_2\cup\cdots\cup I_d\cup Y
   =D-\{x\}+\{p\}.
\tag{2.1}
\]

The next owner is

\[
 I_2\cup\cdots\cup I_d\cup Y\cup Q_1=R_1,
\tag{2.2}
\]

and every later owner is literally the corresponding old right-context
owner.  Thus `V R_1` is a Johnson edge with

\[
 V\cap R_1=D-\{x\},
\tag{2.3}
\]

which is exactly the old lower facet

\[
 D\cap R_1=D-\{x\}.
\tag{2.4}
\]

The immediate upper target is not preserved:

\[
 D\cup R_1=D\cup\{z\},
\tag{2.5}
\]

whereas

\[
 V\cup R_1=(D-\{x\})\cup\{p,z\}.
\tag{2.6}
\]

For fresh `p` the two values are different.  Hence the cache carries one
named immediate-upper casualty; it must be backed up separately.  There is
no choice `p=x`, because that would give `V=D` and would not reset the
history or separate the endpoint owner.

## 3. Exact complete-right-context transport

Consider the old local source fragment

\[
                         (X,I_1,\ldots,I_d,Y,Q_1,Q_2,\ldots).
\tag{3.1}
\]

### Theorem 3.1 (right-crossing cells copy literally)

Every strict-lower interval of `(3.1)` which meets `Y` and may continue
arbitrarily far into `(Q_1,Q_2,...)` begins at one of

\[
                         I_s\quad(2\le s\le d),
 \qquad\text{or at }Y,Q_1,Q_2,\ldots .
\tag{3.2}
\]

Consequently it occurs literally, with the same width and exact OR value,
inside the cache fragment `(1.10)`.

#### Proof

An interval which begins at `I_1` or earlier and meets `Y` contains

\[
 I_1\cup\cdots\cup I_d\cup Y=D,
\]

which has rank `R`; it is not strict-lower.  Thus every strict-lower
interval meeting `Y` begins strictly after `I_1`, giving `(3.2)`.  From
`I_2` onward, `(1.10)` and `(3.1)` are the same literal source word, so the
same physical subword has the same width and OR.  This includes intervals
ending beyond `Y`; no truncation at the screen is being assumed. \(\square\)

Left-screen intervals and history-only intervals may be copied on an
independent left half-block `(X,I_1,...,I_d,Z)`, exactly as in the split
common-history theorem.  The two physical fragments are disjoint.  Hence,
for one isolated interface, the left half-block together with `(1.10)`
gives an occurrence-injective exact-value transport of the complete old
strict-lower deck, including all right-context crossings.

This corrects the shorter cache
`(F,I_2,...,I_d,Y,G)`: that block copied only intervals ending at `Y` and
did not justify transport of intervals continuing into the old residual
path.

## 4. A genuine input/output history reset

The cache uses the old input history `I` only in its transported cells.
The separate terminal palette half-block may use any ordered nonempty
partition

\[
                         O=(O_1,\ldots,O_d)
\tag{4.1}
\]

of the same current core.  Thus a local owner path can have the form

\[
 B\ \leadsto\ V-R_1-(\text{old residual continuation})
\tag{4.2}
\]

on the transported right branch, while the palette chain exits through an
independent terminal half-block having history `O`.  Algebraically, this is
a genuine reset from input history `I` to output history `O`; the queue
shift recurrence is no longer imposed inside this isolated macro.

The source conclusion is prospective.  To make `(1.10)` a literal
antecedent block, the arm entering `V` must expose
`(F,I_2,...,I_d)` in its final `d` source positions and meet all forced
envelope containments.  Coordinate `p` must be inserted exactly `d` owner
edges before `V` and is deleted on `V R_1`, giving its required positive
run of length `d+1`.  Its surrounding zero gaps, and all other clipped
flags, must be passed to the two-sided long-arm scheduler.  The algebra
above does not construct that simultaneous envelope/event order.

Fresh `p` gives a private endpoint signature.  It separates `V` from the
old all-tag bank, provided the entering tagged arm uses the same declared
private signature.  The old continuation after `V` does not contain `p`,
so no later resource is silently renamed.

## 5. Exact adjacent-height overlap obstruction

Now specialize to the literal role-zero PBBS height spine.  Write

\[
                         D_h=U_{h+1}
\tag{5.1}
\]

for the right endpoint owner of the split at height `h`; this notation is
distinct from source deletion labels.  Its first old right-context owner is

\[
                         R_{h,1}=U_{h+2},
\tag{5.2}
\]

because the next role-zero spine edge is `U_{h+1}U_{h+2}`.

The height-`h` cache therefore replaces that next spine edge by

\[
                         V_h-U_{h+2}.
\tag{5.3}
\]

But the split macro at height `h+1` has its terminal palette half-edge

\[
                         C_{h+1}-U_{h+2}.
\tag{5.4}
\]

If both macros are installed, owner `U_{h+2}` is incident with both
`(5.3)` and `(5.4)` and also must connect onward to the next protected
piece unless that incidence is deleted.  In the intended continuous
degree-two palette chain, its two incidences are already prescribed by the
adjacent split macros.  Adding `(5.3)` gives degree at least three.

### Theorem 5.1 (adjacent-cache no-go)

The full-context cache `(1.10)` cannot be superposed independently at two
consecutive role-zero height-spine interfaces while retaining the adjacent
terminal palette half-edges in one simple two-factor.  The right contexts
are nested through the next shared spine owner; they are not private
residual paths.

Thus the cache theorem is proof-safe for one isolated height, or for a
family whose moved right contexts are genuinely private and owner-disjoint.
It is not an all-height construction.  A global use requires either

1. a different pentagon role whose complete moved context is private from
   the next selected height interface; or
2. one compound overlap macro which absorbs the cache edge and both
   adjacent palette incidences into a single degree-two path.

## 6. Aggregate graph-level accounting and boundary

For `H=O(d)` isolated/nonoverlapping caches, the explicit immediate-upper
casualty bank has size `O(H)`.  After full-union shields, the remaining
one-cut exterior values are indexed by a suffix-chain/prefix-chain product;
at each rank the fixed-rank antichain bound gives `O(HR)` distinct targets.
The rank-stratified backup theorem can protect this polynomial target bank
at the owner/incidence level, with sub-half exposure, before factor
completion.

This graph-level census does not repair the adjacent-height obstruction and
does not prove:

* simultaneous source-envelope planting of all cache/arm blocks;
* zero-gap residence across all seams;
* a degree-two compound overlap macro for consecutive heights;
* a resident antecedent for arbitrary completion cycles;
* an upper-safe linear opening; or
* the final typed/common-cap condition.

The exact gain is narrower but useful:

\[
 \boxed{
 \text{one isolated history reset}
 +\text{complete strict-lower context transport}
 +\text{old lower palette}
 -\text{one named upper value}.}
\]
