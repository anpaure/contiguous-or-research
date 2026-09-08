# Hall-slack and protected-collar absorbers for the exact \(k=15\) compiler

Date: 2026-07-28

Scope: the resident, all-upper-exact, factorable Hamilton-carrier lane at
\(k=15\), with compiler depth \(d=3\). No claim of a length-\(6438\) word is
made.

## 0. Verdict

There is an exact finite augmenting theorem, but the rule

> make one new neighbour of the displayed DM block

is false, even for a purely monotone one-edge addition. The correct object is
the old **Hall-slack profile** over all target sets. If a successor trade
changes \(s\) compiler-cell neighbourhoods, only old Hall sets of slack at
most \(s\) can obstruct a one-unit augmentation, and the necessary and
sufficient inequalities are explicit below.

For the depth-three compiler, if two Hamilton paths differ at \(t\) successor
sources, their compiler graphs differ by at most

\[
                         s\le 30t+36.                     \tag{0.1}
\]

right-cell neighbourhood replacements. Thus a bounded-support successor
trade has a finite bounded Hall collar. A bounded number of assignment
components is not enough: one component may contain many successor sources.

There is also a stronger constructive criterion. Preserve a maximum matching
outside the changed collar, rematch every displaced old target inside the new
collar while leaving one new cell free, and connect that free cell to the
protected old alternating-reachability set. This produces an actual
augmenting path, so the matching deficiency falls by one and no new block of
the old deficiency can appear.

The exact artifacts show both sides of the distinction.

* A three-source reassignment takes the resident/all-upper Hall-31 carrier
  scratch/k15_outer2_p1_h31_bridge.json to the Hall-30 carrier
  scratch/k15_outer2_p1_h30_bridge.json. Hence equal-deficiency relocation is
  not a universal invariant.
* On the Hall-29 carrier, the eight omitted assignment cycles have total
  successor support \(26\). All \(22\) admissible non-parent settings retain
  the same \(1524-1495\) Hall block and have deficiency \(29\) or \(30\).
  This is a genuine bounded-face obstruction.
* In the full fixed two-parent cube, one admissible seven-cycle state raises
  the old Hall-29 neighbourhood from \(1495\) to \(1795\), but its exact audit
  produces another \(1524-1495\) block. The two full Hall inequalities are
  jointly infeasible in that cube. This proves no Hall-zero carrier there;
  it does **not** rule out Hall \(28\), and it is not a no-go for a third
  parent or a new successor arc.

The exact remaining lane-A lemma is therefore a physical realization of the
protected-collar absorber in Section 5, preferably by giving one of the seven
Hall-29 zero-candidate targets a new collar cell. That realization is not
proved here.

## 1. Compiler graph and deficiency

Let \(G=(L,R;E)\) be any finite bipartite graph. In the compiler,
\(L\) is the family of all lower targets and \(R\) is the family of named
short cells. For \(X\subseteq L\), put

\[
 d_G(X)=|X|-|N_G(X)|,
 \qquad
 h=h(G)=\max_{X\subseteq L}d_G(X).                       \tag{1.1}
\]

The defect form of Hall's theorem gives

\[
                         h(G)=|L|-\nu(G),                 \tag{1.2}
\]

where \(\nu(G)\) is the maximum matching size. Define the old Hall slack

\[
                         \sigma_G(X)=h-d_G(X)\ge0.        \tag{1.3}
\]

For the authoritative Hall-29 carrier,

\[
 |L|=16383,\quad |R|=19311,\quad \nu(G)=16354,
 \quad h=29.                                             \tag{1.4}
\]

The canonical alternating-tree witness has

\[
                         |A|=1524,\qquad |N_G(A)|=1495.   \tag{1.5}
\]

## 2. Exact Hall-slack replacement theorem

Suppose \(G'\) is obtained from \(G\) by replacing the left neighbourhood of
each cell \(y\) in a set \(J\subseteq R\), with \(|J|\le s\). Write the old
and new neighbourhoods of \(y\) as \(C_y,C'_y\subseteq L\). For
\(X\subseteq L\), define

\[
\begin{aligned}
 g(X)&=\#\{y\in J:C_y\cap X=\varnothing,\ C'_y\cap X\ne\varnothing\},\\
 \ell(X)&=\#\{y\in J:C_y\cap X\ne\varnothing,\ C'_y\cap X=\varnothing\}.
\end{aligned}                                            \tag{2.1}
\]

Thus \(g(X)\) and \(\ell(X)\) count, cell by cell, the gained and lost
members of the neighbourhood set of \(X\); they do not count individual
target-cell incidences.

### Theorem 2.1 (exact finite absorber potential)

Put

\[
 \Phi(G,G')=
 \min_{X\subseteq L}
 \bigl[\sigma_G(X)+g(X)-\ell(X)\bigr].                  \tag{2.2}
\]

Then

\[
 \boxed{
 h(G')=h(G)-\Phi(G,G'),
 \qquad
 \nu(G')-\nu(G)=\Phi(G,G').}                            \tag{2.3}
\]

Consequently \(G'\) improves the compiler matching by at least one if and
only if

\[
 \boxed{
 g(X)-\ell(X)\ge 1-\sigma_G(X)
 \quad\hbox{for every }X\subseteq L.}                   \tag{2.4}
\]

Since \(\ell(X)\le s\), sets with \(\sigma_G(X)\ge s+1\) satisfy (2.4)
automatically. Hence it is necessary and sufficient to check the finite
slack layers

\[
                         0\le\sigma_G(X)\le s.           \tag{2.5}
\]

#### Proof

Only cells in \(J\) can change their membership in \(N(X)\), and a cell
contributes \(+1\), \(-1\), or \(0\) exactly as in (2.1). Therefore

\[
 |N_{G'}(X)|-|N_G(X)|=g(X)-\ell(X).                     \tag{2.6}
\]

Using \(d_G(X)=h-\sigma_G(X)\),

\[
 d_{G'}(X)
 =h-\bigl[\sigma_G(X)+g(X)-\ell(X)\bigr].              \tag{2.7}
\]

Maximizing (2.7) over \(X\) proves the first identity in (2.3), and (1.2)
proves the second. The equivalence with (2.4) follows because all quantities
are integral. Finally, if \(\sigma_G(X)\ge s+1\), then
\(\sigma_G(X)+g(X)-\ell(X)\ge1\), proving (2.5). \(\square\)

An equal-deficiency relocation is now completely explicit: it is a set
\(X\) for which

\[
                         \sigma_G(X)+g(X)-\ell(X)=0.     \tag{2.8}
\]

If all old zero-slack sets have been repaired, then any relocated block must
come from an old \(j\)-slack set, \(1\le j\le s\), which loses \(j\) more
neighbour cells than it gains.

## 3. Critical lattice and the one-cell portal

Let

\[
 \mathcal C_h=\{X\subseteq L:d_G(X)=h\}                 \tag{3.1}
\]

be the maximum-deficiency family. The neighbourhood function is submodular,
so \(d_G\) is supermodular. If \(X,Y\in\mathcal C_h\), then

\[
 d_G(X\cap Y)+d_G(X\cup Y)
 \ge d_G(X)+d_G(Y)=2h.                                  \tag{3.2}
\]

Both terms on the left are at most \(h\), so both equal \(h\). Thus
\(\mathcal C_h\) is closed under intersection and union. For \(h>0\), put

\[
 K=\bigcap_{X\in\mathcal C_h}X,
 \qquad
 U=\bigcup_{X\in\mathcal C_h}X.                         \tag{3.3}
\]

Then \(K,U\in\mathcal C_h\), and \(K\ne\varnothing\).

The canonical DM witness produced by alternating reachability from all
unmatched left vertices is exactly \(K\). Indeed, fix a maximum matching
\(M\), orient nonmatching edges from \(L\) to \(R\) and matching edges from
\(R\) to \(L\), and let \(K_M\) be the reachable left set. No reachable
right vertex is unmatched, and matching gives a bijection from its reachable
right set to \(K_M\) minus the \(h\) unmatched left vertices. Hence
\(d_G(K_M)=h\). Conversely, equality in Hall's bound for any
\(X\in\mathcal C_h\) forces \(X\) to contain every \(M\)-unmatched left
vertex and to be closed under these alternating steps. Thus
\(K_M\subseteq X\) for every critical \(X\), proving \(K_M=K\).

### Theorem 3.1 (single monotone portal)

Add one previously absent incidence \(xy\), with \(x\in L\), \(y\in R\),
and delete nothing. Then

\[
 \boxed{
 h(G+xy)=h(G)-1
 \quad\Longleftrightarrow\quad
 x\in K\ \hbox{ and }\ y\notin N_G(U).}                 \tag{3.4}
\]

#### Proof

For a critical set \(X\), its neighbourhood grows precisely when
\(x\in X\) and \(y\notin N_G(X)\). Under a monotone addition, every
noncritical set retains deficiency at most \(h-1\). Hence the global
deficiency falls precisely when every critical set gains the new cell.
The first condition holds for every critical set exactly when \(x\in K\).
The second holds for every critical set exactly when
\(y\notin\bigcup_{X\in\mathcal C_h}N_G(X)=N_G(U)\). One new incidence can
lower each deficiency by at most one, so the drop is exactly one. \(\square\)

This is the sharp correction to “add a neighbour of \(A\)”. Since the
canonical \(A\) is \(K\), an added cell may be new to \(N(K)\) but already
belong to the neighbourhood of a larger critical set. The defect then
remains \(h\).

For example, let \(L=\{a_1,\ldots,a_h,b\}\), \(R=\{r\}\), and let the only
old edge be \(br\). Both

\[
 K=\{a_1,\ldots,a_h\},\qquad U=K\cup\{b\}               \tag{3.5}
\]

have deficiency \(h\). Adding \(a_1r\) gives \(K\) one new neighbour, but
\(U\) still has only the neighbour \(r\), so its deficiency remains \(h\).

## 4. Relocation under two cell transfers

The obstruction persists even if the initial maximum-deficiency set is
unique and every right cell remains nonempty.

Fix \(h\ge1\). Let \(C\) have size \(h-1\), put

\[
 L=C\mathbin{\dot\cup}\{a,b,z\},\qquad
 R=\{r,s,t_1,t_2\},                                     \tag{4.1}
\]

and initially take

\[
 N(r)=N(s)=\{b\},\qquad N(t_1)=N(t_2)=\{z\}.            \tag{4.2}
\]

The unique \(h\)-deficient set is \(A=C\cup\{a\}\), which has no
neighbour. Replace only

\[
                         N(r):\{b\}\mapsto\{a\},
 \qquad N(s):\{b\}\mapsto\{z\}.                         \tag{4.3}
\]

Then \(A\) gains the cell \(r\) and falls to deficiency \(h-1\), but
\(B=C\cup\{b\}\) loses \(r,s\), becomes neighbourless, and has deficiency
\(h\). Initially \(B\) had slack two, and exactly

\[
                         \sigma_G(B)+g(B)-\ell(B)=2-2=0.\tag{4.4}
\]

Thus two singleton-to-singleton cell transfers can repair the unique
canonical block and relocate the whole defect. Neither resident/all-upper
validity nor a gain in \(h_A\) can, by itself, exclude this matching-theoretic
shape.

## 5. Depth-three locality and a protected-collar absorber

Write the middle path as \(P=(V_0,\ldots,V_{n-1})\), and let

\[
 E_i=\bigcap_{j=\max(0,i-3)}^{\min(i,n-1)}V_j            \tag{5.1}
\]

be its maximal linear erosion. A row-depth-\(\ell\) cell
\(c(i,\ell)\), where \(\ell\in\{0,1,2\}\), uses
\(E_i,\ldots,E_{i+\ell}\).

Its envelope is their union. A mandatory coordinate can arise only from a
middle start \(q\in[i-3,i+\ell]\), and its carrier set is decided by
\(V_{q-3},\ldots,V_{q+3}\). Therefore the entire candidate neighbourhood
of \(c(i,\ell)\) is determined by

\[
                         V_{i-6},\ldots,V_{i+\ell+3},    \tag{5.2}
\]

a word of length \(\ell+10\). This also proves directly the exact local
lengths \(10,11,12\) used by the native Hall pricing.

### Lemma 5.1 (successor support to cell-replacement rank)

Let \(P,P'\) be two Hamilton paths on the same middle layer, and let \(t\)
be the number of real vertices whose successors differ. Pair every interior
cell whose rooted word (5.2) lies wholly in a common directed run of the two
successor maps. The paired cells have identical target neighbourhoods.
After pairing, the old and new unpaired cell sets \(J,J'\) have equal size

\[
                         |J|=|J'|=s\le30t+36.            \tag{5.3}
\]

#### Proof

At depths \(0,1,2\), a local word contains respectively \(9,10,11\)
successor arcs. On either path, one changed arc belongs to at most that many
rooted words. Hence at most

\[
                         (9+10+11)t=30t                 \tag{5.4}
\]

interior cells are unpaired on each side. There are exactly six left and
six right boundary cells at each of the three row depths, hence \(36\)
boundary cells total. Discard them all. Common-run words pair bijectively;
the total number of cells at each row depth is the same on both paths, so the
remaining old and new cells can be paired within their depth. This proves
(5.3). \(\square\)

The symmetric-difference incidence is supported on \(2s\) cells, but the
number of neighbourhood replacements in Theorem 2.1 is \(s\), not \(2s\).

### Theorem 5.2 (protected-matching collar absorber)

Use the stable pairing of Lemma 5.1 to identify all unchanged cells of the
old and new compiler graphs \(G,G'\). Let \(M\) be a maximum matching of
\(G\), and put

\[
                         B=\{x\in L:M(x)\in J\}.         \tag{5.5}
\]

Delete \(J\) from the \(M\)-alternating digraph and let
\(\mathcal R_M(J)\subseteq L\) be the targets reachable from the
\(M\)-unmatched targets. Suppose there are

1. a cell \(z\in J'\);
2. a matching
   \[
          \rho:B\hookrightarrow J'\setminus\{z\}
   \tag{5.6}
   \]
   using edges of \(G'\); and
3. a target \(x\in\mathcal R_M(J)\) with \(xz\in E(G')\).

Then

\[
                         \boxed{\nu(G')\ge\nu(G)+1.}     \tag{5.7}
\]

In particular \(h(G')\le h(G)-1\), so no new block of deficiency \(h(G)\)
can form.

#### Proof

Transport every edge of \(M\) whose right endpoint is outside \(J\) through
the stable cell pairing, and use \(\rho\) to rematch all targets in \(B\).
This gives a \(G'\)-matching \(M_0\) of size \(|M|\), with the same unmatched
left targets as \(M\), while \(z\) is free. The alternating path from an
unmatched target to \(x\) uses only unchanged cells and transports to
\(G'\). Append \(xz\) and flip along the resulting augmenting path. The
matching size rises by one. \(\square\)

Condition (5.6) is itself only the bounded collar Hall system

\[
 |N_{G'}(Y)\cap(J'\setminus\{z\})|\ge |Y|
 \qquad(Y\subseteq B),                                  \tag{5.8}
\]

on at most \(30t+36\) cells. This is the desired finite absorber: it
certifies the matching increase directly rather than trying to predict the
next DM block.

If \(x\) is an old zero-candidate target, then it is unmatched under every
maximum matching and belongs to \(\mathcal R_M(J)\) by a path of length zero.
Thus the sharp Hall-29 pilot is:

> create one candidate \(xz\) for one of the seven frozen zero-candidate
> targets, and use the remaining changed cells to rematch the old targets
> displaced from the collar.

## 6. Exact artifact consequences

### 6.1 A bounded positive example already exists

The paths

* scratch/k15_outer2_p1_h31_bridge.json, and
* scratch/k15_outer2_p1_h30_bridge.json

differ in exactly three successor sources. Their directed-edge replacement
is

\[
\begin{aligned}
 &(7529,7537),(3435,3437),(7523,11619)\\
 &\hspace{18mm}\longmapsto
 (7529,3437),(7523,7537),(3435,11619).
\end{aligned}                                           \tag{6.1}
\]

Both paths are Hamilton, depth-three resident, and all-upper exact. Their
matching deficiencies are \(31\) and \(30\), respectively. Therefore this
three-source trade has \(\Phi\ge1\) in Theorem 2.1. It proves that bounded
successor absorption is physically possible at \(k=15\); the Hall-29
plateau is not a conservation law.

The relevant canonical blocks are \(1530-1499=31\) and
\(1528-1498=30\). These data belong to this particular pair and must not be
confused with the separate carrier
scratch/k15_trans1113_balanced_hall31.json, whose canonical witness is
\(1529-1498=31\).

### 6.2 The exact bounded Hall-29 face is closed

The eight assignment cycles omitted by the Hall-29 setting have sizes

\[
                         3,3,4,3,3,3,4,3,                \tag{6.2}
\]

and total successor support \(26\). Exhaustive artifact enumeration gives
exactly \(22\) admissible non-parent settings: \(19\) have deficiency \(29\)
and three have deficiency \(30\). Every one has

\[
                         h_A=1495                        \tag{6.3}
\]

for the original \(1524\)-target Hall-29 block \(A\). Therefore no legal
trade supported on that face adds even one neighbour of \(A\), and no
protected-collar absorber exists there.

### 6.3 What the full two-parent closure does and does not prove

Inside the complete \(691\)-variable two-parent cube, one legal seven-cycle
state has

\[
                         h_A=1795,                       \tag{6.4}
\]

but its exact Hall audit has another \(1524-1495\) DM block \(B\). Thus the
old witness can be escaped very strongly while the global potential (2.2)
remains zero for that exhibited state. Exact Benders separation proves

\[
 \boxed{
 \text{every legal state in this cube has }
 h_A\le1523\ \text{or}\ h_B\le1523.}                    \tag{6.5}
\]

Hence the cube contains no Hall-zero carrier. Condition (6.5) does not
exclude a one-unit descent to Hall \(28\), since a Hall-28 carrier need not
satisfy either full inequality \(h_A,h_B\ge1524\). It also says nothing
about a third parent or genuinely new successor arcs.

## 7. Exact remaining lemma

The minimum positive carrier statement exposed by this audit is:

> **Hall-29 protected-collar successor lemma (open).** There is a
> resident, all-upper-exact, factorable Hamilton carrier \(P'\) differing
> from the Hall-29 carrier in \(t=O(1)\) successor sources, together with a
> maximum matching \(M\) of the old compiler graph, such that the changed
> collars satisfy (5.6) and one remaining new cell satisfies (5.7)'s portal
> condition. Equivalently, it is enough to give one of the seven old
> zero-candidate targets a new cell while the displaced matched collar has
> a matching into the other new cells.

This lemma would lower Hall deficiency from \(29\) to at most \(28\) by a
literal matching augmentation. Iterating it would require the same statement
for each new carrier and its new maximum matching; no monotonicity across
iterations is asserted.

What has been refuted is only the weaker rule “increase the neighbourhood of
the currently displayed DM block.” What has been proved is an exact finite
potential, an exact bounded collar size, and a sufficient matching absorber
which cannot relocate equal deficiency.
