# Short-peak density: an explicit `3/8` counterexample

## 1. The theorem ledger

Work in

\[
H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                         \ |x|,|y|,|z|\le a\},
\qquad M_a=3a^2+3a+1.
\]

For a scalar coordinate word and a threshold `h`, a **threshold run** is a
maximal interval on which that coordinate is at least `h`.  Its cost is

\[
                         \lambda=|\text{run}|-1.
\]

Put

\[
                         L=4a+2,
\qquad N_a=M_a-L+1=3a^2-a,
\]

so that `N_a` is the number of length-`L` windows in a linear ordering of
`H_a`.

The proposed short-peak density assertion was that some absolute
`eta>0` should force more than a `(2/3+eta)` proportion of these windows to
contain an internal threshold run with `lambda<=a`.

### Theorem 1 (the proposed density assertion is false)

For every `a`, there is an explicit ordering of `H_a` for which the number
of length-`L` windows containing an internal threshold run of cost at most
`a` is at most

\[
 R_a+1,
 \tag{1.1}
\]

where, on putting `q=floor((a-1)/2)`,

\[
 R_a=M_a-3\left(q(a+1)+\frac{q(q+1)}2\right).
 \tag{1.2}
\]

Consequently

\[
 \frac{R_a+1}{N_a}=\frac38+O(a^{-1}).
 \tag{1.3}
\]

In particular, no positive `eta` can make the proposed
`2/3+eta` lower bound true.  In fact even `2/3-o(1)` is false.
If “length” is interpreted as the number of run positions rather than the
capped-run cost `lambda`, the same counterexample applies a fortiori.

This is a completely explicit, search-free counterexample.  It uses only
full coordinate lines and elementary sign checks.

### What this does and does not prove

Proved here:

* the exact construction and count (1.1)--(1.3);
* the stronger fact that a suffix containing
  `(15/8+O(1/a))a^2` points has no short internal threshold run away from
  its first position; and
* therefore the particular density route to a `(4-epsilon)a^3` universal
  capped-run bound cannot work.

Not proved here:

* that the complete ordering defeats every heterogeneous run assignment;
* that its minimum clipped assignment cost is at least `4a^3-o(a^3)`;
* a subquadratic three-box construction; or
* the original conjecture `nu(k)=B(k)`.

The counterexample refutes one proposed sufficient lemma, not the overall
fan-capped program.

## 2. Three families of high lines

Let

\[
 q=\left\lfloor\frac{a-1}{2}\right\rfloor,
 \qquad
 I_a=\{a-q,a-q+1,\ldots,a-1\}.
 \tag{2.1}
\]

Every `t in I_a` satisfies

\[
                         t>\frac a2.
 \tag{2.2}
\]

For each such `t`, define three full coordinate lines, equipped with the
displayed order:

\[
\begin{aligned}
X_t&=\bigl((t,y,-t-y):-a\le y\le a-t\bigr),
                                     &&y\text{ increasing},\\
Y_t&=\bigl((-t-z,t,z):-a\le z\le a-t\bigr),
                                     &&z\text{ increasing},\\
Z_t&=\bigl((x,-t-x,t):-a\le x\le a-t\bigr),
                                     &&x\text{ increasing}.
\end{aligned}
\tag{2.3}
\]

Each line contains

\[
                         2a+1-t\ge a+2
 \tag{2.4}
\]

points.

### Lemma 2 (the selected lines are pairwise disjoint)

The `3q` lines in (2.3), as `t` ranges over `I_a`, are pairwise disjoint.

#### Proof

Parallel lines of one coordinate are disjoint.  An `x=t` line and a
`y=u` line could meet only in

\[
                         (t,u,-t-u).
\]

This point lies in `H_a` only if `t+u<=a`.  But (2.2) gives `t+u>a`.
The `x/z` and `y/z` cases are identical.  \(\square\)

Thus their union may be used as a literal suffix of a permutation, with no
duplicate point.

## 3. The rotating high-line suffix

List the values of `I_a` in any order, say increasingly, and concatenate

\[
                         X_t\;\Vert\;Y_t\;\Vert\;Z_t
 \tag{3.1}
\]

for each successive `t`.  Call the resulting word `B_a`.

The endpoints of its blocks are

\[
\begin{array}{c|c|c}
\text{block}&\text{first point}&\text{last point}\\ \hline
X_t&(t,-a,a-t)&(t,a-t,-a)\\
Y_t&(a-t,t,-a)&(-a,t,a-t)\\
Z_t&(-a,a-t,t)&(a-t,-a,t).
\end{array}
\tag{3.2}
\]

Since every two selected levels have sum greater than `a`, the transition
from `Z_t` to the next `X_u` also satisfies `t+u>a`.

### Lemma 3 (all interior peaks of the suffix are long)

Apart from a possible local maximum created at the very first position by
the word preceding `B_a`, every internal local-maximum plateau of every
coordinate in `B_a` is one of the full blocks `X_t`, `Y_t`, or `Z_t`.
It consequently contains at least `a+2` positions and has cost at least
`a+1`.

#### Proof

Inside the three block types, the coordinate signs are

\[
\begin{array}{c|ccc}
       &x&y&z\\ \hline
X_t&0&+&-\\
Y_t&-&0&+\\
Z_t&+&-&0.
\end{array}
\tag{3.3}
\]

At `X_t|Y_t`, the `x` coordinate strictly falls, the `y` coordinate
strictly rises, and the `z` coordinate equals `-a` on the two boundary
points.  The latter two-point plateau is a strict local minimum, because
the adjacent values inside both blocks are `-a+1`.

At `Y_t|Z_t`, the analogous local-minimum plateau is `x=-a`.  At
`Z_t|X_u`, it is `y=-a`; moreover

\[
 a-t<u,\qquad a-u<t
\]

because `t+u>a`, so the other two coordinate comparisons are strict and
have the signs shown in (3.3).

It follows that the only `+`-to-`-` reversals in any coordinate word occur
across its full constant-coordinate block.  Every other constant plateau
at a join is a `-a` local minimum.  Formula (2.4) gives the length claim.
Only the incoming comparison at the first position of `B_a` is not
controlled by this internal sign ledger.  \(\square\)

### Lemma 4 (an internal threshold run contains a peak plateau)

Every internal maximal component of a scalar upper-threshold set contains
an internal local-maximum plateau of that scalar word.

#### Proof

Choose the maximum scalar value on the component and one maximal plateau
on which that value is attained.  Its two neighboring values are smaller:
inside the component this follows from maximality of the chosen plateau,
and at a component boundary the outside value is below the threshold and
hence below the maximum.  Thus it is an internal local-maximum plateau.
\(\square\)

### Corollary 5 (the clean suffix has no short threshold run)

Every internal threshold run lying wholly in `B_a` and not using a
possible seam maximum at the first suffix position has

\[
                         \lambda\ge a+1.
 \tag{3.4}
\]

Indeed, Lemma 4 puts a plateau from Lemma 3 inside it.

## 4. Complete the permutation and count contaminated windows

Order all points not used by `B_a` arbitrarily, call this prefix `P_a`, and
set

\[
                         T=P_a\;\Vert\;B_a.
 \tag{4.1}
\]

Let `R_a=|P_a|`.  By Lemma 2 and the line-size formula,

\[
\begin{aligned}
 |B_a|
   &=3\sum_{t=a-q}^{a-1}(2a+1-t)\\
   &=3\sum_{j=1}^{q}(a+1+j)\\
   &=3\left(q(a+1)+\frac{q(q+1)}2\right),
\end{aligned}
\tag{4.2}
\]

which proves (1.2).

By Corollary 5, a threshold run of cost at most `a` either meets `P_a` or
is created by the single uncontrolled incoming comparison at the first
position of `B_a`.  In both cases its left endpoint is at most `R_a+1`.

A window containing an entire run must start no later than the left
endpoint of that run.  Hence every length-`L` window containing a short
internal threshold run has start at most `R_a+1`.  There are at most
`R_a+1` such windows.  This proves (1.1).

Finally `q=a/2+O(1)`, so

\[
 |B_a|=\frac{15}{8}a^2+O(a),
 \qquad
 R_a=\frac98a^2+O(a),
 \qquad
 N_a=3a^2-a.
\tag{4.3}
\]

Dividing proves (1.3).

For reference, the exact parity forms are as follows.  If `a=2m`, then

\[
 R_a=\frac{9m^2+21m+8}{2};
\tag{4.4}
\]

if `a=2m+1`, then

\[
 R_a=\frac{9m^2+21m+14}{2}.
\tag{4.5}
\]

## 5. Why the constant `2/3` heuristic fails

The tempting averaging argument was:

* every length-`(4a+2)` window contains some peak;
* a short peak costs at most `a`;
* every peak costs at most `2a`;
* therefore a short-peak density above `2/3` would push the average below
  `4a/3` and the total below `4a^3`.

The missing premise is exactly the density statement.  The construction
above packs long peaks into a rotating suffix:

\[
 X\text{-line}\longrightarrow
 Y\text{-line}\longrightarrow
 Z\text{-line}\longrightarrow
 X\text{-line}.
\]

At every join, the coordinate shared by the two varying directions sits at
its global minimum `-a`.  Thus the join creates a valley rather than a
short peak.  The peak-edge sets remain disjoint, but that is no obstacle:
the suffix uses many full lines of length between `a+2` and roughly
`3a/2`, and their service windows overlap heavily.

This explains why the three facts

* disjoint peak-edge sets,
* three coordinate directions, and
* the line-size formula `2a+1-|t|`

do not imply positive short-peak density.  They instead permit the explicit
rotating packing above.

## 6. The surviving mathematical target

The density lemma must be replaced by a genuinely weighted statement.  A
future proof of a universal cheap cover would have to use at least one of
the following features, none of which is captured by the binary predicate
`lambda<=a`:

1. the exact distribution of the long costs
   `lambda=2a-t` across the selected levels;
2. non-peak threshold components spanning two or more line blocks;
3. a heterogeneous choice of leftward and rightward runs rather than the
   shortest peak in one fixed forward window; or
4. a global incompatibility between a large rotating suffix and the lower
   target witness geometry that generated the middle ordering.

The most concrete next question is therefore the weighted extremal problem

\[
 \max_T\sum_i\min(\lambda^*(i),a),
\]

or its uncapped `q_i` analogue, evaluated on the explicit family (4.1).
The present theorem says that replacing this weighted problem by a
`short/not-short` window count loses too much information.
