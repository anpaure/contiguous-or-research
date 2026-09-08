# Global portals after DRAY: an exact width-budget construction and its remaining fusion cost

Date: 2026-07-25

## 0. Verdict

The quadratic three-box obstruction does **not** make global portal sharing
empty.  There is an exact construction at precisely the scale left open by
the audited cross-box theorem.

Let (k=3s) be even, split the Boolean coordinates into three (s)-sets,
and fix arbitrary symmetric-chain decompositions in the three blocks.  Their
products partition the Boolean cube into three-chain boxes.  Put

\[
 W=\binom{k}{k/2}.
\]

For every fixed \(\varepsilon>0\), and all sufficiently large \(k\), there is
a literal nonzero Boolean OR word of length at most \(\varepsilon W\), divided
into

\[
 \Theta_\varepsilon\!\left(\frac{W}{\sqrt k}\right)
\]

blocks, such that:

1. every block has one distinguished right endpoint;
2. suffixes ending there represent a saturated central Boolean chain;
3. within each distinguished endpoint, the designated targets lie in
   distinct product boxes; relative to all selected target occurrences,
   the aggregate repeated-box loss is (O(W/\sqrt k)); and
4. the total number of distinct endpoint--box incidences is at least
   \(\gamma\varepsilon W\), for an absolute \(\gamma>0\).

Thus a width-budget word can contain a linear amount of useful cross-box
sharing concentrated in only (Theta(W/\sqrt k)) high-degree physical
endpoints.  Every interval certificate is explicit.

There is a matching lower bound on the number of such endpoints.  All targets
used in the audited dominant-box endpoint ledger lie in a central band of
radius (O(\sqrt k)).  Since the suffix unions at one endpoint form a chain,
one endpoint can meet at most one target in each rank.  Hence its product-box
degree is (O(\sqrt k)), and the forced (Omega(W)) sharing needs

\[
 \boxed{\Omega(W/\sqrt k)\text{ shared endpoints}.}
\]

The construction is therefore scale-sharp as an endpoint-incidence theorem.
It also shows why high-degree singleton activity in the projection ledger is
not the main difficulty: literal endpoint chronology can be supplied.

What it does **not** do is cover the whole cube in (W+o(W)) positions.  In
the construction below, the arms of the isolated portal blocks cost one
position per represented chain level.  They consume (Theta(W)) positions
while designating only (Theta(W/\sqrt k)) common flag endpoints.  Appending
them to an already width-scale middle word would therefore cost linear
order.  To finish the global route, those arm positions must be organized
to supply the middle-owning updates of the principal word as well; the
present construction makes no such incidental-coverage claim.
Equivalently, one needs a stateful MTF/rotor fusion of the portal flags with
only (o(W)) resets.

This note proves the portal construction and the sharp endpoint count.  It
does not prove the constant-one conjecture.

No web search or computation is used.

---

## 1. Product boxes and internal covers

Write the coordinate partition as

\[
 [k]=X_1\sqcup X_2\sqcup X_3,
 \qquad |X_i|=s.
\]

Fix an SCD \(\mathcal D_i\) of (2^{X_i}).  A factor chain has the form

\[
 C_0\subset C_1\subset\cdots\subset C_p,
 \qquad C_t=C_0\cup\{e_1,\ldots,e_t\}.
 \tag{1.1}
\]

A triple of factor chains is a product box

\[
 \mathcal B=C^{(1)}\times C^{(2)}\times C^{(3)}.
 \tag{1.2}
\]

The boxes partition (2^{[k]}).

Call a Boolean cover (S\lessdot T) **internal** when (S,T) belong to the
same product box.  If (S) lies in a fixed box, then that box contains at
most three upper covers of (S): in each factor chain there is at most one
next state.  Dually it contains at most three lower covers of (T).

The following slightly stronger observation will also be useful.

### Lemma 1.1 -- one-box upper-neighbour bound

Let (S\subseteq[k]), and let \(\mathcal B\) be a product box.

* If (S\in\mathcal B), at most three upper neighbours of (S) lie in
  \(\mathcal B\).
* If (S\notin\mathcal B), at most one upper neighbour of (S) lies in
  \(\mathcal B\).

#### Proof

The first statement is the preceding internal-cover observation.

For the second, suppose two distinct upper neighbours (S+x) and (S+y)
belong to the same box.  If (x,y) lie in the same coordinate block, their
block components are two distinct sets of the same rank in one factor
chain, impossible.  If they lie in different blocks, membership of (S+x)
in the box shows that the unchanged (y)-block component of (S) lies in
its factor chain; membership of (S+y) gives the same conclusion for the
(x)-block.  Every other block component is unchanged in both sets.  Thus
all three block components of (S) lie in the three factor chains, so
(S\in\mathcal B), a contradiction. \(\square\)

This lemma already gives a single high-degree portal without probability.
Starting in a central rank, after visiting (j) distinct boxes, at most
(j+2) upper neighbours return to one of them.  Since a central set has
(\Theta(k)) upper neighbours, one may greedily build a saturated chain of
length (O(\sqrt k)) which visits a new product box at every step.  Section
4 gives its literal common-endpoint word.  The stronger aggregate theorem
below produces enough such incidence at the width scale.

### Corollary 1.2 -- one collision-free global flag

Let \(S_a\) have rank \(a\), and let \(L\ge0\) satisfy

\[
 k-a>2L+1.
 \tag{1.3}
\]

Then \(S_a\) extends to a saturated chain

\[
 S_a\subset S_{a+1}\subset\cdots\subset S_{a+L}
 \tag{1.4}
\]

whose \(L+1\) members lie in \(L+1\) distinct product boxes.

#### Proof

Suppose \(S_a,\ldots,S_{a+t}\) have already been chosen in distinct boxes,
where \(t<L\).  By Lemma 1.1, among the upper neighbours of \(S_{a+t}\),
at most three return to its present box and at most one enters each of the
other \(t\) previously visited boxes.  Thus at most \(t+3\) neighbours are
forbidden.  There are \(k-a-t\) upper neighbours in total.  From (1.3),

\[
 k-a-t>2L+1-t\ge t+3
\]

for \(t\le L-1\).  A neighbour in a new box is therefore available.
Induction proves (1.4). \(\square\)

In particular, a central flag of every fixed \(O(\sqrt k)\) length can be
made perfectly collision-free.

---

## 2. A relabeled global SCD has almost no box collisions

Fix any SCD \(\mathcal E\) of the full Boolean cube (2^{[k]}).  It has
exactly (W) chains, one through every middle-layer set.  Let

\[
 m=k/2,
 \qquad
 I_H=\{m-H,m-H+1,\ldots,m+H\},
 \tag{2.1}
\]

where (H\le k/12).

For a coordinate permutation \(\sigma\), a chain (D\in\sigma\mathcal E),
and a product box \(\mathcal B\), put

\[
 n_{D,\mathcal B}
 =\#\{S\in D:|S|\in I_H,\ S\in\mathcal B\}.
 \tag{2.2}
\]

Define the same-box collision count

\[
 \operatorname{Col}_H(\sigma\mathcal E)
 =\sum_{D\in\sigma\mathcal E}\sum_{\mathcal B}
   \binom{n_{D,\mathcal B}}2.
 \tag{2.3}
\]

### Theorem 2.1 -- global SCD collision theorem

For every (H\le k/12), some coordinate relabeling of \(\mathcal E\)
satisfies

\[
 \boxed{
 \operatorname{Col}_H(\sigma\mathcal E)
 \le C\,\frac{HW}{k}}
 \tag{2.4}
\]

for an absolute constant (C).  In particular, for fixed (A) and
(H=\lceil A\sqrt k\rceil),

\[
 \operatorname{Col}_H(\sigma\mathcal E)
 =O_A(W/\sqrt k)=o(W).
 \tag{2.5}
\]

#### Proof

Choose \(\sigma\) uniformly.  Fix a comparable pair (S\subset T) in one
chain of \(\mathcal E\), with

\[
 |S|=r,
 \qquad |T|=r+d.
\]

Conditioned on \(\sigma S\), the set \(\sigma T\) is uniform among the
\(\binom{k-r}{d}\) rank-((r+d)) supersets of \(\sigma S\).

The point \(\sigma S\) lies in one product box.  A point of that same box
which is (d) ranks higher is obtained by advancing a total of (d) steps
among the three factor chains.  A weak composition of (d) into three
parts determines at most one such point.  Therefore

\[
 \Pr(\sigma S,\sigma T\text{ lie in one product box})
 \le
 \frac{\binom{d+2}{2}}{\binom{k-r}{d}}.
 \tag{2.6}
\]

For fixed ranks (r,r+d), the SCD contains at most (W) pairs lying on a
common chain.  Hence

\[
 \mathbb E\operatorname{Col}_H(\sigma\mathcal E)
 \le
 W\sum_{r=m-H}^{m+H-1}
   \sum_{d=1}^{m+H-r}
 \frac{\binom{d+2}{2}}{\binom{k-r}{d}}.
 \tag{2.7}
\]

Put (K=k-r\).  Here (K\ge k/2-H\ge5k/12).  If

\[
 a_d=\frac{\binom{d+2}{2}}{\binom Kd},
\]

then

\[
 \frac{a_{d+1}}{a_d}=\frac{d+3}{K-d}.
 \tag{2.8}
\]

Uniformly for the displayed range (d\le2H\), the last ratio is at most
(3/4) once (k) is large; increasing the absolute constant handles the
remaining finite (k).  Since (a_1=3/K=O(1/k)),

\[
 \sum_{d=1}^{2H}a_d=O(1/k).
 \tag{2.9}
\]

There are at most (2H+1) choices of (r).  Thus the expectation in
(2.7) is (O(HW/k)), and some relabeling attains that bound. \(\square\)

### Remark 2.2 -- fixed-dimensional generalization

Nothing in the collision argument is special to three blocks.  For a
product partition coming from any fixed number \(b\) of block SCDs, the
number of same-box rank-\(d\) extensions of one point is at most

\[
 \binom{d+b-1}{b-1}.
\]

The analogue of (2.8) is

\[
 \frac{a_{d+1}}{a_d}=\frac{d+b}{K-d}.
\]

Therefore, for every fixed \(b\), some relabeling of a global SCD has
central-band same-box collision count

\[
 O_b(HW/k).
\]

The three-block hypothesis enters only when we restrict incidence to the
specific positive-density DRAY target family in Section 3.

### Corollary 2.3 -- distinct-box incidence of the band flags

For the relabeled SCD in Theorem 2.1, let

\[
 \ell_D=\#\{S\in D:|S|\in I_H\},
 \qquad
 d_D=\#\{\mathcal B:D\cap\mathcal B\cap I_H\ne\varnothing\}.
 \tag{2.10}
\]

Then

\[
 \boxed{
 \sum_D d_D
 \ge
 \sum_{r=m-H}^{m+H}\binom kr
 -C\frac{HW}{k}.}
 \tag{2.11}
\]

Indeed, for every integer (u\ge1), (u-1\le\binom u2).  Therefore

\[
 \ell_D-d_D
 =\sum_{\mathcal B}(n_{D,\mathcal B}-1)_+
 \le\sum_{\mathcal B}\binom{n_{D,\mathcal B}}2.
\]

Sum this inequality over (D) and use (2.4).

For fixed (A>0) and (H=\lceil A\sqrt k\rceil), central-binomial ratios
give a constant (c_A>0) such that

\[
 \sum_{r=m-H}^{m+H}\binom kr
 \ge c_A(2H+1)W.
 \tag{2.12}
\]

Thus the (W) global SCD flags have total product-box degree

\[
 \sum_Dd_D=\Theta_A(W\sqrt k).
 \tag{2.13}
\]

This is much larger than the linear sharing forced by the DRAY cross-box
ledger.

---

## 3. The incidence can be restricted to the audited target family

The preceding theorem counts all central-band masks.  It also applies to
the exact target family used in the cross-box endpoint theorem.

Take the dominant chain-height windows from the audited construction:

\[
 p,q\in[\sqrt s,1.1\sqrt s],
 \qquad
 r\in[3\sqrt s,3.1\sqrt s].
 \tag{3.1}
\]

For every such product box, select its full plateau slab.  For every other
box, select its local middle layer.  Call the resulting Boolean target
family \(\mathcal T\).

All targets in \(\mathcal T\) lie in a central band (I_H) with
(H\le\sqrt k), for all sufficiently large (k=3s).  Indeed, the plateau
half-width is

\[
 \frac{r-p-q}{2}\le0.55\sqrt s<\sqrt k.
\]

The exact SCD height histogram and the central-binomial comparison already
used in the audited cross-box theorem give an absolute \(\tau>0\) such that

\[
 \boxed{|\mathcal T|\ge\tau W\sqrt k.}
 \tag{3.2}
\]

Only the positivity of \(\tau\) matters.  Explicitly, a fixed positive
fraction of the three-block boxes lies in (3.1), each such box has
(w=\Theta(k)) points in each of (Theta(\sqrt k)) plateau ranks, the
number of boxes is \(\Theta(W/k)\), and these masks are disjoint.

For a fully numerical ledger, let

\[
 \kappa_L=e^{-1/2}-e^{-121/200},
 \qquad
 \kappa_H=e^{-9/2}-e^{-961/200}.
\]

The numbers of factor chains in the low and high windows are respectively
\((\kappa_L+o(1))W_s\) and \((\kappa_H+o(1))W_s\).  Every dominant box has
at least \(s\) points in each of at least \(0.7\sqrt s\) plateau layers.
Also

\[
 \frac{sW_s^3}{W}\longrightarrow\frac{2\sqrt3}{\pi},
 \qquad
 \frac{s^{3/2}W_s^3}{W\sqrt k}\longrightarrow\frac2\pi.
\]

Thus (3.2) holds, for example, with any fixed

\[
 0<\tau<\frac{1.4}{\pi}\kappa_L^2\kappa_H
\]

after increasing the threshold in \(s\).

For one global SCD chain (D), let

\[
 d_D(\mathcal T)
 =\#\{\mathcal B:D\cap\mathcal B\cap\mathcal T\ne\varnothing\}.
 \tag{3.3}
\]

The collision count in Theorem 2.1 dominates collisions after restriction
to \(\mathcal T\).  Hence

\[
 \boxed{
 \sum_Dd_D(\mathcal T)
 \ge\tau W\sqrt k-O(W/\sqrt k).}
 \tag{3.4}
\]

Thus the global SCD flags supply the right kind of incidences, not merely
activity in irrelevant boxes.

---

## 4. Literal common-endpoint portals

We now turn each selected global SCD flag into an actual Boolean word.

Let the part of a saturated chain in the band be

\[
 S_a\subset S_{a+1}\subset\cdots\subset S_b,
 \qquad |S_t|=t.
 \tag{4.1}
\]

Put

\[
 E_t=S_t\setminus S_{t-1}
 \qquad(a<t\le b).
\]

Every (E_t) is a singleton.  Emit the block

\[
 \boxed{
 E_b,E_{b-1},\ldots,E_{a+1},S_a.}
 \tag{4.2}
\]

It is nonzero because (a=m-H>0).  For every (a\le t\le b), the suffix
of (4.2) beginning at (E_t), with the evident one-term convention at
(t=a), has union

\[
 S_a\cup E_{a+1}\cup\cdots\cup E_t=S_t.
 \tag{4.3}
\]

Thus every band point of the chain is represented by a suffix ending at the
single final position of the block.  Concatenating such blocks does not
destroy any certificate.

### Theorem 4.1 -- width-budget global portal word

There are absolute constants \(\tau,\gamma>0\) with the following property.
For every fixed (0<\varepsilon\le1), and all sufficiently large even
(k=3s), there is a literal nonzero word \(\mathcal P_\varepsilon\) of
length at most \(\varepsilon W\) and a set of

\[
 P=\Theta_\varepsilon(W/\sqrt k)
 \tag{4.4}
\]

distinguished right endpoints such that suffix witnesses ending at those
endpoints give at least

\[
 \boxed{\gamma\varepsilon W}
 \tag{4.5}
\]

distinct endpoint--product-box incidences belonging to the selected target
family \(\mathcal T\).

#### Proof

Use Theorem 2.1 with (H=\lceil\sqrt k\rceil), and order the (W) global
SCD chains so that (d_D(\mathcal T)) is nonincreasing.  Put

\[
 P=\left\lfloor\frac{\varepsilon W}{2H+1}\right\rfloor.
 \tag{4.6}
\]

The average of the largest (P) values is at least the average of all (W)
values.  By (3.4),

\[
 \sum_{i=1}^{P}d_{D_i}(\mathcal T)
 \ge
 \frac{P}{W}
 \left(\tau W\sqrt k-O(W/\sqrt k)\right)
 \ge\gamma\varepsilon W
 \tag{4.7}
\]

for some absolute \(\gamma>0\).

Encode the band segment of each selected chain by (4.2) and concatenate the
blocks.  Each block has at most (2H+1) entries, so (4.6) gives total length
at most \(\varepsilon W\).  Formula (4.3) is the literal interval
certificate.  The definition of (d_D(\mathcal T)) counts each product box
only once at one endpoint, exactly as required. \(\square\)

For later use, the selected family may be thinned to genuinely
high-incidence flags without changing its order of magnitude.  Indeed,
\(d_D(\mathcal T)\le \ell_D\le2H+1\), while (4.7) and (4.6) say that the
average selected degree is at least a fixed positive multiple of (H).
Discarding flags below half that average leaves
\(\Theta_\varepsilon(W/\sqrt k)\) flags, each of degree and hence band
length \(\Theta(\sqrt k)\), with \(\Theta(\varepsilon W)\) total incidence
(after changing the absolute constants).

This theorem realizes, rather than merely counts, the high-degree endpoint
escape.  Its scale is not an artifact of the proof; the next section gives
the matching lower bound.

---

## 5. A sharp rank-span obstruction to sparser global portals

At one right endpoint (j), the suffix unions

\[
 A_j\subseteq A_{j-1}\cup A_j\subseteq\cdots\subseteq
 A_1\cup\cdots\cup A_j
 \tag{5.1}
\]

form an inclusion chain.  Therefore one endpoint represents at most one
distinct mask in each rank.

### Theorem 5.1 -- central-band endpoint cap

Let all selected targets have ranks in

\[
 m-H,m-H+1,\ldots,m+H.
\]

Then every physical endpoint belongs to at most (2H+1) selected
endpoint--box incidences on either the left or the right.  Consequently, if

\[
 \mathcal C_\partial
 =\sum_j\bigl((\ell_j-1)_++(r_j-1)_+\bigr)
 \tag{5.2}
\]

is supported on (P) physical positions, then

\[
 \boxed{\mathcal C_\partial\le4HP.}
 \tag{5.3}
\]

#### Proof

The right-endpoint assertion follows from (5.1).  For a fixed left
endpoint, increasing the right endpoint also gives an inclusion chain, so
the same rank argument applies.  Each of \(\ell_j,r_j\) is at most
(2H+1), hence each physical position contributes at most (4H) to
(5.2). \(\square\)

The audited dominant-box theorem supplies constants (delta_0>0) and
(H=O(\sqrt k)) such that any word of length (W+o(W)) has

\[
 \mathcal C_\partial\ge2\delta_0W-o(W).
 \tag{5.4}
\]

Combining (5.3) and (5.4) gives

\[
 \boxed{P=\Omega(W/\sqrt k).}
 \tag{5.5}
\]

Thus even “unbounded-degree” endpoint sharing cannot be concentrated in
fewer than (W/\sqrt k) central portals.  The construction of Theorem 4.1
attains this order and supplies linear useful incidence.  In this exact
sense the surviving global-portal scale is now sharp.

The analogous raw letter statement is very different: a singleton can
have nonzero projection in exponentially many product boxes.  Theorem 5.1
shows why that activity degree alone is misleading.  Useful interval
chronology is charged through endpoint chains, whose central-band degree is
only (O(\sqrt k)).

---

## 6. Common bottoms and complements do not provide a cheaper portal

Two tempting forms of sharing can be ruled out exactly.

### Proposition 6.1 -- literal box origins have degree one

Distinct product boxes have distinct embedded origins.  Hence one literal
word occurrence cannot be the exact local-origin/reset mask for two boxes.

#### Proof

Distinct chains in an SCD have distinct minimum elements, because the chains
partition the Boolean lattice.  The three coordinate blocks are disjoint,
so the union of the three minima determines each minimum separately.  It
therefore determines the product box. \(\square\)

Thus “share the common bottom mask” cannot mean sharing exact translated
origins: there is no common origin.  A proper submask may of course lie
below targets in many boxes, but it is then a genuine high-degree partial
portal and is subject to the endpoint chronology above.

### Proposition 6.2 -- complements cannot share one endpoint

No physical endpoint represents both (S) and (S^c) unless one of them is
empty.

#### Proof

All suffix unions ending at one endpoint are comparable.  But (S) and
(S^c) are disjoint.  If (S\subseteq S^c), then (S=\varnothing); the
reverse inclusion similarly forces (S^c=\varnothing). \(\square\)

Hence complement symmetry may pair a right portal with a different left or
right portal, but it cannot double the useful central degree of one physical
endpoint.

---

## 7. The exact remaining fusion theorem

Theorem 4.1 deliberately uses isolated reverse-difference blocks.  If the
selected band segment of chain (D) contains (ell_D) vertices, its block
has (ell_D) entries but only its last position is the common endpoint
carrying the central flag.  The other (ell_D-1) positions are singleton
arm entries.  Across the selected portals,

\[
 \sum_D\ell_D=\Theta(W)
\]

when the useful endpoint--box incidence is (Theta(W)).  Therefore these
isolated blocks cannot be appended as an (o(W)) repair.

This identifies the remaining theorem more precisely than “find global
portals.”  The portals themselves now exist at the correct incidence and
cardinality scales.  What is missing is **middle-productive arm fusion**:

> Arrange \(W-o(W)\) middle-owner states in one nonzero word so that moving
> from one state endpoint to the next costs one new entry, all but \(o(W)\)
> word positions end distinct middle-layer witnesses, a designated
> \(\Theta(W/\sqrt k)\) of the states carry the high-degree portal flags,
> and the total reset cost is \(o(W)\).

In the last-occurrence partition of an OR word, this is exactly an MTF state
trajectory.  In the rotor language, it is a low-switch resolution of the
global SCD flags.  Theorem 2.1 adds a useful new requirement for choosing
that resolution: after relabeling, its central flags already have
(O(W/\sqrt k)) aggregate same-product-box collisions, so they provide more
than enough cross-box incidence if they can be dynamically fused.

Equivalently, a successful word must make the singleton arms in (4.2) do
double duty as the updates which create the next middle owner.  The literal
portal theorem proves that there is no box-incidence or within-portal
chronology obstruction.  The unresolved obstruction is entirely between
successive portal states.

### 7.1 A sharp isolated-arm tax

The linear cost of the displayed construction is not an artefact of using
singletons.

Let \(J\) be a family of designated right endpoints in an arbitrary word.
At endpoint \(j\), suppose \(d_j\) distinct targets are certified by
intervals ending at \(j\).  Their left endpoints must be distinct, because
one pair of physical endpoints determines only one interval and one OR.
Let \(s_i\) be the number of designated certificates which start at physical
position \(i\).  Then the exact incidence identity is

\[
 \boxed{\sum_{j\in J}d_j=\sum_i s_i.}
 \tag{7.1}
\]

Consequently, if all designated starts lie in a portal appendage of length
\(Q\), and every position in that appendage starts at most \(\Delta\)
designated certificates, then

\[
 \boxed{
 Q\ge\frac1\Delta\sum_{j\in J}d_j.}
 \tag{7.2}
\]

For isolated blocks, \(\Delta=1\).  If their endpoint-sharing excess is
\[
 C=\sum_{j\in J}(d_j-1),
\]
then
\[
 Q\ge C+|J|.
 \tag{7.3}
\]

Thus isolated global portals carrying \(\Omega(W)\) useful incidence have
an unavoidable \(\Omega(W)\) appendage cost.  An \(o(W)\) repair must either
reuse its arm starts with unbounded average multiplicity, or, more
relevantly, make those positions part of the already necessary
middle-owning word.  Equation (7.1) is the exact start-side counterpart of
the endpoint-sharing ledger.

### 7.2 One-update threading forces a rotor/Johnson trajectory

There is also an exact state constraint on the desired double duty.

At a word endpoint, form the ordered last-occurrence partition by scanning
backwards.  If its leading blocks are

\[
 L,\{z_1\},\ldots,\{z_h\},
 \qquad |L|=m-h,
 \tag{7.4}
\]

then their prefix unions expose a saturated lower flag from rank \(m-h\)
through rank \(m\).

Append one mask \(X\) of size \(m-h\), and suppose the next endpoint again
has a core-leading saturated flag whose core is exactly \(X\).  Then

\[
 \boxed{|L\setminus X|\le1.}
 \tag{7.5}
\]

Indeed, under the move-to-front update the new ordered partition begins

\[
 X,\quad L\setminus X,\quad
 \{z_1\}\setminus X,\ldots,\{z_h\}\setminus X,\ldots,
 \tag{7.6}
\]

after empty blocks are deleted.  The block immediately following \(X\)
must be a singleton in order to expose rank \(m-h+1\).  If
\(L\setminus X\) is nonempty, this gives (7.5); if it is empty, (7.5) is
automatic.  Since \(|L|=|X|\), the two cores are equal or adjacent in
\(J(k,m-h)\).

The following one-update successor shows that this restriction is sharp.
If
\[
 x\in L,\qquad y\notin L\cup\{z_1,\ldots,z_h\},
\]
append
\[
 X=L-x+y.
\]
Then (7.6) begins
\[
 L-x+y,\{x\},\{z_1\},\ldots,\{z_{h-1}\},
\tag{7.7}
\]
which is again a core-leading saturated flag after one actual word update.
When a full radius-(h) state is present and (y) is chosen from its
complement reservoir (R), this is the canonical rotor successor used
below; the displayed weaker condition also permits noncanonical MTF
successors.

For a full radius-\(h\) rotor state write

\[
 (L_t;z_{t,1},\ldots,z_{t,2h};R_t)
\]

and let \(x_t\in L_t,\ y_t\in R_t\) be the exchange used at time \(t\).
Its middle owner is

\[
 M_t=L_t\cup\{z_{t,1},\ldots,z_{t,h}\}.
\]

The rotor recurrence gives the exact delayed Johnson law

\[
 \boxed{
 M_{t+1}=M_t-z_{t,h}+y_t,
 \qquad
 z_{t,h}=x_{t-h}\quad(t\ge h).}
 \tag{7.8}
\]

Thus the element chosen from the lower core at time \(t\) does not leave
the middle owner until time \(t+h\).  Every coordinate which newly enters
after initialization consequently has a middle-membership run of at least
\(h+1\) consecutive states; in a cyclic trajectory this applies to every
run.  Conversely, lifting a prescribed middle Johnson path to these portal
states requires choosing each future leaving coordinate inside the lower
core \(h\) steps earlier.  This is the exact delayed-run constraint which
is absent from the collision theorem.

The canonical rotor is a sufficient, especially rigid subclass of legal
one-update MTF transitions; it is not the complete classification.  For
example, an element used as (y) may already lie in the old singleton
queue rather than in (R), and the next state can still begin with a full
core-leading singleton flag.  In that case (7.8) need not hold.  What is
forced for every one-update transition under the hypothesis preceding
(7.5) is the Johnson adjacency (7.5); the exact delayed law (7.8) and its
run consequence apply to the canonical rotor subclass.

Therefore a one-entry-per-portal fusion of the flags from Theorem 4.1 is
not an arbitrary ordering problem.  Their cores and singleton queues must
form one long legal MTF trajectory; restricting to the canonical rotor
subclass additionally imposes (7.8), while flags of different radii
require compatible radius changes or resets.  The random relabeling in
Theorem 2.1 controls product-box collisions but supplies no such
trajectory.

One can average product-box incidence over all oriented rotor states, and
an Euler circulation realizes that average by actual MTF updates.  What is
still missing is a **single-copy, distinct-target extraction** of
width-scale mass from that circulation.  A short consecutive piece may
revisit the same Boolean targets, while selecting well-separated states
reintroduces connector cost.  Thus the multiplicity circulation does not
by itself improve Theorem 4.1 to an \(o(W)\)-length repair.

The sharp stateful fusion gate left by this note is consequently:

> Select \(\Theta(W/\sqrt k)\) high-incidence radius-\(\Theta(\sqrt k)\)
> flags on one legal MTF walk (or, more restrictively, one canonical rotor
> walk), with \(\Theta(W)\) distinct selected
> targets and only \(o(W)\) total updates including connectors.

Such a theorem would turn the presently isolated global portals into a
sublinear incremental stage.  It is not proved here.

---

## 8. Self-audit

The vulnerable points are as follows.

1. **Translation by box bottoms.**  The collision proof uses only Boolean
   membership in the product box.  Local rank differences equal global rank
   differences inside a fixed translated box, so the weak-composition count
   is unchanged by the bottom.
2. **Arbitrary SCDs.**  A product box has at most one state for each triple
   of factor-chain indices.  Thus one weak composition determines at most
   one rank-(d) extension.  No canonical SCD is assumed.
3. **Uniform comparable pairs.**  A uniform coordinate permutation sends a
   fixed pair (S\subset T) to a uniform comparable pair of the same two
   ranks.  Conditional on the lower set, the upper set is a uniform
   (d)-extension.  This justifies (2.6).
4. **Pair multiplicity.**  At fixed ranks, one global SCD chain contains at
   most one set of each rank, so there is at most one pair per chain and at
   most (W) pairs.  This is the factor in (2.7).
5. **Collision to incidence.**  If a chain visits one box (u) times, its
   loss in distinct box degree is (u-1\le\binom u2).  Hence pair collisions
   dominate every repeated-box loss, including nonconsecutive returns.
6. **Target-family restriction.**  Restricting from the whole band to
   \(\mathcal T\) can only delete collision pairs.  Its size is
   (Theta(W\sqrt k)) by the already audited fixed positive fraction of
   dominant boxes and their disjoint plateau slabs.
7. **Literal suffix direction.**  The differences in (4.2) are written in
   descending rank order.  Starting at (E_t) and ending at (S_a) includes
   exactly (E_t,E_{t-1},\ldots,E_{a+1},S_a), whose union is (S_t).
8. **Nonzero convention.**  The band bottom rank is (m-H>0), and all other
   arm entries are singletons.  Every emitted letter is nonempty.
9. **No claim of universality.**  The word in Theorem 4.1 realizes the
   required linear cross-box endpoint capacity, but it is not claimed to
   cover every mask.  The missing middle-productive fusion is stated
   explicitly in Section 7.

The exact conclusion is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{The high-degree global-portal escape is real and scale-sharp:}\\
 \Theta(W/\sqrt k)\text{ literal common-endpoint portals can carry }
 \Theta(W)\text{ useful cross-box incidence within a width budget.}\\
 \text{The remaining cost is not portal existence but stateful fusion of
 their arms into the middle-owning trajectory.}
 \end{gathered}}
\]
