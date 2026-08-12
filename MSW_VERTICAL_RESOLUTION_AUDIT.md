# Vertical audit of the Mütze--Standke--Wiechert factor

This note separates three facts which are easy to conflate.

1.  The Mütze--Standke--Wiechert (MSW) construction gives an exact
    `C_(2m+1)`-factor of the odd graph, hence an exact decomposition of the
    middle layer into tight wreaths.
2.  The even-core Chung--Feller columns have a perfect **upper** first
    shadow.
3.  Neither the columns nor the resulting odd wreaths have a perfect lower
    first shadow.  In particular, the unchanged MSW factor is not a vertical
    cyclic-interval SCD.

The primary source is Mütze, Standke and Wiechert,
[A minimum-change version of the Chung--Feller theorem for Dyck paths](https://tmuetze.de/papers/dyck.pdf),
especially Lemmas 6, 12--14 and Theorem 4.

## 1. Flip coordinates and the exact column formula

Fix a Dyck path `x in D_(2m)^0`.  Following MSW, write

\[
 x_i=f^i(x),\qquad y_i=g(x_i),\qquad x_{i+1}=h(y_i)
       \quad(0\le i<m).
\]

Let `a_i` be the coordinate inserted by `g`, and let `b_i` be the coordinate
deleted by `h`.  Thus

\[
             \pi(x)=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1}).       \tag{1.1}
\]

Lemma 12 says that (1.1) is a permutation of `[2m]`.  Since each coordinate
is flipped exactly once, the initial up-step set is

\[
                         x_0=\{b_0,\ldots,b_{m-1}\},
\]

and, for every `0<=i<=m`,

\[
 \boxed{
 x_i=\{a_0,\ldots,a_{i-1}\}\ \cup\
       \{b_i,\ldots,b_{m-1}\}.
 }                                                               \tag{1.2}
\]

Consequently the intersection and union of a window of `q+1` consecutive
column states are

\[
 \boxed{
 \begin{aligned}
 L_{x,i}^{(q)}
   &=\bigcap_{s=0}^{q}x_{i+s}
     =\{a_0,\ldots,a_{i-1}\}\cup
       \{b_{i+q},\ldots,b_{m-1}\},\\
 U_{x,i}^{(q)}
   &=\bigcup_{s=0}^{q}x_{i+s}
     =\{a_0,\ldots,a_{i+q-1}\}\cup
       \{b_i,\ldots,b_{m-1}\},
 \end{aligned}
 }                                                               \tag{1.3}
\]

for `0<=i<=m-q`.  Formula (1.3) is the exact all-depth collision test for the
column proposal.  Lemma 14 makes the two flip-coordinate lists recursively
computable, but it does not imply that the sets in (1.3) cover their layers.

## 2. The one first-shadow theorem which is true

### Theorem 1 (perfect upper shadow of the columns)

As `x` ranges over `D_(2m)^0` and `0<=i<m`, the sets

\[
                         x_i\cup x_{i+1}
\]

are every `(m+1)`-subset of `[2m]` exactly once.

### Proof

By construction,

\[
                 x_i\cup x_{i+1}=y_i=g(x_i).                    \tag{2.1}
\]

The states `x_i`, with `x in D_(2m)^0` and `0<=i<m`, are exactly all balanced
paths outside the final flaw class `D_(2m)^m`: the Chung--Feller columns
partition every flaw class, and only their final states belong to `D^m`.
MSW Lemma 6 states that

\[
 g:L_{2m,m}\setminus D_{2m}^m\longrightarrow L_{2m,m+1}
\]

is a bijection.  Equation (2.1) proves the claim. QED.

The tempting dual statement for intersections is false.  The paper proves
only the endpoint identity `x_m=bar(x_0)`.  It does **not** prove

\[
                         x_{m-i}=\overline{x_i},
\]

and that relation is false in general.  Thus complementation cannot be used
edge-by-edge to turn Theorem 1 into a lower-shadow theorem.

For the lower first shadow, the exact map is simply

\[
 \lambda(x_i)=x_i\cap x_{i+1}
   =\{a_0,\ldots,a_{i-1}\}\cup\{b_{i+1},\ldots,b_{m-1}\}.       \tag{2.2}
\]

Its domain and codomain have the same cardinality,

\[
 |\mathcal D_m|m=\binom{2m}{m-1},
\]

so every missing lower set is paired with a collision.  Two column slots
collide precisely when the two prefix--suffix sets in (2.2) agree.  This is
the exact collision characterization; unlike (2.1), the map (2.2) is not a
bijection.

The smallest failure is visible directly in MSW Figure 4, with no search.
For `m=3` the five flip permutations are

\[
\begin{gathered}
(6,2,4,3,5,1),\quad(6,4,5,2,3,1),\quad
(4,2,3,1,6,5),\\
(2,1,4,3,6,5),\quad(2,1,6,4,5,3).
\end{gathered}                                                   \tag{2.3}
\]

Substitution in (2.2) gives thirteen of the fifteen two-subsets.  The two
missing sets are

\[
                         \{1,4\},\qquad\{3,6\},                  \tag{2.4}
\]

while `\{1,6\}` and `\{3,4\}` each occur twice.  Thus the failure of the
lower-column analogue of Theorem 1 begins in dimension six and is already
certified by the permutations printed in the primary paper.

## 3. Passing to the odd wreath does not repair the defect

Add a coordinate `infinity`.  The MSW odd cycle is

\[
 (x_0,\widetilde y_0,x_1,\widetilde y_1,\ldots,
        x_{m-1},\widetilde y_{m-1},x_m),
 \qquad
 \widetilde y_i=([2m]\setminus y_i)\cup\{\infty\}.              \tag{3.1}
\]

Its omitted-edge label word is

\[
              q=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1},\infty). \tag{3.2}
\]

For any minimum odd cycle with omitted word `q=(q_0,...,q_(2m))`, all
rank-`m-1` interval shadows have the form

\[
       \{q_{i+1},q_{i+3},\ldots,q_{i+2m-3}\},                   \tag{3.3}
\]

with cyclic subscripts.  Thus two slots collide exactly when the alternating
subwords in (3.3) give the same unordered set.  This is a completely
recursive test after substituting the MSW recursion

\[
 \pi(1u0v)=
 (|u|+2,\ |u|+2-\pi(\operatorname{rev}u),\ 1,
                   |u|+2+\pi(v)).                               \tag{3.4}
\]

The equivalent path formulas and the first explicit failure are recorded in
`ODD_GRAPH_EXACT_WREATH_FACTOR.md`.  In particular, for `m=4` the factor in
`KG(9,4)` misses four rank-three sets.  Therefore **no assignment of radii at
all** can turn the unchanged MSW wreaths into a cyclic-interval SCD: the
available depth-one slots already miss required targets.

## 4. The pointed-height assignment fails even earlier

There is a stronger warning about the natural numerical radius assignment.
The pointed-Dyck identity gives exactly the right global radius histogram,
but assigning the heights of each Dyck path to the starts of its own wreath
is already impossible for `m=2`.

The two Dyck paths are

\[
                    x=1100,\qquad x'=1010.
\]

Their MSW flip permutations are

\[
                    \pi(x)=(4,2,3,1),\qquad
                    \pi(x')=(2,1,4,3).
\]

Up to cyclic rotation, the corresponding tight coordinate orders are

\[
 \omega=(2,1,4,3,5),\qquad
 \omega'=(1,3,2,4,5).                                          \tag{4.1}
\]

At depth one, an active start in one of these orders represents

* the singleton consisting of its current coordinate; and
* the four-set complementary to its preceding coordinate.

Thus five active starts cover both ranks exactly when their directed
predecessor-to-current edges form a directed cycle cover of `[5]`.
The two possible edge permutations from (4.1) are

\[
\begin{array}{c|ccccc}
t&1&2&3&4&5\\ \hline
s_\omega(t)&4&1&5&3&2\\
s_{\omega'}(t)&3&4&2&5&1.
\end{array}                                                     \tag{4.2}
\]

The permutation `s_omega^(-1)s_(omega')` is the five-cycle

\[
                         (1\ 4\ 3\ 5\ 2).                      \tag{4.3}
\]

Hence the union of the two bipartite permutation matchings is one alternating
ten-cycle.  It has exactly two perfect matchings: select all five starts of
`omega`, or select all five starts of `omega'`.

On the other hand, the two pointed height multisets are

\[
 (0,1,2,1,0),\qquad(0,1,0,1,0).
\]

They demand respectively three and two depth-one active starts.  No
`3+2` choice is one of the two perfect matchings above.  This proves:

> Even if the five pointed heights may be assigned arbitrarily to the five
> starts inside their own wreath, the per-Dyck-path height quotas cannot
> resolve depth one.

This does not contradict the pointed-Dyck radius identity.  That identity is
only a global count.  A vertical resolution would have to move radius mass
between different wreaths.  Indeed, for `m=2`, activating all starts of one
wreath and none of the other resolves depth one, and one of the active chains
may then be extended to radius two.

## 5. Exact lesson for the global program

The MSW theorem completely settles the middle-only wreath problem, but its
particular cycle factor cannot be used unchanged for the OR construction.
The correct object to vary is the **complementary Johnson path factor**:

\[
 X_0,X_1,\ldots,X_m,\qquad X_m=[2m]\setminus X_0,                \tag{5.1}
\]

where all `X` vertices partition the middle layer and all edge unions
`X_i union X_(i+1)` partition rank `m+1`.  MSW supplies one such factor via
Theorem 1.  The next theorem must rewire the paths while retaining those two
properties and making the lower colors, then deeper shadows, complete.

This is strictly smaller than searching for odd cycles from scratch and
strictly more flexible than attaching the unmodified Dyck-height profile to
the explicit MSW cycles.
