# CCTPF installation recurrence for a dense conveyor reservoir

## Conditional polynomial batching, exact exposure transport, and the exterior-wall threshold

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Use the calibrated CCTPF notation

\[
 M=m+H,\qquad N=N_H=\binom{2m}{m-H},\qquad
 W=\binom{2m}{m},
\tag{0.1}
\]

and let \(k\) and \(p_*\) be the full-history size and maximal single-port
exposure from the port-weighted block-augmentation theorem. Thus

\[
 k=(\sqrt\pi+o(1))m^{3/2},\qquad
 (kp_*)^{-1}=\exp\{\Omega(\sqrt{m\log m})\}.
\tag{0.2}
\]

Let

\[
 R_H=\frac WN,\qquad
 P_H=9M^2+\left(9+256\sum_{q=1}^Hq^2\right)R_H.
\tag{0.3}
\]

The dense three-top theorem supplies \(W/P_H\) full-frame packets. This
note determines exactly what is, and what is not, obtained by combining
that reservoir with CCTPF block augmentation.

The positive numerical fact is strong. If \(K\asymp W/P_H\), then the
number of top roots assigned to one packet in a hypothetical completion is

\[
 g=O\left(\frac{P_H}{R_H}\right)=\operatorname {poly}(m),
 \qquad gkp_*=o(1).
\tag{0.4}
\]

Consequently one packet has more than enough self-contention radius to
reroute its three old roots together with \(g\) new roots, provided all of
those roots already have a common fixed amount of exterior port slack.
Under an exact dynamic slack hypothesis, the reservoir therefore completes
all \(N\) top roots. Consuming the whole reservoir disturbs at most

\[
 3MK=o(W)
\tag{0.5}
\]

middle owners and at most \(O(HMK)=o(W)\) complete protected packet
footprints. Target simplicity, once available, is preserved exactly.

There are, however, two decisive missing hypotheses.

1. The \(W/P_H\) packing separates middle owners and packet
   derivatives, not the complete CCTPF histories. It does not provide a
   choice of CCTPF cores, quota decorations, and shores whose complete
   active target sets are pairwise disjoint.

2. Even after assuming such a realization, deleting one three-history
   packet changes the additive exposure of any root by at most

   \[
                             3kp_*=o(1).
   \tag{0.6}
   \]

   It cannot create fixed slack through a genuine exterior wall. More
   generally, if a block of \(r\) histories is deleted and every candidate
   root has current exposure at least one, the nonnegative port criterion
   cannot certify a replacement by more than \(r\) histories.

The exact missing combinatorial statement is therefore a packet-to-wall
incidence theorem, not another count of packet capacity: the packet
assigned to a root must hit that root's exterior exposure on the scale of
its entire excess over one, with a further ordered staircase of
\((i-1)kp_*\).

For completeness, the existing scalar port budget gives a rigorous but
small positive installation. Assuming a CCTPF-realizable reservoir, one
can extend it to a target-simple matching of size

\[
                        \left\lfloor\frac{N}{8k}\right\rfloor.
\tag{0.7}
\]

The entire added CCTPF trace has at most \(N/8=o(W)\) target incidences.
This is only a \(\Theta(1/k)\) fraction of the top roots and is far from the
coefficient-one leave. Up to constants, \(N/k\) is the last scale forced by
the available first-moment inequality: at size \(N/k\), that inequality is
consistent with exposure one at every root.

Thus the reservoir passes the capacity and \(o(W)\) packet-boundary
ledgers, but installation/completion is not closed. The surviving gate is
the dynamic wall-hitting condition displayed in Theorem 3.1 below.

## 1. The type-compatibility gate

For a CCTPF root \(U\), let \(\Omega_U\) be its literal full-history
catalogue. A history \(F\in\Omega_U\) has a typed protected target set
\(P(F)\) of cardinality \(k\). A family of histories is target-simple if
the roots are distinct and all sets \(P(F)\) are pairwise disjoint.

### Definition 1.1 (CCTPF-realizable packet reservoir)

A family of full-frame conveyor packets is CCTPF-realizable if one can
choose, for every packet and every one of its three tops,

1. one of the two packet shores;
2. a legal CCTPF \(2H\)-core and tail order; and
3. one literal nested quota decoration,

so that the resulting three histories belong to their respective
catalogues \(\Omega_U\), and the union of all resulting histories is
target-simple.

This definition is exactly what is required before CCTPF block augmentation
can be invoked.

### Proposition 1.2 (the dense theorem does not prove Definition 1.1)

The conclusion of the dense \(W/P_H\) conveyor packing does not imply that
its packet family is CCTPF-realizable.

#### Proof

That theorem gives disjoint rank-\(M\) tops, disjoint complete middle-owner
sets, and disjoint supports of the shore derivatives at every protected
depth. Its floor-affinity proof explicitly permits the complete shallow
carriers of different packets to overlap. Disjointness of

\[
 \operatorname {supp}(\Gamma_P^1-\Gamma_P^0)
\]

does not imply disjointness of either \(\operatorname {supp}\Gamma_P^0\)
or \(\operatorname {supp}\Gamma_P^1\). Target simplicity is a condition
on the latter complete supports.

The stronger complete-footprint packing separates the unions of the two
shores between distinct packets. The local conveyor theorem proves
squarefreeness inside one packet only at the middle row. It does not prove
that the three selected histories are internally target-simple at every
active signed row after one common CCTPF phase/quota restriction. Hence
even that stronger packing leaves the within-packet history condition and
the common phase/quota realization to be proved. Neither stated theorem
contains these assertions. \(\square\)

All subsequent positive statements therefore state CCTPF realizability as
an explicit hypothesis.

## 2. Exact replacement recurrence

Let \(\mathcal M_t\) be a target-simple CCTPF matching. Put

\[
 \mathcal B_t=\bigcup_{F\in\mathcal M_t}P(F),\qquad
 e_t(V)=\omega_V(\mathcal B_t)
\tag{2.1}
\]

for every top root \(V\). Choose a block
\(S_t\subseteq\mathcal M_t\) of \(r_t\) histories and write

\[
 h_t(V)=\omega_V\left(\bigcup_{F\in S_t}P(F)\right).
\tag{2.2}
\]

By the single-history port bound,

\[
                        0\le h_t(V)\le r_tkp_*.
\tag{2.3}
\]

We use the following slight extension of ordered block augmentation. It is
the same proof, but permits some deleted roots to remain unmatched.

### Lemma 2.1 (replacement with optional root loss)

Let \(A_t=\{U_1,\ldots,U_{a_t}\}\) be distinct roots, none used by
\(\mathcal M_t\setminus S_t\). If

\[
 \boxed{
 e_t(U_i)-h_t(U_i)+(i-1)kp_*<1
 \qquad(1\le i\le a_t),}
\tag{2.4}
\]

then there are histories \(G_i\in\Omega_{U_i}\) such that

\[
 \mathcal M_{t+1}
 =\left(\mathcal M_t\setminus S_t\right)
   \cup\{G_1,\ldots,G_{a_t}\}
\tag{2.5}
\]

is target-simple. In particular,

\[
 |\mathcal M_{t+1}|=|\mathcal M_t|-r_t+a_t.
\tag{2.6}
\]

#### Proof

The frozen exterior in (2.5) has exposure

\[
 \omega_{U_i}(\mathcal B_t\setminus P(S_t))
 =e_t(U_i)-h_t(U_i),
\]

because the old histories are target-disjoint and exposure is additive.
Choose \(G_i\) successively. Before the \(i\)-th choice, the earlier new
histories add at most \((i-1)kp_*\) exposure. Equation (2.4) makes the total
strictly less than one, so cylinder union coverage is less than one and a
literal avoiding history exists. This proves (2.5), and (2.6) is the
cardinality identity. \(\square\)

### Theorem 2.2 (exact exposure transport)

Under Lemma 2.1, define

\[
 g_t(V)=\sum_{i=1}^{a_t}\omega_V(P(G_i)).
\tag{2.7}
\]

Then, for every root \(V\),

\[
 \boxed{e_{t+1}(V)=e_t(V)-h_t(V)+g_t(V),}
\tag{2.8}
\]

with

\[
 0\le h_t(V)\le r_tkp_*,
 \qquad 0\le g_t(V)\le a_tkp_*.
\tag{2.9}
\]

If \(S_t\) consists of \(b_t\) three-history conveyor packets, then

\[
 r_t=3b_t,\qquad h_t(V)\le3b_tkp_*.
\tag{2.10}
\]

If all their old roots are reinstalled together with \(u_t\) formerly
unmatched roots, then

\[
 a_t=3b_t+u_t,\qquad
 |\mathcal M_{t+1}|-|\mathcal M_t|=u_t.
\tag{2.11}
\]

#### Proof

Equation (2.8) is additivity on the target-disjoint decomposition (2.5).
The inequalities follow by applying the one-history bound to every deleted
and every inserted history. Equations (2.10)--(2.11) are the exact packet
and root counts. \(\square\)

For later use define the slack opened by a block at a root by

\[
 \sigma_t(V;S_t)=1-e_t(V)+h_t(V).
\tag{2.12}
\]

Then the augmentation condition is the exact ordered staircase

\[
 \boxed{\sigma_t(U_i;S_t)>(i-1)kp_*.}
\tag{2.13}
\]

This is the sought installation recurrence. Packet number and packet
density alone do not appear in (2.13); only their wall incidence \(h_t\)
does.

## 3. Conditional absorber growth

### Theorem 3.1 (dynamic-slack completion)

Assume a CCTPF-realizable reservoir of \(K\) three-history packets is
installed. Partition all roots outside the reservoir into batches

\[
 R_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}R_K,
 \qquad |R_j|\le g.
\tag{3.1}
\]

Process the packets in an order \(Q_1,\ldots,Q_K\). At stage \(j\), let
\(S_j\) be the three current histories of \(Q_j\), and let

\[
 A_j=\operatorname {root}(S_j)\mathbin{\dot\cup}R_j.
\tag{3.2}
\]

Suppose there is a number \(\eta_m>0\) such that

\[
 \max_{U\in A_j}
 \omega_U\left(\mathcal B_j\setminus P(S_j)\right)
 \le1-\eta_m
\tag{3.3}
\]

at every stage, and

\[
                        (g+2)kp_*<\eta_m.
\tag{3.4}
\]

Then every stage is legal, all \(N\) roots are eventually saturated, and
the final history family is target-simple.

#### Proof

Order the three old roots and the roots of \(R_j\) arbitrarily. There are
at most \(g+3\) roots. For the last one, the left side of (2.4) is at most

\[
 1-\eta_m+(g+2)kp_*<1.
\]

It is smaller for every earlier root. Lemma 2.1 therefore replaces the
three histories by \(3+|R_j|\) histories and increases matching size by
\(|R_j|\). Induction preserves target simplicity. The batches partition
all initially unused roots, so the final matching saturates every root.
\(\square\)

### Corollary 3.2 (the local numerical capacity is sufficient)

At calibrated CCTPF height, take

\[
 K=\left\lfloor\frac{W}{P_H}\right\rfloor,\qquad
 g=\left\lceil\frac{N-3K}{K}\right\rceil_+.
\tag{3.5}
\]

Then

\[
 g\le \frac{2P_H}{R_H}+1=\operatorname {poly}(m)
\tag{3.6}
\]

for all sufficiently large \(m\), and hence

\[
                        (g+2)kp_*=o(1).
\tag{3.7}
\]

Thus any fixed dynamic slack in (3.3) would complete the whole top layer.

#### Proof

Since \(W/P_H\) is exponential, its floor is at least \(W/(2P_H)\).
Using \(N=W/R_H\) gives (3.6). The definition (0.3), together with
\(H=\Theta(\sqrt{m\log m})\), makes \(P_H/R_H\) polynomial in \(m\).
Equation (0.2) says that \(kp_*\) is smaller than the reciprocal of every
polynomial, proving (3.7). \(\square\)

### Proposition 3.3 (packet-resource and boundary ledger)

If all \(K\le W/P_H\) packets are processed, the number of their distinct
middle owners which may cease to follow the original packet shore is at
most \(3MK\), and the union of their complete two-shore protected
footprints has size at most

\[
                        3MK+12HMK.
\tag{3.8}
\]

Both quantities are \(o(W)\). More explicitly,

\[
 \frac{3MK}{W}\le\frac{3M}{P_H}\le\frac1{3M},
\tag{3.9}
\]

and

\[
 \frac{12HMK}{W}\le\frac{12HM}{P_H}
 \le\frac{4H}{3M}=o(1).
\tag{3.10}
\]

All CCTPF owner collisions remain exactly zero.

#### Proof

One packet has \(3M\) common middle owners. At each of the at most \(2H\)
nonzero signed ledgers, the union of its two shores has at most \(6M\)
targets. This proves (3.8). The inequalities use \(P_H\ge9M^2\).
Target simplicity at every replacement follows from Lemma 2.1, so no
collision is hidden in these exceptional-support bounds. \(\square\)

If the physical safe-port collar at depth \(\delta\) is also charged, the
exact conveyor theorem gives \(6(H+\delta-1)\) changed ordered ports per
packet. Hence the whole reservoir has collar boundary

\[
 6K\sum_{\delta=1}^H(H+\delta-1)
 =(9H^2-3H)K
 \le(9H^2-3H)\frac W{P_H}
 =o(W).
\tag{3.10a}
\]

At one fixed depth the sharper count is
\[
 6(H+\delta-1)K\le6(2H-1)\frac W{P_H}=o(W).
\tag{3.10b}
\]

These are changed-port counts. They do not assume that repairing one
changed port has zero word cost.

The proposition controls the packet boundary. It does not say that an
arbitrary newly chosen history has negligible trace distance from a
prescribed baseline history. If every incidence of every replacement
history were charged as leakage, a full completion would have \(kN\)
charged incidences, and

\[
                        \frac{kN}{W}=\frac{k}{R_H}.
\tag{3.11}
\]

At the standard \(H=(1+o(1))\sqrt{m\log m}\), the known asymptotics give
\(R_H=m^{1+o(1)}\), so (3.11) is \(m^{1/2+o(1)}\), not \(o(1)\).
Therefore an all-root application needs a separate chain-aligned trace
compiler: if \(\lambda_U\) denotes the actual extra trace cost of the
history installed at \(U\), its exact required condition is

\[
                        \sum_U\lambda_U=o(W).
\tag{3.12}
\]

For example, average extra cost \(o(R_H)\) per root suffices. The block
augmentation theorem controls collisions, not (3.12).

## 4. The quantitative exterior wall

### Theorem 4.1 (one packet cannot burn a fixed wall)

Let \(Q\) be one three-history packet in \(\mathcal M_t\). For every root
\(U\),

\[
 \omega_U(P(Q))\le3kp_*.
\tag{4.1}
\]

Consequently, if

\[
                        e_t(U)\ge1+3kp_*,
\tag{4.2}
\]

then after deleting \(Q\) the additive exposure of \(U\) is still at least
one. The port-weighted augmentation criterion cannot even install \(U\)
as the first replacement root.

More generally, deleting \(b\) packets cannot cross an exposure excess
\(\varepsilon\) at \(U\) whenever

\[
                        3bkp_*\le\varepsilon.
\tag{4.3}
\]

#### Proof

Equation (4.1) is (2.3) with \(r_t=3\). Under (4.2), the post-deletion
exposure is at least \(e_t(U)-3kp_*\ge1\), contradicting the strict
inequality required at the first step. The same proof with \(3b\)
histories gives (4.3). \(\square\)

At calibrated height, (4.1) is exponentially small on the
\(\sqrt{m\log m}\) scale. Thus deleting one packet does not itself expose
the fixed positive slack used in Theorem 3.1.

### Theorem 4.2 (saturated-wall no-growth for the additive criterion)

Let \(S_t\) contain \(r_t\) histories. Suppose every root in a proposed
replacement set \(A_t\) has

\[
                        e_t(U)\ge1.
\tag{4.4}
\]

If \(a_t>r_t\), no ordering of \(A_t\) can satisfy (2.4).

#### Proof

Consider the root in position \(r_t+1\). By (2.3) and (4.4),

\[
 e_t(U_{r_t+1})-h_t(U_{r_t+1})+r_tkp_*
 \ge1-r_tkp_*+r_tkp_*=1.
\]

This violates the strict inequality (2.4). \(\square\)

This statement concerns the nonnegative additive port certificate. It
does not assert that every other, cancellative augmentation is impossible.
There is also an exact obstruction at the cylinder-union level. If for a
root \(U\) there is a family

\[
 \mathcal W_U\subseteq
 \mathcal B_t\setminus P(S_t)
\quad\text{with}\quad
 \beta_U(\mathcal W_U)=1,
\tag{4.5}
\]

then every literal history of \(U\) meets the frozen exterior, so no
replacement can install \(U\), independent of additive estimates. A wall
as in (4.5) which is supported outside the reservoir survives deletion of
the entire reservoir.

The dense packet theorem controls top, middle-owner, and derivative
collisions. It supplies no lower bound on

\[
 h_Q(U)=\omega_U(P(Q))
\tag{4.6}
\]

for a blocked root \(U\), and no theorem that a packet meets every exact
cover (4.5). The required new hypothesis is precisely the following
ordered wall-hitting inequality:

\[
 \boxed{
 h_{Q_j}(U_i)>\bigl(e_j(U_i)-1\bigr)+(i-1)kp_*
 }
\tag{4.7}
\]

for every root assigned to packet \(Q_j\). Equation (4.7) is just (2.13)
rewritten, so it is both exact and sufficient for the existing
augmentation theorem. For a one-packet block, \(h_{Q_j}(U_i)\le3kp_*\):
all but the first three roots of a large batch must therefore already have
strictly subunit exposure. This is the quantitative exterior-wall
obstruction to the proposed automatic absorber growth.

### Corollary 4.3 (best-case complete-frame grant still has only polylogarithmic growth)

The preceding ceiling can be stated for an arbitrary removed typed target
set, without assuming it is a union of histories. Suppose every candidate
root has current exposure at least one, and grant that a deletion removes
\(R\) typed targets, each of port weight at most \(p_*\) for every candidate
root. If \(a\) new histories are then chosen successively by the
port-weighted criterion, then

\[
                             a\le\left\lceil\frac Rk\right\rceil.
\tag{4.8}
\]

In particular:

1. deleting \(r\) complete CCTPF histories has \(R=rk\), so it can install
   at most \(r\) saturated roots; if the \(r\) old roots are reinstalled,
   the certified net gain is exactly zero;
2. even if one grants deletion of every protected cell in all three
   complete conveyor frames, then

   \[
                  R_{\rm full}\le3M(2H-1)
   \tag{4.9}
   \]

   and one packet installs at most

   \[
   \left\lceil\frac{3M(2H-1)}k\right\rceil
   =\left(\frac6{\sqrt\pi}+o(1)\right)\sqrt{\log m}
   \tag{4.10}
   \]

   saturated roots at calibrated height.

Consequently all \(K\le W/P_H\) packets together have best-case
saturated-wall capacity

\[
 O\left(\frac{W\sqrt{\log m}}{P_H}\right)
 =o\left(\frac N{\sqrt m}\right).
\tag{4.11}
\]

Thus even the artificially favorable operation of deleting complete
full-frame footprints cannot repair the coefficient-one root leave through
a saturated exterior by independent packet absorptions.

#### Proof

The removed set lowers exposure by at most \(Rp_*\). At position \(i\), a
root of pre-deletion exposure at least one has certified exposure at least

\[
                       1-Rp_*+(i-1)kp_*.
\]

Strict inequality below one requires \((i-1)k<R\). Taking \(i=a\) proves
(4.8). A CCTPF history has exactly \(k\) typed targets. A complete
three-frame packet has three frames and \(2H-1\) protected typed rows
(the middle row and both signs for \(1\le q<H\)), with \(M\) cells per
frame and row, proving (4.9). Equation (4.10) follows from
\(M=(1+o(1))m\), \(H=(1+o(1))\sqrt{m\log m}\), and
\(k=(\sqrt\pi+o(1))m^{3/2}\).

Finally, using \(N=W/R_H\) and
\(P_H\ge256S_2(H)R_H\),

\[
 \frac{(W/P_H)\sqrt{\log m}}{N/\sqrt m}
 \le
 \frac{R_H\sqrt{m\log m}}{P_H}
 \le
 \frac{\sqrt{m\log m}}{256S_2(H)}
 =O\left(\frac1{m\log m}\right),
\]

which proves (4.11). \(\square\)

## 5. What the scalar budget does install

The failure of automatic completion should not obscure a small positive
consequence. The global CCTPF port census says that every target-simple
matching of \(n\) histories satisfies

\[
                        \sum_U e(U)\le kn.
\tag{5.1}
\]

### Theorem 5.1 (first-moment installation to density \(1/(8k)\))

Assume that a CCTPF-realizable conveyor reservoir has been installed, and
let its target-simple history matching have size \(n_0=3K\), where

\[
                        K\le\frac W{P_H}.
\tag{5.2}
\]

For all sufficiently large calibrated \(m\), it extends to a target-simple
matching of size

\[
                        n_*=\left\lfloor\frac N{8k}\right\rfloor.
\tag{5.3}
\]

No reservoir packet need be deleted. The added histories have at most

\[
                        k(n_*-n_0)\le\frac N8=o(W)
\tag{5.4}
\]

typed protected target incidences in total.

#### Proof

First, \(n_0<n_*\) for large \(m\). Indeed,

\[
 \frac{3K}{N/(8k)}\le\frac{24kR_H}{P_H}=o(1),
\tag{5.5}
\]

because \(P_H\ge256S_2(H)R_H\),
\(S_2(H)=\Theta(H^3)\), \(k=\Theta(m^{3/2})\), and
\(H^3/k=\Theta((\log m)^{3/2})\).

Suppose a current matching has size \(n\le n_*\). By (5.1), at most

\[
                        2kn\le\frac N4
\tag{5.6}
\]

roots have exposure greater than \(1/2\). At most \(n\le N/8\) roots are
already occupied. Thus at least \(5N/8\) roots are simultaneously
unmatched and have exposure at most \(1/2\).

Put

\[
                        r_0=\left\lfloor\frac1{4kp_*}\right\rfloor.
\tag{5.7}
\]

We have \(r_0=o(N)\). To see this without an unproved lower estimate for
\(p_*\), use the middle term in its definition:

\[
 p_*\ge\frac{L}{\binom{s}{H}},
 \qquad
 r_0\le\frac{\binom{s}{H}}{4kL}.
\tag{5.8}
\]

Here \(\log\binom{s}{H}=o(m)\), whereas \(\log N=\Theta(m)\).

Choose at most \(r_0\) low-exposure unmatched roots, stopping early if the
matching reaches \(n_*\). For the \(i\)-th chosen root,

\[
 \omega_{U_i}(\mathcal B)+(i-1)kp_*
 <\frac12+\frac14<1.
\tag{5.9}
\]

Lemma 2.1 with \(S_t=\varnothing\) adjoins histories on the whole batch.
Repeat. The matching size increases at every round and never exceeds
\(n_*\), so the argument terminates at (5.3). Equation (5.4) follows from
the exact size \(k\) of every history. Finally

\[
 \frac NW=\frac1{R_H}=m^{-1+o(1)}
\tag{5.10}
\]

at calibrated height, proving \(N=o(W)\). \(\square\)

The scale in Theorem 5.1 is the natural limit of the known scalar
information. When \(n=N/k\), the right side of (5.1) equals \(N\), which
is consistent with \(e(U)=1\) at every root. Theorem 4.2 then gives no net
growth. This does not construct such a physical matching; it proves that
the first-moment census alone cannot force a continuation beyond
\(\Theta(N/k)\).

## 6. Exact boundary

Proved:

1. the exact block replacement and exposure recurrences (2.4), (2.8);
2. the polynomial per-packet completion demand \(g=O(P_H/R_H)\) and the
   exponentially stronger self-contention radius;
3. conditional all-root completion under the dynamic slack condition
   (3.3);
4. \(o(W)\) middle-owner and complete packet-footprint disturbance even if
   the whole reservoir is consumed;
5. the one-packet bound \(h_Q(U)\le3kp_*\);
6. the saturated-wall no-growth theorem for every nonnegative
   port-weighted block certificate;
7. the best-case complete-frame saturated capacity
   \(O(\sqrt{\log m})\) per packet and its \(o(N/\sqrt m)\) global ceiling;
8. the exact ordered packet-to-wall condition (4.7); and
9. first-moment growth, after assuming CCTPF realization, to \(N/(8k)\)
   histories with \(o(W)\) total added trace.

Not proved:

1. a CCTPF-realizable decoration of the \(W/P_H\) full-frame packet
   reservoir;
2. the dynamic wall-hitting inequality (4.7) for those packets;
3. an \(o(W)\)-overhead trace compiler for arbitrary all-root replacements;
4. exclusion of an exact exterior cylinder wall supported away from the
   reservoir; or
5. coefficient one.

The proposed automatic iteration therefore fails at a precise place:
deleting a packet has exponentially large cardinality radius but opens
only exponentially small port slack. A successful absorber theorem must
correlate packet footprints with the actual exterior walls; packet density
and owner disjointness by themselves cannot do so.
