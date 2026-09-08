# The two-sided \(Q_8\) carousel has an exact owner splice and a sparse-seam suspension

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The missing owner-support substitution for the four-stage carousel is
available.  It does not come from independently switching overlay
components.  Instead one splices the four factors by a common four-class
owner phase.

Let

\[
                         C_0,C_1,C_2,C_3                 \tag{0.1}
\]

be the four classes determined, in cyclic Gray order, by the two child
parities in \(Q_8=Q_4^L\times Q_4^R\):

\[
\begin{aligned}
 C_0&=(0,0),&C_1&=(0,1),&
 C_2&=(1,1),&C_3&=(1,0).
\end{aligned}                                          \tag{0.2}
\]

Every carousel factor \(P^{(j)}\) maps \(C_i\) bijectively to
\(C_{i+1}\), independently of \(j\).  Define

\[
 {\cal R}(x)=P^{(i)}(x)\qquad(x\in C_i).              \tag{0.3}
\]

Then \({\cal R}\) is an exact neighbour permutation of all 256 owners.
More strongly, every component of \({\cal R}\) is an isometric
\(C_{16}\).  Thus the four formal frame interfaces of the source theorem
do literalize on one exact owner partition.

This finite splice admits a sparse-seam macro suspension.  Give each of
the eight seam positions in the first half of an \({\cal R}\)-cycle a
disjoint block of \(L\) fresh payload directions.  After the seam edge at
position \(t\), traverse the \(t\)-th payload block.  Raw isometry needs no
extra hypothesis; calling that block a literal fixed-frame payload also
requires the phase compatibility stated below.
The resulting direction word has first half

\[
 w_0,\rho_0,\ w_1,\rho_1,\ \ldots,\ w_7,\rho_7,      \tag{0.4}
\]

where \(|\rho_t|=L\), and its second half repeats (0.4).  It is therefore
an isometric

\[
                         C_{\,16(L+1)}
\]

in dimension \(8+8L\).  The lifted cycles are owner-disjoint, and hence
factor their explicitly declared carrier exactly.

There are 16 seam edges and \(16L\) payload edges on each macrocycle.
At most \(16H\) cyclic starts of an \(H\)-window meet a seam, so the exact
bad-start fraction is at most

\[
                         {H\over L+1}.                \tag{0.5}
\]

Consequently \(H=o(L)\) gives an \(o(1)\) fraction of maximum-depth starts
meeting a seam.  It does not by itself give \(o(W)\) aggregate loss after
summing every \(q\le H\): naive disposal costs
\(\Theta(H^2/L)\) of the carrier mass.  See
MATH_AUDIT_Q8_CAROUSEL_AGGREGATE_SEAM_LOSS_20260726.md.
Away from these starts, every protected window lies wholly inside one
payload segment.  If the inserted payload path carries the existing
fixed-frame decoder **and its endpoint phase is reset correctly**, that
same certificate applies to the embedded window.  With no separate reset,
take \(L\) even so seam parity agrees with the original carousel parity.
The macro theorem does not manufacture payload injectivity or a phase
certificate from an arbitrary order.

This proves the requested local macro-substitution lemma.  It does not
tile the full ambient cube or remove the bottom-wire invariant.  The exact
remaining global task is to pack the displayed carriers owner-disjointly
and make their four payload frames diffuse enough to clear the outer
target cuts.

## 1. A general phasewise owner-splicing lemma

The owner argument is elementary but useful beyond the present \(Q_8\)
cell.

### Lemma 1.1 (phasewise splice)

Let a finite set \(V\) be partitioned as

\[
                         V=C_0\dot\cup\cdots\dot\cup C_{r-1}.
\]

Suppose \(F_0,\ldots,F_{r-1}\) are permutations of \(V\), each satisfying

\[
                         F_j(C_i)=C_{i+1}             \tag{1.1}
\]

for every \(i,j\), with indices modulo \(r\).  Define

\[
                         R(x)=F_i(x)\qquad(x\in C_i). \tag{1.2}
\]

Then \(R\) is a permutation of \(V\).  If all \(F_j\)-edges are edges of
one graph, so are all \(R\)-edges.

#### Proof

For each \(i\), the restriction

\[
                         F_i:C_i\longrightarrow C_{i+1}
\]

is injective.  Equation (1.1) makes it surjective.  The restrictions in
(1.2) therefore give disjoint bijections from the classes \(C_i\) onto
the classes \(C_{i+1}\), which together form a bijection of \(V\).
The edge assertion is immediate. \(\square\)

Notice what this avoids.  No interaction component of two factors is
chosen independently.  The connected sector overlay in Proposition 5.1
of the source theorem is therefore irrelevant to exactness: the splice
uses one complete phase restriction from each factor.

## 2. Application to the four \(Q_8\) shores

Let \(P^{(j)}\), \(j\in\mathbb Z_4\), be the forced crossed factors built
from

\[
                         S_j=SK^j,\qquad
 S=(2\ 4),\quad K=(1\ 2\ 3\ 4).                    \tag{2.1}
\]

All four are exact isometric \(C_{16}\)-factors by the source theorem.

For a state \(x=(u,v)\), put

\[
                         p_L=|u|\pmod2,\qquad
                         p_R=|v|\pmod2.              \tag{2.2}
\]

The four classes in (0.2) have 64 owners each.

### Lemma 2.1 (common four-phase advance)

For every \(j\),

\[
                         P^{(j)}(C_i)=C_{i+1}.       \tag{2.3}
\]

#### Proof

At total even parity the forced crossed map changes one coordinate in
the right child.  Thus

\[
                         (0,0)\mapsto(0,1),
\qquad                   (1,1)\mapsto(1,0).
\]

At total odd parity it changes one coordinate in the left child.  Thus

\[
                         (0,1)\mapsto(1,1),
\qquad                   (1,0)\mapsto(0,0).
\]

This is exactly the cyclic order (0.2), and it is independent of
\(S_j\).  Since \(P^{(j)}\) is a permutation, each restriction is a
bijection. \(\square\)

Lemma 1.1 now proves that (0.3) is an exact neighbour permutation of
\(Q_8\).  The next section proves the nonautomatic part: its cycles are
still isometric.

## 3. Exact direction word of the spliced carousel

Use zero-based parent direction labels in \(\mathbb Z_4\).  In these
labels the parent outgoing direction at phase \(c\) is \(d(c)=c\), the
cycle \(K\) is \(i\mapsto i+1\), and

\[
                         S(i)=-i,\qquad
                         S_j(i)=-(i+j).              \tag{3.1}
\]

The four parent phase classes are the cosets of

\[
 H=\langle e_0+e_2,e_1+e_3\rangle.
\]

Translation by coordinate \(i\) changes a parent phase \(a\) by

\[
                         a\longmapsto
                         a+(-1)^{a+i}.               \tag{3.2}
\]

This is read directly from the quotient cycle

\[
 H,\ e_0+H,\ e_0+e_1+H,\ e_1+H.
\]

Fix an \({\cal R}\)-orbit and choose its origin in \(C_0\).  Write the
two initial parent phases as \(c,c'\), both even.  Applying successively
the shores \(j=0,1,2,3\), formula (3.2) gives

\[
\begin{array}{c|c|c|c}
\text{stage}&\text{moved child}&\text{direction}&
                         \text{new phase pair}\\ \hline
0&R&R(-c)&(c,c'+1)\\
1&L&L(-c'-2)&(c+1,c'+1)\\
2&R&R(1-c)&(c+1,c'+2)\\
3&L&L(-c'-1)&(c+2,c'+2).
\end{array}                                           \tag{3.3}
\]

The next four stages use the same four shores and give

\[
\begin{array}{c|c}
4&R(-c-2)\\
5&L(-c')\\
6&R(-c-1)\\
7&L(1-c').
\end{array}                                           \tag{3.4}
\]

All labels are modulo four.  The right labels in (3.3)--(3.4) are

\[
                         -c,\ 1-c,\ 2-c,\ 3-c,
\]

and the left labels are

\[
                         -c'-2,\ -c'-1,\ -c',\ 1-c'.
\]

Each list is all of \(\mathbb Z_4\).

### Theorem 3.1 (exact owner-support carousel factor)

Every component of \({\cal R}\) is an isometric \(C_{16}\).  Consequently
\({\cal R}\) partitions all 256 \(Q_8\) owners into sixteen such cycles.

#### Proof

Equations (3.3)--(3.4) show that the first eight moves use every one of
the eight cube directions exactly once.  Hence the eighth vertex is the
complement of the starting vertex.  Complementing a \(Q_4\) state adds
\(1111\in H\), so it preserves each parent phase.  The shore rule and
the direction word therefore repeat for the next eight moves.

Thus the direction word is \(\omega\omega\), where \(\omega\) is a
permutation of the eight directions.  Such a walk is a simple isometric
\(C_{16}\): no interval of at most eight moves repeats a direction, the
eight-step displacement is the all-one vector, and the next eight moves
return to the start.  Exact ownership follows from the permutation
property already proved by Lemma 1.1. \(\square\)

This is the missing finite substitution theorem.  Formal port
compatibility alone would not imply it; the common phase advance supplies
permutation exactness, and (3.3)--(3.4) supplies isometry.

## 4. The two-sided interface ledger

Let \(\Xi_j^+\) and \(\Xi_j^-\) be the successor and predecessor frame
labels of shore \(P^{(j)}\).  The source theorem gives

\[
                         \Xi_j^-=\Xi_{j+1}^+          \tag{4.1}
\]

cyclically.

At a state in \(C_j\), the spliced factor leaves along \(P^{(j)}\).
At the next state, in \(C_{j+1}\), the incoming frame is
\(\Xi_j^-\), while the next outgoing carousel shore uses
\(\Xi_{j+1}^+\).  Equation (4.1) says these are literally the same frame.
Thus a phase-compatible payload path inserted between the two seam edges
may remain in that common fixed frame.  Equality of frame labels is not by
itself a payload endpoint-phase certificate.

After four interfaces the label returns to its starting value.  The
eight-edge first half of Theorem 3.1 makes two full turns of this
four-stage frame carousel.  Hence the first-half port and the
complementary second-half port carry the same frame label.

## 5. Sparse-seam macro suspension

Fix \(L\ge1\).  Adjoin eight mutually disjoint payload direction blocks

\[
                         D_0,\ldots,D_7,\qquad |D_t|=L. \tag{5.1}
\]

Choose an order

\[
                         \rho_t=(d_{t,1},\ldots,d_{t,L})
\]

of each \(D_t\).  More generally, \(\rho_t\) may be one path supplied by
a certified fixed-frame payload factor; only its distinct-direction word
is used in the owner and cycle proof below.  Raw isometry holds for every
\(L\).  To regard \(\rho_t\) as inheriting the parity-indexed fixed-frame
ledger with no additional phase reset, require \(L\) even: the seam at
position \(t(L+1)\) then has parity \(t\).  For odd \(L\), a separate exact
phase-reset/port certificate is required.

Let

\[
 C=(x_0,x_1,\ldots,x_{15})
\]

be one \({\cal R}\)-cycle, with seam direction word

\[
                         w_0\cdots w_7w_0\cdots w_7. \tag{5.2}
\]

Starting at \(x_0\) with every payload bit zero, perform

\[
                         w_0,\rho_0,w_1,\rho_1,\ldots,w_7,\rho_7,
\tag{5.3}
\]

then repeat the same word.  In the first copy, each payload block changes
from all zero to all one.  After (5.3), the base and all payload
coordinates have therefore been complemented.  The second copy returns
them all to their starting values.

### Theorem 5.1 (exact sparse-seam macrocycle)

The walk (5.3) repeated twice is an isometric

\[
                         C_{\,16(L+1)}
\]

in \(Q_{8+8L}\).  Applying it to all sixteen \({\cal R}\)-cycles gives
sixteen pairwise owner-disjoint macrocycles, and hence an exact factor of
their union

\[
                         {\cal S}_L\subset Q_{8+8L},
\qquad
                         |{\cal S}_L|=256(L+1).       \tag{5.4}
\]

#### Proof

The first-half word (5.3) contains each of the eight seam directions once
and each of the \(8L\) fresh payload directions once.  It is a permutation
of all \(8+8L\) coordinates.  Repeating it gives the doubled-permutation
criterion for an isometric cycle.

Distinct base \({\cal R}\)-cycles have disjoint vertex sets.  Every lifted
macrocycle projects into its own base cycle, so two lifted supports cannot
meet.  There are sixteen cycles, each of length \(16(L+1)\), proving
(5.4). \(\square\)

The owner-support statement is literal: every owner of \({\cal S}_L\)
occurs once, not fractionally and not once per shore.  The support
\({\cal S}_L\) is part of the construction and is independent of any
subsequent target selection.

## 6. Exact seam-loss bound

Call the sixteen occurrences of the base directions \(w_t\) on one
macrocycle seam edges.  All other edges lie in one of the sixteen
length-\(L\) payload runs.

### Proposition 6.1 (window loss)

For every \(1\le H\le L\), the number of cyclic starts whose next
\(H\) edges contain a seam is at most

\[
                         16H.                       \tag{6.1}
\]

The fraction of such starts on one macrocycle is consequently at most

\[
                         {H\over L+1}.               \tag{6.2}
\]

The same bounds hold for backward windows.

#### Proof

One fixed edge belongs to exactly \(H\) directed cyclic windows of length
\(H\).  A union bound over the sixteen seam edges gives (6.1).  Divide by
the cycle length \(16(L+1)\).  Reversing orientation changes neither
count. \(\square\)

Thus every nonexceptional forward or backward protected window is wholly
contained in one payload segment.  A phase-compatible lower/upper decoder
already certified for that payload path is unchanged by adjoining frozen
base and exterior coordinates.  This is a transfer statement, not a claim
that an arbitrary permutation word has injective literal shadows.
Discarding all seam-meeting starts costs the exact proportion (6.2).

If a family of these carriers contains \(G\) owners, the total number of
discarded directed starts is at most

\[
                         {H\over L+1}\,G.            \tag{6.3}
\]

Choosing \(L/H\to\infty\) makes this \(o(G)\).

## 7. What is and is not proved

The following gates are closed.

1. **Owner substitution.**  Equation (0.3) is one exact permutation of
   all \(Q_8\) owners; no componentwise independence is assumed.
2. **Cycle geometry.**  The splice is an isometric \(C_{16}\)-factor.
3. **Two-sided ports.**  Consecutive shores have identical predecessor
   and successor frame labels.
4. **Long payloads.**  The macrocycles in Theorem 5.1 have one bounded
   seam edge per length-\(L\) payload segment.
5. **Maximum-depth start loss.**  Both orientations lose at most
   \(H/(L+1)\) of their starts at one maximum depth.  Aggregate disposal
   across all depths costs \(O(H^2/L)\), and therefore needs an additional
   seam decoder or global coverage theorem.

Three outer statements do not follow.

1. The \(256(L+1)\)-owner carrier \({\cal S}_L\) is not asserted to tile
   all of \(Q_{8+8L}\).  In particular it is not yet a \(2^r\)-owner CPM
   packet option for \(r=8(L+1)\).  A canonical first-eligible packing,
   packet completion, or another disjoint-carrier theorem is still
   required.
2. The four frames still normalize the inherited bottom-wire system.
   Sparse seams make frame changes cheap, but do not by themselves give
   \(\Omega(H)\) transport across every coordinate cut.
3. A fixed-frame payload decoder controls nonseam windows only.  Literal
   targets created by seam-meeting windows have deliberately been charged
   to (6.3), not decoded.

The positional antipodal pairing is also explicit on each macrocycle.  In the
first-half word

\[
 (w_0,\rho_0,w_1,\rho_1,\ldots,w_7,\rho_7),
\]

the antipodal offset \(4(L+1)\) pairs \(w_t\) with \(w_{t+4}\), and pairs
the \(a\)-th payload direction of \(D_t\) with the \(a\)-th direction of
\(D_{t+4}\).  The first four pairs are the standard \(Q_8\) bottom wires.
Thus all sixteen completed macrocycles share one enlarged *positional*
matching.  If the payload direction fields normalize the corresponding
common phase kernel, this is a genuine statewise bottom matching and the
fixed-frame Gaussian deficit persists.  The positional fact alone does not
constrain an arbitrary payload decoder.

There is also a precise substitution boundary.  Theorem 5.1 constructs
and factors its own carrier.  Replacing a prescribed macrocycle inside an
unrelated pre-existing factor would require equality between that
factor's owner cylinder and \({\cal S}_L\).  Predecessor/successor frame
compatibility alone does not imply this equality.  Thus the theorem is an
exact packet-carrier substitution, not an arbitrary cycle-trade theorem.

The surviving coefficient-one task is now purely global: pack these
carriers on \(W-o(W)\) middle owners, choose their payload frame labels so
that the nonseam windows have \(o(W)\) literal target holes, and charge the
seam windows by (6.3).
