# SCD flags: exact rail balance, statewise Hall, and the owner-rainbow chronology gate

**Date:** 2026-08-01  
**Status:** unconditional exact reduction and an explicit SCD counterexample.
The protected marked-chain selector is exact, but it does not automatically
admit even a directed cycle cover.  Legal chronology factors first through a
de Bruijn rail-balance equation, then independent statewise Hall systems,
then one owner-rainbow coupling.  No all-dimensional positive lift is
claimed.

## 0. Verdict

Put \(k=2m+1\), \(2\le d\le m\), and let an all-high depth-\(d\) flag at a rank-\(m\) root
be

\[
 f=(q;z_1,z_2,\ldots,z_{d-1}),
 \qquad B(f)=q-\{z_1,\ldots,z_{d-1}\}.                          \tag{0.1}
\]

The SCD selector theorem chooses such a flag at every root and marks every
high target exactly once.  Chronology imposes a new exact condition.

Define the rail prefix and suffix

\[
 \partial^-f=(z_1,\ldots,z_{d-2}),
 \qquad
 \partial^+f=(z_2,\ldots,z_{d-1}).                             \tag{0.2}
\]

Every literal successor turn sends a flag with rail suffix \(w\) to a flag
with rail prefix \(w\).  Hence a necessary condition is

\[
 \boxed{
 |\{f:\partial^-f=w\}|=|\{f:\partial^+f=w\}|
 \quad\hbox{for every ordered }(d-2)\hbox{-word }w.}           \tag{0.3}
\]

This is exactly zero boundary in the order-\((d-2)\) de Bruijn rail graph.
It is not implied by exact target coverage.

Even (0.3) is not sufficient.  Inside every rail state one must solve a
literal root-exchange matching; the selected edges over all states must then
use every rank-\((m+1)\) owner exactly once.  Connectedness and quotient
voltage come only after those three rows close.

The standard recursive SCD with its natural continuation already fails at
the first row.  At \((k,m,d)=(7,3,3)\), its exact target table has nonzero
rail divergence and 15 zero-out roots.  One explicit dead root is given in
Section 4.

## 1. Literal shift law

Let

\[
 f=(p;z_1,\ldots,z_{d-1})quad\hbox{and}\quad
 g=(q;y_1,\ldots,y_{d-1}).                                    \tag{1.1}
\]

### Lemma 1.1 (all-high legal turn)

A literal turn from \(f\) to \(g\) exists exactly when there are
\(\beta\notin p\) and \(\gamma\in B(f)\) such that

\[
 q=p-\{z_1\}+\{\beta\},                                      \tag{1.2}
\]

and

\[
                (y_1,\ldots,y_{d-1})
                =(z_2,\ldots,z_{d-1},\gamma).                  \tag{1.3}
\]

The owner of this turn is

\[
                              o=p\cup\{\beta\}.                \tag{1.4}
\]

#### Proof

In age notation, \(o-q\) must lie in the oldest singleton class of \(f\),
so the leaving coordinate is \(z_1\), giving (1.2).  Every surviving
singleton age class shifts upward by one, forcing
\(y_i=z_{i+1}\) for \(i<d-1\).  The new last singleton is drawn from the
old age-zero block \(B(f)\), giving \(y_{d-1}=\gamma\).  Conversely these
relations satisfy every age-transition containment with equality. \(\square\)

Equation (1.3) proves the boundary condition (0.3).

## 2. Exact statewise factorization

Fix one flag table \({\cal F}\), one flag at every rank-\(m\) root.  For an
ordered \((d-2)\)-word \(w\), put

\[
 L_w=\{f\in{\cal F}:\partial^+f=w\},
 \qquad
 R_w=\{g\in{\cal F}:\partial^-g=w\}.                           \tag{2.1}
\]

Make a bipartite graph \(G_w=(L_w,R_w;E_w)\).  Join \(f\in L_w\) to
\(g\in R_w\) exactly when (1.2)--(1.3) hold.  Colour the edge by its owner
(1.4).

### Theorem 2.1 (rail-state chronology theorem)

The fixed flag table admits a literal directed cycle cover of its roots if
and only if every \(G_w\) has a perfect matching.

It admits an owner-exact literal directed cycle cover if and only if one can
choose a perfect matching in every \(G_w\) so that the union contains every
rank-\((m+1)\) owner colour exactly once.

#### Proof

Every legal transition belongs to exactly one state \(w\), by (1.3).
A directed cycle cover uses every flag once as a tail and once as a head, so
its transitions restrict to a perfect matching between \(L_w\) and \(R_w\)
for every state.

Conversely, the union of statewise perfect matchings gives every flag one
successor and one predecessor.  It is therefore a directed permutation of
the roots, and every edge is a legal literal turn.  Requiring each owner
colour once is exactly the extra owner statement. \(\square\)

### Corollary 2.2 (the three exact chronology rows)

For a fixed exact target table, the cycle-cover gate separates as:

1. **rail balance:** \(|L_w|=|R_w|\) for every \(w\);
2. **statewise Hall:** \(|N_{G_w}(X)|\ge|X|\) for every
   \(X\subseteq L_w\) and every \(w\);
3. **owner rainbow:** select the statewise perfect matchings with every owner
   colour exactly once.

The third row is a rainbow matching/three-index assignment problem and does
not follow from the first two.  A one-component chronology additionally
requires the usual subtour elimination or a subsequent safe splice.

In a cyclic quotient, voltage/holonomy is a fourth, later row.  Failure of
(0.3) occurs before voltage is defined.

## 3. Why target exactness does not imply rail balance

The marked-chain selector controls which nested **sets** occur.  Rail balance
controls ordered deletion **words**.  The arbitrary continuation below a
chain minimum is unmarked, so it can change (0.3) without changing any root
or named-target equation.

More explicitly, take an exact selector containing a root whose marked chain
stops before depth \(d-1\).  Two different legal completions of its deletion
word can have different prefix/suffix boundary vectors.  Replacing one by
the other preserves the complete marked selector.  If one table is balanced,
the replacement makes it unbalanced unless the two boundary vectors agree;
if the first table is unbalanced, the claim is already witnessed.

Thus there exist exact marked selectors which fail (0.3).  The next section
gives a fully explicit SCD instance which fails much more strongly.

## 4. Explicit dead root in the recursive SCD

Use the standard recursive SCD: from a chain

\[
 A_k\subset\cdots\subset A_\ell\subseteq B_{n-1},              \tag{4.1}
\]

form

\[
 A_k\subset\cdots\subset A_\ell
 \subset A_\ell\cup\{n-1\},                                  \tag{4.2}
\]

and, when \(k<\ell\),

\[
 A_k\cup\{n-1\}\subset\cdots\subset A_{\ell-1}\cup\{n-1\}.
                                                                    \tag{4.3}
\]

Continue a short downward segment by deleting the least available element
of its chain minimum.

At \(n=7,m=3,d=3\), consider

\[
 p=\{0,1,6\},qquad f_p=(p;1,0),qquad B(f_p)=\{6\}.            \tag{4.4}
\]

Its possible successor roots are

\[
 q_\beta=\{0,6,\beta\},qquad \beta\in\{2,3,4,5\}.             \tag{4.5}
\]

The recursive SCD flags at these roots are

\[
                         f_{q_\beta}=(q_\beta;0,\beta).         \tag{4.6}
\]

Rail overlap forces the first entry zero, which (4.6) satisfies, but the
last entry must belong to \(B(f_p)=\{6\}\).  Instead it is \(\beta\).
Therefore \(p\) has no legal successor.

This table is nevertheless an exact marked SCD selector by the SCD theorem.
Hence exact target coverage plus one flag per root does not imply even a
cycle cover, let alone owner exactness or connectedness.

## 5. Independent H100 audit

The C++ audit

`scratch/audit_scd_flag_turn_balance_20260801.cpp`

constructs the recursive SCD literally, derives its deletion flags, computes
the rail boundary, and replays every legal root transition.  Representative
results are:

\[
\begin{array}{c|c|c|c|c|c}
n&m&d&\|\partial{\cal F}\|_1&\text{zero-out roots}&\text{legal turns}\\ \hline
7&3&3&24&15&36\\
9&4&3&48&21&254\\
9&4&4&110&56&127\\
11&5&3&132&28&1369\\
11&5&4&340&84&909
\end{array}                                                     \tag{5.1}
\]

These are finite audits, not an asymptotic no-go.  They authenticate the
scope distinction exposed by Theorem 2.1.

## 6. Corrected remaining construction

The protected selector theorem permits arbitrary prescribed task flags by
quarantining their suffixes from the lower matching.  It does **not**
quarantine their roots from chronology: every root still needs one incoming
and one outgoing turn.  A prescribed dead flag is therefore fatal.

The shortest remaining all-high statement is:

> **Transition-compatible protected chain-factor theorem.**  Choose the
> adjacent-level chain matchings and the unmarked deletion continuations so
> that (i) every named high target occurs exactly once, (ii) the prescribed
> task flags are retained, (iii) every rail-state graph \(G_w\) has a
> perfect matching, and (iv) those matchings admit an owner-rainbow choice.

After this theorem, one still has to join the directed cycle cover and
preserve the upper/residence/compiler guards.  The stationary pull-clock
theorem proves the fractional analogue of rail balance, while the SCD and
protected-selector theorems prove the integral named-target marginal.  The
unproved operation is their **common integral rounding** inside the
statewise Hall and owner-rainbow fibre.

## 7. Equivalent serialized-chain formulation

The statewise formulation has a useful chronology-first equivalent.  Let

\[
 q_0,q_1,\ldots,q_{W-1},q_W=q_0                              \tag{7.1}
\]

be a cyclic ordering of all rank-\(m\) roots, with Johnson transitions

\[
 q_{i+1}=q_i-\{a_i\}+\{b_i\}.                                 \tag{7.2}
\]

### Theorem 7.1 (resident Johnson serialization)

Assume every positive coordinate run in the incidence word of (7.1) has
length at least \(d\).  Then

\[
                         f_i=(q_i;a_i,a_{i+1},\ldots,a_{i+d-2}) \tag{7.3}
\]

is a well-defined all-high flag, and \(f_i\to f_{i+1}\) is a legal literal
turn.  Moreover, for \(1\le j<d\),

\[
 q_i-\{a_i,\ldots,a_{i+j-1}\}
 =q_i\cap q_{i+1}\cap\cdots\cap q_{i+j}.                      \tag{7.4}
\]

Conversely, one connected legal all-high flag chronology has the form
(7.1)--(7.3), and its marked suffixes are selected occurrences from the
intersection decks (7.4).

#### Proof

If a future leaving coordinate \(a_{i+t}\), \(t<d\), were absent from
\(q_i\), it would have entered after time \(i\) and left within fewer than
\(d\) steps, contradicting the run floor.  The future leaving coordinates
are distinct for the same reason.  Thus (7.3) is a flag.  Its rail shifts by
one at the next step, and the newly appended leaving coordinate lies in the
old bottom block; Lemma 1.1 gives legality.  No removed coordinate can
re-enter inside the window, so repeated intersection gives (7.4).

Conversely, Lemma 1.1 identifies the first rail coordinate with the leaving
coordinate and shifts the rest.  Iterating around the connected chronology
gives (7.3), and deleting its first \(j\) entries gives (7.4). \(\square\)

### Corollary 7.2 (exact remaining carrier statement)

A connected transition-compatible exact marked-chain selector is equivalent
to a resident Johnson Hamilton cycle for which every high target occurs in
at least one intersection deck (7.4).  Exact target multiplicity is then
obtained by marking one chosen occurrence.

Owner exactness is exactly distinct coverage of the adjacent unions

\[
                              q_i\cup q_{i+1}.                  \tag{7.5}
\]

Thus the SCD theorem solves the static chain partition, but serializing it
recovers a precise decorated-carrier problem:

\[
 \boxed{
 \text{resident Johnson Hamilton cycle}
 +\text{ complete lower intersection decks}
 +\text{ rainbow adjacent unions}.}
\]

Arbitrary-width upper unions, opening, and the terminal compiler remain
outside this equivalence.  In a quotient construction, coprime voltage is
the additional lift condition.
