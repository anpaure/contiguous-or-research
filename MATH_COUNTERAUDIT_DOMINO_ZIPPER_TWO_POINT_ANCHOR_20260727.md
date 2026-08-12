# Counteraudit of the paired-window zipper at a two-point anchor

Date: 2026-07-27

## 0. Outcome

The row

\[
 k=2\quad\Longrightarrow\quad\text{zero new free labels}
\]

in Lemma 2.1 of
`MATH_THEOREM_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md`
is false.  A cross-shore star--top shared edge fixes the top carrier, but
does not fix either its endpoint four-set or the pairing of that four-set
into endpoint dominoes.  There is a literal extendable **top-only**
corridor with

\[
 \binom{R-1}{2}=\Theta(n^2)
\]

choices having the same prescribed common edge and the same top phase.
Thus the two-point anchor can release a whole unordered pair.

In this top-only corridor the shared edge lies in two different star cells
of the second packet, so a decoder cannot canonically reclassify it as a
star-phase edge.  The immediate two-star collar contains
eight distinct targets, exactly two of which need lie in the fixed packet.
Hence the corridor has six local noncommon targets for its two free
labels.  A charge of three missing targets per free label is sharp at this
radius; a charge of four per free label is impossible from the immediate
two-star collar.

There is a separate mate-edge/shore hinge.  If the shared pair is itself
one endpoint domino, one incident star can be an entire common star cell.
Then an arbitrary second endpoint pair has \(\Theta(n^2)\) choices while
the immediate two-star collar has only four noncommon targets.  Thus an
unqualified charge of three per free label is also false; the value three
is sharp only for the genuine top-only split.

This invalidates the proof of the claimed \(n^{s/3}\) inverse theorem.  It
does not by itself refute the numerical exponent \(1/3\): the corrected
local corridor lies exactly on that exponent.  Independently, the global
uniform theorem is refuted by
`MATH_OBSTRUCTION_GLOBALLY_ALIGNED_DOUBLE_SEGMENT_DOMINO_ENTROPY_20260727.md`,
whose two-segment family reaches exponent \(1/2-o(1)\).

## 1. Fixed packet and cross-shore edge

Let

\[
 n=2m,\qquad R=2r+1<m,
\]

and fix a domino-twin packet (F).  Choose one of its star cores

\[
 A=B_i\cup B_{i+1}\cup\cdots\cup B_{i+r-1},
 \qquad |A|=2r=R-1.
\]

Write its two boundary dominoes as

\[
 B_{i-1}=\{u,u'\},
 \qquad
 B_{i+r}=\{v,v'\}.
\]

Take the cross-shore pair

\[
 E=\{u,v\}
\]

and the two fixed targets

\[
 X=A\cup\{u\},\qquad Y=A\cup\{v\}.                    \tag{1.1}
\]

They form an edge of the star cell of (F), with

\[
 X\cap Y=A,
 \qquad
 X\cup Y=U:=A\cup E.                                   \tag{1.2}
\]

If the edge is declared to be in the top phase of a second packet, (1.2)
fixes its top carrier (U).  It does not fix the four labels which are
eligible to be deleted from (U).

## 2. The mate-edge corridor and its limitation

For every two-set

\[
 \Lambda=\{a,b\}\in\binom A2,                          \tag{2.1}
\]

pair the elements of (A\setminus\Lambda) arbitrarily into
(r-1) dominoes

\[
 D_1,D_2,\ldots,D_{r-1}.
\]

Choose two further dominoes (H_-,H_+), disjoint from (U), and consider
the following consecutive corridor in a second domino word:

\[
 H_-,\ E,\ D_1,\ldots,D_{r-1},\ \Lambda,\ H_+.         \tag{2.2}
\]

The (r+1) central dominoes from (E) through (Lambda) have union
(U).  Their top cell is

\[
 \mathcal T_\Lambda
 =\{U\setminus\{z\}:z\in E\cup\Lambda\}.              \tag{2.3}
\]

In particular,

\[
 U\setminus\{u\}=Y,
 \qquad
 U\setminus\{v\}=X.                                   \tag{2.4}
\]

Thus every value of (Lambda) realizes exactly the same prescribed edge
({X,Y}) in exactly the same top carrier (U).

The two star cells immediately incident with (2.3) have cores

\[
 A
 \quad\text{and}\quad
 K_\Lambda=(A\setminus\Lambda)\cup E,                  \tag{2.5}
\]

and are

\[
 \mathcal S_\Lambda^+
 =\{A\cup\{z\}:z\in E\cup H_+\},                      \tag{2.6}
\]

\[
 \mathcal S_\Lambda^-
 =\{K_\Lambda\cup\{z\}:z\in H_-\cup\Lambda\}.      \tag{2.7}
\]

The two targets of (2.7) obtained from (z=a,b) are respectively
(U\setminus\{b\}) and (U\setminus\{a\}), the other half of the top
cell (2.3).  Hence (2.6)--(2.7) are a literal two-star collar in a completed
domino packet, not an abstract Johnson configuration.

### Proposition 2.1 (local list size)

The data (X,Y), the top phase, and the carrier (U) admit

\[
 \binom{R-1}{2}
\]

different choices of the endpoint domino (Lambda).  Different choices
give different top cells and therefore different simple packet supports
after completion.

#### Proof

The endpoint four-set of (2.3) is (E\cup\Lambda), which is recovered
from the four targets of the top cell as their set of omitted labels.
Thus distinct (Lambda)'s give distinct top cells.

In a paired cyclic word a carrier of (r+1<m) consecutive disjoint
dominoes occurs at only one start: equality of two such carrier unions
would give equality of their block-index intervals.  Hence a completed
simple support cannot identify the displayed top cells for two distinct
values of (Lambda).  Finally

\[
 \binom{|A|}{2}=\binom{R-1}{2}=\Theta(n^2).
\]

\(\square\)

This already displays the missing endpoint pair.  However, the edge
\(\{X,Y\}\) is also contained in the star cell with core \(A\), because
\(E\) was paired as one endpoint domino.  A decoder could therefore record
the edge in star phase.  The next section removes this ambiguity.

Knowing a
top union (W_j\cup C_{j+r}) does not determine (C_{j+r}).  The
recurrences

\[
 W_{j+1}=(W_j\setminus C_j)\cup C_{j+r}
\]

cannot be used until that endpoint domino has been exposed.  A phase bit
does not expose it.

## 3. Exact immediate-collar count for the mate-edge corridor

We next choose (H_+,H_-) so that the corridor has no accidental common
targets.

Choose (H_+) in blocks of (F) which are not the two boundary blocks of
(A).  Then

\[
 \mathcal S_\Lambda^+\cap F=\{X,Y\}.                   \tag{3.1}
\]

Indeed a target consisting of the (r) consecutive full blocks (A)
and one further label belongs to (F) exactly when that label lies in one
of the two adjacent boundary blocks.

There is also no hidden occurrence of the two remaining members of the
(F)-cell elsewhere in the second packet.  Its (r) consecutive blocks
(D_1,ldots,D_{r-1},\Lambda) partition all of (A).  If a target of the
second packet contains all (2r) labels of (A), its (r)-block core must
contain every one of these blocks: omitting one block would omit two target
labels, while the split boundary supplies only one.  Hence its core is
exactly (A), and its extra label must lie in the displayed boundary
dominoes (E) or (H_+).  Choosing (H_+) away from
(\{u',v'\}) therefore makes

\[
 \mathcal S_i(F)\cap G=\{X,Y\}                         \tag{3.1a}
\]

in every completion of the corridor.

For (K_\Lambda), define

\[
 Z_\Lambda
 =\{z\notin K_\Lambda:K_\Lambda\cup\{z\}\in F\}.
\]

The induced Johnson graph of a twin packet has clique number four, so

\[
 |Z_\Lambda|\le4.                                      \tag{3.2}
\]

Choose the two labels of (H_-) outside
(U\cup Z_\Lambda\cup H_+).  There are linearly many available labels.
The two extensions indexed by (H_-) are then outside (F).  The two
extensions indexed by (Lambda) are also outside (F): their occupancy
in the fixed (F)-dominoes consists of (r-1) full blocks and three
singleton blocks, since (E) is cross-shore.  Therefore

\[
 \mathcal S_\Lambda^-\cap F=\varnothing.               \tag{3.3}
\]

The star cells of one packet are disjoint.  Combining (3.1)--(3.3),

\[
 \left|
 (\mathcal S_\Lambda^+\cup\mathcal S_\Lambda^-)
 \cap F
 \right|=2,                                             \tag{3.4}
\]

and hence

\[
 \left|
 (\mathcal S_\Lambda^+\cup\mathcal S_\Lambda^-)
 \setminus F
 \right|=8-2=6.                                        \tag{3.5}
\]

### Corollary 3.1 (sharp local charge)

The two-point anchor releases the two labels of (Lambda).  Its immediate
two-star collar contains exactly six noncommon targets.  Thus the best
possible charge at this radius is

\[
 \frac{6\text{ noncommon targets}}{2\text{ free labels}}=3.             \tag{3.6}
\]

In particular, four missing targets per free label cannot be derived from
the cell together with its immediate two-star collar.

Equation (3.6) also explains why the numerical \(1/3\) exponent is not
refuted by this local family.  It refutes the asserted decoding table,
which assigns zero free labels at \(k=2\), and supplies the exact replacement
one would need in a corrected proof: two free labels must be charged to the
six-target two-star collar.

## 4. Genuine top-only split: the decisive \(k=2\) counterexample

Retain the cross-shore labels \(E=\{u,v\}\) and choose an ordered pair of
distinct labels

\[
 p,q\in A.
\]

Use the two endpoint dominoes

\[
 P=\{u,p\},\qquad Q=\{v,q\},                            \tag{4.1}
\]

pair \(A\setminus\{p,q\}\) into \(r-1\) internal dominoes
\(D_1,\ldots,D_{r-1}\), and form the corridor

\[
 H_-,\ P,\ D_1,\ldots,D_{r-1},\ Q,\ H_+.               \tag{4.2}
\]

The central top carrier is still

\[
 U=A\cup\{u,v\}.
\]

Its two common targets are \(X=U\setminus\{v\}\) and
\(Y=U\setminus\{u\}\).  The two adjacent star cores are

\[
 K_-=U\setminus Q=(A\setminus\{q\})\cup\{u\},
\qquad
 K_+=U\setminus P=(A\setminus\{p\})\cup\{v\}.           \tag{4.3}
\]

The target \(X\) lies in the star with core \(K_-\), while \(Y\) lies in
the star with core \(K_+\).  Therefore no star cell of the second packet
among the displayed collars contains both \(X\) and \(Y\).  In fact no
star cell anywhere in a completion can contain both.  Such a star would
have core \(X\cap Y=A\).  But the labels of \(A\) occupy the \(r-1\)
internal blocks together with \(p\in P\) and \(q\in Q\).  A block interval
containing both \(p\) and \(q\) must also contain \(u\) and \(v\), while
omitting either endpoint omits one of \(p,q\).  Hence \(A\) is not a union
of \(r\) second-packet dominoes.  The common edge is genuinely top-only.

### Proposition 4.1 (top-only local multiplicity and charge)

There are \(\Theta(n^2)\) distinct top cells with the same common edge
\(\{X,Y\}\) and the same top carrier \(U\).  Their immediate two-star
collars can be chosen to contain exactly two targets of \(F\), hence
exactly six noncommon targets.

#### Proof

The endpoint four-set is

\[
 D=\{u,v,p,q\}.
\]

As the unordered pair \(\{p,q\}\) ranges over \(\binom A2\), these are
\(\binom{R-1}{2}=\Theta(n^2)\) distinct top cells.  Fix either assignment
of \(p,q\) to the two endpoints.

In the star with core \(K_-\), the endpoint \(Q\) supplies \(X\) and the
noncommon target \(U\setminus\{q\}\).  In the star with core \(K_+\), the
endpoint \(P\) supplies \(Y\) and the noncommon target
\(U\setminus\{p\}\).  The latter two targets are outside \(F\) by the
cross-shore occupancy calculation: each has \(r-1\) full \(F\)-dominoes
and three singleton dominoes.

For either core \(K\), the possible extension labels

\[
 Z(K)=\{z:K\cup\{z\}\in F\}
\]

have cardinality at most four, because all such extensions form a clique
in the Johnson graph induced by \(F\).  Choose the two labels of \(H_-\)
outside \(Z(K_-)\), and those of \(H_+\) outside \(Z(K_+)\), keeping the
two blocks disjoint from the carrier and each other.  The two collar stars
then meet \(F\) in \(\{X\}\) and \(\{Y\}\), respectively.  They are
disjoint four-target cells of the second packet, so their union has eight
targets, two common and six noncommon.  \(\square\)

This is a direct counterexample to the \(k=2\) row: the phase is uniquely
top, yet the row releases the two labels \(p,q\).

## 5. The same-shore mate hinge: why an unconditional charge \(3\) is false

There is a stronger local degeneracy if mate edges are allowed.  Let
\(E=B_{i+r}\) be one whole boundary domino of the \(F\)-star with core
\(A=A_i\), and put \(U=A\cup E\).  The opposite endpoint domino of this
native \(F\)-top carrier is \(O=B_i\).  Choose

\[
 \Lambda=\{a,b\}\in\binom{A\setminus O}{2}.             \tag{5.1}
\]

Use \(E\) and \(\Lambda\) as the endpoint dominoes of a second-packet top
cell, pair \(A\setminus\Lambda\) internally, and take the exterior
boundary at the \(A\)-star to be the other \(F\)-boundary domino
\(B_{i-1}\).  Then that entire incident star cell is exactly
\(\mathcal S_i(F)\), while the other incident star has core

\[
 (A\setminus\Lambda)\cup E.
\]

The latter can be given an exterior boundary avoiding its at most four
possible \(F\)-extensions, exactly as above.  Its two top targets are
\(U\setminus\{a\}\) and \(U\setminus\{b\}\); neither belongs to \(F\)
because \(a,b\) are not in the native endpoint set \(E\cup O\).
Consequently the immediate two-star collar consists of one completely
common star and one completely noncommon star:

\[
 8\text{ targets},\qquad 4\text{ common},\qquad
 4\text{ noncommon}.                                   \tag{5.2}
\]

There are \(\binom{R-3}{2}=\Theta(n^2)\) choices of \(\Lambda\).
Therefore no unconditional radius-one argument can charge three missing
targets to each free endpoint label.  This is a mate-edge/shore hinge:
the shared pair is simultaneously in star and top phase.  It must be
handled separately from Proposition 4.1, for example by following intact
shore or whole-domino transport farther than one collar.

## 6. Completion, including a complete common cell

Every corridor (2.2), (4.2), and the same-shore corridor of Section 5
extends to a full cyclic domino word: pair the unused labels arbitrarily
and place the resulting dominoes outside the displayed corridor.

In the Gaussian annulus write

\[
 h=m-2r=q_0+1.
\]

After reserving (A) and its two split boundary labels, the complement of
the displayed (F)-core contains a consecutive run of

\[
 m-r-2=r+h-2
\]

intact (F)-dominoes.  For (h\ge6), choose (H_-,H_+) near the ends of
this run and leave (r+2) consecutive intact dominoes in their original
order in the completion.  The middle (r) of those blocks, with their two
unchanged boundary blocks, form a complete common star cell.  Thus the
local family is compatible with the global-dihedral anchor assumed by the
zipper lemma.

The other common-cell data of the completions need not be identical as
(Lambda) varies.  Accordingly, Proposition 2.1 is a counterexample to
the local (k=2) decoding assertion and to its proof, not by itself a
counterexample to the final numerical list bound.  The latter is already
closed negatively by the independent double-segment construction cited in
Section 0.

## 7. Proved boundary

The following statements are now exact.

1. A genuine top-only star--top shared edge determines its carrier but
   leaves an arbitrary endpoint pair: local multiplicity
   \(\Theta(n^2)\).
2. A phase bit does not remove this multiplicity; in Proposition 4.1 the
   phase is uniquely top.
3. The immediate top-only collar has six noncommon targets.  Thus \(3\)
   per free label is sharp there, and \(4\) is false.
4. The mate-edge/shore hinge has only four noncommon collar targets for
   two free labels.  Thus even \(3\) is false without the top-only
   qualification.
5. Any valid global \(1/3\) argument would need a disjoint or bounded-overlap
   packing of these six-target collars.  The zipper proof contains no such
   packing.
6. Even such a repair cannot yield a uniform exponent below \(1/2\) in the
   stated range \(s=o(m)\), because the aligned double-segment family is a
   separate global obstruction.

The mechanisms agree: the top-only six-target corridor proves that a
\(1/3\) charge is available only while its two fronts are private and no
mate hinge is used.  In the
double-segment construction the second modified segment is displaced by
\(r\), so one remote front of each corridor is the same front (up to the
annular offset \(h=m-2r\)).  The first-collar charges therefore cease to
be additive, which is exactly how the global exponent rises from (1/3)
toward \(1/2\).
