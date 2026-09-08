# The Fano precedence obstruction: equal length is at least seven

Date: 2026-07-26

Method: pure mathematics.  This note answers the fresh-reservoir Fano
packet question left by
`MATH_THEOREM_GEODESIC_C6_LINEARITY_AND_FANO_CLOSURE_20260726.md`.

## 0. Outcome

The seven Fano (3)-cycles do close algebraically and obey the necessary
pair-linearity law, but they cannot be realized with only the three
mandatory router exchanges, nor with one additional storage exchange.

> **Rank-five pointwise and rank-seven equal-length lower bounds.**  In every
> monotone realization in which the seven routers use disjoint petal
> reservoirs, each physical strand needs its three mandatory router
> exchanges and at least two additional petal exchanges.  Moreover, six
> of the seven strands need at least three additional exchanges, and a
> global span count forces one strand to need at least four.  Thus an
> equal-length packet has port rank/length at least seven.

The proof is a finite betweenness contradiction on the Fano incidence
graph.  It is independent of router orientations, the order of the seven
lines, and freshness of the (X/Y) shores.  In particular, no choice of
the identity

\[
 (135)^{-1}(245)(236)(034)(146)(056)(012)=1
\]

produces the requested rank-(3) or rank-(4) literal packet; ranks five
and six are also impossible for an equal-length packet.

There is a second exact conclusion.  Any closed router tube whose *full*
layer-by-layer (X/Y) atlas is unchanged is neutral at every depth:
all load vectors (mu_q), and hence all overload and collision ledgers,
are identical before and after the switch.  Such a tube can be an
ownership/repackaging primitive, but not by itself a balancing move.

## 1. Fresh-reservoir Fano model and complete local ledger

Let (mathcal L) be the seven lines of the Fano plane on a point set
(P), and order them arbitrarily.  A point of (P) denotes a physical
strand.  Each point lies on three lines and each pair of points lies on a
unique line.

For every line (L={x,y,z}), choose a fresh petal reservoir

\[
 A_L={a_{L,x},a_{L,y},a_{L,z}},                     \tag{1.1}
\]

with the (A_L)'s pairwise disjoint.  At the instant of the (L)-router,
its complete common-core incidence ledger is

\[
 \mathcal X_L={K_L+a_{L,x},K_L+a_{L,y},K_L+a_{L,z}},                \tag{1.2}
\]

\[
 \mathcal Y_L={K_L+a_{L,x}+a_{L,y},
                  K_L+a_{L,y}+a_{L,z},
                  K_L+a_{L,z}+a_{L,x}}.             \tag{1.3}
\]

Both orientations of the alternating (C_6) use exactly (1.2)--(1.3),
once each.  One orientation transfers the three petals around the cycle

\[
                         x\longrightarrow y\longrightarrow z
                           \longrightarrow x,                         \tag{1.4}
\]

and the other reverses all arrows.  Thus for every unordered pair in
(L), one of the three (L)-petals is deleted permanently on one strand
and inserted permanently on the other.

The phrase *fresh reservoir* means that an (L)-petal is not an active
petal of any (M)-router with (M\ne L).  A strand outside (L) may
still change its membership in an (L)-petal by an auxiliary monotone
exchange.  Those auxiliary changes are precisely what the theorem below
counts.

## 2. One transferred petal gives one betweenness constraint

For a line (M), write (t(M)in{1,ldots,7}) for its position in the
chosen order.  Fix

\[
                         L={x,y,z},qquad p\notin L.                 \tag{2.1}
\]

Let (L_{px}), (L_{py}), (L_{pz}) be the unique Fano lines through
the indicated pairs.  They are three distinct lines, all different from
(L).

### Lemma 2.1 (betweenness)

Suppose the (L)-router transfers an (L)-petal from (x) to (y).
If strand (p) never changes membership in this petal, then

\[
 t(L) 	ext{lies strictly between} t(L_{px}) 	ext{and} t(L_{py}).
                                                                        \tag{2.2}
\]

#### Proof

Call the transferred coordinate (a).  Immediately before the
(L)-router,

\[
                         a\in x,qquad a\notin y,                      \tag{2.3}
\]

and immediately after it,

\[
                         a\notin x,qquad a\in y.                     \tag{2.4}
\]

The changes are permanent by Johnson geodesicity.

At the (L_{px})-router, (a) is not an active petal because reservoirs
are fresh.  Its membership must therefore agree on the entire common
core, in particular on strands (p) and (x).  Hence the constant value
of (a) on (p) is

\[
 \mathbf1_{a\in p}=
 \begin{cases}
 1,&t(L_{px})<t(L),\\
 0,&t(L_{px})>t(L).
 \end{cases}                                                         \tag{2.5}
\]

The same argument at (L_{py}), using (2.3)--(2.4) on (y), gives

\[
 \mathbf1_{a\in p}=
 \begin{cases}
 0,&t(L_{py})<t(L),\\
 1,&t(L_{py})>t(L).
 \end{cases}                                                         \tag{2.6}
\]

Equations (2.5)--(2.6) agree exactly when one of (L_{px},L_{py}) occurs
before (L) and the other after it.  This is (2.2). (square)

## 3. The Fano precedence contradiction

### Theorem 3.1 (one auxiliary flip for every outside incidence)

For every pair ((p,L)) with (p\notin L), strand (p) must change
membership in at least one coordinate of the reservoir (A_L).

#### Proof

Assume instead that all three (L)-petal memberships are constant on
(p).  Orient the (L)-router as the directed cycle
(x\to y\to z\to x); the reverse orientation gives the same three
unordered constraints.  Lemma 2.1 says that (t(L)) lies strictly
between each of

\[
 ig(t(L_{px}),t(L_{py})ig),qquad
 ig(t(L_{py}),t(L_{pz})ig),qquad
 ig(t(L_{pz}),t(L_{px})ig).                       \tag{3.1}
\]

No real number lies between every pair of three distinct real numbers:
after ordering them (r_1<r_2<r_3), being between (r_1,r_2) requires
(t(L)<r_2), while being between (r_2,r_3) requires (t(L)>r_2).
This contradiction proves that at least one (A_L)-membership changes on
(p). (square)

The theorem is purely an incidence/precedence statement.  Allowing an
upper vertex to be reused, or changing the exterior collars, does not
remove it.

### Corollary 3.2 (pointwise rank-five lower bound)

Every physical strand in a fresh-reservoir Fano closure performs at least
five petal exchanges.  Consequently rank (3) and rank (4) are
impossible.

#### Proof

A Fano point (p) belongs to three router lines and is outside the other
four.  Its three router incidences force three active-petal exchanges.

For each of the four lines (L\not\ni p), Theorem 3.1 forces a membership
flip on (p) in a coordinate of (A_L).  The four reservoirs are
disjoint.  One Johnson exchange flips at most two such memberships—one
deletion and one insertion—so these four flips require at least two
additional exchanges.  They cannot be merged with the three router
exchanges, whose deleted and inserted petals belong to reservoirs of
lines containing (p), whereas the four forced flips belong to lines
not containing (p).  Thus

\[
                         3+\left\lceil\frac42\right\rceil=5          \tag{3.2}
\]

petal exchanges are necessary on every strand. (square)

The extremal stages sharpen this further.

### Lemma 3.3 (an extreme line costs three flips)

Let (L) be the first or the last router line in the seven-stage order.
For every (p\notin L), strand (p) must change membership in all three
coordinates of (A_L).

#### Proof

Assume first that (L) is earliest.  The three lines
(L_{px},L_{py},L_{pz}) all occur after (L).  For every directed petal
transfer in the (L)-cycle, the two comparison lines therefore lie on
the same side of (L).  Lemma 2.1 says that the corresponding petal
cannot remain constant on (p).  The three directed transfers use the
three distinct coordinates of (A_L), so all three memberships change.
The latest-line case is identical with time reversed. (square)

### Corollary 3.4 (six strands have rank at least six)

At least six of the seven Fano strands perform at least six petal
exchanges.

#### Proof

Fix the earliest line (L_-).  If (p\notin L_-), Lemma 3.3 forces three
flips from (A_{L_-}), while Theorem 3.1 forces at least one flip from
each of the other three lines not containing (p).  These are six flips
in disjoint reservoirs, hence at least three auxiliary Johnson exchanges.
Together with the three mandatory router exchanges, (p) uses at least
six.

The same conclusion holds for every point outside the latest line
(L_+).  Two distinct Fano lines meet in one point, so

\[
 |(P\setminus L_-)\cup(P\setminus L_+)|
 =4+4-2=6.                                             \tag{3.3}
\]

Thus six strands need at least six exchanges. (square)

For a point \(p\), define

\[
 a_p=\min\{t(M):p\in M\},\qquad
 c_p=\max\{t(M):p\in M\},
\tag{3.4}
\]

and

\[
 e_p=(a_p-1)+(7-c_p).
\tag{3.5}
\]

Thus \(e_p\) is the number of lines outside the closed time interval
spanned by the three router lines containing \(p\).

### Lemma 3.5 (span-refined flip count)

Strand \(p\) has at least

\[
 4+2e_p
\tag{3.6}
\]

auxiliary fresh-reservoir membership flips, and hence at least

\[
 5+e_p
\tag{3.7}
\]

total petal exchanges.

#### Proof

There are four lines \(L\not\ni p\).  If \(t(L)\) lies strictly between
\(a_p\) and \(c_p\), the three comparison times in (3.1) straddle \(L\)
and at least one of its three petal memberships must flip.  If
\(t(L)<a_p\) or \(t(L)>c_p\), all three comparison times lie on one side
of \(L\), so Lemma 3.3's argument forces all three memberships to flip.
Thus the baseline is four flips, with two additional flips for every
outside-span line, proving (3.6).

The reservoirs are disjoint and one auxiliary Johnson exchange realizes
at most two required flips.  Since \(4+2e_p\) is even, at least
\(2+e_p\) auxiliary exchanges are necessary.  Adding the three mandatory
router exchanges proves (3.7). \(\square\)

### Theorem 3.6 (equal-length rank at least seven)

Every equal-length fresh-reservoir Fano packet has port rank/length at
least seven.

#### Proof

The quantity \(a_p-1\) counts the number of initial line positions before
the first line containing \(p\).  Hence

\[
 \sum_{p\in P}(a_p-1)
 =\sum_{r=1}^{6}
   \#\{p:\text{the first }r\text{ lines omit }p\}.
\tag{3.8}
\]

The first line leaves four points uncovered.  Two Fano lines meet in one
point, so the first two lines have union size five and leave two points
uncovered.  All later summands are nonnegative.  Therefore

\[
 \sum_p(a_p-1)\ge4+2=6.
\tag{3.9}
\]

Applying the same argument to the reversed order gives

\[
 \sum_p(7-c_p)\ge6.
\tag{3.10}
\]

Consequently

\[
 \sum_p e_p\ge12.
\tag{3.11}
\]

Some point has \(e_p\ge\lceil12/7\rceil=2\).  Lemma 3.5 forces that
strand to make at least \(5+2=7\) petal exchanges.  Equal length forces
all strands to have length at least seven. \(\square\)

The bound does **not** assert that rank seven suffices.  At equality all
forced flips must pair optimally into monotone exchanges, while the seven
\(X/Y\) shores remain disjoint.  That is the next finite problem if this
lane is retained.

## 4. Why complete-ledger closure is all-depth neutral

The Fano obstruction above concerns existence.  There is an independent
issue concerning usefulness.

Let a layered flag atlas have, at every lower rank (r), a multiset
(mathcal V_r) of (r)-sets and, at every intervening upper rank, a
multiset (mathcal U_r).  A router switch changes only the incidences
which join these vertices.  Call a closed packet *complete-ledger
preserving* if before and after the switch

\[
                         mathcal V_r'=mathcal V_r,qquad
                         mathcal U_r'=mathcal U_r                    \tag{4.1}
\]

as literal multisets at every phase of every completed flag.

### Theorem 4.1 (all-depth neutrality)

A complete-ledger-preserving closed packet leaves every depth load vector
unchanged:

\[
                         \mu_q'(S)=\mu_q(S)
                  \qquad\text{for all }q,S.                           \tag{4.2}
\]

Consequently it leaves unchanged

\[
 L_q, U_q, O_q, M_q, P_q, E_q, K_q                            \tag{4.3}
\]

and every statistic depending only on the depth load vectors.

#### Proof

At depth (q), (mu_q(S)) is exactly the multiplicity of (S) in the
corresponding lower-layer multiset (mathcal V_{m-q}).  Equality (4.1)
therefore gives (4.2) coordinate by coordinate.  Each quantity in (4.3)
is a function of (mu_q), so it is unchanged. (square)

### Corollary 4.2 (role of a closed Fano packet)

Even if a rank-seven \(X/Y\) atlas exists, switching it cannot directly
decrease the MWB objective if the complete atlas is held fixed.  Its only
possible role is as a repackaging primitive which makes a subsequent
*atlas-changing* trade legal.  A claimed direct balancing gain from a
closed tube with identical complete ledgers is necessarily an accounting
error.

This distinguishes two uses of ``same ledger'' that must not be conflated:

1. equality only on the local middle collar preserves exact ownership but
   may allow other depths to change;
2. equality on the fully completed flag atlas forces the all-depth
   neutrality proved above.
