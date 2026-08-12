# Seam-crossing range maxima: the exact minimal two-port gadget

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web search is used.

## 0. Outcome

This note attacks the direct-OR escape left after the same-phase
Pascal/Gray rotating-frame packet was closed by the phase-residence cut.
It gives an exact minimal two-port range-maximum theorem.

Let \(Z_1,\ldots,Z_t\) be distinct targets of one common grade in a
finite product of chains. A pure edge-seam gadget has \(t\) nonzero
letters on each side of one seam, and every \(Z_j\) is the maximum of a
window which genuinely crosses that seam. Such a gadget exists if and
only if the packet has an ordering for which every coordinate profile is
valley-quasiconvex:

\[
 Z_j(x)\le \max\{Z_i(x),Z_k(x)\}
 \qquad(i<j<k).
\tag{0.1}
\]

In the Boolean case this is exactly

\[
\boxed{\{j:x\notin Z_j\}\text{ is an interval for every coordinate }x.}
\tag{0.2}
\]

If the common meet

\[
K=\bigwedge_{j=1}^t Z_j
\]

is nonzero, the canonical word has length exactly

\[
\boxed{2t,}
\tag{0.3}
\]

and this is minimal under the edge-seam convention. Identifying the two
seam-adjacent copies of \(K\) gives the vertex-seam convention of length
\(2t-1\). These conventions are different and must not be conflated.

The theorem is constructive: put

\[
A_j(x)=\min_{k\ge j}Z_k(x),\qquad
B_j(x)=\min_{k\le j}Z_k(x).
\tag{0.4}
\]

Then \(A_j\) increases, \(B_j\) decreases, (0.1) is equivalent to

\[
Z_j=A_j\vee B_j,
\tag{0.5}
\]

and the literal word

\[
A_t,A_{t-1},\ldots,A_1,\quad
B_t,B_{t-1},\ldots,B_1
\tag{0.6}
\]

realizes \(Z_j\) by the unique anti-diagonal crossing window with \(j\)
left letters and \(t-j+1\) right letters.

This is the positive theorem. It also exposes the sharp obstruction.
Abstract rainbowness means only that the \(Z_j\)'s are distinct; it does
not imply (0.1). A Boolean coordinate with packet pattern

\[
0,1,0
\tag{0.7}
\]

already forbids the minimal seam.

More strongly, rainbow plus literal tower legality does not imply any
\(t+O(1)\) direct-OR packet. There are fully literal critical packets with

\[
t=\Theta(H),\qquad q=H,
\]

complete signed chains from rank \(m-H\) through rank \(m+H\), and common
old/switched terminal states, for which every literal word, allowing
arbitrary internal and seam-crossing witnesses, has length at least

\[
\boxed{\Omega(t(H+q))=\Omega(H^2).}
\tag{0.8}
\]

The construction is explicit and the lower bound is certified by mutually
incompatible coordinate pins. Its only scope caveat is that the prescribed
literal packet has not been embedded as selected rows of one exact source
factor.

Thus the exact surviving constant-one statement is narrower:

> Order and group the actual factor-conditioned diffuse packets so that
> their target profiles satisfy (0.1) simultaneously in the required
> modes and depths, their forced arm words are already-paid suffixes and
> prefixes of neighboring critical blocks, and their last-occurrence
> partitions match one common entrance/exit pair.

The \(2t\) arm span may not be inserted afresh at
\(\Theta(W/H)\) critical seams; that would cost \(\Theta(W)\). It must be
reused. No such global arm-matching theorem is proved here, and no
coefficient-one conclusion is claimed.

## 1. Range-maximum and port conventions

Let

\[
\mathcal Q=\prod_{x\in\Omega}\{0,1,\ldots,c_x\}
\]

with coordinatewise maximum \(\vee\). A nonzero word

\[
W=(w_1,\ldots,w_N)
\]

realizes \(Z\in\mathcal Q\) when

\[
Z=\bigvee_{r=a}^b w_r
\tag{1.1}
\]

for some nonempty interval \([a,b]\).

Fix a seam between a left arm

\[
\lambda_t,\ldots,\lambda_2,\lambda_1
\]

and a right arm

\[
\rho_1,\rho_2,\ldots,\rho_t,
\]

where \(\lambda_1,\rho_1\) are seam-adjacent. Define

\[
L_j=\bigvee_{d=1}^j\lambda_d,\qquad
R_s=\bigvee_{d=1}^s\rho_d.
\tag{1.2}
\]

The anti-diagonal crossing windows are

\[
M_j=L_j\vee R_{t-j+1},
\qquad 1\le j\le t.
\tag{1.3}
\]

Every \(M_j\) uses \(t+1\) physical letters and genuinely crosses the
edge seam.

The edge-seam length is \(2t\). If one common nonzero mask is physically
identified as the last left and first right letter, the vertex-seam length
is \(2t-1\). If one permits an extreme target not to cross the seam, the
span can fall again. All lower bounds below state the convention they use.

## 2. Exact edge-seam theorem

### Theorem 2.1 (quasiconvex packet criterion)

Let \(Z_1,\ldots,Z_t\) be distinct targets of equal grade. The following
are equivalent.

1. There is a nonzero \(2t\)-letter edge-seam word for which
   \(M_j=Z_j\) in (1.3).
2. For every coordinate \(x\) and every \(i<j<k\),
   \[
   Z_j(x)\le\max\{Z_i(x),Z_k(x)\},
   \tag{2.1}
   \]
   and \(K=\bigwedge_jZ_j\ne0\).
3. For every coordinate \(x\) and every scalar level \(a\), the strict
   sublevel set
   \[
   \{j:Z_j(x)<a\}
   \tag{2.2}
   \]
   is an interval, possibly empty or all of \([t]\), and \(K\ne0\).

When these conditions hold, (0.4)--(0.6) give an explicit gadget.

#### Proof

Suppose a seam word exists. For fixed \(x\), put

\[
\alpha_j=L_j(x),\qquad \beta_j=R_{t-j+1}(x).
\]

The sequence \(\alpha_j\) is nondecreasing and \(\beta_j\) is
nonincreasing. Moreover

\[
Z_j(x)=\max\{\alpha_j,\beta_j\}.
\tag{2.3}
\]

For every level \(a\), the set where \(\alpha_j<a\) is a prefix and the
set where \(\beta_j<a\) is a suffix. Their intersection, which is exactly
(2.2), is an interval. This proves (3), and the interval-sublevel
criterion is equivalent to (2.1).

Every crossing window contains both nonzero seam-adjacent letters
\(\lambda_1,\rho_1\). Their join lies below every \(Z_j\), so
\(K\ne0\).

Conversely, assume (2.1). Define \(A_j,B_j\) by (0.4). They satisfy

\[
A_1\le A_2\le\cdots\le A_t,\qquad
B_1\ge B_2\ge\cdots\ge B_t.
\tag{2.4}
\]

For every coordinate,

\[
\max\{A_j(x),B_j(x)\}
=\max\left\{
\min_{k\ge j}Z_k(x),
\min_{k\le j}Z_k(x)
\right\}.
\]

The right side is at most \(Z_j(x)\). If it were strictly smaller, there
would be indices \(i<j<k\) with both \(Z_i(x)\) and \(Z_k(x)\) below
\(Z_j(x)\), contradicting (2.1). Hence (0.5) holds.

Use the word (0.6), with the first displayed list ordered far-to-near and
the second near-to-far. The join of the \(j\) left letters nearest the
seam is \(A_j\), and the join of the \(t-j+1\) right letters nearest the
seam is \(B_j\). Their crossing window therefore has maximum \(Z_j\).
Every \(A_j,B_j\) contains \(K\ne0\), so all word letters are nonzero.
\(\square\)

### Theorem 2.2 (sharp length)

Every edge-seam word realizing \(t\) distinct equal-grade targets by
genuine crossing windows has at least \(t\) left-arm positions and at
least \(t\) right-arm positions. Hence its span is at least \(2t\).

#### Proof

Two chosen witnesses cannot have the same left endpoint. If they did,
the shorter would be contained in the longer, so their maxima would be
comparable. Distinct equal-grade targets in a product of chains are
incomparable. The same argument applies to right endpoints.

Every crossing witness has one endpoint on each side of the seam. Thus
there are at least \(t\) physical positions on each side. The construction
of Theorem 2.1 attains the bound. \(\square\)

### Boolean specialization

For Boolean targets, (2.1) forbids exactly the coordinate pattern
\(0,1,0\). Thus it is equivalent to (0.2).

There is also a frontier-only description. Put

\[
K=\bigcap_jZ_j.
\]

For \(1\le j<t\), the coordinates gained in passing from \(Z_j\) to
\(Z_{j+1}\) enter a new left layer, and the coordinates lost enter a new
right layer:

\[
\lambda_{j+1}=Z_{j+1}\setminus Z_j,\qquad
\rho_{t-j+1}=Z_j\setminus Z_{j+1}.
\tag{2.5}
\]

Place \(K\) in both seam-adjacent letters. If a coordinate disappears and
later reappears, the interval-zero condition places it once on each arm.
This is the Boolean expansion of (0.4)--(0.6).

The condition is order-sensitive. Finding the order is exactly a
consecutive-zeros ordering problem for the coordinate-by-target incidence
matrix. Ordinary rainbowness supplies no such order.

## 3. General internal/crossing characterization

The edge-seam theorem is the sharp zero-slack case. The next theorem
characterizes arbitrary two-port words with internal and crossing
witnesses.

Let a fixed extended line of positions be partitioned into:

- fixed left/right port positions \(F\), carrying prescribed nonzero masks
  \(E_v\);
- internal positions \(V\), whose masks are to be chosen.

For every target \(T\) prescribe one interval \(I_T\) in the extended
line, required to meet \(V\). Put

\[
E(T)=\bigvee_{v\in I_T\cap F}E_v.
\tag{3.1}
\]

### Theorem 3.1 (Boolean ported Safe-Pin criterion)

There are nonzero internal masks \(G_v\), \(v\in V\), satisfying

\[
T=E(T)\vee\bigvee_{v\in I_T\cap V}G_v
\tag{3.2}
\]

for every target \(T\) if and only if there are bits

\[
a_{v,x}\in\{0,1\}\qquad(v\in V,\ x\in\Omega)
\]

with the following properties.

1. \(E(T)\le T\) for every \(T\).
2. If \(v\in I_T\) and \(x\notin T\), then \(a_{v,x}=0\).
3. If \(x\in T\) is not already supplied by \(E(T)\), then
   \[
   \sum_{v\in I_T\cap V}a_{v,x}\ge1.
   \tag{3.3}
   \]
4. Every internal site is nonempty:
   \[
   \sum_x a_{v,x}\ge1.
   \tag{3.4}
   \]

For a general product of chains, the identical statement holds after
replacing membership bits by coordinate levels and replacing (3.3) by the
corresponding maximum-level condition.

#### Proof

Given a word, take \(a_{v,x}=1\) exactly when the Boolean coordinate
\(x\) belongs to \(G_v\). A target which omits \(x\) cannot have a
witness interval containing a letter with \(x\), proving necessity.
Every included coordinate must occur in a fixed or internal witness
letter, and every word letter is nonzero.

Conversely set

\[
G_v=\{x:a_{v,x}=1\}.
\]

Conditions 1--2 prevent every extraneous coordinate, condition 3 supplies
every required coordinate, and condition 4 makes the word literal and
nonzero. Thus (3.2) holds exactly. \(\square\)

This is an iff statement after the witness intervals are chosen. The
minimal internal length of a two-port gadget is therefore the least
\(|V|\) over:

1. an interval assignment \(T\mapsto I_T\);
2. bits satisfying Theorem 3.1; and
3. the desired common-state constraints below.

There is no abstract graph-coverage shortcut around these three items.

### Four possible witness types

For a concatenation

\[
L\mid G\mid R,
\]

every interval meeting \(G\) is exactly one of:

\[
\begin{array}{ll}
G[i,j],&
\text{internal},\\[2mm]
P_a\vee G[1,j],&
\text{left-crossing},\\[2mm]
G[i,|G|]\vee Q_b,&
\text{right-crossing},\\[2mm]
P_a\vee G[1,|G|]\vee Q_b,&
\text{crossing both ports},
\end{array}
\tag{3.5}
\]

where \(P_a\) is a suffix maximum of \(L\), \(Q_b\) is a prefix maximum
of \(R\), and \(G[i,j]\) is an internal interval maximum. A proposed
gadget is literal only after every advertised target is exhibited in one
of these four forms.

### Common ordered-partition states

Range-maximum port compatibility and MTF state compatibility are different.
If the entrance state is

\[
\Sigma=(C_1,\ldots,C_s)
\]

and the internal update word is \(G_1,\ldots,G_\ell\), its exact terminal
last-occurrence partition is

\[
\begin{aligned}
\operatorname {Last}_\Sigma(G)
=\big(&G_\ell,\,
G_{\ell-1}\setminus G_\ell,\,
\ldots,\,
G_1\setminus\!\bigcup_{k=2}^{\ell}G_k,\\
&C_1\setminus\!\bigcup_{k=1}^{\ell}G_k,\,
\ldots,\,
C_s\setminus\!\bigcup_{k=1}^{\ell}G_k\big),
\end{aligned}
\tag{3.6}
\]

after deleting empty blocks.

Thus two mode words \(G^0,G^1\) have common entrance and exit states
\(\Sigma,\Omega\) exactly when

\[
\operatorname {Last}_\Sigma(G^0)
=\operatorname {Last}_\Sigma(G^1)
=\Omega.
\tag{3.7}
\]

Equations (3.2)--(3.7) are a complete finite characterization of a
literal two-mode two-port gadget. Equality of unordered port target sets
does not imply (3.7).

Appending the full ground set makes (3.7) true in one letter, but every
window crossing that reset has maximum equal to the full ground set.
Therefore the full reset is a common terminal state, not a serviceable
proper-target port.

## 4. Nested tower geometry

For an actual radius-\(H\), depth-\(q\) occurrence, the complete signed
tower contains

\[
D=H+q
\tag{4.1}
\]

strict rank increments from its deepest lower target through its
depth-\(q\) upper target.

Suppose \(r\) distinct equal-rank outer targets \(U_i\) have selected
nested interval charts

\[
I_{i,0}\subsetneq I_{i,1}\subsetneq\cdots
\subsetneq I_{i,D}=J_i,
\tag{4.2}
\]

and the maximum on \(J_i\) is \(U_i\). Let the ambient extended word have
\(N\) positions.

### Theorem 4.1 (sliding-ladder lower bound and rigidity)

One has

\[
\boxed{N\ge r+D.}
\tag{4.3}
\]

If equality holds, after ordering by left endpoint,

\[
\boxed{J_i=[i,i+D]\qquad(1\le i\le r),}
\tag{4.4}
\]

every \(I_{i,0}\) is a singleton, and every tower step adds exactly one
left or right endpoint.

#### Proof

The \(J_i\)'s form an interval-containment antichain. Indeed, containment
of witness intervals implies containment of their maxima, and distinct
equal-rank targets are incomparable.

Order the intervals by increasing left endpoint. Their right endpoints
are then also strictly increasing. Hence the \(i\)-th left endpoint is at
least \(i\). The \(D\) strict interval extensions in (4.2) give

\[
|J_i|\ge D+1,
\]

so its right endpoint is at least \(i+D\). There must remain \(r-i\)
larger right endpoints within \([N]\), giving

\[
i+D\le N-r+i.
\]

This proves (4.3).

At equality, every inequality used above is equality. Thus the left
endpoints are \(i\), the right endpoints are \(i+D\), the outer intervals
have length \(D+1\), the initial interval has length one, and every strict
extension adds one endpoint. \(\square\)

The equality case is not an informal packet: it is the rigid moving-OR
system

\[
U_i=\bigvee_{j=i}^{i+D}w_j
\tag{4.5}
\]

with all central and intermediate flag pins imposed on its subwindows.

### Corollary 4.2 (overlap degree)

Let

\[
\Delta=\max_{x\in\Omega}\#\{i:x\le U_i\}.
\tag{4.6}
\]

Then

\[
\boxed{N\Delta\ge r(D+1).}
\tag{4.7}
\]

If

\[
d=N-r-D,
\]

then

\[
\boxed{\Delta\ge\left[\min\{r,D+1-d\}\right]_+.}
\tag{4.8}
\]

#### Proof

The total position--outer-interval incidence is at least \(r(D+1)\).
At a fixed physical position choose one coordinate appearing in its
nonzero letter. Every selected outer interval containing that position
has a target containing the chosen coordinate, so the position belongs to
at most \(\Delta\) outer intervals. This proves (4.7).

For (4.8), the endpoint argument in Theorem 4.1 gives

\[
\ell_i\le i+d,\qquad r_i\ge i+D.
\]

The physical position \(D+1\) therefore belongs to the first
\(\min\{r,D+1-d\}\) outer intervals. Any coordinate in its nonzero letter
belongs to all their targets. \(\square\)

Thus a critical \(N=r+D+O(1)\) ladder requires a coordinate shared by
\(\Theta(D)\) packet targets. Rainbowness at one depth gives no such
high-degree overlap.

## 5. A sharp literal counterpacket

The preceding lower bound assumed nested witness charts. The next
pin certificate gives a stronger obstruction which permits arbitrary
unrelated witnesses in the competing word.

### Lemma 5.1 (incompatible pin requests)

For a required target \(T\) and coordinate \(x\in T\), call \((T,x)\)
a pin request. Two requests \((T,x)\), \((T',x')\) are incompatible when

\[
x\notin T'\quad\text{or}\quad x'\notin T.
\tag{5.1}
\]

If a collection of pin requests is pairwise incompatible, every literal
word realizing all their targets has at least as many physical positions
as requests.

#### Proof

Choose a witness interval for every target. A request \((T,x)\) has some
position in its witness whose letter contains \(x\). If one position
served two requests, its letter would contain both \(x,x'\), and both
witness targets would contain both coordinates. This contradicts (5.1).
\(\square\)

The same argument says that the length is at least the chromatic number of
the incompatibility graph of any chosen pin-request family.

### Proposition 5.2 (harmonic pin-degree bound)

For occurrence \(i\), choose one fresh coordinate
\(\xi_{i,p}\in T_{i,p}\setminus T_{i,p-1}\) at every step
\(0\le p\le D\), with the natural interpretation at \(p=0\). Let
\(U_j=T_{j,D}\) be occurrence \(j\)'s outer target and put

\[
d_{i,p}=\#\{j:\xi_{i,p}\in U_j\}.
\tag{5.2}
\]

Every literal word realizing the complete packet satisfies

\[
\boxed{
N\ge\sum_{i=1}^r\sum_{p=0}^{D}\frac1{d_{i,p}}.}
\tag{5.3}
\]

In particular, if

\[
\Delta_{\rm inc}=\max_{i,p}d_{i,p},
\]

then

\[
\boxed{
N\ge\frac{r(D+1)}{\Delta_{\rm inc}}.}
\tag{5.4}
\]

#### Proof

Assign every pin request to one position in its selected witness carrying
its pin coordinate. Requests from one strict chain assigned to one
position are impossible: the later pin is absent from the earlier target.

Suppose a physical position serves a set \(\mathcal R\) of requests.
Its one letter contains every pin coordinate belonging to
\(\mathcal R\), and every witness using that position contains the whole
letter. Thus each pin in \(\mathcal R\) belongs to the outer target of
every occurrence represented in \(\mathcal R\). Consequently

\[
d_{i,p}\ge|\mathcal R|
\]

for every request in that set, and

\[
\sum_{(i,p)\in\mathcal R}\frac1{d_{i,p}}\le1.
\]

Sum this inequality over physical positions. Equation (5.4) follows by
bounding every denominator by \(\Delta_{\rm inc}\). \(\square\)

Thus an \(O(r)\)-length critical gadget with \(D=\Theta(H)\) requires
physical positions serving \(\Theta(H)\) mutually compatible pins. This
is the precise high-overlap/common-coordinate theorem absent from abstract
rainbow binning.

### Theorem 5.3 (critical private-chain obstruction)

Let \(D=H+q\). For even \(r\), there are \(r\) complete literal signed
towers, with distinct deepest lower targets, central roots and owners, and
rainbow depth-\(q\) upper targets, such that every literal word covering
them has length at least

\[
\boxed{\frac r2(D+2).}
\tag{5.5}
\]

For odd \(r\), the corresponding lower bound is

\[
\boxed{\frac{r+1}{2}(D+2)-1.}
\tag{5.6}
\]

The witnesses in the competing word may be arbitrary internal or
seam-crossing intervals and need not preserve the displayed nested charts.

#### Proof

Group the occurrences into pairs. In each pair, give the first occurrence
a strict chain

\[
T_0\subsetneq T_1\subsetneq\cdots\subsetneq T_D
\tag{5.7}
\]

with fresh successive coordinates

\[
\xi_0,\xi_1,\ldots,\xi_D,
\]

all absent from every earlier member of that chain and from every target
outside the pair. The requests

\[
(T_j,\xi_j),\qquad 0\le j\le D,
\]

are pairwise incompatible. Give the second occurrence one outer target
with a further coordinate \(\eta\) absent from every \(T_j\) and every
other pair. Its request is incompatible with all preceding requests.

Coordinates belonging to different pairs are absent from the other
pairs' targets, so all

\[
\frac r2(D+2)
\]

requests are mutually incompatible. Lemma 5.1 proves (5.5). For odd
\(r\), use \((r-1)/2\) pairs and one unpaired chain with \(D+1\)
requests, giving (5.6). \(\square\)

### Explicit Boolean realization at \(q=H\)

Put \(D=2H\), and take a common set

\[
|K|=m-H-1.
\]

For each pair \(h\), take fresh coordinates

\[
x_{h,0},x_{h,1},\ldots,x_{h,D+1}.
\]

Use the literal block

\[
K\cup\{x_{h,0}\},\,
K\cup\{x_{h,1}\},\ldots,\,
K\cup\{x_{h,D+1}\}.
\tag{5.8}
\]

The first occurrence uses the nested intervals

\[
[1,1],[1,2],\ldots,[1,D],[0,D],
\tag{5.9}
\]

and the second uses

\[
[D,D],[D-1,D],\ldots,[1,D],[1,D+1].
\tag{5.10}
\]

Their successive maxima have sizes

\[
m-H,m-H+1,\ldots,m+H.
\]

The two outer targets are

\[
K\cup\{x_{h,0},\ldots,x_{h,D}\},
\qquad
K\cup\{x_{h,1},\ldots,x_{h,D+1}\}.
\tag{5.11}
\]

They have private entering coordinates \(x_{h,0}\) and \(x_{h,D+1}\).
Across different pairs all variable coordinates are disjoint, so the
outer targets are rainbow. The rank-\((m-1)\) and rank-\(m\) members of
the chains give distinct literal central roots and owners for \(H\ge2\).

For the switched mode, replace the two private endpoint letters in (5.8)
by

\[
K\cup\{a\}
\]

for one fixed coordinate \(a\) outside every old target. This changes only
the two depth-\(H\) outer targets, fixes every lower flag and every upper
flag below depth \(H\), and preserves all central roots and owners.

For

\[
s\le
\min\left\{
\left\lfloor\frac H2\right\rfloor,
\left\lfloor\frac{m+H}{2H+2}\right\rfloor
\right\},
\tag{5.12}
\]

one may take \(r=2s=\Theta_A(H)\) on a ground set of size at most
\(2m+1\) when \(H=\lceil A\sqrt m\rceil\); reserve one additional unused
coordinate together with \(a\) as the omitted source pair. Concatenating
the pair blocks gives a word attaining (5.5). Appending the full ground set once gives
both modes a common coarse one-block terminal MTF state without changing
any internal witness.

This is a fully literal direct-OR counterexample to a theorem based only
on rainbow packet membership, literal central edges, and flag towers. It
does not prove that this adversarial packet occurs among selected rows of
one exact pair-omission factor.

## 6. A positive strong Johnson seam

The exact edge-seam criterion has a particularly transparent physical
special case.

Assume \(H\le(m+1)/2\). Let

\[
P=K\cup\{p\},\qquad Q=K\cup\{q\}
\tag{6.1}
\]

be adjacent \(m\)-sets, with \(|K|=m-1\). Choose four pairwise
label-disjoint ordered rails

\[
A=(a_0,\ldots,a_{H-2}),\quad
R=(r_0,\ldots,r_{H-2})\subset K,
\]

and

\[
D=(d_0,\ldots,d_{H-2}),\quad
B=(b_0,\ldots,b_{H-2})
\subset\Omega\setminus(K\cup\{p,q\}).
\]

Put

\[
C=K\setminus(A\cup R).
\tag{6.2}
\]

Start at

\[
V_0=C\cup R\cup D\cup\{p\},
\tag{6.3}
\]

perform the exchanges

\[
d_i\mapsto a_i\quad(0\le i\le H-2),
\qquad p\mapsto q,
\qquad r_i\mapsto b_i\quad(0\le i\le H-2).
\tag{6.4}
\]

Call such a \(2H\)-state Johnson seam strong when all \(2H-1\)
departing labels and all \(2H-1\) entering labels are globally distinct
and the central transition is the prescribed edge \(P\to Q\).
Construction (6.3)--(6.4) is strong, gives exactly \(2H\) middle states,
and crosses that seam.

### Theorem 6.1 (four-rail normal form)

The top crossing lower-intersection and upper-range-max packets of
(6.3)--(6.4) are

\[
S_j
=C\cup\{a_i:i<j\}\cup\{r_i:i\ge j\},
\tag{6.5}
\]

and

\[
U_j
=(K\cup\{p,q\})
 \cup\{d_i:i\ge j\}\cup\{b_i:i<j\},
\tag{6.6}
\]

for \(0\le j<H\). In particular,

\[
\bigcup_jS_j=P\cap Q=K,\qquad
\bigcap_jU_j=P\cup Q.
\tag{6.7}
\]

Conversely, every globally label-disjoint strong Johnson seam has this
form after ordering its packet. Equivalently, the prescribed lower packet
and upper packet must be geodesic Johnson paths under one common indexing,
satisfy (6.7), and use the same two-element central orientation. If
\(P,Q\) are not prescribed, the two elements of

\[
\bigcap_jU_j\setminus\bigcup_jS_j
\]

give exactly the two possible seam orientations.

#### Proof

Before the central exchange, each step replaces one \(d_i\) by one
\(a_i\); after it, each step replaces one \(r_i\) by one \(b_i\).
Intersecting the \(H+1\) consecutive middle states in the \(j\)-th top
window retains exactly \(C\), the already-entered \(a_i\)'s, and the
not-yet-departed \(r_i\)'s, giving (6.5). Taking their union retains the
central \(K\cup\{p,q\}\), the not-yet-departed \(d_i\)'s, and the
already-entered \(b_i\)'s, giving (6.6).

Conversely, consecutive lower top targets expose the ordered exchanges
\(r_i\mapsto a_i\), and consecutive upper top targets expose
\(d_i\mapsto b_i\). Their union and intersection identify \(K\) and
\(K\cup\{p,q\}\). Global label-disjointness separates the four rails.
The only remaining choice is which element of the two-point difference is
\(p\) and which is \(q\). Reversing the displayed reconstruction verifies
every state and every top window. \(\square\)

The top packet forces all smaller crossing packets: they are the
intersections and unions of the corresponding shorter consecutive
subwindows of the same \(V\)-word. Independent set equality at each depth
is therefore not enough. Literal use of Theorem 6.1 requires checking one
common indexing, every induced smaller-depth packet, the outer
\(H\)-transition history, and the terminal ordered-partition condition
(3.7).

The \(U_j\)'s are literal crossing range maxima of the displayed
middle-state word. The \(S_j\)'s are its matching intersection traces;
they require the usual lower bulk/difference word if they too are to be
literal OR targets. Theorem 6.1 is therefore a positive upper-seam and
state-compatibility regime, not by itself a one-word signed-band theorem.

Theorem 6.1 does not evade the audited
same-source phase-age separation for canonical owner-fixed spikes; its
role is to state exactly what a successful direct seam would have to look
like after the canonical phase restriction is abandoned or different
phases are interleaved.

## 7. Exact constant-one ledger

At Gaussian depth the audited critical-seam demand has order

\[
b=\Theta(W/H).
\tag{7.1}
\]

A standalone minimal packet with \(t=\Theta(H)\) uses \(2t=\Theta(H)\)
arm positions. Paying those positions afresh at all \(b\) seams costs

\[
\Theta(H)\Theta(W/H)=\Theta(W),
\tag{7.2}
\]

which is fatal for coefficient one.

The edge-seam theorem is quantitatively useful only in overlap form:

1. its \(t\) left letters are an already-paid suffix of the preceding
   critical block;
2. its \(t\) right letters are an already-paid prefix of the next block;
3. only \(O(1)\) connector letters, or no new letter, are charged at the
   seam;
4. the target order satisfies the coordinate interval condition (2.1);
5. both modes satisfy the ported Safe-Pin equations and the common-state
   equality (3.7); and
6. all smaller-depth windows induced by the same arms have the prescribed
   targets.

An \(O(1)\) connector cost at \(O(W/H)\) seams is \(O(W/H)=o(W)\).
The \(\Theta(H)\) arm cost is not.

The exact advance is therefore a replacement of the informal
two-port request by three checkable objects:

\[
\boxed{
\text{consecutive-zero packet order}
+\text{already-paid arm matching}
+\text{last-occurrence state matching}.}
\tag{7.3}
\]

What remains unproved for the actual exact-factor collision packets is a
global ordering/matching theorem producing these three objects
simultaneously in both modes and at every required depth.

## 8. Independently checked scope

The decisive statements were derived independently in three forms:

1. the coordinatewise quasiconvex factorization (Theorem 2.1);
2. endpoint-injection and sliding-ladder rigidity (Theorems 2.2 and 4.1);
3. the pin incompatibility certificate (Theorem 5.3).

The scope boundary is exact.

- The report proves a complete minimal pure edge-seam theorem.
- It proves that rainbow plus literal tower data alone cannot imply a
  short direct-OR gadget.
- It gives a positive four-rail common-seam normal form.
- It does not embed the adversarial packet in one exact source factor.
- It does not order the real diffuse packets into consecutive-zero
  families.
- It does not prove common MTF ports from range-max port coverage.
- It does not prove constant one.

The canonical same-phase rotating-frame theorem is already closed more
strongly by the phase-residence bound

\[
t'-t\ge H+q.
\]

This note does not repackage that no-go. It characterizes the genuinely
noncanonical seam-crossing range-max escape which remains after it.
