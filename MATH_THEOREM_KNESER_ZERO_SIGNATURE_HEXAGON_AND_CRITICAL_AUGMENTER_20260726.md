# Kneser critical rounding: an exact augmenter, a zero-signature hexagon, and the star-cut audit

Date: 2026-07-26

Method: pure mathematics.  This note attacks the two integral gates in
`MATH_THEOREM_KNESER_NEAR_CORE_CRITICAL_ROUNDING_AND_SWITCH_OBSTRUCTION_20260726.md`.

## 0. Verdict

The elementary Kneser rectangle is not the smallest useful local object.
There are two stronger configurations.

1.  A four-coordinate alternating path replaces one selected Kneser edge
    by two.  It covers two previously uncovered lower vertices and changes
    the complementary-owner load by exactly \(+1\) at each of two distinct
    owner pairs and by zero everywhere else.  Thus it is an exact
    **two-slack augmenter** for the clone hypergraph whenever those pairs
    each have a free clone.
2.  A six-coordinate alternating hexagon replaces three selected Kneser
    edges by three others and has **identically zero owner signature**.
    On the quotient owner graph it is the cyclic three-edge switch

    \[
       (a b),(c d),(e f)\longmapsto(a d),(c f),(e b).
    \]

    In particular, when the three old quotient edges lie on three distinct
    owner cycles, the switch merges those quotient cycles into one without
    changing any lower coverage or owner degree.

These are literal balanced multi-rectangle circulations, not fractional
directions.  They show that the exact (0/2) locus, although isolated under
single rectangles, is not rigid under longer alternating Kneser switches.

The four-coordinate move is the first member of an exact hierarchy.  For
**every** two distinct uncovered lower sets \(R,S\), with
\(t=|R\cap S|\), there is a \((2t+1)\)-edge alternating path which replaces
\(t\) old matching edges by \(t+1\) new ones and has owner signature
exactly \(\mathbf e_{[R+h]}+\mathbf e_{[S+h]}\) for a chosen
\(h\notin R\cup S\).  Thus all intersection scales admit exact
two-slack augmenters.  What is not automatic is eligibility: all \(t\)
prescribed old edges must already belong to the current matching and each
of \([R+h],[S+h]\) must have a free clone.

Finally, the natural (t)-star owner-capacity cuts do not give an odd-set
obstruction.  Their aggregate deficiency is exactly (-D), independently
of (t).  Thus the most plausible structured dual obstruction is exactly
calibrated away by the Catalan owner slack.

The remaining theorem is now a concrete supersaturation statement:
an extremal auxiliary matching with more than (O(D)) uncovered lower
vertices must contain an eligible two-slack augmenter, and an extremal
matching with more than (O(D)) owner cycles must contain an eligible
zero-signature hexagon (or a higher member of the same hierarchy).  This
note proves the configurations and all rate ledgers, but not that
supersaturation theorem.

## 1. Notation: the owner-resource map

Put

\[
 \Omega=[2m],\qquad \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal P=\binom{\Omega}{m}/(X\sim X^c).
\]

For a Kneser edge (e=\{R,S\}), write

\[
             \Omega\setminus(R\cup S)=\{a,b\}.
\]

Its two complementary-owner resources are

\[
        \rho(e)=\big\{[R+a],[R+b]\big\}.                     \tag{1.1}
\]

The same unordered pair is obtained from the (S)-side.  An auxiliary
matching in the complement-pair clone hypergraph is exactly a Kneser
matching in which every (P\in\mathcal P) occurs at most twice in the
resource multiset, together with an injection of those occurrences into
the two clones of (P).

## 2. A four-coordinate two-slack augmenter

Let

\[
 \Omega=C\ \dot\cup\ D\ \dot\cup\{0,1,2,3\},\qquad
 |C|=|D|=m-2.                                                  \tag{2.1}
\]

For compactness write (Ci=C\cup\{i\}), and similarly for (D).
Consider the old edge

\[
                       e^- =\{C2,D1\}                         \tag{2.2}
\]

and the two new edges

\[
                 e_1^+=\{C0,D1\},\qquad
                 e_2^+=\{C2,D0\}.                            \tag{2.3}
\]

They form the alternating Kneser path

\[
                   C0-D1-C2-D0,                               \tag{2.4}
\]

whose middle edge is old and whose two outer edges are new.

For a two-subset \(A\subseteq\{0,1,2,3\}\), put

\[
                       P_A=[C\cup A].                          \tag{2.5}
\]

The symbols \(P_A\) and \(P_{A^c}\) are generally distinct: complementation
also exchanges the cores \(C,D\).  Keeping that orientation is essential.

### Theorem 2.1 (two-slack augmentation identity)

The resource multisets in (2.2)--(2.3) are

\[
 \rho(e^-)=\{P_{02},P_{23}\},                                \tag{2.6}
\]

\[
 \rho(e_1^+)\uplus\rho(e_2^+)
   =\{P_{02},P_{23},P_{03},P_{12}\}.                          \tag{2.7}
\]

Consequently the signed owner-load change is exactly

\[
 \rho(e_1^+)+\rho(e_2^+)-\rho(e^-)
   =\mathbf e_{P_{03}}+\mathbf e_{P_{12}}.
                                                                    \tag{2.8}
\]

Suppose an auxiliary matching contains a lift of \(e^-\), the lower
vertices \(C0,D0\) are uncovered, and \(P_{03},P_{12}\) each have a free
clone.  Then replacing \(e^-\) by \(e_1^+,e_2^+\) gives another auxiliary matching,
larger by one.  It covers precisely the two additional lower vertices
\(C0,D0\), preserves every old resource load, and increases the loads of
\(P_{03},P_{12}\) by one each.

#### Proof

The leave of \(e^-\) is \(\{0,3\}\), so (1.1) gives

\[
 \rho(e^-)=\{[C02],[C23]\}=\{P_{02},P_{23}\}.
\]

The leaves of (e_1^+) and (e_2^+) are respectively ({2,3}) and
({1,3}).  Hence

\[
 \rho(e_1^+)=\{P_{02},P_{03}\},\qquad
 \rho(e_2^+)=\{P_{12},P_{23}\},
\]

which proves (2.6)--(2.8).  Reuse the old \(P_{02}\)-clone on \(e_1^+\),
reuse the old \(P_{23}\)-clone on \(e_2^+\), and use one free clone at
each of \(P_{03},P_{12}\).  The four lower vertices in (2.4)
are distinct, and the only old lower vertices used by the new edges are
the endpoints of (e^-).  This proves the matching assertion. \(\square\)

### Corollary 2.2 (exact number for a prescribed endpoint pair)

Let (R,S\in\mathcal L) satisfy (|R\cap S|=1).  There are exactly six
labelled realizations of Theorem 2.1 having (R=C0) and (S=D0): the
common element is forced to be (0), the cores are

\[
                 C=R\setminus\{0\},\qquad D=S\setminus\{0\},
\]

and the three elements of (Omega\setminus(R\cup S)) may be assigned
the labels (1,2,3) in (3!) ways.

This exact count is both useful and cautionary: an arbitrary matching need
not contain one of the six required middle edges.  The theorem supplies a
local augmenting move, not by itself a supersaturation theorem.

### Theorem 2.3 (two-slack augmenter at every intersection scale)

Let \(R,S\in\mathcal L\) be distinct and put

\[
 t=|R\cap S|,\qquad C=R\setminus S,\qquad D=S\setminus R.
                                                                    \tag{2.9}
\]

Then \(0\le t\le m-2\) and \(|C|=|D|=m-1-t\).  Choose
\(h\in\Omega\setminus(R\cup S)\).  The remaining active set

\[
 Z_0=(R\cap S)\ \dot\cup\
       \bigl(\Omega\setminus(R\cup S\cup\{h\})\bigr)          \tag{2.10}
\]

has size \(2t+1\).  Identify it with \(\mathbb Z_{2t+1}\) so that

\[
                 R\cap S=\{0,1,\ldots,t-1\}.                 \tag{2.11}
\]

For \(0\le i\le t\), with all indices in \(\mathbb Z_{2t+1}\), define

\[
 A_i=\{-i,-i+1,\ldots,t-1-i\},\qquad
 B_i=\{t-i,t+1-i,\ldots,2t-1-i\}.                            \tag{2.12}
\]

There is an alternating Kneser path from \(R=C\cup A_0\) to
\(S=D\cup B_t\) whose old and new parity classes are

\[
 e_i^-=\{C\cup A_{i+1},D\cup B_i\}
       \quad(0\le i<t),                                      \tag{2.13}
\]

\[
 e_i^+=\{C\cup A_i,D\cup B_i\}
       \quad(0\le i\le t).                                  \tag{2.14}
\]

Its owner-resource signature is

\[
             \sum_{i=0}^{t}\rho(e_i^+)
             -\sum_{i=0}^{t-1}\rho(e_i^-)
             =\mathbf e_{[R\cup\{h\}]}
              +\mathbf e_{[S\cup\{h\}]}.                    \tag{2.15}
\]

Consequently, if an auxiliary matching contains lifts of all \(t\) old
edges, leaves \(R,S\) uncovered, and each of \([R+h],[S+h]\) has a free
clone,
then switching the entire path increases its size by one, covers \(R,S\),
and respects every clone capacity.

#### Proof

The sets \(A_i,B_i\) are disjoint \(t\)-sets.  Their union misses

\[
                    g_i=-i-1
\]

inside \(Z_0\), in addition to \(h\).  Similarly \(A_{i+1}\) and \(B_i\)
are disjoint and miss

\[
                    q_i=t-1-i
\]

inside \(Z_0\), in addition to \(h\).  Therefore all displayed pairs are
Kneser edges.  The \(A_i\)'s are distinct, as are the \(B_i\)'s, so both
parity classes are matchings.  Also \(A_0=B_t=R\cap S\), giving the stated
endpoints.

For a \((t+1)\)-subset \(Y\subseteq Z_0\cup\{h\}\), abbreviate

\[
                         P_Y=[C\cup Y].                       \tag{2.16}
\]

The two resources of the new edge \(e_i^+\) are

\[
             P_{A_i\cup\{g_i\}},\qquad P_{A_i\cup\{h\}},     \tag{2.17}
\]

and those of the old edge \(e_i^-\) are

\[
        P_{A_{i+1}\cup\{q_i\}},\qquad
        P_{A_{i+1}\cup\{h\}}.                                \tag{2.18}
\]

The interval identity

\[
             A_i\cup\{g_i\}=A_{i+1}\cup\{q_i\}               \tag{2.19}
\]

cancels the first resources in (2.17)--(2.18) for \(0\le i<t\).
The \(h\)-resources telescope, leaving \(P_{A_0\cup\{h\}}\).  Finally,

\[
 Z_0\setminus(A_t\cup\{g_t\})=A_0,
\]

so complementation in the full ground set gives

\[
 [C\cup A_t\cup\{g_t\}]
   =[D\cup A_0\cup\{h\}]
   =[S\cup\{h\}].                                             \tag{2.20}
\]

Together with
\([C\cup A_0\cup\{h\}]=[R\cup\{h\}]\), this gives the two distinct
terminal resources in (2.15).
Clone reuse is now identical to Theorem 2.1: every cancelled resource
keeps its old clone, and the two terminal occurrences use one free clone
from each of \([R+h],[S+h]\).  These owner pairs are distinct because
both displayed representatives contain \(h\), whereas complementary
middle sets are disjoint. \(\square\)

For a fixed pair \(R,S\), there are \(t+2\) choices for \(h\) and
\(t!(t+1)!\) oriented identifications in (2.11).  This gives factorial
template supply.  For fixed ordered endpoints and \(t\ge1\), the resulting
ordered paths are distinct: \(h\) is the unique active coordinate absent
from every lower vertex of the path, while the successive differences
\(A_i\triangle A_{i+1}\) recover the cyclic labels, with the one remaining
label recovered from \(B_0\).  At \(t=0\), the two choices of the
distinguished \(h\) label the same direct Kneser edge, with its two
terminal resources exchanged.  This harmless multiplicity two is retained
in the labelled census below.  The load-bearing issue is not formal
existence of a path but the simultaneous presence of its \(t\) old edges
in the current matching.

### Corollary 2.4 (exact critical template census)

Fix \(R\in\mathcal L\).  The number of ordered pairs
\((S,\mathcal A)\), where \(|R\cap S|=t\) and \(\mathcal A\) is an
oriented augmenter of Theorem 2.3 from \(R\) to \(S\), is exactly

\[
 \begin{aligned}
 \mathsf A_t(R)
 &=\binom{m-1}{t}\binom{m+1}{t+2}
     (t+2)t!(t+1)!\\
 &=(m-1)_t\,(m+1)_{t+2},                                    \tag{2.21}
 \end{aligned}
\]

where labelled templates are counted (including the multiplicity two at
\(t=0\)) and \((x)_j=x(x-1)\cdots(x-j+1)\).  With
\(\Delta=\binom{m+1}{2}\), uniformly for \(t=o(\sqrt m)\),

\[
              {\mathsf A_t(R)\over\Delta^t}
       =2^t m^2\exp\!\bigl(O(t^2/m)\bigr).                   \tag{2.22}
\]

#### Proof

There are

\[
 \binom{m-1}{t}\binom{m+1}{m-1-t}
 =\binom{m-1}{t}\binom{m+1}{t+2}
\]

choices of \(S\) with intersection \(t\) with \(R\).  Theorem 2.3 has
\((t+2)t!(t+1)!\) oriented labelled realizations for each such \(S\).
For \(t\ge1\) the injectivity just proved prevents physical overcounting;
for \(t=0\) the stated labelled convention applies.  Factorial
cancellation gives (2.21), and the standard falling-factorial estimate
gives (2.22).
\(\square\)

Equation (2.22) locates the critical scale exactly.  In the diffuse
benchmark where

* an old Kneser edge is present with density \(\Delta^{-1}\);
* a second endpoint is uncovered with density \(z\); and
* an owner clone is free with density \(f\),

the expected number of labelled eligible depth-\(t\) augmenters from a
fixed uncovered \(R\) is

\[
               (1+o(1))\,2^t m^2 zf^2.                      \tag{2.23}
\]

This is a calibration, not a proof of independence.  At the desired
critical scale \(z\asymp f\asymp1/m\), it becomes

\[
                         (1+o(1)){2^t\over m}.                \tag{2.24}
\]

Thus \(t=\log_2m+O(1)\) is exactly the first scale at which the augmenter
inventory can remain visible at a Catalan-size leave.  Bounded augmenters
stall above the target, while the logarithmic hierarchy has precisely the
right entropy.  A rigorous proof must replace the diffuse multiplication
in (2.23) by a correlation-robust supersaturation inequality for the
actual matching.

### Corollary 2.5 (balanced circulations from paired augmenters)

For an oriented augmenter \(\mathcal A\), let

\[
 \tau_{\mathcal A}
   =\sum_{e\in E^+(\mathcal A)}\mathbf e_e
    -\sum_{e\in E^-(\mathcal A)}\mathbf e_e.                  \tag{2.25}
\]

If \(\mathcal A,\mathcal A'\) have the same ordered endpoints \(R,S\) and
the same special coordinate \(h\), then

\[
 \partial_{\mathcal L}
   (\tau_{\mathcal A}-\tau_{\mathcal A'})=0,\qquad
 \rho(\tau_{\mathcal A}-\tau_{\mathcal A'})=0.                \tag{2.26}
\]

Thus differences of same-terminal augmenters give a factorial family of
simultaneous lower-neutral and owner-neutral integer circulations.  If two
chosen paths are internally vertex-disjoint, the positive and negative
parts of their difference are literal Kneser matchings and hence form an
exact zero-signature switch.

#### Proof

Along one alternating path every internal lower vertex occurs once with
each sign, while the two endpoints occur only in the positive parity
class.  Hence

\[
                  \partial_{\mathcal L}\tau_{\mathcal A}
                  =\mathbf e_R+\mathbf e_S.
\]

Theorem 2.3 gives

\[
                  \rho(\tau_{\mathcal A})
                  =\mathbf e_{[R+h]}+\mathbf e_{[S+h]}.
\]

Both expressions depend only on \(R,S,h\), so subtraction proves (2.26).
Internal vertex-disjointness makes the two resulting parity classes
matchings after cancelling any common edge. \(\square\)

## 3. A six-coordinate zero-signature hexagon

Let

\[
 \Omega=C\ \dot\cup\ D\ \dot\cup Z,\qquad
 |C|=|D|=m-3,\qquad Z=\{0,1,2,3,4,5\}.                       \tag{3.1}
\]

Write (Cij=C\cup\{i,j\}), and similarly for (D).  Consider the three
old matching edges

\[
\begin{aligned}
 e_0^-&=\{C01,D24\},\\
 e_1^-&=\{C13,D04\},\\
 e_2^-&=\{C12,D34\},
\end{aligned}                                                  \tag{3.2}
\]

and the three new matching edges

\[
\begin{aligned}
 e_0^+&=\{C13,D24\},\\
 e_1^+&=\{C12,D04\},\\
 e_2^+&=\{C01,D34\}.
\end{aligned}                                                  \tag{3.3}
\]

The six edges alternate around the simple Kneser hexagon

\[
 C01-D24-C13-D04-C12-D34-C01.                                \tag{3.4}
\]

For a three-subset \(A\subset Z\), put \(P_A=[C\cup A]\).  As in
Section 2, the core \(C\) is retained in this notation; no identification
of \(P_A\) with \(P_{Z\setminus A}\) is made.

### Theorem 3.1 (zero owner signature)

The two parity classes (3.2)--(3.3) use exactly the same owner-resource
multiset:

\[
 \biguplus_{i=0}^2\rho(e_i^-)
 =\biguplus_{i=0}^2\rho(e_i^+)
 =\{P_{013},P_{015},P_{123},P_{135},P_{012},P_{125}\}.        \tag{3.5}
\]

Therefore any auxiliary matching containing lifts of all three old edges
may replace them by lifts of the three new edges, reusing the same clone of
each resource.  The projected Kneser matching, its cardinality, every lower
degree, and every individual middle-owner degree are preserved exactly.

#### Proof

For the old edges, (1.1) gives successively

\[
\{P_{013},P_{015}\},\qquad
 \{P_{123},P_{135}\},
\]

\[
\{P_{012},P_{125}\}.
\]

For the new edges it gives

\[
\{P_{013},P_{135}\},
\]

\[
\{P_{123},P_{125}\},\qquad
 \{P_{012},P_{015}\}.
\]

These are the same six resources, each once.  Both parity classes are
matchings by inspection of their six distinct lower vertices.  Clone
reuse then proves the final assertion. \(\square\)

### Corollary 3.2 (a literal component-splicing move)

Let (overline H(Q)) be the quotient owner graph on (mathcal P), with
one edge joining the two resources of each selected Kneser edge.  In the
notation of (3.5), the hexagon changes the three quotient edges

\[
 (P_{013}P_{015}),\ (P_{123}P_{135}),\ (P_{012}P_{125})       \tag{3.6}
\]

to

\[
 (P_{013}P_{135}),\ (P_{123}P_{125}),\ (P_{012}P_{015}).     \tag{3.7}
\]

If (3.6) lies on three distinct cycle components of the (0/2) quotient
owner graph, then (3.7) joins them into one cycle.  Thus the quotient cycle
count falls by two.  Since the physical Johnson lift is a two-fold cover
of the quotient graph, its number of cycle components also falls whenever
the three old quotient cycles are distinct (from at least three components
over them to at most two over the new quotient cycle).

#### Proof

Deleting one edge from each old quotient cycle produces three paths with
endpoint pairs as in (3.6).  The new pairs in (3.7) concatenate those paths
cyclically, hence form one quotient cycle.  A cycle has either one or two
components in a two-fold cover. \(\square\)

This is the balanced multi-rectangle circulation missing from the
single-rectangle analysis: its owner signature is zero **over the
integers**, not merely modulo two.

### Corollary 3.3 (exact hexagon census and its critical limitation)

The number of unoriented zero-signature hexagons of Theorem 3.1 is

\[
        { (2m)!\over12\,(m-2)!^2}
        ={W\,m^2(m-1)^2\over12}.                              \tag{3.8}
\]

#### Proof

The hexagon has a core-only normal form.  Put

\[
 K_A=C\cup\{1\},\qquad K_B=D\cup\{4\}.
\]

These are disjoint \((m-2)\)-sets.  Of the four remaining coordinates,
choose one unused coordinate \(h\); call the other three \(X\).  The six
lower vertices are

\[
              \{K_A+x:x\in X\}\ \dot\cup\
              \{K_B+x:x\in X\}.                              \tag{3.9}
\]

Their Kneser graph is \(K_{3,3}\) with the diagonal removed, hence a
6-cycle.  Its two parity matchings are precisely the two sides of the
zero-signature switch.  Conversely, the two three-fold intersections
recover \(K_A,K_B\), and the unique absent coordinate recovers \(h\).

There are

\[
 {1\over2}\binom{2m}{m-2}\binom{m+2}{m-2}
\]

unordered choices of the two cores and four choices of \(h\).  This
simplifies to (3.8). \(\square\)

Under the diffuse benchmark in which each prescribed Kneser edge is
present with density \(\Delta^{-1}\), the number of hexagons with one
specified parity class present is only

\[
 {Wm^2(m-1)^2\over12}\Delta^{-3}
 =\left({2\over3}+o(1)\right){W\over m^2}.                    \tag{3.10}
\]

Counting both choices of old parity doubles the constant.  Thus bounded
hexagons are algebraically sufficient to move inside the exact owner-load
locus, but their diffuse supply is a factor \(m\) below the critical
component scale \(D\asymp W/m\).  A proof that starts with
\(\Theta(W)\) owner cycles cannot expect isolated six-coordinate
hexagons alone to merge down to \(O(D)\); it needs longer paired-augmenter
circulations, a non-diffuse cycle geometry, or a separate low-component
construction.  This is a rate limitation, not an impossibility theorem.

## 4. The exact extremal successor

Choose an auxiliary matching lexicographically as follows:

1. maximize its cardinality;
2. subject to that, minimize the number of cycle components of its
   (0/2) owner core.

Then it contains no eligible configuration of Theorem 2.1 and no
cycle-merging configuration of Theorem 3.1.  Consequently the critical
Kneser theorem would follow from the following purely finite
supersaturation statement.

> **Augmenter--hexagon supersaturation.**  If an auxiliary matching has
> (u\gg D) uncovered lower vertices, it contains an eligible two-slack
> augmenter.  If its (0/2) owner core has (c\gg D) cycle components,
> it contains an eligible zero-signature hexagon on three distinct cycles;
> the same alternatives hold after discarding (O(D)) nonpolarized owner
> pairs.

Unlike the original critical-rounding statement, this successor has two
explicit finite certificates and an exact descent potential
((u,c)).  Its truth is not established below; the next two sections audit
the principal obstruction and the natural dual cuts.

The augmentation half can be stated without qualitative language.  For a
matching \(\mathcal F\), let

\[
 z={u\over N},\qquad
 f={D+u\over W};                                               \tag{4.1}
\]

\(f\) is the **exact** fraction of unused owner clones.  Let
\(\mathsf X_t(\mathcal F)\) count oriented Theorem 2.3 templates whose two
endpoints are uncovered, all old edges belong to \(\mathcal F\), and both
terminal owner pairs have a free clone.  Then the following is sufficient
for critical rounding:

\[
 \boxed{\quad
 u\ge C D\ \Longrightarrow\
 \sum_{0\le t\le L_m}\mathsf X_t(\mathcal F)>0,
 \qquad
 L_m=\left\lceil\log_2m+3\log_2\log m\right\rceil .
 \quad}                                                       \tag{4.2}
\]

Indeed, every counted template reduces \(u\) by two and preserves all
clone capacities.  Iteration stops only at \(u<CD\).  The diffuse census
(2.23) predicts, per uncovered endpoint,

\[
          \mathsf X_t/u\asymp 2^tm^2zf^2.                    \tag{4.3}
\]

At the last relevant scale \(u\asymp D\), one has
\(z,f\asymp1/m\), and the right side is \(2^t/m\).  Thus the window in
(4.2) contains a factor \((\log m)^3\) of benchmark slack.  The real open
content of (4.2) is robustness against correlations created by the
previous switches; no further counting or rate choice is missing.

## 5. Why a bounded augmenter inventory cannot prove the critical rate

For a fixed (t)-set (T\subset\Omega), let

\[
       \mathcal U_T=\{R\in\mathcal L:T\subseteq R\}.           \tag{5.1}
\]

Then

\[
 |\mathcal U_T|=\binom{2m-t}{m-1-t}
                =(2^{-t}+o(1))N                              \tag{5.2}
\]

for (t=o(\sqrt m)).  Every two members of (mathcal U_T) intersect in
at least (t) points.  In particular, for (t\ge2) this family contains
no endpoint pair for Theorem 2.1, despite having size ((1/4+o(1))N\gg D)
when (t=2).

More generally, an augmenter whose two uncovered endpoints are required
to have intersection below a fixed (s) is invisible on every (s)-star,
whose size is ((2^{-s}+o(1))N).  Since

\[
                       D={N\over m},                          \tag{5.3}
\]

local-intersection augmenters must reach

\[
                       s\ge(1-o(1))\log_2m                    \tag{5.4}
\]

before their largest elementary blind spot falls to the critical scale.
Thus Theorem 2.1 is a genuine positive move, but a proof from local
augmenters requires either a logarithmic hierarchy or a theorem excluding
clustered leaves.

## 6. The (t)-star owner cuts are exactly calibrated, not obstructive

For (1\le t\le m-1) and fixed (T\in\binom\Omega t), put

\[
 a_t=|\mathcal U_T|=\binom{2m-t}{m-1-t}.                     \tag{6.1}
\]

Let (mathcal P_T\subseteq\mathcal P) be the owner pairs having a
representative which contains (T).  The representative is unique, and

\[
 p_t:=|\mathcal P_T|=\binom{2m-t}{m-t},\qquad
 {p_t\over a_t}={m+1\over m-t}.                              \tag{6.2}
\]

Thus the cut has positive, but only relative (O(t/m)), owner slack.

Let an auxiliary matching have size (k=(N-u)/2), and let (u_T) of
its uncovered lower vertices belong to (mathcal U_T).  Because two
members of (mathcal U_T) cannot be disjoint, every covered member of
(mathcal U_T) lies on a different selected Kneser edge.  Such an edge
uses two clones from (mathcal P_T).  Let (ell_T\ge0) count all other
selected resource incidences in (mathcal P_T).  Clone capacity gives

\[
             2(a_t-u_T)+\ell_T\le2p_t.                       \tag{6.3}
\]

### Theorem 6.1 (aggregate star-cut identity)

Summed over all (T\in\binom\Omega t), the leakage is exactly

\[
       \sum_T\ell_T=2(N-u)\binom{m-1}{t-1}.                  \tag{6.4}
\]

Moreover

\[
 \binom{2m}{t}(p_t-a_t)
 =N\binom{m-1}{t-1}+D\binom mt.                              \tag{6.5}
\]

Consequently the sum of all capacity inequalities (6.3) reduces to

\[
                         u\ge-D,                              \tag{6.6}
\]

and is therefore vacuous.  In particular, the full hierarchy of natural
(t)-star cuts supplies no averaged odd-set obstruction to critical
rounding.

#### Proof

Fix a selected Kneser edge.  Each of its two owner-pair resources has two
middle representatives, and hence contains (2\binom mt) occurrences of
(t)-sets.  Its total resource incidence over all (T)'s is therefore
(4\binom mt).  Its two lower endpoints contain altogether
(2\binom{m-1}t) (t)-sets; for each such (T), two of the resource
incidences are already charged to the covered star vertex.  The remaining
leakage per selected edge is

\[
 4\left(\binom mt-\binom{m-1}t\right)
 =4\binom{m-1}{t-1}.
\]

Multiplying by (k=(N-u)/2) proves (6.4).

For (6.5), substitute (6.1)--(6.2) and use factorial cancellation; an
equivalent form is

\[
 \binom{2m}{t}\left[
 \binom{2m-t}{m-t}-\binom{2m-t}{m-1-t}\right]
 =\binom{2m}{m-1}\binom{m-1}{t-1}
  +{1\over m+1}\binom{2m}{m}\binom mt.
\]

Finally sum (6.3), use

\[
 \sum_Tu_T=u\binom{m-1}t,
\]

and insert (6.4)--(6.5).  After cancelling the common
(N\binom{m-1}{t-1}) term, Pascal's identity leaves precisely

\[
 -u\binom mt\le D\binom mt,
\]

which is (6.6). \(\square\)

Individual star cuts remain informative: (6.3) says that a construction
covering nearly every member of one (t)-star must suppress leakage into
(mathcal P_T) to its narrow (O(t/m)) capacity margin.  What Theorem
6.1 rules out is an aggregate contradiction obtained merely by summing
those cuts.

## 7. Rate audit for the mesoscopic compiler

Recall

\[
 W=\binom{2m}m,\qquad N={m\over m+1}W,\qquad
 D=W-N={W\over m+1}.                                         \tag{7.1}
\]

For

\[
                      H=\sqrt m\log\log m,                   \tag{7.2}
\]

one has

\[
 {D\over W/H}={H\over m+1}
   =(1+o(1)){\log\log m\over\sqrt m}\longrightarrow0.       \tag{7.3}
\]

Therefore (u,c=O(D)) are both more than strong enough:

\[
                  O(D)=o(W/H).                               \tag{7.4}
\]

The exact moves above incur no hidden (H)-loss.  The augmenter changes
one matching edge into two and the hexagon changes three into three; their
support sizes are bounded independently of (m,H), and their owner-load
identities are exact.  The only unresolved loss is quantitative
availability: a bounded family of such moves does not defeat the
(t)-star blind spots before logarithmic support size.

## 8. Honest conclusion

The critical Kneser lane has advanced in two ways.

* There is now a literal capacity-respecting augmentation move at every
  intersection scale, so Catalan clone slack can be consumed in exact
  two-terminal packets rather than by diffuse rounding.
* There is now a literal zero-signature component switch, so the
  elementary-rectangle freeze does not extend to the full alternating
  Kneser switch space.

The surviving mathematical problem is not the existence of balanced local
directions.  It is a critical supersaturation/anti-clustering theorem for
those directions, necessarily with logarithmically growing reach or an
independent mechanism preventing (t)-star concentration.  The aggregate
star-cut calculation supplies no dual obstruction.  No critical-rate
matching or component theorem is claimed here.
