# PDRC regeneration at the first shadow

Date: 2026-07-25

Pure mathematics only.

This note attacks the regeneration gate in
MATH_ATTACK_LADDER_PRIORITY_OWNER_SCALE_NIBBLE_20260725.md.

Put

\[
W=\binom{2m}{m},\qquad
M=m+H,\qquad
N=\binom{2m}{M},
\tag{0.1}
\]

where

\[
H\sim\sqrt{m\log m},\qquad
MN=W-o(W),
\tag{0.2}
\]

and put

\[
Q=\sqrt{m(\log\log m+\gamma)}\,(1+o(1)),
\qquad
C_m=(\log m)^2.
\tag{0.3}
\]

The enlarged first deadline is

\[
\bar d_1=O(C_m).
\tag{0.4}
\]

## 0. Verdict

The \(q=1\) PDRC problem has an exact structural solution, but the required
object is not supplied by the currently proved two-sided-rainbow forests.

### Positive theorem

If one can choose one carrier-confined packet on \(N-o(N)\) tags so that

* its middle owners are globally disjoint;
* its claimed lower first-shadow colors are globally disjoint;
* its claimed upper first-shadow colors are globally disjoint;
* every packet withholds at most \(C_m\) phase columns at depth one;

then the depth-one deadline/availability part of PDRC regenerates
**exactly** after every bite. Selected
packets simply delete their private owners and private first-shadow colors;
every unselected packet has at most \(C_m\) possibly blocked phase
columns.

This is a theorem, not a density heuristic. It reduces \(q=1\) regeneration
to a carrier-confined two-sided-rainbow packet factor.

### What fails

1. The exact Greene--Kleitman two-sided-rainbow graph on
   \(J(2m,m)\) is branching.  The former claim that its largest linear
   subforest retains only \(W/2\) edges was false.  The exact rooted-tree DP
   values through \(m=7\) are recorded in
   `MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`;
   whether its necessary linearization loss is asymptotically large enough
   to rule out near-complete path packets remains open.
2. A return-free geodesic inside an \(M\)-carrier has at most \(H\)
   edges. Covering \(M\) phase owners by such pieces needs at least
   \[
   \frac{M}{H+1}
   =(1+o(1))\sqrt{\frac m{\log m}}
   \gg(\log m)^2
   \tag{0.5}
   \]
   pieces per tag. The inherited forest colors leave one unresolved
   first-shadow boundary per piece, far beyond \(\bar d_1\).
3. Buffer states can color these boundaries only after a new global,
   carrier-restricted two-sided SDR is proved. Their colors are not
   inherited from the rainbow forest.
4. The near-spanning two-sided-rainbow linear-forest theorem has only an
   \(o(W)\) component bound and no calibrated carrier-support bound. It
   does not imply \(o(N)\) bad tags.

### Higher rows

Depth-one regeneration does not propagate automatically. Two
carrier-confined geodesic triples can have disjoint lower and upper
first-shadow colors while sharing their lower depth-two color. This can be
repeated more than \(\bar d_2=O(\log^2m)\) times on distinct phase columns.
Thus a path can have \(B_1=0\) but \(B_2>\bar d_2\), so no common priority
exists.

The precise remaining theorem is therefore stronger than a \(q=1\)
forest:

> Construct a carrier-confined two-sided-rainbow packet factor on
> \(N-o(N)\) tags, together with a phase-overlap rule ensuring
> \(B_q\le\bar d_q\) for every \(q\le Q\).

The first-shadow forest alone does not close PDRC.

## 1. Exact depth-one requirement

For a base packet \(P\), let \(B_1(P)\) be the number of phase columns
whose lower or upper depth-one target has already been used. The deadline
criterion says exactly

\[
\boxed{B_1(P)\le\bar d_1.}
\tag{1.1}
\]

Since

\[
\bar d_1
=\max\{d_1,\lceil C_m\lambda_1\rceil\}
=(1+o(1))(\log m)^2,
\tag{1.2}
\]

every surviving packet must have

\[
M-O(\log^2m)
\tag{1.3}
\]

phase columns whose two first-shadow colors are unused.

This is a pathwise statement. A global residual containing many unused
first-shadow targets is irrelevant if those targets do not align on the
same carrier path.

## 2. A theorem which regenerates \(q=1\) exactly

### Definition 2.1 (carrier first-shadow packet factor)

Let \(\mathcal T\subseteq\binom{[2m]}M\) be a carrier-tag family. For every
\(U\in\mathcal T\), let \(P_U\) be a positive carrier-confined rotor
object with:

* a middle-owner support \(\mathsf O(P_U)\);
* a good phase set \(\mathsf G(P_U)\);
* the lower first-shadow support \(\mathsf L(P_U)\) on those phases;
* the upper first-shadow support \(\mathsf A(P_U)\) on those phases.

It is a \(C\)-defective carrier first-shadow packet factor if

\[
|\mathsf O(P_U)|=M,
\tag{2.1}
\]

\[
|\mathsf G(P_U)|\ge M-C.
\tag{2.2}
\]

Every phase in \(\mathsf G(P_U)\) contributes both its lower and upper
first-shadow color, and internal row rainbowness gives

\[
|\mathsf L(P_U)|=|\mathsf A(P_U)|=|\mathsf G(P_U)|.
\tag{2.2a}
\]

The three families

\[
\{\mathsf O(P_U):U\in\mathcal T\},
\quad
\{\mathsf L(P_U):U\in\mathcal T\},
\quad
\{\mathsf A(P_U):U\in\mathcal T\}
\tag{2.3}
\]

are separately pairwise disjoint.

The packet may consist of several literally compiled rotor chunks. The
unclaimed depth-one phase columns include all boundary columns whose
dummy colors have not been globally certified.

### Theorem 2.2 (exact first-shadow regeneration)

Suppose there is a \(C_m\)-defective carrier first-shadow packet factor on

\[
|\mathcal T|=N-o(N)
\tag{2.4}
\]

tags, with aggregate literal reset excess \(o(W)\).

Then:

1. the complete packet family has only \(o(W)\) owner holes and
   \(o(W)\) holes in each signed first-shadow row;
2. after selecting any subfamily of packets, every unselected packet has
   \[
   B_1(P_U)\le C_m
   \tag{2.5}
   \]
   relative to the colors used by the selected subfamily;
3. consequently the depth-one deadline/availability part of PDRC
   regenerates exactly under every sequence of bites.

#### Proof

Owner coverage is at least

\[
M(N-o(N))=W-o(W).
\tag{2.6}
\]

The number of claimed lower colors, and separately upper colors, is at
least

\[
(M-C_m)(N-o(N)).
\tag{2.7}
\]

Now

\[
N_1:=\binom{2m}{m-1}
=W-O(W/m),
\tag{2.8}
\]

\[
W-MN=O(WH/m)=o(W),
\tag{2.9}
\]

and

\[
C_mN=O(W\log^2m/m)=o(W).
\tag{2.10}
\]

More explicitly,

\[
\begin{aligned}
0
&\le N_1-(M-C_m)|\mathcal T|\\
&\le |N_1-W|+|W-MN|+C_mN+M(N-|\mathcal T|)
=o(W),
\end{aligned}
\tag{2.11}
\]

which proves the first-shadow hole bounds.

For the regeneration statement, selected packets use only their private
supports in (2.3). These supports are disjoint from every unselected
packet's good-phase supports. Hence a blocked first-shadow color of an
unselected packet can occur only outside \(\mathsf G(P_U)\), on at most
\(C_m\) phases. This proves (2.5), and (1.1) follows after fixing the
constant in the deadline enlargement. \(\square\)

This theorem removes all stochastic degree-regeneration issues at
depth one by replacing the residual random catalogue with a fixed global
packet factor. It does not assert the raw-load clause of Definition 6.1
for the withheld phases; those phases may have repeated raw colors, but
they are permanently assigned height zero. Thus the theorem bypasses,
rather than proves, that unnecessary clause at \(q=1\).

## 3. Audit of the proved two-sided-rainbow forests

### 3.1 Greene--Kleitman is not linear; former quantitative bound retracted

The Greene--Kleitman construction gives an exact two-sided-rainbow graph
on the even middle layer:

\[
e=W-\operatorname{Cat}_m.
\tag{3.1}
\]

It is a forest, but it branches.  Its indegree distribution alone does not
optimize a linear subforest: after deleting a vertex's outgoing edge, two
incoming edges may remain.  Thus the former equations (3.2)--(3.3), including
the asserted \(W/2\) optimum and the resulting linear loss, are withdrawn.

The correct two-state rooted-tree DP is proved in
`MATH_CORRECTION_GK_PROJECTION_LINEAR_SUBFOREST_TREE_DP_20260731.md`.  It
gives exact retained-edge maxima `13,44,159,588,2188` for `m=3,...,7`, but
currently no asymptotic estimate strong enough to compare with the
\(O(\log^2m)\) deadline or an \(o(W)\) reserve.

### 3.2 The near-spanning linear forest has the wrong quantitative data

The conflict-matching construction gives a globally two-sided-rainbow
linear forest with

\[
W-o(W)
\tag{3.4}
\]

edges in its stated adjacent-dimensional setting. Its proof gives neither:

* a component count \(o(W/m)=o(N)\);
* a guarantee that all but \(o(W)\) vertices lie on path intervals whose
  coordinate union has size at most \(M\);
* a grouping of those intervals into one packet on each of
  \(N-o(N)\) prescribed carrier tags.

An \(o(W)\) component estimate by itself is insufficient. For example,
\(W/\log m\) components is \(o(W)\) but is much larger than both \(N\) and
the permitted \(C_mN\) boundary scale relevant to tag packets.

The odd-dimensional theorem also cannot be inserted into the even
carrier catalogue without an additional lift preserving its two color
maps. No such lift is contained in the theorem.

## 4. The carrier-geodesic barrier

A Johnson path

\[
X_0,X_1,\ldots,X_g
\tag{4.1}
\]

is return-free geodesic when every transition inserts a new coordinate
and no inserted coordinate leaves during the segment. Then

\[
\left|\bigcup_{i=0}^gX_i\right|=m+g.
\tag{4.2}
\]

### Lemma 4.1 (carrier length ceiling)

If a return-free geodesic is contained in an \(M=m+H\) carrier \(U\),
then

\[
\boxed{g\le H.}
\tag{4.3}
\]

#### Proof

Equation (4.2) and containment in \(U\) give

\[
m+g\le m+H.
\]

\(\square\)

### Proposition 4.2 (inherited-color boundary obstruction)

Suppose an \(M\)-phase carrier packet is assembled from \(k\) linear
chunks of a globally two-sided-rainbow forest. Suppose only internal
forest edges are used as certified first-shadow phase pairs; boundary
dummy colors are not separately certified.

Then at most

\[
M-k
\tag{4.4}
\]

phase columns have certified lower and upper first-shadow colors.
Consequently a \(C_m\)-defective packet requires

\[
\boxed{k\le C_m.}
\tag{4.5}
\]

If every chunk is return-free geodesic and carrier-confined, then

\[
k\ge\left\lceil\frac{M}{H+1}\right\rceil
=(1+o(1))\frac mH
\gg C_m.
\tag{4.6}
\]

Thus simple chopping of the proved forest into buffered carrier-geodesic
chunks cannot satisfy depth-one PDRC.

#### Proof

A linear chunk with \(v\) owner vertices has only \(v-1\) internal
transitions. Summing over chunks with total \(M\) vertices gives \(M-k\)
certified transition pairs. This proves (4.4)--(4.5). Lemma 4.1 gives at
most \(H+1\) owner vertices per chunk, proving (4.6). Finally,

\[
\frac{m/H}{\log^2m}
=(1+o(1))\frac{\sqrt m}{\log^{5/2}m}
\longrightarrow\infty.
\]

\(\square\)

### Scope

The proposition does not say boundary phases are intrinsically unusable.
A radius-\(Q\) rotor initialization can expose lower and upper dummy flags
at a chunk endpoint. The point is that their two-sided global
rainbowness is a new matching problem. It is not inherited from the
forest theorem.

## 5. Boundary buffers: what can be proved

Ignoring already-used colors and carrier restrictions, endpoint owners
do admit almost-complete one-sided boundary SDRs.

Let \(\mathcal X\subseteq\binom{[2m]}m\). Join
\(X\in\mathcal X\) to every lower facet \(X-\{x\}\), and separately to
every upper cofacet \(X+\{y\}\).

### Lemma 5.1 (unrestricted boundary near-SDR)

There is a subset

\[
\mathcal X'\subseteq\mathcal X
\tag{5.1}
\]

with

\[
|\mathcal X-\mathcal X'|
\le\frac{2|\mathcal X|}{m+1},
\tag{5.2}
\]

such that the members of \(\mathcal X'\) have pairwise distinct selected
lower facets and pairwise distinct selected upper cofacets.

#### Proof

The normalized matching property of the Boolean lattice gives, for every
\(\mathcal A\subseteq\mathcal X\),

\[
|\partial^-\mathcal A|
\ge\frac{N_1}{W}|\mathcal A|
=\frac m{m+1}|\mathcal A|.
\tag{5.3}
\]

The deficiency form of Hall's theorem therefore gives a lower-facet
matching which misses at most

\[
\max_{\mathcal A\subseteq\mathcal X}
\left(|\mathcal A|-|\partial^-\mathcal A|\right)
\le\frac{|\mathcal X|}{m+1}
\tag{5.4}
\]

owners. Apply the same argument to upper cofacets, whose layer has the same
size \(N_1\), and delete the union of the two exceptional owner sets.
The two matchings then coexist on \(\mathcal X'\). \(\square\)

For each retained owner \(X\), independently choosing a matched lower
facet \(X-x\) and upper cofacet \(X+y\) gives a legal Johnson exchange

\[
X\longrightarrow X-x+y.
\tag{5.5}
\]

This lemma shows that boundary completion has no unrestricted marginal
obstruction.

It does **not** solve the buffered carrier problem:

1. the selected cofacet may use \(y\notin U\);
2. the chosen colors may already be internal colors of another forest
   chunk;
3. matching boundary colors can create new endpoints or destroy the
   desired carrier-path ordering;
4. lower and upper matching does not ensure that the exchanges join the
   prescribed chunks.

The relevant residual bipartite graphs are obtained after deleting almost
all colors, and (5.3) need not survive in those residuals.

## 6. The exact \(q=1\) carrier packing gate

Theorem 2.2 reduces q=1 PDRC to the following statement.

### Carrier-confined two-sided-rainbow packet theorem (open)

There are \(N-o(N)\) distinct carrier tags \(U\) and, on each tag, a
positive rotor object \(P_U\) such that:

1. \(P_U\) claims \(M\) distinct middle owners contained in \(U\);
2. \(P_U\) is a union of legal carrier rotor chunks whose total reset
   toll over all tags is \(o(W)\);
3. at least \(M-C_m\) phase columns of \(P_U\) have certified lower and
   upper first-shadow colors;
4. all claimed owners are globally distinct;
5. all certified lower first-shadow colors are globally distinct;
6. all certified upper first-shadow colors are globally distinct.

Theorem 2.2 proves that this statement gives exact depth-one PDRC
regeneration.

Two coefficient-safe subarchitectures are possible.

* **Few chunks:** use at most \(C_m\) inherited-color chunks per tag.
* **Many buffered chunks:** use \(O(M/H)\) geodesic chunks per tag and
  prove a new two-sided-rainbow matching for all boundary dummy colors.
  The reset cost remains
  \[
  N\frac MH Q
  =O(WQ/H)
  =o(W),
  \tag{6.1}
  \]
  but Proposition 4.2 shows that the boundary matching is indispensable.

Neither subarchitecture follows from the existing forest theorem.

## 7. Depth one does not force depth two

The obstruction is already visible in two geodesic edges.

Fix an \((m-2)\)-set \(S\), and choose eight distinct coordinates

\[
a,b,c,d,e,f,g,h\notin S.
\tag{7.1}
\]

Define two three-vertex Johnson paths

\[
\begin{aligned}
P:\quad&
S+ab,\quad S+bc,\quad S+cd,\\
P':\quad&
S+ef,\quad S+fg,\quad S+gh.
\end{aligned}
\tag{7.2}
\]

Their lower first-shadow colors are

\[
S+b,\quad S+c
\tag{7.3}
\]

and

\[
S+f,\quad S+g,
\tag{7.4}
\]

respectively. Their upper first-shadow colors are

\[
S+abc,\quad S+bcd
\tag{7.5}
\]

and

\[
S+efg,\quad S+fgh.
\tag{7.6}
\]

All eight first-shadow colors displayed in (7.3)--(7.6) are distinct.
However,

\[
\bigcap_{X\in P}X
=S
=\bigcap_{X\in P'}X.
\tag{7.7}
\]

Thus the two paths share their lower depth-two color.

Both paths lie in the carrier

\[
S\cup\{a,b,c,d,e,f,g,h\},
\tag{7.8}
\]

whose size is \(m+6\), and hence in an \(M\)-carrier for all sufficiently
large \(m\).

### Proposition 7.1 (no automatic higher-row absorption)

There is no deterministic implication of the form

\[
B_1(P)=0
\quad\Longrightarrow\quad
B_2(P)\le\bar d_2
\tag{7.9}
\]

based only on two-sided first-shadow rainbowness and carrier confinement.

#### Proof

The gadget (7.2) gives a depth-two collision with no first-shadow
collision. Choose a candidate exact-rainbow carrier path and select \(r\)
of its distinct lower depth-two flags. Declare those \(r\) targets used
and declare every first-shadow target of the candidate unused. Then
\(B_1=0\) and \(B_2\ge r\).

For any prescribed

\[
r=O(\log^2m)
\tag{7.10}
\]

each used depth-two target also has a local carrier-confined witness whose
first-shadow colors avoid the corresponding candidate colors: use the
alternative four outside coordinates in (7.2). These local witnesses can
be made mutually first-shadow-disjoint greedily, since at step \(i\) only
\(O(r)\) first-shadow sets have been used while every
\((m-2)\)-core has \(m+2\) available outside coordinates.

For fixed depth two,

\[
d_2\le5
\tag{7.11}
\]

for all sufficiently large \(m\), because

\[
\frac{R_2}{N}
=\frac{\lambda_H}{\lambda_2}
\ge\frac M{\lambda_2}
>M-5.
\]

Also \(\Lambda_2=2+o(1)\), so

\[
\bar d_2=O(C_m).
\tag{7.12}
\]

Choose the constant in (7.10) larger than that in (7.12). Then
\(B_1=0\) but \(B_2>\bar d_2\). \(\square\)

This is a local deadline obstruction. It does not assert that the declared
forbidden family is the complete residual of already selected full
catalogue packets. It proves that a common priority cannot deduce higher
deadline feasibility from depth-one freshness alone. Showing that actual
residuals avoid these gadgets is an additional theorem.

## 8. Consequence for common priority

Common priority has one precise role. Once a base packet satisfies

\[
B_q(P)\le\bar d_q
\qquad(1\le q\le Q),
\tag{8.1}
\]

it can place all first-blocked phase columns below their deadlines
simultaneously. It does not create (8.1).

Theorem 2.2 would make the \(q=1\) deadline inequality stable under every
bite.
Proposition 7.1 shows that the remaining inequalities do not follow.

In geodesic-grid language, first-shadow freshness forbids shared cells on
the two first off-diagonals. Two grids may still meet at distance two or
larger. The product-grid overlap lemma can control these meetings only
after wide shared rectangles are declared additional conflicts. No degree
estimate proving that those conflicts remain sparse under repeated bites
is currently available.

## 9. Final theorem target

The PDRC regeneration problem separates into two genuine construction
theorems.

### PDRC-1

Prove the carrier-confined two-sided-rainbow packet theorem in Section 6.
This gives exact first-shadow regeneration by Theorem 2.2.

### PDRC-\(>1\)

Choose the same packet factor so that, after every selected subfamily, each
unselected packet satisfies

\[
B_q(P)\le\bar d_q
\quad(2\le q\le Q),
\tag{9.1}
\]

or prove the equivalent product-grid rectangle-conflict bound.

The existing two-sided-rainbow forests prove neither statement. Their
first-shadow color injectivity is global, but they lack the carrier packet
structure and the higher-row overlap control.

## 10. Status

The theorem obtained here is exact:

\[
\boxed{
\text{carrier-confined two-sided-rainbow packet factor}
\Longrightarrow
\text{automatic }q=1\text{ deadline regeneration}.
}
\tag{10.1}
\]

The natural attempt to manufacture that factor by chopping the proved
forest into buffered geodesic pieces fails unless a new boundary-color
matching is added. Return-free carrier chunks are too short by the factor

\[
\frac{m/H}{\log^2m}\longrightarrow\infty.
\tag{10.2}
\]

Finally, common priority does not automatically absorb higher rows:
depth-two collisions can be repeated while every first-shadow color remains
fresh.

Therefore constant one is not closed by the current forest. The next
useful proof must construct PDRC-1 itself, rather than invoke the forest
only through its global color counts.
