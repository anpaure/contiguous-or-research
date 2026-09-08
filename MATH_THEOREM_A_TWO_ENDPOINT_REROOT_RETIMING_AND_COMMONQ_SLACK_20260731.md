# Two-endpoint rerooting, singleton retiming, and the exact common-Q slack boundary

Date: 2026-07-31  
Lane: A  
Status: unconditional general theorems, with the solved K16 construction as an exact instance

## 0. Result and scope

The optimal K16 word is now frozen at length 12,873. Its middle chronology is
the genuine-four-filter two-endpoint reroot, and its lower compiler is one
simultaneous common-cap matching. This note extracts the reusable mathematics:

1. an exact formula for every interval OR after two endpoint reroots;
2. an exact cost and feasibility criterion for singleton retiming;
3. an exact fibre and waste formulation of common-Q;
4. a counterexample showing that marginal Hall slack, even robust expansion,
   does not imply common-Q; and
5. two quantitative sufficient routes: clutter-safe cut retention and a
   spread or local-lemma matching theorem.

The finite K16 search is closed. No new K16 search is proposed here.

## 1. Exact two-endpoint reroot theorem

Let

\[
T=(T_0,\ldots,T_{N-1})
\]

be a set-valued word, and choose \(0\le a<b-1<N\). Put

\[
R_{a,b}(T)=operatorname{rev}(T[0,a])
 \;\Vert\;T[a+1,b-1]
 \;\Vert\;\operatorname{rev}(T[b,N-1]),                 \tag{1.1}
\]

where all displayed intervals are inclusive. Write \(\mu_1(X)\) for the
multiset of adjacent unions of a word \(X\).

### Theorem 1.1 (q1 transport and complete interval deck)

The q1 multiset changes by exactly

\[
\begin{aligned}
\mu_1(R_{a,b}(T))=\mu_1(T)
 &-\delta_{T_a\vee T_{a+1}}
  -\delta_{T_{b-1}\vee T_b}\\
 &+\delta_{T_0\vee T_{a+1}}
  +\delta_{T_{b-1}\vee T_{N-1}}.                     \tag{1.2}
\end{aligned}
\]

Moreover, every interval OR of \(R_{a,b}(T)\) belongs to exactly one of the
following four geometric classes, up to coincidences of values:

1. an interval lying wholly inside one of the three original blocks;
2. a left ladder
   \[
   \bigvee_{i=0}^{u}T_i\ \vee\
   \bigvee_{i=a+1}^{v}T_i,
   \qquad 0\le u\le a,quad a+1\le v\le b-1;           \tag{1.3}
   \]
3. a right ladder
   \[
   \bigvee_{i=u}^{b-1}T_i\ \vee\
   \bigvee_{i=v}^{N-1}T_i,
   \qquad a+1\le u\le b-1,quad b\le v<N;             \tag{1.4}
   \]
4. a two-seam ladder
   \[
   \bigvee_{i=0}^{u}T_i\ \vee\
   \bigvee_{i=a+1}^{b-1}T_i\ \vee\
   \bigvee_{i=v}^{N-1}T_i,
   \qquad 0\le u\le a,quad b\le v<N.                 \tag{1.5}
   \]

Consequently, for any desired upper family \(\mathcal U\), the reroot is
upper-complete if and only if its three internal witness banks together with
the ladders (1.3)--(1.5) cover \(\mathcal U\).

#### Proof

Reversal preserves every internal unordered adjacent pair. The only deleted
adjacencies are the two original cut edges, and the only inserted adjacencies
are the two new block seams. This proves (1.2).

A contiguous interval in the reroot either stays in one block, crosses just
the left seam, crosses just the right seam, or crosses both. A suffix of the
reversed left block is an original prefix \(T[0,u]\), while a prefix of the
reversed right block is an original suffix \(T[v,N-1]\). These observations
give (1.3)--(1.5) and exhaust all intervals. The final equivalence is then
the definition of upper completeness. ∎

### Corollary 1.2 (dimension-uniform repair certificate)

Suppose \(T\) is a Johnson path. Then \(R_{a,b}(T)\) is a Johnson path if
and only if its two new seam pairs are Johnson adjacent. If the two deleted
q1 colours have multiplicity at least two and the two inserted colours are
the two missing q1 colours, the reroot is q1-complete. If, in addition, the
bank-and-ladder criterion of Theorem 1.1 holds, it is upper-complete at every
depth.

Thus two endpoint reroots may repair an entire nested upper defect tower,
not merely two q1 colours. Preservation of the old crossing witness bank is
a separate hypothesis; q1 multiplicity alone does not imply it.

### K16 calibration

For the authentic chronology, \(a=6388\), \(b=12826\). The removed q1
colours `c3ce` and `f38c` each retain another occurrence, while the new seams
install `d3cc` and `b3cc`. The two endpoint ladders supply exactly

```text
b3cc d3cc d3ce f3cc dbce fbce
```

and exhaustive replay shows that no old upper mask is lost. This gives the
carrier SHA

```text
c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

## 2. Exact singleton-retiming lemma

Let physical starts \(s_0<\cdots<s_{N-1}\) and deadlines
\(q_0<\cdots<q_{N-1}\) define middle intervals
\(I_i=[s_i,q_i]\). Let

\[
E_p=\bigcap_{i:p\in I_i}T_i                              \tag{2.1}
\]

be the maximal middle envelope, and assume
\(\bigvee_{p\in I_i}E_p=T_i\) for every row.

### Lemma 2.1 (retiming cost)

Keep the omitted starts fixed. Let \(Y\) be the omitted-deadline set, assume
\(y\in Y\), \(y+\tau\notin Y\), and \(\tau\ge0\). If \(y\) is replaced by
\(y+\tau\), with the resulting ordered pairing still legal, then the total
selected proper-prefix area decreases by exactly \(\tau\).

#### Proof

The area is

\[
\sum_i(q_i-s_i)=\sum_iq_i-\sum_is_i.
\]

The retained deadline set loses \(y+\tau\) and gains \(y\), while the start
sum is unchanged. ∎

### Lemma 2.2 (exact singleton pin)

A physical position \(p\) may be capped to a singleton \(\{z\}\) while
preserving every middle row if and only if

\[
z\in E_p                                                   \tag{2.2}
\]

and, for every \(i\) with \(p\in I_i\),

\[
\{z\}\vee\bigvee_{q\in I_i\setminus\{p\}}E_q=T_i.       \tag{2.3}
\]

When the singleton cell \([p,p]\) belongs to the lower catalogue, it then
realizes target \(\{z\}\). Marginal feasibility after pinning is exactly
Hall in the candidate graph recomputed from the capped envelope, after
deleting the singleton target and its reserved cell.

#### Proof

Only rows containing \(p\) change. Condition (2.2) is precisely
nonemptiness of the new letter, and (2.3) is precisely preservation of each
affected row OR. The final Hall statement is ordinary matching after the
fixed incidence is contracted. ∎

For K16, retiming the third omitted deadline from 6386 to 6388 costs two
area units and exposes position 6389, where

\[
E_{6389}=\mathtt{0xc304}\longmapsto\mathtt{0x8000}.
\]

After reserving this singleton, 26,331 residual targets have 32,229 cells,
347,677 incidences, and a perfect marginal matching. The residual cell
surplus is 5,898.

## 3. Common-Q is one fibre, not the union of marginal fibres

Fix an envelope word \(E\) after all fixed pins and catalogue restrictions
have been installed, together with its middle and fixed-pin obligations, a
lower target family \(\mathcal L\), and a physical cell catalogue
\(\mathcal C\). Let
\(\mathcal W(E)\) be the set of nonempty words \(Q\) with
\(Q_p\subseteq E_p\) which preserve every middle obligation and fixed pin.
For \(Q\in\mathcal W(E)\), label a cell by

\[
\ell_Q(C)=\bigvee_{p\in C}Q_p.                          \tag{3.1}
\]

### Theorem 3.1 (fibre formulation)

A common-Q lower compiler exists if and only if there is one
\(Q\in\mathcal W(E)\) such that

\[
\mathcal L\subseteq\{\ell_Q(C):C\in\mathcal C\}.        \tag{3.2}
\]

The marginal individual-host graph is the union, over
\(Q\in\mathcal W(E)\), of the fibre graphs

\[
G_Q=\{(S,C):\ell_Q(C)=S\}.                              \tag{3.3}
\]

Thus Hall in the marginal union exchanges the required quantifiers:
targetwise witnesses may come from different \(Q\)'s.

#### Proof

A physical cell has one label under a fixed word, so (3.2) assigns distinct
cells automatically to distinct target masks. Conversely, any simultaneous
compiler word has every lower target among its cell labels. An incidence is
individually feasible exactly when capping by that target alone produces
some middle-feasible word in the corresponding fibre, which proves (3.3).
∎

### Proposition 3.2 (exact slack/waste identity)

Put \(n=|\mathcal L|\), \(m=|\mathcal C|=n+s\), and define

\[
D(Q)=\bigl|\{\ell_Q(C):C\in\mathcal C\}\cap\mathcal L\bigr|,
\qquad W(Q)=m-D(Q).                                      \tag{3.4}
\]

Then the number of lower holes is exactly

\[
h(Q)=n-D(Q)=W(Q)-s.                                      \tag{3.5}
\]

Hence scalar slack \(s\) is only the unavoidable waste baseline. Exact
common-Q requires one word with \(W(Q)=s\); asymptotic near-coverage is
equivalent to excess waste \(W(Q)-s=o(n)\).

## 4. Marginal slack does not imply common-Q

### Proposition 4.1 (robust-Hall interface obstruction)

There are arbitrarily large common-cap interfaces with uniform
\(5/2\)-fold marginal Hall expansion and no common-Q realization.

#### Proof

Use four pairwise distinct coordinates \(a,b,x,y\) and five ordered
positions \(0,1,2,3,4\), with center envelope
\(E_2=\{a,b\}\) and outer envelopes \(E_i=\{x,y\}\). Take targets

\[
A=\{a,x\},\qquad B=\{b,y\},
\]

and the five distinct length-at-most-three cells

\[
[1,2],\ [2,3],\ [0,2],\ [1,3],\ [2,4].                 \tag{4.1}
\]

There are no additional middle or fixed-pin obligations in this interface.
Each cell individually realizes either target by intersecting its outer
letters with \(\{x\}\) or \(\{y\}\) and its center with \(\{a\}\) or
\(\{b\}\). Thus the marginal graph is \(K_{2,5}\), and every nonempty
target subset \(X\) satisfies \(|N(X)|\ge(5/2)|X|\). But any injection uses
two cells both containing position 2, where the common cap is

\[
\{a,b\}\cap A\cap B=\varnothing.
\]

Disjoint unions preserve the expansion ratio and give arbitrary size. ∎

This is an exact obstruction at the common-cap interface, not a claimed
literal P/Q carrier. It proves that total slack, robust marginal expansion,
bounded cell length, and absence of universal matching edges still do not
imply common-Q.

## 5. Two quantitative sufficient theorems

Let \(\mathfrak F\) be the exact family of matching-compatible minimal
common-cap obstructions. Call an edge subgraph \(H\) **clutter-safe** if it
contains no member of \(\mathfrak F\). Then every perfect matching in \(H\)
is common-Q.

For comparison, for an edge subgraph \(H\) put

\[
K_p(H)=E_p\cap
\bigcap_{(S,C)\in H:\,p\in C}S.                         \tag{5.1}
\]

Call \(H\) **Cartesian** if all \(K_p(H)\) are nonempty, they preserve
every middle and fixed-pin obligation, and every edge \((S,C)\in H\)
satisfies

\[
\bigvee_{p\in C}K_p(H)=S.                              \tag{5.2}
\]

If a Cartesian \(H\) has at least one incident edge for every target, then
\(K(H)\) itself is already a common-Q word; no Hall theorem is needed.
Indeed, two distinct targets cannot occur on the same cell of a Cartesian
graph, because (5.2) would give that cell two distinct labels.

### Theorem 5.1 (cutwise slack absorption)

Suppose, for every \(X\subseteq\mathcal L\),

\[
|N_G(X)|\ge(1+\varepsilon)|X|                          \tag{5.3}
\]

and a clutter-safe subgraph \(H\subseteq G\) satisfies

\[
|N_H(X)|\ge(1-\eta)|N_G(X)|.                           \tag{5.4}
\]

If

\[
\eta\le\frac{\varepsilon}{1+\varepsilon},             \tag{5.5}
\]

then \(H\) has a lower-perfect matching, and therefore a common-Q compiler.

#### Proof

Equations (5.3)--(5.5) give \(|N_H(X)|\ge|X|\) for every \(X\).
Hall's theorem supplies a perfect matching in \(H\), and clutter-safety says
that this matching avoids every exact common-cap obstruction. ∎

For the full target set, necessarily \(\varepsilon\le s/n\). Thus the
largest pruning fraction which scalar surplus could ever pay for is

\[
\eta\le\frac{s}{n+s}.                                  \tag{5.6}
\]

At the optimal length \(W+d\), the total lower-cell inventory is at most

\[
dW+\binom{d+1}{2}.
\]

If \(n=\Lambda\) and \(d\) is minimal, then

\[
0\le s<W+d.                                             \tag{5.7}
\]

Since minimality gives
\(\Lambda>(d-1)W+\binom d2\), (5.7) gives
\(s/\Lambda=O(1/d)\); with \(d(k)=\Theta(\sqrt{k})\), this is at most
\(O(k^{-1/2})\). Consequently this particular cut-retention route requires
retaining a \(1-O(1/d)\) fraction of every relevant Hall neighbourhood. A
fixed positive pruning loss cannot be paid for by optimal-length scalar
surplus through this route. Cartesian left-covers and correlated matchings
need not satisfy such a global retention estimate.

There is a second, correlation-based route. Let \(\mathfrak F\) contain all
cell-collision pairs and all inclusion-minimal common-cap obstructions.

### Theorem 5.2 (spread and local-lemma criteria)

Assume there is a probability measure \(\mu\) on lower-perfect marginal
matchings such that, for every \(F\in\mathfrak F\),

\[
\Pr_{M\sim\mu}[F\subseteq M]\le\rho^{|F|}.              \tag{5.8}
\]

If

\[
\sum_{F\in\mathfrak F}\rho^{|F|}<1,                   \tag{5.9}
\]

then a common-Q matching exists.

Alternatively, first delete every unary-forbidden incidence, retain exactly
\(D\) candidate cells for every target, and choose independently and
uniformly. Suppose every remaining bad certificate has size between two and
\(R\), contains at most one choice of any target, and each target variable
occurs in at most
\(\Gamma\) bad certificates. If

\[
e(R\Gamma+1)\le D^2,                                   \tag{5.10}
\]

then there is an injective common-Q assignment.

#### Proof

For (5.8)--(5.9), the union bound gives positive probability that no member
of the exact obstruction clutter occurs. For (5.10), every bad event fixes
at least two independent target choices, so it has probability at most
\(D^{-2}\). It depends only on events sharing one of its at most \(R\)
target variables, hence on at most \(R\Gamma\) events. The symmetric local
lemma gives a simultaneous avoidance. Collision events ensure injectivity;
avoidance of the remaining exact obstruction clutter gives common-Q. ∎

For depth three with middle rows of length at most four, lower cells of
length at most three, and at most one catalogue cell for each start/length
interval, the authenticated conflict-clutter theorem gives \(R\le6\). What
remains in a uniform construction is therefore not a new
scalar estimate, but either a clutter-safe cut-retention theorem or a spread
bound on these bounded local conflicts.

## 6. Dimension-uniform construction corollary

Let \(r=\lceil k/2\rceil\), \(W=\binom{k}{r}\), let \(\Lambda\) be the
number of nonempty targets below rank \(r\), and let \(d=d(k)\) define the
proved lower bound \(B(k)=W+d\).

### Theorem 6.1 (reroot-retime-common-Q compiler)

Suppose there exist:

1. a middle-layer Johnson path obtained by the two-reroot operation (1.1),
   whose internal banks and boundary ladders cover every upper target;
2. a legal monotone depth-\(d\) interval schedule on \(W+d\) physical
   positions, in which the union of every consecutive block of middle-row
   intervals is a contiguous physical interval;
3. a jointly legal retiming and a set of distinct/resolved boundary
   singleton pins whose simultaneous capped envelope preserves every middle
   row and every pin, with total retiming cost no greater than the available
   scalar surplus; and
4. after the pins, either a Cartesian left-cover, a clutter-safe Hall
   subgraph satisfying Theorem 5.1, or a conflict-free matching supplied by
   Theorem 5.2.

Then a universal nonzero word of length \(W+d\) exists, and hence

\[
\nu(k)=B(k).                                             \tag{6.1}
\]

#### Proof

The common-Q matching supplies one nonzero physical word whose depth-\(d\)
middle rows are the prescribed middle-layer path and whose shorter cells
cover every lower target. The path itself covers the middle layer exactly.
Every upper target is a union of a consecutive block of middle rows by item
1, hence is the OR of the corresponding contiguous physical interval. Thus
the word is universal. Its length is \(W+d\), which meets the proved lower
bound. ∎

## 7. Exact K16 instance and the remaining general gate

For K16, the two reroots, the two-unit singleton retiming, and the direct
simultaneous common-cap matching all exist. The decoded word

```text
answers/k16.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

has length 12,873 and independently covers all 65,535 nonempty masks.
Therefore \(\nu(16)=12873=B(16)\).

The reusable open theorem is now precise: construct the reroot ladders and
singleton ports uniformly, then prove either cutwise clutter-safe retention at
the vanishing scale \(s/(\Lambda+s)\), or a spread bound strong enough for
(5.9) or (5.10). Marginal Hall or total scalar slack alone cannot supply the
common quantifier.
