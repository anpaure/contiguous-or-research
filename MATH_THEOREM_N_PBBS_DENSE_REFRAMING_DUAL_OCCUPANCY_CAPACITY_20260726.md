# PBBS dense reframing: exact dual occupancy, a long-cycle conveyor, and the marginal-entropy capacity obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil .                 \tag{0.1}
\]

This note attacks the dense-reframing residual isolated in
`MATH_THEOREM_PBBS_RECIPROCAL_HEIGHT_LOG_STABILITY_AND_DIFFUSION_OBSTRUCTION_20260726.md`.
It does not prove or disprove \((ST_A)\) or \((QST_A)\).  It proves a
sharp capacity obstruction to one natural entropy route and gives an
actual long-cycle calibration family.

There are three exact conclusions.

1.  Along an actual PBBS return, a transition changes the canonical
    first-deepest frame if and only if its dual staircase word is
    nonempty.  Therefore the total reframing count is exactly an
    occupancy count, and the longest stable block is exactly the longest
    zero run in that occupancy word.

2.  Every binary occupancy word is realized by a genuine first
    zero-winding PBBS return.  More strongly, one may insert an arbitrary
    bounded-height Dyck spectator of semilength \(m-O(\sqrt m)\) without
    changing the occupancy word, the first-return margins, or the exact
    endpoint floor \(\Lambda=0\).

3.  Fix \(0<\alpha<A\) and \(\varepsilon>0\), and put

    \[
      s=\lfloor\alpha\sqrt m\rfloor,
      \qquad
      q_m=\left\lceil
       \left({1\over2}+\varepsilon\right)\log _2m
      \right\rceil .                              \tag{0.2}
    \]

    For every fixed \(\eta>0\), all sufficiently large \(m\) admit a
    pairwise quotient-edge-disjoint family \(\mathcal P_m\) of genuine
    nonwrapping, zero-winding, duration-\(s\) PBBS returns on quotient
    cycles longer than \(H_A+1\), of residence \(s+1\le H_A\), such that
    (as full positive-residence intervals, these traces have exactly
    \(s+2\) quotient edges)

    \[
      R(I)\ge {s\over10},\qquad G(I)<q_m
      \quad(I\in\mathcal P_m),                    \tag{0.3}
    \]

    and

    \[
      \boxed{
      |\mathcal P_m|
       \ge {B_m\over s}
          \exp\!\left(-\bigl(\log(3+\eta)+o(1)\bigr)s\right).}
                                                            \tag{0.4}
    \]

    Thus neither a pointwise prohibition based only on these itinerary
    statistics nor generic cyclic interval packing eliminates the dense,
    half-logarithmically gap-free class.
    Formula (0.4) is still exponentially smaller in \(\sqrt m\) than
    the critical scale \(B_m/s\), so it is not a counterexample to
    \((QST_A)\).

There is also an exact marginal no-go.  In the capped dual-array product
which underlies the best zero-winding enumeration, the critical
Boltzmann mass of

\[
 R\ge s/10,
 \qquad
 G<\left({1\over2}+\varepsilon\right)\log _2m
                                                            \tag{0.5}
\]

tends to one uniformly on Gaussian height bands.  Consequently those
statistics remove only \(o(1)\) of the **unconditioned critical product
partition function**.  This is not a coefficientwise assertion after
conditioning the total dual size to the outer semilength.  A proof of
\((QST_A)\) must therefore use either such a fixed-coefficient
correlation, the literal common-carrier equations, or an incompatibility
between the carriers of different quotient-edge-disjoint intervals.
Point margins, scalar first-passage margins, and the occupancy word alone
are insufficient at the unconditioned marginal-product level.

## 1. Dual staircase words are exactly the reframing indicators

Let \(\tau=\phi^2\) be the normalized step-two PBBS map.  Along a genuine
return of invariant height \(s\), write the canonical first-maximum
factorizations as

\[
 D_j=P_j1R_j0S_j.                                 \tag{1.1}
\]

The exact dual-tail decomposition supplies a Dyck word \(T_j\) satisfying

\[
 S_j1P_j=P_{j+1}1\overline {T_j}.                 \tag{1.2}
\]

Here complementation exchanges zero and one without reversing order.

### Lemma 1.1 (exact frame/occupancy dictionary)

The transition \(D_j\mapsto D_{j+1}\) preserves the transported
canonical first-deepest frame if and only if

\[
                         T_j=\varnothing.          \tag{1.3}
\]

Moreover, if

\[
 e_j=\delta(D_j),\qquad d_j=|S_j|+1,
\]

then

\[
 \boxed{|T_j|=e_j+d_j-e_{j+1}-1.}                \tag{1.4}
\]

#### Proof

The literal block rotation is

\[
 \tau D_j=S_j1P_j0R_j.                            \tag{1.5}
\]

The endpoint of the transported old deepest spine is the height-\(s\)
visit at the end of \(S_j1P_j\).  The new canonical first-deepest leaf is
the height-\(s\) visit at the end of \(P_{j+1}1\).  Equation (1.2) says
that the contour between these visits is \(\overline {T_j}\), a
nonpositive excursion based at height \(s\).

If \(T_j\ne\varnothing\), the two visits are distinct and the new one is
strictly earlier, so the frame changes.  If \(T_j=\varnothing\), the two
visits and hence their unique root-to-leaf spines coincide.  This proves
(1.3).  Taking lengths in (1.2) gives (1.4). \(\square\)

For a return core with transitions indexed by \(0\le j\le s-2\), define

\[
 R(I)=\#\{j:T_j\ne\varnothing\},                  \tag{1.6}
\]

and let \(G(I)\) be the maximum length of a consecutive run of empty
\(T_j\)'s.  Lemma 1.1 gives these identities literally.  In particular,
there is no additional binary invariant hidden in the phrase
"canonical reframing itinerary."

## 2. A spectator-conveyor realization theorem

The next construction extends the star-comb return by allowing zero
teeth and by inserting a large arbitrary spectator.

Fix \(s\ge3\), an index \(1\le k\le s-1\), nonnegative integers

\[
 L_0,L_1,\ldots,L_{s-2}\ge0,                     \tag{2.1}
\]

and a Dyck word \(Q\) of semilength \(q\) satisfying

\[
 \operatorname {ht}(Q)\le \min\{k,s-k\}.         \tag{2.2}
\]

Put \(F_i=(10)^{L_i}\).  Define a literal canonical sector word of
height \(s\) by

\[
 A_i=F_i\ (0\le i\le s-2),\qquad A_{s-1}=\varnothing,           \tag{2.3}
\]

\[
 B_k=Q,\qquad B_i=\varnothing\ (i\ne k),          \tag{2.4}
\]

inside

\[
 D_0=A_0\,1A_1\,1\cdots1A_{s-1}\,1
       0B_{s-1}0\cdots0B_1\,0B_0.                \tag{2.5}
\]

Its semilength is

\[
 m=s+q+\sum_{i=0}^{s-2}L_i.                      \tag{2.6}
\]

### Theorem 2.1 (exact spectator conveyor)

Assume \(m>s\).  The word \(D_0\) starts a genuine first zero-winding
PBBS return of step-two duration exactly \(s\).  For
\(0\le j\le s-2\), its \(j\)-th core transition changes frame if and only
if

\[
                         L_{s-j-2}>0.              \tag{2.7}
\]

Writing

\[
 U_j=\sum_{i=0}^{s-j-2}L_i
 \quad(0\le j<s),\qquad U_s=0,                   \tag{2.8}
\]

the exact deficit and endpoint ledgers are

\[
 d_j=1+2q\,\mathbf1_{\{j=k\}}\quad(0\le j<s),   \tag{2.9}
\]

\[
 \delta(D_j)=s+2U_j+2q\,\mathbf1_{\{j\ge k+1\}}
 \quad(0\le j\le s),                            \tag{2.10}
\]

and

\[
 |T_j|=2L_{s-j-2}\quad(0\le j\le s-2),
 \qquad T_{s-1}=\varnothing.                     \tag{2.11}
\]

Finally,

\[
 \boxed{\Lambda=\delta(D_0)+\delta(D_s)-2m=0.}   \tag{2.12}
\]

#### Proof

The following sector invariant makes the chronology explicit.  For
\(0\le j\le s-1\), the star part of the canonical phase-\(j\) sectors is

\[
 A_i^{(j),\star}=
 \begin{cases}
  F_{i-j},&j\le i\le s-2,\\
  \varnothing,&\text{otherwise},
 \end{cases}                                      \tag{2.13a}
\]

and

\[
 B_i^{(j),\star}=
 \begin{cases}
  F_{2s-j-i-2},&s-j\le i\le s-1,\\
  \varnothing,&\text{otherwise}.
 \end{cases}                                      \tag{2.13b}
\]

The spectator occupies \(B_{k-j}\) for \(0\le j\le k\), and occupies
\(A_{j-k-1}\) for \(k+1\le j\le s\).  These positions never collide
with the displayed star ranges: \(k-j<s-j\) on the \(B\)-side and
\(j-k-1<j\) on the \(A\)-side.

Equations (2.13a)--(2.13b) follow by induction from the literal sector
transport.  At transition \(j\), the formal top pre-spine forest is
exactly \(F_{s-j-2}\).  If it is nonempty, its first tooth becomes the
new canonical spine child.  Its remaining teeth followed by the old
transported spine child form exactly the post-spine forest
\(F_{s-j-2}\) in (2.13b).  If it is empty, no reframing occurs and the
formal transport already gives (2.13a)--(2.13b) at phase \(j+1\).
Thus the induction is valid with arbitrary zero \(L_i\)'s and proves
(2.7).

Every \(F_i\) has height at most one, so all displayed canonical
pre-spine stars stay strictly below height \(s\).  While \(Q\) is post-spine,
its weakest height cap is \(s-k\).  While it is pre-spine, its weakest
strict cap occurs at the endpoint and is \(k\).  Condition (2.2) therefore
shows that \(Q\) never preempts the displayed spine.  It is transported
unchanged through the entire induction.

For the transition phases \(0\le j<s\), the root-level post-spine word is
empty except at phase \(k\), where it is \(Q\).  This proves (2.9).  (At
the return endpoint, the transported star gives
\(B_0^{(s)}=F_{s-2}\) and hence
\(d(D_s)=1+2L_{s-2}\); this unused next-transition deficit is not part of
(2.9).)  The unconsumed pre-spine stars contribute
\(2U_j\) to the first-maximum position.  The spectator contributes
another \(2q\) precisely after it has crossed from \(B_0\) to \(A_0\).
This proves (2.10).

Let \(C_j=\sum_{i<j}d_i\).  Equations (2.9)--(2.10) give

\[
 C_j=j+2q\,\mathbf1_{\{j\ge k+1\}},              \tag{2.14}
\]

and hence, for every \(j<s\),

\[
 \delta(D_j)-C_j=s-j+2U_j>0,                     \tag{2.15}
\]

while \(\delta(D_s)=C_s=s+2q\).  All quantities are strictly below
\(N=2m+1\).  Thus the ordinary zero-winding equality occurs at phase
\(s\) and at no earlier odd phase.  The height-gap theorem excludes an
earlier return of either parity.  Since \(m>s\), the resulting gap
\(2s+1\) is nonwrapping.

Substitution of (2.9)--(2.10) in (1.4) proves (2.11).  Finally

\[
 \delta(D_0)=s+2\sum_iL_i,qquad
 \delta(D_s)=s+2q,
\]

and (2.6) gives (2.12). \(\square\)

The theorem realizes every binary word of length \(s-1\): take
\(L_i=1\) on the desired support and \(L_i=0\) elsewhere.  The arbitrary
spectator \(Q\) changes none of the binary chronology.

## 3. Dense, gap-free actual returns have exponential-rate mass

We now count a large subfamily of Theorem 2.1.  The purpose is not to
approach the critical scale, but to make quotient-edge disjointness and
long-cycle survival explicit.

Fix \(0<\alpha<A\) and put \(s=\lfloor\alpha\sqrt m\rfloor\).  Take

\[
 k=\lfloor s/2\rfloor,
 \qquad t=\min\{k,s-k\}.                          \tag{3.1}
\]

Fix an integer \(K\ge2\), and restrict each \(L_i\) to
\(\{0,1,\ldots,K\}\).  Put

\[
 a_K=\sum_{\ell=0}^{K}4^{-\ell},qquad
 p_K={a_K-1\over a_K},qquad
 \rho_K={1\over a_K}.                            \tag{3.2}
\]

Under the normalized product weight proportional to
\(4^{-\sum_iL_i}\), the indicators \(\mathbf1_{\{L_i>0\}}\) are
independent Bernoulli variables of parameter \(p_K\).  Since \(K\ge2\),

\[
 p_K\ge {5\over21}>{1\over5}.                    \tag{3.3}
\]

### Lemma 3.1 (weighted dense words with no half-logarithmic gap)

Let \(n=s-1\), and let \(q_m\) be as in (0.2).  The total product weight
of vectors \((L_0,\ldots,L_{s-2})\) satisfying

\[
 \#\{i:L_i>0\}\ge s/10                         \tag{3.4}
\]

and having no consecutive zero run of length \(q_m\) is at least

\[
                         a_K^{s-1}\exp(-o(s)).    \tag{3.5}
\]

#### Proof

Let \(b=\lfloor(q_m-1)/2\rfloor\), and partition the \(n\) positions
into consecutive full blocks of length \(b\), plus one terminal block of
length less than \(b\).  Require every full block to contain a positive
\(L_i\).  A zero run can then use at most the tail of one full block and
the head of the next block, or the final short block.  Its length is less
than \(2b<q_m\).

The full blocks are independent, so the probability of this event is

\[
 (1-\rho_K^b)^{\lfloor n/b\rfloor}
 =\exp\!\left(-O\left({s\over b}\rho_K^b\right)\right)
 =\exp(-o(s)),                                    \tag{3.6}
\]

because \(b\to\infty\).  Independently, the Chernoff bound and (3.3)
give

\[
 \Pr\!\left(\#\{i:L_i>0\}<s/10\right)\le e^{-c_Ks}. \tag{3.7}
\]

Both requirements are increasing events in the product partial order.
The elementary Harris inequality therefore lower-bounds the probability
of their intersection by the product of their probabilities.  It is
\(\exp(-o(s))\).  Multiplication by the full weight \(a_K^{s-1}\)
proves (3.5). \(\square\)

### Lemma 3.2 (uniform spectator mass)

For fixed \(\alpha>0\) and fixed \(K\), uniformly over
\(0\le L_i\le K\), put

\[
 M=m-s-\sum_iL_i.                                \tag{3.8}
\]

Then, for all sufficiently large \(m\),

\[
 \#\{Q\in\mathcal D_M:\operatorname {ht}(Q)\le t\}
 \ge c_{\alpha,K}\,4^{-s-\sum_iL_i}B_m.          \tag{3.9}
\]

#### Proof

Here \(M=m-O_{\alpha,K}(\sqrt m)\), while
\(t=(\alpha/2+o(1))\sqrt m\).  Thus \(M/t^2\) stays in a fixed compact
subinterval of \((0,\infty)\).  The finite path-graph lower bound gives

\[
 \#\{Q\in\mathcal D_M:\operatorname {ht}(Q)\le t\}
 \ge c_{\alpha,K}4^MM^{-3/2}.                    \tag{3.10}
\]

Wallis' estimate gives \(B_m\le C4^mm^{-3/2}\).  Since
\(M/m\to1\), division proves (3.9). \(\square\)

### Theorem 3.3 (actual long-cycle capacity lower bound)

For every fixed \(A>0\), \(0<\alpha<A\), \(\varepsilon>0\), and
\(\eta>0\), the family in (0.3)--(0.4) exists.

#### Proof

Sum (3.9) over the vectors in Lemma 3.1.  The number \(\mathcal S_m\) of
distinct genuine start roots obtained from Theorem 2.1 satisfies

\[
 \begin{aligned}
 |\mathcal S_m|
 &\ge c_{\alpha,K}B_m4^{-s}
       \sum_{\mathbf L\in\mathcal G_{m,s}}4^{-\sum_iL_i}\\
 &\ge c_{\alpha,K}B_m4^{-s}a_K^{s-1}\exp(-o(s)).
 \end{aligned}                                    \tag{3.11}
\]

Here \(\mathcal G_{m,s}\) denotes the set of vectors satisfying the two
conditions in Lemma 3.1.

The sector decomposition of \(D_0\) recovers \(\mathbf L\) and \(Q\),
so no two counted roots coincide.  By Theorem 2.1 and Lemma 3.1, they
all satisfy (0.3).

Since \(a_K\uparrow4/3\), choose fixed \(K\) so large that

\[
                         {4\over a_K}<3+\eta.     \tag{3.12}
\]

Then (3.11) gives

\[
 |\mathcal S_m|
 \ge B_m\exp\!\left(-\bigl(\log(3+\eta)+o(1)\bigr)s\right). \tag{3.13}
\]

The audited voltage-itinerary bound places only \(\exp(o_A(m))\)
quotient roots on cycles of length at most \(H_A+1\).  For all
sufficiently large \(m\), \(s+1\le H_A\), so the constructed return
has residence at most \(H_A\), and its full positive-residence trace
has exactly \(K=s+2\le H_A+1\) quotient edges.  The logarithm of
the right side of (3.13) is

\[
                         m\log4-O(\sqrt m),       \tag{3.14}
\]

so deleting every short-cycle root changes (3.13) by a relative
\(o(1)\).  Every remaining duration-\(s\) trace is nonwrapping on its
quotient cycle.

Finally, on a directed cycle, one chosen full residence interval of
\(K=s+2\) consecutive edges intersects intervals whose starts lie in at
most \(2K-1=2s+3\) positions.  Greedy selection therefore retains at
least a \((2s+3)^{-1}\) fraction of the remaining starts.  This proves
(0.4), after absorbing the constant factor and \(2+3/s\) into the
\(o(1)\) term.  The required one-start-per-edge hypothesis holds because
return starts are bijectively reindexed by quotient edges (using the
preceding tail-time edge), and the normalized roots in \(\mathcal S_m\)
are distinct.
\(\square\)

The exponential factor in (0.4) is important for scope.  The theorem
rules out a deterministic ban and shows that cyclic interval packing is
not the missing source of a vanishing factor.  It does not approach
\(B_m/s\), so it gives no lower bound against \((QST_A)\).

## 4. The capped dual-product is saturated by the critical chronology

We now isolate why the individual dual height caps give no entropy
contraction on the remaining class.

For a genuine zero-winding return of duration \(s\) and endpoint overlap
\(\Lambda=2\ell\), the audited shifted cap on the dual word is

\[
 \operatorname {ht}(T_j)\le
 \beta_j:=\min\{s-1-j,j+1+\ell\},
 \qquad0\le j<s.                                 \tag{4.1}
\]

Let \(\mathfrak T_{s,\ell}\) be the product of these capped Dyck-word
classes.  Give a tuple \(\mathbf T\) the critical Boltzmann probability
proportional to

\[
                         4^{-\sum_j|T_j|/2}.       \tag{4.2}
\]

The factors are independent.  If a cap is \(b\), then

\[
 C_b(1/4)={2(b+1)\over b+2},                      \tag{4.3}
\]

so

\[
 \Pr(T_j=\varnothing)={b+2\over2(b+1)},
 \qquad
 \Pr(T_j\ne\varnothing)={b\over2(b+1)}.          \tag{4.4}
\]

Only the core indices \(0\le j\le s-2\) are used below.

### Theorem 4.1 (critical dual-occupancy saturation)

There are absolute constants \(c>0\) and \(s_0\) such that, uniformly in
\(\ell\ge0\), for \(s\ge s_0\),

\[
 \Pr\left(\#\{0\le j\le s-2:T_j\ne\varnothing\}<s/10\right)
 \le e^{-cs}.                                    \tag{4.5}
\]

Moreover, for every \(2\le q\le s/4\),

\[
 \boxed{
 \Pr(\text{some run of }q\text{ consecutive empty }T_j)
 \le 4s(q+2)2^{-q}.}                             \tag{4.6}
\]

Consequently, for every fixed \(0<a<A\), uniformly for

\[
 a\sqrt m\le s\le A\sqrt m,
 \qquad
 q=q_m,
\]

the product probability of

\[
 \#\{j:T_j\ne\varnothing\}\ge s/10,
 \qquad G(\mathbf T)<q_m                          \tag{4.7}
\]

tends to one.

#### Proof

For every

\[
                         s/4\le j\le3s/4-1,
\]

one has \(\beta_j\ge s/4-1\).  Hence (4.4) gives a nonempty probability
at least \(1/3\) for all sufficiently large \(s\).  There are at least
\(s/2-2\) such independent positions, so their mean is at least
\(s/6-2/3\).  The threshold \(s/10\) is a fixed fraction below this
mean for all sufficiently large \(s\), and the Chernoff bound gives
(4.5).

For (4.6), fix a consecutive core interval \(J\) of length \(q\).  Since

\[
 \beta_j\ge\min\{j+1,s-1-j\},                    \tag{4.8}
\]

there are three cases.  If \(J\) lies in the left half, its lower bounds
in (4.8) increase by one at each step, and (4.4) telescopes to

\[
 \Pr(T_j=\varnothing\ \forall j\in J)
 \le 2^{-q}{a+q+1\over a+1}
 \le(q+2)2^{-q}                                  \tag{4.9}
\]

for an integer \(a\ge1\).  The right half is identical after reversal.
 If \(J\) crosses the midpoint, every cap in \(J\) is at least
 \(s/2-q-1\).  Since \(q\le s/4\), (4.4) gives

\[
 \Pr(T_j=\varnothing\ \forall j\in J)
 \le e^2 2^{-q}\le4(q+2)2^{-q}.                 \tag{4.10}
\]

after enlarging the harmless constant for the finitely many small
\(q\)'s.  A union bound over fewer than \(s\) starts proves (4.6).

 For \(q=q_m\), equation (4.6) is at most

\[
 4A(q_m+2)\sqrt m\,m^{-1/2-\varepsilon}
 =O_A((\log m)m^{-\varepsilon})=o(1).            \tag{4.11}
\]

Combine this with (4.5). \(\square\)

Theorem 4.1 is a capacity statement about the exact capped product used
in the present array majorants.  It is not a claim that arbitrary product
arrays satisfy the common-carrier word equation or are actual PBBS
returns.  Nor does the unconditioned probability estimate imply that the
same ratio tends to one in the coefficient with a prescribed total
semilength: conditioning can in principle correlate occupancy with total
size.  What is proved is exact at the stated level: imposing linear
reframing and excluding stable blocks above the half-logarithmic threshold
removes only \(o(1)\) of the unconditioned product's critical mass, so
those two marginal conditions alone supply no loss in that partition
function.

## 5. Quotient-edge disjointness and the exact surviving gate

Theorem 3.3 uses quotient-edge disjointness in its strongest elementary
form: after short cycles are deleted, arbitrary duration-\(s\) starts,
whose full residence intervals have \(s+2\) quotient edges, lose at most
a factor \(2s+3\) under greedy cyclic interval packing.  Its actual
family already has

\[
 R\ge s/10,\qquad G<q_m,\qquad
 w=0,qquad\Lambda=0.                             \tag{5.1}
\]

Thus none of the following gives the desired little-oh through the
pointwise or unconditioned independent-product estimates tested here:

1. the binary locations of frame changes;
2. a pointwise assertion forbidding dense or gap-free reframing;
3. the scalar first-passage inequalities;
4. the individual dual height caps; or
5. generic interval packing on the quotient cycles.

One exact escape not tested by the capacity constructions is literal
carrier compatibility.  For zero winding it includes the transported
tail equations

\[
 (\overline T_{u-1}0)\cdots(\overline T_t0)R_t
 =R_u(0S_u)\cdots(0S_{t+1}),                     \tag{5.2}
\]

at all pairs of phases, together with canonical first-maximum validity.
The product theorem in Section 4 deliberately forgets (5.2), while the
spectator conveyor satisfies it only in a family whose density is
\(\exp(-\Theta(s))\).  A second escape, not excluded by the
unconditioned Boltzmann calculation, is a coefficientwise contraction
after fixing the total dual size at the required outer semilength.

Accordingly the precise remaining positive statement is one of the
following genuinely stronger assertions.

* **Fixed-coefficient or single-return carrier entropy:** either the
  dense event has a vanishing fraction of the capped product's target
  total-size coefficient, or the actual solutions of all equations
  (5.2) in the dense class have a vanishing coefficient relative to the
  full capped product, uniformly at semilength \(m\asymp s^2\).

* **Cross-return carrier incompatibility:** even if their start count is
  critical, a positive fraction of their duration-\(s\), full
  \((s+2)\)-edge quotient traces must overlap because their literal
  carrier words coincide in a bounded-multiplicity certificate.

Neither assertion is proved here.  The established boundary is exact:
the proposed dense-itinerary entropy is saturated at the marginal level,
actual dense gap-free returns survive on long quotient cycles with the
quantitative lower bound (0.4).  A fixed-coefficient contraction, literal
common-carrier compatibility, or cross-trace compatibility remains
capable of proving \((QST_A)\).
