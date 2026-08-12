# A symmetric-chain decomposition exactly solves the unrestricted all-high ordered-chain selector

**Date:** 2026-08-01  
**Status:** unconditional exact integral selector theorem.  It solves the
unrestricted local-order flag/mark system and, more strongly, permits any
at-most-\(m+1\) prescribed root flags by quarantining their suffixes
unmarked.  In the occurrence-labelled selector LP, any prescribed marks
with distinct target values can also be retained; fully marked prefixes
from distinct roots are therefore compatible exactly when they are
vertex-disjoint.  The theorem does not balance successor turns,
serialize an Euler chronology, or prove any upper/residence gate.

## 0. Verdict

Let \(k=2m+1\), \(1\le d\le m+1\), and let a depth-\(d\) local flag at a
rank-\(m\) root be

\[
 q=T_0\supset T_1\supset\cdots\supset T_{d-1},
 \qquad |T_j|=m-j.                                             \tag{0.1}
\]

The exact unrestricted selector asks for one flag at every rank-\(m\) root
and a choice of marked suffixes such that every target of every rank

\[
                       m-1,m-2,\ldots,m-d+1                    \tag{0.2}
\]

is marked exactly once.

An ordinary symmetric-chain decomposition of \(B_{2m+1}\) gives this
object immediately.  Consequently,

\[
 \boxed{\text{the unrestricted all-high ordered-chain selector is integral.}}
                                                                    \tag{0.3}
\]

The determinant-two minor in the selector matrix proves only that a generic
TU argument is unavailable.  It is not an existence obstruction.

## 1. Symmetric chains and middle roots

Fix any symmetric-chain decomposition \({\cal D}\) of the Boolean lattice
\(B_{2m+1}\).  A chain \(C\in{\cal D}\) has the form

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{2m+1-a},
 \qquad |C_r|=r,                                               \tag{1.1}
\]

for some \(a\le m\).

Every such chain contains a unique rank-\(m\) set

\[
                              q_C=C_m.                          \tag{1.2}
\]

Since the decomposition partitions the lattice, the map

\[
                         C\longmapsto q_C                       \tag{1.3}
\]

is a bijection from the chains of \({\cal D}\) to
\(\binom{[2m+1]}m\).  Equivalently, the number of chains is the width
\(\binom{2m+1}m\), and every middle root belongs to its unique chain.

## 2. Turning one chain into one local flag

Let \(C\) start at rank \(a\), and put \(\ell=m-a\).  Going downward from
\(q_C\), define the distinct deleted elements

\[
 z_j=C_{m-j+1}-C_{m-j},
 \qquad 1\le j\le\ell.                                        \tag{2.1}
\]

Then

\[
                 C_{m-j}=q_C-\{z_1,\ldots,z_j\}.               \tag{2.2}
\]

If \(\ell<d-1\), append any \(d-1-\ell\) distinct elements of the minimum
set \(C_a\) to the deletion word.  This is always possible, because

\[
              |C_a|=a=m-\ell\ge d-1-\ell                       \tag{2.3}
\]

whenever \(d-1\le m\).

Thus every chain supplies a complete local flag

\[
                  f_C=(q_C;z_1,\ldots,z_{d-1}).                 \tag{2.4}
\]

Mark its rank-\((m-j)\) suffix exactly when \(j\le\ell\), namely while
the flag follows the genuine symmetric chain.  The arbitrary continuation
below the chain minimum is left unmarked.

## 3. Exact selector theorem

### Theorem 3.1 (SCD ordered-chain selector)

The flags \(f_C\), one for every \(C\in{\cal D}\), use every rank-\(m\)
root exactly once.  Their marked suffixes use every target of every rank in
(0.2) exactly once.

#### Proof

Root exactness is the bijection (1.3).

Fix \(1\le j<d\) and a target
\(T\in\binom{[2m+1]}{m-j}\).  It belongs to a unique chain
\(C\in{\cal D}\).  Since that chain contains a set at rank \(m-j\), its
minimum rank satisfies

\[
                              a\le m-j.                         \tag{3.1}
\]

Hence \(\ell=m-a\ge j\).  Equation (2.2) says that the marked
rank-\((m-j)\) suffix of \(f_C\) is exactly \(C_{m-j}=T\).
No other flag marks \(T\), because the chains partition the lattice.
This proves exactness simultaneously at every displayed rank. \(\square\)

### Corollary 3.2

The integral flag/mark system

\[
 \sum_{f:\operatorname{root}(f)=q}x_f=1,
 \qquad
 \sum_{f:T_j(f)=T}y_{f,j}=1,
 \qquad 0\le y_{f,j}\le x_f,                                  \tag{3.2}
\]

has a zero-one solution for every \(d\le m+1\).

This strictly strengthens the uniform fractional flag theorem.  No global
order menu, Birkhoff rounding, or chain absorber is required for the
unrestricted local-order selector.

## 4. Strict adjacent-level shadow surplus

The protected statement follows from a useful exact expansion inequality.

### Lemma 4.1 (upper-shadow surplus)

Let \(1\le r\le m\), and let
\(\varnothing\ne{\cal X}\subseteq\binom{[2m+1]}{r-1}\).  Then

\[
                    |\partial^+{\cal X}|
                    \ge |{\cal X}|+2m+1-r.                     \tag{4.1}
\]

#### Proof

Complement \({\cal X}\) to a family
\({\cal F}\subseteq\binom{[2m+1]}k\), where

\[
                              k=2m+2-r.                         \tag{4.2}
\]

The upper shadow of \({\cal X}\) is the complement of the lower shadow of
\({\cal F}\).  Write \(|{\cal F}|=\binom{x}{k}\), with
\(k\le x\le2m+1\).  The Lovasz form of Kruskal--Katona gives

\[
                         |\partial^-{\cal F}|\ge\binom{x}{k-1}. \tag{4.3}
\]

The difference

\[
 g(x)=\binom{x}{k-1}-\binom{x}{k}
     =\binom{x}{k-1}{2k-1-x\over k}                            \tag{4.4}
\]

is increasing on this interval.  Indeed,

\[
 {d\over dx}\log g(x)
 =\sum_{i=0}^{k-2}{1\over x-i}-{1\over2k-1-x}>0,              \tag{4.5}
\]

because \((k-1)/x>1/2\) while
\(2k-1-x\ge2\) in the stated range.  Therefore

\[
 g(x)\ge g(k)=k-1=2m+1-r.                                     \tag{4.6}
\]

Equations (4.3)--(4.6) prove (4.1). \(\square\)

### Corollary 4.2 (forced adjacent matching)

In the containment graph between ranks \(r-1\) and \(r\), every matching
of at most \(2m+1-r\) prescribed edges extends to a matching saturating the
entire rank-\((r-1)\) shore.

#### Proof

Delete the endpoints of the prescribed edges.  For any remaining lower
family \({\cal X}\), at most the number of prescribed upper endpoints is
lost from its neighbourhood.  Lemma 4.1 leaves at least \(|{\cal X}|\)
neighbours.  Hall's theorem applies. \(\square\)

## 5. Arbitrary prescribed root flags with zero sidecar

### Theorem 5.1 (protected marked-chain selector)

Let \({\cal P}\subseteq\binom{[2m+1]}m\) be any set of

\[
                              h\le m+1                          \tag{5.1}
\]

distinct protected roots, and prescribe an arbitrary depth-\(d\) local
flag at every root in \({\cal P}\), where \(d\le m+1\).  There is an exact
integral selector
which:

* uses the prescribed flag at every protected root;
* uses one flag at every other root;
* marks every target of ranks \(m-1,\ldots,m-d+1\) exactly once;
* marks no suffix of a protected flag.

In particular, the protected selector has zero target sidecar.

#### Proof

If \(d=1\), there are no target rows and the assertion follows by using the
prescribed flags at protected roots and the unique depth-one flag elsewhere.
Assume henceforth that \(d\ge2\).

At the top adjacency, delete the \(h\) protected rank-\(m\) roots.  Lemma
4.1 with \(r=m\), followed by Hall, gives a matching \(M_m\) saturating
every rank-\((m-1)\) target into the remaining roots, since the surplus is
\(m+1\).

For each \(r=m-1,m-2,\ldots,m-d+2\), choose any containment matching
\(M_r\) saturating rank \(r-1\) into rank \(r\).  Such a matching follows
from Lemma 4.1 with no deleted vertices.

The union of the \(M_r\) is a vertex-disjoint chain forest through the high
rank slab: every non-top vertex has one upward edge, and every vertex has at
most one downward child.  Every high target lies in exactly one chain, and
every nonsingleton chain ends at an unprotected root because of the choice
of \(M_m\).

At each unprotected root, follow its chain downward to define the marked
part of its local flag, then extend arbitrarily and unmarked to depth \(d\).
At each protected root, use the prescribed flag and mark nothing.  The
chain forest marks every high target exactly once, while all protected root
equations are satisfied. \(\square\)

The theorem handles arbitrary overlaps among the prescribed suffix words,
because those words are quarantined rather than used as target providers.

## 6. Three different meanings of a prescribed marked segment

The selector variables are occurrence-labelled.  This must be separated
from the stronger request that an unlabelled edge set lie in one chain
factor.  Forgetting the occurrence labels changes the exact compatibility
condition.

### Theorem 6.1 (occurrence-labelled forced marks)

Let \(q_1,\ldots,q_h\) be distinct roots, with \(h\le m+1\), and prescribe
one complete depth-\(d\) flag

\[
 f_i=(q_i=T^i_0\supset T^i_1\supset\cdots\supset T^i_{d-1})
                                                               \tag{6.1}
\]

at each root.  Let
\[
                   {\cal R}\subseteq[h]\times\{1,\ldots,d-1\}
\]
be a set of forced occurrence labels \((i,j)\), meaning
\(y_{f_i,j}=1\).  There is an exact integral selector
using all the prescribed flags and marks if and only if

\[
                  (i,j)\longmapsto T^i_j
       \quad\hbox{is injective on }{\cal R}.                    \tag{6.2}
\]

For partial flag data, one must additionally require that the prescriptions
at each root extend to one local flag.

#### Proof

Necessity follows from the target equality in (3.2): two distinct forced
occurrences of one target would give that row load at least two.

For sufficiency, apply Theorem 5.1 to the \(h\) prescribed flags, initially
marking none of their suffixes.  Every target then has one marked provider
on a flexible-root flag.  For each \((i,j)\in{\cal R}\), remove the unique
flexible mark on \(T^i_j\) and put it on the prescribed occurrence
\(y_{f_i,j}\).  Injectivity makes these transfers disjoint.  The LP has no
contiguity constraint on the set of marked depths of one chosen flag, so
all remaining equations are unchanged. \(\square\)

In particular, prescribed unmarked path portions may branch or coalesce.
For example, at \(m=3,d=3\), the flags

\[
             123\to12\to1,\qquad124\to12\to2                  \tag{6.3}
\]

cannot both lie in a chain forest, but forcing only their depth-two targets
\(1\) and \(2\) is selector-feasible.  At the other extreme,
\(\{1\}\to\varnothing\) and \(\{2\}\to\varnothing\) give the smallest
forced-target collision.

### Corollary 6.2 (fully marked rooted prefixes)

Suppose the prescriptions are rank-\(m\)-rooted prefixes at distinct roots
and every nonroot vertex of every prefix is forced marked.  For
\(h\le m+1\), the following are equivalent:

1. the occurrence-labelled forced-mark selector is feasible;
2. the rooted prefixes are pairwise vertex-disjoint; and
3. one root-preserving chain forest contains all the prefixes.

#### Proof

Two rooted prefixes meet only at the same rank.  A meeting therefore forces
the same target occurrence twice, so Theorem 6.1 proves \(1\Rightarrow2\).
If the prefixes are disjoint, their edges form a matching at every
interface, with at most \(h\) edges per interface.  Corollary 4.2 extends
those matchings independently to a chain factor, proving \(2\Rightarrow3\).
A chain component has one rank-\(m\) root, so the original root ownership is
preserved.  Finally \(3\Rightarrow2\Rightarrow1\), where the last implication
uses Theorem 6.1 and permits any already fixed unmarked continuation below
the prescribed prefixes. \(\square\)

Thus two prefixes from distinct roots cannot concatenate: their first
meeting is a coalescence and is forbidden.  This is the precise scope of
the protected note's vertex-disjoint formulation.

### Theorem 6.3 (unlabelled edge-set factor criterion)

Now forget root labels and occurrence multiplicities.  Let \(E\) be the
set-theoretic union of prescribed saturated fragments in the high slab,
and let \(E_r\) be its edges between ranks \(r\) and \(r-1\), for
\[
                         m-d+2\le r\le m.
\]
Write \(U(E_r)\) and \(D(E_r)\) for their upper and lower endpoints, and let
\(N\) denote neighbourhood in the rank-\((r-1,r)\) containment graph.  The
edge set \(E\) extends to a chain factor covering every high target if and
only if, at every such interface,

* \(E_r\) is a matching; and
* for every \({\cal X}\subseteq\binom{[2m+1]}{r-1}\setminus D(E_r)\),

\[
          |N({\cal X})\setminus U(E_r)|\ge|{\cal X}|.           \tag{6.4}
\]

These are simply the exact residual Hall conditions after the forced
matching endpoints are deleted.

If \(E\) is the union of at most \(h\le m+1\) saturated fragments, then
(6.4) is automatic.  Indeed \(|E_r|\le h\), and Lemma 4.1 gives, for every
nonempty residual \({\cal X}\),

\[
 |N({\cal X})\setminus U(E_r)|
 \ge |{\cal X}|+2m+1-r-|E_r|\ge|{\cal X}|.                     \tag{6.5}
\]

Consequently, in this bounded unlabelled model, extendibility is equivalent
to the union being a descending linear forest.  Here fragments really may
concatenate: \(12\to1\) and \(1\to\varnothing\) are one valid unlabelled
path.  The resulting provider forest contains every required edge value,
but it need not retain any forgotten occurrence label or prescribed-root
ownership.

### Sharpness of the protected-bank size

For \(m\ge2\) and \(d\ge2\), the universal threshold \(h\le m+1\) is sharp.
Choose a rank-\((m-1)\) set \(A\) and \(a\in A\).  For each of the \(m+2\)
elements \(x\notin A\), prescribe and mark

\[
 A\cup\{x\}\longrightarrow (A\setminus\{a\})\cup\{x\}.       \tag{6.6}
\]

These rooted edges are pairwise vertex-disjoint and their marked targets
are distinct, but their roots exhaust all rank-\(m\) neighbours of \(A\).
The target \(A\) has no possible provider.  Thus target injectivity alone,
and even pairwise disjoint rooted prefixes, need not suffice at \(h=m+2\).

In summary:

* arbitrary prescribed flags are compatible when quarantined (Theorem 5.1);
* for \(h\le m+1\), arbitrary labelled forced marks are compatible exactly
  when their forced targets are distinct (Theorem 6.1);
* fully marked distinct-root prefixes are compatible exactly when they are
  vertex-disjoint (Corollary 6.2); and
* descending-linear-forest compatibility belongs to the different,
  unlabelled edge-set factor problem (Theorem 6.3).

## 7. What the theorem does not preserve

The construction is deliberately selector-level.

1. **Successor legality.**  Flags on two consecutive roots must satisfy the
   literal age-transition inequalities.  An SCD chooses flags rootwise and
   supplies no legal turn factor between them.
2. **Euler balance and connectivity.**  The theorem has no chronology and
   no one-component circulation.
3. **Residence and upper shadows.**  The arbitrary continuation below a
   chain minimum is harmless for marked lower targets but may be unusable in
   a resident upper-complete carrier.
4. **A small global-order menu.**  Every local flag is induced by some total
   order, but the SCD proof does not place all roots in a bounded or
   support-optimal common menu.

Thus the corrected remaining gate is:

> **Transition-compatible protected selector.**  Starting from the exact
> protected marked-chain factor of Theorem 5.1, choose successor turns so
> that every root has balanced literal indegree/outdegree and the selected
> factor admits one Euler chronology, without losing target exactness.

The all-depth cubic absorber theorem gives a spread local mechanism for
changing complete flags while preserving the other suffix marginals.  Its
physical turn-safe lifting is precisely what is still missing.

## 8. Consequence for the research frontier

| Gate | Status |
|---|---|
| symmetric fractional marginals | proved |
| unrestricted one-copy nested-chain selector | proved by Theorem 3.1 |
| bounded protected rankwise containment | proved |
| bounded prescribed complete flags, selector only | proved by Theorem 5.1 |
| bounded occurrence-labelled prescribed marks | exact target-injectivity criterion, Theorem 6.1 |
| fully marked distinct-root prefixes | exact vertex-disjointness criterion, Corollary 6.2 |
| bounded unlabelled edge fragments | exact descending-linear-forest criterion, Theorem 6.3 |
| legal balanced successor factor on the selected flags | open |
| one Euler chronology plus upper/residence/compiler guards | open |

Accordingly, an additive-constant proof cannot fail merely because the high
target chains do not admit an integral owner assignment.  Any surviving
failure must come from the prescribed/physical correlation rows.
