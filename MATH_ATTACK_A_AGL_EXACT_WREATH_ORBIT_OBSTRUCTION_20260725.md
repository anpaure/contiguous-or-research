# Affine wreath packets: the exact orbit obstruction and the surviving large-orbit gate

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is used.

## 0. Verdict

Let

\[
 p=2m+1\ \text{be prime},\qquad
 W=\binom p m,\qquad B=W/p=\operatorname{Cat}_m,
\]

and let

\[
 G=\operatorname{AGL}(1,p)
 =\{x\mapsto ax+b:a\in\mathbb F_p^\times, b\in\mathbb F_p\}.
\]

There is a sharp exact obstruction:

\[
\boxed{\text{For every }p\ge7,\text{ no exact middle wreath factor is }G\text{-invariant}.}
\tag{0.1}
\]

The proof is literal row-orbit arithmetic.  The arithmetic-progression rows
form one orbit of size (m).  Every non-AP row orbit has size (pm) or
(2pm).  Hence a (G)-invariant row family has size congruent to (0) or
(m) modulo (pm), whereas

\[
 B\equiv2(-1)^m\pmod p.
\]

For (m\ge3), this is neither (0) nor (m) modulo (p).

This kills an **exact** AGL-equivariant completion of the AP seed.  It does
not kill a near-equivariant core.  The least row-count correction is always
less than (pm=O(m^2)), so its owner and fixed-Gaussian-window shadow cost
is polynomial and therefore (o(W)).

There is also no local large-orbit obstruction.  Almost every cyclic row has
trivial affine stabilizer and is simultaneously AGL-rainbow at every depth
(q\le A\sqrt m): its complete (G)-orbit is a genuine middle packing and
has no internal shadow collision anywhere in that window.  Thus the exact
remaining theorem is a correlated selection and extendibility theorem for
these good large orbits.  Neither orbit arithmetic nor genericity supplies
that selection.

## 1. Rows, intervals, and affine rainbowness

An underlying wreath row is an unoriented cyclic order modulo rotation and
reversal.  For an oriented representative

\[
 \pi=(\pi_i)_{i\in\mathbb Z_p},
\]

write

\[
 I_i^{(r)}(\pi)=\{\pi_i,\pi_{i+1},\ldots,\pi_{i+r-1}\}.
\tag{1.1}
\]

For a set of ranks (R\subseteq\{2,\ldots,m\}), call (pi)
**strongly AGL-rainbow on (R)** if, for every (r\in R),

1. every (I_i^{(r)}(\pi)) has trivial stabilizer in (G); and
2. if (gI_i^{(r)}(\pi)=I_j^{(r)}(\pi)) for (g\in G), then
   (g=1) and (i=j).

If this holds at (r=m), the row itself has trivial (G)-stabilizer.  Its
row orbit therefore has (|G|=p(p-1)) rows.  At every controlled rank it
has exactly

\[
 |G|p
\tag{1.2}
\]

distinct interval targets.  In particular, its middle targets are disjoint,
so one good row orbit is a literal partial exact factor.

## 2. The AP orbit is exactly rainbow at every central depth

For (d\ne0), let

\[
 R_d=(0,d,2d,\ldots,(p-1)d).
\tag{2.1}
\]

Rotation removes the additive origin and reversal identifies (d) with
(-d).  Thus there are (m=(p-1)/2) underlying AP rows, and (G) is
transitive on them.

### Lemma 2.1 — stabilizer of a finite AP interval

For (2\le r\le m), put

\[
 S_r=\{0,1,\ldots,r-1\}\subseteq\mathbb F_p.
\]

Then

\[
 \operatorname{Stab}_G(S_r)
 =\{1,\ x\mapsto r-1-x\}.
\tag{2.2}
\]

#### Proof

For (t\ne0), the overlap (|S_r\cap(S_r+t)|) is at most (r-1), and
equality holds exactly for (t=\pm1).  If (x\mapsto ax+b) stabilizes
(S_r), it carries the pair ((S_r,S_r+1)) to
((S_r,S_r+a)).  Hence (a=\pm1).  If (a=1), a nonzero translation
cannot stabilize a nonempty proper subset, so (b=0).  If (a=-1), the
image of the two endpoints forces (b=r-1).  Both displayed maps do
stabilize (S_r).  \(\square\)

### Corollary 2.2 — exact AP shadow orbit

At every (2\le r\le m), all (mp) length-(r) intervals of the (m)
AP rows are distinct.  They form one (G)-orbit, of size

\[
 |G|/2=pm.
\tag{2.3}
\]

Consequently the AP rows are a partial exact middle factor and are perfectly
rainbow in every lower central shadow.  Complementation gives the same
statement in the paired upper shadows.

#### Proof

Every AP interval is an affine image of (S_r).  Lemma 2.1 gives orbit
size (pm).  There are also exactly (mp) row-slot pairs.  The natural
surjection from row-slot pairs to the affine orbit therefore has equal
domain and codomain sizes and is a bijection.  \(\square\)

This positive fact has negligible scale.  If

\[
 N_q=\binom p{m-q},\qquad K=\lceil A\sqrt m\rceil,
\]

then an AP-only family has aggregate lower-shadow defect

\[
 \sum_{q=0}^K(N_q-pm)=\Theta_A(W\sqrt m).
\tag{2.4}
\]

Including or deleting the entire AP orbit can change that aggregate defect
by at most

\[
 pm(K+1)=O_A(m^{5/2})=o(W).
\tag{2.5}
\]

Thus AP rows are exact boundary data, not a positive-density construction.

## 3. Complete classification of affine row-orbit sizes

### Lemma 3.1 — row stabilizers

Let (R) be an underlying wreath row.

* If (R) is AP, then
  \[
  |\operatorname{Stab}_G(R)|=2p.
  \tag{3.1}
  \]
* If (R) is not AP, then
  \[
  |\operatorname{Stab}_G(R)|\le2.
  \tag{3.2}
  \]

Hence the AP rows form one orbit of size (m), while every non-AP row
orbit has size

\[
 pm\quad\text{or}\quad2pm.
\tag{3.3}
\]

#### Proof

The stabilizer of an unoriented cyclic row acts faithfully on its (p)
cyclic positions, and hence embeds into the dihedral group (D_{2p}).
If it contains an element of order (p), that element is a nonidentity
translation, since the translation group is the unique Sylow-(p) subgroup
of (G).  A row stabilized by a nonzero translation satisfies

\[
 \pi_{i+s}=\pi_i+1
\]

for some nonzero position shift (s), and iteration makes (pi) an AP
order.  Conversely an AP row is stabilized by every translation and by
one affine reflection, giving the order (2p) stabilizer in (3.1).

For a non-AP row, its stabilizer has order prime to (p).  A subgroup of
(D_{2p}) whose order is prime to (p) has order at most two: two distinct
reflections generate a nontrivial (p)-rotation.  This proves (3.2).
Orbit-stabilizer and (|G|=p(p-1)=2pm) give (3.3).  \(\square\)

### Corollary 3.2 — invariant row-count lattice

Every (G)-invariant family (mathcal R) of distinct underlying rows has

\[
 \boxed{|\mathcal R|=\varepsilon m+pm,t}
 \qquad(\varepsilon\in\{0,1\},\ t\in\mathbb Z_{\ge0}).
\tag{3.4}
\]

The bit (arepsilon) records whether the unique AP row orbit is selected.

## 4. No exact AGL-equivariant wreath factor

### Theorem 4.1 — universal prime obstruction

If (p=2m+1\ge7) is prime, no exact middle wreath factor is invariant under
(G=\operatorname{AGL}(1,p)).

#### Proof

An exact factor has (B=\operatorname{Cat}_m) rows.  As usual,

\[
 B=\frac1{m+1}\binom{p-1}m
 \equiv2(-1)^m\pmod p.
\tag{4.1}
\]

Indeed, (inom{p-1}m\equiv(-1)^m\pmod p), while
(2(m+1)=p+1\equiv1\pmod p).

By Corollary 3.2, the row count of an invariant family is congruent modulo
(p) to either (0) or (m).  The residue in (4.1) is nonzero.  If (m)
is even, equality with (m) would force (m=2).  If (m) is odd, then
(2(-1)^m\equiv p-2=2m-1), and equality with (m) would force (m=1).
Both are excluded by (m\ge3).  Therefore (B) lies in neither permitted
residue class.  \(\square\)

This strengthens the translation-only obstruction: full AGL equivariance
fails for both parities of (m).

## 5. The forced non-equivariant residue is only polynomial

Suppose a (G)-invariant core contains the AP orbit and an exact factor is
obtained by adjoining (b) arbitrary exceptional rows.  Corollary 3.2 gives
the exact congruence

\[
 \boxed{b\equiv B-m\pmod{pm}.}
\tag{5.1}
\]

In particular,

\[
 b\ge
 \begin{cases}
 m+3,&m\text{ even and }m\ge4,\\
 m-1,&m\text{ odd and }m\ge3,
 \end{cases}
\tag{5.2}
\]

by reduction modulo (p).  On the other hand, the least nonnegative residue
in (5.1) is less than (pm).  Thus row-count divisibility asks for at most
(O(m^2)) exceptional rows.  This is an arithmetic upper bound on the
necessary correction size, not an existence theorem for a core attaining
it.

The corresponding owner count is (pb).  Even at the worst arithmetic
residue, changing all canonical shadows of the exceptional owners through
(K=\lceil A\sqrt m\rceil) depths costs at most

\[
 pbK<O_A(p^2m\sqrt m)=O_A(m^{7/2})=o(W).
\tag{5.3}
\]

Hence Theorem 4.1 forbids zero-exception affine completion but supplies no
coefficient-one obstruction.

## 6. Generic non-AP affine orbits are multidepth-rainbow

The exact obstruction is not caused by unavoidable collisions inside large
orbits.

### Lemma 6.1 — affine near-invariance count

Let (g\in G\setminus\{1\}).  As a permutation of (mathbb F_p), (g)
has at most (m+1) cycles.  For every (t\ge0),

\[
 \#\{S\subseteq\mathbb F_p:|S\setminus gS|=t\}
 \le 2^{m+1}\binom p{2t}.
\tag{6.1}
\]

#### Proof

If (g) is a nonzero translation it is one (p)-cycle.  Otherwise it is
conjugate to (x\mapsto ax), where (a\ne1); it has one fixed point and
((p-1)/\operatorname{ord}(a)\le(p-1)/2=m) other cycles.

Write the indicator of (S) around the directed cycles of (g).  There are
exactly (t) transitions (1\to0) and (t) transitions (0\to1), hence
(2t) transition edges.  Choose those edges in at most (inom p{2t})
ways.  Once they are fixed, the binary word on each cycle has at most two
choices.  There are at most (m+1) cycles, proving (6.1).  \(\square\)

### Lemma 6.2 — one affine positional collision

Fix (A>0), (0\le q\le A\sqrt m), (r=m-q), two distinct cyclic
positions (i,j), and (g\in G\setminus\{1\}).  If (pi) is a uniformly
random cyclic order and the two positional intervals differ in (t)
positions, then

\[
 \Pr\bigl(I_j^{(r)}(\pi)=gI_i^{(r)}(\pi)\bigr)
 \le \exp\{-\log(2)m+O_A(\sqrt m\log m)\}.
\tag{6.2}
\]

The same bound holds for
(Pr(gI_i^{(r)}=I_i^{(r)})).

#### Proof

Conditional on (I_i^{(r)}=S), the second interval is uniform among the

\[
 \binom rt\binom{p-r}t
\tag{6.3}
\]

sets meeting (S) in (r-t) points.  Lemma 6.1 therefore gives

\[
 \Pr(I_j^{(r)}=gI_i^{(r)})
 \le
 \frac{2^{m+1}}{\binom pr}
 \frac{\binom p{2t}}{\binom rt\binom{p-r}t}.
\tag{6.4}
\]

For (r=m-q), a crude comparison with the balanced Vandermonde identity
gives, uniformly in (0\le t\le r),

\[
 \frac{\binom p{2t}}{\binom rt\binom{p-r}t}
 \le p^2m^q
 =\exp\{O_A(\sqrt m\log m)\}.
\tag{6.5}
\]

Indeed,
(inom{m-q}t\ge m^{-q}\binom mt),
(inom{m+q+1}t\geinom mt),
(inom{2m+1}{2t}\le p\binom{2m}{2t}), and the central term in
Vandermonde gives
(inom{2m}{2t}\le p\binom mt^2).
Also

\[
 \binom p{m-q}\ge c_A\frac{4^m}{\sqrt m}.
\tag{6.6}
\]

Substitution proves (6.2).  For a stabilizer event take (t=0) directly
in Lemma 6.1.  \(\square\)

### Theorem 6.3 — simultaneous good large orbits

For every fixed (A>0), the proportion of cyclic rows which are strongly
AGL-rainbow simultaneously at all ranks

\[
 m-\lceil A\sqrt m\rceil,\ldots,m
\tag{6.7}
\]

tends to one exponentially fast up to a subexponential factor.  Every such
row has a trivial stabilizer, and its full (G)-orbit is a partial exact
middle factor with no internal collision in any paired lower or upper
shadow in the window.

#### Proof

Apply Lemma 6.2 to all (O_A(\sqrt m)) ranks, all (p^2) ordered position
pairs, and all (|G|=p(p-1)) affine maps.  The union-bound prefactor is
polynomial, while (6.2) is exponentially small.  The stabilizer events are
included by taking equal positions.  Strong rainbowness at the middle rank
forces the row stabilizer to be trivial.  If two targets in the lifted row
orbit coincided, pulling one back by the inverse affine map would violate
strong rainbowness.  Complementation transfers the conclusion to upper
shadows.  \(\square\)

Thus AGL packetization improves neither by AP magic nor fails by local
collision: AP packets are negligible, while generic large packets are
locally perfect.

## 7. The exact quotient problem left open

Almost every central target also has trivial affine stabilizer.  Indeed,
Lemma 6.1 with (t=0), summed over (g\ne1), shows that the number of
rank-(r) targets with nontrivial stabilizer is at most

\[
 |G|2^{m+1}=o_A\!\left(\binom pr\right)
\tag{7.1}
\]

uniformly in the fixed Gaussian window.

Discard these negligible exceptional targets and quotient each rank by
(G).  A good large row orbit becomes one column containing exactly (p)
distinct quotient targets at every depth.  At the middle rank, selected
columns must be a matching.  At lower and upper ranks, the same selected
columns must cover all but aggregate (o(W/|G|)) quotient targets.  Finally,
the uncovered middle owners must decompose into actual exceptional wreath
rows; cardinality and congruence alone do not give this extendibility.

The minimal positive theorem in this lane is therefore:

> **Extendible AGL large-orbit core.**  For every fixed (A>0), find an
> AGL-invariant union (mathcal G) of strongly multidepth-rainbow row
> orbits, optionally together with the AP orbit, such that
> 
> 1. its middle supports are disjoint;
> 2. it is contained in one exact wreath factor
>    (mathcal F=mathcal G\dot\cup\mathcal E), with
>    (|\mathcal E|=o_A(B/\sqrt m)) (a polynomial residue would suffice);
> 3. for (K=\lceil A\sqrt m\rceil),
>    \[
>    \sum_{q=0}^K
>    \left(
>      N_q-left|\bigcup_{R\in\mathcal G}\mathcal C_q(R)\right|
>    \right)=o(W).
>    \tag{7.2}
>    \]

Adding the exceptional rows cannot increase the missing-shadow defect, so
(7.2) would give the desired exact middle factor with aggregate shallow
defect (o(W)).

The uniform fractional all-row measure is balanced, and Theorem 6.3 says
almost all candidate columns are internally good.  Neither fact rounds the
common growing-rank quotient cover.  Independent selection retains the
usual occupancy defect, and orbit averaging an already chosen exact factor
only averages its defect; it does not create the required correlated
integral resolution.

## 8. Audit boundary

What is proved:

* the AP orbit is an exact partial factor and is perfectly rainbow at every
  paired central depth;
* every non-AP AGL row orbit has size (pm) or (2pm);
* no exact AGL-invariant wreath factor exists for any prime (p\ge7);
* the exact forced row-count residue for an AP-containing core is (5.1), and
  its worst possible coefficient-one cost is polynomial;
* generic full-size AGL row orbits are simultaneously internally rainbow
  throughout every fixed Gaussian window;
* nonfree target orbits are exponentially negligible.

What is not proved:

* that a near-complete matching of the good middle quotient columns exists;
* that such a matching has aggregate multidepth cover defect (o(W));
* that its middle leave is extendible by actual wreath rows;
* any coefficient-one theorem.

Accordingly, strict AGL equivariance is exactly obstructed, while
near-equivariant large-orbit completion remains a genuine correlated
resolution problem rather than an arithmetic one.
