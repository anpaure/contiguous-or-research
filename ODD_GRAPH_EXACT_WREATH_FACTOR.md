# The odd-graph route is already exact

## 1. Correction to the previous ledger

Put

\[
        n=2m+1,
        \qquad W=\binom{2m+1}{m},
        \qquad C_m=\frac{W}{2m+1}.
\]

The middle-only problem is not open, even approximately.  Mütze, Standke and
Wiechert proved that the odd graph

\[
                     O_{2m+1}=KG(2m+1,m)
\]

has a spanning `C_(2m+1)`-factor.  It consists of exactly `C_m` cycles.  Thus
all `W` middle sets are partitioned into minimum odd cycles.

Reference: T. Mütze, C. Standke and V. Wiechert, *A minimum-change version of
the Chung--Feller theorem for Dyck paths*, European J. Combin. 69 (2018),
260--275, Theorem 4; arXiv:1603.02525.  The same factor is the starting object
in T. Mütze, J. Nummenpalo and B. Walczak, *Sparse Kneser graphs are
Hamiltonian*, J. London Math. Soc. 103 (2021), 1253--1275.

Consequently no new nibble, absorption theorem, or approximate cycle-packing
argument is needed for the middle layer.

## 2. Every minimum odd cycle is a wreath

This equivalence is elementary but useful enough to record carefully.

Let

\[
             A_0,A_1,\ldots,A_{n-1},A_n=A_0
\]

be a closed walk of length `n=2m+1` in `KG(n,m)`.  For every edge put

\[
             z_i=[n]\setminus(A_i\cup A_{i+1}).        \tag{2.1}
\]

The set in (2.1) is a singleton, which we identify with its element.  For a
coordinate `z`, let `t_z` be the number of indices `i` for which `z_i=z`.

Across an edge not labelled `z`, membership of `z` toggles: exactly one of the
two disjoint `m`-sets contains it.  Across an edge labelled `z`, both endpoints
omit it.  Since the incidence bit returns to its starting value after going
round the odd walk,

\[
                         n-t_z\equiv0\pmod2.
\]

Hence every `t_z` is odd.  On the other hand,

\[
                         \sum_{z\in[n]}t_z=n.
\]

There are `n` coordinates, so necessarily

\[
                         t_z=1\quad(z\in[n]).           \tag{2.2}
\]

Thus `(z_0,...,z_(n-1))` is a permutation of the ground set.  The recurrence

\[
                         A_{i+1}=\overline{A_i}\setminus\{z_i\}
\]

then has the unique cyclic solution

\[
       A_i=\{z_{i+1},z_{i+3},\ldots,z_{i+2m-1}\}.       \tag{2.3}
\]

Since multiplication by `2` permutes `Z_n`, the sets in (2.3) are precisely
the length-`m` cyclic intervals in the cyclic order

\[
                         z_0,z_2,z_4,\ldots .           \tag{2.4}
\]

Therefore every `C_n` in the odd graph is a wreath, and conversely every
wreath gives such a `C_n`.  The MSW factor is consequently an exact wreath
decomposition for `(n,m)=(2m+1,m)`.

## 3. The explicit Chung--Feller factor

Let `D_(2m)^e` be the balanced up/down paths with exactly `e` flaws.  MSW give
a bijection

\[
                    f:D_{2m}^e\longrightarrow D_{2m}^{e+1}
\]

which flips one down-step to an up-step and one up-step to a down-step.  They
factor it as `f=h\circ g`, where `g` performs the first flip.  Starting with
`x\in D_(2m)^0`, put

\[
 x_0=x,\qquad y_i=g(x_i),\qquad x_{i+1}=h(y_i)=f(x_i)
       \quad(0\le i<m).                                 \tag{3.1}
\]

Interpret `x_i` as an `m`-subset of `[2m]` and `y_i` as an `(m+1)`-subset.
With a new coordinate `\infty`, set

\[
                 \widetilde y_i=([2m]\setminus y_i)\cup\{\infty\}.
\]

Then

\[
 c(x)=(x_0,\widetilde y_0,x_1,\widetilde y_1,
             \ldots,x_{m-1},\widetilde y_{m-1},x_m)     \tag{3.2}
\]

is a `C_(2m+1)` in the odd graph.  The endpoint identity

\[
                         x_m=[2m]\setminus x_0
\]

closes the cycle.  As `x` ranges over the `C_m` ordinary Dyck paths, the
cycles (3.2) are vertex-disjoint and cover every middle set.

Let

\[
 \pi(x)=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1})       \tag{3.3}
\]

be the MSW flip-position permutation: `a_i` is inserted by `g` and `b_i` is
deleted by `h`.  The omitted-edge label word of (3.2) is exactly

\[
                    \widehat\pi(x)=(\pi(x),\infty).     \tag{3.4}
\]

This follows because the edge `x_i \widetilde y_i` omits `a_i`, the edge
`\widetilde y_i x_(i+1)` omits `b_i`, and the closing edge `x_mx_0` omits
`\infty`.

## 4. Exact depth-one shadow formula

For a general minimum odd cycle with omitted-label word

\[
                         q=(q_0,\ldots,q_{n-1}),
\]

the associated middle sets are (2.3).  Tight-neighbouring middle intervals
are two steps apart in this odd-cycle order.  Their rank-`m-1` intersection is

\[
 L_i(q)
   :=A_i\cap A_{i-2}
    =\{q_{i+1},q_{i+3},\ldots,q_{i+2m-3}\},             \tag{4.1}
\]

with indices modulo `n`.  Its complement

\[
                         U_i(q)=[n]\setminus L_i(q)     \tag{4.2}
\]

is the corresponding rank-`m+2` interval.  Hence lower rank `m-1` and upper
rank `m+2` have exactly the same coverage and collision multiplicities.

For the MSW factor, substitute `q=widehat(pi)(x)` from (3.4).  Define

\[
 \mu(S)=\#\{(x,i):x\in D_{2m}^0,\ i\in\mathbb Z_n,
                       \ L_i(\widehat\pi(x))=S\}.       \tag{4.3}
\]

Then the first noncentral lower shadow is complete exactly when

\[
                         \mu(S)>0
             \quad\text{for every }S\in\binom{[n]}{m-1}.
\]

Two slots collide exactly when their alternating subwords in (4.1) give the
same unordered set.  Formulae (4.1)--(4.3), together with the recursive MSW
formula

\[
 \pi(1u0v)=
   \bigl(|u|+2,\ |u|+2-\pi(\operatorname{rev}u),\ 1,
                    \ |u|+2+\pi(v)\bigr),              \tag{4.4}
\]

are an exact, recursion-only collision test.
Here `rev(u)` means reverse the word `u` and interchange its up- and
down-steps, as in the MSW paper.

There is also a useful description directly in the Chung--Feller paths.  The
entire multiset of rank-`m-1` colors from the cycle (3.2) is

\[
\begin{aligned}
 &x_i\cap x_{i+1} &&(0\le i<m),                         \tag{4.5a}\\
 &[2m]\setminus y_0,\quad[2m]\setminus y_{m-1},        \tag{4.5b}\\
 &\{\infty\}\cup\bigl([2m]\setminus(y_{i-1}\cup y_i)\bigr)
                                      &&(1\le i<m).     \tag{4.5c}
\end{aligned}
\]

Thus a target not containing `infinity` is missing precisely when it belongs
to neither (4.5a) nor (4.5b), and a target containing `infinity` is missing
precisely when it is absent from (4.5c).  This is the exact obstruction, not
an envelope or Hall relaxation.

## 5. The MSW factor is not vertically complete

The first failure occurs at `m=4`.  Recursion (4.4) over the fourteen Dyck
paths gives a factor of `KG(9,4)`.  Its `14*9=126` rank-three slots have the
multiplicity distribution

\[
  \#\{S:\mu(S)=0,1,2,3\}=(4,35,44,1).                 \tag{5.1}
\]

The four missing rank-three masks are

\[
              \{1,4,7\},\quad \{2,5,8\},
              \quad\{2,5,9\},\quad\{4,7,9\}.          \tag{5.2}
\]

Here `9` is the distinguished coordinate `infinity`.  By (4.2), the four
missing rank-six masks are their complements:

\[
 \{2,3,5,6,8,9\},\quad
 \{1,3,4,6,7,9\},\quad
 \{1,3,4,6,7,8\},\quad
 \{1,2,3,5,6,8\}.                                    \tag{5.3}
\]

Thus the exact middle factor does **not** automatically cover even the first
noncentral ranks.  This is a mathematical counterexample to using the MSW
factor unchanged as the central row of the OR construction.

For orientation only, direct evaluation of (4.3) gives the following missing
counts; these data are not used as a theorem.

\[
\begin{array}{c|rrrrrrrrr}
m&4&5&6&7&8&9&10&11&12\\ \hline
\#\{S:\mu(S)=0\}
 &4&32&176&837&3709&15811&65860&270337&1098850
\end{array}
\]

In particular, the defect is not behaving like a bounded seam error.

## 6. Distinguished-coordinate path-factor normal form

The exact factor suggests a better general search space.  Fix the coordinate
`infinity`.  Every wreath has `m+1` middle windows avoiding `infinity`, and
they occur consecutively in its tight order.  They form a Johnson path

\[
                       X_0,X_1,\ldots,X_m              \tag{6.1}
\]

in `binom([2m],m)` with

\[
                       X_m=[2m]\setminus X_0.           \tag{6.2}
\]

Put

\[
                       Y_i=X_i\cup X_{i+1}.             \tag{6.3}
\]

The `Y_i` are `(m+1)`-sets.  Conversely, (6.1)--(6.3) give the wreath

\[
 X_0,\ ([2m]\setminus Y_0)\cup\{\infty\},\ X_1,
 \ldots,([2m]\setminus Y_{m-1})\cup\{\infty\},\ X_m.
                                                               \tag{6.4}
\]

Therefore an exact wreath decomposition is equivalent to a collection of
`C_m` paths (6.1) such that

* the `X`-vertices partition `binom([2m],m)`;
* the edge-unions `Y_i` partition `binom([2m],m+1)`;
* every path joins complementary endpoints.

For any such path factor, its depth-one colors are exactly

\[
\begin{aligned}
 &X_i\cap X_{i+1} &&(0\le i<m),\\
 &[2m]\setminus Y_0,\quad[2m]\setminus Y_{m-1},\\
 &\{\infty\}\cup([2m]\setminus(Y_{i-1}\cup Y_i))
                                      &&(1\le i<m).
\end{aligned}                                           \tag{6.5}
\]

This is the correct next combinatorial problem: construct a complementary
Johnson path factor satisfying the two rainbow conditions in (6.5), then
extend the same factor to deeper shadows.  The MSW factor is one explicit
path factor, but (5.2) proves that its particular layered matchings are not
the required rainbow choice.

The slot excess is already only lower order.  Per path there are `m+2`
slots in (6.5) not containing `infinity`, versus `m C_m` such targets in
total, and `m-1` slots containing `infinity`, versus

\[
                  \binom{2m}{m-2}
                    =\frac{m(m-1)}{m+2}C_m
\]

such targets.  Hence exact depth-one coverage asks for only the forced
`O(C_m)=O(W/m)` collisions.  It is a sharply structured rainbow path-factor
problem, not a cycle-packing problem.
