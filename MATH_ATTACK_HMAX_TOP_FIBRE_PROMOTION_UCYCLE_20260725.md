# The \(H=m-1\) top-fibre reduction: promotion words and the transversal Ucycle gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad H=m-1.
\tag{0.1}
\]

At this extreme depth there are only \(2m\) possible collar tops,

\[
 U_r=[2m]\setminus\{r\}.
\tag{0.2}
\]

A full useful state over \(U_r\) is exactly a permutation of \(U_r\); its
middle owner is the set of its first \(m\) letters.  A distinct-owner
bridge-one promotion moves a letter outside that first \(m\)-prefix to the
front.  Thus promotion paths are exactly LRU-miss words: every block of
\(m+1\) consecutive requested symbols is repetition-free, and the middle
owners are their consecutive \(m\)-windows.

This gives an exact reformulation of the proposed construction.  One must
choose one top fibre and one permutation state for every middle owner so
that:

1. the selected middle \(m\)-windows partition \(\binom{[2m]}m\);
2. the recency prefixes cover every nonempty proper Boolean mask; and
3. the selected states form \(o(W/m)\) promotion paths.

Such a system would give a contiguous-OR word of length

\[
 W+O(mp+m^2)=W+o(W).
\tag{0.3}
\]

There is no fractional capacity obstruction: the uniform distribution on
all admissible fibre states has owner degree one, prefix load
\(W/\binom{2m}k\ge1\) at every rank \(k\), and an exact fractional
promotion circulation.

There is also a genuine local integral factor.  In every fixed fibre, the
exact odd-wreath factor on \(2m-1\) points becomes, by complementation, an
exact factor of all fibre owners into promotion cycles of length \(2m-1\).
However, this is quantitatively too fragmented:

\[
 \frac{W}{2m-1}=\Theta(W/m)
\tag{0.4}
\]

components are still required by any onefold construction using only whole
local wreath cycles.  Likewise, every promotion path whose owners retain
one fixed included coordinate has length at most \(m\), so fixed-core
hierarchies also incur \(\Omega(W/m)\) components.

The free-extension problem therefore survives both earlier canonical
no-gos, but is not solved here.  Its exact remaining content is a
transversal central-Ucycle problem: splice the resolvable local promotion
cycles, while selecting exactly one of the \(m\) missing-coordinate
occurrences of every middle set, into trajectories of average length
\(\omega(m)\), and simultaneously retain all-rank prefix coverage.

## 1. Full-depth states are fibre permutations

For \(H=m-1\), a full radius-\(H\) state has the form

\[
 \omega=(L;z_1,\ldots,z_{2m-2};R),
 \qquad |L|=|R|=1.
\tag{1.1}
\]

Write \(R=\{r\}\).  Its collar top is

\[
 U_r=[2m]\setminus\{r\}
 =L\cup\{z_1,\ldots,z_{2m-2}\}.
\tag{1.2}
\]

If \(L=\{u_1\}\) and \(z_i=u_{i+1}\), identify the useful state with

\[
 \sigma=(u_1,u_2,\ldots,u_{2m-1})\in\operatorname{Sym}(U_r).
\tag{1.3}
\]

Its rank-\(k\) prefix mask is

\[
 P_k(\sigma)=\{u_1,\ldots,u_k\},
\qquad1\le k\le2m-1,
\tag{1.4}
\]

and its middle owner is

\[
 X(\sigma)=P_m(\sigma).
\tag{1.5}
\]

Conversely, for every middle owner \(X\) and every \(r\notin X\), every
permutation of \(U_r\) whose first \(m\) letters are \(X\) is a maximal-chain
extension of \(X\).  Thus each owner has exactly

\[
 \boxed{m\cdot m!\,(m-1)!}
\tag{1.6}
\]

admissible top-fibre states.

### Proposition 1.1 (promotion is move-to-front outside the cache)

Let \(\sigma=(u_1,\ldots,u_{2m-1})\).  Every distinct-owner promotion
successor is

\[
 \boxed{
 \operatorname{mtf}_{u_j}(\sigma)
 =(u_j,u_1,\ldots,u_{j-1},u_{j+1},\ldots,u_{2m-1}),
 \qquad m<j\le2m-1.}
\tag{1.7}
\]

Its owner is

\[
 \boxed{
 X'=X(\sigma)-\{u_m\}+\{u_j\}.}
\tag{1.8}
\]

Promotion preserves the fibre \(U_r\).

#### Proof

In the general bridge-one promotion formula, \(L\) has one element, so the
removed lower element is forced to be \(u_1\).  Moving \(z_{j-1}=u_j\)
from the singleton list into \(L\), while moving \(u_1\) to the front of
the singleton list, gives exactly (1.7).  The owner changes precisely when
the promoted position lies after the first \(m\) letters, and then the new
prefix drops \(u_m\), proving (1.8).  The union of all useful blocks is
unchanged, so the top remains \(U_r\). \(\square\)

The graph of all fibre permutations under (1.7) is regular: every state
has \(m-1\) successors and \(m-1\) predecessors.

## 2. Exact LRU-word representation

Promotion paths have a useful word description which contains all their
chronology.

### Theorem 2.1 (promotion path--recency word equivalence)

Fix a fibre \(U\), \(|U|=2m-1\).  A directed promotion path

\[
 \sigma_0\to\sigma_1\to\cdots\to\sigma_{\ell-1}
\tag{2.1}
\]

is equivalent to an initialized word

\[
 a_{-(2m-2)},\ldots,a_0,a_1,\ldots,a_{\ell-1}
\quad\text{over }U
\tag{2.2}
\]

such that:

1. the initial \(2m-1\) symbols are all distinct;
2. for every \(t\ge1\),
   \[
     a_t\notin\{a_{t-1},\ldots,a_{t-m}\};
     \tag{2.3}
   \]
3. \(\sigma_t\) lists the elements of \(U\) in decreasing order of their
   most recent occurrence at time \(t\).

In particular, every \(m+1\) consecutive symbols in (2.2) are distinct,
and

\[
 \boxed{
 X(\sigma_t)=\{a_t,a_{t-1},\ldots,a_{t-m+1}\}.}
\tag{2.4}
\]

For every \(k\le m\),

\[
 \boxed{
 P_k(\sigma_t)=\{a_t,a_{t-1},\ldots,a_{t-k+1}\}.}
\tag{2.5}
\]

For \(k>m\), \(P_k(\sigma_t)\) is the set of the \(k\) most recently
occurring distinct symbols.

#### Proof

Initialize the negative-time history by reading \(\sigma_0\) backwards.
Appending \(a_t\) and moving it to the front of the recency list is exactly
the move-to-front update.  It is a distinct-owner promotion precisely when
\(a_t\) lies outside the first \(m\) recency positions, which is (2.3).
Induction gives item 3.  Condition (2.3) makes the last \(m\) actual symbols
distinct, so they are exactly the first \(m\) recency entries.  This proves
(2.4)--(2.5).

Conversely, start from the recency order supplied by the initial history.
Condition (2.3) places every new letter outside the current middle prefix,
so each update is a promotion of the form (1.7). \(\square\)

Thus the middle-owner problem is a simple-string window problem, but with a
different alphabet \(U_r\) allowed on different paths.

## 3. Exact top-fibre Ucycle gate

Call a family of initialized words from Theorem 2.1 an
\(H_{\max}\)-system if:

1. every word omits one fixed coordinate \(r\), its top-fibre label;
2. its length-\(m\) windows in (2.4), over all words, contain every member
   of \(\binom{[2m]}m\) exactly once; and
3. for every nonempty proper \(S\subset[2m]\), one selected recency state
   has \(P_{|S|}=S\).

Let \(p\) be the number of words.

### Theorem 3.1 (equivalence with the maximal-chain formulation)

There is a choice of one maximal-chain extension for every middle owner
which satisfies conditions (i)--(ii) in the problem statement if and only
if there is an \(H_{\max}\)-system with

\[
 p=o(W/m).
\tag{3.1}
\]

#### Proof

Group the selected maximal-chain states by their promotion-path components.
Promotion preserves the top fibre, and Theorem 2.1 supplies the initialized
word of every component.  Exact use of every middle owner is item 2 in the
definition, while coverage of every proper mask is item 3.

Conversely, turn every word state into its fibre permutation by Theorem
2.1.  Its prefixes are one maximal chain through the middle window (2.4).
Items 2--3 give the required owner partition and mask coverage, and the
words themselves are the promotion paths. \(\square\)

### Theorem 3.2 (literal compiler)

An \(H_{\max}\)-system with \(p\) paths gives one contiguous-OR word of
length

\[
 \boxed{W+O(mp+m^2).}
\tag{3.2}
\]

Consequently (3.1) implies length \(W+o(W)\).

#### Proof

Inside a path, every update is bridge one.  Initializing a full useful
prefix or moving between two path components costs at most \(2H+O(1)=O(m)\)
entries.  This contributes \(O(mp)\).  Group the paths by their \(2m\)
top fibres; the additional complete fibre resets cost \(O(m)\) per fibre,
hence \(O(m^2)\).  Every proper mask is a prefix of one selected state, so
no literal repair entries are needed. \(\square\)

## 4. There is no fractional capacity obstruction

Let \(\mathscr S\) be the set of all pairs \((r,\sigma)\), where
\(r\in[2m]\) and \(\sigma\) is a permutation of \(U_r\).  Give every state
the weight

\[
 x=\frac1{m\cdot m!\,(m-1)!}.
\tag{4.1}
\]

### Proposition 4.1 (uniform owner and prefix marginals)

Every middle owner has total state weight exactly one.  Every rank-\(k\)
mask has total prefix weight

\[
 \boxed{
 \frac{W}{\binom{2m}{k}}\ge1.}
\tag{4.2}
\]

#### Proof

The owner assertion is (1.6).  Coordinate permutations act transitively on
rank-\(k\) masks and preserve the state weights.  Every unit of total owner
weight supplies one rank-\(k\) prefix, so the total prefix weight at that
rank is \(W\).  Division by \(\binom{2m}{k}\) proves (4.2). \(\square\)

For every directed promotion arc \(\sigma\to\sigma'\) inside one fibre,
give the arc weight

\[
 y=\frac{x}{m-1}.
\tag{4.3}
\]

### Proposition 4.2 (exact fractional promotion circulation)

At every admissible state, the total incoming arc weight and total outgoing
arc weight both equal its state weight \(x\).  Together with Proposition
4.1 this is an exact fractional owner-transversal cycle cover with uniform
prefix coverage.

#### Proof

The promotion digraph has indegree and outdegree \(m-1\).  Equation (4.3)
gives both sums equal to \(x\). \(\square\)

Thus neither owners, masks, fibre capacities, nor promotion degrees give a
fractional obstruction.  The missing step is integral and correlated:
choose one state from each owner fibre, retain almost all of its fractional
circulation, and avoid prefix holes at every rank.

## 5. Exact local promotion cycles from the odd wreath factor

Fix one top fibre \(U\), \(|U|=2m-1\).  The exact odd-wreath factor on
\((m-1)\)-subsets of \(U\) partitions that layer into cycles of length
\(2m-1\).  Complement inside \(U\) to obtain a factor of
\(\binom Um\).

### Proposition 5.1 (a wreath cycle is a promotion cycle)

Let

\[
 \pi=(u_0,u_1,\ldots,u_{2m-2})
\tag{5.1}
\]

be the cyclic order underlying one wreath.  Put

\[
 X_j=\{u_j,u_{j+1},\ldots,u_{j+m-1}\}
\tag{5.2}
\]

with cyclic indices, and define the fibre permutation

\[
 \sigma_j=
 (u_{j+m-1},u_{j+m-2},\ldots,u_{j-m+1}).
\tag{5.3}
\]

Then \(X(\sigma_j)=X_j\) and

\[
 \boxed{
 \sigma_{j+1}
 =\operatorname{mtf}_{u_{j+m}}(\sigma_j).}
\tag{5.4}
\]

The promoted letter is the last letter of \(\sigma_j\), so every arrow is
a distinct-owner promotion.

#### Proof

The first \(m\) terms of (5.3) are the reverse listing of (5.2).  Since

\[
 j+m\equiv j-m+1\pmod{2m-1},
\tag{5.5}
\]

the new letter \(u_{j+m}\) is the last term of \(\sigma_j\).  Moving it to
the front gives exactly \(\sigma_{j+1}\). \(\square\)

### Corollary 5.2 (exact resolvable local factor)

For every top fibre \(U_r\), all \(m\)-subset owners contained in \(U_r\)
partition into promotion cycles of length \(2m-1\).

This is a genuine integral result and uses the free maximal-chain
extensions, not a canonical SCD word.

However, every global middle owner lies in exactly \(m\) top fibres.  The
union of the \(2m\) local factors is therefore an exact \(m\)-fold owner
multicover, not a onefold selection.

### Corollary 5.3 (whole-wreath fragmentation obstruction)

Any onefold owner partition made only from whole local wreath cycles has at
least

\[
 \boxed{\frac{W}{2m-1}=\Theta(W/m)}
\tag{5.6}
\]

promotion components.  It cannot satisfy (3.1).

#### Proof

Every chosen component contains exactly \(2m-1\) owners, and the chosen
components cover all \(W\) owners once. \(\square\)

Thus the exact odd-wreath theorem solves the local fibre geometry but not
the required asymptotic splicing.  A successful construction must create
promotion paths of average owner length \(\omega(m)\).

## 6. A sharp fixed-core obstruction

The freedom to choose maximal chains is real, but it cannot rescue
architectures which keep a positive coordinate permanently in the middle
prefix.

### Theorem 6.1 (fixed-present-coordinate lifetime)

Let

\[
 \sigma_0\to\sigma_1\to\cdots\to\sigma_{\ell-1}
\tag{6.1}
\]

be a promotion path.  If one coordinate \(c\) belongs to every middle owner
\(X(\sigma_t)\), then

\[
 \boxed{\ell\le m.}
\tag{6.2}
\]

Consequently any owner partition in which every promotion component has a
nonempty fixed included core has at least \(W/m\) components.

#### Proof

Because \(c\) never leaves the middle prefix, it is never eligible to be the
promoted letter.  Every promotion prepends another letter and shifts the
position of \(c\) one place to the right.  If its initial position is
\(i\le m\), it leaves the middle prefix after \(m-i+1\) transitions.
Therefore at most \(m-i\) transitions, hence at most \(m-i+1\le m\)
states, can retain \(c\).  Summing the component lengths proves the final
claim. \(\square\)

This rules out, at the required strict scale, smallest-missing-coordinate
partitions and other laminar schemes whose fibre classes retain a fixed
positive core.  It does not obstruct balanced owner-dependent fibre
assignments with empty intersection along long paths.

## 7. Why the canonical Gray/SCD failures do not decide this gate

The earlier cool-lex/Greene--Kleitman obstruction fixes both a canonical
SCD chain word and a prescribed combination Gray order.  It proves that
only \(\operatorname{Cat}_m\) of those prescribed transitions can be lifted
by move-to-front.

The present gate fixes neither object.  Every owner may choose:

* any one of its \(m\) missing-coordinate fibres;
* any of its \(m!\,(m-1)!\) permutations in that fibre; and
* any incoming and outgoing promotion compatible with the selected path.

At the owner level every Johnson edge \(X\to X-a+b\) can be realized by
some maximal-chain states: put \(a\) last in the source middle prefix, put
\(b\) in its suffix, and use move-to-front.  The constraint is global
queue consistency along a long path, not local existential adjacency.

Hence the canonical Gray/SCD no-gos do not imply a negative answer here.
Conversely, the exact local wreath cycles in Section 5 do not imply a
positive answer, because their components are too short and their
\(m\)-fold owner occurrences have not been rounded.

## 8. Exact surviving theorem

The \(H=m-1\) line is reduced to the following integral statement.

> **Transversal top-fibre Ucycle theorem.**  Select one admissible fibre
> permutation for every middle owner so that:
>
> 1. the selected states decompose into \(o(W/m)\) paths in the promotion
>    digraph;
> 2. for every \(1\le k\le2m-1\), their rank-\(k\) prefixes cover
>    \(\binom{[2m]}k\).

Equivalently, round the fractional promotion circulation of Proposition
4.2 to an owner-transversal path system with subcritical boundary and no
prefix holes.

The exact local factor in Corollary 5.2 supplies a resolvable \(m\)-fold
integral point.  What is missing is a onefold transversal which splices a
\(1-o(1)\) fraction of those \(2m-1\)-cycles, or replaces them by genuinely
longer recency words.

No frame, rank, divisibility, degree, or fractional-capacity obstruction is
present.  The proved obstructions are instead:

* whole local wreath cycles give only the critical
  \(\Theta(W/m)\) component scale; and
* any fixed-present-core construction also has at least \(W/m\)
  components.

A proof must exploit owner-dependent fibre assignment and maximal-chain
freedom to produce recency trajectories of average length \(\omega(m)\).
No such integral splicing theorem, and no universal obstruction to it, is
proved here.
