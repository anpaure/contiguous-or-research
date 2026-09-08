# Connectivity-free middle factors: exact protected splicing and a two-cycle refutation

Date: 2026-07-29

Status: the unconditional **direct flat-carrier**
\(c-1\)-seam/slack claim is **false**. An
explicit \(k=5\) equivariant two-cycle factor is resident, complete in every
lower and upper shadow, and passes the cyclic one-core Hall gate, but no
one-cut-per-cycle, one-direct-seam splice remains resident. This note also
proves the exact conditional theorem that does turn a disconnected factor
into an optimal word.

## 1. Parameters and the claim being tested

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W={k\choose r},\qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s}.
\tag{1.1}
\]

Let \(d=d(k)\) be the least positive integer satisfying

\[
 dW+{d+1\choose2}\geq\Lambda,
\tag{1.2}
\]

and put

\[
 B(k)=W+d,\qquad
 \sigma=dW+{d+1\choose2}-\Lambda.
\tag{1.3}
\]

For a linear word \(X=(X_i)\), write

\[
 (DX)_i=X_i\cup X_{i+1}.
\tag{1.4}
\]

For a cyclic or linear rank-\(r\) Johnson chronology \(T\), define

\[
 I_q(T;i)=\bigcap_{a=0}^{q}T_{i+a},\qquad
 U_q(T;i)=\bigcup_{a=0}^{q}T_{i+a}.
\tag{1.5}
\]

The assertion tested here was that a resident, lower/upper-shadow-complete,
equivariant quotient \(2\)-factor with \(c\) components could automatically
be opened and joined by \(c-1\) seams, with the seam cost paid from
\(\sigma\). This conflates:

1. the number of physical lift cycles;
2. the number \(c-1\) of new Johnson adjacencies; and
3. the lower/upper occurrences and Hall neighbours changed by the cuts.

They are not equal.

## 2. Quotient components are not physical components

Let \(C_k=\langle\rho\rangle\) act by coordinate rotation. Its action on
\({[k]\choose r}\) is free. If a rank-\(r\) set were fixed by a nontrivial
subgroup of order \(a\mid k\), it would be a union of coordinate orbits of
size \(a\), so \(a\mid r\). But

\[
 \gcd(k,r)=\gcd(2m+1,m+1)=1.
\]

### Lemma 2.1 (voltage lift count)

Let \(Q\) be an oriented quotient cycle with voltage
\(v_Q\in\mathbb Z_k\). Its physical lift consists of

\[
 \gcd(k,v_Q)
\tag{2.1}
\]

cycles, each of length

\[
 |Q|\,{k\over\gcd(k,v_Q)}.
\tag{2.2}
\]

Thus the physical component count is

\[
 c_{\rm phys}=\sum_Q\gcd(k,v_Q).
\tag{2.3}
\]

It equals the quotient component count only when every voltage is a unit.

#### Proof

After one circuit of \(Q\), the sheet coordinate changes by \(v_Q\). The
orbits of translation by \(v_Q\) on \(\mathbb Z_k\) number
\(\gcd(k,v_Q)\), each of length \(k/\gcd(k,v_Q)\). Multiplying by the
quotient length proves the formulas. \(\square\)

At prime \(k=13\), nonzero voltage happens to imply unit voltage. It does
not at composite \(k=15\).

## 3. Exact physical ports and residence

Let

\[
 F=C_1\sqcup\cdots\sqcup C_c
\tag{3.1}
\]

be the physical rank-\(r\) Johnson \(2\)-factor. A direct one-cut splice
datum consists of one deleted edge \((z_a,x_a)\) per cycle, an orientation
of the opened path \(P_a=x_a,\ldots,z_a\), an order
\(a_1,\ldots,a_c\), and the proposed cross edges
\(z_{a_j}x_{a_{j+1}}\).

It is a physical path datum exactly when

\[
 |z_{a_j}\cap x_{a_{j+1}}|=r-1
 \qquad(1\leq j<c).
\tag{3.2}
\]

Thus the component port graph must have a Hamilton path with compatible
oriented cuts. Connectivity of an untyped component graph is insufficient.
In a quotient description, endpoint phases determined by the voltages must
realize all equations (3.2) simultaneously.

One may instead permit a direct **rank-\(s\) relaxed seam** between
nonadjacent rank-\(r\) endpoints. It still adds no middle vertex, but it is
not an edge of the Johnson factor. The following identity is then forced.

### Lemma 3.1 (rank-\(s\) seam identity)

Let consecutive middle sets \(M,N\) have rank \(r\), and put

\[
 s=r-|M\cap N|.
\]

Then

\[
 |M\cap N|=r-s,\qquad |M\cup N|=r+s.
\tag{3.3}
\]

If \(E\) is the maximal linear depth-\(d\) erosion of a resident \(T\),
the corresponding nonboundary cell of \(D^{d-1}E\) is \(M\cap N\), while
the corresponding cell of \(DT\) is \(M\cup N\). Thus \(s>1\) removes
both an immediate rank-\((r-1)\) lower slot and an immediate rank-\((r+1)\)
upper slot. Any such loss must be repaired in the targetwise ledgers below.

#### Proof

The rank formulas are inclusion-exclusion. The lower statement is the
maximal-erosion intersection identity, and the upper statement is the
definition of \(D\). \(\square\)

No middle vertex is added by a direct seam. If the result compiles, its
word still has length \(W+d\). Inserting connector vertices instead makes
the middle chronology longer than \(W\) and cannot prove \(B(k)\).

### Lemma 3.2 (exact residence collar test)

The concatenated chronology \(T=P_{a_1}\cdots P_{a_c}\) is depth-\(d\) resident
if and only if no coordinate trace contains an internal word

\[
 0\,1^\ell\,0\qquad(1\leq\ell\leq d).
 \tag{3.4}
\]

If every old cycle is cyclically depth-\(d\) resident, every new violation
meets a new seam. If every component has more than \(d\) vertices, this is
an exact \(d\)-collar test at one seam at a time.

#### Proof

An internal positive coordinate run is admissible exactly when its length
is at least \(d+1\). Old component interiors do not change, so every new
short run crosses a new adjacency. A length-\(d+2\) test window cannot meet
two seams when the intervening components are longer than \(d\).
\(\square\)

## 4. Shadow preservation is targetwise

For \(\varepsilon\in\{-,+\}\), let
\(\chi_q^-=I_q\) and \(\chi_q^+=U_q\). For a target \(S\), let

* \(\mu_q^\varepsilon(S)\) be its old cyclic multiplicity;
* \(\ell_q^\varepsilon(S)\) count old occurrences crossing selected cuts;
* \(g_q^\varepsilon(S)\) count new occurrences crossing seams.

### Theorem 4.1 (cut-and-seam identity)

For the spliced path,

\[
 \boxed{
 \mu_{q,T}^\varepsilon(S)
 =\mu_q^\varepsilon(S)-\ell_q^\varepsilon(S)
   +g_q^\varepsilon(S).}
\tag{4.1}
\]

The required depth-\(q\) shadow is therefore preserved if and only if

\[
 \mu_q^\varepsilon(S)-\ell_q^\varepsilon(S)
   +g_q^\varepsilon(S)\geq1
\tag{4.2}
\]

for every target at that depth.

#### Proof

Every old window not crossing a selected cut is unchanged. The old
cut-crossing windows are precisely the removed multiset, and every new path
window not already old crosses a new seam. These three multisets partition
the new windows. \(\square\)

If all components have more than \(q\) vertices, the cuts remove \(cq\)
windows and the seams add \((c-1)q\). The net occurrence loss is

\[
 q,
\tag{4.3}
\]

independent of \(c\). This says nothing about which target loses its last
witness. In particular, \(c-1\) is not a shadow cost.

For upper ranks, (4.2) with \(\varepsilon=+\) and
\(1\leq q\leq k-r\) is the exact test.

Let \(E\) be the maximal linear depth-\(d\) erosion of a resident path.
For \(1\leq q<d\), the interior of \(D^{d-q}E\) consists of the
\(W-q\) path intersections \(I_q(T;i)\), and the row has \(2q\) further
endpoint cells. If \(b_q(S)\) counts those endpoint cells, then

\[
 \operatorname{mult}_{D^{d-q}E}(S)
 =\mu_q^-(S)-\ell_q^-(S)+g_q^-(S)+b_q(S).
\tag{4.4}
\]

Indeed, the maximal erosion is the intersection of all carrier entries
whose depth-\(d\) source window contains the given source position. The
resident Johnson intersection-tower identity therefore identifies the
nonboundary cells of \(D^{d-q}E\) with the \(q+1\)-fold intersections of
consecutive carrier entries. This gives \(W-q\) interior cells. Since the
row length is \(W+q\), exactly \(2q\) cells remain at the two boundaries,
which proves (4.4).

Assume additionally that each global endpoint component has more than
\(q\) vertices, so its entire \(q\)-collar consists of old resident Johnson
edges. For a rank-\((r-q)\) lower target \(S\), then,

\[
 b_q(S)=0.
\tag{4.5}
\]

The \(q\) cells on either boundary have successive ranks
\(r,r-1,\ldots,r-q+1\), all larger than \(r-q\). Thus, in the maximal
erosion's fixed row, a missing rank-\((r-q)\) colour is not repaired by
an endpoint cell. A compiler may instead shrink a source letter and realize
the colour literally. Whether that can retain \(DA=DE\) is exactly a
one-core containment/Hall question; the known \(k=13\) compiler made the
repair while leaving that grading.

In the odd lower-\(q=1\) rainbow case, let \(R\) be the set of \(c\) cut
colours and \(S_{\rm seam}\) the set of seam colours. The natural missing
set is exactly

\[
 H=R\setminus S_{\rm seam}.
\tag{4.6}
\]

Its size can range from \(1\) to \(c\); it is not forced to equal \(c-1\).
In a general depth-\(d\) compiler, only two boundary chains lie outside the
\(W-1\) path adjacencies, so boundary-only repair requires \(|H|\leq2\),
with the relevant endpoint containments. In the graded one-core subclass
\(DA=DE\), the fixed row \(D^{d-1}E\) cannot repair the hole. A graded
word may still realize a member of \(H\) **literally as a source letter**,
provided a one-core containment port exists. In the maximal resident
Johnson envelope, every rank-\((r-1)\) value in a nonextreme fixed lower
cell is a path-edge intersection, while the two extreme boundary chains
contain rank-\(r\) endpoint sets. Hence every member of \(H\) is absent
from all fixed rows and must be added to the flexible Hall target family
below. The usual graph on ranks at most \(h\) is insufficient whenever
\(H\ne\varnothing\).

In particular, a disconnected odd rainbow factor always creates at least
one new rank-\((r-1)\) Hall demand. Preserving an old matching on
\(\mathcal L_h\) does not settle the splice: that matching and the new
members of \(H\) must fit simultaneously in one physical occurrence graph.

## 5. Exact one-core extension and Hall preservation

Put \(h=r-d\). Let \(E=(E_p)_{p=0}^{W+d-1}\) be nonempty and satisfy

\[
 D^dE=T.
\tag{5.1}
\]

A linear one-core is \(C\subseteq E\) satisfying

\[
 DC=DE.
\tag{5.2}
\]

### Lemma 5.1 (pin-compatible core condition)

Suppose some positions have prescribed letters \(S_p\subseteq E_p\), and
require \(C_p\subseteq S_p\). Such a one-core exists if and only if, for
every coordinate \(x\) and adjacent pair \(p,p+1\) with

\[
 x\in E_p\cup E_{p+1},
\tag{5.3}
\]

at least one endpoint both contains \(x\) in its envelope and is not forced
by its pin to omit \(x\).

Equivalently, no positive support edge has both endpoints forced omitted.
In particular, a support-run endpoint adjacent to a zero outside the run
must be available. A global word endpoint is exempt only from the absent
outer edge, not from its inward edge.

#### Proof

Equation (5.2) is coordinatewise

\[
 c_p(x)\vee c_{p+1}(x)
 =e_p(x)\vee e_{p+1}(x),\qquad c_p(x)\leq e_p(x).
\tag{5.4}
\]

Every positive edge therefore needs an available selected endpoint. This
is necessary. If it holds, select every available occurrence of \(x\).
Doing this independently for each coordinate constructs the core.
\(\square\)

Put

\[
 \mathcal L_h=\{S:1\leq|S|\leq h\}.
\]

More generally, let \(\mathcal F\) be any family of lower targets designated
for literal source-row realization. In the splice application it contains
every target missing from the fixed rows. In the ordinary graded Johnson
case this includes \(\mathcal L_h\), and after a disconnected rainbow splice
it also includes the set \(H\) in (4.6). For a fixed one-core \(C\), define

\[
 \mathcal G_C(\mathcal F)
 =(\mathcal F,\{0,\ldots,W+d-1\};E),
\tag{5.5}
\]

by

\[
 S\sim p\quad\Longleftrightarrow\quad
 C_p\subseteq S\subseteq E_p.
\tag{5.6}
\]

Suppose old and new occurrence graphs have a common stable right set
\(R_0\) on which all neighbourhoods agree. Put

\[
 J_-=R\setminus R_0,\qquad J_+=R'\setminus R_0.
\tag{5.7}
\]

For a target shore \(X\), define

\[
 \eta_G(X)=|N_G(X)|-|X|,\quad
 \ell(X)=|N_G(X)\cap J_-|,\quad
 g(X)=|N_{G'}(X)\cap J_+|.
\tag{5.8}
\]

### Theorem 5.2 (exact Hall update)

The new graph saturates every target in \(\mathcal F\) if and only if

\[
 \boxed{
 \eta_G(X)-\ell(X)+g(X)\geq0
 \quad\text{for every }X\subseteq\mathcal F.}
\tag{5.9}
\]

More generally, let \(M_0\) be any retained valid partial matching on a
target family \(\mathcal R\subseteq\mathcal F\). It extends to a matching
saturating \(\mathcal F\) if and only if

\[
 G'\bigl[\mathcal F\setminus\mathcal R,\,
 R'\setminus M_0(\mathcal R)\bigr]
\tag{5.10}
\]

has a matching saturating \(\mathcal F\setminus\mathcal R\).
For a former full matching \(M\), take \(\mathcal R\) to be exactly the
targets whose old edges remain valid. This also handles newly added flexible
targets such as \(H\), which were absent from the old matching.

#### Proof

The stable and changed right sets are disjoint, so

\[
 |N_{G'}(X)|-|X|
 =|N_G(X)|-|X|-\ell(X)+g(X).
\]

Hall's theorem proves (5.9). After fixing \(M_0\), the right vertices in
(5.10) are exactly those still available. \(\square\)

An asymmetric physical splice normally destroys the cyclic action on
positions. The old weighted quotient Hall inequalities cannot simply be
reused. One must retain a phase-resolved physical matching and apply
(5.10), or test the new physical graph. If a new graph genuinely remains
equivariant, weighted quotient Hall remains exact using actual orbit sizes;
short left or nonfree right orbits are not unit vertices.

## 6. Corrected connectivity-free compiler theorem

### Theorem 6.1 (protected splice implies an optimal word)

Let \(d=d(k)<r\), and put \(h=r-d\geq1\). Suppose a direct splice datum on
the physical lift satisfies:

1. its phases and ports produce a rank-\(r\) middle chronology \(T\) of
   length \(W\), listing every rank-\(r\) target once; seams may be Johnson
   or explicitly audited rank-\(s\) relaxed seams;
2. \(T\) is depth-\(d\) resident and has a nonempty envelope \(E\) of
   length \(W+d\) with \(D^dE=T\);
3. let \(\mathcal K(E)\) be the family of lower targets occurring in one
   of the fixed rows \(D^jE\), \(1\leq j\leq d-1\), and put
   \[
      \mathcal F=
      \{S\subseteq[k]:1\leq|S|<r\}\setminus\mathcal K(E);
   \]
4. every rank-\(r+q\) target, \(1\leq q\leq k-r\), occurs in \(D^qT\);
5. a pin-compatible one-core \(C\subseteq E\), \(DC=DE\), has a physical
   graph \(\mathcal G_C(\mathcal F)\) saturating \(\mathcal F\).

Then there is a nonempty word \(A\) of length \(W+d\) containing every
nonempty subset of \([k]\) as a contiguous OR. Hence

\[
 \nu(k)=B(k)=W+d.
\tag{6.1}
\]

#### Proof

Choose a saturating matching in \(\mathcal G_C\). Put the matched target at
each matched position and \(E_p\) at each unmatched position. Then

\[
 C\subseteq A\subseteq E.
\]

Monotonicity and \(DC=DE\) give

\[
 DE=DC\subseteq DA\subseteq DE,
\]

so \(DA=DE\), and consequently

\[
 D^jA=D^jE\quad(1\leq j\leq d),\qquad D^dA=T.
\tag{6.2}
\]

The matching supplies every lower target absent from the fixed rows, while
\(\mathcal K(E)\) supplies the rest. The middle chronology supplies rank
\(r\). Finally

\[
 D^{d+q}A=D^qT,
\tag{6.3}
\]

so Hypothesis 4 supplies all larger ranks. The word has length \(W+d\);
the deadline lower bound supplies the reverse inequality. \(\square\)

Within the **literal-flexible-target graded subclass**, the one-core/Hall
condition is also necessary: if \(A\subseteq E\), \(DA=DE\), and every
target in \(\mathcal F\) is required to occur as a source letter, then
\(A\) is itself a one-core and one literal occurrence of each member of
\(\mathcal F\) is a matching. A graded word could instead realize one of
these targets first as a multi-letter OR, so Hall is not necessary without
the literal source-row hypothesis. The theorem does not claim that every
optimal word is graded.

## 7. Why scalar slack cannot pay for seams

At derivative row \(j<d\), opening \(c\) sufficiently long cyclic
components removes

\[
 c(d-j)
\tag{7.1}
\]

old cyclic cells. The \(c-1\) seams create \((c-1)(d-j)\) mixed cells, and
the two global endpoints create \(2(d-j)\) boundary cells. Thus the final
row count is

\[
 W-c(d-j)+(c-1)(d-j)+2(d-j)=W+d-j.
\tag{7.2}
\]

Up to \(cd\) old source neighbours can change, and across all lower rows
the old collar contains

\[
 c\sum_{s=1}^{d}s=c{d+1\choose2}
\tag{7.3}
\]

cells. This is not \(c-1\). There is also no additive length charge
\(c-1\): a direct seam replaces an adjacency and adds no vertex.

For (7.1), a row-\(j\) cell is controlled by a carrier footprint of
length \(d-j+1\). Exactly \(d-j\) cyclic starts cross a chosen cut. The
same number cross each new seam, and truncating the two outer cyclic
collars contributes \(d-j\) new cells at each global endpoint. Summing
over \(j=0,\ldots,d-1\) gives (7.3).

In the graded allocation, \(\sigma\) decomposes by rows as

\[
 \sigma=
 \left[(W+d)-\sum_{s=1}^{h}{k\choose s}\right]
 +\sum_{j=1}^{d-1}
 \left[(W+d-j)-{k\choose h+j}\right].
\tag{7.4}
\]

These are row capacities, not transferable target addresses or Hall
margins. A boundary flag may move one demand from a fixed derivative row
to the source row, but only through an actual containment port satisfying
the common-core Hall constraints. Explicitly,

\[
\begin{array}{c|c}
k&\text{row decomposition of }\sigma\\ \hline
5&8=7+1,\\
13&1059=627+431+1,\\
15&2928=1495+1432+1.
\end{array}
\tag{7.5}
\]

The top lower row has only one global spare. More generally, the exact
equality ledger

\[
 \sigma=\Delta_{\rm depth}+\Delta_{\rm repeat}
\tag{7.6}
\]

audits a completed optimal word. It implies none of (3.2), (3.4), (4.2),
(5.4), or (5.9).

## 8. Exact equivariant counterexample at \(k=5\)

Work on \(\mathbb Z_5\), with \(k=5,r=3,W=10\). Since
\[
 10+1<15\leq2\cdot10+{3\choose2},
\]
one has \(d(5)=2\). Define

\[
 A_i=\{i,i+1,i+2\},\qquad A_i\longrightarrow A_{i+1},
\tag{8.1}
\]

and

\[
 B_i=\{i,i+1,i+3\},\qquad B_i\longrightarrow B_{i+2},
\tag{8.2}
\]

with indices modulo \(5\).

### Proposition 8.1 (all cyclic gates pass)

The two directed \(5\)-cycles:

1. partition \({\mathbb Z_5\choose3}\);
2. are equivariant quotient loops of voltages \(1\) and \(2\), hence lift
   to exactly two physical cycles;
3. are cyclically depth-two resident;
4. are complete in every lower and upper shadow; and
5. admit a cyclic equivariant one-core whose Hall graph saturates every
   singleton target.

#### Proof

The complements of the \(A_i\) are the five adjacent pairs, while the
complements of the \(B_i\) are the five diagonals. Thus the ten triples are
distinct and exhaustive. Rotation advances each displayed edge; the
voltages \(1,2\) are units modulo \(5\).

Along either cycle a fixed coordinate occurs at exactly three consecutive
cycle positions. Every positive run has length \(3=d+1\).

The immediate lower labels are

\[
 A_i\cap A_{i+1}=\{i+1,i+2\},\qquad
 B_i\cap B_{i+2}=\{i,i+3\}.
\tag{8.3}
\]

They are respectively the five adjacent pairs and five diagonals, so lower
\(q=1\) is globally rainbow. Also

\[
 A_i\cup A_{i+1}=B_i\cup B_{i+2}
 =\mathbb Z_5\setminus\{i+4\},
\tag{8.4}
\]

so upper \(q=1\) contains every four-set. Three consecutive vertices on
either cycle have singleton intersection and full union, proving both
\(q=2\) shadows.

For the \(A\)-cycle take \(P_i^A=\{i\}\). Index the \(B\)-cycle as
\(T_j^B=B_{2j}\) and take

\[
 P_j^B=\{2j+1\}.
\tag{8.5}
\]

Then \(D^2P=T\). The singleton-valued one-core is forced to be \(C=P\),
since each coordinate of a \(DP\) edge is available only at its own
endpoint. Every singleton has one candidate on each cycle, so Hall
saturates all five singleton targets. \(\square\)

### Theorem 8.2 (no resident one-seam splice)

No choice of one cut in each cycle, either order, either orientation, and
one direct concatenation seam produces a linearly depth-two resident
rank-three chronology. In particular, allowing a non-Johnson seam does not
evade the obstruction.

#### Proof

Suppose such a splice exists. Let \(X\) be the terminal vertex of the first
opened cycle and \(X'\) its neighbour across the deleted cut. Let \(Y\) be
the initial vertex of the second opened cycle and \(Y'\) its neighbour
across its deleted cut. Put

\[
 R_X=X\cap X',\qquad R_Y=Y\cap Y'.
\tag{8.6}
\]

For every \(a\in X\setminus Y\), if \(a\in R_X\), the deleted edge lies
inside the unique cyclic length-three positive run of \(a\). Cutting it
splits the run into nonempty endpoint pieces of lengths \(1\) and \(2\).
The piece ending at \(X\) is followed by \(Y\), which omits \(a\), and
becomes a forbidden internal short run. Hence

\[
 X\setminus Y\subseteq X\setminus R_X.
\]

The right side has size one. The cycles are vertex-disjoint and all their
vertices have rank three, so \(X\ne Y\) and \(|X\setminus Y|\geq1\).
Therefore \(|X\setminus Y|=1\): residence itself forces the seam to be
Johnson. Put \(S=X\cap Y\). Both \(R_X\) and \(S\) are two-subsets of \(X\),
so

\[
 R_X=S.
\tag{8.7}
\]

The same argument for \(Y\setminus X\) gives

\[
 R_Y=S.
\tag{8.8}
\]

But (8.3) says that all ten cut-edge intersection colours are distinct.
Two component edges cannot both have colour \(S\), a contradiction.
Reversal changes neither cut colours nor run lengths. \(\square\)

### Corollary 8.3 (slack cannot legalize the seam)

No depth-two source word can have any of these direct concatenations as its
middle chronology.

#### Proof

Coordinatewise, applying \(D^2\) dilates every source occurrence across
three consecutive output positions. Unions of such dilated intervals have
no internal positive run shorter than three. Thus every chronology of the
form \(D^2A\) is linearly depth-two resident, contrary to Theorem 8.2.
\(\square\)

Here

\[
 \Lambda={5\choose1}+{5\choose2}=15,\qquad
 \sigma=2\cdot10+{3\choose2}-15=8,
\tag{8.9}
\]

while \(c-1=1\). Thus even unit voltages, two physical components, cyclic
residence, complete shadows, a passing cyclic one-core Hall matching, and
\(\sigma\gg c-1\) do not imply a legal one-seam splice.

This theorem rules out exactly the advertised one-cut-per-component,
direct-seam architecture, including rank-\(s>1\) seam relaxation. It does
not rule out larger multi-cut surgery.

## 9. Exact comparison with the \(k=13\) success

The quotient cycles have

\[
 (|Q_0|,v_0)=(119,8),\qquad (|Q_1|,v_1)=(13,6).
\tag{9.1}
\]

They lift to physical cycles of lengths \(1547\) and \(169\). The selected
cuts and seam have ledger

\[
\begin{array}{c|c|c}
\text{edge}&\text{intersection}&\text{union}\\ \hline
2515-2395&2387&2523\\
2167-2391&2135&2423\\
2515-2391&2387&2519.
\end{array}
\tag{9.2}
\]

The seam recreates cut colour \(2387\), while \(2135\) is the unique
natural lower-\(q=1\) hole. It is boundary-repaired literally by

\[
 A_{1718}=2135.
\tag{9.3}
\]

All lower depths \(q=2,\ldots,6\), all upper depths
\(q=1,\ldots,6\), and depth-three residence survive. This was not inferred
from slack: among \(24960\) oriented physical candidates, \(6032\)
preserved every upper depth and only \(1092\) also passed exact residence.

The lower compiler was then solved afresh on the physical path:

\[
 4095/4095
\tag{9.4}
\]

in the flexible short-cell Hall graph, followed by an independently
verified common word of length \(1719=W+d\).

No equivariant graded one-core matching was transported. For the saved
maximal erosion \(P\) and word \(A\),

\[
 |\{i:(DA)_i\ne(DP)_i\}|=209,\qquad
 |\{i:(D^2A)_i\ne(D^2P)_i\}|=1.
\tag{9.5}
\]

The seam also breaks \(C_{13}\)-equivariance. Hence \(k=13\) proves one
exceptionally compatible two-cycle splice, not automatic spliceability or
quotient-Hall preservation.

## 10. Proved boundary and smallest replacement lemma

Hamiltonicity of the input middle factor is unnecessary: Theorem 6.1 only
needs a protected physical splice certificate. What is false is that
residence, cyclic shadow completeness, equivariance, one-core Hall, and
scalar slack force such a certificate in the direct flat-carrier
architecture.

The smallest useful replacement is the following general gate.

> **Protected port-path lemma (unproved in general).** In the intended
> family of equivariant quotient factors, choose physical phases, one cut
> per lift cycle, orientations, and a component order so that: every cross
> port is Johnson or is an explicitly audited rank-\(s\) seam; every seam
> passes the residence collar test; the
> targetwise upper inequalities (4.2) hold; use (4.4)--(4.6) to identify
> the exact family \(\mathcal F\) not covered by fixed lower rows; and find
> a pin-compatible one-core whose physical graph simultaneously matches
> \(\mathcal F\), subject to Hall (5.9) or residual matching (5.10).

Those conditions are jointly sufficient by Theorem 6.1. The \(k=5\)
example proves that the residence-port part cannot be omitted. The
last-witness identity proves that cyclic support cannot replace targetwise
inequalities. The Hall-update identity proves that \(\sigma\) cannot replace
the common-core condition.

## 11. Adversarial audit

Theorem 8.2 was checked independently for both orientations and both
component orders. Its proof uses only four explicit facts: every coordinate
run has length three, each cut label has size two, the two components have
disjoint vertex sets, and the ten cut labels are globally rainbow.
Residence first forces any putative seam to be Johnson. The proof does not
assume shadow safety; it proves that no candidate reaches that later gate.

Its scope is deliberately exact:

* it refutes one cut per component plus one direct seam;
* it does not refute multi-cut/multi-seam surgery;
* it does not refute a nonflat deadline embedding in which the factor
  vertices cease to be one common \(D^d\) row;
* it refutes automatic transport, not an unrelated optimal \(k=5\) word;
* it remains a counterexample after adding pre-splice cyclic one-core Hall.

It refutes the dimension-uniform assertion. If the proposed assertion is
instead restricted specifically to \(k=15\), or to a quotient class that
forbids voltage loops, Theorem 8.2 is not a counterexample to that narrower
statement; the exact protected conditions of Sections 3--6 are then the
remaining gate.

The positive Theorem 6.1 is the literal sandwich

\[
 DC\subseteq DA\subseteq DE=DC,
\]

followed by \(D^dA=T\) and \(D^{d+q}A=D^qT\). It requires a physical Hall
matching after an asymmetric splice. A quotient flow alone is not a phased
matching certificate, and the old quotient graph is not an automorphism
quotient of the final path.

Therefore no finite optimality conclusion follows from a bare disconnected
factor. The proved result is the conditional compiler theorem together with
the unconditional \(k=5\) refutation.
