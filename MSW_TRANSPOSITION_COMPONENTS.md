# Transposition components of the MSW wreath factor

## 1. Outcome

Let

\[
        n=2m+1,
        \qquad b=\operatorname{Cat}_m,
\]

and let \(F_m\) be the exact wreath factor of Mütze--Standke--Wiechert,
indexed by the Dyck words of semilength \(m\).  For a coordinate
transposition \(\tau\), compare \(F_m\) with \(\tau F_m\).  Their
middle-set interaction multigraph has the wreaths of the two factors as its
two vertex classes and one edge for each middle set.  Every connected
component is an independently switchable exact trade.

The component structure has both a negative and a positive side.

* A generic transposition gives one giant component in all audited cases.
  In particular, every transposition involving the distinguished coordinate
  gives one component for \(2\le m\le10\).
* The adjacent old-coordinate transposition

  \[
                           \tau=(2\ 3)                 \tag{1.1}
  \]

  has, for every \(m\), at least

  \[
                           \operatorname{Cat}_{m-2}    \tag{1.2}
  \]

  pairwise independent components containing exactly two wreaths on each
  side.  This is a theorem, not an extrapolation.  Since

  \[
  \frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
    =\frac{m(m+1)}{4(2m-1)(2m-3)}
    \longrightarrow\frac1{16},                       \tag{1.3}
  \]

  the legal component cube has linear dimension in the number of MSW
  wreaths.

Moreover, each two-wreath component acts at rank \(m-1\) as one elementary
Petr--Turek square, and those square supports are disjoint between
components.  Thus the signed rank selectors do have explicit integral lifts;
the price is that each lift has additional effects at lower ranks.

## 2. MSW notation

Write a Dyck word with `1` for an up-step and `0` for a down-step.  If
\(x\) is a Dyck word, let

\[
                         \rho(x)
\]

be its MSW flip-position permutation.  The omitted-label word of the
corresponding odd-graph cycle is

\[
                         q(x)=(\rho(x),n).             \tag{2.1}
\]

For an omitted-label word \(q=(q_0,\ldots,q_{n-1})\), its middle masks are

\[
 M_i(q)=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-1}\},
 \qquad i\in\mathbb Z_n.                              \tag{2.2}
\]

In this note, \(\mathcal W_m(q)\) denotes the family of masks in (2.2).
This is the omitted-label representation of the usual contiguous-interval
wreath; multiplication of the cyclic positions by two converts one
representation into the other.

The MSW recursion is

\[
 \rho(1u0v)=
 \bigl(|u|+2,\ |u|+2-\rho(\operatorname{rev}u),\ 1,
                 \ |u|+2+\rho(v)\bigr),              \tag{2.3}
\]

where `rev` reverses and complements the word, and scalar operations on a
permutation act entrywise.

## 3. An explicit family of legal two-for-two trades

Let \(R\) be any Dyck word of semilength \(m-2\), and define

\[
                      x_R=1100R,
              \qquad  y_R=1010R.                     \tag{3.1}
\]

Both are Dyck words of semilength \(m\).  Since \(\rho(10)=(2,1)\), two
applications of (2.3) give

\[
 \begin{aligned}
 q(x_R)&=(4,2,3,1,\ 4+\rho(R),\ n),\\
 q(y_R)&=(2,1,4,3,\ 4+\rho(R),\ n).                  \tag{3.2}
 \end{aligned}
\]

Put

\[
 \begin{aligned}
 C_R&=(4,2,3,1,T_R),&D_R&=(2,1,4,3,T_R),\\
 C'_R&=(4,3,2,1,T_R),&D'_R&=(3,1,4,2,T_R),           \tag{3.3}
 \end{aligned}
\]

where \(T_R=(4+\rho(R),n)\).  Thus

\[
                         C'_R=\tau C_R,
             \qquad     D'_R=\tau D_R.               \tag{3.4}
\]

### Theorem 1 (Catalan family of integral selector lifts)

For every \(R\in\mathcal D_{m-2}\),

\[
 \mathcal W_m(C_R)\mathbin{\dot\cup}\mathcal W_m(D_R)
  =
 \mathcal W_m(C'_R)\mathbin{\dot\cup}\mathcal W_m(D'_R).              \tag{3.5}
\]

Consequently

\[
             z_R=e_{C'_R}+e_{D'_R}-e_{C_R}-e_{D_R}   \tag{3.6}
\]

is a support-feasible two-for-two trade.  As \(R\) varies, the negative
supports are disjoint subsets of \(F_m\), the positive supports are disjoint
subsets of \(\tau F_m\), and the trades are distinct connected components
of the interaction graph.  Hence they may all be switched independently.

#### Proof

The words \(C_R,D_R\) are two distinct blocks of the exact MSW factor, so
their middle wreaths are disjoint.  Their transposed copies are likewise
disjoint.  It remains to prove equality of the two unions.

Use positions \(0,1,2,3\) for the displayed four-entry prefix in (3.3).
For a fixed cut \(i\), the tail part of (2.2) is the same in all four words.
Except at cuts \(i=1,3\), the following elementary prefix table matches the
two old masks with the two new masks at the same cut:

\[
\begin{array}{c|c|c|c}
\text{selected prefix positions}&
  \{C_R,D_R\}&\{C'_R,D'_R\}&\text{matching}\;\\ \hline
\{1,3\}&\{\{1,2\},\{1,3\}\}&
          \{\{1,3\},\{1,2\}\}&\text{swapped}\\
\{0,3\}&\{\{1,4\},\{2,3\}\}&
          \{\{1,4\},\{2,3\}\}&\text{fixed}\\
\{0,2\}&\{\{3,4\},\{2,4\}\}&
          \{\{2,4\},\{3,4\}\}&\text{swapped}.
\end{array}                                                     \tag{3.7}
\]

The cuts \(i=1\) and \(i=3\) have the same selected tail positions,
namely \(4,6,\ldots,2m\).  Across these two cuts and the two old words, the
selected prefix singleton is respectively \(3,4,2,1\); across the two new
words it is \(2,4,3,1\).  Both multisets are therefore
\(\{\{1\},\{2\},\{3\},\{4\}\}\).  This proves (3.5).

The pairs belonging to different \(R\)'s are disjoint because all Dyck
words in (3.1) are different.  Equality (3.5) says that no interaction edge
leaves one pair.  It cannot split into singleton components: that would say
that a middle wreath is fixed by one coordinate transposition, whereas an
unoriented odd cyclic order has no transposition in its dihedral stabilizer
for \(m\ge2\).  Thus every pair is exactly one connected component.  QED.

This theorem supplies \(\operatorname{Cat}_{m-2}\) actual integral moves,
not merely signed tangent directions.

## 3a. The same selector occurs at every Dyck-component boundary

The preceding construction is not confined to the first four steps of the
Dyck word.  It is stable under an arbitrary complete Dyck prefix.

### Lemma 1a (MSW concatenation law)

If \(P,Q\) are Dyck words and \(P\) has semilength \(s\), then

\[
             \rho(PQ)=(\rho(P),\ 2s+\rho(Q)).          \tag{3.8}
\]

#### Proof

Induct on the number of primitive components of \(P\).  The empty case is
immediate.  Write the first component as \(1u0\) and the remaining Dyck
suffix as \(v\), so \(P=1u0v\).  Formula (2.3) gives the same initial block
for \(\rho(PQ)\) and \(\rho(P)\).  In the last block apply the induction
hypothesis to \(vQ\).  The total shift before the copy of \(\rho(Q)\) is

\[
        (|u|+2)+|v|=|P|=2s.
\]

This gives (3.8).  QED.

Fix \(0\le s\le m-2\), a Dyck prefix \(P\in\mathcal D_s\), and a Dyck
suffix \(R\in\mathcal D_{m-s-2}\).  Put

\[
          x_{P,R}=P1100R,\qquad y_{P,R}=P1010R,
\qquad     \tau_s=(2s+2\ \ 2s+3).                     \tag{3.9}
\]

### Theorem 1b (contextual Catalan selector cubes)

For every fixed \(s\), the interaction graph between \(F_m\) and
\(\tau_sF_m\) contains at least

\[
                \operatorname{Cat}_s
                \operatorname{Cat}_{m-s-2}             \tag{3.10}
\]

independent two-wreath components.  They are indexed by \((P,R)\), and the
negative side of the component consists of the two MSW blocks indexed by
\(x_{P,R},y_{P,R}\).

#### Proof

By (3.8), the omitted-label words of the two blocks have a common initial
word \(\rho(P)\), followed by the shifted four-letter patterns

\[
 (2s+4,2s+2,2s+3,2s+1),\qquad
 (2s+2,2s+1,2s+4,2s+3),                                \tag{3.11}
\]

and then a common tail.  Cyclically rotate each omitted-label word so that
the displayed four-letter pattern comes first.  The old common prefix
\(\rho(P)\) merely moves to the end of the common tail.  After subtracting
\(2s\) from the four displayed labels, the four old and transposed orders
are exactly the four orders in (3.3), with an otherwise arbitrary common
tail.  The cut table (3.7), including its two exceptional cuts, therefore
proves the same disjoint two-for-two equality.

For fixed \(s\), the factorization

\[
             P\;\{1100,1010\}\;R                    \tag{3.12}
\]

uniquely recovers \(P\), the choice of the two middle words, and \(R\).
Hence the negative supports for different \((P,R)\) are disjoint, and the
positive supports are disjoint because \(\tau_s\) is a bijection.  The
two-for-two equality seals each pair from the rest of the interaction graph;
the same dihedral-stabilizer argument as in Theorem 1 rules out a split into
singletons.  Thus all these pairs are independent components.  Counting the
choices of \(P,R\) gives (3.10).  QED.

The endpoint cases \(s=0\) and \(s=m-2\) each give
\(\operatorname{Cat}_{m-2}\) independent components.  Summed over all
possible boundaries, the number of *occurrences* of contextual selectors is

\[
 \sum_{s=0}^{m-2}\operatorname{Cat}_s
                  \operatorname{Cat}_{m-s-2}
   =\operatorname{Cat}_{m-1},                         \tag{3.13}
\]

although components belonging to different values of \(s\) need not have
disjoint factor supports and therefore cannot all be switched at once.
Equation (3.13) exposes a recursive Catalan hierarchy of legal local charts,
not one isolated cube.  A natural absorption strategy is to choose a
prefix-free family of Dyck-component boundaries and use the unused suffix
charts recursively.

## 4. Exact action on the first lower shadow

Interpret \(R\) as its set of up-step positions in \([2m-4]\).  Its final
step is down, so \(2m-4\notin R\).  Define

\[
 K_R=4+\Bigl([2m-4]\setminus\bigl(R\cup\{2m-4\}\bigr)\Bigr).          \tag{4.1}
\]

Then \(|K_R|=m-3\), and the map \(R\mapsto K_R\) is injective.

### Theorem 2 (disjoint elementary-square action)

At rank \(m-1\), the trade (3.6) has action

\[
\begin{aligned}
B_{m-1}z_R={}&
 e_{K_R\cup\{2,2m\}}
-e_{K_R\cup\{3,2m\}}\\
&-e_{K_R\cup\{2,2m+1\}}
+e_{K_R\cup\{3,2m+1\}}.                            \tag{4.2}
\end{aligned}
\]

The four-set supports in (4.2) are pairwise disjoint as \(R\) varies.  By
complementation, the same holds at the paired upper rank \(m+2\).

#### Proof

Use the alternating rank-\((m-1)\) intervals

\[
 I_i(q)=\{q_{i+1},q_{i+3},\ldots,q_{i+2m-3}\}.        \tag{4.3}
\]

Substituting the four prefixes in (3.3), all terms cancel except the four
choices of one endpoint from \(\{2,3\}\) and one endpoint from
\(\{2m,2m+1\}\).  The common interior is the shifted complement of the
initial Dyck mask with its forced final down-step deleted; this is exactly
\(K_R\) in (4.1).  The signs are obtained directly from (3.6), yielding
(4.2).

Every set in (4.2) uniquely reveals its choices from the two endpoint pairs
and then its core \(K_R\).  Since \(R\mapsto K_R\) is injective, supports
from two different \(R\)'s cannot meet.  QED.

Thus (3.6) is an **integral lift of an elementary rank-\((m-1)\) selector**.
It is not fully rank-local: it also changes ranks \(2,\ldots,m-2\).  Remote
enumeration through \(m=10\) gives support eight at each such rank and
support four at rank \(m-1\), always with coefficients in \(\{-1,0,1\}\).
For fixed depth \(q=m-r\), the maximum number of these size-two trades
touching one rank-\(r\) target is exactly \(\operatorname{Cat}_q\) in all
audited cases.  Proving the latter formula in general is the next useful
bounded-codegree lemma.

## 5. The exact Catalan component hierarchy

For \(\tau=(2\ 3)\), the complete data obey the striking formula

\[
 \boxed{
 \#\{\text{components of size }
        \operatorname{Cat}_j+\operatorname{Cat}_{j+1}\}
     =\operatorname{Cat}_{m-j-2}
 }
 \qquad(0\le j\le m-2).                              \tag{5.1}
\]

Theorem 1 proves the \(j=0\) part directly.  The boundary-connectivity
theorem in `MSW_BOUNDARY_CONNECTIVITY.md`, followed by the suffix-local
induction in `MSW_COMPONENT_HIERARCHY_REDUCTION.md`, proves the full formula
for every \(m\).  Its sizes add correctly because

\[
 \sum_{j=0}^{m-2}
 \operatorname{Cat}_{m-j-2}
   (\operatorname{Cat}_j+\operatorname{Cat}_{j+1})
 =\operatorname{Cat}_m.                              \tag{5.2}
\]

Equivalently, if \(C(z)=\sum_{r\ge0}\operatorname{Cat}_rz^r\), the component
size generating function is

\[
 \sum_{j\ge0}(\operatorname{Cat}_j+operatorname{Cat}_{j+1})z^j
 =C(z)+C(z)^2.                                       \tag{5.3}
\]

The exact component description is as follows.  Put

\[
 \mathcal A_j=
   \{\,1u0:u\in\mathcal D_{j+1}\,\}
   \;\dot\cup\;
   \{\,10\,1v0:v\in\mathcal D_j\,\}.                 \tag{5.4}
\]

For every \(R\in\mathcal D_{m-j-2}\), the component is exactly

\[
                         \{AR:A\in\mathcal A_j\}.     \tag{5.5}
\]

In words, \(A\) is either one primitive Dyck component of semilength
\(j+2\), or an initial `10` followed by one primitive component of
semilength \(j+1\); the remaining Dyck suffix \(R\) is fixed.  Formula
(5.4) gives the component size
\(|\mathcal A_j|=\operatorname{Cat}_{j+1}+\operatorname{Cat}_j\), and every
Dyck word has a unique such initial atom followed by a suffix.  Suffix
locality proves that each proper class is closed, while the MNW flippability
spanning tree proves boundary connectivity of the top class.  Theorem 1 is
exactly the case \(j=0\).

The observed component totals are:

\[
\begin{array}{c|rrrrrrrrr}
m&2&3&4&5&6&7&8&9&10\\ \hline
\operatorname{Cat}_m
 &2&5&14&42&132&429&1430&4862&16796\\
\#\text{ components for }(2\ 3)
 &1&2&4&9&23&65&197&626&2056\\
\#\text{ size-two components}
 &1&1&2&5&14&42&132&429&1430
\end{array}                                                       \tag{5.6}
\]

In contrast, among all coordinate transpositions the number producing one
connected component was

\[
 10/10,16/21,27/36,42/55,61/78,84/105,111/136,
 142/171,177/210                                      \tag{5.7}
\]

for \(m=2,\ldots,10\).  Thus the answer to the original dichotomy is:

> A generic transposition usually gives one giant component, but selected
> interior adjacent transpositions expose a positive-density family of
> constant-size legal components.

The analyzer is
[msw_transposition_components.cpp](./msw_transposition_components.cpp).
All enumeration was run remotely in the visible `tmux` session
`msw_components`; no enumeration was run on the Mac.  The program rebuilds
the MSW factor, asserts exact ownership of every middle mask, constructs the
interaction graph independently for each transposition, and computes every
component by disjoint-set union.

## 6. Exact expansion lemma still needed

Theorem 1 resolves the existence of many integral moves at the initial MSW
factor.  It does not yet prove that choosing those moves improves all
vertical shadows.  The appropriate successor is no longer a vague
``round the signed selectors'' statement.

For an exact factor \(F\), a transposition \(\pi\), an interaction component
\(K\), and a rank \(r\), put

\[
 \Delta_{K,r}
 =B_r\bigl({\mathbf 1}_{K\cap\pi F}
            -{\mathbf 1}_{K\cap F}\bigr).                         \tag{6.1}
\]

All components of one interaction graph switch independently.  A sufficient
global theorem is the following.

### Component-frame/absorption target

For every factor reachable from an MSW factor and every central-band defect
vector, find a coordinate transposition \(\pi\) with a linear number of
\(O(1)\)- or \(O(m)\)-size components such that:

1. **Frame expansion.**  On the zero-point-marginal discrepancy spaces,

   \[
   \sum_K\left(\sum_{q\le h}
      \langle f_{m-q},\Delta_{K,m-q}\rangle\right)^2
    \ge \lambda_m\sum_{q\le h}\|f_{m-q}\|_2^2,       \tag{6.2}
   \]

   for an explicit \(\lambda_m\) large enough for iterative correction.

2. **Bounded target load.**  For every fixed depth \(q\), each rank
   \(m-q\) target lies in the support of only \(O_q(1)\) component vectors.
   The size-two MSW family suggests the sharp value
   \(\operatorname{Cat}_q\).

3. **Absorption/stability.**  After switching a conflict-free subfamily,
   either the same expansion remains available in the new factor or the
   unused components contain an absorber for the newly introduced lower-rank
   defects.

Theorem 2 proves an especially strong boundary case of this target: at depth
one, the \(\operatorname{Cat}_{m-2}\) square supports are completely
disjoint.  The unresolved issue is simultaneous control of their correlated
effects at deeper ranks and persistence after switching.

This is now the precise bridge between Petr--Turek's real rank selectors and
integral exact factors.  Constant-size legal lifts exist in positive density;
what remains is a multirank expansion/absorption theorem, not the discovery
of a first integral circuit.
