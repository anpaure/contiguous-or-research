# Proportional Gaussian atoms: primitive-cell restitution and quantitative rounding

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computer experiment is used. Every selected state and every deletion below
is a positive literal atom operation.

---

## 0. Outcome

Use the parameters of
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`:

\[
n=2m+1,\qquad W=\binom nm,\qquad
H=\lceil\alpha\sqrt{m\log m}\rceil,\qquad
b=\lfloor m^{3/4}\rfloor,\qquad
p=\left\lfloor\frac Wb\right\rfloor,
\]

where \(1/\sqrt2<\alpha<\sqrt3/2\), and

\[
N_q=\binom n{m+q},\qquad
b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\]

The required absolute leave scale is

\[
\frac p{\sqrt m}=(1+o(1))\frac{W}{m^{5/4}}.
\tag{0.0}
\]

This report proves three positive reductions.

1. **The atom fibre is almost rigid.** The \(b\) middle targets of one
   atom form an induced Johnson path. Once that oriented path is fixed,
   all but \(O(\sqrt m)\) designated slots can be chosen to be literal
   unions or intersections of its middle vertices and hence are fixed by
   the path. Only \(O(\sqrt m)\) boundary slots depend on the completion
   of the coordinate word.
2. **Primitive-cell rounding has an exact matching guarantee.** Suppose
   \(P=p-\ell _0\) atoms are partitioned into positive two-state cells,
   including three-atom redecomposition cells. If \(I\) is the mean
   internal collision of the cells and \(X'\) is the overlap of their
   averaged supports, conditional expectation produces a literal corner,
   and conflict deletion gives a matching of size

   \[
   \boxed{|M|\ge p-\ell _0-I-X'.}
   \tag{0.1}
   \]

   The clipped duplicate residue \(\mathcal R\) in (3.12) satisfies
   \(\mathcal R\le I+X'\) and improves (0.1) to
   \(|M|\ge p-\ell _0-\lfloor\mathcal R\rfloor\). For internally
   disjoint states it has the explicit form

   \[
   R=\sum_v\left[
   \frac12\sum_iw_i(v)-1+
   \prod_i\left(1-\frac{w_i(v)}2\right)
   \right]
   \le \frac X4,
   \]

   and the positive construction gives

   \[
   \boxed{|M|\ge p-\ell _0-\lfloor R\rfloor
   \ge p-\ell _0-R.}
   \tag{0.2}
   \]

   Here \(X\) is the total cross-overlap between doubled supports of
   distinct cells. The simpler collision estimate
   \(|M|\ge p-\ell _0-X/4\) remains valid. Equivalently, (3.15) says that
   \(R=o(p/\sqrt m)\) exactly when the doubled supports have both
   \(o(p/\sqrt m)\) excess above capacity two and
   \(o(p/\sqrt m)\) split-only multiply owned targets. Thus

   \[
   \ell _0+\mathcal R=o(p/\sqrt m),
   \quad\text{or, in the internally disjoint case,}\quad
   \ell _0+R=o(p/\sqrt m),
   \tag{0.3}
   \]

   proves the proportional tight-atom matching lemma and hence constant
   one through its Theorem 2.1.
3. **The first nontrivial projection is a clipped diamond problem.** An
   atom matching with leave \(o(p/\sqrt m)\) projects to a fixed
   four-partite, four-uniform diamond matching leaving \(o(W/\sqrt m)\)
   upper colours. A positive clipped-restitution construction from any
   gap-two inclusion matching loses at most

   \[
   \mathfrak C(M)=\sum_C(d_M(C)-2)_+.
   \tag{0.4}
   \]

   Therefore \(\min_M\mathfrak C(M)=o(W/\sqrt m)\) is a concrete
   sufficient first quantitative restitution target.

For an atom-level legal primitive triple whose two endpoints are internally
atom-disjoint, there is no intrinsic middle-coordinate rounding penalty.
Equality of its two middle-owner cells supplies the middle part of the gap,
but not the nonmiddle estimates \(R=o(p/\sqrt m)\) or
\(X=o(p/\sqrt m)\). A three-wreath trade does not automatically become
such a cell after cutting: block alignment and internal atom disjointness
must also be proved. Proposition 2.4 gives a literal local witness: two
atoms can be completely middle-disjoint and still share a forced
depth-two target. The required aggregate cross-cell estimates remain
unproved. No claim of constant one is made.

---

## 1. Exact shallow quotas

Write

\[
W=pb+r,\qquad 0\le r<b.
\tag{1.1}
\]

Since \(p\) is exponentially larger than \(b\),

\[
\frac Wp=b+\frac rp=b+o(1).
\tag{1.2}
\]

### Lemma 1.1 -- the first four quotas

For all sufficiently large \(m\),

\[
\boxed{b_0=b_1=b,\qquad b_{-1}=b_2=b-1.}
\tag{1.3}
\]

#### Proof

Binomial symmetry gives \(N_0=N_1=W\), so (1.2) gives
\(b_0=b_1=b\). Also

\[
N_{-1}=N_2=\frac m{m+2}W.
\]

Consequently

\[
\frac{N_2}{p}
=b-\frac{2b}{m+2}+\frac{rm}{p(m+2)}.
\]

Since \(r/p\le b/p=o(b/m)\),

\[
b-\frac{N_2}{p}
=\frac{2b}{m+2}-\frac{rm}{p(m+2)}
=(2+o(1))\frac bm\in(0,1).
\]

Hence \(N_2/p\in(b-1,b)\), proving (1.3). \(\square\)

For later use, the exact central ratio has the product bound

\[
\boxed{
\frac{N_h}{W}
=\prod_{j=1}^{h}
\frac{m+2-j}{m+j}
\le
\exp\!\left(-\frac{h(h-1)}{m+1}\right).
}
\tag{1.4}
\]

Indeed the \(j=1\) factor is one, and for \(a=j-1\),

\[
\log\frac{m+1-a}{m+1+a}
=-2\operatorname{arctanh}\frac a{m+1}
\le-\frac{2a}{m+1}.
\]

---

## 2. The exact atom fibre over its middle path

Let

\[
x=(x_0,\ldots,x_{m+b+H-1})
\]

be an injective atom word, and put

\[
T_i=A_{i,0}(x)=\{x_i,\ldots,x_{i+m-1}\},\qquad 0\le i<b.
\tag{2.1}
\]

### Lemma 2.1 -- middle-path rigidity

The sets \(T_0,\ldots,T_{b-1}\) induce exactly the path \(P_b\) in
\(J(n,m)\). More precisely,

\[
|T_i\cap T_j|=m-|i-j|.
\tag{2.2}
\]

Hence their unlabelled family determines their linear order up to reversal.
For the chosen orientation,

\[
\boxed{
A_{i,h}=\bigcup_{j=0}^{h}T_{i+j}\quad(i+h<b),
}
\tag{2.3}
\]

and

\[
\boxed{
A_{i,-h}=\bigcap_{j=0}^{h}T_{i-j}\quad(i\ge h).
}
\tag{2.4}
\]

#### Proof

Since \(b<m\), two length-\(m\) position intervals whose starts differ
by \(d<b\) overlap in exactly \(m-d\) positions. Thus two middle targets
are Johnson-adjacent exactly when their indices differ by one, proving the
first assertion and the order reconstruction.

The union in (2.3) is the position interval from \(x_i\) through
\(x_{i+m+h-1}\), while the intersection in (2.4) is the interval from
\(x_i\) through \(x_{i+m-h-1}\). These are exactly the designated targets.
\(\square\)

For prescribed start sets \(I_q\), define the number of boundary slots

\[
\begin{aligned}
F(I)={}&
\sum_{h=1}^{H+1}
|I_h\cap\{b-h,\ldots,b-1\}|\\
&+\sum_{h=1}^{H}
|I_{-h}\cap\{0,\ldots,h-1\}|.
\end{aligned}
\tag{2.5}
\]

All designated slots outside this list are fixed by the oriented middle
path through (2.3)--(2.4). Thus two completions of the same oriented path
can differ in at most \(F(I)\) labelled target slots and in at most
\(2F(I)\) coordinates of their incidence vectors.

### Theorem 2.2 -- boundary-minimal proportional starts

The start sets can be chosen so that

\[
\boxed{
F(I)=F_{\min}:=
\sum_{h=1}^{H+1}(b_h-b+h)_+
+\sum_{h=1}^{H}(b_{h+1}-b+h)_+
=O\!\left(\frac{m^2}{b^2}\right)=O(\sqrt m).
}
\tag{2.6}
\]

#### Proof

At upper depth \(h\), exactly \(b-h\) starts have \(i+h<b\). Choosing
as many of those as possible leaves precisely

\[
(b_h-(b-h))_+=(b_h-b+h)_+
\]

boundary starts. At lower depth \(-h\), exactly \(b-h\) starts have
\(i\ge h\). Binomial symmetry gives \(b_{-h}=b_{h+1}\), so the minimum
is the second positive part in (2.6). Choices at different depths are
independent in the proportional-atom definition, hence the minima are
simultaneously attainable.

It remains to bound the sum. From (1.2) and (1.4),

\[
b_h\le(b+o(1))
\exp\!\left(-\frac{h(h-1)}{m+1}\right).
\tag{2.7}
\]

Put \(h_0=\lceil5m/b\rceil\). For
\(h_0\le h\le\sqrt m\), use
\(1-e^{-y}\ge y/3\) for \(0\le y\le1\) to get

\[
b-b_h\ge
\frac{b h(h-1)}{3(m+1)}-o(1)\ge h
\]

for large \(m\). For \(h\ge\sqrt m\), the left side is at least a fixed
positive multiple of \(b\), whereas \(h\le H+1=o(b)\). Therefore every
positive part in (2.6) vanishes for \(h\ge h_0\). For smaller \(h\), each
positive part is at most \(h\), so

\[
F_{\min}\le2\sum_{h<h_0}h=O(h_0^2)
=O(m^2/b^2)=O(\sqrt m).
\]

\(\square\)

### Corollary 2.3 -- immutable adjacent colours

Use \(I_1=\{0,\ldots,b-1\}\) and
\(I_{-1}=\{1,\ldots,b-1\}\), as permitted by (1.3). For
\(0\le i<b-1\), put

\[
U_i=T_i\cup T_{i+1},\qquad L_i=T_i\cap T_{i+1}.
\tag{2.8}
\]

Then

\[
U_i=A_{i,1},\qquad L_i=A_{i+1,-1}.
\tag{2.9}
\]

Consequently every proportional-atom matching projects to a family of
vertex-disjoint middle paths whose edges are simultaneously rainbow in
their union colours \(U_i\) and intersection colours \(L_i\). These
\(2(b-1)\) colours per path are invariant under every completion of the
fixed oriented middle path.

### Proposition 2.4 -- literal middle-disjointness does not control depth two

For every sufficiently large \(m\), there are two literal atom words whose
entire designated middle-target families are disjoint but which have the
same designated depth-two target. Thus disjoint middle ownership alone
does not make the nonmiddle residue in Section 3 vanish pointwise.

#### Proof

Fix an \((m+2)\)-set \(S\) and eight distinct elements
\(1,\ldots,8\in S\). The three \(m\)-sets obtained by omitting

\[
\{1,2\},\quad\{2,3\},\quad\{3,4\}
\]

form a literal three-window sliding fragment: order the first \(m+2\)
word positions so that the last two letters are \(1,2\), the first two
are \(3,4\), and the remaining letters of \(S\) occupy the intervening
positions. Its first three length-\(m\) windows are exactly the displayed
sets, and their common length-\((m+2)\) union is \(S\). Do the same with

\[
\{5,6\},\quad\{6,7\},\quad\{7,8\}.
\]

The six middle sets are distinct. Since \(2(b+H-2)<m-1\) for all large
\(m\), extend the two words after their first \(m+2\) positions using
disjoint lists from \([n]\setminus S\), each of length \(b+H-2\).
For a middle window starting at \(i\ge3\), exactly \(i-2\) of its letters
belong to its extension list. Hence such a window cannot equal a window
of the other word, whose nonempty extension part lies in a disjoint list;
it also cannot equal any of the first three windows, which lie inside
\(S\). The first three windows were already distinct across the two words.
Thus all \(b\) designated middle targets of one word are disjoint from all
\(b\) of the other, while

\[
A_{0,2}^{(1)}=S=A_{0,2}^{(2)}.
\]

Taking \(I_2=\{0,\ldots,b-2\}\), as in Section 4, designates this shared
target.
\(\square\)

---

## 3. Positive primitive-cell rounding

Let \(\mathcal V\) be the disjoint union of all target parts of the
proportional atom hypergraph. Suppose \(P=p-\ell _0\) atoms are organized
into cells \(i=1,\ldots,s\). Cell \(i\) has two positive states
\(\mathcal A_i^0,\mathcal A_i^1\), each containing the same number of
physical atoms. Write

\[
r_i=|\mathcal A_i^0|=|\mathcal A_i^1|,
\qquad \sum_{i=1}^s r_i=P=p-\ell _0.
\tag{3.0}
\]

Frozen atoms may be treated as degenerate cells with two identical states.

For \(v\in\mathcal V\), let

\[
a_i^\epsilon(v)
=\#\{e\in\mathcal A_i^\epsilon:v\in e\},\qquad
\bar a_i(v)=\frac{a_i^0(v)+a_i^1(v)}2.
\tag{3.1}
\]

Define

\[
I=\frac12\sum_{i,v}
\left[
\binom{a_i^0(v)}2+
\binom{a_i^1(v)}2
\right]
\tag{3.2}
\]

and

\[
X'=\sum_{i<j}\langle\bar a_i,\bar a_j\rangle
=\sum_v\sum_{i<j}\bar a_i(v)\bar a_j(v).
\tag{3.3}
\]

### Theorem 3.1 -- conditional-expectation restitution rounding

There is a literal choice of one state from every cell whose total target
pair collision is at most

\[
\boxed{
\mathsf C
:=\sum_{v\in\mathcal V}\binom{\mu(v)}2
\le I+X'.
}
\tag{3.4}
\]

Deleting at most \(I+X'\) selected atoms leaves an atom matching. Hence

\[
\boxed{|M|\ge p-\ell _0-I-X'.}
\tag{3.5}
\]

In particular, if

\[
\ell _0+I+X'=o(p/\sqrt m),
\tag{3.6}
\]

then the matching hypothesis of Theorem 2.1 in the proportional-atom
reduction holds.

#### Proof

Choose the cell states independently and fairly. Coordinatewise,

\[
\binom{\sum_i a_i(v)}2
=\sum_i\binom{a_i(v)}2
+\sum_{i<j}a_i(v)a_j(v).
\]

The expectation of the first sum is (3.2), and independence makes the
expectation of the second sum (3.3). Therefore

\[
\mathbb E\mathsf C=I+X'.
\]

Fix the cell choices one at a time, always choosing a state whose
conditional expected final collision is no larger than the current
conditional expectation. This produces a positive integral corner
satisfying (3.4). It is exactly a quadratic restitution rule against the
current load plus the averaged untouched load of the unresolved cells.

Form the conflict graph on the selected atoms, joining two atoms when they
share at least one target. Every conflict-graph edge is counted at least
once in \(\mathsf C\), so the graph has at most \(\mathsf C\) edges.
Choosing one endpoint of every conflict edge gives a vertex cover of size
at most \(\mathsf C\). Delete that cover. The remaining atoms are pairwise
target-disjoint, proving (3.5)--(3.6). \(\square\)

### Corollary 3.2 -- exact doubled-support form

Assume that each state \(\mathcal A_i^\epsilon\) is internally an atom
matching. Put

\[
w_i(v)=a_i^0(v)+a_i^1(v)\in\{0,1,2\}
\tag{3.7}
\]

and

\[
X=\sum_v\sum_{i<j}w_i(v)w_j(v).
\tag{3.8}
\]

Then \(I=0\), \(X'=X/4\), and Theorem 3.1 gives

\[
\boxed{|M|\ge p-\ell _0-X/4.}
\tag{3.9}
\]

Thus pairwise disjoint doubled cell supports give an exact matching, and
total doubled-support cross-overlap \(X=o(p/\sqrt m)\) gives the required
quantitative matching.

There is an exact parity-restitution identity behind (3.9). Put

\[
z_i=a_i^1-a_i^0,\qquad
t(v)=\sum_iw_i(v),\qquad
O=|\{v:t(v)\text{ is odd}\}|,
\]

\[
B=\sum_v\left\lfloor\frac{(t(v)-1)^2}{4}\right\rfloor,
\qquad
\Gamma=4B+\sum_i\|z_i\|_2^2-O.
\tag{3.10}
\]

Then

\[
\boxed{\Gamma=2X.}
\tag{3.11}
\]

Indeed, at one coordinate let
\(s=|\{i:w_i=1\}|=\sum_i z_i^2\). A parity split gives

\[
4\left\lfloor\frac{(t-1)^2}{4}\right\rfloor+s-
\mathbf1_{\{t\text{ odd}\}}
=t^2-2t+s.
\]

Since \(w_i^2-2w_i=-1\) exactly when \(w_i=1\), the last expression is

\[
2\sum_{i<j}w_iw_j.
\]

Summing proves (3.11). Thus the parity identity and the elementary
conditional-expectation proof give exactly the same pair-collision
certificate.

### Theorem 3.3 -- clipped duplicate-restitution rounding

Under the hypotheses of Theorem 3.1, put

\[
\boxed{
\mathcal R=\sum_{v\in\mathcal V}\left[
\sum_i\bar a_i(v)-1+
\prod_i\frac{
\mathbf1_{\{a_i^0(v)=0\}}+
\mathbf1_{\{a_i^1(v)=0\}}}{2}
\right].
}
\tag{3.12}
\]

There is a literal choice of one state from every cell for which deleting
at most \(\lfloor\mathcal R\rfloor\) selected atoms leaves an atom
matching. Consequently

\[
\boxed{
|M|\ge p-\ell _0-\lfloor\mathcal R\rfloor
\ge p-\ell _0-\mathcal R.
}
\tag{3.13}
\]

Moreover \(0\le\mathcal R\le I+X'\). Under the internally matching hypotheses
of Corollary 3.2, write \(R=\mathcal R\). Then

\[
R=\sum_{v\in\mathcal V}\left[
\frac{t(v)}2-1+
\prod_i\left(1-\frac{w_i(v)}2\right)
\right]
\le\frac X4,
\]

so (3.13) becomes

\[
|M|\ge p-\ell _0-\lfloor R\rfloor
\ge p-\ell _0-R.
\]

Thus the clipped theorem sharpens both collision certificates, and the
inequalities can be strict.

#### Proof

Choose the cell states independently and fairly, and let \(L(v)\) be the
selected load at target \(v\). The cell contributions are independent,
whether or not a state is internally disjoint, and

\[
\begin{aligned}
\mathbb E(L(v)-1)_+
&=\mathbb EL(v)-\Pr(L(v)\ge1)\\
&=\sum_i\bar a_i(v)-1+\Pr(L(v)=0)\\
&=\sum_i\bar a_i(v)-1+
\prod_i\frac{
\mathbf1_{\{a_i^0(v)=0\}}+
\mathbf1_{\{a_i^1(v)=0\}}}{2}.
\end{aligned}
\]

Therefore the expected duplicate excess

\[
D=\sum_v(L(v)-1)_+
\]

is exactly \(\mathcal R\). Conditional expectation selects a literal state
corner with \(D\le\mathcal R\). At each target mark all but one of its
incident selected atoms. The union of all marked atoms has cardinality at
most \(D\), and deleting that union leaves load at most one at every
target. Since \(D\) is integral, this proves (3.13).

Pointwise,

\[
(L(v)-1)_+\le\binom{L(v)}2.
\]

Taking expectations and using the computation in Theorem 3.1 gives
\(\mathcal R\le I+X'\). If both cell states are internally matchings, then
\(a_i^\epsilon(v)\in\{0,1\}\), so

\[
\bar a_i(v)=\frac{w_i(v)}2,
\qquad
\frac{
\mathbf1_{\{a_i^0(v)=0\}}+
\mathbf1_{\{a_i^1(v)=0\}}}{2}
=1-\frac{w_i(v)}2.
\]

This gives the displayed formula for \(R\), and Corollary 3.2 gives
\(R\le X/4\). \(\square\)

The clipped residue has an exact support form. Put

\[
f_v=|\{i:w_i(v)=2\}|,\qquad
s_v=|\{i:w_i(v)=1\}|,
\qquad t(v)=2f_v+s_v.
\]

The summand \(r_v\) of this internally matching specialization \(R\) is

\[
\boxed{
r_v=\frac{(t(v)-2)_+}{2}
+\mathbf1_{\{f_v=0,\ s_v\ge2\}}2^{-s_v}.
}
\tag{3.14}
\]

Indeed a cell with \(w_i(v)=2\) hits \(v\) in both states, one with
\(w_i(v)=1\) hits it in exactly one state, and all other cells avoid it.
Thus the product in (3.12) is zero when \(f_v>0\), is \(2^{-s_v}\)
when \(f_v=0\), and (3.14) follows by separating \(s_v=0,1\).

Define

\[
A=\sum_v(t(v)-2)_+,
\qquad
S=|\{v:f_v=0,\ s_v\ge2\}|.
\]

Then

\[
\boxed{
\frac{A+S}{4}\le R
=\frac A2+
\sum_{\substack{v:f_v=0\\s_v\ge2}}2^{-s_v}
\le\frac A2+\frac S4
\le\frac{A+S}{2}.
}
\tag{3.15}
\]

In particular the same positive selection-and-deletion construction obeys

\[
\boxed{|M|\ge p-\ell _0-\frac A2-\frac S4.}
\]

For the lower bound, a split-only coordinate with \(s_v=2\) contributes
exactly \(1/4\); when \(s_v\ge3\), its contribution is at least
\((s_v-1)/4\); and every other positive contribution is
\((t(v)-2)/2\). Thus \(R=o(p/\sqrt m)\) is equivalent, for this fair-state
certificate, to

\[
A=o(p/\sqrt m)\quad\text{and}\quad S=o(p/\sqrt m).
\tag{3.16}
\]

### Corollary 3.4 -- atom-level primitive triples

Suppose each cell consists of two literal decompositions of the same
three-atom middle-owner cell, distinct cells have disjoint middle-owner
cells, and both endpoint decompositions are atom matchings. Then the cell
meets every hypothesis of Corollary 3.2. Its middle coordinates contribute
nothing to \(X\): there \(w_i=2\) on its own cell and zero on every other
cell.

Consequently primitive triples have zero intrinsic middle restitution
cost. One simple sufficient cross-cell certificate is

\[
\boxed{
\sum_{v\notin\text{middle}}
\sum_{i<j}w_i(v)w_j(v)=o(p/\sqrt m).
}
\tag{3.17}
\]

Under (3.17) and \(\ell _0=o(p/\sqrt m)\), conditional expectation and
conflict deletion construct the desired atom matching. Same-middle-union
legality verifies that the omitted middle contribution to \(X\) is zero,
but does not by itself bound the displayed nonmiddle contribution. This is
an explicit sufficient untouched-cell term. The stronger sufficient
certificate is the nonmiddle part of \(R=o(p/\sqrt m)\), equivalently the
two conditions in (3.16). Neither certificate is necessary for a specially
coordinated signing.

The hypothesis is atom-level. A same-middle-union trade of three complete
wreath rows supplies it only after one additionally aligns the proportional
block cuts, proves that each three-atom endpoint is internally disjoint in
every target part, and pairs the resulting atom cells without loss. None of
those lifting assertions is automatic from row-level ownership legality.

---

## 4. The fixed four-uniform diamond projection

Choose

\[
I_2=\{0,\ldots,b-2\},
\tag{4.1}
\]

which has the required size \(b_2=b-1\). For an atom word and
\(0\le i<b-1\), put

\[
S_i=A_{i,2},\quad
C_i^0=A_{i,1},\quad
C_i^1=A_{i+1,1},\quad
R_i=A_{i+1,0}.
\tag{4.2}
\]

Then

\[
R_i=C_i^0\cap C_i^1,qquad
S_i=C_i^0\cup C_i^1.
\tag{4.3}
\]

Define \(\mathcal D_m\) with four parts

\[
\mathcal U=\binom{[n]}{m+2},\quad
\mathcal L=\binom{[n]}m,\quad
\mathcal M_0,\mathcal M_1
\]

where \(\mathcal M_0,\mathcal M_1\) are role-labelled copies of
\(\binom{[n]}{m+1}\). Its edges are

\[
\left(
S, S\setminus\{a,b\},
(S\setminus\{a\})^{(0)},
(S\setminus\{b\})^{(1)}
\right),qquad a\ne b\in S.
\tag{4.4}
\]

### Theorem 4.1 -- quantitative diamond necessity

An atom matching of size \(s\) projects to a \(\mathcal D_m\)-matching
of size \(s(b-1)\). In particular, if \(s=p-t\) with
\(t=o(p/\sqrt m)\), its uncovered \(\mathcal U\)-vertices number

\[
\boxed{
N_2-(p-t)(b-1)<p+t(b-1)=o(W/\sqrt m).
}
\tag{4.5}
\]

#### Proof

Inside one atom, consecutive diamonds use the same underlying middle
\((m+1)\)-set only in opposite role clones; all their other entries are
distinct. Between atoms, target disjointness gives disjoint entries in all
four parts. Hence the projection is a matching.

Since \(b_2=b-1\), the floor remainder gives
\(0\le N_2-p(b-1)<p\), proving the first inequality in (4.5). Also

\[
p=O(W/m^{3/4})=o(W/\sqrt m),
\]

and

\[
t(b-1)=o\!\left(\frac{pb}{\sqrt m}\right)=o(W/\sqrt m).
\]

\(\square\)

### Lemma 4.2 -- degrees, codegrees, and the fractional point

The exact degrees are

\[
d_{\mathcal U}=(m+2)(m+1),\qquad
d_{\mathcal L}=d_{\mathcal M_0}=d_{\mathcal M_1}=m(m+1).
\tag{4.6}
\]

The nonzero pair codegrees, in the order

\[
(\mathcal U,\mathcal L),\quad
(\mathcal U,\mathcal M_j),\quad
(\mathcal L,\mathcal M_j),\quad
(\mathcal M_0,\mathcal M_1),
\]

are respectively

\[
2,\qquad m+1,\qquad m,\qquad 1
\tag{4.7}
\]

when the two vertices are compatible, and zero otherwise. Giving every
edge weight \(1/d_{\mathcal U}\) saturates every \(\mathcal U\)-vertex and
loads every vertex of each other part by exactly

\[
\frac m{m+2}.
\tag{4.8}
\]

#### Proof

For fixed \(S\), choose the ordered pair \((a,b)\). For fixed
\(R\in\mathcal L\), choose an ordered pair from its \(m+1\)-element
complement. For a fixed role-labelled middle facet, choose the missing
outside element and the removed inside element. These give (4.6).

A compatible \((S,R)\) leaves two orientations. A compatible upper or
lower colour together with one role-labelled middle facet leaves,
respectively, \(m+1\) or \(m\) choices. Two compatible role-labelled
middle facets determine their union and intersection uniquely. This proves
(4.7), and degree division proves (4.8). \(\square\)

The fractional point has no capacity defect. The following theorem gives
an exact positive integral construction from one clipped statistic.

### Theorem 4.3 -- clipped restitution produces a diamond matching

Let \(G\) be the bipartite gap-two inclusion graph from \(\mathcal U\) to
\(\mathcal L\). Choose a matching \(M\) saturating \(\mathcal U\), and
for \(C\in\binom{[n]}{m+1}\) let \(d_M(C)\) be the number of selected
intervals \([R,S]\) having \(C\) as one of their two middle facets. Put

\[
\mathfrak C(M)=\sum_C(d_M(C)-2)_+.
\tag{4.9}
\]

Then \(\mathcal D_m\) has a matching of size at least

\[
\boxed{N_2-\mathfrak C(M).}
\tag{4.10}
\]

In particular,

\[
\boxed{
\operatorname{match}(\mathcal D_m)
\ge N_2-\min_M\mathfrak C(M).
}
\tag{4.11}
\]

#### Proof

The gap-two graph is biregular. Its degrees at \(\mathcal U\) and
\(\mathcal L\) are \(\binom{m+2}{2}\) and \(\binom{m+1}{2}\),
respectively. Degree counting gives Hall's condition, so a matching
saturating \(\mathcal U\) exists.

Project each selected \((R,S)\) to the Johnson edge joining the two middle
facets strictly between \(R\) and \(S\). Its middle degree is \(d_M\).
While a vertex has degree at least three, delete one incident projected
edge. Every deletion reduces \(\mathfrak C\) by at least one, so at most
\(\mathfrak C(M)\) edges are deleted before the projected graph has maximum
degree two.

Orient every path and cycle component consistently. Every middle set now
occurs at most once as a tail and at most once as a head. Put tails in role
zero and heads in role one. The selected upper and lower colours remain
distinct because they came from the matching \(M\). The oriented diamonds
therefore form a \(\mathcal D_m\)-matching of the stated size. \(\square\)

The associated quadratic restitution has an exact decomposition. Let

\[
\Phi(M)=\sum_C\binom{d_M(C)}2,qquad
z(M)=|\{C:d_M(C)=0\}|.
\]

Since \(\sum_Cd_M(C)=2N_2\),

\[
\boxed{
\Phi(M)-(2N_2-W)
=z(M)+
\sum_{d_M(C)\ge3}\binom{d_M(C)-1}{2}.
}
\tag{4.12}
\]

Indeed subtracting \(\sum_Cd_M(C)-W\) from \(\Phi\) gives one unit at
degree zero, zero at degrees one and two, and
\(\binom{d-1}{2}\) at degree \(d\ge3\). The right side of (4.12)
dominates \(\mathfrak C(M)\). Thus the quadratic optimum is a stronger
sufficient target, while (4.9) is the direct clipped statistic used by the
deletion construction.

If a full \(\mathcal U\)-matching has maximum middle degree two, then

\[
2z(M)+|\{C:d_M(C)=1\}|
=2(W-N_2)=\frac{4W}{m+2}=o(W/\sqrt m).
\tag{4.13}
\]

Therefore the unavoidable endpoint/isolated residue already lies below the
required scale. A sufficient unproved quantitative diamond gate is

\[
\boxed{
\min_M\mathfrak C(M)=o(W/\sqrt m).
}
\tag{4.14}
\]

Even (4.14) is only the first projection of the atom theorem: its directed
diamond components must still concatenate into length-\(b\) paths with
distinct removed coordinates, distinct added coordinates, compatible
initial facets, and all depths \(|q|\le H+1\).

---

## 5. A positive central construction without fixed-block fragmentation

The fixed size \(b\) need not create a loss at the literal-word level.

### Theorem 5.1 -- variable blocks cover both middle ranks exactly

Let an exact wreath factor partition the middle layer into

\[
B_0=\frac Wn
\]

cyclic rows. Put \(a=\lfloor n/b\rfloor\), and divide \(n\) by \(a\):
write \(n=aq+r_0\), \(0\le r_0<a\). Each cyclic row can be partitioned into
\(a\) consecutive blocks, \(r_0\) of length \(q+1\) and the rest of
length \(q\). Thus every block length satisfies

\[
\ell\in\left\{\left\lfloor\frac na\right\rfloor,
\left\lceil\frac na\right\rceil\right\}
=b+O(b^2/n)=b+O(\sqrt m),
\tag{5.1}
\]

whose lengths sum exactly to \(n\). Emitting the usual
\(\ell+2H+1\) base windows for every block has total length

\[
\boxed{
W+(2H+1)B_0a
=W+O(HW/b)=W+o(W).
}
\tag{5.2}
\]

It covers ranks \(m\) and \(m+1\) exactly.

#### Proof

Partition a cyclic list of \(n\) starts into \(a\) consecutive pieces as
evenly as possible. Since \(n/a=b+O(b^2/n)\), (5.1) follows. The principal
block lengths sum to \(nB_0=W\); the repeated initialization/seam cost is
the second term in (5.2), and \(H/b=o(1)\).

Moreover \(\ell+H=o(m)\), so the required coordinate segment has length
strictly less than \(n\) and is injective even when read across the cyclic
cut.

The exact wreath factor covers every length-\(m\) interval once. In an odd
cycle, the complement of every length-\((m+1)\) interval is a length-\(m\)
interval with a fixed cyclic shift of its start. Hence the same rows also
cover every rank-\((m+1)\) target once. Cutting the starts into blocks loses
none of them. \(\square\)

This theorem is a literal construction, not a matching in the original
fixed-\(b\) hypergraph. Its role is to remove fragmentation as a separate
source of loss. The first new shadow beyond it is exactly the diamond/
first-shadow gate in Section 4.

---

## 6. Exact proved and conditional boundary

The following statements are proved.

1. Proportional starts may be chosen so that only \(O(\sqrt m)\) target
   slots per atom depend on completion of an oriented middle path.
2. The \((m-1)\)-intersection and \((m+1)\)-union colours of every middle-
   path edge are completion-rigid.
3. Two-state positive cells round by conditional expectation, and conflict
   deletion gives (3.5). For internally disjoint cells the sharper clipped
   deletion theorem gives (3.13), with \(R\le X/4\). Primitive-triple
   middle coordinates have zero contribution to both certificates.
4. The full atom theorem quantitatively implies the diamond matching in
   (4.5).
5. Any \(\mathcal U\)-saturating gap-two inclusion matching gives a
   positive diamond matching after at most \(\mathfrak C(M)\) clipped
   deletions.
6. Variable wreath blocks remove the apparent one-fixed-block loss while
   covering the two middle ranks exactly in \(W+o(W)\) literal length.

The desired proportional atom matching follows from the concrete positive
construction target

\[
\boxed{
P=p-\ell _0\text{ atoms arranged into positive two-state cells with }
\ell _0+\mathcal R=o(p/\sqrt m).
}
\tag{6.1}
\]

The simpler condition \(\ell _0+I+X'=o(p/\sqrt m)\) implies (6.1).

For internally disjoint primitive triples, the sharper sufficient
certificate is

\[
\boxed{\ell _0+R=o(p/\sqrt m),}
\tag{6.2}
\]

and the simpler condition

\[
\boxed{\ell _0+X/4=o(p/\sqrt m)}
\tag{6.3}
\]

implies (6.2). These are sufficient certificates for the displayed
fair-state rounding, not necessary conditions for every coordinated
signing.

What remains unproved is the construction of cells satisfying (6.1) or
(6.2). The same-middle-union condition guarantees their exact middle
ownership, but the forced targets in (2.3)--(2.4), already including the
two colours in (2.8), contribute to cross-cell overlap and cannot be changed
by internal completion choices. Genuine middle-path refactorings must make
those forced supports nearly disjoint; the \(O(\sqrt m)\) completion fibre
can then be rounded separately.

Thus, once genuine atom-level primitive cells satisfying Corollary 3.4 are
supplied, their endpoint choices compose under the sharp positive rounding
theorem. Middle-owner equality alone does not verify the untouched-cell
cross-overlap hypothesis. A concrete quantitative first test is (4.14), and
the strongest positive fair-state certificate proved here is (6.2).
