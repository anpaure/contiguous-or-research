# Unseeded ordinary frames: an SCD-seeded Hall compiler, the cyclic-closure gate, and the rotor-macro wall

Date: 2026-07-27

Scope: constant-one program; pure mathematics only.  No computation,
search, solver, web input, or fixed-uniformity matching theorem is used.

## 0. Outcome and exact logical boundary

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{M},\qquad
 R_H={W\over N}.
\tag{0.1}
\]

Take the critical packing height: \(H\) is the least integer for which

\[
 R_H\ge M.
\tag{0.2}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 R_H=M+O(H),\qquad MN=W-o(W),\qquad N=O(W/m).
\tag{0.3}
\]

An ordinary frame on a top \(U\in\binom{[2m]}M\) is the \(M\)-set of
rank-\(m\) cyclic windows of one cyclic order on \(U\).  The installation
of the twelve-top/rectangle bank requires an **integral matching** of
\(N-o(N)\) such frames, not merely \(W-o(W)\) distinct owners in the union
of \(N\) possibly intersecting frames.

This note proves the following.

1. Every full symmetric-chain decomposition supplies a distinct entrance
   owner for every rank-\(M\) top.  Starting from those entrances, choosing
   the remaining coordinates of the top orders is an exact sequence of
   ordinary bipartite Hall problems.  If \(\delta_t\) is the Hall deficiency
   at layer \(t\), the principal-owner repeat excess is at most

   \[
                         \sum_{t=0}^{m-1}\delta_t.          \tag{0.4}
   \]

2. Closing the \(N\) resulting open paths into cyclic frames adds exactly
   \((H-1)N\) owner occurrences.  Hence

   \[
   E_{\rm full}\le \sum_t\delta_t+(H-1)N,                 \tag{0.5}
   \]

   and \(\sum_t\delta_t=o(W)\) suffices for a literal one-frame-per-top
   union with \(W-o(W)\) distinct owners.

   This is **not** the integral near-resolution needed by the bank.  A
   sufficient integral statement is

   \[
   \sum_t\delta_t+Q_{\rm wrap}=o(N),                      \tag{0.6}
   \]

   where \(Q_{\rm wrap}\) is the actual additional repeat excess created
   by the \(H-1\) wrap owners per top.  More generally, it is enough that
   the final frame-conflict graph have a vertex cover of size \(o(N)\).
   Neither sufficient statement is proved here.

3. Pairwise overlap of size at least two in one Hall layer is localized
   exactly in equal-\((m+1)\)-core classes.  Distinct cores share at most
   one facet.  An equal-core class of \(s\) states whose union of currently
   allowed facets has size \(d\) forces deficiency at least \(s-d\).
   Equal-core classes are not all Hall obstructions: a linear star of
   distinct cores can have deficiency \(s-1\).  Thus the deterministic
   route must control every Hall cut, not only higher pair overlaps.

4. The existing one-hole SCD/rotor reservoir macro does not repair the
   cyclic gate.  In its natural \(2(m-H)\)-top necklace, every restored
   deleted owner is equal to a retained owner in another ring.  The frame
   conflict graph is a union of cycles and at most half of its full frames
   can coexist in an ordinary-frame matching.  Thus the macro is a valid
   open-path/support packet but is statewise unusable as an integral
   ordinary-frame packet.

5. Batching these paths also does not create a black-box growing-rank
   matching theorem.  The macro's top projection is square-critical, and
   its owner lift has a nonvanishing **linear** codegree parameter.  The
   top bound survives every top-regular thinning, and the owner bound
   survives every owner-regular thinning.

6. The complete external factorial-overlap table of ordinary frames is
   computed exactly through order \(H\).  Uniformly for \(2\le t\le H\),

   \[
   A_t^{\rm ext}
   ={2MD\over(m)_{t-1}^2}
     \left(1+O\!\left({1\over m-H}+{H^2\over(m-H)^2}\right)\right).
   \tag{0.7}
   \]

   Thus there is no hidden static high-order tail.  The missing assertion
   is deterministic/dynamic avoidance of equal-core and adjacent-domino
   concentration after long prefixes.  Fixed-uniformity
   Pippenger--Spencer cannot be substituted for it.

Consequently the current SCD/rotor lane has an exact positive reduction,
but not the unseeded ordinary-frame near-resolution.  The sharp surviving
gate is a circular SCD Hall theorem proving (0.6), or directly an
\(o(N)\)-vertex-cover bound for the final frame-conflict graph.

## 1. Critical calibration

Minimality of \(H\) gives \(R_{H-1}<M-1\).  Since

\[
 {R_H\over R_{H-1}}={M\over m-H+1},
\tag{1.1}
\]

we have

\[
 M\le R_H<(M-1){M\over m-H+1}=M+O(H).
\tag{1.2}
\]

The standard expansion

\[
 \log R_H
 =\sum_{j=1}^H\log {m+j\over m-j+1}
 ={H^2\over m}+O\!\left({H^3\over m^2}+{H\over m^2}\right)
\tag{1.3}
\]

and (R_H\asymp m) prove the first assertion in (0.3).  The rest follows
from (N=W/R_H) and

\[
 {MN\over W}={M\over R_H}=1-O(H/m).
\tag{1.4}
\]

We shall use repeatedly

\[
 W-(m+1)N
 =N(R_H-m-1)=O(HN)=o(W).
\tag{1.5}
\]

## 2. The exact open-path compiler

Let (U\) be a rank-(M) top and let

\[
 \mathbf c=(c_0,c_1,\ldots,c_{M-1})
\tag{2.1}
\]

be a linear order of its coordinates.  For (0\le i\le m), define the
nonwrapping principal owner

\[
 P_i(U,\mathbf c)
 =U\setminus\{c_i,c_{i+1},\ldots,c_{i+H-1}\}.
\tag{2.2}
\]

These (m+1) owners are distinct.  Reading (2.1) cyclically adds the
remaining (H-1) wrap owners and gives the complete ordinary frame.

For a family of (C) distinct tops with one order on each, let
\(\mu_X^{\rm pr}\) and \(\mu_X^{\rm full}\) be the principal and full owner
multiplicities, and put

\[
 Q=\sum_X(\mu_X^{\rm pr}-1)_+,
 \qquad
 E_{\rm full}=\sum_X(\mu_X^{\rm full}-1)_+.
\tag{2.3}
\]

### Theorem 2.1 (long open-path compiler)

For every such family,

\[
 \boxed{E_{\rm full}\le Q+(H-1)C.}                       \tag{2.4}
\]

Moreover

\[
 \boxed{
 W-|\operatorname {supp}\mu^{\rm full}|
 =W-MC+E_{\rm full}
 \le W-(m+1)C+Q.}                                      \tag{2.5}
\]

#### Proof

There are exactly ((m+1)C) principal occurrences and exactly
((H-1)C) added wrap occurrences.  Adding one occurrence raises repeat
excess by at most one, proving (2.4).  Since there are (MC) full
occurrences,

\[
 |\operatorname {supp}\mu^{\rm full}|=MC-E_{\rm full}.
\]

Substitute (2.4) to obtain (2.5).  \(\square\)

For (C=N), (1.5) and (2.5) give the exact support implication

\[
 Q=o(W)\quad\Longrightarrow\quad
 |\operatorname {supp}\mu^{\rm full}|=W-o(W).
\tag{2.6}
\]

The (N) open paths already have the desired component scale:

\[
 N=O(W/m)=o(W/H).
\tag{2.7}
\]

Thus the endpoint count is not the obstruction.  The issue is choosing
the paths and closing them without distributing conflicts over a linear
number of tops.

## 3. Every SCD gives distinct entrances

Fix any full symmetric-chain decomposition \(\mathscr C\) of
\(2^{[2m]}\).  For every rank-\(M\) top \(U\), let \(X_U\) be the unique
rank-\(m\) member of the chain containing \(U\).  Then

\[
 X_U\subset U,\qquad |U\setminus X_U|=H.                \tag{3.1}
\]

### Lemma 3.1 (SCD entrance injection)

The owners \(X_U\), \(U\in\binom{[2m]}M\), are pairwise distinct.

#### Proof

A symmetric chain contains at most one set at rank (M).  Hence distinct
rank-(M) tops lie on distinct chains.  Those chains also contain at most
one rank-\(m\) set, so their middle members are distinct.  \(\square\)

Order the (H)-set (U\setminus X_U) arbitrarily as

\[
 c_{U,0},\ldots,c_{U,H-1}.
\tag{3.2}
\]

Then (P_0(U)=X_U), so the principal paths start without a collision.

## 4. The layerwise Hall compiler

Suppose the coordinates through (c_{U,t+H-1}) have been chosen, where
(0\le t\le m-1).  Put

\[
 A_U(t)
 =U\setminus\{c_{U,t+1},\ldots,c_{U,t+H-1}\}.
\tag{4.1}
\]

Thus (|A_U(t)|=m+1).  Let (R_U(t)) be the set of coordinates of (U)
not yet used in the word.  It has size (m-t).  Choosing
(x\in R_U(t)) as (c_{U,t+H}) creates exactly

\[
 P_{t+1}(U)=A_U(t)\setminus\{x\}.                        \tag{4.2}
\]

Let \(\mathcal Y_t\) be the owners not used in earlier layers.  Define a
bipartite graph \(\Gamma_t\) with left side the \(C\) current top states,
right side \(\mathcal Y_t\), and

\[
 U\sim A_U(t)-x
 \quad\Longleftrightarrow\quad
 x\in R_U(t),\ A_U(t)-x\in\mathcal Y_t.                 \tag{4.3}
\]

Its exact Hall deficiency is

\[
 \delta_t=C-\nu(\Gamma_t)
 =\max_{S\subseteq\mathcal U}
   \bigl(|S|-|N_{\Gamma_t}(S)|\bigr).
\tag{4.4}
\]

Choose a maximum matching.  On every matched state use the matched
coordinate.  On each of the \(\delta_t\) unmatched states choose any
remaining coordinate; such a coordinate exists because (t<m).

### Theorem 4.1 (integral layer compiler)

After all (m) layers,

\[
 \boxed{Q\le\sum_{t=0}^{m-1}\delta_t.}                  \tag{4.5}
\]

Consequently

\[
 \boxed{
 E_{\rm full}
 \le\sum_{t=0}^{m-1}\delta_t+(H-1)C}                   \tag{4.6}
\]

and

\[
 \boxed{
 W-|\operatorname {supp}\mu^{\rm full}|
 \le W-(m+1)C+\sum_{t=0}^{m-1}\delta_t.}               \tag{4.7}
\]

#### Proof

At layer (t), the matched choices are mutually distinct and lie outside
all earlier layers.  Each unmatched choice adds one occurrence and can
raise principal repeat excess by at most one.  Thus
(Q_{t+1}\le Q_t+\delta_t).  Since (Q_0=0) by Lemma 3.1, induction
proves (4.5).  Equations (4.6)--(4.7) follow from Theorem 2.1.
\(\square\)

This is an actual deterministic reduction, not a fractional assignment:
every matched facet fixes one literal next coordinate of one top order.

## 5. Exact layer overlap and two different Hall cuts

The complete facet star of an ((m+1))-set (A) is

\[
 \partial A=\{A-a:a\in A\}.                             \tag{5.1}
\]

### Lemma 5.1 (two common facets determine the core)

If (A\ne B) are ((m+1))-sets, then

\[
                         |\partial A\cap\partial B|\le1. \tag{5.2}
\]

Hence two candidate rows in one Hall layer can have two distinct common
owners only if their cores (A_U(t)) are equal.

#### Proof

If distinct (m)-sets (Y,Z) are facets of (A), then
(A=Y\cup Z).  Thus if they are also facets of (B), then
\(B=Y\cup Z=A\).  \(\square\)

Equality of cores is necessary, not by itself sufficient, for a
two-cell overlap: the currently remaining deletion sets and the freshness
restriction may be disjoint.

For a fixed core \(A\), let \(\mathcal C_A(t)\) be its current left-state
class.  Write

\[
\mathcal F_A(t)
 =\bigcup_{U\in\mathcal C_A(t)}N_{\Gamma_t}(U)
 \subseteq\partial A.
\tag{5.3}
\]

### Corollary 5.2 (equal-core Hall cut)

For every (A),

\[
 \boxed{
 \delta_t\ge
 \bigl(|\mathcal C_A(t)|-|\mathcal F_A(t)|\bigr)_+.}    \tag{5.4}
\]

More generally the same inequality holds for every subfamily of one
core class, with its own union of allowed facets.

This is just the Hall cut supported on that class.  In particular, (s)
states with the same core and only (d) allowed facets force
\(\delta_t\ge s-d\).

Equal-core classes do not exhaust Hall deficiency.

### Proposition 5.3 (distinct-core linear-star cut)

Let \(Y\) be an \(m\)-set, let \(a_1,\ldots,a_s\) be distinct
coordinates outside \(Y\), and put

\[
 A_i=Y\cup\{a_i\},\qquad R_i=\{a_i\}.                   \tag{5.5a}
\]

The \(s\) candidate rows have distinct cores and each has the singleton
neighbourhood \(\{Y\}\).  Hence every two rows meet in exactly one cell,
but

\[
                         \boxed{\delta_t\ge s-1.}        \tag{5.5b}
\]

These states are compatible with literal last-layer word prefixes.
Choose pairwise distinct \(H\)-sets
\[
 S_i\subseteq[2m]\setminus Y,\qquad a_i\in S_i,
\]
put \(Q_i=S_i-\{a_i\}\) and \(U_i=Y\cup S_i\), place \(Q_i\) in the
final live queue, and leave \(a_i\) as the last unchosen coordinate.
Then the core is \(A_i\) and the unique next facet is \(Y\).  If a fixed
\(H\)-set \(B\subset Y\) begins every word, the entrance owners are
\[
 (Y\setminus B)\cup S_i,
\]
and are pairwise distinct.  This does not assert that an arbitrarily
prescribed collection of entrances occurs in one fixed SCD.

Thus Lemma 5.1 localizes all pairwise intersections of multiplicity at
least two, but a Hall theorem must also exclude one-cell stars and general
unions of such linear overlaps.

The cut is compatible with pairwise distinct entrances before imposing
the full SCD incidence constraints.  Choose an ((m+1))-set (A),
distinct ((H-1))-sets

\[
 Q_j\subseteq[2m]\setminus A,
 \qquad U_j=A\cup Q_j,                                  \tag{5.5}
\]

a (d)-set (R\subset A), and an (H)-set
(B_0\subset A\setminus R).  The entrances

\[
 X_j=U_j\setminus B_0                                  \tag{5.6}
\]

are distinct.  Begin each word with (B_0), then place the coordinates
of (A\setminus(B_0\cup R)), then the coordinates of (Q_j), and leave
the coordinates of (R) last.  At the stage where the (H-1) live queue
is (Q_j), every core is (A) and every candidate owner is in

\[
                         \{A-r:r\in R\}.                 \tag{5.7}
\]

Thus (s>d) such states force deficiency at least (s-d).

This example does **not** prove that one full SCD can be forced to realize
all the displayed pairs ((U_j,X_j)).  Its exact implication is narrower:
the SCD axiom gives the entrance injection, but entrance injection alone
does not propagate the Hall condition through later layers.

A convenient sufficient condition follows from the same bipartite graph.
If

\[
 a_t=\min_U d_{\Gamma_t}(U),\qquad
 b_t=\max_X d_{\Gamma_t}(X),                            \tag{5.8}
\]

then

\[
 \nu(\Gamma_t)\ge \min\{1,a_t/b_t\}\,C,
 \qquad
 \delta_t\le
 \left(1-\min\{1,a_t/b_t\}\right)C.                   \tag{5.9}
\]

Indeed, if (L_0\cup R_0) is a minimum vertex cover, the edges out of
the (C-|L_0|) uncovered left vertices all enter (R_0), so
(a_t(C-|L_0|)\le b_t|R_0|).  Minimize
\((|L_0|+|R_0|)\) under this inequality.  If \(b_t=0\), then
\(\nu(\Gamma_t)=0\) and \(\delta_t=C\), which is handled separately.

## 6. Why (W-o(W)) support is not the needed resolution

Let \(\mathcal F\) be the \(C\) final full frames and form their conflict
graph \(G_{\rm conf}\): two top vertices are adjacent when their owner
decks intersect.  Deleting a vertex cover of this graph leaves an
ordinary-frame matching.

### Lemma 6.1 (repeat excess gives a sufficient pruning bound)

The set of frames participating in at least one repeated owner has size
at most (2E_{\rm full}).  Hence

\[
 E_{\rm full}=o(C)\quad\Longrightarrow\quad
 \tau(G_{\rm conf})=o(C).                               \tag{6.1}
\]

#### Proof

If an owner has multiplicity \(\mu\ge2\), then the number of its incident
frames is \(\mu\le2(\mu-1)\).  Sum this bound over repeated owners; multiple
counting of a bad frame only improves the result.  \(\square\)

For (C=N), retaining (N-o(N)) frames covers

\[
 M(N-o(N))=W-o(W)                                      \tag{6.2}
\]

owners exactly once.  Thus an exact sufficient SCD target is

\[
 \boxed{
 \sum_t\delta_t+Q_{\rm wrap}=o(N),}                    \tag{6.3}
\]

where (Q_{\rm wrap}=E_{\rm full}-Q\) is the actual nonnegative increase
in repeat excess during cyclic closure.  The automatic estimate

\[
 Q_{\rm wrap}\le(H-1)N                                \tag{6.4}
\]

is excellent on the owner scale, because (HN=o(W)), but useless on the
frame-pruning scale, because (HN\gg N).

There is sufficient scalar room for a successful closure.  If the
principal owners were all distinct, their hole set would have size

\[
 W-(m+1)N=(H-1)N+(W-MN).                               \tag{6.5}
\]

The wrap demand is ((H-1)N).  What is missing is a correlated circular
Hall theorem placing almost all wrap owners in these holes while keeping
them mutually distinct.  Histogram or total-capacity equality alone is
not sufficient.

## 7. The one-hole reservoir macro is not an ordinary-frame packet

This section audits the strongest available SCD/rotor batching proposal.
Put

\[
                         s=m-H,\qquad s>2H.              \tag{7.1}
\]

Choose an ordered (2H)-set

\[
 Q=(q_0,q_1,\ldots,q_{2H-1})                            \tag{7.2}
\]

and cyclically order its complement as

\[
 V=(v_0,v_1,\ldots,v_{2s-1}).                           \tag{7.3}
\]

For (i\in\mathbb Z_{2s}), put

\[
 T_i=\{v_i,v_{i+1},\ldots,v_{i+s-1}\},\qquad
 U_i=Q\cup T_i,                                         \tag{7.4}
\]

and give (U_i) the natural cyclic order ((Q,T_i)).

### Lemma 7.1 (exact middle-owner collisions in one macro)

Two owner decks belonging to distinct (U_i,U_j) intersect if and only
if, after a cyclic relabelling,

\[
 j=i+H,                                                  \tag{7.5}
\]

and the omitted (H)-intervals are respectively

\[
 \operatorname {prefix}_H(T_i),\qquad
 \operatorname {suffix}_H(T_{i+H}).                     \tag{7.6}
\]

The two resulting owners are literally equal:

\[
 U_i\setminus\operatorname {prefix}_H(T_i)
 =U_{i+H}\setminus\operatorname {suffix}_H(T_{i+H})
 =Q\cup\{v_{i+H},\ldots,v_{i+s-1}\}.                  \tag{7.7}
\]

There are exactly \(2s\) such duplicated owner labels, equivalently
\(2s\) conflict edges and \(2s\) units of repeat excess; there is no
triple collision.  Every top is incident with two conflict edges.

#### Proof

Suppose (U_i\setminus I=U_j\setminus J), where (I,J) are cyclic
(H)-intervals in the two natural words.  Interchange the rings if
necessary and write (j=i+t), (1\le t\le s).  The top differences are

\[
 \{v_i,\ldots,v_{i+t-1}\}\subseteq I,
 \qquad
 \{v_{i+s},\ldots,v_{i+s+t-1}\}\subseteq J.            \tag{7.8}
\]

Thus (t\le H).  Because (H<|Q|=2H<s), the first interval has the
form suffix of (Q) followed by prefix of (T_i), and the second has the
form suffix of (T_{i+t}) followed by prefix of (Q).  Equality on the
common (Q)-coordinates forces both (Q)-pieces to be empty: they have
length at most (H-t<|Q|), and a nonempty proper prefix and suffix of a
word on distinct coordinates cannot be the same set here.  Therefore

\[
 I=\operatorname {prefix}_H(T_i),\qquad
 J=\operatorname {suffix}_H(T_{i+t}).                   \tag{7.9}
\]

Equality of the remaining proper (v)-intervals forces (t=H), proving
(7.5)--(7.7).  The same classification gives uniqueness and excludes a
third ring.  \(\square\)

Deleting from each ring the owner obtained by omitting
\(\operatorname {suffix}_H(T_i)\) leaves \(2s(M-1)\) pairwise distinct
owners.  This is the valid one-hole reservoir macro.

Restoring the deleted owner does not add a fresh resource: by (7.7) it is
already the retained prefix owner in ring (i-H).  Therefore the full
frame-conflict graph on the (2s) rings has edge set

\[
                         \{\{i,i+H\}:i\in\mathbb Z_{2s}\}. \tag{7.10}
\]

It is the Cayley graph
\(\operatorname {Cay}(\mathbb Z_{2s},\{\pm H\})\).  If
\(g=\gcd(2s,H)\), its components are \(g\) cycles of length \(2s/g\).
Consequently every independent set has size
\[
 g\left\lfloor{s\over g}\right\rfloor\le s.
\tag{7.10a}
\]
We have proved:

### Theorem 7.2 (statewise integral wall)

At most half of the (2s) natural full frames in one reservoir macro can
belong to an ordinary-frame matching.  This remains true even if the
retained owner sets of different macros are globally disjoint.

Thus the implication

\[
 \text{near-matching of one-hole macros}
 \Longrightarrow
 \text{near-matching of full ordinary frames}            \tag{7.11}
\]

is false.  What the macro gives is (W-o(W)) **support with repeat
excess (O(N))**, distributed over a positive fraction of the frames.
That distinction is decisive for bank installation.

## 8. Exact macro degrees and regular-thinning obstructions

Although Theorem 7.2 already blocks the literal full-frame lift, it is
useful to record why selecting the open macros is not a black-box nibble
problem either.  We count directed presentations, including all orders of
(Q).

### Proposition 8.1 (top projection)

Every top has macro degree

\[
 D_T=(2H)!\binom M{2H}(s!)^2.                            \tag{8.1}
\]

For two tops at Johnson distance (d), their codegree is

\[
 D_{TT}(d)=
 \begin{cases}
 (2H)!\binom{M-d}{2H}\,2(d!)^2((s-d)!)^2,
       &1\le d<s,\\[1mm]
 (2H)!(s!)^2,&d=s,\\
 0,&d>s.
 \end{cases}                                             \tag{8.2}
\]

Consequently

\[
 {D_{TT}(d)\over D_T}
 ={2(d!)^2\over(M)_d(s)_d}\quad(1\le d<s),              \tag{8.3}
\]

and

\[
 {\Delta_{TT}\over D_T}={2\over Ms}.                    \tag{8.4}
\]

#### Proof

For a prescribed top, choose and order its (2H)-core, then order the
top's residual (s)-set and its complementary (s)-set as the two blocks
of the (V)-cycle.  This gives (8.1).

For two tops at distance (d<s), their core lies in their
((M-d))-element intersection.  The two residual (s)-windows have Venn
blocks of sizes (d,s-d,d,s-d), which can occur in the two cyclic
orientations and can be internally ordered in
(2(d!)^2((s-d)!)^2) ways.  This proves the first line of (8.2); the
disjoint case (d=s) gives the second.  Division by (8.1) proves (8.3),
whose maximum is at \(d=1\).  \(\square\)

The top uniformity is (k_T=2s), so

\[
 k_T^2{\Delta_{TT}\over D_T}={8s\over M}\longrightarrow8. \tag{8.5}
\]

This is not an artefact of using the full catalogue.  Every macro contains
exactly (2s) distinct Johnson-adjacent top pairs.  Since
(J(2m,M)) has (NMs/2) edges, every top-regular subcatalogue of degree
(D'_T) has average adjacent-pair codegree

\[
                         {2D'_T\over Ms}.                 \tag{8.6}
\]

Thus its maximum has at least the same normalized value as (8.4).

For \(\ell+1<s\) consecutive tops of a macro, the same block count gives
the exact relative codegree

\[
 \boxed{{D_{\ell+1}^{\rm con}\over D_T}
 ={2\over(M)_\ell(s)_\ell}.}                            \tag{8.7}
\]

For every fixed \(\ell\),

\[
 (2s)^{2\ell}{D_{\ell+1}^{\rm con}\over D_T}
 \longrightarrow2\cdot4^\ell.                          \tag{8.8}
\]

So the full finite overlap tower remains critical at its consecutive
top patterns.

### Proposition 8.2 (owner-path density invariant)

Let an owner-regular packet catalogue have owner degree (D_X), and let
every packet contain (K_X) distinct middle owners spanning a
vertex-disjoint Johnson path forest with (b) components.  Then

\[
 \boxed{
 {\Delta_{XX}\over D_X}
 \ge {2(K_X-b)\over K_Xm^2}.}                            \tag{8.9}
\]

#### Proof

Every packet contains at least \(K_X-b\) distinct Johnson edges.  If
\(\mathcal E\) is the packet catalogue, owner regularity gives
\(|\mathcal E|K_X=WD_X\).  Hence the total packet--Johnson-edge incidence
is at least

\[
                         {WD_X\over K_X}(K_X-b).          \tag{8.10}
\]

The middle Johnson graph has (Wm^2/2) edges.  Averaging (8.10) over
them proves (8.9).  \(\square\)

In the one-hole macro,

\[
 K_X=2s(M-1),\qquad b=2s,                               \tag{8.11}
\]

because each deleted ring cycle becomes a path on (M-1) owners.  Thus

\[
 {\Delta_{XX}\over D_X}
 \ge {2(M-2)\over(M-1)m^2}.                             \tag{8.12}
\]

The full top-plus-owner uniformity is

\[
                         k=2sM.                          \tag{8.13}
\]

The catalogue is top- and owner-regular, and double counting gives

\[
 {D_X\over D_T}={(M-1)N\over W}={M-1\over R_H}\le1.    \tag{8.14}
\]

Therefore (D_{\min}=D_X), and

\[
 k{\Delta_2\over D_{\min}}
 \ge {4sM(M-2)\over(M-1)m^2}=4-o(1).                   \tag{8.15}
\]

The same lower bound holds in every owner-regular thinning, by
Proposition 8.2.  Thus batching \(\Theta(m)\) long rotor paths into one
\(\Theta(m^2)\)-resource edge has a nonvanishing linear overlap parameter;
regular sparsification cannot turn it into a sparse growing-rank nibble.

## 9. Exact all-order external overlaps of full frames

We finish by checking that the missing gate is not an unexamined static
higher-overlap tail.  Work in the directed cyclic-order catalogue and put

\[
 B=\binom mH,\qquad D=B\,m!H!.                          \tag{9.1}
\]

Thus \(D\) is the degree of every middle owner.  Fix a frame \(F\), write
\(\mathcal O(F)\) for its owner deck, and define

\[
 A_t^{\rm ext}(F)
 =\sum_{\substack{G:\operatorname {top}(G)\ne
                         \operatorname {top}(F)}}
   \binom{|\mathcal O(F)\cap\mathcal O(G)|}{t}.         \tag{9.2}
\]

For \(\ell\ge1\), define

\[
 C_{\ell,k}
 =\sum_{\substack{g_1+\cdots+g_\ell=k\\g_i\ge1}}
   \prod_{i=1}^{\ell}(g_i!)^2,
 \qquad
 \rho_k={(m)_k\over B(H)_k}.                            \tag{9.3}
\]

### Theorem 9.1 (exact external factorial moments)

One has

\[
 \boxed{A_1^{\rm ext}=MD\left(1-{1\over B}\right).}    \tag{9.4}
\]

For every \(2\le t\le H\), with \(\ell=t-1\),

\[
 \boxed{
 A_t^{\rm ext}
 =2MD\sum_{k=\ell}^{H-1}
       (1-\rho_k){C_{\ell,k}\over(m)_k^2}.}             \tag{9.5}
\]

For \(t>H\), \(A_t^{\rm ext}=0\).

#### Proof

Equation (9.4) follows by rooting at each of the \(M\) owners of \(F\):
there are \(D\) incident directed frames, of which exactly \(m!H!=D/B\)
use the top of \(F\).

For \(t\ge2\), an externally realizable \(t\)-subset of the cyclic deck of
\(F\) has a unique minimal cyclic arc of span \(k<H<M/2\).  If the
successive gaps in that arc are \(g_1,\ldots,g_\ell\), its full common
codegree is

\[
                  {2D\prod_i(g_i!)^2\over(m)_k^2}.       \tag{9.6}
\]

Indeed, root at the left endpoint.  The nested-prefix formula gives
\(\prod_i(g_i!)^2/(m)_k^2\) for one shore orientation in the second
frame, and the globally reversed orientation gives the factor two.
Mixed orientations contradict nesting.  For a fixed gap composition,
there are exactly \(M\) rotations of the unique minimal arc.

Among the frames counted by (9.6), the fraction using the original top is

\[
 { (H-k)!(m-H)!\over(m-k)!}
 ={(m)_k\over B(H)_k}=\rho_k.                           \tag{9.7}
\]

Subtracting (9.7) leaves the external frames.  Sum over the \(M\)
rotations, over \(k\), and over all gap compositions, proving (9.5).

Finally, owner decks on two distinct tops intersect in at most \(H\)
owners: choose a coordinate in one top but not the other; exactly \(H\)
windows of the first deck omit it.  Hence (9.2) vanishes for \(t>H\).
\(\square\)

### Corollary 9.2 (uniform asymptotics)

Uniformly for \(2\le t\le H\),

\[
 \boxed{
 A_t^{\rm ext}
 ={2MD\over(m)_{t-1}^2}
 \left(1+O\!\left({1\over m-H}+{H^2\over(m-H)^2}\right)\right).} \tag{9.8}
\]

#### Proof

The leading composition has \(k=\ell\) and all gaps one.  Moreover

\[
 \rho_k\le\rho_{H-1}={1\over m-H+1}.                    \tag{9.9}
\]

Writing \(k=\ell+j\),

\[
 C_{\ell,\ell+j}
 \le\binom{\ell+j-1}{j}(j+1)!^2.                       \tag{9.10}
\]

Indeed there are the displayed number of weak compositions of (j),
and the product of their shifted factorials is at most ((j+1)!).
After division by the additional (2j) falling-factorial terms, the
ratio of successive majorants is (O(H^2/(m-H)^2)=o(1)).  Summing the
tail proves (9.8).  \(\square\)

In particular

\[
 {A_2^{\rm ext}\over D}={2+o(1)\over m},\qquad
 {A_3^{\rm ext}\over D}={2+o(1)\over m^3}.              \tag{9.11}
\]

For (0\le x=o(\sqrt m)), binomial expansion and (9.8) give

\[
 \boxed{
 \sum_{\operatorname {top}(G)\ne\operatorname {top}(F)}
 \left((1+x)^{J(F,G)}-1-xJ(F,G)\right)
 =(2+o(1)){Dx^2\over m},}                               \tag{9.12}
\]

where \(J(F,G)=|\mathcal O(F)\cap\mathcal O(G)|\).

The leading (t=2) mass is concentrated on adjacent consecutive owner
pairs of (F): their external codegree is

\[
 {2D\over m^2}
 \left(1-{1\over\binom{m-1}{H-1}}\right),              \tag{9.13}
\]

and all nonconsecutive pair shapes contribute (O(D/m^3)) in aggregate.
Thus the static high-order ledger is benign, but the live catalogue may
still concentrate on these adjacent domino cores.

For any retained subcatalogue \(\mathcal E'\), transitivity gives the exact
raw identity

\[
 \sum_{F\in\mathcal E_0}
 \sum_{\substack{G\in\mathcal E'\\
                  \operatorname {top}(G)\ne\operatorname {top}(F)}}
 \binom{J(F,G)}t
 =|\mathcal E'|A_t^{\rm ext}.                            \tag{9.14}
\]

Restricting the outer sum to active frames only decreases the left side.
But (9.14) has no live-density factor.  It therefore does not prohibit a
trajectory from placing much of its surviving mass in a small collection
of equal-core or domino links.

## 10. Final theorem boundary

The following statements are proved and integral.

* One SCD supplies pairwise distinct principal entrance owners.
* Every subsequent coordinate layer is an ordinary maximum matching, and
  its exact accumulated principal-repeat charge is at most
  \(\sum_t\delta_t\).
* The cyclic closure toll is exactly \(H-1\) occurrences per top.
* Equal-core facet classes are the only source of pairwise row
  intersections of size at least two; distinct-core linear stars are a
  separate Hall obstruction.
* The one-hole rotor macro has a literal half-density full-frame conflict
  obstruction.
* Its top projection remains critical under top-regular thinning, and its
  owner projection remains critical under owner-regular thinning.
* The complete static external factorial moments are controlled through
  the entire growing range \(t\le H\).

The literal support target would follow from

\[
                         \sum_t\delta_t=o(W).             \tag{10.1}
\]

The integral ordinary-frame resolution needed for the rectangle bank
would follow from the strictly stronger circular target

\[
 \boxed{
 \sum_t\delta_t+Q_{\rm wrap}=o(N),}                     \tag{10.2}
\]

or, more generally, from an \(o(N)\) vertex cover of the final conflict
graph.  Neither (10.1) nor (10.2) is inferred from the static overlap
table, and neither is proved for a coherent SCD trajectory here.

The next positive theorem must therefore be a genuinely deterministic
SCD/rotor result: it must keep **all** Hall deficiencies summable,
including equal-core clusters and distinct-core linear stars, and
simultaneously reserve the circular wrap facets.  A fixed-uniformity
Pippenger--Spencer citation, a regular thinning of the one-hole macro, or
an aggregate owner histogram does not cross this gate.
