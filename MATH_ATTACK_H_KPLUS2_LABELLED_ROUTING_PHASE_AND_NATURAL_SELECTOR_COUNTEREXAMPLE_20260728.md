# Lane H: phase conservation and a natural-selector counterexample for the \(k\mapsto k+2\) lift

Date: 2026-07-28

## 0. Verdict

The general simultaneous labelled-routing theorem is not proved here.
The phase question and the canonical endpoint-priority lift are resolved
as follows.

1. Phase conservation is a genuine obstruction to a partition into
   owner-disjoint local three-vertex packets. It is not an obstruction to
   a fused chronology: the local paths can share their \(X,Y\) endpoints,
   producing an exact path forest.
2. If the omitted \(U\)-indices are the stable Catalan leave of size \(b\),
   the canonical complementary-phase switch bank has exactly \(2b\)
   missing and \(2b\) duplicate cross-state occurrences. Its repair is
   necessarily a Catalan-sized global defect circulation.
3. On the exact stored \(k=11\) carrier, rooted at the cut used by its exact
   compiler, the first-occurrence Catalan selector traps an old-coordinate
   run of length three. Since \(d(13)=3\), the \(11\to13\) lift requires
   internal runs of length at least four. The natural selector therefore
   fails residence before the lower compiler is considered.
4. Independently, the first-occurrence \(U\)-selector misses an explicit
   empty-signature rank-eight target and hence violates \((US^*)\). The
   last-occurrence selector has a second explicit missed target.
5. The first \(A\)-selector retains only \(158\) of the \(165\) protected
   adjacent-pair colours. A scalar boundary count alone would permit these
   seven holes, but their endpoint supports cannot fit into two rank-five
   cores. Hence even the linear common lower compiler fails in this strict
   first-selector architecture.

The exact \(k=11,12,13,14\) words do not support a fixed local priority
rule. Their common invariant is the finished integral datum
\((T,\phi)\): one global chronology, one common lower pin injection, and
the four simultaneous flat conditions \(F1\)--\(F4\). The surviving gate
must permit global rethreading or genuinely adaptive native representatives,
and then solve one fresh common pin table.

## 1. The local diamond and its two phases

Let \(k=2r-1\), and let

\[
 T_0,T_1,\ldots,T_{W-1},\qquad W=\binom{2r-1}{r},
\]

be a cyclic Johnson carrier; indices in this section are modulo \(W\).
Put

\[
 C_i=T_i\cap T_{i+1},\qquad
 T_i=C_i\cup\{u_i\},\qquad
 T_{i+1}=C_i\cup\{v_i\}.
\]

After adjoining \(x,y\), the local six-state rectangle at old edge \(i\)
contains

\[
\begin{aligned}
 A_i&=C_i\cup\{x,y\},
 &U_i&=C_i\cup\{u_i,v_i\}=T_i\cup T_{i+1},\\
 X_i&=T_i\cup\{x\},
 &Y_i&=T_i\cup\{y\},\\
 X_{i+1}&=T_{i+1}\cup\{x\},
 &Y_{i+1}&=T_{i+1}\cup\{y\}.
\end{aligned}
\]

Its two disjoint three-vertex paths are

\[
 P_i^A=Y_i-A_i-X_{i+1},
 \qquad
 P_i^U=X_i-U_i-Y_{i+1}.
\tag{1.1}
\]

Each pair is locally first-shadow perfect. The issue is exact composition
of the shared \(X,Y\) owners.

### Theorem 1.1 (exact packet-phase conservation)

Regard the chosen paths as owner-disjoint packets, so two packet occurrences
of the same endpoint count as a duplicate. Choose exactly one path in
(1.1) at each old edge, and put \(s_i=0\) for \(P_i^A\) and \(s_i=1\)
for \(P_i^U\). Then

\[
 \boxed{
 m(X_j)=s_j+1-s_{j-1},\qquad
 m(Y_j)=1-s_j+s_{j-1}.}
\tag{1.2}
\]

Every \(X_j,Y_j\) occurs exactly once if and only if
\(s_j=s_{j-1}\) for every \(j\). Hence \(s\) is constant on each
connected old carrier cycle.

#### Proof

\(X_j\) is the first endpoint of \(P_j^U\) and the last endpoint of
\(P_{j-1}^A\), giving the first formula. Similarly, \(Y_j\) is the first
endpoint of \(P_j^A\) and the last endpoint of \(P_{j-1}^U\), giving the
second. Both multiplicities equal one precisely when
\(s_j=s_{j-1}\). Connectivity gives constancy. \(\square\)

Constant \(A\)-phase omits the \(U\)-centres, while constant \(U\)-phase
omits the \(A\)-centres. Both sectors are nonempty in every nondegenerate
lift. Thus phase conservation genuinely blocks the strict edge-local
switch bank. This bank is not by itself a full child factor: it chooses
only one local centre per old edge. The theorem says that this bank cannot
be mixed while retaining exact cross ownership; it does not forbid a
supplementary nonlocal packet system.

### Theorem 1.2 (independent both/none choices do not escape)

In the same owner-disjoint packet model, let
\(a_i,u_i\in\{0,1\}\) independently indicate whether \(P_i^A,P_i^U\)
are used; both or neither may be chosen. Exact use of every cross state is
equivalent to

\[
 u_j+a_{j-1}=1,\qquad a_j+u_{j-1}=1.
\tag{1.3}
\]

Consequently

\[
 a_j=a_{j-2},\qquad u_j=1-a_{j-1}.
\tag{1.4}
\]

Thus the selection is two-periodic. On an odd carrier cycle it is constant;
on an even cycle the only additional possibilities alternate between
choosing both local paths and choosing neither. If, as in the rainbow
diamond lift, the \(A_i\) are pairwise distinct and comprise the required
\(A\)-sector, this independent local bank cannot be a full child factor:
every \(A_i\) forces \(a_i=1\), and then (1.3) forces \(u_i=0\) for all
\(i\), omitting every required \(U\)-owner.

#### Proof

The two equations in (1.3) are the exact \(X_j,Y_j\) multiplicity
conditions. Substituting \(u_j=1-a_{j-1}\) into the shifted second equation
gives \(a_j=a_{j-2}\). The cycle classification follows. The final
assertion uses the fact that \(A_i\) occurs in this local bank only in
\(P_i^A\). \(\square\)

The word “multiplicity” in Theorems 1.1--1.2 is packet multiplicity.
Two packets meeting at the same endpoint need not duplicate the physical
owner; they may be fused there. That distinction gives the exact escape.

### Theorem 1.3 (endpoint-sharing fusion)

Assume the \(A_i\) are distinct. Let \(I\subseteq\mathbb Z_W\) select
distinct \(U_i\)-owners. Form the graph

\[
 \mathcal F(I)=
 \bigcup_{i\in\mathbb Z_W}P_i^A
 \ \cup\
 \bigcup_{i\in I}P_i^U,
\tag{1.5}
\]

where coincident \(X,Y\) endpoints are identified as single physical
vertices. Then \(\mathcal F(I)\) uses every \(A_i,X_i,Y_i\) exactly once
and every selected \(U_i\) exactly once. Its degrees are

\[
\begin{aligned}
\deg(A_i)&=2,&\deg(U_i)&=2,\\
\deg(X_j)&=1+\mathbf 1_I(j),&
\deg(Y_j)&=1+\mathbf 1_I(j-1).
\end{aligned}
\tag{1.6}
\]

The graph is a disjoint union of paths and cycles. Its path endpoints are

\[
 \{X_z,Y_{z+1}:z\in I^c\}.
\tag{1.7}
\]

The full indexed graph \(\mathcal F(\mathbb Z_W)\) has
\(\gcd(W,2)\) cycles, corresponding to the \(+2\) index orbits. If
\(I^c\) meets every such orbit, then \(\mathcal F(I)\) is a path forest
with exactly \(|I^c|\) components. In general it has
\(|I^c|\) path components together with one residual cycle for every
\(+2\) orbit missed by \(I^c\).

#### Proof

Every \(A_i\)-path supplies the distinct vertices \(Y_i,A_i,X_{i+1}\).
Adding \(P_i^U\) identifies its endpoints with the already present
\(X_i,Y_{i+1}\) and adds only the new centre \(U_i\). This proves exact
ownership and (1.6). Traversing an \(U_i\)-path followed by an
\(A_{i+1}\)-path advances the index from \(i\) to \(i+2\), proving the
\(\gcd(W,2)\)-cycle decomposition. Deleting the two incident edges and
centre \(U_z\) cuts its \(+2\) cycle at the two vertices in (1.7). A cycle
with \(c>0\) cuts becomes \(c\) paths; a cycle with no cut remains a
cycle. Summing over the \(+2\) orbits proves the claim. \(\square\)

Thus phase conservation does not kill the general edge-local fused
chronology. It kills only the owner-disjoint packet interpretation. The
actual gates are now exactly the coloured \(A\)-choice, residence,
\(U\)-provider chronology, and the common pin table.

The fusion (1.5) is not itself an OR compiler: every \(A_i\) is still
isolated between one \(Y\)- and one \(X\)-state, and every selected \(U_i\)
is isolated between one \(X\)- and one \(Y\)-state. Hence it has no native
\(AA\) or \(UU\) edge and retains the length-two new-coordinate runs. It
settles ownership/phase only.

### Corollary 1.4 (exact Catalan packet-defect ledger)

Suppose the desired \(U\)-representative set is
\(I\subset\mathbb Z_W\), with \(|I^c|=b\), and \(I^c\) is stable in
the index cycle. Put \(s_i=\mathbf 1_I(i)\). Then there are exactly \(2b\)
phase boundaries. At every \(0\to1\) boundary one \(X\)-state is doubled
and the corresponding \(Y\)-state is omitted; at every \(1\to0\)
boundary the roles reverse. Therefore

\[
 \boxed{
 \text{missing cross-occurrence mass}=2b,\qquad
 \text{duplicate cross-occurrence mass}=2b.}
\tag{1.8}
\]

Equivalently, the total \(L^1\) deviation from exact ownership is \(4b\).

#### Proof

Every member of the stable set \(I^c\) is an isolated zero of the cyclic
binary word \(\mathbf 1_I\), and contributes one entering and one leaving
phase boundary. Formula (1.2) gives one omission and one duplication at
each boundary. \(\square\)

More explicitly, for \(z\in I^c\), the missing labels are
\(X_z,Y_{z+1}\) and the duplicated labels are \(Y_z,X_{z+1}\).
Stability makes these labels distinct for different \(z\).

This complement-phase bank contains only \(b\) local \(A\)-paths, not the
full Catalan \(A\)-forest of \(W-b\) edges. Equation (1.8) is therefore
the exact cross-owner cost of the obvious local switch assignment, not a
complete child-factor ledger.

For the odd diamond lift,

\[
 b=C_r=\frac{1}{r+1}\binom{2r}{r}.
\]

This is \(o(W)\), so (1.8) is not
an asymptotic obstruction to coefficient one. It is the exact circulation
that a positive global construction must carry. Theorem 1.2 shows that
uncorrelated both/none choices are still insufficient. Open endpoints,
off-edge endpoints, or larger correlated rectangles remain possible.

## 2. A general native-spine residence obstruction

Let

\[
 \widehat C=(C_0,C_1,\ldots,C_{M-1})
\]

be a path of equal-rank sets. Colour the native edge
\(e_i=C_iC_{i+1}\) by

\[
 \rho_i=C_i\cap C_{i+1}.
\]

A native exact-colour forest chooses one occurrence of every edge colour
and retains every chosen edge as a literal consecutive \(AA\) adjacency.

### Theorem 2.1 (singleton-hazard obstruction)

Fix a coordinate \(z\) and integers \(a<b\). Assume

\[
 z\notin C_a\cup C_b,\qquad
 z\in C_{a+1}\cap\cdots\cap C_{b-1},\qquad
 b-a-1<D,
\tag{2.1}
\]

and assume every colour

\[
 \rho_a,\rho_{a+1},\ldots,\rho_{b-1}
\tag{2.2}
\]

occurs only once on the native spine. Then no native exact-colour forest
can occur inside a \(D\)-resident chronology.

#### Proof

Every edge in (2.2) is the unique occurrence of a required colour and is
therefore selected. Thus \(C_a,\ldots,C_b\) occur consecutively in one
retained \(A\)-component. Their \(z\)-pattern is

\[
 0\,1^{\,b-a-1}\,0.
\]

The one-run is internal and shorter than \(D\), contradicting residence.
\(\square\)

The same proof works whenever a particular occurrence rule forces the
whole interval, without the singleton hypothesis. The obstruction is
specifically native: if \(R\) is a rank-\((s-1)\) colour in the full
Johnson graph on rank-\(s\) sets over \(k\) coordinates, then it has

\[
 \binom{k-s+1}{2}
\tag{2.3}
\]

possible same-colour edges. Thus a colour singleton on one spine usually
has many off-spine replacements.

## 3. The exact \(k=11\to13\) natural-selector counterexample

Use the certificate

/Users/amir.nuriyev/Documents/problem/scratch/sigma_sat_k11_allcentral_cap2.certificate.json

with SHA-256

a23b8d6847dba4350cca8dc8b9da89519e77067e58c866422713115887aaf397.

It contains a cyclic rank-six carrier of length \(462\), with all \(462\)
first-lower and all \(330\) first-upper colours. Root it at the cut used
by the audited exact compiler: if middle_cycle is the stored array, take

\[
 T_i=\text{middle\_cycle}_{\,i+2\pmod{462}}.
\]

Define

\[
 \widehat C_0=T_{461}\cap T_0,\qquad
 \widehat C_{i+1}=T_i\cap T_{i+1}\quad(0\le i\le460),
\tag{3.1}
\]

and

\[
 e_j=\widehat C_j\widehat C_{j+1},\qquad
 R_j=\widehat C_j\cap\widehat C_{j+1}\quad(0\le j\le460).
\tag{3.2}
\]

The \(R_j\) cover all \(330=\binom{11}{4}\) rank-four colours, with
multiplicity histogram

\[
 1^{210}2^{109}3^{11}.
\tag{3.3}
\]

Any one-representative Catalan selector keeps \(330\) native edges and has

\[
 462-330=132=C_6
\tag{3.4}
\]

components. The scalar Catalan count is exact.

### Theorem 3.1 (first-occurrence residence failure at the exact cut)

The first-occurrence selector on (3.2) is not depth-three resident.

#### Proof

The five completed-spine vertices

\[
\begin{array}{c|l}
j&\widehat C_j\\ \hline
253&\{3,5,6,8,9\}\\
254&\{1,3,5,8,9\}\\
255&\{1,5,7,8,9\}\\
256&\{1,4,5,7,8\}\\
257&\{4,5,7,8,10\}
\end{array}
\tag{3.5}
\]

have coordinate-\(1\) pattern \(0,1,1,1,0\). The four intervening
colours and all their native occurrence indices are

\[
\begin{array}{c|l|l}
j&R_j&\{i:R_i=R_j\}\\ \hline
253&\{3,5,8,9\}&\{253,286\}\\
254&\{1,5,8,9\}&\{254\}\\
255&\{1,5,7,8\}&\{255\}\\
256&\{4,5,7,8\}&\{256,293\}.
\end{array}
\tag{3.6}
\]

In each row, \(j\) is the least occurrence. The first selector retains
all four edges and traps an internal length-three run.

For \(k=13\),

\[
 W_{13}=\binom{13}{7}=1716,\qquad
 \Lambda_{13}=2^{12}-1=4095.
\]

Since

\[
 2W_{13}+3=3435<4095,\qquad
 3W_{13}+6=5154\ge4095,
\]

the exact deadline is \(d(13)=3\). A depth-three flat compiler requires
every internal coordinate run to have length at least \(d+1=4\), a
contradiction. \(\square\)

The last-occurrence rule fails on the same root. The vertices
\(\widehat C_{383},\ldots,\widehat C_{387}\) are

\[
\begin{gathered}
\{2,3,5,10,11\},\ \{1,3,5,10,11\},\
\{1,3,5,8,11\},\\
\{1,3,6,8,11\},\ \{3,6,8,9,11\},
\end{gathered}
\]

again giving coordinate-\(1\) pattern \(0,1,1,1,0\). The four
intervening colour occurrence sets are

\[
 \{277,383\},\quad\{262,307,384\},\quad\{385\},\quad\{58,386\},
\]

so indices \(383,384,385,386\) are all last occurrences.

There is also a choice-independent counterexample at a different fixed
root. With the certificate's stored root, coordinate \(2\) has pattern
\(0,1,1,1,0\) on
\(\widehat C_{233},\ldots,\widehat C_{237}\), and the four intervening
colours

\[
 \{1,6,9,11\},\quad
 \{1,2,6,11\},\quad
 \{1,2,3,6\},\quad
 \{1,3,6,8\}
\tag{3.7}
\]

are all singleton colours. Theorem 2.1 defeats every native occurrence
selector at that root. This does not say that every root defeats every
adaptive selector.

As a light finite audit, all \(462\) roots were checked. Exactly \(253\)
have complete rank-four native colour support. On every eligible root,
the first selector has \(41\) to \(45\) short residence intervals and the
last selector has \(27\) to \(33\). Roots without complete support fail
before residence. The explicit calculation (3.5)--(3.6), not this census,
is the symbolic first nontrivial lift test.

## 4. Independent failure of the inherited \(U\)-priority rule

Return to the exact-cut root of Section 3 and define cyclically

\[
 V_i=T_i\cup T_{i+1}.
\]

There are \(330\) distinct rank-seven \(V\)-colours. The first-occurrence
\(U\)-selector keeps the least index of every colour. Consecutive selected
indices \(i,i+1\) give the inherited \(UU\) witness

\[
 V_i\cup V_{i+1}=T_i\cup T_{i+1}\cup T_{i+2}.
\tag{4.1}
\]

### Theorem 4.1 (explicit \((US^*)\) failure)

Let

\[
 Z=\{1,2,4,5,6,8,9,11\}.
\tag{4.2}
\]

The complete list of old \(T\)-intervals with union \(Z\) is

\[
 [13,16],\quad[14,16],\quad[321,323],\quad[393,395],
\tag{4.3}
\]

where \([a,b]\) denotes \(T_a,\ldots,T_b\) and uses the \(U\)-indices
\(a,\ldots,b-1\). Their first-selector patterns are

\[
 (1,0,1),\quad(0,1),\quad(0,1),\quad(0,1).
\tag{4.4}
\]

No inherited \(U\)-interval witnessing \(Z\) is wholly selected. Hence
the chronology violates \((US^*)\) already for an empty-signature
rank-eight target.

#### Proof

Direct set union gives the exhaustive list (4.3). For the three
length-three \(T\)-intervals, the first-occurrence pairs of their two
\(V\)-colours are

\[
 (13,15),\qquad(15,322),\qquad(237,394),
\]

giving the three two-bit patterns. Direct inspection of
\(V_{13},V_{14},V_{15}\) gives \((1,0,1)\). An upper witness avoiding
both \(x,y\) must consist entirely of \(U\)-states, so (4.3)--(4.4)
exclude every witness. No \(A,X,Y\) seam can repair \(Z\), because its
union contains \(x\) or \(y\). \(\square\)

This first selector already has \(33\) adjacent omitted-index pairs and
therefore also fails the immediate-lower stable-set condition. The target
\(Z\) is an additional genuinely upper diagnostic, not the selector's only
defect.

For the last-occurrence selector, the target

\[
 Z'=\{2,3,4,5,6,7,8,11\}
\tag{4.5}
\]

has exactly the provider intervals

\[
 [1,3],\quad[105,107],\quad[105,108]
\]

with last-selector patterns

\[
 (0,1),\quad(1,0),\quad(1,0,1).
\]

Thus reversing the endpoint priority does not solve the upper gate.

## 5. The common multirow compiler: exact scope

For the strict native \(A\)-forest, let
\(I_A\subseteq\{0,\ldots,460\}\) be the selected edge indices. A
depth-three both-new second-lower colour has the form

\[
 \widehat C_i\cap\widehat C_{i+1}\cap\widehat C_{i+2}.
\]

Inside the inherited \(A\)-shore it survives only if

\[
 i,i+1\in I_A.
\tag{5.1}
\]

For the first selector at the exact cut, (5.1) covers exactly \(158\) of
the \(165=\binom{11}{3}\) rank-three colours. The missing masks are

\[
 193,289,772,1041,1154,1156,1408,
\tag{5.2}
\]

equivalently

\[
\begin{gathered}
\{1,7,8\},\ \{1,6,9\},\ \{3,9,10\},\ \{1,5,11\},\\
\{2,8,11\},\ \{3,8,11\},\ \{8,9,11\}.
\end{gathered}
\tag{5.3}
\]

The following lemma separates the cyclic obstruction from the linear
boundary issue.

### Lemma 5.1 (cyclic forcing and linear boundary escape)

Let \(T_i=D^3A_i\) have middle rank \(R\). Assume intersections of two
consecutive \(T\)'s have rank at most \(R-1\), and intersections of three
consecutive \(T\)'s have rank at most \(R-2\).

1. In the cyclic model, a rank-\((R-1)\) target can occur only in row
   \(D^2A\). A rank-\((R-2)\) target absent from every central triple
   intersection can also occur only in row \(D^2A\).
2. In a linear word with \(N\) central states and length \(N+3\), the same
   statement holds except at
   the eight cells

   \[
   A_0,A_1,DA_0,DA_1,\quad
   A_{N+1},A_{N+2},DA_N,DA_{N+1}.
   \tag{5.4}
   \]

#### Proof

\(DA_i=A_i\cup A_{i+1}\) is contained in
\(T_{i-2}\cap T_{i-1}\cap T_i\), and a base cell is contained in at least
the same three central windows. Hence an interior \(D^0\) or \(D^1\)
value has rank at most \(R-2\). If its rank is \(R-2\), it equals the
containing triple intersection. This proves the cyclic assertion and the
interior linear assertion. Precisely the four displayed cells at each
linear end lie in fewer than three central windows. \(\square\)

In the present odd child middle layer, there are \(N\)
rank-\((R-1)\) targets and \(N\) cyclic row-\(D^2\) cells. They occupy
that row bijectively, so any hole in (5.1) kills the cyclic strict compiler.

In the linear model there are \(N+1\) row-\(D^2\) cells and eight
exceptional boundary cells. For \(h\) missing rank-\((R-2)\) triple
colours, the safe crude boundary-relaxed Hall deficiency is only

\[
 (N+h-8)-(N+1)=h-9.
\tag{5.5}
\]

For \(h=7\), (5.5) gives no contradiction. Thus (5.2) is a rigorous
cyclic obstruction, while the scalar linear test passes with slack two.
The endpoint supports nevertheless give a stronger, genuinely linear
obstruction for this strict selector.

### Theorem 5.2 (endpoint-support obstruction for the seven holes)

Assume the strict first-occurrence \(A\)-forest: every both-new
rank-\((R-1)\) colour is retained at exactly one native \(AA\) gap, with no
additional \(AA\) rethreading. In any linear depth-three compiler, every
hole \(H\) in (5.3) must be contained in one of the two global middle
endpoints after adjoining \(x,y\).

For the seven holes (5.3), this is impossible. Consequently the strict
first-occurrence \(A\)-forest admits no common linear multirow compiler,
for any choice of the two global endpoints.

#### Proof

Every one of the ten exceptional cells

\[
 D^2:\ 0,N;\qquad
 D^1:\ 0,1,N,N+1;\qquad
 D^0:\ 0,1,N+1,N+2
\tag{5.6}
\]

is contained in the left or right middle endpoint. Hence a hole realized
directly at the boundary is endpoint-contained.

Suppose instead that \(H\cup\{x,y\}\) occurs in an interior \(D^2\) cell.
That cell is contained in the native rank-\((R-1)\) colour
\(S\supset H\cup\{x,y\}\) of its \(AA\) gap. Since the cell has shrunk to
rank \(R-2\), the target \(S\) must be realized elsewhere. It cannot occur
in an interior \(D^0\) or \(D^1\) cell by Lemma 5.1. It cannot occur at a
different interior \(D^2\) gap: in the strict first forest, \(S\) is the
unique selected \(AA\) occurrence of that both-new colour, and no other
status gap contains both \(x,y\). Therefore \(S\) is boundary-supported,
so again

\[
 H\cup\{x,y\}\subset S\subset T_0
 \quad\text{or}\quad
 H\cup\{x,y\}\subset S\subset T_{N-1}.
\tag{5.7}
\]

Any endpoint supporting a both-new hole has the form
\(C\cup\{x,y\}\), where \(C\) is an old rank-five set. Thus two rank-five
sets would have to cover the seven old triples. Write

\[
\begin{aligned}
a&=\{1,7,8\},& b&=\{1,6,9\},& c&=\{3,9,10\},\\
d&=\{1,5,11\},& e&=\{2,8,11\},&
f&=\{3,8,11\},& g&=\{8,9,11\}.
\end{aligned}
\]

Assign \(c\) to one of the two rank-five endpoint cores, called red.
Because \(a,d,e\) are disjoint from \(c\), none can share a five-set with
\(c\); they are blue. Since \(b\cap e=\varnothing\), \(b\) is red. But

\[
 b\cup c=\{1,3,6,9,10\}
\]

already fills the red five-set, so \(g\) is blue. Also
\(b\cap f=\varnothing\), so \(f\) is blue. The blue core would then have
to contain

\[
 a\cup d\cup e\cup f\cup g
 =\{1,2,3,5,7,8,9,11\},
\]

which has size eight. This is impossible. \(\square\)

The theorem is architecture-specific. Extra \(AA\) rethreading, a repeated
selected first-lower colour, or a different representative selector breaks
the unique displaced-colour charge and remains open.

## 6. The invariant mined from the exact \(k=11,12,13,14\) words

The exact words share the following flat integral interface.

* \(T\) is one permutation of the middle layer.
* One injection \(\phi\) assigns every lower target to a physical
  short-band cell.
* The legal-position sets \(Q_x(T,\phi)\) obey the common central-positive,
  lower-positive, and nonzero conditions \(F1\)--\(F3\).
* Every upper target is a consecutive union of \(T\), the
  chronology-only condition \(F4\), equivalently the full \((US^*)\).

The maximal word

\[
 A_p=\{x:p\in Q_x(T,\phi)\}
\]

is then exact. Residence after pins is part of \(F1(T,\phi)\); one may
not certify a bare chronology and then solve independent lower rows.
By contrast, \(F4\) is a property of \(T\) alone and no lower pin choice
can repair it.

The four finite mechanisms differ.

* \(k=11\): one resident quotient cycle plus a safe cut; repeated-lower
  slack \(369\).
* \(k=12\): a six-piece odd-to-even braid; endpoint depth loss \(2\) and
  repeated-lower slack \(264\).
* \(k=13\): two resident all-shadow cycles plus one shadow-safe splice;
  endpoint depth loss \(2\) and repeated-lower slack \(1057\).
* \(k=14\): a six-piece braid whose minimum new-coordinate run is exactly
  the legal length three; endpoint depth loss \(1\) and repeated-lower
  slack \(391\).

The \(k=14\) braid is explicitly defect-driven: extracting its required
three-vertex \(B\)-block deletes two unique upper colours, and two selected
\(A\)-cuts expose exactly those colours so that five new seams restore
them. The lower pin table is then solved afresh. This is not a local phase
rule.

The odd one-hole paths also have an exact Catalan block identity. If a
Hamilton path in \(J(2r-1,r)\) has distinct first intersections omitting
only \(C_*\), then for every \(t\)-set \(Q\), the number \(b_Q\) of
maximal vertex blocks containing \(Q\) is

\[
 \boxed{
 b_Q=
 \binom{2r-1-t}{r-t}
 -\binom{2r-1-t}{r-1-t}
 +\mathbf 1_{Q\subseteq C_*}.}
\tag{6.1}
\]

Indeed, \(b_Q\) equals the number of vertices containing \(Q\) minus the
number of internal edges whose intersection contains \(Q\). For \(t=2\),
the binomial difference is \(C_{r-1}\). Thus the Catalan block census is
automatic once the one-hole path exists; it does not select
residence-safe representatives, upper providers, or a common pin table.

The additional candidate invariants are false:

* exact \(k=13\) has \(78\) triple-covered first-upper colours, so a simple
  upper design is not necessary;
* the \(k=13\) carrier has two physical cycles before one global splice,
  so one cyclic carrier is not necessary;
* direct compiler copying across the \(3\to2\) deadline drop is impossible:
  at least \(94\) \(k=11\) and \(658\) \(k=13\) depth-two assignments
  become illegal.

## 7. The surviving global theorem

The counterexample identifies the smallest escape from the canonical
priority rule: change the root and make globally adaptive native choices,
or introduce off-spine \(AA/UU\) edges. Within the diamond lane, the
following simultaneous construction is sufficient:

1. an exact child owner path \(T^+\);
2. a coloured \(A\)-forest using one edge of every both-new lower colour,
   with repeated native occurrences or off-spine edges cutting every
   residence hazard;
3. a \(U\)-forest whose omitted indices satisfy the first-lower condition
   and whose retained intervals supply every target required by \((US^*)\);
4. a global cross-state circulation cancelling the packet defects (1.8),
   or an off-edge rethreading which avoids that switch bank;
5. one injective pin table \(\phi^+\) satisfying \(F1\)--\(F3\) for all
   lower rows simultaneously, including every central, seam, and boundary
   pin.

This nonlocal defect-driven labelled-routing statement would finish the
same-parity flat induction. The exact \(k=11,\ldots,14\) words prove that
its output interface is nonempty in those dimensions. They do not provide
a dimension-independent construction.

## 8. Adversarial scope audit

* Theorem 1.1 assumes exactly one path in (1.1) per old edge. Theorem 1.2
  allows independent both/none choices, but both theorems keep all cross
  endpoints on their native old edges. They do not cover open endpoints,
  off-edge endpoints, or larger correlated packets.
* Theorem 1.3 shows that endpoint identification already evades packet
  phase conservation at the owner-graph level. It does not provide
  residence or shadows: its \(A\)- and \(U\)-centres remain isolated.
* Theorems 2.1 and 3.1 assume retained native \(A\)-edges are literal
  consecutive \(AA\) adjacencies. Off-spine same-colour edges and global
  reordering can evade them.
* Theorem 4.1 concerns the inherited first-occurrence \(U\)-forest.
  Adaptive representatives or nonnative \(UU\) edges can restore the
  displayed target.
* The seven protected-pair holes do not violate the scalar linear bound
  (5.5). Theorem 5.2 uses the stronger endpoint-support cut and is valid
  only for the strict first-occurrence forest with unique selected
  first-lower colours and no extra \(AA\) rethreading.
* Nothing here disproves the unrestricted simultaneous labelled-routing
  theorem, the flat induction, or the contiguous-OR conjecture. What is
  disproved is the natural local/priority lift. The remaining theorem must
  be genuinely global and defect-driven.

## 9. Audited local sources

The general flat interface and the finite-word fingerprints used above are
proved or certified in:

* MATH_LANE_E_FLAT_DEADLINE_COMPILER_EQUIVALENCE_AND_INDUCTION_GATE_20260728.md;
* MATH_LANE_S_MONOTONE_DEADLINE_SCD_COMPILER_AND_DIAMOND_RECURSION_20260728.md;
* MATH_ATTACK_H_KPLUS2_DIAMOND_CATALAN_SEAM_RELAXED_INDUCTION_20260728.md;
* K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md;
* MATH_K13_EXACT_1719_CERTIFICATE_20260728.md;
* MATH_K14_EXACT_3434_CERTIFICATE_20260728.md.
