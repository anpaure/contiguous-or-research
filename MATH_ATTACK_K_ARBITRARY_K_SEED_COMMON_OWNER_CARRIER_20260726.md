# An arbitrary-\(k\) common-owner signed \(Q_2\) carrier

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

For every integer \(k\ge1\), there is an explicit common middle-owner
carrier \(\mathcal U_k\) and a Boolean family

\[
                         \{\mathscr F_\epsilon:
                         \epsilon\in\{0,1\}^k\}
\tag{0.1}
\]

of literal exact factors into physical \(Q_2\)'s such that:

1. every factor covers the same

   \[
                              |\mathcal U_k|=16(2k+1)
   \tag{0.2}
   \]

   owners exactly once;
2. relative to one fixed coordinate matching, the complete lower ledger is

   \[
   \boxed{
    L^-_\epsilon
    =16(k+|\epsilon|)f_0+
      16(k+1-|\epsilon|)f_1;}
   \tag{0.3}
   \]

3. the upper ledger is the identical shift

   \[
   \boxed{
    L^+_\epsilon
    =16(k+|\epsilon|)f_1+
      16(k+1-|\epsilon|)f_2;}
   \tag{0.4}
   \]

4. every bit has the exact background-independent drift

   \[
                         16(e_0-e_1)
   \quad\hbox{and}\quad 16(e_1-e_2);
   \tag{0.5}
   \]

5. all \(2^k\) factors possess one common \(\mathbb Z_4\) owner colouring
   and therefore suspend, on identical support, to

   \[
                         4(2k+1)
   \tag{0.6}
   \]

   physical \(C_{2h}\)'s for every \(h\ge2\).

In the all-new state \(\epsilon=\mathbf1\), the exact death density is

\[
                         \boxed{{k\over2k+1}.}
\tag{0.7}
\]

The source-high, death, survivor-high, and source-zero densities are

\[
 {k+1\over2k+1},\qquad
 {k\over2k+1},\qquad
 {1\over2k+1},\qquad
 {k\over2k+1}.
\tag{0.8}
\]

The \(k\) death bits are pointwise disjoint, so no inclusion--exclusion or
fractional interpretation is involved.

For \(k=3\), this gives a fully explicit \(112\)-owner, eight-corner
carrier with \(28\) physical \(Q_2\)'s per corner and all-new death
density \(3/7\).

The construction also packs at growing \(k\).  If

\[
                         k=k(m)\longrightarrow\infty,
 \qquad                   64^k=o(m^{1/3}),
\tag{0.9}
\]

then one may choose \(r=m^{2/3+o(1)}\) canonical eligible blocks, tensor
their factors, and obtain near-spanning exact \(C_{4r}\)-factors with
\(W/(4r)\) components.  A shallow product-transversal \(q\)-window sees
the exact decrement

\[
                         \operatorname{Bin}
                         \left(q,{k\over2k+1}\right).
\tag{0.10}
\]

At \(q=A\sqrt m+O(1)\), its centre differs from the exact uniform-target
centre by \(O_A(\sqrt m/k)=o(\sqrt m)\), and its extra variance is
\(O_A(\sqrt m)\), negligible on the ambient \(\Theta(m)\) variance
scale.  Thus the arbitrary-\(k\) carrier removes the Gaussian full-pair
type obstruction while the standard component collar is

\[
                         O(HW/r)=o(W).
\tag{0.11}
\]

This does not prove labelled target balance, full all-depth carrier
affinity, cross-packet collision control, or coefficient one.  It proves
the exact \(k\)-seed hypothesis, common phase, integrality, and the
simultaneous asymptotic pair-type law.

## 1. Coordinate blocks and the neutral contexts

For \(j=0,1,\ldots,k\), take a disjoint six-coordinate block

\[
                         B_j=
 \{a_j,b_j,c_j,d_j,e_j,f_j\}
\tag{1.1}
\]

with base pairs

\[
                         a_jb_j,\qquad c_jd_j,\qquad e_jf_j.
\tag{1.2}
\]

Put

\[
                         O_j=\{a_j,c_j,e_j\}.
\tag{1.3}
\]

Thus \(O_j\) splits all three base pairs.

For \(i=1,\ldots,k\), define four death states

\[
\begin{aligned}
D_i=\{&
a_ib_ie_i,\ a_ib_if_i,\\
&c_id_ie_i,\ c_id_if_i
\}
\end{aligned}
\tag{1.4}
\]

and four buffer states

\[
\begin{aligned}
Z_i=\{&
b_ic_ie_i,\ a_id_ie_i,\\
&b_ic_if_i,\ a_id_if_i
\}.
\end{aligned}
\tag{1.5}
\]

Every member of \(D_i\) contains exactly one full base pair.  Every member
of \(Z_i\) splits all three base pairs.  The neutral state \(O_i\) lies in
neither family.

For the survivor block \(B_0\), use only the four death states \(D_0\)
defined by the same formula (1.4).

Let

\[
                         C_i=\bigcup_{\substack{0\le j\le k\\j\ne i}}O_j.
\tag{1.6}
\]

The special-state components are

\[
 \mathcal S_i=\{C_i\cup X:X\in D_i\cup Z_i\},
 \qquad 1\le i\le k,
\tag{1.7}
\]

and

\[
                         \mathcal S_0=
 \{C_0\cup X:X\in D_0\}.
\tag{1.8}
\]

Every special state has rank \(3(k+1)\) on \(6(k+1)\) coordinates.

### Lemma 1.1 (component disjointness)

The \(k+1\) families

\[
                         \mathcal S_0,\mathcal S_1,\ldots,\mathcal S_k
\tag{1.9}
\]

are pairwise disjoint.

#### Proof

Suppose \(i\ne j\).  Every state in \(\mathcal S_j\) restricts to the
neutral state \(O_i\) in block \(B_i\).  Every state in
\(\mathcal S_i\) restricts in \(B_i\) to a member of
\(D_i\cup Z_i\) when \(i\ge1\), or to \(D_0\) when \(i=0\).
By construction none of these local states equals \(O_i\).  Thus no
global state lies in both components. \(\square\)

This use of neutral contexts is the only tagging mechanism.  Every
coordinate remains part of the same fixed pair frame.

## 2. The common middle carrier

Adjoin two common reservoir pairs

\[
                         R_1=\{u,v\},\qquad R_2=\{w,x\}
\tag{2.1}
\]

with their four split orientations

\[
                         \mathcal Y=\{uw,vw,vx,ux\}
\tag{2.2}
\]

and reservoir square

\[
                         Q_R=(uw,vw,vx,ux).
\tag{2.3}
\]

Define

\[
 \boxed{
 \mathcal U_k=
 \{S\cup Y:
 S\in\mathcal S_0\dot\cup\cdots\dot\cup\mathcal S_k,\quad
 Y\in\mathcal Y\}.}
\tag{2.4}
\]

The ambient coordinate set has size

\[
                         6(k+1)+4=6k+10,
\tag{2.5}
\]

while every owner has rank

\[
                         3(k+1)+2=3k+5={6k+10\over2}.
\tag{2.6}
\]

Thus \(\mathcal U_k\) lies literally in the middle layer of its ambient
cube.  Lemma 1.1 and (2.2) give

\[
 |\mathcal U_k|
 =4\left(4+8k\right)
 =16(2k+1),
\tag{2.7}
\]

proving (0.2).

## 3. The old and new local resolutions

Fix \(1\le i\le k\).  On the seed component

\[
                         (\mathcal S_i\times\mathcal Y)
\tag{3.1}
\]

there are two exact resolutions.

The old resolution is all vertical:

\[
 \mathscr A_i^0=
 \{(C_i\cup X)\cup Q_R:X\in D_i\cup Z_i\}.
\tag{3.2}
\]

It consists of eight reservoir \(Q_2\)'s.

The new resolution has, for each \(t\in\{e_i,f_i\}\), the special square

\[
 Q_{i,t}=
 (a_ib_it,\ b_ic_it,\ c_id_it,\ a_id_it).
\tag{3.3}
\]

At every fixed reservoir orientation \(Y\), take

\[
                         (C_i\cup Q_{i,t})\cup Y.
\tag{3.4}
\]

Thus

\[
 \mathscr A_i^1=
 \{(C_i\cup Q_{i,t})\cup Y:
 t\in\{e_i,f_i\},\ Y\in\mathcal Y\}.
\tag{3.5}
\]

It also consists of eight \(Q_2\)'s.

### Lemma 3.1 (one exact seed)

Both \(\mathscr A_i^0\) and \(\mathscr A_i^1\) partition the identical
32-owner component \(\mathcal S_i\times\mathcal Y\).

#### Proof

The old resolution is immediate.  The two special squares in (3.3)
are disjoint: one uses the four local states with \(e_i\), the other the
four with \(f_i\).  Together they cover

\[
                         D_i\dot\cup Z_i.
\]

Repeating them at the four fixed reservoir orientations covers all
\(8\cdot4=32\) owners once.  Consecutive states in (3.3) use the two
disjoint swaps \(a_i\leftrightarrow c_i\) and
\(b_i\leftrightarrow d_i\), so every cell is a physical Johnson
\(Q_2\). \(\square\)

On the survivor component use the fixed vertical resolution

\[
                         \mathscr A_0=
 \{(C_0\cup X)\cup Q_R:X\in D_0\}.
\tag{3.6}
\]

It consists of four \(Q_2\)'s.

For \(\epsilon=(\epsilon_1,\ldots,\epsilon_k)\in\{0,1\}^k\), define

\[
 \boxed{
 \mathscr F_\epsilon=
 \mathscr A_0\mathbin{\dot\cup}
 \mathop{\dot\bigcup}_{i=1}^k\mathscr A_i^{\epsilon_i}.}
\tag{3.7}
\]

### Theorem 3.2 (the arbitrary-\(k\) exact factor cube)

Every \(\mathscr F_\epsilon\) is a partition of \(\mathcal U_k\) into

\[
                         4+8k=4(2k+1)
\tag{3.8}
\]

physical \(Q_2\)'s.  Hence (3.7) gives \(2^k\) literal exact factor
corners on one common owner support.

#### Proof

The carrier components are disjoint by Lemma 1.1.  Lemma 3.1 gives two
exact resolutions of every seed component, and (3.6) resolves the
survivor component.  Their disjoint union proves exact one-copy ownership
for every bit vector. \(\square\)

## 4. Exact lower and upper ledgers

Use the base matching consisting of all pairs in (1.2) and the two
reservoir pairs (2.1).  Every neutral context \(C_i\) splits all its base
pairs.

In an old vertical cell over \(D_i\), every lower edge retains the one
full local pair, so its four occurrences have type one.  In an old
vertical cell over \(Z_i\), every lower edge has type zero.  Therefore one
old seed component has ledger

\[
                         16f_0+16f_1.
\tag{4.1}
\]

Every lower special edge in (3.3) has type zero.  Its local intersection
is one of

\[
                         b_it,\quad c_it,\quad d_it,\quad a_it,
\tag{4.2}
\]

and none is a base pair.  Hence the new seed component has ledger

\[
                         32f_0.
\tag{4.3}
\]

The survivor component contributes

\[
                         16f_1.
\tag{4.4}
\]

Summing (4.1)--(4.4) proves the lower formula (0.3).

For upper edges, an old vertical cell fills one reservoir pair.  It
therefore has type one over \(Z_i\) and type two over \(D_i\).  In a new
special cell, the local unions are

\[
 a_ib_ic_it,\quad
 b_ic_id_it,\quad
 a_ic_id_it,\quad
 a_ib_id_it.
\tag{4.5}
\]

Each contains exactly one full local base pair, while the fixed reservoir
orientation remains split.  Thus the old and new seed upper ledgers are

\[
                         16f_1+16f_2,
 \qquad                   32f_1,
\tag{4.6}
\]

and the survivor contributes \(16f_2\).  This proves (0.4).

In particular every bit has exactly the signed drift (0.5), independently
of every other bit and of an arbitrary frozen exterior core.

## 5. Pointwise categories

Index each lower edge occurrence by its base owner and the oriented
factor edge selected there.  Give the old and new special squares the
orientations in (3.3).  On seed component \(i\), the exact type identity is

\[
 f_\epsilon(S,Y)
 =f_{\mathbf0}(S,Y)
  -\epsilon_i\mathbf1_{\{S|_{B_i}\in D_i\}}.
\tag{5.1}
\]

The death indicators for different \(i\)'s have disjoint owner supports,
because the components \(\mathcal S_i\) are disjoint.  Under the uniform
owner law on \(\mathcal U_k\), every death class has size \(16\), the
survivor-high class has size \(16\), and the union of all buffer-zero
classes has size \(16k\).  This proves (0.8).

At \(\epsilon=\mathbf1\), (5.1) is a
\(\operatorname{Bernoulli}(k/(2k+1))\) decrement.  No owner is counted
twice.

## 6. Common phase and all-length suspension

Order the reservoir orientations as

\[
                         y_0=uw,\quad y_1=vw,\quad
                         y_2=vx,\quad y_3=ux.
\tag{6.1}
\]

Define \(g\) on every special carrier state as follows.

* On the four states of each square \(C_i\cup Q_{i,t}\), assign
  \(0,1,2,3\) in its displayed cyclic order.
* On the four survivor states, assign any values.

This is well-defined: the two squares for one seed are disjoint, different
seed components are disjoint, and the survivor component is disjoint from
all seeds.

Colour owners by

\[
                         c(S\cup y_j)=g(S)+j\pmod4.
\tag{6.2}
\]

On every vertical reservoir square, the colours are cyclic
\(0,1,2,3\).  On every special square at fixed \(y_j\), they are the
assigned cyclic colours shifted by \(j\).  Thus:

### Lemma 6.1 (simultaneous phase compatibility)

The same owner colouring \(c\) is phase-compatible with every cell in
every one of the \(2^k\) factors \(\mathscr F_\epsilon\).

Adjoin \(h-2\) fresh split coordinate pairs.  Replace every coloured
square with the standard cycle having direction word

\[
 \alpha,\beta,e_1,\ldots,e_{h-2},
 \alpha,\beta,e_1,\ldots,e_{h-2}.
\tag{6.3}
\]

The lifted tail fibre above an owner depends only on its common colour.
Consequently:

### Theorem 6.2 (common-support all-length \(k\)-seed suspension)

For every \(h\ge2\), all \(2^k\) factors lift to exact factors of one
identical owner support.  Every lifted factor consists of exactly

\[
                         4(2k+1)
\tag{6.4}
\]

pairwise disjoint physical isometric \(C_{2h}\)'s.

## 7. Canonical global packing

Let

\[
                         n_k=6k+10,\qquad
                         p_k={16(2k+1)\over2^{6k+10}}
                             ={2k+1\over2^{6k+6}}.
\tag{7.1}
\]

Partition as many ordinary coordinates as possible into labelled
\(n_k\)-blocks carrying \(\mathcal U_k\).  Let

\[
                         B=\left\lfloor {2m\over n_k}\right\rfloor.
\tag{7.2}
\]

Call a block eligible when its restriction belongs to \(\mathcal U_k\).
Before conditioning on total rank, the eligible count is
\(\operatorname{Bin}(B,p_k)\).

For every owner with at least \(r\) eligible blocks, choose its first
\(r\), freeze the exterior, and vary the selected restrictions over

\[
                         \mathcal U_k^r.
\tag{7.3}
\]

The first-\(r\) list is stable because every varied selected block remains
in \(\mathcal U_k\), while every unselected block is frozen.  Hence the
sets (7.3) form disjoint canonical packets.

### Theorem 7.1 (near-spanning \(k\)-seed tensor)

If

\[
                              r\le {Bp_k\over2},
\tag{7.4}
\]

and \(G\) is the number of retained owners, then

\[
 {W-G\over W}
 \le 2(m+1)\exp\left(-{Bp_k\over8}\right).
\tag{7.5}
\]

Every packet has \(2^{kr}\) exact resolutions.  Each resolution partitions
the packet into

\[
                         [\,4(2k+1)\,]^r
\tag{7.6}
\]

physical \(Q_{2r}\)'s.  If \(2r\) is a power of two, applying the Hamming
syndrome factor gives a literal exact \(C_{4r}\)-factor with

\[
                              {G\over4r}
\tag{7.7}
\]

components.

#### Proof

The half-mean Chernoff bound gives
\(\Pr(Z<Bp_k/2)\le e^{-Bp_k/8}\).  Conditioning fair bits on rank \(m\)
costs at most \(2(m+1)\), proving (7.5).  Selector stability gives the
packet partition.  Theorem 3.2 and Cartesian products give (7.6), and
the Hamming factor gives (7.7). \(\square\)

For fixed \(k\), \(Bp_k=\Theta_k(m)\), so every
\(r=o(m)\) is eventually available and the leave is
\(e^{-\Omega_k(m)}W\).

For growing \(k\),

\[
                         Bp_k=\Theta\left({m\over64^k}\right).
\tag{7.8}
\]

Thus \(r=m^{2/3+o(1)}\) is available whenever
\(64^k=o(m^{1/3})\), proving the packing assertion in (0.9).

## 8. Gaussian pair-type action

There is a phase issue which must be removed before tensoring.  Merely
knowing the uniform-owner density in Section 5 is not enough: a Hamming
phase could in principle correlate with the parity class of the two
opposite death vertices of a special square.  The following balanced
cell charts remove that correlation pointwise.

On every all-new cell with \(t=e_i\), identify the displayed cyclic order
with

\[
                         00,10,11,01.
\tag{8.1}
\]

Its two death vertices then have even cube parity.  On every all-new cell
with \(t=f_i\), rotate the chart once, identifying

\[
 (b_ic_if_i,c_id_if_i,a_id_if_i,a_ib_if_i)
 \quad\hbox{with}\quad
                         (00,10,11,01).
\tag{8.2}
\]

Its two death vertices then have odd cube parity.  The four reservoir
orientations give four cells of each chart type.  Consequently, for every
fixed abstract vertex \(z\in Q_2\), exactly four of the eight cells of
seed \(i\) declare \(z\) a death vertex.  Among all
\(8k+4=4(2k+1)\) all-new cells, exactly \(4k\) declare it a death vertex.
Thus

\[
 \Pr(\text{death}\mid z)
 ={4k\over8k+4}={k\over2k+1},
 \qquad z\in Q_2.
\tag{8.3}
\]

This is stronger than the unconditional owner count in Section 5.  The
old vertical cells may similarly be charted by the reservoir order
\(y_0,y_1,y_2,y_3=00,10,11,01\).  Consequently the phasewise census holds
at every Boolean corner, not only at the all-new corner.  If
\(s=|\epsilon|\), then at every fixed abstract vertex there are

\[
 4s\ \text{death cells},\qquad
 4(k-s+1)\ \text{lower-survivor cells},
\tag{8.3a}
\]

among the \(4(2k+1)\) cells.  Moreover the upper birth indicator is
pointwise the complement of the lower death indicator: old vertical
cells and survivor cells always birth, while a new special cell births
exactly at a buffer vertex.  Hence a corner of weight \(s\) has the exact
conditional rates

\[
 p_s^-={s\over2k+1},
 \qquad p_s^+=1-p_s^-={2k+1-s\over2k+1}.
\tag{8.3b}
\]

Thus independently choosing corner weights \(s_j\) in distinct tensor
blocks realizes the exact phase-robust Poisson-binomial lower operator
with parameters \(s_j/(2k+1)\), and the complementary upper operator.
The all-new choice is \(s_j=k\) throughout.

The chosen charts give the exact product bijection

\[
 \mathcal U_k^r
 \cong
 \{1,\ldots,4(2k+1)\}^{,r}\times Q_{2r},
\tag{8.4}
\]

where the first coordinate records the local factor cell.  Use the same
Hamming cycle factor on the abstract \(Q_{2r}\) in every product cell.
After permuting its coordinate axes, its cyclic direction order is

\[
 \alpha_1,\ldots,\alpha_r,
 \beta_1,\ldots,\beta_r,
 \alpha_1,\ldots,\alpha_r,
 \beta_1,\ldots,\beta_r.
\tag{8.5}
\]

Every cyclic window of at most \(r\) directions meets each local carrier
block at most once.  Conditional on an arbitrary abstract cube vertex,
on its Hamming component and phase, and hence on the exact set of touched
blocks, the local cell identities remain independent and uniform in
(8.4).  Equation (8.3) therefore gives the exact conditional law

\[
                         D_q\sim
\operatorname{Bin}\left(q,{k\over2k+1}\right)
\qquad(q\le r).
\tag{8.6}
\]

No phase-independence assumption is hidden here.  Choose the all-new
state in every block.  For every \(q\le\min\{r,A\sqrt m\}\), the lower
pair type after the window is the source pair type minus \(D_q\), because
each touched block is used only once.

The full one-dimensional birth--death operator is also exact.  At every
fixed local cube vertex, the all-new cells have the three phasewise
categories

\[
\begin{array}{c|ccc}
 &\text{source type}&\text{lower type}&\text{upper type}\\ \hline
\text{buffer}&0&0&1\\
\text{death}&1&0&1\\
\text{survivor}&1&1&2
\end{array}
\]

with respective multiplicities \(4k,4k,4\).  Consequently the exact
joint local probability-generating polynomial is

\[
 \boxed{
 \Xi_k(x,y,z)
 ={kz+kxz+xyz^2\over2k+1}.}
\tag{8.6a}
\]

The \(q\) touched blocks contribute \(\Xi_k^q\), conditional on every
exterior, component and Hamming phase.  If \(R\) is the number of full
pairs outside the touched blocks, their joint generating function is

\[
 \mathbb E\bigl[(xyz)^R\bigr]\,\Xi_k(x,y,z)^q.
\tag{8.6b}
\]

In particular, writing \(\mathcal R_{m,q}(u)=\mathbb E u^R\), the three
marginal generating functions are

\[
\begin{aligned}
 \mathcal P_{\rm src}(u)
 &=\mathcal R_{m,q}(u)
   \left({k+(k+1)u\over2k+1}\right)^q,\\
 \mathcal P_-(u)
 &=\mathcal R_{m,q}(u)
   \left({2k+u\over2k+1}\right)^q,\\
 \mathcal P_+(u)
 &=u^q\mathcal P_-(u).
\end{aligned}
\tag{8.6c}
\]

Equivalently, on every compatible packet-sector source polynomial, the
exact lower operator is

\[
 \mathcal T^-_{k,q}:
 \mathcal P_{\rm src}(u)\longmapsto
 \mathcal P_{\rm src}(u)
 \left({2k+u\over k+(k+1)u}\right)^q,
\tag{8.6d}
\]

and the upper operator is \(u^q\mathcal T^-_{k,q}\).  The ratio in
(8.6d) is asserted only on the compatible sector, where the displayed
source factor divides exactly; it is not a Markov kernel on arbitrary
formal input laws.  Formula (8.6b), rather than the ratio, is the literal
positive realization.

The mean and variance are

\[
 \mathbb ED_q
 ={qk\over2k+1}
 ={q\over2}-{q\over2(2k+1)},
\tag{8.7}
\]

\[
 \operatorname{Var}D_q
 ={qk(k+1)\over(2k+1)^2}=O(q).
\tag{8.8}
\]

Conditional on the infinity bit, the exact target centre displacement is

\[
 \Delta_{\varepsilon,q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}
 ={q\over2}+O_A(1).
\tag{8.9}
\]

At \(q=A\sqrt m+O(1)\), equations (8.7)--(8.9) give centre error

\[
                         O_A\left({\sqrt m\over k}+1\right).
\tag{8.10}
\]

For completeness, let \(F_m\) be the source full-pair count of a uniformly
chosen retained owner, conditional on its infinity bit, and let
\(F^{\rm out}_{m,q}\) be its output type.  The leave estimate (7.5)
puts the law of \(F_m\) at vanishing total-variation distance from the
uniform middle-layer law.  Hence

\[
 {F_m-\mathbb EF_m\over\sqrt m}
 \Longrightarrow N(0,1/16).
\tag{8.11}
\]

Pointwise additivity and (8.6) give

\[
 F^{\rm out}_{m,q}=F_m-D_q,
 \qquad
 {D_q-\mathbb ED_q\over\sqrt m}\longrightarrow0
 \quad\hbox{in probability},
\tag{8.12}
\]

where the second assertion follows from (8.8), without any independence
from \(F_m\).  The uniform rank-\((m-q)\) target has the same limiting
variance \(1/16\), and (8.10) is \(o(\sqrt m)\) when \(k\to\infty\).
Slutsky's theorem therefore proves that the normalized output pair-type
law and the normalized uniform-target pair-type law have the same
Gaussian limit.

The upper law is simultaneous and equally explicit.  At a special
vertex, the upper edge creates one new full pair exactly on the buffer
vertices, namely when the lower edge does not kill a full pair.  At a
survivor vertex the lower death is zero and the vertical upper edge fills
one reservoir pair.  Hence, pointwise on every touched block,

\[
                         B=1-D,
\tag{8.13}
\]

where \(B\) is the source-to-upper birth indicator and \(D\) is the lower
death indicator.  The balanced charts therefore give

\[
 B_q=q-D_q\sim
 \operatorname{Bin}\left(q,{k+1\over2k+1}\right).
\tag{8.14}
\]

The exact uniform upper-target centre displacement, conditional on the
frozen infinity bit, is

\[
 \Delta^+_{\varepsilon,q}
 ={q(2m-2\varepsilon+q-1)\over2(2m-1)}
 ={q\over2}+O_A(1).
\tag{8.15}
\]

Since

\[
 \mathbb EB_q
 ={q\over2}+{q\over2(2k+1)},
 \qquad \operatorname{Var}B_q=O(q),
\tag{8.16}
\]

the identical Slutsky argument gives the uniform upper-target Gaussian
limit.  Thus the leading lower and upper pair-type laws are obtained
simultaneously, with their exact local anticorrelation retained.

This is a Gaussian type-law theorem, not an exact finite equality of the
full orbit laws.  The constant death rate in (8.3) is not the exact
state-dependent nested deletion rate \(2f/(m-q)\).  Their difference is
invisible in the leading Gaussian limit when \(k\to\infty\), but must
still be handled for exact labelled quotas.

## 9. Component and collar scale

Choose a power-of-two \(2r\) with

\[
                         r=m^{2/3+o(1)}
\tag{9.1}
\]

under the availability condition \(64^k=o(m^{1/3})\).  The exact global
factor has \(G/(4r)\) components.  Through
\(H=A\sqrt m+O(1)\), the standard certified collar is

\[
                         O\left({HW\over r}\right)
 =O_A(Wm^{-1/6+o(1)})=o(W).
\tag{9.2}
\]

Unlike the fixed-radius-\(t\) Hamming architecture, the all-new row uses
\(kr\) signed seed bits across \(r\) carrier blocks.  Its induced pair
frame changes on at most one seed component in each block, so its actual
matching-switch radius is at most \(r\), not \(kr\).  This is still not
confined to an \(O(\sqrt m)\)-radius matching ball when \(r\gg\sqrt m\).
Thus the earlier action-density ceiling does not contradict (8.6).

## 10. Exact boundary

Proved:

1. an explicit arbitrary-\(k\) common owner carrier;
2. \(2^k\) literal exact \(Q_2\)-factor corners;
3. exact lower and upper affine bit ledgers;
4. all-new death density \(k/(2k+1)\);
5. one common \(\mathbb Z_4\) phase and all-length suspension;
6. canonical near-spanning tensor packing, including growing \(k\);
7. simultaneous disappearance of the Gaussian pair-type mean and variance
   obstruction for \(k\to\infty\); and
8. an \(o(W)\) certified component collar at \(r\gg\sqrt m\).

Not proved:

* complete labelled lower/upper target balance;
* exact finite transport of every \((\varepsilon,f)\)-orbit law;
* removal of the finite joint rigidity
  \(\mathcal P_+(u)=u^q\mathcal P_-(u)\);
* full-depth affine carrier vectors for the \(2^k\) corners;
* cross-packet shadow collision control;
* literal odd-wreath completion of the exponentially small leave; or
* coefficient one.

The \(k\)-seed completion, phase, density, and Gaussian type gates are
therefore positive.  The surviving work is the occurrence-resolved
all-depth and labelled collision problem, not local factor ownership.
