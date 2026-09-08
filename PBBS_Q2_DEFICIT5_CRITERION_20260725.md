# Exact deficit-five criterion for the second PBBS turn shadow

Date: 2026-07-25

No computation or external input is used here.

## 0. Result

Let \(n=2m+1\), let \(f\) be the canonical PBBS permutation of
\(\binom{[n]}m\), and put \(g=f^2\). For a \(g\)-orbit write its vertices
\(A_i,A_{i+2},A_{i+4},\ldots\), and define

\[
T_i=A_i\cap A_{i+2}\cap A_{i+4}.
\]

The no-gap-three theorem implies pointwise that \(|T_i|=m-2\). The
remaining question is whether every \(S\in\binom{[n]}{m-2}\) occurs.

This note gives an exact answer criterion in terms of the five forward and
five reverse unmatched zeros of the deficit-five word of \(S\), and then
proves that the criterion is always satisfied. Consequently:

\[
\boxed{\text{Every rank-\((m-2)\) set occurs as a canonical PBBS
second turn color.}}
\]

The proof is local. Expand a coordinate that is unmatched in both
directions as two consecutive symbols \(C,A\). A five-by-five run lemma
selects an \(A\to C\) transition having at most two opposite-type marks
in each relevant adjacent gap. That good transition canonically supplies
two consecutive step-two PBBS edges whose three-state intersection is the
prescribed \(S\).

## 1. The deficit-five data

Fix

\[
S\in\binom{[n]}{m-2},\qquad Z=[n]\setminus S,
\]

so \(|Z|=m+3\). Let \(U_+(S)\) and \(U_-(S)\) be the five forward and
reverse unmatched zeros of the cyclic word of \(S\).

For \(u\in Z\), put

\[
C_u=S\cup\{u\}\in\binom{[n]}{m-1},
\]

and write

\[
P_u=U_+(C_u),\qquad Q_u=U_-(C_u).
\tag{1.1}
\]

Both \(P_u\) and \(Q_u\) have size three. They can be read directly from
the deficit-five word, without redoing a parenthesis matching.

### Lemma 1.1 — deletion of two old unmatched zeros

Order \(U_+(S)\) in the direction in which the cyclic word is read. If
\(p_u\) is the strict predecessor of \(u\) in \(U_+(S)\), then

\[
\boxed{P_u=\{p_u,\operatorname{pred}p_u,
                    \operatorname{pred}^2p_u\}.}
\tag{1.2}
\]

Order \(U_-(S)\) in the same physical direction. If \(q_u\) is the
strict successor of \(u\) in \(U_-(S)\), then

\[
\boxed{Q_u=\{q_u,\operatorname{succ}q_u,
                    \operatorname{succ}^2q_u\}.}
\tag{1.3}
\]

#### Proof

Cut at the five forward-unmatched zeros and write

\[
0_{a_0}D_0\,0_{a_1}D_1\,0_{a_2}D_2\,0_{a_3}D_3\,0_{a_4}D_4,
\tag{1.4}
\]

where all \(D_i\) are Dyck words. If \(u=a_i\), changing \(u\) to a one
removes \(a_i\) and matches \(a_{i+1}\); the remaining unmatched zeros are
\(a_{i+2},a_{i+3},a_{i+4}\). Here the strict predecessor of \(u\) is
\(a_{i+4}\), so these are precisely that predecessor and its first two
predecessors. If \(u\) lies in \(D_i\), the two new units of excess match
\(a_{i+1},a_{i+2}\); the remaining zeros are
\(a_i,a_{i+4},a_{i+3}\), with \(a_i\) the strict predecessor of \(u\).
This proves (1.2). Reverse the physical circle. Predecessor becomes
successor, and the same argument proves (1.3). \(\square\)

For any three-set \(P\) on the circle, let

\[
\operatorname{pv}_{P}(x)=\text{the strict predecessor of \(x\) in \(P\)},
\]

and define \(\operatorname{nx}_{Q}(x)\) analogously using strict successor.

## 2. Exact internal-edge relation

For distinct \(a,u,c\in Z\), define

\[
(a,u,c)\in\mathcal E_S
\tag{2.1}
\]

when

\[
\boxed{
c=\operatorname{pv}_{P_u}(a),\qquad
a=\operatorname{nx}_{Q_u}(c).}
\tag{2.2}
\]

### Lemma 2.1 — every deficit-five internal edge

For distinct \(a,u,c\in Z\),

\[
\boxed{
g\bigl(S\cup\{a,u\}\bigr)=S\cup\{u,c\}
\quad\Longleftrightarrow\quad
(a,u,c)\in\mathcal E_S.}
\tag{2.3}
\]

#### Proof

For the deficit-three core \(C_u\), the exact predecessor/successor law is

\[
r_+(C_u\cup\{a\})=\operatorname{pv}_{P_u}(a),\qquad
r_-(C_u\cup\{c\})=\operatorname{nx}_{Q_u}(c).
\tag{2.4}
\]

Let \(X=C_u^c\setminus\{a,c\}\). By the definition of the PBBS map,

\[
f(C_u\cup\{a\})=X=f^{-1}(C_u\cup\{c\})
\]

holds exactly when the two equalities in (2.2) hold. This is equivalent
to \(f^2(C_u\cup\{a\})=C_u\cup\{c\}\), proving (2.3). \(\square\)

Thus define a directed graph \(H_S\) on the pair states

\[
\binom Z2
\]

by putting the arc

\[
\{a,u\}\longrightarrow\{u,c\}
\tag{2.5}
\]

for every \((a,u,c)\in\mathcal E_S\). It is exactly the subgraph induced
by the fibre

\[
\{S\cup P:P\in\tbinom Z2\}
\]

inside the step-two PBBS permutation \(g\). In particular, every vertex
has indegree and outdegree at most one.

The arc with middle label \(u\) is exactly a first-shadow occurrence of
\(C_u=S\cup\{u\}\). Consequently the complete first-shadow theorem gives

\[
\boxed{
1\le \#\{(a,c):(a,u,c)\in\mathcal E_S\}\le3
\quad(u\in Z),}
\tag{2.6}
\]

and hence

\[
m+3\le |E(H_S)|\le3(m+3).
\tag{2.7}
\]

## 3. Exact support and missing criterion

For ordered distinct \(b,c\in Z\), define

\[
\begin{aligned}
\operatorname{In}_S(b,c)&=
\mathbf1\{\exists a:(a,b,c)\in\mathcal E_S\},\\
\operatorname{Out}_S(b,c)&=
\mathbf1\{\exists d:(b,c,d)\in\mathcal E_S\}.
\end{aligned}
\tag{3.1}
\]

There is no hidden search in (3.1). The possible \(a\) and \(d\) are
unique and the indicators have the explicit forms

\[
\begin{aligned}
a&=\operatorname{nx}_{Q_b}(c),&
\operatorname{In}_S(b,c)=1
&\Longleftrightarrow
a\notin\{b,c\},\ \operatorname{pv}_{P_b}(a)=c,\\
d&=\operatorname{pv}_{P_c}(b),&
\operatorname{Out}_S(b,c)=1
&\Longleftrightarrow
d\notin\{b,c\},\ \operatorname{nx}_{Q_c}(d)=b.
\end{aligned}
\tag{3.2}
\]

### Theorem 3.1 — exact deficit-five support formula

Let

\[
\mu_{P,2}(S)=\#\{i:A_i\cap A_{i+2}\cap A_{i+4}=S\}.
\]

For \(m\ge2\),

\[
\boxed{
\mu_{P,2}(S)=
\sum_{\substack{b,c\in Z\\b\ne c}}
\operatorname{In}_S(b,c)\operatorname{Out}_S(b,c).}
\tag{3.3}
\]

Equivalently,

\[
\boxed{
S\text{ is missing from the second PBBS turn shadow}
\Longleftrightarrow
H_S\text{ has no directed path of two edges}.}
\tag{3.4}
\]

Since \(H_S\) is a partial permutation, the last condition is equivalent
to saying that every one of its arcs is an isolated directed component;
that is, \(H_S\) is a directed matching.

#### Proof

A two-edge path in \(H_S\) has the unique form

\[
S\cup\{a,b\}\longrightarrow
S\cup\{b,c\}\longrightarrow
S\cup\{c,d\},
\tag{3.5}
\]

with \((a,b,c),(b,c,d)\in\mathcal E_S\). Conversely, every term counted
on the right of (3.3) gives exactly this path. The pointwise no-gap-three
theorem says every PBBS step-two three-state intersection has rank \(m-2\).
All three states in (3.5) contain \(S\), so their intersection is therefore
exactly \(S\). Conversely, if a three-state intersection equals \(S\),
both of its step-two edges lie in the displayed fibre and give a path of
the form (3.5). This proves (3.3)--(3.4).

Finally, \(g\) is a permutation, so \(H_S\) has maximum in- and outdegree
one. It has no two-edge path exactly when its tail and head vertex sets
are disjoint, equivalently when all arcs are isolated. \(\square\)

### Theorem 3.2 — complete second PBBS turn shadow

For every \(m\ge2\) and every \(S\in\binom{[n]}{m-2}\),

\[
\boxed{\mu_{P,2}(S)\ge1.}
\tag{3.6}
\]

Form a circular word \(\mathcal W_S\) with one symbol
\(A_x\) for every \(x\in U_+(S)\) and one symbol \(C_x\) for every
\(x\in U_-(S)\), in their physical circular order. If a coordinate
\(x\) belongs to both unmatched sets, replace that one physical mark by
the two consecutive symbols

\[
C_x,A_x.
\tag{3.7}
\]

#### Proof

Write the expanded circular word in runs

\[
A^{\alpha_0}C^{\gamma_0}\cdots
A^{\alpha_{t-1}}C^{\gamma_{t-1}},
\qquad
\sum_i\alpha_i=\sum_i\gamma_i=5.
\tag{3.8}
\]

At the boundary \(A_c,C_b\) after the \(i\)-th \(A\)-run, let \(x_i\)
be the number of \(A\)-symbols strictly between \(C_b\) and the next
\(C\)-symbol, and let \(y_i\) be the number of \(C\)-symbols encountered
moving backwards from \(A_c\) to the preceding \(A\)-symbol. Thus

\[
x_i=
\begin{cases}
0,&\gamma_i\ge2,\\
\alpha_{i+1},&\gamma_i=1,
\end{cases}
\qquad
y_i=
\begin{cases}
0,&\alpha_i\ge2,\\
\gamma_{i-1},&\alpha_i=1.
\end{cases}
\tag{3.9}
\]

We claim some boundary satisfies

\[
x_i\le2,\qquad y_i\le2.
\tag{3.10}
\]

If \(t=1\), this is immediate. If \(t=2\), choose an \(A\)-run of
size at least three. Then \(y_i=0\); if \(\gamma_i=1\), the other
\(A\)-run has size at most two, so \(x_i\le2\), while
\(\gamma_i\ge2\) gives \(x_i=0\). If \(t\ge3\), choose a largest
\(A\)-run. If it has size at least two, then \(y_i=0\), and the next
\(A\)-run has size at most two because all \(A\)-parts are positive and
sum to five; hence \(x_i\le2\). If every \(A\)-run has size one, then
\(t=5\), every \(C\)-run also has size one, and \(x_i=y_i=1\) at every
boundary. This proves (3.10).

Fix such a boundary and denote it

\[
A_c,C_b.
\tag{3.11}
\]

The coordinates \(b,c\) are distinct: at a shared coordinate the forced
local order is \(C_x,A_x\), not \(A_x,C_x\).

Let \(a\) be the coordinate of the next \(C\)-symbol strictly after
\(C_b\), and let \(d\) be the coordinate of the preceding \(A\)-symbol
strictly before \(A_c\). We claim

\[
(a,b,c)\in\mathcal E_S,\qquad (b,c,d)\in\mathcal E_S.
\tag{3.12}
\]

First consider the core \(C_b=S\cup\{b\}\). Because \(b\in U_-(S)\),
formula (1.3) says that \(Q_b\) consists of the next three \(C\)-marks
strictly after \(C_b\); in particular, its first member is \(a\).
Formula (1.2) says that \(P_b\) consists of the three \(A\)-marks strictly
preceding the physical position of \(b\). Equivalently, flipping \(b\)
removes the first two \(A\)-marks after \(C_b\). Since \(x_i\le2\), no
remaining \(A\)-mark lies between \(C_b\) and \(C_a\); hence

\[
a=\operatorname{nx}_{Q_b}(c),\qquad
c=\operatorname{pv}_{P_b}(a),
\]

which proves the first assertion in (3.12).

Now consider the core \(C_c=S\cup\{c\}\). Since \(c\in U_+(S)\),
formula (1.2) says that \(P_c\) consists of the preceding three
\(A\)-marks, with \(d\) the first one encountered backwards. Formula
(1.3) says that \(Q_c\) consists of the next three \(C\)-marks. The
inequality \(y_i\le2\) ensures that none of the other two selected
\(C\)-marks lies between \(d\) and \(c\); the adjacency in (3.11) then
makes \(b\) the first selected \(C\)-mark after \(d\).
Therefore

\[
d=\operatorname{pv}_{P_c}(b),\qquad
b=\operatorname{nx}_{Q_c}(d),
\]

proving the second assertion in (3.12).

Lemma 2.1 now gives the two-edge path

\[
S\cup\{a,b\}\longrightarrow
S\cup\{b,c\}\longrightarrow
S\cup\{c,d\}.
\tag{3.13}
\]

The inequalities in (3.10), together with the forced shared-mark order
\(C_x,A_x\), also ensure \(a,b,c,d\) are distinct whenever required by
the two swaps. Theorem 3.1 says that the turn color of (3.13) is \(S\).
This proves (3.6). \(\square\)

The known fibre cap also becomes transparent. In a path (3.5), the two
labels deleted from the initial state are \(a,b\). Parenthesis
monotonicity puts both in \(U_-(S)\), and they are distinct. The initial
pair determines the PBBS path. Hence

\[
\boxed{1\le\mu_{P,2}(S)\le\binom52=10.}
\tag{3.12}
\]

### Corollary 3.3 — Catalan second-row overload and collision energy

For all sufficiently large \(m\), the balanced floor at depth two is one.
Let

\[
R_2=W-\binom{2m+1}{m-2}.
\]

Then the complete support and the cap ten give

\[
\boxed{O_2(P_m)\le R_2<12\operatorname{Cat}_m}
\tag{3.13}
\]

and, for the floor-corrected unordered-pair energy

\[
Q_2(P_m)=\frac12\sum_S(\mu_{P,2}(S)-1)(\mu_{P,2}(S)-2),
\]

\[
\boxed{Q_2(P_m)\le4R_2<48\operatorname{Cat}_m.}
\tag{3.14}
\]

#### Proof

Since every load is positive,

\[
\sum_S(\mu_{P,2}(S)-1)=R_2.
\]

Thus the total excess above load two is at most \(R_2\), proving the first
inequality in (3.13). For \(1\le j\le10\),

\[
\binom{j-1}{2}\le4(j-1).
\]

Summing proves \(Q_2(P_m)\le4R_2\). Finally,

\[
\frac{R_2}{\operatorname{Cat}_m}
=\frac{6(2m+1)(m+1)}{(m+2)(m+3)}<12.
\]

\(\square\)

## 4. Why complete \(q=1\) alone did not close (3.4)

Equation (2.6) supplies at least one internal arc for every \(u\in Z\),
but it does not force two such arcs to concatenate. The fibre has

\[
\binom{m+3}{2}
\]

vertices, whereas (2.6) supplies only \(m+3\) forced arcs. The gap is
quadratic versus linear.

This is a sharp logical obstruction, not merely a failure of a numerical
estimate. On an abstract cyclic label set \(Z=\mathbb Z_k\), \(k=m+3\ge5\),
the \(k\) arcs

\[
\{u,u+1\}\longrightarrow\{u,u+2\}
\qquad(u\in\mathbb Z_k)
\tag{4.1}
\]

form a directed matching: the tails are the distance-one pairs and the
heads are the distance-two pairs. Thus they give one first-shadow arc for
every core label and no second-shadow path. This abstract configuration
is not asserted to satisfy the PBBS ten-mark rules. It proves that the
complete-\(q=1\) theorem, the correct-rank theorem, and the fibre cap alone
cannot establish \(q=2\) coverage. Any proof of completeness must use the
specific coupling of \(P_u\) and \(Q_u\) inherited from one deficit-five
word. Theorem 3.2 supplies exactly that missing coupling: the five-by-five
run lemma finds an \(A\to C\) transition whose two local gap counts are at
most two, and that good transition forces a head of one internal arc to be
the tail of another.

## 5. Status

Proved here:

1. the three-unmatched-zero sets \(P_u,Q_u\) are explicit consecutive
   triples of the original five unmatched-zero sets;
2. every internal step-two edge is characterized by (2.2);
3. the exact multiplicity formula (3.3);
4. the exact missing criterion (3.4);
5. the transition construction (3.9)--(3.11), which excludes that
   directed-matching obstruction for every deficit-five PBBS word;
6. complete rank-\((m-2)\) support with the exact bounds
   \(1\le\mu_{P,2}(S)\le10\);
7. Catalan-scale second-row overload and collision energy.

Thus both depth-two gates are closed for the canonical PBBS factor:
every three-state turn has the correct rank, and every target of that rank
occurs.
