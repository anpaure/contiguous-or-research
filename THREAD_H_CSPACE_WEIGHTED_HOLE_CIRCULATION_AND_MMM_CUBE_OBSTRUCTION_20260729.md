# Thread H: weighted c-space hole circulation and the fixed MMM-cube obstruction

Date: 2026-07-29

Status: exact weighted-integral potential; exact coupling of the lower `q2`
and terminal `q3` decks; exact last-witness augmentation criterion; transparent
`2^5`-case no-go for the five parallel MMM menus selected by the frozen
`k=15` seed; exact autocorrelation obstruction to every pure legal three-end
and three-start cycle on that seed.  This note does **not** obstruct other MMM
gluing-tree changes, coupled start/end boundary circulations, or higher
boundary cycles, and it does not claim that support completion alone solves
the full owner/compiler Hall problem.

## 1. Result

For the frozen resident strict spiral, the `47` lower-`q2` holes represent
`685` missing physical rank-six targets, while the `11` missing rank-five
orbits represent exactly the `165` terminal zero-degree compiler targets.
The exact physical hole potential is therefore

\[
                         \Phi=685+165=850.                 \tag{1.1}
\]

This is not an ad hoc score.  At each depth it is exactly the collision
excess above its unavoidable baseline.  Moreover, the `q2` targets are the
adjacent-union colours of the single rank-five circulation formed by the
`q3` targets.  Thus the two ledgers must be moved by one common chronology.

For any legal move, the change in `Phi` is exactly the physical weight of
last witnesses destroyed minus the physical weight of first witnesses
created.  This gives an exact integral last-witness potential.  For the particular
five-menu MMM cube present in the seed, the baseline is the unique minimum
among unit-voltage, depth-three-resident endpoints: the only other feasible
endpoint has potential `865`.  Hence this whole fixed-menu cube contains no
monotone lower-shadow/compiler augmentation.

The pure boundary-cycle lane is also closed at arity three: all `4,078`
legal pure end cycles and all `4,037` legal pure start cycles violate an
exact middle-deck autocorrelation moment.  The first unclosed run move must
couple starts and ends, combine several defective cycles, or use at least
four boundaries.

## 2. The common rank-five circulation

Put

\[
 k=15,\qquad r=8,\qquad d=3,\qquad
 W=\binom{15}{8}=6435=15N,\qquad N=429.
\]

Let \(\rho\) be cyclic coordinate rotation.  The frozen carrier
\(T=(T_i)_{i\in\mathbb Z_W}\) is a strict voltage-one spiral, so, after choosing the
audited orientation,

\[
                         T_{i+N}=\rho T_i.              \tag{2.1}
\]

Define the lower traces

\[
 P_i^{(q)}=\bigcap_{a=0}^{q}T_{i-a},\qquad q=2,3,        \tag{2.2}
\]

and abbreviate

\[
                         Z_i=P_i^{(2)},\qquad Y_i=P_i^{(3)}.
\]

Depth-three residence gives `|Z_i|=6` and `|Y_i|=5` at every physical
position.

### Lemma 2.1 (literal derivative coupling)

For every `i`,

\[
                         \boxed{Z_i=Y_i\cup Y_{i+1}}.    \tag{2.3}
\]

Consequently `Y` is a cyclic Johnson walk on rank-five sets and the lower
`q2` occurrence at `i` is exactly the union colour of its edge
`Y_iY_(i+1)`.

#### Proof

Both `Y_i` and `Y_(i+1)` are rank-five subsets of

\[
 Z_i=T_i\cap T_{i-1}\cap T_{i-2}.
\]

The first omits from `Z_i` the coordinate inserted on the seam
`T_(i-3)T_(i-2)`; the second omits the coordinate deleted on the seam
`T_iT_(i+1)`.  If those omitted coordinates were equal, that coordinate
would have the internal positive run

\[
                         T_{i-2},T_{i-1},T_i
\]

of length three, contrary to depth-three residence.  The two rank-five
facets of the rank-six set `Z_i` are therefore distinct, and their union is
`Z_i`.  This is the literal `D P^(3)=P^(2)` identity.  \(\square\)

This identity is the first essential obstruction to separate depthwise
Hall arguments: a proposed `q2` rerouting and a proposed `q3` rerouting are
legal together only if they are the edge and vertex decks of the same
rank-five circulation.

## 3. Orbit-normalized loads

For \(q=2,3\), let \(\mathcal O_q\) be the set of \(C_{15}\)-orbits on
\((8-q)\)-subsets.  For \(O\in\mathcal O_q\), write

\[
 w_O=|O|,
 \qquad
 n_q(O)=|\{0\le i<N:[P_i^{(q)}]_\rho=O\}|.             \tag{3.1}
\]

The physical load of each individual target in \(O\) is denoted
\(\lambda_q(O)\).

### Lemma 3.1 (quotient-to-physical load)

Assume more generally that
\(T_{i+N}=\rho^vT_i\) with \(\gcd(v,15)=1\).  Then

For every orbit `O`,

\[
                 \boxed{\lambda_q(O)=\frac{15n_q(O)}{w_O}},
 \qquad
                 \sum_{O\in\mathcal O_q}n_q(O)=N.      \tag{3.2}
\]

#### Proof

The unit-voltage identity also holds for every intersection in (2.2).  The
fifteen lifts of one quotient occurrence traverse the powers
\(1,\rho^v,\ldots,\rho^{14v}\), hence all fifteen rotations
of its target.  An orbit of size `w_O` is traversed uniformly, each member
appearing `15/w_O` times.  Summing over the `n_q(O)` quotient occurrences
gives (3.2).  There is one quotient occurrence at each of the `N` quotient
positions.  \(\square\)

### Lemma 3.2 (the two orbit censuses)

At rank six there are `335` orbits: `333` have size fifteen and two have
size five.  At rank five there are `201` orbits: `200` have size fifteen and
one has size three.

#### Proof

For rank six, the identity rotation fixes `binom(15,6)=5005` sets.  Each of
the two rotations with `gcd(15,t)=5` has five coordinate cycles of length
three and fixes `binom(5,2)=10` rank-six sets.  No other nonidentity
rotation fixes a rank-six set.  Burnside gives

\[
                         \frac{5005+2\cdot10}{15}=335.
\]

Those ten periodic sets have stabilizer exactly the order-three subgroup:
an additional order-five symmetry would generate all of \(C_{15}\), forcing
the subset size to be zero or fifteen.  They therefore form two orbits of
size five.

For rank five, each of the four rotations with `gcd(15,t)=3` has three
coordinate cycles of length five and fixes three rank-five sets.  Other
nonidentity rotations fix none.  Hence

\[
                         \frac{3003+4\cdot3}{15}=201,
\]

The three periodic sets have stabilizer exactly the order-five subgroup by
the same argument, and therefore form one orbit of size three.  \(\square\)

## 4. Exact weighted collision potential

Define the quotient hole count and quotient collision excess by

\[
 h_q=|\{O:n_q(O)=0\}|,
 \qquad
 e_q=\sum_O(n_q(O)-1)_+.                              \tag{4.1}
\]

Define their physical weighted analogues by

\[
 H_q=\sum_{O:n_q(O)=0}w_O,
 \qquad
 C_q=\sum_O w_O(\lambda_q(O)-1)_+.                    \tag{4.2}
\]

### Theorem 4.1 (weighted hole-excess identity)

Let \(M_q=|\mathcal O_q|\) and
\(V_q=\binom{[15]}{8-q}\).  Then

\[
 \boxed{e_q=N-M_q+h_q},                               \tag{4.3}
\]

and

\[
 \boxed{C_q=W-|V_q|+H_q}.                             \tag{4.4}
\]

Thus the collision excess above the unavoidable pigeonhole baseline is
exactly the hole mass, both quotientwise and physically.

#### Proof

If `A_q={O:n_q(O)>0}`, then

\[
 e_q=\sum_{O\in A_q}(n_q(O)-1)
     =N-|A_q|=N-(M_q-h_q).
\]

By (3.2), for an occupied orbit

\[
 w_O(\lambda_q(O)-1)=15n_q(O)-w_O.
\]

Therefore

\[
 C_q=15\sum_O n_q(O)-\sum_{O\in A_q}w_O
     =W-(|V_q|-H_q),
\]

which is (4.4).  \(\square\)

### Corollary 4.2 (the exact frozen-seed ledger)

The quotient-normalized spectra are

\[
\begin{array}{c|l|c|c|c}
q&\text{normalized orbit loads}&h_q&e_q&H_q\\ \hline
2&0^{47}1^{165}2^{105}3^{18}&47&141&685\\
3&0^{11}1^{54}2^{62}3^{49}4^{21}5^4&11&239&165.
\end{array}                                                   \tag{4.5}
\]

At `q2`, the two size-five orbits, represented by `3171` and `5285`, are
both holes; the other `45` holes have size fifteen.  Hence

\[
 H_2=2\cdot5+45\cdot15=685,
 \qquad C_2=(6435-5005)+685=2115.                    \tag{4.6}
\]

At `q3`, the unique size-three orbit, represented by `4681`, has normalized
load one and physical load five.  All eleven holes are full size-fifteen
orbits, with representatives

\[
 157,285,651,661,665,837,1187,1233,1349,1585,2329.    \tag{4.7}
\]

Thus

\[
 H_3=11\cdot15=165,
 \qquad C_3=(6435-3003)+165=3597.                    \tag{4.8}
\]

The asserted combined physical potential is therefore

\[
 (C_2+C_3)-[(6435-5005)+(6435-3003)]
 =H_2+H_3=850.                                       \tag{4.9}
\]

At terminal rank five, the forced-port condition is
\(F_i\subseteq S\subseteq P_i^{(3)}\).  Since
\(|S|=|P_i^{(3)}|=5\), this reduces to \(S=P_i^{(3)}\).  Hence the `165`
missing physical rank-five targets in (4.8)
are exactly the `165` zero-degree terminal compiler targets; no one-core or
matching choice can repair them while the carrier is fixed.

## 5. Last witnesses and exact circulation

Let a legal carrier move send `n_q` to `n'_q`, where both endpoints are
unit-voltage strict spirals and every `q2` and `q3` window has respectively
rank six and rank five (in particular, both endpoints may be
depth-three-resident).  Define

\[
 G_q=\{O:n_q(O)=0<n'_q(O)\},
 \qquad
 L_q=\{O:n_q(O)>0=n'_q(O)\}.                          \tag{5.1}
\]

These are the first witnesses gained and last witnesses lost.

### Theorem 5.1 (exact last-witness identity)

For each depth,

\[
 e'_q-e_q=|L_q|-|G_q|,                                \tag{5.2}
\]

and

\[
 C'_q-C_q=H'_q-H_q
 =\sum_{O\in L_q}w_O-\sum_{O\in G_q}w_O.             \tag{5.3}
\]

In particular:

1. the move is support-monotone at both depths exactly when
   \(L_2=L_3=\varnothing\);
2. such a move is a strict augmentation exactly when at least one of
   `G_2,G_3` is nonempty;
3. without support monotonicity, the physical potential decreases exactly
   when the total weight of gained first witnesses exceeds the total weight
   of destroyed last witnesses.

#### Proof

Equations (5.2) and (5.3) follow by subtracting (4.3) and (4.4), since all
other terms are state-independent.  The three characterizations are then
literal translations of the definitions.  \(\square\)

There is also an exact multi-move formulation.  Let `B` be a bank of
physically compatible, commuting collision-neutral bundles, and let
\(\delta_{b,q,O}\) be the fully recomputed net change of \(n_q(O)\) caused by
bundle `b`.  Additivity is assumed only for this compatible bank; overlapping
halos must first be evaluated as a single composite bundle.  A selection
\(x_b\in\{0,1\}\) completes both supports if and only if

\[
 \boxed{
 n_q(O)+\sum_{b\in B}x_b\delta_{b,q,O}\ge1
 \quad(q=2,3,\ O\in\mathcal O_q).}                    \tag{5.4}
\]

Equivalently, every orbit has donor capacity `n_q(O)-1` against net removal.
This is the exact common two-depth conditional `0-1` feasibility system.  It
is not by itself a network circulation, an annealed covariance, or a
separate depthwise matching.

For an elementary bank in which each independently installable and
position-compatible move
transfers one quotient occurrence from one donor orbit to one hole and has
no other load effect, (5.4) is an ordinary capacitated bipartite flow.
Max-flow/min-cut gives the exact criterion

\[
 |X|\le\sum_{D\in N(X)}(n_q(D)-1)                     \tag{5.5}
\]

for every set `X` of holes.  This positive Hall theorem does **not** apply
automatically to 3-cycle or MMM bundles, because one selected bundle couples
several transfers at both depths.

The failure of separate Hall tests is already integral.  Consider two
service holes `h_1,h_2`, two unit-capacity `q2` donors `a_1,a_2`, two
unit-capacity `q3` donors `b_1,b_2`, and the four bundles

\[
 (h_1,a_1,b_1),\ (h_1,a_2,b_2),\
 (h_2,a_1,b_2),\ (h_2,a_2,b_1).                       \tag{5.6}
\]

Each deck separately has a perfect Hall assignment, but every pair serving
both holes repeats either an `a` donor or a `b` donor.  Assigning weight
`1/2` to all four bundles is fractionally feasible.  The submatrix on rows
`h_1,a_1,b_1,b_2` is

\[
 \begin{pmatrix}
 1&1&0&0\\1&0&1&0\\1&0&0&1\\0&1&1&0
 \end{pmatrix},
 \qquad \det=2.                                      \tag{5.7}
\]

Thus no total-unimodularity or separate-Hall conclusion is available
without an additional balanced/laminar property of the *actual* c-space
bundle catalogue.

## 6. MMM locality and the all-hole capacity cut

An MMM parallel switch changes the gluing across one quotient seam while
retaining all quotient blocks.  A lower window changes only when it crosses
that seam.  Therefore one switch changes at most

\[
                     2\text{ quotient `q2` cells},
 \qquad             3\text{ quotient `q3` cells}.     \tag{6.1}
\]

### Proposition 6.1 (all-hole Hall shore)

After changing `s` distinct parallel seams from the frozen seed, at most
`2s` of the original `47` missing `q2` orbits can gain first witnesses.
Consequently

\[
 h'_2\ge47-2s,
 \qquad
 H'_2\ge685-30s.                                     \tag{6.2}
\]

In particular, completing `q2` by parallel MMM switches requires at least

\[
                         \left\lceil47/2\right\rceil=24
                                                                  \tag{6.3}
\]

changed seams.

#### Proof

Every newly covered old hole needs a changed quotient cell whose new label
is that hole.  Distinct hole orbits require distinct cells.  The union of
the changed `q2` cells has size at most `2s` by (6.1), proving the first
bound.  Every target orbit has physical size at most fifteen, so those cells
can remove at most `30s` physical units of the old weighted deficit; losses
of old last witnesses can only increase the new deficit.  \(\square\)

This is a genuine Hall capacity cut on the full missing shore.  The bound
is specific to parallel seam switches.  A run-end 3-cycle can have long
support, so (6.1)--(6.3) must not be transferred to that move class.

## 7. Exact obstruction in the selected five-menu cube

Keep the frozen quotient necklace order and every selector except the five
parallel menus below.  Bit zero is the frozen choice and bit one is its
parallel alternative:

\[
\begin{array}{c|c|c|c}
\text{bit}&\text{selector}&0&1\\ \hline
0&0&(127,7,10)&(127,10,14)\\
1&175&(1807,7,12)&(1807,11,12)\\
2&316&(3179,4,13)&(3179,4,8)\\
3&380&(4699,7,14)&(4699,13,14)\\
4&384&(4717,4,14)&(4717,4,8).
\end{array}                                                   \tag{7.1}
\]

There are only `32` assignments.  Exactly `15` have unit voltage.  Their
complete support/residence summary is:

\[
\begin{array}{c|r|r|r|r|r}
b_0b_1b_2b_3b_4&v&\text{residence defects}&h_2&h_3&\text{upper holes}\\ \hline
00000&1&0&47&11&95\\
01000&8&0&47&12&94\\
11000&7&15&48&13&94\\
01100&13&30&47&12&92\\
00010&13&15&48&11&95\\
11010&4&30&49&13&94\\
10110&2&60&49&12&93\\
00001&4&15&47&12&95\\
01001&11&15&47&13&94\\
10101&8&60&48&13&93\\
01101&1&45&47&13&92\\
00011&1&30&48&12&95\\
01011&8&30&48&13&94\\
11011&7&45&49&14&94\\
01111&13&60&48&13&92.
\end{array}                                                   \tag{7.2}
\]

### Theorem 7.1 (fixed five-menu MMM no-go)

Among all unit-voltage, depth-three-resident states of the five-menu cube
(7.1), the frozen state is the unique minimizer of each of

\[
 h_2+h_3,\qquad h_2+H_3,\qquad H_2+H_3.               \tag{7.3}
\]

The only other feasible state is the single switch

\[
                 (1807,7,12)\longrightarrow(1807,11,12).       \tag{7.4}
\]

It preserves the entire `q2` missing family, fills no `q3` hole, and destroys
the last witness of the full size-fifteen `q3` orbit represented by `1159`.
Thus its three potentials in (7.3) change respectively as

\[
 58\longrightarrow59,\qquad
 212\longrightarrow227,\qquad
 850\longrightarrow865.                               \tag{7.5}
\]

In particular, no sequence confined to this cube can end at a resident
unit-voltage carrier that is a monotone lower support augmentation of the
seed.

#### Proof

The exact `32`-assignment replay gives the exhaustive unit-voltage table
(7.2).  Its only residence-zero rows are `00000` and `01000`.  Literal
comparison of those two rows gives identical `q2` missing representatives;
the second `q3` missing set is the first union `{1159}`.  Orbit `1159` has
size fifteen.  Equations (7.3)--(7.5) and uniqueness follow.  Since every
endpoint of every switch sequence within the fixed cube is one of the same
`32` assignments, allowing infeasible intermediate assignments cannot
create a third feasible endpoint.  \(\square\)

The switch (7.4) does gain upper orbit `1951` and loses no upper orbit.  This
does not offset the terminal lower loss: upper support and lower/compiler
support are separate mandatory gates.  In particular, an annealer that
rewards the upper gain while omitting terminal `q3` can move in the wrong
direction for the compiler.

## 8. Pure boundary 3-cycles are also closed

The five-menu obstruction leaves open MMM switches outside that cube.  The
most immediate scalar run-algebra alternative can, however, be ruled out
completely on the same carrier.

Use the persistent coordinate trace \(c\in\{0,1\}^W\) with

\[
                         T_j=\{x:c_{j-xN}=1\}.          \tag{8.1}
\]

For \(1\le s\le7\), define the rotation-invariant pair moment

\[
 a_s(T)=\sum_{x\in\mathbb Z_{15}}
          \mathbf1_{\{x,x+s\subseteq T\}},             \tag{8.2}
\]

and the scalar lag autocorrelation

\[
 A_s(c)=\sum_{p\in\mathbb Z_W}c_pc_{p-sN}.             \tag{8.3}
\]

### Lemma 8.1 (middle-deck moment obstruction)

One has

\[
                         A_s(c)=\sum_{j=0}^{N-1}a_s(T_j).       \tag{8.4}
\]

If \(T_0,\ldots,T_{N-1}\) contain exactly one representative of every
rotation orbit of rank-eight sets, then necessarily

\[
                         \boxed{A_s(c)=\binom{13}{6}=1716}     \tag{8.5}
\]

for every \(1\le s\le7\).

#### Proof

Expanding (8.2) using (8.1) and putting \(p=j-xN\) gives (8.4), because
the pairs \((j,x)\) index every \(p\in\mathbb Z_W\) once.  All rank-eight
rotation orbits have size fifteen since \(\gcd(15,8)=1\).  Rotating one
representative through its orbit and then ranging over all quotient
representatives therefore ranges over every rank-eight set once.  For each
of the fifteen ordered coordinate pairs \((x,x+s)\), exactly
\(\binom{13}{6}\) rank-eight sets contain that pair.  Since \(a_s\) is
rotation-invariant, division by the orbit size fifteen yields (8.5).
\(\square\)

Now unwrap the \(N=429\) positive runs of \(c\) as
\([S_i,E_i]\).  A **pure end 3-cycle** fixes every start and cyclically
reassigns the end residues of three distinct runs.  On this seed, receiver
\(i\) can receive donor \(j\) at the unique lift

\[
 E'_i\equiv E_j\pmod N,
 \qquad
 E'_i\in[S_i+3,S_{i+1}-2].                            \tag{8.6}
\]

The three endpoint shifts must sum to zero.  These conditions are necessary
and sufficient for the pure move to preserve the endpoint transversal,
total weight, minimum run length four, and nonempty gaps.  A **pure start
3-cycle** is the dual operation with all ends fixed and

\[
 S'_i\equiv S_j\pmod N,
 \qquad
 S'_i\in[E_{i-1}+2,E_i-3],                            \tag{8.7}
\]

again with zero total shift.

### Theorem 8.2 (fixed-seed pure 3-cycle no-go)

On the frozen `k=15` trace there are exactly `4,078` legal pure end
3-cycles and `4,037` legal pure start 3-cycles.  None preserves the middle
necklace deck.  More precisely, the least lag \(s\le5\) at which (8.5)
fails has the following exhaustive census:

\[
\begin{array}{c|rrrrr}
 &s=1&s=2&s=3&s=4&s=5\\ \hline
\text{pure ends}&3601&412&56&7&2\\
\text{pure starts}&3612&366&55&4&0.
\end{array}                                                   \tag{8.8}
\]

#### Proof

For each receiver, the verifier scans the literal interval (8.6) or (8.7).
Each interval has length below \(N\), so a donor residue has at most one
legal lift.  It enumerates every directed cycle on three distinct receivers
and retains exactly the zero-total-shift cycles.  For every retained cycle it
rebuilds all `6,435` bits, independently revalidates total weight, all run
and gap bounds, both boundary-residue transversals, and all residue-class
rank sums.  It then computes (8.3) literally.  The two rows of (8.8) sum to
`4,078` and `4,037`; there is no unwitnessed row.  Lemma 8.1 therefore rules
out middle-deck exactness for every candidate.  \(\square\)

The persistent trace in this audit is exactly the cyclic reversal of the
coordinate-zero trace reconstructed from the MMM fixture:

\[
                         c^{\rm run}_p=c^{\rm MMM}_{-p}.        \tag{8.9}
\]

The weighted-hole replay asserts (8.9) bit by bit.  Under (8.1), it implies

\[
                     T_j^{\rm run}=-T_{-j}^{\rm MMM},           \tag{8.10}
\]

so the two presentations differ by cyclic-order reversal together with the
coordinate relabeling \(x\mapsto-x\).  These operations exchange pure start
and pure end moves and preserve middle-deck exactness and all moment tests.
Thus Theorem 8.2 applies to the same carrier up to this explicit relabeling.
It also reconciles the previously recorded `4,037` pure-end census in the
MMM orientation with the `4,037` pure-start row in the reversed orientation.

There is a further exact additive obstruction for those `4,037` MMM-oriented
pure-end moves.  Let

\[
             \Sigma(g)=(\Delta M(g),\Delta L_1(g))             \tag{8.11}
\]

be the signed middle/q1 orbit-load signature.  The frozen meet-in-the-middle
audit checks all

\[
                         \binom{4037}{2}=8{,}146{,}666
\]

unordered pairs and finds no zero singleton, no inverse pair, and no pair
whose negative is a catalogue singleton.  Hence no set of at most three
distinct catalogue moves has signed sum zero.  In particular, a
q1-halo-disjoint additive repair using this pure-end catalogue needs at
least four moves.  This conclusion does not apply to the other `4,078`
boundary class or to overlapping sequential moves, whose signatures are
nonlinear.

The theorem is deliberately scoped.  It does not rule out:

1. a coupled move changing starts and ends simultaneously;
2. a zero-sum composite of several individually defective boundary cycles;
3. a cycle on four or more boundaries;
4. an MMM switch outside the five-menu cube or a gluing-tree change.

Every remaining candidate must first satisfy the exact middle/q1 kernel

\[
 \sum_j(\mathbf e_{\mu'_j}-\mathbf e_{\mu_j})=0,
 \qquad
 \sum_j(\mathbf f_{\lambda'_j}-\mathbf f_{\lambda_j})=0,       \tag{8.12}
\]

and in particular all moment equations (8.5), before its joint
\(\delta_{q,O}\) signature may enter (5.4).

The smallest exact replacement lemma is now:

> **Unproved coupled-boundary common-circulation lemma.**  The frozen seed
> admits a physically compatible collection of coupled start/end or
> higher-boundary moves satisfying (8.10), preserving depth-three
> residence, and whose fully recomputed signatures satisfy (5.4)
> simultaneously for every `q2` and `q3` orbit.

The aggregate donor totals `e_2=141>47` and `e_3=239>11` do not obstruct
this lemma, but subset adjacency cuts may do so even one deck at a time.
The determinant-two bundle (5.6)--(5.7) explains why aggregate or separate
depthwise feasibility does not prove a common integral selection.

Even a proof of this support lemma would settle only the zero-degree and
lower-shadow gates.  The resulting carrier would still require the full
one-core owner/compiler Hall audit.

## 9. Reproducibility

The new transparent replay is

```text
scratch/audit_k15_cspace_weighted_hole_mmm_cube_20260729.py
SHA-256 e14f24f5b9b7b967906c4e0b61bb35d46ce788c2609a1e1d3167f8044df82585
```

It enumerates only the `32` assignments in (7.1), reconstructs each physical
cycle through the repository quotient catalogue, recomputes residence and
all lower loads literally, verifies the normalized and physical numerical
ledgers used in (4.3)--(4.4), and asserts every claim in Theorem 7.1.  Its
frozen inputs are

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
  4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10
scratch/graded_quotient_pipeline.py
  a364a0e48e1f35dc9610436adf3e841f16290b883f12308de04dfce728fa8fda
scratch/extract_mmm_gluing_family.py
  f54d3840221857e02be4c82574704ee3e4a4884ae213c0728c30ba8010fafe67
scratch/k15_runtrans_seed_3eac_20260729.cw
  7dd31950ffd69eea819d5ea413feb66f1d32bc1d88fe206a2b11faf26c1fd332
```

Theorem 8.2 is certified independently by

```text
scratch/audit_k15_cspace_pure_boundary_3cycles_20260729.py
  57803b5ea0b981475485c3a5408ad563d3acd4e3d9df20ef954f439c418e94f9
scratch/k15_cspace_pure_boundary_3cycles_20260729.audit.json
  d56484d55e7d7875031b01efdcbd5cd118ec2e627f9a01655b55c36d667ba436
```

The compact certificate is derived from verifier stdout and augmented with
the verifier hash.  It records both complete cycle counts, both
first-violated-lag histograms, checksums of the distributions of the first
violated lag and its signed delta, and the logical bit-vector hash
`ddeb2de0106340d10f1a265c08c7843123357c080625bc92d3d37b62d93e8885`.
Its `3eac...` original-raw field is a historical recorded hash and is not
used as a verified premise; the retained file's checked raw hash is the
listed `7dd...`, while logical identity is enforced by `ddeb...`.
The exhaustive run was performed on the allowed H100 CPU; no heavy local
search was used.  The local `2^5` replay and source audits take only a few
seconds.

The independent structural sources are:

```text
MATH_ATLAS_STRICT_SPIRAL_RUNTRACE_SOLUTIONS_20260729.md
MATH_THEOREM_RUN_TRANSVERSAL_CSPACE_MARKOV_BASIS_AND_TWO_DECK_TRADES_20260729.md
MATH_THEOREM_MMM_PARALLEL_SWITCH_CSPACE_SHEAR_AND_K15_ESCAPE_20260729.md
MATH_THEOREM_STRICT_SPIRAL_THREE_RUN_CYCLE_OBSTRUCTION_20260729.md
MATH_THEOREM_K15_THREE_CYCLE_SIGNATURE_ARITY_FOUR_20260729.md
```

The additive arity-four lower bound uses the frozen result

```text
scratch/k15_three_cycle_mitm_remote_20260729/k15_three_cycle_signature_mitm.result.json
  324eec348c33b7eaeb49ad72b68de56900f1b0d5dcdd4d7c2e7eb5f4da693327
```
