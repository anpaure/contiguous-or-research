# Lower-bound audit for the three-chain box conjecture

## 1. Question and outcome

Let

\[
 P(p,q,r)=[0,p]\times[0,q]\times[0,r]
\]

be embedded as three disjoint chains of singleton increments.  Thus the point
`(a,b,c)` denotes the union of the first `a`, first `b`, and first `c`
increments in the three coordinate blocks.  Write `g_3(p,q,r)` for the least
length of a word of arbitrary increment masks whose nonempty contiguous unions
contain every nonzero point of `P(p,q,r)`.

The basic endpoint and interval-slack arguments do **not** disprove

\[
 g_3(p,q,r)\leq \operatorname{width}P(p,q,r)+O(p+q+r+1).
\]

They instead show that an additive surface-scale term is genuinely necessary.
For the cubic box one gets the sharp scale

\[
 \boxed{
 g_3(d,d,d)\geq \operatorname{width}P(d,d,d)
                    +{2d\over3}+O(1).}
\]

The coefficient `2/3` comes from the interval-slack count at the middle rank.
Pure coordinate axes and coordinate faces give further necessary support
conditions, but they cannot simply be added to the middle-rank bound: the same
physical positions can participate in both kinds of witnesses.

Consequently, any counterexample with excess `Omega(width)` must use a new
transition, precedence, pinning, or collision obstruction.  Antichain size,
endpoint injectivity, short-interval capacity, axes, and faces by themselves
all live on the allowed boundary scale.

There is one genuine structural no-go: the most obvious **fixed central-row**
proof cannot work for cubic boxes.  At every admissible rank-slack delay, the
three top coordinate increments are too rare and pairwise incompatible to
satisfy the factorization run condition.  This kills the ansatz
`T=D^t A` with `T` a permutation of the middle layer; it does not kill an
unrestricted word with variable middle-rank witness intervals.

## 1.1 Exact coordinatewise-closure reduction

The local problem has a simpler exact normal form that should be used in any
further attack.

For an arbitrary increment mask `E`, define its coordinatewise closure

\[
 \operatorname{cl}(E)=(h_X(E),h_Y(E),h_Z(E)),
\]

where `h_X(E)` is the largest index of an `X`-increment in `E`, or zero if
there is none, and similarly for the other axes.  The triple denotes the union
of the corresponding three prefixes.

### Theorem 0 (range-maximum normal form)

Replacing every word entry `E_i` by `cl(E_i)` preserves every interval whose
union is a box point.  Consequently, `g_3(p,q,r)` is exactly the least length
of a sequence of nonzero triples

\[
 v_i=(x_i,y_i,z_i)\in[0,p]\times[0,q]\times[0,r]
\]

such that every nonzero triple `(x,y,z)` is the componentwise maximum of one
contiguous range:

\[
 (x,y,z)=\left(\max_{i\in I}x_i,
                 \max_{i\in I}y_i,
                 \max_{i\in I}z_i\right).           \tag{1.1}
\]

### Proof

Closure commutes with union:

\[
 \operatorname{cl}\!\left(\bigcup_{i\in I}E_i\right)
      =\bigvee_{i\in I}\operatorname{cl}(E_i),       \tag{1.2}
\]

where the join on the right is componentwise maximum.  If the original union
is a box target, it is already coordinatewise closed, so (1.2) is that same
target.  Thus every old witnessing interval survives closure.  Conversely,
closed triples are legal increment masks, so any range-maximum sequence is an
OR word for the box.  Zero triples may be deleted in the nonzero problem
without destroying any nonzero witness. \(\square\)

This reduction loses nothing and turns the local conjecture into a purely
geometric problem about contiguous range maxima of points in an integer box.

## 2. Rank-slack theorem for an arbitrary chain box

Let

\[
 m_s=[z^s](1+z+\cdots+z^p)(1+z+\cdots+z^q)
                       (1+z+\cdots+z^r)
\]

and

\[
 L_s=\sum_{j=1}^{s-1}m_j.
\]

Thus `m_s` is the number of box points of rank `s`, while `L_s` counts the
nonzero points strictly below rank `s`.

### Theorem 1 (box rank-slack bound)

For every `s`,

\[
 g_3(p,q,r)\geq m_s+\tau_s,
\]

where `tau_s` is the least nonnegative integer `t` satisfying

\[
 \boxed{L_s\leq t m_s+{t+1\choose2}.}                 \tag{2.1}
\]

Hence

\[
 g_3(p,q,r)\geq
 \max_s\bigl(m_s+\tau_s\bigr).                       \tag{2.2}
\]

### Proof

Suppose a word has length `n=m_s+t`.  Choose one witnessing interval for each
rank-`s` point.  Two chosen intervals cannot contain one another: containment
of intervals implies containment of their unions, while two distinct points
of the same rank are incomparable.

Order the `m_s` selected intervals by increasing left endpoint,

\[
 I_i=[\ell_i,u_i],\qquad 1\leq i\leq m_s.
\]

Their right endpoints are also strictly increasing.  Both endpoint sequences
are increasing `m_s`-subsets of `[m_s+t]`, so

\[
             i\leq \ell_i\leq u_i\leq i+t.            \tag{2.3}
\]

Every physical interval `J=[a,b]` of length at least `t+1` has `a<=m_s` and
contains

\[
 I_a\subseteq[a,a+t]\subseteq J.
\]

Its union therefore contains a rank-`s` target and has at least `s`
increments.  A target of rank below `s` must consequently use a physical
interval of length at most `t`.

There are exactly

\[
 \sum_{h=1}^t(n-h+1)
   =t m_s+{t+1\choose2}
\]

such intervals.  Distinct target masks require distinct physical intervals,
which proves (2.1).  \(\square\)

This proof permits completely arbitrary word entries.  If an interval has a
box point as its union, every entry in it is automatically a subset of that
point, since union has no cancellation.

## 3. Exact cubic middle layer

Put `P_d=P(d,d,d)` and `M_d=width(P_d)`.

### Even side length

If `d=2a`, the unique middle rank is `3a`, and inclusion-exclusion gives

\[
 M_d=3a^2+3a+1.                                      \tag{3.1}
\]

There are `(2a+1)^3` points in total.  By rank symmetry, the number of
nonzero points strictly below the middle rank is

\[
 L_d={ (2a+1)^3-M_d\over2}-1
     =4a^3+{9\over2}a^2+{3\over2}a-1.                \tag{3.2}
\]

Let `tau_d` be the least integer satisfying

\[
 L_d\leq \tau_d M_d+{\tau_d+1\choose2}.
\]

Substitution of `tau_d=(4/3)a+c` into (3.1)--(3.2) gives

\[
 \tau_d={4a\over3}+O(1)={2d\over3}+O(1).             \tag{3.3}
\]

More precisely, at the real quadratic root,

\[
 \tau_d={4a\over3}-{7\over54}+O(a^{-1}),
\]

before rounding upward to an integer.

### Odd side length

If `d=2b-1`, the two middle ranks have the common size

\[
 M_d=3b^2.                                            \tag{3.4}
\]

Using the lower of them, the nonzero points below it number

\[
 L_d=4b^3-3b^2-1.                                    \tag{3.5}
\]

The quadratic root now gives

\[
 \tau_d={4b\over3}-{35\over27}+O(b^{-1})
        ={2d\over3}+O(1).                            \tag{3.6}
\]

Combining Theorem 1 with (3.1)--(3.6) proves

\[
 \boxed{g_3(d,d,d)\geq M_d+{2d\over3}+O(1).}         \tag{3.7}
\]

Thus `width+O(d)` is the smallest possible order of a uniform cubic theorem.
A claim of `width+o(d)` is false.

## 4. A two-boundary obstruction to a fixed central row

Suppose a prescribed row

\[
 T=(T_1,\ldots,T_M)
\]

is to factor with delay `t`:

\[
 T_i=A_i\cup A_{i+1}\cup\cdots\cup A_{i+t}.           \tag{4.1}
\]

Coordinatewise factorization gives the familiar necessary run condition:
every `1`-run strictly internal to the incidence word

\[
 (1_{b\in T_1},\ldots,1_{b\in T_M})
\]

has length at least `t+1`.  Runs touching the first or last row position may
be shorter.

### Lemma 2 (two-boundary rare-coordinate obstruction)

Assume there are three coordinates `x,y,z` such that:

1. each occurs in between `1` and `t` members of `T`; and
2. no member of `T` contains two of `x,y,z`.

Then (4.1) has no factor.

### Proof

The total number of occurrences of each coordinate is at most `t`, so it
cannot have an internal `1`-run: such a run would have length at least `t+1`.
Every nonempty incidence support must therefore contain the first or the last
row position (or both).  The three supports are pairwise disjoint by
assumption 2, but only two boundary positions are available.  Two supports
must contain the same boundary position, a contradiction. \(\square\)

### Theorem 3 (no fixed middle row for an even cube)

Let `d=2a>=2`.  There is no word `A` and no permutation `T` of the middle
rank of `P_d` satisfying

\[
                    T=D^tA
\]

for any `t>=a+1`.

### Proof

Let `x_{2a},y_{2a},z_{2a}` be the top increments in the three coordinate
chains.  A middle point has rank `3a`.  Fixing its first coordinate at `2a`
leaves

\[
                         y+z=a,

\]

so `x_{2a}` occurs in exactly `a+1` middle points.  The same is true of the
other two top increments.  No middle point contains two of them, because two
maximal coordinates already have rank `4a>3a`.  Lemma 2 applies whenever
`t>=a+1`. \(\square\)

The rank-slack delay from Section 3 always lies in this forbidden range.  In
fact, substituting `t=a` into (2.1) gives the deficit

\[
 L_d-\left(aM_d+{a+1\choose2}\right)=a^3+a^2-1>0,

\]

so `tau_d>=a+1` for every `a>=1`.  Therefore:

\[
 \boxed{\text{No rank-slack-optimal cubic construction can have one fixed
 middle row }T=D^{\tau_d}A.}                         \tag{4.2}
\]

The same obstruction holds for odd cubes `d=2b-1>=3` if one uses the lower
middle layer.  Each top increment occurs in exactly `b` lower-middle points,
the three supports are pairwise disjoint, and

\[
 L_d-\left((b-1)M_d+{b\choose2}\right)
   =b^3-{b^2\over2}+{b\over2}-1>0.

\]

Hence `tau_d>=b`, again triggering Lemma 2.

This theorem must not be promoted to an unrestricted lower bound.  For a word
of length `M+t`, selected middle witnesses have the monotone-band form

\[
 I_i=[i+\alpha_i,i+\beta_i],
 \qquad 0\leq\alpha_1\leq\cdots\leq\alpha_M\leq t,
 \quad 0\leq\beta_1\leq\cdots\leq\beta_M\leq t.

\]

They need not all be translates of one fixed window.  Variable boundary
regimes can give the three rare coordinates different effective cuts.  The
fixed-row no-go says that a successful proof of the three-box lemma must use
this freedom (or use repeated/noncentral skeletons), rather than copying the
fixed-delay Boolean construction literally.

## 5. Why optimizing the rank does not change the scale

The middle rank is not an arbitrary choice.  For `d=2a`, throughout the
central quadratic regime,

\[
 m_{3a-y}=M_d-y^2\qquad(0\leq y\leq a).              \tag{5.1}
\]

Moving the selected rank down by `y` removes approximately `y M_d` lower
targets, so its required slack falls by only `y+O(y^2/d)`, while its antichain
term loses `y^2`.  Moving upward reverses the linear slack change but retains
the same quadratic antichain loss.  Therefore only `y=O(1)` can improve the
middle-rank expression, and such an improvement is bounded.

Ranks a fixed positive fraction of `d` from the middle lose `Theta(d^2)` in
layer size and can recover only `O(d)` through the quotient `L_s/m_s`.
Ranks whose layers are `o(d^2)` satisfy the crude quadratic estimate

\[
 \tau_s\leq \sqrt{2(d+1)^3}+O(1)=O(d^{3/2})=o(M_d),  \tag{5.2}
\]

obtained by using only the binomial term in (2.1).  Splitting these three
regimes shows that the complete rank-slack bound (2.2) satisfies

\[
 \max_s(m_s+\tau_s)=M_d+{2d\over3}+O(1).             \tag{5.3}
\]

So no choice of rank upgrades this family of arguments to an
`Omega(M_d)` excess.

## 6. Forced pure-axis entries

The box geometry yields constraints not visible in the rank count.

### Lemma 4 (strict-chain height forcing)

Let

\[
 \varnothing=X_0\subsetneq X_1\subsetneq\cdots\subsetneq X_h
\]

be a strict chain.  Any word whose interval unions include
`X_1,...,X_h` contains at least `h` distinct entries that are subsets of the
corresponding chain targets.

### Proof

Choose `x_i in X_i minus X_{i-1}`.  A witness for `X_i` contains an entry `E_i`
with `x_i in E_i subseteq X_i`.  Define

\[
 \operatorname{ht}(E)=\min\{j:E\subseteq X_j\}.
\]

Then `ht(E_i)=i`; hence the entries `E_i` are distinct. \(\square\)

Apply this to the three coordinate axes.  A witness for a pure first-axis
target cannot contain any increment from the other two axes.  The three
families of forced nonempty entries are disjoint.  Therefore

\[
 \boxed{g_3(p,q,r)\geq p+q+r.}                       \tag{6.1}
\]

This is important for thin boxes, but for a cube it is swallowed by the
quadratic width.  It cannot be added to (3.7), because a pure-axis entry may
also lie inside a selected middle-rank witness.

There is a stronger shell-by-shell form.  Number increments within every
coordinate chain starting at one.  For an entry `E`, define its height to be
the largest increment index appearing in `E`.  Let `A^(h)` be the subsequence
of entries of height exactly `h`, projected onto the level-`h` increments of
the coordinate chains that reach level `h`.

### Theorem 5 (Boolean shell lower bound)

Put

\[
 q_h=\#\{s\in\{p,q,r\}:s\geq h\}.
\]

Then every universal three-box word satisfies

\[
 |A^{(h)}|\geq \nu(q_h),
 \qquad
 g_3(p,q,r)\geq\sum_{h\geq1}\nu(q_h).                \tag{6.2}
\]

Here `nu(1)=1`, `nu(2)=2`, and `nu(3)=4`.  In particular, if
`p>=q>=r`,

\[
 \boxed{g_3(p,q,r)\geq4r+2(q-r)+(p-q)=p+q+2r.}       \tag{6.3}
\]

### Proof

Fix `h` and a nonempty subset `S` of the `q_h` active coordinate chains.
Choose the box target whose coordinate is `h` on the axes in `S`, `h-1` on
the other active axes, and the full (shorter) chain on every inactive axis.
This target contains precisely the level-`h` increments indexed by `S` and
contains no increment of height greater than `h`.

Every entry of a witness has height at most `h`.  Delete from that witness all
entries of height below `h`.  In the global height-`h` subsequence the retained
entries remain consecutive, and their level-`h` projection has union exactly
`S`.  Thus `A^(h)` is a universal nonzero OR word on `q_h` bits, proving
`|A^(h)|>=nu(q_h)`.  The height classes are disjoint, so summing proves
(6.2)--(6.3). \(\square\)

For a cube this improves the support-only bound from `3d` to `4d`.  It still
cannot be added to the quadratic middle-antichain term: the same four entries
per shell may be used inside middle-rank witnesses.  It is another genuinely
surface-scale constraint, not a width-scale counterexample.

## 7. Forced face-supported subwords

The deletion argument is useful in full generality.

### Lemma 6 (hereditary lower-subbox constraint)

For a word `A` and `0<=u<=p`, `0<=v<=q`, `0<=w<=r`, let

\[
 N(u,v,w)=\#\{j:A_j\subseteq (u,v,w)\},
\]

where `(u,v,w)` denotes the corresponding prefix mask.  If `A` is universal
for `P(p,q,r)`, then

\[
 \boxed{N(u,v,w)\geq g_3(u,v,w).}                    \tag{7.1}
\]

### Proof

Delete every entry not contained in `(u,v,w)`.  A witness for a target in the
lower subbox `P(u,v,w)` contains only entries that are subsets of that target,
so no entry inside that witness is deleted.  It remains a contiguous interval
of the retained subsequence.  The subsequence is therefore universal for the
lower subbox and has length at least `g_3(u,v,w)`. \(\square\)

Let `N_{\bar Z}` be the number of positions whose entries contain no increment
from the third coordinate block.  Every witness for a point of the face
`[0,p]x[0,q]x{0}` lies entirely in such positions.  Delete every other entry
from the word.  A face witness was already a consecutive run of retained
entries, so it remains contiguous after deletion.  The retained subsequence
is therefore a universal word for the two-chain face.

The exact two-chain result is `g_2(p,q)=p+q`: the two pure axes force `p+q`
entries and the usual suffix--prefix word attains it.  Consequently,

\[
 N_{\bar Z}\geq p+q.                                 \tag{7.2}
\]

Cyclically,

\[
 N_{\bar X}\geq q+r,
 \qquad
 N_{\bar Y}\geq p+r.                                \tag{7.3}
\]

Summing (7.2)--(7.3) counts a one-block entry twice, a two-block entry once,
and a three-block entry zero times.  Lemma 4 already supplies `p+q+r`
one-block entries, so the face inequalities can be tight using precisely the
forced axis entries.  Face-supported positions can also be endpoints of
full-box witnesses.  Hence these stronger exact face inequalities still do
not yield an additive width-order loss.

## 8. Scale audit

Let `H=p+q+r` and `V=(p+1)(q+1)(r+1)`.  Every rank has at most `W=width(P)`,
so

\[
                         V\leq(H+1)W.                \tag{8.1}
\]

At a middle rank, the short-interval demand is approximately

\[
 {V/2\over W},                                       \tag{8.2}
\]

which is never larger than `(H+1)/2` by (8.1).  For balanced boxes it is a
positive constant times `H`; for cubic boxes it is `2d/3+O(1)`.

This explains the dimensional match behind the conjecture:

* the main antichain cost is the two-dimensional central cross-section
  `Theta(d^2)`;
* the unavoidable interval-slack repair is the one-dimensional thickness
  `Theta(d)`;
* summing such thickness errors over the Boolean chain boxes is precisely the
  lower-order term in the three-block aggregation theorem.

## 9. The exact orthogonal-chain gate

There is a stronger necessary condition that does not reduce to rank counts.

### Theorem 7 (every word induces two orthogonal chain partitions)

If a target family `P` has a universal contiguous-union word of length `n`,
then `P` has two orthogonal chain partitions, each using at most `n` nonempty
chains.

### Proof

Choose one witness `[l(S),r(S)]` for each target `S`.  Group the targets first
by common right endpoint.  With the endpoint fixed, extending the interval to
the left only increases its union, so every group is a chain.  These groups
partition `P` and there are at most `n` of them.

Group the same targets by common left endpoint.  Extending to the right again
only increases the union, giving a second chain partition with at most `n`
chains.  A chain from the first partition and a chain from the second can
share at most one target, because their intersection would have the uniquely
determined witness interval `[l,r]`.  Thus the partitions are orthogonal.
\(\square\)

Consequently, an `Omega(width)` disproof of the three-box conjecture could be
obtained by proving that every orthogonal pair of chain partitions of the
cube needs `(1+c)M_d` chains.  The elementary longest-chain obstruction is far
too weak here: a cubic box has longest-chain length `3d+1=O(d)`, whereas
`M_d=Theta(d^2)`.  Unlike the two-dimensional grid, orthogonality has enough
nominal room in three dimensions.

Theorem 7 is only a gate.  A word additionally orders the two chain families
by physical endpoints, puts their occupied intersections in the triangular
region `l<=r`, and must realize their labels by coordinatewise unions.  Thus
even a width-sized orthogonal pair would not by itself prove the local OR
lemma, while failure of every near-width orthogonal pair would disprove it.

## 10. What a genuine disproof must show

The following lower-bound mechanisms have now been exhausted at their natural
scale:

1. one antichain per right endpoint;
2. nonnesting of equal-rank witness intervals;
3. counting all physical intervals of bounded length;
4. forced pure-axis entries;
5. forced face-supported endpoints; and
6. optimizing the rank in the interval-slack theorem.

For cubic boxes they give `width + Theta(d)`, not
`(1+c)width`.  An `Omega(width)` counterexample must therefore prove that a
positive fraction of the nominal endpoint chains are unusable or collide.
Plausible sources are:

* a transition obstruction between consecutive suffix-union chains;
* incompatibility of two near-width orthogonal chain covers;
* a precedence obstruction at their intersections;
* coordinatewise pin failure in every near-width growth diagram; or
* a multi-rank collision inequality that cannot be reduced to counting short
  physical intervals.

Conversely, a construction meeting (3.7) up to another `O(d)` term would be
order-sharp locally and would validate the global three-block route.
