# Fine-strip conjugate packets: the exact multiple-choice gate and its critical-load obstruction

Date: 2026-07-26

Method: pure mathematics.  No computation, search, solver, or probabilistic
claim about the actual strip factors is used.

## 0. Outcome

Let

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
 \qquad
 H=\left\lceil\sqrt{m\log m}\right\rceil,
 \qquad h=m^{3/4+o(1)}.
\]

There is a natural way to combine several exact middle strip factors which
does not pay the middle baseline more than once.  Overlay the factors on
their common middle owners.  Each connected component has the same owner
support on every shore, so it is a **support-matched packet**.  Choosing one
shore independently in every packet always gives another exact middle strip
factor.

This note determines exactly what remains after making that reduction.

1.  For arbitrary many shores, the target problem is a multiple-choice
    exact-cover CSP.  Its fractional relaxation has the exact weighted Hall
    dual

    \[
    \boxed{
    \sum_T w_T
       \leq
    \sum_P\max_i\sum_T w_Ta_{P,i}(T)
    \quad\hbox{for every }w\geq0.}                 \tag{0.1}
    \]

    This condition is necessary and sufficient for **fractional** packet
    choices.  It is not sufficient for integral choices, already for two
    packets, two shores, and two target layers.

2.  Independent packet choices have an exact LLL formulation.  At the
    present parameters, however, the port system is at mean load one on a
    target universe of size

    \[
      |\mathcal T_H|=(\sqrt\pi+o(1))W\sqrt m.       \tag{0.2}
    \]

    Consequently, in a critically regular conjugate catalogue, an
    independent-choice proof can have expected leave \(o(W)\) only if almost
    every target is nearly **anchored** in one packet.  For a fixed number
    of shores, all but \(o(W)\) targets must in fact be completely anchored.
    A diffuse independent-conjugation argument therefore cannot prove the
    annulus theorem by LLL or alteration.

3.  For two shores there is an exact integral normal form.  If all but
    \(o(W)\) port targets have exactly two catalogue occurrences, the
    nontrivial targets form a signed multigraph on the overlay packets.
    A packet shore choice is a \(\{0,1\}\)-potential on its vertices, and a
    target is covered exactly once precisely when its signed edge equation
    is satisfied.  Thus the exact residual invariant is the signed-graph
    frustration index

    \[
      \boxed{\tau(G)=\min_x
       |\{e=PQ:x_P\oplus x_Q\ne s_e\}|.}            \tag{0.3}
    \]

    In particular, simultaneous exact port coverage is equivalent to every
    signed cycle being balanced.  Aggregate leave \(o(W)\) follows from

    \[
       \text{two-copy load imbalance }=o(W),
       \qquad \tau(G)=o(W).                         \tag{0.4}
    \]

    Conversely, modulo the same load-imbalance term and the already proved
    critical port-mass ledger, any \(o(W)\)-leave choice forces
    \(\tau(G)=o(W)\).

At the calibrated values of \(H,h\), the graph has at most
\(W/(2h)=Wm^{-3/4+o(1)}\) vertices but
\((\sqrt\pi+o(1))W\sqrt m\) target edges.  Hence almost every edge is an
independent cycle constraint: the cycle-space dimension is

\[
 (1-o(1))\sqrt\pi W\sqrt m.                         \tag{0.5}
\]

The route is therefore not closed by Hall, LLL, or the availability of
many conjugates.  It is reduced to a sharp statewise alternative:

* construct two structured, support-matched strip factors whose port-sign
  labelling is a coboundary off \(o(W)\) targets; or
* exhibit \(\Omega(W)\) edge-disjoint frustrated cycles, which refutes that
  pair immediately.

This is a useful successor gate: it identifies the deterministic Latin /
cohomological identity a successful packet construction must possess.

## 1. Overlay packets

Let \(\Omega\subseteq\binom{[2m]}m\) be a common owner set.  For
\(i\in[K]\), let \(\mathcal F_i\) partition \(\Omega\) into physical
\(2h\)-strips.  The cleanest case is \(\Omega=\binom{[2m]}m\); a common
leave of size \(o(W)\) can be appended literally and changes none of the
arguments below.

Form the \(K\)-partite incidence hypergraph whose vertices are the strips
of the \(\mathcal F_i\)'s and whose owner-hyperedge at \(X\in\Omega\)
joins the unique strips

\[
 C_i(X)\in\mathcal F_i,\qquad X\in C_i(X).          \tag{1.1}
\]

Call a connected component \(P\) of this incidence hypergraph an overlay
packet, and let \(U_P\) be its set of owner-hyperedges.

### Lemma 1.1 (support matching)

For every packet \(P\) and every shore \(i\), the strips of
\(\mathcal F_i\) in \(P\) partition exactly \(U_P\).  In particular their
number is

\[
                         b_P={|U_P|\over2h},         \tag{1.2}
\]

independent of \(i\).  Therefore choosing one shore \(i(P)\in[K]\) in
each packet produces another exact strip factor of \(\Omega\).

#### Proof

If one strip vertex lies in a component, all of its owner-hyperedges lie
there.  Conversely every owner-hyperedge in the component has its incident
strip on every shore in the component.  Since each \(\mathcal F_i\)
partitions \(\Omega\), its component strips partition \(U_P\).  Every strip
has \(2h\) owners, proving (1.2).  The sets \(U_P\) partition \(\Omega\),
so independent shore choices preserve exact middle ownership. \(\square\)

This lemma is insensitive to how the factors were obtained.  In
particular the \(\mathcal F_i\) may be coordinate conjugates of one exact
or near-exact factor.  The substantive issue is the shadow profile of the
alternative decompositions of each \(U_P\).

## 2. The port CSP

Let

\[
 \mathcal T_H=
 \bigcup_{q=1}^H
 \left(\binom{[2m]}{m-q}\mathbin{\dot\cup}
       \binom{[2m]}{m+q}\right)                    \tag{2.1}
\]

be the signed nonmiddle target universe.  Fix any integral port system of
the fine-strip port theorem.  For a packet \(P\), shore \(i\), and target
\(T\), put

\[
 a_{P,i}(T)=
 \#\{C\in\mathcal F_i\cap P:(C,T)\text{ is a selected port incidence}\}.
                                                               \tag{2.2}
\]

A packet choice \(x_P\in[K]\) produces certified load

\[
                         L_x(T)=\sum_Pa_{P,x_P}(T). \tag{2.3}
\]

Thus the literal integral problem is the multiple-choice CSP

\[
                         L_x(T)\geq1
                 \quad(T\in\mathcal T_H),          \tag{2.4}
\]

or its aggregate-leave version.  Whole strips, not incidences, are being
chosen in (2.3).

### Theorem 2.1 (exact fractional Hall dual)

There are fractional packet choices

\[
 x_{P,i}\geq0,\qquad \sum_i x_{P,i}=1,             \tag{2.5}
\]

with

\[
 \sum_{P,i}a_{P,i}(T)x_{P,i}\geq1
 \quad(T\in\mathcal T_H)                            \tag{2.6}
\]

if and only if (0.1) holds for every nonnegative target weight vector
\(w\).

#### Proof

The set of achievable fractional load vectors is the Minkowski sum

\[
 \mathcal L=sum_P
 \operatorname{conv}\{a_{P,i}:i\in[K]\}.           \tag{2.7}
\]

Condition (2.6) asks whether \(\mathcal L\) intersects
\(\mathbf1+\mathbb R_{geq0}^{\mathcal T_H}\).  If it does, maximizing a
nonnegative functional \(w\) over \(\mathcal L\) gives (0.1).  If it does
not, separation from the upward orthant supplies a separating functional
with \(w\geq0\), and its maximum over (2.7) is the right side of (0.1),
which is then strictly smaller than \(\sum_Tw_T\). \(\square\)

Equivalently, the maximum fractional coverage LP has dual value

\[
 |\mathcal T_H|-
 \max_{0\leq w\leq1}
 \left[
   \sum_Tw_T-sum_P\max_i\sum_Tw_Ta_{P,i}(T)
 \right].                                          \tag{2.8}
\]

The upper bound \(w\leq1\) is the dual of capping the covered amount of
one target at one.

### Proposition 2.2 (Hall is not integral, already in two layers)

There are two packets, two alternatives per packet, and four targets for
which (2.5)--(2.6) is feasible with equality at every target, but no
integral packet choice covers all four targets.

#### Proof

Write the targets as \(t_1,t_2,u_1,u_2\), with the \(t\)'s and \(u\)'s
regarded as two different ranks.  Give the two alternatives of \(P\) the
sets

\[
 P_0=\{t_1,u_1\},\qquad P_1=\{t_2,u_2\},            \tag{2.9}
\]

and those of \(Q\) the sets

\[
 Q_0=\{t_1,u_2\},\qquad Q_1=\{t_2,u_1\}.            \tag{2.10}
\]

Weighting every alternative by \(1/2\) gives every target fractional load
one.  The four integral choices miss respectively \(t_2,u_2,u_1,t_1\).
Thus even two rankwise-perfect Hall systems can be jointly inconsistent.
\(\square\)

This is the smallest parity obstruction.  It rules out any claim that
rankwise Hall, the fractional orbit average, or total unimodularity of the
individual port-thinning graphs rounds the packet choices.

It also amplifies at exactly the fine-strip scale.

### Corollary 2.3 (parameter-matched abstract obstruction)

Let \(p\) be even and pair \(p\) binary packets.  On every packet pair put
\(s\) disjoint clones of each of the four targets in (2.9)--(2.10).  Then

1. the target count and the selected occurrence mass are both
   \(2sp\);
2. every alternative has exactly \(2s\) target incidences;
3. uniform fractional packet choices give every target load exactly one;
   but
4. every integral packet choice misses exactly \(sp/2\), one quarter of
   all targets.

Taking

\[
 p\asymp {W\over2h},
 \qquad s\asymp \sqrt\pi h\sqrt m                 \tag{2.11}
\]

gives

\[
 2sp\asymp\sqrt\pi W\sqrt m,
 \qquad 2s\asymp2\sqrt\pi h\sqrt m,               \tag{2.12}
\]

which are respectively the actual annulus target mass and the actual
average port width per selected strip at the calibrated parameters.

#### Proof

The assertions add over the disjoint packet pairs.  On one pair, every
choice misses one of the four target types and duplicates another.  With
\(s\) clones this gives \(s\) holes out of \(4s\) targets.  Equations
(2.11)--(2.12) are substitution. \(\square\)

This corollary is an abstract packet system, not a claim that the gadget is
realized by physical strips.  Its role is sharp: degree normalization,
critical total mass, correct packet count, correct port width, and exact
fractional Hall all coexist with a linear (indeed \(\Theta(W\sqrt m)\))
integral defect.  A positive annulus theorem must use a physical
chronology/cocycle identity that excludes this gadget.

## 3. The exact LLL criterion and the anchoring requirement

Choose shores independently, using arbitrary distributions
\(\xi_{P,i}\) on \([K]\).  Put

\[
 p_{P,T}=\sum_{i:a_{P,i}(T)>0}\xi_{P,i},             \tag{3.1}
\]

the probability that packet \(P\) covers \(T\).  The bad event that
\(T\) is missed has exact probability

\[
 \Pr(B_T)=\prod_P(1-p_{P,T}).                       \tag{3.2}
\]

Let \(\Gamma(T)\) consist of targets \(T'\ne T\) for which some packet
has both \(p_{P,T}>0\) and \(p_{P,T'}>0\).

### Theorem 3.1 (packet LLL)

If there are numbers \(z_T\in(0,1)\) such that

\[
 \prod_P(1-p_{P,T})
 \leq z_T\prod_{T'\in\Gamma(T)}(1-z_{T'})
 \quad(T\in\mathcal T_H),                          \tag{3.3}
\]

then some integral packet choice covers every target.  For aggregate
leave one does not need LLL: there is a choice leaving at most

\[
                         \sum_T\prod_P(1-p_{P,T})  \tag{3.4}
\]

targets.

#### Proof

The events \(B_T\) are functions of independent packet variables and the
displayed graph is a dependency graph.  Equation (3.3) is the asymmetric
Lovasz local lemma.  Equation (3.4) follows by expectation. \(\square\)

The relevant obstruction is already visible in (3.4).

### Lemma 3.2 (critical-load anchoring bound)

Put

\[
 \lambda_T=\sum_Pp_{P,T},\qquad
 \alpha_T=\max_Pp_{P,T}.
\]

If \(\alpha_T<1\), then

\[
 \boxed{
 \Pr(B_T)\geq
 \exp\left(-{\lambda_T\over1-\alpha_T}\right).}   \tag{3.5}
\]

#### Proof

For \(0\leq u\leq\alpha_T<1\),

\[
 \log(1-u)\geq-{u\over1-u}\geq-{u\over1-\alpha_T}.
\]

Sum this inequality over the packets and exponentiate. \(\square\)

Suppose now that the catalogue is critically regular at \(T\): under
uniform shore choices, \(\lambda_T=1+o(1)\).  If

\[
 \alpha_T\leq1-{2+o(1)\over\log m},                 \tag{3.6}
\]

then (3.5) is at least \(m^{-1/2+o(1)}\).  Since the band has
\(\Theta(W\sqrt m)\) targets, a positive fraction of targets satisfying
(3.6) already contributes \(\Omega(W)\) expected holes.  To make (3.4)
\(o(W)\), almost every target must therefore put
\(1-O(1/\log m)\) of its coverage probability inside one packet.

There is a sharper discrete statement for a fixed number of shores.

### Corollary 3.3 (fixed-shore no-alteration theorem)

Assume uniform choices from \(K\) alternatives, every target has exactly
\(K\) simple catalogue occurrences, and hence \(\lambda_T=1\).  If \(T\)
is not anchored (its \(K\) occurrences are not all alternatives of one
packet), then

\[
                         \Pr(B_T)\geq{K-1\over K^2}.             \tag{3.7}
\]

Consequently an independent-choice/alteration proof with fixed \(K\) can
have expected aggregate leave \(o(W)\) only if all but \(o(W)\) targets
are anchored.

#### Proof

Each nonzero \(p_{P,T}\) is a multiple of \(1/K\), their sum is one, and
no one equals one.  Under those constraints the product
\(\prod_P(1-p_{P,T})\) is minimized by

\[
 p_1={K-1\over K},\qquad p_2={1\over K},
\]

which gives (3.7). \(\square\)

Thus adding a bounded number of generic conjugates does not create an LLL
route.  The copies of almost every target would have to coalesce into one
overlay packet.  Diffuse copies reproduce the critical Poisson loss.

There is an equally explicit obstruction to applying a black-box
independent-transversal theorem.  Let \(S_v\) be the simple port set of an
alternative vertex \(v=(P,i)\), put

\[
 r_{P,T}=|\{i:T\in S_{P,i}\}|,
 \qquad r_T=\sum_Pr_{P,T}.                           \tag{3.8}
\]

Then the exact ordered external-conflict mass is

\[
 \boxed{
 \sum_v\sum_{w:\,P(w)\ne P(v)}|S_v\cap S_w|
 =\sum_T\left(r_T^2-\sum_Pr_{P,T}^2\right).}        \tag{3.9}
\]

In particular, if \(r_T=K\) and
\(\max_Pr_{P,T}\le(1-\delta)K\) on a target set \(\mathcal U\), the
right side of (3.9) is at least

\[
                         \delta K^2|\mathcal U|.    \tag{3.10}
\]

If every two alternatives from distinct packets share at most \(\zeta\)
ports, the conflict graph consequently has maximum degree at least its
average degree, hence

\[
 \Delta_{\rm conf}\ge
 {\delta K|\mathcal U|\over \zeta|\mathcal P|}.     \tag{3.11}
\]

For \(|\mathcal U|\asymp|\mathcal T_H|\) this is
\(\Omega(\delta K h\sqrt m/\zeta)\).  Thus a condition such as
\(K\ge2\Delta_{\rm conf}\) can hold in the diffuse regime only when the
pair codegree \(\zeta\) is itself a positive fraction of the entire
\(\Theta(h\sqrt m)\) alternative width.  Low codegree, which helps an
ordinary nibble, makes this particular independent-transversal criterion
worse rather than better.  Equation (3.9), unlike that conclusion, is an
exact identity; it permits an anchored catalogue because anchored copies
make the external-conflict summand zero.

## 4. Two shores: exact signed-graph normal form

Take \(K=2\), label the shores by \(0,1\), and write the selected shore of
packet \(P\) as \(x_P\in\mathbb F_2\).  Count catalogue **occurrences**,

\[
                         r_T=\sum_{P,i}a_{P,i}(T).  \tag{4.1}
\]

Let \(\mathcal T^{(2)}=\{T:r_T=2\}\).  For
\(T\in\mathcal T^{(2)}\), record its two occurrence literals

\[
                         (P,a),\qquad(Q,b).         \tag{4.2}
\]

Parallel edges and loops are allowed.  Make a signed edge \(e_T=PQ\) with
label

\[
                         s_T=1\oplus a\oplus b.     \tag{4.3}
\]

### Theorem 4.1 (XOR packet theorem)

For every \(T\in\mathcal T^{(2)}\), the selected port load is exactly one
if and only if

\[
                         x_P\oplus x_Q=s_T.         \tag{4.4}
\]

Consequently all two-occurrence targets are covered exactly once if and
only if the signed multigraph is balanced: the XOR of the labels around
every cycle is zero.  Equivalently, it has no label-one loop and no
frustrated cycle.

#### Proof

The occurrence \((P,a)\) is selected precisely when \(x_P=a\).  As an
\(\mathbb F_2\)-valued truth indicator this is

\[
                         1\oplus x_P\oplus a.
\]

Exactly one of the two literals is true precisely when their XOR is one,
which rearranges to (4.4).  A system of equations
\(x_P\oplus x_Q=s_{PQ}\) is solvable precisely when the labels sum to zero
around every cycle: necessity follows by telescoping, and sufficiency by
fixing one root value in every component and integrating the labels along
a spanning tree. \(\square\)

The loop cases are informative.  Opposite-shore occurrences \((P,0)),
\((P,1)\) give a label-zero loop and cover \(T\) for either packet choice.
Two same-shore occurrences in one packet give a label-one loop and make
exact coverage impossible.

Define the frustration index

\[
 \tau(G)=\min_{x\in\mathbb F_2^{V(G)}}
       |\{T\in\mathcal T^{(2)}:
              x_P\oplus x_Q\ne s_T\}|.             \tag{4.5}
\]

It is also the minimum number of signed edges whose deletion makes the
graph balanced.

### Theorem 4.2 (near-cover criterion for a conjugate pair)

Put

\[
                         \mathfrak B_2
       =\sum_{T\in\mathcal T_H}|r_T-2|.             \tag{4.6}
\]

If

\[
                         \mathfrak B_2+\tau(G)=o(W),             \tag{4.7}
\]

then a packet shore choice gives aggregate certified nonmiddle leave
\(o(W)\).  Hence, with \(H/h=o(1)\), the chosen whole strips and literal
repair give a word of length \(W+o(W)\) for the central band.

Conversely, suppose \(\mathfrak B_2=o(W)\) and the aggregate chosen port
mass differs from \(|\mathcal T_H|\) by \(o(W)\), as it does for the
calibrated integral port system below.  If some packet choice has
aggregate leave \(o(W)\), then \(\tau(G)=o(W)\).

#### Proof

At most \(\mathfrak B_2\) targets lie outside \(\mathcal T^{(2)}\).  Choose
\(x\) attaining (4.5).  Every satisfied edge has selected load exactly
one by Theorem 4.1.  Thus only the exceptional targets and the
\(\tau(G)\) violated edges can be holes, proving the first assertion.

For the converse, a violated regular edge has load zero or two.  Hence the
number of violated edges is at most the number of regular holes plus the
number of regular overload targets.  The identity

\[
 \sum_T(L_x(T)-1)
 =\sum_T(L_x(T)-1)_+-|\{T:L_x(T)=0\}|              \tag{4.8}
\]

and the assumed \(o(W)\) total-mass error show that \(o(W)\) holes imply
\(o(W)\) overload.  Removing the \(o(W)\) exceptional targets gives
\(\tau(G)=o(W)\). \(\square\)

This is an exact statewise theorem, not a random-sign heuristic.  A family
of \(\Omega(W)\) edge-disjoint frustrated cycles is an immediate
certificate that the proposed conjugate pair cannot work.

## 5. Calibration at the annulus parameters

For \(q=o(m^{2/3})\), uniformly in the present range,

\[
 {N_q\over W}=\exp\left(-{q^2\over m}+o(1)\right). \tag{5.1}
\]

Therefore

\[
 \begin{aligned}
 |\mathcal T_H|
 &=2\sum_{q=1}^HN_q\\
 &=(\sqrt\pi+o(1))W\sqrt m,                       \tag{5.2}
 \end{aligned}
\]

because \(H/\sqrt m=\sqrt{\log m}+o(1)\).

An exact factor contains

\[
                         B={W\over2h}               \tag{5.3}
\]

strips, up to an \(o(W)\) divisibility leave.  Every overlay packet contains
at least one strip on every shore, so

\[
                         |\mathcal P|\leq B
       ={W\over2m^{3/4+o(1)}}.                     \tag{5.4}
\]

The integral port theorem gives one strip, at signed depth \(q\), either
floor or ceiling of

\[
                         2h{N_q\over N_1}           \tag{5.5}
\]

ports.  Hence every packet selection of \(B\) strips has signed-depth
port mass within \(B\) of

\[
 B\,2h{N_q\over N_1}=W{N_q\over N_1}.              \tag{5.6}
\]

Since \(N_1=Wm/(m+1)\), summing over signs and depths gives

\[
 \begin{aligned}
 \left|\sum_TL_x(T)-|\mathcal T_H|\right|
 &\leq
 2\sum_{q=1}^H{N_q\over m}+2HB\\
 &=O(W/\sqrt m)+O(HW/h)=o(W).                      \tag{5.7}
 \end{aligned}
\]

This proves the critical-mass hypothesis used in the converse part of
Theorem 4.2, uniformly for every packet choice.  It also shows why ordinary
random coverage is the wrong scale: the system has only
\(|\mathcal T_H|+o(W)\) selected occurrences for
\(|\mathcal T_H|\) targets.

If the pair-balance hypothesis \(\mathfrak B_2=o(W)\) holds, the signed
graph has

\[
 E=(\sqrt\pi+o(1))W\sqrt m                         \tag{5.8}
\]

edges and at most \(B\) vertices.  Its cycle-space dimension is at least

\[
 \begin{aligned}
 E-B
 &=(\sqrt\pi+o(1))W\sqrt m,                       \tag{5.9}
 \end{aligned}
\]

because \(B/E=\Theta((h\sqrt m)^{-1})=m^{-5/4+o(1)}\).
Thus (4.7) asks for the edge signs to agree with one vertex potential off
only \(o(W)\) of \(\Theta(W\sqrt m)\) edges, a relative error
\(o(m^{-1/2})\).

For calibration only, if the signs on a fixed graph were independent fair
bits, a union bound over the at most \(2^B\) vertex potentials and a
Chernoff bound would give

\[
                         \tau(G)=(1/2-o(1))E
                         \quad\text{with high probability}.   \tag{5.10}
\]

Equation (5.10) is **not** asserted for coordinate conjugates; their signs
are highly structured.  It records the strength of the required identity:
random signs miss (4.7) by a factor \(\Theta(\sqrt m)\).

The average number of certified ports per selected strip across the full
band is

\[
 { |\mathcal T_H|+o(W)\over B}
 =(2\sqrt\pi+o(1))h\sqrt m
 =m^{5/4+o(1)}.                                    \tag{5.11}

Consequently a black-box independent-transversal theorem based on part
size versus maximum conflict degree is also in the wrong regime.  The
large port width is not merely an artefact of the earlier hypergraph
formulation; it reappears as the dense signed constraint graph.

## 6. What is positive and what remains open

### Proved here

1. support-matched overlay packets from any number of exact strip factors;
2. exact preservation of middle ownership under one shore choice per
   packet;
3. the exact fractional weighted Hall criterion (0.1);
4. a two-layer determinant/parity counterexample to integral Hall;
5. the exact product-choice LLL condition and the critical anchoring lower
   bound;
6. the exact signed-graph/XOR normal form for two pair-balanced shores;
7. the necessary and sufficient near-cover statistic
   \(\mathfrak B_2+\tau(G)\), modulo the proved critical mass ledger; and
8. the full \(H=\sqrt{m\log m}\), \(h=m^{3/4+o(1)}\) parameter audit.

### Not proved

No known pair of conjugate strip factors is shown to satisfy

\[
                         \mathfrak B_2+\tau(G)=o(W).             \tag{6.1}
\]

The overlay construction, fractional Hall condition, and LLL do not imply
(6.1).  At the calibrated scale they expose why: almost every one of
\(\Theta(W\sqrt m)\) target constraints must be discharged by the same
packet potential identity.

### Exact next experiment/theorem

For a structured conjugate pair \((\mathcal F,g\mathcal F)\), compute or
prove bounds for

\[
 \mathfrak B_2(g)
   =\sum_T|r_T(g)-2|,
 \qquad
 \tau(G_g).                                         \tag{6.2}
\]

There are only two decisive outcomes.

* A proof of (6.1), together with the already proved port compiler, closes
  the fine-strip annulus gate and hence coefficient one.
* A packing of \(\Omega(W)\) edge-disjoint frustrated cycles gives a
  statewise obstruction to that conjugate pair and cannot be repaired by
  fractional averaging or LLL.

For \(K>2\), the corresponding exact object is the exact-one CSP

\[
 \sum_{(P,i)\text{ occurrence of }T}\mathbf1[x_P=i]=1.          \tag{6.3}
\]

The binary signed graph is the only case in which (6.3) collapses to a
linear cycle-sum criterion.  More shores do not by themselves create a
rounding theorem; they create a higher-alphabet Latin constraint system.
