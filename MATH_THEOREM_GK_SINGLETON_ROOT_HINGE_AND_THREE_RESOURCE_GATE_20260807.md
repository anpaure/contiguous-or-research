# Every Greene--Kleitman singleton root has a matching-compatible hinge

**Date:** 2026-08-07  
**Method:** explicit parenthesis-record analysis in the standard
Greene--Kleitman symmetric-chain decomposition  
**Status:** unconditional local theorem.  It makes the Hall-safe SCD
omission bank compatible with one hinge at every omitted colour.  Global
privacy is reduced to a three-resource list-transversal; that transversal
and the second coloured perfect matching remain open.

## 1. The SCD omission bank

Represent subsets of `[2m]` by binary words, with `1` an upstep and `0` a
downstep.  Use the standard parenthesis matching.  In the Greene--Kleitman
SCD, the successor of a word below the middle flips its rightmost unmatched
zero to one.

Every rank-`(m-1)` word has a successor of rank `m`; these successors are
distinct.  Their image has order

\[
 {2m\choose m-1}=m\operatorname {Cat}_m.
\]

The omitted rank-`m` words are exactly the fully matched Dyck words.  Put

\[
 \mathcal O_{\rm GK}=\{\text{Dyck words of semilength }m\},
 \qquad |\mathcal O_{\rm GK}|=\operatorname {Cat}_m. \tag{1.1}
\]

Writing `t(B)` for the SCD successor of a rank-`(m-1)` word `B`, the edges

\[
                         B\subset t(B)               \tag{1.2}
\]

form a perfect matching from `binom([2m],m-1)` onto
`binom([2m],m)\O_GK`.  Hence this omission bank is Hall-safe before any
hinges are planted.

We use the elementary record interpretation: in any parenthesis word, the
unmatched zeros are precisely the downsteps creating new record-low
heights.  The rightmost unmatched zero is the step which first creates the
last such record.

## 2. An explicit hinge at every Dyck root

Fix `U in O_GK`, with `m>=2`.  Let `u` be the first upstep of `U`.

### Case I: the first primitive component has semilength at least two

Let `y` be the closing downstep of the first primitive component.  Its
second step is necessarily an upstep; call it `b`.  Let `x` be the
downstep matched to `b`.

Thus

\[
                         u<b<x<y.                    \tag{2.1}
\]

### Case II: the first primitive component is `10`

Let `y` be its closing downstep.  Since `m>=2`, there is a second primitive
component.  Let `b` be its opening upstep and let `x` be its closing
downstep.  Thus

\[
                         u<y<b<x.                    \tag{2.2}
\]

In either case define

\[
 a=U\setminus\{u,b\},\qquad
 X=a+b=U-u,
\]

\[
 B_x=a+x,qquad B_y=a+y,                            \tag{2.3}
\]

and

\[
 Q_x=a+b+x,qquad Q_y=a+b+y.                        \tag{2.4}
\]

### Theorem 2.1 (SCD-compatible root hinge)

The Greene--Kleitman successor satisfies

\[
                         t(X)=Q_y,qquad t(B_x)=Q_x. \tag{2.5}
\]

Consequently

\[
 B_x\subset Q_x\supset X\subset Q_y\supset B_y     \tag{2.6}
\]

is a Boolean incidence hinge in which the first and third edges are the
fixed SCD matching edges.  Suppression gives two Johnson edges of the same
intersection colour `a`, and `X subset U` supplies the endpoint ticket to
the omitted root.

#### Proof

First consider `X=U-u`.  Relative to the Dyck height of `U`, the height of
`X` is lower by two from `u` onward.  It first reaches record `-1` at `u`
and record `-2` at the close `y` of the first primitive component; it never
goes below `-2`.  Thus `y` is the rightmost unmatched zero and
`t(X)=X+y=Q_y`.

In Case I, the word `B_x=U-u-b+x` is lower by two after `u`, lower by four
from `b` through the interior of its matched excursion, and lower by two
again after `x`.  The first primitive component stays above height zero,
and the `b`-excursion stays at height at least two.  Hence `B_x` first
creates record `-1` at `u` and record `-2` at `b`, never going lower.
Therefore `b` is its rightmost unmatched zero.

In Case II, changing the first component `10` at `u` creates successive
records `-1` at `u` and `-2` at `y`.  Flipping the opener `b` of the next
component creates record `-3` at `b`; flipping its close `x` upward returns
the suffix displacement to `-2`.  Thus the unmatched positions have the
ordered pattern `0,0,0,1`, and `b` is again the rightmost unmatched zero.

In both cases `t(B_x)=B_x+b=Q_x`, proving (2.5).  The containments in
(2.6) are immediate.  The two suppressed intersections are

\[
                         B_x\cap X=X\cap B_y=a.
\]

Finally `X=U-u subset U`. \(\square\)

## 3. Exact alternating-matching interpretation

Orient (2.6) from `B_x` to `B_y`.  Colour its edges alternately.  The SCD
matching is

\[
                         B_xQ_x,\qquad XQ_y,          \tag{3.1}
\]

and the prospective second matching is

\[
                         XQ_x,\qquad B_yQ_y.          \tag{3.2}
\]

Thus no modification of the first perfect matching is required.  Also,
`Q_x,Q_y` lie outside `O_GK` automatically because they are SCD successor
images.

The central facets

\[
                         X_U=U-\{1\}                 \tag{3.3}

are pairwise distinct over all Dyck roots `U`, because every Dyck word
starts with the same first upstep and deleting it is injective.  Hence the
resources `X_U` and `Q_{y,U}=t(X_U)` are already globally private.

## 4. The remaining three-resource transversal

Let `L_U` be the list of all hinges at `U` satisfying the two fixed-matching
relations (2.5).  The explicit construction above proves that every
`L_U` is nonempty.

Put

\[
                  \mathcal X=\{X_U:U\in\mathcal O_{\rm GK}\}.
\]

After the automatic privacy in (3.3), a full private bank compatible with
the fixed SCD matching is obtained exactly by choosing one member of every
`L_U` so that

\[
 \{B_{x,U},B_{y,U}:U\in\mathcal O_{\rm GK}\}
 \quad\hbox{has size }2|\mathcal O_{\rm GK}|,          \tag{4.1}
\]

\[
 \{B_{x,U},B_{y,U}:U\in\mathcal O_{\rm GK}\}
 \cap\mathcal X=\varnothing,                           \tag{4.2}
\]

and

\[
                 U\longmapsto a_U
 \quad\hbox{is injective}.                             \tag{4.3}
\]

The first two conditions are one two-claim transversal on the
rank-`(m-1)` shore, with the fixed bank `mathcal X` reserved; the third is
an ordinary transversal on the rank-`(m-2)` colours.

Indeed, (4.1)--(4.2) make all `B_x,B_y,X` vertices globally distinct.
Since `t` is injective, they also make every `Q_x=t(B_x)` distinct from
every `Q_y=t(X)` and from the other `Q_x` vertices.  Condition (4.3) makes
the suppressed intersection colours private.  Conversely a collision in
the physical hinge bank is either a collision among the rank-`(m-1)`
vertices, hence violates (4.1) or (4.2), or a collision among the
rank-`(m-2)` intersection colours, hence violates (4.3).

Thus prescribing the Hall-safe SCD omission bank does **not** destroy the
local hinge menu.  It reduces the prospective private-bank theorem to one
explicit three-resource list-transversal on Catalan-indexed Dyck roots,
where a choice claims the resource triple `(B_x,B_y,a)` and must avoid the
fixed `X` bank.

This note does not prove that transversal.  Even after it is proved, one
must extend the second matching (3.2), cover every intersection colour,
and control its cycle count.  The theorem closes only the first-matching
and one-hinge-per-omitted-root rows.
