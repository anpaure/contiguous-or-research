# A context-phased parity compiler and the breaking of fixed-strength blind atoms

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Outcome

Let

\[
                         n=4\cdot2^t,
 \qquad R=2n.
\]

There is a genuinely different recursive parity-complete compiler obtained
by replacing the old child selector \(|x|\pmod2\) with

\[
                         |x|+|p|\pmod2
\]

at every internal recursion node.  Explicitly, if \(n=2h\),
\(p=(p_0,p_1)\), and \(x=(u,v)\), put

\[
 \widehat F_{n,p}(u,v)=
 \begin{cases}
  (\widehat F_{h,p_0}(u),v),
       &|u|+|v|+|p_0|+|p_1|\equiv0\pmod2,\\
  (u,\widehat F_{h,p_1}(v)),
       &|u|+|v|+|p_0|+|p_1|\equiv1\pmod2.
 \end{cases}                                      \tag{0.1}
\]

At \(n=4\), use the same audited \(Q_4\) seed
\(F_{4,p}\) as the diverse-order compiler.

This modification preserves all exact local gates.

1. Every row \(\widehat F_{n,p}\) is a factor into isometric
   \(C_{2n}\)'s with doubled-permutation direction words.
2. For every source \(x\), the full context column

   \[
    p\longmapsto p\oplus e_{\widehat d_{n,p}(x)}
   \]

   is a parity-reversing permutation of \(Q_n\).
3. The forward and reverse joint aligned traces are injective through
   coarse depth \(n/4\).
4. The paired physical lift is an exact \(C_{4n}=C_{2R}\)-factor of
   \(Q_{2n}=Q_R\), with literal two-sign, two-orientation trace
   injectivity through physical depth \(n/2-1=R/4-1\).

The compiler is not a conjugate of the old context array under the affine
relabelings which preserve the paired compiler interface.  In the old
array, for fixed \(x\), varying \(p\) can change the first direction only
inside one fixed bottom \(Q_4\)-leaf.  In (0.1), varying the dyadic
parities of \(p\) routes the first move to every bottom leaf in one root
half.  The first-direction context range grows from at most four to at
least \(n/8\).  Thus (0.1) is not an old affine option with its columns
permuted or complemented; it changes the context/source incidence array
before the physical affine orbit is taken.

Most importantly, (0.1) breaks the old fixed-strength blind atoms.  If a
window visits \(d\) bottom leaves, the old recursion was blind to every
even context change on all unvisited leaves.  Its type-\(2t\) atom was
\(4^{-t}+o(1)\).  Under (0.1), preserving the same leaf schedule forces
even parity separately in a dyadic frontier of blind cells.  If their
coarse-coordinate sizes are \(s_1,\ldots,s_b\), then

\[
                         \sum_js_j^2=O(n^2/d),       \tag{0.2}
\]

and the number of weight-\(2t\) context shifts in the blind kernel is

\[
                         O_t((n^2/d)^t).             \tag{0.3}
\]

Relative to the ambient physical shell this contributes only

\[
 \boxed{
                         O_t(4^{-t}d^{-t})}          \tag{0.4}
\]

instead of \(4^{-t}+o(1)\).  At a Gaussian window
\(q=A\sqrt m\), one has \(d=\Theta(q)\), so every fixed-strength atom
from the old unvisited-context flat tends to zero polynomially.

The new compiler still has exponential blind cells: a length-\(q\)
binary schedule reads only the dyadic parity tests on its visited search
forest.  Thus this theorem breaks the constant higher atoms but does not
prove a global near-cover or show that the complete new enumerator has no
other atoms.  The exact new enumerator is obtained from the old transfer
by replacing every scheduling bit \(c\) with \(c\oplus\kappa\).

## 1. Exact row factorhood

Write

\[
                         \epsilon(z)=|z|\pmod2.
\]

For a fixed row context \(p\), the selector in (0.1) is

\[
                         s_p(x)=\epsilon(x)\oplus\epsilon(p).
                                                               \tag{1.1}
\]

Every cube-neighbour move toggles \(\epsilon(x)\), while \(p\) is fixed
along the row.  Therefore successive moves alternate the two children.
The child maps act on disjoint coordinates, so

\[
 \boxed{
 \widehat F_{n,p}^{2}(u,v)
 =\bigl(\widehat F_{h,p_0}(u),
        \widehat F_{h,p_1}(v)\bigr).}              \tag{1.2}
\]

### Theorem 1.1 (row cycles)

Every component of \(\widehat F_{n,p}\) is an isometric
\(C_{2n}\), and its direction word is \(\pi\pi\) for a permutation
\(\pi\) of the \(n\) coordinates.

#### Proof

The seed has this property.  Suppose it holds at \(h\).  Equation (1.2)
shows that an even parent return requires simultaneous returns in both
children.  Both child points have exact period \(2h\), so the first parent
return occurs after \(4h=2n\) moves.  Odd return times are impossible by
cube parity.

During the first \(n=2h\) parent moves, each child makes \(h\)
consecutive child moves.  Any \(h\) consecutive letters in a child word
\(\sigma\sigma\) contain every child coordinate exactly once.  Hence the
first \(n\) parent directions form a permutation of all \(n\)
coordinates.  The child direction phases and the left-right alternation
then repeat, giving the same permutation in the next \(n\) moves.
\(\square\)

## 2. Exact full-column bijectivity

Let \(\widehat d_{n,p}(x)\) be the outgoing direction and define

\[
 \widehat\Theta_{n,x}(p)
 =p\oplus e_{\widehat d_{n,p}(x)}.                 \tag{2.1}
\]

For \(x=(u,v)\), the recursion is

\[
 \widehat\Theta_{n,(u,v)}(p_0,p_1)=
 \begin{cases}
  (\widehat\Theta_{h,u}(p_0),p_1),
       &\epsilon(x)\oplus\epsilon(p)=0,\\
  (p_0,\widehat\Theta_{h,v}(p_1)),
       &\epsilon(x)\oplus\epsilon(p)=1.
 \end{cases}                                      \tag{2.2}
\]

### Theorem 2.1 (column permutation)

For every \(x\in Q_n\), \(\widehat\Theta_{n,x}\) is a
parity-reversing permutation of the full \(Q_n\).

#### Proof

The seed is the audited full-column complete mapping.  Assume the theorem
at \(h\), and suppose the output in (2.2) is \(q=(q_0,q_1)\).  Since one
child column toggles one context bit, the unknown input satisfies

\[
                         \epsilon(p)=\epsilon(q)\oplus1.
\]

Consequently its branch is already determined by the output:

\[
 s=\epsilon(x)\oplus\epsilon(q)\oplus1.            \tag{2.3}
\]

If \(s=0\), recover

\[
                         p_0=\widehat\Theta_{h,u}^{-1}(q_0),
 \qquad p_1=q_1.
\]

If \(s=1\), recover

\[
                         p_0=q_0,
 \qquad p_1=\widehat\Theta_{h,v}^{-1}(q_1).
\]

The child inverse reverses parity, so the recovered input has exactly the
parity used in (2.3), and hence really uses the asserted branch.  This is
a two-sided inverse.  Every output differs from its input in one bit, so
the permutation reverses parity. \(\square\)

Restricting (2.1) to \(E_n\) gives the exact complete mapping
\(E_n\to O_n\) required by the physical paired lift.

## 3. Joint trace recovery

For a forward or reverse coarse \(q\)-window let

\[
 \widehat{\mathcal C}_{n,q}^{\pm}(p,x)
 =\bigl(\widehat J_{n,p,q}^{\pm}(x),
         p|_{(\widehat J^{\pm})^c},
         x|_{(\widehat J^{\pm})^c}\bigr).          \tag{3.1}
\]

### Theorem 3.1 (quarter-depth joint trace theorem)

Both maps in (3.1) are injective on \(Q_n\times Q_n\) for

\[
                         0\le q\le n/4.             \tag{3.2}
\]

#### Proof

The \(Q_4\) assertion is unchanged.  Let \(n=2h\).  A parent window of
even depth \(q=2r\) projects to consecutive child windows of depths
\((r,r)\).  The parent support split and outside restrictions are exactly
the two child codes.  The order in which the children moved is irrelevant
when their depths are equal.

For odd depth \(q=2r+1\), the child depths are \((r+1,r)\) in one order.
Their support cardinalities identify the child which moved first.  The
parent data again split into two child codes.  Although the first-child
selector is now

\[
 (\epsilon(u)\oplus\epsilon(v))
 \oplus(\epsilon(p_0)\oplus\epsilon(p_1)),          \tag{3.3}
\]

it need not be known before decoding: the unequal support cardinalities
give it, and the child codes recover the full child sources and contexts.

If \(q\le n/4=h/2\), both child depths are at most \(h/4\), exactly as
in the original quarter-depth induction.  This proves the forward map.
For the inverse map, a predecessor toggles total source parity, so inverse
moves also alternate children; deleting the other child's moves again
leaves consecutive reverse child windows with the same depth split.  The
identical induction proves the reverse map. \(\square\)

The fixed-context row proof likewise gives ordinary two-sided trace
injectivity through coarse depth \(n/2\).  The physical half-step decoder
uses only the adjacent substitution

\[
                         i\longmapsto(b_i,a_i)
\]

and the joint code (3.1).  Hence the existing half-step proof applies
verbatim and gives literal physical injectivity for both signs, both
phases, and both orientations through

\[
                         1\le \ell\le n/2-1.        \tag{3.4}
\]

Together with Theorems 1.1 and 2.1, this constructs the claimed exact
\(Q_R\) compiler factor.

## 4. Context routing and nonconjugacy

Identify the \(L=n/4\) bottom leaves with \(\{0,1\}^t\).  For a dyadic
tree node \(v\), put

\[
 r_v(x,p)=\epsilon(x|_v)\oplus\epsilon(p|_v).       \tag{4.1}
\]

If \(k=(k_0,\ldots,k_{t-1})\) is written least-significant-bit first,
the \(k\)-th visited leaf is \(a_1\cdots a_t\), where

\[
                         a_j=k_{j-1}\oplus
                         r_{a_1\cdots a_{j-1}}(x,p).
                                                               \tag{4.2}
\]

The proof is the usual recursive alternation: the node at depth \(j-1\)
has previously been visited \(\lfloor k/2^{j-1}\rfloor\) times.  Unlike
the old recursion, every nonroot phase in (4.2) contains a genuine
context parity.

The phases remain physically constrained:

\[
                         r_v=r_{v0}\oplus r_{v1}.    \tag{4.3}
\]

They are not independent abstract switch bits.  Nevertheless, for fixed
\(x\) and even root context \(p\), the descendant context parities can
route the first move to every leaf in the root half selected by
\(\epsilon(x)\).  At least one seed direction is attainable in each such
leaf.  Therefore

\[
 \left|\{\widehat d_{n,p}(x):p\in E_n\}\right|
                         \ge L/2=n/8.               \tag{4.4}
\]

For the old recursion this cardinality is at most four, since the leaf is
fixed by \(x\) and only its seed direction varies.  The cardinality of a
fixed-source context range is preserved by every affine relabeling of the
context, source, and direction columns which preserves the paired-lift
fibration.  Thus, for \(n>32\), the two context-indexed row arrays are not
conjugate in that compiler category.  The claim is deliberately about the
paired compiler template, not about an arbitrary nonlinear isomorphism of
the underlying unlabelled cycle set.

## 5. Exact dyadic blind cells

Fix a physical window and let \(A\) be its set of \(d\) visited bottom
leaves.  In the protected range these leaves are distinct.  Let
\(\mathcal T(A)\) be the union of their root-to-leaf paths in the dyadic
tree.  The **frontier cells** are the maximal dyadic subtrees disjoint from
\(A\) whose parent lies in \(\mathcal T(A)\).  Their leaf sets partition
the unvisited leaves.

Let \(C_1,\ldots,C_b\subset[n]\) be the corresponding sets of coarse
context coordinates, four per bottom leaf.  Define

\[
 \mathcal B_A
 =\left\{\alpha\in Q_n:
  \alpha|_{A\times[4]}=0,
  \quad |\alpha\cap C_j|\equiv0\pmod2
       \ (1\le j\le b)\right\}.                   \tag{5.1}
\]

### Lemma 5.1 (blind-cell classification)

Every \(\alpha\in\mathcal B_A\) preserves the complete ordered leaf
schedule through the window and changes no visited seed context.
Conversely, among context shifts which vanish on the visited leaves,
preserving that ordered leaf schedule forces the parity conditions in
(5.1).

#### Proof

The branch at a queried node \(v\) changes precisely when
\(|\alpha|_v\) is odd.  Every queried node is the disjoint union of
visited leaves and frontier cells below it.  Conditions (5.1) therefore
make every queried-node parity zero and preserve (4.2).  Since
\(\alpha\) vanishes on visited leaves, their local seed contexts and
directions are unchanged.

Conversely, schedule preservation makes \(|\alpha|_v=0\) at every node
on every visited path.  Subtract the equation at a visited child from the
equation at its parent.  The parity on the sibling frontier subtree is
zero.  Repeating down every visited path gives the condition for every
maximal frontier cell. \(\square\)

Thus the old blind flat is replaced by the direct sum

\[
                         \mathcal B_A=\bigoplus_{j=1}^b E(C_j),
                                                               \tag{5.2}
\]

of even-parity spaces on the frontier cells.  It still has exponential
size

\[
                         |\mathcal B_A|
 =2^{n-4d-b},                                      \tag{5.3}
\]

but its low-weight spectrum is much thinner.

## 6. Fixed-strength atom suppression

The visited leaf set of any consecutive window is recursively balanced:
at every dyadic node, its two children receive numbers of visits differing
by at most one.  Therefore no frontier cell contains more than
\(2L/d\) leaves.  Since the frontier cells are disjoint and contain at
most \(L\) leaves in total,

\[
 \sum_{j=1}^b|C_j|^2
 =16\sum_{j=1}^b|C_j/4|^2
 \le {32L^2\over d}
 ={2n^2\over d}.                                   \tag{6.1}
\]

### Theorem 6.1 (blind atom bound)

For every fixed \(t\ge1\), the number of weight-\(2t\) shifts in
\(\mathcal B_A\) satisfies

\[
 \boxed{
 \#\{\alpha\in\mathcal B_A:|\alpha|=2t\}
 \le C_t\left({n^2\over d}\right)^t}              \tag{6.2}
\]

for a constant \(C_t\) depending only on \(t\).

#### Proof

Every cell contains an even number of selected coordinates.  Pair the
selected coordinates arbitrarily inside each cell.  Every admissible
\(2t\)-set therefore admits a representation by \(t\) unordered pairs,
each pair lying in one cell.  The number of choices of one ordered pair is
at most

\[
                         \sum_j\binom{|C_j|}{2}
 \le\frac12\sum_j|C_j|^2=O(n^2/d).
\]

Choosing \(t\) such pairs overcounts every set by a factor depending only
on \(t\), which proves (6.2). \(\square\)

In the physical compiler, a pure context shift changes only the fixed
\(b\)-columns.  The ambient type-\(2t\) shell has
\(\binom{R-q}{2t}=\Theta_t((2n)^{2t})\) members.  Dividing (6.2) by this
shell gives

\[
 {\#\text{ certified blind type-}2t\text{ continuations}
   \over\binom{R-q}{2t}}
                         =O_t(4^{-t}d^{-t}),         \tag{6.3}
\]

uniformly when \(q=o(R)\).  The old compiler allowed every even
\(2t\)-set on \(n-O(q)\) unvisited \(b\)-coordinates and gave
\(4^{-t}+o(1)\).  This proves the advertised breaking of the entire old
fixed-strength hierarchy.

The same estimate is the direct replacement for the old \((t+1)\)-face
atom.  Choose \(t\) disjoint weight-two shifts from the blind kernel.  The
number of ordered choices is at most

\[
 \left(\sum_j\binom{|C_j|}{2}\right)^t
 =O_t((n^2/d)^t),
\]

whereas the ambient ordered disjoint-pair type has
\(\Theta_t(R^{2t})\) choices.  Its conditional common-option probability
is therefore \(O_t(4^{-t}d^{-t})\), rather than the old
\(4^{-t}+o(1)\).

Equation (6.3) controls the formerly blind context-flat contribution.  It
does not rule out other tuples with the same affine column type arising
from changes of source bits, changes inside visited leaves, or accidental
support coincidences.  Those terms are coefficients of the exact new
higher enumerator.

## 7. Exact new higher enumerator

The \(k\)-start transfer theorem remains valid with one change.  If a
start has context parity \(\kappa_s\) and source parity \(c_s\), its child
schedule is formed using

\[
                         c_s\oplus\kappa_s           \tag{7.1}
\]

instead of \(c_s\).  After choosing the left-child parities
\((\alpha_s,\beta_s)\), the left recursive scheduling bit is
\(\alpha_s\oplus\beta_s\), while the right scheduling bit is

\[
 (\kappa_s\oplus\alpha_s)
 \oplus(c_s\oplus\beta_s).                         \tag{7.2}
\]

The two child column-histogram polynomials multiply exactly as before.
Thus the same finite \(Q_4\) seed computes every pair and higher
common-label coefficient for the new template.  In particular, the new
compiler can be inserted into the existing packet-option and one-sided
product-hole formulations without changing their owner constraints.

## 8. Boundary of the result

Proved:

1. a context-reading recursive template not conjugate to the old
   context-blind scheduler;
2. exact row factorhood and full-column parity completeness;
3. the same quarter-depth joint and physical \(H\)-window injectivity;
4. an exact dyadic classification of its residual unvisited-context
   blind cells;
5. suppression of every old fixed-strength \(4^{-t}\) atom to
   \(O_t(4^{-t}d^{-t})\); and
6. the exact modification of the higher-enumerator recursion.

Not proved:

1. that the complete new enumerator has no other degree-scale atoms;
2. a cross-parent near-cover by mixtures of old and new templates;
3. the arbitrary-weight one-sided configuration Hall inequality; or
4. coefficient one.

The universal alternative in the question is therefore false for the
specific constant-strength obstruction: parity-complete recursive
factorhood does not force the old \(4^{-t}\) blind-flat hierarchy.  What
is unavoidable for a binary recursion is a weaker information bound: a
length-\(q\) schedule queries only its visited dyadic decision forest, so
an exponential residual blind subspace remains unless one adds a
higher-rate controller.  The context-phased compiler is the minimal exact
construction separating these two phenomena.
