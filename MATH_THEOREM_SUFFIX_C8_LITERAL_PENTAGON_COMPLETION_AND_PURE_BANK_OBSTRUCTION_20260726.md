# Literal pentagon completion of the suffix \(C_8\) ledger and the pure-bank obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

Let \(C^{\rm out}_8\) be the clean rank-three suffix switch from
`MATH_THEOREM_BALLOT_FORCED_C8_SUFFIX_ROUTER_BANK_20260726.md`. There are
two different conclusions.

1. **Literal positive packet.** A bounded certified local completion is
   the complete five-strand \(D_3\) pentagon factor. It has
   identity endpoint permutation, three Johnson steps on every row, and
   exact lower/upper ownership ledgers. Suspended in the last six
   coordinates, it gives a literal fixed-exterior packet on

   \[
                          5\operatorname {Cat}_{r-3}
     =\left(\frac5{64}+O(r^{-1})\right)\operatorname {Cat}_r          \tag{0.1}
   \]

   rows. Thus a positive-density equal-length packet exists with the common
   displacement \(e=0\).

2. **Pure-\(C_8\) obstruction.** This completion is not a power or a
   resource-disjoint combination of the corrected clean \(C_8\)'s. Every
   nonempty subfamily of the suffix bank has disjoint nonidentity
   four-cycle monodromy and displacement pattern \((1,1,1,2)\) on each
   component. Concatenating aligned copies acts on independent Cartesian
   port coordinates, not repeatedly on one transported label. A natural
   second matching-pure clean rank-three \(C_8\) is not composable with
   \(C^{\rm out}_8\): in either order the second toggle closes an internal
   cycle.

The pentagon therefore proves the literal packet requested in the question,
but it does not prove that the useful carrier of the clean \(C_8\) survives.
Indeed one of the four inserted \(C_8\) edges is absent from the completed
factor. For coefficient one, the remaining issue is a carrier-preserving
repair, not equal-length or middle-ownership existence.

## 1. The outgoing clean \(C_8\)

Use the canonical rank-three paths

\[
\begin{array}{c|c}
a&123-1236-136-1346-146-1456-456\\
b&124-1246-126-1256-156-1356-356\\
c&125-1245-145-1345-345-3456-346\\
d&134-1234-234-2346-236-2356-256\\
e&135-1235-235-2345-245-2456-246.
\end{array}                                                        \tag{1.1}
\]

The selected outgoing edges

\[
 124-1246,\qquad146-1456,\qquad
 145-1345,\qquad134-1234                              \tag{1.2}
\]

belong to four distinct rows and form the alternating star cycle

\[
 \boxed{124-1246-146-1456-145-1345-134-1234-124.}     \tag{1.3}
\]

After toggling (1.3), the five components are

\[
\begin{array}{c|c|c}
\text{root}&\text{new lower-state trace}&\text{terminal root label}\\ \hline
a&123,136,146,126,156,356&b\\
b&124,234,236,256&d\\
c&125,145,456&a\\
d&134,345,346&c\\
e&135,235,245,246&e.
\end{array}                                                        \tag{1.4}
\]

Thus its endpoint permutation is

\[
                         \rho=(a\ b\ d\ c),            \tag{1.5}
\]

and its row semilengths, in the order \((a,b,c,d,e)\), are

\[
                         (5,3,2,2,3).                  \tag{1.6}
\]

On the active roots \((b,a,c,d)\), the port displacements are
\((1,1,1,2)\). Hence (1.4) is an exact abstract degree/path ledger, but not
a fixed-exterior minimum-wreath packet.

## 2. No combination inside the disjoint suffix bank

For every Dyck prefix \(A\) of semilength \(r-3\), let \(C_A\) be the
suspension of (1.3) to the four roots

\[
 A110100,\quad A111000,\quad A110010,\quad A101100.     \tag{2.1}
\]

The supports \(\Omega_A\) of distinct \(A\)'s are disjoint.

### Theorem 2.1 (direct-sum monodromy obstruction)

Let \(\mathcal A\) be any nonempty set of suffix contexts. Toggling
\(C_A\) for every \(A\in\mathcal A\) gives endpoint permutation

\[
                         \rho_{\mathcal A}
                          =\prod_{A\in\mathcal A}\rho_A,             \tag{2.2}
\]

where the factors are disjoint four-cycles. Consequently:

1. \(\rho_{\mathcal A}\ne1\);
2. a fixed exterior \(e=0\) is impossible;
3. no one common moving exterior works, because each active orbit contains
   both displacement one and displacement two; and
4. applying bank toggles in an arbitrary finite sequence gives no new
   possibility: each \(C_A\) occurs only according to the parity of its
   number of toggles, so the sequence reduces to (2.2).

Thus no nonempty bounded—or unbounded—combination internal to the corrected
suffix bank is a literal equal-length wreath packet.

#### Proof

The four root supports in (2.1) are disjoint for different prefixes.
Hence their endpoint operations have disjoint supports and commute. A
product of disjoint nonidentity cycles is the identity only when no factor
occurs. The displacement assertion is the local calculation
\((1,1,1,2)\). Finally, toggling the same incidence cycle twice restores
the original edge set, proving the parity reduction. \(\square\)

This obstruction is stronger than the scalar count: the bank may touch a
positive fraction of all roots, but its direct-sum endpoint defect cannot
cancel across contexts.

## 3. Concatenated copies give a tensor, not a power

One might try to put several six-coordinate blocks in a root and use one
\(C_8\) at each block. The context law prevents those blocks from acting
successively on the same four labels.

### Proposition 3.1 (suffix erasure)

Suppose four Dyck roots support the local cycle (1.3) in a concatenation
block. Then the four roots are identical outside that block. In particular,
their suffixes after the block are identical. They cannot support a second
copy of (1.3) in a later disjoint block on the same four original roots.

#### Proof

Every lower vertex in (1.3) has one common spectator set outside the local
six coordinates. Before the active block is processed, the unprocessed
suffix occurs literally in that spectator. Equality of the four spectator
sets therefore forces equality of the four suffix words. A later active
block would require those same four suffixes to realize four different
local words, a contradiction. \(\square\)

For independent holes the port set is Cartesian. If the \(j\)-th local
atom acts by \(\rho\), then

\[
 T_j(x_1,\ldots,x_k)
  =(x_1,\ldots,x_{j-1},\rho x_j,x_{j+1},\ldots,x_k).   \tag{3.1}
\]

For any nonempty set \(S\) of active holes,

\[
                         \prod_{j\in S}T_j(x)
   =\bigl(\rho^{\mathbf1_{1\in S}}x_1,\ldots,
          \rho^{\mathbf1_{k\in S}}x_k\bigr),          \tag{3.2}
\]

which is nonidentity. Thus concatenation cannot turn four physical copies
into the formal power \(\rho^4=1\). It produces independent tensor
coordinates, exactly as the geodesic correction requires.

## 4. The smallest overlapping matching-pure attempt fails

The canonical rank-three factor contains a second clean matching-pure
star \(C_8\), now in the incoming matching:

\[
 \boxed{136-1236-236-2346-346-3456-356-1356-136.}     \tag{4.1}
\]

Its selected incoming edges lie on the four distinct rows

\[
                         a,\quad d,\quad c,\quad b.     \tag{4.2}
\]

So (4.1) is a legal clean toggle in the canonical factor. It is not a
second stage for (1.3).

### Theorem 4.1 (two-order internal-cycle obstruction)

Neither order of toggling (1.3) and (4.1) is strand-admissible. In each
order, the second proposed toggle closes one nonempty internal segment into
a cycle.

#### Proof

Toggle (1.3) first. In (1.4), the incoming edges

\[
 1236-136\quad\hbox{and}\quad1356-356                 \tag{4.3}
\]

both lie on the new path rooted at \(a\). Removing them exposes the
internal segment from \(136\) to \(1356\). The new half of (4.1) contains
the edge

\[
                         1356-136,                     \tag{4.4}
\]

which closes that segment into a component with no global endpoint.

Conversely, toggle (4.1) first. The resulting relevant paths are

\[
\begin{array}{c|c}
a&123,236,256\\
b&124,126,156,136,146,456\\
c&125,145,345,356\\
d&134,234,346.
\end{array}                                                        \tag{4.5}
\]

Now the outgoing edges \(124-1246\) and \(146-1456\) from (1.2) both
lie on the new path rooted at \(b\). Removing them exposes the nonempty
segment from \(1246\) to \(146\), while the new half of (1.3) contains

\[
                         1246-146.                     \tag{4.6}
\]

Again an internal cycle is created. The exact strand test therefore rejects
the second toggle in both orders. \(\square\)

Also, three clean \(C_8\) endpoint operations can never close monodromy:
each is an odd four-cycle, so their product is odd. Hence four is the first
group-theoretically possible number, while Proposition 3.1 blocks the
obvious four-block conveyor.

## 5. A literal five-strand completion

Although the pure bank does not compile, the complete rank-three pentagon
factor supplies a bounded residual repair. Replace (1.1) by

\[
\begin{array}{c|c|c}
\text{root}&X_0,X_1,X_2,X_3&Y_0,Y_1,Y_2\\ \hline
a&123,126,156,456&1236,1256,1456\\
b&124,234,345,356&1234,2345,3456\\
c&125,235,236,346&1235,2356,2346\\
e&135,136,146,246&1356,1346,1246\\
d&134,145,245,256&1345,1245,2456.
\end{array}                                                        \tag{5.1}
\]

### Theorem 5.1 (literal equal-length packet)

The rows (5.1) partition every three-set and every four-set of \([6]\),
each row has three Johnson steps, and the path rooted at \(P\) ends at
\([6]\setminus P\). Thus (5.1) is a literal fixed-exterior \(D_3\)-port
factor with the common displacement \(e=0\).

#### Proof

The twenty entries in the middle column of (5.1) are visibly the twenty
three-subsets of \([6]\), with no repetition. The fifteen entries in the
last column are visibly the fifteen four-subsets, with no repetition.
Every displayed upper state is the union of its adjacent lower states, so
all incidences are legal. The last lower states are respectively

\[
 456=\overline{123},\quad356=\overline{124},\quad
 346=\overline{125},\quad246=\overline{135},\quad
 256=\overline{134}.                                  \tag{5.2}
\]

This proves both complete ownership ledgers, equal length, and identity
port monodromy. \(\square\)

The abstract factor obtained from (1.1) by first toggling (1.3) has the
same vertex degrees as (5.1). Their symmetric difference is therefore a
red/blue balanced incidence subgraph and admits an alternating-cycle
decomposition. Toggling that complete decomposition is a bounded residual
repair from the clean \(C_8\) ledger to the literal packet (5.1). Only the
final combined replacement is used physically.

### Theorem 5.2 (positive-density suffix suspension with full collars)

For every \(r\ge3\) and every Dyck word \(A\) of semilength \(r-3\),
replace the five canonical paths rooted at

\[
 A111000, A110100, A110010, A101010, A101100       \tag{5.3}
\]

by the spectator extension of (5.1). These replacements are pairwise
resource-disjoint and together form a literal exact wreath-factor packet
affecting \(5\operatorname {Cat}_{r-3}\) rows. Every changed vertex lies at
or after phase \(r-3\).

#### Proof

After the prefix \(A\) has been processed, its complement is a common
spectator \(O_A\) of size \(r-3\). Map every local lower and upper state by

\[
                         X\mapsto O_A\cup X,
 \qquad                 Y\mapsto O_A\cup Y.           \tag{5.4}
\]

Theorem 5.1 shows that these images enumerate exactly the same local
lower/upper vertex sets as the five canonical rows, once each. The left
boundary state is \(O_A\cup P\), and the right boundary state is
\(O_A\cup([6]\setminus P)\), exactly the old two boundary states. Hence
both crossing collars are literal unchanged joins; there are no new
crossing \(Y\)-vertices to count. All internal \(X/Y\)-vertices are owned
once by (5.4).

Different prefixes \(A\) index disjoint canonical row bundles. Their local
vertex sets were disjoint before replacement and are unchanged as sets, so
the replacements remain resource-disjoint. This proves global exactness.
The row count is five per prefix. Finally

\[
 {5\operatorname {Cat}_{r-3}\over\operatorname {Cat}_r}
 =\frac{5r(r-1)(r+1)}{8(2r-1)(2r-3)(2r-5)}
 \longrightarrow\frac5{64}.                          \tag{5.5}
\]

\(\square\)

No row-dependent exterior is used: \(O_L=O_R=O_A\), all final endpoint
labels are fixed, and the complete crossing-collar ledger is inherited
literally.

## 6. Why this is not yet a coefficient-one carrier theorem

The completed factor (5.1) does not retain the entire new half of the clean
cycle (1.3). In particular,

\[
                         145-1456                     \tag{6.1}
\]

is inserted by (1.3) but absent from (5.1), while the old edge

\[
                         145-1345                     \tag{6.2}
\]

removed by (1.3) is restored. Thus that entire arm of the clean switch is
canceled. The other three new half-edges

\[
                         124-1234,\qquad146-1246,\qquad134-1345       \tag{6.3}
\]

are present. Therefore the signed carrier of the isolated clean \(C_8\)
cannot be assigned unchanged to the completed packet.

**Exact conclusion.** A literal positive-density equal-length packet
exists, namely the five-strand pentagon suspension. No nonempty combination
internal to the corrected disjoint suffix-\(C_8\) bank is physical, and the
natural matching-pure overlapping two-\(C_8\) attempt fails the strand
test. The remaining coefficient-one problem is to find a residual repair
whose full carrier retains a favourable nonzero projection.
