# Growing-depth common-top promotion fibres

Date: 2026-07-25

> **Calibration update.** The primary one-packet-per-top route now uses the
> least \(H\) with \(\lambda_H\ge m+H\), so that
> \((m+H)N_H=W-o(W)\). Its exact packet hypergraph and augmented near-factor
> gate are in
> `MATH_ATTACK_CALIBRATED_TOP_PACKET_HYPERGRAPH_20260725.md`. The
> opposite-side calibration below remains a valid overcomplete variant but
> is no longer the primary construction.

Pure mathematics only. No search, computation, solver, or generic
probabilistic rounding theorem is used.

## 0. Verdict

Put

\[
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
\lambda_q=\frac{W}{N_q}.
\]

Choose \(H\) to be the largest integer for which

\[
\lambda_H\le m+H.
\tag{0.1}
\]

Then

\[
H=(1+o(1))\sqrt{m\log m},\qquad
N_H=(1+o(1))\frac Wm.
\tag{0.2}
\]

Consequently

\[
N_H=o(W/H),\qquad HN_H=o(W),
\tag{0.3}
\]

and the two Boolean tails outside depths \(\pm H\) contain only

\[
O(W/H)=o(W)
\tag{0.4}
\]

masks. Thus one independently initialized promotion path for every
rank-\((m+H)\) top has negligible total reset cost.

Inside a fixed top \(U\), \(|U|=m+H\), every cyclic order of \(U\) gives an
exact promotion-only cycle of length \(m+H\). Its owners are the cyclic
\(m\)-intervals, its depth-\(q\) lower flags are cyclic
\((m-q)\)-intervals, and its upper flags are cyclic
\((m+q)\)-intervals. Hence the proposed local atom is valid at every depth.

Three further statements are proved here.

1. The inclusion graph admits an exact integral assignment of every middle
   owner \(X\) to a containing top \(U\), with every top receiving either
   \(\lfloor\lambda_H\rfloor\) or \(\lceil\lambda_H\rceil\) owners. Thus
   top capacity and all rounding are harmless.
2. Averaging common-top promotion cycles over all tops and cyclic orders
   gives an exact fractional owner partition. At every depth \(q\le H\),
   every lower and upper target has flag weight exactly \(W/N_q\ge1\).
3. Independent selection of one, or any fixed number, of cyclic orders per
   top leaves a positive fraction of the middle owners uncovered. For one
   order the expected uncovered fraction tends to \(e^{-1}\). Thus the
   fractional solution cannot be rounded top by top.

The exact integral top-fibre theorem is **not proved or refuted**. The
remaining obstruction is a cyclic-interval design with extremely thin
shallow-rank slack. At depth one, the \(W\) chosen lower flags may have only

\[
W-N_1=\frac{W}{m+1}
\tag{0.5}
\]

duplicate excess if they cover the whole rank; the same is true above the
middle. An arbitrary balanced owner-to-top assignment has no reason to
satisfy this near-injectivity or to be orderable by promotion.

The exact gate isolated in Section 7 is sufficient for a
\(W+o(W)\)-letter contiguous-OR word. It is strictly smaller than a global
SCD: it asks only for one useful state per middle owner, grouped into
\(O(N_H)\) common-top promotion paths, with coverage rather than exact
partition at the other central ranks.

## 1. The critical growing depth

The exact central ratio is

\[
\lambda_h
=\frac{\binom{2m}{m}}{\binom{2m}{m-h}}
=\prod_{i=0}^{h-1}\frac{m+i+1}{m-i}.
\tag{1.1}
\]

For \(h=o(m^{2/3})\), Taylor expansion with a uniform remainder gives

\[
\log\lambda_h
=\frac{h^2}{m}
+O\!\left(\frac hm+\frac{h^3}{m^2}\right).
\tag{1.2}
\]

Indeed, the linear contribution in the \(i\)-th factor is
\((2i+1)/m\), whose sum is \(h^2/m\), while the quadratic remainders sum
to \(O(h^3/m^2)\).

### Proposition 1.1 (exact threshold and slack)

Let \(H\) be defined by (0.1), and put

\[
M=m+H.
\tag{1.3}
\]

Then

\[
H=(1+o(1))\sqrt{m\log m},
\tag{1.4}
\]

and

\[
1\le\frac{M}{\lambda_H}
<\frac{M}{M+1}\frac{m+H+1}{m-H}
=1+O(H/m).
\tag{1.5}
\]

Consequently

\[
N_H=\frac{W}{\lambda_H}
=(1+O(H/m))\frac WM,
\tag{1.6}
\]

and the total number of slots in one full length-\(M\) promotion cycle per
top exceeds \(W\) by only

\[
MN_H-W=O(WH/m)=o(W).
\tag{1.7}
\]

#### Proof

For every fixed \(\varepsilon>0\), substitute

\[
h_\pm=(1\pm\varepsilon)\sqrt{m\log m}
\]

in (1.2). Then

\[
\log\lambda_{h_\pm}
=(1\pm\varepsilon)^2\log m+o(1),
\]

whereas \(\log(m+h_\pm)=\log m+o(1)\). Thus the last crossing in
(0.1) lies between \(h_-\) and \(h_+\), proving (1.4).

Maximality gives \(\lambda_H\le M\) and

\[
\lambda_{H+1}
=\lambda_H\frac{m+H+1}{m-H}>M+1.
\]

Rearranging proves (1.5); (1.6)--(1.7) follow. \(\square\)

### Proposition 1.2 (reset and literal-tail ledger)

At the depth in Proposition 1.1,

\[
HN_H=O(WH/m)=o(W),
\tag{1.8}
\]

and

\[
2\sum_{q=H+1}^{m}N_q=O(W/H)=o(W).
\tag{1.9}
\]

#### Proof

Equation (1.8) follows from (1.6). Also

\[
\frac{N_{q+1}}{N_q}=\frac{m-q}{m+q+1}.
\tag{1.10}
\]

For \(q\ge H\), using \(1-x\le e^{-x}\),

\[
\frac{N_{q+1}}{N_q}
\le \exp(-H/m).
\]

Hence the tail is bounded by a geometric series:

\[
\sum_{q=H+1}^mN_q
\le \frac{N_H}{e^{H/m}-1}
=O\!\left(\frac mH N_H\right)
=O(W/H).
\]

Lower and upper tails have equal sizes, proving (1.9). \(\square\)

## 2. The exact common-top promotion cycle

Fix

\[
U=\{u_0,u_1,\ldots,u_{M-1}\}
\]

with cyclic indices modulo \(M=m+H\). Define

\[
X_t=\{u_t,u_{t+1},\ldots,u_{t+m-1}\}.
\tag{2.1}
\]

The transition \(X_t\to X_{t+1}\) deletes \(u_t\) and inserts
\(u_{t+m}=u_{t-H}\).

At \(X_t\), take the lower deletion and upper addition queues

\[
\alpha_t=(u_t,u_{t+1},\ldots,u_{t+H-1}),
\tag{2.2}
\]

\[
\beta_t=(u_{t-1},u_{t-2},\ldots,u_{t-H}).
\tag{2.3}
\]

Equivalently, the full useful state is

\[
\omega_t=
\left(
I(t+H,m-H);\
u_{t+H-1},\ldots,u_t,
u_{t-1},\ldots,u_{t-H};\
[2m]\setminus U
\right),
\tag{2.4}
\]

where \(I(a,r)\) denotes the cyclic interval of length \(r\) in \(U\)
starting at \(u_a\).

### Theorem 2.1 (promotion-cycle compiler)

The states

\[
\omega_0\to\omega_1\to\cdots\to\omega_{M-1}\to\omega_0
\tag{2.5}
\]

form a directed bridge-one cycle. Every arc is the last-position singleton
promotion. The middle owners \(X_t\) are distinct, and for every
\(0\le q\le H\),

\[
L_q(\omega_t)=I(t+q,m-q),
\tag{2.6}
\]

\[
U_q(\omega_t)=I(t-q,m+q).
\tag{2.7}
\]

In particular, the depth-\(H\) upper flag is always the common top \(U\).

#### Proof

In (2.4), choose

\[
x=u_{t+H},\qquad z_{2H}=u_{t-H}=u_{t+m}.
\]

The promotion rule moves \(z_{2H}\) into the lower block, moves \(x\)
to the first singleton position, and shifts every other singleton one
place. The result is exactly \(\omega_{t+1}\). The owners in (2.1) are
distinct because their complementary cyclic \(H\)-intervals are distinct.
Deleting the first \(q\) entries of (2.2) gives (2.6), while adjoining the
first \(q\) entries of (2.3) gives (2.7). \(\square\)

Every contiguous segment of (2.5) is therefore one legal promotion-only
path. This permits variable exact fibre loads without any divisibility
assumption on \(W\) or \(N_H\).

## 3. Exact owner-to-top load balancing

Let \(\mathcal X=\binom{[2m]}m\) and
\(\mathcal U=\binom{[2m]}{m+H}\). Join \(X\) to \(U\) when \(X\subset U\).
The left and right degrees are

\[
a=\binom mH,
\qquad
b=\binom{m+H}H,
\tag{3.1}
\]

and double counting gives

\[
Wa=N_Hb,
\qquad
\lambda_H=\frac ba.
\tag{3.2}
\]

### Theorem 3.1 (integral balanced top assignment)

There is a map

\[
\phi:\mathcal X\longrightarrow\mathcal U,
\qquad X\subset\phi(X),
\tag{3.3}
\]

such that every top receives either

\[
\lfloor\lambda_H\rfloor
\quad\text{or}\quad
\lceil\lambda_H\rceil
\tag{3.4}
\]

owners.

#### Proof

Give every inclusion edge the fractional value \(1/a\). Every left vertex
then has incident sum one, and every right vertex has incident sum
\(b/a=\lambda_H\), which lies in the interval in (3.4).

Consider the bipartite-flow polytope defined by

\[
\sum_{U\supset X}x_{XU}=1
\quad(X\in\mathcal X),
\tag{3.5}
\]

\[
\lfloor\lambda_H\rfloor
\le\sum_{X\subset U}x_{XU}
\le\lceil\lambda_H\rceil
\quad(U\in\mathcal U),
\tag{3.6}
\]

and \(0\le x_{XU}\le1\). The fractional point above proves feasibility.
The constraint matrix is the node-edge incidence matrix of a bipartite
graph with integral lower and upper bounds, hence is totally unimodular.
It has an integral feasible vertex. At that vertex every left equality
chooses exactly one incident edge, giving (3.3)--(3.4). \(\square\)

This theorem settles every scalar rounding issue. It does **not** order the
assigned owners. For a common-top cycle, the complements

\[
Q_X=U\setminus X\in\binom UH
\tag{3.7}
\]

must be cyclic \(H\)-intervals in one order of \(U\), or in only a few
orders if a few paths per top are allowed. That consecutive-interval
condition is absent from the totally-unimodular assignment.

## 4. Conditional coefficient-one compiler

Call a family \(\mathscr P\) a **growing top-fibre promotion cover** when:

1. every member is a bridge-one promotion path whose full states have one
   common top \(U\in\mathcal U\);
2. the middle owners on all paths partition \(\mathcal X\);
3. for every \(q\le H\), their lower depth-\(q\) flags cover
   \(\binom{[2m]}{m-q}\), and their upper flags cover
   \(\binom{[2m]}{m+q}\); and
4. the number of paths is \(p=O(N_H)\).

Condition 3 at \(q=H\) forces every top \(U\) to occur on at least one
path, because promotion preserves the top and the depth-\(H\) upper flag is
exactly \(U\). Thus \(p\ge N_H\) if each path is confined to one top, and
condition 4 is the correct order of magnitude.

### Theorem 4.1 (top-fibre gate implies coefficient one)

If growing top-fibre promotion covers exist at the depth in Proposition
1.1, then there is a nonzero contiguous-OR word of length

\[
W+o(W)
\tag{4.1}
\]

covering every nonempty subset of \([2m]\).

#### Proof

Initialize each useful-state path independently and then use its bridge-one
updates. The exact useful-prefix compiler uses one entry per owner plus
\(O(H)\) initialization entries per path. Thus the controlled central band
has a word of length

\[
W+O(Hp)=W+O(HN_H)=W+o(W)
\]

by (1.8). Append every mask in the two outer tails literally. Proposition
1.2 adds only \(O(W/H)=o(W)\) entries. All appended masks are nonempty
except the empty set, which need not be covered. \(\square\)

The theorem uses the exact path-hitting flags of the selected states. It
does not assume that arbitrary near-optimal OR words reduce to singleton
near-Ucycles.

## 5. The exact symmetric fractional solution

For a fixed top \(U\), let \(\mathfrak C(U)\) be the family of directed
cyclic orders of \(U\), modulo cyclic rotation. Each order gives the
length-\(M\) promotion cycle of Theorem 2.1.

There are

\[
b=\binom MH
\]

middle owners contained in \(U\), while one cycle contains exactly \(M\)
of them. By transitivity, a uniformly chosen cyclic order contains a fixed
owner \(X\subset U\) with probability

\[
\frac Mb.
\tag{5.1}
\]

### Theorem 5.1 (fractional all-rank promotion cover)

For each top \(U\), distribute total weight

\[
c=\frac{\lambda_H}{M}
\tag{5.2}
\]

uniformly over \(\mathfrak C(U)\). Then:

1. every middle owner has total cycle weight exactly one;
2. at every depth \(q\le H\), every lower and upper target has flag weight
   exactly
   \[
   \frac W{N_q};
   \tag{5.3}
   \]
3. the total cycle weight is
   \[
   cN_H=\frac WM.
   \tag{5.4}
   \]

#### Proof

A middle owner \(X\) lies in exactly \(a=\binom mH\) tops. Equations
(3.2), (5.1), and (5.2) give its total weight as

\[
a\frac Mb\frac{\lambda_H}{M}=1.
\]

The weighted construction is invariant under every coordinate permutation.
It has total middle-state weight \(W\), and every state supplies one lower
and one upper flag at depth \(q\). Transitivity on each rank therefore gives
weight \(W/N_q\) at every target. Finally (5.4) follows from
\(\lambda_HN_H=W\). \(\square\)

Because \(W/N_q\ge1\), this is an exact fractional solution of every owner
equality and every flag-cover inequality. Its weighted initialization cost
is

\[
O\!\left(H\frac WM\right)=o(W).
\tag{5.5}
\]

The sole missing step is integral low-fragmentation rounding.

## 6. Exact audits of tempting roundings

### 6.1 Full cycles have a divisibility/slot mismatch

Selecting one full promotion cycle at every top creates

\[
MN_H=W+O(WH/m)
\tag{6.1}
\]

owner occurrences. They cannot partition the \(W\) owners unless
\(MN_H=W\), equivalently \(\lambda_H=M\). In particular, an assertion that
the full cycles themselves form an exact partition silently assumes this
equality and the resulting divisibility. Variable path lengths avoid the
obstruction: only \(O(WH/m)=o(W)\) total cycle slots must be omitted.

The issue is not the number of omitted slots, but arranging them in only
\(O(1)\) intervals per top while removing every owner collision and every
owner hole.

### 6.2 Independent cyclic orders leave linearly many owner holes

Choose one cyclic order independently and uniformly at every top. For a
fixed owner \(X\), the events over its \(a\) containing tops are independent,
each with probability \(M/b\). Hence

\[
\Pr(X\text{ is uncovered})
=\left(1-\frac Mb\right)^a.
\tag{6.2}
\]

Now

\[
a\frac Mb=\frac M{\lambda_H}=1+O(H/m),
\tag{6.3}
\]

while \(M/b\to0\). Therefore

\[
\Pr(X\text{ is uncovered})=e^{-1}+o(1),
\tag{6.4}
\]

and the expected number of uncovered owners is

\[
(e^{-1}+o(1))W.
\tag{6.5}
\]

If a fixed number \(C\) of independent orders is chosen at every top, the
same calculation gives uncovered probability \(e^{-C}+o(1)\), still a
positive constant. This refutes independent topwise rounding. It does not
refute a correlated integral design.

### 6.3 Shallow ranks have almost no collision budget

Let \(c_q^-(T)\) be the multiplicity of a rank-\((m-q)\) target among the
\(W\) selected lower flags. If every target is covered, then exactly

\[
\sum_T(c_q^-(T)-1)=W-N_q.
\tag{6.6}
\]

The identical formula holds for the upper flags. In particular,

\[
W-N_1=\frac{W}{m+1}.
\tag{6.7}
\]

Thus depth-one coverage requires both flag maps to be injective outside
only \(O(W/m)\) collision excess. More generally, for
\(q=o(\sqrt m)\), (1.2) gives

\[
W-N_q=O(q^2W/m).
\tag{6.8}
\]

The symmetric fractional solution has exactly the right marginals, but
generic independent orders have occupancy-scale, hence linear, holes at
these nearly square ranks. Any rounding theorem must preserve two-sided
rainbowness at all shallow depths simultaneously.

### 6.4 Balanced containment is not promotion orderability

For the balanced assignment \(\phi\) of Theorem 3.1, fix a top \(U\) and
write

\[
\mathcal Q_U=\{U\setminus X:\phi(X)=U\}
\subseteq\binom UH.
\tag{6.9}
\]

To use one common-top cycle, every member of \(\mathcal Q_U\) must be an
\(H\)-interval in one cyclic order of \(U\), and the selected intervals
must form one contiguous run if only one path is allowed. A generic family
of \(\lfloor\lambda_H\rfloor\) or \(\lceil\lambda_H\rceil\) \(H\)-sets
does not have this consecutive-ones property. Total unimodularity proves
only (3.3)--(3.4); it supplies none of this order structure.

Allowing arbitrary promotion paths enlarges the local family, but does not
remove the queue recurrence: the lower departure word shifts FIFO and the
upper word updates by deleting the returned coordinate. Pairwise Johnson
adjacency or top containment alone is therefore insufficient.

## 7. The exact remaining combinatorial lemma

The clean cyclic subgate is the following.

> **Growing common-top interval-path theorem \(\mathrm{GTIP}\).** At the
> depth \(H\) from (0.1), choose for every
> \(U\in\binom{[2m]}{m+H}\) at most \(C\) directed cyclic orders of \(U\),
> where \(C\) is an absolute constant, and in each chosen order take at
> most one contiguous segment of the promotion cycle from Theorem 2.1, so
> that:
>
> 1. the segment owners partition \(\binom{[2m]}m\); and
> 2. for every \(q\le H\), their intervals (2.6) cover rank \(m-q\) and
>    their intervals (2.7) cover rank \(m+q\).

The constant \(C\) may be replaced by the aggregate condition that the
total number of segments is \(O(N_H)\). Theorem 4.1 then gives coefficient
one.

There is an exact finite integer formulation. Let \(\mathcal A\) be the
set of all triples \((U,\pi,I)\), where \(\pi\) is a directed cyclic order
of \(U\) and \(I\) is a nonempty cyclic interval of its \(M\) promotion
states. For \(A\in\mathcal A\), write \(V(A)\) for its owners and
\(L_q(A),U_q(A)\) for its two flag families. The required binary variables
\(x_A\) obey

\[
\sum_{A:X\in V(A)}x_A=1
\qquad\left(X\in\binom{[2m]}m\right),
\tag{7.1}
\]

\[
\sum_{A:T\in L_q(A)}x_A\ge1,
\qquad
\sum_{A:S\in U_q(A)}x_A\ge1
\quad(1\le q\le H),
\tag{7.2}
\]

and

\[
\sum_{A:\,\operatorname{top}(A)=U}x_A\le C
\qquad(U\in\mathcal U).
\tag{7.3}
\]

Depth \(H\) in (7.2) also forces at least one selected segment at every top.
The fractional construction in Theorem 5.1 solves (7.1)--(7.2) when full
cycles are allowed fractionally, with total path weight \(W/M\). What is
missing is an integral solution of (7.1)--(7.3), with all shallow collision
budgets (6.6) respected simultaneously.

A strictly smaller first test is obtained by retaining only \(q=1\) in
(7.2). It asks for an exact owner partition into \(O(N_H)\) common-top
promotion paths whose lower intersections and upper unions both cover their
adjacent ranks. Failure of this two-sided first-band gate would refute the
route. Success would still leave the nested depths \(2,\ldots,H\).

## 8. Theorem ledger

### Proved

1. The exact critical choice \(H=(1+o(1))\sqrt{m\log m}\).
2. \(N_H=(1+o(1))W/m=o(W/H)\).
3. One reset per top costs \(O(HN_H)=o(W)\).
4. Both outer Boolean tails contain only \(O(W/H)=o(W)\) masks.
5. The exact length-\((m+H)\) common-top promotion cycle and all its flags.
6. An exact integral balanced owner-to-containing-top assignment by total
   unimodularity.
7. An exact symmetric fractional common-top cycle solution covering every
   controlled lower and upper rank.
8. The full-cycle slot mismatch is only \(O(WH/m)=o(W)\), but must be
   removed in low-fragmentation intervals.
9. Independent selection of any fixed number of cyclic orders per top
   leaves a positive fraction of owner holes.
10. The exact shallow-rank collision budget (6.6), including
    \(W/(m+1)\) at depth one.
11. \(\mathrm{GTIP}\) implies a \(W+o(W)\) contiguous-OR word.

### Open

1. The two-sided first-band integral path gate.
2. The simultaneous nested flag-cover constraints through depth \(H\).
3. Hence \(\mathrm{GTIP}\) and the unrestricted growing top-fibre promotion
   theorem.

The growing-depth proposal therefore survives every reset, tail, capacity,
and fractional-coverage audit. Its exact frontier is a correlated
cyclic-interval rounding theorem. The critical warning is that the average
owner degree in one independently chosen cycle per top is asymptotically
one, so no uncoordinated topwise choice can approach the required integral
partition.
