# Expansion-rich status-orbit resets in the rank-twisted packet atlas

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 \Omega=\binom{[2m]}m,\qquad W=|\Omega|.
\]

Choose logarithmic rank-twisted macroblocks

\[
 B_j=A_j\mathbin{\dot\cup}C_j,qquad |A_j|=|C_j|=d,
 \qquad d\equiv0\pmod4,qquad d=\Theta(\log m),
\]

leaving fewer than \(2d\) residual coordinates frozen as part of each
cell label. Let

\[
 N=d\lfloor m/d\rfloor=m-O(d)
\]

be the number of rank-selected frame edges. Assume that the admissible
compiler dimension \(R\) satisfies

\[
 H=o(R),\qquad R\log m=o(m).                         \tag{0.1}
\]

The following statements are proved.

1. All but \(o(W/H)\) middle owners admit an exact, owner-disjoint
   partition into physical reset cubes \(Q_S\) in which at least a fixed
   fraction of the axes cross rank-twisted parent-status cells.
2. These cubes admit a transversal \(Q_R\)-packetization and an
   exponential orbitwise reset menu such that every packet has at least

   \[
                              R/40                         \tag{0.2}
   \]

   genuinely parent-crossing active axes.
3. Installing the diverse-order compiler gives a partial owner
   permutation on

   \[
                         G=W-o(W/H)                         \tag{0.3}
   \]

   owners which is cyclically \(H\)-safe and has exactly

   \[
                         \kappa={G\over2R}=o(W/H)             \tag{0.4}
   \]

   cycles.
4. Fix a perfect matching \(\Pi\) whose edges lie wholly inside the
   macroblock halves \(A_j,C_j\), pairing the residual coordinates
   separately. Every active direction crosses one half to the other, so

   \[
                              E_\Pi(P)=G.                       \tag{0.5}
   \]

   Thus the linear genuine pair-breaking requirement is met maximally.
   At least \((1/40-o(1))G\) transitions also cross old parent-status
   labels.
5. Orbitwise reset choices can be made exactly run-neutral. They preserve
   the owner set, cycle count, \(H\)-safety, common run vector, and hence
   every lower and upper point margin at every depth.

This closes the growing-reset **owner, density, safety, cycle, and point-
projection** gates. It does not prove \(o(W)\) aggregate literal quota
error. The exact remaining assertion is a deterministic all-depth,
two-sign slab-option configuration Hall theorem. Uniform, independent,
or random-Latin option choices retain a linear Poisson floor defect.

## 1. The full status-orbit factorization

Fix a local-rank vector. It fixes one perfect matching in each
macroblock, hence a global product matching with \(N\) edges. Pair those
frame edges into \(N/2\) designated pairs

\[
                         (f_j,g_j),qquad 1\le j\le N/2.          \tag{1.1}
\]

For a parent status word, let \(J\) be the positions at which the two
statuses are \(\{0,1\}\), and put \(t=|J|\). Swapping \(0\leftrightarrow1\)
independently at positions in \(J\) partitions the parent labels into
\(2^t\)-element orbits. The set \(J\), every status outside \(J\), and
the number \(S\) of singleton frame edges are invariant throughout such
an orbit.

Write at one mixed position

\[
 f=\{a,c\},\qquad g=\{a',c'\},qquad a,a'\in A,quad c,c'\in C. \tag{1.2}
\]

Across the two parent labels \((1,0)\), \((0,1)\) and their singleton
orientations, the four local owner states are

\[
                         \{a\},\ \{c\},\ \{a'\},\ \{c'\}.     \tag{1.3}
\]

They have two relevant one-factorizations:

\[
 \mathcal M_0=\bigl\{\{a,c\},\{a',c'\}\bigr\},
 \qquad
 \mathcal M_1=\bigl\{\{a,c'\},\{c,a'\}\bigr\}.                \tag{1.4}
\]

The first preserves the two parent labels and the second crosses them.
Every edge in both factorizations is a literal cross-half Johnson edge.

### Theorem 1.1 (exact orbit reset atlas)

For every status orbit and every word

\[
                         \varepsilon\in\{0,1\}^{J},             \tag{1.5}
\]

using \(\mathcal M_{\varepsilon_j}\) at position \(j\) partitions the
same orbit owner union into \(2^t\) coordinate-disjoint physical
\(Q_S\)'s. The axes consist of one chosen edge from (1.4) at every
position in \(J\), together with all unchanged singleton frame edges
outside \(J\).

#### Proof

At one position, either one-factorization in (1.4) partitions the same
four states (1.3) into two disjoint physical edges. Taking the Cartesian
product over the \(t\) mixed positions gives \(2^t\) channel cubes of
dimension \(t\). Tensoring the common singleton orientations outside
\(J\) raises every channel dimension to

\[
        t+\#\{\hbox{singleton frame edges outside }J\}=S.
\]

The channel cubes partition the entire orbit union. Distinct rank
vectors, status orbits, residual pins, and channel labels are already
owner-disjoint. \(\square\)

Thus (1.5) is a genuine exponential physical reset menu. It is not an
auxiliary colour lift.

## 2. Exponentially small exceptional owner mass

For a fixed rank vector under the unconditioned endpoint-state census,
the four states of every frame edge are independent. A designated pair
has \(16\) states, exactly four of which have status pair \(\{0,1\}\).
Consequently

\[
                         t\sim\operatorname{Bin}(N/2,1/4).      \tag{2.1}
\]

The total singleton count is independently censused as

\[
                         S\sim\operatorname{Bin}(N,1/2).        \tag{2.2}
\]

The elementary Chernoff bounds give

\[
 \Pr(t<N/16)\le e^{-N/64},
 \qquad
 \Pr(S<N/3)\le e^{-N/36}.                         \tag{2.3}
\]

There are at most

\[
 (2d+1)^{\lfloor m/d\rfloor}
 =\exp\!\left(O\!\left({m\log d\over d}\right)\right)
 =2^{o(m)}                                               \tag{2.4}
\]

rank vectors, and the residual pins contribute \(2^{O(d)}=2^{o(m)}\).
For a fixed vector, the subsets actually inducing it form a subfamily of
the unconditioned space used in (2.1)--(2.2), so the union bound is valid.
After restricting to the middle rank, (2.3)--(2.4) show that the bad
owner mass is \(e^{-\Omega(m)}W=o(W/H)\).

Every retained reset cube therefore satisfies

\[
                         S\ge N/3,qquad t\ge N/16,qquad
                         {t\over S}\ge {1\over16}.              \tag{2.5}
\]

## 3. Transversal packetization with dense reset axes

In every retained \(Q_S\), choose a core

\[
                         J_0\subseteq J,qquad
 |J_0|=\lfloor t/2\rfloor,                              \tag{3.1}
\]

and force \(\varepsilon_j=1\) on \(J_0\). The other positions in
\(J\setminus J_0\) remain free, so the reset menu still has size

\[
                         2^{t-|J_0|}\ge2^{t/2-1}.               \tag{3.2}
\]

Partition the \(S\) abstract cube axes into \(R\) groups with sizes
differing by at most one. Since \(R=o(S)\), the axes in \(J_0\) can fill
at least

\[
 \left\lfloor{|J_0|\over\lceil S/R\rceil}\right\rfloor
                         \ge {R\over40}                         \tag{3.3}
\]

whole groups for all sufficiently large \(m\). Apply a direction-spread
perfect matching in every group and take Cartesian products of its
matching edges. This is the exact transversal \(Q_R\)-tiling. Every
packet chooses one active axis from every group, so (3.3) proves that it
has at least \(R/40\) parent-crossing active axes.

Install the certified diverse-order factor into isometric \(C_{2R}\)'s
in every packet. Assumption (0.1) gives cyclic \(H\)-safety. Every packet
has \(2^R/(2R)\) cycles, proving (0.4).

Every active axis joins an \(A_j\)-coordinate to a \(C_j\)-coordinate.
For the audit matching \(\Pi\) chosen inside the halves, none is a
\(\Pi\)-edge. Hence every selected physical transition is pair-breaking,
which proves (0.5).

An isometric packet factor uses each of its \(R\) directions on exactly
\(2^R/R\) edges. Therefore the fraction of physical transitions using a
parent-crossing axis is at least \(1/40\). At signed depth \(q\), incidence
counting alone gives at least the same \(1/40\) fraction of starts whose
window contains a reset axis. Under a complete affine compiler batch the
stronger reset-free bound is

\[
 {\binom{R-R/40}q\over\binom Rq}+2^{-\Omega(S)}
 \le e^{-q/40}+o(1).                               \tag{3.4}
\]

The last assertion is an abstract/support marginal. It is not a literal
target-quota theorem.

## 4. Exact run-neutrality and point margins

Put

\[
                 c_R={2^{R-1}\over R},qquad
                 g_R={2^R\over R}=2c_R.             \tag{4.1}
\]

One \(Q_R\)-packet factor contributes \(c_R\) deletion runs to each
endpoint of every active direction. If \(n_v\) is the number of retained
packet supports incident with coordinate \(v\), its run vector is

\[
                              r_v=c_Rn_v.                        \tag{4.2}
\]

At one mixed position, both one-factorizations in (1.4), taken across
their two channel edges, contain every one of \(a,c,a',c'\) exactly once.
Deploy the same abstract packet tiling and compiler labels on
corresponding channels. Switching \(\mathcal M_0\leftrightarrow\mathcal
M_1\) then changes no coordinate's aggregate active-axis incidence.
Tensoring proves:

### Theorem 4.1 (orbitwise run-neutral resets)

Every orbitwise reset word \(\varepsilon\) has the same owner-incidence
vector, run vector, cycle count, and signed point margins as every other
word in the matched deployment.

Indeed, if

\[
 a_v=\#\{X\in\Omega_{\rm ret}:v\in X\},                         \tag{4.3}
\]

then at every \(q\le H\) the actual trace tables satisfy exactly

\[
 \sum_{T\ni v}\mu_q^-(T)=a_v-qr_v,
 \qquad
 \sum_{U\ni v}\mu_q^+(U)=a_v+qr_v.               \tag{4.4}
\]

Thus dense physical reset choices do not disturb the exact common-run
line. The theorem does **not** assert that the common vector (4.2) is
coordinate-uniform; exact uniformization of the packet-support incidence
\((n_v)\) is a separate capacitated design problem.

For comparison, a single \(Q_{R+1}\) slab resolved along axis \(a\) has

\[
 r^{(a)}=g_R\sum_{e\in\Sigma\setminus\{a\}}\chi_e,              \tag{4.5}
\]

and changing \(a\) to \(b\) gives

\[
                         r^{(b)}-r^{(a)}=g_R(\chi_a-\chi_b).     \tag{4.6}
\]

The orbitwise two-channel construction cancels these coarse run residues
exactly.

## 5. A sharp audit of the single-slab mechanism

Let one \(Q_{R+1}\) slab replace an old active axis \(i\) by a
parent-crossing axis \(e\). It contains \(2^{R+1}\) owners. Exact
direction regularity gives

\[
 \Delta E_\Pi
 =2g_R\bigl(\mathbf1_{e\notin\Pi}-\mathbf1_{i\notin\Pi}\bigr). \tag{5.1}
\]

Consequently a disjoint slab layer of owner mass \(M\) changes the number
of pair-breaking transitions by at most

\[
                              {M\over R}.                        \tag{5.2}
\]

It cannot create linear pair-breaking mass from a pair-preserving base.
The full status-orbit atlas avoids this ceiling because a positive
fraction of every packet's axes, and in fact all axes relative to the
inside-half audit matching, are already physical breakers.

At depth \(q<R\), exactly

\[
                              2qg_R                               \tag{5.3}
\]

starts in one slab use the exchanged axis. Hence one disjoint slab layer
has exactly \(Mq/R\) genuinely parent-crossing starts. This is a raw-
incidence capacity statement, not a bound on the number of literal target
identities changed after the two packets receive new compiler contexts.

## 6. Exact remaining configuration theorem

Index the retained status orbits or slabs by \(P\). Let \(\mathcal O_P\)
be its legal whole-factor options: orbit resolution, packet support,
compiler conjugate, and the matched channel labels. Put

\[
 A_{P,o,q,\epsilon,T}
 =\mathbf1\{T\text{ occurs from option }o
                    \text{ at signed depth }(q,\epsilon)\}.     \tag{6.1}
\]

One must choose a single option \(o_P\in\mathcal O_P\) such that

\[
 \mu_{q,T}^{\epsilon}=\sum_PA_{P,o_P,q,\epsilon,T},             \tag{6.2}
\]

the run equations (4.4) hold, and

\[
 \sum_{q\le H,\epsilon}
       \operatorname{dist}_1(\mu_q^\epsilon,\mathcal B_q)=o(W), \tag{6.3}
\]

where \(\mathcal B_q\) is the exact floor/ceiling quota set of the
retained mass.

Already fractionally, separation requires for every literal all-depth,
two-sign target weight array \(\lambda\)

\[
 \sum_P\min_{o\in\mathcal O_P}
   \sum_{q,\epsilon,T}\lambda_{q,\epsilon,T}
                         A_{P,o,q,\epsilon,T}
 \le
 \sum_{q,\epsilon}h_{\mathcal B_q}(\lambda_{q,\epsilon}),       \tag{6.4}
\]

with the same option inside the minimum at every depth and sign. Integral
selection is strictly stronger.

The known transversal, affine-twirl, slab-IDP, and reset-flow theorems
prove (6.4) only for direction marginals, exterior cylinders, and coarse
Gaussian profile weights. They do not prove it for arbitrary block-
labelled literal weights. Independent or random-Latin option choices have
the usual bounded mean at Gaussian depth and leave \(\Omega_A(W)\) holes.

Therefore the expansion-rich physical reset family exists, but its
target-labelled routing theorem remains open. No Hall cut surviving the
full independent-rank status-orbit menu is proved here.

## 7. Audited boundary

Proved:

1. a near-spanning exact full status-orbit reset atlas;
2. a fixed positive density of genuinely parent-crossing axes in every
   retained packet;
3. maximal pair-breaking mass relative to an inside-half audit pairing;
4. cyclic \(H\)-safety and \(o(W/H)\) cycles;
5. an exponential run-neutral reset menu and exact common point margins;
6. the sharp \(M/R\) and \(Mq/R\) single-slab capacity formulae.

Unproved:

1. exact coordinate-uniform run incidence for the full retained owner
   set;
2. an exact \(H\)-safe completion of the exponentially small leave;
3. the arbitrary-weight configuration inequality (6.4);
4. integral option selection with (6.3); and
5. coefficient one.

The decisive advance is that sparse physical reset supply is no longer
the obstruction. The surviving problem is entirely target-labelled and
chronological.
