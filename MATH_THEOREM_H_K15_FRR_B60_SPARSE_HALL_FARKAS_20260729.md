# Sparse Hall--Farkas certificates for the static `FRR(7,4)` endpoint no-go

Date: 2026-07-29  
Lane: H  
Status: proved, solver-free replay.  The certificates concern the saved
source-fixed static seam catalogue; they are not an unrestricted
`FRR(7,4)` no-go.

## 0. Verdict

The endpoint-stage `INFEASIBLE` verdict for equations (2.2)--(2.6) of
`MATH_THEOREM_K15_FRR_STATIC_ENDPOINT_EXACT_COVER_20260729.md` has a sparse
continuous explanation.

1. A **29-row spacing-free Hall--Farkas certificate** uses only two collar
   covers, eighteen endpoint equations, and nine upper-colour equations.
   It projects to

   \[
      z_{22}+z_{401}\le1,                                    \tag{0.1}
   \]

   while the two collars force `z_22>=1` and `z_401>=1`.
2. A separate **23-row inclusion-minimal certificate** uses one collar, one
   spacing row, sixteen endpoint equations, and five upper equations.  It
   forces

   \[
      z_{204}\ge z_{401},\qquad z_{206}\ge z_{401},
      \qquad z_{401}\ge1,                                    \tag{0.2}
   \]

   contradicting `z_204+z_206<=1`.  Deleting any one of its 23 model rows
   leaves an explicit `0-1` solution of the other 22 rows.

Both proofs use only the displayed equalities, covering inequalities,
ordinary box bounds, and nonnegativity.  They remain contradictions over
the continuous cube `[0,1]`; integrality, the cardinality equation
`sum z_h=60`, and every lower-colour row are absent.

This does **not** prove a general lower bound `b>=61`.  It proves something
stronger but much narrower: changing the cut budget cannot repair the saved
`B_0`, `Z_15`-equivariant, source-fixed static seam catalogue.  The catalogue
uses the two-sided compatibility rule (1.1) and omits dynamic seams whose
validity could change under overlapping cuts.  Positive-only collar seams,
nonequivariant repairs, a different antecedent, and unrestricted `RTR` remain
outside the theorem.

## 1. Notation

Let

* `E(h,L)` and `E(h,R)` denote the two endpoint equations (2.5) owned by cut
  orbit `h`;
* `U(h)` denote upper-colour equation (2.6); and
* `y_i` denote seam variable `i` in the zero-based saved catalogue.

Every such equality has the form

\[
       \sum_{i\in D}y_i=z_h.                                  \tag{1.1}
\]

All variables are nonnegative and at most one.  An empty domain therefore
forces `z_h=0`; once `z_h=0`, every seam in its domain is zero.

The only collar rows used below are

\[
 z_{20}+z_{21}+z_{22}+z_{23}\ge1,                             \tag{1.2}
\]

\[
 z_{400}+z_{401}+z_{402}+z_{403}\ge1.                         \tag{1.3}
\]

## 2. The spacing-free 29-row Hall certificate

### Theorem 2.1

The subsystem consisting of the following 29 original model rows is
infeasible over `[0,1]`:

* the two collar rows (1.2)--(1.3);
* the nineteen zero/peeling rows

  \[
  \begin{gathered}
  U(20),\ E(66,L),\ U(66),\ E(66,R),\ E(134,R),\ U(134),\\
  E(169,R),\ E(169,L),\ U(402),\ E(21,L),\\
  E(157,L),\ E(157,R),\ E(400,R),\ U(403),\\
  E(161,L),\ U(161),\ E(28,R),\ E(28,L),\ U(28);
  \end{gathered}                                               \tag{2.1}
  \]

* and the eight core equations

  \[
  E(23,R),\ U(205),\ E(205,R),\ E(22,R),\ E(401,R),
  \ E(27,R),\ U(27),\ E(27,L).                               \tag{2.2}
  \]

No spacing, cut-cardinality, or lower-colour row is used.

#### Proof: zero peeling

The empty roles are

\[
 U(20),\quad E(66,L),\quad E(134,R),\quad E(169,R),\quad U(402).
                                                                    \tag{2.3}
\]

Thus `z_20=z_66=z_134=z_169=z_402=0`.  The exact small domains in the
saved catalogue are:

\[
\begin{array}{c|l}
U(66)&y_{218}+y_{1022}=z_{66}\\
E(21,L)&y_{218}=z_{21}\\
E(66,R)&y_{606}+y_{607}+y_{608}+y_{609}=z_{66}\\
E(157,L)&y_{606}=z_{157}\\
E(157,R)&y_{1204}+y_{1205}+y_{1206}=z_{157}\\
E(161,L)&y_{1204}=z_{161}\\
U(161)&y_{274}=z_{161}\\
E(28,R)&y_{274}=z_{28}.
\end{array}                                                     \tag{2.4}
\]

Nonnegativity successively gives

\[
 z_{21}=z_{157}=z_{161}=z_{28}=0.                             \tag{2.5}
\]

Similarly,

\[
 E(169,L)\Longrightarrow y_{1237}=y_{1241}=0,
\]

and the domains

\[
 E(400,R):y_{1241}=z_{400},qquad
 U(403):y_{1237}+y_{1241}=z_{403}                             \tag{2.6}
\]

give `z_400=z_403=0`.  Finally `E(28,L)` kills `y_272`, while
`U(28)` kills `y_750,y_977,y_982`.

#### Proof: the first collar

The relevant equations are

\[
 E(23,R):\quad z_{23}=y_{230}+y_{231}+y_{232}.                 \tag{2.7}
\]

Since `z_134=0`, row `U(134)` kills `y_230,y_231`, so
`z_23=y_232`.  Next

\[
\begin{aligned}
 U(205):\quad
 z_{205}&=y_{232}+y_{234}+y_{235}+y_{236}+y_{1171}+y_{1426},\\
 E(205,R):\quad
 z_{205}&=y_{234}+y_{750}+y_{977}+y_{982}+y_{1426}.
\end{aligned}                                                  \tag{2.8}
\]

Subtracting and using the zeros from `U(28)` gives

\[
 y_{232}+y_{235}+y_{236}+y_{1171}=0.                          \tag{2.9}
\]

Hence `z_23=0`.  Equation `E(22,R)` has the singleton domain

\[
                       z_{22}=y_{226}.                        \tag{2.10}
\]

Together with `z_20=z_21=z_23=0`, collar (1.2) now forces

\[
                       z_{22}\ge1.                            \tag{2.11}
\]

#### Proof: the second collar and the Hall shore

Because `y_272=0`,

\[
 E(401,R):\quad z_{401}=y_{263}.                              \tag{2.12}
\]

The three equations around owner 27 are

\[
\begin{aligned}
 E(27,R):\quad z_{27}&=y_{261}+y_{262}+y_{263}+y_{264},\\
 U(27):\quad z_{27}&=y_{258}+y_{264},\\
 E(27,L):\quad z_{27}&=y_{226}+y_{257}+y_{258}+y_{259}+y_{260}.
\end{aligned}                                                  \tag{2.13}
\]

The first two imply

\[
 y_{258}=y_{261}+y_{262}+y_{263}\ge y_{263}=z_{401}.          \tag{2.14}
\]

Using (2.10), (2.13), nonnegativity, and the box bound
`z_27<=1` gives the projected Hall inequality

\[
 z_{22}+z_{401}=y_{226}+y_{263}
 \le y_{226}+y_{258}\le z_{27}\le1.                          \tag{2.15}
\]

On the other hand, `z_400=z_402=z_403=0`, so collar (1.3) forces

\[
                       z_{401}\ge1.                           \tag{2.16}
\]

Equations (2.11), (2.15), and (2.16) give

\[
          2\le z_{22}+z_{401}\le1,
\]

a contradiction.  QED.

### Hall interpretation

The two collars require one unit at owner 22 and one unit at owner 401.
The endpoint/upper equalities project both units into the single capacity-one
shore `E(27,L)`.  Inequality (2.15) is exactly the deficient-shore Hall cut.

The two collar rows are individually essential for this displayed
certificate.  If (1.2) is removed, set

\[
 z_{401}=z_{27}=y_{263}=y_{258}=1
\]

and all other displayed variables to zero.  If (1.3) is removed, set

\[
 z_{22}=z_{27}=y_{226}=y_{264}=1
\]

and all other displayed variables to zero.  These assignments satisfy the
remaining 28 rows.  No claim is made that all 29 rows form a globally
minimum-cardinality irreducible subsystem.

## 3. A 23-row inclusion-minimal Farkas certificate

The preceding proof avoids spacing.  There is also a smaller row set for
which deletion-minimality can be proved completely.

### Theorem 3.1

The following 23 rows form an inclusion-minimal infeasible subsystem over
`[0,1]`:

1. collar `C={400,401,402,403}`;
2. spacing row `z_204+z_206<=1`;
3. endpoint equations

   \[
   \begin{gathered}
   E(27,R),E(28,L),E(28,R),E(66,L),E(66,R),\\
   E(157,L),E(157,R),E(161,L),E(169,L),E(169,R),\\
   E(204,R),E(206,R),E(309,L),E(309,R),E(400,R),E(401,R);
   \end{gathered}                                              \tag{3.1}
   \]

4. upper equations

   \[
        U(27),U(161),U(401),U(402),U(403).                    \tag{3.2}
   \]

#### Proof of infeasibility

Rows `E(169,R),E(169,L),E(400,R),U(402),U(403)` force

\[
 z_{400}=z_{402}=z_{403}=0,
\]

so the collar gives `z_401>=1`.

Rows `E(309,L),E(309,R)` kill `y_1662`.  Therefore

\[
 U(401):z_{401}=y_{1425},qquad
 E(204,R):z_{204}=y_{1420}+y_{1425},
\]

and hence

\[
                       z_{204}\ge z_{401}.                    \tag{3.3}
\]

The chain

\[
\begin{aligned}
E(66,L),E(66,R)&\Longrightarrow y_{606}=0,\\
E(157,L),E(157,R)&\Longrightarrow y_{1204}=0,\\
E(161,L),U(161)&\Longrightarrow y_{274}=0,\\
E(28,R),E(28,L)&\Longrightarrow y_{272}=0
\end{aligned}                                                  \tag{3.4}
\]

gives `E(401,R):z_401=y_263`.  Subtracting `E(27,R)` from
`U(27)` gives

\[
 y_{258}=y_{261}+y_{262}+y_{263}\ge z_{401}.                  \tag{3.5}
\]

Finally `E(206,R)` gives

\[
                       z_{206}\ge z_{401}.                    \tag{3.6}
\]

Adding (3.3), (3.6), and the spacing row yields

\[
 2z_{401}\le z_{204}+z_{206}\le1,
\]

contradicting `z_401>=1`.  This again uses only linear equalities and
nonnegativity.

#### Proof of inclusion-minimality

Let

\[
 A=\{z_{401},z_{204},y_{1425}\},\qquad
 B=\{z_{401},z_{27},z_{206},y_{263},y_{258}\}.                \tag{3.7}
\]

All variables not displayed in a witness are zero.  Removing the collar is
satisfied by the all-zero point; removing spacing is satisfied by `A union
B`.  For the five rows on the collar-zero arm, use respectively

\[
\begin{array}{c|l}
E(169,R)&z_{169},z_{400},z_{403},y_{1241}\\
E(169,L)&z_{400},z_{403},y_{1241}\\
E(400,R)&z_{400}\\
U(402)&z_{402}\\
U(403)&z_{403}.
\end{array}                                                     \tag{3.8}
\]

For the four rows on the `A` arm, retain `B` and add respectively

\[
\begin{array}{c|l}
E(309,L)&z_{309},y_{1662}\\
E(309,R)&y_{1662}\\
U(401)&\varnothing\\
E(204,R)&y_{1425}.
\end{array}                                                     \tag{3.9}
\]

For the first eight rows of the zero chain (3.4), retain `A` and add,
respectively,

\[
\begin{array}{c|l}
E(66,L)&z_{66},z_{157},z_{161},z_{28},y_{606},y_{1204},y_{274},y_{272}\\
E(66,R)&z_{157},z_{161},z_{28},y_{606},y_{1204},y_{274},y_{272}\\
E(157,L)&z_{157},z_{161},z_{28},y_{1204},y_{274},y_{272}\\
E(157,R)&z_{161},z_{28},y_{1204},y_{274},y_{272}\\
E(161,L)&z_{161},z_{28},y_{274},y_{272}\\
U(161)&z_{28},y_{274},y_{272}\\
E(28,R)&z_{28},y_{272}\\
E(28,L)&y_{272}.
\end{array}                                                     \tag{3.10}
\]

For the last four rows, retain `A` and use respectively

\[
\begin{array}{c|l}
E(401,R)&\varnothing\\
E(27,R)&y_{263}\\
U(27)&z_{27},y_{263}\\
E(206,R)&z_{27},y_{263},y_{258}.
\end{array}                                                     \tag{3.11}
\]

Direct substitution shows that each row-deletion witness violates only the
named deleted row.  Hence every one of the 23 rows is essential to this
subsystem.  This proves inclusion-minimality, not minimum cardinality among
all infeasible subsystems.  QED.

For exact comparison with the saved pseudo-Boolean file, these rows are OPB
lines

```text
94, 711,
1431,1432,1433,1508,1509,1690,1691,1698,
1714,1715,1785,1789,1994,1995,2177,2179,
2255,2389,2629,2630,2631.
```

## 4. Scope: not a universal `b>=61` theorem

The cardinality equation (2.2) is absent from both certificates.  Therefore
their conclusion is not “minimum cut size is at least 61.”  Inside the saved
static catalogue, no cut budget can satisfy the displayed endpoint/upper
system.

This stronger-looking conclusion is source-relative.  The seam columns were
built from:

1. the frozen `6390`-cycle turn derivative `B_0`;
2. `Z_15`-equivariant endpoint and upper-colour orbits;
3. source-fixed capped traces justified by separated collars; and
4. the two-sided compatibility rule (1.1), which is stronger than the exact
   positive-only `FRR` seam rule.

The 29-row proof drops spacing equations, but it does not add seams omitted
when this static catalogue was generated.  It is therefore a no-go for the
catalogue polyhedron, not for arbitrary overlapping or dynamically
recomputed collars.  It also leaves open nonequivariant seams, changes to the
small component, another rank-seven antecedent, and unrestricted `RTR(7,4)`.

The precise implication is:

> The saved `B_0` has no `Z_15`-equivariant, source-fixed, two-sided-
> compatible rainbow-collar repair represented by equations (2.3)--(2.6),
> at budget 60 or at any other budget.

That is the sharp proved boundary.

