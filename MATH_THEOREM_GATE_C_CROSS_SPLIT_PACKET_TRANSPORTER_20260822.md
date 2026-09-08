# Gate C: a cross-split three-to-three packet transporter

**Status (2026-08-22).**  The construction below is proved for every odd
`b=2h+1>=5`.  It gives two three-atom matchings on different coordinate
splits whose covered sets differ by exchanging two structured `b^2`-vertex
packets.  Thus it is a genuine cross-split `3<->3` trade and a hole-packet
transporter.  Unlike the one-to-two absorber, it is not confined to one
fixed split.

The transporter preserves the number of covered vertices.  It does not by
itself reduce the leave or prove Gate C.  The remaining positive problem is
to build a large compatible network of these trades which routes an
arbitrary structured leave into the packet atlas of the one-to-two
absorbers.

## 1. The local identity

Let `A,B` be disjoint `b`-sets.  Label

\[
 A=\{0,1,\ldots,2h\},
 \qquad
 w=h-1,quad u=2h-1,quad v=2h.                       \tag{1.1}
\]

On `A` take the cyclic orders

\[
\begin{aligned}
 \alpha_0&=(0,1,\ldots,2h),\\
 \alpha_1&=(0,1,\ldots,2h-2,v,u),\\
 \alpha_2&=(u,h-2,h-3,\ldots,0,
                 h,h+1,\ldots,2h-2,v,w),
\end{aligned}                                         \tag{1.2}
\]

and let `mathcal D_i` be their decks of cyclic `h`-intervals.  Swapping the
last two entries of `alpha_0` changes exactly two deck members.  With

\[
\begin{aligned}
 L&=\{0,\ldots,h-2\},&M&=\{h,\ldots,2h-2\},\\
 A_*&=L\cup\{v\},&B_*&=M\cup\{u\},\\
 X&=L\cup\{u\},&Y&=M\cup\{v\},
\end{aligned}                                         \tag{1.3}
\]

one has

\[
 \mathcal D_0-\mathcal D_1=\{A_*,B_*\},
 \qquad
 \mathcal D_1-\mathcal D_0=\{X,Y\}.                 \tag{1.4}
\]

The first `h` entries of `alpha_2` form `X` and the next `h` form `Y`.
Moreover `mathcal D_0 cap mathcal D_2` is empty.  To check the latter,
besides `X,Y` the windows of `alpha_2` are

\[
 \{0,\ldots,h-a-1\}\cup\{h,\ldots,h+a-1\}
                    \quad(1\le a\le h-1),             \tag{1.5}
\]

\[
 \{h-a+1,\ldots,h-1\}\cup\{h+a,\ldots,2h\}
                    \quad(2\le a\le h-1),             \tag{1.6}
\]

together with

\[
 \{w,v\}\cup\{h+1,\ldots,2h-2\},
 \qquad
 \{1,\ldots,h-1,u\}.                                 \tag{1.7}
\]

Every displayed set has two components in the natural cycle, and `X,Y`
are the two non-natural sets in (1.4).  This proves disjointness, including
the case `h=2` by direct reading of the same formulas.

Define

\[
 \mathcal R=(\mathcal D_0\dot\cup\mathcal D_2)-\mathcal D_1.
                                                               \tag{1.8}
\]

Then

\[
 \boxed{
 \mathcal D_0\dot\cup\mathcal D_2
 =\mathcal D_1\dot\cup\mathcal R,
 \qquad |\mathcal R|=b.}                              \tag{1.9}
\]

For `h=2`, `mathcal R` happens to be another cyclic deck; for `h>=3` it is
not.  That distinction does not affect the transporter identity.

Fix any cyclic order `beta` on `B` and let `mathcal Y` be its deck of
`(h+1)`-intervals.  Put

\[
 E_i=\{D\cup Z:D\in\mathcal D_i, Z\in\mathcal Y\}quad(i=0,1,2),
 \qquad
 P=\{R\cup Z:R\in\mathcal R, Z\in\mathcal Y\}.      \tag{1.10}
\]

Each `E_i` is a genuine product atom, `|P|=b^2`, and the Cartesian lift of
(1.9) is

\[
 \boxed{
 E_0\dot\cup E_2=E_1\dot\cup P.}                    \tag{1.11}
\]

Write

\[
                         D=E_1\dot\cup P
                           =E_0\dot\cup E_2.           \tag{1.12}
\]

Thus `D` is an absorber domain of size `2b^2`.

## 2. A disjoint copy on another split

Let

\[
                         W={2b\choose b}.              \tag{2.1}
\]

### Lemma 2.1 (existence of a disjoint cross-split domain copy)

For every odd `b>=5`, there is a coordinate permutation `g` such that

\[
                         D\cap gD=\varnothing          \tag{2.2}
\]

and

\[
                         gA\notin\{A,B\}.              \tag{2.3}
\]

#### Proof

First suppose `b>=9` and choose `g` uniformly from the symmetric group on
`A union B`.  For fixed middle vertices `S,T`, the probability `gS=T` is
`1/W`.  Therefore

\[
 \mathbb E|D\cap gD|={|D|^2\over W}={4b^4\over W},    \tag{2.4}
\]

and Markov's inequality gives

\[
 \Pr(D\cap gD\ne\varnothing)\le {4b^4\over W}.       \tag{2.5}
\]

Also

\[
 \Pr(gA\in\{A,B\})={2(b!)^2\over(2b)!}={2\over W}.  \tag{2.6}
\]

For `b=9`, direct arithmetic gives

\[
 {18\choose9}=48620>4\cdot9^4+2=26246.               \tag{2.7}
\]

The ratio `binom(2b,b)/b^4` is increasing for `b>=9`, since

\[
 {{2b+2\choose b+1}\over{2b\choose b}}
       =4-{2\over b+1}
       >\left(1+{1\over b}\right)^4.                 \tag{2.8}
\]

Hence `W>4b^4+2` for every `b>=9`.  The union of the bad events in
(2.5)--(2.6) has probability less than one, proving existence.

For the two remaining cases, label `A union B` by `0,...,2b-1` with
`A={0,...,b-1}`.  The following image lists give suitable permutations:

\[
\begin{array}{c|l}
b& (g(0),g(1),\ldots,g(2b-1))\\ \hline
5&(5,0,1,2,4,7,3,8,6,9),\\
7&(12,4,0,9,13,6,8,7,10,2,11,1,5,3).
\end{array}                                           \tag{2.9}
\]

The finite verification consists simply of applying each permutation to
the `2b^2` sets in (1.12); the companion script checks (2.2)--(2.3).
\(\square\)

## 3. The transporter trade

Fix a permutation from Lemma 2.1 and define

\[
 \mathcal M_- =\{E_1,gE_0,gE_2\},
 \qquad
 \mathcal M_+ =\{E_0,E_2,gE_1\}.                     \tag{3.1}
\]

### Theorem 3.1 (cross-split three-to-three packet transporter)

Both families in (3.1) are three-atom matchings.  Their covered sets obey

\[
\begin{aligned}
 \bigcup\mathcal M_-&=E_1\dot\cup gE_1\dot\cup gP,\\
 \bigcup\mathcal M_+&=E_1\dot\cup gE_1\dot\cup P.
\end{aligned}                                         \tag{3.2}
\]

Thus the matchings have the common covered core

\[
                              E_1\dot\cup gE_1,        \tag{3.3}
\]

and switching from `mathcal M_-` to `mathcal M_+` covers precisely `P`
while uncovering precisely `gP`.  The reverse switch transports the hole
packet in the opposite direction.  Atoms from the two sides of (3.1) use
the distinct unordered splits `{A,B}` and `{gA,gB}`.

#### Proof

Inside `D`, the atoms `E_0,E_2` are disjoint; inside `gD`, the atoms
`gE_0,gE_2` are disjoint.  Equation (2.2) makes every atom supported in
`D` disjoint from every atom supported in `gD`.  Hence both sides of (3.1)
are matchings.

Using (1.11) and its image under `g`,

\[
\begin{aligned}
 \bigcup\mathcal M_-
 &=E_1\dot\cup(gE_0\dot\cup gE_2)
  =E_1\dot\cup gE_1\dot\cup gP,\\
 \bigcup\mathcal M_+
 &=(E_0\dot\cup E_2)\dot\cup gE_1
  =E_1\dot\cup P\dot\cup gE_1.
\end{aligned}
\]

This is (3.2).  Distinctness of the splits is (2.3).  \(\square\)

The trade is exactly compatible with the fixed-band rigidity theorem.  It
does not try to replace a matching supported wholly inside one band by a
cross-split matching with the same covered set.  Instead, it uses a second,
disjoint cross-split domain and changes the covered packet from `gP` to
`P`.

There is a complement-symmetric version which directly respects the prime
coordinate-residue obstruction.  For a middle-layer family `mathcal F`, let
`overline mathcal F` denote its set of coordinate complements.  The
families `D,overline D` are disjoint because their members have respectively
`h,h+1` points in `A`.  Put

\[
                         H=D\dot\cup\overline D.       \tag{3.4}
\]

### Corollary 3.2 (complement-symmetric six-to-six transporter)

For every odd `b>=7`, one can choose a cross-split permutation `g` such
that

\[
                         H\cap gH=\varnothing.         \tag{3.5}
\]

Then

\[
 \mathcal M_-\dot\cup\overline{\mathcal M_-}
 \quad\longleftrightarrow\quad
 \mathcal M_+\dot\cup\overline{\mathcal M_+}          \tag{3.6}
\]

is a trade between six-atom matchings.  It exchanges the complement-closed
hole packet

\[
                         gP\dot\cup\overline{gP}
 \quad\text{with}\quad
                         P\dot\cup\overline P.         \tag{3.7}
\]

#### Proof

The set `H` has size `4b^2`.  For uniform random `g`,

\[
 \Pr(H\cap gH\ne\varnothing)\le {16b^4\over W},
 \qquad
 \Pr(gA\in\{A,B\})={2\over W}.                       \tag{3.8}
\]

At `b=11`,

\[
 {22\choose11}=705432>16\cdot11^4+2=234258,           \tag{3.9}
\]

and the monotonicity calculation (2.8) makes the inequality persist for
all larger `b`.  Thus a suitable `g` exists for `b>=11`.  For `b=7,9`, the
following verified image lists work:

\[
\begin{array}{c|l}
7&(0,11,1,13,8,12,9,10,7,3,6,5,2,4),\\
9&(8,13,2,5,10,14,1,7,11,15,4,9,16,0,3,17,12,6).
\end{array}                                           \tag{3.10}
\]

Condition (3.5) makes all four domains
`D,overline D,gD,overline{gD}` pairwise disjoint.  Apply Theorem 3.1 and
its coordinate complement simultaneously.  Their common cores and packet
differences are disjoint, which proves (3.6)--(3.7).  \(\square\)

This doubled transporter preserves complement symmetry at every stage.  It
does not assert such a doubled placement for the exceptional finite case
`b=5`.

## 4. What remains for a positive packing theorem

Make a directed packet graph whose vertices are permutation copies of
`P`.  Put an arc `P -> gP` whenever the corresponding domains can be chosen
disjoint as in Lemma 2.1.  Theorem 3.1 moves one uncovered packet along
such an arc without changing the total number of holes.

A coordinated Gate-C proof would follow from an atlas with both of the
following properties:

1. the eventual structured leave is tiled by packet vertices of this
   graph; and
2. vertex-disjoint transporter paths route those packets to triggers of
   the one-to-two absorbers, where they can be removed.

Theorem 3.1 proves that the packet graph has cross-split edges for every
odd `b>=5`.  It does not prove connectivity, simultaneous vertex-disjoint
routing, or a near-spanning packet tiling.  Those are the remaining global
matching/flow conditions.

## 5. Mechanical verification

The companion script

`scratch/verify_gate_c_cross_split_packet_transporter_20260822.py`

checks the local identity for odd `b=5,...,31`, checks both explicit
permutations in (2.9), verifies the two matching unions in (3.2), and checks
the doubled placements (3.10).
