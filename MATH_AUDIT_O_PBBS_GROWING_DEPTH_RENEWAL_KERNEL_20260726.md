# PBBS growing-depth chronology: exact horizon renewal, all-time fibre kernel, and shell-packing lower bounds

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .
\tag{0.1}
\]

The exact depth-two/depth-three PBBS audits and the new short-return
threshold kernel are mutually consistent, but two different notions of
depth must not be conflated.

* A consecutive omitted-label gap \(2q-1\) has positive residence \(q\)
  on the complemented centered chronology and has a full cut support of
  \(q+1\) quotient edges.
* It first enters the short-return family at horizon \(H=q\).
* At \(q=2\) there is no such return. At \(q=3\), the gap-five shell has
  exactly \(m-1\) normalized starts and \(n(m-1)\) physical starts.
  These are the exact depth-three wrong-rank defects. They coexist with
  complete correct depth-three support and correct-fibre load between
  one and thirty-five.

The new kernel does have an exact all-horizon recurrence. If

\[
 0<B_1(E)<B_2(E)<\cdots
\]

are the predecessor-selection times of a first-pruned core \(E\), define

\[
 T_z(E):={B_{2z+2}(E)+1\over2}.                  \tag{0.2}
\]

Then \(T_z(E)\) is an integer, is strictly increasing in \(z\), and is
exactly the residence of a parent whose terminal free-slot occupancy is
\(z\). Consequently

\[
 Z_H(E)=\max\{z:T_z(E)\le H\},                  \tag{0.3}
\]

and

\[
 \boxed{Z_{H+1}(E)-Z_H(E)\in\{0,1\}.}           \tag{0.4}
\]

The exact shell added from \(H\) to \(H+1\) is one free-slot level.
This gives the coefficient-exact recurrence in Theorem 2.1 below.

There is also an exact arbitrary-time extension of the published
two-point Pascal kernel. After all parent fibres over a reduced orbit are
pulled back to one weak-composition simplex, simultaneous activity at any
set of phases is just a family of coordinate upper bounds. Its cardinality
is one explicit coefficient, formula (3.4). Thus the *outer Pascal
kernel* iterates at every depth with no loss.

What does not iterate is a contraction. The recurrence still needs the
actual event process

\[
 T_z(\tau^tE)=H
\]

and the transported-slot collision pattern. Neither is determined by the
depth-two/depth-three data. Repeated peak deletion has total Pascal mass
one, and along the critical pruning profile the product of zero-slot
fractions is \(1/2\), not zero. Hence the kernel alone cannot prove
\((ST_A)\).

There is nevertheless a rigorous growing-depth lower bound. Let
\(L_q^{(H)}\) be the number of retained normalized starts of exact
residence \(q\), on quotient cycles longer than \(H+1\). Then

\[
 \boxed{
 \overline\nu_H\ge
 \max_{3\le q\le H}{L_q^{(H)}\over2q+1}.}
\tag{0.5}
\]

More globally, with

\[
 J_H=1+\lfloor\log_2(H+1)\rfloor,
\]

\[
 \boxed{
 \overline\nu_H\ge {1\over4J_H}
 \sum_{q=3}^{H}{L_q^{(H)}\over q+1}.}
\tag{0.6}
\]

These inequalities are uniform in \(q\) and use the actual physical
chronology, not a marginal surrogate. They do not decide \((ST_A)\), but
they give an exact necessary obstruction to every positive proof.

## 1. Indexing dictionary and the fixed-depth audits

Let \((A_t)\) be one oriented odd-graph PBBS component, and let
\(\lambda_t\) be the omitted coordinate on the edge
\(A_tA_{t+1}\). On a step-two parity row,

\[
 B_{j+1}=B_j-\{\lambda_{\epsilon+2j+1}\}
                 +\{\lambda_{\epsilon+2j}\}.     \tag{1.1}
\]

Suppose two consecutive occurrences of one omitted coordinate have gap

\[
 g=2s+1.                                          \tag{1.2}
\]

On the parity on which the first occurrence is an insertion, the
coordinate is present for exactly \(s\) owner states and the two toggles
span \(s+1\) transitions. On the opposite parity it is absent for
\(s+1\) owner states. After complementing that opposite row, it becomes
a positive residence of

\[
 q=s+1={g+1\over2}                                \tag{1.3}
\]

owner states, bounded by exactly

\[
 q+1=s+2                                          \tag{1.4}
\]

transition edges. Therefore the complemented \(G_H+P_H\) chronology is
spoiled precisely by gaps

\[
 g\le2H-1,                                        \tag{1.5}
\]

and the corresponding full interval has at most \(H+1\) quotient edges.
This is the off-by-one convention used in \((ST_A)\).

The fixed-depth audits now read as follows.

1. The no-gap-three theorem gives no residence-two interval. Every
   centered row is \(G_2\), and the complemented rows are \(G_2+P_2\).
   The lower depth-two correct loads lie in \([1,10]\), and the upper
   loads lie in \([1,3]\).
2. Gap five is the first return. It has \(s=2\), residence \(q=3\), and
   four-edge full support. There are exactly \(m-1\) normalized starts,
   hence \(n(m-1)\) physical starts. Every such start contributes one
   unit of depth-three rank excess.
3. Independently, every rank-\((m-3)\) target has a correct directed
   depth-three PBBS occurrence, with correct-occurrence load in
   \([1,35]\). Thus complete correct support and short-return chronology
   are separate statistics already at depth three.
4. Gap seven has residence four. Its normalized shell has exact size
   \(2^{m-1}-m\). This is exponentially large but still exponentially
   negligible compared with \(B_m\).

The original, uncomplemented rank-\(m\) row can fail \(P_2\) at a
gap-five return, because its shorter positive run has only \(s=2\)
states. This does not contradict the preceding dictionary: \((ST_A)\)
uses the complemented full support, whose residence is \(s+1=3\).

## 2. Exact all-horizon renewal

Fix a nonempty first-pruned core

\[
 E\in\mathcal D_d,\qquad k=\operatorname {pk}(E),
 \qquad y=m-d-k,\qquad K=2d+1.                    \tag{2.1}
\]

Its inverse fibre is

\[
 \mathcal W_{K,y}={(n_0,\ldots,n_{K-1})\ge0:
                    \sum_an_a=y\}.               \tag{2.2}
\]

Write \(\star(E)\) for the terminal free slot. The exact predecessor
theorem says that the first parent return for terminal occupancy \(z\) is

\[
 G(D)=B_{2z+2}(E),                                \tag{2.3}
\]

provided the event precedes the outer circumference. In every fixed
Gaussian window it does.

### Lemma 2.1 (integer residence epochs)

For every feasible \(z\), \(B_{2z+2}(E)\) is odd. Hence the numbers
\(T_z(E)\) in (0.2) are strictly increasing positive integers.

#### Proof

Equation (2.3) realizes \(B_{2z+2}(E)\) as the gap between consecutive
occurrences of one omitted PBBS label. Such gaps are odd. Strict increase
follows from the strict increase of the predecessor-selection times.
\(\square\)

The parent has residence at most \(H\) exactly when

\[
 B_{2z+2}(E)\le2H-1
 \quad\Longleftrightarrow\quad
 T_z(E)\le H.                                     \tag{2.4}
\]

Thus (0.3) is identical to the published threshold definition. With the
convention \(Z_H=-1\) before the first epoch, strict integer increase
immediately proves (0.4). More explicitly,

\[
 Z_{H+1}=Z_H+1
 \quad\Longleftrightarrow\quad
 T_{Z_H+1}=H+1.                                   \tag{2.5}
\]

### Theorem 2.1 (exact residence-shell recurrence)

Let \(L_q^{\rm all}(m)\) be the number of normalized rank-\(m\) roots
whose first return has residence exactly \(q\), before short quotient
cycles are deleted. Apart from the completely pruned one-root exception,

\[
 \boxed{
 L_q^{\rm all}(m)=
 \sum_{d=1}^{m-1}\ \sum_{E\in\mathcal D_d}
 \ \sum_{z=0}^{m-d-\operatorname {pk}(E)}
 \mathbf1_{\{T_z(E)=q\}}
 \binom{m+d-\operatorname {pk}(E)-z-1}{2d-1}.}
\tag{2.6}
\]

Consequently

\[
 \boxed{
 R_H^{\rm all}=\sum_{q\le H}L_q^{\rm all},
 \qquad
 R_{H+1}^{\rm all}-R_H^{\rm all}=L_{H+1}^{\rm all}.}
\tag{2.7}
\]

#### Proof

If the terminal coordinate equals \(z\), the remaining free mass
\(y-z\) is distributed among \(K-1=2d\) slots. Its exact cardinality is

\[
 \binom{y-z+K-2}{K-2}
 =\binom{m+d-\operatorname {pk}(E)-z-1}{2d-1}.
\]

Equation (2.4) identifies its exact residence. Inverse fibres partition
the parent roots, proving (2.6). Summation over shells proves (2.7).
\(\square\)

At the level of one fixed core, the new fibre sheet added at horizon
\(H+1\) is either empty or exactly

\[
 \{n_{\star(E)}=Z_H(E)+1\}.                       \tag{2.8}
\]

This is the sharp recurrence supplied by the short-return kernel. It is
not a closed recurrence in \(Z_H\) alone: after an epoch occurs, the next
waiting time

\[
 T_{z+1}(E)-T_z(E)                                \tag{2.9}
\]

is a new PBBS dynamical datum.

## 3. The exact arbitrary-time Pascal kernel

Fix one reduced \(\tau_d\)-cycle and one invariant parent rank/peak cell.
The literal parent PBBS transport identifies every fibre with a reference
copy of \(\mathcal W_{K,y}\). Persistent equality particles preserve
their cyclic order, so this transport permutes the free-gap coordinates.
Thus at phase \(i\), parent activity pulls back to

\[
 A_i=\{\mathbf n:n_{a_i}\le Z_i\},                \tag{3.1}
\]

where \(a_i\in[K]\) is the transported terminal-slot address and
\(Z_i=Z_H(\tau^iE)\). An inactive reduced phase has \(Z_i=-1\) and
\(A_i=\varnothing\).

For a finite phase set \(I\), define, for every slot \(a\),

\[
 c_a(I)=\min\{Z_i:i\in I,\ a_i=a\},              \tag{3.2}
\]

with \(c_a=\infty\) when the set is empty. If any selected phase is
inactive, put the intersection equal to zero.

### Theorem 3.1 (all-time threshold-cylinder kernel)

If every phase in \(I\) is active, then

\[
 \boxed{
 \left|\bigcap_{i\in I}A_i\right|
 =[x^y]\prod_{a:c_a(I)<\infty}
       (1+x+\cdots+x^{c_a(I)})
       \prod_{a:c_a(I)=\infty}{1\over1-x}.}
\tag{3.3}
\]

Equivalently, if \(C(I)=\{a:c_a(I)<\infty\}\), then

\[
 \boxed{
 \left|\bigcap_{i\in I}A_i\right|
 =\sum_{J\subseteq C(I)}(-1)^{|J|}
 \binom{y-\sum_{a\in J}(c_a(I)+1)+K-1}{K-1},}
\tag{3.4}
\]

with the binomial-zero convention.

#### Proof

Repeated tests of one transported coordinate reduce to the smallest cap,
which gives (3.2). For a constrained coordinate \(a\), the generating
polynomial is \(1+x+\cdots+x^{c_a}\); for an unconstrained coordinate it
is \((1-x)^{-1}\). Extracting total free mass \(y\) proves (3.3).
Inclusion--exclusion on the violations
\(n_a\ge c_a+1\) gives (3.4). \(\square\)

The published one- and two-point formulas are the cases \(|I|=1,2\).
The same formula handles exact new shells by replacing the factor for a
coordinate constrained to equal \(z\) by \(x^z\). Two unequal equality
requirements on the same address give zero. Thus all mixed old-shell and
new-shell terms in the identity

\[
\begin{aligned}
 \mathcal C_{H+1}-\mathcal C_H
 ={}&|E_{H+1}\cap\tau^{-(H+2)}E_{H+1}|\\
 &+\sum_{t=1}^{H+1}\bigl(
 |S_H\cap\tau^{-t}E_H|
 +|E_H\cap\tau^{-t}S_H|
 +|S_H\cap\tau^{-t}S_H|\bigr),                  \tag{3.5}
\end{aligned}
\]

where \(S_H=E_{H+1}\setminus E_H\), have exact coefficient formulas.
For (3.5), either use untrimmed sets or delete once and for all every
cycle of length at most the final horizon plus one, so that the sets are
nested.

The algebraic kernel is therefore genuinely uniform in the number of
phases. Its state is not one scalar: it is the collision partition of the
addresses \((a_i)\), together with the coordinatewise minimum caps. This
state is the first exact obstruction to closing (3.5) from one- and
two-point marginals.

In the Pascal saddle

\[
 d=m/2+O(\sqrt{m\log m}),\qquad
 k=m/6+O(\sqrt{m\log m}),                          \tag{3.6}
\]

one coordinate has tail

\[
 \Pr(n_a>L)
 ={(y)_{\underline{L+1}}\over
   (y+K-1)_{\underline{L+1}}}
 =4^{-(L+1)}(1+o(1))                              \tag{3.7}
\]

uniformly for \(L=3\log m\). Hence every local block of
\(O_A(\sqrt m)\) phase tests can be truncated to occupancies at most
\(3\log m\) at total Pascal mass \(o_A(B_m/H)\). This validates the
low-slot reduction uniformly for one Gaussian local block. It does not
make \(O(\sqrt m)\) distinct-coordinate tests asymptotically independent:
their accumulated falling-factorial correction is
\(\exp(O(H^2/m))=\exp(O_A(1))\), not \(1+o(1)\).

## 4. Exact shadow-excess recurrence and the depth-two/depth-three seeds

Let \(M_s\) be the number of normalized consecutive omitted-label gaps
\(2s+1\), so

\[
 L_q=M_{q-1}.                                      \tag{4.1}
\]

Normalize the PBBS rank-excess potential by the spatial deck and put

\[
 e_q=\sum_{s\ge1}(q-s)_+M_s.                     \tag{4.2}
\]

The physical excess is \(ne_q\). Discrete differentiation gives

\[
 \boxed{
 R_q=e_q-e_{q-1},\qquad
 L_q=e_q-2e_{q-1}+e_{q-2}.}
\tag{4.3}
\]

Thus the exact residence-shell process is the second discrete derivative
of the all-window PBBS rank excess. This is a genuine \(q\)-uniform
recurrence. It is a census recurrence, not a chronology recurrence: it
does not record where the corresponding intervals occur on their quotient
cycles.

The audited initial values are

\[
 e_1=e_2=0,\qquad
 L_2=0,\qquad
 L_3=m-1.                                         \tag{4.4}
\]

Equivalently, the physical depth-three excess is

\[
 ne_3=n(m-1).                                     \tag{4.5}
\]

The next exact shell is

\[
 L_4=2^{m-1}-m.                                   \tag{4.6}
\]

These seeds prove that every fixed early depth is negligible on the
Catalan scale. They do not constrain the second differences in a growing
Gaussian window.

The all-depth fan theorem supplies, independently,

\[
 1\le\mu_q^{-,\mathrm{corr}}(S)
 \le\binom{2q+1}{q}.                              \tag{4.7}
\]

Equation (4.7) counts correct-rank occurrences. Equations (4.2)--(4.3)
count wrong-rank residence defects. The coexistence of (4.5) with
complete depth-three support proves that no recurrence using only the
correct-fan loads can control \(L_q\).

## 5. Uniform shell-packing lower bounds

Fix a final horizon \(H\), and retain only quotient cycles of length
greater than \(H+1\). Let \(L_q^{(H)}\) be the number of exact
residence-\(q\) starts on those cycles. Every corresponding interval has
exactly \(q+1\) consecutive quotient edges.

### Theorem 5.1 (one-shell lower bound)

For every \(3\le q\le H\),

\[
 \boxed{
 \overline\nu_H\ge
 \left\lceil{L_q^{(H)}\over2q+1}\right\rceil.}
\tag{5.1}
\]

#### Proof

Restrict to the residence-\(q\) shell. On one quotient cycle, two
\((q+1)\)-edge circular intervals can intersect only if their start
positions differ by one of the \(2q\) nonzero offsets from \(-q\) through
\(q\). There is at most one return start at each quotient position.
Hence the shell conflict graph has maximum degree at most \(2q\). A
greedy independent set has size at least
\(L_q^{(H)}/(2q+1)\). Different quotient cycles are disjoint. \(\square\)

This proves (0.5). In terms of the excess recurrence, before the
negligible short-cycle deletion it reads

\[
 \overline\nu_H\ge
 \max_{3\le q\le H}
 {e_q-2e_{q-1}+e_{q-2}\over2q+1},                 \tag{5.2}
\]

with the appropriate short-cycle subtraction when a retained inequality
is required.

### Theorem 5.2 (dyadic harmonic-shell lower bound)

Equation (0.6) holds.

#### Proof

Partition the intervals by dyadic support length:

\[
 2^j\le q+1<2^{j+1}.
\]

Let \(N_j\) be the number in bin \(j\). Every interval in that bin has
fewer than \(2^{j+1}\) edges. Thus its conflict degree within the bin is
less than \(2^{j+2}-1\), and the bin has an independent subfamily of
size at least \(N_j/2^{j+2}\). On the other hand,

\[
 \sum_{q\text{ in bin }j}{L_q^{(H)}\over q+1}
 \le {N_j\over2^j}.
\]

The best bin therefore contributes at least one fourth of its harmonic
mass. There are at most \(J_H\) bins, proving (0.6). \(\square\)

The logarithm in (0.6) cannot be removed for arbitrary circular interval
systems from shell sizes alone: intervals of geometrically many lengths
can all contain one common edge. A PBBS improvement would have to use the
predecessor itinerary or transported-slot cocycle.

Two necessary consequences of \((ST_A)\) are now explicit:

\[
 L_q^{(H)}=o_A\!\left({(2q+1)B_m\over H}\right)
 \quad(3\le q\le H),                              \tag{5.3}
\]

and

\[
 \sum_{q=3}^{H}{L_q^{(H)}\over q+1}
 =o_A\!\left({B_m\log H\over H}\right).          \tag{5.4}
\]

They are obstructions, not sufficient conditions.

## 6. Why the exact kernel does not close \((ST_A)\)

There are four independent losses.

1. **The renewal epochs are not determined recursively by their count.**
   Equation (0.4) says at most one new slot layer appears at each horizon,
   but the waiting time (2.9) is an unconstrained reduced-PBBS statistic.
2. **The all-time fibre kernel retains address monodromy.** Formula
   (3.4) depends on which phase tests hit the same free slot. The
   two-point same-slot factor can be \(4/3+o(1)\) larger than the product
   density. At \(O(\sqrt m)\) phases, the entire collision partition is
   needed.
3. **Peak-deletion recursion has coefficient one.** The inverse fibres
   partition the Catalan space with total Pascal weight one. On the
   critical pruning profile \(r_j\sim r/(j+1)\), the successive zero-slot
   fractions are

   \[
   1-{1\over(j+2)^2},
   \]

   whose infinite product is \(1/2\). Thus repeated zero-slot restrictions
   do not force vanishing mass.
4. **Pair correlations do not upper-bound packing.** Even divergent mean
   short-lag correlation is compatible, for circular interval systems,
   with an independent family containing a positive fraction of all
   starts. A positive proof needs the full degree/cluster law, not only
   \(R_H\) and \(\mathcal C_H\).

The exact recurrence candidates left after this audit are therefore:

\[
 \text{renewal event process }(T_z(\tau^tE)),
\tag{6.1}
\]

\[
 \text{transported-slot cocycle }(a_t),
\tag{6.2}
\]

and the circular interval scheduling recurrence on the actual supports.
The outer weak-composition algebra is solved by (3.4).

## 7. Precise proved boundary

Proved here, from the audited PBBS inputs:

* the exact residence normalization \(T_z=(B_{2z+2}+1)/2\);
* the one-layer horizon increment (0.4);
* the exact shell census (2.6)--(2.7);
* the arbitrary-time Pascal threshold kernel (3.3)--(3.4);
* the second-difference shadow/residence recurrence (4.3);
* the exact depth-two/depth-three seeds and their correct normalization;
* the uniform shell and dyadic packing lower bounds (5.1) and (0.6).

Not proved:

* no \(o_A(B_m/H)\) upper bound for \(\overline\nu_H\);
* no Catalan-critical lower bound for a bounded-degree return family;
* no distribution theorem for the renewal epochs or slot-address cocycle;
* no implication from all-depth correct-support loads to residence packing.

Thus the short-return kernel does iterate exactly as an algebraic fibre
kernel, but it does not iterate as a contracting probabilistic recurrence.
The sharp remaining datum is the Pascal-weighted, growing-window joint law
of (6.1)--(6.2) along the actual reduced PBBS cycles.

## 8. Addendum: adjacent-particle split form of every occupancy sheet

The predecessor epochs in Section 2 admit a sharper orbitwise expression.
This section audits the augmentation factor, parity, and the constants in
the resulting fixed-degree packing bound.

Work on a particle-augmented rank-\(d\) reduced orbit \(\mathcal O\), put

\[
 p=2d+1,\qquad L=|\mathcal O|,
\]

and write \(\kappa_s\in\mathbb Z_p\) for the particle selected at ordinary
PBBS time \(s\). Every particle is selected \(L/p\) times. Fix adjacent
particles \(b,a=b+1\). Write the \(b\)-selection times as \(t_{b,i}\), put

\[
 g_{b,i}=t_{b,i+1}-t_{b,i},                       \tag{8.1}
\]

and let \(s_{b,i}\) be the unique \(a\)-selection strictly between
\(t_{b,i-1}\) and \(t_{b,i}\). Define

\[
 r_{b,i}=t_{b,i}-s_{b,i}.                         \tag{8.2}
\]

Strict adjacent-particle alternation gives this unique split.

### Theorem 8.1 (all-occupancy adjacent-split formula)

For terminal occupancy \(z\ge0\), the parent return gap is

\[
 \boxed{
 G^{(z)}_{b,i}
 =r_{b,i}+\sum_{j=0}^{2z}g_{b,i+j}.}
\tag{8.3}
\]

The endpoint is the \((2z+2)\)-nd future \(b\)-selection,
\(t_{b,i+2z+1}\). Moreover

\[
 \boxed{
 G^{(0)}_{b,i}=r_{b,i}+g_{b,i},\qquad
 G^{(z+1)}_{b,i}=G^{(z)}_{b,i}
 +g_{b,i+2z+1}+g_{b,i+2z+2}.}
\tag{8.4}
\]

If

\[
 h_{b,i}=s_{b,i+1}-s_{b,i}
 =g_{b,i}+r_{b,i}-r_{b,i+1},                     \tag{8.5}
\]

then the split-index recurrence is

\[
 \boxed{
 G^{(z)}_{b,i+1}-G^{(z)}_{b,i}
 =g_{b,i+2z+1}-h_{b,i}.}
\tag{8.6}
\]

#### Proof

Starting immediately after the \(a\)-selection at \(s_{b,i}\), the
future \(b\)-selections are

\[
 t_{b,i},t_{b,i+1},\ldots .
\]

The terminal spacing \(2z+1\) requires \(2z+1\) previous \(b\)-moves
before the final predecessor move. Hence the final move is the
\((2z+2)\)-nd future selection, at \(t_{b,i+2z+1}\). Its delay from
\(s_{b,i}\) is exactly (8.3). The next \(a\)-selection lies strictly
between \(t_{b,i}\) and \(t_{b,i+1}\), hence before the final predecessor
move even when \(z=0\). Thus the leader-return clause in the exact
predecessor-passage theorem is automatic. This proves (8.3), and adding
the next two \(b\)-gaps proves (8.4).

Shifting \(i\) in (8.3) gives

\[
 G^{(z)}_{b,i+1}-G^{(z)}_{b,i}
 =(r_{b,i+1}-r_{b,i})+g_{b,i+2z+1}-g_{b,i}.
\]

Equation (8.5) turns the right side into (8.6). \(\square\)

On an actual PBBS orbit, \(G^{(z)}_{b,i}\) is an odd ordinary-time gap.
Its residence and full support length are respectively

\[
 q^{(z)}_{b,i}={G^{(z)}_{b,i}+1\over2},\qquad
 q^{(z)}_{b,i}+1.                                 \tag{8.7}
\]

Strict alternation by itself does not force this odd parity; abstract
alternating-word examples with even values are not PBBS realizations.
Thus (8.3) must not be called a residence without the conversion (8.7).

### Theorem 8.2 (exact augmented occupancy-sheet census)

Put \(y=m-d-k\) and

\[
 K_z(m;d,k)=\binom{m+d-k-z-1}{2d-1}.             \tag{8.8}
\]

Apart from the completely pruned one-root exception, the number of
untrimmed normalized parent roots of exact residence \(q\) is

\[
 \boxed{
 L_q^{\rm all}(m)=
 \sum_{d,k}\ \sum_{\mathcal O}
 {1\over2d+1}
 \sum_{b\in\mathbb Z_{2d+1}}
 \sum_{i=1}^{L/(2d+1)}
 \sum_{z=0}^{y}
 K_z(m;d,k)
 \mathbf1_{\{G^{(z)}_{b,i}=2q-1\}}.}
\tag{8.9}
\]

Here \(\mathcal O\) ranges over particle-augmented reduced orbits of the
indicated rank and peak count.

#### Proof

Every augmented phase selects one particle \(a\), hence belongs to a
unique triple \((b=a-1,i,s_{b,i})\). For fixed phase and fixed terminal
occupancy \(z\), stars and bars gives exactly (8.8) parent lifts.
Theorem 8.1 gives their return gap. Every unaugmented reduced root has
exactly \(p=2d+1\) particle augmentations, which accounts for the single
factor \(1/p\). There is no additional parity factor: summing all ordinary
phases counts both \(\tau=\phi^2\) subdecks, whose union is the complete
root set. \(\square\)

The factor \(1/(2d+1)\) is only the augmented-to-root normalization. It
must not be applied a second time to the inverse-fibre sheet. At the
Pascal saddle, for fixed \(z\),

\[
 {K_z(m;d,k)\over P_m(d,k)}
 =\left({3\over4}+o(1)\right)4^{-z}.             \tag{8.10}
\]

### Fixed-degree packing constants and the parity correction

Let \(x\) be an augmented phase and let

\[
 a_H(x)=\mathbf1_{\{G^{(0)}(x)\le2H-1\}}.        \tag{8.11}
\]

This is the reduced predecessor-active indicator. If \(\sigma\) denotes
one ordinary augmented PBBS step, define the two-sided degree majorant

\[
 \Delta_H(x)=\sum_{u=1}^{H+1}
 \bigl(a_H(\sigma^{2u}x)+a_H(\sigma^{-2u}x)\bigr). \tag{8.12}
\]

The exponent is \(2u\), not \(u\): one parent quotient step is
\(\tau=\phi^2\). Nor can it be replaced by \(i\mapsto i+u\), because
\(i\) indexes visits of one particle and the intervening ordinary-time
gaps are variable.

For every eligible parent above \(x\), its full conflict degree is at
most \(\Delta_H(x)\). Indeed, an eligible shifted parent at quotient lag
\(u\) makes the shifted core predecessor-active at the corresponding
ordinary phase \(\sigma^{2u}x\). The shifted terminal occupancy need not
equal the initial occupancy. This is why a fixed-\(z\) active-phase count
does not majorize conflict degree; (8.11), or the actual transported
occupancy vector, is required.

Consequently, if a parent subfamily \(\mathcal U\) satisfies

\[
 \Delta_H(x(D))\le K\qquad(D\in\mathcal U),       \tag{8.13}
\]

then Caro--Wei gives the exact bound

\[
 \boxed{
 \overline\nu_H\ge
 {\bigl(|\mathcal U|-Z_H^{\rm cyc}\bigr)_+\over K+1}.}
\tag{8.14}
\]

If only the forward count

\[
 \Delta_H^+(x)=\sum_{u=1}^{H+1}a_H(\sigma^{2u}x)
\]

is bounded by \(K\), orient every conflict edge forward. Then
\(|E|\le K|\mathcal U|\), and Caro--Wei--Cauchy gives only

\[
 \boxed{
 \overline\nu_H\ge
 {\bigl(|\mathcal U|-Z_H^{\rm cyc}\bigr)_+\over2K+1}.}
\tag{8.15}
\]

There is no intrinsic factor two in (8.14). A later restriction to one
of the two simple-return parities can halve the packing, but that is a
separate reduction. Combining (8.10) with (8.14), a fixed-\(z\),
two-sided degree-\(K\) augmented phase mass \(M\) in the saddle gives the
leading quotient-packing coefficient

\[
 {3\,4^{-z}\over4(K+1)}M,                         \tag{8.16}
\]

before short-cycle error. The optional simple-return reduction changes
this to \(3\,4^{-z}/(8(K+1))\).
