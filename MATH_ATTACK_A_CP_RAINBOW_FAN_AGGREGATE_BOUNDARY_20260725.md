# Lane A after the linear seam: rainbow zero-winding sectors and the exact CP boundary

Date: 2026-07-25

Method: pure mathematics only.  No finite search, solver, computation, or
web search is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B=\operatorname{Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
\]

where \(A>0\) is fixed.  The audited dominance-staircase seam reduces the
coefficient-one PBBS gate to

\[
 \boxed{\overline\nu_H=O_A(B/N).}
 \tag{CP_A}
\]

The present report does **not** prove \((CP_A)\), and hence does not prove
coefficient one.  It gives the following unconditional advances and a
sharp failure theorem for the most direct zero-winding route.

1.  Every genuine zero-winding return is a rainbow return: before the
    returned endpoint, all \(2h+1\) omitted labels are distinct.  Its two
    owner parities are exact fixed-core halves of one cyclic wreath, and
    one complement-projected half has the literal \((2h+1)\)-letter OR
    compiler

    \[
      \{a_0\},\ldots,\{a_{h-1}\},F,
      \{b_0\},\ldots,\{b_{h-1}\}.
    \]

2.  The audited triangular Pascal fan extends through every pruning level,
    with cyclic wrapping handled exactly.  At level \(j\), it fixes

    \[
      t_j=\min\{j,2r_j\}
    \]

    independent weak-composition degrees.  This yields the full integral
    profile factor in (3.4) below.

3.  On the unsaturated part of a profile, that factor always obeys the
    endpoint estimate

    \[
      Q\le \sqrt{h/r_0}.
    \]

    The hoped-for strengthening \(Q=O(h/r_0)\), which would combine with
    trace length to reach \(B/N\), is false even for genuine zero-winding
    returns with \(h=\sqrt{r_0}\).  An explicit protected-sector family
    satisfies

    \[
      Q\frac{r_0}{h}\longrightarrow\infty.
    \]

    This is a theorem about actual PBBS chronology, not merely a formal
    convex rank profile.

4.  The preceding counterprofiles lie in the exact no-preemption cone.
    That whole cone has superpolynomially small Catalan mass in every fixed
    Gaussian window, in fact \(o_A(B/N)\).  Thus the counterprofiles close
    the **pointwise** fan-times-trace proof but do not disprove
    \((CP_A)\).

5.  For positive winding, the two endpoint sector partitions have common
    mass exactly \(wN\).  The resulting two-parity budget proves the
    \((CP_A)\)-scale estimate for every fixed high-winding sector

    \[
      w\ge\eta\sqrt r.
    \]

    For a rigorous fixed-rank split, the positive residual is
    \(1\le w<\eta\sqrt r\) for any chosen fixed \(\eta>0\), especially
    \(w=1\).

The exact missing input is therefore aggregate rather than pointwise.  For
zero winding it is a trace--fan tensorization across spine-changing
profiles; for low positive winding it is a genuine transported-sector
matching inequality.  Both are stated precisely in Section 7.

## 1. Zero-winding coordinates

Let \(D_j=\tau^jD_0\), where \(\tau=\phi^2\), and write the canonical
first-maximum factorization as

\[
 D_j=P_j1R_j0S_j.
\]

Put

\[
 c_j=|S_j|+1,
 \qquad \delta_j=|P_j|+1,
 \qquad C_j=\sum_{i<j}c_i,
 \qquad Y_j=\delta_j-C_j.
 \tag{1.1}
\]

Suppose that the initial omitted coordinate \(u\) has a genuine first
zero-winding return after \(2h+1\) ordinary PBBS moves.  Then

\[
 C_h=\delta_h<N.
 \tag{1.2}
\]

The two-step block identity gives

\[
 Y_{j+1}-Y_j=-d(\phi D_j)<0.
 \tag{1.3}
\]

Thus

\[
 0=C_0<C_1<\cdots<C_h<N,
 \tag{1.4}
\]

and

\[
 \delta_0=Y_0>Y_1>\cdots>Y_h=0.
 \tag{1.5}
\]

The strict staircase theorem also gives

\[
 \operatorname{ht}(D_j)=h
 \quad(0\le j\le h),
 \qquad c_0=1.
 \tag{1.6}
\]

The actual omitted labels are

\[
 \boxed{
 \lambda_{2j}=a_j:=u-C_j,
 \qquad
 \lambda_{2j+1}=b_j:=u+Y_j
 }
 \pmod N.
 \tag{1.7}
\]

Here \(b_h=a_0=u\) is the returned endpoint.

## 2. Rainbow rigidity and the literal fixed-core compiler

### Theorem 2.1 (rainbow zero-winding trace)

The labels

\[
 \lambda_0,\lambda_1,\ldots,\lambda_{2h}
\]

are pairwise distinct.  The only repetition through the return endpoint is

\[
 \lambda_{2h+1}=\lambda_0=u.
\]

#### Proof

Equations (1.4) and (1.7) make the even labels pairwise distinct, and
(1.5) does the same for the odd labels.  Suppose that

\[
 a_j=b_k
\]

other than \((j,k)=(0,h)\).  Since \(C_j,Y_k\in[0,N-1]\), the congruence
in (1.7) gives

\[
 C_j+Y_k=N.
 \tag{2.1}
\]

If \(k\ge j\), then

\[
 N=C_j+Y_k\le C_k+Y_k=\delta_k<N,
\]

a contradiction.  Hence \(k<j\).  The two equal occurrences are at
times \(2k+1\) and \(2j\), and neither parity contains an intervening
copy.  They therefore delimit a consecutive return of odd gap

\[
 2(j-k)-1\le2h-1.
\]

The normalized root at its first occurrence is \(\phi D_k\), whose height
is \(h\) by height invariance.  The height--gap theorem requires every
consecutive return on that orbit to have gap at least \(2h+1\), a
contradiction.  This proves the theorem.  \(\square\)

### Theorem 2.2 (two fixed cores)

Let \(A_t\in\binom{[N]}r\) be the original PBBS states.  There are
disjoint sets \(K,K'\), each of size \(r-h\), such that

\[
 \boxed{
 A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
             \cup\{b_j,\ldots,b_{h-1}\}}
 \tag{2.2}
\]

for \(0\le j\le h\), and

\[
 \boxed{
 A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
              \cup\{a_{j+1},\ldots,a_h\}}
 \tag{2.3}
\]

for \(0\le j\le h\).  Moreover

\[
 A_{2h+2}=K\cup\{a_1,\ldots,a_h\}.
 \tag{2.4}
\]

#### Proof

The factor recurrence is

\[
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.
 \tag{2.5}
\]

The rainbow theorem says that the \(2h+1\) active labels are all distinct.
At time zero, every \(b_j\) is present and every \(a_j\) is absent until
its insertion.  Hence

\[
 A_0=K\cup\{b_0,\ldots,b_{h-1}\},
\]

with \(|K|=r-h\).  The inactive complement has size \(2(r-h)\), and
the Kneser recurrence splits it into \(K\dot\cup K'\).  Iterating (2.5)
gives (2.2); complementing across the omitted label gives (2.3); the
returned endpoint move gives (2.4).  \(\square\)

The active labels in the cyclic order

\[
 (b_0,\ldots,b_{h-1},a_0,\ldots,a_h)
 \tag{2.6}
\]

make (2.2)--(2.3) the two fixed-core halves of an exact wreath.  Arbitrary
orders of \(K\) and \(K'\) give \((r-h)!^2\) explicit ambient wreath
completions of the open segment.  The actual returned endpoint edge is
kept separate: it repeats \(a_0\), whereas a short simple wreath completion
must next use an inactive core label.

### Theorem 2.3 (literal target-square compiler)

Choose either complement-projected half and orient it so that

\[
 X_{t+1}=X_t-\{a_t\}+\{b_t\},
 \qquad 0\le t<h.
 \tag{2.7}
\]

Put

\[
 F=X_0\setminus\{a_0,\ldots,a_{h-1}\}.
\]

Then \(|F|=r+1-h\ge1\), and

\[
 X_t=F\cup\{a_t,\ldots,a_{h-1}\}
          \cup\{b_0,\ldots,b_{t-1}\}.
 \tag{2.8}
\]

For \(0\le p,q\le h\), define

\[
 T_{p,q}=F\cup\{a_q,\ldots,a_{h-1}\}
             \cup\{b_0,\ldots,b_{p-1}\}.
 \tag{2.9}
\]

Then

\[
 T_{p,q}=
 \begin{cases}
  \displaystyle\bigcap_{t=p}^{q}X_t,&p\le q,\\[5pt]
  \displaystyle\bigcup_{t=q}^{p}X_t,&p\ge q.
 \end{cases}
 \tag{2.10}
\]

All \((h+1)^2\) targets are distinct, and the literal word

\[
 \boxed{
 \{a_0\},\ldots,\{a_{h-1}\},F,
 \{b_0\},\ldots,\{b_{h-1}\}}
 \tag{2.11}
\]

has OR equal to \(T_{p,q}\) on its interval of positions

\[
 [q,h+p].
\]

#### Proof

Equation (2.8) follows by iterating (2.7), using rainbowness to exclude
all arrival--departure collisions.  Coordinatewise intersection and union
then give (2.10).  In (2.11), the interval \([q,h+p]\) contains exactly
the displayed members of (2.9).  Nonemptiness follows from \(|F|\ge1\).
Distinctness follows from the disjoint \(a\)- and \(b\)-labels.  \(\square\)

This is a literal compiler, not a transversal.  Its scope is local: it
covers owner intervals lying wholly in the sector.  It does not itself
cover longer \(H\)-windows extending beyond both endpoints, nor does it
bound how many sectors can be edge-disjoint globally.

## 3. The full wrapped Pascal fan

Let

\[
 D^{(j)}=\partial^jD,
 \qquad r_j=\tfrac12|D^{(j)}|,
 \qquad
 \ell=\min\{j:r_j=h-j\}.
 \tag{3.1}
\]

Thus \(D^{(\ell)}\) is the mountain of rank \(h-\ell\).  The audited
tight-return fan gives at level \(j\) the \(j+1\) exact returns

\[
 I_{j,a}=[2a,\,2a+2(h-j)+1],
 \qquad 0\le a\le j.
 \tag{3.2}
\]

Their returned equality-particle labels are consecutive cyclic labels.

### Theorem 3.1 (full-depth wrapped inverse capacity)

For \(1\le j\le\ell\), put

\[
 t_j=\min\{j,2r_j\},
 \qquad
 y_j=r_{j-1}-2r_j+r_{j+1}\ge0.
 \tag{3.3}
\]

At inverse level \(j\), the fan fixes \(t_j\) independent degrees of the
weak composition of \(y_j\) into \(2r_j+1\) cyclic child slots.
Consequently, for every fixed realizable rank profile and bottom core, the
compatible inverse-tower fraction is at most

\[
 \boxed{
 \widehat Q_\ell(\mathbf r)=
 \prod_{j=1}^{\ell}
 \frac{
  \binom{r_{j-1}+r_{j+1}-t_j}{2r_j-t_j}
 }{
  \binom{r_{j-1}+r_{j+1}}{2r_j}
 }.}
 \tag{3.4}
\]

#### Proof

The unrestricted inverse fibre at level \(j\) is the weak-composition
simplex

\[
 \binom{y_j+2r_j}{2r_j}
 =\binom{r_{j-1}+r_{j+1}}{2r_j}.
 \tag{3.5}
\]

Adjacent members of the fan give terminal-gap equations in \(j\)
consecutive cyclic slot labels.  There are \(\min\{j,2r_j+1\}\) distinct
labels.  A composition has only \(2r_j\) independent degrees, so choose
any \(t_j=\min\{j,2r_j\}\) of them.  Equality-particle transport to a
common phase expresses each equation as one prescribed value of the
corresponding initial slot variable.  Distinct labels prescribe distinct
variables.

If the prescribed variables have total value \(w\ge0\), the number of
remaining compositions is

\[
 \binom{y_j-w+2r_j-t_j}{2r_j-t_j}
 \le
 \binom{y_j+2r_j-t_j}{2r_j-t_j}.
\]

Divide by (3.5) and multiply over the conditionally independent inverse
levels.  This gives (3.4).  \(\square\)

For every \(j\le2h/3\), rank dominates height and gives

\[
 2r_j\ge2(h-j)\ge j.
\]

Hence \(t_j=j\) unconditionally through depth \(2h/3\), improving the
old \(h/2\) cutoff.  If \(q=h-\ell\) and \(\ell\ge2q\), the final fibre is
saturated.  Since first-mountain minimality gives \(y_\ell\ge1\), its
factor is at most

\[
 \frac1{\binom{2q+y_\ell}{2q}}
 \le\frac1{2q+1}.
 \tag{3.6}
\]

## 4. The pointwise product ceiling and its genuine counterprofile

First suppose the relevant nonzero-curvature levels are unsaturated, so
their factors in (3.4) use \(t_j=j\).  Write

\[
 P_j=
 \begin{cases}
 \displaystyle\prod_{i=0}^{j-1}
 \frac{2r_j-i}{2r_j+y_j-i},&y_j>0,\\[7pt]
 1,&y_j=0,
 \end{cases}
 \qquad Q=\prod_{j=1}^{\ell}P_j.
 \tag{4.1}
\]

The hypothesis says precisely that \(j\le2r_j\) whenever \(y_j>0\),
so every displayed nontrivial product is defined.  Zero-curvature levels
contribute one even when their cyclic slot list has wrapped.

### Lemma 4.1 (universal square-root endpoint bound)

One has

\[
 \boxed{Q\le\sqrt{h/r_0}.}
 \tag{4.2}
\]

#### Proof

Put \(d_j=r_{j-1}-r_j\).  At the terminal mountain,
\(d_{\ell+1}=1\), and

\[
 y_j=d_j-d_{j+1}.
\]

Summation by parts gives

\[
 r_0=h+\sum_{j=1}^{\ell}j y_j.
 \tag{4.3}
\]

Define

\[
 S_{j+1}=h+\sum_{a>j}a y_a,
 \qquad S_j=S_{j+1}+j y_j.
 \tag{4.4}
\]

The rank identity is

\[
 r_j=h-j+\sum_{a>j}(a-j)y_a\le S_{j+1}.
 \tag{4.5}
\]

Every factor in \(P_j\) is at most

\[
 \left(1+\frac{y_j}{2r_j}\right)^{-1},
\]

so

\[
 P_j\le
 \left(1+\frac{y_j}{2S_{j+1}}\right)^{-j}.
\]

Bernoulli's inequality gives

\[
 P_j^{-2}
 \ge
 \left(1+\frac{y_j}{2S_{j+1}}\right)^{2j}
 \ge1+\frac{j y_j}{S_{j+1}}
 =\frac{S_j}{S_{j+1}}.
\]

Multiplication telescopes from \(S_1=r_0\) to
\(S_{\ell+1}=h\), proving (4.2).  \(\square\)

The square-root bound is too weak for \((CP_A)\).  More importantly, the
desired first-power endpoint bound is false dynamically.

### Theorem 4.2 (genuine Gaussian counterprofile to \(Q=O(h/r_0)\))

For every \(K\ge1\), put

\[
 h=10^{3K},\qquad \ell=10^K,
 \qquad J_t=10^t\quad(1\le t\le K),
 \tag{4.6}
\]

and define

\[
 y_{J_t}=2^{K-t}10^{3K-t}
          =\frac{2^{K-t}h}{J_t},
 \qquad
 y_1=h^2-2^Kh,
 \tag{4.7}
\]

with all other \(y_a=0\).  There is a Dyck root of semilength

\[
 r_0=h^2
\]

which starts a genuine first zero-winding return of gap \(2h+1\), has
first mountain depth \(\ell\), realizes exactly the curvature profile
(4.7), and satisfies

\[
 \boxed{
 Q\frac{r_0}{h}
 >\frac9{10}\bigl(2e^{-3/5}\bigr)^K
 \longrightarrow\infty.}
 \tag{4.8}
\]

#### Proof

Use a first-deepest spine of height \(h\).  Put every pre-spine forest
\(A_i\) equal to empty.  In the protected post-spine sector at depth
\(a\), put

\[
 B_a=(1^a0^a)^{y_a}.
 \tag{4.9}
\]

Every supported \(a\) satisfies \(a\le\ell<h/2\), and

\[
 \operatorname{fht}(B_a)=a\le a.
\]

The audited no-preemption criterion therefore applies.  Through all
\(h\) shifts,

\[
 \delta(D_j)-C_j=h-j>0\quad(j<h),
 \qquad \delta(D_h)=C_h.
\]

Thus the return is genuine, first, and zero-winding.  Its cumulative
deficit is

\[
 C_h=2h^2-h<2h^2+1,
\]

so there is no hidden modular wrap.

After \(j\) peak-pruning rounds, a length-\(a\) path contributes
\((a-j)_+\).  Hence

\[
 r_j=h-j+\sum_{a>j}(a-j)y_a.
 \tag{4.10}
\]

The sparse forest mass is

\[
 \sum_{t=1}^KJ_ty_{J_t}=h(2^K-1),
\]

and (4.7) gives \(r_0=h^2\).  Since \(y_\ell>0\), (4.10) also makes
\(\ell\) the first mountain depth.

For \(J_t=10^t\), put \(G_t=2^{K-t}h\).  Then

\[
 r_{J_t}=G_t-J_t\left(1+\sum_{u>t}y_{J_u}\right).
\]

The relative subtraction is at most

\[
 10^{-2K}+\sum_{v\ge1}20^{-v}
 \le\frac1{100}+\frac1{19}.
\]

Consequently

\[
 2r_{J_t}-J_t+1>\frac53G_t.
\]

Since \(J_ty_{J_t}=G_t\) and \(\log(1+x)\le x\),

\[
 -\log P_{J_t}<\frac35.
\]

At level one,

\[
 r_1>\frac9{10}2^Kh,
 \qquad
 P_1>\frac9{10}\frac{2^K}{h}.
\]

All other curvature factors equal one.  Multiplication proves (4.8), and
\(2e^{-3/5}>1\) because \(\log2>3/5\).  \(\square\)

### Corollary 4.3 (the explicit obstruction is aggregate-negligible)

Let \(G_{r,h}\) be the number of protected no-preemption roots of
semilength \(r\) and height \(h\).  Then, for every fixed \(A>0\),

\[
 \boxed{
 \sum_{1\le h\le A\sqrt r}G_{r,h}=o_A(B/N).}
 \tag{4.11}
\]

#### Proof

The original height-\(h\) attachment restriction and the protected-sector
restriction together give the exact product

\[
 G_{r,h}=[z^{r-h}]
 \prod_{i=0}^{h-1}C_{\min\{i,h-i\}}(z).
 \tag{4.12}
\]

For the needed upper bound, coefficientwise monotonicity gives

\[
 G_{r,h}\le[z^{r-h}]\prod_{i=0}^{h-1}C_i(z)
 =[z^{r-h}]\frac1{F_h(z)},
 \tag{4.12a}
\]

where \(C_i\) counts Dyck forests of height at most \(i\), and

\[
 F_0=F_1=1,
 \qquad F_{j+1}=F_j-zF_{j-1}.
\]

At \(z=1/4\),

\[
 F_h(1/4)=\frac{h+1}{2^h}.
\]

Nonnegative coefficients give

\[
 G_{r,h}\le\frac{4^r}{2^h(h+1)}.
 \tag{4.13}
\]

The same roots have height \(h\), so the path-graph bound gives

\[
 G_{r,h}\le4^r\exp\!\left(-c\frac r{(h+2)^2}\right).
 \tag{4.14}
\]

Split at \(h=6\log_2r\).  The sum below the split is

\[
 O(\log r)4^r
 \exp\!\left(-c'\frac r{\log^2r}\right)
 =o(B/N).
\]

By (4.13), the remaining sum, even extended to all heights, is at most

\[
 4^r\sum_{h\ge6\log_2r}2^{-h}
 =O(4^rr^{-6})
 =o(B/N),
\]

because \(B/N\asymp4^r/r^{5/2}\).  This proves (4.11).  \(\square\)

Theorem 4.2 therefore rules out a pointwise proof, not the aggregate
conjecture.  Any successful argument must show that all other profiles
with large \(Q\) are similarly rare, or exploit clustering of their
traces.

## 5. Positive winding: an exact two-endpoint overlap

For a general return of step-two time \(s\), put

\[
 a_j=\delta(D_j),\quad b_j=\delta(\phi D_j),
 \quad c_j=d(D_j),\quad \widehat c_j=d(\phi D_j).
\]

The block identities give

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1}.
 \tag{5.1}
\]

With

\[
 C_j=\sum_{i<j}c_i,
 \qquad Y_j=a_j-C_j,
\]

one has

\[
 Y_{j+1}=Y_j-\widehat c_j.
 \tag{5.2}
\]

If the winding is \(w\ge1\), then

\[
 C_s=a_s+wN,
 \qquad Y_s=-wN.
 \tag{5.3}
\]

### Theorem 5.1 (two-endpoint overlap staircase)

Define

\[
 E_j=(-C_{j+1},-C_j],
 \qquad O_j=(Y_{j+1},Y_j]
 \quad(0\le j<s).
\]

Then the \(E_j\)'s and \(O_j\)'s are two ordered partitions whose common
range is exactly

\[
 (-wN,0].
\]

Their nonempty intersections form a monotone path of at most \(2s-1\)
cells, have total length \(wN\), and one cell has length at least

\[
 \boxed{\frac{wN}{2s-1}.}
 \tag{5.4}
\]

#### Proof

The increasing \(C_j\)'s partition
\((-a_s-wN,0]\) through the intervals \(E_j\).  Equation (5.2) makes the
\(Y_j\)'s strictly decreasing from \(a_0\) to \(-wN\), so the \(O_j\)'s
partition \((-wN,a_0]\).  Their common interval is \((-wN,0]\).
Restricting both partitions to it leaves at most \(2(s-1)\) internal
boundary points, hence at most \(2s-1\) refinement cells.  Their indices
move monotonically because both endpoint lists are ordered.  Pigeonhole
gives (5.4).  \(\square\)

### Theorem 5.2 (two-endpoint winding budget)

For every quotient-edge-disjoint family \(\mathcal P\) of return intervals,

\[
 \boxed{
 \sum_{I\in\mathcal P}
 \bigl(2Nw(I)+a_0(I)+a_s(I)\bigr)
 \le2\mathscr D_r,}
 \tag{5.5}
\]

where

\[
 \mathscr D_r=\sum_{D\in\mathcal D_r}d(D)
 =\Theta(B\sqrt r).
 \tag{5.6}
\]

#### Proof

The even trace supports are disjoint, so (5.3) gives

\[
 \sum_I(a_s(I)+Nw(I))
 \le\mathscr D_r.
\]

The map \(\phi\) is a bijection.  Hence the half-shifted trace supports
are also disjoint, and the telescope of (5.2) gives

\[
 \sum_I(a_0(I)+Nw(I))
 \le\mathscr D_r.
\]

Adding proves (5.5).  The moment estimate (5.6) is the audited exact
first-deficit moment theorem.  \(\square\)

### Corollary 5.3 (high winding is at the CP scale)

For every \(K\ge1\),

\[
 \#\{I\in\mathcal P:w(I)\ge K\}
 =O\!\left(\frac{B}{K\sqrt r}\right).
 \tag{5.7}
\]

In particular, for every fixed \(\eta>0\),

\[
 \boxed{
 \#\{I\in\mathcal P:w(I)\ge\eta\sqrt r\}
 =O_\eta(B/N).}
 \tag{5.8}
\]

Thus, after fixing any \(\eta>0\), only
\(1\le w<\eta\sqrt r\) remains on the positive side.

## 6. What the proved structure does not multiply

There are two separate critical failures.

First, for zero winding, edge-disjointness gives a trace factor of order
\(1/h\), while the harmonic fan gives a fibre factor of order \(1/h\).
Theorem 4.2 proves that these two factors cannot be multiplied pointwise
over every genuine rank profile.  The protected counterprofiles have large
pointwise fan fraction, even though Corollary 4.3 proves that their total
Catalan mass is negligible.

Second, for positive winding, Theorem 5.1 gives one large even--odd overlap
cell, but summing the cell lengths reproduces the same moment resource
\(\mathscr D_r\) as (5.5).  It does not square that resource.  A formal
constant-profile cycle can simultaneously saturate the height, centered
winding, both endpoint, area, voltage, and trace ledgers at packing
\(\Theta(B/\sqrt r)\).  Such a profile fails literal omitted-coordinate
coverage and is not a PBBS orbit; its role is to show that the word
compatibility cannot be omitted.

The rainbow OR compiler in Theorem 2.3 also does not evade these failures.
It provides exact local witnesses, but an independent sector contains
\((h+1)^2\) distinct targets.  Any word covering just those targets has
length \(L\) with

\[
 \frac{L(L+1)}2\ge(h+1)^2,
\]

so \(L\ge(\sqrt2+o(1))h\).  Independent sector compilation therefore has
positive linear cost.  Coefficient one requires sharing across profiles or
ambient collars, not merely the local compiler.

## 7. Exact remaining lemmas

### 7.1 Zero winding

Let \(b_{r,h}\) be the number of semilength-\(r\) Dyck roots of height
exactly \(h\).  A sufficient theorem at precisely the required scale is:

> **Chronology-sensitive zero-winding square-trace lemma — UNPROVED.**  For
> every fixed \(A>0\), every quotient-edge-disjoint family
> \(\mathcal P_h^0\) of genuine zero-winding returns of height \(h\le
> A\sqrt r\) satisfies
> \[
>   |\mathcal P_h^0|\le C_A\frac{b_{r,h}}{h^2}.
> \tag{7.1}
> \]

Indeed, the standard height spectrum gives

\[
 \sum_{h\le A\sqrt r}\frac{b_{r,h}}{h^2}
 =O_A(B/r).
 \tag{7.2}
\]

For completeness, heights at least \(\sqrt r\) contribute at most
\(B/r\).  On the dyadic block

\[
 2^{-j-1}\sqrt r<h\le2^{-j}\sqrt r,
\]

the path-graph estimate gives

\[
 \sum_{t\le2^{-j}\sqrt r}b_{r,t}
 \le C B\,2^{3j}e^{-c4^j}.
\]

Multiplication by the largest \(h^{-2}\) on the block bounds its
contribution by

\[
 \frac{CB}{r}\,2^{5j}e^{-c4^j},
\]

and this series is summable.  This proves (7.2), including the
low-height range.  Thus (7.1) implies the zero-winding part of
\((CP_A)\).

The content of (7.1) is exactly a tensorization: trace disjointness alone
gives one \(1/h\), and the Pascal fan alone gives the other only on typical
profiles.  It must use the rainbow chronological trace to combine them
after summing over profiles.  Theorem 4.2 proves that (7.1) cannot follow
from a universal pointwise bound \(Q=O(h/r_0)\).

### 7.2 Positive winding

Choose from every low-winding interval a cell of Theorem 5.1 with length at
least \(N/(2H-1)\).  Edge-disjointness makes the chosen even roots distinct
and the chosen half-shifted roots distinct.  The remaining theorem is:

> **Genuine transported-sector matching lemma — UNPROVED.**  For every
> fixed \(A,\eta>0\), every matching obtained from genuine PBBS trajectories
> by selecting one such large cell from each edge-disjoint return with
> \(1\le w<\eta\sqrt r\) has size \(O_{A,\eta}(B/N)\).

The word “genuine” is indispensable: the exact numerical pseudoprofile
described in Section 6 violates the conclusion while satisfying all scalar
ledgers.

Apply the positive lemma with any one fixed \(\eta>0\), and combine it with
Corollary 5.3 for \(w\ge\eta\sqrt r\).  Together with the zero-winding
lemma, this implies \((CP_A)\); the audited dominance-staircase seam then
implies coefficient one.

## 8. Adversarial audit

1.  The false converse \(d(D)=1\Rightarrow\) return is never used.  Every
    zero-winding theorem begins with an actual first zero-winding return.

2.  Rainbowness is proved using the height--gap theorem; it is not inferred
    from monotonicity of the two same-parity lists alone.

3.  The literal compiler covers only the internal target square of one
    sector.  It is not claimed to repair arbitrary external crossing
    windows or to prove \((CP_A)\).

4.  Cyclic wrapping in the Pascal fan is retained through
    \(t_j=\min\{j,2r_j\}\).  The invalid claim that all terminal fan labels
    are distinct is not used.

5.  The first version of the multiscale counterprofile put side forests
    before the deepest spine and was unsafe.  The proved version puts all
    side forests in the protected post-spine sectors, satisfies the exact
    no-preemption criterion, and was independently audited.

6.  The counterprofile disproves only the pointwise profile estimate.  Its
    whole protected cone is \(o(B/N)\), so it is not a counterexample to
    \((CP_A)\).

7.  The high-winding theorem uses quotient normalization: its total
    resource is \(\mathscr D_r\), not \(N\mathscr D_r\).

8.  No claim of coefficient one is made.  The remaining zero-winding and
    low-positive-winding lemmas are explicitly unproved.
