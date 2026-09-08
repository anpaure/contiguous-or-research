# Seven planted split hosts realize the sharp octagon chain banks locally

Date: 2026-08-01  
Lane: Thread D, source-signature repair for the quaternary octagon  
Status: exact local planted-host menu for every `d>=5`, together with an
exact current-word obstruction.  This is **not** a contextual-transparency
theorem: owner/deadline legality and the cross-host deck remain open.

## 0. Verdict

Let `Delta_0=Deck(Y^0)-Deck(Y^1)` and
`Delta_1=Deck(Y^1)-Deck(Y^0)` for the two expanded sharp sources.  The
inclusion widths `6,7` do have a useful interpretation, but not the initially
suggested one.

There is an explicit menu of seven *planted* old letters `X_h`.  If each
`X_h` occurs next to the displayed outward filler trace, then the
union-preserving split

\[
                         X_h\longmapsto X_h,B_h^\epsilon       \tag{0.1}
\]

creates one exclusive endpoint ray.  In phase zero the seven rays partition
`Delta_1`; in phase one six of them partition `Delta_0`, while the seventh
can use the neutral split `X_7 -> X_7,X_7`.  Every old interval is preserved
by contracting (0.1), and both new positions have the phase-common cap
`X_h`.

This is an exact **local ray algebra**, not a construction in the current
octagon antecedent.  None of the seven `X_h` is a letter of either current
sharp source.  More strongly, arbitrary union-preserving refinements of all
current letters still miss `3d-3` targets in either direction.  Thus the
menu identifies what must be planted; it does not turn the eight existing
filler corridors into seven legal split sites.

Finally, separately correct local rays need not have a common global deck.
Intervals trimming two planted blocks, or continuing beyond a listed ray,
can create fresh masks.  Full contextual transparency additionally requires
equality of the new internal/prefix/suffix decks (or an exact guarded Hall
assignment), as well as owner, deadline, residence and contraction legality.

## 1. Notation and the one-sided split lemma

Suppress a fixed core `K` only in prose, and write

\[
             F[i,j]=\{f_i,f_{i+1},\ldots,f_j\}.             \tag{1.1}
\]

If an old word contains `X` followed by letters `R_1,...,R_s`, replace `X`
by `X,B`, where `empty != B subseteq X`.  Then contraction preserves every
old interval, while the new right-facing cells have values

\[
                 B,\ B\cup R_1,\ldots,
                 B\cup R_1\cup\cdots\cup R_s.              \tag{1.2}
\]

The first half `X` is deliberately unchanged.  Hence its exclusive
left-facing intervals already had the same values before the split.  Formula
(1.2) is the only locally new ray.  The reversed statement is identical.

This overlapping split is legitimate: `X union B=X`.  It adds one source
position, gives both positions cap `X`, and raises by one only the deadlines
of transported old intervals containing the host.

## 2. The exact seven chain pairs

The superscript on `C_h^epsilon` denotes the *receiving* phase.  Thus
`C_h^0 subseteq Delta_1` and `C_h^1 subseteq Delta_0`.

### 2.1 The prefix ray

\[
\begin{aligned}
 C_P^0&=\{K+za_3+F[1,j]:1\le j\le d-1\},\\
 C_P^1&=\{K+za_1+F[1,j]:1\le j\le d-1\}.                 \tag{2.1}
\end{aligned}
\]

Take

\[
 B_P^0=K+za_3+f_1,\quad B_P^1=K+za_1+f_1,\quad
 X_P=K+za_1a_3+f_1,                                      \tag{2.2}
\]

and the outward trace `f_2,f_3,...,f_(d-1)`.

### 2.2 Three terminal filler rays

For `x_0=a_1` and `x_1=a_3`, put

\[
\begin{array}{c|c|c}
h&B_h^\epsilon&\text{successive outward additions}\\ \hline
G_d&K+zx_\epsilon+f_d&f_{d-1},\ldots,f_2\\
G_{d+1}&K+zx_\epsilon+F[d,d+1]&f_{d-1},\ldots,f_3\\
G_{0,d+1}&K+zx_\epsilon+f_0+F[d,d+1]&f_{d-1},\ldots,f_3.
\end{array}                                               \tag{2.3}
\]

Here the indexing `x_0=a_1,x_1=a_3` is correct because phase zero is
receiving `Delta_1`.  The common hosts are the unions of the two bases:

\[
\begin{aligned}
X_{G_d}&=K+za_1a_3+f_d,\\
X_{G_{d+1}}&=K+za_1a_3+F[d,d+1],\\
X_{G_{0,d+1}}&=K+za_1a_3+f_0+F[d,d+1].                  \tag{2.4}
\end{aligned}
\]

Their rays are exactly

\[
\begin{aligned}
C_{G_d}^\epsilon
 &=\{K+zx_\epsilon+F[t,d]:2\le t\le d\},\\
C_{G_{d+1}}^\epsilon
 &=\{K+zx_\epsilon+F[t,d+1]:3\le t\le d\},\\
C_{G_{0,d+1}}^\epsilon
 &=\{K+zx_\epsilon+f_0+F[t,d+1]:3\le t\le d\}.          \tag{2.5}
\end{aligned}
\]

### 2.3 The short exterior/high ray

Take

\[
 B_E^0=K+a_1+f_0f_1,\quad B_E^1=K+a_3+f_0f_1,\quad
 X_E=K+a_1a_3+f_0f_1.                                    \tag{2.6}
\]

In phase zero use the additions

\[
 f_2,\qquad \{a_0,a_3\}\cup F[3,d],\qquad f_{d+1};       \tag{2.7}
\]

in phase one use

\[
 f_2,\qquad \{a_0,a_2\}\cup F[3,d].                     \tag{2.8}
\]

They give

\[
\begin{aligned}
C_E^0=\{&K+a_1+f_0f_1, K+a_1+f_0f_1f_2,\\
        &K+a_0a_1a_3+F[0,d], K+a_0a_1a_3+F[0,d+1]\},\\
C_E^1=\{&K+a_3+f_0f_1, K+a_3+f_0f_1f_2,\\
        &K+a_0a_2a_3+F[0,d]\}.                           \tag{2.9}
\end{aligned}
\]

### 2.4 The asymmetric long/short pair

Take

\[
\begin{aligned}
B_S^0&=K+a_3+F[1,3],\\
B_S^1&=K+a_1+F[2,d+1],\\
X_S&=K+a_1a_3+F[1,d+1].                                  \tag{2.10}
\end{aligned}
\]

In phase zero append `f_4,...,f_(d+1)` and then `{a_0,a_2}`.  In phase one
append, in order, `f_1`, `{a_2,a_3}`, and `f_0`.  The resulting chains are

\[
\begin{aligned}
C_S^0={}&\{K+a_3+F[1,j]:3\le j\le d+1\}\\
 &\cup\{K+a_0a_2a_3+F[1,d+1]\},\\
C_S^1={}&\{K+a_1+F[2,d+1],K+a_1+F[1,d+1],\\
 &\hspace{12mm}K+a_1a_2a_3+F[1,d+1],
 K+a_1a_2a_3+F[0,d+1]\}.                                \tag{2.11}
\end{aligned}
\]

Notice that `|X_S|=r` when `|K|=r-d-3`; this is the tightest candidate
host in the menu.

### 2.5 The seventh, phase-zero-only ray

Put

\[
 B_R^0=K+a_3+F[2,3],\qquad
 X_R=K+a_0a_3+F[2,3].                                    \tag{2.12}
\]

Splitting `X_R -> X_R,B_R^0` and appending `f_4,...,f_(d+1)` gives

\[
 C_R^0=\{K+a_3+F[2,j]:3\le j\le d+1\}.                  \tag{2.13}
\]

Phase one uses the neutral split `X_R -> X_R,X_R`, which introduces no new
one-sided value relative to that reference host and trace.

## 3. Exact partition and rank ledger

The seven phase-zero receiver banks and six phase-one receiver banks are
pairwise disjoint and satisfy

\[
\begin{aligned}
\Delta_1={}&C_P^0\mathbin{\dot\cup}C_{G_d}^0
 \mathbin{\dot\cup}C_{G_{d+1}}^0
 \mathbin{\dot\cup}C_{G_{0,d+1}}^0
 \mathbin{\dot\cup}C_E^0\mathbin{\dot\cup}C_S^0
 \mathbin{\dot\cup}C_R^0,\\
\Delta_0={}&C_P^1\mathbin{\dot\cup}C_{G_d}^1
 \mathbin{\dot\cup}C_{G_{d+1}}^1
 \mathbin{\dot\cup}C_{G_{0,d+1}}^1
 \mathbin{\dot\cup}C_E^1\mathbin{\dot\cup}C_S^1.       \tag{3.1}
\end{aligned}
\]

The chain lengths are respectively

\[
(d-1,d-1,d-2,d-2,4,d,d-1),\qquad
(d-1,d-1,d-2,d-2,3,4),                                  \tag{3.2}
\]

and hence sum to `6d-3` and `4d+1`.

If `|K|=r-d-3`, the seven common-host ranks are

\[
 r-d+1, r-d+1, r-d+2, r-d+3, r-d+1, r, r-d+1.     \tag{3.3}
\]

Thus every proposed `X_h` has rank at most `r` for `d>=5`.  Rank is not the
obstruction; literal occurrence in a deadline-compatible antecedent is.

## 4. Why these are planted, not native, hosts

None of the seven `X_h` in Section 2 is a letter of either authenticated
expanded sharp source.  This finite statement is replayed through depth 64.
There is also an all-arity obstruction independent of this chosen menu.
The exact block-refinement criterion for the current opposite word leaves

\[
             |\Delta_0-Ref(Y^1)|=|\Delta_1-Ref(Y^0)|=3d-3. \tag{4.1}
\]

Hence no number of union-preserving splits of the current eight filler
traces can equalize the decks.  In particular the seven-slot menu cannot be
implemented merely by selecting seven current source letters.

The first six displayed common hosts also contain both `a_1` and `a_3`.
The only tensor owner containing their relevant combined active state is an
isolated union screen; a depth-`d` source envelope meeting a neighbouring
coatom block loses one of them.  This explains geometrically why the merged
letters do not occur, while (4.1) is the stronger complete statement.

## 5. Exact unresolved global conditions

Equations (2.1)--(3.3) prove only that seven planted one-sided split rays
would cover the *old* directed differences.  A regenerative use must still
prove all of the following in one antecedent.

1. Each `X_h` is one actual source letter, with the displayed outward trace
   and a legal terminal blocker.
2. The split half-windows preserve owner rank, middle ownership, residence
   and the allowed deadline staircase.
3. Both positions of each split lie in the prescribed common cap `X_h` and
   simultaneous contraction is matching-safe.
4. Every interval trimming two different planted hosts, and every interval
   continuing past a listed ray, is old/common or has a guarded compiler
   assignment.
5. Equivalently, the final two phases have equal internal, prefix and suffix
   decks (and equal total union), or the remaining protected differences
   satisfy exact Hall.

Item 4 is the **cross-host overshoot gate**.  It is not implied by the
disjoint chain partition.  Therefore this note does not call the seven-host
menu context-transparent and does not claim an `O(1)` recurrence.

## 6. Audit

Run

```text
python3 scratch/audit_threadD_octagon_seven_planted_host_menu_20260801.py --write
```

The light dependency-free replay checks `5<=d<=64`: every cumulative ray
identity, both disjoint partitions (3.1), the chain counts, host unions and
ranks, and absence of all seven hosts from both current expanded sharp
sources.  It deliberately does not manufacture owner/deadline legality or
test unspecified cross-host placements.

