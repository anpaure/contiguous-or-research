# Balanced two-extensions, incidence hexagons, and the additive-constant reduction

Date: 2026-07-31.

This note reconciles three pieces of the construction theory:

1. the middle-level carrier is exactly one balanced two-extension map;
2. its elementary degree-preserving motion is an incidence hexagon;
3. the Pascal four-sector construction used at \(k=17\) has an exact,
   dimension-free residual ledger.

It also separates the exact conjecture \(\nu(k)=B(k)\) from the weaker
additive-constant conjecture. Exact equality asks for a lossless opening.
For \(B(k)+O(1)\), bounded expected opening loss is enough, because the lost
targets may be appended literally.

Throughout, \(k=2m+1\), \(r=m+1\),

\[
   \mathcal L=\binom{[k]}{r-1},\qquad
   \mathcal M=\binom{[k]}r,\qquad
   \mathcal U=\binom{[k]}{r+1}.
\]

## 1. The balanced two-extension normal form

For every \(C\in\mathcal L\), choose two distinct elements

\[
                   f(C)=\{a_C,b_C\}\subseteq [k]\setminus C
\]

and put

\[
                   \sigma(C)=C\cup f(C)\in\mathcal U.
\]

Define a graph \(G_f\) on \(\mathcal M\) by putting the edge

\[
                   C\cup\{a_C\}\ --\ C\cup\{b_C\}
\tag{1.1}
\]

for every \(C\in\mathcal L\). Label this edge by \(C\).

### Proposition 1.1 (exact equivalence)

The graph \(G_f\) is a lower-\(q_1\)-rainbow Johnson 2-factor if and only if

\[
  \#\{a\in T:a\in f(T\setminus\{a\})\}=2
  \qquad\text{for every }T\in\mathcal M.
\tag{1.2}
\]

It is simultaneously upper-\(q_1\)-complete if and only if \(\sigma\) is
surjective onto \(\mathcal U\).

#### Proof

Every edge in (1.1) is a Johnson edge and has intersection exactly \(C\).
There is one edge for every \(C\in\mathcal L\), so the lower colours are
automatically exact. The edge labelled \(T\setminus\{a\}\) is incident to
\(T\) precisely when \(a\in f(T\setminus\{a\})\). Thus (1.2) is exactly the
degree-two condition at \(T\). Finally, the union of the two endpoints of
the edge labelled \(C\) is \(\sigma(C)\), proving the upper assertion. \(\square\)

Thus the two immediate shadow gates are not two unrelated constraints. They
ask for one **balanced surjective two-extension map**

\[
  f:\binom{[k]}{r-1}\longrightarrow
    \binom{[k]\setminus C}{2}.
\tag{1.3}
\]

Connectivity is separate: it asks whether the 2-factor \(G_f\) has one
component. The \(k=13\), \(k=15\), and current \(k=17\) constructions show
that connectivity should be postponed until after the shadow design.

### Theorem 1.2 (PBBS supplies such a map for every odd \(k\))

Let \(p\) be the canonical cyclic-parenthesis/PBBS permutation on the
\(m\)-subsets of \([2m+1]\). Let \(r_+(C)\) and \(r_-(C)\) be the unique
forward- and reverse-unmatched zeros of the cyclic word of \(C\). Then

\[
                     f_{\rm PBBS}(C)=\{r_+(C),r_-(C)\}
\tag{1.4}
\]

is a balanced surjective two-extension map. Its upper loads lie in
\(\{1,2,3\}\), and its 2-factor has at most \(\operatorname{Cat}_m\)
components.

#### Proof

The PBBS inverse formula is

\[
 p(C)=C^c\setminus\{r_+(C)\},\qquad
 p^{-1}(C)=C^c\setminus\{r_-(C)\}.
\]

After complementation, the two neighbours attached to the lower colour
\(C\) are therefore

\[
        p(C)^c=C+r_+(C),\qquad p^{-1}(C)^c=C+r_-(C).
\tag{1.5}
\]

The maps \(C\mapsto p(C)^c\) and \(C\mapsto p^{-1}(C)^c\) are bijections
between the two middle levels, so (1.5) is the union of two perfect
matchings. Hence every rank-\((m+1)\) owner has degree two. Its edge
intersection is \(C\), and its edge union is

\[
 C+r_+(C)+r_-(C)
   =\bigl(p^{-1}(C)\cap p(C)\bigr)^c.
\tag{1.6}
\]

The audited PBBS angle theorem says that every rank-\((m-1)\) set occurs as
\(p^{-1}(C)\cap p(C)\) between one and three times. Complementing proves
surjectivity onto every rank-\((m+2)\) upper target with the same load bound.
For the component count, let \(P_j\) be the PBBS orbit lengths on the lower
level.  Complementing the union of the forward and backward PBBS matchings
turns an orbit of length \(P_j\) into \(\gcd(P_j,2)\) middle-level cycles.
PBBS site homomesy makes every \(P_j\) divisible by the odd integer
\(2m+1\), and hence each resulting cycle has length at least \(2m+1\).
Since the factor has \(\binom{2m+1}{m+1}\) middle owners, it follows directly
that

\[
       c(G_{f_{\rm PBBS}})\le
       \frac{\binom{2m+1}{m+1}}{2m+1}=\operatorname{Cat}_m.
\]

This is the component form of the composite-odd PBBS theorem. \(\square\)

This theorem is not new to the repository: the two-extension identity is the
complement of the first-shadow theorem, and the sharp component bound is
Corollary 2.3 of
THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md. Its
importance here is conceptual. The balanced-surjective map is already an
unconditional all-odd object. The remaining construction problem is to move
within its exact lower-degree fibre while imposing residence, a
seam-compatible chronology, and a lower compiler.  Deeper *support* is not a
separate existence gate: the stronger PBBS theorem below already supplies
it before transport.

The stronger audited PBBS flag theorem also gives correct-window support at
every lower and upper depth on this same factor. It still does not give
minimum positive residence runs or a compatible opening/compiler.

## 2. The incidence-hexagon switch

Subdivide every edge of \(G_f\) by its lower colour. The resulting bipartite
graph lies in the consecutive-level incidence graph between
\(\binom{[k]}{r-1}\) and \(\binom{[k]}r\): every lower-colour vertex has degree
two and every owner vertex has degree two.

Fix \(S\in\binom{[k]}{r-2}\) and distinct \(a,b,c\notin S\). Set

\[
\begin{aligned}
 C_a&=S+a,& C_b&=S+b,& C_c&=S+c,\\
 T_{ab}&=S+a+b,&T_{bc}&=S+b+c,&T_{ca}&=S+c+a.
\end{aligned}
\]

These six vertices form the incidence hexagon

\[
 C_a,T_{ab},C_b,T_{bc},C_c,T_{ca},C_a.
\tag{2.1}
\]

### Proposition 2.1 (legal hexagon move)

Suppose the selected incidences contain

\[
 C_aT_{ab},\quad C_bT_{bc},\quad C_cT_{ca}
\]

and do not already contain the three opposite incidences for the same colour
vertices. Replacing them by

\[
 C_aT_{ca},\quad C_bT_{ab},\quad C_cT_{bc}
\tag{2.2}
\]

preserves every lower-colour degree and every middle-owner degree.
Consequently it preserves the exact lower rainbow and the 2-factor property.
Only the three upper values \(\sigma(C_a),\sigma(C_b),\sigma(C_c)\), the local
component topology, and local run patterns can change.

#### Proof

Every colour vertex in (2.1) loses one selected incidence and gains one.
Every owner vertex does the same. All other incidences are fixed. Contracting
the colour vertices therefore again gives one labelled edge per lower colour
and degree two at every middle owner. \(\square\)

There are no incidence 4-cycles between consecutive Boolean levels: two
distinct \((r-1)\)-sets cannot have two distinct common \(r\)-supersets.
Hence (2.1) is the smallest possible degree-preserving move.  In fact the
finite cycle-space observation has the following all-dimensional proof.

### Proposition 2.2 (hexagons span the binary cycle space)

For every \(0\le q<n\), the cycle space over \(\mathbb F_2\) of the
inclusion graph between ranks \(q\) and \(q+1\) is generated by incidence
hexagons.

#### Proof

For \(q=0\) or \(q=n-1\) the graph is a star, so there is nothing to prove.
For \(1\le q\le n-2\), induct on \(n\).  Separate the vertices according to whether they contain
the last point \(z\).  The graph consists of the two inclusion graphs
\(I(n-1,q)\) and \(I(n-1,q-1)\), joined by the matching

\[
             M_A:A\longleftrightarrow A+z,
                     \qquad A\in\binom{[n-1]}q.       \tag{2.3}
\]

For a binary cycle \(Z\), let \(R\) be the set of \(A\)'s for which \(M_A\)
occurs in \(Z\).  The cardinality of \(R\) is even.  Since the Johnson graph
\(J(n-1,q)\) is connected, choose a binary \(T\)-join \(Q\) in it whose
odd-degree set is \(R\).

If \(AB\) is an edge of \(Q\), write \(A=S+a\), \(B=S+b\).  The hexagon
on \(S,a,b,z\) contains \(M_A,M_B\), the two-edge \(A\)-to-\(B\) path in
\(I(n-1,q)\), and the corresponding two-edge path in
\(I(n-1,q-1)\).  Add these hexagons to \(Z\) for all \(AB\in Q\).  Matching
edge \(M_A\) changes with parity \(\deg_Q(A)\), so all matching edges cancel.
The residue is a cycle in each smaller inclusion graph, and induction
finishes the decomposition. \(\square\)

Thus the symmetric difference of any two balanced factors is algebraically
a sum of hexagons.  This does **not** prove nonnegative fibre connectivity:
the spanning decomposition need not order the hexagons so that every
intermediate toggle has the alternating selected/unselected pattern of
Proposition 2.1.  A legal path may still require neutral sequences or longer
alternating circuits.

### Proposition 2.3 (the unrestricted degree fibre is connected)

Let \(M\) and \(N\) be any two simple degree-two factors in the same
consecutive-level incidence graph.  Then \(M\triangle N\) decomposes into
edge-disjoint circuits alternating between \(M\setminus N\) and
\(N\setminus M\).  Toggling those circuits one at a time gives a legal path
of degree-two factors from \(M\) to \(N\).

#### Proof

At every vertex, the red degree from \(M\setminus N\) equals the blue degree
from \(N\setminus M\), because both full factors have degree two there.
Pair red and blue half-edges locally and follow the pairings.  This partitions
the symmetric difference into alternating circuits.  Toggling one circuit
removes and adds one incidence at every visited vertex, preserving degree
two and simplicity. \(\square\)

In particular, the Middle Levels Theorem supplies a connected target factor,
so every balanced factor can be transported to a Hamilton factor if shadow
and residence constraints are ignored.  Raw component collapse is therefore
unconditional.  The genuine issue is **protected** connectivity: finding a
path or endpoint which also retains the upper decks, residence corridors,
and compiler data.  Hexagons matter because they are the primitive local
generators used by the search, not because longer legal circuits fail to
exist.

The \(k=17\) computation gives the important qualitative fact: strict descent
in the number of missing upper targets stopped at 730 holes, while neutral
hexagon motion crossed the plateau and reached zero. Therefore the useful
general statement is a **plateau-connectivity** statement, not a greedy
descent statement.

## 3. The Pascal four-sector recursion

Write the ground set as

\[
                  [2m+1]=[2m-1]\sqcup\{x,y\}.
\]

The rank-\(r=m+1\) middle layer splits into four sectors

\[
\begin{array}{ll}
 U=\binom{[2m-1]}{m+1},
 &X=\{P+x:P\in\binom{[2m-1]}m\},\\[2mm]
 Y=\{P+y:P\in\binom{[2m-1]}m\},
 &A=\{P+x+y:P\in\binom{[2m-1]}{m-1}\}.
\end{array}
\tag{3.1}
\]

Put

\[
 W_0=\binom{2m-1}m,\qquad
 C=\frac{2}{m+1}W_0=C_m,\qquad
 U_0=W_0-C.
\tag{3.2}
\]

Then

\[
                 |A|=|X|=|Y|=W_0,\qquad |U|=U_0,
\tag{3.3}
\]

and the new middle-layer size is

\[
                 3W_0+U_0=4W_0-C=\binom{2m+1}{m+1}.
\]

The rank-\(m\) lower colours split in the same way: their \(0,x,y,xy\)
signature counts are respectively

\[
                       W_0,\quad W_0,\quad W_0,\quad U_0.
\tag{3.4}
\]

### Proposition 3.1 (component-neutral bridge ledger)

Suppose \(c\le C\), and the \(U\)-sector is partitioned into \(c\) Johnson
paths whose internal intersection colours are distinct. Suppose every path,
including a singleton path, is
bridged as

\[
                     Y_i-U_i-X_i
\]

using two new old-signature colours, and add \(C-c\) direct \(Y-X\) paths.
Assume the internal, bridge, and direct old-signature colours are collectively
distinct. Then:

1. the resulting bank has exactly \(C\) path components, independent of \(c\);
2. it uses every old-signature rank-\(m\) colour exactly once;
3. it uses \(C\) vertices in each of the \(X\) and \(Y\) sectors;
4. all \(W_0\) vertices of \(A\) remain unused, while exactly \(U_0\)
   vertices remain unused in each of \(X,Y\).

#### Proof

The \(c\) paths contain \(|U|-c=U_0-c\) internal edges. Their bridges use
\(2c\) old colours, and the direct paths use \(C-c\). Hence the old-colour
count is

\[
                    (U_0-c)+2c+(C-c)=U_0+C=W_0,
\]

the exact size of the old-signature palette. The remaining assertions follow
from the construction and (3.3). \(\square\)

This identity explains why the number of fragments in the \(k=17\) build was
not a nuisance parameter: after completing the bridge bank, it disappears
from every global count.

## 4. The forced residual three-flow ledger

Attach one distinct \(A\)-vertex to every one of the \(C\) bridge components,
using pairwise-distinct lower colours not already present in the bridge bank.
Let \(p\) attachments use an \(A-X\) edge (an \(x\)-signature lower colour),
and let \(C-p\) use an \(A-Y\) edge.

After these attachments, exactly \(W_0-C=U_0\) vertices remain unused in
each of \(A,X,Y\).  This is the point at which the three unused-sector
counts become equal; it is not true before the \(A\)-attachments.

Every unused vertex in \(A,X,Y\) has residual degree two. Every attached
\(A\)-vertex has residual degree one. Among the used \(X,Y\) vertices, the
attachment-side vertex has residual degree zero and the opposite endpoint has
residual degree one.

### Proposition 4.1 (edge-type counts are forced)

Every residual completion that uses every remaining lower colour exactly once
has exactly

\[
\begin{array}{c|ccccc}
\text{edge type}&AA&XX&YY&AX&AY\\ \hline
\text{number}&U_0&U_0&U_0&C-p&p.
\end{array}
\tag{4.1}
\]

#### Proof

An \(xy\)-signature colour has only \(A\)-owners, so all \(U_0\) such colours
give \(AA\) edges. An \(x\)-signature colour has \(X\)-owners and one possible
\(A\)-owner, so it gives either \(XX\) or \(AX\). There are \(W_0-p\)
remaining \(x\)-colours. The residual \(X\)-degree sum is

\[
                  (C-p)+2U_0=2W_0-C-p.
\]

If \(a\) of the \(x\)-edges are \(AX\), endpoint counting gives

\[
                  a+2(W_0-p-a)=2W_0-C-p,
\]

so \(a=C-p\) and the number of \(XX\) edges is \(U_0\). The \(y\)-sector is
the mirror calculation, giving \(AY=p\) and \(YY=U_0\). The resulting
\(A\)-endpoint count is \(2U_0+(C-p)+p\), exactly its residual demand. \(\square\)

Thus the odd-\(k\) construction has a canonical algebraic core: three
same-shore flows of size \(U_0\), coupled by exactly \(C\) cross edges. The
open issue is not the count but the simultaneous Hall geometry and the
decoration of those flows.

For \(k=17\), \(m=8\),

\[
 W_0=6435,\qquad C=1430,\qquad U_0=5005,\qquad p=715.
\]

The audited construction therefore has

\[
 AA=XX=YY=5005,\qquad AX=AY=715,
\]

exactly as (4.1) predicts.

## 5. The kernel-mass additive-overhead lemma

Let a cyclic carrier component \(Q\) have \(n\) edges. For an upper target
\(Z\) realized by cyclic intervals of \(Q\), define its cut kernel

\[
 B_Q(Z)=\bigcap\{E(I): I\text{ is a cyclic interval of }Q,
                              \ \bigcup I=Z\},
\tag{5.1}
\]

where \(E(I)\) is the edge span of the interval. Cutting an edge \(e\)
destroys every \(Q\)-witness of \(Z\) exactly when \(e\in B_Q(Z)\).

### Lemma 5.1 (average-loss identity)

For a uniformly random cut edge \(e\), the expected number of assigned upper
targets whose witnesses are all destroyed is

\[
                    \frac1n\sum_Z |B_Q(Z)|.
\tag{5.2}
\]

Consequently some cut destroys at most the ceiling of (5.2) targets.

#### Proof

For every target \(Z\), the loss indicator is
\(\mathbf 1_{\{e\in B_Q(Z)\}}\), whose expectation is
\(|B_Q(Z)|/n\). Sum over \(Z\). \(\square\)

For a factor with components \(Q_1,\dots,Q_s\), assign every upper target to
one component that realizes it.  If arbitrary cut tuples are allowed, choosing
the cuts independently gives the corresponding sum of (5.2).  In the actual
carrier problem, however, not every cut tuple need admit Johnson,
residence-safe seams.  Theorem 5.3 therefore uses a distribution supported
only on compatible cut tuples and explicitly controls its marginals.

### Lemma 5.2 (literal repair)

If a word of length \(L\) covers every nonempty target except a family
\(\mathcal D\), appending the members of \(\mathcal D\) as individual letters
gives a universal word of length \(L+|\mathcal D|\).

#### Proof

Every old witness remains a contiguous interval. Each omitted target is now
the union of its one-cell interval. \(\square\)

### Theorem 5.3 (a sufficient theorem for \(B(k)+O(1)\))

Suppose that for every sufficiently large \(k\) there is a protected factor,
with an arbitrary number of components, such that:

1. exactly one edge is cut in each component, and there is a probability
   distribution \(\mathcal D\) supported on the resulting ordered,
   oriented cut tuples with **Johnson and strongly \(d\)-resident** seams;
2. for every component \(Q_i\), every edge \(e\in E(Q_i)\) has marginal
   cut probability
   \[
          \Pr_{\mathcal D}[e_i=e]\le \frac{\alpha}{|E(Q_i)|};
   \tag{5.3}
   \]
3. for every tuple in the support of \(\mathcal D\), a partial exact compiler
   produces a length-\(B(k)\) word \(A\) with \(D^dA=T\) and misses at most
   \(h_0\) lower targets, including any unrecycled cut colours;
4. the upper targets can be assigned to realizing components so that the
   **global normalized kernel mass** satisfies
   \[
       \sum_i\frac1{|E(Q_i)|}
        \sum_{Z\text{ assigned to }Q_i}|B_{Q_i}(Z)|\le M_0.
   \tag{5.4}
   \]

Then

\[
                         \nu(k)\le B(k)+h_0+\alpha M_0.
\tag{5.5}
\]

In particular, if \(h_0,M_0,\alpha\) are absolute constants, then

\[
                         \boxed{\nu(k)=B(k)+O(1)}.
\]

#### Proof

Choose a random compatible tuple from \(\mathcal D\).  For a target \(Z\)
assigned to \(Q_i\), all assigned witnesses are destroyed only if the selected
cut belongs to \(B_{Q_i}(Z)\).  By (5.3), its loss probability is at most
\(\alpha|B_{Q_i}(Z)|/|E(Q_i)|\).  Summing and using (5.4), the expected
number of upper casualties is at most \(\alpha M_0\); hence some compatible
tuple has no more casualties than that.

For this tuple, run the partial compiler.  Because \(D^dA=T\), the union of
any surviving consecutive carrier interval is the union of a consecutive
interval of \(A\), so every surviving upper witness lifts to the compiled
word.  The only uncertified targets are its at most \(h_0\) lower defects and
the bounded upper casualty family.  Append all of them and apply Lemma 5.2.
The general lower bound \(\nu(k)\ge B(k)\) finishes the assertion. \(\square\)

This theorem is deliberately weaker than the exact construction theorem.
Exact equality needs zero upper casualties or a zero-cost seam repair, and it
needs the cut lower colours absorbed inside the existing \(d\)-cell halo.
The additive-constant conjecture needs neither: bounded casualties can be paid
for literally.

The one-cut hypothesis is essential to this kernel calculation.  With
several cuts in one source component, a target is lost when the cut *set*
meets every witness span; this is a transversal event and is not characterized
by membership of one edge in the intersection kernel (5.1).  Multi-cut braids
must use the protected-span formulation of
`MATH_THEOREM_K_ALL_FRAGMENT_BRAID_LOCALITY_AND_SERVICE_20260731.md` instead.

The global form (5.4) is important.  A bounded number of components is a
sufficient way to obtain it, but is not necessary.  There may be many small
components to which no target is assigned because all of their upper values
have witnesses on larger components.  Such components still create lower
seams for the compiler, but they incur no term in the upper cut-kernel ledger.
Thus component count and additive overhead are genuinely different
statistics.

The observed big-component normalized kernel masses are approximately
\(1.000\) at \(k=13\) and \(0.974\) at \(k=15\). Thus the data sit exactly in
the regime of Theorem 5.3 even though the sharper zero-loss union bound is
critical.  A general proof must additionally construct the compatible cut
distribution with bounded marginal distortion \(\alpha\); mere existence of
one legal seam is not enough.  Subject to that explicit interface, this is the
cleanest current explanation for why
\(B(k)+O(1)\) should be substantially easier than \(\nu(k)=B(k)\).

## 6. Current evidence and resulting proof targets

The \(k=17\) four-sector construction has now produced, with independent
literal replay, a balanced surjective two-extension map on all
\(\binom{17}{8}=24310\) lower colours:

* every rank-9 owner has degree two;
* every rank-8 lower colour occurs once;
* every one of the \(\binom{17}{10}=19448\) rank-10 upper targets occurs.

The factor currently has 21 components. A full cyclic-interval replay leaves
only 1,937 deeper upper masks (rank profile
\(11:1572,\ 12:358,\ 13:7\), and none above), but it still has 5,973 short
positive runs of lengths two or three. It is therefore not yet a
length-24313 word.

Retained artifacts:

* factor SHA-256
  `6b24e8ab4c77e3e5711cacab233db29733e1b27c74b735a8fb84c9a1c3643702`;
* extension-map SHA-256
  `4df887b944eba57f3a7a935b5d5df4c6ab6bb3b944f29b3889de7aecc1e748d7`;
* independent factor-audit payload
  `41998e7f1be376b0ad39265c8dfb0915a5289568e61c24aee7873556696b5825`;
* independent extension-map payload
  `9b274c704707ab60d9b3c816f0d193076b63f3cc5d19695521b74268c9d6328c`.

Surjectivity does not force a simple excess design.  Its upper-load
histogram is

\[
  1^{15166},2^{3733},3^{519},4^{29},5^1.
\]

Thus the correct immediate gate is surjectivity, not the stronger and
unnecessary assertion that all upper loads lie in \(\{1,2\}\).

For comparison, the unconditional canonical PBBS map at \(k=17\) has 146
components and upper-load histogram

\[
  1^{14722}\,2^{4590}\,3^{136}.
\]

It already has complete support at every depth, but fails the residence and
bounded-component requirements.  The new 21-component factor is therefore
best read as a transport result inside the same exact degree fibre: it trades
the canonical PBBS chronology for much lower component count while retaining
the two immediate rainbows.

The evidence suggests three distinct theorem targets.

1. **Protected-fibre transport.** Starting from the unconditional PBBS
   all-depth factor, neutral alternating-circuit motion can reduce residence
   defects and component count while retaining or restoring every protected
   deck.  Greedy hexagon descent is false: the \(k=17\) trajectory had a
   strict local minimum at 730 missing upper targets, while neutral motion
   subsequently reached zero.
2. **Protected bounded-component endpoint.** Hexagon/alternating-circuit
   motion can simultaneously impose residence, deeper decks, and \(O(1)\)
   components. This is the concrete form of the protected-factor existence
   statement in the earlier PBBS/Markov reduction.
3. **Bounded normalized kernel mass.** A protected endpoint can be chosen
   with the assigned version of (5.3) bounded by an absolute constant. With
   bounded compiler defect, this alone proves \(B(k)+O(1)\); a zero-loss or
   seam-repair strengthening gives the exact formula.

The closed-form one-coordinate splice

\[
             X,\ \{z\},\ (X\text{ without its last letter})+z
\]

still gives the unconditional recurrence \(\nu(k+1)\le2\nu(k)\), but it
duplicates the entire compiler halo and therefore incurs \(O(d(k))\), not
known \(O(1)\), overhead relative to \(B(k+1)\). The protected-factor route
above is the current route that genuinely distinguishes the additive-constant
conjecture from the already-proved doubling recurrence.
