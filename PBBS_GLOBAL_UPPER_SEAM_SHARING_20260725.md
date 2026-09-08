# Exact global sharing of the upper PBBS seam charts

Date: 2026-07-25

## 0. Result and limitation

The \(2H\)-owner upper halo in the dominance-staircase seam theorem can be
shared exactly across different cuts.  On one owner component, all upper
crossing targets are represented by a word with one transition-pair letter
for every transition in the union of the cut neighbourhoods, plus one core
letter per cut (and at most a linearization halo at a cyclic drawing seam).

This is a genuine cross-cut compiler.  It can save a factor comparable to
the number of cuts in one \(H\)-window.  It does not yet prove constant one:
under the best unconditional residence estimate those neighbourhoods may
cover a positive fraction, or all, of the \(W\)-scale owner edges.  The
result would then add \(\Theta(W)\) letters.  It also does not fuse the
lower Pareto staircases.

## 1. Transition-pair identity

Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}                       \tag{1.1}
\]

be a directed Johnson owner trajectory.  Put

\[
 E_i=\{r_i,a_i\}.                                  \tag{1.2}
\]

For a cut between \(X_{c-1}\) and \(X_c\), let

\[
 C_c=X_{c-1}\cap X_c.                              \tag{1.3}
\]

For \(s,t\ge1\), define the crossing upper target

\[
 U^{(c)}_{s,t}=\bigcup_{j=c-s}^{c+t-1}X_j.          \tag{1.4}
\]

### Lemma 1.1 (exact pair-core decomposition)

\[
 \boxed{
 U^{(c)}_{s,t}
 =C_c\cup\bigcup_{i=c-s}^{c+t-2}E_i.}              \tag{1.5}
\]

#### Proof

Every set on the right is contained in the left.  Indeed,
\(C_c\subseteq X_{c-1}\cup X_c\), and
\(E_i\subseteq X_i\cup X_{i+1}\).

Conversely take \(x\in X_j\) for some
\(c-s\le j\le c+t-1\).  If \(x\in C_c\), there is nothing to prove.
Suppose first that \(j\le c-1\).  Follow the owner trace forward from
\(X_j\) to the central edge.  If \(x\) is absent before \(X_{c-1}\), its
first departure is some \(r_i=x\) with \(j\le i\le c-2\).  If it remains
in \(X_{c-1}\) but is not in \(C_c\), then \(x=r_{c-1}\).  Thus in either
case \(x\) belongs to one of the displayed \(E_i\)'s.  The case
\(j\ge c\) is symmetric: either \(x=a_{c-1}\), or its first arrival after
the central edge is some \(a_i=x\) with \(c\le i\le j-1\).  This proves
(1.5), with arbitrary departures and reentries allowed. \(\square\)

## 2. The global upper word

Let \(\mathcal C\) be a set of selected cuts on a linear owner component.
For a target depth cutoff \(H\), define the transition neighbourhood

\[
 S_H(\mathcal C)
 =\bigcup_{c\in\mathcal C}
   \{c-H,c-H+1,\ldots,c+H-2\}.                     \tag{2.1}
\]

Split this set into maximal consecutive integer intervals.  For each such
interval, emit its transition-pair letters \(E_i\) in chronological order.
Immediately after \(E_{c-1}\), insert the core letter \(C_c\) whenever
\(c\in\mathcal C\) lies in this block.  Concatenate the blocks.

### Theorem 2.1 (shared upper seam compiler)

This word represents every \(U^{(c)}_{s,t}\) with

\[
 c\in\mathcal C,qquad s,t\ge1,qquad s+t-1\le H,  \tag{2.2}
\]

and has length

\[
 \boxed{|S_H(\mathcal C)|+|\mathcal C|.}            \tag{2.3}
\]

All letters are nonzero.

#### Proof

Fix \(c,s,t\).  The transition range
\([c-s,c+t-2]\) is contained in the one component of
\(S_H(\mathcal C)\) containing the full neighbourhood of \(c\).  Take
the word interval beginning at \(E_{c-s}\).  If \(t=1\), end just after
the inserted \(C_c\); otherwise end at \(E_{c+t-2}\).  It contains all
the transition pairs in (1.5) and the core \(C_c\).

It may also contain an inserted core \(C_d\) belonging to another cut.
Such an insertion occurs after \(E_{d-1}\), with both central owners
\(X_{d-1},X_d\) inside the owner window (1.4).  Hence
\(C_d\subseteq U^{(c)}_{s,t}\), so it does not change the OR.  Lemma 1.1
now gives the target exactly.

Each \(E_i\) has two distinct coordinates, and every \(C_c\) has rank
one below the owners, so all letters are nonzero.  Counting the pair and
core letters gives (2.3). \(\square\)

For a cyclic component, choose a drawing seam outside
\(S_H(\mathcal C)\) when possible.  If the neighbourhood union is the whole
cycle, linearize once and repeat at most the first \(2H\) pair/core
positions.  Thus the cyclic cost is at most

\[
 |S_H(\mathcal C)|+|\mathcal C|+2H.                \tag{2.4}
\]

## 3. Exact neighbourhood ledger

If the cyclic gaps between consecutive selected cuts are
\(g_1,\ldots,g_J\), then the number of transition indices within backward
distance \(H\) and forward distance \(H-1\) of a cut is at most

\[
 \boxed{
 |S_H(\mathcal C)|
 \le\sum_{j=1}^J\min(g_j,2H-1).}                   \tag{3.1}
\]

Equality holds unless the whole cycle is shorter than the displayed sum.
This follows by partitioning the cycle into the arcs ending at successive
cuts: in an arc of length \(g_j\), at most \(2H-1\) positions lie in the
union of the two adjacent cut neighbourhoods.

In particular,

\[
 |S_H(\mathcal C)|\le\min(\ell,(2H-1)J),           \tag{3.2}
\]

where \(\ell\) is the component length.  Dense clusters are therefore
shared automatically.

## 4. Why this does not yet give an \(o(W)\) excess

The unconditional quotient packing estimate chooses the mesoscopic scale

\[
 L\asymp\sqrt{m/\log m}                             \tag{4.1}
\]

and gives at most order \(B_m/L\) long-interval cuts on the quotient,
apart from a negligible low-height family.  The target depth is
\(H=A\sqrt m\), so \(H/L\asymp\sqrt{\log m}\).  Formula (3.2) can improve
the independent \(HJ\) ledger by this factor when the cut neighbourhoods
overlap, but its worst allowed value is still order \(B_m\) on the
quotient and hence order

\[
 (2m+1)B_m=W                                         \tag{4.2}
\]

after deck lifting.  That is a leading-order second word, not an
\(o(W)\) repair.

There is a matching endpoint reason.  At depth \(H\), the distinct global
owner intervals crossing the selected cuts are indexed by the union

\[
 \bigcup_{c\in\mathcal C}[c-H,c-1].                \tag{4.3}

If their correct upper targets are distinct, a literal word needs at least
the cardinality of (4.3), since one endpoint represents at most one target
of a fixed rank.  Thus neighbourhood sharing can recover the factor
\(H/L\), but no count-only argument forces the remaining \(B_m\)-scale
union to be \(o(B_m)\).

The next gain must therefore come from one of two sources:

1. reuse the transition-pair/core word as part of the principal
   \(W\)-letter word rather than appending it; or
2. prove PBBS-specific collisions or surviving alternative occurrences
   which make the genuinely missing fixed-rank target union \(o(W)\).

The same issue remains, more sharply, for merging the lower Pareto
staircases.  Identity

\[
 P^{(c)}_{s,t}=P^{(c+1)}_{s+1,t-1}                 \tag{4.4}
\]

is exact, but equality of letters does not by itself provide one global
linear ordering in which every local staircase witness remains contiguous.

