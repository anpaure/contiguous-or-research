# A two-stage reserve-top absorber

Date: 2026-07-25

Pure mathematics only.  This note assumes the calibrated top-packet
notation

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H},\qquad M=m+H,
\tag{0.1}
\]

where \(H\) is the least integer satisfying

\[
 \frac{W}{N_H}\ge M.
\tag{0.2}
\]

Thus

\[
 H\sim\sqrt{m\log m},\qquad
 MN_H=W-o(W),\qquad HN_H=o(W).
\tag{0.3}
\]

## 0. Outcome

The two-stage reserve architecture is viable at a sharply quantified
residual scale.

1. The primary stage uses full promotion packets on all but \(R\) reserve
   tops and covers
   \[
   M(N_H-R)-E_{\rm own}
   \tag{0.4}
   \]
   distinct middle owners.  An arbitrary base packet is then placed on
   every reserve top.  If
   \[
   R=o(N_H),\qquad E_{\rm own}=o(W),
   \tag{0.5}
   \]
   the complete base family still has only \(o(W)\) middle holes.  No
   owner-disjointness between the reserve packets and the primary packets
   is required.

2. One rank-isolated unit repair is realized by a localized four-order
   overlay on two phase neighborhoods of total size at most \(2Q+2\).
   It uses at most
   \[
   4Q+4
   \tag{0.6}
   \]
   additional states and at most four promotion paths.  Charging \(2H\)
   per path, its total word-length toll is at most
   \[
   c_{\rm unit}:=8H+4Q+4.
   \tag{0.7}
   \]

3. Put
   \[
   \boxed{
   L_*=\left\lfloor
       \frac{M}{16(H+Q+1)}
       \right\rfloor.}
   \tag{0.8}
   \]
   One reserve top can carry \(L_*\) arbitrary top-local unit repairs with
   total extra word cost at most \(M/2\).  In particular,
   \[
   L_*=\Theta\!\left(\frac{M}{H+Q}\right).
   \tag{0.9}
   \]

4. A family of \(R\) reserve tops therefore carries
   \[
   S\le R L_*
   =\Theta\!\left(\frac{RM}{H+Q}\right)
   \tag{0.10}
   \]
   unit octahedral repairs.  Its entire additional state/reset toll is
   \(O(RM)=o(W)\) under (0.5).

5. Algebraically, throughout the protected window every unit changes one
   controlled rank by a coefficient-one octahedron and preserves the
   middle and all other controlled ranks.  Outside the protected window a
   truncated unit can have single-swap leakage; those flags are not used as
   indispensable witnesses.  A unit has two positive and two negative
   coordinates at its selected rank, so it can fill at most two holes.
   Consequently \(R\) reserve tops can monotonically repair at most
   \[
   2RL_*=
   \Theta\!\left(\frac{RM}{H+Q}\right)
   \tag{0.11}
   \]
   hard-band holes.

6. Equivalently, a sufficient primary residual scale is an aggregate
   top-local octahedral word length
   \[
   \boxed{S=o\!\left(\frac{W}{H+Q}\right).}
   \tag{0.12}
   \]
   If those \(S\) units admit a capacitated assignment to
   \[
   R=O\!\left(\frac{S(H+Q)}{M}\right)=o(N_H)
   \tag{0.13}
   \]
   reserve tops, then all absorber overhead is \(o(W)\).  For
   \(Q=O(H)\), the natural target is \(S=o(W/H)\).

The phrase “admit a capacitated assignment” is essential.  A rank-\(r\)
octahedron uses \(r+2\) coordinates and can be hosted only by a top
containing those coordinates.  Scalar size alone does not group arbitrary
repairs into \(L_*\)-sized top-local banks.  Section 5 gives the exact Hall
condition and the corresponding reserve lattice.

The final conclusion is conditional but exact:

> An owner near-matching plus a legal, top-hostable hard-band residual of
> octahedral length \(o(W/(H+Q))\) yields a \(W+o(W)\) construction.

This improves the one-full-rectangle-per-top cleanup scale
\(O(N_H)=O(W/m)\) by the factor \(M/(H+Q)\), without reviving the fatal
full-packet \(0/2\) overlap.

## 1. One localized unit repair

Fix a top \(U\), \(|U|=M\), and an oriented cyclic order

\[
 C=(c_i:i\in\mathbb Z_M).
\]

For \(1\le k<M\), write

\[
 I_k(C;t)=\{c_t,c_{t+1},\ldots,c_{t+k-1}\}.
\tag{1.1}
\]

Index promotion states by the start \(s\) of their middle \(m\)-interval.
The rank-\(k\) flag at state phase \(s\) is

\[
 I_k(C;s+m-k).
\tag{1.2}
\]

Let \(\tau\) swap the entries in adjacent positions \(b,b+1\).  At rank
\(k\), its only affected state phases are

\[
 \mathcal B_k^{\rm st}(b)
 =\{b-m+1,\ b-m+k+1\}.
\tag{1.3}
\]

For a controlled window

\[
 \mathcal K_Q
 =\{m-Q,m-Q+1,\ldots,m+Q\},
\tag{1.4}
\]

put

\[
 B_Q(b)
 =\bigcup_{k\in\mathcal K_Q}\mathcal B_k^{\rm st}(b).
\tag{1.5}
\]

Then

\[
 B_Q(b)
 =\{b-m+1\}\cup
   \{b-Q+1,\ldots,b+Q+1\},
\tag{1.6}
\]

and hence

\[
 |B_Q(b)|\le2Q+2.
\tag{1.7}
\]

The set in (1.6) is the union of at most two cyclic phase intervals.

Now let \(\sigma\) swap a second adjacent position pair, disjoint from the
first, and put

\[
 C_{ij}=\tau^i\sigma^j C
 \qquad(i,j\in\{0,1\}).
\tag{1.8}
\]

Define two positive localized configurations:

\[
 \mathcal G^0
 =(C_{00}|B_Q(b))\sqcup(C_{11}|B_Q(b)),
\tag{1.9}
\]

\[
 \mathcal G^1
 =(C_{10}|B_Q(b))\sqcup(C_{01}|B_Q(b)).
\tag{1.10}
\]

Here a restriction to \(B_Q(b)\) is split into its at most two cyclic
components, each a literal promotion path.

### Theorem 1.1 (localized incidence equals the full selector)

For every controlled length \(k\in\mathcal K_Q\),

\[
 \boxed{
 \mu_k(\mathcal G^0)-\mu_k(\mathcal G^1)
 =A_k(C_{00}+C_{11}-C_{10}-C_{01}),}
\tag{1.11}
\]

where \(A_k\) is full cyclic length-\(k\) interval incidence.

#### Proof

At a state phase outside \(B_Q(b)\), the rank-\(k\) window contains either
both positions swapped by \(\tau\) or neither.  Therefore

\[
 I_k(C_{00};s+m-k)=I_k(C_{10};s+m-k)
\]

and

\[
 I_k(C_{11};s+m-k)=I_k(C_{01};s+m-k).
\]

The phasewise alternating contribution of the four orders is zero there.
All possibly nonzero phases lie in \(B_Q(b)\), where both diagonals are
present in (1.9)--(1.10).  Summing over the phase circle proves (1.11).
\(\square\)

Let the boundary separation of the two adjacent swaps be \(a\), with

\[
 2\le a\le M-2.
\]

The full four-order selector vanishes at every proper interval length
except

\[
 a,\qquad M-a.
\tag{1.12}
\]

At length \(a\), after writing the cyclic order locally as

\[
 (x,x',K,y,y',\ldots),\qquad |K|=a-2,
\]

its image is

\[
 \boxed{
 \omega(K;x,x',y,y')
 =e_{Kx'y}-e_{Kxy}-e_{Kx'y'}+e_{Kxy'}.}
\tag{1.13}
\]

At length \(M-a\), the image is the within-\(U\) complementary copy of
(1.13).

Indeed, a target coefficient can survive the alternating action of
\(\tau,\sigma\) only if the target contains exactly one label from each
swapped pair.  If the target is a cyclic interval, its two boundary cuts
must therefore separate both pairs.  The two arcs between those cuts have
lengths \(a\) and \(M-a\).  At length \(a\), the four choices of one label
from each pair give exactly (1.13), with the displayed alternating signs.

For lower depth \(q\), take \(a=m-q\); the full selector's companion
length is \(H+q\).  For upper depth \(q\), take \(a=m+q\); its companion
is \(H-q\).  Thus, throughout \(1\le q\le Q\le H-2\), a localized unit:

* changes exactly one rank inside the protected window;
* preserves the middle rank;
* preserves every other rank in the protected window.

The localized equality (1.11) is asserted only for protected lengths.
At an unprotected length, omission of an affected phase leaves the explicit
single-swap counterterm from the truncated rectangle identity.  Those
unprotected overlay flags must therefore be treated as optional additions,
not as witnesses whose later removal is charged as a new hole.  Taking
\(Q=H-2\) protects every calibrated band rank except four boundary layers,
whose total number of masks is \(o(W)\): uniformly for fixed
\(j\in\{0,1,2\}\),

\[
 N_{H-j}=(1+o(1))N_H=O(W/m).
\tag{1.14}
\]

### Proposition 1.2 (exact unit cost)

Each of \(\mathcal G^0,\mathcal G^1\) contains at most

\[
 2|B_Q(b)|\le4Q+4
\tag{1.15}
\]

states and is a union of at most four promotion paths.  Under a \(2H\)
initialization charge per path, its total cost is at most

\[
 \boxed{c_{\rm unit}=8H+4Q+4.}
\tag{1.16}
\]

Its middle occurrence count is at most \(4Q+4\), and

\[
 \mu_m(\mathcal G^0)=\mu_m(\mathcal G^1).
\tag{1.17}
\]

#### Proof

The phase set has at most two components.  Each diagonal uses two orders,
giving at most four promotion paths and (1.15).  The reset ledger gives
(1.16).  Since \(a,M-a\ne m\), Theorem 1.1 and the selector identity give
(1.17).  \(\square\)

The unit is an **overlay**.  It does not replace the reserve top's base
packet; it adds one of the two positive configurations (1.9)--(1.10).
Consequently it can create extra owner occurrences but cannot delete a
middle owner already covered by the base family.

## 2. A bank of repairs on one reserve top

Different units on one reserve top may use completely different cyclic
orders.  They need only have their octahedral coordinate supports contained
in that top.  Their phase neighborhoods need not be disjoint, because every
unit is compiled into its own at most four promotion segments and all costs
are added explicitly.

Set

\[
 L_*=\left\lfloor
       \frac{M}{16(H+Q+1)}
       \right\rfloor.
\tag{2.1}
\]

### Proposition 2.1 (per-top bank capacity)

One reserve top can host \(L_*\) unit repairs with:

\[
 \text{extra states}\le(4Q+4)L_*,
\tag{2.2}
\]

\[
 \text{extra promotion paths}\le4L_*,
\tag{2.3}
\]

\[
 \text{extra reset toll}\le8HL_*,
\tag{2.4}
\]

and total extra word cost

\[
 (8H+4Q+4)L_*\le\frac M2.
\tag{2.5}
\]

The number of additional middle-owner occurrences is at most

\[
 (4Q+4)L_*\le\frac M4.
\tag{2.6}
\]

#### Proof

Equations (2.2)--(2.4) are the sums of Proposition 1.2 over the units.
Since

\[
 8H+4Q+4\le8(H+Q+1),
\]

the definition (2.1) gives (2.5).  Similarly,

\[
 4Q+4\le4(H+Q+1)
\]

gives (2.6).  \(\square\)

The constants \(16,1/2,1/4\) are only a clean safe choice.  The intrinsic
capacity scale is

\[
 \boxed{L_*=\Theta(M/(H+Q)).}
\tag{2.7}
\]

Every unit supplies one binary octahedral direction.  Thus a reserve top
with \(L_*\) installed cells has a positive correction zonotope

\[
 \left\{
 \sum_{j=1}^{L_*}\varepsilon_j\omega_j:
 \varepsilon_j\in\{0,1\}
 \right\}
\tag{2.8}
\]

relative to the reference choice of diagonals.

## 3. Primary owner stage and reserve-owner ledger

Let \(\mathcal R\) be a family of \(R\) reserve tops.  Suppose the primary
stage selects one base packet on every nonreserve top, and those packets
cover at least

\[
 M(N_H-R)-E_{\rm own}
\tag{3.1}
\]

distinct middle owners.

Place an arbitrary full base packet on every reserve top before adding the
localized overlays.

### Proposition 3.1 (reserve tops do not need owner compatibility)

The resulting base family has at most

\[
 \boxed{
 E_m\le W-M(N_H-R)+E_{\rm own}
 =(W-MN_H)+MR+E_{\rm own}}
\tag{3.2}
\]

middle holes.

Localized overlays cannot increase this hole count.  They add at most

\[
 (4Q+4)S
\tag{3.3}
\]

middle-owner occurrences when \(S\) units are installed.

Consequently, if

\[
 R=o(N_H),\qquad E_{\rm own}=o(W),\qquad
 S Q=o(W),
\tag{3.4}
\]

then both the number of middle holes and the added occurrence excess are
\(o(W)\).

#### Proof

Even if every reserve base packet is completely redundant, the primary
support (3.1) remains covered.  Subtracting it from \(W\) proves (3.2).
Every overlay is positive, so it deletes no covered owner.  Equation (3.3)
is Proposition 1.2 summed over the units.  Finally,

\[
 W-MN_H=o(W),\qquad
 MR=o(MN_H)=o(W),
\]

which proves the conclusion.  \(\square\)

This is the main advantage of sparse reserves.  Their base packets can be
chosen solely for absorber support; any owner incompatibility costs at most
\(MR=o(W)\).

## 4. Rank repairs and coverage legality

At a controlled rank, orient a unit octahedron as

\[
 \omega=e_A+e_B-e_C-e_D.
\tag{4.1}
\]

Switching its diagonal increases the loads of \(A,B\) by one and decreases
the loads of \(C,D\) by one.

### Definition 4.1 (legal unit repair)

At the moment it is applied, (4.1) is **coverage-legal** when

\[
 \mu(C)\ge2,\qquad \mu(D)\ge2.
\tag{4.2}
\]

It repairs

\[
 g(\omega)
 =|\{A,B:\mu=0\}|\in\{0,1,2\}
\tag{4.3}
\]

holes and creates none.

### Proposition 4.2 (hole capacity)

A sequence of \(S\) coverage-legal units fills at most \(2S\) holes.
If it has total gain

\[
 G=\sum_{j=1}^S g(\omega_j),
\]

then the hard-band hole count decreases by exactly \(G\).

Thus \(R\) reserve tops, each carrying \(L_*\) units, can fill at most

\[
 \boxed{2RL_*}
\tag{4.4}
\]

holes.

#### Proof

Condition (4.2) guarantees that the two negative coordinates remain
positive.  The only coverage changes are therefore the formerly zero
positive coordinates counted in (4.3).  Sum over the sequence.
\(\square\)

For exact histogram balancing rather than mere coverage, define the
residual after all reference overlays have been installed.  A tuple of
rank corrections \(v_k\) is repairable if

\[
 v_k=\sum_{j:\,k_j=k}\omega_j
\tag{4.5}
\]

for the installed, top-hosted units.  Every \(\omega_j\) has zero point
margins.  Conversely, unrestricted signed octahedra generate the full
zero point-margin lattice, but that lattice statement does not supply the
bounded top-hosting or the coverage legality (4.2).

Effects outside the protected window—including the complementary selector
rank and any truncated single-swap counterterms—are not used in the repair
ledger.  Every overlay is added on top of the base packets, so a final
choice cannot delete a base witness.  If reference-overlay witnesses are
used outside the protected window, their possible loss must instead be
included explicitly in \(E_{\rm band}\) or in the outer-tail patch.

## 5. Exact top-hosting condition

A rank-\(k\) octahedron

\[
 \omega(K;a,b,c,d)
\]

has coordinate support

\[
 F(\omega)=K\cup\{a,b,c,d\},
\qquad |F(\omega)|=k+2.
\tag{5.1}
\]

It is realizable inside a top \(U\) exactly when

\[
 F(\omega)\subseteq U.
\tag{5.2}
\]

The condition is sufficient: arrange \(a,b\) and \(c,d\) as the two
adjacent pairs at boundary separation \(k\), put \(K\) on the intervening
arc, and fill the unused positions arbitrarily.

Let \(\mathcal D\) be a multiset of proposed unit repairs.  Form its
incidence graph with all rank-\(M\) tops, joining \(\omega\) to \(U\) when
(5.2) holds.

### Proposition 5.1 (capacitated hosting Hall condition)

The repairs in \(\mathcal D\) can be assigned to tops, at most \(L_*\) per
top, if and only if every submultiset
\(\mathcal D'\subseteq\mathcal D\) satisfies

\[
 \boxed{
 |\mathcal D'|
 \le L_*\,|N(\mathcal D')|.}
\tag{5.3}
\]

#### Proof

Replace every top by \(L_*\) capacity copies and apply Hall's theorem.
\(\square\)

Condition (5.3) does not itself ensure a sparse number of used tops.  Define

\[
 \kappa_{L_*}(\mathcal D)
\tag{5.4}
\]

to be the least number of tops in any capacity-\(L_*\) hosting assignment.
Then the exact reserve requirement is

\[
 R\ge\kappa_{L_*}(\mathcal D).
\tag{5.5}
\]

The elementary bounds are

\[
 \left\lceil\frac{|\mathcal D|}{L_*}\right\rceil
 \le\kappa_{L_*}(\mathcal D)
 \le|\mathcal D|
\tag{5.6}
\]

when a distinct host exists for every repair.  The lower bound is attained
only when the repair supports cluster into common tops.  Two generic
near-middle octahedra need not fit in one top, because each already uses
about \(m\) coordinates.

For a fixed reserve family \(\mathcal R\), the signed correction lattice at
rank \(k\) is

\[
 \boxed{
 \mathcal L_k(\mathcal R)
 =\sum_{U\in\mathcal R}
   \iota_U\bigl(\ker_{\mathbb Z}U_{U,k}\bigr),}
\tag{5.7}
\]

where \(\iota_U\) extends a vector on \(\binom Uk\) by zero.  Every vector
in (5.7) has zero global point margins, but for sparse
\(\mathcal R\) the reverse inclusion need not hold.  In particular, masks
which lie in no reserve top cannot be changed.  This support invariant is
the exact extra obstruction beyond parity and point margins.

## 6. Exact global ledger

Let \(S=|\mathcal D|\) be the number of installed unit repairs, hosted on
\(R\) reserve tops with at most \(L_*\) per top.

### Proposition 6.1 (word-length ledger)

The base packets and all localized units compile into a word of length at
most

\[
 \boxed{
 MN_H+2HN_H+(8H+4Q+4)S.}
\tag{6.1}
\]

Before literal patching.

#### Proof

There are \(M\) base states and one base reset of cost at most \(2H\) at
each of the \(N_H\) tops.  Proposition 1.2 gives the unit contribution.
\(\square\)

If the primary owner error is \(E_{\rm own}\), the remaining aggregate
nonmiddle hard-band holes after the legal repairs are \(E_{\rm band}\), and
all uncontrolled outer masks are appended literally, the final length is

\[
 \begin{aligned}
 L_{\rm final}\le{}&
 MN_H+2HN_H+(8H+4Q+4)S\\
 &+E_m+E_{\rm band}
 +O(W/H),
 \end{aligned}
\tag{6.2}
\]

where \(E_m\) obeys (3.2).

### Theorem 6.2 (two-stage reserve-top sufficiency)

Assume:

1. \(1\le Q\le H-2\);
2. \(R=o(N_H)\);
3. the primary owner stage satisfies \(E_{\rm own}=o(W)\);
4. the reference-overlay hard-band residual admits a coverage-legal or
   exact signed decomposition into \(S\) top-hosted units, with
   \[
   S\le RL_*,
   \qquad
   S(H+Q)=o(W);
   \tag{6.3}
   \]
5. the unrepaired aggregate hard-band hole count is
   \(E_{\rm band}=o(W)\).

Then

\[
 \boxed{L_{\rm final}=W+o(W).}
\tag{6.4}
\]

#### Proof

By calibration,

\[
 MN_H\le W,\qquad HN_H=o(W).
\]

Condition (6.3) makes the unit toll in (6.2) \(o(W)\).
Proposition 3.1 and assumptions 2--3 give \(E_m=o(W)\).
The band remainder is \(o(W)\) by assumption 5.

Finally, the two tails outside the calibrated band contain

\[
 O(W/H)=o(W)
\]

masks in total, by the standard ratio estimate

\[
 \frac{N_{q+1}}{N_q}
 =\frac{m-q}{m+q+1}
\]

starting at \(q=H\).  Substitute all bounds into (6.2).
\(\square\)

## 7. The primary residual scale

The bank capacity and word ledger give an exact scale conversion.

Let

\[
 S_{\rm prim}
\tag{7.1}
\]

be the least number of top-hostable legal unit octahedra needed to reduce
the primary hard-band residual to \(o(W)\).

### Corollary 7.1 (sufficient scale)

If

\[
 \boxed{
 S_{\rm prim}=o\!\left(\frac{W}{H+Q}\right)}
\tag{7.2}
\]

and those units admit a hosting assignment using

\[
 R=O\!\left(\frac{S_{\rm prim}(H+Q)}M\right)
 =o(N_H)
\tag{7.3}
\]

tops with load at most \(L_*\), then the reserve absorber has total
\(o(W)\) overhead.

#### Proof

Equation (7.2) is exactly the unit-toll condition in (6.3).
Equation (7.3) and \(MN_H=W-o(W)\) imply \(R=o(N_H)\).
The per-top capacity is (2.1), up to the fixed safe constant.
\(\square\)

For monotone hole repair, one unit fills at most two holes.  Thus a primary
aggregate hole residual

\[
 B_{\rm prim}
\tag{7.4}
\]

requires at least \(B_{\rm prim}/2\) units, and the natural sufficient
target is

\[
 \boxed{
 B_{\rm prim}=o\!\left(\frac{W}{H+Q}\right)}
\tag{7.5}
\]

together with a legal top-local octahedral routing.

For \(Q=O(H)\), (7.2) and (7.5) become

\[
 o(W/H).
\tag{7.6}
\]

This is much smaller than a generic \(o(W)\) residual.  In particular,
the reserve bank cannot clean up the \(\Theta(W)\) holes produced by
independent one-packet-per-top selection.

There is a universally safe but weaker regime: assign at most one repair
to each reserve top.  Then \(S=o(N_H)=o(W/m)\) automatically gives sparse
reserves and \(o(W)\) reset toll, without any grouping theorem.  Achieving
the larger \(o(W/(H+Q))\) scale requires the top-local clustering measured
by \(\kappa_{L_*}(\mathcal D)\).

## 8. Audit ledger

### Proved

1. A localized four-order overlay on \(O(Q)\) phases has the exact full
   selector incidence throughout the controlled band.
2. One unit costs at most \(4Q+4\) states, four paths, and
   \(8H+4Q+4\) total entries including resets.
3. One reserve top safely hosts
   \(\Theta(M/(H+Q))\) arbitrary **top-local** units.
4. Reserve base packets need no owner compatibility with the primary
   family when \(R=o(N_H)\).
5. The exact middle-hole bound (3.2).
6. The exact hole gain and donor condition for a legal unit.
7. The exact capacitated Hall condition for hosting repair supports.
8. The reserve correction lattice (5.7) and its support invariant.
9. The complete word-length ledger (6.1)--(6.2).
10. The sufficient residual scale \(o(W/(H+Q))\).

### Still open

1. The primary owner near-perfect packet matching.
2. A primary vertical construction with residual
   \(o(W/(H+Q))\), rather than merely \(o(W)\).
3. A legal octahedral decomposition of that residual with donor loads
   protected throughout.
4. A sparse capacitated top-hosting assignment attaining
   \(R=O(S(H+Q)/M)\).

The reserve construction therefore supplies a rigorous absorber theorem,
not the missing primary near-factor.  Its useful quantitative message is:
one sparse reserve top buys \(\Theta(M/(H+Q))\) exact unit repairs at
\(O(M)\) cost, and the whole two-stage architecture closes precisely when
the primary residual has top-hostable octahedral length
\(o(W/(H+Q))\).
