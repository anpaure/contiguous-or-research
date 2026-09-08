# Upper-rich `D+2` rings: exact ledgers and the frame-Hamilton reduction

## Status

The shortest all-parity all-high ring with simple immediate-upper colours
has period `L=D+2`.  This note computes its exact packet degrees and every
two-resource occurrence class on the owner, immediate-lower, and
immediate-upper shores.

After owner normalization, lower-root load is exactly one and raw upper
load is `(r+1)/(r-1)`.  The surplus `2W/(r+1)` upper occurrences is
unavoidable and may be thinned only at the level of marked providers.

The integral problem has an exact graph form.  A frame `(H,K)` is a complete
graph on `F=H-K`: graph edges are owners, length-two paths are lower roots,
and graph vertices are upper colours.  A packet is a Hamilton cycle in this
graph.  Thus integral rounding is a simultaneous edge/path/vertex-coloured
Hamilton-cycle design.  No near-factor is claimed here.

## 1. The upper-rich ring

Put

\[
 n=2r-1,\qquad D=d+1,\qquad L=D+2,\qquad c=r-D.            \tag{1.1}
\]

Choose

\[
                         K\subset H\subset[n],
 \qquad |K|=c,\quad |H|=r+2,\quad F=H-K,\quad |F|=L.       \tag{1.2}
\]

Let

\[
                         f_0,f_1,\ldots,f_{L-1}             \tag{1.3}
\]

be a cyclic order of `F`, and use the source word

\[
                         A_t=K\cup\{f_t\}.                   \tag{1.4}
\]

Its owner, lower, and upper rows are

\[
 \begin{aligned}
 T_t&=H-\{f_{t-2},f_{t-1}\},\\
 Q_t&=H-\{f_{t-2},f_{t-1},f_t\},\\
 U_t&=H-\{f_{t-1}\},
 \end{aligned}                                             \tag{1.5}
\]

up to a common cyclic reindexing.

### Theorem 1.1 (shortest upper-rich all-high ring)

The word (1.4) is a literal state-balanced owner-once ring.  Its `L`
owners, `L` immediate-lower roots, and `L` immediate-upper colours are
separately pairwise distinct, of ranks `r,r-1,r+1` respectively.

The period `D+1` all-high ring has all immediate-upper colours equal.
Consequently `D+2` is the shortest all-high period with a simple upper row.

#### Proof

A length-`D=L-2` cyclic source interval omits a cyclic two-interval of `F`,
giving `T_t`.  Consecutive omitted two-intervals unite to a three-interval
and intersect in one label, giving `Q_t` and `U_t`.  Every interval length
`1,2,3` is proper in the `L`-cycle and recovers its start, proving
simplicity.  The source word is cyclically balanced under one-step
translation.

At period `D+1`, an owner omits one private label.  Two consecutive owners
omit different labels, so their union is the entire ambient set `H`.
\(\square\)

## 2. Packet count and exact one-resource degrees

Count an unoriented cyclic order as a Hamilton cycle on `F`; there are

\[
                              \gamma_L={(L-1)!\over2}.       \tag{2.1}
\]

such orders.

### Theorem 2.1 (exact packet and degree ledger)

The number of packets is

\[
 |\mathcal P|=
 \binom{2r-1}{r+2}\binom{r+2}{c}{(L-1)!\over2}.            \tag{2.2}
\]

Every owner has degree

\[
 D_O=\binom{r-1}{2}\binom{r}{c}(L-2)!,                    \tag{2.3}
\]

every lower root has degree

\[
 D_-=3\binom r3\binom{r-1}{c}(L-3)!,                      \tag{2.4}
\]

and every upper colour has degree

\[
 D_+=(r-2)\binom{r+1}{c}{(L-1)!\over2}.                    \tag{2.5}
\]

Moreover,

\[
                         D_O=D_-,\qquad
 {D_+\over D_O}={r+1\over r-1}.                            \tag{2.6}
\]

#### Proof

For a fixed owner `T`, choose the two labels of `H-T` from the `r-1`
labels outside `T`, choose `K subset T`, and choose a Hamilton cycle on `F`
containing the specified edge `H-T`.  A fixed edge lies in `(L-2)!`
unoriented Hamilton cycles, proving (2.3).

For a fixed lower root `Q`, choose `H-Q` as a triple from the `r` outside
labels and choose `K subset Q`.  The triple must occur consecutively in the
cycle.  There are three choices of its middle vertex, and a prescribed
two-edge path lies in `(L-3)!` Hamilton cycles.  This proves (2.4).

For a fixed upper set `U`, choose the missing label of `H` in `r-2` ways,
choose `K subset U`, and choose an arbitrary Hamilton cycle on `F`.  This
proves (2.5).  The identities (2.6) also follow immediately by counting
the `L` occurrences of each shore in every packet.  \(\square\)

## 3. Exact normalized pair ledgers

For two equal-rank sets, write `a=|X-Y|=|Y-X|`.  For two rows represented
as complements in `H` of cyclic intervals, write `h` for the overlap of
their hole intervals.

The following tables give:

* `m`: the number of second-row occurrences of the indicated class seen
  from one fixed first-row occurrence inside a packet;
* `N`: the number of possible second sets in that class for one fixed first
  set on `[2r-1]`.

By ground-set transitivity,

\[
                     {d(X,Y)\over D_{\rm first}}={m\over N}. \tag{3.1}
\]

### 3.1 Same-shore pairs

\[
\begin{array}{c|c|c|c}
\text{row}&\text{class}&m&N\\ \hline
O-O&a=1&2&r(r-1)\\
O-O&a=2&L-3&\binom r2\binom{r-1}2\\
Q-Q&a=1&2&(r-1)r\\
Q-Q&a=2&2&\binom{r-1}2\binom r2\\
Q-Q&a=3&L-5&\binom{r-1}3\binom r3\\
U-U&a=1&L-1&(r+1)(r-2)
\end{array}                                                \tag{3.2}
\]

All omitted classes have codegree zero.

### 3.2 Cross-shore pairs

For owner--lower pairs, the hole lengths are two and three:

\[
\begin{array}{c|c|c}
h&m&N\\ \hline
2&2&r\\
1&2&\binom r2(r-1)\\
0&L-4&\binom r3\binom{r-1}2
\end{array}.                                               \tag{3.3}
\]

For owner--upper pairs, the hole lengths are two and one:

\[
\begin{array}{c|c|c}
h&m&N\\ \hline
1&2&r-1\\
0&L-2&r\binom{r-1}2
\end{array}.                                               \tag{3.4}
\]

For lower--upper pairs, the hole lengths are three and one:

\[
\begin{array}{c|c|c}
h&m&N\\ \hline
1&3&\binom r2\\
0&L-3&(r-1)\binom r3
\end{array}.                                               \tag{3.5}
\]

#### Proof

On a cyclic `L`-set, a two-interval has two neighbouring two-intervals and
`L-3` disjoint two-intervals.  A three-interval has two translates with
overlap two, two with overlap one, and `L-5` disjoint translates.  A
singleton is contained in two two-intervals and three three-intervals.
These observations give every `m` in (3.2)--(3.5).

For a fixed rank-`s` set, the number of rank-`t` sets meeting it in rank
`u` is

\[
                         \binom{s}{u}\binom{2r-1-s}{t-u}.   \tag{3.6}
\]

Substitution gives every `N` in the tables.  Finally, the symmetric group
is transitive on each pair class.  Double-count packet-pair incidences and
divide by the corresponding one-resource incidence count to obtain (3.1).
\(\square\)

### Corollary 3.2 (maximum pair scale)

Relative to the owner/lower degree `D_O`, the largest nontrivial pair
codegree is the containment owner--upper class:

\[
                         {\Delta_2\over D_O}={2\over r-1}.  \tag{3.7}
\]

The aggregate normalized double-overlap mass of one three-shore packet is

\[
 {1\over D_O}\sum_{\{x,y\}\subset P}d(x,y)=O(L/r)=O(r^{-1/2})             \tag{3.8}
\]

at triangular depth.

#### Proof

The first assertion follows by inspection of the exact tables, using
`D_+/D_O=(r+1)/(r-1)` for an upper--upper pair.  For (3.8), sum the table
entries over the `O(L^2)` pairs in one packet.  The only order-`1/r`
classes have only `O(L)` occurrences; the `O(L^2)` classes have normalized
codegree `O(L/r^2)` or smaller.  \(\square\)

## 4. Unavoidable upper multiplicity

Let

\[
 W=\binom{2r-1}{r},\qquad W_+=\binom{2r-1}{r+1}
       ={r-1\over r+1}W.                                  \tag{4.1}
\]

### Theorem 4.1 (sharp upper slack)

Any owner-exact cyclic chronology has `W` immediate-upper occurrences.
Even if they are simple inside every packet, globally it has at least

\[
                         W-W_+={2W\over r+1}                \tag{4.2}
\]

repeated upper occurrences.  In the symmetric fractional packet factor,
every upper target has raw load

\[
                         {W\over W_+}={r+1\over r-1}.       \tag{4.3}
\]

Marking the fraction `(r-1)/(r+1)` of upper occurrences gives exact marked
load one.  Equation (4.2) is therefore the exact unavoidable unmarked
upper bank.

#### Proof

There is one upper occurrence per owner transition.  Pigeonhole gives
(4.2), and ground-set transitivity gives (4.3).  \(\square\)

Physical duplicates cannot simply be deleted; the marking only chooses
which occurrences certify the upper targets.  Integral rounding must retain
all transitions while assigning one provider occurrence to every upper
target.

## 5. Exact frame-Hamilton formulation

For one frame `(H,K)`, put a complete graph on vertex set `F=H-K`.

\[
\begin{array}{c|c}
\text{graph object}&\text{Boolean resource}\\ \hline
\text{edge }fg&H-\{f,g\}\quad(\text{owner})\\
\text{two-edge path }f-g-h&H-\{f,g,h\}\quad(\text{lower root})\\
\text{vertex }g&H-\{g\}\quad(\text{upper colour})
\end{array}.                                               \tag{5.1}
\]

### Theorem 5.1 (edge--path--vertex Hamilton equivalence)

An upper-rich packet on `(H,K)` is exactly a Hamilton cycle in `K_F`.
Consequently, an integral packet family is owner/lower exact with an upper
provider assignment precisely when one can select Hamilton cycles from
frames so that:

1. every labelled graph edge in (5.1) is selected at most once globally,
   and the selected edges cover the owner shore;
2. the selected consecutive edge-pairs have distinct path colours and
   cover the lower shore; and
3. among the physically repeated selected graph vertices, one occurrence
   is assigned to every upper colour.

#### Proof

The cyclic private-label order is a Hamilton cycle on `F`.  Formula (1.5)
identifies its graph edges, length-two paths, and vertices with the three
resource rows.  All three assertions follow.  \(\square\)

### Proposition 5.2 (Walecki subreduction)

Suppose first that complete frame edge sets

\[
             \mathcal E(H,K)=\{H-e:e\in\binom F2\}         \tag{5.2}
\]

have been chosen owner-disjointly.

* If `L` is odd, each `K_F` decomposes into `(L-1)/2` Hamilton cycles.
  These cycles cover every owner edge once and create the same number of
  pairwise distinct lower roots inside that frame as owner edges.
* If `L` is even, Walecki decomposition leaves one perfect matching of
  owner edges after `(L-2)/2` Hamilton cycles.

In the odd case, the remaining lower-row problem is to choose the Walecki
decompositions so that their path colours are globally rainbow.  In the
even case, the unmatched perfect matchings require a second frame length or
a priced sidecar.

#### Proof

Use the standard Hamilton decomposition of a complete graph.  Two
edge-disjoint cycles cannot use two different length-two paths on the same
three vertices, because any two such paths share an edge.  Thus the lower
roots created by one decomposition are distinct.  The parity statements
are the usual edge counts for `K_L`.  \(\square\)

### Proposition 5.3 (the owner-frame hypergraph is exactly regular)

Regard every complete frame edge set `mathcal E(H,K)` in (5.2) as one
hyperedge on the owner shore.  It has size `binom(L,2)`, and every owner has
frame degree

\[
                         D_F=\binom{r-1}{2}\binom r c.       \tag{5.3}
\]

Two owners at Johnson distance one have frame codegree

\[
                         (r-2)\binom{r-1}{c},               \tag{5.4}
\]

while two owners at distance two have frame codegree

\[
                         \binom{r-2}{c};                    \tag{5.5}
\]

all larger distances have codegree zero.  Therefore

\[
 {\Delta_{2,F}\over D_F}
      ={2D\over r(r-1)}=O(D/r^2).                          \tag{5.6}
\]

Uniform frame weight `1/D_F` is an exact fractional owner factor.

Nevertheless its aggregate double-overlap mass is not small.  For one
frame edge, exactly

\[
                         L\binom{L-1}{2}                    \tag{5.7}
\]

owner pairs have intersecting two-holes, and exactly

\[
                         3\binom L4                         \tag{5.8}
\]

have disjoint two-holes.  Hence

\[
 \begin{aligned}
 \Xi_F={}&L\binom{L-1}{2}{2D\over r(r-1)}\\
 &+3\binom L4
   {2D(D-1)\over r(r-1)^2(r-2)}.                           \tag{5.9}
 \end{aligned}
\]

At triangular depth this is

\[
                              \Xi_F=\Theta(D^4/r^2)=\Theta(1).             \tag{5.10}
\]

#### Proof

For a fixed owner `T`, choose `H-T` as a two-set outside `T` and choose
`K subset T`, proving (5.3).  At distance one, `H` has one remaining free
label outside the union of the two owners and `K` lies in their
rank-`r-1` intersection, giving (5.4).  At distance two, `H` is their union
and `K` lies in the rank-`r-2` intersection, giving (5.5).  Divide (5.4)
by (5.3), use `c=r-D`, and note that the distance-one value dominates.
The pair counts (5.7)--(5.8) are the numbers of pairs of graph edges which
share one endpoint or are disjoint.  Multiply them by the two normalized
codegrees to obtain (5.9).  \(\square\)

Thus the first owner-frame selection has vanishing **maximum** codegree and
an exact fractional factor, but fails the stronger aggregate-linear
condition `Xi=o(1)`.  A matching theorem which requires only
`Delta_2/D_F=o(1)` would suffice for an approximate frame cover; the
aggregate-linear alteration theorem does not apply at this scale.  This is
why the sparse Hamilton-cycle packets, whose aggregate collision mass is
`O(D/r)`, remain the better direct cover-down atoms.  The frame reduction is
structural, not by itself a near-factor theorem.

## 6. Contracted lower-chain packet design

For a source phase `t`, let

\[
 \mathcal C_t=(V_{t,1}\subset V_{t,2}\subset\cdots\subset V_{t,d})        \tag{6.1}
\]

be the nested proper suffix chain ending at the corresponding owner.  The
private phase labels make all `L` chains target-disjoint inside one packet.

Contract each `mathcal C_t` to one occurrence-labelled ticket.  A decorated
packet then has:

* `L` owner resources;
* `L` contracted lower-chain tickets (whose top members are the lower
  `q1` roots);
* `L` physical upper occurrences, with a provider mark on a fraction
  `(r-1)/(r+1)` in the fractional model.

For any fixed pure packet orbit and fixed chain-shape orbit `A`, the exact
ticket degree is

\[
                    D_A={|\mathcal O|m_A\over|\mathfrak C_A|},             \tag{6.2}
\]

where `m_A` is the number of tickets of shape `A` in one packet and
`mathfrak C_A` is its ground-set orbit.  For a pair orbit `B` of tickets,

\[
                    D_B={|\mathcal O|m_B\over|\mathfrak C_B|}.             \tag{6.3}
\]

These are finite explicit orbit formulas: the chain shapes are determined
only by `(delta,j)`, the low/high phase offset, and the endpoint offset.

### Proposition 6.1 (explicit pure-ticket shapes and degrees)

Fix a pure type `(delta,j)` of period `L_j`, and put `ell=j+1`.  Number an
endpoint by its offset `p in {0,...,j}` after the preceding high separator.
The ranks in its suffix ticket are

\[
 s_q^{(p)}=
 \begin{cases}
 c-\delta+q,&1\le q\le p,\\
 c+q,&p<q\le d,
 \end{cases}                                               \tag{6.4}
\]

with the first line empty when `p=0`.  Every packet has exactly

\[
                              {L_j\over j+1}                 \tag{6.5}
\]

tickets of each offset type.  Since `x_(delta,d)=0`, every positive-weight
type has `j<d`, and every ticket ends at rank `r-1`.

The ground-set orbit of offset zero has size

\[
             |\mathfrak C_{\delta,0}|
                  ={k!\over(c+1)!\,r!},                    \tag{6.6}
\]

while for `1<=p<=j`,

\[
             |\mathfrak C_{\delta,p}|
                  ={k!\over(c-\delta+1)!\,(\delta+1)!\,r!}.
                                                                    \tag{6.7}
\]

Consequently the exact degree of a typed ticket is

\[
 D_{\delta,j,p}
   ={ |\mathcal O_{\delta,j}|\,L_j/(j+1)
      \over |\mathfrak C_{\delta,p}|}.                     \tag{6.8}
\]

#### Proof

A suffix ending at a high phase contains the full core at every width.  A
suffix ending `p>=1` phases into a low run omits the `delta`-set until its
width reaches `p+1`, when the preceding high separator enters and restores
all `delta` coordinates at once.  This proves (6.4)--(6.5).

For any strict rank vector `s_1<...<s_d`, the number of labelled nested
chains with those ranks is

\[
 {k!\over s_1!\,(s_2-s_1)!\cdots(s_d-s_{d-1})!\,(k-s_d)!}. \tag{6.9}
\]

Substitute (6.4): all increments are one except for the single increment
`delta+1` after level `p`.  This gives (6.6)--(6.7).  Double-count
packet-ticket incidences to obtain (6.8).  \(\square\)

For two typed tickets, their orbit is determined by the finite matrix

\[
                         \eta_{ab}=|V_a\cap V'_b|
                         \qquad(1\le a,b\le d).             \tag{6.10}
\]

Indeed this matrix determines the atom sizes in the common refinement of
the two nested flags.  If `m_(alpha,beta,eta)` is the number of ordered
ticket pairs with this matrix in one packet, then the exact contracted
pair codegree is

\[
 D_{\alpha,\beta,\eta}
   ={ |\mathcal O|m_{\alpha,\beta,\eta}
      \over |\mathfrak C_{\alpha,\beta,\eta}|}.             \tag{6.11}
\]

Thus contraction leaves only a finite, explicitly enumerable list of
offset/profile inequalities; it introduces no hidden asymptotic degree
parameter.  The unresolved issue is which of those ticket pairs conflict
through a common named target after different packet embeddings are
combined.

### Exact integral design problem

Let `X` be the disjoint union of owner vertices, upper-provider vertices,
and contracted ticket occurrences.  Let `mathcal H_ring` have one hyperedge
for every integrally marked upper-rich pure packet.  Add a conflict between
two ticket vertices exactly when their internal named-target chains share a
target.

The required lower/`q1` cover-down is a matching in `mathcal H_ring` which:

1. saturates every owner;
2. selects one provider for every upper target;
3. uses no conflicting ticket pair; and
4. leaves only the prescribed triangular boundary tickets plus the allowed
   terminal sidecar.

Theorems 2.1--4.1 prove exact fractional balance and vanishing ordinary
pair spread.  They do not eliminate the ticket-conflict cuts.  Those cuts
are the chain-contracted form of the PBBS cover-free obstruction.

## 7. Exact remaining obstruction

The degree/codegree ledger is favourable enough for a growing-uniformity
cover-down theorem: packet size is `O(D^2)` after exposing ticket contents,
and all noncontainment pair ratios are `O(D/r)`.  However, the following
three hypotheses are still unproved and are each necessary for a direct
matching/absorption application:

1. **Ticket all-cuts:** every family of named lower targets has enough
   compatible chain tickets after owner and upper conditioning.
2. **Upper-provider recourse:** the unavoidable surplus (4.2) can be
   assigned without destroying the ticket matching.
3. **Absorbing closure:** the leave of a growing-uniformity cover-down lies
   in the trade lattice of edge--path--vertex Hamilton packets.

Thus the upper-rich family closes all marginal and ordinary codegree rows.
The exact unsolved object is a correlated rainbow Hamilton design with
chain-ticket conflicts, not another scalar or fractional obstruction.
