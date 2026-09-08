# SCD diamond graph, physical-strip criterion, and nested-shadow propagation

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Verdict

Let \(\mathscr S\) be a symmetric-chain decomposition of
\(2^{[2m]}\).  Every \((m-1)\)-set \(R\) lies in a unique chain which has
a two-step segment

\[
 R\subset X\subset U,qquad |X|=m,quad |U|=m+1.
 \tag{0.1}
\]

Associate with it the Johnson edge joining the two middle sets in the
diamond \([R,U]\):

\[
 e_R=\{X,\;R\cup(U\setminus X)\}.
 \tag{0.2}
\]

There are exactly \(N_1=\binom{2m}{m-1}\) distinct such edges.  They cover
every lower and upper depth-one target exactly once as diamond labels, but
they do **not** automatically form cycles on the middle layer.

This note gives exact answers to the two structural questions.

1.  The edges form a 2-factor on the \(N_1\) nontrivial middle-chain
    vertices if and only if a canonical alternative-corner map \(g\) is a
    permutation of those vertices.  More generally, the vertices lying on
    directed cycles of \(g\) are exactly the maximal cycle-supported part of
    the SCD diamond system.  A single escaping orbit may contain
    \(\Theta(W)\) vertices even though the local degree defect is only one;
    hence an \(o(W)\) degree defect is not enough.
2.  A directed component is a physical \(C_{2h}\)-strip if and only if it
    has length \(2h\) and its deletion/insertion labels satisfy one explicit
    antipodal shift identity.  Thus arbitrary SCD cycles cannot simply be
    reinterpreted as strips.

There is, however, a sharp positive conditional theorem.  If the SCD
diamond graph decomposes into physical \(C_{2h}\)-strips and the strip order
agrees with the nested flags of the SCD through depth \(H\), then the
resulting integral strip family attains the SCI fractional optimum **exactly**:

\[
 \tau_{m,H,h}=\tau^*_{m,H,h}
 =W+\frac HhN_1.
 \tag{0.3}
\]

The nested-flag agreement is load-bearing.  First-shadow resolution alone
does not propagate to depth two: two physical strips can have disjoint
depth-one targets while sharing a depth-two target.  The exact remaining
construction is therefore an SCD whose middle diamond map is an almost
physical strip factor and whose chain flags are almost shift-coherent along
those strips.

## 1. The middle maps of an SCD

Let

\[
 \mathcal A_q
 =\{X\in\tbinom{[2m]}m:\text{the SCD chain through }X
                    \text{ reaches rank }m-q\}.
 \tag{1.1}
\]

Every chain has exactly one middle member, and every rank-\((m-q)\) set
belongs to exactly one chain.  Therefore

\[
 |\mathcal A_q|=N_q:=\binom{2m}{m-q}.
 \tag{1.2}
\]

In particular, put \(\mathcal A=\mathcal A_1\), so

\[
 |\mathcal A|=N_1,qquad
 \left|\binom{[2m]}m\setminus\mathcal A\right|
 =W-N_1=\frac{W}{m+1}=o(W).
 \tag{1.3}
\]

For \(X\in\mathcal A\), let

\[
 d(X)\subset X\subset u(X)
 \tag{1.4}
\]

be the rank \(m-1,m,m+1\) segment of its chain, and write

\[
 \alpha(X)=X\setminus d(X),qquad
 \beta(X)=u(X)\setminus X.
 \tag{1.5}
\]

Define the alternative-corner map

\[
 \boxed{g(X)=X-\alpha(X)+\beta(X).}
 \tag{1.6}
\]

Then the edge in (0.2) associated with \(R=d(X)\) is precisely
\(\{X,g(X)\}\).  The map \(X\mapsto d(X)\) is a bijection from
\(\mathcal A\) to the lower first layer, and \(X\mapsto u(X)\) is a
bijection from \(\mathcal A\) to the upper first layer.

### Lemma 1.1 (simplicity and absence of reverse pairs)

The edges \(\{X,g(X)\}\), \(X\in\mathcal A\), are distinct.  Moreover,

\[
 g(X)\ne X,
 \qquad
 g(X)=Y\Longrightarrow g(Y)\ne X.
 \tag{1.7}
\]

#### Proof

The endpoints of a Johnson edge determine its intersection \(R\) and union
\(U\).  In the SCD, \(R\) has a unique middle successor, so two owners
cannot generate the same edge.  A fixed point is impossible because
\(\alpha(X)\ne\beta(X)\).  If \(g(X)=Y\) and \(g(Y)=X\), then the same
diamond \([X\cap Y,X\cup Y]\) would have two different middle successors
in one SCD, again impossible. \(\square\)

## 2. Exact 2-factor criterion and the path obstruction

Direct every edge from its chain-middle owner \(X\) to \(g(X)\).  Every
vertex of \(\mathcal A\) has outdegree one; a middle vertex outside
\(\mathcal A\) has outdegree zero.

### Theorem 2.1 (SCD diamond 2-factor criterion)

The following are equivalent.

1. The SCD diamond edges form a 2-factor on \(\mathcal A\), with the other
   \(W-N_1=o(W)\) middle vertices isolated.
2. \(g(\mathcal A)=\mathcal A\) and \(g:\mathcal A\to\mathcal A\) is
   bijective.
3. Every vertex of \(\mathcal A\) has indegree one and no edge ends outside
   \(\mathcal A\).

When these conditions hold, the components are the directed cycles of the
permutation \(g\), and every component has length at least three.

#### Proof

The undirected degree of \(X\in\mathcal A\) is one plus its indegree, by
Lemma 1.1; a vertex outside \(\mathcal A\) has degree equal to its
indegree.  Thus degree two on \(\mathcal A\) and degree zero outside is
equivalent to condition 3, which is equivalent to the finite map in
condition 2 being a permutation.  The last assertion follows from
Lemma 1.1. \(\square\)

### Corollary 2.1a (simultaneous central-flip normal form)

For every nontrivial chain replace only its middle member \(X\) by the
opposite corner \(g(X)\), leaving its rank-\((m-1)\) and rank-\((m+1)\)
members and every other member unchanged.  Leave every radius-zero
singleton chain unchanged.  The resulting family is a second SCD if and
only if the diamond map \(g\) is a permutation of \(\mathcal A\).

#### Proof

The replacement remains a saturated chain because

\[
                         d(X)\subset g(X)\subset u(X).
\]

All nonmiddle ranks remain partitioned.  At the middle rank the replaced
nontrivial chains use exactly the multiset \(g(\mathcal A)\), while the
unchanged singleton chains use
\(\binom{[2m]}m\setminus\mathcal A\).  These partition the middle layer
exactly when \(g(\mathcal A)=\mathcal A\) without repetition, which is the
permutation condition. \(\square\)

Thus the desired object may equivalently be called a pair of SCDs which
agree at every nonmiddle set and differ only by simultaneously flipping
all central diamonds.  This equivalence also shows why ordinary SCD
existence does not supply the lift: it is a compatibility theorem for two
integral SCDs sharing all their noncentral data.

For a general SCD let

\[
 \operatorname {Cyc}(g)
 =\{X\in\mathcal A:g^j(X)=X\text{ for some }j\ge1\}.
 \tag{2.1}
\]

### Proposition 2.2 (statewise cyclic-core obstruction)

The union of directed cycles supported by the SCD diamond edges has vertex
set exactly \(\operatorname {Cyc}(g)\).  Consequently an
\(o(W)\)-defect cycle factor using these oriented diamond edges exists only
if

\[
 |\mathcal A\setminus\operatorname {Cyc}(g)|=o(W).
 \tag{2.2}
\]

This condition is strictly stronger than an \(o(W)\) local degree defect.
For example, a functional component may be one directed path through
\(N_1\) vertices ending at a vertex outside \(\mathcal A\).  It has only
one missing indegree and one escaping edge, but its cyclic core is empty.

#### Proof

A directed cycle is plainly contained in \(\operatorname {Cyc}(g)\), and
every periodic orbit is a directed cycle.  Conversely, consider an
undirected 2-regular subgraph made from the oriented diamond edges.  On each
of its components the number of selected edges equals the number of
vertices.  Every vertex has at most one outgoing diamond edge, so every
vertex must contribute its outgoing edge.  Hence the component is directed
and all its vertices are periodic.  The path example proves the final
claim. \(\square\)

This is a genuine statewise obstruction: averaging indegrees or proving
small Hall deficiency does not control the mass trapped in long escaping
orbits.

## 3. Which components are physical strips?

Let

\[
 X_0\to X_1\to\cdots\to X_{\ell-1}\to X_0
 \tag{3.1}
\]

be a directed component of \(g\).  Put

\[
 a_t=X_t\setminus X_{t+1}=\alpha(X_t),qquad
 b_t=X_{t+1}\setminus X_t=\beta(X_t).
 \tag{3.2}
\]

### Theorem 3.1 (physical-strip recognition)

The directed component (3.1) is a physical cyclic \(h\)-strip, with its
given orientation, if and only if

\[
 \ell=2h,qquad
 a_0,a_1,\ldots,a_{2h-1}\text{ are distinct},qquad
 b_t=a_{t+h}\quad(t\bmod 2h).
 \tag{3.3}
\]

In that case, with \(z_t=a_t\) and

\[
 K=X_0\setminus\{z_0,z_1,\ldots,z_{h-1}\},
 \tag{3.4}
\]

one has

\[
 X_t=K\cup\{z_t,z_{t+1},\ldots,z_{t+h-1}\}
 \quad(t\bmod2h).
 \tag{3.5}
\]

#### Proof

For a physical strip, transition \(t\) deletes \(z_t\) and inserts
\(z_{t+h}\), so (3.3) is necessary.

Conversely, (3.2)--(3.3) give

\[
 X_{t+1}=X_t-z_t+z_{t+h}.
 \]

Starting from (3.4), induction yields (3.5).  Distinctness of the \(z_t\)'s
gives \(|K|=m-h\), and (3.5) is exactly the physical strip normal form.
\(\square\)

Thus even a perfect SCD diamond 2-factor is insufficient: its component
lengths, deletion labels, and insertion labels must satisfy (3.3).

## 4. Exact nested-flag coherence

For \(X\in\mathcal A_q\), write the segment of its SCD chain as

\[
 D_q(X)\subset\cdots\subset D_1(X)\subset D_0(X)=X
 =E_0(X)\subset E_1(X)\subset\cdots\subset E_q(X),
 \tag{4.1}
\]

where \(|D_j(X)|=m-j\) and \(|E_j(X)|=m+j\).  Define the deletion and
insertion labels

\[
 \delta_j(X)=D_{j-1}(X)\setminus D_j(X),qquad
 \eta_j(X)=E_j(X)\setminus E_{j-1}(X).
 \tag{4.2}

For \(j=1\), these are \(\alpha(X),\beta(X)\).

Suppose a physical component is indexed as in (3.5).  Say that it is
**SCD-coherent through depth \(H\)** if, for every \(t\) and every
\(j\le\min(H,\text{depth of the chain through }X_t)\),

\[
 \boxed{
 \delta_j(X_t)=z_{t+j-1},qquad
 \eta_j(X_t)=z_{t+h+j-1}.}
 \tag{4.3}

### Lemma 4.1 (flag-to-window identity)

Under (4.3), for \(X_t\in\mathcal A_q\), \(q\le H\),

\[
 D_q(X_t)=\bigcap_{i=0}^qX_{t+i},qquad
 E_q(X_t)=\bigcup_{i=0}^qX_{t+i}.
 \tag{4.4}

#### Proof

By (3.5), deleting \(z_t,z_{t+1},\ldots,z_{t+q-1}\) from \(X_t\) leaves

\[
 K\cup\{z_{t+q},\ldots,z_{t+h-1}\}
 =\bigcap_{i=0}^qX_{t+i}.
\]

Equation (4.3) says that these are exactly the first \(q\) downward SCD
deletions.  The upper identity is identical, using the inserted elements
\(z_{t+h},\ldots,z_{t+h+q-1}\). \(\square\)

## 5. Exact integral-optimum theorem

### Theorem 5.1 (SCD-coherent strip factor)

Assume that the SCD diamond graph on \(\mathcal A_1\) is a disjoint union
of physical \(C_{2h}\)-strips, and that every component is SCD-coherent
through depth \(H<h\).  Then the corresponding integral strip family
covers

* every lower and upper target at every depth \(1\le q\le H\);
* every middle target in \(\mathcal A_1\), exactly once;

and it attains

\[
 \boxed{\tau_{m,H,h}=\tau^*_{m,H,h}
 =W+\frac HhN_1.}
 \tag{5.1}
\]

#### Proof

For each \(q\), the map

\[
 X\mapsto D_q(X)
 \]

is a bijection from \(\mathcal A_q\) to
\(\binom{[2m]}{m-q}\), and \(X\mapsto E_q(X)\) is a bijection to the
upper signed layer.  Lemma 4.1 shows that the strip rooted at every
\(X\in\mathcal A_q\) contains these two targets.  Hence both signed layers
are fully covered.

The physical components partition \(\mathcal A_1\), so there are
\(N_1/(2h)\) strips and they cover those middle targets exactly once.  Use
singleton repair on the remaining \(W-N_1\) middle targets.  The cost is

\[
 (2h+2H)\frac{N_1}{2h}+W-N_1
 =W+\frac HhN_1=\tau^*.
\]

The reverse inequality is the SCI dual bound. \(\square\)

The exact hypotheses force \(2h\mid N_1\).  For asymptotic use they may be
relaxed by deleting \(o(W)\) diamond edges and allowing \(o(W)\) flag
mismatches; the SCI near-factor normal form then charges exactly those
middle defects and shadow holes.

Here is the precise relaxed statement.  Let \(\mathcal F\) be any
vertex-disjoint family of physical components of the SCD diamond graph, and
put

\[
 B_0=|\mathcal A_1\setminus V(\mathcal F)|.
 \tag{5.2}
\]

For \(X\in\mathcal A_q\cap V(\mathcal F)\), call the lower (respectively
upper) rooted flag bad when \(D_q(X)\) (respectively \(E_q(X)\)) is not the
corresponding \((q+1)\)-window intersection (respectively union) in its
oriented physical component.  Let \(B_{\rm flag}\) be the number of bad
rooted flags, counting both signs and all \(1\le q\le H\), and also count
both rooted flags for every \(X\in\mathcal A_q\setminus V(\mathcal F)\).

### Corollary 5.2 (approximate coherent SCD criterion)

If

\[
 B_0+B_{\rm flag}=o(W),
 \tag{5.3}
\]

then the whole-strip family \(\mathcal F\) satisfies SCI.

#### Proof

The components are vertex-disjoint, so the middle load is one on
\(V(\mathcal F)\) and zero elsewhere.  Its \(\ell^1\)-distance from the
all-ones vector is

\[
 W-|V(\mathcal F)|=(W-N_1)+B_0=o(W).
\]

At signed depth \(q\), every target has a unique SCD middle owner in
\(\mathcal A_q\).  Unless its rooted flag was counted bad, the target is a
window of the physical component containing that owner.  Hence the aggregate
number of nonmiddle holes is at most \(B_{\rm flag}=o(W)\).  Apply the SCI
near-factor normal form. \(\square\)

## 6. Why depth one does not automatically propagate

The SCD labels every diamond edge, so a diamond 2-factor resolves the two
first-shadow layers.  It says nothing by itself about intersections of
three consecutive middle states.

The local independence can be seen inside physical strips.  Fix an
\((m-2)\)-set \(P\), and choose distinct outside elements
\(a,b,c,d,a',b',c',d'\).  There are physical strips containing respectively
the consecutive triples

\[
 Pab,\quad Pbc,\quad Pcd,
 \tag{6.1}
\]

and

\[
 Pa'b',\quad Pb'c',\quad Pc'd'.
 \tag{6.2}
\]

(Choose a core \(K\subset P\) of size \(m-h\), put the remaining
\(h-2\) elements of \(P\) in the interior of the active window, and extend
the displayed boundary coordinates to a cyclic active order.)  The two
triples have the same depth-two lower target \(P\), while all four displayed
depth-one lower targets

\[
 Pb,\quad Pc,\quad Pb',\quad Pc'
\]

are distinct; their corresponding upper targets are distinct as well.
Thus depth-two collisions can occur without any depth-one collision.

For a complete SCD diamond factor, exact propagation is the set condition

\[
 \{D_q(X):X\in\mathcal A_q\}
 \subseteq
 \left\{\bigcap_{i=0}^qX_{t+i}:t\text{ ranges over all strip positions}\right\},
 \tag{6.3}
\]

and its upper analogue.  The left side is the entire signed layer.
Condition (4.3) is a local sufficient mechanism for (6.3), but (6.3) does
not follow from its \(q=1\) instance.

## 7. Exact remaining construction

The SCD lane reduces coefficient one to the following concrete statement.

> Construct an SCD of \(2^{[2m]}\) such that, after deleting \(o(W)\)
> middle incidences, its alternative-corner map decomposes into physical
> \(C_{2h}\)-strips, and the aggregate number of SCD flag targets not
> realized by the corresponding consecutive strip windows through
> \(1\le q\le H\) is \(o(W)\).

The statewise quantities that decide the lane are:

1. escaping-orbit mass
   \(|\mathcal A_1\setminus\operatorname {Cyc}(g)|\);
2. mass in cyclic components failing the antipodal label condition (3.3);
3. aggregate failure of the nested shift identities (4.3), or more
   generally of the layer-cover inclusions (6.3).

Small indegree defect, the SCD lower--upper bijection, and exact depth-one
coverage do not control any of these three quantities.

## 8. Equivalent radius-resolved recursive object

There is a useful formulation which removes the SCD from the statement and
is suitable for a recursive construction.

For a middle member \(X\) of an SCD, let \(\rho(X)\) be its chain radius.
For a central-band problem truncate it to

\[
 \bar\rho(X)=\min\{\rho(X),H\}.
 \tag{8.1}
\]

The forced radius census is

\[
 \#\{X:\bar\rho(X)\ge q\}=N_q\qquad(1\le q\le H),
 \tag{8.2}
\]

or equivalently

\[
 \#\{X:\bar\rho(X)=d\}=N_d-N_{d+1}\quad(d<H),
 \qquad
 \#\{X:\bar\rho(X)=H\}=N_H.
 \tag{8.3}
\]

### Definition 8.1 (radius-resolved strip kernel)

A radius-resolved \((H,h)\)-strip kernel consists of an owner-disjoint
family of physical \(C_{2h}\)-strips and a radius
\(\bar\rho(X)\in\{0,1,\ldots,H\}\) on every represented middle owner, such
that

1. the radius census is (8.2), up to the declared leave;
2. for every \(q\le H\), the maps
   \[
   X_t\longmapsto\bigcap_{i=0}^qX_{t+i},qquad
   X_t\longmapsto\bigcup_{i=0}^qX_{t+i}
   \tag{8.4}
   \]
   restricted to the positions with \(\bar\rho(X_t)\ge q\) are injective.

In the exact case, (8.2) and injectivity make the two maps in (8.4)
bijections onto the complete signed depth-\(q\) layers.

### Theorem 8.2 (central-band equivalence)

An SCD whose alternative-corner map is a physical strip factor and whose
flags obey (4.3) produces an exact radius-resolved strip kernel.
Conversely, the chain segments

\[
 \bigcap_{i=0}^{d}X_{t+i}\subset\cdots\subset
 X_t\subset\cdots\subset\bigcup_{i=0}^{d}X_{t+i},
 \qquad d=\bar\rho(X_t),
 \tag{8.5}
\]

of an exact radius-resolved kernel are pairwise disjoint and partition every
rank of the central band.  Hence they form a symmetric saturated-chain
decomposition of that band.

#### Proof

The forward implication is Lemma 4.1 and the SCD radius census.  Conversely,
within one segment the inclusions in (8.5) are saturated because one new
coordinate is removed or added at each step.  At a fixed signed depth \(q\),
the eligible positions number \(N_q\) by (8.2), and their images are
distinct by condition 2, so they partition that layer.  Different ranks
cannot collide.  Thus all segments are disjoint and cover the band. \(\square\)

This is the explicit recursive object equivalent to the SCD construction in
the only ranks used by SCI.  Extending it to a full SCD outside the band is
unnecessary for coefficient one, because the exterior is handled by the
factor-blind product-SCD tail word.

For a convenient sufficient construction one may group only centers of the
same truncated radius into strips.  The divisibility loss is harmless: fewer
than \(2h\) centers are left in each of the \(H\) positive radius classes,
so at most

\[
 O(hH)
 \tag{8.6}
\]

middle owners and at most

\[
 O(hH^2)=o(W)
 \tag{8.7}
\]

central-band flags are lost.  Thus a radius-class construction need only be
asymptotically exact; no divisibility condition can obstruct it.

## 9. Why the standard recursive/product SCD does not construct it

The Greene--Kleitman failure is an instance of a larger statewise no-go.

Call an SCD **globally ordered-star** if there is a strict weight function
\(w:[2m]\to\mathbb R\) such that every chain has a representation

\[
 B\subset B+e_1\subset\cdots\subset B+e_1+cdots+e_s
 \tag{9.1}
\]

with

\[
 w(e_1)<w(e_2)<\cdots<w(e_s).
 \tag{9.2}
\]

This includes the usual fixed-priority BTK/Greene--Kleitman construction and
the standard product recursion with one fixed lexicographic factor priority.

### Theorem 9.1 (ordered-star potential obstruction)

The alternative-corner graph of a globally ordered-star SCD is acyclic.
Consequently it has no physical strip component at all: the unmodified
central diamonds supply zero whole strip cycles.

#### Proof

At the middle of (9.1), the alternative-corner move replaces two consecutive
star coordinates \(e_j,e_{j+1}\):

\[
 X\longmapsto X-e_j+e_{j+1}.
 \]

Therefore the potential

\[
 \Phi(X)=\sum_{x\in X}w(x)
 \tag{9.3}
\]

strictly increases on every directed diamond edge.  There are no directed
cycles.  Proposition 2.2 then shows that the original diamond system has
empty cyclic core. \(\square\)

Acyclicity by itself does **not** give a linear edit-distance lower bound: a
long directed path can be closed by one new edge. The corrected
Greene--Kleitman plane-tree DP instead gives the separate matching-edit lower
bound
\[
 \Delta_m=(0.356895867892\ldots+o(1))W,
\]
not the retracted \(W/2\) formula. The theorem here rules out using a standard
ordered product SCD *as is*; it does not rule out a nonlocal rewiring of its
central diamonds.

Thus a successful recursive/product SCD must use genuinely
context-dependent star orders with no common monotone potential.  Merely
changing the block sizes or tensoring more copies of a fixed-priority product
SCD cannot work.

For the canonical BTK decomposition the potential statement has an exact
radius form.  Use the standard parenthesis matching and list the unpaired
positions

\[
                         u_1<\cdots<u_{2d}.
\]

At the middle member of a radius-
\(d\) chain their values are \(1^d0^d\).  Its central predecessor and
successor differ at \(u_d\) and \(u_{d+1}\).  Hence the alternative corner
has the unpaired pattern

\[
                   1^{d-1}\,0\,1\,0^{d-1}.          \tag{9.4}
\]

The consecutive unpaired positions \(u_d,u_{d+1}\) become one new
canonical parenthesis pair, while all old pairs remain paired.  Thus the
alternative corner is the middle member of a radius-\((d-1)\) chain:

\[
                         \rho(g(X))=\rho(X)-1.        \tag{9.5}
\]

In particular every radius-one center is sent to a radius-zero singleton,
and every positive-radius orbit strictly descends to the omitted middle
set.  This proves directly that the BTK diamond map has empty cyclic core.
The statement is unchanged by a coordinate relabelling or by conjugating
with reverse-complement.

## 10. An exact nonmonotone seed on four coordinates

The obstruction in Section 9 is not an obstruction to SCDs in general.  On
\([4]=\{1,2,3,4\}\), consider the six chains

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset14\subset124\subset1234,\\
 2&\subset&12\subset123,\\
 3&\subset&23\subset234,\\
 4&\subset&34\subset134,\\
 &&13,\\
 &&24.
\end{array}
\tag{10.1}
\]

They form an SCD of \(B_4\).  Its four nontrivial central diamonds give

\[
 14\longrightarrow12\longrightarrow23\longrightarrow34
 \longrightarrow14.
 \tag{10.2}
\]

The deletion labels are

\[
 4,1,2,3,
\]

and the insertion labels are

\[
 2,3,4,1.
\]

Thus (10.2) is exactly a physical \(C_4\), with antipodal shift two.  The
chain radii on its four starts are \(2,1,1,1\); the other two middle chains
have radius zero.  Consequently

\[
 \#\{\rho\ge1\}=4=\binom41,
 \qquad
 \#\{\rho\ge2\}=1=\binom40,
 \tag{10.3}
\]

and the consecutive intersections/unions of the cycle realize the complete
SCD flags at every eligible depth.  This is an exact radius-resolved kernel,
including the endpoint depth two.

The seed is also complement-symmetric in the strongest possible labelled
sense available to a single SCD.  Let

\[
                         \pi=(1\ 3)(2\ 4),
 \qquad \vartheta(S)=\pi([4]\setminus S).             \tag{10.4}
\]

Then \(\vartheta\) reverses each of the four nontrivial chains in (10.1),
interchanges the singleton chains \(13\) and \(24\), and fixes each middle
state \(14,12,23,34\).  Consequently it preserves the SCD and commutes
with the diamond permutation (10.2).  The lower flags

\[
                         1,2,3,4
\]

and upper flags

\[
                         124,123,234,134
\]

are each complete exactly once.  Thus a complement-reversal-symmetric SCD
with the desired diamond-lift property exists at \(m=2\); the obstruction
in Theorem 9.1 is specific to globally ordered/fixed-priority SCDs, not to
complement symmetry itself.

The seed proves that a context-dependent star order can create the desired
cyclic projection.  It also identifies why a binary product recursion is too
small: the central slice of a product of two chains is a line, while four
one-coordinate factors already have a three-dimensional central slice and
support (10.2).

Naively tensoring the seed on a fixed list of blocks is nevertheless far too
small.  If \(r\) disjoint four-coordinate blocks are required to have one of
the four cycle states in (10.2), then the number of compatible global middle
sets is exactly

\[
4^r\binom{2m-4r}{m-2r}.
 \tag{10.5}
\]

For \(r=o(m)\), its ratio to \(W\) is

\[
4^{-r}\left(1+o(1)\right)
\sqrt{\frac{m}{m-2r}},
 \tag{10.6}
\]

and is exponentially small when \(r\to\infty\).  Therefore a successful
tensor recursion must choose its local four-coordinate carriers from the
owner context (as in first-eligible packetizations) and then solve the
resulting cross-packet seam problem.  A fixed tensor power of (10.1) cannot
cover a positive fraction of the middle layer.

## 11. The finite recursion identity which would tensor the seed

The preceding seed isolates a concrete composition law.  State it in a form
which separates the finite local issue from the global census.

### Contextual four-child cyclic resolver (CFCR)

Given four already resolved child chain systems and any four child-chain
boxes meeting the global central band, CFCR must choose, as a function of the
four outside child contexts,

1. one of the local four-coordinate cyclic orders conjugate to (10.1);
2. a shore of the eight-coordinate rectangle/24-owner associator whenever
   two adjacent choices disagree;
3. seam pairings which fuse all same-radius remainders *across* child boxes,

so that the following identities hold.

For every global middle owner \(X\) retained by the resolver there is one
outgoing alternative-corner edge, and

\[
 X\mapsto f(X)
 \tag{11.1}
\]

is a permutation on all but \(E_0\) owners.  Its cycles have physical
deletion/insertion words

\[
 a_0,a_1,\ldots,a_{2h-1},qquad b_t=a_{t+h},
 \tag{11.2}
\]

and, for the truncated chain radius \(\bar\rho\),

\[
 \delta_j(X_t)=a_{t+j-1},qquad
 \eta_j(X_t)=a_{t+h+j-1}
 \quad(1\le j\le\bar\rho(X_t)).
 \tag{11.3}
\]

The global radius census, not a boxwise approximation, must be

\[
 \#\{X:\bar\rho(X)\ge q\}=N_q+e_q,
 \qquad
 \sum_{q=0}^H|e_q|=o(W).
 \tag{11.4}
\]

Finally the resolver must satisfy

\[
 E_0+sum_{q=1}^H E_q^{\rm flag}=o(W),
 \tag{11.5}
\]

where \(E_q^{\rm flag}\) counts rooted identities in (11.3) which fail or
are absent.

### Theorem 11.1 (CFCR implication)

An iterated CFCR satisfying (11.1)--(11.5) constructs a radius-resolved
strip kernel and hence proves SCI.

#### Proof

Equations (11.1)--(11.2) give the physical strip components outside
\(E_0\) owners.  Equations (11.3)--(11.4) identify their eligible windows
with the forced SCD flags in every signed rank.  Therefore the number of
middle defects plus aggregate nonmiddle holes is bounded by

\[
 O(E_0)+O\!\left(\sum_q|e_q|\right)
       +O\!\left(\sum_qE_q^{\rm flag}\right)=o(W).
\]

Corollary 5.2, or directly the SCI near-factor normal form, finishes.
\(\square\)

All census and divisibility terms in this implication are now explicit.
The exact Boolean radius law supplies (11.4) before grouping.  Grouping
globally by truncated radius loses only (8.6)--(8.7).  It is essential that
the associator fuse remainders globally: paying a remainder separately in
each four-chain product box can sum to \(\Theta(W)\), and the established
four-box endpoint obstructions show that such independent resets cannot be
hidden in a local error term.

What remains unproved is the CFCR seam identity itself.  The four-coordinate
seed (10.1) verifies it at the first nontrivial scale, and the bounded
24-owner associator supplies an exact owner-preserving change of local shore,
but no current theorem proves the simultaneous global bounds (11.2)--(11.5)
after iterating those shore changes.
