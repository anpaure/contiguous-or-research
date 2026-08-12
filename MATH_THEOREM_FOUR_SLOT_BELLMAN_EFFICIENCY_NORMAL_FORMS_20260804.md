# Four-slot Bellman clocks: efficiency normal forms and the first new transient

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  Positivity for all
four-slot tables is not proved here.

Let

\[
 (c_0,c_1,c_2,c_3,c_4)=(0,x,y,z,T)                  \tag{0.1}
\]

be nondecreasing and internally superadditive.  Thus

\[
 y\ge2x,qquad z\ge x+y,qquad
 T\ge x+z,qquad T\ge2y,                            \tag{0.2}
\]

and assume `T>=A=sqrt(pi)/2`.  Its Bellman clock is

\[
 V_0=0,qquad
 V_m=\max_{1\le j\le\min(4,m)}(c_j+V_{m-j}).        \tag{0.3}
\]

Since `x<=y/2`, the maximal efficiency is one of

\[
 {y\over2},qquad {z\over3},qquad {T\over4}.        \tag{0.4}
\]

The three corresponding regimes have the exact forms below.

## 1. Two-slot-efficient regime

### Theorem 1.1

Suppose `y/2` is maximal.  Then

\[
 T=2y,qquad r:=z-y\in[x,y/2],                      \tag{1.1}
\]

and

\[
 V_{2q}=qy,qquad
 V_{2q+1}=
 \begin{cases}
 x,&q=0,\\
 qy+r,&q\ge1.
 \end{cases}                                        \tag{1.2}
\]

Consequently

\[
 \sum_{m\ge0}K(V_m)=\mathcal L_2(y;r)+K(x)-K(r).    \tag{1.3}
\]

If `y>=A`, this sum is strictly positive.  Thus the only unresolved part
of this regime has

\[
 A/2\le y<A.                                        \tag{1.4}
\]

#### Proof

Maximality gives `T<=2y`, while (0.2) gives the reverse inequality.  It
also gives `2z<=3y`, so `r<=y/2`; the two inequalities involving `z` in
(0.2) give `r>=x`.

The size-four generator is exactly two size-two generators.  Pairs of
size-one generators are no better than one size-two generator, pairs of
size-three generators are no better than three size-two generators, and a
residual size-one plus size-three pair is no better than two size-two
generators.  The parity normal form is therefore (1.2).

If `y>=A`, cancellation in (1.3) gives

\[
 C(y)+K(x)-\sum_{q\ge1}e^{-(A+qy+r)^2}
 \ge\mathcal L_2(y;x)>0,                            \tag{1.5}
\]

because `r>=x` and the two-slot theorem applies to `(0,x,y)`.  Finally
`T=2y>=A` gives the lower endpoint in (1.4). \(\square\)

The interval (1.4) is a real scope boundary: deleting the dominated
size-four generator leaves a period `y` which need not itself reach `A`,
so the proved normalized three-slot theorem cannot simply be cited.

## 2. Three-slot-efficient regime

Assume now

\[
 {z\over3}\ge {y\over2},qquad
 {z\over3}\ge {T\over4}.                            \tag{2.1}
\]

Put

\[
 u=T-z,qquad
 w=\max\{y,2u\},qquad
 v=\max\{y,u+x\}.                                   \tag{2.2}
\]

Then

\[
 x\le u\le z/3,qquad
 y\le w\le2z/3,qquad v\le w,qquad u+y\le z.       \tag{2.3}
\]

### Theorem 2.1 (two-transient three-coset form)

The exact Bellman clock is

\[
\begin{array}{c|ccc}
q&V_{3q}&V_{3q+1}&V_{3q+2}\\ \hline
0&0&x&y\\
1&z&z+u&z+v\\
q\ge2&qz&qz+u&qz+w.
\end{array}                                         \tag{2.4}
\]

The eventual cosets are precisely the Bellman cosets of the effective
three-slot table

\[
 (0,u,w,z).                                         \tag{2.5}
\]

This table is internally superadditive:

\[
 w\ge2u,qquad z\ge u+w.                            \tag{2.6}
\]

#### Proof

From (2.1), `4z>=3T`, hence `z>=3u`.  Also `2z>=3y`.
Together with (0.2), these give (2.3).  If `w=y`, then
`u+w<=z` by `u<=z/3` and `y<=2z/3`; if `w=2u`, then
`u+w=3u<=z`.  This proves (2.6).

We verify (2.4) in the recurrence (0.3).  The inequalities used in the
three residue rows are

\[
 x+y\le z,quad u+y\le z,quad w+x\le z,quad
 w+u\le z,quad 2y\le z+u,quad v+y\le z+u.         \tag{2.7}
\]

They follow from (0.2)--(2.3), considering separately
`w=y,2u` and `v=y,u+x`.  Substitution gives successively

\[
 V_{3q}=qz,qquad V_{3q+1}=qz+u (q\ge1),
\]

and

\[
 V_2=y,qquad V_5=z+v,qquad
 V_{3q+2}=qz+w (q\ge2).
\]

Every displayed lower bound is attained by the corresponding combination
of size-three and size-four generators, so the inequalities are equalities.
The effective table (2.5) has `2w<=z+u` in both cases
(`2y<=T` or `4u<=z+u`), so its own three-slot normal form has residues
`0,u,w`, proving the last assertion. \(\square\)

The exact comparison with the effective clock is

\[
\begin{aligned}
 \sum_mK(V_m)-\sum_mK(V_m^{\rm eff})
 ={}&K(x)-K(u)+K(y)-K(w)\\
    &+K(z+v)-K(z+w).                                \tag{2.8}
\end{aligned}
\]

This is the first genuinely new four-slot transient.  The first two
differences move values to the left but have no global sign because `K` is
not monotone on the whole compact range.  The last difference is
nonpositive: `z+v>=T>=A`, `v<=w`, and `K` increases on the tail.  Thus the
correction cannot be discarded by a pointwise monotonicity argument.

There is a second scope obstruction: (2.1) and `T>=A` imply only

\[
 z\ge3A/4,                                           \tag{2.9}
\]

not `z>=A`.  Therefore even the effective table (2.5) need not lie in the
normalization range of the proved three-slot theorem.  Equations
(2.8)--(2.9) are the exact new gate in this regime.

## 3. Four-slot-efficient regime

Suppose

\[
 {T\over4}\ge {y\over2},qquad
 {T\over4}\ge {z\over3}.                            \tag{3.1}
\]

Put `alpha=T/4` and reduced weights

\[
 d_j=c_j-j\alpha\le0qquad(1\le j\le3).             \tag{3.2}
\]

For `r in Z/4Z`, let `beta_r` be the maximum reduced weight of a walk from
zero to `r` using steps `1,2,3`, with step `j` carrying weight `d_j`.

### Theorem 3.1 (finite Apery reduction)

Each `beta_r` is attained by a simple walk with at most three steps.  For
all sufficiently large `q`,

\[
 V_{4q+r}=qT+r\alpha+\beta_r.                       \tag{3.3}
\]

More explicitly, (3.3) holds once `4q+r` is at least the total ordinary
capacity of a maximizing simple walk; this capacity is at most nine.
Thus the whole tail is four shifted arithmetic Gaussian lattices, and all
nonperiodicity is confined to capacities below nine.

#### Proof

Every closed walk has total ordinary capacity divisible by four.  By
(3.2), its reduced weight is nonpositive.  Removing a repeated-vertex
closed segment therefore does not decrease the reduced weight.  A
maximizer may consequently be chosen simple, and a simple walk on four
vertices has at most three edges and ordinary capacity at most nine.

For a capacity `m=4q+r`, every exact-fill configuration has value

\[
 \alpha m+\hbox{(reduced walk weight)}.
\]

Unused integer capacity can be filled by size-one generators without
decreasing value, so exact fill is harmless.  A maximizing simple walk can
be padded by size-four generators, whose reduced weight is zero, whenever
`m` is at least its ordinary capacity.  This proves (3.3). \(\square\)

## 4. Exact four-slot frontier

Every four-slot table is now in one of three proof-safe forms:

1. a two-coset clock, with only the compact range (1.4) unresolved;
2. a three-coset clock with exactly the three transient differences (2.8)
   and possible subcritical effective endpoint (2.9);
3. a genuine four-coset clock with a finite Apery prefix of capacity below
   nine.

No arbitrary infinite Bellman recursion remains at `n=4`.  What is new
relative to `n<=3` is not another residue relaxation: it is the signed
finite transient (2.8) and the four-state reduced walk in Theorem 3.1.
This note does not prove four-slot positivity, the all-clock inequality, or
`nu(k)<=B(k)+O(1)`.
