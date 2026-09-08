# Signed ERP for the two-parity PBBS packet and the deep crossing Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad H=\lceil A\sqrt m\rceil,
 \qquad W=\binom{2m+1}{m}.
\tag{0.1}
\]

All finite erosion statements are made for \(H<m\), which holds for all
sufficiently large \(m\) at fixed \(A\).

Consider a genuine simple PBBS return of gap \(2s+1\), where
\(1\le s<m\). The packet identities hold throughout this range; whenever
they are invoked as part of ERP\(_H\), assume in addition \(s\le H\).
This note settles the sign and baseline-credit parts of
erosion replacement provenance, and gives an exact obstruction at the
first unresolved deep crossing scale.

1. The complemented two-parity packet has an exact signed circular word
   of length \(2s+3\). More strongly, it has an ordinary full-port word
   of length \(3s+2\). If \(t\) packets form \(c\) literal full-port
   trails, their exact word length is

   \[
      \boxed{t(2s+2)+cs}.                                      \tag{0.2}
   \]

   Thus its packet-interior excess over the \(2s+2\) owner occurrences
   per packet is exactly \(cs\), not a fractional credit.

2. Every one of the \(2s+2\) signed owner occurrences maps to a distinct
   nonnegative endpoint-capped erosion position in its own projected
   trajectory. For a globally owner-occurrence-disjoint packet family,
   this gives an integral injection into deleted principal baseline
   positions. The more general owner-to-erosion assignment is an interval
   bigraph, and its exact capacitated Hall inequalities are given below.

3. On an \(H\)-erosion-admissible capped exterior path, deleting one block
   \([r,r+s]\) of erosion indices disturbs more than the physical owner
   windows crossing the packet. At depth \(d\), after deleting packet-
   internal windows, the exact residual occurrence counts are

   \[
   \begin{array}{c|cc}
       &d\le s&d>s\\ \hline
    \text{lower intersections}&H&s+H-d+1\\
    \text{upper unions}&H+2d&s+H+d+1.
   \end{array}                                                   \tag{0.3}
   \]

   These include wholly exterior ghost windows. Hence a seam-crossing
   occurrence catalogue is not a complete ERP catalogue.

4. On such an admissible path, every incremental pin in one floor-correct
   all-depth flag has a unique canonical erosion carrier. The lower carriers are
   \(D_{a+q-H}\), and the upper carriers are \(D_{a+q+1}\). Therefore
   every individual flag has a saturated increasing SDR: the obstruction
   is not one-flag Hall failure. Once one of these unique cells is
   deleted, however, the pin cannot be shifted to an adjacent surviving
   canonical cell. It must be carried by a new cell, bundled with another
   flag, or supplied by a different occurrence of the same target.

5. There is an exact deep collision/Hall cut which uses actual target
   supports, not occurrence mass. Let \(d_I\) be the number of distinct
   floor-correct depth-\((s-1)\) lower targets among the \(2(s-1)\)
   windows crossing the even-out and odd-in cuts of a packet \(I\). If a
   local replacement deletes the packet's \(2s+2\) principal erosion
   positions and \(c_I\) additional collar positions, has net excess
   \(\delta_I\), and exports \(\rho_I\) of the forced certificates, then

   \[
      \boxed{
      c_I+\rho_I+\delta_I\ \ge\ d_I-s-3.}                         \tag{0.4}
   \]

   This is a sharp lower bound for the displayed target subfamily. It is
   genuinely at depth \(q=s-1\ge3\) when \(s\ge4\).

6. If both exposed shores persist as same-carrier FIFO rows, then

   \[
      d_I=2s-2,
   \]

   and (0.4) becomes

   \[
      \boxed{c_I+\rho_I+\delta_I\ge s-5.}                          \tag{0.5}
   \]

   Thus the natural two-shore common-carrier continuation has a linear
   local toll. In contrast, a single common-carrier shore admits an exact
   noncellular FIFO braid with \(O(H)\) total border charge per trail.

The remaining global escape is consequently precise. On a critical
family with \(\sum_I s_I=\Theta(W)\), one needs some combination of
actual deep-support collisions, linear collar absorption with complete
provenance, and a cross-packet pin--cap system exporting and compatibly
bundling the remaining certificates while opening only \(o(W/H)\)
critical-length physical trails. No audited \(q\ge3\) PBBS multiplicity
theorem proves the collision alternative, the old collar architecture has
linear net charge, and no construction presently proves the required
export. Thus no coefficient-one conclusion is asserted.

## 1. The signed two-parity packet

Let

\[
 \Gamma=(\gamma_0,\ldots,\gamma_{2s})
\tag{1.1}
\]

be the active cyclic order of a simple return. There are disjoint cores
\(K,K'\), each of size \(m-s\), such that the two original parity rows are
\(m\)-sets \(E_j,O_j\), \(0\le j\le s\). Put

\[
 P_j=E_j^c,\qquad Q_j=O_j^c.                                      \tag{1.2}
\]

These are the rank-\((m+1)\) rows on which the principal erosion word is
written. Direct cyclic-window complementation gives

\[
 \boxed{
 P_j=K'\cup
 \{\gamma_{j+s},\ldots,\gamma_{2s}\}
 \cup\{\gamma_0,\ldots,\gamma_{j-1}\},}                          \tag{1.3}
\]

and

\[
 \boxed{
 Q_j=K\cup\{\gamma_j,\ldots,\gamma_{j+s}\}.}                    \tag{1.4}
\]

Empty displayed intervals are omitted.

### Theorem 1.1 (exact signed target formulas)

For \(0\le p\le q\le s\),

\[
\begin{aligned}
 \bigcap_{j=p}^{q}P_j
 &=K'\cup\{\gamma_{q+s},\ldots,\gamma_{2s}\}
        \cup\{\gamma_0,\ldots,\gamma_{p-1}\},\\
 \bigcup_{j=p}^{q}P_j
 &=K'\cup\{\gamma_{p+s},\ldots,\gamma_{2s}\}
        \cup\{\gamma_0,\ldots,\gamma_{q-1}\},\\
 \bigcap_{j=p}^{q}Q_j
 &=K\cup\{\gamma_q,\ldots,\gamma_{p+s}\},\\
 \bigcup_{j=p}^{q}Q_j
 &=K\cup\{\gamma_p,\ldots,\gamma_{q+s}\}.
\end{aligned}                                                       \tag{1.5}
\]

Consequently the circular word

\[
 \boxed{
 \mathcal Z^\pm=
 (\gamma_s,\ldots,\gamma_{2s},
  K'\cup\{\gamma_{2s}\},
  \gamma_0,\ldots,\gamma_{s-1},
  K\cup\{\gamma_s\})}                                             \tag{1.6}
\]

has length \(2s+3\) and circularly represents every target in (1.5).

#### Proof

For the \(P\)-row, a coordinate in the active cycle survives every
window from \(p\) through \(q\) precisely on the two displayed terminal
arcs in the first line of (1.5); it occurs in at least one window precisely
on the larger two arcs in the second line. The \(Q\)-row is an ordinary
sliding \((s+1)\)-window, giving the last two lines. In (1.6), every
\(P\)-target is an interval through the \(K'\)-cell, and every
\(Q\)-target is the complementary circular interval through the
\(K\)-cell. All letters are nonempty because \(s<m\). \(\square\)

The complement signs are exact:

\[
 \bigcap P=(\bigcup E)^c,\qquad
 \bigcup P=(\bigcap E)^c,                                         \tag{1.7}
\]

and similarly for \(Q,O\). Thus (1.6) is not an unsigned cardinality
analogue of the old chart; it is the literal chart on the principal
complement-projected trajectories.

### Theorem 1.2 (full-port linear word)

Define

\[
\begin{aligned}
 A&=(\gamma_s,\ldots,\gamma_{2s-1}),\\
 B&=(\gamma_0,\ldots,\gamma_{s-1}),\\
 R&=(\gamma_{s+1},\ldots,\gamma_{2s}),\\
 C'&=K'\cup\{\gamma_{2s}\},\qquad
 C=K\cup\{\gamma_s\}.
\end{aligned}                                                       \tag{1.8}
\]

Then

\[
 \boxed{\mathcal J^\pm=(A,C',B,C,R)}                               \tag{1.9}
\]

has length \(3s+2\), and represents every target in (1.5) as an ordinary
nonwrapping interval. Its first \(2s+1\) cells \((A,C',B)\) serve the
\(P\)-row, and its last \(2s+1\) cells \((B,C,R)\) serve the \(Q\)-row.

Every internal lower intersection has the same left endpoint as its last
owner. Every internal upper union has the same right endpoint as its last
owner. Hence the word carries literal nested signed flags, not only an
unrooted set catalogue.

If \(t\) packets are partitioned into \(c\) directed chains satisfying
literal ordered port equality

\[
 R_I=A_J                                                        \tag{1.10}
\]

at every chain edge, their packet-interior targets have one word of exact
length

\[
 \boxed{
 t(3s+2)-s(t-c)=t(2s+2)+cs.}                                      \tag{1.11}
\]

#### Proof

The four formulas in (1.5) are respectively the intervals beginning and
ending at the evident singleton cells on the two overlapping subwords in
(1.9). For example, a \(P\)-intersection begins at
\(\gamma_{q+s}\), passes through \(C'\), and ends at
\(\gamma_{p-1}\); the endpoint conventions cover empty arms. The other
three cases are identical.

At a chain edge, identify the \(s\) terminal cells \(R_I\) with the
\(s\) initial cells \(A_J\). Every old interval remains contiguous.
There are \(t-c\) joins, proving (1.11). \(\square\)

The excess interpretation in (1.11) requires the complete \(2s+2\)
owner occurrences of distinct selected packets to be disjoint. Equality
of set values at two different occurrences does not create a second
baseline credit.

## 2. Integral owner-to-erosion provenance

Fix one signed/parity projected path

\[
 X_0,X_1,\ldots,X_{\ell-1}
\tag{2.1}
\]

and its nonnegative endpoint-capped erosion word

\[
 D_i=\bigcap_{h=0}^{H}\widetilde X_{i+h}.
\tag{2.2}
\]

For the canonical witness assertions in this section and Section 3, assume
the path is **\(H\)-erosion-admissible**: every internally bounded positive
coordinate residence has at least \(H+1\) owner states, with constant
endpoint capping, and \(H<m\). Under exactly this hypothesis, the audited
erosion identity is

\[
 X_u=\bigcup_{i=u-H}^{u}D_i,                                      \tag{2.3}
\]

with the understood capped/padding indices at a path endpoint.

Without \(H\)-erosion-admissibility, a coordinate in a positive run of at
most \(H\) owner states can occur in \(X_u\) but in no \(D_i\), so (2.3),
the witness interpretation of Theorem 2.1, and the existence part of
Theorem 3.2 can fail. A PBBS application must first cut or explicitly
replace every such short run. The special first-owner map in Corollary 2.2
remains a formal injection of *position indices*, but it earns only length
credit until this collateral replacement is certified.

Let \(O=\{u_1<\cdots<u_r\}\) be selected owner occurrences. Let
\(E\) be the bank of erosion indices actually made available for deletion,
and give \(i\in E\) integral capacity \(b_i\). Define

\[
 N(u)=E\cap[u-H,u].                                                 \tag{2.4}
\]

### Theorem 2.1 (exact owner-credit Hall theorem)

There is an integral assignment of each selected owner occurrence to a
distinct available erosion credit, respecting capacities, if and only if

\[
 \boxed{
 |S|\le
 \sum_{i\in\bigcup_{u\in S}N(u)}b_i
 \quad\text{for every }S\subseteq O.}                              \tag{2.5}
\]

Because the neighborhoods are ordered intervals, it is enough to check
consecutive blocks in the ordered owner list:

\[
 \boxed{
 k-j+1\le
 \sum_{i\in E\cap
       \bigcup_{h=j}^{k}[u_h-H,u_h]}b_i
 \quad(1\le j\le k\le r).}                                       \tag{2.6}
\]

Whenever the intervals in the block overlap consecutively, the right
side simplifies to

\[
 \sum_{i\in E\cap[u_j-H,u_k]}b_i.                                 \tag{2.7}
\]

#### Proof

Equation (2.5) is the capacitated Hall theorem. For the reduction, split
the neighborhood intervals of an arbitrary owner subset into connected
components. Capacities add over components, so a violation contains a
violating component. In one component, insert every selected owner of
\(O\) lying between its first and last owner. This increases demand and
does not enlarge the component's interval union. Thus a violating subset
produces a violating consecutive block. The converse is immediate.
\(\square\)

This theorem separates two notions which must not be conflated. An owner
occurrence is a requested signed flag root; a \(D\)-index is one paid
baseline position. Matching them earns one unit of length credit. It does
not assert \(X_u=D_i\), and it does not by itself preserve the other old
witnesses using \(D_i\).

### Corollary 2.2 (natural packet injection)

If \(u\in E\) and \(b_u\ge1\) for every selected owner, then

\[
 \pi(u)=u                                                        \tag{2.8}
\]

is an injection. In particular, map the occurrences \(P_j,Q_j\) in one
packet to the erosion positions whose first owners are those occurrences.

On an odd physical \(f\)-orbit of length \(L\), conventional indexing of
the complement-projected \(g=f^2\) trajectory gives

\[
 P_j=X_j,\qquad Q_j=X_{\kappa+j},qquad
 \kappa={L+1\over2}.                                               \tag{2.9}
\]

On an even physical orbit, the two parities lie on the two separate
\(g\)-orbits and are indexed separately. Since \(s<m\), the cores are
nonempty and disjoint, and the \(2s+2\) packet owners are distinct.
Therefore a full-packet owner-occurrence-disjoint selection maps
integrally to \(2s+2\) distinct nonnegative erosion positions. Together
with Theorems 1.1--1.2, this proves the signed packet-interior part of
ERP\(_H\).

If one tries to use only the left padding bank

\[
 E=\{-H,-H+1,\ldots,-1\}
\tag{2.10}
\]

for owners \(0,\ldots,s\), the maximum matching has size
\(\min(s+1,H)\). Its exact deficiency is

\[
 \boxed{\Delta_{\rm pad}(s,H)=(s+1-H)_+.}                          \tag{2.11}
\]

Thus padding alone works for \(s\le H-1\), while \(s=H\) has deficiency
one per parity. Adding the nonnegative cell \(D_0\) removes it. This is
only an \(O(1)\)-per-packet issue, not the Gaussian-scale obstruction.

## 3. The exact collateral halo and unique arm carriers

Let one deleted erosion block be

\[
 I=[r,r+s].                                                        \tag{3.1}
\]

For an owner window \([a,b]\), where \(d=b-a\le H\), the canonical
lower and upper witnesses are

\[
 J^-_{a,b}=[b-H,a],\qquad J^+_{a,b}=[a-H,b].                       \tag{3.2}
\]

### Proposition 3.1 (exact affected halo)

One has

\[
 J^-_{a,b}\cap I\ne\varnothing
 \iff a\ge r\ \text{ and }\ b\le r+s+H,                           \tag{3.3}
\]

and

\[
 J^+_{a,b}\cap I\ne\varnothing
 \iff b\ge r\ \text{ and }\ a\le r+s+H.                           \tag{3.4}
\]

With full collars, the total affected counts at depth \(d\) are

\[
 s+H-d+1\quad\text{and}\quad s+H+d+1                              \tag{3.5}
\]

for the lower and upper signs. Subtracting the
\(\max(s-d+1,0)\) packet-internal windows gives exactly (0.3).

#### Proof

An interval \([x,y]\) meets \([r,r+s]\) exactly when
\(x\le r+s\) and \(y\ge r\). Substitute the two intervals in (3.2),
then put \(b=a+d\) and count the integral values of \(a\). \(\square\)

The residual family is not just the owner windows crossing either packet
edge. For example, when \(d\le H-1\), the wholly right lower window

\[
 [r+s+H-d,r+s+H]                                                   \tag{3.6}
\]

has lower erosion support beginning at \(r+s\). The wholly right upper
window

\[
 [r+s+H,r+s+H+d]                                                   \tag{3.7}
\]

has upper support beginning at \(r+s\). Each loses a canonical witness
cell although neither owner window crosses the packet. These are the
ghost windows omitted by a physical-seam-only catalogue.

There is nevertheless no Hall failure inside one correct flag.

Write a floor-correct path as

\[
 X_{t+1}=X_t-\{r_t\}+\{\iota_t\}.                                 \tag{3.8}
\]

### Theorem 3.2 (unique erosion carrier of every incremental pin)

Suppose

\[
 L_q=\bigcap_{h=0}^{q}X_{a+h},qquad
 |L_q|=k-q,quad |L_{q+1}|=k-q-1.                                 \tag{3.9}
\]

Then

\[
 L_q\setminus L_{q+1}=\{r_{a+q}\}.                               \tag{3.10}
\]

Within the canonical witness

\[
 L_q=\bigcup_{i=a+q-H}^{a}D_i,                                    \tag{3.11}
\]

the loss pin occurs in exactly one erosion letter:

\[
 \boxed{r_{a+q}\in D_{a+q-H},\qquad
 r_{a+q}\notin D_i\ (a+q-H<i\le a).}                             \tag{3.12}
\]

Dually, if

\[
 U_q=\bigcup_{h=0}^{q}X_{a+h},qquad
 |U_q|=k+q,quad |U_{q+1}|=k+q+1,                                 \tag{3.13}
\]

then the new pin \(\iota_{a+q}\in U_{q+1}\setminus U_q\) has the
unique carrier

\[
 \boxed{\iota_{a+q}\in D_{a+q+1}}                                \tag{3.14}
\]

inside the canonical witness for \(U_{q+1}\).

#### Proof

Some letter in (3.11) contains \(r_{a+q}\). If \(D_i\) contains that
coordinate, its \((H+1)\)-owner window cannot cross the transition after
\(X_{a+q}\), where the coordinate is absent. Hence
\(i+H\le a+q\). Together with \(i\ge a+q-H\), this forces
\(i=a+q-H\), proving (3.12).

The inserted coordinate is absent through \(X_{a+q}\). Any erosion
window containing it and lying in the upper witness must therefore start
at or after \(a+q+1\); that is also the largest index in the witness.
This proves (3.14). \(\square\)

Thus the lower and upper provenance maps are

\[
 q\longmapsto a+q-H,qquad q\longmapsto a+q+1.                    \tag{3.15}
\]

They are strictly increasing and saturate the FIFO requests. This proves
all depths at once, including \(q\ge3\). It also proves the conservative
obstruction: after the unique cell in (3.12) or (3.14) is deleted, no
other surviving cell in the same canonical witness can carry the pin.

This is an occurrence statement. A target need not become globally
missing if another occurrence of the same set has a surviving witness.
That distinction is essential below.

## 4. The actual deep crossing collision cut

Write the active labels in the return order

\[
 (b_0,\ldots,b_{s-1},a_0,\ldots,a_s)                              \tag{4.1}
\]

and put

\[
 B=\{b_0,\ldots,b_{s-1}\},\qquad
 C_e=K'\cup\{a_s\},\qquad C_o=K\cup\{a_0\}.                     \tag{4.2}
\]

The two projected packet blocks are the FIFO rows

\[
 P_j=C_e\cup\{a_j,\ldots,a_{s-1}\}
          \cup\{b_0,\ldots,b_{j-1}\},                            \tag{4.3}
\]

and

\[
 Q_j=C_o\cup\{b_j,\ldots,b_{s-1}\}
          \cup\{a_1,\ldots,a_j\},                                \tag{4.4}
\]

for \(0\le j\le s\), with empty arms omitted. Their exposed shared-token
endpoint owners are

\[
 X_e=P_s=C_e\cup B,qquad X_o=Q_0=C_o\cup B.                     \tag{4.5}
\]

Consider the actual projected cut immediately after \(X_e\), and the
actual projected cut immediately before \(X_o\). A depth-
\(q=s-1\) window crossing either cut contains the corresponding endpoint
owner. Retain only the floor-correct windows, and let

\[
 \mathscr C_I
\tag{4.6}
\]

be the set of distinct lower target values among them. Put

\[
 d_I=|\mathscr C_I|.                                               \tag{4.7}
\]

There are at most \(2(s-1)\) occurrences, so

\[
 0\le d_I\le2s-2.                                                  \tag{4.8}
\]

Every \(T\in\mathscr C_I\) has rank \(m-s+2\), and

\[
 T\subseteq X_e\quad\text{or}\quad T\subseteq X_o.               \tag{4.9}
\]

In particular

\[
 a_i\notin T\qquad(1\le i\le s-1).                              \tag{4.10}
\]

The packet also contains the internal targets

\[
 \boxed{
 R_i=\bigcap_{j=i}^{s}Q_j
 =K\cup\{a_0,\ldots,a_i\},qquad1\le i\le s-1.}                 \tag{4.11}
\]

### Theorem 4.1 (sharp deep collision/Hall obstruction)

Every nonzero literal word representing all targets in

\[
 \mathscr C_I\cup\{R_1,\ldots,R_{s-1}\}                          \tag{4.12}
\]

has length at least

\[
 \boxed{d_I+s-1.}                                                  \tag{4.13}
\]

The bound is sharp for this displayed target subfamily.

Consequently, suppose a local replacement segment deletes the packet's
\(2s+2\) principal erosion positions and \(c_I\) additional collar
positions. Let \(\rho_I\) be the number of the forced positions in the
proof below whose chosen witnesses lie outside the segment, and let
\(\delta_I\) be its net excess. Then

\[
 \boxed{
 \delta_I\ge d_I-s-3-c_I-\rho_I,}                                 \tag{4.14}
\]

equivalently (0.4).

#### Proof

Choose one witness interval for each distinct target
\(T\in\mathscr C_I\). Two distinct equal-rank targets cannot have the
same left endpoint: ORs of intervals with one fixed left endpoint are
nested as the right endpoint moves, while distinct equal-cardinality sets
are incomparable. Thus these targets force \(d_I\) distinct word
positions.

For each \(1\le i\le s-1\), choose in a witness for \(R_i\) one
position whose letter contains \(a_i\). Such a position exists because
the interval OR is \(R_i\). These \(s-1\) positions are pairwise
distinct. Indeed, if \(i<j\) and one position served both choices, its
letter would contain \(a_j\), but every letter in the \(R_i\)-witness is
a subset of \(R_i\), which excludes \(a_j\).

None of these \(a_i\)-bearing positions is one of the \(d_I\) crossing-
target left endpoints. Every letter in a witness for a target
\(T\in\mathscr C_I\) is a subset of \(T\), and (4.10) says that such a
letter contains no \(a_i\). This proves (4.13).

Conversely, list the \(d_I+s-1\) distinct sets in (4.12) as singleton
letters. This covers the displayed subfamily and proves sharpness. If
\(\rho_I\) forced positions are exported, at least
\(d_I+s-1-\rho_I\) positions remain inside the segment. Subtract
\(2s+2+c_I\) deleted baseline positions to obtain (4.14). \(\square\)

This is the promised Hall cut. Its requests are the \(d_I\) distinct
equal-rank witness starts and the \(s-1\) private incremental-pin cells.
Their neighborhoods are disjoint by (4.10). The full request set has
deficiency \(d_I-s-3\) against the packet's \(2s+2\) paid cells.

It is also support-correct. The parameter \(d_I\) counts distinct target
values after collisions, not rooted occurrences. The theorem therefore
does not infer a support defect from the raw number \(2(s-1)\).

### Corollary 4.2 (persistent-carrier two-shore no-go)

Suppose the even outgoing shore continues as a same-\(C_e\) FIFO block
through the token tuple \(B\), and the odd incoming shore is preceded by
a same-\(C_o\) FIFO block through \(B\). Then the even crossing targets
are

\[
 U_i=C_e\cup\{b_i\},\qquad1\le i\le s-1,                          \tag{4.15}
\]

and the odd crossing targets are

\[
 V_i=C_o\cup\{b_i\},\qquad0\le i\le s-2.                          \tag{4.16}
\]

They are \(2s-2\) pairwise distinct floor-correct rank-
\((m-s+2)\) targets. Hence

\[
 d_I=2s-2                                                        \tag{4.17}
\]

and every local replacement satisfies

\[
 \boxed{c_I+\rho_I+\delta_I\ge s-5.}                              \tag{4.18}
\]

#### Proof

In a common-carrier FIFO row, owners are the carrier together with
length-\(s\) token windows. The intersection of \(s\) consecutive owners
is the carrier plus the unique token common to those windows. The
\(s-1\) windows crossing the outgoing cut of the first block give
\(b_1,\ldots,b_{s-1}\); those crossing the incoming cut of the second
give \(b_0,\ldots,b_{s-2}\). This proves (4.15)--(4.16).

The targets are distinct within each family because the \(b_i\)'s are
distinct. Across the two families they are distinct because the carriers
\(C_e,C_o\) are disjoint and have size \(m-s+1\ge2\). Now apply
Theorem 4.1. \(\square\)

For \(s\ge4\), the scale in this theorem is genuinely \(q=s-1\ge3\).
The numerical lower bound becomes positive without collar/export credit
at \(s\ge6\), and is asymptotically linear.

### 4.1 The carrier-change fork

The fixed packet circle also has an exact limitation when the exterior
does not preserve the carrier. At the even shore, let \(v_x\) be the
capped right residence endpoint of \(x\in K'\). For a lower crossing
query whose left endpoint lies in the packet-side range where every
coordinate of \(K'\) is present, and whose right endpoint is owner
index \(b\), one has

\[
 T\cap K'=\{x\in K':v_x\ge b\}.                                  \tag{4.19}
\]

If this is a nonempty proper subset of \(K'\), the fixed packet word
\(\mathcal Z^\pm\) cannot represent \(T\): its only \(K'\)-bearing
cell contains all of \(K'\), while every other cell avoids \(K'\). Thus
every core-splitting crossing target must use an exterior/helper cell.
The \(K\)-shore is identical.

If the queried core does not split and persists through the whole range,
the fixed-core obstruction disappears; with the additional FIFO-order
hypothesis, one is in the common-carrier regime on that shore. The
following two local implications are therefore exact:

\[
 \boxed{
 \begin{array}{l}
 \text{a proper nonempty core split forces export from the fixed packet
 chart;}\\
 \text{persistent FIFO cores permit one-shore fusion, but two such shores
 obey (4.18).}
 \end{array}}                                                     \tag{4.20}
\]

This is not an exhaustive dichotomy. In particular, wholesale loss
\(T\cap K'=\varnothing\), a nonsplit but non-FIFO active order, and mixed
behavior on the opposite shore require separate analysis. Nor is it a
claim that every actual PBBS boundary has a core split at depth three.
Equation (4.20) identifies the first failure in the two stated local
architectures only.

## 5. A positive one-shore noncellular braid

The obstruction above is specifically two-shore. There is a complete
positive theorem for one persistent carrier.

Let \(C\ne\varnothing\), and let

\[
 P_h=(p_{h,0},\ldots,p_{h,s-1}),\qquad0\le h\le t,               \tag{5.0a}
\]

be ordered tuples such that each tuple has distinct coordinates,
\(C\cap P_h=\varnothing\), and adjacent tuples are disjoint:

\[
 P_{h-1}\cap P_h=\varnothing\qquad(1\le h\le t).                \tag{5.0b}
\]

Nonadjacent tuples may reuse coordinates. Concatenate the tuples into one
token line. The consecutive length-\(s\) token windows give

\[
 v=ts+1                                                        \tag{5.1}
\]

owners in \(t\) FIFO blocks. Use the common-carrier word consisting of
the \((t+1)s\) token cells enriched by \(C\), followed by one cell \(C\).
Its length is

\[
 (t+1)s+1=v+s.                                                    \tag{5.2}
\]

### Theorem 5.1 (one-shore FIFO ERP)

The word in (5.2) represents every consecutive intersection and union of
the \(v\) owners, at every available depth. Every endpoint-capped erosion
letter on the row is nonempty because it contains \(C\). Hence all \(v\)
principal erosion positions may be replaced by this word with exact
internal excess \(s\).

Only the two outer borders of the whole chain remain. Using the audited
one-border erosion chart, including endpoint initialization, costs at most
\(5H-1\) cells per border. Thus one chain has total net excess at most

\[
 \boxed{s+2(5H-1).}                                                \tag{5.3}
\]

For \(c\) pairwise owner-disjoint chains with \(s\le H\), the total is at
most \((11H-2)c\). In particular it is \(o(W)\) whenever

\[
 Hc=o(W).                                                         \tag{5.4}
\]

#### Proof

A token occurrence is present in a consecutive interval of owner times.
The union of consecutive owner windows is the corresponding token span;
their intersection is their common token overlap, or just \(C\) when the
overlap is empty. By (5.0b), equal labels in nonadjacent tuples occur at
token positions separated by at least \(s+1\). Their positive owner runs
therefore have a missing owner time between them, so they cannot hand off
across a connected query interval and create a spurious intersection.
Enriching every token cell by \(C\), and appending the one terminal
\(C\)-cell, realizes all these targets. This proves (5.2).

Every old erosion-range witness whose owner window lies wholly inside the
chain is one of these intersections or unions. The only unverified old
witnesses meet an outer border, and the established border chart restores
them with the stated charge. \(\square\)

Theorem 5.1 proves a genuine noncellular braid: the excess is independent
of the number of blocks inside one trail. It does not join the disjoint
carriers \(C_e,C_o\) inside a two-parity packet; Corollary 4.2 is exactly
the obstruction to that promotion.

## 6. The exact global Hall boundary

For a deleted bank, distinguish the occurrence halo from actual support
loss. At signed depth \(q\), define

\[
 \mathcal D_q^\pm=
 \{T:\text{every old literal witness of }T
       \text{ uses a deleted erosion index}\}.                    \tag{6.1}
\]

Only \(\mathcal D_q^\pm\) is a compulsory global repair family. The
larger family obtained by asking only that every *canonical certified*
witness be hit is a conservative provenance ledger, not necessarily an
actual hole family, because accidental old witnesses may exist. A cut
belongs to \(q\) rooted depth-\(q\) windows, but several such windows may
have the same target, or the target may have an untouched occurrence.
Therefore raw quantities such as \(qJ\) and \(H(H+1)J\) cannot be used as
support-level Hall numerators without a multiplicity or alternative-
occurrence theorem.

For a fixed proposed carrier word, use candidate left endpoints for lower
targets and candidate right endpoints for upper targets. Join
\(T\in\mathcal D_q^\pm\) to an endpoint \(p\) exactly when a legal capped
interval with that signed endpoint has OR \(T\). The exact endpoint Hall
defect is

\[
 \boxed{
 \Delta_q^\pm=
 \max_{\mathcal A\subseteq\mathcal D_q^\pm}
 (|\mathcal A|-|N(\mathcal A)|)_+.}                               \tag{6.2}
\]

For this fixed endpoint graph, \(\Delta_q^\pm\) is exactly the number of
unmatched target requests. An extension which only adds new endpoint
vertices without changing the old endpoint neighborhoods needs at least
\(\Delta_q^\pm\) such vertices. An interior insertion can change many old
interval ORs, so an arbitrary redesigned word must have its endpoint graph
recomputed; (6.2) is not an invariant lower bound under such a redesign.
For a fixed final carrier, vanishing of (6.2) is sufficient to assign
distinct endpoints at that depth. Simultaneous depths require the assigned
targets at one endpoint to form a nested flag.

The flag-level form is also exact when the carrier cells are fixed. A
request is

\[
 d=(f,j,p_d,U_d,J_d),                                             \tag{6.3}
\]

where \(f\) is a flag, \(j\) its FIFO order, \(p_d\) its required pin,
\(U_d\) its target cap, and \(J_d\) its permitted carrier range. For
fixed carrier cells \(C_z\), put

\[
 N(d)=\{z\in J_d:p_d\in C_z\subseteq U_d\}.                       \tag{6.4}
\]

If these neighborhoods are monotone intervals for one flag, an increasing
embedding exists if and only if every consecutive request block obeys

\[
 \boxed{
 b-a+1\le
 \left|\bigcup_{j=a}^{b}N(f,j)\right|.}                            \tag{6.5}
\]

This is Hall plus the standard uncrossing for a monotone interval graph.
Equations (3.12)--(3.15) show that the undeleted erosion carrier satisfies
(6.5) with equality for every individual PBBS flag.

When carrier letters are themselves to be designed, ordinary Hall is no
longer sufficient. A collection \(B\) of requests can share one new cell
exactly when

\[
 \boxed{
 \begin{gathered}
 B\text{ contains at most one request from each flag},\\
 \{p_d:d\in B\}\subseteq\bigcap_{d\in B}U_d,
 \end{gathered}}                                                   \tag{6.6}
\]

together with a common permitted placement and the FIFO order. The union
of the pins is then a legal cell. Selecting such compatible bundles is an
integral hypergraph partition problem, not a bipartite matching problem.
Thus a generic invocation of Hall after allowing cross-flag cell sharing
would be false.

Finally, after the compatible fragments are selected, make each fragment
a directed edge from its literal input port to its literal output port.
In a weak component \(C\) containing at least one edge, the minimum number
of directed trails covering every edge is

\[
 \boxed{
 \tau(C)=\max\left\{1,
       \sum_{v\in C}(d^+(v)-d^-(v))_+\right\}.}                   \tag{6.7}
\]

Indeed, the degree imbalance is necessary; adding that many dummy arcs
balances the component, and deleting them from an Euler circuit proves
sufficiency. Writing \(\operatorname{wcc}_E(G)\) for the weak components
containing at least one edge, one has

\[
 \tau(G)=\sum_{C\in\operatorname{wcc}_E(G)}\tau(C),              \tag{6.8}
\]

If every opening in component \(C\) has the same port toll \(h_C\), the
exact scalar opening requirement is

\[
 \boxed{
 \sum_{C\in\operatorname{wcc}_E(G)}h_C\tau(C)=o(W).}             \tag{6.9}
\]

For nonuniform tolls, replacing \(h_C\) by their maximum is sufficient
but need not be sharp. The convenient condition \(H\tau(G)=o(W)\) is
sufficient when every port has length at most \(H\), and is equivalent up
to constants in the critical regime where every opening toll is
\(\Theta(H)\). It is not necessary for a library containing many much
shorter ports.

Equations (4.14), (6.2), (6.5), (6.6), and (6.9) are the exact remaining
interfaces. The new quantitative content is (4.14): for an actual packet
with \(\delta_I=o(s)\),

\[
 \boxed{d_I\le s+3+c_I+\rho_I+o(s).}                              \tag{6.10}
\]

Thus either \(d_I\le s+3+o(s)\), or collar absorption plus certificate
export has total size \(\Omega(s)\). In the persistent-carrier model,
\(d_I=2s-2\), so

\[
 c_I+\rho_I\ge s-5-o(s).                                         \tag{6.11}
\]

## 7. Precise implication boundary

The following is proved under the stated packet, floor-correctness,
owner-disjointness, and—where erosion identities are invoked—the explicit
\(H\)-erosion-admissibility hypotheses.

* The signed/complemented packet chart and its exact full-port ledger.
* An integral owner-occurrence-to-erosion assignment, including the exact
  interval Hall theorem and the natural first-owner injection.
* The exact asymmetric erosion halo, including the exterior ghost windows.
* Unique all-depth provenance for every lower loss pin and upper insertion
  pin.
* The support-level deep collision cut
  \(c_I+\rho_I+\delta_I\ge d_I-s-3\).
* The linear two-shore obstruction
  \(c_I+\rho_I+\delta_I\ge s-5\) under persistent-carrier FIFO
  continuation.
* A positive one-shore FIFO ERP braid with \(O(H)\) charge per physical
  trail.

What is not proved is exactly the following PBBS support theorem:

\[
 \boxed{
 \begin{array}{l}
 \text{For a critical owner-disjoint packet family, combine actual}\\
 \text{deep-support collisions with provenance-safe collar absorption and}\\
 \text{pin--cap-compatible cross-packet bundling so that the residual}\\
 \text{request mass is }o(W)\text{ and the opening charge satisfies (6.9).}
 \end{array}}                                                     \tag{7.1}
\]

The signed owner-credit and packet-interior provenance subgate is therefore
closed positively. Full ERP\(_H\) is not. The old local two-parity/common-
carrier attempt is closed negatively at depth \(q=s-1\). The surviving
route is genuinely noncellular and genuinely support-sensitive;
occurrence counts alone neither prove nor refute it.
