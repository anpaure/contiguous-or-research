# Tight one-to-two augmenters: fixed-residual lift and singleton cuts

Date: 2026-08-01  
Lane: Thread D / off-support torsion escape  
Status: exact role-retaining fixed-residual lift criterion, exact
simultaneous rank in that state-preserving model, and two smallest singleton
cuts.  One cuts the selected-switch projection even with unrestricted
residual rematching; the sharper switch-rich cut applies only when the
residual matching is fixed.  No obstruction to prospective completion by
other columns or compound alternating reachability is claimed.

## 0. Outcome

The owner-slot augmenter of
`MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md`
has an especially simple **role-retaining, fixed-residual** lift to the
prospective oriented-diamond system.  Besides a selected auxiliary switch,
it needs exactly

1. one prescribed edge of the residual predecessor matching; and
2. one unused head.

Consequently simultaneous direct augmentations form an exact four-partite
matching problem on

\[
  (\hbox{missing colour},\ \hbox{selected switch},\
    \hbox{residual predecessor edge},\ \hbox{unused head}).       \tag{0.1}
\]

The complete polynomial local supply does **not** imply statewise all-cut
expansion.  At the literal smallest parameter `m=3`, one prospective linear
forest has no selected compatible switch for its missing colour.  A second,
sharper state has all four possible selected switches and all four required
new heads free, but none of the eight required fixed residual predecessor
edges.  The latter failure occurs before the graphic constraint but is
escaped if the residual predecessor matching may be globally rematched.

The new augmenter therefore is a valid primitive for off-support torsion
escape, but an upstream reroute must align the residual predecessor matching
if the lift is required to retain all unaffected predecessor assignments.
Raw menu size and the number of Catalan residual slots do not do this.

## 1. Prospective states

Let `Omega` have size `2m-1`.  A selected oriented diamond is

\[
                 d=(R;L,T,V),                         \tag{1.1}
\]

where

\[
 |R|=m+1,\quad |L|=m-1,\quad |T|=|V|=m,
 \qquad T\cap V=L,\quad T\cup V=R.                   \tag{1.2}
\]

In a prospective state `(X,Y)`, the values in each of the four roles of
`X` are injective and `Y` is a perfect incidence matching between the lower
and tail values unused by `X`.  Let

\[
             H_0=\binom{\Omega}{m}\setminus V(X)       \tag{1.3}
\]

be the unused-head bank.  Cross-role coincidences are allowed, as they must
be: a set used as a tail may simultaneously lie in `H_0`.

## 2. Exact oriented lift of one tight augmenter

Fix a missing upper colour `R`.  Suppose `X` contains the oriented auxiliary
diamond

\[
 f=(S;L,A,C),                                         \tag{2.1}
\]

and that there are pairwise distinct labels

\[
 a,b\in R,\qquad c\notin R,
\]

such that

\[
\begin{aligned}
 L&=R-\{a,b\},& A&=L+a,& C&=L+c,\\
 S&=L+\{a,c\}.                                      \tag{2.2}
\end{aligned}
\]

For `x in L`, put

\[
 L_x=(L-x)+c,\qquad B=L+b,\qquad D_x=(L-x)+\{a,c\}. \tag{2.3}
\]

### Theorem 2.1 (role-retaining fixed-residual lift criterion)

The tight replacement

\[
\begin{aligned}
 f&=(S;L,A,C)\\
 &\longmapsto
 e=(R;L,A,B),\qquad g=(S;L_x,D_x,C)                 \tag{2.4}
\end{aligned}
\]

is an exact prospective augmentation with

1. the old tail `A` and old head `C` retained in their roles; and
2. every surviving edge of `Y` left unchanged,

if and only if

\[
                    (L_x,D_x)\in Y,qquad B\in H_0.  \tag{2.5}
\]

When (2.5) holds, the new state is

\[
 X'=X-f+e+g,qquad Y'=Y-(L_x,D_x).                   \tag{2.6}
\]

It retains every old predecessor/head resource of `f`, consumes exactly one
residual predecessor edge and one unused head, and leaves every other row
unchanged.  If the rooted arcs of `X` form a linear forest, the additional
graphic condition is exactly that

\[
       X-f+\{A\mathbin{\to}B,D_x\mathbin{\to}C\}      \tag{2.7}
\]

is a linear forest.

#### Proof

The Boolean identities in (2.2)--(2.3) give

\[
 L\subset A,B\subset R,qquad
 L_x\subset D_x,C\subset S.                         \tag{2.8}
\]

The new target edge retains the lower-tail pair `(L,A)` of `f`; the rerouted
auxiliary edge retains its head `C`.  Its only new lower-tail pair is
`(L_x,D_x)`, so exact completion of the predecessor matching is equivalent
to this pair belonging to `Y`.  Its only new head is `B`, so head injectivity
is equivalent to `B in H_0`.  Removing this one edge from `Y` proves every
partition equality in (2.6).  Under the two stated preservation conditions,
the new lower and new tail must be removed as one old residual edge, proving
necessity.  Equation (2.7) is the literal graphic-independence test.
\(\square\)

Thus the three new owner-slot resources in the un-oriented theorem do not
become three arbitrary free objects in this state-preserving orientation:
one lower and one tail are rigidly coupled as a prescribed residual edge.

### Remark 2.2 (scope)

If arbitrary rematching of the residual lower-tail incidence graph is
allowed, `(L_x,D_x) in Y` is not necessary.  It is then enough that the new
unused lower and tail shores admit some perfect incidence matching.  This is
a different, global operation, and Section 4 gives an explicit escape of
exactly that kind.

## 3. Exact fixed-residual direct-augmenter rank

For a missing-colour set `D`, let `A_D(X,Y)` be the set of triples

\[
                  \alpha=(R,f,x)                     \tag{3.1}
\]

for which `R in D`, `f in X` has (2.1)--(2.2), and (2.5) holds.  Give
`alpha` the four resource labels

\[
       R(\alpha)=R,\quad F(\alpha)=f,\quad
       P(\alpha)=(L_x,D_x),\quad H(\alpha)=B.         \tag{3.2}
\]

Let `nu_aug(D;X,Y)` be the maximum size of a subset of `A_D(X,Y)` injective
in all four labels.  If topology is required, additionally impose graphic
independence of all replacements after deleting their distinct switch arcs.

### Theorem 3.1 (simultaneous fixed-residual augmentation)

Exactly `nu_aug(D;X,Y)` colours of `D` can be filled simultaneously by the
role-retaining tight replacements while every surviving residual edge is
fixed.  In particular,
all of `D` can be filled directly if and only if

\[
                       \nu_{\rm aug}(D;X,Y)=|D|.       \tag{3.3}
\]

#### Proof

Distinct switch labels ensure that no old selected edge is replaced twice.
Distinct predecessor labels give distinct new lower and tail resources,
because `Y` is a matching.  Distinct head labels give distinct new heads;
all are disjoint from the old head set by (2.5).  The old resources retained
from distinct switches were already disjoint in their respective roles.
Hence Theorem 2.1 applies simultaneously.  Conversely every simultaneous
tight replacement records precisely the four injectivities (3.2).
\(\square\)

For every `A subset D`, the familiar projection cuts

\[
\begin{aligned}
 |N_F(A)|&\ge |A|,& |N_P(A)|&\ge |A|,& |N_H(A)|&\ge |A|             \tag{3.4}
\end{aligned}
\]

are necessary.  More generally, if sets of switch, predecessor, and head
vertices jointly meet every candidate through `A`, their total cardinality
is an upper bound on the direct rank through `A`.  These are only necessary
hypergraph-cover cuts: (3.1)--(3.2) is a four-partite matching, not an
ordinary bipartite Hall system.  The exact all-cut assertion is its matching
rank, not any one projection of it.

### Proposition 3.2 (exact one-colour incidence census)

Fix `R` and ignore the current-state filters `f in X`, `(L_x,D_x) in Y`,
and `B in H_0`.  In the complete oriented structural bank there are

\[
\begin{array}{c|c|c}
\text{resource shore}&\text{number of vertices through }R
                     &\text{candidate degree through }R\\ \hline
\text{switches }f &(m+1)m(m-2)&m-1\\
\text{predecessor pairs }(L_x,D_x)
  &\frac12(m+1)m(m-1)(m-2)&2\\
\text{heads }B&m+1&m(m-1)(m-2).
\end{array}                                                   \tag{3.5}
\]

The total number of structural candidates is therefore

\[
                  (m+1)m(m-1)(m-2).                    \tag{3.6}
\]

In an actual selected state, at most one switch is selected for each
auxiliary upper colour `S`.  Hence

\[
 |N_F(\{R\})\cap X|\le (m+1)(m-2),\qquad
 |\mathcal A_{\{R\}}(X,Y)|\le(m+1)(m-2)(m-1).         \tag{3.7}
\]

#### Proof

The ordered parameters `(a,b,c,x)` have respectively
`(m+1),m,(m-2),(m-1)` choices.  A switch forgets only `x`, giving the first
row.  A predecessor pair determines `c=L_x-R`, determines
`a=D_x-L_x`, and leaves the two labels `b,x` interchangeable, giving degree
two and the second row.  A head is `B=R-a`; after fixing `a`, the parameters
`b,c,x` remain free, giving the third row.  Finally
`S=R-b+c`, so there are only `(m+1)(m-2)` possible auxiliary colours in a
selected state, proving (3.7).  \(\square\)

This census also shows precisely why the `Theta(m^4)` abstract supply does
not itself give a fixed-state expansion estimate: selection of one
representative per auxiliary upper colour removes one factor of `m`, and
the residual matching can then delete the entire remaining neighbourhood,
as Section 4 does at the first parameter.

### Proposition 3.3 (exact scalar capacity ledger)

Write

\[
 W=\binom{2m-1}{m},\qquad
 U=\binom{2m-1}{m+1}=W-C,
 \qquad C=\operatorname {Cat}_m.                     \tag{3.8}
\]

If `X` omits `d` upper colours, then `|X|=U-d` and

\[
                         |Y|=|H_0|=C+d.              \tag{3.9}
\]

Filling all `d` colours by Theorem 2.1 consumes exactly `d` residual
predecessor edges and `d` unused heads, leaving exactly `C` of each.  Thus
the total capacities have the sharp required surplus; every failure of
(3.3) is a neighbourhood/correlation or graphic failure, not a scalar
shortage of lower-tail or head resources.

#### Proof

There are `W` lower, tail, and head values.  Each selected diamond consumes
one of each, so their unused shores have size
`W-(U-d)=C+d`.  Theorem 2.1 consumes one object from each shore per net new
selected diamond.  \(\square\)

## 4. The two smallest singleton cuts

### Proposition 4.1 (empty selected-switch projection)

At `m=3`, let `Omega=[5]`, omit `R=1234`, and select

\[
\begin{array}{c|c|c|c}
S&L&T&V\\ \hline
2345&25&235&245\\
1345&35&345&135\\
1245&45&245&145\\
1235&15&135&125.
\end{array}                                           \tag{4.A1}
\]

The four lower, tail, and head values are separately distinct.  The rooted
arcs form the two directed paths

\[
                  235\to245\to145,qquad
                  345\to135\to125.                   \tag{4.A2}
\]

The unused lower and tail shores have the residual perfect matching

\[
 12\to125,\quad13\to123,\quad14\to145,\quad
 23\to234,\quad24\to124,\quad34\to134.               \tag{4.A3}
\]

Nevertheless no row of (4.A1) is a compatible tight switch for `R`:
every selected lower contains `5`, whereas every tight switch lower is
`R-{a,b}` and hence is contained in `R`.  Therefore

\[
                         N_F(\{R\})=\varnothing.      \tag{4.A4}
\]

This is a direct singleton obstruction even if the residual matching may be
arbitrarily rematched.  It is an obstruction only to using the tight
one-to-two bank from this already selected state; it does not exclude an
off-support representative change or a prospective choice of a different
state.  It also does not contain the later tight-pivot bank, so no protected
all-parameter obstruction is inferred from it.

#### Proof

All displayed containments in (4.A1)--(4.A3) are literal.  Separate
injectivity and (4.A2) prove that this is a prospective graphic state.
Compatibility with (2.2) forces `L subset R`, contradicting every selected
lower in (4.A1).  \(\square\)

### Proposition 4.2 (all switches present, fixed residual row empty)

Take `m=3`, `Omega=[5]`, and omit

\[
                           R=1234.                    \tag{4.1}
\]

Use the selected diamonds

\[
\begin{array}{c|c|c|c}
S&L&A&C\\ \hline
2345&34&234&345\\
1345&14&134&145\\
1245&12&124&125\\
1235&23&123&235
\end{array}                                           \tag{4.2}
\]

and the residual predecessor matching

\[
 Y=\{13\to135,15\to125,24\to245,
       25\to235,35\to345,45\to145\}.                \tag{4.3}
\]

This is the exact state of Proposition 6.1 in
`MATH_THEOREM_THREAD_D_HALF_INTEGRAL_HYPERCIRCUIT_AND_RESIDUAL_SLOT_ABSORPTION_20260801.md`.

Every row of (4.2) is a compatible selected switch for `R`, and its new
head is unused.  Nevertheless the complete list of required residual pairs
is

\[
\begin{array}{c|c|c}
S&B&\text{required }(L_x,D_x)\\ \hline
2345&134&45\to245,\ 35\to235\\
1345&124&45\to345,\ 15\to135\\
1245&123&25\to245,\ 15\to145\\
1235&234&35\to135,\ 25\to125.
\end{array}                                           \tag{4.4}
\]

None of the eight pairs in (4.4) belongs to (4.3).  Therefore

\[
                  \mathcal A_{\{1234\}}(X,Y)=\varnothing,
       \qquad \nu_{\rm aug}(\{1234\};X,Y)=0.         \tag{4.5}
\]

The obstruction is entirely the correlation between the free lower and
tail banks.  It is not caused by switch supply, head supply, or topology.

For each of the eight structural rows in (4.4), the owner-slot theorem has
four choices for the two newly used slot labels once the selected switch
slots are fixed.  Thus all `32` corresponding labelled owner-slot
augmenters fail the role-retaining fixed-residual lift criterion.  The
parameter `m=3` is minimal because the augmenter count contains the factor
`m-2`.

This proves that the complete one-to-two bank does not imply even singleton
role-retaining fixed-residual expansion, and hence cannot by itself imply
that all-cut statement.

It is important that (4.5) not be promoted to an unrestricted prospective
obstruction.  For example, replace the first row of (4.2) by

\[
 (1234;34,234,134),\qquad (2345;35,235,345).          \tag{4.6}
\]

Together with the other three rows of (4.2), these five diamonds have a
residual perfect matching

\[
 13\to135,\quad15\to145,\quad24\to245,\quad
 25\to125,\quad45\to345.                             \tag{4.7}
\]

Thus the same structural tight replacement succeeds after a nonlocal
rematching of `Y`, even though its required fixed residual edge
`35->235` was absent from (4.3).  Equations (4.6)--(4.7) sharply separate
the refuted fixed-residual all-cut claim from the still-live unrestricted
prospective theorem.

## 5. What survives for off-support rounding

The obstruction (4.5) is not a no-go for compound service.  The same state
has the protected-safe two-colour chain already displayed in Proposition
6.1: one representative transposition changes the residual matching, after
which the missing colour is inserted.  Therefore the correct state graph
has both

1. protected predecessor/head transpositions; and
2. the tight one-to-two augmentations of Theorem 2.1.

If `Gamma_P(X,Y)` is this protected state graph, define

\[
 r^{\rm aug}_P(X,Y;D)=
 \min\{q:\text{a state at distance }q\text{ has }
                  \nu_{\rm aug}(D)=|D|\}.             \tag{5.1}
\]

The new local theorem gives high branching inside `Gamma_P`; it does not
bound (5.1).  A valid bounded-total off-support theorem must prove an
all-cut expansion or recursive routing statement in this correlated state
graph after contracting the fixed quotient bank and the tight-pivot bank.
Neither the `Theta(m^4)` number of abstract augmenters per colour nor the
scalar count of free Catalan slots proves it.  Allowing global residual
rematching enlarges this graph and escapes the singleton cut, but requires a
separate simultaneous-Hall argument for each visited lower/tail shore.

The exact positive target is consequently:

> construct the integral partial state prospectively so that every exported
> defect shore has four-partite augmenter rank equal to its size after only
> `O(1)` protected state transitions.

That statement is strictly stronger than residual capacity, but strictly
weaker than demanding that every defect be directly augmentable in the
initial state.
