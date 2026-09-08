# Multi-frame rainbow packets: exact two-resolution theorem

Date: 2026-07-25

## 0. Scope

This note does **not** prove coefficient one.  It addresses the precise
cross-stratum problem left after
`ROTOR_SCD_PARITY_CHECK_CYCLE_TILING_20260725.md`, Theorem 4.1.

The main positive result is an exact integer theorem.  After one common
scaling, the complete central band has two simultaneous resolutions:

1. a **dynamic resolution** into long-residence, two-sided-rainbow rotor
   cycles using many coordinate-pair frames, with total reset toll
   (O(QW/sqrt m));
2. a **coverage resolution** of the very same labelled-chain multiset into
   (Q) genuine integral symmetric-chain decompositions.

Thus fixed-frame type capacity, local residence, two-sided shadow
injectivity, radius divisibility, and existence of genuine SCD colors all
coexist exactly.  What is not supplied is a low-fragmentation bijection
between the two resolutions.  The final theorem below states that remaining
integral gate exactly.

In particular, the note proves an exact integral owner partition with zero
designated band holes **after choosing any one SCD color**, but it does not
prove that the resulting physical pieces have sublinear bridge toll.  The
unproved assertion is the bridge/path-cover estimate
$(\mathrm{BR}_A)$, equivalently the still cleaner decorated-SCD gate
$(\mathrm{EP}_A)$ below.

Throughout,

\[
 n=2m,
 \qquad W=\binom{2m}{m},
 \qquad N_q=\binom{2m}{m-q}.
 \tag{0.1}
\]

Fix a clipped depth (H<m), put (N_{H+1}=0) only for the following
definition, and set

\[
 \gamma_d=
 \begin{cases}
 N_d-N_{d+1},&0\le d<H,\\
 N_H,&d=H.
 \end{cases}
 \tag{0.2}
\]

Then

\[
 \sum_{d=0}^H\gamma_d=W,
 \qquad
 \sum_{d=q}^H\gamma_d=N_q
 \quad(0\le q\le H).
 \tag{0.3}
\]

Choose a power of two (ell\le m) with (H\le\ell/2).  In the
coefficient-one application one may take the largest power of two at most
(m), so

\[
 m/2<\ell\le m
 \tag{0.4}
\]

and (H= A\sqrt m) is admissible for every fixed (A) and all sufficiently
large (m).

## 1. From one recursive cycle to a packet of symmetric chains

An (ell)-frame consists of disjoint sets

\[
 C,\quad \{a_1,b_1\},\ldots,\{a_\ell,b_\ell\},\quad D
 \tag{1.1}
\]

partitioning ([2m]), where

\[
 |C|=|D|=m-\ell.
 \tag{1.2}
\]

Its orientation cube is

\[
 Q(C;\{a_i,b_i\})=
 \left\{
 C\cup\{x_i: x_i\in\{a_i,b_i\},\ 1\le i\le\ell\}
 \right\}.
 \tag{1.3}
\]

Embed one cycle of the recursive factor (F_\ell) from Theorem 4.1 in
this cube and write its middle vertices cyclically as

\[
 Z_0,Z_1,\ldots,Z_{2\ell-1}.
 \tag{1.4}
\]

Write

\[
 Z_{i+1}=Z_i-r_i+s_i,
 \tag{1.5}
\]

with cyclic indices.  The pair indices in the transition word occur in an
order (pi\pi).  In particular every block of at most (ell) successive
transitions uses distinct frame pairs, and the (2\ell) outgoing ground
coordinates (r_i) are all distinct.

For (0\le q\le d\le\ell/2), define

\[
 L_q(i)=\bigcap_{j=0}^q Z_{i+j},
 \qquad
 U_q(i)=\bigcup_{j=0}^q Z_{i-j}.
 \tag{1.6}
\]

Then

\[
 |L_q(i)|=m-q,
 \qquad |U_q(i)|=m+q,
 \tag{1.7}
\]

and

\[
 L_d(i)\subset\cdots\subset L_1(i)\subset Z_i
 \subset U_1(i)\subset\cdots\subset U_d(i)
 \tag{1.8}
\]

is a saturated radius-(d) symmetric chain.  Denote it by
(mathcal C_{i,d}).

### Proposition 1.1 (one cycle is a genuine rotor packet)

For every (d\le\ell/2):

1. the (2\ell) chains
   (mathcal C_{0,d},\ldots,\mathcal C_{2\ell-1,d}) are pairwise
   disjoint;
2. their labelled radius-(d) states form one directed (2\ell)-cycle in
   the radius-(d) rotor graph;
3. the packet contains exactly (2\ell) masks in every rank
   (m-d,m-d+1,\ldots,m+d).

Call this collection a **radius-(d) rainbow packet** and denote it by
(mathcal P_d).

#### Proof

For the lower side, the labelled mask (L_q(i)) is exactly the forward
shadow (Sigma_q^+(Z_i)) in Theorem 4.1.  For the upper side it is the
reverse shadow (Sigma_q^-(Z_i)), with empty and full interchanged.
The two injectivity assertions in that theorem prove pairwise disjointness
at every rank.  Different ranks are automatically disjoint.

For the rotor assertion, the ordered singleton list of the state at (i)
is

\[
 r_{i+d-1},r_{i+d-2},\ldots,r_i,
 r_{i-1},r_{i-2},\ldots,r_{i-d}.
 \tag{1.9}
\]

Its lower block is (L_d(i)), and its residual block is the complement of
(U_d(i)).  Equation (1.5) and the no-repeat property give

\[
 L_d(i+1)=L_d(i)-r_{i+d}+s_i.
 \tag{1.10}
\]

Thus the rotor update uses (x=r_{i+d}) and (y=s_i), shifts the list
(1.9) by one position, and produces exactly the state at (i+1).  After
(2\ell) steps the state returns.  Item 3 follows from item 1. \(\square\)

## 2. Exact orbit multicover

Let

\[
 G=(2m)!.
 \tag{2.1}
\]

For every (d\le H), take (gamma_d) formal copies of
(sigma\mathcal P_d) for every coordinate permutation
(sigma\in S_{2m}).  Multiplicity is retained: two relabellings which
happen to give the same unlabelled packet are still different occurrences.
Let (mathfrak M) be the resulting labelled-chain multiset and put

\[
 \boxed{Q=2\ell G.}
 \tag{2.2}
\]

Let (Omega_d) be the set of oriented radius-(d) states

\[
 (L;z_1,\ldots,z_{2d};R),
 \qquad |L|=|R|=m-d.
 \tag{2.3}
\]

### Theorem 2.1 (exact multi-frame packet multicover)

The multiset (mathfrak M) has the following exact properties.

1. Every state in (Omega_d) occurs exactly
   
   \[
   {Q\gamma_d\over|\Omega_d|}
   \tag{2.4}
   \]
   
   times.
2. Every Boolean mask in every rank (m-H,\ldots,m+H) occurs in exactly
   (Q) designated chains.
3. The packets give a physical dynamic resolution of all occurrences into
   genuine rotor cycles.  Cutting each cycle once has exact prefix-reset
   toll
   
   \[
   \boxed{
   \mathfrak T_{\rm dyn}
   ={Q\over\ell}\sum_{d=1}^H d\gamma_d
   ={Q\over\ell}\sum_{q=1}^H N_q.}
   \tag{2.5}
   \]

#### Proof

The group (S_{2m}) is transitive on (Omega_d).  The packet
(mathcal P_d) contains (2\ell) radius-(d) states, so all its (G)
labelled relabellings contain (2\ell G=Q) state occurrences.  Repeating
this (gamma_d) times proves (2.4).

At rank (m\pm q), every radius-(d) chain with (d\ge q) contains one
mask.  Coordinate transitivity and (2.4) show that the contribution to a
fixed mask from radius (d) is (Q\gamma_d/N_q).  Summing and using
(0.3) gives degree (Q).

There are (gamma_dG) packet occurrences of radius (d).  One cut packet
has (2\ell) transition entries and exact prefix-extraction overhead
(2d).  Its reset contribution is therefore (2d).  Summing gives

\[
 \sum_{d=1}^H2d\gamma_dG
 ={Q\over\ell}\sum_{d=1}^H d\gamma_d.
 \tag{2.6}
\]

Finally, summation by parts in (0.2) gives

\[
 \sum_{d=1}^H d\gamma_d=\sum_{q=1}^HN_q.
 \tag{2.7}
\]

This proves (2.5). \(\square\)

### Corollary 2.2 (the dynamic toll is already negligible)

Uniformly in (H\le m),

\[
 \sum_{q=1}^H N_q=O(W\sqrt m).
 \tag{2.8}
\]

Consequently, for the choice (0.4),

\[
 \boxed{\mathfrak T_{\rm dyn}=O(QW/\sqrt m)=o(QW).}
 \tag{2.9}
\]

#### Proof

For (q\le m),

\[
 {N_q\over W}
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}
 \le \exp\left(-{q^2\over2m}\right).
 \tag{2.10}
\]

Indeed the (i)-th ratio is
(1-(2i+1)/(m+i+1)), and (m+i+1\le2m).  A Gaussian integral proves
(2.8), and (0.4) proves (2.9). \(\square\)

This is already stronger than a fractional calculation: it is an exact
integer (Q)-fold OR multicover carried by actual low-reset words.

### 2.1 Uniform-(H) collar lift

For the direct literal compiler it is useful to give **every** owner a full
radius-(H) physical collar, even when its designated SCD radius is only
(d<H).  This costs no leading term.

For every (d\le H), replace the packet (mathcal P_d) above by the full
packet (mathcal P_H) on the same recursive cycle, and tag each of its
owners by radius (d).  Its designated chain is the radius-(d) truncation
of its physical radius-(H) chain.  Take (gamma_d) copies of every
coordinate relabelling, just as before.  Denote the resulting collared
multiset by (mathfrak M^H).

### Proposition 2.3 (exact full-collar lift)

The tagged radius-(d) truncations in (mathfrak M^H) have exactly the
same state multiplicities (2.4) and exactly the same designated mask degree
(Q) as (mathfrak M).  Every occurrence additionally carries physical
lower and upper flags through depth (H).  Its dynamic packet resolution
has reset toll

\[
 \boxed{
 \mathfrak T_{\rm collar}
 =2HGW={QWH\over\ell}.}
 \tag{2.11}
\]

For (H=O_A(\sqrt m)) and (0.4), this is (O_A(QW/\sqrt m)=o_A(QW)).

#### Proof

Truncating the radius-(H) state at one center to radius (d) gives
exactly the state constructed directly at radius (d): formula (1.9) is
simply shortened at both ends.  The coordinate group is transitive on
(Omega_d), so the proof of (2.4) is unchanged.  Designated rank-
(m\pm q) masks are read only from tags (d\ge q), and (0.3) again gives
degree (Q).  Tags (d<q) merely furnish incidental additional physical
shadows.

There are

\[
 G\sum_{d=0}^H\gamma_d=GW
\]

full-collar packets.  Each costs (2H) to initialize, proving (2.11).
\(\square\)

## 3. The same multiset has an exact SCD resolution

Fix an arbitrary full symmetric-chain decomposition (mathcal D_0) of
(B_{2m}), clip it at depth (H), and retain each coordinate-labelled
chain state.  Take (2\ell) copies of every relabelled SCD
(sigma\mathcal D_0), (sigma\in S_{2m}).

### Theorem 3.1 (exact two-resolution identity)

As labelled-chain multisets,

\[
 \boxed{
 \mathfrak M
 =2\ell\bigsqcup_{\sigma\in S_{2m}}\sigma\mathcal D_0.}
 \tag{3.1}
\]

In particular, (mathfrak M) admits an exact coverage resolution into

\[
 Q=2\ell(2m)!
 \tag{3.2}
\]

genuine integral clipped SCD colors.

#### Proof

The clipped SCD (mathcal D_0) has exactly (gamma_d) radius-(d)
states.  Across its (G) coordinate relabellings, transitivity makes the
multiplicity of every member of (Omega_d) equal to

\[
 {G\gamma_d\over|\Omega_d|}.
 \tag{3.3}
\]

After (2\ell) repetitions this becomes

\[
 {2\ell G\gamma_d\over|\Omega_d|}
 ={Q\gamma_d\over|\Omega_d|},
 \tag{3.4}
\]

which is exactly the multiplicity in (2.4).  Equality holds state by state
and radius by radius, proving (3.1). \(\square\)

### Meaning of Theorem 3.1

The two exact resolutions solve different halves of the problem.

* Packet resolution: perfect physical chronology, exponentially diverse
  frame orders, two-sided rainbow shadows, and (o(QW)) reset toll.
* SCD resolution: exact one-owner coverage of every Boolean mask in every
  color.

The remaining problem is not divisibility or existence of either
resolution.  It is to synchronize them with few color changes along the
packet cycles.

There is no legal operation which divides the dynamic word by (Q).
Choosing one SCD color does give an exact integral owner partition and exact
designated coverage, but its occurrences may be scattered among
(Theta(W)) packet fragments.  Conversely, keeping one dynamic packet
layer preserves low reset cost but need not cover each Boolean mask once.
Thus (2.9) is a multiplicity-level statement, not a one-copy coefficient-one
proof.

## 4. Exact low-fragmentation gate

Choose a statewise bijection implementing (3.1), thereby coloring every
chain occurrence in every packet by one of the (Q) genuine SCD colors.
For a packet (P) of radius (d(P)) and a color (c), let
(r(P,c)) be the number of nonempty cyclic runs of color (c) around
the (2\ell)-cycle.  Define

\[
 \mathfrak T_{\rm frag}
 =\sum_P\sum_{c=1}^Q2d(P)r(P,c).
 \tag{4.1}
\]

### Theorem 4.1 (packet-resolution criterion)

Fix (A>0), let (H=\lceil A\sqrt m\rceil), and choose (ell) by
(0.4).  If the bijection in Theorem 3.1 can be chosen so that

\[
 \boxed{\mathfrak T_{\rm frag}=o_A(QW),}
 \tag{PR_A}
\]

then one of its (Q) SCD colors has rotor path-forest toll (o_A(W)).
Consequently the direct rotor--SCD construction gives the central band with
length (W+o_A(W)).  If ((\mathrm{PR}_A)) holds for every fixed (A),
the standard (A\to\infty) diagonal argument proves coefficient one.

#### Proof

For a fixed color and radius, its monochromatic packet runs are
vertex-disjoint directed rotor paths spanning all chains of that color and
radius.  Thus they form a legal rotor path forest, whose prefix toll is at
most the color's contribution to (4.1).  Summing over colors gives
(mathfrak T_{\rm frag}), so one color contributes at most
(mathfrak T_{\rm frag}/Q=o_A(W)).  The exact rotor extraction theorem
then gives the stated literal central-band word.  The audited tail estimate
and then (A\to\infty) give coefficient one. \(\square\)

Notice that Theorem 3.1 alone does not imply ((\mathrm{PR}_A)).  An
arbitrary statewise bijection may alternate colors at every position of
every packet.

### 4.1 A strictly weaker bridge-only gate

Apply Theorem 3.1 to the tagged truncations of the full-collar multiset
(mathfrak M^H).  Thus every occurrence is assigned one of the (Q) SCD
colors, and its full radius-(H) physical collar is retained as extra
data.

For one color (c), cut every collared packet into the maximal cyclic runs
whose owner occurrences have color (c).  Let (mathcal R_c) be the
resulting family of nonempty runs.  Every member of (mathcal R_c) is a
radius-(H) legal phase piece in the sense of the exact useful-prefix
compiler.  For two such pieces (R,R'), let (b(R,R')) be their exact
positive useful-prefix bridge length.  Define the optimal excess traveling
cost

\[
 B_c=min_{\text{linear orders }R_1,\ldots,R_t\text{ of }\mathcal R_c}
 \sum_{j=1}^{t-1}\bigl(b(R_j,R_{j+1})-1\bigr).
 \tag{4.2}
\]

### Theorem 4.2 (bridge-only descaling criterion)

For every statewise SCD resolution of (mathfrak M^H), each color (c)
satisfies the following two exact assertions.

1. The pieces in (mathcal R_c) partition all (W) middle owners.
2. Their physical flags cover every lower and upper mask through depth
   (H); in particular every aggregate hole count is zero.

Consequently, if the statewise bijections in Theorem 3.1 can be chosen so
that

\[
 \boxed{\sum_{c=1}^Q B_c=o_A(QW),}
 \tag{BR_A}
\]

then (mathrm{MFUP}_A) holds with zero shadow defect, and the direct
literal compiler gives coefficient one after the usual fixed-(A)
diagonalization.

#### Proof

One SCD color contains one chain centered at every middle mask.  The
statewise resolution assigns that chain to exactly one occurrence of that
center, so its packet runs partition the middle layer.

Now fix a target in rank (m\pm q), (q\le H).  Its color-(c) SCD chain
has tagged radius (d\ge q).  The physical radius-(H) collar of the
assigned occurrence restricts to exactly that tagged radius-(d) state.
Therefore its depth-(q) physical shadow is the target.  Extra flags from
owners tagged below (q) are harmless.  This proves zero holes.

Order the pieces using a minimizer in (4.2).  The exact direct phase
compiler gives length

\[
 W+2H+B_c.
 \tag{4.3}
\]

Under ((\mathrm{BR}_A)), some color has (B_c=o_A(W)), proving the
claim. \(\square\)

The gate ((\mathrm{BR}_A)) is strictly weaker than asking that packets be
nearly monochromatic.  Color changes may be numerous if the resulting
pieces can be reordered through short useful-prefix bridges.  Moreover the
coverage resolution constrains only the radius-(d) truncation; its many
full radius-(H) extensions remain available for collar synchronization.
This extension freedom is absent from the stronger exact-SCD path-forest
formulation.

### 4.2 Exact one-step bridge graph

A complete radius-$H$ state is an ordered partition

\[
 \omega=(L;z_1,\ldots,z_{2H};R),
 \qquad |L|=|R|=m-H.
 \tag{4.4}
\]

Only the useful prefix $(L;z_1,\ldots,z_{2H})$ is relevant to a bridge.
Let $\omega'$ have useful prefix
$(L';z'_1,\ldots,z'_{2H})$.

### Proposition 4.3 (complete classification of bridge-one arcs)

The exact useful-prefix bridge satisfies $b(\omega,\omega')=1$ if and only
if one of the following holds.

1. **Identity:**
   \[
   L'=L,
   \qquad (z'_1,\ldots,z'_{2H})=(z_1,\ldots,z_{2H}).
   \tag{4.5}
   \]
2. **Rotor shift:** for some $x\in L$ and $y\in R$,
   \[
   L'=L-x+y,
   \qquad
   (z'_1,\ldots,z'_{2H})=(x,z_1,\ldots,z_{2H-1}).
   \tag{4.6}
   \]
3. **Singleton promotion:** for some $x\in L$ and $1\le j\le2H$,
   \[
   L'=L-x+z_j,
   \qquad
   (z'_1,\ldots,z'_{2H})
   =(x,z_1,\ldots,z_{j-1},z_{j+1},\ldots,z_{2H}).
   \tag{4.7}
   \]

Consequently every useful prefix has exactly

\[
 \boxed{1+(m-H)^2+2H(m-H)=1+m^2-H^2}
 \tag{4.8}
\]

distinct bridge-one successors.  The bridge-one digraph is regular and
strongly connected; it contains the ordinary radius-$H$ rotor graph as the
subgraph (4.6).

#### Proof

Append $L'$ to the source state.  After the new front block $L'$, the
surviving old blocks occur in the order

\[
 L\setminus L',\quad
 z_1\setminus L',\ldots,z_{2H}\setminus L',\quad
 R\setminus L'.
 \tag{4.9}
\]

The target requires the first $2H$ nonempty survivors to be singletons.
Since $|L|=|L'|$, either $L=L'$, or $L\setminus L'=\{x\}$ and
$L'\setminus L=\{y\}$.  In the first case all $2H$ old singleton blocks
must survive, giving (4.5).  In the second case $y$ lies either in $R$ or
among the old singleton blocks.  If $y\in R$, the first $2H$ survivors are
$x,z_1,\ldots,z_{2H-1}$, giving (4.6).  If $y=z_j$, precisely that old
singleton disappears and (4.7) results.  These alternatives are exhaustive
and each displayed update works.

The choices in (4.5)--(4.7) give distinct useful prefixes, proving (4.8).
Coordinate transitivity gives equal indegree and outdegree.  The rotor
subgraph is strongly connected for $H\le m-2$, so the larger bridge graph
is strongly connected. \(\square\)

### 4.3 Exact collar-extension reservoir

Let

\[
 \omega_d=(L;z_1,\ldots,z_{2d};R)\in\Omega_d.
\]

A radius-$H$ extension of $\omega_d$ is obtained by choosing and ordering
$H-d$ elements of $L$ below its displayed singleton list and independently
choosing and ordering $H-d$ elements of $R$ above that list.  Hence the
number of extensions is exactly

\[
 \boxed{
 E_{d,H}=\bigl((m-d)_{H-d}\bigr)^2.}
 \tag{4.10}
\]

The stabilizer of $\omega_d$ is transitive on these extensions.  It follows
that, conditional on any tagged radius-$d$ state in the full-collar
multicover $\mathfrak M^H$, every one of its $E_{d,H}$ extensions occurs
with equal multiplicity.

There is an exact orbit identity which removes the apparent global-capacity
qualification.  Take any clipped SCD $\mathcal D$, and independently choose
one radius-$H$ extension of every tagged chain state of $\mathcal D$.
Call the result a **decorated SCD** $\widetilde{\mathcal D}$.

### Proposition 4.4 (decorated-SCD orbit identity)

For every decorated SCD,

\[
 \boxed{
 \mathfrak M^H
 =2\ell\bigsqcup_{\sigma\in S_{2m}}
 \sigma\widetilde{\mathcal D}}
 \tag{4.11}
\]

as multisets of tagged radius-$H$ useful states.

#### Proof

For a fixed tag $d$, the decorated SCD has exactly $\gamma_d$ full-collar
states.  The coordinate group is transitive on $\Omega_H$, so its complete
orbit contains every tagged radius-$H$ state with the same multiplicity.
After $2\ell$ repetitions, the total number of tag-$d$ occurrences is

\[
 2\ell G\gamma_d=Q\gamma_d.
\]

The tag-$d$ part of $\mathfrak M^H$ is also coordinate-invariant and has
the same total size.  Therefore the two multiplicities agree state by
state.  Sum over $d$. \(\square\)

Thus one may choose the collars in a single SCD first; the complete orbit
automatically supplies an exact capacity-respecting resolution of the
packet multicover.

This yields a purely graph-theoretic sufficient theorem for one integral
object.

### Corollary 4.5 (extension path-cover gate)

If there is one decorated SCD whose $W$ useful states have a directed path
cover in the bridge-one graph with

\[
 \boxed{p=o_A(W/H),}
 \tag{EP_A}
\]

then $(\mathrm{BR}_A)$, hence $\mathrm{MFUP}_A$, holds.

#### Proof

Use each bridge-one path as one fused phase.  Between different paths use
an arbitrary useful-prefix bridge, whose excess is at most $2H$.  Hence the
decorated SCD itself has bridge excess at most

\[
 B\le2Hp=o_A(W).
 \tag{4.12}
\]

Its chains already give zero shadow holes.  Equivalently, apply Proposition
4.4 to all coordinate copies and then Theorem 4.2. \(\square\)

The degree formula (4.8), extension count (4.10), and orbit identity (4.11)
remove every local availability, capacity, and divisibility concern.  They
do not prove $(\mathrm{EP}_A)$: one decorated integral SCD must still form
long bridge-compatible paths.  This is the remaining correlated integral
selection problem in its weakest current form.

### Theorem 4.6 (exact ordered-Hall formula for the remaining gate)

Fix a clipped SCD $\mathcal D$.  For each of its chains $K$, let
$\mathcal E_H(K)$ be the extension list of size (4.10).  A collar selector
$e$ chooses one member $e(K)\in\mathcal E_H(K)$ for every chain.

Given also a total order $\prec$ on the chains, form the split bipartite
graph $B(e,\prec)$ with a left and right copy of every chain and an edge

\[
 K_{\rm L}K'_{\rm R}
 \tag{4.12a}
\]

exactly when $K\prec K'$ and the chosen useful states have a bridge-one arc
$e(K)\to e(K')$.  Put

\[
 \delta(e,\prec)=
 \max_{\mathcal A\subseteq\mathcal D}
 \bigl(|\mathcal A|-|N_{B(e,\prec)}(\mathcal A)|\bigr).
 \tag{4.12b}
\]

Then the exact minimum number of directed bridge-one paths covering one
chosen collar from every chain is

\[
 \boxed{
 p_H^*(\mathcal D)=
 \min_e\min_{\prec}\delta(e,\prec).}
 \tag{4.12c}
\]

Consequently $(\mathrm{EP}_A)$ is exactly

\[
 \boxed{
 \min_{\mathcal D}p_H^*(\mathcal D)=o_A(W/H).}
 \tag{4.12d}
\]

#### Proof

For fixed $e$ and $\prec$, the allowed directed graph is acyclic.  A
matching in its split graph selects arcs with at most one entering and one
leaving each vertex, hence gives a vertex-disjoint path cover with
$W-|M|$ paths.  Conversely every path cover can be made increasing in a
total order and gives a split matching of size $W-p$.  Therefore the global
minimum path count is

\[
 \min_e\min_{\prec}(W-\nu(B(e,\prec))).
\]

The deficiency form of Hall's theorem says

\[
 W-\nu(B)=\max_{\mathcal A}(|\mathcal A|-|N_B(\mathcal A)|),
\]

proving (4.12c).  Equation (4.12d) is Corollary 4.5. \(\square\)

The collar choice must be made before both the incoming and outgoing
matching constraints are evaluated.  Pairwise nonemptiness between chain
lists is therefore insufficient: one selected collar must support both
adjacent arcs.  This is the exact correlation absent from the marginal
Hall-continuation flows.

### Proposition 4.7 (first-band audit of the bridge graph)

Let two distinct owners $X,Y$ in one decorated SCD be joined by a
bridge-one arc.  If the source tag is positive, then

\[
 L_1(X)=X\cap Y.
 \tag{4.13}
\]

If the target tag is positive, then

\[
 U_1(Y)=X\cup Y.
 \tag{4.14}
\]

Consequently every bridge-one path cover, after deleting the arcs incident
with a radius-zero owner, projects to a two-sided-rainbow Johnson linear
forest.  If the path cover has $p$ components, this forest retains at least

\[
 W-p-2\gamma_0
 \tag{4.15}
\]

edges.

#### Proof

For a full useful state, its middle owner is

\[
 X=L\cup\{z_1,\ldots,z_H\}.
\]

In the rotor case (4.6),

\[
 Y=X-z_H+y.
\]

In the promotion case (4.7), a choice $j\le H$ leaves the middle owner
unchanged, and hence cannot join two distinct owners of one SCD color.  For
$j>H$,

\[
 Y=X-z_H+z_j.
\]

Thus in every relevant case $X\cap Y=X-z_H$.  This is the radius-one lower
member of every positive source tag.  Also the target singleton in position
$H+1$ is $z_H$, so its radius-one upper member is $Y+z_H=X\cup Y$.

Distinct positive-tag SCD chains own distinct lower and upper masks, proving
two-sided rainbowness.  A path cover has $W-p$ internal arcs.  At most
$\gamma_0$ have a radius-zero source and at most $\gamma_0$ have a
radius-zero target, proving (4.15). \(\square\)

This recovers the already proved first-band rainbow-forest phenomenon as a
necessary shadow of $(\mathrm{EP}_A)$ and checks that the bridge relaxation
does not hide a depth-one collision.

### 4.4 The SCD condition can be removed entirely

The direct useful-prefix compiler does not require the selected flags to
come from an SCD.  It only requires one useful state at every middle owner
and coverage of every target in the controlled band.  In fact the latter
condition is feasible with exact floor/ceiling balance at every depth,
simultaneously and integrally.

For a full radius-$H$ state $\omega_X$ centered at $X$, write

\[
 L_q(\omega_X)\subset X\subset U_q(\omega_X)
 \qquad(0\le q\le H)
 \tag{4.16}
\]

for its lower and upper flags.

### Theorem 4.8 (balanced full flags at every middle owner)

For every $H<m$ there is a selection

\[
 \omega_X\in\Omega_H
 \qquad\left(X\in\binom{[2m]}m\right)
 \tag{4.17}
\]

of one full useful state centered at every middle set such that, for every
$q\le H$, every rank-$(m-q)$ target occurs among the
$L_q(\omega_X)$ either

\[
 \left\lfloor {W\over N_q}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil {W\over N_q}\right\rceil
 \tag{4.18}
\]

times, and the analogous assertion holds for every rank-$(m+q)$ target
among the $U_q(\omega_X)$.  In particular all lower and upper targets
through depth $H$ are covered.

#### Proof

First construct the lower flags.  Use the layered inclusion network on

\[
 \binom{[2m]}m,\binom{[2m]}{m-1},\ldots,
 \binom{[2m]}{m-H}.
\]

Split every depth-$q$ set $S$ into an in-node and an out-node, and give
its internal arc the integral capacity interval

\[
 \left[
 \left\lfloor {W\over N_q}\right\rfloor,
 \left\lceil {W\over N_q}\right\rceil
 \right].
 \tag{4.19}
\]

At depth zero the capacity is exactly one.  Join each set to all of its
facets with capacity interval $[0,W]$, supply one unit at every middle set,
and demand total flow $W$ at the bottom.

There is a symmetric fractional flow: every depth-$q$ set has throughput
$\lambda_q=W/N_q$ and splits it equally among its $m-q$ facets.  A
depth-$(q+1)$ set has $m+q+1$ parents, and hence receives

\[
 {m+q+1\over m-q}\lambda_q
 ={W\over N_{q+1}}=\lambda_{q+1}.
 \tag{4.20}
\]

All lower and upper capacities are integral.  The standard
lower-bounded-flow reduction and total unimodularity of a directed
incidence matrix therefore give an integral flow.  Decomposing it into
$W$ unit paths gives one nested deletion flag from every middle owner,
with the multiplicities (4.18) simultaneously at all depths.

Apply the same construction independently to the complements of the
middle sets and then complement every resulting lower flag.  This gives
the upper flags with the same balanced multiplicities.

Write the successive lower deletions from $X$ as
$\alpha_1(X),\ldots,\alpha_H(X)$ and the successive upper additions as
$\beta_1(X),\ldots,\beta_H(X)$.  They combine into the full state

\[
 \begin{split}
 L&=X-\{\alpha_1,\ldots,\alpha_H\},\\
 (z_1,\ldots,z_H)&=(\alpha_H,\ldots,\alpha_1),\\
 (z_{H+1},\ldots,z_{2H})&=(\beta_1,\ldots,\beta_H),\\
 R&=[2m]-\bigl(X\cup\{\beta_1,\ldots,\beta_H\}\bigr).
 \end{split}
 \tag{4.21}
\]

Its flags are exactly the two prescribed flags. \(\square\)

Call a selection as in (4.17) a **covering prefix transversal** if every
lower and upper target through depth $H$ occurs at least once; balance is
not part of the definition.  Theorem 4.8 proves that such transversals
exist before chronology is imposed.

### Corollary 4.9 (covering-prefix path gate)

Suppose that, for $H=\lceil A\sqrt m\rceil$, there is a covering prefix
transversal whose selected useful states have a directed bridge-one path
cover with

\[
 \boxed{p=o_A(W/H).}
 \tag{CP_A}
\]

Then the complete central band through depth $H$ has a literal word of
length $W+o_A(W)$.  If $(\mathrm{CP}_A)$ holds for every fixed $A$, then
coefficient one follows by the usual diagonal argument.

#### Proof

Initialize the first useful state of each path and use one update entry for
each subsequent state.  A path containing $s$ owners costs exactly
$s+2H$ entries, so all paths together cost

\[
 W+2Hp=W+o_A(W).
 \tag{4.22}
\]

At the endpoint belonging to $X$, the initialized or updated MTF state
literally exposes all suffix unions in (4.16).  The covering-transversal
condition therefore covers the entire band.  The standard tail estimate
and diagonalization finish the implication. \(\square\)

This is strictly weaker than $(\mathrm{EP}_A)$.  Every decorated SCD in
Corollary 4.5 is a covering prefix transversal, because its designated
chain members cover the band, but $(\mathrm{CP}_A)$ imposes neither a
radius census nor disjointness of the selected flags.  The exact
coefficient-one gate furnished by this note should therefore be taken to
be $(\mathrm{CP}_A)$ rather than $(\mathrm{EP}_A)$.

Theorem 4.8 also isolates the obstruction sharply: exact integrality,
common middle ownership, simultaneous nesting, two-sidedness, and zero
holes are all achievable together.  What is not proved is that these
choices can be made inside $o(W/H)$ bridge-one paths.

### 4.5 Flag-sequence form of the bridge rule

Write a full useful state centered at $X$ as

\[
 \omega_X=(X;\alpha_1,\ldots,\alpha_H;
                 \beta_1,\ldots,\beta_H),
 \tag{4.23}
\]

where $\alpha_1,\ldots,\alpha_H$ are the successive lower deletions and
$\beta_1,\ldots,\beta_H$ are the successive upper additions.  Thus its
ordered singleton list is

\[
 (\alpha_H,\ldots,\alpha_1,
   \beta_1,\ldots,\beta_H).
 \tag{4.24}
\]

### Theorem 4.10 (exact queue--cache transition)

Let $X\ne Y$, and write $Y=X-a+b$, where $a\in X$ and $b\notin X$.
There is a bridge-one arc $\omega_X\to\omega_Y$ if and only if all of the
following hold.

1. The element removed from the owner is the first scheduled deletion:
   \[
   a=\alpha_1(X).
   \tag{4.25}
   \]
2. For some
   \[
   x\in X-\{\alpha_1(X),\ldots,\alpha_H(X)\},
   \tag{4.26}
   \]
   the target deletion queue is
   \[
   (\alpha_1(Y),\ldots,\alpha_H(Y))
   =(\alpha_2(X),\ldots,\alpha_H(X),x).
   \tag{4.27}
   \]
3. Put
   \[
   e=
   \begin{cases}
   b,&b\in\{\beta_1(X),\ldots,\beta_H(X)\},\\
   \beta_H(X),&b\notin\{\beta_1(X),\ldots,\beta_H(X)\}.
   \end{cases}
   \tag{4.28}
   \]
   Delete $e$ from the ordered source cache, retaining the order of the
   other entries.  The target cache is
   \[
   (\beta_1(Y),\ldots,\beta_H(Y))
   =\bigl(\alpha_1(X),
   (\beta_1(X),\ldots,\beta_H(X))\setminus e\bigr).
   \tag{4.29}
   \]

In particular, a bridge path is exactly a FIFO deletion queue coupled to
an ordered cache of absent coordinates: one deletes the head of the
queue, appends one reserve element to its tail, inserts the deleted
coordinate at the front of the cache, and either promotes the newly added
coordinate out of the cache or evicts the oldest cache entry.

#### Proof

In the notation of Proposition 4.3, a change of middle owner must remove
$z_H=\alpha_1(X)$ and add $b$.  The new lower half of the singleton list is

\[
 (x,\alpha_H(X),\ldots,\alpha_2(X)),
\]

which is (4.27) after reversing it into deletion order.  The condition
$x\in L$ is exactly (4.26).

If $b$ belongs to the source upper singleton list, Proposition 4.3 is the
promotion case: $b$ disappears from that list.  If it does not, the update
is the rotor case, in which the last singleton $\beta_H(X)$ falls into the
residual tail.  In either case the old deleted owner-coordinate
$\alpha_1(X)$ enters the first upper position, giving (4.28)--(4.29).
The same calculation in reverse proves sufficiency. \(\square\)

The lower half has a particularly clean owner-path interpretation.  Let

\[
 X_{i+1}=X_i-a_i+b_i
 \tag{4.30}
\]

be a Johnson path.  Say that it has **forward residence $H+1$** if every
coordinate newly added at step $i$ remains in the middle owner for at
least the next $H+1$ owner occurrences; equivalently,

\[
 b_i\notin\{a_{i+1},\ldots,a_{i+H}\}
 \tag{4.31}
\]

whenever the displayed indices exist.

### Corollary 4.11 (one-sided residence and cache equivalence)

Away from the last $H$ vertices of a finite path, a Johnson owner path
lifts to bridge-one useful states if and only if it has forward residence
$H+1$.  Its lower deletion queue is then forced:

\[
 (\alpha_1(X_i),\ldots,\alpha_H(X_i))
 =(a_i,a_{i+1},\ldots,a_{i+H-1}).
 \tag{4.32}
\]

After an arbitrary valid initial upper cache is chosen, all later upper
caches are forced by (4.28)--(4.29).  Moreover, for every available
$q\le H$,

\[
 L_q(\omega_{X_i})
 =\bigcap_{j=0}^{q}X_{i+j}.
 \tag{4.33}
\]

No analogous consecutive-union identity is required: promotions may
reinsert a cached coordinate after one absent owner, and the upper flags
remain literal even in that case.

#### Proof

Iterating (4.27) gives (4.32).  The last new entry in the queue at step
$i$ must lie in

\[
 X_i-\{a_i,\ldots,a_{i+H-1}\};
\]

this is equivalent to saying that $a_{i+H}$ was already present at
$X_i$, which is precisely (4.31).  Conversely (4.31) makes every required
tail entry legal, so (4.27) constructs the lower half along the path.
Starting with any ordered $H$-subset of $[2m]-X_0$, recurrence
(4.28)--(4.29) preserves the property of being an ordered $H$-subset of
the current complement and therefore constructs the upper half.

Finally the $q$ scheduled removals in (4.32) are distinct and each is
absent from at least one of $X_i,ldots,X_{i+q}$.  Every element of $X_i$
outside those removals persists throughout that interval.  This proves
(4.33).  A promoted cache element gives the stated failure of a forced
past-union formula. \(\square\)

Consequently $(\mathrm{CP}_A)$ has the following exact owner-path form.
Find $o(W/H)$ forward-resident Johnson paths covering all middle owners;
complete the deletion queues freely on the final $H$ vertices of each
path, and choose one initial ordered $H$-cache on each path.  The lower
flags are the consecutive forward intersections at every nonboundary
position and the chosen queue completions at the boundary, while all upper
flags are the cache prefixes generated by (4.28)--(4.29).  These two flag
families must cover their respective band targets.  The slightly stronger
condition that the nonboundary forward intersections alone cover every
lower target is therefore sufficient.  This formulation is strictly less
rigid than the older requirement of simultaneous consecutive intersection
and union shadows with two-sided coordinate residence.

### 4.6 The stationary queue--cache relaxation is exact

The queue--cache graph has a completely explicit uniform circulation.  This
proves that the remaining obstruction is not continuous transport or
portal cost.

Let $\mathcal Q_H$ be the digraph on all full useful states, retaining only
the bridge-one arcs which change the middle owner.  Every owner has

\[
 M_H=(m)_H^2
 \tag{4.34}
\]

states: choose the ordered deletion queue and the ordered outside cache
independently.  By Theorem 4.10, every state has exactly

\[
 D_H=m(m-H)
 \tag{4.35}
\]

owner-changing successors: choose the newly added coordinate $b$ in the
current complement and the new queue-tail $x$ in the current reserve.

### Theorem 4.12 (exact stationary multicover)

For $H\le m-2$, the digraph $\mathcal Q_H$ is regular and strongly
connected.  It therefore has an Euler circuit.  After one useful-prefix
initialization, that circuit is a literal word of transition length

\[
 \boxed{W M_H D_H.}
 \tag{4.36}
\]

Along it every middle owner occurs exactly $M_HD_H$ times, and every fixed
lower or upper target at depth $q\le H$ occurs exactly

\[
 \boxed{M_HD_H,{W\over N_q}}
 \tag{4.37}
\]

times.  In particular (4.37) is an integer.  Normalizing by $M_HD_H$
gives a genuine stationary fractional solution with owner mass one and
perfectly uniform lower and upper loads $W/N_q$ at every depth
simultaneously.

#### Proof

The rotor arcs, obtained when $b$ lies in the residual set, form the
ordinary strongly connected radius-$H$ rotor graph.  Hence the larger
owner-changing graph is strongly connected.  The inverse form of
Theorem 4.10 gives the same indegree as (4.35): choose the predecessor's
newly added coordinate in the target reserve, and then either its promoted
cache position or its evicted residual coordinate.  Thus the graph is
Eulerian.

An Euler circuit uses every directed edge once, so it departs from every
state $D_H$ times.  There are $M_H$ states over each owner, proving the
owner multiplicity.

The coordinate group is transitive on the lower targets of any fixed
depth and preserves the full state set.  Since there are $WM_H$ states
and each carries one depth-$q$ lower target, every such target belongs to
exactly $WM_H/N_q$ states.  Multiplication by the $D_H$ departures proves
(4.37).  The upper calculation is identical. \(\square\)

Equivalently, if $z_\omega=1/M_H$ at every state and
$f_e=1/(M_HD_H)$ at every owner-changing bridge arc, then

\[
 \sum_{e\in\delta^+(\omega)}f_e
 =\sum_{e\in\delta^-(\omega)}f_e=z_\omega,
 \qquad
 \sum_{\omega:\,c(\omega)=X}z_\omega=1,
 \tag{4.38}
\]

and all flag marginals are exactly uniform.  Thus the linear relaxation of
$(\mathrm{CP}_A)$ has zero boundary and zero coverage defect, and one
explicit integer scaling of it is one actual MTF Euler word.

The unresolved descaling is now an integral **partition-circulation**
problem: select one state from each owner fibre, retain almost one incoming
and one outgoing bridge arc at each selected state, and preserve coverage
of all flag targets.  The equality between incoming and outgoing state at
the same owner is essential.  If it is dropped, the owner-incidence part
splits into ordinary bipartite transportation problems; Theorem 4.8,
separately, rounds all flag marginals.  What is not justified is one common
rounding which identifies the incoming state, outgoing state, and balanced
flag state at almost every owner.  That three-way identification is the
queue--cache synchronization obstruction.  Theorem 4.12 shows that no
fractional, divisibility, or multiplicity-level strengthening can by itself
settle it.

### Corollary 4.13 (owner-only cyclic description)

Let

\[
 X_{i+1}=X_i-a_i+b_i
 \qquad(i\in\mathbb Z/s\mathbb Z)
 \tag{4.39}
\]

be a cyclic Johnson trajectory with forward residence $H+1$, and assume
that every coordinate changes membership somewhere on the cycle.  For a
coordinate outside $X_i$, call its most recent transition from present to
absent its last open removal, and order the absent coordinates by these
removal times, most recent first.  Then there is a unique full useful state
over every $X_i$ which makes (4.39) a bridge-one cycle.  It is given by

\[
 \begin{aligned}
 (\alpha_1(X_i),\ldots,\alpha_H(X_i))
   &=(a_i,a_{i+1},\ldots,a_{i+H-1}),\\
 (\beta_1(X_i),\ldots,\beta_H(X_i))
   &=\text{the $H$ most recent open removals at time $i$}.
 \end{aligned}
 \tag{4.40}
\]

Consequently its literal flags have the owner-only form

\[
 L_q(X_i)=X_i-\{\text{the next $q$ removal labels}\},
 \tag{4.41}
\]

\[
 U_q(X_i)=X_i+\{\text{the $q$ most recent open removal labels}\}.
 \tag{4.42}
\]

#### Proof

Forward residence makes the next $H$ removal labels distinct members of
$X_i$, so the first line of (4.40) is valid and obeys the queue recurrence.
There are always $m$ absent coordinates, hence at least $H$ open absence
intervals.  At transition $i$, the newly removed $a_i$ becomes the newest
open interval.  If $b_i$ is among the previously $H$ newest open intervals,
that interval closes and is deleted from the list.  If it is older, closing
it does not change the old top $H$; insertion of $a_i$ then evicts their
oldest member.  These are exactly the two cases (4.28)--(4.29).

Thus (4.40) gives a bridge-one cycle.  The queue is forced by future
transitions.  On a cycle every absent coordinate has a well-defined most
recent open removal, so the cache recurrence is forced as well.  Equations
(4.41)--(4.42) are the definitions of the flags. \(\square\)

This gives a smaller owner-only sufficient target: a support-full cycle
cover of the middle layer with $o(W/H)$ cycles, forward residence $H+1$,
and complete coverage by the two event sets in (4.41)--(4.42).  Unlike the older
two-sided-run formulation, short absent runs are legal; they are handled by
cache promotion.

## 5. Up-set path-hitting form of packet ownership

For a rank-(m-q) mask (T), write

\[
 \mathcal U_T=\{X\in\tbinom{[2m]}m:T\subseteq X\}.
 \tag{5.1}
\]

### Proposition 5.1 (exact path-hitting dictionary)

Let (X_0,\ldots,X_q) be a Johnson path whose (q) transitions remove
distinct coordinates.  Then

\[
 \boxed{
 \bigcap_{i=0}^qX_i=T
 \quad\Longleftrightarrow\quad
 X_0,\ldots,X_q\in\mathcal U_T.}
 \tag{5.2}
\]

Dually, for a rank-(m+q) mask (U),

\[
 \boxed{
 \bigcup_{i=0}^qX_i=U
 \quad\Longleftrightarrow\quad
 X_0,\ldots,X_q\subseteq U.}
 \tag{5.3}
\]

#### Proof

Distinct removed coordinates imply

\[
 \left|\bigcap_{i=0}^qX_i\right|=m-q.
 \tag{5.4}
\]

If all vertices contain (T), then (T) is contained in this
intersection; equality follows from equal cardinalities.  The reverse
implication is immediate.  Equation (5.3) is the complement-dual argument.
\(\square\)

Therefore an integral packet resolution is exactly a simultaneous
path-hitting design: at depth (q), every up-set (mathcal U_T) must
contain exactly one selected (q)-edge packet segment whose start has
radius at least (q), and the complementary down-set condition must hold
simultaneously.  This formulation makes no reference to a global pair
frame and is the correct support language for cross-frame coupling.

## 6. Why resetting at frame changes cannot work

The exact packet orbit genuinely mixes coordinate frames.  This mixing is
not optional.

Fix one perfect matching (mathcal P) of the (2m) coordinates.  For a
rank-(m-q) target with (f) full pairs relative to (mathcal P), put

\[
 T_{f,q}=
 {m!\over f!(f+q)!(m-2f-q)!}2^{m-2f-q},
 \tag{6.1}
\]

and let

\[
 V_f={m!\over f!^2(m-2f)!}2^{m-2f},
 \qquad
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
 \tag{6.2}
\]

Suppose a rotor path forest uses (mathcal P)-pair flips except for
(s_q) exceptional arcs among its radius classes (d\ge q), and let
(P_q) be the total number of path components in those classes.

### Proposition 6.1 (critical density of transparent frame changes)

One has

\[
 \boxed{q(P_q+s_q)\ge D_{m,q}.}
 \tag{6.3}
\]

If (q=x\sqrt m+o(\sqrt m)) with fixed (x>0), then

\[
 {D_{m,q}\over W}\longrightarrow
 e^{-x^2}\Phi_{\rm G}(x/2)-\Phi_{\rm G}(-3x/2)>0.
 \tag{6.4}
\]

Consequently any (o(W))-toll construction has

\[
 \boxed{s_q=\Omega_x(W/\sqrt m).}
 \tag{6.5}
\]

If every exceptional arc is treated as a hard reset, those resets alone
cost (Omega_x(W)).  Hence the necessary frame changes must be
**transparent internal rotor transitions**, not seams at which the word is
reinitialized.

#### Proof

Across the classes (d\ge q), at least (N_q-qP_q) starts are followed
by (q) selected arcs.  One exceptional arc contaminates at most (q)
such windows, so at least (N_q-qP_q-qs_q) are pure fixed-frame windows.
Pure windows preserve the full-pair type (f), and type (f) has only
(V_f) starts for (T_{f,q}) possible targets.  Therefore

\[
 N_q-qP_q-qs_q
 \le\sum_f\min(V_f,T_{f,q})=N_q-D_{m,q},
 \tag{6.6}
\]

which proves (6.3).  The local central limit calculation giving (6.4) is
the fixed-pair capacity theorem.  An (o(W)) prefix toll implies
(P_q=o(W/q)), so (6.3)--(6.4) give (6.5).  Cutting at (s_q) radius-at
least-(q) transitions costs at least (2qs_q=\Omega_x(W)). \(\square\)

This rules out a tempting but invalid use of Theorem 4.1: one cannot glue
fixed-frame rainbow cycles and simply pay a reset at every change of frame.
The frame changes occur at the critical density (W/\sqrt m), and almost
all of them must preserve physical chronology across the splice.

## 7. Exact remaining theorem

The strongest packet-preserving target is $(\mathrm{PR}_A)$.  The direct
compiler proves that it is enough to solve the strictly weaker decorated
bridge problem:

> **Decorated-SCD bridge theorem $(\mathrm{EP}_A)$.**  For every fixed
> $A>0$, some clipped integral SCD admits one radius-$H$ extension of every
> chain state, $H=\lceil A\sqrt m\rceil$, such that the selected useful
> states have a bridge-one path cover with $o_A(W/H)$ components.

By Proposition 4.4, the complete coordinate orbit of that one decorated SCD
is automatically an exact resolution of the multi-frame packet multicover.
By Corollary 4.5, its bridge paths give a literal coefficient-one central
band with zero designated shadow holes.

This theorem is strictly integral.  The following have been proved exactly
above and therefore are not part of the remaining obstruction:

* mixing enough coordinate-pair frames to remove the Gaussian type bias;
* long coordinate residence;
* two-sided shadow injectivity through (A\sqrt m);
* the exact clipped radius census;
* divisibility after one explicit integer scaling;
* existence of genuine SCD colors;
* (o(QW)) dynamic reset cost before the two resolutions are synchronized;
* an exact integral owner partition and zero designated band holes in every
  SCD color;
* the complete bridge-one graph and every collar-extension multiplicity.

What remains is only the long path-cover assertion in $(\mathrm{EP}_A)$
(or the stronger packet synchronization $(\mathrm{PR}_A)$).  Proposition
6.1 shows that a proof must allow $(\Theta(W/\sqrt m))$-scale transparent
frame mixing; treating those changes as independent packet resets is
quantitatively incapable of proving coefficient one.  Neither
$(\mathrm{EP}_A)$ nor $(\mathrm{PR}_A)$ is proved in this note.
