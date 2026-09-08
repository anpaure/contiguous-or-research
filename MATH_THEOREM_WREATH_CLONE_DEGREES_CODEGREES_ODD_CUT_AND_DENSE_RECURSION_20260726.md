# Clone-aware wreath cycles: exact degrees, laminar codegrees, the local odd cut, and recursive dense mixing

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 \Omega=\binom{[2m]}m,\qquad W=|\Omega|,
 \qquad N_q=\binom{2m}{m-q},
 \qquad \lambda_q={W\over N_q}=c_q+\alpha_q.                  \tag{0.1}
\]

Consider the directed wreath cycles obtained from cyclic orders of the
\(2m\) coordinates, and the clone-aware lift having \(c_q\) compulsory
slots and one optional slot at every signed depth-\(q\) target.

This note computes its incidence kernel exactly.

1. There are \((2m-1)!\) directed wreath cycles.  A complementary owner
   pair has degree

   \[
                                  D_0=m!^2,                     \tag{0.2}
   \]

   while every lower or upper depth-\(q\) target has degree

   \[
                                  D_q=(m-q)!(m+q)!
                                      =\lambda_qD_0.            \tag{0.3}
   \]

2. If two complementary owner pairs are at quotient Johnson distance
   \(d\in\{1,\ldots,m-1\}\), their exact normalized codegree is

   \[
                         {D(p,p')\over D_0}
                           ={2\over\binom md^2}.                 \tag{0.4}
   \]

3. If \(T\) is a lower target of size \(k=m-q\), \(p_X=\{X,X^c\}\),
   and \(a=|T\cap X|\), then

   \[
   {D(p_X,T)\over D_0}
      ={\nu_{q}(a)\over
        \binom ma\binom m{k-a}},                               \tag{0.5}
   \]

   where \(\nu_q(a)=q+1\) for \(a\in\{0,k\}\), and
   \(\nu_q(a)=2\) otherwise.  In particular,

   \[
              \max_{p,T}{D(p,T)\over D_0}
              ={q+1\over\binom mq}.                            \tag{0.6}
   \]

4. For two distinct targets of the same lower rank, with
   \(d=|T\setminus T'|\),

   \[
   {D(T,T')\over D_q}
   =
   \begin{cases}
   \displaystyle {2\over
        \binom{m-q}{d}\binom{m+q}{d}},&1\le d<m-q,\\[3mm]
   \displaystyle {2q+1\over\binom{m+q}{2q}},&d=m-q.
   \end{cases}                                                  \tag{0.7}
   \]

5. The largest correlations are instead the laminar cross-depth ones.
   If \(U\subset T\), \(|T|=m-q\), \(|U|=m-r\), and \(s=r-q\), then

   \[
                         {D(T,U)\over D_q}
                           ={s+1\over\binom{m-q}s}.             \tag{0.8}
   \]

   In particular, an adjacent child has conditional codegree

   \[
                                  {2\over m-q}.                 \tag{0.9}
   \]

   Upper formulas reduce to these by complementation.  There is one
   exceptional mixed-sign identity:

   \[
                              D(T,T^c)=D_q.                     \tag{0.10}
   \]

   Thus the naïve lower/upper clone hypergraph has constant weighted
   codegree \(1/\lambda_q\) between the compulsory clones of \(T\) and
   \(T^c\).  This is deterministic pairing, not random overlap.

Fuse every complementary signed pair \((T,T^c)\) into one quota vertex
and assign the two physical occurrences to the same clone.  In this
**paired-sign clone hypergraph**, the maximum weighted codegree through
\(H=o(m)\) satisfies

\[
 {2\over m+1}
 \le
 \max_{u\ne v}\sum_{e\supset\{u,v\}}\widehat w_e
 \le {2+o(1)\over m-H}.                                      \tag{0.11}
\]

Thus the kernel is genuinely sparse, but only at scale \(m^{-1}\).  Since
a lifted edge has rank

\[
                                  K=m(2H+1),                    \tag{0.12}
\]

one cannot infer the required absolute \(o(W)\) leave from a fixed-rank
edge-colouring theorem: the elementary correlation product is
\(K\Delta_2=\Theta(H)\), not \(o(1)\).  This is a limitation of that
black-box route, not a matching impossibility.

There is, however, a genuine odd-set obstruction to **internal** packet
closure.  In every canonical six-owner \(J(4,2)\) fibre, contract the
three local antipodal owner pairs.  The internal \(2\)-safe cycle columns
are the three edges of a triangle.  Their fractional matching has value
\(3/2\), whereas an integral matching has value at most one.  Summed over
the \((1-o(1))W/6\) fibres, this is exactly the stable dense-mixing toll:
an almost-spanning safe factor must have cross-fibre transition incidences
in \(\Omega(W)\) distinct local fibres.  One dense cycle column may supply
many of those incidences.

The odd cut is not global.  It is destroyed constructively by dense
mixing.  For every \(2\le s\le m-2\), a context cube \(Q_s\) times one local
\(J(4,2)\) admits an explicit physical \(2\)-safe Hamilton cycle of
length

\[
                                  6\cdot2^s.                    \tag{0.13}
\]

This recursively fuses \(2^s\) obstructed six-fibres into one cycle.  It
proves that the triangle obstruction demands dense physical columns; it
does not prohibit them.  Extending this recursion to \(H>2\) while
retaining the all-depth clone matching remains the exact positive gate.

## 1. The directed wreath multihypergraph

A directed cyclic order

\[
                         \pi=(v_0,v_1,\ldots,v_{2m-1})           \tag{1.1}
\]

is taken modulo cyclic rotation, but not reflection.  It gives

\[
                         X_i=\{v_i,\ldots,v_{i+m-1}\},
                         \qquad i\in\mathbb Z_{2m}.             \tag{1.2}
\]

Distinct directed cyclic orders are retained as parallel configuration
columns if they have the same unlabelled owner support.  There are
\((2m-1)!\) such orders.

The cycle contains \(X_i^c=X_{i+m}\).  Contract complementary owners and
write \(p_X=\{X,X^c\}\).  Every wreath column contains exactly \(m\)
owner-pair vertices.

At signed depth \(q<m\),

\[
 \begin{aligned}
 L_q(i)&=\{v_{i+q},\ldots,v_{i+m-1}\},\\
 U_q(i)&=\{v_i,\ldots,v_{i+m+q-1}\}.
 \end{aligned}                                                  \tag{1.3}
\]

Each of the two lists in (1.3) contains \(2m\) distinct targets.

## 2. Exact vertex degrees

### Proposition 2.1 (owner and target degrees)

Equations (0.2)--(0.3) hold.

#### Proof

Fix \(X\) as the window in positions \(0,\ldots,m-1\).  Its elements may
be ordered in \(m!\) ways and the elements of \(X^c\) in another \(m!\)
ways.  Every directed cyclic order containing \(p_X\) has a unique such
rotation, proving \(D_0=m!^2\).

Fix a lower target \(T\) of size \(m-q\) in positions
\(q,\ldots,m-1\).  Its elements can be ordered in \((m-q)!\) ways and all
remaining \(m+q\) coordinates in \((m+q)!\) ways.  The target occurrence
has a unique start, so \(D_q=(m-q)!(m+q)!\).  The upper count is its
complement.  Finally,

\[
 {D_q\over D_0}={(m-q)!(m+q)!\over m!^2}
 ={\binom{2m}m\over\binom{2m}{m-q}}=\lambda_q.                 \tag{2.1}
\]

\(\square\)

## 3. Exact owner codegrees

Fix representatives \(X,Y\) with \(d_J(X,Y)=d\).  If a wreath order has
\(X=X_0\) and \(Y=X_d\), its four consecutive coordinate sectors are

\[
 X\setminus Y,\quad X\cap Y,\quad Y\setminus X,
 \quad [2m]\setminus(X\cup Y),                                 \tag{3.1}
\]

of sizes \(d,m-d,d,m-d\).  They may be ordered in

\[
                                  [d!(m-d)!]^2                  \tag{3.2}
\]

ways.  The quotient pair \(p_Y\) may occur in either cyclic orientation,
giving the two disjoint placements \(d\) and \(m-d\).

### Proposition 3.1 (owner-pair codegree)

For distinct quotient owner vertices,

\[
 D(p_X,p_Y)=2[d!(m-d)!]^2,
 \qquad
 {D(p_X,p_Y)\over D_0}={2\over\binom md^2}.                    \tag{3.3}
\]

In particular the largest owner codegree ratio is \(2/m^2\).

## 4. Owner--target codegrees

Condition on a cyclic order containing \(p_X\), represented with the
\(X\)-half first.  The orders inside \(X\) and \(X^c\) are independent
uniform permutations.  Let \(T\) be a lower target of size \(k=m-q\) and
put \(a=|T\cap X|\).

If \(a=0\) or \(a=k\), the interval \(T\) lies in one half and has
\(q+1\) possible positions.  If \(0<a<k\), it crosses one of the two
half-boundaries, giving two possible positions.  At any specified
position, the probability that the required coordinate subsets occupy
the interval is

\[
                         {1\over\binom ma\binom m{k-a}}.        \tag{4.1}
\]

The position events are disjoint.

### Proposition 4.1 (owner--target kernel)

Equation (0.5) holds.  Its maximum is attained when \(T\subseteq X\) or
\(T\subseteq X^c\), and is (0.6).

#### Proof of the maximum

For an interior split, first count disjoint ordered pairs consisting of an
\(a\)-set and a \((k-a)\)-set.  This gives

\[
 \binom ma\binom m{k-a}
 \ge \binom ma\binom{m-a}{k-a}
 =\binom mk\binom ka.                                         \tag{4.2}
\]

Since \(\binom ka\ge2/(q+1)\),

\[
 {2\over\binom ma\binom m{k-a}}
 \le {q+1\over\binom mk}
 ={q+1\over\binom mq}.                                        \tag{4.3}
\]

The finitely many endpoint equalities are immediate. \(\square\)

## 5. Target--target codegrees

Fix a lower target \(T\) of size \(k=m-q\) as one cyclic interval.  The
remaining arc has size \(m+q\).

If another \(k\)-target \(T'\) has Johnson distance \(d<k\) from \(T\),
then it must begin at offset \(d\) from one of the two ends of \(T\).
The common \((k-d)\)-set must occupy the corresponding end of the random
order of \(T\), and the new \(d\)-set the adjacent end of the complementary
arc.  The two orientations give

\[
 {2\over\binom kd\binom{m+q}d}.                                \tag{5.1}
\]

If \(T,T'\) are disjoint, then \(T'\) can occupy any of the \(2q+1\)
length-\(k\) subintervals of the complementary arc, giving

\[
                         {2q+1\over\binom{m+q}k}
                         ={2q+1\over\binom{m+q}{2q}}.          \tag{5.2}
\]

This proves (0.7).

Now let \(U\subset T\) have size \(k-s\).  Conditional on the random
order of \(T\), the specified set \(U\) can occupy any of its \(s+1\)
length-\((k-s)\) subintervals.  Each position has probability
\(1/\binom ks\), and the events are disjoint.  This proves (0.8).

More generally, let \(|U|=l=m-r\le k\) and put \(a=|T\cap U|\).  The
complete cross-depth kernel is

\[
 {D(T,U)\over D_q}
 ={\nu_{q,r}(a)\over
   \binom ka\binom{m+q}{l-a}},                                  \tag{5.3}
\]

where

\[
 \nu_{q,r}(a)=
 \begin{cases}
 r-q+1,&a=l,\\
 q+r+1,&a=0,\\
 2,&0<a<l.
 \end{cases}                                                   \tag{5.4}
\]

Indeed, an interval contained in \(T\) has \(k-l+1=r-q+1\) positions;
one contained in the complementary arc has
\((m+q)-l+1=q+r+1\) positions; and a partially overlapping interval
must cross one of the two boundaries.  At each position the two specified
coordinate parts must occupy the displayed positions in the independent
orders of \(T\) and its complementary arc, giving the denominator in
(5.3).  The position events are disjoint.

For distinct targets with \(q,r\le H=o(m)\), (5.3) is maximized by an
adjacent nested pair and is at most \(2/(m-H)\).  This follows directly
from the three cases in (5.4): the nested case is
\((s+1)/\binom ks\), maximized at \(s=1\); the exterior and crossing
cases have at least the corresponding two-factor binomial denominator.

An upper target is equivalent, after complementation and a cyclic shift,
to a lower interval of its complementary rank.  Thus nondegenerate upper
and mixed-sign codegrees are instances of the same interval formulas.
There is one exact degenerate identity.  From (1.3),

\[
                         U_q(i+m)=[2m]\setminus L_q(i).         \tag{5.5}
\]

Consequently every wreath cycle containing a lower target \(T\) also
contains the upper target \(T^c\), and conversely.  Therefore

\[
                              D(T,T^c)=D_q.                     \tag{5.6}
\]

## 6. Signed-pair fusion and codegrees after quota cloning

If lower and upper occurrences are cloned independently, (5.6) gives

\[
 \sum_{e\supset\{(T,i)^-,(T^c,j)^+\}}\widehat w_e
 ={1\over\lambda_q}.                                           \tag{6.1}
\]

This constant codegree is forced by exact complementation.  It should be
contracted, not estimated as noise.

For every lower target \(T\) of rank \(m-q\), create one *signed-pair*
quota object

\[
                              [T]_q=(T^-,(T^c)^+).               \tag{6.2}
\]

Give \([T]_q\) the \(c_q\) compulsory clones
\([T]_{q,1},\ldots,[T]_{q,c_q}\) and one optional clone.  In a lifted
wreath column, pair the occurrence \(L_q(i)=T\) with
\(U_q(i+m)=T^c\) and assign both to the same clone.  The resulting edge
has \(2m\), rather than \(4m\), target-clone vertices at depth \(q\), so
its total rank through \(H\) is \(m(2H+1)\).

The literal unweighted clone census is also exact.  Put

\[
 b_q=c_q+1,
 \qquad
 \mathcal L_H=\prod_{q=1}^H b_q^{2m}.                         \tag{6.U1}
\]

Every physical wreath column has exactly \(\mathcal L_H\) paired-sign
clone lifts.  Hence

\[
 \widehat D(p)=D_0\mathcal L_H,
 \qquad
 \widehat D([T]_{q,i})={D_q\mathcal L_H\over b_q}              \tag{6.U2}
\]

for every owner pair and every compulsory or optional clone.  For
distinct physical occurrences,

\[
 \begin{aligned}
 \widehat D(p,p')&=D(p,p')\mathcal L_H,\\
 \widehat D(p,[T]_{q,i})&={D(p,T)\mathcal L_H\over b_q},\\
 \widehat D([T]_{q,i},[U]_{r,j})
   &={D(T,U)\mathcal L_H\over b_qb_r}.
 \end{aligned}                                                 \tag{6.U3}
\]

Two different clones of the same signed-pair occurrence have codegree
zero.  Since \(D_q/D_0=\lambda_q<b_q\), the maximum unweighted vertex
degree is \(D_0\mathcal L_H\), attained on the owner-pair shore.  Thus
(0.2)--(0.8) also give every ordinary degree and codegree of the lifted
multihypergraph exactly.

Give every physical wreath cycle weight \(1/D_0\).  At depth \(q\), send
each paired occurrence to a specified compulsory clone with probability
\(1/\lambda_q\), and to the optional clone with probability
\(\alpha_q/\lambda_q\).  Denote the resulting fractional matching by
\(\widehat w\).  Every compulsory signed-pair clone has degree one, and
every optional clone has degree \(\alpha_q\).

This fusion loses no quota capacity.  In any integral matching it enforces

\[
                         \mu_q^-(T)=\mu_q^+(T^c),               \tag{6.3}
\]

so covering all compulsory paired clones and at most one optional clone
gives the required floor/ceiling loads on both signs.  The restriction is
compatible with the common-run point identity: complementation gives
\(h_{q,v}^++h_{q,v}^-=|\mathcal H_q^-|\) automatically.

For a compulsory signed-pair clone \([T]_{q,i}\), Propositions 4.1 and
5.1 give

\[
 \sum_{e\supset\{p_X,[T]_{q,i}\}}\widehat w_e
 ={1\over\lambda_q}
 {\nu_q(a)\over\binom ma\binom m{k-a}},                        \tag{6.4}
\]

and, for two compulsory target clones at depths \(q,r\),

\[
 \sum_{e\supset\{[T]_{q,i},[U]_{r,j}\}}\widehat w_e
 ={1\over\lambda_r}{D(T,U)\over D_q}.                         \tag{6.5}
\]

The optional formulas multiply the corresponding expression by
\(\alpha_q\), \(\alpha_r\), or both.

At depth one,

\[
 \lambda_1={m+1\over m},\qquad
 \max_{p,T,i}
 \sum_{e\supset\{p,[T]_{1,i}\}}\widehat w_e
 ={2\over m+1}.                                                \tag{6.6}
\]

Equations (0.4), (0.7), and (0.8) show that, uniformly for \(q,r\le
H=o(m)\), every other distinct-vertex weighted codegree is at most

\[
                              {2+o(1)\over m-H}.                \tag{6.7}
\]

This proves (0.11).

The significance is precise.  Edge transitivity gives exact vertex
degrees, and all non-laminar pair correlations are \(O(m^{-2})\).  The
only \(m^{-1}\) correlations are containment of a target in a source
owner and containment of one protected target in the adjacent-depth
target.  They are forced by chronology.  Treating all clone vertices as
independent colours discards this decomposable laminar structure.

## 7. The genuine local odd-set inequality

For \(m=2\), the owner-pair shore of the directed wreath hypergraph is
literally three vertices.  Each wreath cycle contains two of them, and
each of the three two-subsets occurs with the two directed orientations.
After parallel orientations are identified, the owner hypergraph is
\(K_3\).  Thus the original permutation-square obstruction is already an
odd-set obstruction in the wreath matching polytope.

Fix one six-owner fibre

\[
                         \mathcal F=\{C\cup S:S\in\tbinom B2\},
                         \qquad |B|=4.                          \tag{7.1}
\]

The local antipodal pairs are

\[
                         A_S=\{C\cup S,C\cup(B\setminus S)\},  \tag{7.2}
\]

giving three pair-vertices.  A physical cycle lying wholly in
\(\mathcal F\) is \(2\)-safe exactly when it is a four-cycle whose square
is local complementation.  It therefore covers exactly two of the three
vertices (7.2).  Conversely every choice of two local antipodal pairs has
such a four-cycle.

After parallel orientations are identified, the internal cycle
hypergraph on (7.2) is the triangle \(K_3\).  If its three columns have
variables \(y_1,y_2,y_3\), the local degree relaxation admits

\[
                              y_1=y_2=y_3={1\over2},             \tag{7.3}
\]

of total value \(3/2\).  Every integral matching obeys the odd-set
inequality

\[
                              y_1+y_2+y_3\le1.                  \tag{7.4}
\]

Thus the internal fractional closure has an exact \(3/2\) gap.  A column
which covers the whole fibre must leave it physically; labels or clone
assignments do not change (7.4).

Equivalently, the degree bound predicts two colours for the three local
columns, while the triangle requires three: its edge-chromatic index is
three although its maximum degree is two.  The missing third colour is
exactly the odd-set inequality (7.4), not a degree or codegree estimate.

There are \((W-E_m)/6\) disjoint canonical fibres, with \(E_m=o(W)\).
If \(L\) owners are left uncovered, at most \(L\) of their odd cuts may be
ignored.  Summing (7.4) therefore forces at least

\[
                              {W-E_m\over6}-L                   \tag{7.5}
\]

fibres to meet a physical cross-fibre column.  This is the odd-set form
of the stable dense-mixing toll.

## 8. A recursive dense physical escape

The odd inequalities are destroyed if the cycle columns mix many fibres.
The following construction does so explicitly at memory two.

Fix the local four-block \(B\).  Outside \(B\), choose
\(2\le s\le m-2\) disjoint
coordinate pairs

\[
                              \{x_1,y_1\},\ldots,\{x_s,y_s\}.   \tag{8.1}
\]

Choose a fixed exterior set of size \(m-2-s\), disjoint from (8.1), and
freeze every other exterior coordinate as absent.  Choosing exactly one
endpoint from every pair in (8.1) now gives contexts of size \(m-2\)
forming a physical context cube \(Q_s\); an edge exchanges \(x_i\) and
\(y_i\).
Tensor it with the six local owners \(\binom B2\).

Let

\[
                         D_0,D_1,\ldots,D_{\ell-1},qquad
                         \ell=2^s,                              \tag{8.2}
\]

be a cyclic Gray Hamilton order of \(Q_s\), and let

\[
                         S_0,S_1,\ldots,S_5                     \tag{8.3}
\]

be the cyclic order

\[
                         12,13,34,14,24,23                     \tag{8.4}
\]

in \(J(4,2)\).  Since \(\gcd(\ell,6)=2\), put

\[
                         L=\operatorname{lcm}(\ell,6)=3\ell.  \tag{8.5}
\]

For \(t\in\mathbb Z_L\), concatenate the two vertices

\[
                         D_t\cup S_t,qquad D_{t+1}\cup S_t,   \tag{8.6}
\]

where the indices on \(D\) and \(S\) are read modulo \(\ell\) and six.

### Theorem 8.1 (recursive \(Q_s\times J(4,2)\) closure)

The sequence (8.6) is a physical \(2\)-safe Hamilton cycle on all
\(6\cdot2^s\) owners of \(Q_s\times J(4,2)\).

#### Proof

The first vertices in the pairs (8.6) are indexed by
\((t\bmod\ell,t\bmod6)\).  They are distinct for
\(0\le t<L\).  The second vertices are indexed by
\(((t+1)\bmod\ell,t\bmod6)\) and are likewise distinct.  The two lists
are disjoint: equality would require simultaneous congruences whose
difference is one modulo \(\gcd(\ell,6)=2\).  Thus (8.6) lists
\(2L=6\ell\) distinct vertices, all vertices of the product.

Transitions alternate cyclically between one exterior cube exchange and
one internal \(J(4,2)\) exchange.  The former uses coordinates outside
\(B\), the latter coordinates inside \(B\).  Every two consecutive
transitions therefore use disjoint physical coordinates, so every
two-step window is geodesic. \(\square\)

The construction fuses \(2^s\) local triangle obstructions into one long
cycle and uses \(3\cdot2^s\) cross-fibre transitions.  This is the dense
mixing demanded by (7.5).  It also reduces the number of components
exponentially in \(s\).

### Lemma 8.2 (depth-one traces remain injective)

Both depth-one target maps, intersection and union, are injective on the
cycle (8.6).

#### Proof

Write

\[
 A_t=D_t\cup S_t,
 \qquad B_t=D_{t+1}\cup S_t.                                  \tag{8.7}
\]

The lower targets on the two alternating edge types are

\[
 \begin{aligned}
 A_t\cap B_t&=(D_t\cap D_{t+1})\cup S_t,\\
 B_t\cap A_{t+1}&=D_{t+1}\cup(S_t\cap S_{t+1}).
 \end{aligned}                                                 \tag{8.8}
\]

They cannot collide across types because their intersections with the
local block \(B\) have sizes two and one.  A context edge of the cyclic
Gray Hamilton cycle occurs once modulo \(\ell\).  Its three repetitions
over \(0\le t<3\ell\) have local phases separated by
\(\ell\equiv2\) or \(4\pmod6\), and the three corresponding \(S_t\)'s
are distinct.  Hence the first line of (8.8) is injective.

For the second line, the local singleton word along (8.4) is

\[
                         1,3,4,4,2,2.                           \tag{8.9}
\]

On each orbit of addition by two modulo six, its three entries are
distinct.  Since every context \(D_{t+1}\) repeats precisely on one such
three-phase orbit, the second line of (8.8) is also injective.

For upper targets, the two local ranks are two and three.  The missing
coordinate word of the local unions is

\[
                         4,2,2,3,1,4,                           \tag{8.10}
\]

which is likewise rainbow on every addition-by-two orbit.  The same
argument, using context-edge unions on the external edges, proves upper
injectivity. \(\square\)

For \(H>2\), (8.6) is insufficient because an exterior cube direction may
recur after only one intervening internal exchange.  A higher-memory
recursion must replace the two-alphabet alternation by a direction word in
which every physical exchange coordinate has cyclic spacing at least
\(H\), while simultaneously preserving the clone incidences of Sections
4--6.  This is now the exact recursive dense-design problem; the bounded
colour and sparse-seam alternatives are closed by (7.4)--(7.5).

## 9. Verdict

The clone-aware wreath kernel is fully explicit.  It is edge-transitive
on every unlabelled orbit, has owner codegree \(O(m^{-2})\), same-depth
target codegree \(O(m^{-2})\), and only the forced adjacent-rank laminar
codegree \(\Theta(m^{-1})\).  The exact local fractional/integral gap is
the triangle odd set (7.4), not a scalar degree deficit.

Dense mixing removes that odd set: Theorem 8.1 gives a recursive literal
closure for \(H=2\), and Lemma 8.2 shows that this repair preserves exact
depth-one rainbow traces on each long component.  What remains for
constant one is an \(H\)-spaced version of this recursion, or an integral
matching theorem which exploits the signed-pair contraction and laminar
kernel (0.8) rather than treating the \(m(2H+1)\)-uniform paired-sign
clone hypergraph as generic.
