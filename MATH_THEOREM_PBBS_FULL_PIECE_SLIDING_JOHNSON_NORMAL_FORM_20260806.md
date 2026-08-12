# Consecutive full PBBS pieces are exactly sliding Johnson-union runs

**Date:** 2026-08-06  
**Method:** literal interval-union recurrence  
**Status:** unconditional local normal form and an explicit arbitrarily long
support-first chart.  This proves that full SCD pieces need not be isolated
or reset one at a time.  A single common-core star word serializes up to
\(n-s+1\) consecutive full pieces with no cover defect.  It does not
partition the named Boolean layers into such stars or place the stars in one
PBBS owner envelope.

## 1. Full endpoint charts

Let

\[
                         A=(A_i)_{i\in\mathbb Z}
\]

be a word of nonempty subsets of an \(n\)-set.  For an endpoint \(i\) put

\[
                 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i,
                 \qquad1\le j\le d.                 \tag{1.1}
\]

Call endpoint \(i\) a **full rank-\(s\) endpoint** when

\[
                         |Z_{i,j}|=s+j-1
                         \qquad(1\le j\le d).         \tag{1.2}
\]

Thus its complete endpoint chain is a saturated chain through the rank slab
\(s,\ldots,s+d-1\).

### Theorem 1.1 (sliding-union normal form)

For any run of full rank-\(s\) endpoints, put

\[
                              B_i:=Z_{i,1}=A_i.        \tag{1.3}
\]

Then

\[
 \boxed{
 Z_{i,j}=B_{i-j+1}\cup\cdots\cup B_i,
 \qquad |B_{i-j+1}\cup\cdots\cup B_i|=s+j-1.}       \tag{1.4}
\]

In particular, at two consecutive full endpoints,

\[
                         |B_{i-1}\cup B_i|=s+1.       \tag{1.5}
\]

If their bottom targets are distinct, they are adjacent in the Johnson
graph \(J(n,s)\).  More generally, when the window in (1.4) is extended
one step to the left, the new bottom target contributes exactly one new
coordinate:

\[
 \left|B_{i-j}\setminus
        (B_{i-j+1}\cup\cdots\cup B_i)\right|=1
                         \qquad(1\le j<d).             \tag{1.6}
\]

Conversely, any sequence of rank-\(s\) sets \((B_i)\) satisfying the
second equality in (1.4) becomes a literal run of full pieces by taking
\(A_i=B_i\).

#### Proof

Equation (1.3) is the singleton case of (1.1), and substituting it into
(1.1) gives the first equality in (1.4).  The second equality is exactly
(1.2).  At \(j=2\), two distinct rank-\(s\) sets with union rank \(s+1\)
have intersection rank \(s-1\), proving Johnson adjacency.

The union of the last \(j\) bottom targets has rank \(s+j-1\), while the
union after adjoining \(B_{i-j}\) has rank \(s+j\).  Their set difference
therefore has size one, which is (1.6).  The converse follows by reading
the same equalities backward. \(\square\)

This theorem is stronger than chain consistency inside independently
assigned endpoint chains.  It identifies the exact cross-endpoint row:
full pieces occur in sliding Johnson-union runs.

## 2. A literal common-core star run

Choose

\[
                         Q\in{[n]\choose s-1}
\]

and distinct labels

\[
                         z_0,z_1,\ldots,z_{L-1}
                         \in[n]\setminus Q,            \tag{2.1}
\]

where

\[
                         d+1\le L\le n-s+1.            \tag{2.2}
\]

Read the indices modulo \(L\), and define the cyclic source word

\[
                         B_i=Q\cup\{z_i\}.              \tag{2.3}
\]

### Theorem 2.1 (cyclic star packet)

Every endpoint of (2.3) is a full rank-\(s\) endpoint.  More precisely,

\[
 \boxed{
 Z_{i,j}=Q\cup\{z_{i-j+1},\ldots,z_i\},
 \qquad |Z_{i,j}|=s+j-1}                                \tag{2.4}
\]

for \(1\le j\le d\).  All \(Ld\) displayed targets are distinct:
at a fixed depth they are distinct cyclic intervals of the labelled
\(L\)-cycle, while targets at different depths have different ranks.

Consequently (2.3) is one literal support-first interval chart containing
\(L\) consecutive full pieces and exactly \(L\) different targets in each
rank

\[
                         s,s+1,\ldots,s+d-1.            \tag{2.5}
\]

It has no negative-cover defect and needs no unused endpoint between its
pieces.

#### Proof

Take the union of \(j\) consecutive letters in (2.3).  Their common core
is \(Q\), and their private labels are the \(j\) distinct cyclic labels in
(2.4).  This proves the equality and rank statement.  Since \(j<L\), two
different cyclic intervals of length \(j\) in a cycle of distinct labels
cannot have the same set: their complements have a nonempty boundary, and
the start is recovered as the unique member whose predecessor is outside
the interval.  Different \(j\)'s give different cardinalities.  Literal
realizability makes every coordinate-cover inequality automatic.
\(\square\)

### Corollary 2.2 (linear packet)

If

\[
                         L+d-1\le n-s+1,
\]

the same construction on a linear list of \(L+d-1\) distinct private
labels gives \(L\) consecutive full endpoints.  Alternatively, cutting a
cyclic length-\(L\) packet and discarding its first \(d-1\) endpoints leaves
\(L-d+1\) full linear endpoints.  Thus wrap voltage is not essential; a
star packet can be used as a protected linear chart with the stated
boundary loss.

## 3. Relation to the theta reset deficit

The full-piece reset theorem shows that a private extra endpoint for every
full piece fails by

\[
                         (2\sigma-1+o(1))W.             \tag{3.1}
\]

Theorem 2.1 proves that the missing shared serialization is locally
possible at arbitrary length.  Taking the largest packet in (2.2), one
packet can group

\[
                         n-s+1=\Theta(n)                 \tag{3.2}
\]

full pieces without any reset endpoint.  Therefore the raw number of star
packets needed to absorb the theta deficit is only

\[
                         O(W/n).                         \tag{3.3}
\]

This is Catalan scale rather than endpoint scale.

Equation (3.3) is only a count.  Distinct star packets can share bottom or
higher targets, and the fixed PBBS maximal envelopes need not contain the
common cores \(Q\) on the desired physical intervals.  The exact remaining
star-factor theorem is:

> Select a target-disjoint family of common-core star packets covering at
> least \((2\sigma-1+o(1))W\) full pieces, and place them in the varying
> PBBS envelopes with one owner-compatible Euler order.

If proved, the remaining full pieces could receive the private reset
endpoints counted by the theta theorem.  This would close the full-piece
part of merged serialization; short pieces and the global compiler would
still require their own protected matching.

## 4. Scope

The normal form and star packet are exact literal constructions.  They do
not assert the star-factor theorem, target-disjoint global packing,
compatibility with a prescribed PBBS owner chronology, or an additive
constant upper bound.
