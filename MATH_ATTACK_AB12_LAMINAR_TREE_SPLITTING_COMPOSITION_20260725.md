# Lane AB12: exact AB--K laminar composition, persistent seams, and the carrier-supported splitting obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer experiment, or long-running local job is used. Every positive
construction below stays inside one literal integral exact middle wreath
factor. Every conditional switch is explicitly labelled conditional.

Status: theorem-level composition and no-go report. The requested
\(\Omega(W)\) productive splitting operation is **not** obtained. What is
proved is stronger than a failure to combine two estimates:

* after pruning the two overlapping packet colours, the menu-avoiding AB
  rounding and K's laminar half-packet preparation coexist in one exact
  product cube;
* the combined factor retains the AB super-\(W\) quadratic-energy gain and
  has only \(o(W)\) shallow action;
* nevertheless it still has \((1/16-o(1))W\) depth-one holes;
* every K-style shifted carrier having enough orbit capacity at depth \(H\)
  has vanishing owner density, and even polynomially many such carriers have
  only \(o(W)\) total shallow action;
* K's \((11/128-o(1))W\) seam reservoir survives the pruned AB rounding with
  no loss, but each such seam is an internal middle-root edge of one fresh
  component and its natural rank-\((m-1)\) core is fixed by the fresh colour;
  it is therefore not a clean occurrence-pair split;
* a fixed layered use of K's spanning tree has exactly one ownership bundle
  and hence zero productive splitting;
* within K10's stated component-monochromatic lift, the only remaining use is
  genuinely sequential recomputation with positive-density collateral rows.
  K's current theorems do not control those rows or their loss.

Thus the proposed *controlled-carrier* completion is disproved. The literal
composition itself is productive: it preserves both the AB rounded family and
K's full seam constant. A successful nonlocal completion must additionally
control remote lower-shadow occurrences across recomputed components. For the
one-stage clean-pair operation isolated in Section 10, this means controlling
signed-cycle frustration under the same all-depth signing. That conclusion
cannot be obtained from the existing laminar TU signing, orbit-capacity
allocation, or static spanning-tree word.

---

## 0. Notation and exact verdict

Fix \(A>0\), and put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\operatorname{Cat}_m=\frac Wn,\qquad
 H=\lceil A\sqrt m\rceil .                            \tag{0.1}
\]

At depth \(q\le H\), write

\[
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+\rho_q,\quad 0\le\rho_q<N_q,                \tag{0.2}
\]

\[
 S_A(m)=\sum_{q=1}^H\frac1{c_q}
       =(\kappa_A+o_A(1))\sqrt m,                     \tag{0.3}
\]

where

\[
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}. \tag{0.4}
\]

Let \(O_q(F)\) be the exact balanced-quota overload and

\[
 J_A(F)=\sum_{q=1}^H\frac{O_q(F)}{c_q}.               \tag{0.5}
\]

Put

\[
 s_0=\left\lceil\frac{3H}{4}\right\rceil.             \tag{0.6}
\]

The exact positive composition uses:

1. K's unshifted laminar packets

   \[
   K_R=\{1100R,1010R\},
   \qquad R\in\mathcal D_{m-2};                       \tag{0.7}
   \]

2. K's shifted orbit carrier of colour \(s_0\);
3. the AB6 packet blocks of colours

   \[
   \mathcal S^*
   =\{3,4,\ldots,m-H-2\}\setminus\{s_0\}.             \tag{0.8}
   \]

The AB packet count is

\[
 K^*
 =\sum_{u=H}^{m-5}\operatorname{Cat}_u
  -\operatorname{Cat}_{m-s_0-2}.                     \tag{0.9}
\]

The main positive theorem constructs exact factors
\(F_{\mathrm{lam}}^\sharp,F_{\mathrm{lam}}^{\mathrm{rd}}\) in one joint
packet cube. Every retained AB bridge avoids a full connected K menu that
still carries \((7/128-o(1))W\) seams and, after one global conjugation, also
avoids any fixed AB8/K9 protected menu.
They obey

\[
 \boxed{
 \mathcal Q_H(F_{\mathrm{lam}}^\sharp)
 -\mathcal Q_H(F_{\mathrm{lam}}^{\mathrm{rd}})
 >
 K^*\left[
 \frac{4^H}{32L_AH^4}-(2H-1)
 \right],}                                           \tag{0.10}
\]

where \(L_A=e^{2(A+1)(A+2)}\), and

\[
 \frac{
 \mathcal Q_H(F_{\mathrm{lam}}^\sharp)
 -\mathcal Q_H(F_{\mathrm{lam}}^{\mathrm{rd}})
 }W\longrightarrow\infty.                            \tag{0.11}
\]

If \(r^*\) is the number of AB packet signs changed by the balanced
rounding, then

\[
 r^*=\frac{K^*}{2}+O(m)                              \tag{0.12}
\]

and

\[
 \boxed{
 |J_A(F_{\mathrm{lam}}^{\mathrm{rd}})
   -J_A(F_{\mathrm{lam}}^\sharp)|
 \le
 \left(\frac{\kappa_A}{768}+o_A(1)\right)
 \frac W{\sqrt m}.}                                  \tag{0.13}
\]

K's laminar preparation itself also has \(o(W)\) shallow action. Yet the
combined exact endpoint satisfies

\[
 \boxed{
 M_1(F_{\mathrm{lam}}^{\mathrm{rd}})
 \ge\left(\frac1{16}-o(1)\right)W,
 \qquad
 J_A(F_{\mathrm{lam}}^{\mathrm{rd}})
 \ge\left(\frac1{16}-o(1)\right)W.}                  \tag{0.14}
\]

The K orbit-tree allocation cannot remove this obstruction on its proved
carrier. Even granting arbitrary rowwise permutations of every shifted
carrier row, the full controlled composition still obeys

\[
 \boxed{M_1\ge(1/16-o(1))W}                          \tag{0.15}
\]

and has only \(o(W)\) total weighted shallow action.

This is not a contradiction: an \(o(W)\)-action operation cannot fill
\(\Theta(W)\) old holes. K's positive-density middle-root movement can change
future component geometry dramatically, but K proves no target-disjoint
first-shadow split from that movement.

---

## 1. The legal pruned product cube

For a Dyck word \(Z\), write \(\operatorname{ir}(Z)\) for its initial run of
ones.

### Lemma 1.1 (owner and root disjointness)

The three carrier families in (0.7)--(0.8) are pairwise owner-disjoint:

* the rows \(1100R\) and \(1010R\) have initial run two and one,
  respectively;
* every row in the shifted colour-\(s\) packet block has initial run exactly
  \(s\);
* distinct shifted colours have distinct initial runs.

Consequently K's unshifted packets, K's shifted \(s_0\)-carrier, and all
retained AB blocks in \(\mathcal S^*\) have pairwise disjoint canonical
middle-root unions.

#### Proof

The first two assertions follow by inspection. For
\(P_s=1^s0^s\), both \(P_s1100R\) and \(P_s1010R\) begin with exactly \(s\)
ones because the next symbol in \(P_s\) is zero. The retained indices satisfy
\(s\ge3\) and omit \(s_0\), proving owner disjointness.

An exact factor partitions the middle roots by owner rows. Hence disjoint
owner families own disjoint root unions. Each two-for-two component switch
preserves its complete invariant root union. Therefore all side choices in
the product of these packet cubes remain mutually root-disjoint. \(\square\)

### Lemma 1.2 (persistent exactness)

Every choice of sides in this joint packet cube is a literal integral exact
factor. At every cube vertex, each packet is still one complete component of
the freshly recomputed overlay for its own transposition.

#### Proof

Each audited packet is a genuine two-row ownership component. Its two shores
partition the same invariant middle-root union. By Lemma 1.1 the unions of
different packets are disjoint. Fix one packet, let \(U\) be its root union,
and let \(\tau\) be its colour. Then \(\tau U=U\). If \(U'\) is any other
packet union, \(U'\cap U=\varnothing\), and therefore

\[
 \tau U'\cap U
 =\tau(U'\cap\tau^{-1}U)
 =\tau(U'\cap U)
 =\varnothing.                                      \tag{1.1}
\]

Thus the right shore of a changed packet cannot create a new
\(\tau\)-ownership edge into \(U\), even though \(U'\) need not itself be
\(\tau\)-invariant. Applying this to every other packet proves that the fixed
packet remains a complete freshly recomputed component. The product choice
partitions all middle roots exactly once, so every vertex is integral and
exact. \(\square\)

The pruning is essential. The unshifted rows have initial runs one and two,
so the colour-two AB block can overlap them. The colour-\(s_0\) AB block is
the shifted K carrier itself.

---

## 2. Simultaneous menu avoidance

Let

\[
 \mathcal T^*=\{\tau_s=(2s+2\ \ 2s+3):s\in\mathcal S^*\}. \tag{2.1}
\]

This is a coordinate matching.

K's orbit tree consists of:

* a path on the always-in atom \(\mathcal I_{s_0}^+\);
* a path on the always-out atom \(\mathcal Z_{s_0,H}^+\);
* one edge joining those paths; and
* the edge \((\beta_{s_0}\ \gamma_{s_0})=\tau_{s_0}\).

### Lemma 2.1 (tree avoiding the AB matching)

The two internal paths and their joining edge can be chosen so that K's whole
orbit tree is edge-disjoint from \(\mathcal T^*\).

#### Proof

The forbidden graph \(\mathcal T^*\) is a matching. On either K atom \(V\),
the graph \(K_V-\mathcal T^*\) has minimum degree at least \(|V|-2\). For all
sufficiently large \(m\), both atoms have at least four vertices, and hence

\[
 |V|-2\ge |V|/2.
\]

Dirac's theorem supplies a Hamilton cycle in each atom. Choose first an
allowed cross-atom pair \(iz\); such a pair exists because deleting a matching
cannot exhaust the complete bipartite set of cross pairs. Break the first
Hamilton cycle at an edge incident with \(i\), and the second at an edge
incident with \(z\). The resulting Hamilton paths have endpoints \(i,z\), so
joining them by \(iz\) gives the required allowed internal paths and joining
edge. Finally \(\tau_{s_0}\notin\mathcal T^*\) by the pruning in (0.8).
\(\square\)

The tree can be placed in a full K menu without reusing any retained AB
bridge label, at the cost of an explicit seam constant.

### Lemma 2.2 (a bridge-disjoint full K menu)

For all sufficiently large \(m\), there is a near-perfect coordinate matching
\(M_0\supseteq\mathcal T^*\), a K Hamilton path \(P_m\), and a productive
near-perfect seam matching \(\mathcal R_m^0\) such that

\[
 (P_m\cup\mathcal R_m^0)\cap M_0=\varnothing        \tag{2.2}
\]

and the colours in \(\mathcal R_m^0\) support at least

\[
 \boxed{\left(\frac7{128}-o(1)\right)W}             \tag{2.3}
\]

distinct K seams. In particular the entire connected orbit menu
\(\mathcal O_m^0=P_m\cup\mathcal R_m^0\) is label-disjoint from every
retained AB bridge.

#### Proof

Extend the matching \(\mathcal T^*\) to a near-perfect matching \(M_0\),
choosing the extension not to contain \(\tau_{s_0}\). This is possible because
for all sufficiently large \(m\), \(|\mathcal S^*|=m-H-5\), so exactly
\(2H+11\) coordinates are left unmatched by \(\mathcal T^*\), including the
two endpoints of \(\tau_{s_0}\). Pair those two endpoints with two distinct
other free coordinates and complete the matching, leaving one coordinate
unmatched. Apply Lemma 2.1 with the larger forbidden matching \(M_0\). The
joined atom path and the prescribed \(\tau_{s_0}\)-edge form a two-component
linear forest in \(K_n-M_0\). Of the four endpoint pairs between its two path
components, a matching forbids at most two, so an allowed pair joins them.
The \(r=n-O(H)\) unused vertices span a complete graph minus a matching, of
minimum degree at least \(r-2\ge r/2\), and hence have a Hamilton cycle.
Choose on that cycle a vertex other than the possible \(M_0\)-mate of a path
endpoint, break an incident cycle edge, and attach the resulting path. This
gives a Hamilton completion \(P_m\subseteq K_n-M_0\).

Choose a near-one-factorization of the odd complete graph \(K_n\) having
\(M_0\) as one of its \(n\) near-perfect colour classes. Let \(\mathcal E\) be K's
selected laminar root set and put \(p=|\mathcal E|/W\to1/16\). Before choosing
a matching class, K's proof supplies

\[
 T_m\ge\left(\frac{11}{128}-o(1)\right)nW           \tag{2.4}
\]

counted boundary seams. For a fixed \(X\in\mathcal E\), at most \(m\)
transpositions of the coordinate matching \(M_0\) move \(X\). Hence the
excluded class contains at most

\[
 m|\mathcal E|
 =\left(\frac1{16}+o(1)\right)mW.                  \tag{2.5}
\]

counted seams. The other \(n-1=2m\) classes therefore contain in total at
least

\[
 \left(\frac7{64}-o(1)\right)mW.                   \tag{2.6}
\]

One of them, denoted \(\mathcal R_m^0\), contains at least (2.3). It is a
different factorization class from \(M_0\), so it is edge-disjoint from
\(M_0\). \(\square\)

Now fix an arbitrary AB8/K9 protected menu \(\mathcal M\) whose coordinate
components have size below \(m\), as in AB10. Its complement contains a
matching of size \(m\). Since \(|\mathcal T^*|\le m\), one coordinate
permutation \(g\) maps \(\mathcal T^*\) into that complement. Conjugate the
entire joint construction, including K's full menu, by \(g\).

Conjugation preserves the disjointness in Lemma 2.2. Thus:

\[
 g\mathcal T^*g^{-1}\cap\mathcal M=\varnothing,
 \qquad
 g\mathcal T^*g^{-1}\cap g\mathcal O_m^0g^{-1}
 =\varnothing.                                       \tag{2.7}
\]

The first statement is avoidance of the fixed protected menu. The second is
avoidance of K's conjugated full menu. It does **not** mean that the
conjugated K menu equals the original un-conjugated menu; all of K's
membership-atom formulas must be conjugated with it.

This is a statement about the simultaneous starting packet cube. Distinct
coordinate labels do not imply that a later complete component in a fresh
K-menu overlay avoids the retained AB root unions. Such a component may
contain and move AB rows. Consequently neither the AB packet persistence nor
the cost of a genuinely sequential K cut follows from (2.7); that would
require a protected-carrier theorem for the freshly recomputed components.

---

## 3. Exact positive composition

K's laminar theorem chooses

\[
 k_{\mathrm{lam}}
 =\sum_Rx_R
 =\frac12\operatorname{Cat}_{m-2}+O(1)               \tag{3.1}
\]

unshifted size-two packets and switches their complete components. Fix this
laminar endpoint as the background of the retained AB packet cube.

For an AB block \(s\), put \(k_s=\operatorname{Cat}_{m-s-2}\), and use the
audited quantities

\[
 \Lambda_s=\|D_s\|_H^2-V_s.                          \tag{3.2}
\]

The shifted-pile and packet-action theorems give

\[
 \frac{\Lambda_s}{4}
 >
 k_s\left[
 \frac{4^H}{32L_AH^4}-(2H-1)
 \right].                                            \tag{3.3}
\]

### Theorem 3.1 (literal pruned AB--K composition)

There is a coherent retained-AB endpoint
\(F_{\mathrm{lam}}^\sharp\) over K's literal laminar background and a
balanced retained-AB endpoint \(F_{\mathrm{lam}}^{\mathrm{rd}}\) satisfying
(0.10). Every intermediate packet microstep is a literal integral exact
factor.

#### Proof

Lemma 1.2 supplies one heterogeneous exact packet cube. Treat the fixed
laminar choice and every omitted packet as part of the affine background.
Choose the retained AB coherent signs backward, exactly as in the AB6
balanced-block theorem. Balanced resampling in block \(s\) has expected gain
at least

\[
 \frac14\left(1+\frac1{\kappa_s}\right)\Lambda_s
 \ge\frac{\Lambda_s}{4}.                             \tag{3.4}
\]

The finite product distribution has a deterministic outcome attaining its
mean total gain. Sum (3.3) over \(s\in\mathcal S^*\). Exactness of every
microstep is Lemma 1.2. \(\square\)

### Lemma 3.2 (retained packet density)

\[
 \boxed{\frac{K^*}{B}\longrightarrow\frac1{768}.}    \tag{3.5}
\]

#### Proof

Writing \(u=m-j\), the unpruned sum in (0.9) begins at \(j=5\). Hence

\[
 \frac1B\sum_{u=H}^{m-5}C_u
 \longrightarrow\sum_{j=5}^{\infty}4^{-j}
 =\frac1{768}.                                       \tag{3.6}
\]

Since \(s_0\to\infty\),

\[
 \frac{C_{m-s_0-2}}B=O_A(4^{-s_0})=o(1).             \tag{3.7}
\]

Subtracting proves (3.5). \(\square\)

Since the bracket in (0.10) grows faster than every polynomial and
\(K^*/W\sim1/(768n)\), equation (0.11) follows.

Balanced rounding changes

\[
 r^*=\frac{K^*}{2}+O(|\mathcal S^*|)
     =\frac{K^*}{2}+O(m)                             \tag{3.8}
\]

packet signs. One packet has half-\(\ell^1\) action two at depth one and
four at every depth \(2,\ldots,H\). Therefore

\[
 |J_A(F_{\mathrm{lam}}^{\mathrm{rd}})
   -J_A(F_{\mathrm{lam}}^\sharp)|
 \le r^*(4S_A-2).                                    \tag{3.9}
\]

Equations (0.3), (3.5), \(B=W/n\), and \(n\sim2m\) give the leading constant
\(\kappa_A/768\) in (0.13).

K's laminar preparation changes \(k_{\mathrm{lam}}\) packet signs, so its
entire shallow action is at most

\[
 k_{\mathrm{lam}}(4S_A-2)
 =O_A(B\sqrt m)
 =O_A(W/\sqrt m)
 =o(W).                                              \tag{3.10}
\]

Thus the positive composition is literal, menu-avoiding, productively rounded
in \(\mathcal Q_H\), and shallow-stable.

---

## 4. The composed factor still has a linear first-shadow obstruction

Let

\[
 J_m=(2m-3)\operatorname{Cat}_{m-2},
 \qquad
 \rho_1=\frac{2W}{m+2}.                               \tag{4.1}
\]

The marked-gap theorem gives

\[
 M_1(F_m^{\mathrm{MSW}})\ge J_m-\rho_1.              \tag{4.2}
\]

Every two-for-two packet toggle has exactly two positive first-shadow cells,
so it fills at most two old holes.

### Theorem 4.1 (linear holes survive the legal composition)

\[
 \boxed{
 M_1(F_{\mathrm{lam}}^{\mathrm{rd}})
 \ge
 J_m-\rho_1-2K^*-2k_{\mathrm{lam}}
 =\left(\frac1{16}-o(1)\right)W.}                    \tag{4.3}
\]

Consequently (0.14) holds.

#### Proof

Relative to the canonical corner, the terminal retained-AB vertex differs in
at most \(K^*\) packet signs. K's laminar endpoint differs in exactly
\(k_{\mathrm{lam}}\) packet signs. The carrier families are disjoint, so
these toggles may be ordered arbitrarily. At each toggle the hole count can
drop by at most two. This proves the first inequality.

Now

\[
 \frac{J_m}{W}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}
 \longrightarrow\frac1{16},                         \tag{4.4}
\]

while \(\rho_1=o(W)\), \(K^*=O(B)=o(W)\), and
\(k_{\mathrm{lam}}=O(B)=o(W)\). Finally
\(J_A\ge O_1\ge M_1\). \(\square\)

This theorem already rules out a direct repair by the legal packet
composition. K's remaining positive theorem is the shifted orbit-tree route,
which is considered next.

---

## 5. The controlled shifted carrier has \(o(W)\) action

K's shifted colour \(s_0\) has

\[
 R_0=\operatorname{Cat}_{m-s_0-2}                   \tag{5.1}
\]

two-row packets, hence \(2R_0\) carrier rows.

Even grant the strongest nonphysical relaxation: allow each carrier row to be
replaced by an arbitrary coordinate permutation of itself, with no component
compatibility condition. At every depth one row has \(n\) occurrences, so
the half-\(\ell^1\) distance between its old and new load vectors is at most
\(n\).

### Theorem 5.1 (optimistic controlled-carrier ceiling)

Let \(F_{\mathrm{comp}}\) be any endpoint obtained from the conjugated
canonical factor using at most \(K^*\) retained AB packet toggles and the
\(k_{\mathrm{lam}}\) laminar packet toggles. Let \(G_{\mathrm{ctrl}}\) be
obtained from \(F_{\mathrm{comp}}\) only by arbitrary coordinate
permutations of all \(2R_0\) shifted carrier rows, even if these rowwise
replacements are optimistically assumed to preserve exactness. Then

\[
 \boxed{
 M_1(G_{\mathrm{ctrl}})
 \ge
 J_m-\rho_1-2K^*-2k_{\mathrm{lam}}-2nR_0
 =\left(\frac1{16}-o(1)\right)W,}                   \tag{5.2}
\]

and the complete weighted shallow action is at most

\[
 \boxed{
 (K^*+k_{\mathrm{lam}})(4S_A-2)
 +2nR_0S_A
 =o(W).}                                             \tag{5.3}
\]

#### Proof

The packet bounds were proved above. Arbitrarily replacing one row can fill at
most \(n\) old depth-one holes and has half-\(\ell^1\) action at most \(n\)
at each depth. This gives the first expressions in (5.2)--(5.3).

The Catalan ratio satisfies

\[
 \frac{R_0}{B}=O_A(4^{-s_0})                         \tag{5.4}
\]

with \(s_0\asymp H\). Therefore

\[
 \frac{2nR_0}{W}=2\frac{R_0}{B}=o(1),                \tag{5.5}
\]

and

\[
 \frac{2nR_0S_A}{W}
 =2\frac{R_0}{B}S_A=o(1).                            \tag{5.6}
\]

The packet term in (5.3) is \(O_A(B\sqrt m)=o(W)\).
Substitute these estimates and (4.4). \(\square\)

At depth one, the limitation is even more direct. A K cylinder has
\(C_1=1\) certified lower tag. It contains no certified duplicate pair to
split. The number of certified lower depth-one tags is only

\[
 \operatorname{Cat}_{m-s_0-3}=o(W).                 \tag{5.7}
\]

The complementary marked tag lies in the upper layer and does not turn
(5.7) into a depth-one \((0,2)\) certificate.

Thus K's explicit orbit allocation routes a sparse tagged subledger. It does
not split the marked-gap first-shadow duplicates from Theorem 4.1.

---

## 6. A general density--orbit-capacity obstruction

The choice \(s_0=3H/4+O(1)\) is not the source of the scale mismatch. It is
forced, up to a weaker logarithmic bound, by the deepest Catalan pile.

Consider a K-style shifted carrier of arbitrary parameter \(s\ge0\). At
depth \(H\), its movable atom has size

\[
 u=2s+2H+5,                                          \tag{6.1}
\]

and its private target contains \(a=s+2\) points from that atom. The K orbit
has

\[
 Q_H=2\binom{2s+2H+5}{s+2}                           \tag{6.2}
\]

possible targets, while one private cylinder has \(C_H\) certified tags.
Injective routing requires

\[
 Q_H\ge C_H.                                         \tag{6.3}
\]

### Theorem 6.1 (capacity forces vanishing carrier density)

Assume (6.3). Then either \(s>H\), or

\[
 \boxed{
 s\ge
 \frac{H\log4-\log(8H^2)}{\log(4H+5)}-2.}            \tag{6.4}
\]

Consequently, for every such carrier,

\[
 \frac{\operatorname{Cat}_{m-s-2}}B
 \le2^{-(s+2)}
 =\exp\!\left[-\Omega\!\left(\frac H{\log H}\right)\right]. \tag{6.5}
\]

For \(H=\lceil A\sqrt m\rceil\), even \(m^d\) such carriers, for any fixed
\(d\), have total *direct rowwise carrier-supported* all-depth action
\(o(W)\).

#### Proof

For \(H\ge2\),

\[
 C_H\ge\frac{4^H}{4H^2}.                             \tag{6.6}
\]

If \(s\le H\), then \(2s+2H+5\le4H+5\), and

\[
 Q_H
 \le2(4H+5)^{s+2}.                                   \tag{6.7}
\]

Combine (6.3), (6.6), and (6.7), then take logarithms. This gives (6.4).
If \(s>H\), the conclusion that \(s\to\infty\) is stronger.

For \(r\ge2\),

\[
 \frac{C_{r-1}}{C_r}
 =\frac{r+1}{4r-2}\le\frac12.                        \tag{6.8}
\]

Iterating (6.8) proves the first inequality in (6.5).

Let \(P(m)\le m^d\) be the number of carriers, with parameters
\(s_1,\ldots,s_{P(m)}\). Their total rowwise all-depth action, divided by
\(W\), is at most

\[
 2H\sum_{i=1}^{P(m)}2^{-(s_i+2)}
 \le 2P(m)H
       \exp\!\left[-\Omega\!\left(\frac H{\log H}\right)\right].
                                                               \tag{6.9}
\]

By (6.4), or by the stronger alternative \(s_i>H\), the negative logarithm
of every \(2^{-s_i}\) is
\(\Omega(H/\log H)\), which dominates
\(\log P(m)+\log H=O(\log m)\) when \(H\asymp\sqrt m\). Thus (6.9) tends
to zero. \(\square\)

### Corollary 6.2

Retuning \(s\) to \(O(1)\) gives a positive-density carrier but destroys
depth-\(H\) capacity: \(Q_H\) is polynomial in \(H\), whereas
\(C_H=4^H/\operatorname{poly}(H)\). Retaining the K orbit-capacity mechanism
forces a sparse carrier and cannot directly service \(\Theta(W)\)
first-shadow pairs.

This closes every polynomial-size union of K-style shifted carriers as a
direct carrier-supported splitting operation. It does **not** say that an
\(o(W)\)-action laminar preparation cannot change the geometry of a later
fresh overlay: K's preparation moves a positive density of middle roots, and
future components may drag rows lying outside the sparse carrier. Sections 10
and 11 quantify precisely what such an indirect route would still have to do.

---

## 7. Why the seam reservoir does not supply the missing split

K's laminar preparation creates a middle-root set whose fresh overlays carry

\[
 \left(\frac{11}{128}-o(1)\right)W                  \tag{7.1}
\]

genuine commutator seams across a coordinate matching. This is the only
proved \(\Theta(W)\) resource in the K menu. First, this resource really does
compose with the AB rounding.

### Theorem 7.1 (all K seams survive the pruned AB rounding)

At every retained-AB endpoint over the fixed K-laminar background, with the
shifted \(s_0\) carrier kept on its certified side, every seam counted in K's
original matching remains a distinct loopless non-native seam of the freshly
recomputed overlay of the same colour. Thus the unrestricted joint factor
retains the full constant in (7.1). For the fully bridge-disjoint menu of
Lemma 2.2, the retained constant is \(7/128\).

#### Proof

It is enough to use the native labels; a simultaneous global conjugation
preserves the argument. Put \(\tau=(2\ 3)\), let \(\mathcal E\) be K's
selected root union, and let \(\alpha\) be the joint piecewise root
involution. Thus \(\alpha=\tau\) on \(\mathcal E\),
\(\alpha=\eta_j=\tau_{s_j}\) on each retained AB cell whose packet is
switched, and \(\alpha=1\) on all other root cells. These cells are disjoint
complete canonical root unions and are invariant under their displayed
involutions, so \(\alpha\) is a well-defined involutive bijection. Every
retained \(\eta_j\) has support disjoint from \(\{2,3\}\).

Take one K-counted boundary edge

\[
 X\longleftrightarrow\rho X,qquad
 X\in\mathcal E,\quad \tau X\ne X,\quad
 \rho X\notin\mathcal E,                            \tag{7.2}
\]

where \(\rho\) is its coordinate-transposition colour. Put \(Y=\tau X\).
The pulled-back fresh relation is \(\theta_\rho=\alpha\rho\alpha\), and

\[
 \theta_\rho(Y)=\alpha\rho X=\gamma\rho X,          \tag{7.3}
\]

where \(\gamma=1\) unless \(\rho X\) lies in a switched AB cell, in which
case \(\gamma=\eta_j\) for that cell. If \(\gamma=1\), (7.3) differs from
the native transition \(\rho Y=\rho\tau X\) because \(\tau X\ne X\).

Suppose \(\gamma=\eta_j\) and, contrary to the claim, (7.3) equals
\(\rho\tau X\). Then the transposition

\[
 \kappa=\rho\eta_j\rho
\]

satisfies \(\kappa X=\tau X\). Since \(\tau X\ne X\), the symmetric
difference \(X\triangle\tau X=\{2,3\}\). A transposition moving \(X\) has
its support equal to the symmetric difference between \(X\) and its image,
so \(\kappa=\tau\). Hence \(\eta_j=\rho\tau\rho\). But conjugating
\((2\ 3)\) by a single transposition leaves at least one of the coordinates
2 or 3 in its support, whereas \(\eta_j=\tau_{s_j}\), \(s_j\ge3\), contains
neither. This is impossible.

The image under the bijection \(\alpha\) of a counted boundary edge remains
loopless because \(\mathcal E\) and every AB cell are unions of disjoint
complete canonical owner blocks. Bijectivity also preserves distinctness of
the counted seams. The last assertion now follows from Lemma 2.2. \(\square\)

The preservation theorem is static: it applies to the rounded endpoint before
any seam-colour component is cut. Four distinctions are still decisive.

### 7.2 A seam is not a first-shadow constraint

A seam is a Johnson edge between middle roots. K does not prove that the
intersection of those roots is a cyclic rank-\((m-1)\) occurrence in either
relevant owner row. It therefore does not give a moved target pair
\((S,\sigma S)\) with load \((0,2)\), two unit component coefficients, or
target-disjointness.

The audited direct-alignment theorem supplies at most \(4B=o(W)\) directly
first-shadow-aligned owner incidences for one fresh colour. The remaining
seams may be useful through nonlocal containment, but no such theorem is
proved.

There is an exact local obstruction. For a seam (7.2), its natural
rank-\((m-1)\) core is

\[
 C=X\cap\rho X.                                     \tag{7.4}
\]

The set \(C\) contains neither exchanged coordinate and is therefore fixed
by \(\rho\). If it is a cyclic occurrence in an incident row, its load is a
fixed-target contribution and is invariant under every component-side choice.
Hence one seam creates **zero** clean moved \((0,2)\) constraints by this
local core map. Any productive conversion must pair remote lower-shadow
occurrences belonging to two different fresh components.

### 7.3 Seams need not be dispersed among components

Seams are ownership edges. Many seams may lie in one connected ownership
component. A connected overlay has only the two whole-factor sides and cannot
split even one \((0,2)\) pair between distinct component signs.

Thus the numerical inequality \(11/128>1/16\) has no splitting implication.
K explicitly proves neither distinct-component dispersion nor a targetwise
occurrence-pair map.

Indeed, a seam is itself one ownership edge and therefore lies **inside** one
fresh component. The two owners incident with that seam cannot be the two
different component vertices required by the clean constraint graph of
Section 10.

### 7.4 The seam statements are not sequentially persistent

Theorem 7.1 proves that all counted seams persist through the static pruned AB
rounding. They are still certified in separate fresh-colour overlays of that
one rounded factor. After one seam colour is actually cut and components are
recomputed, neither K nor Theorem 7.1 proves that another matching-colour seam
persists. Label-disjointness does not protect a complete recomputed component
from entering AB or K root cells belonging to other labels.

These are failures of exact hypotheses, not semantic distinctions.

---

## 8. Static use of the connected menu gives zero splitting

K completes its menu to a Hamilton path on all \(n\) coordinates. Hence the
menu contains a coordinate spanning tree and generates \(S_n\).

### Theorem 8.1 (fixed layered collapse)

For every exact factor \(F\), take any fixed layered word containing the
pulled-back edges of K's coordinate spanning tree. The joined endpoint
ownership partition has one block. Consequently its endpoint bundle cube has
only the two choices

\[
 F,\qquad \sigma F,                                  \tag{8.1}
\]

where \(\sigma\) is the word product. The two endpoints are global coordinate
relabelings, have the same \(J_A\) and hole count, and split zero duplicate
pairs into independently signable bundles.

#### Proof

For a set \(T\) of transposition colours, every block of the join of the
individual ownership partitions owns a root union invariant under
\(\langle T\rangle\). If \(T\) contains a coordinate spanning tree, then
\(\langle T\rangle=S_n\), which is transitive on the rank-\(m\) roots.
Therefore the join has one block.

The layered endpoint theorem says each endpoint bundle independently chooses
its first or last shore. With one bundle, only the two whole shores in (8.1)
remain. Coordinate relabeling permutes target coordinates and preserves all
quota distances. \(\square\)

Thus K's coherent group-orbit allocation cannot be lifted by treating the
whole tree word as one static endpoint cube. K10's proposed
component-monochromatic lift would instead have to use a genuinely sequential
history with fresh component recomputation. This does not rule out unrelated
direct short-permutation overlays or multistage repairs outside that route.

---

## 9. Laminar TU does not survive the component quotient

K's laminar signing matrix is TU before physical component identifications.
At a routing stage, however, packets lying in the same freshly recomputed
ownership component must receive the same action bit.

### Proposition 9.1 (minimal quotient obstruction)

There is a laminar half-balance system and one component equality whose
quotient has no integral solution.

#### Proof

Take two packet indices \(i,j\) and the laminar row

\[
 L=\{i,j\}.
\]

Half-balance requires

\[
 x_i+x_j=1.                                          \tag{9.1}
\]

If one fresh ownership component identifies their route bits, physical
component coherence imposes

\[
 x_i=x_j=y.                                          \tag{9.2}
\]

The quotient of (9.1) is

\[
 2y=1,                                               \tag{9.3}
\]

which has no integral solution. Equivalently, the quotient matrix contains
an entry two and is not totally unimodular. \(\square\)

This proposition does not assert that the displayed equality necessarily
occurs in K's exact factor. It proves that laminarity alone gives no
component-quotient theorem. K's component-monochromatic hypothesis is a real
additional condition, not an automatic consequence of laminar TU.

---

## 10. The explicit split operation that would work

For clarity, the exact physical operation needed after a sequential menu
stage can be stated without fractional language.

Fix a current exact factor \(F\), a transposition \(\sigma\), and its freshly
recomputed complete ownership components \(\mathscr C\). Let \(\mathcal P\)
be a target-disjoint family of depth-one moved pairs

\[
 p=\{S,\sigma S\}
\]

whose current loads are \((0,2)\). Record the component containing each of
the two unit occurrences at the overloaded target, with multiplicity.

Define the component constraint multigraph

\[
 \Gamma_{\sigma,\mathcal P}
\]

with vertex set \(\mathscr C\) and one edge for every \(p\in\mathcal P\),
whose endpoints are its two occurrence components. Parallel edges are kept.
If both occurrences lie in one component, the edge is a loop.

For a component signing \(\varepsilon\in\{\pm1\}^{\mathscr C}\), define

\[
 \operatorname{fr}_\varepsilon(\Gamma)
 =\#\{uv\in E(\Gamma):\varepsilon_u=\varepsilon_v\}, 
                                                               \tag{10.1}
\]

where a loop is always counted, and put

\[
 \operatorname{fr}(\Gamma)
 =\min_\varepsilon\operatorname{fr}_\varepsilon(\Gamma).
                                                               \tag{10.2}
\]

### Theorem 10.1 (exact MaxCut splitting operation)

For every component signing \(\varepsilon\), switching exactly its negative
components produces a literal integral exact factor, and the number of
designated depth-one holes left is exactly

\[
 \operatorname{fr}_\varepsilon
   (\Gamma_{\sigma,\mathcal P}).                    \tag{10.3}
\]

Consequently the maximum number of repaired pairs is

\[
 \operatorname{MaxCut}(\Gamma_{\sigma,\mathcal P}), 
                                                               \tag{10.4}
\]

and the optimal residual is exactly

\[
 \boxed{
 \operatorname{fr}(\Gamma)
 =|E(\Gamma)|-\operatorname{MaxCut}(\Gamma),}        \tag{10.5}
\]

which is also the minimum number of edges that must be deleted to make the
multigraph bipartite.

#### Proof

For an edge \(uv\), exactly one duplicate occurrence moves to the opposite
target precisely when \(\varepsilon_u=-\varepsilon_v\). The pair then becomes
\((1,1)\). If the endpoint signs agree, either neither occurrence or both
occurrences move, leaving \((0,2)\) or \((2,0)\), and hence exactly one hole.
A loop can never be cut. Target-disjointness makes these statements
simultaneous. Every switched object is a complete freshly recomputed
ownership component, so the child is literal, integral, and exact. This
proves (10.3)--(10.5).

For the last characterization, delete the monochromatic edges of an optimal
signing; all remaining edges cross its two colour classes, so the remainder is
bipartite. Conversely, a bipartition after deleting \(r\) edges gives a
signing with at most \(r\) monochromatic edges. \(\square\)

The unsigned component-incidence matrix of these clean rows has two unit
entries on a nonloop edge and one entry two on a loop. It is totally
unimodular exactly when \(\Gamma\) is bipartite: for a bipartite graph,
negating the columns of one vertex class gives an oriented incidence matrix;
a loop gives a \(1\times1\) minor of determinant two, and an odd cycle gives
an odd-cycle minor of determinant two. Thus (10.5) is also the exact failure
of the clean depth-one TU system.

There is an exact all-depth loss certificate, not merely a graph analogy.
For every moved pair at depth \(q\), use AB10's invariant pair total
\(\ell_{q,p}\), parity \(\pi_{q,p}=\ell_{q,p}\bmod2\), signed component
sum \(D_{q,p}(\varepsilon)\), and orbit-profile floor
\(\Delta_q^\sigma\). For a selected clean pair at depth one,

\[
 \frac12\bigl(|D_{1,p}(\varepsilon)|-\pi_{1,p}\bigr)
 =\mathbf1_{\{\varepsilon_u=\varepsilon_v\}}.       \tag{10.6}
\]

Therefore AB10's exact profile theorem, split into the selected clean rows and
all other rows, gives for every common signing

\[
 \boxed{
 \begin{aligned}
 J_A(F_\varepsilon)
 \le{}&\sum_{q=1}^H\frac{\Delta_q^\sigma}{c_q}
       +\operatorname{fr}_\varepsilon(\Gamma)\\
 &+\frac12
   \sum_{\substack{1\le q\le H,\ p\text{ moved}\\
                    (q,p)\notin\{1\}\times\mathcal P}}
   \frac{|D_{q,p}(\varepsilon)|-\pi_{q,p}}{c_q}.
 \end{aligned}}                                     \tag{10.7}
\]

Thus an actual \(o(W)\)-loss split would follow from one freshly recomputed
stage and one common signing satisfying

\[
 |\mathcal P|\ge(1/16-o(1))W,                       \tag{10.8}
\]

\[
 \sum_q\frac{\Delta_q^\sigma}{c_q}=o(W),\qquad
 \operatorname{fr}_\varepsilon(\Gamma)=o(W),        \tag{10.9}
\]

and

\[
 \frac12
   \sum_{(q,p)\notin\{1\}\times\mathcal P}
   \frac{|D_{q,p}(\varepsilon)|-\pi_{q,p}}{c_q}
 =o(W).                                              \tag{10.10}
\]

Equations (10.8)--(10.10) are sufficient with the correct common-signing
quantifier order. Near-bipartiteness alone is not sufficient, because a
MaxCut-optimal signing need not control either the invariant orbit-profile
floor or the nonclean/deeper residue.

This is the explicit splitting operation. It is not yet an AB--K
construction, because K proves none of (10.8)--(10.10) for an actual
sequential stage. Under those three exact hypotheses, Theorem 10.1 and (10.7)
repair all but \(o(W)\) of the selected first-shadow pairs and yield
\(J_A(F_\varepsilon)=o(W)\). Those hypotheses are unproved.

The tree's laminarity concerns coordinate-membership atoms. It does not imply
that the occurrence constraint graph
\(\Gamma_{\sigma,\mathcal P}\) is bipartite, nearly bipartite, or even has
\(\Theta(W)\) edges.

---

## 11. Positive-density collateral is unavoidable

The controlled carriers cannot repair the first shadow, but a physical
component cut may drag rows outside them. Quantitatively, a successful lift
must do so on a positive-density scale.

Let \(F_0\) be any coordinate relabeling of the canonical MSW factor, and let
\(b(F,F_0)=|F\triangle F_0|/2\) be unpointed row distance. The marked-gap
stability theorem gives

\[
 M_1(F)
 \ge
 \left[
 J_m-(m-1)b(F,F_0)-\rho_1
 \right]_+.                                          \tag{11.1}
\]

### Theorem 11.1 (collateral row-distance floor)

Any terminal exact factor with \(M_1=o(W)\) has

\[
 b(F,F_0)\ge(1/8-o(1))B.                             \tag{11.2}
\]

Even granting coexistence without the pruning of Section 1, the full AB10
packet cube, K's laminar selected rows, and K's shifted carrier account for
at most

\[
 \left(\frac7{96}+o(1)\right)B                       \tag{11.3}
\]

canonical rows at the terminal endpoint. Hence any successful physical lift
must remove at least

\[
 \boxed{
 \left(\frac5{96}-o(1)\right)B}                      \tag{11.4}
\]

additional canonical rows as collateral.

#### Proof

Equation (11.2) follows by solving (11.1) for \(b\), using
\(J_m/W\to1/16\) and \(W/B=n\sim2m\).

For the optimistic unpruned count, a cube vertex differs from the canonical
corner in at most two rows per AB packet. AB10 has

\[
 \frac{K_{\mathrm{AB}}}{B}\longrightarrow\frac1{192},
\]

so its row distance is at most

\[
 2K_{\mathrm{AB}}
 =\left(\frac1{96}+o(1)\right)B.                    \tag{11.5}
\]

K's laminar half-signing removes

\[
 2k_{\mathrm{lam}}
 =C_{m-2}+O(1)
 =\left(\frac1{16}+o(1)\right)B                     \tag{11.6}
\]

canonical rows. The shifted carrier has \(o(B)\) rows. Add
(11.5)--(11.6) to obtain (11.3), and subtract from the necessary
\(1/8=12/96\) in (11.2). \(\square\)

The legal pruned composition has an even smaller controlled row set. The
constant \(5/96\) is deliberately the more generous obstruction.

### Corollary 11.2 (sharp collateral beyond the pruned endpoint)

Let \(F_{\mathrm{comp}}\) be the actual pruned AB--K endpoint constructed in
Sections 1--3. Every exact factor \(G\) with \(M_1(G)=o(W)\) satisfies

\[
 \boxed{
 b(G,F_{\mathrm{comp}})
 \ge\left(\frac{23}{384}-o(1)\right)B.}             \tag{11.7}
\]

In particular, since K's shifted orbit carrier contains only
\(2C_{m-s_0-2}=o(B)\) rows, a successful later physical lift must change at
least \((23/384-o(1))B\) noncarrier rows.

#### Proof

The pruned endpoint is at canonical row distance at most

\[
 2k_{\mathrm{lam}}+2K^*
 =\left(\frac1{16}+\frac1{384}+o(1)\right)B
 =\left(\frac{25}{384}+o(1)\right)B.                \tag{11.8}
\]

By (11.2), \(b(G,F_0)\ge(1/8-o(1))B\). The triangle inequality gives

\[
 b(G,F_{\mathrm{comp}})
 \ge b(G,F_0)-b(F_{\mathrm{comp}},F_0)
 \ge\left(\frac{48-25}{384}-o(1)\right)B.
\]

At most \(o(B)\) of these changes can be confined to the shifted carrier.
\(\square\)

There is also a path-action statement. Let
\(\mathsf A_1^{\mathrm{coll}}\) be the sum of the positive first-shadow
actions of all collateral row transitions along a proposed lift. From
Theorem 5.1 and the fact that filling one old hole consumes one unit of
positive first-shadow action,

\[
 M_1(F_{\mathrm{end}})
 \ge
 \left(\frac1{16}-o(1)\right)W
 -\mathsf A_1^{\mathrm{coll}}.                       \tag{11.9}
\]

Thus \(M_1=o(W)\) requires

\[
 \boxed{
 \mathsf A_1^{\mathrm{coll}}
 \ge\left(\frac1{16}-o(1)\right)W.}                  \tag{11.10}
\]

K provides neither target-disjoint beneficial alignment for this collateral
action nor an \(o(W)\) bound on its harmful all-depth loss.

---

## 12. Independent audit and exact boundary

The decisive constants and implication scopes were independently checked.

### 12.1 Audited positive constants

* Omitting colours two and \(s_0\) makes all three packet carriers owner- and
  root-disjoint.
* The retained Catalan tail has density \(1/768\).
* Balanced AB rounding changes \(1/1536+o(1)\) of the \(B\) packet signs, and
  the resulting leading relative-\(J_A\) constant is \(\kappa_A/768\).
* The internal-coherence lower bound and its factor \(1/4\) are unchanged, so
  the total \(\mathcal Q_H\)-gain divided by \(W\) diverges.
* K's laminar half-signing has \(O_A(W/\sqrt m)\) shallow action.
* The joint piecewise-involution calculation preserves every one of K's
  original counted seams, hence the unrestricted constant \(11/128\).
* Requiring the whole K menu to avoid all AB bridge labels still leaves the
  explicit seam constant \(7/128\).

### 12.2 Audited no-go constants

* The controlled shifted carrier has \(2C_{m-s_0-2}\) rows and
  \(o(W)\) action.
* Capacity at depth \(H\) forces the exact lower bound (6.4); hence
  polynomially many capacity-feasible carriers remain \(o(W)\).
* The optimistic unpruned controlled row distance is \(7B/96+o(B)\), leaving
  a collateral requirement \(5B/96-o(B)\).
* Relative to the actual pruned endpoint, the sharper additional row-distance
  requirement is \(23B/384-o(B)\).
* The controlled operations fill only \(o(W)\) old holes, so their terminal
  hole count remains \(1/16-o(1)\) times \(W\).

### 12.3 Exact proved/conditional boundary

Proved:

1. The pruned AB--K packet composition is literal, integral, exact, and
   simultaneously menu-avoiding; a full bridge-disjoint K menu retains
   \((7/128-o(1))W\) seams.
2. It retains the AB productive quadratic-energy gain with \(o(W)\) shallow
   action.
3. The full \((11/128-o(1))W\) seam reservoir survives the static pruned AB
   rounding, but a seam's local core is fixed and supplies no clean moved
   depth-one constraint.
4. It does not repair the \(\Omega(W)\) first-shadow obstruction.
5. No polynomial union of K-style capacity-feasible shifted carriers can
   supply the repair directly.
6. K's seam count alone gives neither targetwise splitting nor component
   dispersion.
7. Static layered use of K's spanning tree gives one bundle and zero
   splitting.
8. Laminar TU alone does not survive arbitrary physical component
   identifications.
9. The MaxCut operation in Theorem 10.1 is an explicit legal split; its exact
   residual is graph frustration, and (10.7) is the complete all-depth loss
   certificate.

Unproved:

1. No sequential K-menu stage is known to produce the
   \((1/16-o(1))W\)-edge occurrence graph in (10.8).
2. No near-bipartiteness or \(o(W)\) signed-cycle-frustration theorem is known
   for that graph at the same signing that controls all other depths.
3. No theorem controls the invariant orbit-profile floor or the weighted
   all-depth collateral loss of the
   positive-density noncarrier rows forced by Theorem 11.1.
4. K's component-monochromatic lift remains conditional.

Accordingly, the requested explicit \(\Omega(W)\) split with \(o(W)\) loss
does not follow from the menu-avoiding rounded family plus K's laminar
orbit-tree menu. The composition, full label avoidance, and seam persistence
have been made literal and exact. For the one-stage clean-pair completion
isolated here, the remaining failure is the remote occurrence-pair map, its
signed-cycle frustration, and the positive-density collateral requirement,
not an unexamined packet-compatibility clause. Other direct or multistage
mechanisms are not ruled out. No constant-one or literal contiguous-OR
conclusion is claimed.
