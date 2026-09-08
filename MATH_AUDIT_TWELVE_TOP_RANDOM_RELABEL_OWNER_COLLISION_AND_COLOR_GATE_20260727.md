# Audit of the twelve-top random-relabel owner collision and colour gate

Date: 2026-07-27

Audited file:
MATH_THEOREM_TWELVE_TOP_RANDOM_RELABEL_OWNER_COLLISION_AND_COLOR_GATE_20260727.md.

Method: pure mathematics only. No computation, search, solver, web input,
or reliance on another audit is used.

## 0. Corrected verdict

Write

\[
 n=2m,\quad M=m+H,\quad d=m-3H+1,\quad
 N=\binom{2m}{M},\quad W=\binom{2m}{m},\quad
 \lambda=\frac WN.
\]

The following parts of the audited report are correct as written:

1. the \(12H\) one-outside and \(12(d-H)\) two-outside census;
2. the exact legal core-relabel marginal \(p_P(X)\);
3. the packet second moment \(\sigma\);
4. the exact pair-collision and repeat-excess identities;
5. the universal annealed lower bounds
   \[
   \mathbb E\operatorname{Pair}\ge(1/2-o(1))W,\qquad
   \mathbb E\operatorname{Excess}\ge(e^{-1}-o(1))W;
   \]
6. the pooled one-layer load bound \(\alpha\), including the exact
   constant-three slack;
7. the Poisson-binomial positive-part estimate; and
8. the existence of a pooled realization with maximum owner degree at
   most \(L\), after a quantitatively negligible deletion.

The current patched report is substantively correct. No material
correction remains.

### Essential scope boundary

The newly added McDiarmid estimate proves

\[
 \Pr\!\left(\operatorname{Excess}<(e^{-1}-\varepsilon)W\right)
 \le \exp[-\Omega_\varepsilon(W/m)].                       \tag{0.1}
\]

Thus independent packetwise relabeling fails with overwhelmingly high
probability, not merely in expectation. It still does not prove that
the minimum over all deterministic legal relabel choices is linear:
an exponentially rare good choice is not excluded. The current primary
file now states this distinction correctly.

Earlier issues have already been corrected in the primary report:
the pooled deletion now retains the sharp
\(Wm^{-4+o(1)}\)-packet and \(Wm^{-3+o(1)}\)-owner-loss rates, and the
invalid packet-pair probability equality has been replaced by the exact
packet-star clique argument. The displayed syntax of (6.3) is also now
correct.

The pooled capacity theorem is valid and the surviving deterministic
gate is a packet-respecting near-\(L\)-edge-colouring plus
source-compatible chronology.

## 1. Audit of the exact packet marginal

Let \(P=(C,S,E)\), where

\[
 |C|=M-2,\qquad |S|=6,\qquad
 E=\binom S2\setminus J.
\]

Put

\[
 B_1=\binom{M-2}{m-1},\qquad B_2=\binom{M-2}{m-2}.
\]

On one repaired shore, every row has exactly \(H\) owners retaining one
outside label. In an unrotated row these are one pure context and
\(H-1\) mixed contexts; in a rotated row they are \(H\) mixed contexts.
The other \(d-H\) owners retain both outside labels.

At an outside label \(x\), the unrotated carrier contributes
\(1+(H-1)=H\) one-outside owners retaining \(x\), and the rotated carrier
contributes \(H\). Thus each \(x\in S\) occurs in exactly \(2H\) such
owners. Summing over \(x\) gives \(12H\); summing the two-outside owners
over the twelve carrier edges gives \(12(d-H)\).

Fix \(X=A\cup\{x\}\), where \(A\in\binom C{m-1}\). The \(2H\) core
role-subsets attached to \(x\) are distinct: equality of two would give
two equal owners inside one squarefree shore. Under a uniform
permutation of \(C\), each is uniform in \(\binom C{m-1}\), and two
distinct role-subsets cannot have the same image under one permutation.
Consequently the \(2H\) events are disjoint and

\[
 \Pr(X\in\mathcal O(P))=\frac{2H}{B_1}.                   \tag{1.1}
\]

Similarly, for \(X=A\cup e\), \(e\in E\), the \(d-H\) relevant core
role-subsets are distinct and

\[
 \Pr(X\in\mathcal O(P))=\frac{d-H}{B_2}.                  \tag{1.2}
\]

All other owners have probability zero. Hence the audited formula

\[
 p_P(X)=
 \frac{2H}{B_1}1_{\mathcal A_1(P)}(X)
 +
 \frac{d-H}{B_2}1_{\mathcal A_2(P)}(X)                    \tag{1.3}
\]

is exact, not merely an expected-occurrence formula.

Since \(|\mathcal A_1(P)|=6B_1\) and
\(|\mathcal A_2(P)|=12B_2\),

\[
 \sum_Xp_P(X)=12d
\]

and

\[
 \sum_Xp_P(X)^2
 =\frac{24H^2}{B_1}+\frac{12(d-H)^2}{B_2}.                \tag{1.4}
\]

Thus Sections 1--2 pass without correction.

### Audit of the explicit \(K_{ij}\) coefficient

For \(i,j\in\{1,2\}\), put
\[
 \mathcal E_1(P)=\binom{S_P}{1},\qquad
 \mathcal E_2(P)=\binom{S_P}{2}\setminus J_P,
\]
and similarly for \(Q\). Fix traces
\(T\in\mathcal E_i(P)\), \(U\in\mathcal E_j(Q)\).

An owner \(X\) with
\[
 X\cap S_P=T,\qquad X\cap S_Q=U
\]
exists in both potential families precisely when
\[
 T\cap S_Q=U\cap S_P,\qquad
 T\setminus U\subseteq C_Q,\qquad
 U\setminus T\subseteq C_P.                              \tag{1.5}
\]
Indeed, the first equality is forced on \(S_P\cap S_Q\). Every element
of \(T\setminus U\) must be supplied by the \(Q\)-core, and every
element of \(U\setminus T\) by the \(P\)-core. After these forced
elements, all remaining elements of \(X\) must lie in
\(C_P\cap C_Q\). Conversely these conditions construct both
representations.

Since \(T\cup U\) is disjoint from \(C_P\cap C_Q\), the number of
completions is
\[
 \binom{|C_P\cap C_Q|}{m-|T\cup U|}.
\]
The traces of an owner are unique, so summing over \(T,U\) causes no
double count. Thus (3.3a)--(3.3b) of the primary report are exact.

## 2. Audit of the one-layer collision identities

For independently relabelled packets let

\[
 Z_X=\sum_PI_P(X),\qquad
 \Lambda_X=\sum_Pp_P(X).
\]

Packetwise independence gives

\[
 \mathbb E\sum_X\binom{Z_X}{2}
 =\frac12\sum_X\left(\Lambda_X^2-\sum_Pp_P(X)^2\right),    \tag{2.1}
\]

and the identity
\[
 (r-1)_+=r-1_{\{r\ge1\}}
\]
gives

\[
 \mathbb E\sum_X(Z_X-1)_+
 =\sum_X\left(\Lambda_X-1+\prod_P(1-p_P(X))\right).        \tag{2.2}
\]

These formulas and the \(K_{ij}(P,Q)\) expansion are correct.

Let \(R=\sum_X\Lambda_X=d(N-\ell)=(1-o(1))W\). By
Cauchy--Schwarz,

\[
 \sum_X\Lambda_X^2\ge\frac{R^2}{W}.                       \tag{2.3}
\]

Moreover

\[
 \sigma=\frac{24H^2}{B_1}+\frac{12(d-H)^2}{B_2}=o(1),
\]
because \(B_1\ge\binom m2\), \(B_2\ge\binom m3\), and
\(H=o(m)\). Therefore \(K\sigma=o(W)\), and (2.1) yields the
audited \((1/2-o(1))W\) lower bound.

The maximum one-owner probability is indeed

\[
 u=\frac{2H}{B_1},
\]
because

\[
 \frac{(2H/B_1)}{((d-H)/B_2)}
   =\frac{2(m-1)}{d-H}>1.                                 \tag{2.4}
\]

Using
\[
 \log(1-p)\ge-\frac p{1-u}
\]
and Jensen for the convex function
\[
 x\mapsto x-1+e^{-x/(1-u)}
\]
proves the \((e^{-1}-o(1))W\) expected-excess bound.

The added McDiarmid estimate is also correct. The excess can be written
as
\[
 \operatorname{Excess}=R-|\{X:Z_X>0\}|,
\]
where \(R\) is fixed. Replacing one packet deck by another changes the
union support by at most \(2(12d)\), so this is a valid bounded
difference constant. There are
\[
 K=(1-o(1))N/12=\Theta(W/m)
\]
independent packet variables. For fixed \(\varepsilon>0\), the
expectation lower bound places
\((e^{-1}-\varepsilon)W\) a distance \(\Theta_\varepsilon(W)\) below
the mean. Hence
\[
 \Pr\!\left(
 \operatorname{Excess}<(e^{-1}-\varepsilon)W
 \right)
 \le
 \exp\left[
 -\Omega_\varepsilon\!\left(
 \frac{W^2}{K(24d)^2}
 \right)\right]
 =\exp[-\Omega_\varepsilon(W/m)].                         \tag{2.5}
\]
Thus product-random relabeling has linear excess with overwhelmingly
high probability. This still does not lower-bound the deterministic
minimum over all legal choices.

## 3. Audit of the pooled coefficient \(\alpha\)

Fix an owner \(X\), and let \(T=\binom mH\) be the number of tops
containing it. In one top-disjoint layer, let \(a_X\) and \(b_X\) count
packets for which \(X\) lies in the one-outside and two-outside
potential families.

If \(X\in\mathcal A_1(P)\), its unique outside label has degree four in
\(K_6-J\), so exactly four packet tops contain \(X\). If
\(X\in\mathcal A_2(P)\), exactly one packet top contains it. Hence

\[
                         4a_X+b_X\le T.                   \tag{3.1}
\]

Also

\[
 \frac{(2H/B_1)/4}{(d-H)/B_2}
   =\frac{m-1}{2(d-H)}\le1,                               \tag{3.2}
\]

using \(d-H=m-4H+1\ge(m-1)/2\). Maximizing the linear load under
(3.1) therefore gives

\[
 \Lambda_X\le\alpha:=\frac{(d-H)T}{B_2}.                  \tag{3.3}
\]

The exact ratio

\[
 \frac{B_2}{T}
 =\lambda\frac{m(m-1)}{(m+H)(m+H-1)}
\]
gives

\[
 \alpha=
 \frac{(d-H)(m+H)(m+H-1)}{m(m-1)\lambda}.                 \tag{3.4}
\]

Under \(\lambda\ge M=m+H\),

\[
 1-\alpha\ge
 \frac{3mH+4H^2-m-5H+1}{m(m-1)}
 =\left(3+o(1)\right)\frac Hm.                            \tag{3.5}
\]

Thus the exact slack constant three is correct.

### Audit of the carrier-respecting bulk Hall theorem

For a covered top \(U=C\cup e_U\), the number of two-outside candidate
owners is
\[
 A_2=\binom{M-2}{m-2}.
\]
A fixed owner belongs to at most
\[
 B=\binom mH
\]
such top neighbourhoods, because \(B\) is already the total number of
rank-\(M\) tops containing that owner. Therefore every top set
\(\mathcal A\) has
\[
 |\Gamma(\mathcal A)|\ge\frac{A_2}{B}|\mathcal A|.         \tag{3.6}
\]

The exact ratio is
\[
 \frac{A_2}{B}
 =\lambda\frac{m(m-1)}{M(M-1)}
 \ge\frac{m(m-1)}{M-1},                                  \tag{3.7}
\]
using \(\lambda\ge M\). Moreover
\[
 m(m-1)-(m-4H+1)(m+H-1)
 =3mH+4H^2-m-5H+1>0.                                    \tag{3.8}
\]
Hence
\[
 \frac{A_2}{B}\ge d-H.
\]
Cloning every top \(d-H\) times now satisfies Hall exactly. The selected
owners contain the designated carrier pair \(e_U\), so they lie in the
correct two-outside potential family, not merely in the unrestricted
containment graph.

Finally
\[
 (d-H)(N-o(N))=W-o(W)
\]
under the calibrated relation \(\lambda=M+O(H)\), and the omitted
one-outside mass is \(HN=o(W)\). The theorem is therefore correct and
strictly stronger than unrestricted unbundled Hall. It remains
unbundled because the assigned \(H\)-complements need not be consecutive
windows of one common repaired word.

## 4. Audit of the positive-part Chernoff estimate

Pool \(L=(1+o(1))m\) layers. For each \(X\), the pooled load \(D_X\)
is Poisson-binomial with

\[
 \mu_X\le L\alpha,\qquad L-\mu_X\ge(3-o(1))H.              \tag{4.1}
\]

For \(0<\mu<L\), take \(\theta=\log(L/\mu)\). Since for every integer
\(r\ge1\),

\[
 r\le\frac{e^{\theta r}}{e^\theta-1},
\]

the standard Bernoulli exponential moment bound gives

\[
 \mathbb E(D-L)_+
 \le\frac{L}{L-\mu}
 \exp\left(-\frac{(L-\mu)^2}{2L}\right).                  \tag{4.2}
\]

The case \(\mu=0\) is trivial and should be mentioned separately.

The expansion

\[
 \log\lambda
 =\frac{H^2}{m}
 +O\left(\frac{H^2}{m^2}+\frac{H^4}{m^3}\right)
\]
is correct in the stated range. Since
\(\lambda=M+O(H)=(1+o(1))m\), it implies
\[
 H^2/m=(1+o(1))\log m.
\]

Equations (4.1)--(4.2) then yield

\[
 \mathbb E(D_X-L)_+
 \le\frac{m}{(3-o(1))H}
       \exp\left[-\left(\frac92-o(1)\right)\frac{H^2}{m}\right]
 =m^{-4+o(1)}.                                            \tag{4.3}
\]

Summing (4.3) gives total expected overload at most
\(Wm^{-4+o(1)}\). Choose a realization whose total overload is at most
the expectation. Repeatedly delete a packet through an overloaded
owner. Every deletion lowers total overload by at least one and cannot
raise any other load. Therefore at most \(Wm^{-4+o(1)}\) deletions
suffice. Since each packet has \(12d=O(m)\) owner incidences, the lost
owner incidence mass is at most \(Wm^{-3+o(1)}=o(W)\).

Thus Section 5 is mathematically sound after its deletion conclusion is
stated at the proved quantitative scale.

## 5. Audit of the LLL, full-orbit degree ratio, and chronology

### 5.1 Packet-star clique

For one near-perfect layer define the atomic owner event
\[
 A_{P,Q,X}=\{X\in\mathcal O(P)\cap\mathcal O(Q)\}.
\]
Its probability is \(p_P(X)p_Q(X)\). All events involving one packet
\(P\) form a clique in the standard packet-variable dependency graph.
With
\[
 S_P=\sum_{Q\ne P}\sum_Xp_P(X)p_Q(X),
\]
one has
\[
 \sum_PS_P=2\mathbb E\operatorname{Pair}\ge(1-o(1))W.     \tag{5.1}
\]
There are \((1-o(1))N/12\) packets, so
\[
 \frac1K\sum_PS_P\ge(12-o(1))\frac WN=\Theta(m).           \tag{5.2}
\]

For a clique \(\mathcal C\), standard asymmetric-LLL witnesses would
give
\[
 \sum_{A\in\mathcal C}\Pr(A)
 \le\sum_{A\in\mathcal C}
 x_A\prod_{B\in\mathcal C\setminus\{A\}}(1-x_B)\le1.      \tag{5.3}
\]
Thus (5.1) proves that some packet-star clique violates the criterion
by a factor \(\Theta(m)\). The primary argument is correct after the
displayed syntax of its (6.3) is repaired.

This conclusion is scoped to the ordinary variable-dependency graph.
Events sharing a packet variable may admit a specialized lopsided
relation, and merging owner events when two packets share several owners
changes the event system.

There is also a deterministic post-thinning analogue. If \(D_X\le L\)
are the owner degrees after Section 5 and \(I=(1-o(1))LW\) is total
owner incidence mass, then
\[
 \sum_X\binom{D_X}{2}
 \ge W\binom{I/W}{2}
 =\left(\frac12-o(1)\right)WL^2.                          \tag{5.4}
\]
Under independent uniform \(L\)-colouring, the average atomic
owner-event probability sum at a packet star is
\[
 (1-o(1))\,12d=\Theta(m).
\]
Again, this statement concerns owner-labelled atomic events; duplicate
logical colour events must be merged before it can analyze a different
lopsidependency formulation.

### 5.2 Full-orbit degree ratio

Let \(E\) be the number of columns in the complete role-labelled orbit,
and let \(D_T,D_X\) be its top and owner degrees. Full ambient symmetry
is transitive on both resource classes. Every column contains twelve
tops and \(12d\) owners, so incidence counting gives
\[
 ND_T=12E,\qquad WD_X=12dE,
\qquad \frac{D_X}{D_T}=\frac{dN}{W}=1-o(1)<1.             \tag{5.5}
\]
This is exact.

If a proper \((1+o(1))D_T\)-edge-colouring existed, each colour class
would have at most \(N/12\) edges by top-disjointness, while the average
class size would be
\[
 \frac{E}{(1+o(1))D_T}=(1-o(1))\frac N{12}.
\]
Hence all but \(o(D_T)\) classes would have size
\((1-o(1))N/12\), and properness on the full resource hypergraph would
make them owner-disjoint as well. This implication is correct; the
edge-colouring existence remains unproved because the resource rank is
\(\Theta(m)\).

### 5.3 Chronological owner conservation

Every repaired twelve-top move has literally equal old and new
middle-owner incidence vectors. Therefore, for any simultaneously
applicable collection of source shores,
\[
 \mu_{t+1}-\mu_t
 =\sum_P\left(
 1_{\mathcal O(P,\mathrm{new})}
 -1_{\mathcal O(P,\mathrm{old})}
 \right)=0.                                               \tag{5.6}
\]
Thus a squarefree owner vector stays squarefree through any genuinely
source-compatible sequence of repaired moves. This is an exact
conservation law and correctly explains why independent-layer collision
loss is not an unavoidable chronological toll.

It does not construct the sequence: the target words at one time still
must be certified source words for the next collection. The primary
report correctly leaves this chronology compatibility unproved.

## 6. Final corrected boundary

Unconditionally proved:

1. exact packet owner marginals, including the explicit \(K_{ij}\)
   compatibility coefficient, and exact collision expectations;
2. linear collision under independent packet relabeling with failure
   probability at most \(\exp[-\Omega(W/m)]\);
3. the exact carrier-respecting unbundled Hall factor covering
   \(W-o(W)\) two-outside owner mass;
4. an exact pooled owner-capacity realization with maximum degree \(L\)
   after at most \(Wm^{-4+o(1)}\) packet deletions and \(o(W)\) owner
   incidence loss;
5. failure of the standard asymmetric atomic owner-event LLL via the
   packet-star clique;
6. the full-orbit degree ratio \(D_X/D_T=dN/W=1-o(1)\); and
7. exact conservation of the middle-owner vector along every genuinely
   applicable repaired chronology.

Not proved:

1. a deterministic lower bound on the minimum collision over all legal
   relabel choices;
2. failure of every possible lopsided or grouped-event LLL;
3. a lift of the carrier-respecting Hall factor to twelve common legal
   repaired word decks;
4. an \(L\)-edge-colouring, even approximately, of the pooled resource
   hypergraph; or
5. chronological compatibility of any resulting colours.

Accordingly, “independent relabeling and the canonical LLL do not solve
the gate” is rigorous. “No deterministic legal relabeling can be good”
and “every possible LLL misses by \(\Theta(m)\)” remain overclaims.
