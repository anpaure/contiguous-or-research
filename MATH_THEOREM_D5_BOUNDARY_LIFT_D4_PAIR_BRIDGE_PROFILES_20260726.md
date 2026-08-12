# A 42-path $D_5$-port lift of the $D_4$ pair bridge

Date: 2026-07-26

Method: pure mathematics only. The two displayed \(D_4\)-port path factors
and their literal positional ledgers are used as exact input. No search,
solver, computation, or web input is used.

## 0. Result

There is an explicit noncanonical \(D_5\)-port factor on \([10]\):
twenty-eight of its forty-two rooted complement paths are canonical MSW
paths, and the other fourteen are the right-boundary lifts of the complete
\(D_4\) pair bridge.

The lift has fixed \(D_5\) ports and exact \(X/Y\) ledgers. Its full lower
profiles have the following form.

* At depth four, both complete factors have the uniform singleton profile

  \[
                 \mu_4=42\sum_{x\in[11]}e_x.             \tag{0.1}
  \]

  Hence the aggregate signed depth-four profile is zero. Nevertheless all
  eight variable boundary positions \(a_1,\ldots,a_4,b_1,\ldots,b_4\)
  have nonzero occurrence-resolved signed profiles. They are eight
  available boundary cells, but they cancel when their carrier labels are
  forgotten.

* At depth three, the full signed profile is explicitly given by (4.4).
  It is nonzero. In particular its targets containing the new distinguished
  coordinate \(c\) contain the uncancelled term

  \[
       -3e_{\{c,2\}}+5e_{\{c,3\}}
          -e_{\{c,4\}}-e_{\{c,6\}}.                    \tag{0.2}
  \]

  No other changed depth-three start contains \(c\), so (0.2) cannot
  cancel. Thus the \(D_4\) bridge has a genuine off-matched
  carrier-resolved \(D_5\) action.

The left-boundary lift is exact in its correspondingly relabelled
left-aligned frame. Together the right and left lifts expose eight nonzero
boundary occurrence cells, listed in (5.3). They become distinct physical
carrier slices if an outer atlas supplies distinct tags, but that tagging
theorem is not supplied by the local $D_5$ construction.

It is not yet a five-to-eight-way independently selectable local atom. One
fourteen-row packet choice moves all of its boundary cells with correlated
signs, and overlapping right/left packets require a joint ownership
completion. Thus the construction escapes the canonical binary
\(V_4\) target kernel but does not by itself prove the residual-cap
allocation needed for coefficient one.

## 1. The \(D_4\) positional datum

Put \(J=[8]\). For \(H\in\{F,G\}\), where \(F\) is canonical and \(G\)
is the new complete \(D_4\)-port factor, write a rooted path as

\[
 X_t^H(P)=
  \bigl(P\setminus\{a_1^H,\ldots,a_t^H\}\bigr)
   \cup\{b_1^H,\ldots,b_t^H\},\qquad0\le t\le4.          \tag{1.1}
\]

Its cyclic coordinate word is

\[
 q_H(P)=(a_1^H,a_2^H,a_3^H,a_4^H,
         b_1^H,b_2^H,b_3^H,b_4^H,\omega),              \tag{1.2}
\]

where \(\omega\) is the old distinguished coordinate. For a position set
\(A\subseteq\mathbb Z_9\), define

\[
 D_A=\sum_{P\in D_4}
 \left(
 e_{\{q_i^G(P):i\in A\}}
 -e_{\{q_i^F(P):i\in A\}}
 \right).                                               \tag{1.3}
\]

For a cyclic interval of length \(\ell\) beginning at \(j\), write

\[
                         \Delta_{\ell,j}
 =D_{\{j,j+1,\ldots,j+\ell-1\}}.                       \tag{1.4}
\]

Let \(\delta_k=\Delta_{1,k-1}\), with positions numbered one through nine
as in (1.2). Direct reading of the two displayed path tables gives

\[
\begin{array}{c|l|c}
k&\delta_k&\|\delta_k\|_1/2\\ \hline
1&-3e_2+5e_3-e_4-e_6&5\\
2&2e_2-3e_3-3e_4+2e_5-e_6+3e_7&7\\
3&-e_2+4e_4-4e_5-e_6+2e_7&6\\
4&2e_2-2e_3+2e_5+3e_6-5e_7&7\\
5&-4e_2+4e_3-e_4-e_6+2e_7&6\\
6&3e_2-e_3-2e_4&3\\
7&-e_3+2e_4-3e_6+2e_7&4\\
8&e_2-2e_3+e_4+4e_6-4e_7&6\\
9&0&0.
\end{array}                                             \tag{1.5}
\]

In particular,

\[
                         \sum_{k=1}^{9}\delta_k=0,       \tag{1.6}
\]

but every one of the eight variable-position cells is nonzero.

## 2. The explicit right-boundary \(D_5\) factor

Let

\[
                         \alpha=9,\qquad\beta=10,
                         \qquad c=11.                   \tag{2.1}
\]

The \(D_5\) core is \([10]=J\sqcup\{\alpha,\beta\}\), and \(c\) is its
distinguished odd-graph coordinate.

For \(P\in D_4\) define six states

\[
 \widetilde X_t^H(P)=\{\alpha\}\cup X_t^H(P)
                  \quad(0\le t\le4),\qquad
 \widetilde X_5^H(P)=\{\beta\}\cup(J\setminus P).       \tag{2.2}
\]

Their ports are

\[
 \widetilde X_0^H(P)=\{\alpha\}\cup P,\qquad
 \widetilde X_5^H(P)=\{\beta\}\cup(J\setminus P),       \tag{2.3}
\]

which are complementary five-subsets of \([10]\). The first port is the
Dyck word \(P10\), so the fourteen roots in (2.3) belong to \(D_5\).

Let \(F_5\) be the canonical \(D_5\)-port factor. By the MSW
concatenation law, the rows of \(F_5\) rooted at \(P10\) are exactly
(2.2) with \(H=F\). Define

\[
 \widehat G_R=
  \left(F_5\setminus
     \{\widetilde X^F(P):P\in D_4\}\right)
  \cup
     \{\widetilde X^G(P):P\in D_4\}.                   \tag{2.4}
\]

Thus (2.4) is an explicit forty-two-path factor: fourteen paths are given
by (2.2) with \(H=G\), and the remaining
\(42-14=28\) paths are the unchanged canonical rows.

### Theorem 2.1 (exact \(X/Y\) ledgers and fixed ports)

The paths in \(\widehat G_R\) partition both middle ranks on \([10]\) and
have the same \(D_5\) ports as \(F_5\). Hence \(\widehat G_R\) is an exact
\(D_5\)-port factor.

#### Proof

For \(0\le t\le4\), the changed \(X\)-states are obtained by adjoining
\(\alpha\) to the seventy \(D_4\) \(X\)-states. Since \(F\) and \(G\)
both enumerate all of \(\binom J4\), their lifted \(X\)-ledgers agree.
The terminal states in (2.2) depend only on \(P\), so they agree row by
row.

For \(0\le t<4\), the adjacent-union colors are

\[
                         \{\alpha\}\cup Y_t^H(P).       \tag{2.5}
\]

The two \(D_4\) factors enumerate the same complete \(Y\)-rank, so these
ledgers agree. The last color is the fixed set

\[
              \{\alpha,\beta\}\cup(J\setminus P),      \tag{2.6}
\]

again common row by row. Therefore the fourteen old and new packets own
identical \(X/Y\) supports. Replacing one packet inside the exact factor
\(F_5\) preserves exactness. Equation (2.3) proves the port assertion.
The shore counts close exactly:

\[
 84+28\cdot6=252=\binom{10}{5},\qquad
 70+28\cdot5=210=\binom{10}{6}.
\]

\(\square\)

The cyclic coordinate word of the lifted row is

\[
 Q_R^H(P)=
 (a_1^H,a_2^H,a_3^H,a_4^H,\alpha,
  b_1^H,b_2^H,b_3^H,b_4^H,\beta,c).                    \tag{2.7}
\]

## 3. Depth four: zero aggregate and eight boundary cells

At depth four, a lower target is a cyclic interval of length one in
\(Q_R\). Every coordinate word of every one of the forty-two rows is a
permutation of \([11]\). Consequently

### Theorem 3.1 (full depth-four profile)

\[
 \boxed{
 \mu_4^{F_5}=\mu_4^{\widehat G_R}
            =42\sum_{x\in[11]}e_x.}                    \tag{3.1}
\]

The aggregate signed depth-four profile is zero. On the changed packet,
the eleven position-cell profiles are

\[
 (\delta_1,\delta_2,\delta_3,\delta_4,0,
  \delta_5,\delta_6,\delta_7,\delta_8,0,0).             \tag{3.2}
\]

#### Proof

Every row contributes each singleton coordinate once, proving (3.1).
Reading the positions in (2.7) and using (1.5) gives (3.2). Equation
(1.6) makes their aggregate zero. \(\square\)

Thus there are eight nonzero boundary occurrence cells. They are not yet
eight independently capacitated targets: in the isolated \(D_5\) factor
their coordinate images overlap and sum to zero.

## 4. Depth three: the nonzero carrier profile

For a fixed coordinate \(z\notin J\) and a singleton signed vector
\(v=\sum_xv(x)e_x\), write

\[
                         z\star v=\sum_xv(x)e_{\{z,x\}}. \tag{4.1}
\]

In \(Q_R\), the eleven length-two starts are

\[
\begin{gathered}
(a_1,a_2),(a_2,a_3),(a_3,a_4),(a_4,\alpha),
(\alpha,b_1),(b_1,b_2),\\
(b_2,b_3),(b_3,b_4),(b_4,\beta),(\beta,c),(c,a_1).
\end{gathered}                                           \tag{4.2}
\]

Only the fourteen lifted rows change; the other twenty-eight rows cancel
from the comparison.

### Theorem 4.1 (full signed depth-three profile)

\[
\boxed{
\begin{aligned}
 \widehat\Delta^{R}_3={}&
 \Delta_{2,0}+\Delta_{2,1}+\Delta_{2,2}
 +\alpha\star(\delta_4+\delta_5)\\
 &+\Delta_{2,4}+\Delta_{2,5}+\Delta_{2,6}
 +\beta\star\delta_8+c\star\delta_1.
\end{aligned}}                                           \tag{4.3}
\]

Equivalently, the complete profiles satisfy

\[
 \boxed{
 \mu_3^{\widehat G_R}
 =\mu_3^{F_5}+\widehat\Delta^{R}_3.}                   \tag{4.4}
\]

Moreover \(\widehat\Delta^{R}_3\ne0\), and

\[
                         \frac12\|
                         \widehat\Delta^{R}_3\|_1\ge5.  \tag{4.5}
\]

#### Proof

Apply the positional definition (1.3) to the eleven starts in (4.2).
Pairs wholly inside the old word give the six displayed
\(\Delta_{2,j}\) terms. Splitting the old adjacency \((a_4,b_1)\) by
\(\alpha\) gives the two \(\alpha\)-carrier singleton terms. The last
old boundary adjacencies become \((b_4,\beta)\) and \((c,a_1)\); the
fixed pair \((\beta,c)\) contributes zero. This proves (4.3)--(4.4).

No term in (4.3) other than \(c\star\delta_1\) contains \(c\). From
(1.5),

\[
 c\star\delta_1=
 -3e_{\{c,2\}}+5e_{\{c,3\}}
 -e_{\{c,4\}}-e_{\{c,6\}}.                            \tag{4.6}
\]

It is nonzero and has positive mass five. Its support is disjoint from all
other terms, proving (4.5). \(\square\)

Thus the explicit forty-two-path factor has the required nonzero
off-matched carrier action. Exactness does not force collar cancellation
at depth three.

## 5. Left lift and the eight-cell atlas

There is a second exact boundary embedding. Relabel the core coordinates
so that the new pair precedes the copy of \(J\), and put

\[
 \widetilde X_0^H=\{\alpha\}\cup P,\qquad
 \widetilde X_{t+1}^H=\{\beta\}\cup X_t^H
                    \quad(0\le t\le4).                 \tag{5.1}
\]

Its coordinate word is

\[
 Q_L^H=(\alpha,a_1^H,a_2^H,a_3^H,a_4^H,
        \beta,b_1^H,b_2^H,b_3^H,b_4^H,c).              \tag{5.2}
\]

The same \(X/Y\)-ledger proof as Theorem 2.1, with a fixed first boundary
color instead of a fixed last one, gives another exact forty-two-path
\(D_5\)-port factor \(\widehat G_L\) in this left-aligned frame. Its
other twenty-eight paths are the canonical completion in that frame.

Across the right and left lifts, the separator-crossing depth-three cells
are

\[
\begin{array}{c|cccc}
R&(\alpha,a_4)&(\alpha,b_1)&(\beta,b_4)&(c,a_1)\\
L&(\alpha,a_1)&(\beta,a_4)&(\beta,b_1)&(c,b_4).
\end{array}                                               \tag{5.3}
\]

Their signed profiles are respectively

\[
\begin{array}{c|cccc}
R&\alpha\star\delta_4&\alpha\star\delta_5&
  \beta\star\delta_8&c\star\delta_1\\
L&\alpha\star\delta_1&\beta\star\delta_4&
  \beta\star\delta_5&c\star\delta_8.
\end{array}                                               \tag{5.4}
\]

All eight entries are nonzero by (1.5).

### Lemma 5.1 (conditional five-to-eight physical carrier cells)

Suppose a phase-disjoint outer atlas places five through eight cells of
(5.3) under pairwise distinct exterior tags. Then their physical target
slices are disjoint, every whole-packet choice remains an exact port
substitution, and all tagged cell profiles remain nonzero.

#### Proof

Adjoining distinct fixed exterior tags sends different cells into disjoint
target slices. Phase-disjoint whole-packet substitutions have disjoint
\(X/Y\) slabs, so their exact ledgers add and their choices commute.
\(\square\)

This is a conditional atlas statement, not a construction of the required
tags. It also does not say that the eight cells inside one overlapping
parent are independently selectable.

## 6. Relation to the \(V_4\) obstruction and remaining gate

The canonical two-boundary \(V_4\) overlay has one indivisible principal
component and only permutes four loads. The construction above uses a
non-coordinate fourteen-row packet and exports eight nonzero boundary
occurrence cells. It therefore escapes the **zero-action** and
four-cell-alphabet parts of the canonical obstruction.

Two limitations remain.

1. One binary choice \(F\leftrightarrow G\) moves all cells of its packet
   with the correlated positional tensor (1.3). The cells are not
   independent signs.
2. Right- and left-boundary packets overlap if installed in the same
   parent. Their separate exactness does not imply a joint product. They
   must be put in phase-disjoint contexts or completed as one multi-state
   ownership atom.

For a current residual capacity \(c_\beta\), the exact coefficient-one
test for a tagged atom is

\[
 \sum_S\bigl(\mu_3^{F_5}(S)
       +\widehat\Delta_3(S)-c_\beta(S)\bigr)_+
 <
 \sum_S\bigl(\mu_3^{F_5}(S)-c_\beta(S)\bigr)_+.        \tag{6.1}
\]

Theorem 4.1 supplies a nonzero direction, not the favourable sign of
(6.1) in the canonical global background.

The remaining construction target is therefore:

> Build a common-completion library for the right/left/primitive
> forty-two-path packets, or a phase-disjoint positive-density atlas, whose
> five-to-eight carrier slices meet the actual residual capacities at all
> protected depths simultaneously.

## 7. Final conclusion

\[
 \boxed{\text{An explicit exact \(D_5\)-port boundary lift exists, and its
 full depth-three carrier profile is nonzero.}}          \tag{7.1}
\]

Its full depth-four profile cancels, but it exposes eight nonzero
position-resolved boundary cells. A separate outer-tag theorem is needed
to turn five through eight of them into disjoint physical capacity cells.
The unresolved step is joint cell tagging/selection and residual-cap
alignment, not \(D_5\) exact completion.
