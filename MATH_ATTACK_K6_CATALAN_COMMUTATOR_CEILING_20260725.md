# Lane K: positive-density Catalan packet rebundling and its Gaussian-window ceiling

Date: 2026-07-25

Method: pure mathematics only. No finite search, computation, solver, or web input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad B=\frac Wn=\operatorname{Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. Let \(F_m\) be the canonical MSW exact wreath factor.

This report proves a positive-density exact rebundling theorem and, at the same time,
an exact obstruction to obtaining the coefficient-one theorem from that rebundling.

For every Dyck prefix \(P\in\mathcal D_s\) and suffix
\(R\in\mathcal D_{m-s-2}\), the two canonical rows

\[
 P1100R,\qquad P1010R                                      \tag{0.1}
\]

form a whole size-two ownership component for the transposition

\[
 \tau_s=(2s+2\ \ 2s+3).                                   \tag{0.2}
\]

Let \(\mathfrak M_m\) be the graph on \(\mathcal D_m\) consisting of all
these packet edges. The exact maximum matching of this graph is

\[
 \boxed{
 \nu(\mathfrak M_m)=\frac{\operatorname{Cat}_m-O_m}{2},
 }
                                                                  \tag{0.3}
\]

where

\[
 \boxed{
 \sum_{m\ge0}O_mz^m
 =\frac{1+z}{1+z+2z^2-(1+z)zC(z)},
 \qquad C(z)=\sum_{m\ge0}\operatorname{Cat}_mz^m.
 }
                                                                  \tag{0.4}
\]

Moreover,

\[
 \frac{O_m}{\operatorname{Cat}_m}\longrightarrow\frac{25}{36},
 \qquad
 \boxed{
 \nu(\mathfrak M_m)
 =\left(\frac{11}{72}+o(1)\right)B.
 }
                                                                  \tag{0.5}
\]

The matching packets are owner-disjoint. They remain components after any other
matching packets have been switched, so all their \(2^{\nu(\mathfrak M_m)}\)
side choices are literal integral exact wreath factors. Switching all matched
packets replaces

\[
 \boxed{
 2\nu(\mathfrak M_m)
 =\left(\frac{11}{36}+o(1)\right)B
 }
                                                                  \tag{0.6}
\]

canonical wreaths and reassigns the same fraction of all \(W\) middle owners.
Thus positive-density persistent rebundling is genuinely possible.

The obstruction is that every packet in (0.1) is shadow-small at **every**
rank. If \(z\) is its signed two-for-two exchange and \(B_rz\) is its
rank-\(r\) cyclic-interval histogram, then

\[
 \boxed{
 \begin{array}{c|c|c}
 r&|\operatorname{supp}B_rz|&\|B_rz\|_1\\ \hline
 1,m&0&0\\
 2\le r\le m-2&8&8\\
 m-1&4&4.
 \end{array}}
                                                                  \tag{0.7}
\]

The upper-rank statement is the complementary copy of (0.7). In particular,
one packet has half-\(\ell^1\) action \(2\) at depth one and \(4\) at every
depth \(2\le q\le H\).

Let \(O_q(F)\) be balanced overflow at rank \(m-q\), let

\[
 c_q=\left\lfloor
 \frac{W}{\binom n{m-q}}
 \right\rfloor,
 \qquad
 J_A(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q},             \tag{0.8}
\]

and put

\[
 S_A(m)=\sum_{q=1}^{H}\frac1{c_q},
 \qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
                                                                  \tag{0.9}
\]

Then

\[
 S_A(m)=(\kappa_A+o(1))\sqrt m,                     \tag{0.10}
\]

and the entire maximum-matching cube has diameter

\[
 \boxed{
 \operatorname{diam}J_A
 \le \nu(\mathfrak M_m)(4S_A-2)
 =\left(\frac{11\kappa_A}{18}+o(1)\right)B\sqrt m
 =O_A\!\left(\frac W{\sqrt m}\right)=o(W).
 }
                                                                  \tag{0.11}
\]

At depth one the conclusion is even more direct: all packet choices together can
fill at most \(2\nu(\mathfrak M_m)=O(B)=o(W)\) old holes. Under the frozen
premise

\[
 M_1(F_m)\ge\delta W                                      \tag{0.12}
\]

for some fixed \(\delta>0\), every factor in this positive-density cube still has

\[
 \boxed{M_1\ge(\delta-o(1))W.}                         \tag{0.13}
\]

Whole-factor coordinate preparations do not amplify the cube. Any word made from
global relabellings and toggles of the currently transported matching packets has
the exact normal form

\[
 \boxed{gF_\varepsilon}                                  \tag{0.14}
\]

for one final coordinate permutation \(g\) and one native packet-sign vector
\(\varepsilon\). Hence every such nonlocal commutator has the same ceiling
(0.11), and a closed relabelling commutator ends inside the native cube.

This rigorously closes the following architecture:

> choose a positive-density root-disjoint family of canonical contextual
> size-two MSW packets, interleave their switches with arbitrary whole-factor
> coordinate relabellings, and use the resulting commutators to balance a fixed
> Gaussian window.

It cannot repair even the first shadow. More generally, any path whose every
round consists of root-disjoint universal aligned four-letter packets requires

\[
 \boxed{(\delta-o(1))n}                                \tag{0.15}
\]

rounds before it can reduce \(\delta W\) first-shadow holes to \(o(W)\). The
all-band weighted ledger independently gives the weaker but premise-flexible lower
bound \((\delta/\kappa_A+o(1))\sqrt m\).

The theorem does **not** rule out a genuinely overlapping, state-dependent
recomputation which leaves this aligned packet atlas and produces large nonlocal
components. A further theorem below does force a bridge colour with

\[
 E_\rho\ge(25/144-o(1))W
 \quad\text{coarse packet-cell edges},\qquad
 |Z_\rho|\ge(25/72-o(1))B
 \tag{0.16}
\]

fresh owners in components meeting several cells. This is a positive-density
fragmentation-or-large-component alternative. Its audited limitation is essential:
the count can be supported entirely on unmatched singleton cells, where the
preparatory gauge is the identity. It is therefore not positive-density
side-mismatch seam dispersion and gives no lower-shadow sign. For the explicit
side-mismatch seams, the existing direct degree count still forces only
\(\Omega(B/n)\) owner mass; coordinate noncommutation would not improve that
counting implication by itself. Nor does the MSW packet matching automatically
transfer to the canonical PBBS factor.

There is nevertheless one new PBBS theorem. The initial canonical PBBS 2-factor
contains

\[
 n\bigl(\operatorname{Cat}_{m-1}-2^{m-2}\bigr)
 =\left(\frac14-o(1)\right)W                         \tag{0.17}
\]

explicit clean alternating \(C_8\)'s, including a vertex-disjoint subfamily of
size \((1/256-o(1))B\). This closes the formerly open clean-cycle **supply**
gate. It does not close the balance gate: the switches are ordinary integral
2-factor switches, not yet componentwise point-regular or exact-wreath
rebundlings.

## 1. Exact packet graph

Every Dyck word has a unique factorization into primitive Dyck words. Write

\[
 A=10,\qquad D=1100.                                    \tag{1.1}
\]

The partner \(1010\) in (0.1) is \(AA\). Thus an edge of
\(\mathfrak M_m\) replaces one primitive factor \(D\) by the two primitive
factors \(AA\), or conversely. No substring interpretation is intended: \(D\)
and \(A\) are factors in the unique primitive decomposition.

The shifted MSW component theorem gives more than a signed relation. For each
presentation

\[
 PDR\longleftrightarrow PAAR,                            \tag{1.2}
\]

the two rows on the left form one complete ownership component between \(F_m\)
and \(\tau_sF_m\), where \(s\) is the semilength of \(P\). Therefore either side
of (1.2) partitions exactly the same packet of middle masks. The move is a legal
integral exact-factor move. At the odd-graph 2-factor level it is the universal
balanced profile-three alternating \(C_8\); the all-dimensional supply proved
below is, however, specific to the canonical MSW rows.

### 1.1 Expansion fibers

Expand every primitive \(D\) in a Dyck word to \(AA\). This expansion is
invariant along every edge of \(\mathfrak M_m\). Its image is a Dyck word whose
primitive factorization contains no \(D\).

Fix one expanded image. Its maximal runs of \(A\)'s have lengths
\(\ell_1,\ldots,\ell_t\). Inside a run of length \(\ell\), a preimage is exactly
a tiling of an interval of length \(\ell\) by monomers \(A\) and dimers \(D\).
Let \(T_\ell\) be the graph of these tilings, adjacent when one \(D\) is toggled
with \(AA\). The expansion fiber is exactly

\[
 T_{\ell_1}\square\cdots\square T_{\ell_t}.              \tag{1.3}
\]

Indeed, every packet toggle acts in one run. Conversely, toggling every dimer to
two monomers connects every tiling to the all-\(A\) tiling, so (1.3) is connected.
Thus the expansion fibers are exactly the connected components of
\(\mathfrak M_m\).

## 2. Maximum matching inside a fiber

### Lemma 2.1 (one-run matching)

The tiling graph \(T_\ell\) has a perfect matching if
\(\ell\equiv2\pmod3\), and otherwise has a maximum matching leaving exactly one
vertex unmatched.

#### Proof

For \(\ell\ge2\), pair

\[
 DQ\longleftrightarrow AAQ
 \qquad(Q\in T_{\ell-2}).                              \tag{2.1}
\]

This matches every tiling beginning in \(D\) and every tiling beginning in
\(AA\). The only remaining tilings begin in \(AD\), and their residual graph is
the copy

\[
 AD\,T_{\ell-3}.                                       \tag{2.2}
\]

Recurse on (2.2). The bases \(T_0,T_1\) each leave one vertex, while \(T_2\)
has the perfect edge \(D\leftrightarrow AA\). Hence the construction is perfect
for \(\ell\equiv2\pmod3\) and leaves one vertex otherwise.

For maximality, \(|T_\ell|\) obeys

\[
 f_0=f_1=1,\qquad f_\ell=f_{\ell-1}+f_{\ell-2}.          \tag{2.3}
\]

Modulo two this sequence has period three, so \(f_\ell\) is even exactly when
\(\ell\equiv2\pmod3\). Parity forbids a perfect matching in the other two
classes. The constructed matching is therefore maximum. \(\square\)

### Lemma 2.2 (product matching)

A fiber (1.3) has a perfect matching if at least one \(\ell_i\) is
\(2\pmod3\). If every \(\ell_i\) is \(0\) or \(1\pmod3\), it has a maximum
matching leaving exactly one vertex.

#### Proof

Use the matching of Lemma 2.1 in the first coordinate. If it is perfect, it
matches the whole Cartesian product. If it leaves one vertex in every slice,
match those leftover vertices along the second coordinate, and continue.
This gives a perfect product matching as soon as one factor matching is perfect,
and otherwise leaves one product vertex.

The product order is even in the first case and odd in the second. Hence parity
again proves maximality. \(\square\)

## 3. Enumeration of odd fibers

Let \(O_m\) be the number of expansion fibers of odd order. By Lemma 2.2 these
are precisely the \(D\)-free primitive-factor strings in which every maximal
\(A\)-run has length \(0\) or \(1\pmod3\).

The generating function of all primitive Dyck words is \(zC(z)\). After removing
\(A\), of weight one, and \(D\), of weight two, the rigid primitive factors have
generating function

\[
 R(z)=zC(z)-z-z^2.                                     \tag{3.1}
\]

An allowed \(A\)-run has generating function

\[
 L(z)=\sum_{\ell\not\equiv2\ (3)}z^\ell
 =\frac{1+z}{1-z^3}.                                   \tag{3.2}
\]

The unique run/rigid decomposition is

\[
 \text{run}\,(\text{rigid}\ \text{run})^*.
\]

Therefore

\[
\begin{aligned}
 O(z)
 &=\sum_{m\ge0}O_mz^m
   =\frac{L(z)}{1-R(z)L(z)}\\
 &=\boxed{
 \frac{1+z}{1+z+2z^2-(1+z)zC(z)}.}                    \tag{3.3}
\end{aligned}
\]

Each even fiber contributes half its vertices to a matching and each odd fiber
contributes half minus one half. Since the fibers partition all
\(\operatorname{Cat}_m\) vertices, Lemma 2.2 proves the exact formula

\[
 \nu(\mathfrak M_m)=\sum_{\text{fibers }K}
 \left\lfloor\frac{|K|}{2}\right\rfloor
 =\frac{\operatorname{Cat}_m-O_m}{2}.                  \tag{3.4}
\]

### 3.1 Singularity and the constant \(11/72\)

Put

\[
 u=\sqrt{1-4z}.
\]

The Catalan identities give

\[
 zC(z)=\frac{1-u}{2},\qquad z=\frac{1-u^2}{4}.          \tag{3.5}
\]

Substitution in (3.3) yields

\[
 O(z)=\frac53-\frac{25}{18}u+O(u^2),                  \tag{3.6}
\]

whereas

\[
 C(z)=2-2u+O(u^2).                                     \tag{3.7}
\]

There is no hidden pole of \(O(z)\) in \(|z|\le1/4\). Indeed \(R,L\) have
nonnegative coefficients and

\[
 R(1/4)L(1/4)=\frac5{21}<1.                            \tag{3.8}
\]

Square-root coefficient extraction from (3.6)--(3.7) therefore gives

\[
 \frac{O_m}{\operatorname{Cat}_m}\longrightarrow
 \frac{25/18}{2}=\frac{25}{36}.                       \tag{3.9}
\]

Equations (3.4) and (3.9) prove

\[
 \nu(\mathfrak M_m)
 =\left(\frac{11}{72}+o(1)\right)B.                   \tag{3.10}
\]

## 4. Exact persistence and literal integrality

For a component packet \(K\), let \(U_K\) be the disjoint union of the middle
masks owned by its rows. If \(K\) is a component for \(\tau\), then

\[
 \tau U_K=U_K,                                         \tag{4.1}
\]

and both \(K\) and \(\tau K\) partition \(U_K\).

### Lemma 4.1 (heterogeneous packet cube)

Let \((\tau_i,K_i)\), \(1\le i\le L\), be component packets of one exact
factor whose owner sets are pairwise disjoint. Then for every
\(\varepsilon\in\{0,1\}^L\),

\[
 F_\varepsilon
 =\left(F\setminus\bigcup_iK_i\right)
   \cup\bigcup_i\tau_i^{\varepsilon_i}K_i              \tag{4.2}
\]

is an integral exact factor. After any subfamily has been toggled, every
untoggled packet is still exactly a component of its freshly recomputed
transposition overlay.

#### Proof

Distinct rows of an exact factor own disjoint middle blocks. Hence the root
packets \(U_{K_i}\) are disjoint. On each \(U_{K_i}\), either \(K_i\) or
\(\tau_iK_i\) is a row partition; outside their union the original rows remain.
This proves exactness of (4.2).

Toggling packets other than \(K_j\) changes no row on \(U_{K_j}\). Because
\(U_{K_j}\) is \(\tau_j\)-invariant, no fresh \(\tau_j\)-ownership edge can enter
or leave that root packet. Its internal connected owner graph is unchanged.
Thus it remains one whole component. \(\square\)

A graph matching in \(\mathfrak M_m\) is owner-disjoint, so Lemma 4.1 applies.
Switching all matching packets changes \(2\nu(\mathfrak M_m)\) rows. Each row
owns \(n\) middle masks and the packets are root-disjoint, so the fraction of all
middle owners whose grouping is reassigned is

\[
 \frac{2n\nu(\mathfrak M_m)}{W}
 =\frac{2\nu(\mathfrak M_m)}B
 \longrightarrow\frac{11}{36}.                       \tag{4.3}
\]

Every state in (4.2) is an actual collection of cyclic orders partitioning the
middle layer. Consequently it may be linearized into a literal contiguous-OR
word by the usual wreath linearization; no fractional, signed, or post-rounded
factor is used anywhere in the construction.

## 5. Universal all-rank footprint

After rotating the common prefix behind the four-letter gadget and relabelling its
four coordinates, every packet has the universal omitted-label words

\[
\begin{array}{ll}
 C=(\delta,\beta,\gamma,\alpha,T),
 &D=(\beta,\alpha,\delta,\gamma,T),\\
 C'=(\delta,\gamma,\beta,\alpha,T),
 &D'=(\gamma,\alpha,\delta,\beta,T),
\end{array}                                             \tag{5.1}
\]

with an otherwise arbitrary common tail \(T\). The signed exchange is

\[
 z=e_{C'}+e_{D'}-e_C-e_D.                              \tag{5.2}
\]

For an omitted-label word \(q=(q_0,\ldots,q_{n-1})\), its rank-\(r\)
cyclic intervals are the step-two windows

\[
 I_i^r(q)=\{q_i,q_{i+2},\ldots,q_{i+2r-2}\},
 \qquad i\in\mathbb Z_n.                               \tag{5.3}
\]

Multiplication of positions by \(2^{-1}=m+1\pmod n\) converts these into
ordinary consecutive \(r\)-windows. Under that conversion, the exceptional
positions \(0,1,2,3\) of (5.1) become

\[
 0,\ m+1,\ 1,\ m+2.                                    \tag{5.4}
\]

Thus the four exceptional positions form two adjacent pairs

\[
 \{0,1\},\qquad\{m+1,m+2\},                            \tag{5.5}
\]

separated by common-tail gaps of lengths \(m-1\) and \(m-2\).

Assume \(r\le m-1\). A consecutive \(r\)-window cannot meet both pairs in
(5.5). There are three cases.

1. If it meets neither pair, all four masks in (5.2) agree and cancel.
2. If it contains both positions of one pair, the two old exceptional-label
   sets and the two new exceptional-label sets agree as multisets and cancel.
3. It contains exactly one exceptional position. For each of the two adjacent
   pairs there are exactly two such boundary windows: the window ending at the
   first position and the window beginning at the second.

Put

\[
 \partial_K=e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}}.     \tag{5.6}
\]

If \(E,O\) denote the two common-tail gaps in cyclic order and
\(\ell=r-1\), the four surviving boundary contributions, up to a simultaneous
orientation reversal, are exactly

\[
 \partial_{\operatorname{suf}_\ell(O)}
 +\partial_{\operatorname{suf}_\ell(E)}
 -\partial_{\operatorname{pre}_\ell(E)}
 -\partial_{\operatorname{pre}_\ell(O)}.               \tag{5.7}
\]

For \(2\le r\le m-2\), these four cores are distinct. They contain none of
\(\alpha,\beta,\gamma,\delta\), so the eight resulting targets are distinct as
well. Every coefficient is \(+1\) or \(-1\). Hence

\[
 |\operatorname{supp}B_rz|=\|B_rz\|_1=8
 \qquad(2\le r\le m-2).                                \tag{5.8}
\]

For \(r=m-1\), the prefix and suffix of the shorter gap are both the complete
gap and cancel in (5.7). The two remaining dipoles have four distinct targets,
so

\[
 |\operatorname{supp}B_{m-1}z|
 =\|B_{m-1}z\|_1=4.                                    \tag{5.9}
\]

At rank one the four empty-core dipoles cancel. At rank \(m\), (5.2) has zero
histogram because it is an exact middle-factor exchange. Complementation gives
the corresponding upper-rank formulas. This proves (0.7).

## 6. Gaussian-window diameter

Let

\[
 N_q=\binom n{m-q},\qquad W=c_qN_q+r_q,\qquad0\le r_q<N_q. \tag{6.1}
\]

Let \(\mathcal B_q\) be the set of quota vectors with exactly \(r_q\) entries
\(c_q+1\) and all other entries \(c_q\). Define

\[
 O_q(\mu)=\frac12\min_{b\in\mathcal B_q}\|\mu-b\|_1.    \tag{6.2}
\]

Distance to a fixed set is Lipschitz, so for two equal-total load vectors
\(\mu,\nu\),

\[
 |O_q(\mu)-O_q(\nu)|
 \le\frac12\|\mu-\nu\|_1.                              \tag{6.3}
\]

By (5.8)--(5.9), one packet toggle changes \(J_A\) by at most

\[
 \ell_A
 =\frac2{c_1}+4\sum_{q=2}^{H}\frac1{c_q}
 =4S_A(m)-2,                                            \tag{6.4}
\]

 because \(c_1=1\) for all sufficiently large \(m\) (indeed for \(m\ge3\)).

For \(q=O_A(\sqrt m)\), the exact quotient is

\[
 \frac W{N_q}
 =\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.                  \tag{6.5}
\]

Taylor expansion, uniform on this range, gives

\[
 \log\frac W{N_q}
 =\frac{q(q+1)}m+O_A(m^{-1/2}).                         \tag{6.6}
\]

Consequently the Riemann sums for \(1/c_q\) converge away from the finitely
many jump points of \(x\mapsto\lfloor e^{x^2}\rfloor\), and those points have
zero measure. Hence

\[
 S_A(m)
 =(\kappa_A+o(1))\sqrt m,
 \qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.    \tag{6.7}
\]

Two vertices of the maximum-matching cube differ in at most
\(\nu(\mathfrak M_m)\) packet signs. Telescoping (6.3)--(6.4) and using
(3.10) proves

\[
\begin{aligned}
 |J_A(F_\varepsilon)-J_A(F_{\varepsilon'})|
 &\le\nu(\mathfrak M_m)(4S_A-2)\\
 &=\left(\frac{11\kappa_A}{18}+o(1)\right)B\sqrt m\\
 &=O_A(W/\sqrt m)=o(W).                                \tag{6.8}
\end{aligned}
\]

This is an all-\(q\le A\sqrt m\) statement on the same packet signs. No
rank-by-rank reorientation has been used.

### 6.1 Direct first-shadow obstruction

At rank \(m-1\), one packet has two positive and two negative unit cells. It can
fill at most two holes of the starting load. Thus for every cube vertex

\[
 M_1(F_\varepsilon)
 \ge M_1(F_m)-2|\operatorname{supp}\varepsilon|
 \ge M_1(F_m)-2\nu(\mathfrak M_m).                     \tag{6.9}
\]

Since \(2\nu(\mathfrak M_m)=O(B)=o(W)\), the frozen macroscopic-defect premise
(0.12) gives (0.13).

There is also a quota formulation. Every depth-one quota is at least one, so each
hole contributes at least one unit of deficit. Equal total load and quota imply
that total deficit equals total overflow. Therefore

\[
 O_1(F)\ge M_1(F).                                     \tag{6.10}
\]

Equations (6.8) and (6.10) show that every cube vertex has

\[
 J_A(F_\varepsilon)\ge(\delta-o(1))W.                  \tag{6.11}
\]

Thus this cube cannot satisfy the weighted-overload gate for coefficient one.

## 7. Whole-relabel commutators do not amplify the packets

Fix any owner-disjoint packet family \((\tau_i,K_i)\) in an exact factor \(F\),
and let \(F_\varepsilon\) be its heterogeneous cube.

### Theorem 7.1 (relabel-toggle normal form)

Consider an arbitrary word of the following two operations.

1. Globally relabel the current factor by a coordinate permutation.
2. Toggle the current transported image of one of the fixed packets.

After every prefix of the word, the state has the form

\[
 \boxed{gF_\varepsilon}                                \tag{7.1}
\]

for the cumulative global permutation \(g\) and a native sign vector
\(\varepsilon\).

#### Proof

The claim holds initially with \(g=1\) and \(\varepsilon=0\). A global
permutation \(\sigma\) sends \(gF_\varepsilon\) to
\(\sigma gF_\varepsilon\).

In state \(gF_\varepsilon\), packet \(i\) is transported to the component on
root packet \(gU_{K_i}\), with current side
\(g\tau_i^{\varepsilon_i}K_i\) and transposition
\(g\tau_i g^{-1}\). Lemma 4.1 makes it a fresh whole component. Toggling it
changes only \(\varepsilon_i\), giving \(gF_{\varepsilon\oplus e_i}\). This
closes the induction. \(\square\)

All packet toggles commute because their root packets are disjoint, and each is an
involution. Hence every internal packet commutator is the identity. Theorem 7.1
also shows that arbitrary whole-factor preparations between packet switches do not
conjugate different packets independently in the final frame: they contribute only
the one common final permutation \(g\). Since \(J_A\), the missing counts, and all
balanced-overflow objectives are coordinate-relabel invariant, (6.8)--(6.11) hold
for every endpoint of this larger relabel-toggle architecture.

This is the promised exact nonlocal-commutator ceiling. It does not apply if, after
a preparation, one selects a **new overlapping fresh component** rather than the
transported image of an unused fixed packet. That is the only relevant escape from
Theorem 7.1.

## 8. A pathwise aligned-round lower bound

Call one aligned round at a current exact factor a jointly applicable family of
pairwise root-disjoint universal common-tail trades (5.1). The family may be chosen
afresh after every preceding round. It need not belong to the original MSW matching.

Every trade consumes two negative rows, so a round contains at most \(B/2\) trades.
By (6.4), its endpoint changes \(J_A\) by at most

\[
 \frac B2(4S_A-2)=(2S_A-1)B.                          \tag{8.1}
\]

A path of \(R\) such rounds therefore satisfies

\[
 |J_A(F_R)-J_A(F_0)|\le R(2S_A-1)B.                   \tag{8.2}
\]

If \(M_1(F_0)\ge\delta W\), then (6.10) gives
\(J_A(F_0)\ge\delta W\). Reaching \(J_A(F_R)=o(W)\) requires

\[
\begin{aligned}
 R
 &\ge\frac{(\delta-o(1))W}{(2S_A-1)B}\\
 &=\boxed{
 \left(\frac{\delta}{\kappa_A}+o(1)\right)\sqrt m.}
                                                                  \tag{8.3}
\end{aligned}
\]

This permits packet reuse across rounds and does not assume every microstep is
downhill. Its scope is exactly the universal aligned four-letter class, with
root-disjointness within each round. Larger freshly recomputed transposition
components, nonaligned profile-three \(C_8\)'s, and moves containing auxiliary rows
are outside (8.3).

Without grouping microsteps into rounds, a path of \(M\) individual universal
aligned packet toggles changes \(J_A\) by at most \(M(4S_A-2)\). Thus the same
hypotheses force

\[
 M\ge\left(\frac{\delta}{2\kappa_A}+o(1)\right)B\sqrt m. \tag{8.4}
\]

The frozen first-shadow premise gives a stronger speed limit. A packet has exactly
two positive first-shadow cells, so one microstep can reduce the hole count by at
most two. A root-disjoint round has at most \(B/2\) packets and can reduce it by at
most \(B\). Therefore, if \(M_1(F_0)\ge\delta W\) and
\(M_1(F_R)=o(W)\), then

\[
 \boxed{
 R\ge(\delta-o(1))\,\frac WB=(\delta-o(1))n,
 \qquad
 M\ge\left(\frac{\delta}{2}-o(1)\right)W.
 }                                                       \tag{8.4a}
\]

This direct depth-one bound dominates (8.3)--(8.4) under the macroscopic-hole
premise. The weighted bounds remain useful because they control the complete
Gaussian ledger without assigning all progress to depth one.

### 8.1 Positive-density coarse-cell turnover

The maximum matching leaves a positive density of singleton cells. This can be
combined with all-colour owner regularity to produce a much stronger coarse bridge
than the seam-only estimate of Section 9.

First reserve the \(m-3\) row-disjoint packets of distinct colours

\[
 \tau_s=(2s+2\ \ 2s+3),\qquad 2\le s\le m-2.            \tag{8.5}
\]

Starting with a maximum matching, delete every matching edge incident with one of
the \(2(m-3)\) reserved vertices and insert the reserved edges. At most
\(2(m-3)\) old matching edges are deleted and \(m-3\) are inserted. Thus the
resulting matching has size at least

\[
 \nu(\mathfrak M_m)-(m-3).                              \tag{8.6}
\]

Let \(u\) be its number of unmatched singleton vertices. Maximality of
\(\nu(\mathfrak M_m)\), (8.6), and (3.4) give

\[
 O_m\le u\le O_m+2(m-3),
\qquad
 \boxed{u=\left(\frac{25}{36}+o(1)\right)B.}            \tag{8.7}
\]

Partition the \(B\) owner rows into the matched two-row cells and these \(u\)
singleton cells. Every matched cell is a complete component packet, so every
packet-side choice preserves its middle-root union. Singleton cells are untouched.
Consequently, for every coordinate transposition \(\rho\), the fresh
\(\rho\)-owner multigraph contracted onto these cells is edge-for-edge independent
of every packet sign.

For one exact factor row, the all-transposition loopless owner degree is exactly

\[
 D=n(m-1)(m+2).                                         \tag{8.8}
\]

Indeed, at each shorter cyclic distance \(d=1,\ldots,m\) there are \(n\)
coordinate pairs, and a colour at distance \(d\) has owner degree
\(2\min(d,m-1)\). Summing gives (8.8).

Let \(I_\rho\) be the number of colour-\(\rho\) edge incidences at singleton
cells, and let \(E_\rho\) be the number of colour-\(\rho\) owner edges joining
different packet cells. Every loopless edge incident with a singleton leaves its
cell. An edge has at most two singleton endpoints, so

\[
 \sum_\rho I_\rho=uD,\qquad E_\rho\ge\frac12 I_\rho.     \tag{8.9}
\]

The reserved transpositions (8.5) use \(n-7\) coordinates in disjoint pairs. A
coordinate transposition commutes with every reserved colour exactly when it is
one of the \(m-3\) reserved swaps or both its coordinates lie among the seven
unused coordinates. There are

\[
 (m-3)+\binom72=m+18                                    \tag{8.10}
\]

such colours. Each colour contributes at most \(u(n-3)\) singleton incidences.
The remaining

\[
 \binom n2-(m+18)=2m^2-18                               \tag{8.11}
\]

colours are coordinate-noncommuting with at least one reserved packet colour.
Deleting the colours in (8.10) from (8.9) and averaging gives one remaining
\(\rho\) with

\[
 I_\rho\ge
 \frac{u[D-(m+18)(n-3)]}{2m^2-18}.                      \tag{8.12}
\]

Therefore

\[
\boxed{
 E_\rho
 \ge
 \frac{u[D-(m+18)(n-3)]}{2(2m^2-18)}
 =\left(\frac{25}{144}-o(1)\right)W.
}                                                        \tag{8.13}
\]

This \(\rho\) depends only on the fixed root-cell partition, not on the packet
signs. Hence (8.13) holds after every choice in the heterogeneous cube.

Let \(Z_\rho\) be the owner union of fresh \(\rho\)-components meeting at least
two packet cells. Every crossing edge in (8.13) has both endpoints in \(Z_\rho\),
and every fresh owner has loopless \(\rho\)-degree at most \(n-3\). Thus

\[
 2E_\rho\le(n-3)|Z_\rho|,
\]

and

\[
\boxed{
 |Z_\rho|
 \ge\left(\frac{25}{72}-o(1)\right)B.
}                                                        \tag{8.14}
\]

For every threshold \(L\), either one such fresh component has more than \(L\)
owners, or there are at least

\[
 \left(\frac{25}{72}-o(1)\right)\frac BL               \tag{8.15}
\]

fresh components meeting multiple packet cells.

Equations (8.13)--(8.15) are genuine positive-density coarse turnover. They do
not prove positive-density commutator seams. The lower bound came from singleton
incidences; all certified edges could be singleton--singleton edges, on which the
piecewise preparation is the identity at both endpoints. Coordinate noncommutation
of \(\rho\) with a reserved colour does not force the counted edge to meet that
reserved root packet. If all singleton cells are merged into their one identity-gauge
region, this artificial fine-cell expansion no longer gives (8.13).

Thus (8.14) supplies a strong fresh fragmentation-or-large-component theorem, but
not targetwise NAE scattering, useful lower-shadow leakage, or a nonzero commutator
drift.

There is an exact reason middle-root turnover cannot simply be renamed
first-shadow turnover. Fix \(\rho=(a\ b)\). Every moved middle-root orbit has the
unique form

\[
 \{S\cup\{a\},\,S\cup\{b\}\},
 \qquad
 S\in\binom{[n]\setminus\{a,b\}}{m-1}.                 \tag{8.16}
\]

Thus the map from a colour-\(\rho\) middle edge to its core \(S\) is injective.
However, if a wreath owns \(S\cup\{a\}\), then \(S\) is one of that wreath's
rank-\((m-1)\) cyclic intervals only when \(a\) is one of the two endpoints of
the owned middle window. In one cyclic row a fixed label is an endpoint of exactly
two middle windows. The same holds for \(b\), so over the whole factor at most

\[
 4B                                                        \tag{8.17}
\]

colour-\(\rho\) owner incidences are directly boundary-aligned with their cores.
Consequently even (8.13), which is \(\Theta(W)=\Theta(nB)\), certifies only
\(O(B)\) directly visible first-shadow incidences. Any useful effect from the
remaining edges must arise from genuinely nonlocal component containment leakage,
not from the middle-edge core map alone.

## 9. Why a \(\Theta(B)\) seam count does not by itself escape the ceiling

Let \(U\) be the root union of a switched family of \(\tau\)-components and define
the piecewise involution of the middle layer

\[
 \alpha_U(X)=
 \begin{cases}
 \tau X,&X\in U,\\
 X,&X\notin U.
 \end{cases}                                           \tag{9.1}
\]

Because \(U\) is \(\tau\)-invariant, \(\alpha_U\) is an involution. After pulling
the child rows back to the original row labels, the freshly recomputed
\(\sigma\)-owner relation is generated by

\[
 \boxed{
 o_F(Y)\sim o_F(\alpha_U\sigma\alpha_UY).
 }                                                       \tag{9.2}
\]

The crossing \(\sigma\)-orbits are exactly the mixed-side seams, and their number
is

\[
 s=|U\setminus\sigma U|
 =\frac12|U\triangle\sigma U|.                         \tag{9.3}
\]

Let \(Z\) be the owner union of the fresh components which meet at least one seam.
Every crossing orbit gives a loopless fresh edge: \(U\) is a union of whole
\(\tau\)-component root packets and \(\tau U=U\), so after pullback its two
owners lie respectively in a selected and an unselected old \(\tau\)-component
and are distinct. The loopless transposition-owner degree of one wreath is at most
\(n-3\). Every crossing root orbit therefore has two distinct owner incidences.
Consequently

\[
 \boxed{|Z|\ge\frac{2s}{n-3}.}                         \tag{9.4}
\]

If every mixed fresh component has at most \(L\) owners, their number is at least

\[
 \boxed{
 \left\lceil\frac{2s}{(n-3)L}\right\rceil.
 }                                                       \tag{9.5}
\]

The factor \(n\) in (9.4) is decisive. For the explicit smallest-component
preparation,

\[
 s=2\operatorname{Cat}_{m-2}
 =\left(\frac18+o(1)\right)B,                          \tag{9.6}
\]

so (9.4) certifies only

\[
 |Z|\ge\left(\frac14+o(1)\right)\frac Bn.              \tag{9.7}
\]

Here the displayed preparation uses \(\tau=(2\ 3)\) and
\(\sigma=(4\ 5)\), which commute. It proves the seam-count ceiling but is not
a noncommuting-coordinate example. In this explicit family the crossing roots
are \(\tau\)-moved, so the piecewise involution \(\alpha_U\) does fail to
commute with \(\sigma\); these are genuine piecewise-commutator seams. No such
conclusion is inferred from the bare inequality \(s>0\) for an arbitrary \(U\).

For the balanced spectral preparation, the audited seam constant is

\[
 \beta=\frac{1287-700\sqrt3}{512},\qquad
 s\ge(\beta-o(1))B,                                    \tag{9.8}
\]

and (9.4) gives only

\[
 |Z|\ge(2\beta-o(1))\frac Bn.                          \tag{9.9}
\]

The averaging which produces (9.8) ranges over all \(\sigma\ne\tau\); it does
not prove that its maximizing \(\sigma\) overlaps \(\tau\). If a separate theorem
supplied the same seam count for an overlapping, genuinely noncommuting
\(\sigma\), the degree implication (9.4) would still be only \(O(B/n)\).

Thus \(\Theta(B)\) seams do not by counting alone force \(\Theta(B)\) mixed
owners or components. Even under a constant component-size cap, (9.5) gives only
\(\Omega(B/n)\) fresh components. One component with \(\Theta(B/n)\) owners is
compatible with all these inequalities. This does not prove concentration; it
proves that the existing seam estimate cannot prove the dispersion needed to leave
the aligned-packet ceiling.

## 10. Frozen Catalan-tail libraries

For completeness, the earlier exact Catalan hierarchy gives a second, independent
static ceiling. Let the suffix depth be \(r=m-j-2\), and retain all canonical
\((2\ 3)\)-components with \(r\ge L\). Their first-shadow action support is at
most

\[
 A_{m,L}
 =\sum_{r=L}^{m-2}
 (4m-4r+2)
 (\operatorname{Cat}_{m-r-2}+\operatorname{Cat}_{m-r-1})
 \operatorname{Cat}_r
 =O\!\left(\frac W{\sqrt L}\right),                    \tag{10.1}
\]

although these components contain \((3/8+o(1))B\) wreaths when \(L\to\infty\)
and \(L=o(m)\).

Suppose a frozen commutator library uses \(K\) such atlases and a coordinate group
moving at most \(b\) coordinates. A rank target has group orbit size at most
\(2^b\). Hence the union of every possible transported action support has size at
most

\[
 |E^*|\le K2^bA_{m,L}
 =O\!\left(\frac{K2^bW}{\sqrt L}\right).               \tag{10.2}
\]

If

\[
 K2^b=o(\sqrt L),                                      \tag{10.3}
\]

then an arbitrarily long word in this frozen library leaves all but \(o(W)\)
first-shadow coordinates unchanged. This includes every fixed \(K,b\) with
\(L\asymp m\). As with Theorem 7.1, the hypothesis is frozen support; a newly
recomputed component under a different transposition is outside (10.2). If the
word also contains standalone whole-factor relabellings, “unchanged” here is
understood relative to the final globally relabelled baseline.

### 10.1 An explicit PBBS clean-\(C_8\) reservoir

This subsection is independent of the MSW packet matching. It resolves the clean
directed-cycle supply question for the **initial** canonical PBBS factor, while
leaving the topology-compatible balance question open.

For a core \(K\in\binom{[n]}{m-1}\), put \(T=K^c\). Let
\(U_+(K)\) and \(U_-(K)\) be the three unmatched zeros under forward and reverse
cyclic parenthesis matching. For \(u\in T\), define

\[
 \alpha_K(u)=r_+(K\cup\{u\}),\qquad
 \beta_K(u)=r_-(K\cup\{u\}).                            \tag{10.4}
\]

These are exactly the two heads of the out-arcs from \(u\) in the PBBS auxiliary
digraph \(D_K\).

### Lemma 10.1 (exact predecessor/successor rule)

\(\alpha_K(u)\) is the strict cyclic predecessor of \(u\) in \(U_+(K)\), and
\(\beta_K(u)\) is the strict cyclic successor of \(u\) in \(U_-(K)\).

#### Proof

Cut the deficit-three word at its forward unmatched zeros:

\[
 0_{a_0}D_0\,0_{a_1}D_1\,0_{a_2}D_2,                  \tag{10.5}
\]

with each \(D_i\) Dyck. If the flipped zero \(u\) lies inside \(D_i\), changing it
to one creates two excess opens, which consume the next two displayed unmatched
zeros and leave \(a_i\), the preceding unmatched zero. If \(u=a_i\), that
unmatched zero disappears and its new open consumes \(a_{i+1}\), again leaving
the strict predecessor \(a_{i-1}\). This proves the formula for \(\alpha_K\).
Applying the same argument in reversed cyclic order proves the successor formula
for \(\beta_K\). \(\square\)

### Theorem 10.2 (PBBS clean-cycle reservoir)

For \(m\ge4\), the initial canonical PBBS factor supports at least

\[
 \boxed{
 N_m^{\rm PBBS}
 =n\bigl(\operatorname{Cat}_{m-1}-2^{m-2}\bigr)
 =\left(\frac14-o(1)\right)W
 }                                                       \tag{10.6}
\]

distinct alternating \(C_8\)'s. It contains a vertex-disjoint subfamily of size

\[
 \boxed{
 \left\lfloor\frac{N_m^{\rm PBBS}}{128m}\right\rfloor
 =\left(\frac1{256}-o(1)\right)B.
 }                                                       \tag{10.7}
\]

#### Proof

Choose a labelled cyclic start \(a\) and a Dyck word \(D\) of semilength
\(m-1\) and height \(h\ge3\). Define the deficit-three core word

\[
 w(K)=0_a\,D\,0_{a_1}0_{a_2}.                          \tag{10.8}
\]

The three displayed zeros are exactly

\[
 U_+(K)=\{a,a_1,a_2\}.                                  \tag{10.9}
\]

For \(j=0,1,2\), let \(b_j\) be the downstep of \(D\) immediately after its
rightmost visit to height \(h-j\). These steps exist, are distinct, and occur in
the order \(b_0,b_1,b_2\) inside \(D\). We claim

\[
 U_-(K)=\{b_0,b_1,b_2\}.                                \tag{10.10}
\]

For \(j=0,1\), the segment after \(b_j\) and before \(b_{j+1}\) starts and ends
at height \(h-j-1\) and never rises above that height, by rightmostness. It has
sum zero and every relative prefix sum is nonpositive. For the cyclic third
segment, the suffix after \(b_2\) never exceeds height \(h-3\); it is followed by
the two trailing zeros, the initial zero \(a\), and the prefix of \(D\) ending at
height \(h\) before \(b_0\). Its total is

\[
 -(h-3)-3+h=0,                                         \tag{10.11}
\]

and all relative prefix sums are again nonpositive. Reversing each of these
three segments produces a Dyck word. Hence, in reverse cyclic matching, the
three displayed \(b_j\)'s are precisely the unmatched zeros, proving (10.10).

Starting at \(a_1\), the six anchors occur cyclically as

\[
 A_0=a_1,\ A_1=a_2,\ A_2=a,\ B_0=b_0,\ B_1=b_1,\ B_2=b_2.
                                                                  \tag{10.12}
\]

Lemma 10.1 now gives the directed cycle

\[
 A_1\longrightarrow B_0\longrightarrow B_1
 \longrightarrow A_2\longrightarrow A_1,              \tag{10.13}
\]

using respectively \(\beta,\beta,\alpha,\alpha\). It is clean. Indeed,

\[
\begin{array}{c|c}
v&\{\alpha_K(v),\beta_K(v)\}\\ \hline
B_0&\{A_2,B_1\}\\
B_1&\{A_2,B_2\}\\
A_2&\{A_1,B_0\}\\
A_1&\{A_0,B_0\},
\end{array}                                             \tag{10.14}
\]

so none of the four reverse arcs of (10.13) occurs. The clean-\(C_4\)
dictionary therefore supplies one PBBS-supported alternating \(C_8\), with
unique core \(K\).

The map \((a,D)\mapsto K\) is injective. The three anchors in \(U_+(K)\) are
intrinsic; among their three cyclic gaps exactly one is nonempty. Its preceding
anchor recovers \(a\), and its contents recover \(D\).

Dyck paths of semilength \(r\) and height at most two are in bijection with
compositions of \(r\): their primitive factors are
\(1(10)^{j-1}0\), indexed by the parts \(j\). There are \(2^{r-1}\) such paths.
With \(r=m-1\), the number of admissible \(D\)'s is therefore

\[
 \operatorname{Cat}_{m-1}-2^{m-2}.                     \tag{10.15}
\]

There are \(n\) labelled choices of \(a\), proving the exact first expression in
(10.6). Also

\[
 \frac{n\operatorname{Cat}_{m-1}}W
 =\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_m}
 =\frac{m+1}{2(2m-1)}\longrightarrow\frac14,            \tag{10.16}
\]

while \(n2^{m-2}/W=o(1)\), proving the asymptotic.

Every PBBS middle vertex lies in at most \(16m\) supported alternating
\(C_8\)'s. Greedily selecting one cycle and discarding all cycles meeting one of
its eight vertices removes at most \(8\cdot16m=128m\) candidates. This proves
(10.7). \(\square\)

For \(R\) vertex-disjoint selected switches, the eight touched vertices per
switch change at most one old and one new first-shadow colour each. Hence

\[
 \|\Delta\mu_{m-1}\|_1\le16R,                           \tag{10.17}
\]

and at most \(8R\) new holes can be created. Thus even the positive-density
subfamily in (10.7) has only \(O(B)=o(W)\) first-shadow action.

The scope restriction is decisive. “Clean” means only that the four proposed
reverse arcs are absent. It does not imply the centered-segment zero/opposite-pair
conditions required for componentwise point regularity, component increase, or
length-\(n\) outputs. Vertex-disjoint cycles may be toggled simultaneously as an
ordinary spanning 2-factor operation, but not yet as balanced exact-wreath
rebundling. The six-label description and the supply theorem apply to the initial
canonical PBBS factor and need not persist after the first switch.

## 11. Final theorem-level verdict

The Catalan hierarchy now has an exact positive and negative theorem at the same
scale.

1. **Positive density is real.** The complete contextual size-two packet graph has
   exact maximum matching (0.3), with asymptotic packet density \(11/72\), row
   density \(11/36\), and middle-owner density \(11/36\). Every subset and every
   switching order is an integral exact factor.
2. **The entire cube is Gaussian-window inert.** Every packet has exact footprint
   (0.7), so the whole cube has diameter \(O_A(W/\sqrt m)=o(W)\). It preserves a
   frozen \(\delta W\) first-shadow defect up to \(o(W)\).
3. **Whole-relabel commutators add nothing.** Their endpoints have the exact normal
   form \(gF_\varepsilon\), so they inherit the same ceiling.
4. **Repeated aligned rounds are quantitatively slow.** The all-band ledger gives
   \((\delta/\kappa_A+o(1))\sqrt m\) rounds, while the frozen first-shadow
   premise sharpens this to \((\delta-o(1))n\) rounds and
   \((\delta/2-o(1))W\) individual packet toggles.
5. **Coarse turnover can have positive density.** Equations (8.13)--(8.15) give
   \((25/144-o(1))W\) crossing packet-cell edges and
   \((25/72-o(1))B\) fresh owners, uniformly over all packet signs.
6. **Coarse turnover is not seam dispersion.** Its counted edges may lie entirely
   between identity-gauge singleton cells. A bare side-mismatch seam count loses a
   factor \(n\) under the direct degree argument, even if coordinate
   noncommutation is separately imposed.
7. **Frozen tail commutators are also inert** under (10.3).
8. **PBBS clean connectors are abundant.** Theorem 10.2 supplies
   \((1/4-o(1))W\) initial clean \(C_8\)'s and
   \((1/256-o(1))B\) vertex-disjoint ones, but proves none of the balance
   conditions needed for exact-wreath merge--reorder--split.

Therefore none of the mechanisms quantified here—positive-density owner
replacement, a fixed persistent packet cube, arbitrary whole-factor preparations,
or the mere existence of \(\Theta(B)\) seams—establishes

\[
 \nu(k)\le(1+o(1))W(k).                                \tag{11.1}
\]

The only surviving version of this lane must simultaneously do all of the following:

* leave the universal aligned four-letter packet atlas;
* use overlapping state-dependent component recomputation;
* produce a fresh component family with \(\Omega(W)\)-scale lower-shadow action;
* release the relevant bounded-coordinate orbit profiles;
* turn the coarse owner mass of (8.14) into genuinely noncommuting, targetwise
  component dispersion rather than identity-region turnover;
* prove that useful mixed-owner mass is new rather than recycled; and
* control the same signs at every \(q\le A\sqrt m\).

No theorem here rules out that genuinely nonlocal escape. Conversely, no presently
proved Catalan or PBBS connector theorem supplies it. In particular, (0.3)--(0.7)
are MSW statements. Importing the constants \(11/72\) or \(11/36\) into the
canonical PBBS factor would require a factor-transfer or a PBBS
balance-compatible packet theorem. The clean-cycle supply of Theorem 10.2 is not
such a transfer.

## 12. Independent audit

The proof was independently checked along four separate lines.

* The primitive-factor audit verified that \(D\) means the primitive factor
  \(1100\), not substring avoidance; that expansion fibers are exactly Cartesian
  products of monomer/dimer tiling graphs; and that the recursive matching is
  maximum by the Fibonacci parity period. It independently derived (3.3), checked
  the absence of a nearer pole via \(R(1/4)L(1/4)=5/21\), and recovered the
  constants \(25/36\), \(11/72\), and \(11/36\).
* The shadow audit independently put the four exceptional omitted-label positions
  into the two adjacent step-two pairs (5.5), classified every possible window,
  and recovered support/\(\ell^1\) sizes \(4\) and \(8\). It checked the
  half-\(\ell^1\) normalization, the factor \(4S_A-2\), the constant
  \(11\kappa_A/18\), the restricted scope of the all-band
  \(\Omega(\sqrt m)\)-round bound, and the stronger direct
  \(\Omega(n)\)-round first-shadow speed limit.
* Two independent turnover audits recovered the exact all-colour degree
  \(n(m-1)(m+2)\), the \(m+18\) excluded colours, the unordered-edge factor
  \(1/2\), and the constants \(25/144\) and \(25/72\). Both identified the same
  indispensable caveat: singleton--singleton edges are identity-gauge edges, so
  (8.13) is coarse-cell turnover and not a mixed-cocycle seam theorem.
* Two independent PBBS audits rederived the strict predecessor/successor rule,
  the reverse-unmatched steps (10.10), clean cycle (10.13), injectivity, the
  subtraction \(2^{m-2}\), and the constants \(1/4\) and \(1/256\). Both
  confirmed that this is clean-cycle supply only, not balanced exact rebundling.

The audits agree that the report proves an exact MSW persistent-cube ceiling and
an initial-PBBS clean-cycle supply theorem, but neither PBBS balanced rebundling
nor a global impossibility theorem for all adaptive component switches.
