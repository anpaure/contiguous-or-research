# A deterministic companion atlas, and the root-phase cut

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, web
input, or probabilistic existence theorem is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.1}
\]

and assume

\[
 H=o(m),\qquad H\ge3,\qquad M\ge8H+4,
 \qquad \frac WN=(1+o(1))m.
\tag{0.2}
\]

The local move is the three-top collar-neutral re-root packet from
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`.
Its source shore has one \(\omega\)-row and two \(\eta\)-rows, and its
target shore reverses the two placeholders in all three rows.

There are three exact conclusions.

1. There is a completely deterministic resolution of the Johnson top
   triangles which uses no fresh top reservoir and supplies

   \[
          \left(\frac14+o(1)\right)m
   \tag{0.3}
   \]

   distinct potential re-root directions at all but
   \(e^{-\Omega(m)}N\) tops. Its total direction incidence is

   \[
          \left(\frac14+o(1)\right)mN
          =\left(\frac14+o(1)\right)W.
   \tag{0.4}
   \]

2. The resolution has an exact cyclic-word lift. A two-lane reverse
   word makes every selected top triangle literally an
   \(\omega/\eta/\eta\) packet shore; switching a layer changes only
   its local orientation bit, and all layers commute. Thus neither the
   common-core order, the two-base arm assignment, nor companion reuse
   is the obstruction.

3. The lift is not a lift by the actual retained paths. In one literal
   retained-path state the near placeholder is in rooted position
   three. Consequently successive direction pairs at a top must form a
   label walk. In the deterministic resolution the direction pairs at
   each top are disjoint, so they form a matching. It therefore needs
   one rooted source component for every direction. The aggregate
   number of required root interfaces is

   \[
          \left(\frac14+o(1)\right)W.
   \tag{0.5}
   \]

   Hence this natural resolvable triangle construction has a positive
   coefficient-scale interface toll. The same conclusion holds for
   every product of disjoint bounded-size triangle or tetrahedron
   carriers.

There is a complementary exact Latin-square construction. On one fixed
\((M-2)\)-core it gives \(q=\Theta(m)\) perfectly compatible packet
rounds, with no root interface at all. But every top repeats the same
two-label direction in every round. Thus the two simplest deterministic
mechanisms lie on opposite sides of the exact tradeoff:

\[
\begin{array}{c|c|c}
\text{construction}&\text{literal source reuse}&
                    \text{distinct directions per top}\\ \hline
\text{fixed-core Latin resolution}&\text{yes}&1\\
\text{disjoint-block resolution}&\text{root-free yes, rooted no}
                                  &\Theta(m).
\end{array}
\tag{0.6}
\]

The remaining combinatorial lemma is therefore not an ordinary
triangle factorization. One needs a changing-core triangle resolution
whose direction graph at almost every top has \(o(m)\), preferably one,
components, together with a simultaneous common-core word chart. This
is stated precisely in Section 7.

## 1. The exact root-walk condition

A current state on a top \(U\) is not merely a cyclic order. It is a
rooted retained path. In the collar-neutral packet, the retained
\(\omega\)-word starts two letters before placeholder \(A\), and the
retained \(\eta\)-word starts two letters before placeholder \(B\).
Thus in all three source rows the active tail label is in rooted
position three.

On one top the local transition has the form

\[
 (r_1,r_2,x,\ldots,y,\ldots)
       \longmapsto
 (r_1,r_2,y,\ldots,x,\ldots).
\tag{1.1}
\]

The rooted origin and every position are fixed; only \(x,y\) are
interchanged.

### Lemma 1.1 (root-walk lemma)

Consider an uninterrupted sequence of literal three-top re-root
packets at one fixed top, with no intervening change of the retained
path root. If its successive distinct label directions are

\[
                         e_1,e_2,\ldots,e_s\in\binom U2,
\tag{1.2}
\]

then they admit orientations

\[
                         e_i=(v_{i-1},v_i)
\tag{1.3}
\]

for one label walk \(v_0,v_1,\ldots,v_s\) in \(U\). In particular,
consecutive direction pairs intersect.

More generally, if a family \({\cal E}_U\subseteq\binom U2\) is
realized using \(r_U\) rooted source components, then

\[
                         r_U\ge c(G_U),
\tag{1.4}
\]

where \(G_U=(U,{\cal E}_U)\) and \(c(G_U)\) is the number of its
nonempty connected components.

#### Proof

Before the first switch, position three contains some label \(v_0\).
The first direction must be \(\{v_0,v_1\}\), because one of its two
placeholders is at position three. After (1.1), position three contains
\(v_1\). Induction gives (1.3). Every uninterrupted sequence is
therefore contained in one connected component of \(G_U\), which
proves (1.4). \(\square\)

This is stronger than the column-histogram invariant. It is a dynamic
condition on the order of the packet incidences. A top-support
factorization does not see it.

## 2. A deterministic resolution with linear distinct-direction load

Partition all but \(s\le2\) coordinates into triples

\[
 [n]=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_b
       \mathbin{\dot\cup}R,
 \qquad |B_j|=3,\quad b=\lfloor n/3\rfloor.
\tag{2.1}
\]

For a top \(U\), write

\[
                         \alpha_j(U)=|U\cap B_j|.
\tag{2.2}
\]

Fix \(j\). For every \((M-2)\)-set
\(C\subseteq[n]\setminus B_j\), the three tops

\[
                         C\cup e,
              \qquad e\in\binom{B_j}{2},
\tag{2.3}
\]

form one Johnson triangle. As \(C\) varies, these triangles are
top-disjoint and partition exactly the tops with \(\alpha_j(U)=2\).
Thus (2.3) is an explicit triangle factor of that entire occupancy
stratum. No matching theorem is being invoked.

Put

\[
                         X(U)=\#\{j:\alpha_j(U)=2\}.
\tag{2.4}
\]

### Lemma 2.1 (exact first moment)

One has

\[
 \sum_{U\in\binom{[n]}M}X(U)
       =3b\binom{n-3}{M-2},
\tag{2.5}
\]

and hence

\[
 \frac1N\sum_U X(U)
   =b\frac{3M(M-1)(n-M)}{n(n-1)(n-2)}
   =\left(\frac14+o(1)\right)m.
\tag{2.6}
\]

#### Proof

For each fixed block, choose its two present labels in three ways and
the other \(M-2\) labels outside it. Summing over the \(b\) blocks gives
(2.5). The factorial simplification gives (2.6). \(\square\)

### Lemma 2.2 (concentration, by counting)

There is an absolute \(c>0\) such that

\[
 \#\left\{U:\left|X(U)-\frac{3b}{8}\right|>\frac b{20}\right\}
                         \le e^{-cm}N.
\tag{2.7}
\]

#### Proof

Take independent Bernoulli variables of parameter \(p=M/n\) on the
\(n\) coordinates. The events that a block has occupancy two are
independent across blocks, with probability

\[
                         3p^2(1-p)=\frac38+o(1).
\tag{2.8}
\]

The elementary exponential-moment bound for a sum of independent
\(0\)-\(1\) variables gives an \(e^{-\Omega(b)}\) tail outside the
interval in (2.7). Conditional on total size \(M\), the set is uniform
on \(\binom{[n]}M\). Stirling's inequalities give

\[
             \Pr\{\operatorname{Bin}(n,p)=M\}\ge c_0n^{-1/2}.
\tag{2.9}
\]

Conditioning therefore multiplies the tail by at most \(O(\sqrt n)\),
which is still \(e^{-\Omega(m)}\). This is a counting argument for a
fixed deterministic block partition, not a random choice of the
resolution. \(\square\)

Thus the fixed block partition already supplies \(\Theta(m)\) distinct
top directions at almost every top. The companions in (2.3) are other
members of the same fixed top universe and are reused in all later
block layers.

## 3. An exact cyclic-word lift of every block layer

We now verify the word state, before restoring the retained root.

Give every triple \(B_j\) a cyclic orientation. If
\(B_j=\{x,a,y\}\), write it as

\[
                         x\longrightarrow y\longrightarrow a
                           \longrightarrow x.
\tag{3.1}
\]

For each occupancy vector
\(\alpha=(\alpha_1,\ldots,\alpha_b)\), attach an orientation bit
\(\epsilon_j(\alpha)\in\{+,-\}\) whenever \(\alpha_j=2\). Reversing
the bit reverses all three edges of (3.1).

For a top \(U\) with occupancy vector \(\alpha\), make two local lane
words \(A_j(U),D_j(U)\) as follows.

* If \(\alpha_j=2\), orient its present edge using
  \(\epsilon_j(\alpha)\), put its tail in \(A_j(U)\), and its head in
  \(D_j(U)\).
* If \(\alpha_j\ne2\), put the labels of \(U\cap B_j\), in a fixed
  order, in \(A_j(U)\), and put nothing in \(D_j(U)\).

Define the cyclic word

\[
 \Pi_\epsilon(U)=
 A_1(U)A_2(U)\cdots A_b(U)\,(U\cap R)\,
 D_b(U)D_{b-1}(U)\cdots D_1(U).
\tag{3.2}
\]

Empty local words are simply omitted.

Fix an active block \(B_j\). If \(u\in A_j(U)\) and
\(v\in D_j(U)\) are its two present labels, then the two open cyclic
gaps between them contain exactly

\[
 \ell_j(U)=\left|U\cap\bigcup_{i<j}B_i\right|,
 \qquad
 r_j(U)=\left|U\cap\left(R\cup\bigcup_{i>j}B_i\right)\right|
\tag{3.3}
\]

labels. This is the reason for reversing the second lane.

Call the occurrence \((U,j)\) admissible when

\[
                         \ell_j(U),r_j(U)\ge 4H+1.
\tag{3.4}
\]

### Lemma 3.1 (only \(O(H)\) bad directions per top)

For every top \(U\), at most \(4H+2\) indices counted by \(X(U)\)
fail (3.4).

#### Proof

List the active indices increasingly. Before the \(k\)-th active
block, the earlier active blocks alone contribute \(2(k-1)\) labels to
\(\ell_j(U)\). Hence fewer than \(2H+2\) active blocks can have
\(\ell_j(U)<4H+1\). The reverse argument gives the same bound for
\(r_j(U)\). Adjusting the two endpoint roundings gives the displayed
bound. \(\square\)

### Theorem 3.2 (literal unrooted packet shore)

Fix an occupancy vector \(\alpha\), an admissible block \(B_j\) with
\(\alpha_j=2\), and all actual labels outside \(B_j\). The three cyclic
words (3.2) on the tops (2.3) are exactly one shore of a common
collar-neutral packet. Switching that packet reverses
\(\epsilon_j(\alpha)\) and leaves every other local bit fixed.

Consequently all admissible block layers concatenate exactly as cyclic
word tables, in any order.

#### Proof

Deleting the two \(B_j\)-labels from any of the three words leaves the
same labelled cyclic word on \(C\). The two insertion gaps are also the
same. By (3.4), both intervening core arcs have at least \(4H+1\)
labels. On each arc take the two end arms of length \(2H-1\); at least
three filler labels remain. This parses the common core into the arms
and fillers of the bases \(\omega,\eta\).

Write the oriented block as in (3.1). The three induced cyclic words at
the two gaps are

\[
                         xP yQ,\qquad aP xQ,\qquad yP aQ,
\tag{3.5}
\]

for the two common core arcs \(P,Q\). The first is
\(\omega^+(x,y)\). After cyclic rotation, the second is
\(\eta^+(x,a)\), and the third is \(\eta^+(a,y)\). Thus (3.5) is
exactly the old packet shore. Reversing the three oriented edges gives
the three minus states, hence flips precisely
\(\epsilon_j(\alpha)\).

For a later block \(B_k\), its three tops have identical actual labels
and identical occupancy data outside \(B_k\). Any earlier admissibility
decision and bit flip depends only on that common data. Their
restrictions off \(B_k\) therefore remain literally equal. Hence the
same argument applies after any preceding layers, and the layers
commute. \(\square\)

This theorem audits the strongest static source conditions: the
position pair is common, the core word is common, the \(\omega/\eta\)
roles are correct, and all arm labels agree. It is not merely a
top-support or marginal statement.

## 4. Exact direction and helper ledger

Let

\[
 A(U)=\#\{j:\alpha_j(U)=2\text{ and }(U,j)
                         \text{ satisfies }(3.4)\}.
\tag{4.1}
\]

Lemmas 2.1 and 3.1 give

\[
 \begin{aligned}
 \sum_U A(U)
  &\ge 3b\binom{n-3}{M-2}-(4H+2)N\\
  &=\left(\frac14+o(1)\right)mN
   =\left(\frac14+o(1)\right)W.
 \end{aligned}
\tag{4.2}
\]

The opposite inequality with \(X(U)\) shows equality in the asymptotic
form. Lemma 2.2 shows that all but \(e^{-\Omega(m)}N\) tops have
\(A(U)=\Theta(m)\).

For every fixed block and occupancy vector, (2.3) is a disjoint packet
factor. Hence every helper top used by one packet is itself a focal or
helper top in many other block layers. There is no fresh-helper forest:
the total number of top incidences is exactly the left side of (4.2),
distributed on the original \(N\) tops with average \(\Theta(m)\).

Thus the companion-source allocation is solved at the unrooted cyclic
word level.

## 5. Why the retained paths do not concatenate

For one admissible block \(B_j\), Theorem 3.2 becomes the actual local
packet after rooting each of its three cyclic words two positions before
the oriented tail in \(A_j(U)\). This root depends on \(j\).

At a fixed top, the direction pairs

\[
                         \{U\cap B_j:(U,j)\text{ is admissible}\}
\tag{5.1}

are pairwise vertex-disjoint, because the coordinate blocks are
disjoint. Therefore their direction graph is a matching with exactly
\(A(U)\) nonempty components.

### Theorem 5.1 (positive-scale root-phase cut)

Any realization of all directions (5.1) by the actual rooted
collar-neutral packets needs at least \(A(U)\) rooted source components
at top \(U\). Aggregated over all tops, it needs

\[
                         \sum_U A(U)
                  =\left(\frac14+o(1)\right)W
\tag{5.2}
\]

root components.

#### Proof

Apply Lemma 1.1 to the matching (5.1), and then sum (1.4) over tops.
Equation (4.2) gives (5.2). \(\square\)

After one block switch, the underlying cyclic word is exactly the
source word required by every later block, but the retained phase starts
at the wrong place. This is a literal state inequality: the two path
states have different first owner and different retained phase set.
No relabelling of the packet shore removes it.

Accordingly, if each change of retained root has even one unit of
unshared interface cost, the construction incurs \(\Omega(W)\) excess
and cannot prove coefficient one. The theorem does not claim that every
possible multi-top root-change mechanism costs one unit; it proves that
such a mechanism must itself cancel a positive \(W\)-scale family of
root changes. The local three-top packet alone does not do so.

The owner ledger stops at exactly the same point. One packet preserves
its \(3d\) middle owners, and replacement inside an already squarefree
table is safe. But the cyclic atlas does not select one common retained
path per top across its block layers, so it does not by itself furnish a
coefficient-one owner table.

## 6. Latin squares and bounded tetrahedron products

### 6.1 A perfectly compatible fixed-core Latin schedule

Fix one \((M-2)\)-set \(D\). In the complement of \(D\), take three
disjoint copies \(X,Y,Z\) of an abelian group \(G\), \(|G|=q\). Use
the three classes of tops

\[
                         D+xy,\qquad D+yz,\qquad D+zx.
\tag{6.1}
\]

Orient every pair by

\[
                         X\longrightarrow Y\longrightarrow Z
                           \longrightarrow X.
\tag{6.2}
\]

For \(t\in G\), take all packets

\[
                         (x,y,z),\qquad z=x+y+t.
\tag{6.3}
\]

For fixed \(t\), (6.3) partitions every edge top in (6.1) once: the
third coordinate is uniquely recovered from either two incident
coordinates. Every triangle is cyclic under (6.2), so one common
two-gap chart on \(D\) makes it an exact packet shore. Switching the
whole factor reverses every edge orientation. The next factor is again
cyclic, with the opposite shore. Thus all \(q\) Latin factors are exact
successive rooted source tables; no interface or helper reset occurs.

However, a top \(D+uv\) has the same active pair \(\{u,v\}\) in every
factor. It alternates the same two rooted states. Its number of distinct
re-root directions is exactly one. The Latin schedule solves recurrence
but has no direction entropy.

### 6.2 Bounded coordinate carriers

Partition the coordinates into blocks of size at most \(r\), and
suppose every selected direction at a top lies in one coordinate block.
If \(E(U)\) directions are selected at \(U\), then its direction graph
has at least

\[
                         \frac{E(U)}{\binom r2}
\tag{6.4}
\]

nonempty components. Indeed, one block contains at most \(\binom r2\)
distinct directions and different blocks have disjoint label sets.

For every fixed \(r\), a design with \(E(U)=\Theta(m)\) therefore has
\(\Theta(m)\) rooted components at a typical top and \(\Theta(W)\)
components globally. This includes disjoint triangle blocks
\((r=3)\), tetrahedron blocks \((r=4)\), and every finite product of
such bounded carriers. A tetrahedral monodromy may connect the three
labels inside one block, but it cannot move the root token to another
coordinate block without a new interface.

Thus enlarging a triangle to a fixed tetrahedron does not repair the
coefficient-scale defect. A successful block hierarchy must have a
growing carrier and must explicitly connect the local direction graphs.

## 7. The exact remaining deterministic lemma

For a packet support

\[
 P=(C;x,a,y),
\tag{7.1}
\]

write

\[
 e_{C+xy}(P)=xy,\qquad e_{C+xa}(P)=xa,
 \qquad e_{C+ay}(P)=ay.
\tag{7.2}
\]

The required support object is the following.

> **Rooted Johnson triangle resolution (RJTR).** Select and order
> packet supports so that:
>
> 1. all but \(o(N)\) tops have \(\Theta(m)\) distinct incident
>    direction edges (the near-full coefficient-one form asks for
>    \(m-o(m)\));
> 2. the direction graph \(G_U\) at every retained top has
>    \(o(m)\) connected components, with aggregate
>    \(\sum_Uc(G_U)=o(W)\);
> 3. every component is given a trail order, and on every packet the
>    three current trail edges are oriented cyclically;
> 4. these local trail orders admit one global chronology; and
> 5. at every occurrence the three current cyclic words have one
>    common deleted-core order and the same two admissible insertion
>    gaps, so that the oriented tails are their actual rooted
>    position-three labels.

Conditions 2--3 are forced by Lemma 1.1. Condition 5 is the exact
\(\omega/\eta/\eta\) source test proved in Theorem 3.2, not an average
degree condition. Given RJTR and a squarefree initial owner table
containing its source paths, the local packet theorem switches the
chronology with zero protected-depth derivative and preserves the
middle owner set at every step.

The constructions above settle the two projections separately:

* the block atlas satisfies conditions 1 and 5 but violates condition
  2 on \((1/4+o(1))W\) incidences;
* the fixed-core Latin atlas satisfies the rooted recurrence and chart
  requirements in conditions 2--5 but violates condition 1, having one
  distinct edge per top.

Therefore RJTR, rather than another ordinary resolvable triangle
decomposition, is the first genuinely missing combinatorial lemma. A
positive construction must use changing cores on a growing carrier so
that the same rooted token walks through linearly many labels while the
two companion trails remain synchronized. No bounded triangle,
tetrahedron, or fixed-core Latin template can do this.

## 8. Exact implication boundary

Proved here:

1. a deterministic top support with \(\Theta(m)\) distinct directions
   per typical top and full helper reuse;
2. an exact common-core cyclic-word lift of every selected packet;
3. the exact aggregate direction count
   \((1/4+o(1))W\);
4. the root-walk necessity for all literal retained-path chronologies;
5. an exact \((1/4+o(1))W\) root-interface cut for the block atlas;
6. a perfectly recurrent fixed-core Latin source schedule and its
   one-direction obstruction; and
7. the bounded triangle/tetrahedron product no-go.

Not proved here:

1. RJTR on a growing changing-core carrier;
2. a zero-cost global mechanism cancelling the root interfaces in
   (5.2); or
3. a coefficient-one squarefree owner factor containing the resulting
   rooted packet chronology.

The companion shortage is therefore not a shortage of tops or cyclic
orders. It is the need to make the distinguished rooted label move
coherently through the same high-degree changing-core resolution on all
three shores.
