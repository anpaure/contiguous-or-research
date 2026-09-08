# Carry-aware superadditive clocks and the exact knapsack obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  This note repairs the
loss of carry information in the one-period residue relaxation.  It does not
prove the final Gaussian inequality.

Put

\[
 A={\sqrt\pi\over2}
\]

and

\[
 K(x)=
 \begin{cases}
 1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
 -e^{-(A+x)^2},&x>A,
 \end{cases}
 \qquad K(\infty)=0.                                  \tag{0.1}
\]

The unresolved smooth configuration inequality is

\[
 \int_0^\infty K(a(t))\,dt\ge0                       \tag{0.2}
\]

for every nondecreasing superadditive clock `a`.  The earlier residue
envelope retained only the partition `t=q+r`, and therefore discarded
alternative partitions which cross the period boundary.  The construction
below retains every such carry exactly.

## 1. The least extension of one compact profile

Let `b:[0,1]->[0,infinity]` be nondecreasing, with `b(0)=0`, and internally
superadditive:

\[
 b(x+y)\ge b(x)+b(y)\qquad(x,y\ge0, x+y\le1).       \tag{1.1}
\]

Define its unbounded-knapsack closure by

\[
 (\mathsf Sb)(t)=
 \sup\left\{
       \sum_{i=1}^m b(r_i):
       m\ge0,\ 0\le r_i\le1,\ \sum_i r_i\le t
      \right\}.                                      \tag{1.2}
\]

The empty sum is zero.  Infinite values are allowed.

### Theorem 1.1 (least superadditive extension)

The function `mathsf S b` is nondecreasing and superadditive on
`[0,infinity)`, and

\[
 (\mathsf Sb)(t)=b(t)\qquad(0\le t\le1).             \tag{1.3}
\]

If `a` is any nondecreasing superadditive clock whose restriction to
`[0,1]` is `b`, then

\[
 \boxed{a(t)\ge(\mathsf Sb)(t)\quad(t\ge0).}          \tag{1.4}
\]

Thus `mathsf S b` is the pointwise least global clock extending `b`.

#### Proof

Concatenating two feasible lists in (1.2) proves superadditivity.  Increasing
the available capacity proves monotonicity.  If `t<=1`, repeated use of
(1.1) shows that every feasible list has value at most
`b(sum_i r_i)<=b(t)`, while the singleton list `(t)` attains `b(t)`.  This
proves (1.3).

For any feasible list, superadditivity of `a` gives

\[
 a(t)\ge a\!\left(\sum_i r_i\right)
       \ge\sum_i a(r_i)=\sum_i b(r_i).
\]

Taking the supremum proves (1.4). \(\square\)

The closure obeys the exact max-plus Bellman equation

\[
 (\mathsf Sb)(t)=
 \sup_{0\le r\le\min(1,t)}
       \bigl(b(r)+(\mathsf Sb)(t-r)\bigr),            \tag{1.5}
\]

with the usual harmless convention at `r=0`.  Equation (1.5), rather than
the single choice `r=t-floor(t)`, is the missing carry recurrence.

## 2. Exact compact variational reduction

Assume now that

\[
 T:=b(1)\ge A.                                       \tag{2.1}
\]

Then `mathsf S b(t)>=floor(t)T`, so in particular
`mathsf S b(t)>=A` for `t>=1`.  On this range `K` is increasing.

### Theorem 2.1 (carry-aware compact reduction)

Among all nondecreasing superadditive clocks with fixed compact profile
`b`, the least possible Gaussian functional is attained by the knapsack
closure:

\[
 \boxed{
 \inf_{a|_{[0,1]}=b}
 \int_0^\infty K(a(t))\,dt
 =\mathcal J(b),
 }                                                     \tag{2.2}
\]

where

\[
 \mathcal J(b):=
 \int_0^1K(b(t))\,dt+
 \int_1^\infty K((\mathsf Sb)(t))\,dt.               \tag{2.3}
\]

Consequently, (0.2) is equivalent to

\[
 \boxed{\mathcal J(b)\ge0}                           \tag{2.4}
\]

for every compact profile satisfying (1.1) and (2.1).

#### Proof

Theorem 1.1 gives `a>=mathsf S b`.  Both sides are at least `A` after time
one, and `K` is increasing on `[A,infinity]`.  Therefore

\[
 \int_1^\infty K(a(t))\,dt
 \ge\int_1^\infty K((\mathsf Sb)(t))\,dt.
\]

The first-period integrals agree.  The clock `mathsf S b` itself is
admissible and attains equality, proving (2.2).

For an arbitrary nonzero finite-valued clock, choose `h>0` with
`a(h)>=A` and rescale time by `h`; the functional is multiplied by the
positive factor `h`.  A finite-valued clock which never reaches `A` is
identically zero by superadditivity and has nonnegative (indeed infinite)
functional.

It remains to justify a clock which jumps to infinity at a finite time
`tau`.  If its finite values below `tau` are unbounded, choose `h<tau`
with `A<=a(h)<infinity` and apply the preceding argument; (1.4) and tail
monotonicity remain valid with the value infinity.  If those finite values
are bounded, rescale `tau=1`, keep the profile on `[0,1)`, and replace only
the endpoint value infinity by a finite `T` larger than both `A` and twice
the finite bound.  This preserves internal superadditivity.  The resulting
closures satisfy

\[
 (\mathsf Sb_T)(t)\ge\lfloor t\rfloor T\qquad(t\ge1),
\]

so their tail integrals tend to zero as `T` tends to infinity, by dominated
convergence.  Their first-period integrals equal the original compact
integral.  Hence (2.4) for finite endpoints passes to the blow-up clock.
No truncation of a superadditive clock is being used.  This proves the
equivalence. \(\square\)

### Corollary 2.2 (finite carry arity)

In (1.2) it is enough to use partitions for which

\[
 r_i+r_j>1\qquad(i\ne j).                             \tag{2.5}
\]

Every such partition of capacity `t` has at most

\[
 \lceil2t\rceil                                      \tag{2.6}
\]

parts.

#### Proof

If two parts have sum at most one, replace them by their sum.  Condition
(1.1) says that this does not lower the value.  Iteration gives (2.5).
At most one remaining part is at most `1/2`, so
`t>(m-1)/2` for a partition with `m` parts.  Hence
`m<2t+1`, which is equivalent to (2.6). \(\square\)

Thus the exact carry correction is finite on every bounded time interval;
it is not an infinite-part relaxation.

## 3. An explicit carry lower bound

For `t=q+r`, where `q>=1` is an integer and `0<=r<1`, (1.2) contains both
of the feasible partitions

\[
 \underbrace{1+\cdots+1}_{q\text{ times}}+r
 \quad\hbox{and}\quad
 \underbrace{{q+r\over q+1}+\cdots+{q+r\over q+1}}
             _{q+1\text{ times}}.
\]

Therefore

\[
 (\mathsf Sb)(q+r)\ge
 \max\left\{qT+b(r),
 (q+1)b\!\left({q+r\over q+1}\right)\right\}.        \tag{3.1}
\]

Since `K(x)=-exp(-(A+x)^2)` on the tail, every clock with first-period
profile `b` satisfies the fully explicit bound

\[
\begin{aligned}
 \int_0^\infty K(a(t))\,dt
 \ge{}&\int_0^1K(b(r))\,dr\\
 &-\sum_{q\ge1}\int_0^1
 \exp\!\left[-\left(A+
 \max\left\{qT+b(r),
 (q+1)b\!\left({q+r\over q+1}\right)\right\}
 \right)^2\right]dr .                                \tag{3.2}
\end{aligned}
\]

The second term in the maximum is supported on the terminal layer
`(q/(q+1),1)` of the compact profile.  It is exactly the first carry which
the old residue envelope omitted.  The full closure (1.2) retains all
higher carries.

## 4. Why the critical half-step is not a counterclock

The endpoint profile responsible for the negative pair relaxation would
place value zero on the first half-period and value `A` on the second.  A
genuine superadditive clock cannot simultaneously have period value `A`:
two second-half times add across the boundary and force a value at least
`2A`.

The least genuine profile is

\[
 b_\star(r)=
 \begin{cases}
 0,&0\le r<1/2,\\
 A,&1/2\le r<1,\\
 2A,&r=1.
 \end{cases}                                         \tag{4.1}
\]

It satisfies (1.1), and direct knapsack packing gives

\[
 (\mathsf Sb_\star)(t)=A\lfloor2t\rfloor             \tag{4.2}
\]

outside irrelevant endpoints.  Hence

\[
 \mathcal J(b_\star)
 ={1\over2}\sum_{m\ge0}K(mA)>0.                     \tag{4.3}
\]

The strict sign is precisely the already-proved all-ceiling inequality at
step `A`.  Thus the negative number
`G_A(0)+G_A(A)` is an artifact of deleting the carry; its arithmetically
closed clock passes strictly.

## 5. Exact finite Bellman obstruction

The compact reduction can be discretized without losing a possible
counterexample.

For a compact profile `b` and an integer `n>=1`, put

\[
 b_n(r)=b\!\left({\lfloor nr\rfloor\over n}\right)
 \quad(0\le r<1),
 \qquad b_n(1)=b(1).                                  \tag{5.1}
\]

Then `b_n` is nondecreasing, internally superadditive, and `b_n<=b`.
Let

\[
 c_j=b(j/n)\qquad(0\le j\le n).                      \tag{5.2}
\]

The table is nondecreasing and satisfies

\[
 c_0=0,qquad c_{i+j}\ge c_i+c_j
 \quad(i+j\le n),qquad c_n\ge A.                    \tag{5.3}
\]

Define its unbounded integer-knapsack value by

\[
 V_0=0,
 \qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j})
 \quad(m\ge1).                                       \tag{5.4}
\]

For `m<=n`, (5.3) gives `V_m=c_m`.  For all `m`,

\[
 (\mathsf Sb_n)(t)=V_{\lfloor nt\rfloor}             \tag{5.5}
\]

away from grid endpoints, and therefore

\[
 \boxed{
 \mathcal J(b_n)={1\over n}\sum_{m\ge0}K(V_m).
 }                                                     \tag{5.6}
\]

### Theorem 5.1 (finite carry equivalence)

The universal clock inequality (0.2) holds if and only if

\[
 \boxed{
 \sum_{m\ge0}K(V_m)\ge0                              \tag{5.7}
 }

for every integer `n>=1` and every real table satisfying (5.3), with
`V` given by the exact carry recurrence (5.4).

In particular, if a genuine counterclock exists, then a finite
superadditive table with a negative Bellman sum exists.

#### Proof

One direction is immediate from the step profile `b_n` and (5.6).

Conversely, suppose every finite Bellman sum is nonnegative and fix `b`.
At every continuity point of the monotone function `b`,
`b_n(r)->b(r)`.  Hence continuity and boundedness of `K` on `[0,b(1)]`
give

\[
 \int_0^1K(b_n(r))\,dr
 \longrightarrow\int_0^1K(b(r))\,dr.                \tag{5.8}
\]

Because `b_n<=b`, Theorem 1.1 gives
`mathsf S b_n<=mathsf S b`.  Both closures are at least `A` after time
one, so monotonicity of `K` on the tail yields

\[
 \int_1^\infty K((\mathsf Sb_n)(t))\,dt
 \le
 \int_1^\infty K((\mathsf Sb)(t))\,dt.               \tag{5.9}
\]

The Gaussian tails are integrable uniformly because
`mathsf S b_n(t)>=floor(t)b(1)`.  Combining (5.8)--(5.9),

\[
 \limsup_{n\to\infty}\mathcal J(b_n)\le\mathcal J(b).
                                                               \tag{5.10}
\]

Every term on the left is nonnegative by (5.6)--(5.7), so
`mathcal J(b)>=0`.  Theorem 2.1 finishes the proof. \(\square\)

To verify (5.5), observe that a part in the `j`-th grid cell has value
`c_j` and consumes at least `j/n` units of capacity.  Conversely that
minimum consumption is attained at the left endpoint.  Thus a list fits
before time `t` exactly when its integer weights have sum at most
`floor(nt)`, which is the recurrence (5.4).

## 6. Denomination insertion is not monotone

One tempting induction would start with an arithmetic clock and insert
denominations one at a time, hoping that the Bellman sum never decreases.
That is false even at the smallest nontrivial table.

Write

\[
 C(a):=\sum_{m\ge0}K(ma).                            \tag{6.1}
\]

For the table

\[
 n=2,\qquad(c_0,c_1,c_2)=(0,0,A),                   \tag{6.2}
\]

the recurrence gives `V_m=A floor(m/2)` and Bellman sum `2C(A)`.  Insert
the undominated generator `c_1=A/2`.  Then

\[
 V_m={mA\over2}
\]

and the new sum is `C(A/2)`.  The exact ceiling formula gives

\[
 \boxed{
 C(A/2)-2C(A)
 =e^{-\pi/4}-{1\over2}
  +4\sum_{q\ge1}\left(e^{-4\pi q^2}-e^{-16\pi q^2}\right)<0.
 }                                                     \tag{6.3}
\]

Both `C(A/2)` and `C(A)` are strictly positive; only insertion
monotonicity fails.

For completeness, the strict sign can be checked without decimals.  The
proved bound `1-2e^{-pi/4}>3/35` gives

\[
 {1\over2}-e^{-\pi/4}>{3\over70}.                    \tag{6.4}
\]

Also `pi>3`, the degree-four exponential bound `e^12>1237`, and
`e^{12pi}>37` give

\[
 4\sum_{q\ge1}e^{-4\pi q^2}
 <{4\over1237(1-1/37)}<{3\over70}.                  \tag{6.5}
\]

Equations (6.4)--(6.5) prove (6.3).

There is one exact harmless insertion class.  If a new generator `(j,c)`
satisfies

\[
 c\le V_j                                             \tag{6.6}
\]

for the old Bellman clock, then it changes no `V_m`: replace each use of
the new generator by an old configuration of capacity at most `j` and
value at least `c`.  Thus dominated denominations are inert.  The example
(6.2)--(6.3) shows that every useful induction must control the global
rearrangement caused by an **undominated** insertion; its net Gaussian
effect need not have one sign.

## 7. Every two-slot Bellman table passes

The smallest mixed table can be closed completely.

### Theorem 7.1 (two-slot positivity)

Let

\[
 n=2,
 \qquad(c_0,c_1,c_2)=(0,y,T),
 \qquad 0\le y\le {T\over2},
 \qquad T\ge A.                                      \tag{7.1}
\]

Then its Bellman clock is

\[
 V_{2q}=qT,
 \qquad V_{2q+1}=qT+y,                               \tag{7.2}
\]

and

\[
 \boxed{
 \sum_{m\ge0}K(V_m)>0.
 }                                                     \tag{7.3}
\]

#### Proof

The recurrence (5.4) and `T>=2y` give (7.2).  Put

\[
 C(T)=\sum_{q\ge0}K(qT),
 \qquad
 F_T(y)=\sum_{q\ge0}K(qT+y).                         \tag{7.4}
\]

The desired sum is `C(T)+F_T(y)`.  For fixed `y` it is nondecreasing in
`T` on the admissible range: the `q=0` terms are fixed, and every `q>=1`
argument lies in `[A,infinity)`, where `K` is increasing.

If `y>=A/2`, the least admissible period is `T=2y`.  At that period the two
residue classes interlace to form the complete arithmetic clock:

\[
 C(2y)+F_{2y}(y)=\sum_{m\ge0}K(my)=C(y)>0,            \tag{7.5}
\]

by the all-ceiling theorem.

It remains to take `0<=y<=A/2`.  Monotonicity in `T` reduces this case to
`T=A`.  On this interval,

\[
 F_A(y)=1-e^{-(A-y)^2}
        -\sum_{q\ge0}e^{-(A+y+qA)^2}.                \tag{7.6}
\]

Let

\[
 \phi(z)=ze^{-z^2},
 \qquad
 \lambda(z)={\phi'(z)\over\phi(z)}={1\over z}-2z.
\]

The function `lambda` is strictly decreasing.  At an interior critical
point of `F_A`, with

\[
 w=A-y,
 \qquad z_q=A+y+qA,
\]

differentiating (7.6) gives

\[
 \sum_{q\ge0}\phi(z_q)=\phi(w).                      \tag{7.7}
\]

Using `z_q>=z_0` and the decrease of `lambda`, a second differentiation
gives

\[
\begin{aligned}
 {1\over2}F_A''(y)
 &=\sum_{q\ge0}\phi'(z_q)+\phi'(w)\\
 &\le\bigl(\lambda(A+y)+\lambda(A-y)\bigr)\phi(w)\\
 &=2A\left({1\over A^2-y^2}-2\right)\phi(w)<0.       \tag{7.8}
\end{aligned}
\]

The last inequality uses

\[
 A^2-y^2\ge{3A^2\over4}={3\pi\over16}>{1\over2}.
\]

Thus every interior critical point of `F_A` is a strict local maximum.
Its minimum on `[0,A/2]` is attained at an endpoint.  At those endpoints,

\[
 C(A)+F_A(0)=2C(A)>0,
 \qquad
 C(A)+F_A(A/2)=C(A/2)>0,                             \tag{7.9}
\]

again by the all-ceiling theorem.  This proves (7.3). \(\square\)

Consequently a finite Bellman counterexample, if one exists, must have
grid size at least three.  The theorem does not say that a clock generated
by two denominations at an arbitrary larger grid has been settled.

## 8. What remains

The failed residue-pair relaxation has been removed.  The complete
continuum price question is now the exact finite statement (5.7):

> every nondecreasing internally superadditive denomination table has a
> nonnegative Gaussian cost along its unbounded-knapsack Bellman clock.

No independent residue choice remains, and every quotient carry is priced
by (5.4).  Ceiling clocks are the one-denomination subfamily and pass
strictly.  Mixed-denomination tables are the only possible obstruction.

This note does not prove (5.7), does not construct the Rayleigh coagulation
kernel, and does not imply `nu(k)<=B(k)+O(1)`.  It gives an exact
carry-faithful finite target for the remaining smooth configuration gate.
