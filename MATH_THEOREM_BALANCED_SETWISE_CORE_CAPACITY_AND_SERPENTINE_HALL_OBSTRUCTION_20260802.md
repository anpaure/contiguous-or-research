# Balanced setwise-core capacity and the serpentine Hall obstruction

**Date:** 2026-08-02  
**Status:** unconditional all-\(k\) \(d+O(1)\) capacity chronology on a
two-dimensional orbit quotient; exact Hall counterexamples to the canonical
diagonal serpent and to monotone diagonal order; and an exact adaptive
five-orbit K46 repair.  No adaptive all-\(k\) chain factor is claimed.

## 0. Verdict

Let

\[
 h=\lfloor k/2\rfloor,\qquad \ell=k-h,
 \qquad r=\lfloor(k-1)/2\rfloor,
 \qquad W={k\choose\lfloor k/2\rfloor},
\]

and preserve a fixed \(h\)-set \(H\) **setwise**.  The strict-lower orbit
types are

\[
 {\cal O}_{i,j}=\{S:|S\cap H|=i,\ |S\setminus H|=j\},
 \qquad 1\le i+j\le r,                              \tag{0.1}
\]

with mass

\[
                    q_{i,j}={h\choose i}{\ell\choose j}.       \tag{0.2}
\]

There are only \((h+1)(\ell+1)=O(k^2)\) types, and containment is exactly
the product order

\[
                    (i,j)\preceq(i',j')
          \quad\Longleftrightarrow\quad i\le i',\ j\le j'.    \tag{0.3}
\]

Packing the whole types by next fit, in *any* order for \(k\ge9\), uses at
most

\[
             \left\lceil {\Lambda\over W}\right\rceil+4       \tag{0.4}
\]

capacity blocks, where

\[
                    \Lambda=\sum_{s=1}^r{k\choose s}.          \tag{0.5}
\]

The same bound holds for the canonical rank-diagonal serpent at the small
dimensions by direct evaluation.  Since the established deadline
parameters obey

\[
             \left\lceil\Lambda/W\right\rceil\le d(k)+1,
\]

this is an unconditional \(d(k)+5\) capacity chronology.

Capacity is not Hall.  For the canonical serpent---increasing total rank,
and increasing \(i\) on odd diagonals but decreasing \(i\) on even
diagonals---the first failed global type flow is already \(k=9\).  Its
three loads are

\[
                              125,125,5                         \tag{0.6}
\]

against \(W=126\), but one exact terminal Hall set has supply \(130\) and
only the \(126\) owners as neighbors.  Thus the deficit is \(4\).

Changing to monotone increasing diagonals only postpones the same defect:
at \(k=19\), a terminal Hall set has supply \(92\,378+1\,125\) and owner
capacity \(92\,378\).  Therefore neither aggregate capacity nor a fixed
endpoint convention proves Theorem 7.3's all-\(k\) Hall clause.

## 1. Orbit scale

Put

\[
 c_n={n\choose\lfloor n/2\rfloor},\qquad
 M=c_hc_\ell,qquad
 q={\Lambda\over W},\qquad \delta={M\over W}.         \tag{1.1}
\]

Every orbit in (0.1) has mass at most \(M\).

### Lemma 1.1 (exact coarse bounds)

For \(k\ge9\),

\[
                 \delta\le {10\over21},
                 \qquad q\delta<2.                    \tag{1.2}
\]

#### Proof

The central-binomial recurrences

\[
 c_{2a+1}={2a+1\over a+1}c_{2a},
 \qquad c_{2a+2}=2c_{2a+1}                            \tag{1.3}
\]

give

\[
 \delta_{2a}={c_a^2\over c_{2a}},
 \qquad
 \delta_{2a+1}={c_ac_{a+1}\over c_{2a+1}}.           \tag{1.4}
\]

The local peaks occur at the pairs \(2a+1,2a+2\) with \(a\) odd.
Consecutive such peaks have ratio

\[
 {4(a+2)^3\over(a+3)(2a+3)(2a+5)}<1,                \tag{1.5}
\]

because the denominator minus the numerator is
\(4a^2+15a+13\).  Direct evaluation at \(k=9,10,11,12\) then gives

\[
 \sup_{k\ge9}\delta_k=\delta_9={60\over126}={10\over21}.
\]

The elementary Wallis bounds

\[
 {2^n\over\sqrt{2n}}\le c_n\quad(n\ge6),
 \qquad
 c_n\le {2^n\over\sqrt{n+1}}\quad(n\ge1)            \tag{1.6}
\]

give, since \(h,\ell\ge3\),

\[
 M\le {2^k\over\sqrt{(h+1)(\ell+1)}},
 \qquad
 W\ge {2^k\over\sqrt{2k}}.                          \tag{1.7}
\]

Also \(\Lambda<2^{k-1}\).  Hence

\[
 q\delta={\Lambda M\over W^2}
 <{k\over\sqrt{(h+1)(\ell+1)}}<2,                   \tag{1.8}
\]

because \((h+1)(\ell+1)>k^2/4\).  This proves (1.2).
\(\square\)

### Theorem 1.2 (balanced setwise-core capacity)

For \(k\ge9\), next-fit packing of the intact orbit types in any order uses
at most \(\lceil\Lambda/W\rceil+4\) blocks.  In particular the canonical
diagonal serpent has depth at most \(d(k)+5\).

#### Proof

If next fit produces \(b\) nonempty blocks, each of the first \(b-1\)
blocks has load greater than \(W-M\).  Therefore

\[
 b-1<{\Lambda\over W-M}
 ={q\over1-\delta}
 =q+{q\delta\over1-\delta}
 <q+{42\over11},                                     \tag{1.9}
\]

where Lemma 1.1 was used in the last step.  Since \(b\) is integral,

\[
                       b\le\lceil q\rceil+4.         \tag{1.10}
\]

The dimensions \(3\le k\le8\) have respectively at most
\(1,1,2,2,2,2\) next-fit blocks under every rank-respecting type order;
thus they also satisfy (1.10).  The deadline consequence follows from
\(\lceil q\rceil\le d(k)+1\).  \(\square\)

The estimates are at the correct scale:

\[
 {M\over W}\sim\sqrt{8\over\pi k},
 \qquad
 {\Lambda\over W}\sim\sqrt{\pi k\over8},
 \qquad
 {\Lambda M\over W^2}\longrightarrow1.              \tag{1.11}
\]

Thus the balanced setwise core is a critical-granularity construction:
its largest item is \(\Theta(W/d)\), enough for \(d+O(1)\) capacity but
without the large slack used in the logarithmic pointwise-core
\(d+1\)-block theorem.

## 2. Exact terminal aperture

The finite obstruction below is an instance of a general necessary Hall
condition.

### Lemma 2.1 (terminal owner-aperture inequality)

Let \(\tau\) be any chronology of the strict-lower orbit types, and let
\(Z_\tau\) be the union of all types below rank \(r\) which have no
strictly later comparable target type.  If the global successor graph has
a matching saturating its left shore, then

\[
                 |Z_\tau|\le W-{k\choose r}.          \tag{2.1}
\]

Consequently, when \(k=2a+1\) is odd, \(Z_\tau\) must be empty.  In
particular every penultimate type obeys the exact aperture disjunction

\[
\begin{split}
 &\tau(i,a-i)>\tau(i,a-1-i)\\
 &\hspace{22mm}\text{or}\quad
 \tau(i+1,a-1-i)>\tau(i,a-1-i),
 \qquad 0\le i<a.                                    \tag{2.2}
\end{split}
\]

Thus the later rank-\(a\) types must hit the relevant edges
\(\{i,i+1\}\) of the type path.  When \(k=2a\) is even, (2.1) permits only

\[
              W-{2a\choose a-1}={W\over a+1}          \tag{2.3}
\]

units of unexposed lower mass.

#### Proof

Let \(R\) be the complete rank-\(r\) target layer.  No source in \(R\) has
a target successor, and \(Z_\tau\) has none by definition.  Hence
\(R\cup Z_\tau\) has right-neighborhood contained in the owner layer.
The complete layer \(R\) sees every owner, so that neighborhood has total
capacity exactly \(W\).  Hall gives

\[
                  {k\choose r}+|Z_\tau|\le W,
\]

which is (2.1).  For odd \(k\), \({k\choose r}=W\).  A penultimate type
\((i,a-1-i)\) has precisely the two rank-\(a\) upper types displayed in
(2.2), proving the disjunction.  Formula (2.3) follows from
\({2a\choose a-1}=aW/(a+1)\).  \(\square\)

This lemma is only a terminal cut.  Satisfying it does not imply the
interior Hall inequalities.

## 3. The exact K9 serpent obstruction

At \(k=9\), take \(h=4\), \(\ell=5\), \(r=4\), and \(W=126\).  Traverse
the types by increasing \(s=i+j\), increasing \(i\) for odd \(s\), and
decreasing \(i\) for even \(s\).  Next fit gives

\[
\begin{array}{c|l|c}
\text{block}&\text{last relevant types}&\text{load}\\ \hline
0&(0,3),(1,2),(2,1)&125\\
1&(3,0),(4,0),(3,1),(2,2),(1,3)&125\\
2&(0,4)&5.
\end{array}                                           \tag{3.1}
\]

Let \(X\) consist of all rank-four source types together with the rank-three
type \((3,0)\).  The rank-four sources have no later target type.  The only
rank-four strict supersets of \((3,0)\) are \((4,0)\) and \((3,1)\), both
in its own block; the only later type \((0,4)\) is incomparable.  Hence
\(X\) has no right-target neighbor.  All its remaining neighbors lie in
the rank-five owner layer, whose total capacity is \(W=126\).  But

\[
 |X|_q={9\choose4}+q_{3,0}
      =126+{4\choose3}{5\choose0}
      =130.                                           \tag{3.2}
\]

This is a literal Hall violation of size four.  It is an endpoint-aperture
failure: the full top target rank already consumes the complete owner
capacity, while \((3,0)\) has no exposed later root.

The exact type max-flow has value \(251<\Lambda=255\), so the exhibited
cut is also minimum.  Minimum-cut optimality is independently replayed by
the audit script; the nonexistence conclusion needs only (3.2).

## 4. Fixed endpoint direction also fails

Order every diagonal by increasing \(i\).  At \(k=19\), where
\(h=9\), \(\ell=10\), \(r=9\), next fit has loads

\[
                         87\,637, 86\,863, 87\,643. \tag{4.1}
\]

In the second block lie the rank-eight types \((0,8),(1,7)\) and all of
their rank-nine upper types

\[
 (0,9),(1,8),(2,7).                                  \tag{4.2}
\]

The later rank-nine suffix begins at \((3,6)\), so neither lower type has
a later comparable target.  Take \(X\) to be these two types together with
the complete rank-nine source layer.  Again its only neighbors are owners,
of total capacity

\[
                            W={19\choose9}=92\,378.   \tag{4.3}
\]

Its supply is

\[
 W+{9\choose0}{10\choose8}+{9\choose1}{10\choose7}
 =W+45+1\,080=W+1\,125.                              \tag{4.4}
\]

Thus monotone increasing diagonal order fails Hall by \(1\,125\).
Reversing every diagonal has the symmetric endpoint problem (the exact
type flow deficiency is \(4\,149\)).

## 5. Separating the top rank is not sufficient

There is a canonical repair of Lemma 2.1: pack ranks \(1,\ldots,r-1\),
close the current block, and put the complete rank-\(r\) target layer in
one final block.  Every lower type then has a later comparable rank-\(r\)
type, so \(Z_\tau=\varnothing\).

### Lemma 5.1 (boundary-staircase Hall inequality)

Let \(L_u\) denote the complete rank-\(u\) target layer.  Suppose that, at
one consecutive pair of chronology times, the following configuration
occurs:

* \(P\subseteq L_s\) and \(A\subseteq L_{s-1}\) are at the earlier time;
* every rank-\(s\) upper type of every type in \(A\) belongs to \(P\); and
* \(L_s\setminus P\) and the complete layer \(L_{s+1}\) are at the later
  time.

Write \(\partial^+P\subseteq L_{s+1}\) for the product-order upper shadow
of \(P\).  Global Hall requires

\[
 |A|_q+{k\choose s}+{k\choose{s+1}}
 \le |\partial^+P|_q+W.                              \tag{5.1}
\]

#### Proof

Take as left set

\[
                    X=A\cup L_s\cup L_{s+1}\cup\cdots\cup L_r.
\]

A rank-\(s+1\) target neighbor of \(A\) passes through a rank-\(s\)
upper type in \(P\), and hence lies in \(\partial^+P\).  A source in
\(P\) also has only \(\partial^+P\) as its possible rank-\(s+1\)
neighborhood.  A source in \(L_s\setminus P\) is at the same time as
\(L_{s+1}\), so it has no neighbor there.  All remaining target neighbors
are contained in the complete layers \(L_{s+2},\ldots,L_r\) and the owner
layer.  Therefore

\[
 |N(X)|_q\le |\partial^+P|_q
              +\sum_{u=s+2}^r{k\choose u}+W.
\]

Cancel the common complete upper layers from Hall's inequality for \(X\)
to obtain (5.1).  \(\square\)

This is an actionable orbit-interchange condition: at every such boundary,
an order change must enlarge the weighted shadow of \(P\), reduce the
co-timed mass \(A\), or refine a type.  Terminal aperture alone is the
degenerate top-layer instance.

### Corollary 5.2 (independent later-menu erosion rule)

Assume \(s<\min(h,\ell)\), so the rank-\(s\) types form the path of
vertices

\[
             v_i=(i,s-i),\qquad 0\le i\le s.          \tag{5.2}
\]

Let \(Q=L_s\setminus P\) be the types assigned to the later block.  If
\(Q\) is an independent vertex set of this path, then

\[
 |\partial^+P|_q={k\choose{s+1}}-\varepsilon(Q),      \tag{5.3}
\]

where the only possible erosion is at the two endpoints:

\[
 \varepsilon(Q)
 =\mathbf1_{v_0\in Q}q_{0,s+1}
  +\mathbf1_{v_s\in Q}q_{s+1,0}.                     \tag{5.4}
\]

If \(A_0\subseteq L_{s-1}\) is the family already in the earlier block,
let \(A_Q\) consist of those \((i,s-1-i)\in A_0\) for which neither
\(v_i\) nor \(v_{i+1}\) lies in \(Q\).  Then the boundary-staircase
inequality becomes exactly

\[
                   |A_Q|_q+\varepsilon(Q)
                   \le W-{k\choose s}.                \tag{5.5}
\]

For an earlier-block preload \(L\), the split is capacity-legal whenever

\[
 {k\choose s}+L-W\le |Q|_q
 \le W-{k\choose{s+1}}.                              \tag{5.6}
\]

#### Proof

A rank-\(s+1\) internal type has the two lower path vertices
\(v_{i-1},v_i\).  It is absent from \(\partial^+P\) only if both vertices
belong to \(Q\), which independence forbids.  Each endpoint type has only
one lower path vertex, giving (5.3)--(5.4).  A rank-\(s-1\) type has the
two immediate upper vertices \(v_i,v_{i+1}\), so precisely the types in
\(A_Q\) remain co-timed with all their immediate uppers.  Substitute
(5.3) in Lemma 5.1 to obtain (5.5).  The two inequalities in (5.6) are
exactly \(L+|P|_q\le W\) and
\(|Q|_q+{k\choose{s+1}}\le W\).  \(\square\)

Thus one local adaptive step is a weighted independent-set menu on a path:
hit enough boundary edges while paying only endpoint shadow erosion and
staying in the capacity window.  This criterion controls the cut of
Lemma 5.1 only; it is not a global Hall theorem.

This repair still does not imply global Hall.  Keep increasing \(i\) on
every diagonal below the separated top layer.  The chronology passes the
exact type flow for \(3\le k\le45\), but at \(k=46\) its loads are

\[
 7\,613\,483\,393\,139,\quad
 7\,575\,507\,261\,091,\quad
 7\,988\,294\,956\,851,\quad
 7\,890\,371\,113\,950,                              \tag{5.7}
\]

where \(W={46\choose23}=8\,233\,430\,727\,600\).  The relevant boundaries
are:

* block zero ends with rank-nineteen type \((8,11)\);
* block one starts with \((9,10),(10,9)\) and contains rank-twenty types
  \((i,20-i)\) for \(0\le i\le11\);
* block two contains the remaining rank-twenty types and the complete
  rank-twenty-one layer; and
* block three is the separated rank-twenty-two layer.

Take the left type set

\[
\begin{split}
X={}&\mathcal O_{9,10}\cup\mathcal O_{10,9}
 \cup\bigcup_{i=0}^{20}\mathcal O_{i,20-i}\\
 &\cup\bigcup_{i=0}^{21}\mathcal O_{i,21-i}
 \cup\bigcup_{i=0}^{22}\mathcal O_{i,22-i}.           \tag{5.8}
\end{split}
\]

Its right-target neighborhood is exactly

\[
 \bigcup_{i=0}^{12}\mathcal O_{i,21-i}
 \ \cup\ 
 \bigcup_{i=0}^{22}\mathcal O_{i,22-i},              \tag{5.9}
\]

and it sees the complete rank-twenty-three owner layer.  Indeed, the two
rank-nineteen types have all rank-twenty immediate uppers in their own
block; only the rank-twenty sources with \(i\le11\) have later
rank-twenty-one uppers, yielding precisely the prefix \(0\le i\le12\);
and the later separated rank-twenty-two layer is complete.

Writing

\[
 q_{s,i}={23\choose i}{23\choose s-i},
\]

the supply and neighborhood capacity are respectively

\[
\begin{aligned}
 |X|_q
 &=2q_{19,9}+{46\choose20}+{46\choose21}+{46\choose22}\\
 &=22\,311\,969\,290\,452,\\
 |N(X)|_q
 &=\sum_{i=0}^{12}q_{21,i}+{46\choose22}+{46\choose23}\\
 &=22\,247\,336\,221\,656.
\end{aligned}                                         \tag{5.10}
\]

Thus this endpoint-repaired chronology has the exact interior Hall
deficiency

\[
                         64\,633\,068\,796.           \tag{5.11}
\]

Unlike the K9 and K19 witnesses, this cut has nonempty target-layer
neighborhoods.  It proves that terminal aperture is necessary but not a
sufficient replacement for the global product-order flow.

### Proposition 5.3 (an exact five-orbit K46 repair)

The K46 obstruction is repairable without an extra block.  Keep the same
chronology through rank nineteen and the separated rank-twenty-two layer.
At rank twenty put

\[
 Q=\{(11,9),(14,6),(16,4),(18,2),(20,0)\}             \tag{5.12}
\]

after all other rank-twenty types, in the displayed order.  Next fit puts
the complement \(P=L_{20}\setminus Q\) in block one and \(Q\), together
with the complete rank-twenty-one layer, in block two.  The four exact
loads become

\[
 7\,613\,483\,393\,139,\quad
 7\,430\,698\,757\,713,\quad
 8\,133\,103\,460\,229,\quad
 7\,890\,371\,113\,950,                              \tag{5.13}
\]

all at most \(W=8\,233\,430\,727\,600\).  The exact product-order type
max-flow has value

\[
                         31\,067\,656\,725\,031
                         =\Lambda.                    \tag{5.14}
\]

The menu in (5.12) is independent on the rank-twenty type path.  Its mass
is \(1\,189\,576\,879\,953\), inside the exact capacity window

\[
 386\,844\,910\,066
 \le |Q|_q\le
 1\,289\,904\,147\,324.
\]

Its uncovered earlier-edge mass plus endpoint erosion is
\(1\,266\,390\,681\,039\), below

\[
 W-{46\choose20}=2\,625\,197\,720\,454.
\]

Thus Corollary 5.2 independently verifies that the K46 staircase cut has
been repaired; the full max-flow check verifies all other Hall cuts.

Hence Theorem 7.3's lift gives an unconditional K46 anchored inclusion-
chain factor of depth at most four following this adaptive chronology.

#### Proof

The orbit inventory, block assignment, every compatible type arc, all
source supplies, all right-target and owner capacities, and the integral
maximum flow are reconstructed from binomial coefficients by
`scratch/audit_balanced_setwise_core_serpentine_flow_20260802.py`.  The
replay asserts the five late types in (5.12), the four loads in (5.13), and
equality of the computed flow with the independently summed strict-lower
inventory.  The global orbit-Hall lift then gives the literal matching and
anchored factor.  \(\square\)

This repair is finite evidence for weighted-shadow adaptation, not an
all-\(k\) ordering theorem.

## 6. Consequence and fail-closed boundary

The balanced setwise quotient improves the *description* of the remaining
flow to a weighted two-dimensional product order and proves
\(d(k)+5\) capacity without a logarithmic pointwise core.  It does not
prove global Hall.  The terminal cuts show that a successful chronology
must choose the within-rank order or refine an orbit in response to the
current exposed upper-type suffix.  The K46 interior cut shows that even
separating the complete top layer is insufficient; Proposition 5.3 shows
that an adaptive orbit interchange can nevertheless repair that exact cut.

This is distinct from the pointwise-core failures.  Pointwise fixing
\(O(\log k)\) coordinates gives types \((A,j)\) with a Boolean coordinate
\(A\), \(O(k^{3/2})\) types, and enough item-size slack for \(d+1\)
capacity.  The balanced setwise core has only the two scalar coordinates
\((i,j)\), \(O(k^2)\) types, and critical \(W/d\) orbit size; its failure
above is already the terminal owner/aperture cut, before any subtler
interior Hall cut.

The following remain **UNPROVED** here:

* existence for every \(k\) of an adaptive balanced-core chronology with
  global Hall;
* existence of an adaptive chronology with depth \(d(k)+O(1)\) in any
  orbit model;
* an all-\(k\) anchored chain factor; and
* every literal serialization, overlap, address/history, residence,
  compiler, and regenerative statement.

## 7. Replay

Run

```text
python3 scratch/audit_balanced_setwise_core_serpentine_flow_20260802.py
```

The script constructs the exact weighted product-order type network,
checks the orbit and owner inventories, computes the residual min cut,
independently verifies capacity and conservation of the saved flow, and
replays the K9, K19, separated-top K46 obstruction, and adaptive K46 repair.
It also reports the first failures of six deterministic diagonal orders
through \(k=40\).  Those extra portfolio failures are diagnostics only;
they are not asserted as an obstruction to an adaptive order.
