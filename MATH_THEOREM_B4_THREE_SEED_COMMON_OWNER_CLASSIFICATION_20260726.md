# The three \(B_4\) seeds: exact owner-support classification and the forced antipodal completion

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

There are two different meanings of a three-seed \(B_4\) menu, and they
must not be conflated.

1. On a fixed first-eligible Cartesian packet, the three seeds are **not**
   common-owner states. A rectangular packet determines its seed in every
   active four-block. If two seed fields differ in \(d\) active blocks,
   their owner supports intersect in exactly the fraction \(2^{-d}\).
   Equality of supports occurs only when the seed fields are identical.
2. There is a genuine three-way common-owner trade after adding the forced
   antipodal completion. On the 24-owner carrier

   \[
        \binom B2\mathbin\square Q_2,
   \]

   each seed gives a factor into six physical \(C_4\)'s: four copies of
   its seed square and two reservoir cycles over its omitted antipodal
   pair. All three factors cover exactly the same owners.
3. Tensoring the 24-owner carrier solves the packetwise owner and
   intrapacket parts completely. For every
   \(\theta\in\{0,1,2\}^r\), the same support
   \(\mathcal V^r\) has a resolution into \(6^r\) physical \(Q_{2r}\)'s.
   When \(h=2r\) is a power of two, each resolution has an exact
   \(C_{2h}\)-factor whose two signed depth-\(q\) maps are injective on the
   whole packet for every \(q\le r\). Thus arbitrary seed density is
   compatible with exact ownership and intrapacket rainbows.
4. This positive local theorem does **not** give the requested aggregate
   Hall bound. In the fixed ordered first-eligible 8-block atlas, almost
   every packet selects all active blocks before the terminal quarter of
   the atlas. Every resolution above freezes that quarter. At each
   \(q=A\sqrt m+O(1)\), the resulting hypergeometric suffix cut forces
   \(\kappa_AW-o(W)\) missing targets for each sign.
5. Any two completed local factors have a common four-phase colouring.
   All three together do not: a common four-phase colouring would require
   six different colours at each fixed reservoir state. This obstructs a
   simultaneous six-row phase-labelled component switch, but not the
   packetwise tensor resolution in item 3.

Consequently the precise gate is split sharply. Exact one-copy ownership
and intrapacket injectivity hold on every completed packet, even at full
seed density; the first-eligible atlas covers
\(W-e^{-\Omega(m)}W\) owners this way.  No exact factorization of the
exceptional owner set is constructed here.  Even granting an arbitrary
exact completion of it, the aggregate \(o(W)\) Hall clause is false for
the fixed first-eligible atlas. A successful variant must move the exterior
block atlas, not merely mix the three internal seed frames.

## 1. The three local seeds

Let \(B=\{1,2,3,4\}\), and put

\[
\begin{aligned}
 M_0&=12\mid34,&
 \mathcal A_0&=\{13,14,23,24\},\\
 M_1&=13\mid24,&
 \mathcal A_1&=\{12,14,23,34\},\\
 M_2&=14\mid23,&
 \mathcal A_2&=\{12,13,24,34\}.
\end{aligned}                                                   \tag{1.1}
\]

Thus

\[
             \mathcal A_c=\binom B2\setminus M_c.               \tag{1.2}
\]

Each \(\mathcal A_c\) is the orientation square of the matching \(M_c\),
hence supports one physical \(C_4\). For example, take

\[
\begin{aligned}
 C_0&=(13,14,24,23),\\
 C_1&=(14,12,23,34),\\
 C_2&=(12,13,34,24).
\end{aligned}                                                   \tag{1.3}
\]

For distinct \(c,d\),

\[
       |\mathcal A_c|=4,\qquad
       |\mathcal A_c\cap\mathcal A_d|=2.                         \tag{1.4}
\]

In particular, rotations and reversals of one \(C_c\) preserve its owner
support, whereas changing \(c\) does not.

### Lemma 1.1 (all four-owner injective seeds)

Let \(U\subseteq\binom B2\) have four members, and let

\[
                         X_0\to X_1\to X_2\to X_3\to X_0          \tag{1.5}
\]

be a directed physical \(C_4\) on \(U\). If its four lower edge traces

\[
                         a_i=X_i\cap X_{i+1}                     \tag{1.6}
\]

are distinct, then, after cyclically labelling the four coordinates by
\(a_0,a_1,a_2,a_3\),

\[
                         X_i=\{a_{i-1},a_i\}.                    \tag{1.7}
\]

Consequently \(U\) is exactly one of the three sets \(\mathcal A_c\), and
the directed cycle is determined up to rotation and reversal. Its four
upper edge traces are automatically distinct.

#### Proof

The incoming trace \(a_{i-1}\) and outgoing trace \(a_i\) both belong to
the two-set \(X_i\). They are distinct by hypothesis, so they exhaust it,
proving (1.7). The four labels \(a_i\) are the four coordinates of \(B\).
Thus \(U\) consists of the four edges of the coordinate cycle

\[
             a_0a_1a_2a_3a_0,
\]

which is \(\binom B2\) with the two diagonals, a perfect matching,
deleted. This is one \(\mathcal A_c\). Finally,

\[
 X_i\cup X_{i+1}=\{a_{i-1},a_i,a_{i+1}\}
\]

omits the distinct coordinate \(a_{i+2}\), so the four upper traces are
distinct. \(\square\)

Thus even if one starts from the injectivity requirement rather than from
the displayed catalogue, no additional common-support local seed exists.

## 2. Exact classification of rectangular packet supports

Fix a physical atlas of disjoint four-blocks

\[
                         B_1,\ldots,B_b.                         \tag{2.1}
\]

For \(I\subseteq[b]\), a seed field
\(\sigma=(\sigma_i)_{i\in I}\in\{0,1,2\}^I\), and a fixed outside
configuration \(\xi\) on all coordinates outside
\(\bigcup_{i\in I}B_i\), define

\[
 \mathcal P(I,\sigma,\xi)
 =\left\{X:
      X\setminus\bigcup_{i\in I}B_i=\xi,\quad
      X\cap B_i\in\mathcal A_{\sigma_i}\ (i\in I)
   \right\}.                                                     \tag{2.2}
\]

We assume the fixed rank of \(\xi\) makes every member of (2.2) a middle
set. This includes the packet supports arising from a stable
first-eligible scan.

### Theorem 2.1 (owner-support rigidity)

For one fixed four-block atlas,

\[
 \mathcal P(I,\sigma,\xi)=\mathcal P(J,\tau,\zeta)                \tag{2.3}
\]

if and only if

\[
                         I=J,\qquad \xi=\zeta,\qquad \sigma=\tau. \tag{2.4}
\]

If \(I=J\), \(\xi=\zeta\), and

\[
 d=|\{i\in I:\sigma_i\ne\tau_i\}|,\qquad r=|I|,                  \tag{2.5}
\]

then

\[
 \boxed{
 |\mathcal P(I,\sigma,\xi)\cap
   \mathcal P(I,\tau,\xi)|
       =4^{r-d}2^d=4^r2^{-d}.}                                   \tag{2.6}
\]

#### Proof

Project a packet support onto one physical block \(B_i\). The projection
has four states precisely when \(i\) is active and one state otherwise.
Thus the support itself recovers \(I\). On an inactive block it recovers
the frozen state, hence it recovers \(\xi\). On an active block its
projection is exactly one of the three distinct sets
\(\mathcal A_0,\mathcal A_1,\mathcal A_2\), so it recovers
\(\sigma_i\). This proves (2.3)--(2.4).

For (2.6), the constraints are Cartesian across the active blocks. An
unchanged block contributes four common states, and a changed block
contributes two by (1.4). Multiplication gives \(4^{r-d}2^d\).
\(\square\)

### Corollary 2.2 (dense seed changes are not sparse owner edits)

Changing one seed expels two of the four local owners and imports two new
ones. More generally, changing \(d\) seeds retains only the fraction
\(2^{-d}\) of the old packet. Thus if

\[
                         d\ge c\frac h{\sqrt m}                    \tag{2.7}
\]

and \(h/\sqrt m\to\infty\), the common fraction is \(o(1)\). A seed
choice at the density required by the Gaussian fixed-frame audit is
therefore a wholesale retiling, not a perturbation of the old packet
factor.

## 3. The forced 24-owner common support

Let \(U=\{u,v\}\) and \(W=\{w,x\}\) be two disjoint reservoir pairs, and
let

\[
 Q_R=(uw,vw,vx,ux),\qquad
 \mathcal Y=\{uw,vw,vx,ux\}.                                  \tag{3.1}
\]

Define the common carrier

\[
 \mathcal V
 =\{X\cup Y:X\in\tbinom B2,\ Y\in\mathcal Y\}.                 \tag{3.2}
\]

It contains \(6\cdot4=24\) rank-four owners. A fixed outside core may be
adjoined to embed it in the ambient middle layer.

For \(c\in\{0,1,2\}\), define six physical \(C_4\)'s by

\[
 \mathcal F_c
 =\{C_c\cup Y:Y\in\mathcal Y\}
   \ \dot\cup\
   \{e\cup Q_R:e\in M_c\}.                                    \tag{3.3}
\]

Here \(C_c\cup Y\) varies the special state through
\(\mathcal A_c\) while fixing \(Y\), and \(e\cup Q_R\) fixes the special
state \(e\) while varying the two reservoir pairs.

### Theorem 3.1 (three-way exact common-owner trade)

For every \(c\), \(\mathcal F_c\) is a vertex partition of
\(\mathcal V\) into six physical \(C_4\)'s. Hence

\[
                  \mathcal F_0\longleftrightarrow
                  \mathcal F_1\longleftrightarrow
                  \mathcal F_2                                 \tag{3.4}
\]

is a literal integral three-way owner-preserving trade.

#### Proof

The first four cycles in (3.3) partition
\(\mathcal A_c\times\mathcal Y\). The last two partition
\(M_c\times\mathcal Y\). These sets are disjoint and, by (1.2), their
union is

\[
  (\mathcal A_c\mathbin\dot\cup M_c)\times\mathcal Y
       =\binom B2\times\mathcal Y=\mathcal V.
\]

Every component is an orientation square on two disjoint coordinate
pairs, hence a physical \(C_4\). \(\square\)

### Proposition 3.2 (the antipodal completion is forced)

Fix \(c\). In the axis-aligned class, suppose a \(C_4\)-factor of
\(\mathcal V\) contains the four seed fibres

\[
                         C_c\cup Y\qquad(Y\in\mathcal Y).          \tag{3.5}
\]

Then its remaining two cycles are necessarily

\[
                         e\cup Q_R\qquad(e\in M_c).                \tag{3.6}
\]

#### Proof

After removing (3.5), the uncovered support is \(M_c\times\mathcal Y\).
The two members of \(M_c\) are antipodal in \(J(4,2)\), so there is no
physical edge between their fibres. Each fibre
\(\{e\}\times\mathcal Y\) is already one four-vertex \(C_4\). A connected
four-cycle covering the remainder must therefore stay in one fibre, and
both fibres must be used. This is exactly (3.6). \(\square\)

Thus the two omitted local owners are not disposable boundary errors.
They become two entire reservoir cycles, and they change with the chosen
seed.

### Proposition 3.3 (the six-for-six trade is one owner component)

For \(c\ne d\), the bipartite ownership-overlap graph between the six
cycles of \(\mathcal F_c\) and the six cycles of \(\mathcal F_d\) is
connected.

#### Proof

The three perfect matchings \(M_0,M_1,M_2\) partition the six special
two-sets. Hence \(M_d\subseteq\mathcal A_c\) and
\(M_c\subseteq\mathcal A_d\).

Let \(L_Y\) and \(R_Y\) denote the special cycles of the two shores at
reservoir state \(Y\). Since
\(|\mathcal A_c\cap\mathcal A_d|=2\), \(L_Y\) meets \(R_Y\).
For every \(f\in M_d\), the right reservoir cycle
\(\{f\}\times\mathcal Y\) meets every \(L_Y\), because
\(f\in\mathcal A_c\). Symmetrically, every left reservoir cycle over
\(e\in M_c\) meets every \(R_Y\). Thus all eight special cycles and all
four reservoir-completion cycles on the two shores lie in one connected
overlap component. \(\square\)

Consequently exact owner preservation does not permit one to switch just
the four visible seed fibres and leave the antipodal quartets behind. The
whole six-cycle component must be retiled.

### Proposition 3.4 (the three factors partition the local edge set)

The edge sets of \(\mathcal F_0,\mathcal F_1,\mathcal F_2\) are pairwise
disjoint and together exhaust all 72 physical edges of the induced graph

\[
                         J(4,2)\mathbin\square C_4.                \tag{3.7}
\]

#### Proof

At a fixed reservoir state, an edge of \(J(4,2)\) joins two incident
two-subsets of \(B\). Those two special states lie together in exactly one
of the three orientation squares \(\mathcal A_c\). Hence the twelve
special edges are partitioned into the three four-cycles \(C_c\).

For a fixed special state \(X\), its reservoir fibre occurs in
\(\mathcal F_c\) precisely when \(X\in M_c\). The three perfect matchings
partition \(\binom B2\), so every reservoir edge occurs in exactly one
factor. Thus every special-direction and reservoir-direction edge occurs
once. The count is

\[
                 12\cdot4+6\cdot4=72
                 =3\cdot(6\cdot4).
\]

\(\square\)

## 4. Tensor common-owner resolutions and packet-wide injectivity

For \(c\in\{0,1,2\}\), orient every cycle of \(\mathcal F_c\) as in
(1.3) and (3.1). If \(f_c(Z)\) is the successor of \(Z\) in its unique
cycle, put

\[
 \ell_c(Z)=Z\cap f_c(Z),\qquad
 u_c(Z)=Z\cup f_c(Z).                                      \tag{4.1}
\]

### Lemma 4.1 (local two-sided rainbow map)

For every \(c\), both

\[
 \ell_c:\mathcal V\longrightarrow\binom{B\cup U\cup W}{3},
 \qquad
 u_c:\mathcal V\longrightarrow\binom{B\cup U\cup W}{5}       \tag{4.2}
\]

are injective.

#### Proof

On the four special seed fibres \(C_c\cup Y\), the lower traces have
special/reservoir rank profile \((1,2)\). For every fixed \(Y\), Lemma
1.1 gives the four different special singletons, so these are 16 distinct
targets.

On the two antipodal completion cycles \(e\cup Q_R\), the lower traces
have profile \((2,1)\). The two choices of \(e\in M_c\) and the four
reservoir singleton labels give eight distinct targets. The profiles
\((1,2)\) and \((2,1)\) are disjoint, proving lower injectivity.

For upper traces the two corresponding profiles are \((3,2)\) and
\((2,3)\). The four special edge unions and four reservoir edge unions
are injective in their respective squares, so the same argument proves
upper injectivity. \(\square\)

Take \(r\) disjoint copies \(\mathcal V_1,\ldots,\mathcal V_r\), and put

\[
                         \mathcal P=\mathcal V_1\times\cdots\times
                         \mathcal V_r.                         \tag{4.3}
\]

Thus \(|\mathcal P|=24^r\). For a seed vector
\(\theta=(\theta_1,\ldots,\theta_r)\in\{0,1,2\}^r\), take the Cartesian
product of the six-cell resolutions \(\mathcal F_{\theta_i}\).

### Theorem 4.2 (the \(3^r\) exact common-owner resolutions)

For every \(\theta\in\{0,1,2\}^r\),

\[
 \mathcal P
 =\mathop{\dot\bigcup}_{(j_1,\ldots,j_r)\in[6]^r}
   K^{\theta_1}_{j_1}\times\cdots\times K^{\theta_r}_{j_r},     \tag{4.4}
\]

where every cell is a physical isometric

\[
                         Q_2^r=Q_{2r}.                           \tag{4.5}
\]

Hence all \(3^r\) resolution vectors have exactly the same middle-owner
support.

#### Proof

For each \(i\), the six cells in \(\mathcal F_{\theta_i}\) are a disjoint
partition of \(\mathcal V_i\), by Theorem 3.1. Cartesian products of
these partitions are disjoint and exhaustive. The active coordinate
pairs from different 8-blocks are disjoint, so each product cell is a
literal isometric \(Q_{2r}\) in the ambient Johnson graph. \(\square\)

Assume now that

\[
                         h=2r
\]

is a power of two. In every cell of (4.4), use the recursive exact
Hamming \(C_{2h}\)-factor, placing the two directions from each local
8-block as sibling leaves and using the forward local orientations.

### Theorem 4.3 (exact whole-packet two-sided injectivity)

For every seed vector \(\theta\) and every \(1\le q\le r\), the lower and
upper consecutive depth-\(q\) maps of the resulting \(C_{2h}\)-factor
are injective on the whole common packet \(\mathcal P\).

#### Proof

The dyadic balance law of the recursive Hamming factor says that a cyclic
window of \(q\le r\) directions uses each bottom sibling pair at most
once. Thus each local 8-block is either untouched or traverses one
oriented edge of its \(\mathcal F_{\theta_i}\)-cell.

For a lower target, an untouched block has local rank four and a touched
block has rank three. Hence the target identifies the touched block set.
On an untouched block it records the starting owner literally; on a
touched block it records \(\ell_{\theta_i}(Z_i)\), which determines
\(Z_i\) uniquely by Lemma 4.1. Therefore the global starting owner is
recovered. The upper proof is identical, with local ranks four and five
and the inverse of \(u_{\theta_i}\). \(\square\)

### Corollary 4.4 (arbitrary seed density is locally legal)

Two resolution vectors may differ in any prescribed number of their
\(r\) coordinates, including \(\Omega(h/\sqrt m)\) or all \(r\)
coordinates. Both choices remain exact on the same middle-owner packet,
and both retain two-sided packet-wide injectivity through depth \(r\).

More exactly, fix the all-zero resolution as baseline and let
\(\theta\) differ from it in \(s\) local blocks. Every
\(C_{2h}\)-component of the \(\theta\)-resolution has exactly

\[
                              4s                                \tag{4.6}
\]

transition positions belonging to nonbaseline local frame factors:
each local block contributes two cube directions, each used once in each
half of the isometric cycle. Proposition 3.4 shows that all four are
genuinely new physical edges when the seed changes. Hence choosing
\[
 s=\left\lceil {c h\over4\sqrt m}\right\rceil
\tag{4.7}
\]
gives at least \(c h/\sqrt m\) genuinely nonbaseline transition
positions per component (and \(s\le r=h/2\) for large \(m\)).  Thus the
requested \(\Omega(h/\sqrt m)\) rate is realized exactly while preserving
all conclusions of Theorems 4.2--4.3.

The distinction from Corollary 2.2 is essential: Theorem 4.2 uses the
completed 24-owner local support \(\mathcal V\), not the raw four-owner
support \(\mathcal A_c\).

## 5. Pairwise phase compatibility

Any two completed factors admit one common owner colouring by
\(\mathbb Z_4\). By relabelling \(B\), it is enough to compare

\[
 M=ab\mid cd,\qquad M'=ac\mid bd.                              \tag{5.1}
\]

Orient their special cycles as

\[
 (ac,bc,bd,ad),\qquad (ab,bc,cd,ad).                            \tag{5.2}
\]

Write the reservoir cycle as \(y_0,y_1,y_2,y_3\), in cyclic order, and
put

\[
\begin{array}{c|rrrrrr}
 X&ac&bc&bd&ad&ab&cd\\ \hline
 g(X)&0&1&2&3&0&2.
\end{array}                                                     \tag{5.3}
\]

Define

\[
                         \phi(X,y_k)=g(X)+k\pmod4.                \tag{5.4}
\]

### Proposition 5.1

The restriction of \(\phi\) to every cycle of both completed factors is
a cyclic enumeration \(0,1,2,3\).

#### Proof

On the two special cycles in (5.2), the values in (5.3) are respectively

\[
                         0,1,2,3
 \quad\hbox{and}\quad 0,1,2,3.
\]

On every antipodal completion cycle, the special state \(X\) is fixed and
\(k\) increases by one, so (5.4) again increases by one. \(\square\)

The standard colour-fibre suspension therefore lifts either pair of
completed factors to common-support, phase-compatible families of six
physical \(C_{2h}\)'s for every \(h\ge2\), as in the audited pair-frame
associator theorem.

## 6. Exact obstruction to a simultaneous three-state suspension

The pairwise colourings of Section 5 cannot be made consistent for all
three factors.

### Theorem 6.1 (six-versus-four phase obstruction)

There is no map

\[
                         \phi:\mathcal V\longrightarrow\mathbb Z_4      \tag{6.1}
\]

whose restriction to every \(C_4\)-component of every one of
\(\mathcal F_0,\mathcal F_1,\mathcal F_2\) is a cyclic bijection.

#### Proof

Fix one reservoir state \(Y\in\mathcal Y\). For every \(c\), the factor
\(\mathcal F_c\) contains the special cycle
\(\mathcal A_c\times\{Y\}\). Therefore the four values of \(\phi\) on
that cycle must be pairwise distinct.

Every special state \(X\in\binom B2\) is omitted from exactly one of the
three sets \(\mathcal A_c\), namely from the seed whose antipodal matching
contains \(X\). Given two distinct special states \(X,X'\), choose a
seed index omitted by neither of them. Such an index exists among the
three, even if their omitted indices are different. Then

\[
                         X,X'\in\mathcal A_c.
\]

The preceding paragraph forces
\(\phi(X,Y)\ne\phi(X',Y)\). Hence all six special states over the fixed
reservoir state would require pairwise distinct values in
\(\mathbb Z_4\), which has only four values. Contradiction. \(\square\)

This theorem rules out the standard common-colour suspension of the three
states. It does not rule out a new suspension with a larger phase space,
nontrivial monodromy, or components which mix several 24-owner carriers.
The same proof shows more generally that any owner label which is
injective on each of the three special seed cycles needs at least six
values. Thus a putative simultaneous suspension has an exact local
phase-alphabet lower bound of six.

## 7. Consequences for the first-eligible gate

We now place the common packet \(\mathcal V^r\) into a fixed ordered
first-eligible atlas. Work first on \(2m\) coordinates and write

\[
                         W=\binom{2m}{m}.                         \tag{7.1}
\]

Partition all but \(O(1)\) coordinates into

\[
                         b=\lfloor m/4\rfloor
\]

ordered 8-blocks. Call a block eligible when its restriction belongs to
\(\mathcal V\), and select the first \(r=o(m)\) eligible blocks. Variation
inside \(\mathcal V^r\) preserves eligibility and hence gives a stable
packet partition. Assume also that \(h=2r\) is a power of two, as in
Theorem 4.3. Under independent fair bits, one block is eligible with
probability

\[
                         \frac{24}{2^8}=\frac3{32}.                \tag{7.2}
\]

Let \(R\) be the union of the last \(\lfloor b/4\rfloor\) blocks and put
\(s=|R|\). Then

\[
                         \frac{s}{2m}\longrightarrow\frac14.     \tag{7.3}
\]

Before \(R\), the expected eligible-block count is

\[
                         \left(\frac9{512}+o(1)\right)m.          \tag{7.4}
\]

Since \(r=o(m)\), Chernoff's inequality and conditioning on middle rank
show that all but

\[
                         U_m=e^{-\Omega(m)}W                     \tag{7.5}
\]

middle owners select their first \(r\) blocks before \(R\). Call their
packets normal. Every component of every seed-vector resolution of a
normal packet freezes its restriction to \(R\).

### Theorem 7.1 (seed-density-independent suffix Hall cut)

Fix \(A>0\), and let

\[
                         q=\lfloor A\sqrt m\rfloor
                         \le\min\{H,r\}.                          \tag{7.6}
\]

There is a constant \(\kappa_A>0\) such that the partial factor obtained
by choosing an arbitrary seed vector
\(\theta(P)\in\{0,1,2\}^r\) in every first-eligible common packet, and
every hypothetical exact completion which agrees with it on all normal
packets, satisfies

\[
                         M_q^-\ge\kappa_AW-o(W),\qquad
                         M_q^+\ge\kappa_AW-o(W).                  \tag{7.7}
\]

The conclusion is independent of the number of changed seed coordinates;
it includes full seed density.

In particular, for any exact depth-\(q\)-geodesic completion and any
balanced baseline \((b_T)_T\) with \(\sum_Tb_T=W\), every target has
\(b_T\ge1\).  Hence (7.7) implies \(\Omega_A(W)\) total underload for
each sign; equality of total occurrence and baseline mass gives the same
\(\Omega_A(W)\) overload.  Thus (7.7) is an integral balanced Hall cut,
not only a support statistic.

#### Proof

For an integer \(a\), put

\[
\begin{aligned}
 \mathcal Z_{q,a}^-&=
 \{T\in\tbinom{[2m]}{m-q}:|T\cap R|\le a\},\\
 \mathcal Z_{q,a}^+&=
 \{T\in\tbinom{[2m]}{m+q}:|T\cap R|\ge s-a\},\\
 B_a&=
 |\{X\in\tbinom{[2m]}m:|X\cap R|\le a\}|.
\end{aligned}                                                   \tag{7.8}
\]

On a normal component, every lower phase occurrence belongs to
\(\mathcal Z_{q,a}^-\) exactly when its middle owner has
\(|X\cap R|\le a\). Thus exact middle ownership gives total occurrence
capacity at most \(B_a\) in this target set. Give every exceptional owner
the most favorable possible behavior; it adds at most \(U_m\). Therefore

\[
 M_q^\pm\ge|\mathcal Z_{q,a}^\pm|-B_a-U_m.                       \tag{7.9}
\]

For the upper sign, use middle-layer complementation. No shadow
injectivity is needed for (7.9), since repeated occurrences can only
reduce the number of distinct targets hit.

Put

\[
 v=\frac3{32},\qquad
 d=A\sqrt{\frac23}.                                             \tag{7.10}
\]

Choose \(x_A>0\) so that

\[
                 e^{-A^2}\Phi(d-x_A)>\Phi(-x_A).                 \tag{7.11}
\]

Such a choice exists: for \(x>d\), Mills' estimate gives

\[
 \frac{\Phi(d-x)}{\Phi(-x)}
 =\frac{x}{x-d}
   \exp\!\left(xd-\frac{d^2}{2}+o(1)\right)\longrightarrow\infty.
                                                                    \tag{7.12}
\]

Take

\[
                         a=\left\lfloor\frac s2-x_A\sqrt{vm}\right\rfloor.
                                                                    \tag{7.13}
\]

The hypergeometric central limit theorem and
\(N_q/W\to e^{-A^2}\) give

\[
 \frac{B_a}{W}\longrightarrow\Phi(-x_A),\qquad
 \frac{|\mathcal Z_{q,a}^\pm|}{W}
 \longrightarrow e^{-A^2}\Phi(d-x_A).                            \tag{7.14}
\]

Indeed, the suffix count has middle mean \(s/2\), lower-layer mean
\(s/2-(A/4+o(1))\sqrt m\), and variance \((v+o(1))m\).
Define

\[
 \kappa_A=e^{-A^2}\Phi(d-x_A)-\Phi(-x_A)>0.                       \tag{7.15}
\]

Equations (7.5), (7.9), and (7.14) prove (7.7). \(\square\)

### Corollary 7.2 (what the required density must disturb)

For a more general factor, let \(T_R\) be the number of transition
positions whose two endpoints have different restrictions to \(R\).
Every depth-\(q\) window which fails to freeze \(R\) contains such a
transition, and a fixed transition lies in exactly \(q\) cyclic
depth-\(q\) windows. Hence

\[
                         M_q^\pm\ge\kappa_AW-o(W)-qT_R.           \tag{7.16}
\]

Clearing the cut therefore requires

\[
                         T_R=\Omega(W/\sqrt m).                  \tag{7.17}
\]

Since a coefficient-one factor has \(W/(2h)+o(W/h)\) cycles, this is

\[
                         \Omega(h/\sqrt m)                       \tag{7.18}
\]

**exterior-disturbing** transitions per cycle on average. Internal choices
among \(\mathcal F_0,\mathcal F_1,\mathcal F_2\), however dense, have
\(T_R=0\) on every normal packet and do not pay (7.18).

For an odd ground set, place the one extra coordinate outside all
8-blocks and split owners and targets according to it. Every packet freezes
that coordinate. In each of the two
sectors the finite-coordinate ranks differ by exactly \(q\), the suffix
ratio is still \(1/4+o(1)\), and the two hypergeometric limits in (7.14)
are unchanged. Summing the two sector cuts gives the same conclusion with
the odd middle width.

Thus packetwise exact ownership and intrapacket injectivity are proved on
all but exponentially small owner mass; exact completion of that mass is
not supplied.  Even if such a completion is granted, the aggregate Hall
clause is refuted. A viable constant-one route needs a common-owner
repacketization with genuine exterior transport, not a denser internal
seed field.

## 8. Adversarial audit

1. The equality classification uses one fixed physical four-block atlas.
   It does not compare packets built from overlapping or permuted atlases.
2. Formula (2.6) is an owner-support statement, not a shadow-collision
   estimate.
3. The local 24-owner trade is a six-\(Q_2\) resolution, not one cube.
   The interchangeable \(Q_{2r}\)-cell resolutions arise only after the
   Cartesian tensor construction of Theorem 4.2.
4. Proposition 3.2 is a uniqueness statement only in the displayed
   axis-aligned full-frame class. Absolute minimality among arbitrary
   Johnson cycles is not claimed.
5. Theorem 6.1 excludes a common \(\mathbb Z_4\) colour-fibre suspension.
   It does not contradict Theorem 4.3, which constructs a separate Hamming
   factor after one whole resolution vector has been selected.
6. The Hall cut uses one fixed ordered 8-block atlas and components
   confined to its selected blocks. Overlapping atlases, reordered block
   systems, or exterior-moving components are not ruled out.
7. No coefficient-one conclusion is claimed.
