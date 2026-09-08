# Paired SCDs, doubly-rainbow Johnson factors, and the exact component gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Verdict

Put

\[
 {\cal L}=\binom{[2m]}{m-1},\qquad
 {\cal M}=\binom{[2m]}m,\qquad
 {\cal U}=\binom{[2m]}{m+1},
\]

\[
 W=|{\cal M}|,\qquad N=|{\cal L}|=|{\cal U}|,
 \qquad D=W-N={W\over m+1}=\operatorname {Cat}_m.
 \tag{0.1}
\]

There are three distinct statements which must not be conflated.

1. A pair of full Boolean SCDs which have the same paired nonmiddle chain
   skeleton--including the pairing of each lower half with an upper
   half--and use opposite corners of every central diamond is exactly an
   **outer-extendible** doubly-rainbow Johnson 2-factor.
2. After the ranks outside \(m-1,m,m+1\) are forgotten, outer
   extendibility disappears: paired decompositions of the central
   three-rank band are exactly doubly-rainbow Johnson 2-factors.
3. Such a factor controls depth one, but it gives neither long components
   nor the no-return/nested-flag identities needed at greater depth.

This gives an immediate obstruction to the proposed all-\(m\) construction.
Every coordinate of the swap multigraph of an exact doubly-rainbow factor
has degree

\[
 D=\operatorname {Cat}_m.
 \tag{0.2}
\]

Every cycle makes those degrees even. Hence

\[
 \boxed{\operatorname {Cat}_m\text{ even is necessary}.}
 \tag{0.3}
\]

Since \(\operatorname {Cat}_m\) is odd exactly for
\(m=2^a-1\), no exact paired SCD exists in any of those dimensions. This
is a global obstruction to every SCD, not merely to canonical BTK.

When a paired SCD does exist, its diamond permutation has cycles of length
at least four and therefore at most \(N/4\) components. This bound is exact
at \(m=2\), where the complement-symmetric \(B_4\) seed is one \(C_4\).
It is far from the coefficient-one requirement. For depth \(H\), the
whole-component compiler pays exactly \(2H\) entries per retained physical
component, so the required condition is

\[
 c=o(W/H),
 \tag{0.4}
\]

together with \(o(W)\) total higher-depth flag failures. Permutation of the
alternate corners alone supplies neither condition. In fact, once the
paired half-chain matching is fixed, the factor and all its components are
fixed; the only remaining choices are the two orientations of each
component.

Consequently a disjoint replication of the four-owner \(B_4\) seed cannot
scale. Covering \(W-o(W)\) owners by unfused copies produces
\((1/4-o(1))W\) components. A successful recursion must make a linear
number of cross-context flag-matching changes and leave only \(o(W/H)\)
lifted components. Complement symmetry does not perform those fusions.

The companion note
MATH_OBSTRUCTION_N_PAIRED_SCD_CATALAN_PARITY_AND_QUARTET_FLUX_20260726.md
proves two further constraints not needed for the equivalence below: an
exact omitted-family pair-incidence identity and an
\((1/4+o(1))W\) fixed-quartet flux toll. Those constraints independently
force a linear number of moving-frame or cross-quartet central
transitions. The component toll proved here remains additional: even a
dense flux-correct system must fuse its middle lift into long cycles.

## 1. Flags and their middle lift

Let \(\Gamma_m\) be the bipartite containment graph with shores
\({\cal L}\) and \({\cal U}\), with \(R\sim U\) when \(R\subset U\).
For a flag \((R,U)\), write

\[
 U\setminus R=\{a,b\}
\]

and define its middle lift by

\[
 \lambda(R,U)=\{R+a,R+b\}.
 \tag{1.1}
\]

This is a Johnson edge. Conversely, a Johnson edge \(XY\) determines the
unique flag

\[
 R=X\cap Y,\qquad U=X\cup Y.
 \tag{1.2}
\]

Call a Johnson edge family **exactly doubly rainbow** when every member of
\({\cal L}\) occurs exactly once as an intersection color and every member
of \({\cal U}\) occurs exactly once as a union color. Thus an exactly
doubly-rainbow family is precisely the lift of a perfect matching of
\(\Gamma_m\).

### Lemma 1.1 (flag-matching equivalence)

For \(M_0\subseteq E(\Gamma_m)\), the following are equivalent.

1. \(M_0\) is a perfect matching of \(\Gamma_m\).
2. \(\Lambda(M_0)=\{\lambda(R,U):(R,U)\in M_0\}\) has \(N\) edges and is
   exactly doubly rainbow.

If, in addition, \(\Lambda(M_0)\) is 2-regular on its support, then its
support has exactly \(N\) middle vertices and its complement in
\({\cal M}\) has size \(D\).

#### Proof

Equations (1.1)--(1.2) identify the two shores of \(\Gamma_m\) with the
two edge-color maps. A 2-regular graph has equally many vertices and
edges, giving the last assertion. \(\square\)

Writing a perfect matching as \(U=\phi(R)\), its exact middle degree
function is

\[
 d_\phi(X)
 =\bigl|\{R\in{\cal L}:R\subset X\subset\phi(R)\}\bigr|.
 \tag{1.3}
\]

Therefore the middle-lift gate is the literal pointwise condition

\[
 d_\phi(X)\in\{0,2\}\quad(X\in{\cal M}).
 \tag{1.4}
\]

Because \(\sum_Xd_\phi(X)=2N\), exactly \(N\) vertices then have degree
two. Requiring one component is exactly the additional connectedness of
this degree-two support. Thus perfect matching in the lower--upper flag
graph, middle-degree feasibility, and component control are three
successive constraints.

## 2. Exact central-band equivalence

Let

\[
 B^{\rm cen}_{2m}
 =\binom{[2m]}{m-1}\cup\binom{[2m]}m
  \cup\binom{[2m]}{m+1}.
\]

A symmetric chain decomposition of this three-rank band consists of chains
\(R\subset X\subset U\), together with singleton middle sets.

Call two such decompositions **opposite-corner paired** if they have the
same pairs \((R,U)\), use opposite middle corners of every interval
\([R,U]\), and have the same singleton leave.

### Theorem 2.1 (central-band paired-SCD theorem)

There is a canonical equivalence between

1. opposite-corner paired SCDs of \(B^{\rm cen}_{2m}\); and
2. exactly doubly-rainbow Johnson 2-factors on \(N\) middle vertices.

Under the equivalence, orienting every factor cycle gives the first
decomposition by taking the tail of each lifted edge, and the second
decomposition by taking its head. Conversely, the map from the middle
corner in the first decomposition to the opposite corner in the second is
a permutation \(g\), and its directed cycles are exactly the factor
components.

For a fixed undirected factor with \(c\) components there are exactly
\(2^c\) ordered opposite-corner pairs: one of the two cyclic orientations
may be chosen independently on each component.

#### Proof

Start with an exactly doubly-rainbow 2-factor \(F\). Orient each component.
For an oriented edge \(X\to Y\), put

\[
 R=X\cap Y,\qquad U=X\cup Y.
\]

The first band decomposition uses \(R\subset X\subset U\); the second
uses \(R\subset Y\subset U\). Every lower and upper set occurs once by
double rainbowness. Every support vertex occurs once as a tail and once as
a head because the components are directed cycles. The other \(D\) middle
sets are singleton chains in both decompositions.

Conversely, the common \((R,U)\)'s form a perfect matching of
\(\Gamma_m\). Direct its lifted edge from the first corner to the second.
Every used middle vertex occurs once in each decomposition, hence once as
a tail and once as a head. The resulting map \(g\) is a permutation and
the lift is a directed 2-factor.

Finally, choosing on every edge one endpoint so that every factor vertex
is chosen once has exactly two solutions on each cycle. Indeed, if edge
\(i\) of a cycle chooses its first endpoint with bit \(x_i\), the
condition at the common vertex of edges \(i-1,i\) is
\(x_i=x_{i-1}\). Thus all bits on that component agree. \(\square\)

In particular, \(g\) is one \(N\)-cycle if and only if the doubly-rainbow
lift is connected. Thus the strongest depth-one component target is
exactly a perfect matching of \(\Gamma_m\) whose middle lift is a single
cycle; no additional orientation argument is needed.

The theorem is an equivalence only for the central band. Full Boolean SCDs
have an additional tail condition, made exact next.

## 3. The exact outer-extendibility condition

A **lower half-SCD** is a partition of the ranks \(0,1,\ldots,m-1\) into
saturated chains, each ending at rank \(m-1\). For the chain ending at
\(R\in{\cal L}\), write

\[
 \rho_-(R)=m-\min\{|S|:S\text{ lies in that chain}\}.
 \tag{3.1}
\]

Thus that chain begins in rank \(m-\rho_-(R)\). An upper half-SCD, after
taking complements, is another lower half-SCD indexed by
\(U^c\in{\cal L}\); denote its radius by \(\rho_+(U)\).

### Theorem 3.1 (full paired-SCD equivalence)

Let \(M_0\) be a perfect matching of \(\Gamma_m\), written
\(U=\phi(R)\), and suppose its lift is a 2-factor. The corresponding
central-band pair extends to two full SCDs of \(B_{2m}\) using the same
paired lower and upper half-chains, and differing only at the middle
vertices, if and only if there exist a lower half-SCD and a complemented
upper half-SCD satisfying

\[
 \boxed{\rho_-(R)=\rho_+(\phi(R))\quad(R\in{\cal L}).}
 \tag{3.2}
\]

Equivalently, a full opposite-corner paired SCD is an exactly
doubly-rainbow 2-factor together with a radius-compatible realization of
its flag matching by two half-SCDs.

#### Proof

Necessity follows by deleting the middle vertex from every nontrivial
chain of either full SCD. A symmetric chain which begins in rank
\(m-\rho\) ends in rank \(m+\rho\), so its lower and upper halves have
the same radius.

For sufficiency, orient every lifted factor component. For a matched flag
\((R,U)\) with oriented corners \(X\to Y\), concatenate

\[
 \begin{array}{c}
 \text{the lower half-chain ending at }R,\\
 R\subset X\subset U,\\
 \text{the upper half-chain beginning at }U.
 \end{array}
 \tag{3.3}
\]

Condition (3.2) makes this chain symmetric. The half-SCDs partition every
nonmiddle rank, the directed factor makes the tails \(X\) partition its
support, and the unused \(D\) middle sets are singleton chains. This is
the first full SCD. Replacing every \(X\) by its head \(Y\) gives the
second, with exactly the same nonmiddle skeleton. \(\square\)

Thus an arbitrary doubly-rainbow 2-factor is not, by itself, a full paired
SCD. It always gives the paired central band, but (3.2) is the exact
additional hypothesis. In particular, lower--upper flag Hall and middle
2-regularity do not prove outer extendibility.

There is a terminology trap here. If “agree off the middle” means only
that the two decompositions have the same cover edges wholly below or
wholly above rank \(m\), deleting rank \(m\) remembers the two half-SCDs
but forgets which lower half is paired with which upper half. The matching
\(\phi\) is then still a genuine degree of freedom, constrained by (3.2).
The phrase **opposite-corner paired** in this note uses the stronger,
central-diamond meaning: \(\phi\) is common to the two SCDs. Component
rigidity begins only after that matching is fixed.

Equivalently, after the two half-SCDs are fixed, the full construction is
a perfect matching in the radius-resolved containment graph

\[
 \bigsqcup_{\rho\ge1}
 \Gamma_m\bigl[
   \{R:\rho_-(R)=\rho\},
   \{U:\rho_+(U)=\rho\}
 \bigr],
 \tag{3.4}
\]

subject simultaneously to the middle degree condition (1.4) and the
desired component structure of its lift. This is the exact outer-packet
matching problem; solving the radius quotas separately does not enforce
the lift constraints.

## 4. The Catalan parity obstruction

For a Johnson edge \(e=XY\), define its swap pair

\[
 s(e)=(X\cup Y)\setminus(X\cap Y)=X\triangle Y.
 \tag{4.1}
\]

For an edge family \(F\), let \(G_{\rm sw}(F)\) be the multigraph on
\([2m]\) whose edge multiset is \(\{s(e):e\in F\}\).

### Lemma 4.1 (componentwise Euler law)

If \(C\) is a Johnson cycle, then every coordinate has even degree in
\(G_{\rm sw}(C)\). More exactly, orienting \(C\) orients every swap from
the deleted coordinate to the inserted coordinate, and indegree equals
outdegree at every coordinate.

#### Proof

On returning to the initial middle set, every coordinate has been inserted
as often as it has been deleted. Its undirected swap degree is twice this
number. \(\square\)

### Theorem 4.2 (global Catalan obstruction)

If an exactly doubly-rainbow Johnson 2-factor exists, then every coordinate
of its swap multigraph has degree

\[
 \begin{aligned}
 d_{G_{\rm sw}(F)}(v)
 &=\#\{U\in{\cal U}:v\in U\}
   -\#\{R\in{\cal L}:v\in R\}\\
 &=\binom{2m-1}{m}-\binom{2m-1}{m-2}\\
 &={1\over m+1}\binom{2m}m=D.
 \end{aligned}
 \tag{4.2}
\]

Hence \(D\) is even. Moreover, if \({\cal E}\) is the family of the
\(D\) unused middle vertices, then

\[
 \boxed{d_{\cal E}(v)=D/2\quad(v\in[2m]).}
 \tag{4.3}
\]

#### Proof

For one flag \((R,U)\), its swap pair is \(U\setminus R\), so its
indicator is \({\bf1}_U-{\bf1}_R\). Summing over every lower and upper
color proves (4.2). Lemma 4.1 makes the degree even.

For (4.3), the number of endpoints of the edge \(\lambda(R,U)\) which
contain \(v\) is

\[
 {\bf1}_{v\in R}+{\bf1}_{v\in U}.
\]

Summing over the factor gives

\[
 2d_{{\cal M}\setminus{\cal E}}(v)
 =\binom{2m-1}{m-2}+\binom{2m-1}{m}.
\]

Since \(d_{\cal M}(v)=\binom{2m-1}{m-1}\), rearrangement using (4.2)
gives (4.3). \(\square\)

### Corollary 4.3 (no all-\(m\) paired SCD)

If \(m=2^a-1\), no opposite-corner paired SCD of \(B_{2m}\) exists.
This remains true if disconnected factors are allowed.

#### Proof

The standard binary valuation identities give

\[
 v_2\binom{2m}m=s_2(m),\qquad
 v_2(\operatorname {Cat}_m)=s_2(m)-v_2(m+1),
 \tag{4.4}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
If \(t=v_2(m+1)\), then \(m\) ends in exactly \(t\) ones, so
\(s_2(m)\ge t\), with equality exactly when \(m=2^t-1\). Thus the
Catalan number is odd exactly in the stated dimensions, contradicting
Theorem 4.2. \(\square\)

This obstruction is strictly beyond the canonical-BTK potential
obstruction: it rules out every possible SCD in infinitely many
dimensions. For the remaining dimensions it is only necessary. The
\(B_4\) seed proves sufficiency at \(m=2\), but no all-even-Catalan
construction is proved here.

For completeness, the seed's factor is

\[
 14\longrightarrow12\longrightarrow23\longrightarrow34
 \longrightarrow14.
 \tag{4.5}
\]

One of its full SCDs is

\[
\begin{array}{c}
 \varnothing\subset1\subset14\subset124\subset1234,\\
 2\subset12\subset123,\qquad
 3\subset23\subset234,\qquad
 4\subset34\subset134,\\
 13,\qquad24.
\end{array}
\tag{4.6}
\]

Replacing the four displayed nontrivial middle members along (4.5) gives
the second full SCD and changes no nonmiddle member.

Its lower colors, in order, are

\[
 1,2,3,4,
\]

and its upper colors are

\[
 124,123,234,134.
\]

Thus both color maps are bijections. Its singleton leave is
\(\{13,24\}\); every coordinate occurs once in that leave, agreeing with
\(D/2=1\). The twisted complement
\((1\ 3)(2\ 4)\circ(S\mapsto[4]\setminus S)\) fixes all four factor
vertices. This verifies directly both the positive seed and the fact that
its symmetry does not create a component fusion.

## 5. Exact component information and its limitations

For a factor component \(C\), let \({\cal L}_C,{\cal U}_C\) be its two
edge-color families and \({\cal A}_C\) its middle support. After orienting
\(C\), let \(r_C(v)\) be the number of transitions which insert \(v\)
(equivalently, the number which delete \(v\)).

### Proposition 5.1 (componentwise color-profile identities)

For every coordinate \(v\),

\[
 \boxed{
 \begin{aligned}
 d_{{\cal U}_C}(v)-d_{{\cal L}_C}(v)&=2r_C(v),\\
 d_{{\cal A}_C}(v)
 &=d_{{\cal L}_C}(v)+r_C(v)
  =d_{{\cal U}_C}(v)-r_C(v).
 \end{aligned}}
 \tag{5.1}
\]

In particular, the upper-minus-lower coordinate vector of every individual
component is entrywise nonnegative and even, and
\(\sum_vr_C(v)=|C|\).

#### Proof

For one edge, \({\bf1}_U-{\bf1}_R\) is the indicator of its two swap
coordinates. Summing on \(C\), each coordinate is inserted and deleted
equally often, proving the first identity. The total incidence of \(v\)
among the two middle endpoints of one lifted flag is
\({\bf1}_{v\in R}+{\bf1}_{v\in U}\). Since every middle vertex of \(C\)
has factor degree two,

\[
 2d_{{\cal A}_C}(v)
 =d_{{\cal L}_C}(v)+d_{{\cal U}_C}(v).
\]

Combine this with the first identity. There is one insertion per oriented
edge, giving the final sum. \(\square\)

Thus global Euler balance is weaker than component feasibility: the
parity and dominance equations must hold on every proposed lifted cycle,
not merely after summing all cycles.

### Proposition 5.2 (minimum component length)

Every component of an exactly doubly-rainbow Johnson 2-factor has length
at least four. Consequently

\[
 c(F)\le \left\lfloor{N\over4}\right\rfloor.
 \tag{5.2}
\]

The bound is sharp: at \(m=2\), the complement-symmetric \(B_4\) seed has
\(N=4\) and its lift is one \(C_4\).

#### Proof

Loops and two-cycles are absent in a simple factor. Consider a Johnson
triangle. Write two adjacent vertices as \(R+a,R+b\), with \(|R|=m-1\).
A common Johnson neighbor is of one of two types:

\[
 R+c,
 \qquad\text{or}\qquad
 (R-r)+a+b\quad(r\in R).
 \tag{5.2}
\]

In the first case all three edges have lower color \(R\); in the second
case all three have upper color \(R+a+b\). Hence a doubly-rainbow factor
has no triangle. The \(B_4\) cycle proves equality. \(\square\)

The proposition is the complete component bound obtained from
double-rainbow simplicity alone. Since \(N=(1-o(1))W\), it permits
\(\Theta(W)\) components. The fact that \(g\) is a permutation does not
improve it.

### Proposition 5.3 (fixed-skeleton component rigidity)

Fix the two half-SCDs and the lower--upper flag matching \(M_0\) in
Theorem 3.1. Then every paired SCD supported by this fixed off-middle
skeleton has the same undirected diamond factor \(\Lambda(M_0)\), the same
component partition, and the same component lengths. The only freedom is
to reverse any subset of the components.

#### Proof

The common nonmiddle chain through \(R\) fixes its first upper member
\(U=\phi(R)\), hence fixes the lifted edge \(\lambda(R,U)\). The final
assertion is the \(2^c\) orientation statement in Theorem 2.1. \(\square\)

Thus orientations cannot merge short cycles. Component control must be
built into the lower--upper flag matching or introduced by a change of the
off-middle skeleton.

### Proposition 5.4 (the exact color-preserving exchange space)

Let \(M_0,M_1\) be two perfect matchings of \(\Gamma_m\). Their symmetric
difference is a disjoint union of alternating even cycles in
\(\Gamma_m\). Conversely, switching the matching shore on any union of
such alternating cycles preserves every lower and upper color exactly.

In particular, a two-flag switch

\[
 (R_1,U_1),(R_2,U_2)
 \longleftrightarrow
 (R_1,U_2),(R_2,U_1)
 \tag{5.3}
\]

is legal exactly when all four displayed containments hold. It changes
the lifted component count only if the corresponding four middle-corner
edges perform a genuine cycle splice. After the switch one must separately
verify 2-regularity and the radius compatibility (3.2).

#### Proof

The symmetric difference of two perfect matchings has degree zero or two
at every bipartite vertex, and therefore is a union of alternating even
cycles. Reversing either matching on such a cycle preserves saturation of
both shores. The last statement is the length-four case. \(\square\)

This is the exact reason point margins are insufficient: target colors are
preserved by an alternating matching packet, whereas component fusion is a
property of its middle lift and full paired-SCD validity additionally sees
the two half-chain radii.

## 6. Double rainbowness is not physical-strip structure

Let a directed factor component be

\[
 X_0\to X_1\to\cdots\to X_{\ell-1}\to X_0,
\]

and put

\[
 a_t=X_t\setminus X_{t+1},\qquad
 b_t=X_{t+1}\setminus X_t.
 \tag{6.1}
\]

### Proposition 6.1 (physical-cycle recognition)

The component is a physical sliding-window \(C_{2h}\) exactly when

\[
 \ell=2h,qquad a_0,\ldots,a_{2h-1}\text{ are distinct},qquad
 b_t=a_{t+h}\quad(t\bmod 2h).
 \tag{6.2}
\]

In that case, for a fixed \((m-h)\)-set \(K\),

\[
 X_t=K\cup\{a_t,a_{t+1},\ldots,a_{t+h-1}\}.
 \tag{6.3}
\]

#### Proof

A physical window deletes the first active coordinate and inserts the
antipodal one, proving necessity. Conversely, (6.2) gives
\(X_{t+1}=X_t-a_t+a_{t+h}\); induction from \(X_0\) yields (6.3).
\(\square\)

Neither (6.2) nor even the parity of \(\ell\) follows from local double
rainbowness. For a literal example in \(J(6,3)\), fix coordinate \(6\),
index \(1,\ldots,5\) cyclically, and put

\[
 X_i=\{6,i,i+1\}.
 \tag{6.4}
\]

Then \(X_1X_2\cdots X_5X_1\) is a Johnson \(C_5\), with five distinct
lower colors

\[
 X_i\cap X_{i+1}=\{6,i+1\}
\]

and five distinct upper colors

\[
 X_i\cup X_{i+1}=\{6,i,i+1,i+2\}.
\]

It also satisfies the componentwise Euler law, but it is odd and hence is
not physical. This is a local central-band packet, not a claimed complete
factor of \(J(6,3)\); indeed the global factor in that dimension is
excluded by Corollary 4.3.

For depths \(q>1\), paired SCD data supply chain flags
\(D_q(X),E_q(X)\), while the factor cycle supplies literal windows

\[
 \bigcap_{j=0}^qg^j(X),\qquad
 \bigcup_{j=0}^qg^j(X).
 \tag{6.5}
\]

There is no implication from the depth-one equality to

\[
 D_q(X)=\bigcap_{j=0}^qg^j(X),\qquad
 E_q(X)=\bigcup_{j=0}^qg^j(X).
 \tag{6.6}
\]

Returns among the first \(q\) swaps can even make the sets in (6.5) have
the wrong ranks. Thus paired SCD, double rainbowness, physicality, and
nested-flag coherence are four separate levels of structure.

## 7. The exact coefficient-one component gate

Suppose a paired SCD has a family \({\cal C}\) of retained physical
\(C_{2h_C}\)-components with \(H<h_C\), each coherent through depth
\(H\) in the sense of (6.6). Let

\[
 B_0=N-\sum_{C\in{\cal C}}|C|
 \tag{7.1}
\]

be the nontrivial middle-owner leave, and let \(B_{\rm flag}\) count all
missing or incorrect rooted lower and upper identities in (6.6), over
\(1\le q\le H\), including the corresponding rooted identities of omitted
owners. Let \(\Delta_H\) be the actual number of signed target identities
absent from all retained literal windows. The uniqueness of the SCD owner
at every rank gives

\[
 \Delta_H\le B_{\rm flag}.
 \tag{7.2}
\]

Put \(c=|{\cal C}|\).

### Theorem 7.1 (paired-SCD prefix compiler)

The whole-component physical compiler has the finite central bound

\[
 \boxed{W+2Hc+\Delta_H
 \ \le\ W+2Hc+B_{\rm flag}.}
 \tag{7.3}
\]

before the factor-blind tail term. In particular, the paired-SCD route is
coefficient-safe whenever

\[
 B_0+B_{\rm flag}=o(W),\qquad c=o(W/H).
 \tag{7.4}
\]

For the exact no-leave, no-flag-error case, (7.3) is simply

\[
 W+2Hc.
 \tag{7.5}
\]

#### Proof

The retained cycles use \(N-B_0\) middle owners. Repeating the first
\(2H\) delay atoms linearizes every cyclic lower and upper witness through
depth \(H\), at exactly \(2H\) extra entries per component. Append each
unused middle owner once. The inherent singleton leave has size
\(D=W-N\), so the middle ledger is

\[
 (N-B_0)+2Hc+(D+B_0)=W+2Hc.
\]

Absent signed targets are repaired literally, at cost at most
\(\Delta_H\), and (7.2) gives the rooted-error upper bound. Notice that
\(B_0\) cancels from the middle-length
ledger: an omitted cyclic owner is replaced by one singleton occurrence.
It remains in (7.4) as the structural owner-leave requirement, and it also
forces first-depth flag loss unless separately recovered. This proves
(7.3)--(7.4). \(\square\)

The scale \(c=o(W/H)\) is not cosmetic. In the whole-cycle compiler the
collar is exactly \(2Hc\). Equivalently, since the retained mass is
\((1-o(1))W\), the average retained component length must be
\(\omega(H)\). A bare permutation theorem gives only average length at
least four.

### Corollary 7.2 (factor-blind endgame implication)

Let \(L_m(m-H-1)\) denote the established product-SCD tail cost below the
unresolved central band. Under the hypotheses of Theorem 7.1,

\[
 \nu(2m)\le
 W+2Hc+\Delta_H+L_m(m-H-1),
 \tag{7.6}
\]

and the complete-word parity lift gives

\[
 \nu(2m+1)\le
 2\bigl[W+2Hc+\Delta_H+L_m(m-H-1)\bigr].
 \tag{7.7}
\]

Consequently, when \(H/\sqrt m\to\infty\) and \(H=o(m)\), the proved
factor-blind tail estimate together with (7.2) and (7.4) composes
quantitatively into coefficient one.

#### Proof

Equation (7.3) is precisely the central input required by the
factor-blind product-SCD tail theorem. That theorem appends the term
\(L_m(m-H-1)\) without inspecting the central factor, and its
complete-word lift doubles the even-ground bound. \(\square\)

### Corollary 7.3 (bounded-seed replication no-go)

Suppose \(P\) disjoint copies of the \(B_4\) central seed are inserted in
frozen contexts and no operation fuses different copies. They cover
exactly \(4P\) nontrivial owners and have exactly \(P\) components. If
they cover \(W-o(W)\) middle owners, then

\[
 P=(1/4-o(1))W,
\]

and their whole-component collar is

\[
 2HP=(1/2-o(1))HW,
\]

not \(o(W)\). Reducing to \(o(W/H)\) components requires at least

\[
 P-o(W/H)
 \tag{7.8}
\]

successful cross-component mergers, since one merger can reduce the
component count by at most one.

Thus the complement-symmetric \(B_4\) seed is a valid local base but not a
scaling theorem. A product or outer-packet recursion must simultaneously
alter the flag matching through legal alternating packets, preserve
2-regularity and radius compatibility, and create macroscopic lifted
cycles.

## 8. What complement symmetry does and does not give

Assume first that the common flag skeleton is invariant under ordinary set
complementation and that complementation reverses its nontrivial chains.
Write its flag matching as \(U=\phi(R)\).

### Proposition 8.1 (ordinary-complement Kneser reduction)

The map

\[
 \tau(R)=\phi(R)^c
 \tag{8.1}
\]

is an involution of \({\cal L}\) satisfying \(R\cap\tau(R)=\varnothing\).
For \(m\ge2\), its orbits form a perfect matching of
\(KG(2m,m-1)\). Conversely, every such Kneser matching specifies a
complement-closed perfect flag matching by

\[
 \phi(R)=\tau(R)^c.
 \tag{8.2}
\]

Its canonical middle lift is the paired central-diamond factor. Thus in
the ordinary-complement subclass, the q=1 existence and one-component
targets are respectively:

1. the Kneser matching's canonical lift has degrees only zero and two;
2. its nonisolated lift is connected.

Neither property follows from the Kneser perfect matching alone.

#### Proof

Complement reversal sends the flag \((R,\phi(R))\) to
\((\phi(R)^c,R^c)\). Hence
\(\phi(\phi(R)^c)=R^c\), which is \(\tau^2(R)=R\). Also
\(R\subset\phi(R)\) is equivalent to
\(R\cap\phi(R)^c=\varnothing\). The converse is the same calculation
reversed. The lift and component claims follow from Theorem 2.1.
\(\square\)

The labelled \(B_4\) seed is invariant under a twisted complement, not
ordinary complementation, so Proposition 8.1 does not directly tensor
that seed.

Let \(\theta\) be an involution of the middle layer preserving a directed
factor and commuting with its permutation \(g\).

### Lemma 8.2 (involution action on components)

Every \(g\)-cycle is either paired by \(\theta\) with a distinct cycle of
the same length or is stabilized by \(\theta\). On a stabilized cycle of
length \(\ell\),

\[
 \theta|_C=g^s,
 \qquad 2s\equiv0\pmod\ell.
 \tag{8.3}
\]

If \(\theta\) has no fixed middle set, a stabilized cycle is even and
\(s=\ell/2\).

#### Proof

Commutation sends a \(g\)-orbit to a \(g\)-orbit of the same length. On a
stabilized cyclic orbit, every commuting permutation is a rotation, so it
is \(g^s\). The involution identity gives (8.3). If there are no fixed
points, \(s\ne0\), leaving only the antipodal rotation. \(\square\)

This lemma gives orbit pairing but no bound on the number of orbits. Pure
set complementation is fixed-point-free and hence forces an antipodal
action on every stabilized component; a twisted complement may have fixed
middle sets. In the labelled \(B_4\) seed, the twisted complement fixes the
four cycle states, so even antipodal motion is absent. In neither case does
symmetry fuse components created in different contexts.

## 9. Exact proved and open boundary

The following implications are proved:

\[
 \begin{array}{c}
 \text{full paired SCD}\\
 \Downarrow\\
 \text{outer-extendible exact doubly-rainbow Johnson 2-factor}\\
 \Downarrow\\
 \text{exact }q=1\text{ lower and upper coverage, owner leave }D=o(W).
 \end{array}
 \tag{9.1}
\]

The reverse first implication holds exactly with the radius-compatible
half-SCD condition (3.2). At central-band level it holds without any extra
hypothesis.

The all-\(m\) exact target is false because of Corollary 4.3. For
dimensions with even Catalan number, the following remain unproved:

1. a radius-compatible perfect flag matching whose lift is 2-regular;
2. a construction leaving only \(o(W/H)\) lifted components;
3. physical/no-return component structure through the required depth;
4. aggregate nested-flag error \(o(W)\).

The \(B_4\) seed realizes the exact finite local analogues of these clauses
at \(m=2\). Its fixed disjoint tensor replication fails the asymptotic
component clause by Corollary 7.3. Therefore the sharp recursive target is
not merely to propagate a local central diamond. It is to build a global
radius-compatible flag matching whose middle lift has macroscopic cycles
and whose SCD tails follow those cycles as nested literal windows.
