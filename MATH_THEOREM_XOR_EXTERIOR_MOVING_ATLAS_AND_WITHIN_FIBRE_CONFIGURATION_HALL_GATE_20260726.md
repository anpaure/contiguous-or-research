# An XOR-addressed exterior-moving atlas: all-cut window escape, exact cell rainbows, and the within-fibre Hall gate

Date: 2026-07-26

Method: pure mathematics only.  The proved literal return-free cube
compiler is used as a black box.  No computation, finite search, solver,
or probabilistic independence between target marginals is used.

## 0. Result

Put

\[
 G=\mathbb F_2^\ell,\qquad |G|=2m=2^\ell,
 \qquad W=\binom{2m}{m}.
\tag{0.1}
\]

There is an exact owner partition which lies outside the closed
complete-status-component model.  Its frame is addressed by the owner
itself.  More precisely, there is a fixed-point-free involution
\(\tau:G\to G\), a translation matching

\[
 M_{a(s)}=\{\{x,x+a(s)\}:x\in G\}/2,
 \qquad a(s)=s+\tau(s),
\tag{0.2}
\]

and an owner hash

\[
 \sigma(X)=\bigoplus_{x\in X}x,                         \tag{0.3}
\]

such that the selected cells

\[
 \mathscr C(X)=\mathcal C_{M_{a(\sigma(X))}}(X)          \tag{0.4}
\]

are equal or disjoint and partition the middle layer.  Distinct selected
cells are not obtained by selecting one shore on a common matching-status
overlap component.  They are already disjoint because the address changes
inside a cell only along one \(\tau\)-edge, on which the matching label is
constant.

Let

\[
 r\log m=o(m),\qquad H<r,\qquad H=o(m^{2/3}),             \tag{0.5}
\]

and assume that \(r\) is an admissible dimension for the certified
two-sided return-free compiler through depth \(H\).  For example, the
intended range is

\[
 r=m^{2/3+o(1)},\qquad H=\lceil\sqrt{m\log m}\rceil.      \tag{0.6}
\]

After discarding \(L=e^{-\Omega(m)}W\) owners, the cells in (0.4) admit
one complement-equivariant integral subdivision into owner-disjoint
literal \(Q_r\)-packets, with one complete all-depth factor state in
each packet, having the following properties.

1. **Statewise all-cut escape.**  Fix \(\delta>0\).  Simultaneously for
   every coordinate set \(B\subseteq G\) with
   \(2\delta m\le |B|\le2(1-\delta)m\), and every \(1\le q\le H\),
   the number of retained based depth-\(q\) windows containing a physical
   exchange with exactly one endpoint in \(B\) is at least

   \[
      \bigl(\delta(1-\delta)-o_\delta(1)\bigr)W.          \tag{0.7}
   \]

   Thus no positive-density coordinate projection is frozen in the
   selected integral state.  This is an occurrence statement, not merely
   connectedness of the union of an option catalogue.

2. **Exact parent-cell rainbows.**  For every retained selected XOR cell,
   every sign, and every \(q\le H\), all literal targets emitted by the
   owners of that cell are pairwise distinct.  Consequently all remaining
   target collisions are between distinct selected XOR cells.

3. **Exact complement symmetry.**  The owner successor can be chosen so
   that \(P(X^c)=P(X)^c\).  Hence the lower and upper trace families are
   fused in one state.

4. **A nontrivial configuration-Hall theorem.**  Put

   \[
      q_0=\lceil40\log m\rceil .                            \tag{0.8}
   \]

   The same state can be chosen so that every exact XOR target bin is
   saturated at every \(q_0\le q\le H\), on both signs.  It may also be
   chosen translation-equivariantly, in which case the same assertion
   holds at every odd \(q\le H\).  Therefore the exact configuration-Hall
   inequality holds with zero reserve for every nonnegative target weight
   which, on those depths, depends only on depth, sign, and exact target
   XOR.

The theorem does **not** prove the unrestricted configuration-Hall
inequality.  On the depth set consisting of \([q_0,H]\) and all odd
depths, it reduces the dual to a literal within-fibre statement.  If
\(F_{q,\varepsilon,t}\) is one exact XOR fibre, the remaining linear gate
on those depths is

\[
 \boxed{
 \sum_{\mathscr C}\max_{\omega\in\Omega_{\mathscr C}}
       \sum_{T\in J_{\mathscr C}^{\omega}\cap A}y_T
 \ \ge\ \sum_{T\in A}y_T-o(W\|y\|_\infty) }               \tag{0.9}
\]

for arbitrary unions \(A\) of literal subsets of the fibres and arbitrary
nonnegative weights inside them.  Hash-bin cardinality, projection escape,
and parent-cell rainbows do not imply (0.9), because several different
XOR cells can still emit the same literal target.  This is the exact
surviving Gaussian-window missing-shadow gate.  At the short even depths
\(2\le q<q_0\), the preliminary XOR-bin capacity inequality itself also
remains open.  No quadratic CPCR objective is used.

## 1. The owner-addressed cell partition

Write

\[
 G=K\times\mathbb F_2,
 \qquad K=\mathbb F_{2^{\ell-1}}.
\tag{1.1}
\]

Choose \(\alpha\in K\setminus\{0,1\}\) and define

\[
 \tau(u,0)=(\alpha u,1),\qquad
 \tau(v,1)=(\alpha^{-1}v,0).                         \tag{1.2}
\]

The label of the \(\tau\)-edge indexed by \(u\) is

\[
 a_u=((1+\alpha)u,1).                                \tag{1.3}
\]

Thus the labels are precisely

\[
 \mathcal A=K\times\{1\}.                           \tag{1.4}
\]

For \(a\ne0\), let \(\mathcal C_a(X)\) be the complete status cell of
\(X\) relative to the translation matching \(M_a\).  It is the literal
orientation cube obtained by freely orienting the split \(M_a\)-edges and
freezing every full or empty edge.

### Lemma 1.1 (cell stability)

The cells in (0.4) are equal or disjoint and exhaust
\(\binom Gm\).  They are preserved by complementation.

#### Proof

Put \(s=\sigma(X)\) and \(a=s+\tau(s)\).  Flipping one split edge of
\(M_a\) changes the XOR by exactly \(a\).  Hence every
\(Y\in\mathcal C_a(X)\) has

\[
 \sigma(Y)\in\{s,s+a\}=\{s,\tau(s)\}.               \tag{1.5}
\]

Both hash values choose the same label \(a\), and \(X,Y\) have the same
full/empty/split status.  Therefore

\[
 Y\in\mathscr C(X)\quad\Longrightarrow\quad
 \mathscr C(Y)=\mathscr C(X).                        \tag{1.6}
\]

Intersecting selected cells are consequently equal, and every owner lies
in its selected cell.  Also

\[
 \bigoplus_{x\in G}x=0,
 \qquad \sigma(G\setminus X)=\sigma(X),              \tag{1.7}
\]

because \(\ell\ge4\).  Complementation preserves the selected matching
and exchanges full and empty statuses, proving the last assertion.
\(\square\)

This construction bypasses the complete-status-component obstruction.
It does not start with overlapping whole frame decompositions and then
try to choose one shore on their connected overlap graph.  The owner hash
makes the chosen variable-frame cells disjoint before any packet factor is
installed.

There is also a precise limitation on what “beyond status cells” can mean
while the local packet is still cubical.

### Lemma 1.2 (literal cube rigidity)

Every isometric literal \(Q_r\) in \(J(2m,m)\) is an orientation packet
\[
 \{F\cup Z:Z\text{ chooses one endpoint of each edge of an
 \(r\)-matching }M\}.                                \tag{1.8}
\]
In particular, one literal cube cannot change its coordinate matching
during a trajectory.  A construction beyond common status-component
rounding must either use an owner-addressed mosaic such as (0.4), or use
noncubical path/cycle packets.

#### Proof

At one cube vertex, write two incident Johnson moves as
\(a\mapsto b\) and \(c\mapsto d\), with \(a,c\) selected and \(b,d\)
unselected.  If \(a=c\), the two neighboring cube vertices are Johnson
adjacent, although their cube distance is two; the same contradiction
holds if \(b=d\).  Cross equalities are impossible at the base vertex.
Thus the supports of incident cube axes are disjoint.

In the square generated by these two axes, isometry forces the opposite
vertex to be at Johnson distance two from the base.  The only common
neighbor of the two adjacent vertices with that property is obtained by
performing both disjoint exchanges.  Hence opposite square edges carry
the same coordinate exchange.  Propagating this identity across cube
squares makes the exchange attached to each abstract axis independent of
the cube vertex.  The \(r\) exchanges have pairwise disjoint supports,
and all remaining selected and unselected coordinates are frozen.  This
is exactly (1.8). \(\square\)

## 2. Exact frame masses and a split-edge census

For \(0\le k\le2m\), let

\[
 H_k(s)=\#\{X\in\tbinom Gk:\sigma(X)=s\}.             \tag{2.1}
\]

Fourier inversion gives

\[
\begin{aligned}
 H_k(0)&={1\over2m}\left[\binom{2m}k+(2m-1)B_k\right],\\
 H_k(s)&={1\over2m}\left[\binom{2m}k-B_k\right]
       \quad(s\ne0),                                  \tag{2.2}\\
 B_k&=[z^k](1-z^2)^m.
\end{aligned}
\]

In particular, the two middle hash fibres which select a fixed
\(a\in\mathcal A\) have total mass

\[
 |\Omega_a|={W\over m}+O\!\left(e^{-\Omega(m)}W/m\right). \tag{2.3}
\]

We need a uniform refinement of (2.3).

### Lemma 2.1 (conditional split-edge census)

For every \(a\in\mathcal A\), every edge \(e\in M_a\), and the associated
two-fibre owner class \(\Omega_a\),

\[
 \#\{X\in\Omega_a:|X\cap e|=1\}
 ={W\over2m-1}+O(m2^m)
 =\left({m\over2m-1}+O(e^{-\Omega(m)})\right)|\Omega_a|. \tag{2.4}
\]

The error is uniform in \(a,e\).

#### Proof

Write \(e=\{x,x+a\}\), and let the two allowed owner hashes be
\(\{s,s+a\}\).  After choosing one of the two endpoints of \(e\), the
remaining \(m-1\) points have XOR in one prescribed coset pair modulo
\(\langle a\rangle\).  Fourier inversion on \(G\), after deleting the
two factors belonging to \(e\), has trivial-character contribution

\[
 {2\over m}\binom{2m-2}{m-1}={W\over2m-1}.           \tag{2.5}
\]

The indicator of the two allowed hashes annihilates every character with
\(\chi(a)=-1\).  For \(\chi(a)=1\), the remaining generating polynomial
is obtained from
\((1-z^2)^m\) by deleting two equal-sign linear factors.  Every relevant
coefficient has modulus \(O(2^m)\).  Summing fewer than \(2m\) Fourier
terms and dividing by \(2m\) gives the stated \(O(m2^m)\) bound.  Since
\(W=4^{m-o(m)}\), (2.3) converts (2.5) to the second form in (2.4).
\(\square\)

## 3. The complete-bipartite cut identity

For \(B\subseteq G\), let

\[
 b_a(B)=\#\{e\in M_a:|e\cap B|=1\}.                 \tag{3.1}
\]

The matchings \(M_a\), \(a\in\mathcal A\), partition the edge set of
the complete bipartite graph between
\(K\times\{0\}\) and \(K\times\{1\}\).  Therefore, writing

\[
 b_i=|B\cap(K\times\{i\})|,
\tag{3.2}
\]

we have the exact identity

\[
 \sum_{a\in\mathcal A}b_a(B)
 =b_0(m-b_1)+b_1(m-b_0).                              \tag{3.3}
\]

If \(2\delta m\le |B|\le2(1-\delta)m\), complement \(B\) if needed so
that \(|B|\le m\).  Since \(2b_0b_1\le(b_0+b_1)^2/2\),

\[
 \sum_{a\in\mathcal A}b_a(B)
 \ge2\delta(1-\delta)m^2.                            \tag{3.4}
\]

Let \(d_B(\mathscr C)\) be the number of split axes of a selected cell
which cross \(B\).  Lemma 2.1, summed first over crossing edges and then
over frame labels, gives, uniformly for every such \(B\),

\[
 \sum_{\mathscr C}|\mathscr C|d_B(\mathscr C)
 \ge\bigl(\delta(1-\delta)-o_\delta(1)\bigr)mW.      \tag{3.5}
\]

This is a statewise incidence identity for the selected cell partition.
It is stronger than saying that the union of all possible frame edges is
connected.

## 4. Balanced selector arrays inside every cell

Discard cells of dimension below \(m/3\).  Standard binomial
concentration, conditioned on the middle layer and union-bounded over the
\(2m\) hash values, shows that their owner mass is
\(e^{-\Omega(m)}W\).

In a retained cell \(\mathscr C\cong Q_D\), choose

\[
 s_0=\left\lceil4r\log_2(2em)\right\rceil            \tag{4.1}
\]

selector axes.  By (0.5), \(s_0+r<D\) for large \(m\).  Let \(E'\) be
the remaining \(d=D-s_0\) split axes and consider the complete catalogue

\[
 \mathfrak C_{\mathscr C}
 =\{(R,\eta,\pi):R\in\tbinom{E'}r,
      \eta\in\mathbb F_2^r,\ \pi\in S_r\}.           \tag{4.2}
\]

Its size \(M\) satisfies \(M\le(2em)^r\) and

\[
                         M/2^{s_0}\le M^{-3}.         \tag{4.3}
\]

Freeze the selector orientations, distribute the labels in (4.2) among
the \(2^{s_0}\) branches as evenly as possible, and in a branch labelled
\((R,\eta,\pi)\) partition parallelly into \(Q_r\)'s with active set
\(R\).  Install the \((\eta,\pi)\)-conjugate compiler in all those
subcubes.  This is an exact owner partition.  The owner-mass distribution
of catalogue labels differs from uniform by total variation at most

\[
                         \epsilon_m=M/2^{s_0+1}=o(m^{-A})
\tag{4.4}
\]

for every fixed \(A\).

The arrays can be made complement-equivariant.  On a pair of distinct
complementary cells choose an array on one and transport it to the other.
On a self-complementary cell, pair complementary selector branches and
assign conjugate labels.  The same pairing can be made equivariant under
ground translations after discarding the exponentially small family of
cells with translation stabilizer larger than \(\langle a\rangle\).
These finite orbit pairings change (4.4) by at most a constant factor.

### Lemma 4.1 (exact cell rainbow)

Separately for every \(q\le H\) and both signs, all targets emitted by
owners of one selected cell are distinct.

#### Proof

Inside one \(Q_r\)-packet this is the certified literal trace
injectivity.  Two parallel subpackets in the same selector branch differ
on a split axis outside their active set.  The fixed selected endpoint of
that spectator axis survives every lower intersection and every upper
union, so their targets differ.  Two selector branches differ on a
selector axis, which is also a fixed spectator and gives the same
separation.  These cases exhaust pairs of owners in the cell.
\(\square\)

Thus each selected cell is an exact literal parent-cell rainbow.  Notice
that no assertion about targets from two different cells has been used.

## 5. Proof of statewise all-cut window escape

For a packet \(P\), let \(t_B(P)\) be the number of its active axes
crossing \(B\).  Under the uniform active-set marginal in one cell,

\[
 \mathbb E\,t_B(P)
 ={r\over D-s_0}\bigl(d_B(\mathscr C)-O(s_0)\bigr).  \tag{5.1}
\]

The deterministic selector array changes the expectation by at most
\(r\epsilon_m\).  Since \(D\le m\), summing (5.1) over the owner mass of
all cells and using (3.5) yields

\[
 \sum_P|P|t_B(P)
 \ge\bigl(\delta(1-\delta)-o_\delta(1)\bigr)rW.      \tag{5.2}
\]

The loss from selector axes is at most \(rs_0W/m=o(rW)\), and all
discarded cells have exponentially small mass.  The estimate is uniform
in \(B\), so it holds simultaneously for every macroscopic cut in the
one constructed state.

In a doubled-permutation factor, every packet axis occurs twice on every
\(2r\)-cycle.  Across all based depth-\(q\) windows of a packet, the total
number of incidences with its \(t_B(P)\) crossing axes is

\[
                         |P|{qt_B(P)\over r}.         \tag{5.3}
\]

One window contains at most \(q\) such incidences.  Hence at least
\(|P|t_B(P)/r\) of the based windows cross \(B\).  Sum this inequality
and apply (5.2) to obtain (0.7).

This proves genuine chronological projection escape.  In particular,
the old frozen-carrier Hall cut cannot be applied to this atlas by merely
renaming its carrier.

## 6. Exact target-hash ledger

For a packet of frame \(a\), write its active axes as

\[
 e_j=\{x_j,x_j+a\},\qquad 1\le j\le r,              \tag{6.1}
\]

and encode an owner by \(z\in\mathbb F_2^r\).  If a return-free
depth-\(q\) window uses the support \(J\), then, after absorbing frozen
coordinates in \(\gamma\), its lower and upper hashes are

\[
\boxed{
\begin{aligned}
 \sigma(T^-)&=\gamma+\bigoplus_{j\in J}x_j
                  +\left(\sum_{j\notin J}z_j\right)a,\\
 \sigma(T^+)&=\gamma+\bigoplus_{j\in J}x_j
                  +\left(q+\sum_{j\notin J}z_j\right)a.
\end{aligned}}                                                \tag{6.2}
\]

Modulo \(\langle a\rangle\), both signs therefore have the same
\(q\)-subset-XOR statistic.

We retain only cells whose split-label set is spectrally balanced.  A
Chernoff bound on every nontrivial character of
\(G/\langle a\rangle\), followed by a union bound over frames and
characters and conditioning on the middle layer, discards only
\(e^{-\Omega(m)}W\) owners and gives

\[
 {5m\over24}\le D_\chi^\pm\le {7m\over24}           \tag{6.3}
\]

on the two character shores, for every nontrivial \(\chi\).  Removing
the \(s_0=o(m)\) selector labels leaves a pool \(E'\) for which

\[
 {\bigl||E'_\chi{}^+|-|E'_\chi{}^-|\bigr|\over |E'|}
 \le {1\over3}                                      \tag{6.4}
\]

for all sufficiently large \(m\).

Let

\[
 k_j(\chi)=
 { [u^j](1+u)^{d_+}(1-u)^{d_-}\over\binom dj}.       \tag{6.5}
\]

Its logarithmic derivative gives the exact recurrence

\[
 k_{j+1}={d_+-d_-\over d-j}k_j-{j\over d-j}k_{j-1}. \tag{6.6}
\]

Since \(H=o(m)\), (6.4)--(6.6) imply inductively, with
\(\lambda=3/4\),

\[
                         |k_j(\chi)|\le\lambda^j
                         \qquad(0\le j\le H).        \tag{6.7}
\]

Fourier inversion on the quotient of size \(m\) now gives, uniformly in
the quotient hash \(w\),

\[
 \#\left\{J\in\tbinom{E'}q:
          \bigoplus_{e\in J}\bar e=w\right\}
 ={1\over m}\binom dq\left(1+O(m\lambda^q)\right). \tag{6.8}
\]

### Lemma 6.1 (one-state selector-array hash law)

In the integral selector-array state of Section 4, the target hash of a
uniform based owner occurrence in one retained cell has distribution

\[
 \Pr(\sigma(T^\varepsilon)=t)
 ={1\over2m}
   \left(1+O(m\lambda^q)+O(m\epsilon_m)\right)       \tag{6.9}
\]

uniformly in the cell, \(t\), the sign, and \(q\le H\).

#### Proof

Fix a selector branch and a label \((R,\eta,\pi)\).  The parallel
\(Q_r\)-subpackets in that branch range over every orientation of
\(E'\setminus R\).  In each doubled-permutation cycle, every cyclic
\(q\)-interval in the order \(\pi\) occurs equally often as the support
of a based window.  When \(\pi\) ranges uniformly over \(S_r\), every
\(q\)-subset of \(R\) consequently occurs equally often.  Finally, when
\(R\) ranges uniformly over \(\binom{E'}r\),

\[
 {\binom{d-q}{r-q}\over\binom dr\binom rq}
 ={1\over\binom dq},                                  \tag{6.10}
\]

so the resulting physical support is uniform on \(\binom{E'}q\).

Modulo \(\langle a\rangle\), equation (6.2) now reduces the target-hash
law exactly to the subset-XOR law (6.8).  For a fixed support, the
orientations outside it range uniformly.  Because
\(q<r<D-s_0\), at least one such orientation remains, and its parity
balances the two exact lifts of each quotient hash.  Thus the uniform
catalogue gives probability

\[
 {1\over2m}\left(1+O(m\lambda^q)\right).             \tag{6.11}
\]

The deterministic branch distribution differs from the uniform
catalogue by total variation at most \(\epsilon_m\).  An event can change
in probability by at most this amount, which is a relative
\(O(m\epsilon_m)\) error on the scale \(1/(2m)\).  This proves (6.9).
\(\square\)

Hence, if \(S=W-L\) is the retained owner mass and
\(Z_{q,t}^\varepsilon\) is the number of occurrences sent to exact target
hash \(t\), then this one simultaneous integral state satisfies

\[
 Z_{q,t}^\varepsilon
 ={S\over2m}\left(1+O(m\lambda^q)+O(m\epsilon_m)
                         +O(e^{-\Omega(m)})\right).   \tag{6.12}
\]

The state is common to all depths and both signs; no marginal estimates
have been multiplied.

For \(q_0\le q\le H=o(m^{2/3})\),

\[
 \log{W\over N_q}
 ={q^2\over m}+O\left({q\over m}+{q^3\over m^2}\right),
 \qquad N_q=\binom{2m}{m-q}.                         \tag{6.13}
\]

At the same ranks, the exact XOR-fibre formula (2.2) gives

\[
 H_{m\pm q}(t)
 ={N_q\over2m}\left(1+O(e^{-\Omega(m)})\right).      \tag{6.14}
\]

uniformly in \(t\).  With \(q_0=\lceil40\log m\rceil\), the error in
(6.12) is \(o(q^2/m)\), whereas (6.13) supplies a positive relative
surplus of order \(q^2/m\) at the smallest depth and a larger surplus
afterwards.  Therefore

\[
 \boxed{Z_{q,t}^\varepsilon\ge H_{m\pm q}(t)}
 \qquad(q_0\le q\le H, t\in G, \varepsilon\in\{-,+\}).
\tag{6.15}
\]

If the arrays are chosen translation-equivariantly, target load is
constant on every ground-translation orbit.  At odd target rank every
such orbit is free, has size \(2m\), and contains every XOR value exactly
once.  Consequently

\[
                         Z_{q,t}^\varepsilon={S\over2m}
                         \qquad(q\text{ odd}).       \tag{6.16}
\]

Since \(S>N_q\) for every \(q\ge1\) and large \(m\), (6.16) also
saturates every odd-depth hash bin.

## 7. The exact configuration-Hall test

Fuse complementary selected cells into choice groups.  A legal option
\(\omega\in\Omega_{\mathscr C}\) is one complete complement-compatible
packet subdivision and compiler assignment for that group.  Let

\[
 J_{\mathscr C}^{\omega}
 \subseteq\{(q,\varepsilon,T):1\le q\le H\}           \tag{7.1}
\]

be its literal target support, with multiplicity discarded.  The exact
reserve-\(E\) configuration-Hall inequality is

\[
 \sum_{\mathscr C}\max_{\omega\in\Omega_{\mathscr C}}
       \sum_{v\in J_{\mathscr C}^{\omega}}y_v
 +\rho_E(y)
 \ge\sum_vy_v                                      \tag{7.2}
\]

for every nonnegative target weight \(y\).  It is the support-function
dual of selecting one state per group and assigning each covered target
to one provider.  It is exactly the missing-shadow relaxation; repeated
occurrences inside or between groups carry no penalty.

### Theorem 7.1 (hash-measurable configuration Hall)

Let \(\mathcal Q\) consist of the depths in \([q_0,H]\), together with
the odd depths in \([1,H]\).  Suppose

\[
 y_{q,\varepsilon,T}=c_{q,\varepsilon,\sigma(T)}
 \qquad(q\in\mathcal Q)                              \tag{7.3}
\]

for arbitrary nonnegative constants \(c_{q,\varepsilon,t}\), and let
\(y=0\) off these depths.  Then (7.2) holds with \(E=0\).

#### Proof

Use the one simultaneous integral state constructed in Sections 4 and 6.
Lemma 4.1 says that within a selected cell support size equals occurrence
count, so

\[
\begin{aligned}
 \sum_{\mathscr C}\max_\omega
       \sum_{v\in J_{\mathscr C}^{\omega}}y_v
 &\ge
 \sum_{q\in\mathcal Q,\varepsilon,t}
       c_{q,\varepsilon,t}Z_{q,t}^\varepsilon\\
 &\ge
 \sum_{q\in\mathcal Q,\varepsilon,t}
       c_{q,\varepsilon,t}H_{m+\varepsilon q}(t)\\
 &=\sum_vy_v,
\end{aligned}                                                   \tag{7.4}
\]

where (6.15) and (6.16) give the second inequality.  The same complete
state is used in every summand.  No product of marginal probabilities is
present.  \(\square\)

Thus the exact all-ones weight, every hash-bin indicator, and every
nonnegative combination of them fail to separate the atlas.  The old
fixed-frame Gaussian profile cut is also unavailable: Section 5 gives a
positive density of actual windows crossing every macroscopic coordinate
cut.

Theorem 7.1 does not cover a weight which distinguishes two literal
targets in the same exact hash fibre.  This is not a technical omission:
hash saturation controls the sums in (7.4), while two different selected
cells may put those sums on the same targets.

## 8. Exact remaining missing-shadow identity

Fix one integral state and one fibre

\[
 F=F_{q,\varepsilon,t}
 =\{T:|T|=m+\varepsilon q,\ \sigma(T)=t\}.           \tag{8.1}
\]

Because every selected cell is a rainbow, define the cross-cell load

\[
 z_T=\#\{\mathscr C:T\in J_{\mathscr C}\}.           \tag{8.2}
\]

Put

\[
 R_F=\sum_{T\in F}z_T-|F|,
 \qquad
 E_F=\sum_{T\in F}(z_T-1)_+.                         \tag{8.3}
\]

Whenever the hash bin is saturated, \(R_F\ge0\).  The number of missing
literal targets in the fibre is exactly

\[
 \boxed{
 |\{T\in F:z_T=0\}|=E_F-R_F.}                        \tag{8.4}
\]

Indeed,

\[
 \sum_{T\in F}z_T
 =|\{T:z_T\ge1\}|+E_F,                               \tag{8.5}
\]

and subtracting \(|F|\) proves (8.4).  Hence the desired conclusion is

\[
 \sum_{q\le H,\varepsilon,t}(E_F-R_F)=o(W).           \tag{8.6}
\]

This is an \(L^1\) cross-cell overlap cancellation.  It is strictly weaker
than controlling the quadratic floor energy and is exactly equivalent to
the missing-shadow objective after the owner leave.  A positive proof may
establish (8.6) directly, or prove the full configuration inequality
(7.2).  A negative proof must exhibit a literal within-fibre weight in
(0.9) at the solved depths.  At a short even depth it may instead exhibit
an exact hash-bin deficit.  Neither a frozen coordinate projection nor a
hash-fibre cardinality imbalance can obstruct the Gaussian/mesoscopic
range covered by Theorem 7.1.

## 9. Audited boundary

The following are proved.

* The owner-addressed XOR cells form an exact complement-symmetric
  variable-frame partition.
* One deterministic packet/factor state has quantitative chronological
  escape across every macroscopic coordinate cut simultaneously.
* Every selected XOR cell is an exact all-depth, two-sign literal rainbow.
* The exact XOR-bin configuration dual is satisfied throughout the
  Gaussian/mesoscopic window and at every odd protected depth.
* The only remaining target collisions are cross-cell, and their exact
  contribution to missing shadows is (8.4).

The following are not proved.

* The unrestricted within-fibre configuration-Hall inequality (0.9).
* Exact XOR-bin saturation at the even depths \(2\le q<q_0\).
* An integral augmentation which makes the sum in (8.6) \(o(W)\).
* A non-dyadic extension of the XOR-addressed cell partition.
* A theorem that one individual packet changes its translation matching
  during a cycle.  The result is projection-free at the level of the one
  selected owner atlas: different disjoint owner cells use different
  translation frames, while each packet itself is an ordinary literal
  orientation cube.

Accordingly this note gives a genuine construction beyond global
status-component rounding and closes its owner, projection, complement,
and parent-rainbow tests.  The remaining coefficient-one question is the
literal within-XOR-fibre configuration inequality, together with the
short-even XOR-bin discrepancy; it is not CPCR.
