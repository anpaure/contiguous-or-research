# Mixed-SCD chain covers: determinant two, odd sets, and the integral grouping obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver,
probabilistic black box, or web input is used.

## 0. Verdict

The complete mixed-SCD orbit has exact dynamic safe-option
biregularity, but its chain occurrences cannot be rounded by a direct
TU or Birkhoff theorem.

Let \(M_{\rm ch}\) be the incidence matrix whose rows are Boolean sets and
whose columns are symmetric chains appearing in the complete labelled
coordinate orbit of one SCD.  For every central radius

\[
                         h=m-2r\ge2,                              \tag{0.1}
\]

\(M_{\rm ch}\) contains the minor

\[
 \boxed{
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix}},
 \qquad\det=-2.                                                  \tag{0.2}
\]

Thus \(M_{\rm ch}\) is not totally unimodular.  The same minor survives
after the chains are paired with one fixed companion chain in the other
half: the physical product-path/owner incidence matrix is also non-TU.
Allowing an owner-disjoint mixture therefore does not restore a direct
network-matrix argument.

There is an exact integral invariant.  For every family \(Q\) of Boolean
sets and every exact chain cover \(x\),

\[
 \sum_C |C\cap Q|x_C=|Q|.                                       \tag{0.3}
\]

Modulo two,

\[
 \boxed{
 \sum_{\substack{C:\\|C\cap Q|\ {\rm odd}}}x_C
                \equiv |Q|\pmod2.}                              \tag{0.4}
\]

Hence an odd \(Q\) requires an odd number of selected chains meeting
\(Q\) oddly.  If a history-filtered option catalogue contains only
even-intersection columns on \(Q\), no integral SCD exists, although the
three half-columns in (0.2), each with weight \(1/2\), cover the three
rows fractionally.  This is the missing odd-set/blossom layer behind the
mixed-orbit empty-rectangle theorem.

The obstruction is used only at its proved scope.  It does not say that
the full history-filtered orbit necessarily violates an odd-set
condition, and it does not prove that every SCD is vulnerable.  It proves
that dynamic endpoint biregularity and the fractional orbit average do
not imply an integral robust SCD or path atlas.  Such an atlas must
control (0.4), or bypass half-chain grouping with a stronger
owner-dependent construction carrying a complete product-owner ledger.

## 1. The two possible mixing variables

Let \({\mathfrak E}\) be the complement-closed labelled orbit from the
mixed-SCD theorem.  There are two inequivalent linear formulations.

### Whole-colour variables

If \(y_\gamma\) selects a whole SCD colour
\(\gamma\in{\mathfrak E}\), then every colour covers every Boolean set
once.  The chain-cover equations reduce to

\[
                         \sum_{\gamma\in{\mathfrak E}}y_\gamma=1.
                                                                    \tag{1.1}
\]

This is a simplex and is integral: choose one global colour.  It is not
the mixed-option theorem.  A colour remains admissible only if all of
the route histories assigned to it are simultaneously safe.  The orbit
calculation proves safety for each independently rooted occurrence, not
the existence of one colour safe for all exponentially many adaptive
states.

### Chain-occurrence variables

Let \({\cal C}_{\rm orb}\) be the multiset of individual chains in all
labelled colours and use variables \(x_C\).  One owner-disjoint mixed SCD
requires

\[
                         M_{\rm ch}x={\bf1},
             \qquad x\in\mathbb Z_{\ge0}^{{\cal C}_{\rm orb}}.  \tag{1.2}
\]

History safety deletes or decorates individual columns.  This preserves
the endpoint Kneser inequalities but destroys the whole-colour simplex
(1.1).  The rest of the note audits the integrality of (1.2).

## 2. A determinant-two minor at every useful radius

Fix \(r\ge1\) and \(h=m-2r\ge2\).  Choose a set \(D\) of size \(r-1\)
and four further labels \(1,2,3,4\), disjoint from \(D\).  Put

\[
 A=D\cup\{1\},\qquad
 B=D\cup\{1,2\},\qquad
 E=D\cup\{1,2,3\}.                                  \tag{2.1}
\]

Thus \(A\subset B\subset E\) have ranks \(r,r+1,r+2\).

Consider the following three saturated symmetric chains of minimum rank
\(r\).  Only their first three entries are displayed:

\[
\begin{array}{c|ccc}
 P_{AB}&A&B&D\cup\{1,2,4\}\\
 P_{AE}&A&D\cup\{1,3\}&E\\
 P_{BE}&D\cup\{2\}&B&E.
\end{array}                                                     \tag{2.2}
\]

Complete each row by adding \(h-2\) fresh coordinates in any order, with
the remaining \(r\) coordinates outside its top.  This is possible
because the displayed rank-\((r+2)\) set is followed by exactly \(h-2\)
additions before rank \(m-r\).

### Lemma 2.1 (all three columns occur in the full orbit)

Let \({\mathscr D}\) be any SCD of \(B_m\).  Every chain in (2.2)
appears in the labelled coordinate orbit of \({\mathscr D}\).

#### Proof

Every SCD has

\[
                         b_r=\binom mr-\binom m{r-1}>0           \tag{2.3}
\]

chains of minimum rank \(r\).  Such a chain is specified by three
ordered parts: its bottom \(r\)-set, its ordered \(h\)-letter active
word, and its outside \(r\)-set.  The symmetric group is transitive on
these ordered partitions.  Hence the orbit of any one minimum-\(r\)
chain contains every saturated symmetric chain with that minimum,
including (2.2). \(\square\)

### Theorem 2.2 (chain-incidence non-TU)

On rows \(A,B,E\) and columns \(P_{AB},P_{AE},P_{BE}\), the chain
incidence matrix is exactly (0.2).  Consequently \(M_{\rm ch}\) is not
totally unimodular for every radius \(h\ge2\).

#### Proof

The first column contains \(A,B\) and avoids \(E\); the second contains
\(A,E\) and avoids \(B\); the third contains \(B,E\) and avoids \(A\).
This gives (0.2), whose determinant is \(-2\). \(\square\)

The construction may be placed at

\[
                         h=\sqrt m+O(1),                         \tag{2.4}
\]

with the parity of \(m\).  Thus it lies inside the product-path core used
at \(H=\sqrt m\log\log m\); it is not an exterior-rank artefact.

## 3. The same minor in physical product-path ownership

Take a disjoint second half and fix one symmetric chain

\[
                         R_r\subset R_{r+1}\subset\cdots
                              \subset R_{m-r}                    \tag{3.1}
\]

of minimum rank \(r\).  Pair each chain \(P\) in (2.2) with \(R\).
Its rank-\(m\) product diagonal is

\[
 {\cal P}(P,R)
   =\bigl(P_{r+t}\cup R_{m-r-t}:0\le t\le h\bigr).               \tag{3.2}
\]

Define three physical middle owners

\[
 X_A=A\cup R_{m-r},\qquad
 X_B=B\cup R_{m-r-1},\qquad
 X_E=E\cup R_{m-r-2}.                                           \tag{3.3}
\]

### Theorem 3.1 (product-owner non-TU)

On owner rows \(X_A,X_B,X_E\) and product-path columns

\[
 {\cal P}(P_{AB},R),\quad
 {\cal P}(P_{AE},R),\quad
 {\cal P}(P_{BE},R),                                            \tag{3.4}
\]

the physical incidence matrix is again (0.2).

#### Proof

At phase \(t=0,1,2\), membership of \(X_A,X_B,X_E\) in (3.2) is
exactly membership of \(A,B,E\) in the corresponding first-half chain.
The fixed second-half member in (3.3) merely records the phase.  Apply
(2.2). \(\square\)

Thus replacing one global SCD by independently coloured product paths
does not make the natural owner/path configuration matrix TU.  A TU
extended formulation may still exist after extra state variables are
introduced, but it cannot be inferred from the projected incidence
matrix or from endpoint biregularity.

## 4. The exact odd-set law

Let \({\cal K}\) be any allowed chain catalogue and let
\[
                         M_{\cal K}x={\bf1}                     \tag{4.1}
\]
be an integral exact cover.  For an arbitrary row family \(Q\), sum the
equations indexed by \(Q\).

### Theorem 4.1 (chain-cover parity)

Every integral exact cover satisfies (0.3)--(0.4).  In particular, if
\(|Q|\) is odd, at least one selected chain has odd intersection with
\(Q\).

#### Proof

Interchanging the two finite sums gives
\[
 |Q|=\sum_{Z\in Q}\sum_{C\ni Z}x_C
     =\sum_C|C\cap Q|x_C.
\]
Reduce the identity modulo two. \(\square\)

There is also an approximate version.  If \(L\) is the uncovered row
set, then

\[
 \sum_{\substack{C:\\|C\cap Q|\ {\rm odd}}}x_C
       \equiv |Q\setminus L|\pmod2.                              \tag{4.2}
\]

Hence, if every allowed column meets an odd \(Q\) evenly, at least one
row of \(Q\) must be left uncovered.

### Corollary 4.2 (the triangle blossom)

Restrict to the three rows \(Q=\{A,B,E\}\) and the three pair columns in
(2.2).  The fractional vector

\[
                         x_{AB}=x_{AE}=x_{BE}={1\over2}          \tag{4.3}
\]

covers every row exactly.  No integral vector does.  Equivalently, every
integral packing of these columns obeys the blossom inequality

\[
                         x_{AB}+x_{AE}+x_{BE}\le1,               \tag{4.4}
\]

whereas (4.3) has left side \(3/2\).

#### Proof

Every displayed column covers two of the three rows.  Integrally,
pairwise row-disjointness permits at most one column, proving (4.4).
Equation (4.3) is checked row by row. \(\square\)

For pairwise disjoint odd gadgets \(Q_1,\ldots,Q_s\), if the allowed
catalogue has only even intersections on every \(Q_i\), then any integral
packing leaves at least one row in every gadget.  Thus odd-set failures
can accumulate at coefficient scale; they are not necessarily one
global parity bit.

## 5. Relation to the dynamic empty-rectangle theorem

The mixed-orbit theorem concerns a bipartite graph:

\[
 \{\hbox{typed queue states}\}
       \longleftrightarrow
 \{\hbox{independently coloured endpoint options}\}.            \tag{5.1}
\]

Each typed block is biregular, so its normalized incidence matrix has
the Hall property.  The chain-cover matrix adds a second family of rows:

\[
 \{\hbox{every Boolean set at every intermediate rank}\}.       \tag{5.2}
\]

Three individually legal option columns can have the overlap pattern
(0.2) on these new rows.  The endpoint graph sees three available
options; it does not see the blossom inequality (4.4).

Consequently the following implication is false without an additional
hypothesis:

\[
 \begin{array}{c}
 \text{zero empty-rectangle deficit in every dynamic type block}\\
 +\text{fractional orbit chain cover}
 \end{array}
 \quad\Longrightarrow\quad
 \text{integral robust SCD/path atlas}.                          \tag{5.3}
\]

This does not assert that the actual full safe catalogue violates
(4.2).  It identifies the exact unproved condition: all history-filtered
odd-set cuts must retain enough odd-intersection chain occurrences,
simultaneously with the ordinary Hall cuts.

## 6. Why the standard network extension does not yet repair it

If one SCD is fixed in advance, its chains are already an integral
partition.  Likewise, a fixed lower-half path forest can be represented
by ordinary arc-flow variables in the Boolean inclusion DAG; that
network matrix is TU.

The mixed problem is different.  The admissible arc word for a chain
depends on the queue state assigned to its endpoint.  Different endpoints
therefore carry different forbidden-label sets.  Sharing an intermediate
Boolean vertex couples these terminal-dependent path commodities.  After
the path variables are projected to chain choices, the coupling contains
the triangle (0.2).

Thus a successful extended formulation must do more than restore the
usual inclusion-DAG arc variables.  It must also prove that the
terminal/history commodities can be recoupled by integral local trades.
No such recoupling theorem follows from the current SCD-orbit symmetry.

There is one clean alternative.  Restrict mixing to whole SCD colours.
Then (1.1) is integral automatically, but the missing theorem becomes:

> find one global colour for which the entire coherently generated route
> is safe.

The per-occurrence survival probability
\((\log m)^{-O(1)}\) does not imply this exponentially simultaneous
statement, and the BTK countercuts show that the quantifier exchange is
invalid.

## 7. Exact remaining integral gate

Let \({\cal K}_{\rm safe}\) be the chain or product-path occurrences
which survive the actual two-queue histories.  A sufficient integral
theorem must establish all three items:

1. **ordinary Hall/Farkas cuts:** the fractional cover cone contains the
   desired owner vector up to \(o(W/H)\);
2. **odd-set supply:** for every relevant odd row family \(Q\), the safe
   catalogue contains enough odd-intersection columns to satisfy
   (4.2), with aggregate blossom deficiency \(o(W/H)\); and
3. **normality/absorption:** after the lattice conditions are met, the
   safe chain semigroup has no coefficient-scale holes.

The mixed-orbit theorem proves only the endpoint projection of item 1.
The determinant-two and parity theorems prove that items 2--3 cannot be
deleted from the statement.

No integral robust SCD or owner-disjoint path atlas is obtained here.
What is obtained is a sharp negative resolution of the proposed direct
rounding mechanism:

\[
 \boxed{\text{the natural chain and product-path matrices are non-TU,
 and dynamic biregularity does not supply their odd-set constraints.}}
                                                                    \tag{7.1}
\]

The smallest positive continuation is therefore an owner-preserving
four-chain trade which changes the parity class in (4.2) while keeping
the two queue-safe endpoint types fixed.  Such trades would be the
integral absorbers needed to turn the mixed orbit into an actual atlas.
