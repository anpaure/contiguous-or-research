# Fifth-wave AD: super-long stateful portal fusion

Date: 2026-07-25

## 0. Outcome

Put

\[
W=\binom{2m}{m},\qquad H=\lceil A\sqrt m\rceil,
\qquad L=2H+1,\qquad A_0=A+1,
\]

where \(A>0\) is fixed.  Thus \(H\le A_0\sqrt m\) for every \(m\ge1\).
All asymptotic assertions below are for \(m\to\infty\), with \(A\) fixed;
any assertion using the numerical collision constant \(8\) is made for
\(m\ge m_0(A_0)\).  When product boxes are used, split
\([2m]\) into three equal even blocks, so \(2m=3s\), and fix arbitrary
SCDs in those blocks.

There is **no incompatibility** between delayed Johnson legality and
unbounded product-box occurrence degree.  The reverse-difference arms can
be fused statefully and literally.

The main positive theorem is this.

> **Global no-return packet-fusion theorem.**  Let a no-return Johnson path
> forest partition the \(W\) middle masks into \(C\) components.  Give every
> path its raw canonical radius-\(H\) MTF lift, with a legal terminal dummy
> completion, and initialize independently.  For \(m\ge m_0(A_0)\), after one
> common coordinate relabelling, the resulting literal word has
> exact length
> \[
> \boxed{W+LC}
> \tag{0.1}
> \]
> and contains pairwise disjoint, entirely middle-productive portal packets
> \(\mathcal Q\) satisfying
> \[
> \boxed{
> L|\mathcal Q|
> \ge W-3HC-\frac{8HW}{m}.}
> \tag{0.2}
> \]
> Every packet consists of \(L\) consecutive low-rank MTF updates and its
> right endpoint exposes the \(L\) ranks \(m-H,\ldots,m+H\) in \(L\)
> distinct product boxes.

For the exact odd factor,

\[
C=B=\frac{W}{m+1},
\]

so

\[
\boxed{
|\mathcal Q|=(1-o(1))\frac{W}{2H+1}.}
\tag{0.3}
\]

All components have \(m+1=\omega(H)\) middle states and no finite positive
run.  Thus the construction uses very few super-\(H\)-long components and
almost tiles the principal word by maximal-degree portal packets.

The residual-depletion lower bound is sharp to an additive \(C-1\).  For
any spanning system of \(C\) residual-consuming canonical components with
\(m-H\ge2\),

\[
\boxed{
2HC+1\le\mathfrak P_H^{\min}\le(2H+1)C.}
\tag{0.4}
\]

Consequently

\[
\boxed{
\mathfrak P_H^{\min}=o(W)
\iff HC=o(W)
\iff \frac{W/C}{H}\longrightarrow\infty.}
\tag{0.5}
\]

Thus average component length \(\omega(H)\) is simultaneously the exact
reset-amortization criterion and the packet-boundary-amortization criterion
in the no-return depleted architecture.

There is nevertheless an exact remaining obstruction.  A canonical update
has two modes: a queue-recycling arrival leaves the deepest upper flag fixed,
whereas a deep-complement arrival moves it by one Johnson edge.  If \(a\) is
the number of deep arrivals, \(D\) the number of consuming components, and
\(J\) the number of distinct residual values among nonconsuming components,
then

\[
\boxed{|\mathcal S_H^+|\le J+D+a.}
\tag{0.6}
\]

At Gaussian depth, small portal excess and near-full deepest support force

\[
\boxed{a\ge(e^{-A^2}+o(1))W.}
\tag{0.7}
\]

A sharp cyclic hole rotor has positive runs of length \(m\), all but
\(O_A(H)\) endpoints fully box-rainbow after relabelling, and almost maximal
aggregate distinct support, but its deepest upper support has size one.
Therefore product-box incidence, aggregate incidence, and delayed legality
cannot replace rankwise support.  The remaining global theorem is a
cross-component deep-support theorem, not a state-dynamics or reset theorem.

No web search, finite search, or computation is used.

---

## 1. Extending one reverse-difference portal into an exact state walk

Let

\[
w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1})
\]

be a cyclic ordering of \([2m]\).  Indices of \(w\) are taken modulo
\(2m\), and

\[
I_w(r,k)=\{w_r,w_{r+1},\ldots,w_{r+k-1}\}.
\]

Assume \(1\le H<m\).  Define

\[
T_t=I_w(t,m),
\qquad
L_t=I_w(t+H,m-H).
\tag{1.1}
\]

Put

\[
R_0=\{b_0,\ldots,b_{m-H-1}\},
\tag{1.2}
\]

\[
\Theta_0=
\bigl(
\{b_{m-1}\},\ldots,\{b_{m-H}\},R_0
\bigr),
\tag{1.3}
\]

and recursively set

\[
\Theta_{t+1}
=\bigl(\{w_t\},\Theta_t\setminus\{w_{t+m}\}\bigr),
\tag{1.4}
\]

deleting empty blocks.  Finally let

\[
\Pi_t=
\bigl(
L_t,
\{w_{t+H-1}\},\ldots,\{w_t\},
\Theta_t
\bigr).
\tag{1.5}
\]

### Theorem 1.1 — doubled complementary portal walk

For every \(t\), \(\Pi_t\) is an ordered partition of \([2m]\), and

\[
\boxed{
\Pi_{t+1}=M_{L_{t+1}}(\Pi_t).}
\tag{1.6}
\]

Its middle owner is \(T_t\), and its full signed radius-\(H\) flag is

\[
\boxed{
F_{t,q}=I_w(t-q,m+q),
\qquad -H\le q\le H.}
\tag{1.7}
\]

The \(2m\) middle owners \(T_0,\ldots,T_{2m-1}\) are pairwise distinct,
and all

\[
2m(2H+1)
\]

flag masks in (1.7) are globally distinct.

#### Proof

One has

\[
L_{t+1}
=L_t\setminus\{w_{t+H}\}\cup\{w_{t+m}\}.
\tag{1.8}
\]

Applying the update by \(L_{t+1}\) to (1.5), direct block subtraction
gives

\[
\begin{aligned}
M_{L_{t+1}}(\Pi_t)
=\bigl(&L_{t+1},
\{w_{t+H}\},\{w_{t+H-1}\},\ldots,\{w_t\},\\
&\Theta_t\setminus\{w_{t+m}\}\bigr),
\end{aligned}
\]

which is \(\Pi_{t+1}\) by (1.4).

The first \(H\) blocks of \(\Theta_t\) are always

\[
\{w_{t-1}\},\ldots,\{w_{t-H}\}.
\tag{1.9}
\]

This is true at \(t=0\) by (1.3).  The deleted coordinate \(w_{t+m}\)
cannot lie in the displayed \(H\)-window because \(H<m\), so (1.4) proves
the assertion inductively.

The prefix unions of (1.5), using (1.9), are exactly (1.7).  The middle
prefix is

\[
L_t\cup\{w_{t+H-1},\ldots,w_t\}=I_w(t,m)=T_t.
\]

For a fixed nontrivial cyclic interval length, its starting position is
unique; different values of \(q\) give different ranks.  This proves all
distinctness assertions.  \(\square\)

The literal word realizing the first \(2m\) states is

\[
\boxed{
R_0,
\{b_{m-H}\},\ldots,\{b_{m-1}\},
\{a_0\},\ldots,\{a_{H-1}\},
L_0,L_1,\ldots,L_{2m-1}.}
\tag{1.10}
\]

It has exact length

\[
\boxed{2m+2H+1.}
\tag{1.11}
\]

The first \(2H+2\) letters are the reverse-block initialization of
\(\Pi_0\); after that, every new letter creates a new middle owner and a
whole new radius-\(H\) portal flag.

On the bi-infinite cyclic owner trajectory, every coordinate enters and
leaves exactly \(m\) steps later.  Thus every uncensored finite positive run
has length exactly \(m>H\).  The walk is maximally delayed for the present
purpose.

### 1.1 Starting from a prescribed maximum-degree portal

Let a middle mask \(T\) have a prescribed reverse-difference flag: for every
\(1\le q\le H\),

\[
F_{0,-q}=T\setminus\{x_1,\ldots,x_q\},\qquad
F_{0,0}=T,\qquad
F_{0,q}=T\cup\{y_1,\ldots,y_q\}.
\tag{1.12}
\]

Choose the two coordinate orders so that

\[
a_{j-1}=x_j,
\qquad
b_{m-j}=y_j,
\qquad 1\le j\le H,
\tag{1.13}
\]

and fill the remaining positions arbitrarily.  Then \(T_0=T\), and all
three identities in (1.12) follow from (1.7).

In particular, when \(2m=3s\), \(s\) is even, and \(H\le s/6\), the
audited greedy two-sided box-rainbow portal through any \(T\) extends to the
walk in Theorem 1.1.  Hence a maximum possible product-box degree
\(2H+1\) at the initial endpoint is deterministically compatible with
positive-run delay \(m\).

### 1.2 Residual evolution

During the first half of the walk, the surviving coarse residual is

\[
R_t=R_0\setminus\{b_0,\ldots,b_{t-1}\},
\qquad
|R_t|=(m-H-t)_+.
\tag{1.14}
\]

Its consumption begins with the first update, and it vanishes at
\(t=m-H\).  At the midpoint,

\[
\Theta_m=(\{a_{m-1}\},\ldots,\{a_0\}).
\tag{1.15}
\]

The second half of the walk continues with a fully singleton-refined tail.
At \(t=2m\), the useful flag and middle owner return.  If \(m-H\ge2\), the
complete state does not return to the fresh state \(\Pi_0\), because the
fresh nonsingleton residual has been fully refined.  (At the boundary
\(m-H=1\), every block was already a singleton and \(\Pi_{2m}=\Pi_0\).)
This is why, in the depletion range, the two complementary arms fuse
without an intervening reset and the component is residual-consuming.

### 1.3 Product-box incidence on the explicit walk

For one endpoint, let \(C_t(\sigma)\) count pairs in its flag which a
coordinate permutation \(\sigma\) sends to one product box.  For flag levels
\(a<b\), put \(d=b-a\).  Conditional on the upper mask, the lower mask is a
uniform \(d\)-deletion.  A fixed product box has at most
\(\binom{d+2}{2}\) such predecessors, one for each weak composition of
\(d\) into three factor drops.  Therefore

\[
\mathbb E\sum_tC_t
\le2m\,\varepsilon_{m,H}^{\sharp},
\tag{1.16}
\]

where

\[
\varepsilon_{m,H}^{\sharp}
=\sum_{-H\le a<b\le H}
\frac{\binom{b-a+2}{2}}{\binom{m+b}{b-a}}.
\tag{1.17}
\]

Uniformly for \(H\le A_0\sqrt m\),

\[
\boxed{
\varepsilon_{m,H}^{\sharp}
=\frac{6H}{m}+O_A(m^{-3/2}).}
\tag{1.18}
\]

Indeed, the gap-one contribution is

\[
3\sum_{b=-H+1}^{H}\frac1{m+b}
=\frac{6H}{m}+O_A(m^{-3/2}),
\]

because \(\sum_{b=-H+1}^{H}b=H\) and
\(\sum_{b=-H+1}^{H}b^2=O(H^3)\), so termwise expansion around \(m\)
has error \(O(H/m^2+H^3/m^3)=O_A(m^{-3/2})\).

For completeness, write \(M=m-H\).  For a gap \(d\ge2\), the summand is at
most (here \(b\ge-H+d\), so \(m+b\ge M+d\))

\[
u_d=\frac{\binom{d+2}{2}}{\binom{M+d}{d}}.
\]

Moreover

\[
\frac{u_{d+1}}{u_d}=\frac{d+3}{M+d+1}\le\frac12
\]

for all \(2\le d<2H\) once \(m\ge m_0(A_0)\).  Since

\[
u_2=\frac{12}{(M+1)(M+2)},
\]

the total contribution of \(d\ge2\) is at most

\[
2H\sum_{d=2}^{2H}u_d
\le \frac{48H}{(M+1)(M+2)}
=O_A(H/m^2)=O_A(m^{-3/2}).
\]

Thus one common relabelling has only \(O_A(H)\) colliding endpoint units.
All but \(O_A(H)\) endpoints have degree exactly \(2H+1\), and the total
endpoint degree is

\[
2m(2H+1)-O_A(H).
\tag{1.19}
\]

This proves, already on one explicit state walk, that delayed legality and
near-maximal product-box incidence are compatible.

---

## 2. Productive portal packets on no-return paths

Let

\[
T_0,T_1,\ldots,T_{K-1}
\]

be a no-return Johnson path:

\[
T_{t+1}=T_t-\{p_t\}+\{q_t\},
\]

with no departed coordinate returning and no inserted coordinate later
departing.  Assume \(m\ge2H\).  Extend the departure list by \(H\) dummy
symbols

\[
p_{K-1},\ldots,p_{K+H-2}
\tag{2.0}
\]

chosen distinctly from

\[
\mathcal D_{\rm term}
=\bigcap_{i=\max(0,K-1-H)}^{K-1}T_i.
\]

Indeed \(|\mathcal D_{\rm term}|\ge m-H\ge H\).  No actual departed coordinate lies in the
terminal state, so these dummy symbols are also distinct from every
relevant actual future departure.  Put

\[
L_t=T_t\setminus\{p_t,\ldots,p_{t+H-1}\}
\tag{2.1}
\]

for \(0\le t<K\), using (2.0) near the terminal end.  No-return gives, on
every actual transition,

\[
L_{t+1}=L_t-\{p_{t+H}\}+\{q_t\}.
\tag{2.2}
\]

At every center

\[
2H\le t\le K-1-H,
\tag{2.3}
\]

the exact raw-history MTF state has useful prefix

\[
\bigl(
L_t,
\{p_{t+H-1}\},\ldots,\{p_t\},
\{p_{t-1}\},\ldots,\{p_{t-H}\}
\bigr).
\tag{2.4}
\]

The blocks displayed in (2.4) have last-update times

\[
t,t-1,\ldots,t-2H.
\tag{2.5}
\]

To obtain the full lift, choose any \(H\) distinct initial upper markers
outside \(T_0\), put the remaining coordinates in the final residual block,
reverse-write these \(2H+2\) initial blocks, and then append
\(L_1,\ldots,L_{K-1}\).  Equations (2.1)--(2.2) give the exact MTF
transition at every step.  Once \(t\ge H\), the last \(H\) departure
markers in (2.4) have displaced all arbitrary initial upper markers from
the useful prefix.

### Lemma 2.1 — middle-productive packet identity

For every \(-H\le q\le H\),

\[
\boxed{
F_{t,q}=\bigcup_{j=t-q-H}^{t}L_j.}
\tag{2.6}
\]

Consequently the entire radius-\(H\) flag at time \(t\) is witnessed inside
the literal productive packet

\[
\boxed{
\mathcal A_t=(L_{t-2H},L_{t-2H+1},\ldots,L_t).}
\tag{2.7}
\]

Every one of these \(L\) positions is a principal path update and ends a
middle-owner state.  Centers separated by at least \(L=2H+1\) have disjoint
packets.

#### Proof

The last-occurrence times in (2.5) show that the suffix beginning at
\(L_{t-q-H}\) and ending at \(L_t\) has union equal to the first
\(H+q+1\) blocks of (2.4), which is \(F_{t,q}\).  Equation (2.3) keeps all
letters at principal middle-owner positions, with no excess-initialization
letter and no position depending on a terminal dummy.  At \(t=2H\), the
first packet letter is \(L_0\), which is simultaneously the last
reverse-initialization letter and the principal position for \(T_0\).
\(\square\)

This is the exact stateful fusion of the isolated reverse-difference arm:
one common \(L\)-letter stretch consists entirely of middle-producing
updates and realizes every one of the \(L\) arm targets at its final
endpoint.

### Lemma 2.2 — exact common-endpoint packet minimum

Let a literal OR word realize \(L\) distinct masks by intervals sharing one
right endpoint \(r\).  Their left endpoints are pairwise distinct, since
two intervals \([\ell,r]\) with the same \(\ell\) have the same OR.  Hence
the interval from the earliest left endpoint through \(r\) contains at
least \(L\) physical positions.

Therefore no common-right-endpoint literal packet exposing all
\(2H+1=L\) saturated flag ranks can have fewer than \(L\) positions.  The
productive packet (2.7) attains this minimum exactly.  This minimality is
for the common-endpoint architecture; it does not rule out a different
global word that assigns the target masks to different endpoints.

---

## 3. Global no-return packet fusion

Let a no-return path forest partition all \(W\) middle masks into components
of lengths

\[
K_1,\ldots,K_C,
\qquad
\sum_iK_i=W.
\]

Independently reverse-initialize their raw canonical radius-\(H\) states.
The resulting literal word has exact length

\[
\boxed{W+(2H+1)C.}
\tag{3.1}
\]

There is no missing seam charge: each component contributes \(K_i-1\)
internal updates and a \(2H+2\)-letter initialization.

### Theorem 3.1 — global productive packet packing

Fix \(A_0>0\).  Assume \(H\le A_0\sqrt m\), \(m\ge m_0(A_0)\), and that
the stated three-block SCD product partition exists.  One common coordinate
relabelling gives a family \(\mathcal Q\) of pairwise disjoint packets of
the form (2.7) such that every packet endpoint has occurrence degree exactly
\(L=2H+1\) and

\[
\boxed{
L|\mathcal Q|
\ge W-3HC-\frac{8HW}{m}.}
\tag{3.2}
\]

#### Proof

Apply the collision estimate (1.17) to all \(W\) state flags.  For all
sufficiently large \(m\), its expectation is at most \(8HW/m\), so choose
one permutation with at most that many collision pairs.  The number \(b\)
of state endpoints whose flag repeats a product box is at most the collision
count:

\[
b\le\frac{8HW}{m}.
\tag{3.3}
\]

Component \(i\) has exactly \((K_i-3H)_+\) productive centers satisfying
(2.3).  Delete its bad centers.  Among the \(L\) residue classes of the
remaining center indices modulo \(L\), choose a largest class.  Its centers
are \(L\)-separated, so their packets are disjoint, and it contains at least
one \(L\)-th of the remaining good centers.  Summing over components gives

\[
\begin{aligned}
L|\mathcal Q|
&\ge\sum_i(K_i-3H)_+-b\\
&\ge W-3HC-b.
\end{aligned}
\]

Use (3.3).  \(\square\)

If

\[
HC=o(W),
\tag{3.4}
\]

then (3.2) says

\[
\boxed{
|\mathcal Q|=(1-o(1))\frac{W}{2H+1}.}
\tag{3.5}
\]

The upper bound follows because the packets are disjoint and contain
\(L\) principal positions.  Thus the packing is scale-sharp.

### 3.1 Exact odd-factor application

The cut exact odd factor has

\[
B=\frac{W}{m+1}
\tag{3.6}
\]

complementary geodesics, each with \(m+1\) middle states.  Every inserted
coordinate remains to the terminal state, so there is no finite positive
run.  For \(H=o(m)\),

\[
HB/W=H/(m+1)\longrightarrow0.
\]

Equations (3.1) and (3.5) give a literal word of exact length

\[
\boxed{
W+(2H+1)\frac{W}{m+1}}
\tag{3.7}
\]

which is \(W+o(W)\), and a near-perfect tiling by maximal-degree productive
packets.

The original literal first band is preserved exactly.  On every internal
edge \(T_{t+1}=T_t-\{p_t\}+\{q_t\}\),

\[
F_{t,-1}=T_t\setminus\{p_t\}=T_t\cap T_{t+1},
\qquad
F_{t+1,1}=T_{t+1}\cup\{p_t\}=T_t\cup T_{t+1}.
\tag{3.7a}
\]

The exact odd factor's lower and upper edge colours partition ranks
\(m-1\) and \(m+1\), respectively.  Thus the one word in (3.7) literally
covers every mask in ranks \(m-1,m,m+1\), before any deeper-support theorem
is invoked.

If \(b_i\) denotes the number of bad endpoints on path \(i\), paths with

\[
b_i>\sqrt{mH}
\]

number at most

\[
8B\left(1+\frac1m\right)\sqrt{\frac Hm}.
\tag{3.8}
\]

Every other path contains at least

\[
\frac{m-3H+1-\sqrt{mH}}{2H+1}
\tag{3.9}
\]

disjoint productive box-rainbow portals.  At Gaussian depth the exceptional
fraction is \(O_A(m^{-1/4})\), while every nonexceptional component contains

\[
\left(\frac1{2A}+o_A(1)\right)\sqrt m
\]

such portals.

### 3.2 Globally distinct depth-one anchors

The odd factor's actual upper edge colours partition rank \(m+1\).  For all
sufficiently large \(m\), so in particular \(m\ge3H\), let

\[
\mathcal T_1\subseteq\binom{[2m]}{m+1}
\]

be any prescribed family.  At center \(1\le t\le m\), the canonical
depth-one upper mask is the actual incoming edge colour:

\[
F_{t,1}=T_t\cup\{p_{t-1}\}=T_{t-1}\cup T_t.
\tag{3.10a}
\]

The productive center interval \(2H\le t\le m-H\) therefore omits exactly
\((3H-1)B\) actual upper colours.  After the relabelling used in Theorem
3.1, at least

\[
G=\left(
|\mathcal T_1|-(3H-1)B-\frac{8HW}{m}
\right)_+
\tag{3.10}
\]

productive box-rainbow centers have their actual upper depth-one target in
\(\mathcal T_1\).

Choose on each path the residue class modulo \(L\) containing the most such
centers.  This gives disjoint anchored packets with

\[
\boxed{
P_{\mathcal T}\ge\left\lceil\frac G{2H+1}\right\rceil.}
\tag{3.11}
\]

Their middle targets are globally distinct, and their selected upper
targets are globally distinct.  Each endpoint still has full occurrence
degree \(2H+1\).

For the audited dominant plateau family, one may take

\[
|\mathcal T_1|\ge\alpha W
\]

with an absolute \(\alpha>0\).  Then, for all sufficiently large \(m\),

\[
P_{\mathcal T}\ge\frac{\alpha W}{2(2H+1)}.
\tag{3.12}
\]

Thus \(\Theta(W/H)\) disjoint physical portals have honest distinct middle
and upper anchors, while all \(2H+1\) local flag occurrences remain
box-rainbow.

The total independent-reset excess is \(LB\).  Relative to the anchored
family,

\[
\frac{LB}{P_{\mathcal T}}
\le\frac{2L^2}{\alpha(m+1)}
=\frac{8A^2}{\alpha}+o_A(1).
\tag{3.13}
\]

For the near-maximal occurrence family in (3.5), the reset excess per portal
is

\[
\boxed{4A^2+o_A(1).}
\tag{3.14}
\]

The isolated reverse-difference construction pays \(\Theta(H)\) arm
letters per portal.  Stateful fusion reduces this to a bounded
\(A\)-dependent reset cost while making every packet position
middle-productive.

---

## 4. Residual depletion and the exact component threshold

Let a spanning canonical path system have \(C\) components, all
residual-consuming, and let \(\mathfrak P_H^{\min}\) be the least exact
portal excess over all component orders and exact-state bridges.

### Theorem 4.1 — exact super-\(H\) criterion

Assume \(m-H\ge2\).  Then

\[
\boxed{
2HC+1\le\mathfrak P_H^{\min}\le(2H+1)C.}
\tag{4.1}
\]

Consequently, for a sequence of spanning systems,

\[
\boxed{
\mathfrak P_H^{\min}=o(W)
\iff HC=o(W)
\iff \frac{W/C}{H}\to\infty.}
\tag{4.2}
\]

#### Proof

The first fresh state costs \(2H+1\) excess beyond its middle owner.  The
audited depletion theorem says that every outgoing seam from a consuming
component has bridge length at least \(2H+1\), hence excess at least \(2H\).
There are \(C-1\) such seams.  Therefore

\[
\mathfrak P_H^{\min}
\ge(2H+1)+2H(C-1)=2HC+1.
\]

Independent reverse initialization gives the upper bound.  Since the
component lengths sum to \(W\), their average is \(W/C\), and (4.2)
follows.  \(\square\)

For the odd factor, \(C=B=W/(m+1)\).  Hence its components are
super-\(H\)-long whenever \(H=o(m)\).  If also \(H\to\infty\), its
independent reset ledger is asymptotically optimal:

\[
\frac{(2H+1)B}{2HB+1}=1+O(1/H).
\tag{4.3}
\]

The same condition \(HC=o(W)\) appears in Theorem 3.1.  It is therefore
both necessary for cheap exact resets in the all-depleted class and
sufficient for a near-perfect productive packet packing in the no-return
class.

### 4.1 Sharp continuation after a depleted doubled walk

At the end of the doubled walk in Section 1, the source state has first
block \(A\), \(|A|=m-H\), and every later block is a singleton.  Let a
fresh target have residual block exactly \(A\).  Its first \(2H+1\) blocks
partition \(A^c\).  Deleting their union from the source leaves the single
block \(A\), so the exact bridge formula gives distance at most \(2H+1\).
The depletion theorem gives the reverse inequality.  Thus the distance is
exactly

\[
2H+1.
\tag{4.4}
\]

If \(2m=3s\), \(s\) is even, and \(m\ge3H+2\), this fresh target can be chosen
box-rainbow.  Starting at \(A^c\), greedily delete \(2H\) coordinates.  At
deletion step \(j\), the current mask has \(m+H-j+1\) lower neighbours.
Its own previously used product box contains at most three, and each of the
other \(j-1\) used boxes contains at most one.  Thus at most \(j+2\)
candidates are forbidden.  The inequality

\[
m+H-j+1>j+2
\]

holds through \(j=2H\) under the stated hypothesis.

Consequently \(C\) such local doubled walks can be chained with every new
component beginning at a maximum-degree portal and exact total length

\[
\boxed{2mC+2HC+1.}
\tag{4.5}
\]

This attains the numerical bridge/reset constant \(2HC+1\) in (4.1).  It is
a local exact-state construction, not an attainment theorem inside the
spanning owner-disjoint class: no claim is made that the middle owners of
different doubled walks are disjoint.

---

## 5. The four-reservoir identity and the real deep-support gate

Consider an internal transition of one \(H\)-legal canonical lift for which
\(p_t,\ldots,p_{t+H}\) and both consecutive states are defined (a declared
legal dummy continuation is allowed).  Write its ordered useful prefix as

\[
\Pi_t=\bigl(
L_t,
\{p_{t+H-1}\},\ldots,\{p_t\},
\{u_{t,1}\},\ldots,\{u_{t,H}\},
\mathcal C_t
\bigr),
\tag{5.0}
\]

where \(\mathcal C_t\) is the ordered refined tail.  At the coarser set
level, group the coordinates as

\[
[2m]=L_t\sqcup P_t\sqcup Q_t\sqcup C_t,
\tag{5.1}
\]

where

\[
|L_t|=|C_t|=m-H,
\qquad
|P_t|=|Q_t|=H.
\]

Here:

* \(L_t=F^-_{t,H}\) is the lower core;
* \(P_t\) is the ordered future-departure queue;
* \(Q_t=(u_{t,1},\ldots,u_{t,H})\) is the exposed upper queue;
* \(C_t=[2m]\setminus F^+_{t,H}\) is the union of all blocks beyond that
  upper prefix.

The arrival \(q_t\) lies in exactly one of \(Q_t,C_t\).  Here
\(C_t=\bigcup\mathcal C_t\); the theorem below tracks this union, not an
assertion that the physical tail is one block.

### Theorem 5.1 — exact two-mode state walk

Every internal transition just specified satisfies

\[
L_{t+1}=L_t-\{p_{t+H}\}+\{q_t\},
\tag{5.2}
\]

and

\[
\boxed{
C_{t+1}=
\begin{cases}
C_t,&q_t\in Q_t,\\[2mm]
C_t-\{q_t\}+\{u_{t,H}\},&q_t\in C_t.
\end{cases}}
\tag{5.3}
\]

Thus the lower deepest flag moves on every transition, whereas the upper
deepest flag moves exactly on a **deep-complement arrival**.

#### Proof

The update inserts the new lower core at the front.  The old lower core
loses \(p_{t+H}\), which becomes the newest lower singleton, and the oldest
lower singleton \(p_t\) enters the upper queue.

If \(q_t=u_{t,j}\in Q_t\), the exact next ordered upper queue is

\[
Q_{t+1}=(p_t,u_{t,1},\ldots,\widehat{u_{t,j}},\ldots,u_{t,H}),
\]

which has \(H\) singleton entries.  The refined tail and hence its union
\(C_t\) are unchanged.

If \(q_t\in C_t\), it is removed from the tail.  The new singleton
\(p_t\) makes \(H+1\) upper candidates, so the oldest exposed marker
\(u_{t,H}\) is demoted past the useful upper prefix.  Exactly,

\[
Q_{t+1}=(p_t,u_{t,1},\ldots,u_{t,H-1}),
\]

and the refined tail begins with the retained singleton
\(\{u_{t,H}\}\), followed by \(\mathcal C_t\setminus\{q_t\}\) with empty
blocks deleted.  Thus “demotion” is a coarse-union statement, and its new
union is \(C_t-\{q_t\}+\{u_{t,H}\}\).  This gives (5.3).  \(\square\)

Positive-run legality controls the residence time of an entering coordinate
before it may depart.  It places no lower bound on how often the second mode
in (5.3) occurs.

### Theorem 5.2 — deep-arrival support ledger

Let \(\mathcal S_H^+\) be the rank-\((m+H)\) support at the designated
canonical component endpoints only; incidental masks exposed during resets
or bridges are not included.  Let \(a\) be the total number of internal
deep-complement arrivals over all those components, \(D\) the number of
residual-consuming components, and \(J\) the number of distinct full
initial residual values among the nonconsuming components.  Put

\[
N_H=\binom{2m}{m+H},\qquad
M_H^+=N_H-|\mathcal S_H^+|.
\tag{5.3a}
\]

Then

\[
\boxed{|\mathcal S_H^+|\le J+D+a.}
\tag{5.4}
\]

Consequently

\[
\boxed{a\ge N_H-M_H^+-J-D.}
\tag{5.5}
\]

#### Proof

Before a component's first deep arrival, (5.3) keeps
\(C_t=C_0=R_0\).  Its first deep arrival therefore consumes one coordinate
of the initial residual.  Hence a nonconsuming component has no deep
arrival, and \(C_t\) is its fixed full residual; these components contribute
at most \(J\) values.  A consuming component contributes its initial value
and at most one new value for every deep arrival, giving at most \(D+a\)
further values.  Since
\(F^+_{t,H}=C_t^c\), (5.4) follows.  Equation (5.5) is its rearrangement.
\(\square\)

For the following portal-excess consequence, assume \(m-H\ge2\) and that
each component begins in a fresh exact canonical state.  The audited
residual-depletion system theorem says that

\[
\mathfrak P_H=o(W)
\quad\Longrightarrow\quad
D,J=o(W/H).
\tag{5.6}
\]

If \(H=A\sqrt m+o(\sqrt m)\) and \(M_H^+=o(W)\), then

\[
\frac{N_H}{W}
=\prod_{j=1}^{H}\frac{m-j+1}{m+j},
\qquad
\log\frac{N_H}{W}
=-\frac{H^2}{m}+O_A(m^{-1}).
\tag{5.6a}
\]

Indeed, summing
\(\log(1-(j-1)/m)-\log(1+j/m)\) gives linear term
\(-\sum_{j=1}^H(2j-1)/m=-H^2/m\); the quadratic correction is
\(O(H^2/m^2)\), and the summed cubic remainder is
\(O(H^4/m^3)\), both \(O_A(m^{-1})\).

Therefore \(N_H=(e^{-A^2}+o_A(1))W\).

Equations (5.5)--(5.6) give

\[
\boxed{
a\ge(e^{-A^2}+o_A(1))W,
\qquad
a/D=\omega(H).}
\tag{5.7}
\]

The first inequality forces \(D\ge1\) for all sufficiently large \(m\), so
the quotient in (5.7) is defined; the second then follows from
\(D=o(W/H)\).

Thus a successful few-component construction needs a positive density of
genuinely upper-deep moves.  Merely making components long is not enough.

Complementary geodesics meet this necessary motion condition.  With the
Section 1 reverse initialization, the initial upper queue consists of the
last \(H\) arrivals in reverse order.  The first \(m-H\) arrivals consume
the original residual; each deep update demotes the oldest exposed marker
into \(C_t\), so each of the last \(H\) arrivals is already in \(C_t\) by
the time it arrives.  Thus all \(m\) arrivals on every odd-factor geodesic
are deep and

\[
a=mB=\frac{m}{m+1}W=(1-o(1))W.
\tag{5.8}
\]

Its unresolved defect is therefore cross-component support collision, not
absence of deep motion.

---

## 6. Sharp counterexample: the hole rotor

Let

\[
[2m]=U\sqcup R,
\qquad |U|=m+H,
\qquad |R|=m-H,
\]

and cyclically index \(U=\{u_t:t\in\mathbb Z_{m+H}\}\).  Put

\[
T_t=U\setminus\{u_t,\ldots,u_{t+H-1}\},
\tag{6.1}
\]

\[
L_t=U\setminus\{u_t,\ldots,u_{t+2H-1}\},
\tag{6.2}
\]

and

\[
\Pi_t=
\bigl(
L_t,
\{u_{t+2H-1}\},\ldots,\{u_{t+H}\},
\{u_{t+H-1}\},\ldots,\{u_t\},
R
\bigr).
\tag{6.3}
\]

Assume \(H<m\), so \(m+H>2H\).

### Theorem 6.1 — delayed, box-rainbow, support-collapsed cycle

The states (6.3) form an exact cyclic MTF trajectory:

\[
\boxed{
\Pi_{t+1}=M_{L_{t+1}}(\Pi_t).}
\tag{6.4}
\]

Every positive run has length exactly \(m>H\).  Its signed flags are

\[
F^-_{t,q}
=U\setminus\{u_t,\ldots,u_{t+H+q-1}\},
\tag{6.5}
\]

\[
F^+_{t,q}
=U\setminus\{u_t,\ldots,u_{t+H-q-1}\}.
\tag{6.6}
\]

Consequently, with \(N=m+H\),

\[
|\mathcal S_q^-|=N\quad(0\le q\le H),
\tag{6.7}
\]

\[
|\mathcal S_q^+|=N\quad(0\le q<H),
\tag{6.8}
\]

but

\[
\boxed{|\mathcal S_H^+|=1.}
\tag{6.9}
\]

Its aggregate distinct flag support is

\[
\boxed{2HN+1}
\tag{6.10}
\]

out of \((2H+1)N\) occurrences.

If additionally \(2m=3s\) with \(s\) even, then relative to every fixed
three-block SCD product partition, one common coordinate relabelling makes
all but at most

\[
N\varepsilon_{m,H}^{\sharp}
=6H+O_A(1)
\tag{6.11}
\]

endpoints fully box-rainbow when \(H\le A_0\sqrt m\) and
\(m\ge m_0(A_0)\).

#### Proof

One has

\[
L_{t+1}=L_t-\{u_{t+2H}\}+\{u_t\}.
\]

Updating (6.3) by \(L_{t+1}\) prepends the new core, turns
\(u_{t+2H}\) into the newest singleton, deletes \(u_t\) from the oldest
upper singleton, and leaves \(R\) fixed.  This is exactly \(\Pi_{t+1}\).

The arrival at time \(t\) is \(u_t\), and it next departs after \(m\)
steps.  Formulas (6.5)--(6.6) are the prefix unions of (6.3).  Nonempty
cyclic omitted intervals have \(N\) different starts; at \(q=H\) the upper
omitted interval is empty, giving the single mask \(U\).  This proves
(6.7)--(6.10).

Finally apply the common-relabel collision estimate (1.17) to the \(N\)
state flags.  \(\square\)

The hole rotor has no deep-complement arrivals: every arrival is recycled
from the exposed upper queue, so \(C_t=R\) is fixed.  It attains the
two-mode obstruction sharply.

The example proves more than the failure of an occurrence count.  Even
almost maximal aggregate **distinct** support, maximal delay, and almost
maximal local product-box degree can coexist with complete collapse in one
required signed rank.  Rankwise support cannot be replaced by any of those
three statistics.

---

## 7. Exact scope of the remaining global problem

Let

\[
\mathsf A=\{a_0,\ldots,a_{m-1}\},\qquad
\mathsf B=\{b_0,\ldots,b_{m-1}\},\qquad
\mathsf A\sqcup\mathsf B=[2m],
\]

and assume \(m\ge2H\).  Inside the certified interior of one complementary
geodesic there is no support obstruction.  If

\[
T_t=
(\mathsf A\setminus\{a_0,\ldots,a_{t-1}\})
\cup\{b_0,\ldots,b_{t-1}\},
\]

then for \(H\le t\le m-H\) and \(0\le q\le H\),

\[
F^-_{t,q}
=(\mathsf A\setminus\{a_0,\ldots,a_{t+q-1}\})
\cup\{b_0,\ldots,b_{t-1}\},
\tag{7.1}
\]

\[
F^+_{t,q}
=(\mathsf A\setminus\{a_0,\ldots,a_{t-q-1}\})
\cup\{b_0,\ldots,b_{t-1}\}.
\tag{7.2}
\]

Here an initial segment ending at index \(-1\) is empty, and the two
formulas at \(q=0\) name the same middle mask and are counted once.

For each fixed signed depth these masks are distinct as \(t\) varies,
because their intersection with the arrival set has size \(t\).  Different
signed positive depths have different ranks, and the two signs have
different ranks except at \(q=0\).  Thus the certified interior of one
super-\(H\)-long component has exactly

\[
(2H+1)(m-2H+1)
\]

globally distinct flag masks.  No assertion about unaudited boundary flags
is needed.  Any failure within this interior family is entirely
cross-component.

For the packet family \(\mathcal Q\) in Theorem 3.1, every endpoint is
box-rainbow.  Let \(I_{\rm free}(\mathcal Q)\) be the maximum number of its
endpoint--box cells that can be labelled by pairwise distinct flag masks,
with no prescribed target restriction.  Repeated masks at different
endpoints may be chosen only once, while every distinct mask supplies one
cell and two masks at one endpoint occupy different boxes.  Therefore the
exact free-target identity is

\[
\boxed{
I_{\rm free}(\mathcal Q)
=\left|\bigcup_{Q\in\mathcal Q}\mathcal F(Q)\right|.}
\tag{7.3}
\]

For a prescribed selected target family \(\mathcal T_{\rm sel}\), the exact
usable capacity is instead

\[
\boxed{
I_{\rm sel}(\mathcal Q)
=\left|
\mathcal T_{\rm sel}\cap
\bigcup_{Q\in\mathcal Q}\mathcal F(Q)
\right|.}
\tag{7.4}
\]

Since \(|\mathcal Q|=(1-o(1))W/L\), free support \(\Omega(W)\) is equivalent
to average free degree \(\Omega(H)\) on the packed endpoints.  It does not
by itself imply selected-target incidence, FEN, or \(\mathrm{PTAD}_A\).
The globally distinct middle and upper depth-one anchors in Section 3.2
contribute only \(O(W/H)\) selected masks, so a prescribed deep
packet-support/trace theorem remains necessary.

A single length-\((m+1)\) geodesic supplies at most

\[
L\left\lceil\frac{m+1}{L}\right\rceil
\le m+1+L
\tag{7.5}
\]

packet-flag occurrences.  Hence \(\Omega(W)\) distinct packet support
necessarily uses \(\Omega(W/(m+1+L))=\Omega(B)\) original geodesic pieces,
and \(\Theta(B)\) is the minimum possible number of original pieces in this
packet architecture.  It is not a lower bound on the number of components
after a later fusion or rebundling.

The exact fifth-wave remaining target is therefore:

> Using all \(B\) complementary geodesics, or a \(\Theta(B)\) subfamily,
> choose or rebundle the disjoint productive packets of Theorem 3.1 so that
> their intersection with the prescribed selected deep targets has size
> \(\Omega(W)\), with the required rankwise distribution and trace geometry
> sufficient for \(\mathrm{PTAD}_A\).

This quoted statement is **unproved**.  The stronger tolerance
\(B-o(B/H)\) would be useful but is not forced by the capacity calculation
and is not claimed here.

This target is strictly downstream of the work completed here:

* the state walk is explicit;
* the arms are fused into productive updates;
* the component count is already \(o(W/H)\);
* reset cost is \(o(W)\) and asymptotically optimal;
* delayed legality is maximal;
* product-box occurrence incidence is optimal in order and degree;
* a positive density of upper-deep moves is present.

Only global cross-component rankwise support remains unproved.

---

## 8. Audit checklist

1. **Transition range.**  The half-geodesic transitions are
   \(0\le t<m\); the doubled walk lists states \(0\le t<2m\).  The formal
   state \(\Pi_{2m}\) repeats the middle owner but, when \(m-H\ge2\), not
   the fresh full state.  At \(m-H=1\), the states coincide.
2. **Core exchange.**  The update removes \(w_{t+H}\) from \(L_t\) and
   inserts \(w_{t+m}\); it does not remove \(w_t\).
3. **Literal length.**  The last initialization letter is \(L_0\) and is
   already the first middle-owner endpoint.  Therefore (1.11) and (3.1)
   have no extra seam letter.
4. **Productive guard.**  The interval \(2H\le t\le K_i-1-H\) loses exactly
   \(3H\) possible centers per component.
5. **One permutation.**  Every collision and target argument uses one
   common coordinate relabelling; no independence between endpoints is
   assumed.
6. **Occurrence versus support.**  Box-rainbow means distinct boxes inside
   one endpoint flag.  Relabelling does not destroy equalities between masks
   at different endpoints.  Equations (7.3)--(7.4) and the hole rotor make
   both the free-target and prescribed-target distinctions explicit.
7. **Depletion constants.**  The first initialization contributes
   \(2H+1\) excess and every depleted outgoing seam at least \(2H\), giving
   \(2HC+1\), not \((2H+1)C\), as the lower bound.
8. **No universality claim.**  The odd-factor word covers the complete first
   band \(m-1,m,m+1\) and its deeper canonical flags.  It is not claimed to
   cover every mask in the Gaussian band.  Neither \(\mathrm{PTAD}_A\) nor
   coefficient one is proved.
9. **Dummy completion.**  The last \(H\) departures in a finite path are
   chosen from the common intersection of its last \(H+1\) states.  No
   packet in (2.7) uses a dummy-dependent letter.
10. **Deep-tail state.**  Formula (5.3) is an identity for the union of the
    refined tail.  The demoted coordinate remains a physical singleton; it
    is not merged into a residual block.
11. **Gaussian constant.**  The exact ratio in (5.6a) gives
    \(e^{-A^2}\), with no missing factor two.  The ceiling in
    \(H=\lceil A\sqrt m\rceil\) is absorbed by \(A_0=A+1\).
12. **Component scope.**  The doubled-walk chaining in Section 4.1 proves
    sharpness of the bridge/reset constant only.  It does not construct a
    spanning owner-disjoint system.

### 8.1 Imported inputs and unproved remainder

The argument imports only the already-audited exact odd factor (including
its two-sided edge-colour partition), the greedy two-sided box-rainbow
portal, the dominant-plateau rank-\((m+1)\) count used in Section 3.2, the
exact MTF bridge metric, and the residual-depletion system inequalities.  It
does not import labelled common-owner synchronization, and all masks used by
the positive construction remain literal suffix ORs in one physical word.

The sole forward lemma is the prescribed cross-component deep-support/trace
statement quoted after (7.5); it is explicitly **unproved**.  Raw aggregate
support, product-box occurrence degree, and deep-arrival density are proved
here but are not substituted for that lemma.

### 8.2 Independent adversarial audit verdict

Three independent reconstructions were made after the first draft.

* The state audit rederived (1.6), (1.18), (2.6), the exact \(3H\) guard,
  (3.2), the \(3H-1\) depth-one omission, both reset ratios, (4.1), the
  bridge length (4.4), and the greedy forbidden count \(j+2\).  It found no
  factor-of-two or packet-count error.
* The obstruction audit rederived the two queue modes, the support ledger,
  the Gaussian constant, every hole-rotor support count, and the
  free-target versus selected-target capacity identity.  It corrected the
  odd-geodesic deep-arrival count from the weaker \((m-H)B\) to the exact
  \(mB\).
* A final end-to-end audit independently rederived both literal lengths,
  the \(6H/m\) and safe \(8H/m\) collision constants, the packet union and
  \(3H\) guard, the odd-factor anchor counts, the \(2HC+1\) depletion
  ledger, both reservoir modes, the \(e^{-A^2}\) forcing constant, the
  \(2H(m+H)+1\) hole-rotor support, and both target-capacity identities.  It
  returned a clean pass with no further factor, quantifier, or implication
  correction.

All audit corrections are incorporated above.  The audited verdict is:

\[
\boxed{\text{PASS, with the cross-component selected deep-support theorem
remaining unproved.}}
\]
