# Complementary-segment rectangles for calibrated top packets

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

Let \(U\) be a calibrated top of size

\[
 M=m+H,
\]

and let a directed cyclic order of \(U\) generate its promotion packet.
Choose two disjoint adjacent position swaps \(A,B\), and write the four
orders as \(\pi_{ij}=A^iB^j\pi\).

The full-packet deployment

\[
 \pi_{00}+\pi_{11}
 \quad\longleftrightarrow\quad
 \pi_{10}+\pi_{01}
\]

has the desired signed interval trade, but is unusable as an owner cover:
the two orders on either diagonal differ in only two adjacent swaps and
therefore share at least \(M-4\) of their \(M\) middle owners.  Deploying
two full packets on half the tops covers at most

\[
 {M+4\over2}N_H=(1/2+o(1))W                         \tag{0.1}
\]

distinct owners.

The proposed complementary-segment repair is valid.  Fix

\[
 Q=o(H)
\]

and take two cyclic phase segments \(S,T\subset\mathbb Z_M\) such that

\[
 S\cup T=\mathbb Z_M,
 \qquad |S\cap T|=O(Q),                            \tag{0.2}
\]

with the overlap placed in the two boundary neighborhoods described in
Section 2.  Form the two diagonal configurations

\[
 \mathcal C_0=(\pi_{00}|S)\sqcup(\pi_{11}|T),
 \qquad
 \mathcal C_1=(\pi_{10}|S)\sqcup(\pi_{01}|T).     \tag{0.3}
\]

Each is a union of two legal promotion paths.  For every hard-band length

\[
 \ell=m\pm q,\qquad 0\le q\le Q,                  \tag{0.4}
\]

their incidence difference is **exactly** the full four-order rectangle:

\[
 \boxed{
 I_\ell(\mathcal C_0)-I_\ell(\mathcal C_1)
 =I_\ell(\pi_{00})+I_\ell(\pi_{11})
  -I_\ell(\pi_{10})-I_\ell(\pi_{01}).}           \tag{0.5}
\]

There is no segment-boundary counterterm.

If the two swap cuts have cyclic separation \(r\), the right side of
(0.5) vanishes at every length except

\[
 r\quad\hbox{and}\quad M-r.                       \tag{0.6}
\]

Thus:

* \(r=m-q\) isolates lower depth \(q\);
* \(r=m+q\) isolates upper depth \(q\);

provided \(q\le Q\le H-2\).  The complementary exceptional lengths are
\(H+q\) and \(H-q\), respectively, outside the controlled central band.
At the middle length \(m\), both diagonal segment configurations have
identical owner incidence.

Each configuration has \(M+O(Q)\) owner occurrences and at least
\(M-O(Q)\) distinct owners.  Across all calibrated tops the extra duplicate
mass is

\[
 O(QN_H)=O(WQ/m)=o(W),                              \tag{0.7}
\]

and two path initializations per top cost

\[
 O(HN_H)=o(W).                                     \tag{0.8}
\]

Therefore the segment rectangle is a valid **final absorber after an owner
near-transversal**.  Switching its diagonal does not alter that owner
multiset or any nontarget hard-band histogram.

At one target rank \(r\), the induced elementary trade is

\[
 \boxed{
 e_{Kbc}+e_{Kad}-e_{Kac}-e_{Kbd},}                 \tag{0.9}
\]

where \(|K|=r-2\) and \(a,b,c,d\) are distinct.  These trades generate
exactly the integral kernel of the singleton-incidence map on rank \(r\).
There is no additional parity invariant in the rank-incidence lattice.
The unavoidable invariants are total mass and every coordinate's first
moment.

This lattice statement does not by itself prove sequential absorption.
With nonnegative packet multiplicities, the available corrections form a
bounded signed zonotope, not the whole lattice.  In addition, rectangle
switches cannot repair singleton-marginal imbalance.  For full packets
those marginals are fixed by the top multiplicities; for complementary
segments they also contain a fixed, generally nonuniform stitching term.
The remaining theorem is an available-trade decomposition, allocated
across near-transversal tops, whose signed capacity dominates the residual
errors at all depths \(q\le Q\).

## 1. Why the full-packet diagonal is fatal

Let \(X_t(\pi)\) be the cyclic \(m\)-window starting at phase \(t\).  An
adjacent position swap changes \(X_t\) only when exactly one of the two
swapped positions lies in that window.  There are exactly two such phase
starts.  Hence two disjoint adjacent swaps change at most four of the
\(M\) phase-indexed owners:

\[
 X_t(\pi_{00})=X_t(\pi_{11})
 \quad\hbox{for at least }M-4\text{ values of }t.  \tag{1.1}
\]

The union of the two diagonal owner packets therefore has size at most

\[
 2M-(M-4)=M+4.                                     \tag{1.2}
\]

If packet multiplicities are zero or two with total packet count \(N_H\),
at most \(N_H/2\) tops are active, apart from an irrelevant parity-one
exception.  Equations (1.2) and \(MN_H=(1-o(1))W\) give (0.1).  Thus full
diagonal packets can only be used as signed formal trades, not as the core
owner deployment.

## 2. Exact support of one adjacent swap

Index cyclic positions by \(\mathbb Z_M\).  Let the swap \(A\) interchange
the labels on the two sides of the cut between positions \(a\) and
\(a+1\).  For a cyclic order \(\sigma\), write

\[
 v_{\ell,t}(\sigma)=e_{I_\sigma(t,\ell)}           \tag{2.1}
\]

for the basis vector of the length-\(\ell\) interval starting at \(t\).

### Lemma 2.1 (two sensitive phase starts)

For every \(1\le\ell<M\),

\[
 v_{\ell,t}(\sigma)-v_{\ell,t}(A\sigma)=0
\]

unless

\[
 \boxed{t=a+1\quad\hbox{or}\quad t=a-\ell+1}
 \pmod M.                                           \tag{2.2}
\]

#### Proof

An interval changes under the swap exactly when it contains one swapped
position and not the other.  Since the positions are adjacent, this means
that one boundary of the interval is the cut between them.  The interval
either starts immediately after the cut, giving \(t=a+1\), or ends
immediately before it, giving \(t+\ell-1=a\). \(\square\)

For the hard lengths (0.4), all sensitive starts lie in

\[
 \mathcal B_A(Q)=
 \{a+1\}\cup
 \{a-m-q+1:-Q\le q\le Q\}.                       \tag{2.3}
\]

This is the union of two cyclic neighborhoods of total size \(O(Q)\),
centered at the two cuts separated by \(m\).

Choose a two-arc cover \(S,T\) of the phase circle whose two overlap
components contain the sets in (2.3).  Concretely, cut the circle at the
two centers in (2.3), take the two complementary closed arcs, and enlarge
both arcs by \(Q+2\) phases across each endpoint.  Then

\[
 \mathcal B_A(Q)\subseteq S\cap T,
 \qquad |S\cap T|\le4Q+O(1).                      \tag{2.4}
\]

Because the two principal arc lengths are \(m\) and \(H\), the assumption
\(Q=o(H)\) leaves both paths nonempty and long.

## 3. The diagonal segment identity

For a phase set \(R\), put

\[
 I_{\ell,R}(\sigma)=\sum_{t\in R}v_{\ell,t}(\sigma). \tag{3.1}
\]

Let \(B\) be any second adjacent swap disjoint from \(A\), and retain
\(\pi_{ij}=A^iB^j\pi\).  Define

\[
 \begin{aligned}
 D_\ell
 &:=I_{\ell,S}(\pi_{00})+I_{\ell,T}(\pi_{11})\\
 &\quad-I_{\ell,S}(\pi_{10})-I_{\ell,T}(\pi_{01}).
 \end{aligned}                                      \tag{3.2}
\]

### Theorem 3.1 (no boundary counterterm)

For every hard length (0.4),

\[
 \boxed{
 D_\ell
 =I_\ell(\pi_{00})+I_\ell(\pi_{11})
  -I_\ell(\pi_{10})-I_\ell(\pi_{01}),}           \tag{3.3}
\]

where \(I_\ell=I_{\ell,\mathbb Z_M}\).

#### Proof

At a phase \(t\in S\setminus T\), the contribution to (3.2) is

\[
 v_{\ell,t}(\pi_{00})-v_{\ell,t}(\pi_{10}),      \tag{3.4}
\]

the first difference under \(A\).  At a phase \(t\in T\setminus S\), it
is

\[
 v_{\ell,t}(\pi_{11})-v_{\ell,t}(\pi_{01}),      \tag{3.5}
\]

the same first difference with \(B\) already applied.  By Lemma 2.1 and
(2.4), every phase at which either difference can be nonzero lies in
\(S\cap T\).  Thus (3.4)-(3.5) vanish.

At a phase in \(S\cap T\), all four terms occur and give the full mixed
difference

\[
 v_{00}+v_{11}-v_{10}-v_{01}.                    \tag{3.6}
\]

The same mixed difference vanishes at every phase outside \(S\cap T\),
because it is supported inside the first-difference support of \(A\).
Summing (3.6) over the whole phase circle proves (3.3). \(\square\)

The proof needs the sensitive starts of only one of the two swaps in the
overlap.  Using both makes the construction symmetric but is not necessary.

## 4. Rank isolation and the exact four-set trade

Let the cut of \(B\) occur \(r\) positions after the cut of \(A\).  A
cyclic interval is simultaneously sensitive to both swaps only when its
two boundary cuts are precisely these two cuts.  Therefore the full mixed
difference in (3.3) vanishes unless

\[
 \ell=r\quad\hbox{or}\quad\ell=M-r.               \tag{4.1}
\]

Suppose the oriented arc of length \(r\) between the cuts contains an
internal set \(K\), \(|K|=r-2\).  Label the two swapped pairs so that its
four possible endpoint choices are

\[
 bc,\quad ac,\quad bd,\quad ad.
\]

Then, up to reversing the overall sign,

\[
 \boxed{
 D_r=e_{Kbc}+e_{Kad}-e_{Kac}-e_{Kbd}.}            \tag{4.2}
\]

If

\[
 L=U\setminus(K\cup\{a,b,c,d\}),
\]

the complementary exceptional rank carries

\[
 D_{M-r}=e_{Lad}+e_{Lbc}-e_{Lbd}-e_{Lac}.         \tag{4.3}
\]

For \(r=m-q\), the second rank is \(H+q\); for \(r=m+q\), it is
\(H-q\).  If \(q\le Q\le H-2\), exactly one of the two exceptional ranks
lies in the hard band \([m-Q,m+Q]\).  In particular, for \(q>0\),

\[
 D_m=0.                                            \tag{4.4}
\]

Equations (3.3) and (4.4) prove that the two diagonal segment
configurations have exactly the same middle-owner incidence vector, not
merely the same number of owners.

## 5. Owner overlap and reset ledger

One adjacent swap changes only two phase-indexed middle windows.  Thus
every one of the four orders \(\pi_{ij}\) agrees phasewise with the base
order outside at most four middle phases.

In one segment configuration (0.3), discard the \(O(Q)\) occurrences whose
phase lies in \(S\cap T\), and the \(O(1)\) phases sensitive to \(A\) or
\(B\) at length \(m\).  Every remaining occurrence is the unchanged base
owner at a unique phase in \(\mathbb Z_M\).  Hence

\[
 \boxed{
 \#\{\text{distinct middle owners in }\mathcal C_i\}
 \ge M-O(Q).}                                      \tag{5.1}
\]

Also

\[
 |S|+|T|=M+O(Q).                                   \tag{5.2}
\]

Suppose a previously selected one-packet-per-top family had middle
collision and hole mass \(o(W)\).  Replacing its packet at every absorber
top by one of the configurations (0.3) changes the owner union by at most
\(O(Q)\) per top.  Therefore the added global collision/hole mass is at
most

\[
 O(QN_H)=O(WQ/m)=o(W)                              \tag{5.3}
\]

whenever \(Q=o(m)\), in particular when \(Q=o(H)\).

Each configuration consists of two promotion paths.  Across all tops its
initialization toll is

\[
 4HN_H=o(W).                                       \tag{5.4}
\]

Finally, diagonal switching preserves the middle incidence exactly by
(4.4).  Thus once one diagonal has an acceptable owner near-transversal,
every sequence of rectangle sign choices retains that exact owner
histogram.

## 6. The exact rank-\(r\) lattice

Let

\[
 \mathcal R_r=\mathbb Z^{\binom Ur}
\]

with basis \(e_S\), and define the singleton-incidence map

\[
 \partial_r:\mathcal R_r\longrightarrow\mathbb Z^U,
 \qquad
 \partial_r e_S=\sum_{x\in S}e_x.                 \tag{6.1}
\]

Every rectangle (4.2) lies in \(\ker\partial_r\).  Let \(\mathcal L_r\)
be the integer lattice generated by all such four-set trades.

### Theorem 6.1 (rectangle lattice)

For \(2\le r\le M-2\),

\[
 \boxed{\mathcal L_r=\ker_{\mathbb Z}\partial_r.} \tag{6.2}
\]

Thus the only integral linear invariants are the \(M\) singleton
marginals.  Total mass is already their sum divided by \(r\).  There is no
additional parity obstruction in rank incidence.

#### Proof

Represent an integer vector as a signed multiset of \(r\)-sets.  Membership
in \(\ker\partial_r\) says that its positive and negative multisets have
the same degree at every label.

Give the edges in each multiset temporary column labels.  Two zero-one
incidence matrices with the same row sums and the same column sum \(r\)
are connected by ordinary two-by-two switches: choose two columns on which
the matrices differ, exchange one \(1,0\) pair with one \(0,1\) pair, and
iterate the symmetric-difference distance.  After forgetting column
labels, one such switch is a quadratic uniform-set relation

\[
 e_A+e_B-e_{A-a+b}-e_{B-b+a}.                    \tag{6.3}
\]

It remains to reduce (6.3) to trades (4.2).  Induct on
\(|A\setminus B|\).  The first nontrivial case is exactly a four-label
trade with a common \((r-2)\)-set.  In the general case choose one further
pair \(c\in A\setminus(B\cup\{a\})\),
\(d\in B\setminus(A\cup\{b\})\).  Insert the two intermediate
\(r\)-sets obtained by exchanging \(c,d\).  One four-label trade removes
\(a,b,c,d\), and the remaining quadratic relation has smaller symmetric
difference.  Induction proves that (6.3), and hence every balanced signed
multiset, belongs to \(\mathcal L_r\). \(\square\)

Every elementary generator on the global ground set can be embedded in a
top whenever its union of size \(r+2\) fits inside \(U\), i.e.

\[
 r+2\le M.                                          \tag{6.4}
\]

This explains the harmless restriction \(q\le H-2\) on upper-rank
absorption.

## 7. Positivity and order-space invariants

The lattice theorem is a statement about formal signed incidence.  A
physical segment absorber chooses between two nonnegative configurations
\(\mathcal C_0,\mathcal C_1\).  For a fixed collection of absorber tops,
the attainable correction set is therefore a signed zonotope

\[
 \left\{\sum_j\varepsilon_j\tau_j:
              \varepsilon_j\in\{-1,+1\}\right\}, \tag{7.1}
\]

or its translated \(0/1\) version.  It need not contain every lattice
vector with the correct singleton marginals.  Availability and magnitude
remain genuine constraints.

At the order level there is one further parity observation.  In a rooted
linear representation, \(\pi_{00},\pi_{11}\) have one permutation parity,
and \(\pi_{10},\pi_{01}\) have the opposite parity.  Thus rectangle moves
change the number of odd orders at one top by \(0\) or \(2\), preserving it
modulo two.  For unrooted cyclic orders this parity is intrinsic only when
\(M\) is odd; if \(M\) is even, a one-step cyclic rotation reverses
permutation parity, so no cyclic-order parity invariant remains.

This order parity is not visible in \(\mathcal R_r\) and does not create a
rank-incidence parity obstruction.  It may matter when one asks whether a
prescribed formal sum of trades can be lifted through a fixed pair of
physical segment orders.

## 8. The common first-moment invariant

For one full cyclic packet on top \(U\), every label \(x\in U\) lies in
exactly \(r\) of its \(M\) cyclic intervals of length \(r\).  A
complementary-segment configuration contains every phase at least once and
the overlap \(S\cap T\) twice, but the single copy outside the overlap is
stitched from two different orders.  Its marginal therefore has the form

\[
 r\,\mathbf 1_U+h^{(r)}_{U,i},                    \tag{8.1}
\]

where \(h^{(r)}_{U,i}\) is the complete stitching correction in diagonal
configuration \(\mathcal C_i\): it includes both the second copy on
\(S\cap T\) and the replacement of the reference order by the other order
on one principal segment.  This vector is generally not constant on
\(U\).  Since adjacent swaps alter only \(O(1)\) phase intervals at a fixed
rank, it differs from the literal overlap contribution by only \(O(1)\)
rank-\(r\) interval occurrences.

At every controlled rank \(r=m\pm q\), every rectangle trade lies in
\(\ker\partial_r\), so Theorem 3.1 gives

\[
 h^{(r)}_{U,0}=h^{(r)}_{U,1}.                     \tag{8.2}
\]

Thus the nonuniform stitching term is fixed under diagonal switching,
which is the property needed by the absorber.

If full top \(U\) is deployed with multiplicity \(n_U\), its global
coordinate marginal at rank \(r\) is

\[
 \boxed{
 d_x^{(r)}=r\sum_{U\ni x}n_U.}                    \tag{8.3}
\]

For complementary-segment deployments the exact formula is instead

\[
 \boxed{
 d_x^{(r)}=r\sum_{U\ni x}n_U+b_x^{(r)},}          \tag{8.4}
\]

where \(b^{(r)}\) is the sum of the fixed stitching vectors (8.2).  It may
depend on the chosen orders, segment boundaries, and rank.  Hence balancing
the top degrees alone is not sufficient: the stitching baseline must also be
balanced or absorbed before the rectangle signs are chosen.

More precisely, the *total baseline* (full-packet part plus stitching part)
must have the required singleton marginals before rectangles are used.  A
rank error with nonzero singleton-marginal component cannot be removed by
any sequence of interval rectangles.  Once those exact marginals agree,
the lattice theorem says there is no further **formal** linear invariant.

## 9. Sequential vertical absorption

For different hard lengths \(r=m\pm q\), the formal rectangle effects have
disjoint rank support inside the hard band.  Consequently their incidence
vectors commute: correcting depth \(q\) does not reopen any other depth or
change the middle owner histogram.

This gives the following exact conditional statement.

### Proposition 9.1 (conditional sequential absorber)

Suppose an owner near-transversal has been replaced on a family of tops by
segment configurations (0.3), and suppose that for every target hard rank
\(r\):

1. the desired correction has zero singleton marginals;
2. it is a signed sum of the elementary trades allocated to absorber tops
   at separation \(r\); and
3. the required signs lie in the physical zonotope (7.1).

Then all target ranks can be corrected sequentially, with no change to the
middle-owner incidence and no change to previously corrected hard ranks.
The total extra owner duplication is \(O(QN_H)=o(W)\), and the total reset
toll remains \(o(W)\).

#### Proof

Choose the prescribed diagonal at every allocated absorber.  Theorem 3.1
identifies its segment difference with the full rectangle.  Section 4
isolates that rectangle to its assigned hard rank, while (4.4) preserves
the middle.  Therefore the choices for different ranks commute.  The two
global ledgers are (5.3)-(5.4). \(\square\)

The hypotheses of Proposition 9.1 are not yet proved for the residual of
the calibrated packet near-factor.  In particular:

* owner matching must come first;
* top degrees together with the fixed stitching baselines must supply the
  correct first moments;
* enough absorber tops must realize a spanning family of elementary trades;
  and
* the signed coefficients must fit the bounded nonnegative order-pair
  reservoir.

Thus the segment repair validates the vertical-decoupling **mechanism** but
does not finish the absorber theorem.

## 10. Audit ledger

### Proved

1. Full 0/2 packet rectangles cover at most \((1/2+o(1))W\) owners and are
   unusable as the core deployment.
2. One adjacent swap affects exactly two phase starts at every interval
   length.
3. Two complementary phase segments with \(O(Q)\) overlap can contain all
   hard-band sensitive starts.
4. The diagonal segment difference equals the full four-order rectangle
   with no boundary counterterm.
5. Separation \(m-q\) isolates lower depth \(q\), and separation \(m+q\)
   isolates upper depth \(q\), throughout \(q\le Q\le H-2\).
6. Both diagonal configurations have identical middle-owner incidence.
7. Each configuration retains \(M-O(Q)\) distinct owners, global duplicate
   overhead \(O(QN_H)=o(W)\), and reset toll \(o(W)\).
8. Rank-\(r\) rectangle trades generate exactly the integer kernel of the
   singleton-incidence map; there is no extra rank parity invariant.
9. The top multiplicities plus the fixed segment-stitching baselines
   determine the unalterable first moments at every rank.
10. Formal corrections at distinct hard ranks commute.

### Open

1. An owner-only calibrated packet near-transversal with a compatible
   absorber-top reserve.
2. Coordinate-balanced full-packet and segment-stitching marginals after the
   reserve is chosen.
3. An available signed-trade decomposition of every hard-rank residual.
4. Positivity inside the bounded segment-pair zonotope.
5. Therefore a complete sequential rectangle absorber.

The complementary-segment construction repairs the exact failure of the
full-packet rectangle.  It is a sound rank-isolating final absorber, but
only after the owner near-transversal and first-moment problems have been
solved.
