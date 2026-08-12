# Native trace fibers and the K17 PBBS rank-floor obstruction

Date: 2026-07-31  
Status: unconditional normalization theorem, conditional Pascal flag theorem,
and exact source-relative K17 obstructions  
Scope: common-cap compilation after a carrier and staircase are fixed; no
K17 word, Hamilton path, or unrestricted PBBS no-go is asserted

## 0. Outcome

There is an exact interval/TU subbank, but it is a normalization rather than
an automatic compiler.

For a fixed maximal envelope \(E\) and a protected-row-exact guard word
\(Q\subseteq E\), retain only the **native trace**
incidence

\[
             (\tau_Q(C),C),\qquad
             \tau_Q(C)=\bigcup_{p\in C}Q_p .           \tag{0.1}
\]

Every such cap preserves \(Q\).  The cell fibers of \(\tau_Q\) are disjoint,
and ordering cells fiber by fiber makes every target neighborhood an
interval.  Thus a native exact compiler exists if and only if every target
has a nonempty fiber.  At the tight K17 one-pivot count, this is literal
bijectivity.

The construction boundary is sharp:

* for any depth-three Johnson/Pascal staircase, every trace of the **maximal
  envelope** has rank at least six, so the 9,401 K17 targets of ranks one
  through five have empty native fibers;
* the frozen authenticated 21-component lower-rainbow factor has all 24,310
  rank-eight consecutive-intersection labels, but only 15,095 of 19,448
  rank-seven labels and 10,024 of 12,376 rank-six labels in the next two
  intersection decks; these become native flag traces only after the
  long-run hypothesis or a direct trace replay; and
* that frozen factor has 3,705 cyclic positive runs of length two and 2,268 of
  length three.  The first literal `0110` row already has no protected host
  in a flat depth-three erosion.

Consequently the native-fiber theorem gives the exact desired
interval-convex/TU mechanism, but a full K17 proof still needs a genuinely
shrunk guard word or a non-native guarded bank for the deep lower ideal.

## 1. Native trace normalization

Let \(P\) be the physical positions, let \(E_p\ne\varnothing\) be the fixed
maximal envelope, and let \(Q_p\ne\varnothing\) satisfy
\(Q_p\subseteq E_p\).
Let \(\mathcal C\) be distinct physical lower cells and let \(\mathcal L\)
be the required lower targets.  Assume both \(E\) and \(Q\) are contained in
every protected row through their positions and that \(Q\) realizes all
protected middle and pin rows exactly.  Define

\[
 \tau_Q:\mathcal C\longrightarrow 2^{[k]}\setminus\{\varnothing\},
 \qquad \tau_Q(C)=\bigcup_{p\in C}Q_p.                 \tag{1.1}
\]

Retain the native bank

\[
 H_Q^{\rm nat}=\{(S,C):S\in\mathcal L,
                         \ \tau_Q(C)=S\}.             \tag{1.2}
\]

### Theorem 1.1 (native-fiber zero-defect compiler)

The following are equivalent.

1. \(H_Q^{\rm nat}\) contains a matching saturating \(\mathcal L\).
2. Every native fiber is nonempty:

   \[
                 \tau_Q^{-1}(S)\ne\varnothing
                 \qquad(S\in\mathcal L).             \tag{1.3}
   \]

Whenever these conditions hold, every saturating matching in the native
bank has a maximal common cap \(A(M)\) satisfying

\[
                         Q\subseteq A(M)\subseteq E,   \tag{1.4}
\]

and is a zero-defect compiler.  Moreover, the cells admit an order in which
every target neighborhood is an interval.

#### Proof

For a native edge \((S,C)\) and \(p\in C\), equation (1.1) gives

\[
                            Q_p\subseteq S.             \tag{1.5}
\]

Every selected native cap through \(p\) therefore contains \(Q_p\).
Starting from \(E_p\), their intersection gives the bracket (1.4).
Nonemptiness follows from \(Q_p\ne\varnothing\).  On a protected row,
\(Q\subseteq A(M)\) supplies its complete label and \(A(M)\subseteq E\)
forbids extras.  On a selected native cell \((S,C)\), \(Q\) has OR \(S\)
by definition, while that edge's own cap makes \(A_p(M)\subseteq S\) for
every \(p\in C\).  Its OR is therefore exactly \(S\).  Thus every
common-cap equation holds, although \(A(M)\) need not equal \(Q\).

Each physical cell belongs to exactly one trace fiber.  Fibers for distinct
targets are consequently disjoint.  A saturating matching exists precisely
when one can choose one cell from every nonempty fiber, proving the first
equivalence without a general Hall computation.

Finally, order the cells first by their trace value and arbitrarily inside
each fiber.  The neighborhood of \(S\) is exactly the block
\(\tau_Q^{-1}(S)\), so it is an interval.  The selector matrix is a disjoint
union of target--fiber stars and is totally unimodular.  \(\square\)

This is stronger than merely saying that a chosen matching is safe: the
whole native bank is Cartesian and every matching in it is safe.  It is also
logically only a normalization.  Condition (1.3) says that \(Q\) already
contains every required lower trace; the theorem does not construct such a
\(Q\).

### Corollary 1.2 (tight-cell bijection)

Suppose

\[
                     |\mathcal C|=|\mathcal L|         \tag{1.6}
\]

and every target satisfies (1.3).  Then no cell can have an invalid or
repeated trace: \(\tau_Q:\mathcal C\to\mathcal L\) is a bijection.

Indeed, disjoint nonempty fibers for \(|\mathcal L|\) targets already use at
least \(|\mathcal L|\) cells.  Equality leaves one cell in each fiber and no
cell outside them.

For K17 the one-pivot schedule

\[
 X=\{24310,24311,24312\},\qquad Y=\{0,1,7403\}        \tag{1.7}
\]

has depth histogram \(2^{7401}3^{16909}\) and exactly

\[
                  65,535=\sum_{j=1}^{8}\binom{17}{j}  \tag{1.8}
\]

physical cells.  Thus native trace surjectivity at this schedule is the
zero-slack spectral bijection, not a surplus-Hall condition.

## 2. Pascal canonical flag cells

Let \(T_0,\ldots,T_{W-1}\) be a rank-\(r\) chronology and use the flat
depth-\(d\) maximal erosion

\[
 Q_p=\bigcap_{\max(0,p-d)\le t\le\min(p,W-1)}T_t,
 \qquad 0\le p<W+d.                                  \tag{2.1}
\]

Assume every internal positive coordinate run of \(T\) has length at least
\(d+1\).  For \(0\le q\le d\), define the consecutive flag and its canonical
physical cell

\[
 R_{i,q}=\bigcap_{t=i}^{i+q}T_t,
 \qquad C_{i,q}=[i+q,i+d].                            \tag{2.2}
\]

### Theorem 2.1 (canonical flag identity)

For every valid \(i,q\),

\[
                 \boxed{\tau_Q(C_{i,q})=R_{i,q}.}     \tag{2.3}
\]

Whenever \(R_{i,q}\in\mathcal L\) and \(C_{i,q}\in\mathcal C\), the
canonical flag incidence is therefore native, cap-neutral, and part of the
intervalizable bank of Theorem 1.1.  In particular \(q=0\) is a middle-rank
row rather than a lower incidence in the K17 application.

#### Proof

If \(p\in[i+q,i+d]\), then the owner block \(i,\ldots,i+q\) is contained in
the intersection defining \(Q_p\).  Hence \(Q_p\subseteq R_{i,q}\).

Fix a coordinate \(x\in R_{i,q}\), and let \([a,b]\) be its positive run
containing \([i,i+q]\).  In an internal run, \(x\) occurs in the erosion
exactly on \([a+d,b]\); a boundary run only extends this safe set outward.
Since \(a\le i\), \(b\ge i+q\), and \(b-a+1\ge d+1\), this safe set meets
\([i+q,i+d]\).  Thus \(x\) occurs in some \(Q_p\) on the canonical cell.
The reverse containment was already proved.  \(\square\)

The companion audit exhausts all 356 binary traces of length at most ten
which satisfy the stated boundary/internal-run condition, and all 9,618 of
their canonical cells.  It checks both (2.3) and the pointwise containment
which makes the caps inert.

## 3. The Johnson rank floor

The native maximal-envelope route cannot be the whole K17 compiler.

### Theorem 3.1 (depth-\(d\) Johnson native rank floor)

Let the middle chronology be a Johnson path of rank \(r\), and let a
monotone chain-aligned schedule give every owner interval physical depth at
most \(d\).  Let \(E\) be its maximal envelope before any extra pin or lower
cap.  Then

\[
                     |E_p|\ge r-d                    \tag{3.1}
\]

at every position covered by a middle row.  Consequently every nonempty
native cell trace obeys

\[
                     |\tau_E(C)|\ge r-d.              \tag{3.2}
\]

#### Proof

The owner rows active at a position form a consecutive index block: starts
and deadlines are both increasing, so an inactive row cannot lie between
two active rows.  Since every active row starts within \(d\) physical steps
of the position and starts are distinct integers, there are at most \(d+1\)
active rows.

Intersecting the first rank-\(r\) Johnson owner gives rank \(r\).  Each next
owner differs by one deletion and one insertion, so it can remove at most
one additional coordinate from the running intersection.  The intersection
of at most \(d+1\) consecutive owners therefore has rank at least \(r-d\),
which is (3.1).  A nonempty union containing any such envelope letter cannot
have smaller rank, proving (3.2).  Halo positions unconstrained by a middle
row have full envelope and only increase the bound.  \(\square\)

For K17, \(r=9,d=3\).  Every maximal-envelope native trace has rank at least
six.  The exact excluded population is

\[
 \sum_{j=1}^{5}\binom{17}{j}
   =17+136+680+2380+6188
   =\boxed{9401}.                                     \tag{3.3}
\]

Thus a proof using \(H_E^{\rm nat}\) alone cannot cover K17.  It must first
construct a proper shrink \(Q\subsetneq E\) whose trace map is bijective, or
add non-native incidences with genuine co-selectable trace guards.  That is
exactly the unresolved common-cap quantifier; total unimodularity after the
shrink does not produce the shrink.

## 4. Exact census on the frozen 21-component factor

The authenticated source is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.components
SHA-256 6b24e8ab4c77e3e5711cacab233db29733e1b27c74b735a8fb84c9a1c3643702
```

It has 21 cyclic components and is a literal partition of all 24,310
rank-nine K17 owners.  Taking cyclic consecutive intersections inside every
component gives:

| owner width | occurrences | distinct traces | rank distribution |
|---:|---:|---:|---|
| 2 | 24,310 | 24,310 | all rank 8 |
| 3 | 24,310 | 15,095 | all rank 7 |
| 4 | 24,286 | 13,326 | occurrences: \(20605\) rank 6, \(3681\) rank 7; distinct: \(10024\) rank 6, \(3302\) rank 7 |

The width-two deck is exactly all \(\binom{17}{8}=24310\) rank-eight
targets.  Width three misses

\[
                  19448-15095=4353                   \tag{4.1}
\]

rank-seven targets.  Width four covers only 10,024 of the 12,376 rank-six
targets and also repeats rank-seven values.  The eight length-three factor
components are omitted from the width-four census because a four-owner
physical flag may not revisit a cyclic owner.

These counts identify a useful candidate positive statement: after a
compatible linear opening and root-colour boundary pin, **and** after either
eliminating the short runs required by Theorem 2.1 or directly replaying the
native traces, the lower-\(q_1\) deck has the exact native-fiber form.  The raw
intersection census alone does not establish that conclusion.  It does not
provide the lower ranks, and it does not make the disconnected cycles into
a physical K17 chronology.

## 5. The first flat trace-guard failure

The same frozen factor has the exact cyclic positive-run census

\[
             N_1=0,\qquad N_2=3705,\qquad N_3=2268.  \tag{5.1}
\]

The lexicographically first length-two run is coordinate zero in component
zero, at owner indices 91 and 92:

```text
index       90       91       92       93
owner    0x0bf06  0x0b707  0x0f307  0x0f30e
bit 0        0        1        1        0
```

In a flat depth-three erosion, a bit survives at a physical position only
when four consecutive owners contain it.  No such position exists in either
of the two displayed middle-row intervals.  Their protected host sets for
bit zero are empty before any lower cap is selected.

This is a unary obstruction to using the frozen cyclic order with the flat
canonical flag theorem.  It does **not** exclude an arbitrary-start
staircase or a rethreading which cuts the closed span of every short run.
The singleton-absorbed 736-component atlas and its DFA degree cover are a
different source-relative object and are not contradicted by (5.1).

## 6. Why physical point guards are not themselves laminar

There is also a minimal obstruction to the most direct corridor ordering.
In the exact one-pivot K17 cell atlas, take the four cells

\[
 [7401,7403],\quad[7401,7401],\quad[7402,7402],\quad[7403,7403].
\tag{6.1}
\]

Restrict the three point-cover rows to these columns.  Their matrix is

\[
 \begin{array}{c|cccc}
  & [7401,7403]&[7401]&[7402]&[7403]\\\hline
 7401&1&1&0&0\\
 7402&1&0&1&0\\
 7403&1&0&0&1
 \end{array}.                                         \tag{6.2}
\]

No ordering of the four columns makes all three rows consecutive: the long
cell would have to be adjacent to all three singleton columns, but a column
has only two neighbors in a linear order.  The three cover sets also overlap
in the long cell while each has a private singleton, so they are pairwise
crossing and not laminar.

This does not refute native target-fiber intervalization—the native fibers
are disjoint and use a different order.  It does rule out a shortcut which
tries to make every physical point-cover guard row interval or laminar in
one universal cell order.  Target-specific pruning or a richer
polymatroidal conflict model remains necessary outside the native bank.

## 7. Authentication and strict scope

The fail-closed audit is

```text
scratch/audit_k17_native_trace_pbbs_rank_floor_20260731.py
SHA-256 3fe8a627ae8910d20ff4a4b52bf6eca13e462bc587f29bbf07d92379527d52e9

scratch/k17_native_trace_pbbs_rank_floor_20260731.audit.json
SHA-256 d9cd972f3d89a8c75e82afd229612276e58a8fb38929f5897c990fe253baf690
payload 5965f266f34407860330f286e76400f36ee1ec007d26693abb74a5cbba9b9032
```

The audit also exhausts all 24 column orders of the minimal star and checks
the exact one-pivot cell count and depth histogram.  It launches no solver
and no heavy process.

What is proved:

* exact native-fiber intervalization and zero-defect compilation for a fixed
  surjective guard word;
* tight-count bijectivity;
* the Pascal canonical flag identity;
* the depth-\(d\) Johnson rank floor;
* the displayed frozen-factor shallow decks and short-run core; and
* failure of direct point-cover laminarity/consecutive-ones.

What is not proved:

* existence of a surjective K17 guard word;
* a full lower compiler from the frozen PBBS factor;
* Hamiltonicity, a legal final staircase, or complete deeper upper replay;
* failure of every non-native guarded bank; or
* any unrestricted K17 or all-dimensional no-go.
