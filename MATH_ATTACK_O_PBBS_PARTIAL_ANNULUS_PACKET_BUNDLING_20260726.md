# PBBS correct paths at the corrected partial-annulus density: local packet extension, endpoint circulation, and the seam-coboundary gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

Audited inputs used here are
`MATH_AUDIT_GAUSSIAN_SHARED_PREFIX_PACKET_FRACTIONAL_BRAID_20260726.md`,
`MATH_THEOREM_Q0_PARTIAL_PACKET_GATE_AND_HEREDITARY_TRACE_RIGIDITY_20260726.md`,
`MATH_THEOREM_PBBS_Q_FAN_SUPPORT_Q2_AND_GAUSSIAN_MULTIPLICITY_20260726.md`,
`MATH_ATTACK_O_PBBS_GROWING_DEPTH_CHRONOLOGY_20260726.md`, and
`MATH_AUDIT_O_PBBS_GROWING_DEPTH_RENEWAL_KERNEL_20260726.md`.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
 \qquad 0<a<b<\infty .
\tag{0.2}
\]

All asymptotic statements below are for fixed \(a,b\) and
\(m\to\infty\).  The exact packet count is

\[
 K=\left\lfloor {N_{q_0}\over 2m}\right\rfloor,
 \qquad
 \rho=N_{q_0}-2mK,
 \qquad 0\le \rho<2m.
\tag{0.3}
\]

Thus the corrected gate uses only

\[
 2mK=N_{q_0}-\rho
   =(e^{-a^2}+o(1))W
\tag{0.4}
\]

middle-owner occurrences.  It does not require a near-factor on all
\(W\) middle owners.

This report does not construct the required packet family.  It proves the
sharp endpoint/coboundary obstruction to obtaining it from the presently
proved PBBS correct-path and growing-depth renewal theorems.

The conclusions are as follows.

1.  Every **strongly two-sided geodesic** PBBS fan extends individually
    to an ordinary cyclic-order packet.  The explicit all-depth PBBS
    support fan has this property.  Therefore there is no local extension
    obstruction.

2.  One such seed in each of the \(K\) packets certifies only \(K\) of
    the \(2mK\) required depth-\(q_0\) starts, a proportion \(1/(2m)\).
    Even granting certification of the forced antipodal mate gives only a \(1/m\)
    proportion.  Local PBBS support is consequently negligible at the
    corrected density.

3.  Dense certification is rigid.  Consecutive certified starts must be
    consecutive PBBS iterates.  They therefore form PBBS runs, whose
    exact boundary is

    \[
     r_g(S)=|\{x\in S:gx\notin S\}|
      ={1\over2}\sum_x
       |\mathbf1_S(x)-\mathbf1_S(g^{-1}x)|.
    \tag{0.5}
    \]

    The endpoints must satisfy a coordinate circulation law, every short
    PBBS residence interval must be hit by a seam, and opposite packet
    positions must be pointwise complementary with reversed increments.

4.  If a final packet has \(b\ge1\) non-PBBS transitions, the exact
    number \(u_q\) of depth-\(q\) starts which are not faithful PBBS
    windows obeys the sharp bound

    \[
       u_q\ge \min\{2m,b+q-1\}.
    \tag{0.6}
    \]

    Equality is attained by clustering all seams consecutively.  If all
    but \(o(K)\) packets require a seam, then

    \[
     \sum_{q=q_0}^{H}u_q
       \ge
       \left({e^{-a^2}(b^2-a^2)\over4}+o(1)\right)W.
    \tag{0.7}
    \]

    This is a positive-density **provenance turnover**, not a target-hole
    lower bound.

5.  The distinction in item 4 is decisive.  At deeper ranks the packet
    has a large forced occurrence surplus over \(N_q\).  With one
    clustered seam per packet, the capacity lower bound for targets not
    certified by faithful PBBS windows is eventually positive only at
    \(q=q_0\), where its two-sign value is

    \[
       2\rho+2q_0K
       =\left(ae^{-a^2}+o(1)\right){W\over\sqrt m}
       =o(W).
    \tag{0.8}
    \]

    New seam-crossing packet windows are legal and can in principle
    replace every lost PBBS target.  No \(\Omega(W)\) actual-hole
    obstruction follows from seam counting alone.

6.  The exact remaining object is a signed target coboundary

    \[
      \Delta_q^\sigma
       =\sum_{x\text{ crossing a seam}}
          \bigl([T_{q,\sigma}^{\rm new}(x)]
                -[T_{q,\sigma}^{\rm PBBS}(x)]\bigr),
      \qquad \sigma\in\{-,+\}.
    \tag{0.9}
    \]

    Its total coefficient is zero and its \(\ell^1\)-norm is bounded by
    twice the number of affected starts.  The growing-depth PBBS renewal
    theorem controls neither its negative part nor its cancellation
    against the forced deeper-rank surplus.

Accordingly, the answer is: the corrected owner mass removes the
full-factor obstruction, but the currently proved PBBS chronology does
not bundle the correct paths into the required ordinary packets.  What
can be proved is an exact endpoint, antipodal, residence, and
seam-coboundary obstruction to that deduction.  It isolates a new
positive-density cancellation theorem as the missing gate; it does not
refute the existence of a deliberately rethreaded packet family.

Every use of “obstruction” below has this precise scope.

## 1. The corrected packet ledger

For a family \(\mathcal P\) of \(K\) ordinary cyclic-order packets, let

\[
 D_0(\mathcal P)
  =\left|\bigcup_{P\in\mathcal P}V(P)\right|,
 \qquad
 C_0(\mathcal P)=2mK-D_0(\mathcal P).
\tag{1.1}
\]

Thus \(C_0\) is occurrence excess, not a count of colliding pairs.  Let
\(h_q^-\) and \(h_q^+\) be the actual numbers of absent rank-\((m-q)\)
lower and rank-\((m+q)\) upper targets.  For ordinary packets,

\[
 h_q^+=h_q^-
\tag{1.2}
\]

by complement-antipodality.  Write their common value as \(h_q\).

### Theorem 1.1 (exact partial-packet compiler ledger)

For every such packet family,

\[
 L\le
 W+C_0(\mathcal P)+2HK
   +2\sum_{q=q_0}^{H}h_q.
\tag{1.3}
\]

In particular,

\[
 C_0=o(W),\qquad
 \sum_{q=q_0}^{H}h_q=o(W)
\tag{1.4}
\]

imply a literal middle-plus-annulus word of length \(W+o(W)\).

#### Proof

An ordinary packet has \(2m\) owner states and is cyclically safe through
every depth below \(m\).  Cutting it once and applying the delay-\(H\)
factor produces a literal packet word of length \(2m+2H\).  The \(K\)
packet words therefore cost \(2mK+2HK\).

Append every middle owner not occurring in a packet.  There are

\[
 W-D_0=W-(2mK-C_0)
\]

such owners, so packet words plus middle repair cost exactly
\(W+C_0+2HK\).  Append each missing signed annular target once.  This
adds \(2\sum_qh_q\), proving (1.3).  Concatenation creates no loss of an
internal witness. \(\square\)

The normalization is

\[
 {N_{q_0}\over W}
  =\prod_{i=1}^{q_0}{m-i+1\over m+i}
  =e^{-a^2+O_a(m^{-1/2})},
\tag{1.5}
\]

and hence

\[
 K=(e^{-a^2}+o(1)){W\over2m},
 \qquad
 2HK\le {H\over m}N_{q_0}
        =O_{a,b}(W/\sqrt m)=o(W).
\tag{1.6}
\]

Thus (1.4), not middle leave, is the substantive gate.  If one instead
uses \(K=\lceil N_{q_0}/(2m)\rceil\), the occurrence discrepancy is less
than \(2m=o(W)\), and all conclusions are unchanged.  The literal
identity \(K=N_{q_0}/(2m)\) is not available unless the divisibility
happens to hold.

For later use, let \(E_q^\sigma\) be the occurrence excess in the signed
depth-\(q\) target histogram.  Since the total signed occurrence mass is
\(2mK=N_{q_0}-\rho\), mass conservation gives the exact identity

\[
 h_q^\sigma
 =E_q^\sigma-igl(N_{q_0}-N_q-\rho\bigr).
\tag{1.7}
\]

At \(q=q_0\), this says \(h_{q_0}^\sigma=E_{q_0}^\sigma+\rho\).
At larger depths, \(N_{q_0}-N_q-\rho\) is forced repeat mass, and only
repeat excess above that floor creates a hole.

## 2. Local PBBS fans do extend to ordinary packets

Let

\[
 X_0,X_1,\ldots,X_s\in\binom{[2m]}m,
 \qquad
 X_{i+1}=X_i-\{d_i\}+\{a_i\}.
\tag{2.1}
\]

Call the path strongly geodesic if

\[
 d_0,\ldots,d_{s-1},a_0,\ldots,a_{s-1}
\tag{2.2}
\]

are \(2s\) distinct coordinates.  Equivalently,

\[
 \left|\bigcap_{i=0}^{s}X_i\right|=m-s,
 \qquad
 \left|\bigcup_{i=0}^{s}X_i\right|=m+s.
\tag{2.3}
\]

Lower correctness alone is only the first equality and is insufficient:
an inserted coordinate may later be deleted.

For example, with a fixed \((m-2)\)-set \(C\) disjoint from
\(a,b,c\), the path

\[
 C\cup\{a,c\},\quad C\cup\{b,c\},\quad C\cup\{a,b\}
\tag{2.3a}
\]

has intersection \(C\) of rank \(m-2\), but its union has rank
\(m+1\), not \(m+2\).  The coordinate \(a\) is deleted and reinserted.

### Lemma 2.1 (one-path packet extension)

Every strongly geodesic path of length \(s\le m\) extends to an ordinary
cyclic-order packet.  More precisely, put

\[
 K_0=X_0\setminus\{d_0,\ldots,d_{s-1}\},
 \qquad
 R_0=X_0^c\setminus\{a_0,\ldots,a_{s-1}\}.
\tag{2.4}
\]

For arbitrary internal orders of \(K_0\) and \(R_0\), the cyclic order

\[
 \pi=(d_0,\ldots,d_{s-1},K_0,
      a_0,\ldots,a_{s-1},R_0)
\tag{2.5}
\]

has \(X_0,\ldots,X_s\) as its first \(s+1\) middle windows.  A rooted,
oriented path therefore has exactly

\[
 (m-s)!^2
\tag{2.6}
\]

such displayed completions.

#### Proof

The first \(m\) entries of (2.5) are exactly \(X_0\).  The entry leaving
the length-\(m\) window at step \(i\) is \(d_i\), and the entry entering
it is \(a_i\).  Hence the first \(s\) shifts give (2.1).  The two
unconstrained blocks have sizes \(m-s\), giving (2.6). \(\square\)

### Lemma 2.2 (the explicit PBBS support fan is strongly geodesic)

In the all-depth PBBS support construction for a lower target \(S\), the
states are

\[
 B_t=S\cup
 \{C_0,\ldots,C_{q-t-1}\}
 \cup\{A_0,\ldots,A_{t-1}\},
 \qquad 0\le t\le q.
\tag{2.7}
\]

The transition \(B_t\to B_{t+1}\) deletes \(C_{q-t-1}\) and inserts
\(A_t\).  The PBBS global-maximum construction proves

\[
 C_j=A_h\quad\Longrightarrow\quad j+h\ge2q.
\tag{2.8}
\]

For the selected indices \(0\le j,h\le q-1\), one has
\(j+h\le2q-2\).  Thus the selected \(q\) deletion and \(q\) insertion
labels are all distinct.  Consequently (2.7) is strongly geodesic.
\(\square\)

The native PBBS construction is on \(2m+1\) coordinates.  A single
strong fan has union size \(m+q\), so at least \(m+1-q\) coordinates
lie outside it.  Deleting any one unused coordinate and relabelling the
remaining ground set puts that individual fan into Lemma 2.1.  This is a
local observation only.  The proved PBBS theorem does not supply one
common deletion/relabeling which preserves a dense family of target
identities and a common successor chronology on \([2m]\).

### Corollary 2.3 (the seed-density loss)

One PBBS fan placed in each packet certifies \(K\) depth-\(q_0\) starts,
whereas the packet family has

\[
 2mK=N_{q_0}-\rho
\tag{2.9}
\]

starts.  Hence the certified proportion is exactly \(1/(2m)\).  Even if
one also proves that every forced antipodal mate is PBBS-certified, the
proportion is at most \(1/m\).

Thus individual completion of PBBS fans cannot prove the partial-annulus
gate.  It leaves \((1-o(1))N_{q_0}\) starts to the original cyclic-packet
matching problem.

## 3. The exact ordinary-packet cocycle

Let \((Z_j)_{j\in\mathbb Z_{2m}}\) be a simple cyclic Johnson route and
write

\[
 Z_{j+1}=Z_j-\{d_j\}+\{a_j\},
 \qquad
 \delta_j=\mathbf1_{a_j}-\mathbf1_{d_j}.
\tag{3.1}
\]

### Theorem 3.1 (ordinary-packet characterization)

The route is the middle-window route of a directed cyclic order if and
only if

\[
 \bigl\{\{d_j,a_j\}:0\le j<m\bigr\}
 \text{ is a perfect matching of }[2m]
\tag{3.2}
\]

and

\[
 (d_{j+m},a_{j+m})=(a_j,d_j)
 \qquad(0\le j<m).
\tag{3.3}
\]

In that case

\[
 Z_{j+m}=Z_j^c,
 \qquad
 \delta_{j+m}=-\delta_j.
\tag{3.4}
\]

#### Proof

For a cyclic order \(\pi=(x_0,\ldots,x_{2m-1})\), shifting the
length-\(m\) window at position \(j\) deletes \(x_j\) and inserts
\(x_{j+m}\).  The first \(m\) opposite pairs partition the ground set,
and the second half reverses them.  This proves necessity and (3.4).

Conversely, (3.2) says that all \(d_0,\ldots,d_{m-1},
a_0,\ldots,a_{m-1}\) are distinct.  Validity of the first \(m\)
transitions forces every \(d_j\) to lie in \(Z_0\); none can have been
inserted earlier because no \(d_j\) equals an \(a_i\).  Hence

\[
 Z_0=\{d_0,\ldots,d_{m-1}\},
 \qquad
 Z_0^c=\{a_0,\ldots,a_{m-1}\}.
\]

The cyclic order

\[
 (d_0,\ldots,d_{m-1},a_0,\ldots,a_{m-1})
\]

therefore has the prescribed first half.  Equation (3.3) gives the
prescribed reverse half. \(\square\)

### Corollary 3.2 (two-path antipodal criterion)

Let \((X_i)_{i=0}^s\) and \((Y_i)_{i=0}^s\) be two prescribed strongly
geodesic paths on \([2m]\).  They can occupy the same oriented positions
in the two halves of one ordinary packet if and only if

\[
 Y_i=X_i^c\qquad(0\le i\le s).
\tag{3.5}
\]

Necessity is (3.4).  For sufficiency, extend \((X_i)\) by Lemma 2.1;
its antipodal path is exactly \((X_i^c)\).

This is the first endpoint obstruction.  Complete one-sided PBBS lower
support does not provide complement-aligned pairs of based paths.  The
PBBS cross-shore identity relates an upper trace to a shifted opposite-
parity lower trace, but it is not the pointwise owner identity (3.5).

### Corollary 3.3 (exact owner antipodal balance)

Let \(\mu_0(X)\) be the occurrence multiplicity of a middle owner \(X\)
in a multiset union of ordinary packets.  Then

\[
 \boxed{\mu_0(X)=\mu_0(X^c)\quad
        \text{for every }X\in\binom{[2m]}m.}
\tag{3.6}
\]

In particular, every coordinate belongs to exactly \(mK\) of the
\(2mK\) owner occurrences.

#### Proof

Within each packet, position \(j+m\) is the complement of position
\(j\), by (3.4).  Pairing these positions proves (3.6).  In one packet,
each ground coordinate belongs to one owner in exactly one position of
each antipodal pair, hence to \(m\) owner positions.  Sum over packets.
\(\square\)

For arbitrary proposed PBBS owner multiplicities \(\mu\) and packet
owner multiplicities \(\nu\), (3.6) gives the exact lower bound

\[
 \|\mu-\nu\|_1
 \ge
 \sum_{\{X,X^c\}}|\mu(X)-\mu(X^c)|,
\tag{3.7}
\]

where the sum is over unordered complement pairs.  Thus a PBBS preimage
transversal cannot be passed unchanged to an ordinary packetization
unless its complement imbalance is negligible.  The one-sided PBBS
support theorem gives no bound on (3.7).

There is an equivalent target formulation.  Pairing selected owners as
\(\{X,X^c\}\) gives, whenever both PBBS occurrences are correct, an edge

\[
 \{\Theta_{q_0}(X),\Theta_{q_0}(X^c)\}
\tag{3.8}
\]

in a multigraph on first-rank targets.  Exact target coverage by an
unchanged complement-balanced transversal requires a perfect matching in
this multigraph; the \(o(W)\)-hole version requires a matching missing
only \(o(W)\) targets.  Nonempty one-sided target fibres do not imply this
Tutte condition.

## 4. Dense PBBS certification forces runs

For this section, assume that a valid common projection has put a PBBS
successor permutation \(g\) and its certified starts on the same even
owner universe as the desired packets.  This assumption is itself not
provided by the present odd PBBS theorem.

Let \(S\) be the selected owner starts.  If two certified depth-\(q\)
PBBS words occupy consecutive packet starts and their overlap is retained,
then their owner words overlap in the last \(q\) states.  Determinism of
the PBBS successor forces the second root to be \(gx\).  Hence every
maximal densely certified packet segment is a consecutive \(g\)-run.

### Lemma 4.1 (exact selected-set boundary)

Put

\[
 r_g(S)=|\{x\in S:gx\notin S\}|.
\tag{4.1}
\]

Then

\[
 r_g(S)
 ={1\over2}\sum_x
   |\mathbf1_S(x)-\mathbf1_S(g^{-1}x)|.
\tag{4.2}
\]

If a cyclic sewing of the selected starts agrees with \(g\) except at
\(t\) successor positions, then

\[
 t\ge r_g(S).
\tag{4.3}
\]

Apart from selected whole \(g\)-cycles, \(r_g(S)\) is exactly the number
of maximal selected \(g\)-runs.

#### Proof

Because \(g\) is a permutation, the number of directed edges leaving
\(S\) equals the number entering it.  The summand in (4.2) is one exactly
at a boundary endpoint, proving (4.2).  Every exiting edge must be replaced
in a sewing whose vertex set is \(S\), proving (4.3). \(\square\)

Selected whole \(g\)-cycles require separate treatment.  A whole cycle
which is not already an ordinary \(2m\)-packet must be cut even though it
contributes zero to (4.1).  In the native PBBS factor every centered
component length is a positive multiple of \(2m+1\), so no native
component is already a length-\(2m\) packet.  This statement does not by
itself supply the missing odd-to-even projection.

### Lemma 4.2 (endpoint circulation)

Let \(R_1,\ldots,R_s\) be retained directed PBBS runs, with initial and
terminal owners \(A_i,B_i\).  If \(B\) is the set of new Johnson bridge
transitions completing them into cycles, then

\[
 |B|\ge {1\over2}
 \left\|\sum_{i=1}^{s}
       (\mathbf1_{B_i}-\mathbf1_{A_i})\right\|_1.
\tag{4.4}
\]

For every coordinate subset \(C\subseteq[2m]\), one also has

\[
 |B|\ge
 \left|\sum_{i=1}^{s}
   \bigl(|B_i\cap C|-|A_i\cap C|\bigr)\right|.
\tag{4.5}
\]

#### Proof

The sum of all Johnson increments around every final cycle is zero.
The sum along the retained runs is

\[
 \sum_i(\mathbf1_{B_i}-\mathbf1_{A_i}),
\]

so the bridge sum is its negative.  One Johnson increment has
\(\ell^1\)-norm two, proving (4.4).  Its scalar change on \(C\) has
absolute value at most one, proving (4.5). \(\square\)

The circulation bounds are necessary but not sufficient.  Form the
bipartite bridge graph whose left vertices are the run terminals \(B_i\),
whose right vertices are the run initials \(A_j\), and where
\(B_iA_j\) is allowed when those owners are Johnson-adjacent with the
required endpoint memory.  The run ends must have a perfect matching to
the run starts in this graph, so every Hall cut must hold.  Even a perfect
matching can create forbidden subtours or cycles of the wrong length and
need not satisfy the packet cocycle.

The ordinary-packet cocycle adds two stronger necessary conditions.

* If positions \(j,j+m\) are both retained PBBS edges but their
  increments do not obey

  \[
    \delta_g(Z_{j+m})=-\delta_g(Z_j),
  \tag{4.6}
  \]

  then at least one of those two positions must be a seam.  The \(m\)
  antipodal pairs are disjoint, so the number of defective pairs is a
  lower bound for the seam count.

* Every coordinate return interval of PBBS transition length at most
  \(H\) must contain a seam.  Otherwise that interval would survive
  inside an ordinary packet, contradicting its cyclic \(H\)-safety.
  Therefore the seam count is at least the maximum number of pairwise
  transition-disjoint retained PBBS short-return intervals.

There is also an exact coordinate-exchange balance.  Let \(r_{uv}\) be
the number of retained directed transitions deleting \(u\) and inserting
\(v\), and let \(b_{uv}\) be the corresponding number of bridge
transitions.  Every ordinary packet uses each unordered opposite pair
once in each orientation.  Hence, for every \(u\ne v\),

\[
 r_{uv}+b_{uv}=r_{vu}+b_{vu},
\tag{4.7}
\]

and for every coordinate \(u\),

\[
 \sum_v(r_{uv}+b_{uv})=K,
 \qquad
 \sum_v(r_{vu}+b_{vu})=K.
\tag{4.8}
\]

It follows immediately that

\[
 |B|\ge
 \sum_{\{u,v\}}|r_{uv}-r_{vu}|.
\tag{4.9}
\]

After the two orientations are paired, their common multiplicities form
an undirected \(K\)-regular multigraph on \([2m]\).  A packet family
decomposes this multigraph into \(K\) perfect matchings.  Consequently,
for every odd coordinate set \(U\subseteq[2m]\),

\[
 |\delta(U)|\ge K.
\tag{4.10}
\]

These odd cuts and the full \(K\)-edge-colourability requirement are
additional endpoint obstructions.  They are not sufficient for the
ordered packet decomposition.

The growing-depth renewal kernel computes global PBBS return shells and
gives lower bounds for global interval packings.  It does not bound either
(4.1), (4.4), (4.6), or the short-return packing **after conditioning on
a size-\(N_{q_0}\) target section**.  This target-conditioned distinction
is essential.

## 5. The sharp seam-window count

Fix a final ordinary packet \(P\).  Mark a transition bad if it does not
follow the selected PBBS successor.  Let \(b_P\) be the number of bad
transitions.

If \(b_P>0\), deleting those transitions leaves \(b_P\) cyclic gaps of
good transitions.  Let their lengths be

\[
 g_1,\ldots,g_{b_P}\ge0,
 \qquad
 \sum_i g_i=2m-b_P.
\tag{5.1}
\]

A depth-\(q\) start is faithful precisely when its next \(q\) transitions
are all good.

### Theorem 5.1 (exact seam collar)

The exact number of unfaithful depth-\(q\) starts in \(P\) is

\[
 u_q(P)=2m-
   \sum_{i=1}^{b_P}(g_i-q+1)_+.
\tag{5.2}
\]

Consequently,

\[
 u_q(P)\ge
 \begin{cases}
  0,&b_P=0,\\
  \min\{2m,b_P+q-1\},&b_P>0.
 \end{cases}
\tag{5.3}
\]

For fixed positive \(b_P\), equality is attained by placing all bad
transitions consecutively.

#### Proof

A good gap of length \(g_i\) contains exactly
\((g_i-q+1)_+\) starts of all-good \(q\)-edge windows, proving (5.2).
For fixed \(\sum g_i=2m-b_P\), the sum in (5.2) is maximized by
concentrating all good transitions in one gap.  Its maximum is
\((2m-b_P-q+1)_+\), which gives (5.3).  A consecutive block of bad
transitions realizes this concentration. \(\square\)

Let

\[
 U_q=\sum_{P\in\mathcal P}u_q(P),
 \qquad
 J=|\{P:b_P>0\}|.
\tag{5.4}
\]

Then

\[
 U_q\ge qJ
\tag{5.5}
\]

and therefore

\[
 \sum_{q=q_0}^{H}U_q
 \ge
 J\sum_{q=q_0}^{H}q
 =J{(H-q_0+1)(H+q_0)\over2}.
\tag{5.6}
\]

If \(J=(1-o(1))K\), (1.5)--(1.6) give

\[
 \boxed{
 \sum_{q=q_0}^{H}U_q
 \ge
 \left({e^{-a^2}(b^2-a^2)\over4}+o(1)\right)W.}
\tag{5.7}
\]

There are twice as many affected signed occurrence positions when lower
and upper traces are both counted.  No lower bound for an \(\ell^1\)
target-profile change is asserted: an affected window may retain the same
target, and different changes may cancel.

There is a useful conditional criterion for \(J\).  Suppose \(g\) is a
permutation on the final owner universe, and let \(b_{2m}(g)\) be the
number of its length-\(2m\) cycles which already satisfy Theorem 3.1.
Distinct \(g\)-cycles are owner-disjoint, while a repeated use of one such
cycle contributes \(2m\) to \(C_0\).  Hence

\[
 J\ge K-b_{2m}(g)-{C_0\over2m}.
\tag{5.8}
\]

Thus (5.7) applies whenever pure packet cycles do not already supply
almost all of the required packet count.

## 6. Why the linear seam collar is not a hole obstruction

Let \(p_q^\sigma\) denote the number of signed depth-\(q\) targets not
covered by any faithful PBBS window.  There are only
\(2mK-U_q=N_{q_0}-\rho-U_q\) faithful occurrence positions.  Pure
capacity gives

\[
 \boxed{
 p_q^\sigma\ge
 [N_q-N_{q_0}+\rho+U_q]_+.}
\tag{6.1}
\]

This is a provenance bound.  Unfaithful ordinary-packet windows remain
legal target occurrences, so the actual hole bound obtained from capacity
alone is only

\[
 h_q^\sigma\ge[N_q-2mK]_+.
\tag{6.2}
\]

At \(q=q_0\), (6.2) is merely \(h_{q_0}^\sigma\ge\rho\).

The difference between (5.7) and (6.1) can be made completely explicit.
Suppose every packet has one seam and the seams are clustered optimally.
Then \(U_q=qK\).  The rank decrement is

\[
 N_q-N_{q+1}
 =N_q{2q+1\over m+q+1}.
\tag{6.3}
\]

Uniformly for \(q_0\le q\le H\),

\[
 N_q-N_{q+1}\gg_{a,b}K.
\tag{6.4}
\]

Indeed, \(N_q/N_{q_0}\) stays between two positive constants depending
only on \(a,b\), while the ratio of the left side of (6.3) to
\(K\le N_{q_0}/(2m)\) is \(\Omega_{a,b}(\sqrt m)\).
Moreover,

\[
 N_{q_0}-N_{q_0+1}
 >\rho+(q_0+1)K
\tag{6.5}
\]

for all sufficiently large \(m\).  Thus the bracket in (6.1) is positive
at \(q=q_0\) and negative at every \(q\ge q_0+1\).  Consequently the
sum of the two capacity lower bounds on the right side of (6.1), in this
optimally clustered case, is exactly

\[
 2\rho+2q_0K
 =\left(ae^{-a^2}+o(1)\right){W\over\sqrt m},
\tag{6.6}
\]

which is \(o(W)\).

There is also a direct upper bound at the first annular rank.  If the
reference PBBS starts cover \(N_{q_0}-\rho\) distinct targets and the
sewing uses \(t\) seams, at most \(q_0t\) depth-\(q_0\) starts meet a
seam.  Therefore

\[
 h_{q_0}^\sigma\le \rho+q_0t.
\tag{6.7}
\]

For \(t=O(K)\), this is \(O(W/\sqrt m)=o(W)\).  The corrected density
therefore makes the first rank robust.  The unresolved issue is the sum
over the whole annulus.

## 7. The exact seam coboundary

Assume for the moment that every selected reference window is rank-correct
at the depth and sign under consideration.  Let
\(\mu_{q,\sigma}^{\rm PBBS}\) be its target occurrence vector, and let
\(\mu_{q,\sigma}^{\rm new}\) be the vector after ordinary-packet sewing.
Define

\[
 \Delta_q^\sigma
 =\mu_{q,\sigma}^{\rm new}
   -\mu_{q,\sigma}^{\rm PBBS}.
\tag{7.1}
\]

Only unfaithful starts contribute, so

\[
 \Delta_q^\sigma
 =\sum_{x\in B_q}
  \left([T_{q,\sigma}^{\rm new}(x)]
       -[T_{q,\sigma}^{\rm PBBS}(x)]\right),
\tag{7.2}
\]

where \(|B_q|=U_q\).  Hence

\[
 \sum_T\Delta_q^\sigma(T)=0,
 \qquad
 \|\Delta_q^\sigma\|_1\le2U_q.
\tag{7.3}
\]

If the total number of seam transitions is \(t\), then a seam lies in
exactly \(q\) cyclic \(q\)-edge windows, and the union bound gives

\[
 U_q\le qt,
 \qquad
 \|\Delta_q^\sigma\|_1\le2qt.
\tag{7.4}
\]

There is an exact finite formula at the first annular rank, including the
rounding remainder.  Suppose the reference load is \(\mathbf1_A\) for
some \(A\subseteq\mathcal T_{q_0}\) with
\(|A|=N_{q_0}-\rho\), and put

\[
 \Delta=\mu_{q_0,\sigma}^{\rm new}-\mathbf1_A,
 \qquad
 L=\sum_T(-\Delta(T))_+,
\tag{7.4a}
\]

\[
 G=|\{T\notin A:\Delta(T)>0\}|.
\tag{7.4b}
\]

On \(A\), every negative entry of \(\Delta\) equals \(-1\), so \(L\)
is the number of old targets lost.  Outside \(A\), exactly \(G\) new
targets are gained.  Therefore

\[
 \boxed{h_{q_0}^\sigma=\rho+L-G,}
 \qquad
 0\le G\le\min\{\rho,L\},
\tag{7.4c}
\]

and hence

\[
 h_{q_0}^\sigma\ge\max\{\rho,L\}.
\tag{7.4d}
\]

Mass conservation gives
\(L=\frac12\|\Delta\|_1\).  There is no lower bound on this norm in
terms of \(U_{q_0}\): affected occurrences may merely permute their
targets, giving \(\Delta=0\).

When \(\rho=0\) and the reference depth-\(q_0\) target vector is exactly
the all-one vector, nonnegativity of the new load gives the exact identity

\[
 h_{q_0}^\sigma
 =\sum_T(-\Delta_{q_0}^\sigma(T))_+
 ={1\over2}\|\Delta_{q_0}^\sigma\|_1.
\tag{7.5}
\]

For deeper ranks the reference average exceeds one, and (7.5) is false:
negative coboundary can be absorbed by forced repeat mass.  The exact
success condition is simply

\[
 \boxed{
 \sum_{q=q_0}^{H}\sum_{\sigma\in\{-,+\}}
 \left(
 N_q-\left|\operatorname{supp}
  (\mu_{q,\sigma}^{\rm PBBS}+\Delta_q^\sigma)
 \right|
 \right)=o(W).}
\tag{7.6}
\]

Equations (5.7) and (7.3) show why a support-blind repair fails: deleting
or separately repairing every affected occurrence costs \(\Theta(W)\).
Equation (6.6) shows why this is not a no-go: an intelligently chosen
positive-density coboundary may cancel against the deeper surplus and
leave only \(o(W)\) holes.

More precisely, if \(J=(1-o(1))K\), then an occurrencewise compiler which
discards every unfaithful lower and upper PBBS window pays at least

\[
 2\sum_{q=q_0}^{H}U_q
 \ge
 \left({e^{-a^2}(b^2-a^2)\over2}+o(1)\right)W
\tag{7.7}
\]

repair letters.  Thus the “retain faithful PBBS windows and repair every
crossing” route is rigorously closed at constant one.  Formula (7.7)
does not apply after target-level deduplication or coboundary cancellation.

## 8. Ordered-Hall and antipodal cuts

The coboundary can be phrased as an exact endpoint Hall obstruction.
This is useful because it identifies what a positive construction must
prove, without confusing PBBS provenance with final target coverage.

Fix a depth \(q\) and let \(\mathcal T_q=\binom{[2m]}{m-q}\).  Form a
bipartite graph \(\Gamma_q\) with left and right copies of
\(\mathcal T_q\).  Put an edge \(S_L T_R\) when there is a rank-correct
PBBS start \(x\) for which

\[
 \Theta_q(x)=S,
 \qquad
 \Theta_q(gx)=T,
\tag{8.1}
\]

and the two occurrences overlap in the required literal owner history.
Let \(\nu(\Gamma_q)\) be its maximum matching size and put

\[
 \delta_q=N_{q_0}-\nu(\Gamma_q).
\tag{8.2}
\]

### Proposition 8.1 (one-step ordered-Hall obstruction)

Suppose \(T=2mK=N_{q_0}-\rho\) selected rank-correct PBBS starts are
packetized.  Suppose their **reference PBBS** depth-\(q_0\) target
histogram has \(h\) holes, and \(t\) packet transitions are not PBBS
transitions.  Then

\[
 \boxed{
 h\ge
 \max\left\{\rho,{\delta_{q_0}+\rho-t\over2}\right\}.}
\tag{8.3}
\]

#### Proof

If the target support has size \(N_{q_0}-h\), the repeat excess is

\[
 c=T-(N_{q_0}-h)=h-\rho.
\tag{8.4}
\]

Delete \(c\) repeated occurrence positions, leaving one representative
of every covered target.  At most \(2c\) cyclic adjacencies meet a deleted
position, and at most \(t\) further adjacencies are seams.  Hence at least

\[
 T-2c-t=N_{q_0}-\rho-2c-t
\]

retained adjacencies give edges of \(\Gamma_{q_0}\).  They form a
bipartite matching: retained target labels are unique on each shore.
Thus

\[
 N_{q_0}-\delta_{q_0}
 \ge N_{q_0}-\rho-2c-t.
\]

Substitute \(c=h-\rho\) and also use \(h\ge\rho\). \(\square\)

Thus a linear ordered-Hall defect cannot be hidden by
\(t=O(K)=o(W)\) seams when constructing the initial PBBS target section.
This proposition concerns the reference histogram; after sewing, windows
crossing later seams acquire the coboundary from Section 7.  The current
PBBS support theorem proves nonempty target fibres, not a lower bound on
\(\nu(\Gamma_{q_0})\).

There is a still sharper packet-specific graph.  Let \(\Lambda_q\) be
the graph on \(\mathcal T_q\) joining targets \(S,T\) when there exist
two PBBS-certified depth-\(q\) occurrences whose owner paths are
pointwise complementary and whose increments are reversed, so they can
occupy antipodal packet positions as in Corollary 3.2.

### Proposition 8.2 (antipodal matching obstruction)

Now let \(h\) denote the **final packet** depth-\(q_0\) hole count, and
let \(U\) be the number of depth-\(q_0\) packet starts which are not
PBBS-certified after sewing.  Then

\[
 \boxed{
 h\ge
 \max\left\{\rho,
 {N_{q_0}-2\nu(\Lambda_{q_0})+\rho-2U\over2}
 \right\}.}
\tag{8.5}
\]

In particular, if every start remains PBBS-certified, then

\[
 h\ge
 {N_{q_0}-2\nu(\Lambda_{q_0})+\rho\over2}.
\tag{8.6}
\]

#### Proof

After deleting the \(c=h-\rho\) repeated occurrences, at least
\(T/2-c-U\) antipodal position pairs retain two unique certified
representatives.  They form a matching in \(\Lambda_{q_0}\).  Therefore

\[
 \nu(\Lambda_{q_0})
 \ge {T\over2}-c-U.
\]

Substituting \(T=N_{q_0}-\rho\) and \(c=h-\rho\) gives (8.5).
\(\square\)

On the native odd PBBS layer, complementation sends an \(m\)-owner to an
\((m+1)\)-set, not to another owner.  Thus the native theorem does not
even define the required same-layer \(\Lambda_q\).  A valid even
projection or aligned trim must be proved first.  After such a projection,
the size of \(\nu(\Lambda_q)\) is an open PBBS compatibility census.
Treating the native graph as empty and invoking (8.6) would be invalid,
because the hypotheses of Proposition 8.2 would not yet hold.

## 9. What the growing-depth PBBS recurrence does and does not give

The established PBBS chronology supplies the following genuine inputs.

1. Every lower target has at least one correct PBBS fan at every depth.

2. The explicit support fan is strongly two-sided geodesic, hence locally
   packet-extendible by Section 2.

3. The split-gap renewal kernel computes all first-return shells and
   gives actual lower bounds for packings of short residence intervals in
   the full PBBS chronology.

None of these statements supplies the following target-conditioned data.

1. A size-\(N_{q_0}\) correct-occurrence section with
   \(r_g(S)=O(K)\).

2. Complement-aligned occurrence pairs saturating
   \(\Lambda_{q_0}\).

3. Small endpoint imbalance in (4.4)--(4.5).

4. A seam set which hits every retained short return and simultaneously
   satisfies the perfect-matching cocycle (3.2)--(3.3).

5. Cancellation of the positive-density annular coboundary in (7.6).

The distinction between separate depths and common starts is also
quantitative.  Applying complete support independently at depth \(H\)
guarantees only \(N_H\) certified long columns, while the corrected packet
mass is \(N_{q_0}\), and

\[
 {N_H\over N_{q_0}}
 =e^{-(b^2-a^2)+o(1)}<1.
\tag{9.1}
\]

This is a constant gap in the **proved supply**, not an upper bound on the
number of PBBS starts which may actually be correct through \(H\).

Likewise, choosing one occurrence independently in every target fibre
gives a static section but no control of its boundary (4.1).  The
growing-depth return recurrence is global; it has not been conditioned on
such a section.  Its present lower families are too sparse to force a
linear obstruction at the corrected packet mass, and its scalar shell
identities do not prove a low-boundary section.

## 10. Exact proved and unproved boundary

The following statements are proved in this report.

* The corrected packet compiler needs exactly (1.4), with
  \(K=\lfloor N_{q_0}/(2m)\rfloor\); its collar is automatically \(o(W)\).

* Every explicit PBBS support fan is locally extendible to an ordinary
  packet, but one seed per packet has vanishing density.

* Dense PBBS use forces selected successor runs and the exact owner-
  complement balance, boundary, endpoint-circulation, exchange-balance,
  odd-cut, antipodal, and short-return constraints in Sections 3--4.

* The exact seam-window formula is (5.2), with the sharp Gaussian
  constant (5.7).

* The positive-density seam collar is only provenance turnover.  The
  actual universal capacity obstruction is \(o(W)\), as shown by
  (6.2)--(6.6).

* The residual problem is exactly the target coboundary (7.6), with the
  ordered-Hall and antipodal necessary conditions (8.3) and (8.5).

The following statement remains unproved.

> **PBBS partial-annulus packet braid.**  After a valid common even
> projection, choose exactly \(2mK=N_{q_0}-\rho\) PBBS starts, containing
> one occurrence of all but \(o(W)\) first-rank targets; decompose them
> into complement-aligned long runs; hit all retained residence intervals
> of length at most \(H\); pair their endpoints into exactly \(K\) ordinary
> packet cocycles; and make the resulting coboundaries satisfy (7.6),
> while the middle collision excess is \(o(W)\).

No current PBBS theorem proves this braid.  Conversely, no theorem here
proves that its coboundary must have a linear negative part.  The corrected
partial density defeats the naive seam-count obstruction exactly because
the deeper ranks have forced capacity surplus.

Therefore the sharp status is

\[
\boxed{
 \text{local PBBS extension: proved;}
 \quad
 \text{dense endpoint/coboundary constraints: proved;}
 \quad
 \text{packet construction or linear actual-hole no-go: open.}}
\tag{10.1}
\]

## 11. Independent decisive-step audit

An independent adversarial proof audit checked the floor normalization,
the two-sided local extension criterion, the ordinary-packet cocycle, the
cyclic gap extremum in Theorem 5.1, and the distinction between affected
windows and actual holes.  It also supplied the owner-complement balance
(3.6)--(3.8), the general first-rank coboundary formula (7.4a)--(7.4d),
and the exchange/odd-cut conditions (4.7)--(4.10).

The audit's decisive correction is retained explicitly: although
\(\|\Delta_q\|_1\le2U_q\), there is no positive lower bound on
\(\|\Delta_q\|_1\) in terms of \(U_q\), and neither quantity is an actual
hole count.  The only unconditional first-rank capacity loss is the
rounding term \(\rho\); the larger expression in (6.1) is a loss of
faithful PBBS provenance.  Thus no linear actual-hole conclusion is used
anywhere in this report.
