# The native hook low-target problem is an explicit budgeted core-path language

**Date:** 2026-08-06  
**Method:** exact hook root/core recurrence and mandatory-core thinning;
no search  
**Status:** unconditional equivalence for direct core-only interval tickets.
The proposed universal hook-interval covering statement in Section 6 is
now refuted by
`MATH_THEOREM_PBBS_FULL_HOOK_ENVELOPE_TOKEN_SLIDE_AND_THREE_DIMER_OBSTRUCTION_20260806.md`:
a rank-six three-dimer target has zero hook-interval degree.  The present
note remains the exact language reduction; a mixed-component or
parity-changing extension is required for all low targets.

## 1. Consecutive hook cells

Use

\[
 n=2m+1,
 \qquad h=d+1,
 \qquad p=2d+1,
 \qquad b=m-d-1.
\tag{1.1}
\]

Take `ell` consecutive source positions on a height-`h` hook component.
Let their terminal occupancies be

\[
                         z_0,\ldots,z_{\ell-1}\ge0
\tag{1.2}
\]

and let `q_i` be the physical root at the `i`-th position.  The exact hook
recurrence and mandatory core are

\[
 q_{i+1}=q_i-(2z_i+1),
 \qquad
 F_i=\{q_i,q_i-2z_i\}
     =\{q_i,q_{i+1}+1\}.
\tag{1.3}
\]

Therefore the union of the mandatory cores is

\[
 \boxed{
 M(q_0;z_0,\ldots,z_{\ell-1})
 =\{q_0,\ldots,q_{\ell-1}\}
  \cup\{q_1+1,\ldots,q_\ell+1\}.}
\tag{1.4}

Repeated values are automatically coalesced because (1.4) is a set.

## 2. Exact realization of every budgeted core word

### Theorem 2.1 (hook core-language realization)

Suppose

\[
                         1\le\ell\le d,
 \qquad
                         \sum_{i=0}^{\ell-1}z_i\le b.
\tag{2.1}

Then for every starting coordinate `q_0`, the canonical PBBS factor has a
height-`d+1` hook component containing `ell` consecutive source positions
whose terminal occupancies are (1.2), roots are given by (1.3), and
mandatory-core union is (1.4).

Moreover that source interval can be thinned to its mandatory cores,

\[
                         A_i=F_i,
\tag{2.2}

while all other positions retain their maximal-envelope letters.  The
owner row remains exact and the selected source interval has literal union

\[
                         \bigcup_{i=0}^{\ell-1}A_i=M.
\tag{2.3}

#### Proof

Place the entries `z_0,...,z_(ell-1)` consecutively in a `p`-slot hook
weak composition and distribute the remaining

\[
                         b-\sum_i z_i
\]

arbitrarily among the other `p-ell` slots.  The hook slot-rotation theorem
then supplies the desired consecutive phases, and the physical root can
be placed at `q_0` by coordinate rotation.  Equations (1.3)--(1.4) are the
exact rooted hook identities.

The changed source bank is one block of length `ell<=d`, and every new
letter equals its mandatory core.  Short-gap localization gives
`D^dA=T`; (2.3) is immediate.  `square`

The theorem proves one occurrence.  A simultaneous atlas additionally
needs distinct-component or short-block Hall selection.  When substantial
mass remains outside the prescribed segment the unused slots give a large
weak-composition menu, but no uniform multiplicity claim is made here for
the saturated case `sum z_i=b`.

## 3. Static path formulation

Define the directed hook graph `K_b` on `Z_n` by

\[
 q\longrightarrow q'
 \quad\Longleftrightarrow\quad
 q'=q-(2z+1)
 \text{ for some }0\le z\le b.
\tag{3.1}

Give this arc cost `z` and secondary endpoint `q'+1`.

A length-`ell` directed path

\[
                         q_0\to q_1\to\cdots\to q_\ell
\tag{3.2}

of total cost at most `b` emits the set

\[
                         \{q_0,\ldots,q_{\ell-1}\}
 \cup\{q_1+1,\ldots,q_\ell+1\}.
\tag{3.3}

Theorem 2.1 gives the exact equivalence:

### Corollary 3.1 (direct ticket criterion)

A target `S` has a native core-only hook ticket of width at most `d` if
and only if there is a path (3.2), of length at most `d` and cost at most
`b`, whose emitted set (3.3) is exactly `S`.

The forward implication reads the terminal occupancies of the ticket; the
reverse implication is Theorem 2.1.

This criterion has no hidden owner, q1, upper, or action-angle variable.

## 4. Envelope-assisted version

Core equality is sufficient but not necessary.  Let `P_i` be the maximal
envelope at the path positions.  A target `S` can be realized on the same
source interval whenever

\[
 M\subseteq S\subseteq\bigcup_{i=0}^{\ell-1}P_i
\tag{4.1}

and every `x in S` can be assigned to at least one `i` with `x in P_i`.
The latter assignment is tautological under the right inclusion: put each
extra coordinate into one envelope letter containing it.  More explicitly,
choose sets

\[
 F_i\subseteq A_i\subseteq P_i,
 \qquad
 \bigcup_iA_i=S.
\tag{4.2}

Then the same short-block proof gives `D^dA=T`.

Thus the exact general hook-interval criterion is

\[
 \boxed{
 \exists\text{ budgeted path of length }\le d:
 M\subseteq S\subseteq\bigcup_iP_i.}
\tag{4.3}

The only PBBS data left in the envelope-assisted version are the explicit
hook survivor envelopes along that path.

## 5. Calibrations already closed

* If every `z_i=0`, then `q_i=q_0-i` and (3.3) is one consecutive
  coordinate interval.  This is the one-pile complete consecutive atlas.
* For `ell=1,z_0=1`, (3.3) is a distance-two pair.
* For `ell=2,z_0=z_1=0`, (3.3) is an adjacent pair.
* Zero-terminal one-cell envelopes add every pair of distance at least
  three.

Together these give all ranks one and two and every one-run target through
rank `d`.

## 6. The formerly proposed all-low statement is false

Let `mathcal S_(<=d)` be the nonempty subsets of `Z_n` of size at most
`d`.  The natural pure combinatorial target was:

> **Budgeted hook interval covering.**  Every `S in mathcal S_(<=d)` has
> a path satisfying (4.3), and these paths admit a component-disjoint Hall
> selection from the exponentially large hook angle bank.

The direct form replaces (4.3) by equality in (3.3); the envelope-assisted
form is weaker.  Both universal statements are false.  The exact
full-envelope update is an oriented one-token slide.  Every maximal dimer
forces its own slide, and an odd outgoing dimer must terminate the
interval.  The target

```
{0,-1,-4,-5,-8,-9}
```

has two odd outgoing dimers and therefore no path satisfying (4.3).  The
component Hall graph already has a zero-degree left vertex.

The scalar budget is nevertheless ample for parity-compatible targets:
skipping the largest run gap pays the full cost with linear margin.  The
corrected remaining statement must enlarge the right shore by a second
action partition, a protected multi-hook seam, or a parity-changing
packet.
