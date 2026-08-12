# Cross-cell product-SCD staircases: the directed successor graph and a Gaussian Hall cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input is used.

## 0. Result

Let \(V=X\mathbin{\dot\cup}Y\), where \(|X|=|Y|=m\), and fix
arbitrary symmetric-chain decompositions of the two half-cubes.  Put

\[
 q=q_m,\qquad \frac q{\sqrt m}\longrightarrow A>0,
 \qquad W_m={2m\choose m}.
\tag{0.1}
\]

Section 2 below defines the exact directed graph whose vertices are
oriented product-SCD blocks and whose arcs are legal successor prefixes
for the exported lower staircases in Section 7 of
`MATH_THEOREM_MIXED_PBBS_PRODUCT_SCD_ENDPOINT_COUPLING_CUT_20260726.md`.
An arc out of one block produces \(q\) rank-\(m\) middle targets.  A
capacity-one path cover requires all of those targets to be distinct.

That requirement has a linear Hall obstruction.  More precisely, for
every fixed \(A>0\) there is an explicit Gaussian family
\(\mathcal V_{m,A}\) of source blocks with

\[
 q|\mathcal V_{m,A}|=\Theta_A(W_m)
\tag{0.2}
\]

such that, even after all successor-port capacities are deleted and each
individual staircase state is allowed to choose its successor shore
independently, the number of middle targets accessible to these states is
at most

\[
 q|\mathcal V_{m,A}|-(d_A+o_A(1))W_m,
\tag{0.3}
\]

where the following completely explicit constant is positive.  Set

\[
 x=A+A^{-1},\qquad f(u)=e^{-2u^2},
\tag{0.4}
\]

\[
 \Gamma_A
 =A\bigl(f(x)-f(x+A)\bigr)
   -\int_x^{x+2A}f(u)\,du,
\tag{0.5}
\]

and

\[
 \boxed{
 d_A={2\over\sqrt\pi}\,f(x+2A)\Gamma_A>0.}
\tag{0.6}
\]

Consequently there is no target-capacity-one near-perfect path cover of
the full exported canonical lower-staircase family.  At least

\[
 (d_A+o_A(1))W_m
\tag{0.7}
\]

staircase states, or at least

\[
 (d_A+o_A(1)){W_m\over q}
 =\Theta_A(W_m/\sqrt m)
\tag{0.8}
\]

whole \(q\)-state blocks, must be discarded or recompiled.

The obstruction uses only middle-target capacity.  It therefore remains
valid no matter how many copies of every legal successor port are made
available.  A surviving global rethreading must do at least one of the
following on a positive-density family: abandon the canonical exported
starts, split and interlace a staircase across both coordinate shores,
or change the completed middle target before the next whole product-SCD
prefix.  Merely permuting and orienting the old whole blocks cannot close
the Gaussian annulus.

## 1. Product chains and exported states

Let

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}
\tag{1.1}
\]

be a chain in \(2^X\), and let

\[
 D_b\subset D_{b+1}\subset\cdots\subset D_{m-b}
\tag{1.2}
\]

be a chain in \(2^Y\).  As usual, \(R(C)\) is the base \(C_a\)
followed by the singleton increments of \(C\), and \(L(C)\) is its
reversal; likewise for \(D\).

Assume

\[
 a>b>0,\qquad a-b\ge q,\qquad 2a+q\le m.
\tag{1.3}
\]

Orient the product cell as

\[
 v(C,D)=L(D)\mathbin\Vert R(C).
\tag{1.4}
\]

For \(1\le t\le q\), put \(k=q-t\).  The canonical lower target from
Theorem 5.1 of the preceding report is

\[
 T_t(C,D)
 =D_{a-t}\cup C_{m-a-q+t},
 \qquad |T_t(C,D)|=m-q.
\tag{1.5}
\]

Its canonical start is distinct from the other \(q-1\) starts.  If this
interval is continued to the end of (1.4), its union is

\[
 B_t(C,D)=D_{a-t}\cup C_{m-a},
 \qquad |B_t(C,D)|=m-t.
\tag{1.6}
\]

Thus it needs exactly \(t\) new singleton coordinates to become a
rank-\(m\) interval.

Different triples \((C,D,t)\) in (1.5) give different lower targets.
Indeed the two half-cube SCDs uniquely recover \(C,D\) from the two
components, and their ranks then recover \(t\).  Hence all the states
counted below are genuine distinct rank-\((m-q)\) demands, not duplicate
witnesses for the same target.

## 2. The exact directed successor graph

An oriented product block \(w\) has a **\(q\)-port** when its first \(q\)
letters are singletons.  They all belong to its left half-chain.  Write

\[
 \pi_q(w)=(z_1,\ldots,z_q),\qquad
 P_t(w)=\{z_1,\ldots,z_t\}.
\tag{2.1}
\]

There are two types of port: an \(X\)-port and a \(Y\)-port, according to
the shore containing the \(z_i\).

Define a directed arc

\[
 v(C,D)\longrightarrow w
\tag{2.2}
\]

exactly when, for every \(1\le t\le q\),

\[
 P_t(w)\cap B_t(C,D)=\varnothing.
\tag{2.3}
\]

This is the exact, not merely sufficient, successor condition.  Along
the arc, the common-start middle target produced by state \(t\) is

\[
 M_t(C,D;w)=B_t(C,D)\cup P_t(w).
\tag{2.4}
\]

Its rank is \(m\) by (1.6) and (2.3).  Written by shores, (2.4) is

\[
 \begin{array}{ll}
 X\text{-port}:&
 M_t=(C_{m-a}\cup P_t)\cup D_{a-t},\\[1mm]
 Y\text{-port}:&
 M_t=C_{m-a}\cup(D_{a-t}\cup P_t).
 \end{array}
\tag{2.5}
\]

A directed product-block path cover selects arcs with indegree and
outdegree at most one.  For endpoint baseline reuse it has the additional
capacity condition

\[
 M_t(C,D;w)\ne M_{t'}(C',D';w')
\tag{2.6}
\]

for all distinct exported starts that are retained.  This is forced by
endpoint saturation, with the following exact allowance.  In a word of
length \(W_m+e\), choose one witness for every rank-\(m\) target.  Their
left endpoints form a \(W_m\)-set \(S_0\).  At any fixed left endpoint
there is at most one rank-\(m\) interval union, because all intervals
with that endpoint are nested.  Consequently the map from exported
starts in \(S_0\) to their produced middle targets is injective.  Only
the at most \(e\) positions outside \(S_0\) can violate (2.6).  Thus an
\(o(W_m)\)-excess word permits only \(o(W_m)\) target-capacity
violations.

Condition (2.6) is not an ordinary degree condition on (2.2).  Every
selected arc consumes one successor block and a bundle of \(q\) middle
targets.  The correct incidence object is therefore the bundle
hypergraph with edge

\[
 \{v,w\}\cup\{M_t(C,D;w):1\le t\le q\}.
\tag{2.7}
\]

The cut below is a Hall cut in the middle-target part of this
hypergraph.  In particular it is stronger than a zero-degree or
successor-port cut.

## 3. The Gaussian source rectangle

Put

\[
 x=A+A^{-1},
\tag{3.1}
\]

and, with arbitrary harmless choices at half-integers, define

\[
 \begin{aligned}
 \beta&=\left\lfloor {m\over2}-x\sqrt m\right\rfloor,\\
 \alpha&=\beta-q+1,\\
 b_0&=\alpha-q=\beta-2q+1.
 \end{aligned}
\tag{3.2}
\]

For all sufficiently large \(m\), these are positive and

\[
 2\beta+q\le m.
\tag{3.3}
\]

Let

\[
 \mathcal C_I=\{C:\alpha\le a(C)\le\beta\},
 \qquad
 \mathcal D_0=\{D:1\le b(D)\le b_0\},
\tag{3.4}
\]

and take the source-block rectangle

\[
 \mathcal V_{m,A}
 =\{v(C,D):C\in\mathcal C_I, D\in\mathcal D_0\}.
\tag{3.5}
\]

Every block in (3.5) satisfies (1.3), because

\[
 a-b\ge\alpha-b_0=q,
 \qquad 2a+q\le2\beta+q\le m.
\tag{3.6}
\]

It is also an actual cell in the product tail at cutoff \(m-q\):

\[
 a+b\le\beta+b_0=2\beta-2q+1\le m-q.
\tag{3.7}
\]

If

\[
 A_m(r)={m\choose r}-{m\choose {r-1}},
\tag{3.8}
\]

then telescoping gives the exact source counts

\[
 \begin{aligned}
 N_C&=|\mathcal C_I|
 ={m\choose\beta}-{m\choose{\alpha-1}},\\
 N_D&=|\mathcal D_0|
 ={m\choose{b_0}}-1,\\
 |\mathcal V_{m,A}|&=N_CN_D.
 \end{aligned}
\tag{3.9}
\]

Thus the number of exported states in this rectangle is exactly

\[
 Q_{m,A}=qN_CN_D.
\tag{3.10}
\]

## 4. Exact capacity of the two shores

We now delete every successor-block capacity and even allow the \(q\)
states of one source block to choose their shores independently.  This
can only enlarge the accessible middle-target set.

### Lemma 4.1 (exit-shore capacity)

All targets produced from (3.5) by \(X\)-ports belong to a family of
exact size

\[
 K_X=N_D\sum_{j=b_0}^{\beta-1}{m\choose j}.
\tag{4.1}
\]

#### Proof

For an \(X\)-port put \(j=a-t\).  As

\[
 \alpha\le a\le\beta,qquad1\le t\le q,
\]

one has

\[
 b_0=\alpha-q\le j\le\beta-1.
\tag{4.2}
\]

Formula (2.5) shows that the \(Y\)-component is the fixed chain member
\(D_j\), while the \(X\)-component has rank \(m-j\).  For every pair
\((D,j)\) there are at most

\[
 {m\choose {m-j}}={m\choose j}
\]

such \(X\)-components.  Conversely, the labels \((D,j)\) are distinct:
the SCD partitions every fixed rank, and different \(j\)'s have different
ranks.  Therefore the ambient target cylinders indexed by \((D,j)\)
are disjoint and have total size exactly (4.1).  Every actually legal
output is contained in them. \(\square\)

### Lemma 4.2 (return-shore capacity)

All targets produced from (3.5) by \(Y\)-ports belong to a family of
exact size

\[
 K_Y=\sum_{a=\alpha}^{\beta}A_m(a){m\choose a}.
\tag{4.3}
\]

#### Proof

For a \(Y\)-port, (2.5) has fixed \(X\)-component \(C_{m-a}\).  Its
\(Y\)-component has rank

\[
 |D_{a-t}|+|P_t|=a
\]

by legality (2.3).  Hence for a fixed chain \(C\) it lies in a cylinder
of size \({m\choose a}\).  Top members \(C_{m-a}\) of different SCD
chains are distinct, including across different \(a\), so these
cylinders are disjoint.  Summing over the \(A_m(a)\) chains of minimum
rank \(a\) proves (4.3). \(\square\)

Combining the two lemmas, the complete target neighborhood of all
\(Q_{m,A}\) source states has size at most

\[
 \boxed{|N_M(\mathcal V_{m,A}\times[q])|\le K_X+K_Y.}
\tag{4.4}
\]

This statement already permits more choices than the directed graph:
it ignores port availability, successor-block capacity, path indegrees,
and the requirement that all states of one block use the same shore.

## 5. The deficit is linear

Let

\[
 c_0=\sqrt{2/\pi},\qquad f(u)=e^{-2u^2}.
\tag{5.1}
\]

Uniformly for \(u\) in a fixed compact subset of \((0,\infty)\),
Stirling's formula gives

\[
 {m\choose {m/2-u\sqrt m+O(1)}}
 =(c_0f(u)+o(1)){2^m\over\sqrt m}.
\tag{5.2}
\]

Using (3.2), (3.9), and a Riemann sum in (4.1), we obtain

\[
 \begin{aligned}
 N_C&=(c_0+o(1)){2^m\over\sqrt m}
       \bigl(f(x)-f(x+A)\bigr),\\
 N_D&=(c_0+o(1)){2^m\over\sqrt m}f(x+2A),\\
 \sum_{j=b_0}^{\beta-1}{m\choose j}
   &=(c_0+o(1))2^m\int_x^{x+2A}f(u)\,du.
 \end{aligned}
\tag{5.3}
\]

The return-shore term is lower order.  Indeed the exact identity

\[
 A_m(a)={m\choose a}{m-2a+1\over m-a+1}
\tag{5.4}
\]

and (3.2) imply uniformly on \([\alpha,\beta]\) that

\[
 A_m(a)=O_A\left({1\over\sqrt m}{m\choose a}\right).
\tag{5.5}
\]

There are \(q=O_A(\sqrt m)\) indices, while each central Gaussian
binomial square is \(O_A(4^m/m)\).  Therefore

\[
 K_Y=O_A(4^m/m)=o(W_m).
\tag{5.6}
\]

Equations (3.10), (4.1), and (5.3) now give

\[
 Q_{m,A}-K_X
 =\left(c_0^2f(x+2A)\Gamma_A+o_A(1)\right)
   {4^m\over\sqrt m},
\tag{5.7}
\]

where \(\Gamma_A\) is (0.5).

It remains to check its sign.  Since \(x=A+A^{-1}\),

\[
 {f(x+A)\over f(x)}
 =\exp(-4Ax-2A^2)=\exp(-6A^2-4)\le e^{-4}.
\tag{5.8}
\]

Also, for every \(x>0\),

\[
 \int_x^\infty e^{-2u^2}\,du
 \le {e^{-2x^2}\over4x},
\tag{5.9}
\]

because \(u/x\ge1\) on the interval and

\[
 \int_x^\infty {u\over x}e^{-2u^2}\,du
 ={e^{-2x^2}\over4x}.
\]

Finally

\[
 {1\over4x}={A\over4(A^2+1)}\le {A\over4}.
\tag{5.10}
\]

Thus

\[
 \boxed{
 \Gamma_A
 \ge A f(x)\left({3\over4}-e^{-4}\right)>0.}
\tag{5.11}
\]

Since

\[
 W_m=\left({1\over\sqrt\pi}+o(1)\right){4^m\over\sqrt m}
\tag{5.12}
\]

and \(c_0^2\sqrt\pi=2/\sqrt\pi\), (5.6)--(5.12) prove

\[
 \boxed{
 Q_{m,A}-(K_X+K_Y)
 \ge(d_A+o_A(1))W_m,}
\tag{5.13}
\]

with \(d_A\) from (0.6).  This proves (0.3). \(\square\)

## 6. Exact Hall consequence

Let the left side of the middle-resource incidence graph consist of the
exported tokens

\[
 \mathcal A_{m,A}
 =\{(C,D,t):v(C,D)\in\mathcal V_{m,A},\ 1\le t\le q\}.
\tag{6.1}
\]

Join a token to a rank-\(m\) target whenever that target can arise from
some legal whole-block successor arc, with either shore allowed.  Then
(4.4) and (5.13) give the exact Hall-deficient family

\[
 \boxed{
 |\mathcal A_{m,A}|-|N_M(\mathcal A_{m,A})|
 \ge(d_A+o_A(1))W_m.}
\tag{6.2}
\]

Any capacity-one directed path cover induces a matching in this incidence
graph.  More generally, by the endpoint-saturation argument following
(2.6), a word of length \(W_m+e\) can couple at most \(e\) retained
tokens outside such a matching.  Hence retaining every token in
\(\mathcal A_{m,A}\) forces

\[
 e\ge(d_A+o_A(1))W_m.
\tag{6.3}
\]

If instead the word has \(e=o(W_m)\), it must discard or noncanonically
recompile at least \((d_A+o_A(1))W_m\) tokens.  Because each source block
has \(q\) tokens, at least the number of whole blocks stated in (0.8)
must be affected.

Notice that (6.2) is independent of the actual distribution of SCD port
direction sets.  The old endpoint-mixing countercuts are not used.  Even
a hypothetical complete successor graph cannot overcome this target
cut.

## 7. Proved boundary and surviving escape

The following are proved here.

1. Equations (2.2)--(2.5) are the exact directed whole-block successor
   graph and output law for an exported lower staircase.
2. The Gaussian source rectangle (3.5) contains
   \(\Theta_A(W_m/\sqrt m)\) actual product-tail blocks and
   \(\Theta_A(W_m)\) distinct compulsory lower states.
3. Its two possible whole-block successor shores have the exact ambient
   capacities (4.1) and (4.3).
4. Their union has the linear Hall deficit (6.2), with the explicit
   positive constant (0.6).

Thus the surviving cross-cell route is narrower than a permutation of
canonical product blocks.  A positive result must alter the local state
law (2.5), not merely improve the degree of (2.2).  In particular, an
interlaced successor whose first \(q\) rank increments use both shores
is not covered by Lemmas 4.1--4.2 and is the smallest remaining
possibility.  Such an interlacing would have to remain one literal OR
chronology while preserving the upper witnesses; neither existence nor
impossibility of that stronger gadget is proved here.

No coefficient-one conclusion is claimed.
