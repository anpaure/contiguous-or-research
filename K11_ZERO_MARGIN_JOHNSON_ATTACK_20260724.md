# A Johnson-forest attack on the zero-margin \(k=11\) templates

## 1. Verdict

Assume that a zero-free universal OR word of length \(465\) lies in one of
the zero-margin \(n_5=133\) or \(n_5=132\) templates proved in
`K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md`.

No contradiction is obtained.  In particular, none of the five
\(n_5=132\) modes is eliminated.  The attack does, however, prove four new
structural statements.

1.  At \(n_5=133\), all \(329\) rank-four targets except the carrier \(H\)
    admit an exact common nested matching
    
    \[
    K^{(4)}\subset S^{(5)}\subset U^{(6)}
    \]
    
    onto the \(329\) nonliteral rank-five targets and their \(329\)
    endpoint-matched rank-six targets.  This is an integral, labelled,
    order-compatible matching, not a scalar Hall count.

2.  The four middle endpoint blocks \(01,02,13,23\) form a doubly rainbow
    Johnson forest: both their rank-four intersection colors and their
    rank-six union colors are distinct.  If \(c_M\) of these blocks are
    nonempty, the forest uses exactly \(329-c_M\) of the \(330\) rank-four
    colors.  Consequently at least \(101\) outer \(00/33\) forest edges
    reuse middle rank-four colors, and at least \(26\) distinct rank-four
    colors are reused.  At \(n_5=132\), the one next-level defect weakens
    these constants only to \(100\) edges and \(25\) colors.

3.  The eleven coordinate-run equations extend to every coordinate set
    \(X\subseteq[11]\).  They fuse exactly with the ordered perfect
    rank-five/rank-six matching.  Every uniformly averaged consequence
    closes with an explicit external matching slack; thus no point,
    codimension, or \(42\)-label average contradicts a template.

4.  Among exact zero runs of length at least two, lengths two and three
    are forced to the seam or boundary.  The first unlocalized ordinary
    length is four; under the ordinary hypotheses of Lemma 9.1, such a run
    occurs exactly when two adjacent rank-seven five-window unions are
    equal.  This folding is locally compatible with all the rank-four,
    rank-five, and rank-six rainbow constraints.  The absent rank-seven
    rainbow is therefore a genuine obstruction, not merely a missing
    estimate.

The strongest exact normal form is a nearly spanning rank-three Johnson
frame walk feeding simple Johnson forests in ranks \(4,5,6\), followed by
an unforced fold in rank seven.  The remaining issue is physical
realizability: the abstract middle forest must be lifted to actual
rank-at-most-three entries while also realizing the large forced reuse of
lower intersection colors and the residual external inclusion matching.

No finite search, solver, random experiment, or web search is used below.

## 2. Exact inputs and notation

Write the central rank-at-most-three segment as

\[
A_0,A_1,\ldots,A_{m-1}\subseteq[11]
\]

and put

\[
B_i=A_i\cup A_{i+1},\qquad
C_i=A_i\cup A_{i+1}\cup A_{i+2},\qquad
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}.
\tag{2.1}
\]

There is one seam triple

\[
H=C_s,\qquad \rho:=|H|\in\{3,4\}.
\]

Every other \(C_i\) is a distinct five-set and every \(T_i\) is a distinct
six-set.  The two pair colors under \(H\) have rank below four.  Mode C0 at
\(n_5=132\) has one further low pair.

At \(n_5=133\),

\[
C=P_4\Vert D_3\Vert Q_4,\qquad
m=|D_3|=332-n_4.
\tag{2.2}
\]

The \(n_4\) entries in \(P_4,Q_4\) are distinct literal four-sets.  In
\(D_3\), all but the two seam pairs are distinct nonliteral four-set
targets, all triples except \(H\) are distinct five-set targets, and all
four-windows are distinct six-set targets.  The two seam-pair ranks are
\((2,3),(3,2)\), or \((3,3)\).  Exactly \(229\) distinct masks of ranks at
most three occur literally.  In this \(n_5=133\) slice specifically,
\(|H|=4\); the rank-three carrier occurs only in \(n_5=132\) mode D.

At \(n_5=132\), the five exact modes are

\[
\begin{array}{c|c}
\text{mode}&(x_4,s_3,\rho,t_\ast,g)\\ \hline
A&(1,1,4,2,0)\\
B&(0,2,4,2,0)\\
C0&(0,1,4,3,0)\\
C1&(0,1,4,3,1)\\
D&(0,1,3,3,0).
\end{array}
\tag{2.3}
\]

The central segment has length \(333-n_4\) in A, C0, D and \(332-n_4\)
in B, C1.  The source proof establishes that this list is exhaustive.

Finally, order the selected rank-five and rank-six witness intervals by
their left endpoints:

\[
I_j=[\ell_j,r_j],\qquad
J_j=[u_j,v_j],\qquad0\le j<462,
\]

and write

\[
S_j=\operatorname{OR}(I_j),\qquad
U_j=\operatorname{OR}(J_j).
\tag{2.4}
\]

Both \((S_j)\) and \((U_j)\) list their complete Boolean layers exactly
once.

## 3. Audit of the frozen ordered middle forest

The ordered matching and forest asserted in
`K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md` are correct.

### Theorem 3.1 — ordered perfect middle matching

The rank-five offset schedule is

\[
00^*01^*02^*13^*23^*33^*,
\tag{3.1}
\]

with the (12) block empty.  The rank-six schedule is

\[
01^*02^*03^*13^*23^*.
\tag{3.2}
\]

Moreover

\[
I_j\subsetneq J_j,\qquad S_j\subset U_j
\quad(0\le j<462).
\tag{3.3}
\]

Thus (3.3) is a perfect inclusion matching between the complete rank-five
and rank-six layers.  Every coordinate is the unique added coordinate on
exactly

\[
\binom{10}{5}-\binom{10}{4}=42
\tag{3.4}
\]

matching edges.

#### Proof

The (462) endpoints of either selected family occupy (465) physical
positions, so the normalized left and right offsets are nondecreasing and
belong to ({0,1,2,3}).  Every central four-window has rank six and has
state (03).  A nondecreasing offset sequence containing (03) cannot
also contain the incomparable state (12).  Diagonal rank-six states are
impossible because every individual word entry has rank at most five.
This leaves exactly (3.2).

Endpoint saturation pairs prefix witnesses with their common left endpoint,
suffix witnesses with their common right endpoint, and central triples with
the adjacent four-window directed toward the seam.  These pairings preserve
the endpoint index, proving (3.3).  Finally, the difference between the
point degrees of the complete rank-six and rank-five layers is (252-210),
which proves (3.4).  \(\square\)

### Theorem 3.2 — global rainbow linear forest

Delete transitions between distinct nonempty state blocks in (3.1).  The
remaining adjacencies form a spanning linear forest (F_5) in (J(11,5)).
If (c) state blocks are nonempty, then

\[
1\le c\le6,\qquad |E(F_5)|=462-c\ge456.
\tag{3.5}
\]

All upper union colors on these edges are distinct rank-six targets.

#### Proof

Inside states (00,01,02), the physical intervals satisfy

\[
I_j\cup I_{j+1}\subseteq J_j,
\]

while inside (13,23,33),

\[
I_j\cup I_{j+1}\subseteq J_{j+1}.
\]

The two rank-five targets are distinct and lie in a common six-set, so they
are Johnson adjacent and their union equals the displayed (U)-target.
The target (U_j) is used at most once, giving the rainbow assertion.
Deleting state boundaries leaves one path per nonempty block.  \(\square\)

If (f_x) counts forest edges whose matching orientation adds (x), and
(d_x) counts the one omitted matching edge at each component root, then

\[
f_x+d_x=42,\qquad \sum_xd_x=c,\qquad36\le f_x\le42.
\tag{3.6}
\]

These equations will be re-audited in all codimensions in Section 7.

## 4. The lower Johnson lift

Away from the seam and the one C0 low pair, the physical colors form a
four-level Johnson ladder.  In this section an index is **ordinary** only
when every displayed pair and triple avoids the cells incident to \(H\)
and, in mode C0, avoids the extra low pair.

### Lemma 4.1 — successive intersections and unions

For ordinary indices,

\[
B_i=C_{i-1}\cap C_i,\qquad
C_i=T_{i-1}\cap T_i,
\tag{4.1}
\]

and

\[
C_i=B_i\cup B_{i+1},\qquad
T_i=C_i\cup C_{i+1}.
\tag{4.2}
\]

Hence the normal (B)'s, (C)'s and (T)'s form Johnson path forests in
(J(11,4),J(11,5),J(11,6)), respectively.  The (B,C,T) target values are
simple.  At the (C)-level the lower (B)-colors and upper (T)-colors are
globally distinct, and at the (T)-level the lower (C)-colors are
distinct.  The rank-three intersections of consecutive (B)'s need not be
distinct.

#### Proof

Two consecutive distinct normal four-sets have five-set union, so their
intersection has rank three.  Two consecutive distinct five-sets contain
their common normal four-set and have six-set union, giving the first
identity in each rank.  Two consecutive distinct six-sets contain their
common normal five-set; away from (H), their intersection is exactly that
five-set.  \(\square\)

There is also a useful rank-three frame path.  At an internal ordinary
entry put

\[
Q_i=B_{i-1}\cap B_i\in\binom{[11]}3.
\tag{4.3}
\]

Then (A_i\subseteq Q_i).  Consecutive (Q_i,Q_{i+1}) are distinct,
Johnson adjacent, and

\[
Q_i\cup Q_{i+1}=B_i.
\tag{4.4}
\]

Indeed, equality (Q_i=Q_{i+1}) would put both (A_i,A_{i+1}) inside one
three-set, contradicting (|B_i|=4).

Writing

\[
Q_{i+1}=Q_i-\{d_i\}+\{b_i\},
\]

the physical entry satisfies

\[
\boxed{\{b_{i-1},d_i\}\subseteq A_i\subseteq Q_i.}
\tag{4.5}
\]

Thus an ordinary singleton entry forces \(b_{i-1}=d_i\), and its sole
coordinate is an immediate birth-and-death spike.  The converse is not
asserted.  A rank-two entry contains its incoming and outgoing frame labels.
For two consecutive normal swaps in the \(B\)-path, all four removed and
added coordinates are distinct.  Rank six of the three-\(B\) union forbids
immediate re-addition of the coordinate removed by the preceding swap;
membership rules out the other identifications, while (4.4) rules out
immediately removing the coordinate just added.

At (n_5=133), every literal three-set away from the two endpoints and the
three seam entries equals one of the (Q_i).  Consequently this lower walk
visits at least (159) distinct three-sets in seam type ((2,3)), and at
least (158) in seam type ((3,3)).  The walk need not be vertex-simple;
this is precisely where a naive (165)-vertex pigeonhole argument fails.

## 5. A common \(4\to5\to6\) matching at \(n_5=133\)

Let \(\mathcal L_5\) be the \(133\) literal rank-five target values, and put

\[
\mathcal K_4=\binom{[11]}4\setminus\{H\},\qquad
\mathcal S_5=\binom{[11]}5\setminus\mathcal L_5.
\]

Both families have size \(329\).  Let \(\mathcal U_6\) be the \(329\)
rank-six targets matched in (3.3) from the rank-five witnesses in states
(01,02,13,23).

### Theorem 5.1 — exact nested middle matching

There are bijections

\[
\kappa:\mathcal K_4\longrightarrow\mathcal S_5,\qquad
\upsilon:\mathcal S_5\longrightarrow\mathcal U_6
\]

such that

\[
\boxed{K\subset\kappa(K)\subset\upsilon(\kappa(K))}
\tag{5.1}
\]

for every \(K\in\mathcal K_4\).  Both bijections respect the four physical
state blocks.

#### Proof

The upper bijection is the restriction of (3.3).  For the lower bijection,
work blockwise.

* In state (01), match every literal entry of (P_4) to the selected
  rank-five pair beginning there.
* In state (02), match every normal rank-four pair color before (H) to
  the selected rank-five triple beginning on that pair.
* In state (13), use the corresponding common-right matching after (H).
* In state (23), match every literal entry of (Q_4) to the selected
  rank-five pair ending there.

Each inclusion raises the rank by one.  The four lower families are
disjoint and together contain every rank-four target except (H).  The
four upper families are exactly the nonliteral rank-five targets.  Their
block sizes agree, proving bijectivity.  \(\square\)

Let

\[
a_x=|\{S\in\mathcal L_5:x\in S\}|,\qquad
b_x=|\{U\notin\mathcal U_6:x\in U\}|,\qquad
h_x=\mathbf1_{x\in H}.
\]

The lower and upper additions in (5.1) have exact coordinate degrees

\[
\boxed{
e_x^{4\to5}=90-a_x+h_x,\qquad
e_x^{5\to6}=42+a_x-b_x.
}
\tag{5.2}
\]

Indeed, the point degrees of
\(\mathcal K_4,\mathcal S_5,\mathcal U_6\) are
(120-h_x,210-a_x,252-b_x).  Subtracting consecutive degrees proves
(5.2).  In particular

\[
a_x\le90+h_x,\qquad a_x\le b_x\le a_x+42.
\tag{5.3}
\]

The sums in (5.2) are \(329\) in both ranks.  The complementary part of the
perfect matching is an inclusion bijection

\[
\mathcal L_5\longrightarrow
\binom{[11]}6\setminus\mathcal U_6.
\]

Therefore \(b_x-a_x\) counts the complementary matching edges which add
\(x\); this supplies the asserted inequality \(a_x\le b_x\).  All displayed
inequalities retain ample slack and give no contradiction.

The same calculation has an all-subset form.  If \(X\subseteq[11]\),
(k=11-|X|), and (L_{5,X}) and (O_{6,X}) count members of
\(\mathcal L_5\) and the outer rank-six family disjoint from \(X\), then the
numbers of the two matching steps which start disjoint from (X) and add a
coordinate of (X) are

\[
\binom{k}{4}-\binom{k}{5}-h_X+L_{5,X},
\tag{5.4}
\]

and

\[
\binom{k}{5}-\binom{k}{6}-L_{5,X}+O_{6,X},
\tag{5.5}
\]

respectively.  Here (h_X=1) when (H\cap X=\varnothing).  Both expressions
are nonnegative because they count actual integral matching edges.

## 6. The doubly rainbow middle forest and forced color reuse

Let (c_M) be the number of nonempty blocks among (01,02,13,23), and
let (c_O) be the number among (00,33).

### Theorem 6.1 — two-sided rainbow at (n_5=133)

The four middle blocks contain (329) rank-five vertices and

\[
329-c_M
\]

forest edges.  Their rank-six union colors are globally distinct, and
their rank-four intersection colors are also globally distinct.  Hence
exactly (c_M+1) rank-four colors are not used as middle intersections.

#### Proof

Upper distinctness is Theorem 3.2.  In states (01,23), consecutive
rank-five witnesses overlap in a distinct literal rank-four entry of
(P_4,Q_4).  Since the two five-sets are Johnson adjacent, that entry is
their exact intersection.  In states (02,13), the exact intersection is
the shared distinct nonliteral rank-four pair color.  Literal and
nonliteral rank-four targets are disjoint families.  Thus all lower colors
are distinct.  Subtraction from the complete (330)-element layer gives
the last assertion.  \(\square\)

### Theorem 6.2 — unavoidable outer reuse

At (n_5=133), at least (101) outer (00/33) forest edges have a
rank-four intersection color already used by the middle forest.  These
edges reuse at least (26) distinct middle colors.

#### Proof

The outer blocks contain (133) vertices and (133-c_O) edges.  Fix a
rank-four color (K).  Its rank-five supersets are the seven sets
(K\cup\{x\}), (x\notin K).

If (K) is unused in the middle, its outer edges form a forest on at most
seven vertices and hence number at most six.  If (K) is middle-used, two
of its seven supersets are the nonliteral endpoints of the middle edge.
They cannot be outer literal vertices.  The outer (K)-colored forest then
lives on at most five vertices and has at most four edges.

There are only (c_M+1\le5) middle-unused colors.  Hence at most
(6(c_M+1)) outer edges avoid middle colors, and the number of reused edges
is at least

\[
133-c_O-6(c_M+1)\ge133-2-30=101.
\tag{6.1}
\]

At most four such outer edges use one middle color, proving the lower bound
\(\lceil101/4\rceil=26\).  \(\square\)

This is a genuine finite pigeonhole theorem, but reuse is legal.  A
rank-four set can be the intersection of one middle edge and several outer
literal-five edges without repeating any rank-five vertex or rank-six union
color.

### Theorem 6.3 — the one-defect (n_5=132) version

The middle blocks now contain (330) vertices and (330-c_M) edges.
Deleting at most one exceptional edge makes all their rank-four
intersection colors distinct.  Therefore they use at least (329-c_M)
distinct rank-four colors and leave at most (c_M+1) unused.

The sole possible loss is mode-local:

\[
\begin{array}{c|c}
A&\text{the repeated literal rank-four value},\\
B&\text{the isolated lower satellite},\\
C0&\text{the extra low pair},\\
C1&\text{the attached low vertex/embedded rank-five pair},\\
D&\text{no defect}.
\end{array}
\tag{6.2}
\]

Consequently at least

\[
132-c_O-6(c_M+1)\ge100
\tag{6.3}
\]

outer edges reuse middle colors, on at least (25) distinct rank-four
colors.

#### Proof

For (01,23), a normal overlap is a literal rank-four entry; for (02,13),
it is a nonliteral rank-four pair target.  These normal colors are distinct
across and within the two families.  The exact five-mode classification
shows that (6.2) lists every possible nonnormal or repeated overlap.  More
explicitly, A can lose one color only through its sole repeated literal
four-set; B only through the isolated lower satellite; C0 only through its
extra low pair; C1 only through its attached or embedded low overlap; and D
has no loss.  The two seam overlaps lie at the \(02/13\) state boundary and
are not within-block forest edges.  Remove the one possible exceptional
edge and apply the proof of Theorem 6.2 with \(132\) outer vertices.
\(\square\)

Thus a contradiction from this line would require a new theorem limiting
cross-block reuse.  The current Johnson and endpoint axioms force the reuse
rather than forbid it.

## 7. All-codimension run identities

For (X\subseteq[11]), call an entry (X)-free if it is disjoint from
(X), put (k=11-|X|), and define

\[
L_3(k)=\binom{k}{1}+\binom{k}{2}+\binom{k}{3}.
\]

Let (P_j(X)) be the number of (X)-free length-(j) windows in the
central segment.  If (Z_X) is the number of maximal (X)-free runs, then

\[
Z_X=P_1(X)-P_2(X).
\tag{7.1}
\]

More generally, if (R_X^{(j)}) counts (X)-free runs of length at least
(j), then

\[
R_X^{(j)}=P_j(X)-P_{j+1}(X).
\tag{7.2}
\]

### Theorem 7.1 — exact (n_5=133) hierarchy

Let

* (lambda_X) count literal rank-four boundary values disjoint from (X);
* (r_X) count repeated lower entries disjoint from (X);
* (ell_X) count the two seam-pair colors disjoint from (X); and
* \(h_X=\mathbf1_{H\cap X=\varnothing}\).

Then

\[
\boxed{
Z_X=L_3(k)-\binom{k}{4}
     +\lambda_X+h_X+r_X-2\ell_X.
}
\tag{7.3}
\]

#### Proof

Every lower target except the two seam-pair colors occurs literally, and
the remaining positions are repetitions.  Hence

\[
P_1(X)=L_3(k)-\ell_X+r_X.
\]

The rank-four layer is partitioned into the literal boundary values, the
carrier (H), and the ordinary pair colors.  Adding back the two low pair
cells gives

\[
P_2(X)=\binom{k}{4}-\lambda_X-h_X+\ell_X.
\]

Subtract and use (7.1).  \(\square\)

For \(X=\{x\}\), convert disjoint incidence to containing incidence and,
on the following line, let \(\lambda_x,r_x\) denote containing incidence.
This recovers the eleven equations

\[
Z_x+\lambda_x+r_x
=65+\mathbf1_{x\in H}
 +2\mathbf1_{x\in B_s\cap B_{s+1}}.
\tag{7.4}
\]

Thus (7.4) is only the codimension-one section of (7.3).

The elementary binary bound (Z_X\le m-P_1(X)+1) gives

\[
\lambda_X+h_X+2r_X-3\ell_X
\le m+1-2L_3(k)+\binom{k}{4}.
\tag{7.5}
\]

The lower bound (Z_X\ge1), when (k\ge1), and the trivial upper bound
(Z_X\le P_1(X)) give the other two exact projections

\[
\lambda_X+h_X+r_X-2\ell_X
\ge\binom{k}{4}-L_3(k)+1,
\tag{7.6}
\]

\[
\lambda_X+h_X-\ell_X\le\binom{k}{4}.
\tag{7.7}
\]

Let \(R=\sum_xr_x\) be the total rank incidence of the repeated lower
entries.  Summing (7.5) over coordinates gives only the already known
separator rows

\[
4n_4+2R\ge99
\quad\text{or}\quad
4n_4+2R\ge102,
\tag{7.8}
\]

according as the seam type is \((2,3)\) or its reversal, or is \((3,3)\).
The codimension-two
and higher averages have still more slack.  Hence the new content of (7.3)
is its simultaneous pointwise form, not a stronger scalar total.

### Theorem 7.2 — uniform \(n_5=132\) hierarchy

Let

* \(K_X\) counts missing rank-at-most-three target values disjoint from \(X\);
* \(L_X\) counts low pair colors disjoint from \(X\);
* \(v_X\) counts the possible lower vertex outside \(M_3\) which is disjoint
  from \(X\);
* \(\delta_4=\mathbf1_{\rho=4}\);
* \(\lambda_X\) counts distinct literal rank-four values disjoint from
  \(X\), so mode A's repeated occurrence is counted once; and
* \(r_X,h_X,Z_X\) have the analogous disjoint-\(X\) meanings.

Then

\[
\boxed{
Z_X=L_3(k)-\binom{k}{4}
 +\lambda_X+\delta_4h_X-K_X-L_X+r_X-v_X.
}
\tag{7.9}
\]

In the rank-four carrier modes (K_X=L_X).  In mode D,

\[
K_X=L_X+h_X.
\tag{7.10}
\]

#### Proof

The central entries give

\[
P_1(X)=L_3(k)-K_X+r_X-v_X.
\]

The central pairs give

\[
P_2(X)=\binom{k}{4}-\lambda_X-\delta_4h_X+L_X.
\]

Equation (7.9) is their difference.  The identities in (7.10) are exactly
the mode table's list of missing lower targets.  \(\square\)

For a coordinate \(x\), now use lowercase subscripts for *containing*
incidences: \(h_x=\mathbf1_{x\in H}\), and define
\(\lambda_x,r_x,\ell_x,k_x,v_x\) analogously.  The separator inequality
\(Z_x\le o_x+1\) becomes

\[
\lambda_x+\delta_4h_x+2r_x
\ge8+\ell_x+2k_x+2v_x.
\tag{7.11}
\]

After summation, the rank-four carrier modes satisfy

\[
4(n_4-x_4)+2R\ge84+3L+2v,
\tag{7.12}
\]

where \(R=\sum_xr_x\), \(L=\sum_x\ell_x\), and
\(v=\sum_xv_x\).  Mode D satisfies

\[
4n_4+2R\ge106.
\tag{7.13}
\]

The minimum repetition incidence leaves at least \(99\) units of slack
uniformly over the five modes; (7.11)--(7.13) eliminate none.

### 7.3 Outer target-degree transfer

Let \(\mathcal O_5,\mathcal O_6\) be the rank-five and rank-six target
families outside the central normal triples and four-windows.  Both have
size

\[
d=465-m.
\]

If \(O_{j,X}\) counts members of \(\mathcal O_j\) disjoint from \(X\), then

\[
\boxed{
P_3(X)=\binom{k}{5}-O_{5,X}+h_X,\qquad
P_4(X)=\binom{k}{6}-O_{6,X}.
}
\tag{7.14}
\]

These are exact inventories: (P_3) contains the seam (H) in addition to
the ordinary rank-five targets, while every central four-window is a
rank-six target.

For one coordinate, let \(a_x,b_x\) be its degrees in
\(\mathcal O_5,\mathcal O_6\), let \(\lambda_x\) be its degree among the
distinct literal rank-four values, write \(h_x=\mathbf1_{x\in H}\), let
(ell_x,k_x,r_x,v_x) be the corresponding containing incidences, and let
(e_{j,x}) count exact zero runs of length (j).  The
window identities give

\[
\boxed{
e_{1,x}=a_x-26-2\lambda_x-(2\delta_4+1)h_x
 +2\ell_x+k_x-r_x+v_x,
}
\tag{7.15}
\]

\[
\boxed{
e_{2,x}=48+b_x-2a_x+\lambda_x
 +(\delta_4+2)h_x-\ell_x.
}
\tag{7.16}
\]

The fully localized (e_2)-vector is therefore absorbed by an affine
transfer between the two still-free outer target-degree vectors.  Their
coordinate sums make (7.16) an identity, not a contradiction.

For completeness, if (r_j) counts repeated lower entries of rank (j),
(L) is the rank sum of the low pair colors, and (w) is the rank of the
outside lower vertex in B/C1, the exact number (E_1=\sum_xe_{1,x}) is

\[
\begin{array}{c|c}
\text{mode}&E_1\\ \hline
A&58+3L+2r_1+r_2,\\
B,C1&55+3L+2r_1+r_2+w,\\
C0&47+3L+2r_1+r_2,\\
D&71+2r_1+r_2.
\end{array}
\tag{7.17}
\]

This supplies the complete exact short-run spectrum through length three
when combined with the already proved (E_2,E_3) tables.

## 8. Exact fusion with the (42)-label law

Put

\[
D(k)=\binom{k}{5}-\binom{k}{6}.
\tag{8.1}
\]

This is the number, in any perfect inclusion matching of the complete
middle layers, of edges whose rank-five source is disjoint from (X) and
whose added coordinate belongs to (X).

### Theorem 8.1 — central and external crossing functions

For every (X\subseteq[11]),

\[
\boxed{
G_{\rm cen}(X)=R_X^{(3)}-h_X,\qquad
G_{\rm ext}(X)=D(k)+h_X-R_X^{(3)}.
}
\tag{8.2}
\]

Both functions are nonnegative.  Hence

\[
\boxed{h_X\le R_X^{(3)}\le h_X+D(k).}
\tag{8.3}
\]

#### Proof

The number of central matched rank-five sources disjoint from (X) is
(P_3(X)-h_X); the number of their rank-six partners disjoint from (X) is
(P_4(X)).  Inclusion implies that their difference counts exactly the
edges which enter (X).  By (7.2), this difference is
(R_X^{(3)}-h_X).  Subtract it from the complete matching count (D(k))
to obtain the external count.  \(\square\)

For (X={x}),

\[
e_x^{\rm cen}=R_x^{(3)}-1+\mathbf1_{x\in H},\qquad
e_x^{\rm ext}=42-e_x^{\rm cen}.
\tag{8.4}
\]

Thus the (42)-law contributes no independent coordinate inequality after
the run identities are imposed.

There is an exact moment closure.  For \(0\le t\le11\), use the standard
convention \(\binom ab=0\) when \(b<0\) or \(b>a\).

\[
\boxed{
\sum_{|X|=t}R_X^{(3)}
=(m-3)\binom5{t-1}+\binom{11-\rho}{t}.
}
\tag{8.5}
\]

Each central matching edge is counted by exactly
\(\binom5{t-1}\) choices of \(X\).  Also

\[
\binom{11}{t}D(11-t)=462\binom5{t-1}.
\tag{8.6}
\]

Consequently

\[
\boxed{
\sum_{|X|=t}G_{\rm ext}(X)
=(465-m)\binom5{t-1}.
}
\tag{8.7}
\]

Every uniformly weighted all-codimension inequality therefore closes with
exactly the external matching mass.  Averaging (8.3), including all point
and pair averages, cannot yield a contradiction.

### 8.2 Exact integral residual representation

Let

\[
\mathcal C_{\rm ext}
=\{[11]\setminus S:S\in\mathcal O_5\}
\subseteq\binom{[11]}6
\]

be the residual source-complement family, and let

\[
\mathcal D_{\rm ext}
=\{[11]\setminus U:U\in\mathcal O_6\}
\subseteq\binom{[11]}5
\]

be the residual target-complement family.  Both have size \(465-m\).
An external inclusion flag \(S\subset S\cup\{a\}\) is encoded by

\[
C=[11]\setminus S,\qquad
D=[11]\setminus(S\cup\{a\})=C\setminus\{a\}.
\]

Let \(y_{C,a}\in\{0,1\}\), and set \(y_{C,a}=0\) unless

\[
C\in\mathcal C_{\rm ext},\qquad
C\setminus\{a\}\in\mathcal D_{\rm ext},
\]

and the corresponding two selected intervals have the required common
endpoint in the ordered schedule.  The residual matching is exact precisely
when

\[
\sum_{a\in C}y_{C,a}=1
\qquad(C\in\mathcal C_{\rm ext}),
\tag{8.8}
\]

and

\[
\sum_{\substack{C\in\mathcal C_{\rm ext},\,a\in C\\
                  C\setminus\{a\}=D}}
y_{C,a}=1
\qquad(D\in\mathcal D_{\rm ext}).
\tag{8.9}
\]

The central run data force the additional family of equations

\[
\boxed{
D(11-|X|)+h_X-R_X^{(3)}
=\sum_{\substack{C\in\mathcal C_{\rm ext}\\C\supseteq X}}
  \ \sum_{a\in X}y_{C,a}
\quad(X\subseteq[11]).
}
\tag{8.10}
\]

Indeed, the right side counts exactly the residual sources disjoint from
\(X\) whose matching extension enters \(X\).

Equations (8.3) and (8.7) establish only the nonnegativity and binomial
moments necessary for (8.10).  The exact obstruction is the simultaneous
\(0\)-\(1\) feasibility of (8.8)--(8.10) with the endpoint-support zeros;
those constraints are not decided by the moment identities.

## 9. The first surviving fold is at rank seven

Put

\[
W_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}\cup A_{i+4}.
\]

Every ordinary (W_i) has rank seven, because it is the union of two
distinct six-set four-windows containing their common five-set triple.
The seam-centered five-window can have rank (7+\eta), where

\[
0\le\eta\le5-\rho.
\]

### Lemma 9.1 — exact length-four fold criterion

Let \(1\le i\le m-5\), and assume that both flanking five-windows
\(W_{i-1},W_i\) are ordinary rank-seven windows; equivalently, neither
shared triple \(C_i,C_{i+1}\) is the exceptional seam.  Then an exact
coordinate
zero run on its four positions occurs if and only if

\[
\boxed{W_{i-1}=W_i.}
\tag{9.1}
\]

When this occurs, the coordinate is unique.

#### Proof

Write

\[
W_{i-1}=T_i\cup\{\alpha\},\qquad
W_i=T_i\cup\{\beta\}.
\]

A coordinate absent from (T_i) and present in both flanking entries is
exactly a coordinate belonging to both singleton differences.  Thus it
exists exactly when (alpha=\beta), which is equivalent to (9.1).  Since
both differences are singletons, it is unique.  \(\square\)

A fixed seven-set can label at most six central five-windows.  Indeed its
possible four-window colors are its seven six-set facets, all (T_i) are
globally distinct, and the corresponding edges form a subgraph of one
path on those seven vertices.

This does not force a collision.  The central segment has at most

\[
m-4\le329<\binom{11}{7}=330
\]

ordinary five-windows.  More importantly, equality in (9.1) is locally
compatible with every lower rainbow condition.  For a seven-set (W) and
distinct (a,b,c\in W), take

\[
T_0=W\setminus\{a\},\qquad
T_1=W\setminus\{b\},\qquad
T_2=W\setminus\{c\}.
\]

Then \(T_0,T_1,T_2\) are distinct six-sets, both consecutive unions equal
\(W\), their lower five-set intersections are distinct, and those lower
colors meet in the four-set \(W\setminus\{a,b,c\}\).  If desired, choose
that four-set outside the exceptional rank-four colors so that it is
ordinary.  Thus a repeated
rank-seven color is not excluded by the rank-four/rank-five/rank-six
Johnson flags.

This proves that the short-run argument is exhausted at length three:
rank-five and rank-six rainbows localize exact zero runs of lengths two and
three, while the missing rank-seven rainbow permits ordinary length-four
runs.

## 10. What the finite pigeonhole arguments do and do not prove

Several tempting counts now have exact answers.

1.  The complete rank-five endpoint order already gives at least (456)
    distinct rank-six union colors.  This is feasible because the rank-six
    layer has (462) colors.  Equivalently, the induced alternating middle
    graph is a cover by at most six paths.

2.  The (n_5=133) middle subforest is lower-rainbow on all but at most
    five rank-four colors.  This does not extend to a global lower rainbow:
    Theorem 6.2 forces at least (101) outer edges to reuse those colors.

3.  A rank-four color supports at most six forest edges in total, and at
    most four outer edges once it has a middle edge.  These bounds give the
    exact (26)- and (25)-color reuse theorems, but do not overload any
    seven-vertex rank-four clique.

4.  The lower (Q_i)-walk nearly spans (J(11,3)), but a fixed three-set
    has eight rank-four supersets.  Repeated (Q_i)-vertices can therefore
    coexist with distinct rank-four upper colors.

5.  The all-codimension matching capacities do not merely have positive
    slack: their sums equal the external matching mass exactly by (8.7).
    Those moment equalities alone therefore give no contradiction.

6.  Distinct rank-six four-windows imply the interval bound
    
    \[
    \ell-3\le\binom r6
    \tag{10.1}
    \]
    
    for every central interval of (ell\ge4) entries and OR-rank (r).
    Hence intervals of lengths (5,11,32,88,214) have ranks at least
    (7,8,9,10,11), respectively.  All surviving templates respect these
    thresholds.

Thus every scalar rank count, coordinate total, uniform codimension moment,
and local Johnson clique bound remains on the feasible side.

## 11. Exact surviving obstruction and smallest replacement lemmas

The attack leaves two coupled finite objects.

First, at \(n_5=133\) the central physical word must lift the nested Johnson
tower

\[
\text{almost all rank-3 frames}
\longrightarrow
\binom{[11]}4\setminus\{H\}
\longrightarrow
\binom{[11]}5\setminus\mathcal L_5
\longrightarrow
\mathcal U_6,
\tag{11.1}
\]

with the first three levels constrained by actual consecutive unions and
intersections.  Abstract Johnson paths do not supply entries (A_i)
satisfying simultaneously

\[
A_i\cup A_{i+1}=B_i,\qquad
\{b_{i-1},d_i\}\subseteq A_i\subseteq Q_i,
\tag{11.2}
\]

and the literal requirement that \(229\) distinct lower masks occur.  At
\(n_5=132\), the lower lift is mode-dependent: only after deleting the one
possible exceptional edge from Theorem 6.3 is its lower-intersection family
injective.  The common obstruction is physical liftability, not the exact
\(n_5=133\) bijection (11.1).

Second, the residual cut function in (8.10) must be represented by an
integral endpoint-compatible external matching.  The pointwise
nonnegativity, all binomial moments, and all eleven (42)-label equations
are necessary but not sufficient for that integral representation.

The following are clean sufficient replacement lemmas.  They are
**UNPROVED**.

> **Literal-capacity lemma (LC_{133}).**  Under the exact two-seam-pair,
> rank-(4/5/6) rainbow hypotheses of the (n_5=133) template, an actual
> entry lift contains at most (228) distinct masks of ranks at most three.

The template requires (229), so (LC_{133}) would eliminate the
(n_5=133) slice.

> **Boundary reuse lemma (BR_{133}).**  Either prove that at most (100)
> outer forest edges reuse middle colors, or prove that at most (25)
> distinct middle rank-four colors are reused by outer literal-five
> adjacencies in an actual physical lift.

Theorem 6.2 forces (101) edges and (26) colors, so either alternative
would close the slice.  For (n_5=132), the corresponding alternatives are
an upper bound of (99) edges or an upper bound of (24) colors.

> **Residual matching lemma (RM_{11}).**  For every surviving mode, the
> function on the left of (8.10) has no \(0\)-\(1\) representation satisfying
> (8.8)--(8.10) and the ordered endpoint-state support restrictions.

Any one of these statements would advance the proof.  None follows from
the abstract middle-level forest: spanning alternating paths in the middle
levels graph are compatible with the (42)-label laws.  What remains is
the simultaneous physical lift through ranks at most four and the
endpoint-supported residual matching.

## 12. Final theorem-level status

The zero-margin (n_5=133) and (n_5=132) templates are not contradicted.
Every hypothetical survivor nevertheless satisfies all of the following:

1. the global ordered perfect (5\to6) inclusion matching and exact
   (42)-extension law;
2. a spanning upper-rainbow forest in (J(11,5)) with at most six
   components and at least (456) edges;
3. a middle doubly-rainbow subforest which consumes all but at most five
   rank-four intersection colors;
4. at least (101/26) outer-edge/color reuses at (n_5=133), or
   (100/25) at (n_5=132);
5. the all-codimension run identities (7.3) and (7.9), the outer transfer
   laws (7.14)--(7.17), and the exact matching closure (8.2)--(8.10);
6. a lower rank-three frame walk obeying the physical birth/death lift
   (4.5); and
7. a first possible ordinary fold precisely at repeated rank-seven
   five-window unions.

The surviving obstruction is therefore sharply localized by this attack:
repeated lower intersection colors in the outer literal-five paths,
repeated rank-seven upper unions, and the integral endpoint-supported
external matching are the three explicit gates left open by the exact
counting identities.  A contradiction needs a theorem coupling one of
those freedoms back to the actual lower entry labels; no purely scalar or
uniform-incidence argument established here can do so.
