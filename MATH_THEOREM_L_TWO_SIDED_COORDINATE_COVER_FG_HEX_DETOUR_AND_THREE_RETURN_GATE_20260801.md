# Two-sided coordinate cover at the rolling reset: the exact f/g hex detour and the three-return gate

**Date:** 2026-08-01  
**Lane:** L, terminal compiler / occurrence-labelled lift  
**Status:** exact Johnson owner/palette lemma; sharp shortest-path and
native-boundary obstructions; exact conditional three-return interface.
No regenerative compiler or all-state physical flag lift is claimed.

## 0. Verdict and source boundary

The external input is OpenAI,
[Ten Advances in Mathematics and Theoretical Computer Science, Chapter 9,
Section 2](https://cdn.openai.com/pdf/ten-proofs-oai.pdf), Lemmas 2.2--2.3.
Section 5 states the exact part used here.  The chapter's \(f,g\) are word
maps in an abstract Ramsey colouring; they are not Boolean owner maps or the
side-coordinate variables of Section 3.

The result is sharp.

1. The unique direct-owner collision is removable at the unflagged Johnson
   level.  Three resource-private length-three detours exist when three
   private coordinates are available on each side of the seam.
2. Every length-two detour repeats either the direct owner or one immediate
   lower colour.
3. The clean length-three detour is reversible as a Johnson path, but it is
   not a consecutive strict depth-\(d\) chronology segment for \(d\ge3\):
   its freshly inserted side coordinate leaves two turns later.  An
   alternating path split between the two reset phases is not ruled out by
   this one-phase argument, but needs separate phase flag assignments which
   Chapter 9 does not provide.
4. Endpoint retiming or a longer collared return may evade that obstruction.
   Such a return must still align the attachment and signed predecessor
   projections, pass the fixed-cap \(U_{2,3}\) cut, and leave a common
   phase-contracted exterior.

Separated palettes plus root-level coordinate cover therefore do not close
the three returns.  A positive import needs the full occurrence-labelled
all-state condition in Section 5.

## 1. Adjacent-seam normal form

Let \(A,B\) be adjacent rank-\(r\) sets.  Write uniquely

\[
                 A=S\cup\{x\},\qquad B=S\cup\{y\},           \tag{1.1}
\]

where \(|S|=r-1\) and \(x,y\notin S\), \(x\ne y\).  Their direct edge has
upper owner

\[
                         U=S\cup\{x,y\}.                     \tag{1.2}
\]

For the opened rolling reset, \(A=T_0\), \(B=T_{N-1}\), and
\(U=U_{N-1}\).  After forgetting signs, the attachment pair and both
predecessor-parity pairs have these same endpoint roots.

For a Johnson edge \(VW\), call \(V\cup W\) its owner and \(V\cap W\) its
lower colour.  Equality of Boolean sets is already a capacity-one conflict;
typed names cannot split one physical resource.

## 2. One intermediate root is sharply impossible

### Theorem 2.1 (common-neighbour dichotomy)

Every rank-\(r\) common neighbour \(C\ne A,B\) is exactly one of:

\[
 C=S\cup\{g\},\qquad g\notin S\cup\{x,y\},                  \tag{2.1}
\]

or

\[
 C=(S\setminus\{f\})\cup\{x,y\},\qquad f\in S.              \tag{2.2}
\]

In the first case the two owners are distinct but

\[
                         A\cap C=C\cap B=S.                 \tag{2.3}
\]

In the second case the two lower colours are distinct but

\[
                         A\cup C=C\cup B=U.                 \tag{2.4}
\]

Thus no two-edge \(A-C-B\) detour is simultaneously owner-injective and
lower-colour-injective.  Reversal changes neither defect.

#### Proof

Write \(C=A-a+b\).  Adjacency to \(B\) forces either \(a=x\), giving
\(C=S+b\), or \(a=f\in S,b=y\), giving (2.2).  Direct union and
intersection give (2.3)--(2.4). \(\square\)

## 3. The f/g hex detour

Choose

\[
                 f\in S,\qquad g\notin S\cup\{x,y\},         \tag{3.1}
\]

put

\[
 A_f^g=(S\setminus\{f\})\cup\{x,g\},\qquad
 B_f^g=(S\setminus\{f\})\cup\{y,g\},                         \tag{3.2}
\]

and define

\[
             H(f,g):\quad A-A_f^g-B_f^g-B.                  \tag{3.3}
\]

### Theorem 3.1 (shortest owner/lower-clean detour)

The owners of \(H(f,g)\) are

\[
\begin{aligned}
 O_x&=S\cup\{x,g\},\\
 O_0&=(S\setminus\{f\})\cup\{x,y,g\},\\
 O_y&=S\cup\{y,g\},
\end{aligned}                                               \tag{3.4}
\]

and its lower colours are

\[
\begin{aligned}
 L_x&=(S\setminus\{f\})\cup\{x\},\\
 L_0&=(S\setminus\{f\})\cup\{g\},\\
 L_y&=(S\setminus\{f\})\cup\{y\}.
\end{aligned}                                               \tag{3.5}
\]

Each palette is internally rainbow.  Hence \(H(f,g)\) is clean, and
Theorem 2.1 proves that length three is minimum among non-direct
owner/lower-clean detours avoiding the forbidden direct owner \(U\).  Its
reversal has the same resources.

#### Proof

The successive exchanges are \(f\leftrightarrow g\),
\(x\leftrightarrow y\), and \(g\leftrightarrow f\).
Unions and intersections give (3.4)--(3.5).  Their membership signatures
make the three sets on each shore distinct. \(\square\)

### Theorem 3.2 (three private typed detours)

Let \(I=\{\mathsf A,\mathsf P_0,\mathsf P_1\}\).  Choose injections

\[
 f:I\hookrightarrow S,\qquad
 g:I\hookrightarrow [k]\setminus(S\cup\{x,y\}).             \tag{3.6}
\]

Then the paths \(H(f(i),g(i))\) have pairwise distinct internal roots, all
nine owners distinct, and all nine lower colours distinct.  Apart from
\(A,B\), their displayed physical resources are disjoint.  Each path may be
reversed independently at the unflagged Johnson level.

Conversely, inside (3.3), resource privacy forces both maps in (3.6) to be
injective.  Thus three pairwise-private detours of the form (3.3) exist
exactly when

\[
                         |S|\ge3,\qquad k-|S|-2\ge3.         \tag{3.7}
\]

#### Proof

Distinct \(g\)'s distinguish \(O_x,O_y\).  An \(O_0\) contains both \(x,y\)
and omits its \(f\), so equality of two such sets recovers \(f,g\), and it
cannot equal an \(O_x\) or \(O_y\).  Distinct \(f\)'s distinguish
\(L_x,L_y\); an \(L_0\) contains its outside member \(g\), and equality of
two such sets again recovers \(f,g\).  The internal-root claim is identical.
If \(g\) is repeated then \(O_x,O_y\) repeat; if \(f\) is repeated then
\(L_x,L_y\) repeat. \(\square\)

For \(J(2m+1,m)\), the bank sizes are \(m-1,m\), so (3.7) holds for
\(m\ge4\).  This is only a local supply statement.

## 4. Ordered boundary states

Suppose first that \(H(f,g)\) is intended as one consecutive segment of one
strict all-high chronology.  Its forward leaving word is

\[
                              (f,x,g),                       \tag{4.1}
\]

and its reverse leaving word is \((f,y,g)\).  Hence depth-three boundary
flags at \(A,B\) would necessarily begin with \((f,x)\) and \((f,y)\),
respectively.  These prefix conditions are necessary, but they are not
sufficient: strict flag transition also constrains the appended rail
coordinate.

### Theorem 4.1 (consecutive strict-lift obstruction)

For every \(d\ge3\), neither orientation of \(H(f,g)\) is a consecutive
strict depth-\(d\) all-high chronology segment.

#### Proof

In the forward direction the first turn deletes \(f\) and inserts \(g\).
The next two turns delete \(x\) and then \(g\).  At depth three, the flag at
\(A\) would be \((f,x)\).  After the first turn, strict rail shift must
append a coordinate from the old bottom block
\(A\setminus\{f,x\}\subseteq S\), whereas the required next flag is
\((x,g)\) and \(g\notin A\).  Equivalently, the positive run of \(g\) has
length two, below the depth-\(d\) run floor.  The reverse direction replaces
\(x\) by \(y\) and is identical.  Larger \(d\) retain the same forbidden
depth-three prefix. \(\square\)

At depth two the obstruction disappears: the leaving flags are successively
\(f,x,g\).  Thus Theorem 4.1 is a pull-clock/residence obstruction, not a
Johnson-geometry obstruction.

For calibration, the opened reset has

\[
\begin{aligned}
 A=T_0,\quad B=T_{N-1},\quad
 S&=K\cup\{X_0,\ldots,X_{d-1}\},\\
 x&=X_d,\qquad y=X_{2d+1}.                                  \tag{4.2}
\end{aligned}
\]

Its four native phase prefixes are

\[
\begin{array}{c|c}
 \text{state}&\text{first two deletions}\\ \hline
 A,\rightarrow&(X_0,X_1)\\
 A,\leftarrow&(x,X_{d-1})\\
 B,\rightarrow&(y,X_0)\\
 B,\leftarrow&(X_{d-1},X_{d-2}).
\end{array}                                                 \tag{4.3}
\]

They also fail the necessary \((f,x)\) or \((f,y)\) boundary prefix test.

### Proposition 4.2 (alternating-return scope)

Theorem 4.1 does not rule out using the three undirected edges of \(H(f,g)\)
as an alternating path split between the two phase matchings.  Consecutive
edges of such a symmetric-difference path may belong to different flag
tables, so there is no one-phase run of \(g\) to which the preceding proof
applies.  Such a lift requires explicit occurrence-labelled flag assignments
for both phases and proof that their attachment and predecessor projections
are the required paired returns.  Unflagged Johnson adjacency supplies
neither assertion.

## 5. The Chapter-9 coordinate-cover interface

Fix \(h\ge2\), put

\[
 q=\lceil2h\log h\rceil,\qquad s=q(q+1)+1.                   \tag{5.1}
\]

Chapter 9, Lemma 2.2 constructs fixed word maps

\[
             f_{\rm R},g_{\rm R}:[h]^s\longrightarrow[h]^s  \tag{5.2}
\]

such that

\[
 \forall a,b\in[h]^s\quad\exists j\in[s]:\qquad
       a_j=f_{\rm R}(b)_j
       \quad\text{or}\quad
       b_j=g_{\rm R}(a)_j.                                  \tag{5.3}
\]

For the separated-palette input assume \(h\ge3\).  Lemma 2.3 constructs
abstract palettes \(P,Q\) with
\(|P\setminus Q|=|Q\setminus P|\ge s\).  The Ramsey recursion chooses
distinct labels \(a_j\in Q\setminus P\) and
\(b_j\in P\setminus Q\), using the first label family on the first branch of
(5.3) and the second on the other branch.

This is genuinely all-pairs and stronger than nonempty row and column
margins.  It is nevertheless disjunctive.  Neither branch is universally
available by itself: for fixed \(b\), choose every coordinate of \(a\)
different from \(f_{\rm R}(b)\); the first branch is then absent, and the
second must carry the pair.  The symmetric argument defeats a prescribed
second branch.  The lemmas also supply abstract colour labels, not
occurrence-labelled Johnson owners, flags, or a simultaneous SDR across
three reset tasks.

For a literal return type \(i\), encoded source and sink words
\(u,v\in[h]^s\), and orientation \(\varepsilon\), define

\[
                 \chi_i(u,v;c,z,\varepsilon)=1              \tag{5.4}
\]

only if a coordinate-cover branch expands to one complete
occurrence-labelled
return column, including its old/replacement half, flag chronology, owner
and lower resources, and all declared guards.  The property actually needed
by the reset is

\[
 \boxed{\;
 \forall(u,v)\quad\exists(c,z,\varepsilon):
        \chi_i(u,v;c,z,\varepsilon)=1 .
 \;}                                                        \tag{5.5}
\]

There is no implication from (5.3) to (5.5) without a literal lift theorem.
The consecutive shortest hex lift fails by Theorem 4.1.  An alternating hex
lift remains possible only after the two separate phase flag tables and
their common turn-triple projections are supplied explicitly.

Even if each type separately has nonempty literal menus, simultaneous use
on common coordinate banks is a coupled three-dimensional matching: choose
one eligible \((c_i,z_i,\varepsilon_i)\) per type with all \(c_i\) and all
\(z_i\) distinct.  Separate Hall tests on the two projections are not
sufficient.  For instance,

\[
                 \{(1,1),(2,2)\},\qquad
                 \{(1,2),(2,1)\}                            \tag{5.6}
\]

have full projections on both coordinates, but every cross-menu choice
repeats one coordinate.  Pairwise disjoint physical coordinate banks remove
this selection obstruction, but not the literal-lift obstruction.

## 6. Exact conditional three-return implication

### Theorem 6.1 (literal coordinate-cover three-return lemma)

Fix the three endpoint-state pairs of an opened rolling reset.  Suppose:

1. one cell satisfying (5.4) is selected for each return type, with private
   side coordinates and available owner/lower resources;
2. their union is an aligned return packet: the head--owner projection
   closes exactly the attachment path, the tail--head projection closes
   exactly the two signed predecessor paths, and no other boundary remains;
3. all nonendpoint chronology, palette, occurrence and guard resources are
   mutually disjoint;
4. in one fixed cap \(\theta\), the full hazard union obeys

   \[
    D_{\mathsf A}\cup D_{\mathsf P_0}\cup D_{\mathsf P_1}
                          \in I(M_\theta^*);                 \tag{6.1}
   \]

5. the two selected phase banks are bi-contractible, leaving one represented
   common residual exterior at each downstream stage.

Then the cells form a compatible protected three-return lift.  If (5.5)
holds on separated physical banks and Conditions 2--5 hold for every chosen
triple, the conclusion holds for every triple of boundary states.

#### Proof

Conditions 1--3 give one literal phase exchange with exactly the typed
chronology boundary and no owner/lower collision.  Condition 4 is the exact
dual-transversal criterion for retaining all compiler targets after
reserving the occurrence hazards.  Condition 5 identifies the residual
selection problem in both phases.  These are precisely the compatible
three-return and common-minor hypotheses of the reset theorems. \(\square\)

### Proposition 6.2 (coordinate separation does not remove the 3-circuit)

Conditions 1--3, even with universal (5.5), do not imply (6.1).  Give the
three otherwise private columns distinct hazard cells
\(c_{\mathsf A},c_0,c_1\), and let one compiler target be adjacent to exactly
those cells.  The safe-deletion matroid is \(U_{2,3}\): every proper return
subfamily is safe, while the triple is not.

Likewise, independently routed attachment and predecessor paths do not imply
Condition 2.  Both projections must come from the same literal turn triples;
otherwise the signed sinks may cross or the flags may be incompatible.

## 7. Scope

The f/g hex detour removes the raw capacity-one owner obstruction and proves
why a one-intermediate-root repair cannot work.  A consecutive strict
shortest-detour lift is impossible at the current depth; an alternating
two-phase lift in this particular coordinate-cover architecture remains
unconstructed.

The separate longer-collar target is no longer open:
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`
constructs a `4d+2`-root resident return with exact internal all-width and
compiler transport.  Thus (for this f/g route only) the conditional target
below is historical:

\[
 \boxed{\text{endpoint retiming or a longer collared all-state return}}
 \;+\;
 \boxed{\text{aligned three-projection lift}}
 \;+\;
 \boxed{\text{fixed-cap coindependence and bi-contraction}}.
\]

No global host, exterior-window, common residual compiler, regeneration, or
\(\nu(k)\le B(k)+O(1)\) conclusion is made.
