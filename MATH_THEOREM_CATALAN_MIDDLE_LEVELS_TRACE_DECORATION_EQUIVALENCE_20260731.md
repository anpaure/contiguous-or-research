# Catalan diamond matchings as decorated middle-levels cycles

Date: 2026-07-31  
Status: exact equivalence for the middle-levels-resolvable class; exact
binary-trace topology; explicit (m=3) counterexample showing that an
arbitrary linear diamond matching need not be resolvable

## 1. The three sizes

Fix (m\ge2), put

\[
 \Omega=[2m-1],\qquad \widehat\Omega=\Omega\sqcup\{\infty\},
\]

and write

\[
 Q=\binom{2m-1}{m-1}=\binom{2m-1}{m},\qquad
 P=\binom{2m-1}{m-2}=\binom{2m-1}{m+1},
\]

\[
 K=Q-P=\operatorname {Cat}_m.
\tag{1.1}
\]

The two shores of the Boolean diamond graph on \(\widehat\Omega\) are

\[
 \binom{\widehat\Omega}{m-1}
 =\binom\Omega{m-1}\sqcup
   \left(\infty+\binom\Omega{m-2}\right),
\tag{1.2}
\]

\[
 \binom{\widehat\Omega}{m+1}
 =\binom\Omega{m+1}\sqcup
   \left(\infty+\binom\Omega m\right).
\tag{1.3}
\]

Both have size \(P+Q=mK\).  The physical rank-(m) layer splits into the
two rails

\[
 {cal A}=\left\{\infty+A:A\in\binom\Omega{m-1}\right\},
 \qquad
 {cal B}=\binom\Omega m,
\tag{1.4}
\]

of size \(Q\) each.  Their cross-containment graph is the middle-levels
graph \({\rm ML}(2m-1)\).

## 2. Turn maps on one middle-levels Hamilton cycle

Let a Hamilton cycle of \({\rm ML}(2m-1)\) be written

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,
\tag{2.1}
\]

where \(A_i\in\binom\Omega{m-1}\),
\(B_i\in\binom\Omega m\), and

\[
                       A_i\subset B_i\supset A_{i+1}.
\tag{2.2}
\]

There are two turn colours:

\[
 \ell_i=A_i\cap A_{i+1}\in\binom\Omega{m-2},
 \qquad
 u_i=B_{i-1}\cup B_i\in\binom\Omega{m+1}.
\tag{2.3}
\]

Choose index sets \(I,J\subseteq\mathbb Z_Q\).  Mark the \(A\)-position
\(A_i\) when \(i\in I\), and mark the \(B\)-position \(B_j\) when
\(j\in J\).  Read these marks in the cyclic order (2.1).

### Definition 2.1 (Catalan decoration)

The pair \((I,J)\) is a Catalan decoration of (2.1) when:

1. \(i\mapsto u_i\) is a bijection
   \(I\to\binom\Omega{m+1}\);
2. \(j\mapsto\ell_j\) is a bijection
   \(J\to\binom\Omega{m-2}\); and
3. consecutive marks in cyclic order have opposite rail types.

The first two conditions force

\[
                         |I|=|J|=P.                 \tag{2.4}
\]

Condition 3 has two equivalent forms.  In the cyclic binary word on the
\(2Q\) positions of (2.1), with a one at a marked position, every maximal
zero-run has even length.  Equivalently, after deleting the marked
vertices, every nonempty component of the residual incidence cycle is an
even path.

Every such residual path has a unique perfect matching.  Denote the union
of these path matchings by \(R\).  It has size

\[
                         |R|=Q-P=K.                  \tag{2.5}
\]

Thus the apparent cross choices are in fact forced once the marks are
fixed.

## 3. Exact diamond-matching equivalence

From a Catalan decoration form a set \({\cal M}(C,I,J)\) of diamond
incidences as follows:

\[
 \begin{array}{lll}
 i\in I:& A_i\subset u_i,
     &\psi(A_i,u_i)=B_{i-1}B_i,\\[1mm]
 j\in J:& \infty+\ell_j\subset\infty+B_j,
     &\psi(\infty+\ell_j,\infty+B_j)
       =(\infty+A_j)(\infty+A_{j+1}),\\[1mm]
 A_iB_j\in R:& A_i\subset\infty+B_j,
     &\psi(A_i,\infty+B_j)=(\infty+A_i)B_j.
 \end{array}
\tag{3.1}
\]

Here \(\psi(L,U)\) is the unique Johnson edge formed by the two rank-
\(m\) sets strictly between \(L\) and \(U\).

### Theorem 3.1 (decorated-cycle/perfect-diamond equivalence)

For a fixed Hamilton cycle (2.1), Catalan decorations are in bijection
with perfect matchings of the lower--upper diamond graph whose selected
diamonds are supported on:

* the \(A\)-turns \(B_{i-1}B_i\) of the cycle;
* the \(B\)-turns \((\infty+A_i)(\infty+A_{i+1})\); and
* cross edges of the cycle.

The matching corresponding to \((I,J)\) is exactly (3.1).

#### Proof

Use the shore decompositions (1.2)--(1.3).  A lower colour
\(A\in\binom\Omega{m-1}\) is used by the \(A\)-turn at \(A\) when that
position is marked, and otherwise is used by the unique incident edge of
\(R\).  Every such lower colour is therefore used once.  The lower colours
containing \(\infty\) are used once because the selected \(\ell_j\)'s are
a bijection.

Dually, an upper colour \(\infty+B\) is used by the \(B\)-turn at \(B\)
when marked, and otherwise by the unique incident edge of \(R\).  The
upper colours avoiding \(\infty\) are used once because the selected
\(u_i\)'s are a bijection.  Thus (3.1) is a perfect matching.

Conversely, in a supported perfect matching, every lower colour containing
\(\infty\) can only be supplied by a selected \(B\)-turn and every upper
colour avoiding \(\infty\) only by a selected \(A\)-turn.  This forces
the two bijections and \(|I|=|J|=P\).  The remaining cross edges must
perfectly match the unmarked \(A\)- and \(B\)-positions inside the
residual subgraph of the cycle.  A path has a perfect matching exactly
when it has even order, and then that matching is unique.  This is
precisely condition 3 and gives \(R\). \(\square\)

### Corollary 3.2 (automatic physical degree cap)

The physical lift \(F(C,I,J)=\Psi({\cal M}(C,I,J))\) is a spanning graph
of maximum degree two, with

\[
 |V(F)|=2Q,\qquad |E(F)|=2P+K=P+Q=mK.                \tag{3.2}
\]

Indeed, an unmarked vertex has its one cross edge from \(R\) and is
incident with at most one turn edge: the residual perfect matching implies
that at least one of its two cycle neighbours is unmarked.  A marked vertex
has no cross edge and is incident with at most its two neighbouring turn
edges.

## 4. Exact binary-trace topology

The maximum-degree statement is not yet acyclicity.  Write the cyclic mark
word as alternating maximal runs

\[
                  1^{a_1}0^{b_1}1^{a_2}0^{b_2}\cdots
                  1^{a_s}0^{b_s},                     \tag{4.1}
\]

where \(a_t\ge1\), and condition 3 says \(b_t\ge2\) is even.

### Theorem 4.1 (one-cycle criterion)

The physical graph \(F(C,I,J)\) contains a cycle if and only if

\[
              b_t=2\text{ for every }t,
 \qquad       a_t\text{ is odd for every }t.          \tag{4.2}
\]

When (4.2) holds it contains exactly one cycle.  Otherwise it is a
spanning linear forest, necessarily with exactly

\[
                         2Q-(P+Q)=K                  \tag{4.3}
\]

path components, with isolated vertices allowed.

#### Proof

Forget the set labels and retain the cyclic positions.  Every marked
position contributes the chord joining its two cycle neighbours.  On a
segment \(0,1^a,0\), those chords split by parity.  If \(a\) is odd,
one chord path joins the two boundary zeroes and the other is an internal
path.  If \(a\) is even, there are two paths, each containing exactly one
boundary zero.

On a zero-run \(0^{2b}\), the forced residual matching consists of \(b\)
independent adjacent edges.  It transmits a path from one boundary to the
other exactly when \(b=1\), i.e. when the zero-run has length two.  Hence
a closed route can propagate around the original circle precisely when
every one-run and every zero-run transmits, which is exactly (4.2).  In
that event the transmitted pieces make one cycle; all remaining parity
pieces are paths.  If one block fails to transmit, the circular route is
broken, and every component is a path.  Equation (4.3) is then Euler's
identity for a forest. \(\square\)

This corrects a tempting but false shorter criterion.  It is not enough
that every gap between consecutive marks contain zero or two unmarked
positions.  The cyclic trace

```text
11001100
```

has that property and has alternating rail types among its marks, but its
two marked runs have even length, so the lifted graph is a forest (two
paths), not a cycle.  In consecutive-mark language, the forest condition
is:

* some positive unmarked gap has length at least four; **or**
* some maximal run of consecutive marks has even length.

## 5. The exact scope for an arbitrary Catalan linear matching

Theorem 3.1 is an equivalence for matchings supported by one middle-levels
Hamilton cycle.  This qualification cannot be deleted.

For an arbitrary perfect diamond matching \({\cal M}\), define its forced
middle-levels support \(\Theta({\cal M})\) as follows.

* A cross diamond contributes its one cross edge.
* A same-\({\cal B}\)-rail diamond contributes the two cross edges through
  its unique centre \(A\).
* A same-\({\cal A}\)-rail diamond contributes the two cross edges through
  its unique centre \(B\).

### Proposition 5.1 (Hamilton-extension criterion)

An arbitrary perfect diamond matching admits a decorated-middle-levels
representation if and only if \(\Theta({\cal M})\) is contained in a
Hamilton cycle of \({\rm ML}(2m-1)\).  Given that cycle, its decoration is
unique.

This is immediate: a same-rail edge must be the shortcut of the unique
length-two middle-levels path through its intersection or union centre,
while a cross edge must remain a literal cycle edge.

Linearity of the physical diamond lift does not imply this Hamilton-
extension condition.  Here is a complete counterexample at \(m=3\), on
\([6]\) with \(\infty=5\).  In decimal bitmask notation, match the fifteen
rank-two lower sets to rank-four upper sets by

```text
(3,23) (5,29) (6,15) (9,27) (10,46)
(12,60) (17,51) (18,58) (20,53) (24,30)
(33,45) (34,39) (36,54) (40,43) (48,57)
```

Every pair is a containment, and both coordinates are permutations of the
two shores.  Its physical lift has degree profile

\[
                         0^1 1^8 2^{11},
\]

and component orders \(1,2,4,5,8\), hence is a spanning
\(K=\operatorname {Cat}_3=5\)-path forest.  But
\(\Theta({\cal M})\) has four vertices of degree three (masks
\(25,38,41,56\)), so no two-regular middle-levels Hamilton cycle can
contain it.

Thus the general physical problem and the decorated-cycle problem are not
identical.  The latter is a strong, clean sufficient architecture whose
additional gate is exactly a Hamilton extension in \({\rm ML}(2m-1)\).

## 6. Comparison with the published Hamilton/tight-enumeration theorems

The ordinary Middle Levels theorem supplies (2.1), but none of the two
turn-bijection conditions.  Suppressing the \(B\)-rail gives a Johnson
Hamilton cycle on the \(A\)-sets, and

\[
                   A_iA_{i+1}\longmapsto\ell_i
\]

is its lower-intersection word.  Therefore surjectivity of \((\ell_i)\)
is exactly the extra lower-tight-enumeration property on levels
\(m-2,m-1\).  Dually, suppressing the \(A\)-rail gives the upper-union
word \((u_i)\) on the \(B\)-sets.  A Catalan decoration needs both
surjectivities on the **same** alternating cycle, representatives whose
marks alternate, and the parity condition of Theorem 4.1.

Gregor--Mička--Mütze prove that each consecutive-level interval has a
tight enumeration.  Applied separately, this supplies a cycle with the
\(\ell\)-surjectivity property and, dually, a possibly different cycle
with the \(u\)-surjectivity property.  It does not identify their middle
projections, choose alternating representatives, or impose (4.2).

Likewise, the recursive Middle Levels constructions prove Hamiltonicity
of the undecorated alternating graph.  Their gluing switches preserve a
Hamilton cycle, but their theorems do not state the two turn-colour
surjections or the representative-alternation condition.  The separate
published results therefore stop exactly before Definition 2.1.

### 6.1 Complement-antipodal specialization

There is one useful symmetry reduction, but it still does not close the
gate.  Suppose \(Q=2s+1\) and complementation on \(\Omega\) acts on (2.1)
as the half-turn

\[
                 \overline{A_i}=B_{i+s},\qquad
                 \overline{B_i}=A_{i+s+1}.             \tag{6.1}
\]

Then the two turn words are literally the same up to complement and shift:

\[
                         \overline{u_i}=\ell_{i+s}.     \tag{6.2}
\]

Consequently, if \(I\) chooses one occurrence of every upper turn colour,
then

\[
                         J=I+s                         \tag{6.3}
\]

automatically chooses one occurrence of every lower turn colour.  The two
rainbow gates collapse to one.  What remains is still nontrivial: the
antipodal occurrence set \(I\cup(I+s)\) must alternate by shore, and its
run trace must pass Theorem 4.1.

The parity condition \(Q\) odd holds exactly when \(m\) is a power of two.
Published odd-graph Hamiltonicity supplies complement-antipodal
middle-levels cycles in these dimensions, but does not supply turn
surjectivity or an antipodally interlacing representative set.  Thus even
in the symmetry-favourable subsequence, (6.2) reduces rather than proves
Definition 2.1.

The three-level tight-enumeration theorem is also insufficient: its
distance-two steps may lie within a boundary level, whereas the common
diamond normal form needs the lower--upper distance-two step inside one
Boolean diamond.  This distinction is the occurrence-level common-
refinement obstruction recorded elsewhere in the repository.

Consequently no cited theorem closes the decorated-cycle gate.  The exact
remaining statement within this architecture is:

> Find, for every \(m\), one Hamilton cycle (2.1) whose two turn maps admit
> bijective representative sets \(I,J\) alternating around the cycle and
> satisfying the forest alternative in Theorem 4.1.

This is strictly stronger than Middle Levels Hamiltonicity and strictly
more structured than existence of an arbitrary Catalan linear perfect
matching.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_middle_levels_trace_decoration_20260731.py
```

The audit checks the displayed \(m=3\) counterexample literally and
exhausts all cyclic binary traces through length sixteen, confirming the
perfect-residual-matching and one-cycle criteria.  The mathematical proofs
above do not depend on the audit.
