# Mathematical attack F: the dominant-ray construction is obstructed

## Executive conclusion

The proposed dominant three-box ray theorem (DRAY) is false, throughout its
stated range.

Let

\[
0<a<b,\qquad c>2b
\]

be fixed integers. Then

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0.
}
\tag{1}
\]

Thus no shell braid, corridor fusion, recursive face splice, or other literal
range-maximum construction can have length

\[
(at+1)(bt+1)+o(t^2)
\]

in this parameter range. In particular, the primitive ray

\[
(a,b,c)=(1,2,5)
\]

already satisfies

\[
g_3(t,2t,5t)
\ge
(t+1)(2t+1)+\left(\frac1{10}-o(1)\right)t^2.
\tag{2}
\]

This disproves the proposed sufficient DRAY lemma, not the global
contiguous-OR width conjecture. Other sufficient routes remain logically
available.

---

## 1. Definitions and the quantitative obstruction

Write

\[
P(p,q,r)=[0,p]\times[0,q]\times[0,r].
\]

A range-maximum word is a word

\[
A_1,A_2,\ldots,A_N\in P(p,q,r)
\]

such that every nonzero point of the box is the coordinatewise maximum of
some contiguous factor. Let $g_3(p,q,r)$ be the least possible $N$.

Assume

\[
0<p<q,\qquad r>p+q,
\]

and put

\[
M=(p+1)(q+1),\qquad
h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,
\qquad
\varepsilon=p+q+r-2h\in\{0,1\}.
\tag{3}
\]

Also put

\[
s_0=p+q+2,
\qquad
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor.
\tag{4}
\]

For $K\ge2$, define

\[
B=s_0+
\left\lceil\frac{M-Ks_0}{K}\right\rceil.
\tag{5}
\]

### Theorem 1 (finite quantitative DRAY obstruction)

Every range-maximum word for $P(p,q,r)$, with $D=N-M$, satisfies

\[
\boxed{
D\ge
\frac{M\bigl((r-\varepsilon)/2-q\bigr)-1}
     {h-1+2B}
}
\tag{6}
\]

whenever the numerator is positive.

The rest of the report proves (6), including the literal contiguous-factor
and multiple-pin checks.

---

## 2. The full rectangular middle layer

Because $r>p+q$, the rank-$h$ layer is

\[
\mathcal S_h=
\{(x,y,h-x-y):0\le x\le p,\ 0\le y\le q\}.
\tag{7}
\]

Indeed, (3) gives

\[
p+q\le h\le r,
\]

so $0\le h-x-y\le r$ for every pair $(x,y)$. Consequently

\[
|\mathcal S_h|=M.
\tag{8}
\]

This is also the exact width. The layer (7) is an antichain, so the width is
at least $M$. Conversely, two box points with the same first two
coordinates are comparable, so projection onto $(x,y)$ is injective on
every antichain. Hence every antichain has size at most $M$.

In a range-maximum word, witnesses for an antichain have distinct left
endpoints: two witnesses with the same start are nested and therefore have
comparable maxima. Hence every such word has $N\ge M$, so $D=N-M\ge0$.

The exact number of nonzero targets below rank $h$ is

\[
\begin{aligned}
L_{<h}
&=\sum_{x=0}^{p}\sum_{y=0}^{q}(h-x-y)-1\\
&=M\left(h-\frac{p+q}{2}\right)-1\\
&=M\frac{r-\varepsilon}{2}-1.
\end{aligned}
\tag{9}
\]

The first equality is valid because $h\le r$ and $h\ge p+q$: for a fixed
$(x,y)$, precisely

\[
z=0,1,\ldots,h-x-y-1
\]

give points of rank below $h$. The final subtraction removes the zero
target.

---

## 3. Ordered witnesses and the rank-capped start bound

Choose one factor

\[
I_i=[\ell_i,r_i]
\]

representing each of the $M$ targets in $\mathcal S_h$. Order these
factors by increasing left endpoint.

The left endpoints are distinct. Otherwise two factors with the same start
would be nested, and their maxima would be comparable. Distinct points of
the same rank cannot be comparable. The same containment argument shows
that, after the factors are ordered by their starts, their right endpoints
are strictly increasing as well.

Since $N=M+D$, there are nondecreasing integer sequences

\[
0\le\alpha_1\le\cdots\le\alpha_M\le D,
\qquad
0\le\beta_1\le\cdots\le\beta_M\le D
\tag{10}
\]

such that

\[
\ell_i=i+\alpha_i,
\qquad
r_i=i+\beta_i.
\tag{11}
\]

Put

\[
d_i=r_i-\ell_i=\beta_i-\alpha_i.
\tag{12}
\]

### Lemma 2 (rank-capped starts)

\[
\boxed{
L_{<h}\le\sum_{i=1}^{M}d_i+(h-1)D.
}
\tag{13}
\]

#### Proof

Choose one witness for every nonzero target below rank $h$, and group
these witnesses by their left endpoints.

At a selected start \(\ell_i\), a below-rank witness must end before
\(r_i\). If it ended at or after \(r_i\), it would contain \(I_i\), so its
maximum would dominate the rank-$h$ target represented by $I_i$. There
are at most $d_i$ possible earlier endpoints.

There are exactly $D$ starts that are not among the selected
$\ell_i$'s. At any fixed start, maxima obtained by moving the right
endpoint form a chain. A strict chain of nonzero points below rank $h$
contains at most one point of each rank $1,\ldots,h-1$, hence at most
$h-1$ points. Summing the two contributions proves (13). $\square$

---

## 4. A forced short internal run in every middle block

For a nonnegative integer sequence $u_1,\ldots,u_m$, an internal positive threshold
run is an interval \([s,t]\) with

\[
1<s\le t<m
\]

and some integer threshold $k\ge1$ such that

\[
u_i\ge k\quad(s\le i\le t),
\qquad
u_{s-1}<k,
\qquad
u_{t+1}<k.
\tag{14}
\]

Its edge length is $t-s$, one less than its number of indices.

### Lemma 3 (valley characterization)

If a scalar sequence has no internal positive threshold run, then it is
valley-shaped: for some $\tau$,

\[
u_1\ge\cdots\ge u_\tau
\le\cdots\le u_m.
\tag{15}
\]

#### Proof

Choose an index $\tau$ attaining the global minimum. If the prefix through
$\tau$ is not nonincreasing, there are $i<j<\tau$ with $u_i<u_j$. Since
$u_\tau\le u_i$, this gives

\[
u_j>\max(u_i,u_\tau).
\]

If the suffix from $\tau$ is not nondecreasing, there are
$\tau<j<k$ with $u_j>u_k$, and then

\[
u_j>\max(u_\tau,u_k).
\]

In either case, at the positive integer threshold $u_j$, the positive
component containing $j$ is separated from both ends by lower entries and
is therefore an internal positive run. If neither case occurs, the
sequence has the form (15). $\square$

### Lemma 4 (constant-sum valley bound)

Let

\[
T_i=(x_i,y_i,z_i)\in\mathcal S_h,
\qquad 1\le i\le m,
\]

be distinct. If each of the three coordinate sequences is valley-shaped,
then

\[
m\le p+q+1.
\tag{16}
\]

#### Proof

Choose valley turns for the three coordinates and relabel the coordinates
as $X,Y,Z$ so their turn positions satisfy

\[
\tau_X\le\tau_Y\le\tau_Z.
\]

Before $\tau_X$, all three coordinates are nonincreasing. Since their sum
is always $h$, any such adjacent transition would keep all three
coordinates fixed, contradicting distinctness. Hence $\tau_X=1$.
Similarly, after $\tau_Z$ all coordinates are nondecreasing, so
$\tau_Z=m$.

Between $\tau_X$ and $\tau_Y$, the coordinate $X$ is nondecreasing
while $Y,Z$ are nonincreasing. At every adjacent transition, $X$ must
increase strictly; otherwise constant sum would again force equality of
the two points. Therefore

\[
\tau_Y-\tau_X
\le X_{\tau_Y}-X_{\tau_X}.
\tag{17}
\]

Likewise, between $\tau_Y$ and $\tau_Z$, $Z$ must decrease strictly,
so

\[
\tau_Z-\tau_Y
\le Z_{\tau_Y}-Z_{\tau_Z}.
\tag{18}
\]

Adding (17) and (18), and using
$X_{\tau_Y}+Y_{\tau_Y}+Z_{\tau_Y}=h$,
gives

\[
\begin{aligned}
m-1
&\le X_{\tau_Y}-X_{\tau_X}
   +Z_{\tau_Y}-Z_{\tau_Z}\\
&=h-Y_{\tau_Y}-X_{\tau_X}-Z_{\tau_Z}.
\end{aligned}
\tag{19}
\]

The coordinatewise lower bounds on \(\mathcal S_h\) are

\[
x\ge0,qquad y\ge0,qquad z\ge h-p-q.
\]

Their sum is $h-p-q$, independently of the relabeling. Thus the last
quantity in (19) is at most $p+q$, proving (16). $\square$

### Lemma 5 (short-run mesh lemma)

Every ordering of $p+q+2$ distinct points of $\mathcal S_h$ contains an
internal coordinate-threshold positive run \([u,v]\) satisfying

\[
v-u\le q.
\tag{20}
\]

#### Proof

By Lemmas 3 and 4, some coordinate sequence has an internal positive run.
Start with any such run, let $m_0$ be the largest coordinate value attained
on it, and take the maximal consecutive plateau on which the coordinate is
equal to $m_0$ and which contains one of its occurrences inside the original
run.

Both neighbors of this plateau have coordinate less than $m_0$. For a
neighbor inside the original run this follows from maximality of the
plateau; for a neighbor just outside the original run it follows because
that neighbor is below the original threshold, which is at most $m_0$.
The plateau is therefore itself an internal positive run at threshold
$m_0$.

A fixed $x$-level in $\mathcal S_h$ contains $q+1$ points. A fixed
$y$-level contains $p+1$ points. A fixed $z$-level is given by one
equation $x+y=h-z$, and hence contains at most $p+1$ points. Since
$p<q$, every coordinate level contains at most $q+1$ middle targets.
Thus the plateau has at most $q+1$ indices, which is precisely (20).
$\square$

The coefficient $q$ in (20) is locally sharp. On the constant-sum
surface, order

\[
(0,q),(1,q),\ldots,(p,q),
(p,q-1),\ldots,(p,0),(0,0),
\tag{21}
\]

with the third coordinate always $h-x-y$. The $y$-sequence is
nonincreasing and the $z$-sequence is valley-shaped. The shortest internal
positive run in the $x$-sequence is the top plateau $x=p$, which has
edge length $q$.

---

## 5. Literal multipin-safe corridor inequality

Fix a coordinate threshold $k$. Its incidence word on the ordered middle
targets is

\[
b_i=\mathbf 1\{T_i^{(j)}\ge k\}.
\]

Let $[u,v]$ be an internal positive run, so $b_{u-1}=b_{v+1}=0$.

### Lemma 6 (literal pin gap)

\[
\boxed{
r_{u-1}+2\le\ell_{v+1},
\qquad
\beta_{u-1}-\alpha_{v+1}\le v-u.
}
\tag{22}
\]

#### Proof

Because $b_u=1$ and $I_u$ has maximum $T_u$, there is a physical word
position $s\in I_u$ whose $j$-th coordinate is at least $k$.

The negative witness $I_{u-1}$ contains no such position. Since
$s\ge\ell_u>\ell_{u-1}$, it follows that

\[
s>r_{u-1}.
\]

Likewise, $I_{v+1}$ contains no such position. Since

\[
s\le r_u<r_{v+1},
\]

we must have $s<\ell_{v+1}$. All endpoints are integral, so

\[
r_{u-1}+1\le s\le\ell_{v+1}-1,
\]

which gives the first inequality in (22). Substitution from (11) gives the
second.

Only one occurrence in $I_u$ was used. The threshold may occur at
arbitrarily many physical positions, and different positive witnesses may
use different pins. No common-pin or run-factorability hypothesis is being
assumed. $\square$

If the run in Lemma 6 also satisfies $v-u\le q$, monotonicity of
$\alpha_i,\beta_i$ gives the two one-sided estimates

\[
d_i\le q+\alpha_{v+1}-\alpha_i
\qquad(i<u),
\tag{23}
\]

and

\[
d_i\le q+\beta_i-\beta_{u-1}
\qquad(i>v).
\tag{24}
\]

For example, if $i<u$, then

\[
d_i=\beta_i-\alpha_i
\le\beta_{u-1}-\alpha_i
\le q+\alpha_{v+1}-\alpha_i.
\]

The proof of (24) is the symmetric insertion of
$\beta_{u-1}-\alpha_{v+1}\le q$.

---

## 6. Balanced block pairing and the global length bound

For $K$ as in (4), write

\[
R=M-Ks_0.
\]

Then $0\le R<2s_0$. Partition the ordered $M$ middle targets into $K$
consecutive blocks, distributing the $R$ excess indices as evenly as
possible. Every block has size between $s_0$ and $B$, with $B$ given
by (5). Pair consecutive blocks.

Apply Lemma 5 to the first $s_0$ points of each block, obtaining in every
block an internal run of edge length at most $q$. Its two negative
neighbors lie inside that $s_0$-point subblock, so it remains a genuinely
internal run in the entire middle order.

For each paired pair of blocks, assign every index of the first block to the
run in the second block, and every index of the second block to the run in
the first. Thus all first-block indices lie before their assigned run and
all second-block indices lie after their assigned run. Equations (23) and
(24) apply.

More explicitly, write one paired pair as

\[
C=[a,b],\qquad C'=[b+1,c].
\]

If $[u',v']$ is the run in $C'$, (23) gives

\[
\sum_{i\in C}d_i
\le q|C|+
\sum_{i\in C}(\alpha_{v'+1}-\alpha_i)
\le q|C|+B(\alpha_c-\alpha_a).
\tag{25a}
\]

If $[u,v]$ is the run in $C$, (24) gives

\[
\sum_{i\in C'}d_i
\le q|C'|+
\sum_{i\in C'}(\beta_i-\beta_{u-1})
\le q|C'|+B(\beta_c-\beta_a).
\tag{25b}
\]

The index spans belonging to different block pairs are disjoint. Hence

\[
\sum_{\text{pairs}}(\alpha_c-\alpha_a)\le D,
\qquad
\sum_{\text{pairs}}(\beta_c-\beta_a)\le D.
\]

Summing (25a) and (25b) over all pairs proves

\[
\boxed{
\sum_{i=1}^{M}d_i\le qM+2BD.
}
\tag{25}
\]

This is an order-independent bound. It uses only literal positive
coordinate occurrences in the original word.

---

## 7. Proof of Theorem 1

Combine the exact lower-rank count (9), the rank-capped start inequality
(13), and the corridor bound (25):

\[
M\frac{r-\varepsilon}{2}-1
\le qM+(h-1+2B)D.
\]

Rearranging gives (6). \(\square\)

---

## 8. Ray asymptotics and disproof of DRAY

Now set

\[
p=at,\qquad q=bt,\qquad r=ct.
\]

Because $c>2b>a+b$, all hypotheses above hold. Moreover,

\[
\frac{M}{t^2}\to ab,
\qquad
\frac{h}{t}\to\frac{a+b+c}{2},
\qquad
\frac{B}{t}\to a+b.
\tag{26}
\]

For the last limit, note that

\[
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor
\]

is of order $t$, whereas $0\le M-Ks_0<2s_0=O(t)$. Hence the ceiling
term in (5) is $O_{a,b}(1)$.

Divide (6) by $t^2$. Its numerator divided by $t^3$ tends to

\[
ab\left(\frac c2-b\right),
\]

and its denominator divided by $t$ tends to

\[
\frac{a+b+c}{2}+2(a+b)
=\frac{c+5a+5b}{2}.
\]

Therefore

\[
\liminf_{t\to\infty}\frac{D}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0,
\]

which is (1). Primitivity plays no role in this lower bound; the primitive
example (2) is included only to meet the strongest version of the proposed
ray statement.

---

## 9. Adversarial audit

The main step was independently attacked from three directions. The checks
below all passed.

1. **Repeated physical occurrences.** Lemma 6 uses one occurrence from one
   positive witness. It neither assumes nor concludes that an entire run
   has a common pin.

2. **Plateau extraction.** Even if larger values occur elsewhere in the
   coordinate sequence, the two lower immediate neighbors isolate the
   selected maximum plateau. It is therefore a maximal internal positive
   run at its own exact threshold.

3. **Block boundaries.** The run and both negative neighbors are found
   inside an $s_0$-point subblock. They remain internal after the subblock
   is placed in the full middle order.

4. **Endpoint direction.** A pin from $I_u$ lies to the right of
   $r_{u-1}$ and to the left of $\ell_{v+1}$. This gives
   $\beta_{u-1}-\alpha_{v+1}\le v-u$, the direction needed in (23) and
   (24).

5. **Congestion.** Cross-assigning paired blocks avoids the two-sided
   inside-run estimate. An $\alpha$-increment or $\beta$-increment is
   charged at most $B$ times in its pair, and pair spans are disjoint.

6. **Parity and zero.** The parity term
   $\varepsilon=p+q+r-2h$ is retained exactly in (9). The sole excluded
   below-rank target is the zero point.

7. **Width.** The lower bound is measured from the exact width $M$, not
   from an approximation.

8. **Scope.** The argument refutes DRAY, a sufficient local theorem. It
   does not refute the Boolean contiguous-OR width conjecture itself.

No finite search, computational search, probabilistic experiment, or web
search was used.

---

## Final status

The assigned construction route is genuinely exhausted for the stated
target: the target inequality is impossible. The smallest rigorous
replacement is the finite lower bound (6), and its fixed-ray consequence
(1) gives a positive quadratic excess for every $0<a<b$, $c>2b$.
