# Alternating turn representatives: exact Hall criterion and the first counterexample

Date: 2026-07-31  
Status: exact representative-selection criterion; exact local obstruction;
explicit smallest audited counterexample to “two turn surjections imply an
alternating decoration”

## 1. Setup

Fix a Hamilton cycle of the middle-levels graph on
\(\Omega=[2m-1]\), written

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1},                 \tag{1.1}
\]

where \(|A_i|=m-1\), \(|B_i|=m\), and

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2}.
\]

Its lower and upper turn words are

\[
 \ell_i=A_i\cap A_{i+1}\in\binom\Omega{m-2},
 \qquad
 u_i=B_{i-1}\cup B_i\in\binom\Omega{m+1}.             \tag{1.2}
\]

Assume both words are surjective.  We ask whether one can choose one
occurrence of every upper colour and one occurrence of every lower colour
so that the chosen \(A\)- and \(B\)-positions alternate around (1.1).

## 2. The exact gap--Hall criterion

Choose an upper transversal

\[
 I\subseteq\mathbb Z_Q,\qquad
 i\longmapsto u_i: I\overset\sim\longrightarrow
 \binom\Omega{m+1}.                                   \tag{2.1}
\]

Write its indices cyclically as \(i_0,\ldots,i_{P-1}\).  The gap after
the marked position \(A_{i_t}\) and before \(A_{i_{t+1}}\) contains the
following \(B\)-positions:

\[
 G_t=[i_t,i_{t+1})_{\mathbb Z_Q}
     =\{i_t,i_t+1,\ldots,i_{t+1}-1\}.                 \tag{2.2}
\]

Define the bipartite gap--colour graph \(\Gamma_I\).  Its left vertices
are the \(P\) gaps \(G_t\), its right vertices are the \(P\) lower
colours, and

\[
 G_t\sim L
 \quad\Longleftrightarrow\quad
 \ell_j=L\text{ for some }j\in G_t.                  \tag{2.3}
\]

### Theorem 2.1 (fixed-transversal criterion)

The upper transversal \(I\) extends to alternating bijective turn
representatives if and only if \(\Gamma_I\) has a perfect matching.
Equivalently, for every family \({\cal S}\) of \(I\)-gaps,

\[
 \left|\{\ell_j:j\in\bigcup_{G\in{\cal S}}G\}\right|
 \ \ge\ |{\cal S}|.                                  \tag{2.4}
\]

#### Proof

Between two consecutive selected \(A\)-positions an alternating mark word
contains exactly one selected \(B\)-position.  Its lower colour must be
different in the \(P\) gaps because the lower representatives are
bijective.  Thus an alternating lower selection gives a perfect matching
of \(\Gamma_I\).

Conversely, match every gap to a lower colour and choose any occurrence
of that colour inside the gap.  There is then exactly one selected
\(B\)-position between consecutive selected \(A\)-positions.  The marks
alternate, and all lower colours occur once.  Formula (2.4) is Hall's
theorem. \(\square\)

Consequently the full representative gate is the exact min--max condition

\[
 \boxed{\quad
 \exists\text{ upper transversal }I\text{ satisfying (2.4).}
 \quad}                                                \tag{2.5}
\]

There is also a useful prefix form.  After cutting immediately before a
selected \(A\)-position, alternation is equivalent to

\[
 0\le |I\cap[0,t]|-|J\cap[0,t]|\le1
 \quad\text{for every prefix }[0,t],                  \tag{2.6}
\]

with equality at the end.  Thus (2.5) is a coloured cyclic discrepancy-
one transversal problem, not a consequence of the two separate SDRs.

### Corollary 2.2 (a local spread hypothesis that makes interlacing automatic)

Let \(d_G\) and \(d_L\) denote degrees in \(\Gamma_I\).  If

\[
             \min_G d_G\ \ge\ \max_L d_L,            \tag{2.7}
\]

then \(I\) extends to an alternating decoration.  In particular this
holds when \(\Gamma_I\) is regular.

Indeed, for a family \({\cal S}\) of gaps,

\[
 (\min d_G)|{\cal S}|
 \le e({\cal S},N({\cal S}))
 \le (\max d_L)|N({\cal S})|,
\]

which proves (2.4).  This is one natural quantitative hypothesis under
which two-sided turn coverage really does interlace.

### Corollary 2.3 (circular-arc reduction)

For a lower colour \(L\), put

\[
 N_I(L)=\{t:\ell_j=L\text{ for some }j\in G_t\}.      \tag{2.8}
\]

Suppose every \(N_I(L)\) is a circular interval in the cyclic order of
the gaps.  Then (2.4) is equivalent to the interval inequalities

\[
 \#\{L:N_I(L)\subseteq H\}\le |H|                   \tag{2.9}
\]

for every circular interval \(H\) of gaps.

To prove this, apply Hall on the colour side.  If a deficient colour
family exists, the union of its allowed circular arcs splits into
disjoint interval components.  Every member arc lies in one component,
so one component is itself deficient and violates (2.9).  The converse
is immediate.  Thus gap-convex turn words have a genuinely one-dimensional
interval certificate.

## 3. A local obstruction

Call an upper occurrence \(i\) forced when \(u_i\) occurs nowhere else
in the upper turn word.

### Lemma 3.1 (forced-block obstruction)

If \(i,i+1,\ldots,i+s\) are forced upper occurrences, then any alternating
decoration must select all intervening lower positions

\[
                     i,i+1,\ldots,i+s-1,              \tag{3.1}
\]

and their lower colours must be pairwise distinct.  In particular, three
consecutive forced upper occurrences with
\(\ell_i=\ell_{i+1}\) forbid an alternating decoration.

#### Proof

All forced \(A\)-positions must be selected.  Between two consecutive
selected \(A\)-positions there is only one \(B\)-position, so it too must
be selected.  Bijectivity forbids selecting the same lower colour twice.
\(\square\)

This obstruction is invisible to separate surjectivity of \((u_i)\) and
\((\ell_i)\).

## 4. The explicit \(m=4\) counterexample

Take \(\Omega=[7]\), encoded by bitmasks on bits \(0,\ldots,6\).  The
following cyclic list is a Hamilton cycle of \({\rm ML}(7)\); it alternates
rank three and rank four:

```text
7 23 19 51 49 57 56 60 52 53 21 29 13 15 11 43 35 99
97 113 112 120 104 108 44 45 41 105 73 75 67 71 69 77
76 92 28 30 14 46 42 106 98 114 50 58 26 27 25 89 88 90
74 78 70 102 38 54 22 86 82 83 81 85 84 116 100 101 37 39
```

Starting at the first rank-three vertex, its two turn words are

```text
ell:
3 17 48 48 20 5 9 3 33 96 96 40 40 9 65 65 68 12 12 10 34
34 18 24 24 72 66 6 6 18 80 80 68 36 5

upper:
55 55 59 61 61 61 31 47 107 115 121 124 109 109 107 79 79 93
94 62 110 122 122 59 91 91 94 110 118 118 87 87 117 117 103
```

Both are surjective: the lower word contains all \(21\) rank-two sets,
with multiplicities \(1^7 2^{14}\), and the upper word contains all
\(21\) rank-five sets, with multiplicities \(1^8 2^{12}3^1\).

But upper colours

\[
 u_9=115,\qquad u_{10}=121,\qquad u_{11}=124          \tag{4.1}
\]

are each globally unique.  Hence positions \(A_9,A_{10},A_{11}\) are
forced.  Alternation forces both intervening positions \(B_9,B_{10}\),
where

\[
                  \ell_9=\ell_{10}=96.               \tag{4.2}
\]

This would use the same lower colour twice, contradicting bijectivity.
Lemma 3.1 proves that no alternating representatives exist.

Therefore

\[
 \boxed{\text{two-sided turn surjectivity does not imply a Catalan
 decoration.}}                                        \tag{4.3}
\]

The obstruction occurs before the linear-forest topology test.  The
binary trace criterion from the companion middle-levels note remains a
secondary, exactly characterized face after (2.5) has been passed.

## 5. Minimality and audit scope

For \(m=2\), each turn alphabet has one colour and the representative
selection is immediate.  The audit exhausts all Hamilton cycles of
\({\rm ML}(5)\), fixing one vertex and quotienting only reversal.  There
are exactly \(24\); all \(24\) have both turn maps surjective and all
\(24\) admit alternating representatives.  Thus the displayed \(m=4\)
cycle is the smallest counterexample, with finite exhaustive minimality
at \(m=3\).

Run

```text
python3 scratch/audit_catalan_alternating_turn_sdr_hall_20260731.py
```

The script independently checks the Hamilton cycle, both turn maps, the
three-forced-turn contradiction, all \(12,288\) upper SDRs via the gap
Hall graph, and the complete \(m=3\) Hamilton-cycle census.  The theorem
does not assert existence of a suitable cycle for general \(m\).

