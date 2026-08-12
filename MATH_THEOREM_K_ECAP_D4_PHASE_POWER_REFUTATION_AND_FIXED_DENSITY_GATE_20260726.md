# The canonical ECAP phase maps are not powers of one rotation

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 W=\binom{2m}{m},\qquad B=C_m=\frac{W}{m+1},\qquad
 N_q=\binom{2m}{m-q},
\]

and, at the corrected fixed Gaussian entrance, let

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,
 \qquad a>0\text{ fixed}.
\]

The required number of active middle occurrences and ordinary cyclic
packets is

\[
 2mK=(e^{-a^2}+o(1))W,
 \qquad
 K=\left(\frac{e^{-a^2}}2+o(1)\right)B.
\tag{0.1}
\]

Thus an extensive reciprocal-\(C_8\) Catalan bank has ample scalar row
supply.  If it uses \(u=\lfloor\alpha m\rfloor\),
\(0<\alpha<1/2\), disjoint slots, then all but \(O_\alpha(B/m)\)
canonical roots have a nontrivial variant, and the changed-root supply
divided by the packet demand tends to

\[
                         2e^{a^2}.
\tag{0.2}
\]

The useful selected-row action is much smaller than the raw catalogue.
Uniformly over every \(K\)-root set \(S\), the maximum number of eligible
selected slot incidences is

\[
 Z_K=\left(\frac{\alpha e^{-a^2}}{16}+o(1)\right)W
     =\left(\frac\alpha{16}+o(1)\right)N_{q_0}.
\tag{0.3}
\]

Each incidence is one exact complement-graph two-switch.  It can reduce
the induced edge count by at most one, hence can reduce physical middle
collision by at most two.  Therefore the complete bank can repair at most

\[
 2Z_K=\left(\frac{\alpha e^{-a^2}}8+o(1)\right)W
     =\left(\frac\alpha8+o(1)\right)N_{q_0}
\tag{0.4}
\]

middle collisions on a fixed selected root set.  Equations (0.1)--(0.4)
are the exact supply/action comparison against \(N_{q_0}\).  They prove
capacity, not productive all-depth selection.

This note then closes one proposed way to select the near-alternating
shore.  For the canonical MSW factor, let \(i_t\) send a Dyck root to
its phase-\(t\) middle state and define

\[
 c_t=i_{m-t}^{-1}\circ C\circ i_t,
\tag{0.5}
\]

where \(C\) is set complementation.  At \(m=4\), the two nontrivial
phase maps are

\[
\begin{aligned}
c_1={}&(A\ L)(B\ N)(C\ D\ M)(E\ I\ J)(F\ G\ H\ K),\\
c_2={}&(A\ N)(B\ L)(C\ M)(D\ J)(E\ I)(F\ H)(G\ K).
\end{aligned}
\tag{0.6}
\]

Consequently

\[
 \operatorname {ord}(c_1)=12,
 \qquad c_1c_2(C)=C,
 \qquad c_2c_1(C)=J.
\tag{0.7}
\]

In particular, the \(c_t\) are not powers of one permutation.  A fortiori
they are not odd powers of one plane-tree rotation or promotion of order
\(2m=8\).  The obstruction survives every simultaneous root relabelling,
and also survives inversion arising from reversing all path phases.

This refutes the master-rotation mechanism, but it does not refute ECAP.
The exact remaining middle obstruction is an aggregate odd-cycle or
odd-relation theorem for the genuinely nonabelian family \(\{c_t\}\).
The fixed-density constant is given in Theorem 3.3 below.  The simultaneous
all-depth interval-packing problem remains additional.

## 1. Corrected fixed-density packet supply

The exact ratio is

\[
 \frac{N_q}{W}=\prod_{j=1}^q\frac{m-j+1}{m+j}.
\tag{1.1}
\]

Uniformly for \(q=a\sqrt m+O(1)\), logarithmic expansion gives

\[
 \log\frac{N_q}{W}=-\frac{q^2}{m}+O_a(m^{-1/2}),
\]

and hence

\[
 \frac{N_{q_0}}W=e^{-a^2}+O_a(m^{-1/2}).
\tag{1.2}
\]

Since \(B=W/(m+1)\),

\[
 \frac KB
 =\frac{m+1}{2m}\frac{N_{q_0}}W+o(1)
 =\frac{e^{-a^2}}2+o(1),
\tag{1.3}
\]

which proves (0.1).  The floor leaves fewer than \(2m\) middle
occurrences unused and is therefore negligible on the \(W\)-scale.

For the extensive reciprocal bank, write \(J(x)\) for the set of eligible
slots of root \(x\), and put \(z_x=|J(x)|\).  The exact one- and two-slot
Catalan censuses imply

\[
 \bar z:=\frac1B\sum_xz_x=\frac{\alpha m}{8}+O_\alpha(1),
 \qquad
 \sum_x(z_x-\bar z)^2=O_\alpha(Bm).
\tag{1.4}
\]

For every \(S\subseteq D_m\) with \(|S|=K\), Cauchy--Schwarz gives

\[
 \sum_{x\in S}z_x
 \le K\bar z+\sqrt{K\sum_x(z_x-\bar z)^2}
 =\frac{\alpha e^{-a^2}}{16}W+O_\alpha(Wm^{-1/2}).
\tag{1.5}
\]

Conversely, averaging the left side over all \(K\)-subsets gives the
mean \(K\bar z\).  Thus its maximum is at least \(K\bar z\), and (1.5)
proves (0.3).

The same moment estimate gives

\[
 |\{x:J(x)=\varnothing\}|=O_\alpha(B/m).
\tag{1.6}
\]

Combining (1.3) and (1.6) proves (0.2).  Notice the distinction:

* changed roots are a packet catalogue of size \((1-o(1))B\);
* complete rectangles number
  \(uC_{m-2}=(\alpha/16+o(1))W\);
* selected eligible incidences number only
  \((\alpha e^{-a^2}/16+o(1))W\).

Only the last quantity controls what one selected packet family can
actually change.

## 2. Exact phase decomposition of the cut complement graph

For a canonical row rooted at \(x\in D_m\), let

\[
 X_0(x),X_1(x),\ldots,X_m(x)
\]

be its successive rank-\(m\) states.  Chung--Feller exactness says that
\(i_t(x)=X_t(x)\) bijects \(D_m\) onto flaw layer \(t\).  Therefore
(0.5) is a permutation of \(D_m\), with

\[
                       c_{m-t}=c_t^{-1}.
\tag{2.1}
\]

For \(1\le t<m/2\), let \(H_t\) be the labelled multigraph with one
edge \(\{x,c_t(x)\}\) for every root \(x\).  A two-cycle gives two
parallel labelled edges.  No \(c_t\) has a fixed point: such a fixed point
would put complementary nonport primary tokens in one cut row, whereas the
only complementary primary pair in a row is its two ports.

If \(m\) is even, \(c_{m/2}\) is a fixed-point-free involution and gives
one perfect matching, counted once rather than twice.  Consequently the
canonical cut complement multigraph is the labelled edge-disjoint union

\[
 G_0=\mathop{\dot\bigcup}_{1\le t<m/2}H_t
 \mathbin{\dot\cup}
 \begin{cases}
 M_{m/2},&m\text{ even},\\
 \varnothing,&m\text{ odd}.
 \end{cases}
\tag{2.2}
\]

This is the exact replacement for the false associahedron model.

## 3. The fixed-density odd-cycle criterion

Let \(o_t\) be the number of odd cycles of \(c_t\), and let

\[
 \Delta=B/2-K.
\tag{3.1}
\]

The independence number of \(H_t\) is \((B-o_t)/2\).  Hence every
\(K\)-set \(S\) satisfies

\[
 e_{H_t}(S)\ge\left(\frac{o_t}{2}-\Delta\right)_+.
\tag{3.2}
\]

Indeed, on each cycle, selecting more than its independence number forces
at least that many selected edges, and summing positive parts proves
(3.2).  By (1.3),

\[
 \frac{2\Delta}{B}=1-e^{-a^2}+o(1).
\tag{3.3}
\]

One reciprocal rectangle is exactly a graph two-switch

\[
 xz,yw\longleftrightarrow yz,xw,
\]

whose induced-edge change is

\[
 ({\bf1}_S(y)-{\bf1}_S(x))
 ({\bf1}_S(z)-{\bf1}_S(w))\in\{-1,0,1\}.
\tag{3.4}
\]

Thus (0.3), (2.2), and (3.2) give the following exact asymptotic test.

### Theorem 3.3 (fixed-density phase-cycle obstruction)

For every common-factor reciprocal-\(C_8\) mask \(A\) and every
\(S\subseteq D_m\), \(|S|=K\),

\[
 \frac{e_{G_A}(S)}W
 \ge
 \frac1{2(m+1)}
 \sum_{1\le t<m/2}
 \left(\frac{o_t}{B}-\frac{2\Delta}{B}\right)_+
 -\frac{Z_K}{W}.
\tag{3.5}
\]

In particular, if

\[
 \liminf_{m\to\infty}\frac1m
 \sum_{1\le t<m/2}
 \left(\frac{o_t}{B}-(1-e^{-a^2})\right)_+
 >\frac{\alpha e^{-a^2}}8,
\tag{3.6}
\]

then every such state has \(e_{G_A}(S)=\Omega(W)\), hence physical
middle collision \(2e_{G_A}(S)=\Omega(W)\).  Common-factor ECAP then
fails already at the middle layer.

Equation (3.5) is finite and exact when \(Z_K\) denotes the exact maximum
selected incidence count.  Substituting (0.3) and (3.3) gives (3.6), its
clean fixed-\(a\) limit.

At the one-baseline entrance \(q_0=\lceil m^{1/4}\rceil\), the same
proof uses

\[
 \frac{2\Delta}{B}=m^{-1/2}+O(m^{-3/4})
\]

and the right side of (3.6) becomes \(\alpha/8\).  Thus understanding the
actual joint phase algebra remains important at both scales.

## 4. The complete canonical \(m=4\) phase table

Name the fourteen Dyck roots, in lexicographic subset notation, by

\[
\begin{array}{c|cccccccccccccc}
 &A&B&C&D&E&F&G&H&I&J&K&L&M&N\\ \hline
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&
1345&1346&1347&1356&1357.
\end{array}
\tag{4.1}
\]

Direct application of the MSW recursion

\[
 \rho(1u0v)=
 (|u|+2,\ |u|+2-\rho(\mu u),\ 1,\ |u|+2+\rho(v))
\tag{4.2}
\]

gives the following complete middle-state paths:

\[
\begin{array}{c|ccccc}
A&1234&1348&1368&1568&5678\\
B&1235&1358&1458&1468&4678\\
C&1236&1238&1378&1478&4578\\
D&1237&1367&1467&4567&4568\\
E&1245&1258&1268&1678&3678\\
F&1246&1248&1278&1578&3578\\
G&1247&1267&1567&3567&3568\\
H&1256&1456&3456&3458&3478\\
I&1257&1457&3457&3467&3468\\
J&1345&2345&2358&2368&2678\\
K&1346&2346&2348&2378&2578\\
L&1347&2347&2367&2567&2568\\
M&1356&2356&2456&2458&2478\\
N&1357&2357&2457&2467&2468.
\end{array}
\tag{4.3}
\]

For auditability, the corresponding deletion/insertion words
\((a_1a_2a_3a_4\mid b_1b_2b_3b_4)\) are

\[
\begin{array}{c|c@{\qquad}c|c}
A&2431\mid8657&H&2165\mid4387\\
B&2351\mid8467&I&2157\mid4368\\
C&6231\mid8745&J&1453\mid2867\\
D&2317\mid6458&K&1643\mid2875\\
E&4521\mid8673&L&1437\mid2658\\
F&6421\mid8753&M&1365\mid2487\\
G&4217\mid6538&N&1357\mid2468.
\end{array}
\tag{4.4}
\]

Every line of (4.3) follows by starting at its root and replacing
\(a_j\) by \(b_j\), for \(j=1,2,3,4\).  Hence the table is independently
checkable from (4.4), without any search.

Complementing the phase-one state and locating it in the phase-three
column gives

\[
\begin{array}{c|cccccccccccccc}
x&A&B&C&D&E&F&G&H&I&J&K&L&M&N\\ \hline
c_1x&L&N&D&M&I&G&H&K&J&E&F&A&C&B.
\end{array}
\tag{4.5}
\]

This is the first line of (0.6).  Complementing within the central
phase-two column gives the second line.  In particular, both displayed
permutations are derived solely from the literal owner table.

### Theorem 4.1 (intrinsic phase-power obstruction at \(m=4\))

The canonical complement-phase permutations \(c_1,c_2\) are not powers
of any common permutation.

#### Proof

From (0.6), the cycle lengths of \(c_1\) are

\[
                         2,2,3,3,4,
\]

so \(\operatorname {ord}(c_1)=12\).  This already rules out a power of
any permutation of order \(8=2m\).

More strongly, powers of one permutation commute.  With right-to-left
composition, (0.6) gives

\[
 c_1c_2(C)=c_1(M)=C,
 \qquad
 c_2c_1(C)=c_2(D)=J.
\]

Thus \([c_1,c_2]\ne1\), proving the claim even without prescribing the
order of the putative common permutation. \(\square\)

If all rows are simultaneously reindexed by a bijection \(h\), then

\[
 c_t\longmapsto hc_th^{-1}.
\tag{4.6}
\]

Coordinate relabellings which preserve the Chung--Feller layers induce
exactly such a common conjugacy, since coordinate complementation commutes
with relabelling.  Reversing every path phase additionally replaces the
maps by conjugates of their inverses and exchanges \(t\) with \(m-t\).
Order and commutativity are invariant under these operations.  Hence no
allowed common relabelling or common phase reversal repairs Theorem 4.1.

An arbitrary row-dependent rerooting is outside this statement: it need
not preserve the phase layers or define a common conjugate of (0.5).  Such
a rerooting would itself be a new packet construction, not a proof that
the canonical \(c_t\) are powers of one rotation.

## 5. The tempting ECO census is not yet a theorem

The cycle-length multiset in Theorem 4.1 is

\[
                         \{2,2,3,3,4\}.
\tag{5.1}
\]

It coincides with the multiset \(\{\ell(w)+1:w\in D_3\}\), where
\(\ell(w)\) is final-descent length.  This numerical coincidence does
not mean that \(c_1\) cycles the ECO siblings.  For example,
\(A=1234\) and \(B=1235\) are two children of the same root
\(111000\), but

\[
                            c_1(A)=L\ne B.
\tag{5.2}
\]

Thus the peak-insertion locality theorem alone does not prove even the
orbit partition, and it cannot presently be used as an odd-cycle census.

For reference, if a future proof established only the cycle-length
multiset identity, its consequence would be explicit.  The number of
Dyck words of semilength \(n\) with final descent \(d\) is

\[
 a_{n,d}=\frac{d}{2n-d}\binom{2n-d}{n}.
\tag{5.3}
\]

For fixed \(d\),

\[
 \frac{a_{n,d}}{C_n}\longrightarrow\frac{d}{2^{d+1}},
 \qquad
 \frac{a_{n,d}}{C_n}\le\frac{2d}{2^d}.
\tag{5.4}
\]

Dominated convergence then gives

\[
 \frac1{C_n}\sum_{d\ {\rm even}}a_{n,d}
 \longrightarrow
 \sum_{r\ge1}\frac{2r}{2^{2r+1}}
 =\sum_{r\ge1}\frac r{4^r}=\frac49.
\tag{5.5}
\]

Since \(C_{m-1}/C_m\to1/4\), the unproved multiset identity would imply

\[
                         \frac{o_1}{B}\longrightarrow\frac19.
\tag{5.6}
\]

Equation (5.6) is conditional and is not used anywhere in this report.
Even if true, one phase contributes only \(O(B)=o(W)\) forced edges.
Coefficient-one obstruction at the one-baseline scale requires information
on a positive proportion of the \(\Theta(m)\) phases, or a comparably dense
family of odd phase-word relations.

## 6. All-depth implication and exact boundary

At every proper interval length, one active selected slot makes two
adjacent transpositions and changes lower histogram support by at most
four.  Therefore, for every depth \(q\),

\[
 |h_q(S,A)-h_q(S,0)|\le4Z_K
 =\left(\frac{\alpha e^{-a^2}}4+o(1)\right)W.
\tag{6.1}
\]

The same holds for the upper trace by complementation.  This is a
statewise robustness bound, not a productive sign theorem.  Summing the
right side over \(\Theta(\sqrt m)\) depths is much larger than \(W\), so
separate rankwise capacity cannot yield aggregate \(o(W)\) holes.

The proved boundary is therefore:

1. A positive-density Catalan/Dyck trade bank exists and has more than
   enough literal packet rows for the corrected demand (0.1).
2. Its effective middle action on a selected family is exactly bounded at
   the scale (0.3)--(0.4).
3. The canonical complement graph has the phase-cycle decomposition
   (2.2), and the fixed-density obstruction constant is (3.6).
4. The phase maps are genuinely nonabelian already at \(m=4\); the
   proposed common rotation/promotion, and every shore construction based
   on alternating powers of it, is impossible.
5. No theorem here proves (3.6), constructs a common near-alternating
   shore, or aligns the same slot choices with all depths.  Consequently
   no positive Catalan trade family is yet proved to achieve simultaneously
   aggregate \(o(W)\) holes and \(o(W)\) middle collisions.

The next exact gate is not scalar trade supply.  It is either an
asymptotic odd-cycle/odd-relation census for the noncommuting family
\(\{c_t\}\), or a direct construction of one shore and one dependent
reciprocal mask satisfying the complete hereditary interval ledger.
