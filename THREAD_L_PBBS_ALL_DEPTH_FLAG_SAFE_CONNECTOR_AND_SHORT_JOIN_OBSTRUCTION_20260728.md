# PBBS all-depth flag-safe connectors and the short binary-join obstruction

Date: 2026-07-28

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Audit status: the \(C_6/C_8\) retained-path argument and the all-depth
collar ledger were independently re-derived. The final audited scopes
include the repeated-trail repair in Corollary 4.4, the odd-cycle
qualification in (1.7), unequal old/new correct-rank collar sizes, the
hypersimplex row shift, and the distinction between an \(O(W)\) upper
bound and an \(\Omega(W)\) obstruction.

## 0. Exact outcome

Put

\[
n=2m+1,\qquad
\Omega=[n],\qquad
O_m=KG(n,m),\qquad
W=\binom{2m+1}{m},\qquad
B=\operatorname{Cat}_m=\frac{W}{2m+1}.
\tag{0.1}
\]

Throughout the new short-switch statements, \(m\ge3\).

There are three logically different questions.

1. **Target supply.** This is already solved for the PBBS factor.
   For every \(1\le q\le m\) and every
   \(S\in\binom{\Omega}{m-q}\), the audited PBBS corridor supplies a
   canonically oriented \(q\)-edge step-two path whose full intersection
   is \(S\), with load at most

   \[
   \binom{2q+1}{q}.
   \tag{0.2}
   \]

   Theorem 2.6 of
   MATH_K15_COMPLEMENT_ANTIPODAL_MIDDLE_LEVELS_REDUCTION_20260728.md
   identifies these step-two intersections with the complements of all
   upper traces. Thus the PBBS input already covers the complete
   all-depth flag tower, not merely the \(q=1\) turn row.

2. **Closed-cycle topology.** A nontrivial two-edge cross splice in
   \(O_m\) is impossible because \(O_m\) is \(C_4\)-free. More sharply,
   no alternating \(C_6\) or \(C_8\) switch joins exactly two untouched
   minimum wreath cycles. Therefore any one-shot closed binary
   connector for two minimum wreaths must delete and insert at least five
   edges. A third-cycle catalyst, a previously merged nonminimum
   component, a compound sequence, or an opened-path splice escapes this
   statement.

3. **Flag, residence, and owner transport.** For any supplied clean
   \(t\)-seam reconnection, the exact depth-\(q\) collar contains at most

   \[
   2tq
   \tag{0.3}
   \]

   old flag occurrences and at most \(2tq\) new occurrences. There is a
   literal background-plus-collar decomposition, so complete support is
   preserved if and only if every target whose old occurrences all lie
   in the deleted collar reappears in the new collar. Summed through
   depth \(H\), the per-sign collar mass is at most

   \[
   tH(H+1),
   \tag{0.4}
   \]

   and the total multiplicity-vector \(\ell_1\) change is at most

   \[
   2tH(H+1).
   \tag{0.5}
   \]

   The distance-\(3/5\) residence audit is the \(H=3\) part of the same
   collar: each new seam has four distance-three and six distance-five
   tests. For growing \(H\), all odd distances
   \(3,5,\ldots,2H-1\) must be checked.

This yields the decisive scale distinction. Opening the at most \(B\)
PBBS cycles and using the proved dominance-staircase charts costs

\[
O(HB)=O(W/\sqrt m)=o(W)
\quad\text{when }H=\Theta(\sqrt m).
\tag{0.6}
\]

Hamiltonizing the factor is therefore not needed for asymptotic
coefficient one. By contrast, \(O(B)\) uncontrolled bounded connectors
have the naive all-depth flag ledger

\[
O(BH^2)=O(W)
\quad\text{at }H=\Theta(\sqrt m).
\tag{0.7}
\]

This is only an \(O(W)\) guarantee, so it does not prove an
\(o(W)\) collar. A neutral or highly overlapping connector may have a
smaller actual cost.

There is also an exact residence invariant. If a surgery deletes
\(J_-\) transition edges and inserts \(J_+\) seams, then

\[
|\nu_H(F')-\nu_H(F)|\le\max\{J_-,J_+\}.
\tag{0.8}
\]

Thus Catalan-many local merges cannot create the missing vanishing
factor in the critical short-residence packing estimate.

For asymptotic coefficient one, a connector has force only as part of a
residence-sharing or residence-improving construction while remaining
flag-neutral or passing the exact support-survival test. Pure component
reduction has no force. For the exact finite compiler, a connector may
also be decisive if it supplies one compatible common owner/Hall
extension.

Finally, the hypersimplex completion theorem removes every rankwise
marginal obstruction whenever its sharp coordinate box inequalities
hold; those inequalities are verified for the Hall-29 depth-two and
depth-three rows. For the exact finite chronology/owner problem, the
missing theorem is not another balancing lemma. It is a **simultaneous
hypersimplex lift**: realize compatible rankwise repairs by one
odd-graph chronology, at all depths at once, while retaining residence,
the upper flag tower, and the common owner assignment. This exact gate
is separate from the asymptotic short-residence gate (10.3).

## 1. The exact all-depth flag object

Let

\[
A_0,A_1,\ldots,A_{L-1},A_0
\tag{1.1}
\]

be an oriented cycle in \(O_m\), and colour its edge \(A_jA_{j+1}\)
by

\[
z_j=\Omega\setminus(A_j\cup A_{j+1}).
\tag{1.2}
\]

The colour is identified with its unique element. The odd-graph
recurrence is

\[
A_{j+1}=A_j^c\setminus\{z_j\},
\qquad
A_{j+2}=A_j-\{z_{j+1}\}+\{z_j\}.
\tag{1.3}
\]

For \(q\ge0\), define the step-two depth-\(q\) flag occurrence

\[
\Phi_j^{(q)}
=\bigcap_{h=0}^{q}A_{j+2h}.
\tag{1.4}
\]

Thus \(\Phi_j^{(q)}\) uses \(q+1\) vertices and \(q\) step-two
transitions.

### Lemma 1.1 (exact deletion formula)

For every oriented odd-graph walk,

\[
\boxed{
\Phi_j^{(q)}
=A_j\setminus
\{z_{j+1},z_{j+3},\ldots,z_{j+2q-1}\}.}
\tag{1.5}
\]

In particular,

\[
|\Phi_j^{(q)}|=m-q
\tag{1.6}
\]

if and only if the \(q\) displayed deletion labels are pairwise
distinct members of \(A_j\).

#### Proof

The second identity in (1.3) says that the transition
\(A_{j+2h}\to A_{j+2h+2}\) deletes \(z_{j+2h+1}\).
An element of \(A_j\) belongs to the full intersection if and only if it
is never deleted during these \(q\) transitions. Any later reinsertion
does not restore membership in the earlier states of the intersection.
This proves (1.5). Exactly \(q\) distinct initial elements must be
removed to give (1.6). \(\square\)

For a Hamilton cycle of odd length, in particular the \(k=15\) cycle of
length \(W=6435\), put \(B_i=A_{2i}\). Since multiplication by two
permutes those cyclic indices,

\[
\Phi_{2i}^{(q)}
=F_i^{(q+1)}
=B_i\setminus
\{z_{2i+1},z_{2i+3},\ldots,z_{2i+2q-1}\},
\tag{1.7}
\]

in the notation of the cited Theorem 2.6. As multisets, the complements
of the upper depth-\(q\) traces are exactly these flags, up to the proved
cyclic shift. Consequently correct-rank support of all
\(\Phi^{(q)}\) is equivalent to upper universality at rank
\(m+1+q\).

After an even-length intermediate join, step two has two parity orbits.
One must retain all starts \(j\), equivalently both step-two orbits.
Using only one parity at such an intermediate state would silently discard
half of the flag occurrences.

### Audited PBBS input

Theorem 21.2 of PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md and its
independent all-\(q\) audit prove that, in the canonical forward PBBS
orientation,

\[
\boxed{
1\le \mu_{P,q}^{\mathrm{corr}}(S)
\le \binom{2q+1}{q}}
\tag{1.8}
\]

for every \(S\in\binom{\Omega}{m-q}\). Here only occurrences satisfying
the exact rank test (1.6) are counted. The upper bound is useful for
local congestion, but it gives no redundancy: load one is allowed. It
is also exponential in \(q\), so it is not by itself an aggregate
Gaussian-window congestion estimate.

## 2. Two-edge joins are impossible

### Lemma 2.1 (common-neighbour bound)

Two distinct vertices of \(O_m\) have at most one common neighbour.
They have one precisely when their intersection has size \(m-1\).

#### Proof

If \(X,Y\in\binom{\Omega}{m}\), a common neighbour is an \(m\)-subset
of

\[
\Omega\setminus(X\cup Y),
\]

whose size is \(1+|X\cap Y|\). For distinct \(X,Y\), this is at most
\(m\). It supports an \(m\)-set precisely when
\(|X\cap Y|=m-1\), and then that \(m\)-set is unique. \(\square\)

Thus \(O_m\) has no \(C_4\).

### Corollary 2.2 (no nontrivial closed two-break)

Delete one edge from each of two vertex-disjoint odd-graph cycles. No
opposite cross-pairing of the four endpoints consists of two new legal
odd-graph edges. Any degenerate legal pairing is the original edge
multiset.

#### Proof

A nondegenerate cross-pairing together with the two deleted edges would
be a \(C_4\), contradicting Lemma 2.1. If endpoints repeat, the resulting
pairing contains an old edge and degree two forces the other old edge as
well. \(\square\)

Hence an opened path splice may be binary, but a nontrivial closed-cycle
join requires at least three deleted edges.

## 3. Wreath orientation and the \(C_6\) binary no-go

A minimum odd cycle has length \(n=2m+1\). If its edge-colour word is

\[
q_0,q_1,\ldots,q_{n-1},
\tag{3.1}
\]

then it is a permutation of \(\Omega\), and its vertices are

\[
V_i=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-1}\}.
\tag{3.2}
\]

Indeed, if \(h_x\) is the number of \(x\)-coloured edges, then every
non-\(x\) edge toggles membership of \(x\), whereas an \(x\)-edge has
two endpoints omitting \(x\). Closure of the odd cycle makes
\(n-h_x\) even, hence every \(h_x\) is positive and odd. Since
\(\sum_xh_x=n=|\Omega|\), all \(h_x=1\).

### Lemma 3.1 (wreath orientation parity)

Orient the \(q_0=\alpha\) edge as \(V_0\to V_1\). Let
\(q_s=\beta\ne\alpha\).

1. If \(\beta\notin V_0\), then \(s\) is even and
   \(\alpha\in V_s\).
2. If \(\beta\in V_0\), then \(s\) is odd and
   \(\alpha\notin V_s\).

#### Proof

Formula (3.2) gives \(\beta\in V_0\) exactly when \(s\) is odd. If
\(s>0\) is even, the residue \(-s\pmod n\) is odd and belongs to
\(\{1,3,\ldots,2m-1\}\), so \(q_0\in V_s\). If \(s\) is odd, it does
not. \(\square\)

Every simple \(C_6\) in \(O_m\), for \(m\ge3\), has after relabelling
the form

\[
\begin{array}{lll}
v_0=K+b,&v_1=L+c,&v_2=K+a,\\
v_3=L+b,&v_4=K+c,&v_5=L+a,
\end{array}
\tag{3.3}
\]

where

\[
\Omega=K\mathbin{\dot\cup}L
\mathbin{\dot\cup}\{a,b,c\},
\qquad |K|=|L|=m-1.
\tag{3.4}
\]

Its cyclic edge-colour word is

\[
a,b,c,a,b,c.
\tag{3.5}
\]

For completeness, the normal form follows directly from the colour
word. For any coordinate, the number of non-coordinate edges around an
even cycle is even, so its edge-colour multiplicity is even. Equal
adjacent colours would give \(v_i=v_{i+2}\). On a simple \(C_6\), every
used colour therefore occurs exactly twice, and exactly three colours
are used. The membership-toggle argument also says that the cyclic
distance between consecutive occurrences of one colour is odd; because
equal adjacent colours are excluded, their two occurrences are
opposite. Every other coordinate
toggles on all six edges and hence belongs to all even or all odd
vertices; these coordinates form the disjoint cores \(K,L\). Each of
the three used colours occurs in one even and one odd vertex, and
disjointness of consecutive vertices forces exactly (3.3).

The alternating matchings are

\[
M^-=\{v_0v_1,v_2v_3,v_4v_5\},
\qquad
M^+=\{v_1v_2,v_3v_4,v_5v_0\}.
\tag{3.6}
\]

### Theorem 3.2 (no binary \(C_6\) join of minimum wreaths)

No alternating \(C_6\) switch joins exactly two untouched minimum
odd-graph wreath cycles.

#### Proof

For a general 2-factor, a \(2+1\) allocation of \(M^-\) can merge two
components under one of two retained-path interlacements. It suffices to
show that the favourable interlacement is impossible for a minimum
wreath.

Suppose \(v_0v_1\) and \(v_2v_3\) lie on the same wreath \(C\), while
\(v_4v_5\) lies on another. Orient

\[
v_0v_1:v_0\longrightarrow v_1.
\]

The first edge colour is \(a\). The colour \(c\) is absent from \(v_0\)
and present in \(v_1\). Lemma 3.1 forces the \(c\)-edge
\(v_2v_3\) to occur with orientation

\[
v_2\longrightarrow v_3.
\]

After deleting these two edges, one retained arc of \(C\) therefore
joins \(v_1\) to \(v_2\). But \(v_1v_2\in M^+\), so the new edge
closes that arc into its own cycle. The other retained arc is attached
to the singly cut wreath, leaving two components. Cyclic relabelling
covers the other choices of the twice-used matching pair. \(\square\)

The same \(C_6\) merges three distinct components when one old matching
edge lies in each. It may also make a binary join after one touched
component has ceased to be a minimum wreath. Theorem 3.2 rules out only
the pristine binary use.

## 4. The \(C_8\) binary no-go

### Lemma 4.1 (normal form of a simple \(C_8\))

After possibly shifting the cycle by one edge, every simple \(C_8\) in
\(O_m\) has the form

\[
A_i-D_i-A_{i+1},
\qquad i\in\mathbb Z_4,
\tag{4.1}
\]

where

\[
A_i=K\cup\{u_i\},\qquad
D_i=B_0\setminus\{u_i,u_{i+1}\},
\tag{4.2}
\]

\[
|K|=m-1,\qquad
B_0=\Omega\setminus K,
\tag{4.3}
\]

and \(u_0,u_1,u_2,u_3\) are distinct elements of \(B_0\).

#### Proof

The four vertices \(A_i\) form a closed Johnson four-walk because
consecutive \(A_i,A_{i+1}\) have the unique common odd-graph neighbour
\(D_i\).

A Johnson four-cycle is of one of the following forms: a common
\((m-1)\)-core clique, a common \((m+1)\)-hull clique, or the standard
rectangle. In the common-hull case all consecutive unions are the same,
so all \(D_i\) coincide, contradicting simplicity. In the common-core
case (4.2) is immediate. In the rectangle case write

\[
\begin{aligned}
A_0&=C+a+c,&A_1&=C+b+c,\\
A_2&=C+b+d,&A_3&=C+a+d,
\end{aligned}
\]

with \(|C|=m-2\). If

\[
L=\Omega\setminus(C\cup\{a,b,c,d\}),
\]

then

\[
D_0=L+d,\quad D_1=L+a,\quad
D_2=L+c,\quad D_3=L+b.
\]

Thus the \(D_i\)-parity has the common core \(L\), and shifting the
cycle gives (4.2). \(\square\)

Put

\[
e_i=A_iD_i,\qquad f_i=D_iA_{i+1}.
\tag{4.4}
\]

Their colours are

\[
\operatorname{col}(e_i)=u_{i+1},
\qquad
\operatorname{col}(f_i)=u_i.
\tag{4.5}
\]

Reversing or shifting the displayed \(C_8\), if necessary, lets us call
the deleted alternating matching \(\{e_0,e_1,e_2,e_3\}\); the other
matching is then \(\{f_0,f_1,f_2,f_3\}\).

### Lemma 4.2 (adjacent and opposite wreath pairs)

If adjacent old edges \(e_i,e_{i+1}\) belong to one minimum wreath, then
\(f_i\) is already an edge of that wreath. Hence a clean alternating
\(C_8\) toggle is impossible.

If opposite old edges \(e_i,e_{i+2}\) belong to one minimum wreath, then
deleting them leaves the endpoint pairing

\[
(A_i,A_{i+2}),\qquad(D_i,D_{i+2}).
\tag{4.6}
\]

#### Proof

Two wreath vertices meeting in \(m-1\) points occur at step-two distance
one in the cyclic-interval order, through their unique common odd-graph
neighbour. The adjacent sets \(A_i,A_{i+1}\) have unique common
neighbour \(D_i\), proving the first assertion.

For \(A_i,A_{i+2}\), the unique common neighbour is

\[
D_*=B_0\setminus\{u_i,u_{i+2}\}.
\]

Thus the minimum wreath contains the retained two-edge path
\(A_i-D_*-A_{i+2}\). The complementary retained arc joins
\(D_i\) to \(D_{i+2}\), so deletion leaves exactly the pairings in
(4.6).
\(\square\)

### Theorem 4.3 (no binary \(C_8\) join of minimum wreaths)

No alternating \(C_8\) switch joins exactly two untouched minimum
odd-graph wreath cycles.

#### Proof

A \(3+1\) distribution contains an adjacent pair on the triply used
wreath and is illegal by Lemma 4.2. The same is true of an adjacent
\(2+2\) distribution.

The only potentially legal distribution is

\[
\{e_0,e_2\}\mid\{e_1,e_3\}.
\]

By Lemma 4.2 its retained endpoint matching is

\[
P=(A_0A_2)(D_0D_2)(A_1A_3)(D_1D_3).
\tag{4.7}
\]

Together with

\[
M^+=(D_0A_1)(D_1A_2)(D_2A_3)(D_3A_0),
\tag{4.8}
\]

this forms two alternating four-cycles, not one. Thus two components
remain. \(\square\)

### Corollary 4.4 (first possible closed binary connector)

For \(m\ge3\), a one-shot closed vertex-preserving 2-factor exchange
joining exactly two untouched minimum wreaths must delete and insert at
least five edges.

#### Proof

Colour the symmetric-difference edges old and new. At every vertex the
old and new degrees agree, so the difference decomposes into alternating
edge-simple closed trails. The graph \(O_m\) is triangle-free for
\(m\ge2\), since
three pairwise disjoint \(m\)-sets would require \(3m\le2m+1\), and it
is \(C_4\)-free by Lemma 2.1.

With at most four old edges there are at most eight
symmetric-difference edges. A repeated-vertex closed trail splits into
at least two simple cycles; triangle- and \(C_4\)-freeness would make
their total length at least ten. Hence every nontrivial trail here is a
simple alternating cycle. There cannot be two of them, since each has
even length at least six. Thus the entire nontrivial difference is one
simple \(C_6\) or \(C_8\). Its old matching meets the two pristine
wreaths and its new matching would join them, contradicting Theorem 3.2
or 4.3. \(\square\)

This is not a no-go for an opened-path splice, a third-component
catalyst, or a sequential compound route.

## 5. General connector topology and colour invariants

Let \(F\) be a simple odd-graph 2-factor. A clean \(t\)-switch deletes
a matching

\[
M^-=\{e_1^-,\ldots,e_t^-\}\subseteq F
\]

and inserts a matching

\[
M^+=\{e_1^+,\ldots,e_t^+\}
\]

on the same \(2t\) ports, with \(M^+\cap F=\varnothing\).
Delete \(M^-\), and pair the endpoints which are joined by the retained
paths. Denote this perfect matching by \(P\).

For perfect matchings \(Q,R\) on the ports, let \(\kappa(Q,R)\) be the
number of alternating cycles in \(Q\cup R\), counting a common pair as
a doubled two-cycle.

### Lemma 5.1 (exact topology criterion)

On the affected region,

\[
c(F')-c(F)=\kappa(P,M^+)-\kappa(P,M^-).
\tag{5.1}
\]

In particular, when exactly two old components are touched, a supplied
binary switch joins them if and only if \(P\cup M^+\) is one
alternating cycle.

#### Proof

Contract each retained path to one matching edge. Before the switch the
affected components are exactly the alternating cycles of
\(P\cup M^-\); afterwards they are those of \(P\cup M^+\).
\(\square\)

### Lemma 5.2 (every alternating switch preserves edge-colour counts)

Suppose \(M^-\cup M^+\) is an alternating even cycle in \(O_m\). For
every \(x\in\Omega\), the two matchings contain the same number of
\(x\)-coloured edges.

#### Proof

At an \(x\)-coloured edge both endpoints omit \(x\). Between consecutive
\(x\)-coloured edges, membership of \(x\) toggles at every intervening
edge. Hence their cyclic edge-index distance is odd. The number of
\(x\)-coloured edges is even, since the total number of membership
toggles around an even cycle is even. Their occurrences therefore
alternate between the two edge parities, proving the claim. \(\square\)

Thus every alternating switch preserves the complete \(z\)-histogram.
If its symmetric difference has several alternating circuits, apply
Lemma 5.2 to each circuit. It also preserves the point degrees of the
turn multidesign. Indeed, if
\(h_F(x)\) is the number of factor edges coloured \(x\), then

\[
\deg_{\rm turn,F}(x)
=\binom{2m}{m}-2h_F(x).
\tag{5.2}
\]

This follows because there are \(\binom{2m}{m}\) factor vertices avoiding
\(x\), and the two endpoints of every \(x\)-coloured factor edge are
exactly the avoiding vertices whose turn omits \(x\) for edge-colour
reasons.

Equation (5.2) is only a marginal invariant. It does not preserve turn
support and, by the hypersimplex completion theorem, no rankwise marginal
argument can settle the chronology problem.

## 6. The all-depth flag collar theorem

Let \(F'\) be obtained from an oriented factor \(F\) by a clean
\(t\)-switch. Orient each retained path as it occurs in \(F'\). For
depth \(q\), let \(\Gamma_q(E)\) be the set of starts whose supporting
\(2q\)-edge directed arc meets an edge of \(E\).

### Theorem 6.1 (exact background-plus-collar decomposition)

After restricting to correct-rank \(m-q\) flags, there are multisets

\[
\mathcal B_q,\qquad \mathcal C_q^-,\qquad\mathcal C_q^+
\]

such that

\[
\mathcal F_q^{\rm corr}(F)
=\mathcal B_q\uplus\mathcal C_q^-,
\qquad
\mathcal F_q^{\rm corr}(F')
=\mathcal B_q\uplus\mathcal C_q^+,
\tag{6.1}
\]

and

\[
|\mathcal C_q^-|\le2tq,
\qquad
|\mathcal C_q^+|\le2tq.
\tag{6.2}
\]

More precisely, the exact collar-start sets are the unions of the
backward \(2q\)-start intervals of the deleted, respectively inserted,
seams. Overlaps only reduce their sizes, and the total number of starts
in the affected components is a second automatic upper bound.

#### Proof

A flag arc avoiding every changed seam lies wholly in one retained path.
If that path is reversed, the same \(q+1\) vertices occur in reverse
order, and their intersection is unchanged. These interior occurrences
give the common background \(\mathcal B_q\).

A directed arc supporting \(\Phi_j^{(q)}\) has exactly \(2q\) ordinary
factor edges. For one seam, at most \(2q\) starts have an arc containing
it. Taking the union over \(t\) seams proves (6.2). Restricting to
correct-rank occurrences can only decrease the count. \(\square\)

Write the multiplicities in (6.1) as

\[
b_q(S),\qquad c_q^-(S),\qquad c_q^+(S).
\]

### Corollary 6.2 (exact support-survival criterion)

If the old depth-\(q\) support is complete, the new support is complete
if and only if

\[
\boxed{
b_q(S)+c_q^+(S)\ge1
\quad
\text{for every }S\in\binom{\Omega}{m-q}.}
\tag{6.3}
\]

Equivalently, with

\[
\mathcal L_q
=\{S:b_q(S)=0,\ c_q^-(S)>0\},
\tag{6.4}
\]

one needs

\[
\boxed{\mathcal L_q\subseteq\operatorname{supp}(c_q^+).}
\tag{6.5}
\]

At most \(2tq\) targets can become holes at depth \(q\).

The stronger identity

\[
c_q^+(S)=c_q^-(S)\quad\text{for every }S
\tag{6.6}
\]

defines a depth-\(q\) flag-neutral connector and preserves the entire
load multiset, not only support.

### Corollary 6.3 (summed collar ledger)

Through depths \(1,\ldots,H\),

\[
\sum_{q=1}^{H}|\mathcal C_q^\pm|
\le tH(H+1),
\tag{6.7}
\]

\[
\sum_{q=1}^{H}
\|\mu_q(F')-\mu_q(F)\|_1
\le2tH(H+1),
\tag{6.8}
\]

and the total number of potentially lost target occurrences is at most

\[
tH(H+1).
\tag{6.9}
\]

#### Proof

Sum (6.2) and use
\(\sum_{q=1}^{H}q=H(H+1)/2\). At each depth, replacing at most \(2tq\)
old correct-rank occurrences and adding at most \(2tq\) new correct-rank
occurrences has load-vector \(\ell_1\) cost at most \(4tq\).
The two correct-rank collar counts need not be equal. \(\square\)

The PBBS cap (1.8) does not imply (6.5). If a target has old load one
and that occurrence lies in \(\mathcal C_q^-\), the cap supplies no
outside witness.

## 7. Exact residence collar

Choose an orientation of a new component. Around an inserted seam edge
of colour \(\gamma\), write

\[
\ldots,p_5,p_4,p_3,p_2,p_1,\gamma,
r_1,r_2,r_3,r_4,r_5,\ldots.
\tag{7.1}
\]

Assume first that every retained piece has at least five edges, so a
distance-five interval crosses at most one new seam. Also assume that
every old factor component already avoids colour equality at distances
three and five.

### Theorem 7.1 (distance-\(3/5\) menu)

The complete distance-three test at this seam is

\[
\boxed{
p_3\ne\gamma,\quad
p_2\ne r_1,\quad
p_1\ne r_2,\quad
\gamma\ne r_3.}
\tag{7.2}
\]

The complete distance-five test is

\[
\boxed{
p_5\ne\gamma,\quad
p_4\ne r_1,\quad
p_3\ne r_2,\quad
p_2\ne r_3,\quad
p_1\ne r_4,\quad
\gamma\ne r_5.}
\tag{7.3}
\]

Taken over all inserted seams, these inequalities are necessary and
sufficient for distance-\(3/5\) avoidance. No comparison outside the
radius-five collars changes.

#### Proof

A comparison at forward distance \(d\) which crosses the displayed seam
has endpoints

\[
(p_d,\gamma),(p_{d-1},r_1),\ldots,
(p_1,r_{d-1}),(\gamma,r_d).
\]

This gives (7.2)--(7.3). Every comparison which crosses no new seam lies
inside a retained path and is inherited, possibly reversed, from an old
cycle. Equality is invariant under reversal. \(\square\)

Thus one seam has four distance-three and six distance-five tests and an
eleven-edge collar. A \(t\)-seam connector has at most

\[
4t,\qquad6t,\qquad11t
\tag{7.4}
\]

such tests/positions, with overlaps identified. If retained pieces are
short, the individual lists can overlap or an interval can cross two
seams; the exact test is then the union of all radius-five collar
comparisons. The obstruction remains local, but the seams are not
independent.

For depth \(H\), distance \(2r-1\) contributes \(2r\) comparisons per
seam. Distance one is automatic in a simple factor. Hence the number of
nontrivial raw residence tests per separated seam is

\[
\sum_{r=2}^{H}2r
=H(H+1)-2,
\tag{7.5}
\]

all supported in the radius-\((2H-1)\) collar.

Excluding only distances three and five certifies correct collar ranks
only through \(q=3\). Growing all-depth flag transport requires every odd
distance through \(2H-1\), or the equivalent exact rank test (1.6).

This is a residence-depth law, not a divisor law. In particular the
audited \(k=21\) depth-three target again requires distances three and
five, not three and seven, exactly as recorded in
MATH_ODD_DISTANCE_RESIDENCE_AUDIT_K9_K21_20260728.md.

### Theorem 7.2 (seam-Lipschitz short-residence packing)

Let \(F'\) be obtained from a cycle/path cover \(F\) by deleting
\(J_-\) transition edges, retaining the resulting path interiors in
either orientation, and adding \(J_+\) seam edges. Let \(\nu_H(F)\) be
the maximum size of a family of pairwise transition-edge-disjoint
positive coordinate residence intervals of length at most \(H\). Then

\[
\boxed{
|\nu_H(F')-\nu_H(F)|\le\max\{J_-,J_+\}.}
\tag{7.6}
\]

#### Proof

Let \(\mathcal U\) be the interval family lying wholly in retained path
interiors. It is common to \(F\) and \(F'\), because reversal preserves
the underlying transition-edge set of every coordinate run. Every old
interval outside \(\mathcal U\) contains a deleted edge. In an
edge-disjoint packing, charging each such interval to one contained
deleted edge is injective, so

\[
\nu_H(\mathcal U)\le\nu_H(F)
\le\nu_H(\mathcal U)+J_-.
\]

The identical argument with the new seams gives

\[
\nu_H(\mathcal U)\le\nu_H(F')
\le\nu_H(\mathcal U)+J_+.
\]

Subtract the two intervals. \(\square\)

Consequently \(O_A(B)\) local seams at
\(H_A=\lceil A\sqrt m\rceil\) change \(\nu_{H_A}\) by only
\(O_A(B)=o_A(B\sqrt m)\). They cannot turn a genuinely critical
\(\Theta_A(B\sqrt m)\) packing into the strict little-oh packing needed
for coefficient one. This is stronger than the statement that a pure
merge need not improve residence.

## 8. The explicit \(C_6\) turn menu

Although Theorem 3.2 excludes a binary \(C_6\) join of two pristine
wreaths, the same switch may act on general or previously merged
components. Its \(q=1\) collar is useful to record.

In the normal form (3.3), let \(d_i\) be the colour of the unchanged
factor edge at \(v_i\). Legality together with the clean condition
\(M^+\cap F=\varnothing\) gives

\[
d_0,d_2,d_4\in L,\qquad
d_1,d_3,d_5\in K.
\tag{8.0}
\]

Use the abbreviation

\[
(R-x)+y:=(R\setminus\{x\})\cup\{y\}.
\tag{8.0a}
\]

The six old and new turn colours are

\[
\begin{array}{c|c|c}
i&T_i^-&T_i^+\\ \hline
0&(L-d_0)+c&(L-d_0)+a\\
1&(K-d_1)+b&(K-d_1)+a\\
2&(L-d_2)+b&(L-d_2)+c\\
3&(K-d_3)+a&(K-d_3)+c\\
4&(L-d_4)+a&(L-d_4)+b\\
5&(K-d_5)+c&(K-d_5)+b.
\end{array}
\tag{8.1}
\]

Every turn outside these six ports is unchanged.

On the \(L\)-shore, the number of old turns which cancel against new
turns is

\[
\mathbf1_{d_0=d_2}
+\mathbf1_{d_2=d_4}
+\mathbf1_{d_4=d_0}.
\tag{8.2}
\]

On the \(K\)-shore it is

\[
\mathbf1_{d_1=d_5}
+\mathbf1_{d_3=d_1}
+\mathbf1_{d_5=d_3}.
\tag{8.3}
\]

Therefore each shore has exactly one of three local outcomes:

\[
\begin{array}{c|c|c}
\text{held-colour pattern}&
\text{locally retained turns}&
\text{old/new replacements}\\ \hline
\text{all equal}&3&0\\
\text{exactly two equal}&1&2\\
\text{all distinct}&0&3.
\end{array}
\tag{8.4}
\]

For a \(2+1\) use on two minimum wreaths, the twice-used wreath forces

\[
d_0\ne d_2,\qquad d_1\ne d_3
\tag{8.5}
\]

after cyclic relabelling. Hence at most one cancellation occurs on each
shore, and the total local loss/gain menu is

\[
\boxed{4,\ 5,\ \text{or }6.}
\tag{8.6}
\]

Here \(4,5,6\) is the one-sided number of old local occurrences
replaced, equivalently the number of new local occurrences introduced.
The corresponding local multiplicity-vector \(\ell_1\) changes are
\(8,10,12\). These are not global support-hole counts, because outside
occurrences may survive.

This does not contradict Theorem 3.2: the corresponding switch is a
two-component rerouting, not a join. In a global factor, complete turn
support survives exactly when every old collar target absent from the
new six turns has another occurrence outside the six ports. This is
Corollary 6.2 at \(q=1\).

## 9. Why rankwise balancing is no longer a gate

MATH_HYPERSIMPLEX_MARGINAL_COMPLETION_AND_CHRONOLOGY_GATE_20260728.md
proves the following. If the forced excess-degree vector at depth \(q\)
satisfies

\[
0\le\gamma_{q,x}\le e_q,
\tag{9.1}
\]

then it decomposes into \(e_q\) uniform blocks. Adding one copy of every
rank-\((m+1-q)\) target gives a hole-free multiset with exactly the
actual trace point degrees, and symmetric two-block exchanges connect
the rankwise designs. In the present odd-graph notation this row aligns
with \(\Phi^{(q-1)}\), not \(\Phi^{(q)}\).

At the frozen \(k=15\) Hall-29 state,

\[
\gamma_{2,x}\in[568,574]\subset[0,1428],
\tag{9.2}
\]

\[
\gamma_{3,x}\in[1138,1147]\subset[0,3429].
\tag{9.3}
\]

Thus neither the observed depth-two nor depth-three holes are forced by
point marginals or by the rankwise exchange lattice.

To state the remaining lift exactly in the chronology notation of the
hypersimplex theorem, for \(q\ge2\) let

\[
\mathcal Z_q(\gamma_q)
=\left\{M:
\begin{array}{l}
M\text{ is a multiset of }W-q\text{ rank-}(r-q)\text{ blocks},\\
\binom{[k]}{r-q}\subseteq M,\\
\deg_M(x)=\binom{k-1}{r-q-1}+\gamma_{q,x}\qquad(x\in[k])
\end{array}
\right\}.
\tag{9.4}
\]

The hypersimplex theorem says exactly that every
\(\mathcal Z_q(\gamma_q)\) is nonempty under (9.1). The product cannot
start at \(q=1\): in the central case \(k=2r-1\), the first trace row
has \(W-1\) occurrences but
\(\binom{k}{r-1}=W\) targets, so \(e_1=-1\) and a zero-hole first row is
impossible. Fix its actual multiset \(M_1^{\mathrm{given}}\). For
\(2\le H\le d\) and a resident chronology \(T=(T_i)\), define the
remaining simultaneous trace image by

\[
\Psi_{2:H}(T)
=\left(
\left\{\!\left\{\bigcap_{h=0}^{q}T_{i+h}:0\le i<W-q
\right\}\!\right\}
\right)_{q=2}^{H}.
\tag{9.5}
\]

The doubled braces denote a multiset, so no repeat information is
discarded. In the linear equations below, a multiset is identified with
its multiplicity vector.

The exact missing assertion is an intersection statement, not a degree
statement:

\[
\boxed{
\Psi_{2:H}(\mathcal C_{M_1^{\mathrm{given}};
\,\mathrm{resident,flag,owner}})
\cap\prod_{q=2}^{H}\mathcal Z_q(\gamma_q)\ne\varnothing}
\tag{9.6}
\]

with the evident row-index shift when translated to the odd-graph flags
\(\Phi^{(q-1)}\). Here
\(\mathcal C_{M_1^{\mathrm{given}};
\,\mathrm{resident,flag,owner}}\) denotes the
literal chronology fibre with that prescribed first row and the
prescribed boundary data (and hence the same \(\gamma_q\)), restricted
to chronologies which pass the residence tests, preserve the required
upper-flag occurrences, and admit one common integral owner extension.
Omitting the last condition gives the exact unlabelled zero-hole lift
for rows \(q\ge2\); retaining it gives the exact finite owner-compatible
compiler problem. For asymptotic coefficient one, (9.6) is sufficient
but stronger than necessary: it is enough to reach the corresponding
product with total compiler-weighted defect \(o(W)\).

The exact safe-de-Bruijn theorem makes (9.6) nonformal. Let
\(D_H(k,r)\) be the digraph of two-sided \(H\)-safe Johnson windows, let
\(C_0\) be its middle-owner projection, let \(C_q\) be its depth-\(q\)
intersection projection, and let \(\sigma_q(v)\) be the terminal-suffix
correction. Before adding the upper and owner decorations, the lift is
equivalent to the existence of states \(u,v\) and an integral
nonnegative arc vector \(z\) such that

\[
\begin{aligned}
\partial z&=\mathbf1_u-\mathbf1_v,\\
C_0z+\sigma_0(v)&=\mathbf1_{\binom{[k]}r},\\
C_1z+\sigma_1(v)&=M_1^{\mathrm{given}},\\
C_qz+\sigma_q(v)&\in\mathcal Z_q(\gamma_q)
&& (2\le q\le H),
\end{aligned}
\tag{9.7}
\]

and the positive arc support is one Euler component. Upper-union rows
add their analogous projections. When all relevant controller/cell
spans are bounded by \(h\), exact trace ownership is represented by the
finite-memory decorated graph \(D_{H,h}^{\rm dec}\); without such a
bound one must use the corresponding full finite-memory enlargement.
Its decorated arcs encode one controller skeleton and require its
eligible interval-union catalogue to contain every residual target.
Thus the simultaneous lift is an integral connected-flow problem;
nonemptiness of each separate \(\mathcal Z_q\) does not imply (9.7),
and the coloured-Euler cuts give explicit adjacent-row obstructions.

This also locates the present connector result inside the exact lift
lattice. With endpoints fixed, a signed connector change is a literal
simultaneous linear lift precisely when it is the projection of an
integer circulation \(\eta\) satisfying

\[
\partial\eta=0,\qquad C_0\eta=0,\qquad C_1\eta=0,\qquad
z+\eta\ge0,
\tag{9.8}
\]

with connected resulting support. The condition \(C_1\eta=0\) is what
keeps \(M_1^{\mathrm{given}}\) fixed. Under the lower-row/odd-graph
identification,

\[
C_q\eta=\mathcal C_{q-1}^+-\mathcal C_{q-1}^-.
\tag{9.9}
\]

The analogous complemented upper-union projection at middle depth \(q\)
gives the depth-\(q\) odd-graph collar. Thus (6.5), at the corresponding
odd-graph depth, is the targetwise positivity test for a *supplied*
sparse chronology lift; it does not produce the circulation, prove the
Euler cuts, or supply the decorated owner extension.

The collar criterion (6.5) is instead simultaneous and chronological.
One must choose new collar flags at every depth so that they arise from
one common edge-colour word and satisfy the nested identities (1.5).
Even if a separate two-block repair exists at every rank, no existence
theorem lifts those repairs simultaneously to one odd-graph cycle while
preserving residence and the upper flag tower. The exact finite formula
also requires one common owner/Hall realization.

This is the simultaneous hypersimplex-lift gate. No additional rankwise
balancing lemma can replace it.

## 10. Topology versus coefficient one

The PBBS factor has at most \(B\) components. Opening them and using the
audited dominance-staircase/collar construction costs \(O(H)\) per cut,
and hence

\[
O(HB)=O(HW/m).
\tag{10.1}
\]

At \(H=\Theta(\sqrt m)\), this is \(O(W/\sqrt m)=o(W)\). Therefore
ordinary connector topology is already cheap enough for the asymptotic
coefficient-one theorem.

The authoritative linear dominance-staircase ledger is

\[
\boxed{
L_H\le W+2HB+2(5H-1)\nu_H(P_m).}
\tag{10.2}
\]

For \(H_A=\lceil A\sqrt m\rceil\), its sharp remaining sufficient gate
is

\[
\nu_{H_A}(P_m)=o_A(B\sqrt m).
\tag{10.3}
\]

By Theorem 7.2, \(O_A(B)\) local connector seams change the left side
of (10.3) by only \(O_A(B)=o_A(B\sqrt m)\). Hence such a
Hamiltonization preserves whether the packing is subcritical at this
scale; it cannot by itself manufacture (10.3).

Suppose instead that a Hamiltonization uses bounded switches with a total
of \(T=O(B)\) inserted seams. Corollary 6.3 gives the uncontrolled
all-depth ledger

\[
O(TH^2)=O(BH^2).
\tag{10.4}
\]

At Gaussian depth the generic bound is only \(O(W)\), so it does not
prove \(o(W)\). A shared literal seam chart may reuse letters across
depths, and a neutral or highly overlapping connector may cost much
less; topology alone proves no such reuse and no owner assignment.

Accordingly, an asymptotically useful connector theorem must prove both:

1. flag neutrality, or the exact survival condition (6.5) using genuine
   outside PBBS occurrences; and
2. a residence-sharing mechanism proving (10.3).

By Theorem 7.2, Catalan-many local joins cannot create the required
vanishing factor from a genuinely critical seed. For the exact finite
problem there is a different possible payoff: the connector may supply
one common owner/Hall extension and a literal dominance-staircase
compiler, again while passing the flag-survival ledger.

For the exact finite formula, even \(O(HB)\) is a real palette/owner toll,
so the owner-compatible version remains relevant. For asymptotic
coefficient one, merely turning the PBBS factor into one Hamilton cycle
does not address the true gate.

The published GMN/MNW merge tree does not supply the hypotheses above.
The audited source comparison proves that it starts from the distinct
lexical Middle-Levels factor \(F_{\rm lex}\), not from
\(F_{\rm PBBS}\). Its dynamically flippable hexagons therefore cannot be
transferred to PBBS without a new factor-to-factor connector or a direct
PBBS flippability theorem.

## 11. Conditional connector theorem

### Theorem 11.1 (flag-safe connector sequence)

Let \(F_0\) be an odd-graph factor whose correct-rank flag layers through
depth \(H\) have the complete PBBS support, and let

\[
F_0,F_1,\ldots,F_s
\tag{11.1}
\]

be a sequence of clean dynamically alternating switches. Assume that
\(F_0\) is residence-safe through depth \(H\). In a PBBS application,
all bad intervals not represented in \(F_0\) must already have been
quarantined by the declared cut/repair architecture. Assume at every
step:

1. the desired component change passes the exact topology criterion
   (5.1);
2. every new odd-distance comparison through \(2H-1\) passes the seam
   test of Section 7;
3. for every \(1\le q\le H\), the collar satisfies the exact support
   condition (6.5).

Then every \(F_j\) is residence-safe through depth \(H\), and every
correct-rank flag layer through depth \(H\) has complete support. If the
stronger neutrality identity (6.6) holds at every step, all those flag
load multisets are exactly those of \(F_0\).

If, in addition, the inserted seams and nested flags are supplied with
one compatible integral owner/Hall assignment and literal seam charts,
then the sequence compiles without any unrecorded target or owner loss.

#### Proof

Induct on \(j\). The topology condition keeps a literal 2-factor.
Section 7 confines every possible new short return to a tested seam
collar. Theorem 6.1 leaves a common background at every depth, and
Corollary 6.2 is necessary and sufficient for the new collar to preserve
support. Under (6.6), the old and new collar multisets agree exactly.
The final assertion is precisely the additional integral compiler
hypothesis; it is not inferred from set support. \(\square\)

Theorem 11.1 is a conditional composition theorem, not an existence
theorem for the switches or owner assignments. Without the initial
residence-safe hypothesis, the same proof says only that no new
violation is created at a tested seam; old violations lying inside
retained PBBS pieces persist.

## 12. Exact boundary

Proved here:

1. the exact odd-graph step-two flag formula and its correct-rank test;
2. no nontrivial closed two-break in \(O_m\);
3. no alternating \(C_6\) or \(C_8\) binary join of two untouched
   minimum wreaths;
4. the five-cut lower bound for a one-shot closed binary
   connector;
5. exact topology and edge-colour invariants for any supplied clean
   alternating switch;
6. the background-plus-collar decomposition at every depth, with
   constants \(2tq\), \(tH(H+1)\), and \(2tH(H+1)\);
7. the necessary-and-sufficient support-survival condition;
8. the complete distance-\(3/5\) menu and its growing-\(H\) extension;
9. the seam-Lipschitz invariant for the short-residence packing;
10. the explicit \(C_6\) turn outcome menu; and
11. the conditional flag-safe connector theorem.

Imported audited inputs:

1. complete PBBS support at every depth with cap
   \(\binom{2q+1}{q}\);
2. the exact equivalence between the odd-graph flags and the full upper
   tower;
3. linear dominance-staircase seam cost \(O(H)\);
4. hypersimplex rankwise zero-hole completion; and
5. the exact coloured-Euler/safe-de-Bruijn flow characterization of a
   simultaneous chronology lift.

Not proved:

1. a five-cut or larger binary connector between two minimum wreaths;
2. a dynamically flippable PBBS merge tree;
3. simultaneous all-depth flag survival for any such merge tree;
4. the strict little-oh PBBS residence bound (10.3), or a nonlocal
   residence-sharing surgery which proves it;
5. the simultaneous hypersimplex lift to one chronology; or
6. a common owner/Hall extension for the exact finite compiler.

The remaining boundaries are different in the two scopes. For
asymptotic coefficient one, the sharp gate is the strict little-oh
short-residence estimate (10.3); connector topology cannot create it.
For the exact finite compiler, the sharp gate is the
chronology-sensitive simultaneous hypersimplex lift of the complete
PBBS flag tower together with one common owner/controller extension.
Neither gate is a component-count, point-margin, or separate rankwise
design problem.
