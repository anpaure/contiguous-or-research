# Chronological-upset Hall compression and adaptive orbit repairs

**Date:** 2026-08-02  
**Status:** unconditional Hall compression/uncrossing theorem; exact
counterexamples to deterministic fixed-core orders; unconditional adaptive
static factors at K11, K46, and K121. The all-\(k\)
\(d(k)+O(1)\) Hall clause and every literal serialization statement remain
explicitly **unproved**.

## 0. Verdict

The global flow in Theorem 7.3 of
`MATH_THEOREM_K19_K21_FIXED_CORE_NORMAL_SPLITS_AND_ALLK_ORBIT_TRANSPORT_GATE_20260802.md`
has an exact smaller dual:

> Hall need only be checked on chronology-compatible containment upsets.

For such an upset, Hall is exactly an exposed-root inequality against its
rank-\(r\) owner shadow. This proves a genuine compression theorem, not
another sufficient condition.

Capacity alone still does not imply that inequality. Ascending binary-mask
next fit has an explicit full staircase deficit \(6\,659\,211\,024\) at
K41 and a much larger explicit deficit at K121. Universally safe pairwise
orbit swaps are essentially absent.

There are nevertheless exact adaptive repairs:

* a one-orbit underfill/edge-cover repair at K11;
* a five-orbit balanced-core menu repair at K46, with no extra block; and
* a fresh-collar repair at K121 with depth \(d(121)+1=8\), even though its
  second block has no normalized coupling to the next rank.

These are static chain factors. They are distinct from both the
uniform-adjacent-coupling architecture and literal contiguous-OR
serialization.

## 1. Global successor graph

Let \(\mathcal T\) be the strict-lower targets and \(\mathcal O\) the
rank-\(r\) owners. Fix a chronology

\[
                         \tau:\mathcal T\longrightarrow\{0,\ldots,q-1\}.
\]

The successor graph \(G_\tau\) has a left copy of \(\mathcal T\), right
copies of \(\mathcal T\dot\cup\mathcal O\), and arcs

\[
\begin{aligned}
 x&\longrightarrow y
   &&\Longleftrightarrow\quad
     x\subsetneq y,\quad \tau(x)<\tau(y),\\
 x&\longrightarrow O
   &&\Longleftrightarrow\quad x\subsetneq O.
\end{aligned}                                        \tag{1.1}
\]

A left-saturating matching is exactly an anchored chain factor following
strictly increasing times.

Define the chronological containment order on targets by

\[
 x\preceq_\tau y
 \quad\Longleftrightarrow\quad
 x=y\ \text{or}\ 
 \bigl(x\subsetneq y\ \text{and}\ \tau(x)\le\tau(y)\bigr).    \tag{1.2}
\]

Notice the weak time inequality in (1.2). Same-time containment is not a
successor arc, but it is load-bearing in Hall compression.

## 2. Exact upset compression

### Theorem 2.1 (chronological-upset Hall theorem)

The graph \(G_\tau\) has a matching saturating its left shore if and only if

\[
                         |U|\le |N(U)|                \tag{2.1}
\]

for every \(\preceq_\tau\)-upset \(U\subseteq\mathcal T\).

If a group \(G\) preserves containment and \(\tau\), every Hall failure has
a \(G\)-invariant upset witness of maximum deficiency.

#### Proof

If \(x\preceq_\tau y\), then

\[
                            N(y)\subseteq N(x).       \tag{2.2}
\]

Indeed, every later target or owner containing \(y\) also contains \(x\),
and its target time is later than \(\tau(x)\).

Suppose \(F\) is a Hall witness which is not an upset. Choose
\(x\in F\), \(y\notin F\) with \(x\preceq_\tau y\), and replace \(x\) by
\(y\). Cardinality is unchanged and (2.2) says that the neighborhood cannot
grow. The sum of the ranks of the selected targets strictly increases.
Iteration therefore terminates at an upset with at least the original
deficiency. This proves the first assertion.

Put

\[
                         \delta(F)=|F|-|N(F)|.
\]

Neighborhoods obey

\[
 N(A\cup B)=N(A)\cup N(B),\qquad
 N(A\cap B)\subseteq N(A)\cap N(B),
\]

so \(\delta\) is supermodular:

\[
 \delta(A)+\delta(B)\le\delta(A\cup B)+\delta(A\cap B). \tag{2.3}
\]

Consequently maximum-deficiency witnesses are closed under union and
intersection. If \(F\) is an upset maximizer, every translate \(gF\) is
another. Repeatedly unioning all translates preserves maximal deficiency
and produces a \(G\)-invariant upset. \(\square\)

### Corollary 2.2 (exposed-root form)

For an upset \(U\), let

\[
 R_\tau(U)=
 \{y\in U:\text{there is no }x\in U
          \text{ with }x\subsetneq y,\ \tau(x)<\tau(y)\}.      \tag{2.4}
\]

Let \(\Gamma_r(U)\) be the owner shadow of \(U\). Then Hall for every
upset is equivalent to

\[
                         |R_\tau(U)|\le|\Gamma_r(U)|
                         \qquad\text{for every upset }U.       \tag{2.5}
\]

#### Proof

Every target neighbor of an upset lies inside that upset. Its target
neighborhood is exactly \(U\setminus R_\tau(U)\), while its owner
neighborhood is \(\Gamma_r(U)\). Cancelling
\(|U\setminus R_\tau(U)|\) from Hall gives (2.5). \(\square\)

For a pointwise fixed core \(H\), types are \((A,j)\) of weight
\(\binom{k-|H|}{j}\). The invariant upset relation is exactly

\[
 A\subseteq B,\quad j\le\ell,\quad
 |A|+j<|B|+\ell,\quad \tau(A,j)\le\tau(B,\ell).       \tag{2.6}
\]

Thus Theorem 7.3 is equivalent to weighted exposed-root inequalities only
on chronological product-order upsets.

## 3. Terminal cancellation and orbit exchanges

### Lemma 3.1 (top cancellation)

Let

\[
 Q={ [k]\choose r-2},\qquad
 R={ [k]\choose r-1},\qquad
 O={ [k]\choose r},
 \qquad |O|=W.
\]

For \(F\subseteq Q\), let

\[
 \Gamma_\tau(F)=
 \{T\in R:\exists S\in F,\ S\subset T,\ \tau(S)<\tau(T)\}.
\]

Every saturating successor matching must satisfy

\[
 |F|\le W-|R|+|\Gamma_\tau(F)|.                     \tag{3.1}
\]

For odd \(k\), \(|R|=W\), so this becomes the sharp oriented-shadow law

\[
                         |F|\le|\Gamma_\tau(F)|.     \tag{3.2}
\]

#### Proof

Apply Hall to \(R\cup F\). The complete top target rank sees every owner
and no target. Its owner neighborhood is all \(W\) owners. The only extra
right targets are \(\Gamma_\tau(F)\). \(\square\)

At the final two ranks of a pointwise-core quotient, a top type
\(v=(B,\ell)\) has predecessor menu

\[
 \operatorname {Pred}(v)
 =\{(B,\ell-1)\}
  \cup\{(B-\{b\},\ell):b\in B\},                    \tag{3.3}
\]

with inadmissible boundary types omitted.

Fix one boundary source time \(t\). Suppose top type \(q\) is later than
\(t\), top type \(p\) is not, and all types in a source family \(F\) have
time \(t\). Swap only the two sides of \(p,q\). The later-shadow capacity
of \(F\) changes by exactly

\[
 |p|\mathbf1_{F\cap\operatorname {Pred}(p)\ne\varnothing}
 -
 |q|\mathbf1_{F\cap\operatorname {Pred}(q)\ne\varnothing}.   \tag{3.4}
\]

Apart from the vacuous empty-menu case, the swap is nonworsening for
**every** \(F\) if and only if

\[
 \operatorname {Pred}(q)\subseteq\operatorname {Pred}(p),
 \qquad |p|\ge|q|.                                   \tag{3.5}
\]

Indeed, (3.5) makes every nonzero negative indicator in (3.4) accompany a
positive indicator of at least the same weight. Conversely, a predecessor
in \(\operatorname {Pred}(q)\setminus\operatorname {Pred}(p)\) gives a
negative singleton witness; after menu containment, a common predecessor
gives a negative singleton witness whenever \(|p|<|q|\).

Thus (3.5) classifies swaps which are universally safe for this terminal
shadow face; it is not a global-Hall exchange theorem. The predecessor
menus of distinct interior nonempty core types are
inclusion-incomparable. The only generic distinct nesting is the
empty-core/singleton-core boundary move. To see this, the vertical
predecessor of a top type \(C\) can lie in the menu of \(B\) only when
\(C=B\) or \(C=B-\{b\}\). In the latter case, if \(C\ne\varnothing\), a
horizontal predecessor \(C-\{c\}\) has outside count one larger than every
horizontal predecessor of \(B\), a contradiction. Boundary menus give only
the stated empty/singleton exception. Hence no Ferrers-style sequence of
universally safe local swaps can prove the adaptive theorem; useful swaps
must respond to the current Hall witness.

### Lemma 3.2 (local horizontal-cover law)

Fix an outside ground set of size \(m\). Suppose every source core type
\(A\in{H\choose a}\) has outside size \(j\), its later vertical type
\((A,j+1)\) is present, and the later horizontal types are
\((B,j)\) for \(B\in\mathcal B\subseteq{H\choose a+1}\). Put

\[
 q={m\choose j},\qquad q_+={m\choose{j+1}}.
\]

Hall on this two-face is exactly

\[
 |N_{\mathcal B}(F)|
 \ge \left(1-{q_+\over q}\right)_+|F|
 \qquad(F\subseteq{H\choose a}).                    \tag{3.6}
\]

If the coefficient is positive, singleton cuts force
\(\mathcal B\) to cover every \(a\)-set. Conversely, a covering design is
sufficient whenever the coefficient is at most \(1/(a+1)\).

#### Proof

Every selected source type has a private vertical target of mass \(q_+\).
Its horizontal target types have mass \(q\) and are indexed exactly by
\(N_{\mathcal B}(F)\). Thus Hall is
\(q|F|\le q_+|F|+q|N_{\mathcal B}(F)|\), which is (3.6).
If every \(a\)-set is covered, incidence counting gives
\((a+1)|N_{\mathcal B}(F)|\ge|F|\). \(\square\)

## 4. Exact K11 ordering obstruction and repair

Use a pointwise core of size five and six outside coordinates. Ascending
binary-mask next fit has loads

\[
                         461,\quad457,\quad105
\]

against \(W=462\). Let the core pair be mask \(10001\), and let

\[
 F=\{S\in{[11]\choose4}:10001\subseteq S\}.
\]

All \(36=\binom92\) members of \(F\) occur at the middle time. Their later
rank-five shadow has core masks

\[
 10111,\ 11001,\ 11011,\ 11101,\ 11111
\]

and total mass

\[
                         6+15+6+6+1=34.
\]

Adding the complete rank-five source layer to \(F\) gives supply
\(462+36\) and neighborhood \(462+34\). This is an exact global Hall
deficit two. The ordinary upper shadow of the same principal star has size
\(\binom93=84\); chronology, not Kruskal--Katona expansion, deletes the
needed capacity.

Ordering by decreasing core size fails for **every** within-size
tie-break. Greedy leaves only two core-pair top orbits at the final time.
They cover at most four of the five core points. For an uncovered point
\(c\), the source orbit \((4,\{c\},3)\) has mass \(20\), while its sole
later top neighbor has mass \(15\). Top cancellation gives deficit at
least five.

This obstruction is sharp in that order class. Close the middle block one
pair orbit early and leave three terminal pair orbits forming an edge
cover, for example

\[
                         \{01,02,34\}.
\]

The loads become

\[
                         446,\quad436,\quad141.
\]

An exact pointwise-core type flow saturates all \(561\) sources below rank
five; the complete rank-five source layer then matches the \(462\) owners.
The independently replayed target usages, grouped by rank and core size,
are

\[
 15/15,\ 100/100,\ 6/6,\ 75/75,\ 200/200,\
 150/150,\ 15/30.
\]

Biregular orbit lifting and bipartite integrality give an unconditional
K11 anchored factor of depth three. Three terminal pair orbits are
necessary and sufficient on this face, so the repair is exactly one orbit
of deliberate underfill relative to greedy.

## 5. Full staircase obstructions to deterministic next fit

### Theorem 5.1 (K41 ascending-mask staircase)

At K41, \(d=5,h=6,n=35\), and the quantitative capacity hypothesis

\[
                         6{35\choose17}\le W-{6\choose2}
\]

holds. Ascending binary-mask next fit has block boundaries

\[
\begin{array}{c|c}
0&[1,16]+(17,0{:}9)\\
1&(17,10{:}63)+(18,0{:}42)\\
2&(18,43{:}63)+(19,0{:}53)\\
3&(19,54{:}63)+(20,0{:}55)\\
4&(20,56{:}63).
\end{array}                                         \tag{5.1}
\]

For a valid type \((s,A)\), put \(w_s(A)=\binom{35}{s-|A|}\), and define

\[
\begin{split}
 U={}&\{(s,A):A\ge43\}\\
 &{}\cup\{(s,A):17\le s\le20,\ 10\le A\le42\}\\
 &{}\cup\{(s,A):19\le s\le20,\ 0\le A\le9\}.
\end{split}                                         \tag{5.2}
\]

Its target neighborhood is exactly

\[
\begin{split}
 V={}&\{(s,A):s=17,18,\ A\ge43\}\\
 &{}\cup\{(19,A):A\ge10\}
 \cup\{(20,A):0\le A\le63\}.
\end{split}                                         \tag{5.3}
\]

Every owner is also a neighbor. Direct binomial summation gives

\[
 |U|=827\,279\,041\,974,\qquad
 |V|=551\,490\,893\,730,\qquad
 W=269\,128\,937\,220,
\]

and hence the exact deficiency

\[
                         |U|-|V|-W=6\,659\,211\,024. \tag{5.4}
\]

The identity \(N(U)=V\dot\cup\mathcal O\) follows directly from the block
boundaries and the fact that bitwise containment \(A\subseteq B\) implies
the numeric inequality \(A\le B\). Every displayed target type has an
earlier same-mask or two-rank predecessor in \(U\).

At K121 the same deterministic chronology uses exactly \(d=7\) capacity
blocks but has an explicit chronological-upset staircase deficit

\[
            26\,797\,240\,071\,313\,150\,869\,734\,178\,805\,578\,123.
                                                               \tag{5.5}
\]

Thus deterministic ascending-mask next fit fails at the first dimension
where consecutive whole-rank packing needs \(d+2\). These finite examples
refute that specified ordering, not the asymptotic existence of another
adaptive chronology.

## 6. A global-flow repair beyond adjacent normalization

### Theorem 6.1 (K121 fresh-collar factor)

At K121, pack ranks \(1,\ldots,54\) by ascending-mask next fit into two
blocks, then put each complete rank \(55,\ldots,60\) in its own block. The
eight loads are

\[
\begin{split}
&(191515934355274481024720542180047276,\\
&174358503665531262687919312008666465,\\
&117118180539414377821494470432491764,\\
&138032141350024088146761340152579579,\\
&157405073469325714553324335261713555,\\
&173688356931669753989875128564649440,\\
&185463838757545669514612425416490080,\\
&191645966716130525165099506263706416).
\end{split}                                         \tag{6.1}
\]

Every load is at most \(W\). The exact pointwise-core global type flow
saturates all

\[
                         \Lambda=2^{120}-1
\]

target supply. Therefore Theorem 7.3 gives \(W\) owner-anchored chains of
target depth at most

\[
                         8=d(121)+1.                 \tag{6.2}
\]

This is strictly beyond the adjacent normalized-coupling architecture.
Let \(P_1\) be the second mixed block and \(Q\) the complete rank 55. Fix
the four-core mask \(60\), and let \(F\subseteq P_1\) consist of all
rank \(52,53,54\) sets containing it. Then

\[
\begin{aligned}
 |P_1|&=174358503665531262687919312008666465,\\
 |Q|&=117118180539414377821494470432491764,\\
 |F|&=8079411654070705698938643146427216,\\
 |N_Q(F)|&=4701802627992053429782646936799222.
\end{aligned}
\]

The normalized-Hall cross-product deficit is

\[
126446722006344481489756434267928807640207597129283355999945275958794
>0.                                                   \tag{6.3}
\]

Thus \(P_1\to Q\) has no uniform coupling, while the global flow succeeds
by skipping blocks.

The audit uses a second, sparse encoding of the complete type graph: for
each source time, copy the product-order Hasse DAG, inject each source at
its type node, and expose only later target nodes and owner nodes. Hasse
paths are exactly fixed-core comparabilities, so this sparse network is
equivalent to the dense type flow. It independently returns value
\(\Lambda\).

## 7. Balanced setwise-core alternative

Preserving a balanced core setwise gives types \((i,j)\) of mass
\(\binom hi\binom{k-h}j\), only \(O(k^2)\) types, and the exact product
order. The companion theorem

`MATH_THEOREM_BALANCED_SETWISE_CORE_CAPACITY_AND_SERPENTINE_HALL_OBSTRUCTION_20260802.md`

proves unconditionally

\[
 \text{number of intact-orbit next-fit blocks}
 \le\left\lceil{\Lambda\over W}\right\rceil+4
 \le d(k)+5.                                         \tag{7.1}
\]

It also proves the terminal aperture law and the general boundary
staircase inequality

\[
 |A|+\binom{k}{s}+\binom{k}{s+1}
 \le|\partial^+P|+W.                                \tag{7.2}
\]

Fixed serpentine and monotone orders fail at K9 and K19. Even separating
the complete top target rank leaves an interior deficit
\(64\,633\,068\,796\) at K46. A witness-dependent five-orbit later menu

\[
             \{(11,9),(14,6),(16,4),(18,2),(20,0)\}
\]

repairs the full K46 global flow with four blocks and no extra capacity
block. This is an unconditional K46 anchored factor and an exact example
of min-cut-aware adaptive orbit ordering.

## 8. Exact remaining hypothesis

The surviving all-\(k\) statement may now be written without arbitrary
Hall subsets:

> **UNPROVED adaptive chronological-upset expansion.** There is an absolute
> \(C\) such that, for every \(k\), some fixed-core orbit chronology with
> at most \(d(k)+C\) capacity blocks satisfies
> \[
>                   |R_\tau(U)|\le|\Gamma_r(U)|
> \]
> for every invariant chronological product-order upset \(U\).

By Theorem 2.1 and Corollary 2.2, this is exactly equivalent to the global
Hall clause, not stronger. The K11, K46, and K121 repairs close finite
instances only. The K41/K121 staircases show that capacity, ordinary
Kruskal--Katona shadow expansion, terminal aperture, and universally safe
local swaps do not prove it.

Any all-\(k\) depth-\(d+C\) anchored factor would advance the near-uniform
Boolean chain-decomposition frontier. It would still not supply literal
overlap serialization, endpoint aperture on a physical host, global
address/history propagation, residence, upper/common-cap closure, compiler
closure, or cross-depth regeneration. Every such physical statement
remains **unproved** here.

## 9. Replay

Run

    python3 scratch/audit_fixed_core_nextfit_order_20260802.py \
      --analytic-witnesses --k41-flow-audit --k121-positive

and

    python3 scratch/audit_balanced_setwise_core_serpentine_flow_20260802.py

The first script independently reproduces the reported ascending-mask
deficiencies at K17, K21, and K23; verifies the K11 cuts and adaptive
repairs; proves the analytic K41 and K121 staircase cuts; and checks the
K121 fresh-collar factor through the sparse product-DAG flow. The second
checks the balanced-core capacity theorem, terminal and interior cuts, and
the adaptive K46 repair.
