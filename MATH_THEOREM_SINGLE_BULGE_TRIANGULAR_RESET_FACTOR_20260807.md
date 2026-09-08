# One recycled rank jump gives a zero-charge triangular reset factor

**Date:** 2026-08-07  
**Method:** specialize the sharp pull hinge to one deadline-sized bulge,
then compare its exact rank ledger with the merged PBBS endpoint deficit  
**Status:** unconditional local construction, exact abstract chain factor,
and symmetric fractional literal-factor theorem.  One reset event serves
(d-1) low endpoints and every physical position still carries (d)
strict-lower cells.  This is the smallest currently proved replacement for
the impossible positive-density full-endpoint bank.  The special literal
ring factor, residual PBBS chart, and global fusion remain open.

## 1. Specialize the sharp pull hinge

Use

\[
 n=2m+1,\qquad s=m-2d,\qquad t=m-d,
\tag{1.1}
\]

and put

\[
 D=d+1,\qquad c=m-d-1=t-1.
\tag{1.2}
\]

In the sharp pull-hinge theorem take

\[
                         \delta=d,\qquad j=d-1.
\tag{1.3}
\]

Choose a core (C_0) of size (c), a set (H\subset C_0) of size (d),
and a cyclic private-label set of length

\[
                         \ell=3d.
\tag{1.4}
\]

Repeat the source pattern

\[
                         \mathsf L^{d-1}\mathsf H,
\tag{1.5}
\]

where at phase (u)

\[
 A_u=
 \begin{cases}
 (C_0\setminus H)\cup\{f_u\},&\mathsf L,\\
 C_0\cup\{f_u\},&\mathsf H.
 \end{cases}
\tag{1.6}
\]

The choice (1.4) is a multiple of the schedule period (d).  It is longer
than (D+1), and

\[
                         \ell-D=2d-1\ge D
\tag{1.7}
\]

for (d\ge2).

The sharp pull-hinge theorem gives a simple rank-(m) Johnson owner cycle,
simple immediate lower and upper palettes, and exact regeneration.  The
private coordinates have owner run (D) and owner gap (ell-D); hence
(1.7) also gives two-sided owner residence.  The coordinates of (C_0)
are present in every owner, because every (D)-window meets a high phase.

## 2. Exact endpoint rank profiles

Give a low endpoint its age

\[
                         a\in\{1,\ldots,d-1\},
\]

the number of consecutive low phases ending there.  Give a high endpoint
age (a=0).  The suffix-rank formula of the pull hinge becomes

\[
 |Z_{u,q}|=
 \begin{cases}
 s+q-1,&1\le q\le a,\\
 t+q-1,&a<q\le d.
 \end{cases}
\tag{2.1}
\]

Thus a low endpoint carries

\[
 s,s+1,\ldots,s+a-1,
 \quad
 t+a,t+a+1,\ldots,m-1,
\tag{2.2}
\]

and the high endpoint carries

\[
                         t,t+1,\ldots,m-1.
\tag{2.3}
\]

Every endpoint has exactly (d) proper suffix cells.  Its only nonsaturated
step is the deadline-sized jump between the two displayed intervals.

### Theorem 2.1 (triangular multiplicity ledger)

In one schedule period of (d) endpoints, the exact target-rank
multiplicities are

\[
 \boxed{
 \begin{aligned}
  \mu_{s+q-1}&=d-q &&(1\le q\le d-1),\\
  \mu_{t-1+q}&=q   &&(1\le q\le d).
 \end{aligned}}
\tag{2.4}
\]

They sum to

\[
 \sum_{q=1}^{d-1}(d-q)+\sum_{q=1}^{d}q=d^2,
\tag{2.5}
\]

exactly (d) marked cells per physical endpoint.

#### Proof

The low target of depth (q) occurs exactly at low ages
(a=q,q+1,\ldots,d-1), giving (d-q) occurrences.  The high target of
depth (q) occurs at ages (a=0,1,\ldots,q-1), giving (q) occurrences.
Equation (2.5) is the sum of the two triangular numbers. \(\square\)

Over the literal ring of length (3d), every multiplicity in (2.4) is
multiplied by three.  These are multiplicities of distinct named targets,
not merely occurrence counts.  A low rank-(s+q-1) value is

\[
 (C_0\setminus H)\cup
 \{f_{u-q+1},\ldots,f_u\},
\tag{2.6}
\]

and a high rank-(t-1+q) value is the same private cyclic interval over
(C_0).  Since (q\le d<\ell), different endpoints give different private
intervals.  The two core types lie in disjoint rank bands, so all displayed
marked values are distinct within one ring.

The reset event is the one high phase in each (d)-position schedule
period.  It is not an empty separator: it carries the complete high chain
(2.3).  One reset therefore serves the preceding (d-1) low endpoints,
and no source position is lost.

### Theorem 2.2 (exact saturated bridge completion)

The (d) marked hinge targets at every endpoint can be completed by (d)
new targets to one saturated chain containing exactly one set at every rank
from (s) through (m-1).  The bridge targets can be chosen so that all
(6d^2) marked and bridge targets of one length-(3d) ring are distinct.

Consequently the bridge bank consists of three full depth-(d) chains at
each variable base

\[
                         s,s+1,\ldots,t-1.
\tag{2.7}
\]

#### Proof

Put (P=C_0\setminus H), and fix an order
(H=\{h_1,\ldots,h_d\}).  At a low endpoint of age (a\ge1), let

\[
 I_u=\{f_{u-a+1},\ldots,f_u\},
 \qquad g_u=f_{u-a}.
\]

The last low target is (P\cup I_u), while the first high target is
(P\cup I_u\cup H\cup\{g_u\}).  Insert the bridge

\[
                         P\cup I_u\cup\{h_1,\ldots,h_r\},
                         \qquad1\le r\le d.
\tag{2.8}
\]

Its ranks are (s+a,\ldots,t+a-1).  The next high target adds (g_u), so
the low hinge segment, (2.8), and the high hinge segment concatenate to a
saturated rank-(s)-through-rank-(m-1) chain.

At a high endpoint (a=0), put (g_u=f_u).  To distinguish the three high
occurrences of the ring, bridge first with (g_u), then with
(h_1,\ldots,h_{d-1}), leaving (h_d) for the first marked high target:

\[
 P\cup\{g_u\},
 P\cup\{g_u,h_1\},\ldots,
 P\cup\{g_u,h_1,\ldots,h_{d-1}\}.
\tag{2.9}
\]

This has ranks (s,\ldots,t-1), and the next target
(P\cup H\cup\{g_u\}) has rank (t).

It remains to check collisions.  For low endpoints, intersecting a bridge
target with the private-label shore recovers (I_u); its size recovers the
age, and because (a<\ell), the cyclic interval recovers the endpoint.
Intersecting with (H) then recovers (r).  For high endpoints, every bridge
target contains the endpoint-specific label (g_u), so the same conclusion
holds.  A high bridge cannot equal a low bridge because their private-label
sets are respectively a high singleton and a nonempty all-low interval.

No bridge equals a marked low target because a bridge contains either a
member of (H) or a high private label.  A bridge missing a member of (H)
cannot equal a marked high target.  The only low bridge containing all of
(H) has private part (I_u).  A marked high target of the same rank would
have a cyclic private interval of the same length crossing a high phase;
equality of private intervals would force the same endpoint, where that
depth is low rather than high.  Finally every high bridge omits (h_d).
The marked targets were already shown distinct.  Hence the complete bank is
collision-free. \(\square\)

The theorem removes an otherwise hidden residual-rank problem.  The hinge
does not destroy its old saturated chain mass: it exchanges one half of
each rank-(s)-to-rank-(m-1) chain with a literal moving-bulge profile, while
exporting one variable-base saturated bridge of the same size.

### Lemma 2.3 (strict-lower bridges cannot follow one another)

Let two adjacent endpoints be saturated through depth (d), with respective
bases (a) and (b).  If their containing (d+1)-letter window has rank (m),
then

\[
                         \boxed{b\ge t=m-d.}
\tag{2.10}
\]

Hence no two saturated strict-lower endpoints, even with different bases,
can be consecutive in a flat rank-(m) (D^d) row.

#### Proof

The two top suffixes have ranks (a+d-1) and (b+d-1).  Their shared
depth-(d-1) suffix is the first endpoint's cell of rank (a+d-2).  Therefore

\[
 m\le |X\cup Y|
 \le(a+d-1)+(b+d-1)-(a+d-2)=b+d.
\]

This is (2.10). \(\square\)

Thus the bridge completion is target-exact but not yet physical.  Its full
bridges must be interleaved with high-base or nonsaturated hinge states; a
run of the exported bridges alone would immediately violate Lemma 2.3.

## 3. Exact current and full-endpoint avoidance

At a low endpoint of age (a), the age composition is

\[
 (s,
   \underbrace{1,\ldots,1}_{a-1},
   d+1,
   \underbrace{1,\ldots,1}_{d-a}).
\tag{3.1}
\]

The bulge (d+1) replaces the ordinary unit at age (a), so its conserved
age excess is exactly (d), the minimum deadline scale.  More explicitly,
every depth-(d) endpoint has rank (m-1), hence (alpha=beta=d) in the
adjacent-current notation.  Away from the reset edge the shared
depth-(d-1) suffix has rank (m-2), so (gamma=-d) and the current sum is
exactly (d).  At the last-low-to-high reset edge that shared suffix has
rank (t-2), so (gamma=0) and the current sum is (2d).  Thus the construction
attains the current inequality sharply on every transport edge and pays one
extra deadline bank only at the recycled reset edge.

At the high phase the bulge returns to age zero and the composition is

\[
                         (t,1,\ldots,1).
\tag{3.2}
\]

No endpoint is a full base-(s), depth-(d) endpoint: every low endpoint
has age at most (d-1), and the high endpoint starts at base (t).  Thus
the construction is outside the fixed-additive full-endpoint density
no-go, while every position still supplies (d) nested lower targets.

## 4. Zero local price in the merged endpoint ledger

Let

\[
                         \theta=2\sigma-1.
\tag{4.1}
\]

The merged SCD count is short by

\[
                         (\theta+o(1))W
\tag{4.2}
\]

private reset endpoints.  Rechainizing (R) old full pieces into (R)
single-bulge endpoints has the exact scalar comparison

\[
\begin{array}{c|c|c}
 &\text{full piece plus private reset}&\text{single-bulge endpoint}\\ \hline
\text{named lower cells}&Rd&Rd\\
\text{productive endpoints}&R&R\\
\text{unproductive reset endpoints}&R&0\\
\text{local appended positions}&0&0.
\end{array}
\tag{4.3}
\]

The rank multisets differ, so (4.3) is a rechainization ledger, not a claim
that the same named targets transport unchanged.  If the lower target bank
can be repartitioned into (R=(\theta+o(1))W) literal hinge chains plus the
residual PBBS chains, then the theta deficit is paid with zero local length
charge.

There are (R/(3d)+O(1)) literal rings before global splicing.  Their
fusion is a topology/occurrence problem, not an additive-position charge.

## 5. Exact abstract chain capacity

Fix any symmetric-chain decomposition of (B_n).  Every SCD chain meeting
rank (s) continues beyond rank (m-1).  Select distinct such chains.
For a selected chain assigned age (a\in\{0,\ldots,d-1\}), retain exactly
the ranks in (2.2), or (2.3) when (a=0).

### Proposition 5.1 (abstract triangular factor)

For every

\[
                         R\le {n\choose s},
\tag{5.1}
\]

and every prescribed multiset of (R) ages, there are (R) pairwise
target-disjoint inclusion chains with the corresponding profiles
(2.2)--(2.3).

#### Proof

There are exactly ({n\choose s}) SCD chains meeting rank (s), one for
each rank-(s) set.  Choose (R) of them and assign the ages arbitrarily.
Within one SCD chain all retained ranks are nested; different SCD chains
are disjoint. \(\square\)

In particular, grouping the ages into complete copies of
(0,1,\ldots,d-1) gives an exact abstract target-disjoint bank of

\[
                         d\left\lfloor{{n\choose s}\over d}\right\rfloor
\tag{5.2}
\]

single-bulge endpoints.  This exceeds the theta demand by a fixed factor
asymptotically.

## 6. Symmetric fractional literal-ring factor

Now restrict to chains that arise from the literal rings (1.5)--(1.6).
Average uniformly over all labelled choices of (C_0,H), all private-label
cycles, all roots, and every ground-set permutation.  Give the rings total
fractional mass (T).

At rank (s+q-1), one ring contains (3(d-q)) targets.  At rank
(t-1+q), it contains (3q).  Symmetry therefore gives the respective
per-target loads

\[
 {3(d-q)T\over {n\choose s+q-1}},
 \qquad
 {3qT\over {n\choose t-1+q}}.
\tag{6.1}
\]

The first expression is maximized at (q=1): both the numerator decreases
and the binomial denominator increases with (q).  For the high band,

\[
 { {n\choose t-1+q}\over q}
 \ge { {n\choose t}\over d}.
\tag{6.2}
\]

At the optimal deadline,

\[
 { {n\choose t}\over {n\choose s}}\longrightarrow e^{3\pi/4}>1,
\]

so, for all sufficiently large parameters, the right side of (6.2) is
larger than ({n\choose s}/(d-1)).  Hence the rank-(s) row is the
bottleneck, and

\[
                         \boxed{T\le {1\over3(d-1)}{n\choose s}}
\tag{6.3}
\]

is a fractional matching.  Since one ring has (3d) endpoints, its
fractional endpoint capacity is

\[
                         \boxed{{d\over d-1}{n\choose s}}.
\tag{6.4}
\]

At the optimal deadline,

\[
 {{n\choose s}\over W}\longrightarrow e^{-\pi},
 \qquad
 {e^{-\pi}\over\theta}>3000.
\tag{6.5}
\]

Thus neither named-target counts nor fractional literal-ring capacity
obstruct the required reset bank.

## 7. Exact surviving gate

The remaining theorem is now precise.

> **Triangular hinge-factor theorem.**  Choose target-disjoint literal
> single-bulge rings containing ((\theta+o(1))W) endpoints, extend the
> residual target bank to the merged PBBS endpoint chart, and splice the
> ring owner cycles into one occurrence-labelled owner chronology while
> preserving the coordinate-cover and common-compiler rows.

The abstract factor in Proposition 5.1 and the symmetric fractional literal
factor (6.3) do not imply this joint integral statement.  Each literal ring
contains (3d^2=\Theta(n)) marked targets, and there are
(\Theta(W/d)) ring components to fuse.  The residual chain partition and
the owner/cover/compiler selectors must be chosen in correlation.

## 8. Verdict

A single deadline-sized bulge can serve many theta tasks: it moves through
(d-1) low ages, is restored by one productive high phase, and repeats.
It preserves a flat rank-(m) (D^d) row and has zero local position
charge.  What fails is only the old demand that every serviced endpoint be
a complete full deep piece.

The local reset and its exact scalar, chain, and fractional ledgers are now
closed.  The global triangular hinge-factor theorem remains open, so this
does not yet prove (B(k)+O(1)).
