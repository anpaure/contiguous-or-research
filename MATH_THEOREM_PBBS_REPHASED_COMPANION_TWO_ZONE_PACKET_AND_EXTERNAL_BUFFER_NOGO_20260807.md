# Rephased PBBS companions have an exact two-zone chart, but require an external buffer endpoint

**Date:** 2026-08-07  
**Method:** explicit sliding-window source words, suffix-union recurrence,
and the central-owner rank aperture  
**Status:** unconditional local construction and unconditional global scope
correction.  Endpoint separation really does remove the adjacency
obstruction at the lower-target level: an arbitrary fixed-remainder bank
of rephased companion chains has an explicit target-disjoint two-zone
literal chart.  However, no cyclic serialization using only those lower
and upper companion endpoints can satisfy the PBBS owner row.  Every upper
companion requires a distinct external successor endpoint and a distinct
lag-\(d\) owner-buffer slot carrying \(d+1\) fresh coordinates.  Thus the
adaptive-phase theorem must be proved by a correlated recoupling with the
background reset/piece bank, not by a closed permutation of the rephased
companions alone.

The packet chains have exactly the eligible rank profile, but the theorem
does not assert that a positive-density family of such packets extends to
one global SCD.  This theorem also does not refute the adaptive-phase
merged PBBS chart theorem.
The ordinary merged ledger contains many more background reset endpoints
than the theta-sized rephased bank.  It identifies the exact resources
that those endpoints must provide.

## 1. Parameters and the two companion rank intervals

Use

\[
 n=2m+1,\qquad t=m-d,
\]

and fix a remainder

\[
 2\le r\le d-2,\qquad h=r+1.
\]

An eligible SCD segment has ranks

\[
 t-d-r,t-d-r+1,\ldots,t-1.
\]

After the one-rank phase shift it is split into

\[
 \mathcal L:\quad t-d-r,\ldots,t-d
\tag{1.1}
\]

of length \(h=r+1\), and

\[
 \mathcal U:\quad t-d+1,\ldots,t-1
\tag{1.2}
\]

of length \(d-1\).  In the abstract endpoint injection, \(\mathcal U\)
must occupy suffix depths \(2,\ldots,d\).  The lower piece may occupy any
\(h\) consecutive suffix depths.

Put

\[
 c=t-d-r-1.
\tag{1.3}
\]

For all sufficiently large parameters \(c\ge0\).

## 2. Explicit separated companion packet

Choose a core \(K\) of size \(c\), and choose a cyclically ordered private
bank

\[
 Z=(z_i)_{i\in\mathbb Z/L\mathbb Z}
\]

of distinct coordinates, disjoint from \(K\), where

\[
 L>r+d.
\tag{2.1}
\]

Define two cyclic source components:

\[
 A_i^-=K\cup\{z_i\},
\tag{2.2}
\]

and

\[
 A_i^+=K\cup\{z_{i-r},z_{i-r+1},\ldots,z_i\}.
\tag{2.3}
\]

For cyclic private intervals write

\[
 Z[a,b]=\{z_a,z_{a+1},\ldots,z_b\}.
\]

### Theorem 2.1 (two-zone companion chart)

For every \(i\), the lower component at endpoint \(i\) supplies

\[
 \bigcup_{q=0}^{j-1}A^-_{i-q}
 =K\cup Z[i-j+1,i]
 \qquad(1\le j\le h),
\tag{2.4}
\]

and the upper component at endpoint \(i\) supplies

\[
 \bigcup_{q=0}^{j-1}A^+_{i-q}
 =K\cup Z[i-r-j+1,i]
 \qquad(2\le j\le d).
\tag{2.5}
\]

For a fixed endpoint \(i\), the targets in (2.4)--(2.5) form one strict
saturated chain through exactly the ranks

\[
 t-d-r,t-d-r+1,\ldots,t-1.
\tag{2.6}
\]

All targets displayed over all endpoints are pairwise distinct.  Thus the
two components give \(L\) target-disjoint saturated segments of the exact
eligible SCD shape, with their
rephased lower and upper pieces realized literally and with no coordinate
cover defect internal to either component.

#### Proof

Equation (2.4) is the union of \(j\) private singletons and the common
core.  In (2.5), the union of \(j\) consecutive private windows of length
\(r+1\) is the private interval of length \(r+j\) ending at \(i\).

The private lengths in (2.4) are \(1,\ldots,r+1\); those in (2.5) are
\(r+2,\ldots,r+d\).  Since \(|K|=t-d-r-1\), their ranks are exactly
(2.6).  Condition (2.1) makes every displayed private interval proper.
At a fixed private length, its cyclic endpoint is recoverable, so two
different \(i\)'s give different targets.  Different lengths give
different ranks.  Finally (2.2)--(2.3) are explicit source words, so their
assigned interval values automatically satisfy every coordinatewise
positive/negative cover cut. \(\square\)

The top target of the lower piece is

\[
 D_i=K\cup Z[i-r,i]=A_i^+,
\tag{2.7}
\]

and the bottom target of the upper piece is

\[
 D_i\cup\{z_{i-r-1}\}.
\tag{2.8}
\]

Thus the two zones are not an arbitrary matching: the source letter in the
upper zone is literally the top lower target from its companion chain.
This is the simplest exact separated history one could ask for.

Linear packets follow by opening the two cycles and discarding the
\(O(d+r)\) boundary endpoints whose suffix windows cross a cut.  Hence the
adjacency no-go is not a target-history no-go; it is a host/owner no-go.
Extending many such prescribed segments to one global SCD, or replacing
the SCD by an equally exact residual chain factor, remains a separate
target-packing condition.

## 3. Two consecutive upper companions violate the owner rank

For a source word \(A\), write

\[
 Z_{e,j}=A_{e-j+1}\cup\cdots\cup A_e.
\]

The PBBS owner equation at endpoint \(e\) is

\[
 |Z_{e,d+1}|=m.
\tag{3.1}
\]

An upper companion endpoint has

\[
 |Z_{e,j}|=t-d+j-1
 \qquad(2\le j\le d).
\tag{3.2}
\]

### Lemma 3.1 (upper--upper adjacency is impossible)

Two consecutive physical endpoints cannot both carry upper companion
pieces.

#### Proof

Suppose \(e-1\) and \(e\) are both upper endpoints.  Put

\[
 M=Z_{e-1,d-1}=A_{e-d+1}\cup\cdots\cup A_{e-1}.
\]

By (3.2), \(|M|=t-2\).  The two top targets are

\[
 Z_{e-1,d}=M\cup A_{e-d},
 \qquad
 Z_{e,d}=M\cup A_e,
\]

and each has rank \(t-1\).  Therefore each adds exactly one coordinate to
\(M\).  Their union is the owner window:

\[
 Z_{e,d+1}=Z_{e-1,d}\cup Z_{e,d}.
\]

It has rank at most \(t\), whereas the PBBS owner rank is
\(m=t+d>t\).  This contradicts (3.1). \(\square\)

This proof uses only the assigned upper ranks, not their target labels.

## 4. An upper companion cannot be followed by a lower companion

Assign a lower remainder-\(r\) piece to suffix depths

\[
 a+1,\ldots,a+h,
 \qquad 0\le a\le d-h.
\tag{4.1}
\]

At its depth \(j\), the prescribed rank is

\[
 t-d-r+j-a-1.
\tag{4.2}
\]

### Lemma 4.1 (upper--lower rank descent)

For \(r\ge2\), an upper companion endpoint cannot be immediately followed
by any lower remainder-\(r\) companion endpoint, regardless of whether the
two pieces came from the same SCD chain.

#### Proof

Let the upper endpoint be \(e-1\) and the lower endpoint \(e\).  Because
\(h=r+1\ge3\), the lower depth interval in (4.1) contains some

\[
 j\in[3,d].
\]

The suffix recurrence gives

\[
 Z_{e-1,j-1}\subseteq Z_{e,j}.
\tag{4.3}
\]

But the left side, being an upper target, has rank

\[
 t-d+j-2,
\]

while (4.2) gives the right-side rank

\[
 t-d-r+j-a-1.
\]

Their difference, right minus left, is

\[
 1-r-a<0.
\]

This contradicts (4.3). \(\square\)

Lemma 4.1 strengthens the same-chain adjacency obstruction: for
\(r\ge2\), changing the partner does not help.

## 5. External-buffer lower bound

Call an endpoint **external** if it carries neither an upper nor a lower
piece from the selected eligible rephased bank.

### Theorem 5.1 (one external successor per upper endpoint)

In a cyclic literal PBBS serialization containing \(H\) upper companion
endpoints with remainders at least two, there are at least \(H\) external
endpoint occurrences.  More precisely, the immediate successor map sends
the \(H\) upper endpoints injectively into the external endpoints.

#### Proof

By Lemma 3.1, the successor of an upper endpoint is not upper.  By Lemma
4.1, it is not lower.  Hence it is external.  Distinct positions have
distinct immediate successors on a cycle. \(\square\)

For a union of \(c\) linear regions, the same argument gives at least
\(H-c\) external successors.  Therefore a closed schedule consisting only
of the \(2H\) rephased companion endpoints does not exist.  The adaptive
phase construction necessarily recouples the bank to at least \(H-O(1)\)
background endpoint occurrences.

There is a sharper rank filter on those external successors.  Suppose the
successor endpoint carries a saturated target piece on some depth interval,
and write its rank at depth \(j\) as

\[
 j+c_X.
\]

If that interval meets \([3,d]\), then the suffix recurrence from the
upper endpoint forces

\[
 \boxed{c_X\ge t-d-2.}
\tag{5.1}
\]

Indeed, the preceding upper target at depth \(j-1\) has rank
\(t-d+j-2\) and must be contained in the successor target of rank
\(j+c_X\).  Thus lower-slab pieces cannot serve as successors merely by
being reordered; the host must come from the top-offset bank or be a
genuine reset/nonsaturated state.

In fact any successor whose depth-\(d\) value is prescribed to have rank
\(t-1\) is excluded.  The proof of Lemma 3.1 applies verbatim: that
depth-\(d\) value and the preceding upper top share the preceding upper
depth-\((d-1)\) value of rank \(t-2\), so their owner union has rank at
most \(t<m\).  Therefore the external successor must be a genuinely
nonsaturated/reset state (or a piece leaving the depth-\(d\) cell free to
rise above rank \(t-1\)), not merely another top-slab SCD piece.

The exact successor rank floor is stronger still.  Let

\[
 Y=Z_{e,d}
\]

at the successor of an upper endpoint \(e-1\).  Both \(Y\) and the
preceding upper top contain

\[
 Z_{e-1,d-1}
\]

of rank \(t-2\), and the preceding upper top has only one further
coordinate.  Hence

\[
 m=|Z_{e,d+1}|
 =|Z_{e-1,d}\cup Y|
 \le |Y|+1.
\]

Therefore

\[
 \boxed{|Z_{e,d}|\ge m-1.}
\tag{5.2}
\]

So the successor is not merely external to the companion bank: its
depth-\(d\) state must already be a coatom or an owner.  This identifies
the ordinary high reset bank, rather than the generic residual SCD pieces,
as the natural host shore.

This is an occurrence requirement, not an added-length lower bound.  The
ordinary merged ledger already contains a much larger bank of private
reset endpoints and other pieces.  Those endpoints may serve as the
external successors if their literal states are chosen jointly.

## 6. Exact lag-\(d\) owner-buffer aperture

Let \(e\) carry an upper companion and put

\[
 U_e=Z_{e,d}.
\]

Then \(|U_e|=t-1\), while its central owner \(T_e=Z_{e,d+1}\) has rank
\(m=t+d\).  Since

\[
 T_e=U_e\cup A_{e-d},
\]

we have the exact identity

\[
 \boxed{
 T_e\setminus U_e=A_{e-d}\setminus U_e,
 \qquad |A_{e-d}\setminus U_e|=d+1.}
\tag{6.1}
\]

Now let \(P_p\) be the allowed source envelope at position \(p\), and let
\(\mathcal I\) contain every assigned target/owner interval with declared
value \(T(I)\).  Define the coordinates safe at \(p\) by

\[
 C_p=P_p\cap\bigcap_{I\in\mathcal I:\ p\in I}T(I).
\tag{6.2}
\]

### Corollary 6.1 (buffer-slot necessary condition)

Every upper companion endpoint \(e\) requires

\[
 \boxed{|C_{e-d}\setminus U_e|\ge d+1.}
\tag{6.3}
\]

The \(H\) required lag positions \(e-d\) are pairwise distinct.

#### Proof

Every literal source letter at position \(p\) is contained in \(C_p\): it
must lie in its owner envelope and in every prescribed interval value
containing that position.  Apply this to \(p=e-d\) and use (6.1).
Translation by \(-d\) is a bijection on the cyclic position set. \(\square\)

Thus the nonempty-letter row from the envelope-aware cover criterion is
far from sufficient at an upper endpoint.  Its lag slot must have a
\((d+1)\)-dimensional safe exterior relative to the top target.

For the explicit upper component (2.3), every \((d+1)\)-source window has
value

\[
 K\cup Z[i-r-d,i]
\]

of rank \(t\), not \(m\).  It therefore fails (6.1) by exactly \(d\)
ranks.  The two-zone packet proves target common-history, but it cannot be
dropped unchanged into the PBBS owner row.

## 7. Sharpened remaining host theorem

The adaptive-phase zero-reset ledger can now be physicalized only by a
joint selection satisfying both of the following occurrence-level rows.

1. **Successor buffers.**  Match every upper companion to a distinct
   external immediate successor whose assigned piece/reset state is
   recurrence-compatible.
2. **Lag buffers.**  At the distinct position \(d\) steps before every
   upper endpoint, preserve at least \(d+1\) safe coordinates outside its
   top target as in (6.3).

These rows must be imposed together with the envelope-aware cover-free
conditions

\[
 I\cap U_x\ne\varnothing
\]

for every positive coordinate/interval pair.  They are not implied by the
abstract endpoint count.

Conversely, the two-zone construction proves that no additional
target-history obstruction is intrinsic to the pair

\[
 (d,r)\rightsquigarrow(r+1,d-1).
\]

The remaining theorem is therefore a **background-buffer recoupling
theorem**: embed the explicit separated companion histories into the much
larger existing reset/piece bank while satisfying the successor and lag
matchings and the coordinate cover cuts.  A permutation of the companion
bank alone cannot do it.

## 8. Scope

This note proves:

\[
\boxed{
\begin{gathered}
\text{nonadjacent companion target histories exist explicitly, but}\\
\text{every upper companion consumes one external successor occurrence}\\
\text{and one distinct lag-}d\text{ buffer with }d+1\text{ safe new coordinates.}
\end{gathered}}
\]

It does not construct the background-buffer recoupling, the full merged
PBBS chart, \(\nu(k)\le B(k)+O(1)\), or exact equality.
