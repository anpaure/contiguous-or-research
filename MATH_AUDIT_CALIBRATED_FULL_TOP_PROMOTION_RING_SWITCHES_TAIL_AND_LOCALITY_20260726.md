# Calibrated full-top promotion rings: exact tag filling, forced-tail automaticity, and the local-switch obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
\tag{0.1}
\]

Let \(H\) be the least positive integer such that

\[
                         \lambda_H\ge M:=m+H.
\tag{0.2}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=(1+o(1)){W\over m},
\tag{0.3}
\]

and the exact overshoot bound is

\[
 0\le W-MN_H<{2(H-1)\over M-1}W.
\tag{0.4}
\]

This note audits the proposal to choose one full-top promotion ring at
every top, delete one chain from every ring, and use exact local switches to
obtain an approximate SCD with the forced long-tail history.

The positive local conclusion is stronger than the scalar count suggests.
Let

\[
                         D:=W-(M-1)N_H.
\tag{0.5}
\]

There is a depth

\[
                         q_*=O(\sqrt H)
 =O(m^{1/4}(\log m)^{1/4})=o(m^{1/3})
\tag{0.6}
\]

and an exact tag assignment to all \((M-1)N_H\) retained ring chains such
that:

* every tag count at \(q\ge q_*\) is the exact SCD count;
* all tag deficits lie below \(q_*\), have total \(D\), and create at most
  \[
                         2q_*D
        =O\left({WH^{3/2}\over m}\right)=o(W)
  \tag{0.7}
  \]
  signed shallow holes; and
* one retained chain in every ring has tag \(H\), so the rings give
  exactly \(N_H=o(W/H)\) promotion paths.

Consequently, if one can choose the cyclic orders, deleted phases, and
this tag assignment so that all retained truncated chain masks are
pairwise disjoint, then the literal word length is \(W+o(W)\).  This is a
complete conditional theorem, with no further tag, reset, exterior-tail,
or forced-history gate.

Indeed, the coherent forced-tail requirement becomes automatic.  In every
such legal ring atlas, for each fixed

\[
                         0<b<\sqrt{\log2},
\]

the ring paths themselves have total forced-tail overlap at least

\[
 \boxed{
  \left(\int_0^b(2e^{-x^2}-1)\,dx+o_b(1)\right)W\sqrt m.}
\tag{0.8}
\]

A positive density of their edges therefore has shifted lower/upper tail
agreement of length \(\Theta_b(\sqrt m)\).  The forced-tail theorem is not
an extra obstruction after a mask-disjoint tagged ring atlas has been
selected.

The exact obstruction is global selection, not local ring legality.

1. A single adjacent swap is a legal ring switch and preserves the tag
   census, but changes at most two target occurrences at each rank and at
   most two middle owners.  After \(K\) such switches,
   \[
     {1\over2}\|\mu_r'-\mu_r\|_1\le2K
     \tag{0.9}
   \]
   at every rank.  If the average number of swaps per top is \(k=o(m)\),
   the middle defect changes by only \(o(W)\).  If
   \(k=o(m/H)\), the complete central-band defect changes by only \(o(W)\).
   In particular, perturbing an independent topwise catalogue, which has
   \((e^{-1}+o(1))W\) middle holes, needs \(\Omega(W)\) swaps, or average
   \(\Omega(m)\) per ring.

2. The \((M-1)\)-window middle packet of a repaired ring determines the
   cyclic order, the deleted phase, and every untagged flag family up to
   dihedral symmetry.  Thus, after middle ownership is fixed, the only
   genuine fixed-top freedom is tag reassignment.

3. Swapping tags \(d<e\) on two fixed ring phases is exactly legal inside
   that ring catalogue.  It preserves the middle packet and every tag
   count and changes precisely the active chain choice at depths
   \(d<q\le e\).  Its total two-sign half-\(\ell^1\) action is at most
   \(2(e-d)\).  Hence tag flow is real, but it cannot repair a
   middle-owner collision and can create cross-top outer collisions unless
   coordinated with other rings.

4. Fixed-top adjacent-swap rectangles remain only signed rank selectors.
   In a one-ring-per-top owner packing, every exact fixed-top rectangle
   combination which also preserves the retained middle family in each
   affected top reduces to the same repaired ring on both sides, up to
   reversal and tag reassignment.  Its purported untagged rank-isolating
   effect is zero.  Deleted phases can mediate owner transfer between tops;
   that genuinely nonlocal case is not covered.  The bounded-segment rectangle is
   literal, but it uses multiple truncated segments and lies outside the
   one-ring catalogue.  A successful owner-preserving absorber must use
   genuine cross-top owner transfers.

Thus the promotion-ring route survives positively, but not as a local heat
or small-surgery theorem.  The remaining exact object is a globally
mask-disjoint selection of one repaired ring per top, together with nested
tag-independent sets; local rectangles cannot manufacture it from a
catalogue with a macroscopic middle defect.

## 1. Calibration and the one-hole capacity

The calibrated packet theorem gives

\[
 1\le{\lambda_H\over M}
 <{M-1\over m-H+1}
 =1+O(H/m).
\tag{1.1}
\]

Equations (0.3)--(0.4) follow.  From (0.5),

\[
 D=N_H+(W-MN_H),
\tag{1.2}
\]

and therefore

\[
 N_H\le D
 <N_H+{2(H-1)\over M-1}W
 =O\left({HW\over m}\right)=o(W).
\tag{1.3}
\]

Fix a top \(U\in\binom{[2m]}M\) and a cyclic order of \(U\).  The exact
promotion-ring theorem gives \(M\) saturated chain collars on one directed
lookahead-\(H\) promotion cycle.  Arbitrary tags in \([0,H]\) may be
assigned, subject only to at most one tag \(H\).  The corresponding
truncated chains are pairwise mask-disjoint inside the ring.

Delete one ring chain.  The remaining \(M-1\) chains form one directed
promotion path.  Choose one of them as the unique tag-\(H\) chain.  Doing
this at every one of the \(N_H\) tops gives

\[
 T=(M-1)N_H=W-D
\tag{1.4}
\]

chain slots and exactly \(N_H\) paths.  Their path ratio is

\[
 {N_H\over W/H}={H\over\lambda_H}\le{H\over M}=o(1).
\tag{1.5}
\]

All statements so far are local and exact.  Rings at different tops may
still collide; no global packing is inferred.

## 2. Exact low-tag absorption of the calibration deficit

For \(0\le d<H\), put

\[
                         \gamma_d=N_d-N_{d+1}.
\tag{2.1}
\]

These are the exact numbers of SCD chains of native radius \(d\).  The
clipped tag-\(H\) census is \(N_H\), and

\[
                         \sum_{d=0}^{H-1}\gamma_d=W-N_H.
\tag{2.2}
\]

Let \(q_*\) be the least integer with

\[
                         W-N_{q_*}\ge D.
\tag{2.3}
\]

### Lemma 2.1 (the deficit is confined below \(O(\sqrt H)\))

\[
                         \boxed{q_*=O(\sqrt H).}
\tag{2.4}
\]

#### Proof

Uniformly for \(q=o(\sqrt m)\),

\[
 {N_q\over W}=1-{q^2\over m}
 +O\left({q^4+q^2\over m^2}\right).
\tag{2.5}
\]

By (1.3), \(D/W\le(2+o(1))H/m\).  Taking
\(q=2\lceil\sqrt H\rceil\) in (2.5) gives

\[
                         W-N_q=(4+o(1)){HW\over m}>D
\]

for all sufficiently large \(m\).  Minimality proves (2.4). \(\square\)

Since

\[
 \sum_{d=0}^{q_*-1}\gamma_d=W-N_{q_*}\ge D,
\tag{2.6}
\]

choose integers

\[
 0\le\delta_d\le\gamma_d\quad(0\le d<q_*),
 \qquad
 \sum_{d<q_*}\delta_d=D.
\tag{2.7}
\]

Assign exactly \(\gamma_d-\delta_d\) retained ring slots tag \(d<q_*\),
exactly \(\gamma_d\) slots tag \(q_*\le d<H\), and one slot in every
ring tag \(H\).  The number of lower-tag slots used is

\[
 \sum_{d<H}(\gamma_d-\delta_d)
 =W-N_H-D=(M-2)N_H,
\tag{2.8}
\]

which is exactly the available number.

For \(q<q_*\), put

\[
                         \Delta_q=\sum_{d=q}^{q_*-1}\delta_d.
\tag{2.9}
\]

At either rank \(m-q\) or \(m+q\), the number of selected chains is

\[
 \begin{cases}
 N_q-\Delta_q,&1\le q<q_*,\\
 N_q,&q_*\le q\le H.
 \end{cases}
\tag{2.10}
\]

At the middle rank it is \(W-D=T\).

### Theorem 2.2 (calibrated repaired-ring implication)

Suppose the cyclic orders, deleted phases, and tag placement above can be
chosen so that all retained chain masks are pairwise distinct at every
rank they reach.  Then one literal word covers every nonempty Boolean mask
and has length \(W+o(W)\).

#### Proof

Pairwise distinctness and (2.10) imply exact coverage at every signed depth
\(q_*\le q\le H\), and exactly \(\Delta_q\) holes at each sign for
\(q<q_*\).  Compile the \(N_H\) promotion paths.  Append the \(D\) missing
middle masks, the shallow signed holes, and all masks outside radius \(H\).
The resulting length is at most

\[
\begin{aligned}
 L\le{}&T+2HN_H+D
       +2\sum_{q=1}^{q_*-1}\Delta_q
       +2\sum_{q>H}N_q\\
 ={}&W+2HN_H
       +2\sum_{d=1}^{q_*-1}d\delta_d
       +2\sum_{q>H}N_q.
\end{aligned}
\tag{2.11}
\]

The reset term satisfies

\[
                         HN_H\le{HW\over M}=o(W).
\tag{2.12}
\]

By (1.3) and Lemma 2.1,

\[
 \sum_{d<q_*}d\delta_d
 \le q_*D
 =O\left({WH^{3/2}\over m}\right)=o(W),
\tag{2.13}
\]

because \(H=(1+o(1))\sqrt{m\log m}\).  Finally the exact ratio

\[
 {N_{q+1}\over N_q}={m-q\over m+q+1}
\]

gives

\[
                         \sum_{q>H}N_q=O(W/H)=o(W).
\tag{2.14}
\]

Substitution in (2.11) proves the theorem. \(\square\)

The global hypothesis in Theorem 2.2 is exactly an approximate SCD/tagged
ring factorization.  The theorem proves that its permissible tag deficit
is much larger than zero but still costs only \(o(W)\): exact SCD census
at every tag is not required.

## 3. Forced-tail agreement is automatic after global legality

Use the \(N_H\) ring paths from Theorem 2.2 as one directed path forest on
the \(T=W-D\) retained chains.  For \(q\ge q_*\), exactly \(N_q\) of its
vertices have tag at least \(q\).  Let \(e_q\) be the number of path edges
whose two endpoints both have tag at least \(q\).

### Lemma 3.1 (threshold-run count on the ring forest)

\[
                         \boxed{
 e_q\ge(2N_q-T-N_H)_+.}
\tag{3.1}
\]

#### Proof

Mark the high-tag vertices on each of the \(N_H\) paths.  Their number of
nonempty runs is at most the number \(T-N_q\) of low-tag vertices plus the
number of paths.  A high run on \(s\) vertices contributes \(s-1\)
high--high edges.  Therefore

\[
 e_q\ge N_q-(T-N_q+N_H)=2N_q-T-N_H.
\]

Take the positive part. \(\square\)

Every edge of a repaired ring path is a literal full-radius promotion of
lookahead \(H\).  If both endpoint tags are at least \(q\), global
mask-disjointness makes their two rank-\((m+q)\) masks distinct.  The exact
central-truncation theorem therefore turns the edge into a genuine
radius-\(q\) rotor.  Equivalently, its forced lower/upper tail pairs agree
after the required one-step shift through threshold \(q\).

Fix \(0<b<\sqrt{\log2}\) and put \(B=\lfloor b\sqrt m\rfloor\).
Since \(q_*/\sqrt m\to0\), uniform local limits and (3.1) give

\[
\begin{aligned}
 \sum_{q=q_*+2}^{B}e_q
 &\ge\sum_{q=q_*+2}^{B}(2N_q-T-N_H)\\
 &=\left[
   \int_0^b(2e^{-x^2}-1)\,dx+o_b(1)
   \right]W\sqrt m.
\end{aligned}
\tag{3.2}
\]

For large \(m\), every summand before the equality is positive because
\(2e^{-b^2}-1>0\), while \(D+N_H=o(W)\).  The left side is exactly the
total forced-tail weight, truncated at \(B-q_*-1\).  This proves (0.8).

Put

\[
                         \kappa_b=\int_0^b(2e^{-x^2}-1)\,dx.
\]

Since a path edge has truncated weight at most
\((b+o(1))\sqrt m\), the same averaging argument as in the coherent-tail
theorem shows that at least

\[
 \boxed{
  \left({\kappa_b\over2b-\kappa_b}-o_b(1)\right)W}
\tag{3.3}
\]

edges have tail agreement of length at least
\((\kappa_b/2)\sqrt m\).

Thus the forced-tail theorem supplies a consistency audit, not a new gate,
for a legal promotion-ring atlas.  Separate forests are unnecessary: the
actual ring paths themselves witness its full coherent weight.

## 4. Exact catalogue-local moves

### 4.1 Adjacent order swaps

Swap two adjacent labels in the cyclic order of one repaired ring, keeping
the deleted phase and the tag on every phase fixed.  The new object is again
one exact repaired promotion ring: the promotion-ring theorem applies to
every cyclic order, and the tag restriction is unchanged.

This is local legality only.  The new masks may collide with chains in
other tops, so an adjacent swap is a move of a globally legal atlas only
when those external conflicts are absent or are simultaneously routed
around a cross-top alternating circuit.

At any proper rank, an adjacent swap changes only the two cyclic windows
whose boundary separates the swapped positions.  Restricting to retained
and tag-active phases can only delete changed windows, never add more.

### Proposition 4.1 (statewise adjacent-swap locality)

If two tagged repaired-ring atlases are related by \(K\) adjacent order
swaps in total, then at every rank \(r\),

\[
 \boxed{
 {1\over2}\|\mu_r'-\mu_r\|_1\le2K.}
\tag{4.1}
\]

Their middle-hole counts differ by at most \(2K\), and the sum of their
hole counts over the complete central band differs by at most

\[
                         (4H+2)K.
\tag{4.2}
\]

#### Proof

One swap deletes at most two old target occurrences and inserts at most
two new ones at a fixed rank, giving half-\(\ell^1\) distance at most two.
Sum by the triangle inequality.  A hole functional on two integer load
vectors of equal total mass is one-Lipschitz in half-\(\ell^1\):

\[
 \left|\sum_T(1-x_T)_+-\sum_T(1-y_T)_+\right|
 \le{1\over2}\|x-y\|_1.
\]

The tag census is fixed by the swaps, so the two load vectors have equal
mass at every rank.  There are \(2H+1\) central ranks. \(\square\)

If the average number of swaps per top is at most \(k\), then

\[
 K\le kN_H=(1+o(1)){kW\over m}.
\tag{4.3}
\]

Consequently

\[
 k=o(m)\Longrightarrow
 \text{middle-hole change}=o(W),
\tag{4.4}
\]

and

\[
 k=o(m/H)\Longrightarrow
 \text{aggregate central-hole change}=o(W).
\tag{4.5}
\]

These statements hold for every switch sequence, with no randomness.

For comparison, choose the cyclic order and deleted phase independently
and uniformly at every top.  A fixed middle owner is retained in any one
containing top with the full-packet probability multiplied by
\((M-1)/M\).  The sum of these probabilities is

\[
                         {(M-1)N_H\over W}=1-o(1),
\]

and the individual probabilities are \(o(1)\).  Therefore its uncovered
probability is \(e^{-1}+o(1)\), and the expected middle-hole count is

\[
                         (e^{-1}+o(1))W.
\tag{4.6}
\]

Any realization with \(\varepsilon W\) middle holes needs at least
\((\varepsilon/2-o(1))W\) adjacent swaps before it can have only the
forced \(D=o(W)\) holes.  This is average \(\Omega(m)\) swaps per top.

### 4.2 Tag transpositions

Fix the cyclic order and deleted phase.  Interchange tags \(d<e\) on two
retained phases.  This is always a legal operation in the one-ring
catalogue: Theorem 3.6's within-ring disjointness holds for every tag
assignment with one tag \(H\), and the global tag census is unchanged.
It is not automatically a legal move of an already globally
mask-disjoint atlas, because a newly activated outer mask may collide with
another top.

At depths \(q\le d\), both chains are active before and after the switch.
At depths \(d<q\le e\), exactly one is active and its identity is exchanged.
At depths \(q>e\), neither is active.

### Proposition 4.2 (exact tag-flow action)

A tag transposition \(d<e\):

1. fixes the complete middle-owner vector;
2. fixes every global tag count;
3. changes no signed rank outside \(d<q\le e\); and
4. has total two-sign half-\(\ell^1\) action at most
   \[
                              \boxed{2(e-d).}
   \tag{4.7}
   \]

Thus tag flow is the full fixed-skeleton catalogue mechanism for changing
outer-rank loads.  Turning it into a repair of a global atlas requires an
alternating cross-top circuit.  It can never repair a middle-owner hole or
collision.

## 5. One-hole middle-packet rigidity

The usual middle-packet theorem says that all \(M\) cyclic middle windows
determine the cyclic order up to reversal.  Deleting one window does not
destroy this rigidity.

### Theorem 5.1 (one-hole packet reconstruction)

Assume

\[
                         2\le H<M/2.
\tag{5.1}
\]

Fix a top \(U\).  The unlabelled family of \(M-1\) retained length-\(m\)
windows of a repaired promotion ring determines:

1. the cyclic order of \(U\), up to rotation and reversal;
2. the missing length-\(m\) window; and
3. every untagged cyclic interval family at every rank.

#### Proof

Complement the retained middle windows inside \(U\).  They become
\(M-1\) cyclic \(H\)-intervals.  Join two when their intersection has size
\(H-1\).  Since \(2H<M\), two distinct cyclic \(H\)-intervals have such
an intersection exactly when their starts are consecutive.  The graph on
all \(M\) intervals would be \(C_M\); after one interval is deleted, the
recovered graph is the path \(P_{M-1}\).

Traverse that path, in either direction, as

\[
                         I_1,I_2,\ldots,I_{M-1}.
\]

If the unknown cyclic word is \(c_0,c_1,\ldots,c_{M-1}\), with the missing
interval indexed by zero, then

\[
 I_j\setminus I_{j+1}=\{c_j\},\qquad
 I_{j+1}\setminus I_j=\{c_{j+H}\}
 \quad(1\le j\le M-2).
\tag{5.2}
\]

The first differences recover indices \(1,\ldots,M-2\).  The second
recover indices

\[
 H+1,\ldots,M-1,0,1,\ldots,H-2
 \quad\pmod M.
\]

Together these are every cyclic position.  Hence the word and then the
missing interval are determined.  Reversing the recovered path reverses
the word, and choosing an initial position rotates it; these are the only
ambiguities.  Every interval family is dihedrally invariant. \(\square\)

### Corollary 5.2 (classification of fixed-middle local freedom)

Two repaired rings in one top with the same retained middle-owner family
have the same untagged chain skeleton, up to reversal.  Therefore every
fixed-top local overlay preserving that family can change the clipped SCD
only by reassigning tags among the recovered chain phases.

This qualification is essential: middle-packet rigidity does not recover
the tags.  Proposition 4.2 describes exactly the remaining tag freedom.

## 6. Why fixed-top rectangles do not yield the global packing

Two disjoint adjacent swaps in one cyclic order produce the exact
four-order rectangle.  Its signed interval incidence vanishes at every
length except the two cut separations, and it generates the complete
point-neutral integer lattice at the exceptional rank.  These algebraic
facts remain valid at the calibrated scale.

They do not define a legal move on a one-ring-per-top owner packing.
The two full packets on either rectangle diagonal share at least \(M-4\)
middle owners.  More generally, every sum of fixed-top nonmiddle
rectangles preserves the complete middle vector separately in each top.

### Theorem 6.1 (fixed-top rectangle rigidity in the repaired-ring atlas)

Consider an integral combination of fixed-top adjacent-swap rectangles.
Suppose that after cancellation:

1. each sign contains at most one repaired ring in every top;
2. both signs are middle-owner packings; and
3. in every affected top the retained middle-owner family is the same on
   the two signs.

Then its untagged interval effect is zero at every rank.  Any remaining
effect is a tag reassignment of Proposition 4.2, not a rank-isolating
rectangle effect.

#### Proof

Apply Theorem 5.1 in every affected top.  The positive and negative cyclic
orders agree up to dihedral symmetry and have the same missing phase.
Dihedral symmetry preserves every untagged interval family.  Only the tag
labels, which are absent from the rectangle identity itself, may differ.
\(\square\)

The bounded-segment rectangle remains a valid literal overlay: one full
baseline order plus at most three short promotion segments realizes one
rank square with \(M+O(Q)\) occurrences and at most four paths on a band
of width \(Q\).  It is not one repaired ring and therefore is not a local
move in the catalogue audited here.  Its middle multiset is preserved, so
it cannot repair a pre-existing middle defect.  It is at most a terminal
outer-rank absorber after the owner packing and tag flow are already
available.

A genuinely useful rectangle circuit must transfer owners between
different tops.  The existing owner-transfer theorem then forces an
Eulerian circulation in the distance-\(H\) top graph, with point-balanced
owner flow at every top and capacity \(H-d(U,V)+1\) on a directed top
pair.  No such global circuit is constructed here.

## 7. Exact global gate and audited boundary

For fixed repaired-ring skeletons, tag assignment has a concise exact
form.  At each depth \(q\), let \(G_q\) be the collision graph on retained
chain phases: two phases are adjacent when their rank-\((m-q)\) or
rank-\((m+q)\) masks coincide.  A tag assignment is legal precisely when
the nested active sets

\[
 A_H\subseteq A_{H-1}\subseteq\cdots\subseteq A_0
\tag{7.1}
\]

are independent in \(G_q\) and have the prescribed sizes from (2.10).
The set \(A_H\) must contain exactly one phase in every top.  This nested
independent-set system, together with middle-owner disjointness at
\(q=0\), is the exact integral grouping problem.

Proved here:

1. one deleted chain per calibrated top leaves \(W-D=W-o(W)\) exact ring
   slots and \(N_H=o(W/H)\) paths;
2. all capacity loss can be charged to tags below
   \(q_*=O(\sqrt H)=o(m^{1/3})\), with exact signed-hole cost
   \(O(WH^{3/2}/m)=o(W)\);
3. a globally mask-disjoint tagged repaired-ring atlas gives a literal
   \(W+o(W)\) word;
4. the same actual ring paths automatically realize the full coherent
   Gaussian forced-tail weight and a positive density of
   \(\Theta(\sqrt m)\)-agreement edges;
5. exact adjacent order swaps and tag transpositions stay inside the
   one-ring catalogue, with the statewise locality bounds (4.1)--(4.7),
   but need cross-top coordination to preserve global mask-disjointness;
6. one-hole middle-packet rigidity and the resulting classification of
   fixed-middle local freedom; and
7. the fixed-top rectangle no-go inside the one-ring owner packing.

Not proved:

1. no globally mask-disjoint selection of one repaired ring per top is
   constructed;
2. no nested active-set/tag assignment solving (7.1) is constructed for a
   nontrivial global skeleton;
3. owner-changing cross-top rectangle circuits remain possible;
4. the bounded-segment rectangle may still be useful as an \(o(W)\)
   terminal absorber after a near-solution; and
5. coefficient one is not claimed unconditionally.

The tuned promotion-ring route is therefore viable but genuinely global.
Its tag and forced-tail ledgers close automatically once the mask-disjoint
ring atlas exists.  Neither bounded adjacent-swap surgery nor fixed-top
rank rectangles can create that atlas from a catalogue with linear middle
defect.
