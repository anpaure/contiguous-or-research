# A depth-two compiler obstruction with a perfectly rainbow first shadow

Date: 2026-07-25

Method: exact mathematics only.

## 0. Outcome

The arbitrary-word obstruction in the H1 compiler obstruction note is not
merely a failure of first-shadow rainbowness. It has an exact one-rank
suspension.

For every \(R\ge4\) there is a cyclic rank-three Johnson walk with
\(S=2R\) owners such that

* all \(S\) adjacent lower intersections are pairwise distinct;
* every three-owner intersection used below is floor-correct; but
* every arbitrary nonzero contiguous-OR word covering the owners and the
  lower intersections through depth two has length

\[
 \boxed{L\ge S+\frac{S}{24}.}                     \tag{0.1}
\]

Adding a fixed core lifts the example to every rank at least three.
Consequently exact PBBS first-shadow uniqueness is not, by itself, enough
for an \(S+O(H)\) compiler. The first genuine compiler obstruction can
begin at depth two.

## 1. The suspended walk

Use distinct coordinates

\[
 b_0,\ldots,b_{R-1},p_0,\ldots,p_{R-1},
\]

with subscripts modulo \(R\). Put

\[
\begin{aligned}
 Z_t^-&=\{b_{t-1},b_t,p_t\},\\
 Z_t^+&=\{b_t,p_t,b_{t+1}\}.
\end{aligned}                                      \tag{1.1}
\]

Consider the cyclic rank-three sequence

\[
 Z_0^-,Z_0^+,Z_1^-,Z_1^+,\ldots,
 Z_{R-1}^-,Z_{R-1}^+.                              \tag{1.2}
\]

Consecutive sets are Johnson adjacent. More exactly,

\[
 Z_t^-\cap Z_t^+=\{b_t,p_t\}=:Y_t,                \tag{1.3}
\]

and

\[
 Z_t^+\cap Z_{t+1}^-=\{b_t,b_{t+1}\}=:X_t.        \tag{1.4}
\]

The \(2R\) sets \(X_t,Y_t\) are pairwise distinct. Thus the complete
depth-one lower-colour map of (1.2) is injective.

At depth two,

\[
 Z_{t-1}^+\cap Z_t^-\cap Z_t^+
 =\{b_t\},                                         \tag{1.5}
\]

and

\[
 Z_t^-\cap Z_t^+\cap Z_{t+1}^-
 =\{b_t\}.                                         \tag{1.6}
\]

Both are rank-one sets, the floor-correct rank \(3-2\).

## 2. Transfer of the arbitrary-word lower bound

The required target subfamily consisting of

* the depth-two lower sets \(\{b_t\}\);
* the depth-one lower sets \(X_t,Y_t\); and
* the owners \(Z_t^-,Z_t^+\)

is exactly the target family used in the H1 obstruction, under the
dictionary

\[
\begin{array}{c|c}
\text{old depth-one family}&\text{suspended family}\\ \hline
\{b_t\}&\text{depth-two lower target},\\
X_t,Y_t&\text{depth-one lower target},\\
U_t^-,U_t^+&Z_t^-,Z_t^+\text{ (owner target)}.
\end{array}                                        \tag{2.1}
\]

That proof uses only these displayed sets, not the rank names attached to
them. It permits arbitrary helper letters and arbitrary witness intervals.
Hence it applies verbatim and yields

\[
 L\ge2R+\frac{R}{12}
   =S+\frac{S}{24}.                                \tag{2.2}
\]

A word covering all depth-two lower and upper data certainly covers this
subfamily, so (2.2) is also a lower bound for the full depth-two compiler.

## 3. Fixed-core and odd-graph lifts

For any \(k\ge3\), adjoin a fixed core \(G\) of size \(k-3\) to every
owner and target. Projecting an arbitrary word to the active
\(\{b_t,p_t\}\)-coordinates and deleting zero letters transfers it back
to the rank-three example, so (2.2) remains valid.

In particular, take \(k=m+1\) and \(|G|=m-2\). The construction fits in
\([2m+1]\) whenever

\[
 2R+(m-2)\le2m+1,
\]

so one may take \(S=2R=\Theta(m)\).

It also has the standard integral odd-graph lift. Alternate the
rank-\(m\) complements of the lifted \(Z\)-owners with their distinct
rank-\(m\) edge intersections from (1.3)--(1.4). Consecutive terms are
disjoint. This proves compatibility with exact odd-graph local incidence,
although it does not assert that the cycle belongs to the canonical PBBS
factor.

## 4. Coefficient-one boundary

The first-shadow obstruction from the unsuspended star chain is excluded
by the actual PBBS identity

\[
 X_j\cap X_{j+1}=A_{2j+1},
\]

because the intervening exact middle owners are distinct. The suspended
example proves that this safeguard stops at depth one: pairwise distinct
first shadows coexist with a linear arbitrary-word obstruction generated
by repeated, floor-correct second shadows.

Therefore an \(S+O(H)\) PBBS compiler must use a genuinely deeper
property—balanced second-shadow support, residence chronology, or global
packet rethreading. First-shadow rainbowness plus Johnson adjacency is
rigorously insufficient.
