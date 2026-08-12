# GMM Corollary 2: successor normal form and the exact triple-union boundary

Date: 2026-07-26

Method: pure mathematics and local-source audit only; no computation or web
input.

## 0. Verdict

There is no canonical successor map in Gregor--Mička--Mütze Corollary 2.
For the two-level saturating-cycle case, the proof in the local primary
source `tmp/central/gmlc2.tex` cites Mütze--Su, Theorem 9.  The corollary is
an existence statement and does not choose one of the generally many
saturating cycles, a coordinate order, or a lexical successor.

For any chosen output, the exact successor rule is nevertheless forced into
the following normal form.  If \(\sigma\) is the cyclic successor on the
rank-\((m-1)\) sets, then

\[
 \sigma(R)=R-d_+(R)+a_+(R),
 \qquad
 \sigma^{-1}(R)=R-d_-(R)+a_-(R),                    \tag{0.1}
\]

and the opposite upper colour at \(R\) is

\[
 \boxed{U(R)=R\cup\{a_-(R),a_+(R)\}.}               \tag{0.2}
\]

The published assertion says that \(\sigma\) is one cycle and that
\(R\mapsto R\cup\sigma(R)\) is injective.  It says nothing about
injectivity or near-injectivity of (0.2).

This distinction is substantive.

* A displayed valid saturating cycle in \(J(6,3)\) already has four upper
  duplicates among fifteen occurrences.
* The different, explicit GJM lexical lower forest has a rigorous linear
  family of triple-union collisions: after discarding its path boundaries,
  at least

  \[
   \binom{2m-1}{m-2}-\frac{4W}{m+2}
    =\left(\frac14-o(1)\right)W                    \tag{0.3}
  \]

  pairwise disjoint collision pairs remain.

The second bullet is a no-go for the GJM lexical successor rule, not for an
unspecified GMM/Mütze--Su saturating cycle.  Consequently neither a positive
near-injectivity theorem nor a linear negative theorem for the actual
Corollary 2 existential output is presently imported.

## 1. What Corollary 2 actually imports

The local GMM source states that every interval of consecutive Boolean
levels has a saturating cycle and a tight enumeration.  In its proof, the
case of two nonboundary levels for saturating cycles is discharged by

\[
 \text{Mütze--Su, Theorem 9, `Bipartite Kneser graphs are Hamiltonian'.}
\tag{1.1}
\]

No successor formula is stated in the corollary.  In particular, the
following are not consequences of its quantifiers:

1. that the lower sets occur in a lexical, cool-lex, Greene--Kleitman, or
   PBBS order;
2. that a particular Middle Levels Hamilton cycle is used inside the
   construction;
3. that the predecessor and successor of a lower set are functions of a
   bounded local pattern in its bitstring;
4. that any second-window colour is controlled.

The workspace also contains the implementation
`tmp/cos/code/bits/sat.cpp`.  For two levels it invokes
`SatCycle::sat_2`; this recursively splits on a coordinate and, in the
middle-level base case, invokes `HamCycle`, whose states are transported by
plane-tree rotations.  This is one separately fixed algorithm.  It is not a
formula asserted by Corollary 2, and no workspace theorem derives its
triple-union collision count.

Thus phrases such as "the GMM lexical successor" conflate distinct
constructions.

## 2. The complete successor/predecessor normal form

Let

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0         \tag{2.1}
\]

be any simple saturating cycle between ranks \(m-1,m\).  The \(R_i\)'s
are all rank-\((m-1)\) sets, the \(X_i\)'s are distinct rank-\(m\) sets,
and

\[
 R_i\subset X_i\supset R_{i+1}.                    \tag{2.2}
\]

Define

\[
 \sigma(R_i)=R_{i+1},\qquad \pi(R_i)=R_{i-1}.       \tag{2.3}
\]

### Theorem 2.1 (exact rule)

There are unique labels

\[
 d_+(R),d_-(R)\in R,\qquad
 a_+(R),a_-(R)\notin R                               \tag{2.4}
\]

such that

\[
 \sigma(R)=R-d_+(R)+a_+(R),
 \qquad
 \pi(R)=R-d_-(R)+a_-(R).                            \tag{2.5}
\]

Moreover,

\[
 X_i=R_i\cup\{a_+(R_i)\},
 \qquad
 X_{i-1}=R_i\cup\{a_-(R_i)\},                      \tag{2.6}
\]

the two insertion labels are distinct, and

\[
 \boxed{
 X_{i-1}\cup X_i
 =R_{i-1}\cup R_i\cup R_{i+1}
 =R_i\cup\{a_-(R_i),a_+(R_i)\}.}                   \tag{2.7}
\]

#### Proof

The two lower neighbours of \(X_i\) are distinct facets, so

\[
 X_i=R_i\cup R_{i+1}.
\]

Thus consecutive lower sets differ by one exchange, giving the unique
labels in (2.5), and the added label gives (2.6).  If
\(a_-(R_i)=a_+(R_i)\), then (2.6) would give
\(X_{i-1}=X_i\), contradicting simplicity.  Taking the union in (2.6)
proves (2.7). \(\square\)

Consequently the full imported information is exactly:

* \(\sigma\) is a single-cycle permutation of
  \(\binom{[n]}{m-1}\);
* every arc \(R\to\sigma(R)\) is a Johnson arc;
* the first-window owner map
  \(R\mapsto R\cup\sigma(R)\) is injective.

The second-window map (2.7) is new data.  With

\[
 c_+(\sigma)
 =N-\left|\left\{
 R\cup\{a_-(R),a_+(R)\}:R\in\binom{[n]}{m-1}
 \right\}\right|,                                  \tag{2.8}
\]

the desired upper near-saturation is precisely \(c_+(\sigma)=o(W)\).

## 3. A literal noninjective saturating cycle

On \([6]\), take the cyclic lower sequence

\[
\begin{split}
 26,36,16,15,25,56,45,24,23,13,35,34,46,14,12.
\end{split}                                           \tag{3.1}
\]

Consecutive unions are

\[
\begin{split}
 236,136,156,125,256,456,245,234,123,135,345,346,146,
 124,126,
\end{split}                                           \tag{3.2}
\]

which are fifteen distinct three-sets.  Hence (3.1) is exactly the lower
projection of a simple saturating cycle between ranks two and three.

Its opposite four-set multiset is

\[
\begin{split}
1236,1236,1356,1256,1256,2456,2456,2345,1234,1235,\
1345,3456,1346,1246,1246.
\end{split}                                           \tag{3.3}
\]

Thus the triple-union map has support eleven and collision excess four.
This proves that injectivity is not a formal consequence of saturation.
It is a finite counterexample only; by itself it says nothing about an
asymptotic little-oh bound.

## 4. A rigorous linear collision family for the explicit lexical rule

This section concerns the GJM lower lexical forest, not the unspecified
cycle in Corollary 2.  It is included because it is the one concrete
successor/predecessor rule in the workspace for which the triple-union
question can presently be decided.

Work in dimension \(2m+1\), and let \(F_-\) be the contracted forest from
the two lower lexical matchings.  It is a spanning linear forest on the
rank-\(m\) owners with one edge for every
\(x\in\binom{[2m+1]}{m-1}\).  Hence, with

\[
 W=\binom{2m+1}m,\qquad
 N=\binom{2m+1}{m-1},\qquad
 D=W-N=\frac{2W}{m+2},                               \tag{4.1}
\]

it has exactly \(D\) path components.

For a lower word \(x\), scan its down-steps by the published lexical rule.
The two incident middle owners are obtained by changing the last two
down-steps in this order separately to up-steps.  Their union is therefore

\[
 \psi(x)=x\text{ with both selected down-steps changed to up-steps}.
\tag{4.2}
\]

### Theorem 4.1 (disjoint lexical collisions)

The fibres of \(\psi\) contain at least

\[
 B_m:=\binom{2m-1}{m-2}                              \tag{4.3}
\]

pairwise disjoint colliding pairs.

#### Proof

Choose any word \(y\) of length \(2m-1\) and weight \(m-2\).  Write

\[
 y=A,0,B                                             \tag{4.4}
\]

at the zero where the lattice path first attains its global minimum.
Form

\[
 x=A\,010\,B,\qquad x'=A\,001\,B.                    \tag{4.5}
\]

In \(x\), the first and third displayed zeros are the last two down-steps
in lexical order: they are the two leftmost down-steps starting at the
minimum possible starting height.  In \(x'\), the second displayed zero is
the unique down-step starting one level lower, and the first displayed zero
is next-last.  Therefore

\[
 \psi(x)=A,111,B=\psi(x').                         \tag{4.6}
\]

The pairs are disjoint.  The selected zeros are intrinsic; they are
distance two in the \(010\) member and adjacent in the \(001\) member.
Their positions recover the displayed block, and deleting its final two
positions recovers the unique \(y\).  Counting \(y\) proves (4.3).
\(\square\)

For every edge of \(F_-\) not incident with a path endpoint, the two
neighbouring forest edges give a predecessor and successor lower label.
If these labels are \(R^-,R,R^+\), then the two middle endpoints of the
edge labelled \(R\) are

\[
 R^-\cup R,\qquad R\cup R^+,
\]

and consequently

\[
 \psi(R)=R^-\cup R\cup R^+.                         \tag{4.7}
\]

At most \(2D\) edge labels are incident with path endpoints.  Since the
pairs in Theorem 4.1 are disjoint, deleting every pair which contains a
boundary edge leaves at least

\[
 B_m-2D                                                \tag{4.8}
\]

pairwise disjoint equalities of the literal triple-union form (4.7).  The
exact ratio is

\[
 \frac{B_m}{W}=\frac{m-1}{2(2m+1)},
 \qquad
 \frac{2D}{W}=\frac4{m+2}.                          \tag{4.9}
\]

Thus (4.8) is \((1/4-o(1))W\).

This is a theorem-grade linear obstruction to the explicit lexical path
rule.  Turning the forest into one saturating cycle while changing only
\(o(W)\) of its edges would preserve a linear collision excess, but such a
sparse exact joining theorem is not presently proved and is not supplied by
GMM Corollary 2.

## 5. Imported-versus-proved boundary

The precise status is:

1. **Imported from Corollary 2:** existence of some saturating incidence
   cycle, hence some \(\sigma\) satisfying the three first-window bullets
   after Theorem 2.1.
2. **Proved abstractly here:** the coordinate normal form (2.5)--(2.7), the
   exact collision statistic (2.8), and the finite noninjective certificate
   (3.1)--(3.3).
3. **Proved for a different explicit construction:** the linear lexical
   collision family (4.3)--(4.9).
4. **Not proved:** \(c_+(\sigma)=o(W)\) for a suitably chosen GMM/Mütze--Su
   saturating cycle; \(c_+(\sigma)=\Omega(W)\) for every such cycle; or a
   sparse joining of the GJM lexical forest into one saturating cycle.

Therefore the triple-union gate remains open for the actual Corollary 2
route.  What is closed is the attribution error: Corollary 2 itself does
not contain a concrete successor/predecessor rule from which a
near-injectivity estimate can be read off.

## 6. Construction-specific audit of `SatCycle::sat_2`

This section analyzes the optional local implementation mathematically.  It
does not identify that implementation with the existential choice in
Corollary 2.

For \(n>2k+1\), let \(C_{n,k}\) denote the lower rank-\(k\) cyclic order
produced by `sat_2(k,forward)`.  Let

\[
 A_{n,k}=0^{\,n-k}1^k,\qquad
 B_{n,k}=0^{\,n-k-1}1^k0                            \tag{6.1}
\]

be its two distinguished consecutive lower vertices, and let \(z\) be
the final coordinate.  The distinguished edge has union colour
\(A_{n,k+1}\).

### Proposition 6.1 (exact Pascal splice)

When \(n>2k+1\), the undirected lower cycle \(C_{n,k}\) is obtained as
follows.

1. Take \(C_{n-1,k}\), delete its distinguished edge
   \(A_{n-1,k}B_{n-1,k}\), and traverse the remaining path backwards.
   Embed every set with \(z\) absent.
2. Take \(C_{n-1,k-1}\), delete its distinguished edge
   \(A_{n-1,k-1}B_{n-1,k-1}\), and traverse the remaining path forwards.
   Adjoin \(z\) to every set.
3. Add the two cross edges

   \[
    \{A_{n-1,k-1}+z,A_{n-1,k}\},\qquad
    \{B_{n-1,k},B_{n-1,k-1}+z\}.                    \tag{6.2}
   \]

#### Proof

The full call begins

\[
 A_{n,k}, A_{n,k+1}, B_{n,k}.
\]

Here

\[
 A_{n,k}=A_{n-1,k-1}+z,\qquad
 B_{n,k}=A_{n-1,k}.
\]

The first recursive stack item in the long path is the backward
\((n-1,k)\) call, from \(A_{n-1,k}\) to \(B_{n-1,k}\).  The next two
literal flips first insert \(z\) and then delete coordinate \(n-k-2\),
ending at \(B_{n-1,k-1}+z\).  The final recursive item is the forward
\((n-1,k-1)\) call, which ends at
\(A_{n-1,k-1}+z=A_{n,k}\).  These are exactly the two paths and cross
edges above. \(\square\)

If \({\cal X}_{n,k}\) is the set of selected rank-\((k+1)\) union
colours, the same splice gives the exact owner recursion

\[
\boxed{
 \begin{aligned}
 {\cal X}_{n,k}
  ={}&\bigl({\cal X}_{n-1,k}\setminus
              \{A_{n-1,k+1}\}\bigr)\\
    &\dot\cup\ \{X+z:X\in{\cal X}_{n-1,k-1}\}\\
    &\dot\cup\ \{B_{n-1,k}+z\}.
 \end{aligned}}                                      \tag{6.3}
\]

Indeed, the first child loses its distinguished owner.  The second child's
distinguished owner \(A_{n-1,k}+z\) is restored by the first cross edge,
while the second cross edge adds \(B_{n-1,k}+z\).  The latter is not a
selected owner of the nonmiddle second child; this is the omitted
\(B_{n-1,k}\) vertex recorded in the `sat_2` interface.  Thus (6.3) is a
disjoint union and re-proves first-window injectivity inductively.

### Proposition 6.2 (four-entry triple-union recurrence)

Let \(c_{n,k}\) be the collision excess of the triple-union multiset of
\(C_{n,k}\).  For \(n>2k+1\),

\[
 \boxed{
 \left|c_{n,k}-c_{n-1,k}-c_{n-1,k-1}\right|\le4.}   \tag{6.4}
\]

Here a \(k=0\) child is assigned collision excess zero; its sole lower
vertex is one of the connector entries covered by the error term.

#### Proof

Away from the endpoints of the two deleted distinguished edges, the two
neighbours of every lower vertex are unchanged.  Reversing a child path
does not change the unordered predecessor/current/successor union.
Therefore every unaffected triple union in the first child is inherited
without \(z\), and every unaffected triple union in the second child is
inherited with \(z\) adjoined.

Before the four endpoint entries are replaced, the two child multisets
have disjoint supports: every value in the first omits \(z\), while every
value in the second contains \(z\).  Their collision excess is therefore
the sum of the child excesses.  Replacing one occurrence in a multiset
changes the size of its support, and hence its collision excess, by at most
one.  There are at most four endpoint occurrences.  This proves (6.4).
\(\square\)

The recursion stops either at \(k=0\) or at a Middle Levels state
\((2r+1,r)\).  Let

\[
 \beta_r:=c_{2r+1,r}                                  \tag{6.5}
\]

be the triple-union collision excess of the particular Middle Levels
Hamilton cycle invoked by `HamCycle`.  Coordinate permutations used when
installing that base do not change \(\beta_r\).

### Theorem 6.3 (exact Catalan-weighted reduction)

For the requested even-ground call \((n,k)=(2m,m-1)\),

\[
 \boxed{
 \left|
 c_{2m,m-1}
 -\sum_{r=1}^{m-1}\operatorname{Cat}_{m-r-1}\,\beta_r
 \right|
 \le4\left(\sum_{s=0}^{m-1}\operatorname{Cat}_s-1\right).} \tag{6.6}
\]

In particular, since

\[
 \sum_{s=0}^{m-1}\operatorname{Cat}_s
 =O(\operatorname{Cat}_{m-1})
 =O\!\left(\frac1m\binom{2m}m\right),               \tag{6.7}
\]

the implementation satisfies

\[
 \boxed{
 c_{2m,m-1}
 =\sum_{r=1}^{m-1}\operatorname{Cat}_{m-r-1}\,\beta_r
   +O(W/m).}                                         \tag{6.8}
\]

#### Proof

At a recursive state put \(h=n-2k-1\).  The first child
\((n-1,k)\) changes \(h\) to \(h-1\), and the second child
\((n-1,k-1)\) changes it to \(h+1\).  Starting from \(h=1\), a leaf
of type \((2r+1,r)\) requires

\[
 m-r-1\quad\text{up-steps},\qquad
 m-r\quad\text{down-steps},
\]

with positive height before the last step.  The first-passage ballot count
is

\[
 \operatorname{Cat}_{m-r-1}.                       \tag{6.9}
\]

The number of \(k=0\) leaves is \(\operatorname{Cat}_{m-1}\), by the
same Catalan recursion.  Hence the total number of leaves is

\[
 L_m=\sum_{s=0}^{m-1}\operatorname{Cat}_s.           \tag{6.10}
\]

Every nonleaf has two children, so there are \(L_m-1\) splices.  Iterating
(6.4), using (6.9), proves (6.6).  Finally
\(L_m=O(\operatorname{Cat}_{m-1})\), while exactly

\[
 \operatorname{Cat}_{m-1}
 =\frac{1}{2(2m-1)}\binom{2m}m,                     \tag{6.11}
\]

which proves (6.7)--(6.8). \(\square\)

### Consequence 6.4 (where a linear obstruction can occur)

Neither the recurring connectors nor any fixed-size leaf pattern can force
\(\Omega(W)\) triple-union collisions in this implementation.  All
connectors together contribute only \(O(W/m)\), and for each fixed \(r\)
the total contribution of the \((2r+1,r)\) leaves is also \(O(W/m)\).

The construction-specific question reduces, up to \(O(W/m)\), to the
Catalan-weighted collision excesses \(\beta_r\) of the chosen growing
Middle Levels base cycles.  In particular:

\[
 \beta_r=o\!\left(\binom{2r+1}r\right)\quad(r\to\infty)
 \quad\Longrightarrow\quad
 c_{2m,m-1}=o(W).                                    \tag{6.12}
\]

Indeed, the recursive leaves partition the root lower sets, so

\[
 \sum_{r=1}^{m-1}\operatorname{Cat}_{m-r-1}
       \binom{2r+1}r
 \le \binom{2m}{m-1}.                                \tag{6.13}
\]

Given \(\varepsilon>0\), the terms with sufficiently large \(r\) in
(6.12) are at most \(\varepsilon\) times (6.13), while every fixed finite
set of small \(r\)'s contributes only \(O(W/m)\).  Then let
\(\varepsilon\to0\).

Conversely, a linear lower bound for the implementation cannot be obtained
from the Pascal connectors alone; it must come from a positive weighted
density of collisions in the growing Middle Levels bases.  No such base
estimate is provided by Corollary 2 or by the recursion in `sat.cpp`.
