# Chronological root width, monotone rank refinement, and the K41 three-cut gate

**Date:** 2026-08-02  
**Status:** unconditional root-width bound and monotone refinement theorem;
exact scoped K41 minimum-three-cut result.  The all-\(k\)
\(d(k)+O(1)\) adaptive chronology remains **unproved**.

## 0. Outcome

For a containment-monotone chronology, exposed roots in different time
blocks are mutually incomparable.  Taking a largest antichain from each
same-time root bank therefore gives one global antichain.  This yields the
exact useful bound

\[
 |R_\tau(U)|-|\Gamma_R(U)|
 \le \sum_t\bigl(|R_t|-\operatorname {width}(R_t)\bigr).       \tag{0.1}
\]

Consequently every Hall failure contains two comparable roots in one time
block.  Splitting that block between their ranks is a pure refinement: it
removes no successor arc and strictly decreases that witness.  Under the
stronger hypothesis that the whole chronology is globally rank ordered,
repeating this operation reaches Hall after at most one split at each rank
boundary.

This is an unconditional repair theorem, but it is not a
\(d+O(1)\) theorem.  The K41 ascending-mask chronology makes the
quantitative obstruction exact: no refinement by at most two global rank
cuts has Hall, while cuts at ranks \(17,18,19\) give a saturating depth-eight
flow.  Thus this frozen \(d=5\) chronology needs exactly three pure rank
cuts.  This does not lower-bound arbitrary adaptive orbit menus.

## 1. Definitions

Put \(R=\lceil k/2\rceil\) and \(r=R-1\).  Let \({\cal T}\) be the
nonempty targets of ranks at most \(r\), and let \({\cal O}\) be the
middle rank-\(R=r+1\) owners.  The middle-rank hypothesis is used when an
antichain is lifted to distinct owners.  A chronology
\(\tau:{\cal T}\to\{0,\ldots,q-1\}\) is

- **containment-monotone** if
  \[
                         x\subsetneq y\Longrightarrow
                         \tau(x)\le\tau(y);                    \tag{1.1}
  \]
- **globally rank ordered** if
  \[
                         |x|<|y|\Longrightarrow
                         \tau(x)\le\tau(y)                     \tag{1.2}
  \]
  for all targets, comparable or not.

The second condition is strictly stronger.  This distinction is
load-bearing in the block-count corollary below.

For a chronological upset \(U\), write

\[
 R_t=R_\tau(U)\cap\tau^{-1}(t).                    \tag{1.3}
\]

All cardinalities in this note are vertex cardinalities.  The same
statements apply to an invariant orbit quotient after expanding orbit
weights to vertices.

## 2. The root-width inequality

### Theorem 2.1 (same-time width controls all Hall deficiency)

If \(\tau\) is containment-monotone, then every chronological upset \(U\)
satisfies

\[
 |R_\tau(U)|-|\Gamma_{r+1}(U)|
 \le \sum_t\bigl(|R_t|-\operatorname {width}(R_t)\bigr).       \tag{2.1}
\]

In particular, if Hall fails for \(U\), some bank \(R_t\) is not an
antichain and hence contains comparable roots \(x\subsetneq y\).

#### Proof

If \(t<u\), no member of \(R_t\) is comparable with a member of \(R_u\).
Indeed, \(x\in R_t\), \(y\in R_u\), and \(x\subsetneq y\) would make
\(y\) non-root because \(x\) is strictly earlier.  The reverse containment
\(y\subsetneq x\) contradicts containment monotonicity.

Choose a largest antichain \(A_t\subseteq R_t\) and put
\(A=\bigcup_tA_t\).  The preceding paragraph shows that \(A\) is an
antichain.  A symmetric-chain decomposition of the Boolean lattice maps
each member of \(A\) upward along its chain to a distinct rank-\(r+1\)
owner.  Hence

\[
 |\Gamma_{r+1}(U)|\ge |\Gamma_{r+1}(A)|\ge |A|
 =\sum_t\operatorname {width}(R_t).                 \tag{2.2}
\]

Subtract (2.2) from
\(|R_\tau(U)|=\sum_t|R_t|\) to obtain (2.1).  If every \(R_t\) were an
antichain, the right side would be zero and Hall could not fail. \(\square\)

The bound need not be an equality.  It isolates the only possible source
of deficiency: comparable roots which remain co-timed.

## 3. Pure rank refinement

### Theorem 3.1 (one-block rank-refinement exchange)

Assume only containment monotonicity.  Let a failed upset \(U\) contain
comparable exposed roots \(x\subsetneq y\) at time \(t\), and choose

\[
                         |x|\le a<|y|.                         \tag{3.1}
\]

Replace the old time block \(P_t\) by

\[
 P_t^-:=\{z\in P_t:|z|\le a\},\qquad
 P_t^+:=\{z\in P_t:|z|>a\},                         \tag{3.2}
\]

in that order, omitting an empty piece and shifting later time labels.
Then:

1. every old successor arc remains and only new arcs are added;
2. the maximum Hall deficiency cannot increase;
3. \(U\) remains a chronological upset; and
4. the exposed-root deficiency of this fixed \(U\) strictly decreases.

#### Proof

All old inter-block time comparisons are unchanged.  There was no target
successor arc within \(P_t\); after (3.2), the only new arcs run from
\(P_t^-\) to comparable members of \(P_t^+\).  This proves 1, and 2 follows
because adding right-neighborhood arcs cannot worsen Hall.

The weak-time chronological containment relation already contained every
same-time comparable pair in \(P_t\).  Refinement preserves those order
relations, so every old upset, including \(U\), remains an upset.  Finally,
\(x\) is now strictly earlier than \(y\), so \(y\) is no longer exposed.
Adding predecessor arcs creates no new root.  The owner shadow of the fixed
set \(U\) is unchanged, proving 3--4. \(\square\)

### Corollary 3.2 (finite rank-layer fallback)

If the initial chronology is globally rank ordered, repeated application
of Theorem 3.1 reaches a Hall chronology after at most \(r-1\) added time
blocks.  Thus an initial \(q\)-block chronology has a pure refinement with
at most \(q+r-1\) blocks and a saturating successor matching.

#### Proof

Under global rank order, a boundary between ranks \(a\) and \(a+1\) lies
inside at most one time block.  Once that block is split, the same boundary
can never occur inside a block again.  There are \(r-1\) boundaries among
the nonempty target ranks \(1,\ldots,r\).

If Hall still fails, Theorem 2.1 supplies a same-time comparable pair and
therefore an unsplit intervening rank boundary.  After all required splits,
every time block lies in one rank, so every root bank is an antichain and
Theorem 2.1 gives Hall. \(\square\)

The \(q+r-1\) conclusion is false under containment monotonicity alone:
one rank boundary may cross several time blocks.  The single-block exchange
remains valid there, but this block-count argument does not.

## 4. Exact K41 three-cut gate

Use the certified K41 pointwise-core chronology with a six-point fixed core,
ascending binary masks, outside size \(35\), owner capacity

\[
 W={41\choose20}=269\,128\,937\,220,\qquad d=q=5.     \tag{4.1}
\]

Its five blocks occupy the rank intervals

\[
 [1,17],\ [17,18],\ [18,19],\ [19,20],\ [20,20].     \tag{4.2}
\]

A **pure global rank-cut refinement** is the chronology obtained by choosing
a set \(C\subseteq\{1,\ldots,19\}\) and replacing each old block by its
nonempty consecutive pieces cut after the ranks in \(C\).  No orbit is
otherwise reordered.

### Theorem 4.1 (three cuts are necessary and sufficient on the frozen face)

Every pure global rank-cut refinement with \(|C|\le2\) fails Hall.  The
choice

\[
                              C=\{17,18,19\}                    \tag{4.3}
\]

has eight blocks, all of capacity at most \(W\), and its exact successor
flow saturates all

\[
                              \Lambda=2^{40}-1                 \tag{4.4}
\]

targets.  Therefore the minimum number of pure rank cuts for this frozen
chronology is exactly three, giving depth \(d+3=8\).

#### Proof of necessity

There are three exhaustive cases.

1. If rank boundary \(19\) is not cut, the four rank-19 mask types
   \(54,55,62,63\), together with the complete rank-20 source layer, give
   supply and neighborhood
   \[
   278\,493\,136\,980>274\,696\,839\,780,
   \]
   an exact deficit \(3\,796\,297\,200\).
2. If \(19\) is cut but \(18\) is not, the rank-18 mask suffix
   \(43,\ldots,63\), the corresponding rank-19 suffix, and the complete
   rank-20 layer give
   \[
   385\,669\,193\,010>379\,261\,255\,860,
   \]
   an exact deficit \(6\,407\,937\,150\).
3. With at most two cuts, the only remaining possibility is
   \(C=\{18,19\}\).  The published K41 chronological staircase survives
   with supply
   \(827\,279\,041\,974\), neighborhood
   \(820\,619\,830\,950\), and deficit
   \(6\,659\,211\,024\).

Cuts at other rank boundaries do not change the displayed local time
comparisons.  The companion audit additionally replays every zero-, one-,
and two-cut choice through the independent sparse product-Hasse network.

#### Proof of sufficiency

For (4.3), the eight exact loads are

\[
\begin{split}
&(268\,111\,914\,795,
115\,495\,464\,960,
152\,717\,220\,450,
49\,395\,420\,150,\\
&\quad216\,854\,793\,210,
27\,807\,876\,990,
240\,347\,793\,840,
28\,781\,143\,380).
\end{split}                                                    \tag{4.5}
\]

All are at most \(W\).  The dense containment network and the independently
encoded sparse product-Hasse network both return flow \(\Lambda\).  Orbit
biregularity and bipartite integrality lift the type flow to a vertex
matching. \(\square\)

Theorem 4.1 proves neither that arbitrary K41 chronologies require eight
blocks nor that an all-\(k\) constant must be at least three.  It is a sharp
obstruction only for pure rank cuts of the frozen ascending-mask order.

## 5. Exact remaining hypothesis

Theorems 2.1--3.1 identify the quantitative replacement for unrestricted
rank splitting:

> construct a constant-size root-chain breaker--global rank cuts or
> capacity-neutral orbit menus--which meets every deficient exposed-root
> bank.

The K11 edge-cover menu, K46 five-orbit menu, and K121 fresh collar are
finite examples of such breaking mechanisms.  K41 proves that one or two
pure cuts are not a universal repair even for one certified chronology.
No argument here bounds the number of breakers independently of \(k\).

Still **unproved** are the all-\(k\) \(d+C\) chronology, the anchored
\(d+C\) chain factor, and every literal serialization, protected-host,
address/history, residence, compiler, and regenerative conclusion.

## 6. Replay

Run

```text
python3 scratch/audit_k41_rank_refinement_gate_20260802.py
```

The audit reconstructs the frozen K41 chronology, verifies the three
explicit cut sums, exhausts all refinements using at most two rank cuts,
and checks the three-cut repair with both dense and sparse exact flows.
