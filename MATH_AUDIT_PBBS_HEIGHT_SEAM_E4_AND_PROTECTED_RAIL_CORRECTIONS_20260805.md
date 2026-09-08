# Audit and corrections for the PBBS seam, E4, and protected-rail chain

**Date:** 2026-08-05  
**Method:** literal PBBS edge indexing, normalized roots, and Boolean-set
calculus; no search or computation

**Audited files:**

1. MATH_THEOREM_PBBS_HEIGHT_SEAM_FAN_CALCULUS_AND_MIDDLE_INTERVAL_RESIDUAL_20260805.md;
2. MATH_THEOREM_PBBS_HEIGHT_E4_REFLECTED_RAIL_LEAVES_THREE_ENDPOINTS_PER_HEIGHT_20260805.md;
3. MATH_THEOREM_PBBS_HEIGHT_RESIDUAL_THREE_CHAINS_HAVE_TWO_PROTECTED_RAILS_20260805.md.

## 0. Verdict

The forward/reverse mountain iterates, correct-rank target triangle, and
the local E4 normalized-root calculation are correct in their stable
ranges. The three downstream conclusions are not correct as written.

1. The positive-prefix seam path in the first note uses an edge which the
   simultaneous ladder has deleted. Consequently its Theorem 5.1 does not
   establish the asserted left-ray, diagonal, or deep-end repairs.
2. An E4 rail for the forced cut at \(A_b\) belongs to the next
   height-\(b\) pentagon. In a finite ladder with pentagons through height
   \(H-1\), it is available only for \(b\le H-1\); the whole top family at
   \(b=H\), not just one endpoint, remains untreated.
3. The protected-rail note checks intersections of the rank-\(r\)
   complement states. The physical owner/q1 color is determined by their
   **union**. Each proposed rail repeats its first moving union, so the
   displayed incidence lift is not simple or 2-bounded.

There are clean partial repairs.

* Literal monotone height windows repair most left rays.
* The E4 calculation repairs one more diagonal layer than stated.
* Replacing the two bad cap states produces genuinely simple 2-bounded
  rails for the three named chains.

These corrections do not restore the claimed three-pair residual. With
only the currently proved paths, a non-top height has nine boundary pairs,
and an unclosed top height retains a quadratic family.

## 1. The mountain fan calculus through the target triangle is correct

Put

\[
 A_b=[1,b]\mathbin{\dot\cup}T_b,\qquad
 T_b=\{2b+1,2b+3,\ldots,2r-1\}.
\]

The literal forward and reverse iterates are

\[
 g^tA_b=[0,b-t]\mathbin{\dot\cup}[2b-t+2,2b]
          \mathbin{\dot\cup}T_b\qquad(1\le t\le b),
                                                               \tag{1.1}
\]

and

\[
 g^{-t}A_b=[t+1,b+t]\mathbin{\dot\cup}T_b
             \qquad(0\le t\le b-1).                         \tag{1.2}
\]

Their running intersections give

\[
 F_b(q)=[1,b-q]\mathbin{\dot\cup}T_b,\qquad
 R_b(v)=[v+1,b]\mathbin{\dot\cup}T_b.                       \tag{1.3}
\]

The extra forward endpoint is

\[
 F_b(b+1)=F_b(b+2)=T_{b+1}.                                \tag{1.4}
\]

It follows that the old correct-rank fan at the forced edge has exactly

\[
 u,v\ge0,\qquad u+v\le b-1,                                \tag{1.5}
\]

together with \((u,v)=(b,0)\), and

\[
 C_b(u,v)=[v+1,b-u-1]\mathbin{\dot\cup}T_b                 \tag{1.6}
\]

on (1.5), with \(C_b(b,0)=T_{b+1}\). The rank and width counts in
Sections 2--4 of the first note are therefore proof-safe.

## 2. The positive-prefix seam path is cut

For every mountain state \(A_c\), the forced selected old edge is

\[
                  U_{gA_c}\longrightarrow U_{A_c}.         \tag{2.1}
\]

The height-\(c-1\) pentagon deletes (2.1) and replaces it by

\[
                  U_{A_{c-1}}\longrightarrow U_{A_c}.      \tag{2.2}
\]

For \(u\ge1\), path (5.3) of the first audited note contains precisely the
old final edge (2.1):

\[
 U_{g^uA_c},\ldots,U_{gA_c},U_{A_c}.                      \tag{2.3}
\]

Showing that the interior states \(g^tA_c\) are not exchange-support
states does not retain (2.1), because that deleted incidence is indexed by
the endpoint state \(A_c=Z_{c-1}^1\). Thus the displayed path survives only
for \(u=0\).

In particular, the deductions of all \(C_b(u,0)\), the diagonals, and the
deep endpoint from (5.3)--(5.4) do not follow in the simultaneous ladder.
This also invalidates residual family (6.1) as a complete classification.

### 2.1 A valid monotone-window replacement

There is nevertheless a simple literal repair for most left rays. The
switched connector contains the consecutive owner path

\[
 U_{A_\ell},U_{A_{\ell+1}},\ldots,U_{A_b}.
\]

Since

\[
 \bigcap_{j=\ell}^{b}A_j=[1,\ell]\mathbin{\dot\cup}T_b,   \tag{2.4}
\]

choosing \(\ell=b-u-1\) gives target \(C_b(u,0)\) at exactly \(u+1\)
edges whenever

\[
                         0\le u\le b-3.                   \tag{2.5}
\]

This correction uses only new monotone seams, so it is genuinely
consecutive in the fully switched factor. It does not cover
\(u=b-2,b-1\) or the extra endpoint \(u=b\).

## 3. Exact stable scope of the E4 rail

The local E4 identities are correct. With

\[
 E_b=T_b\cup\{2b+2\},\quad
 G_b=[2,b]\cup E_b,\quad
 B_b=[2,b+1]\cup T_b,
\]

one has, for \(0\le s\le b-4\),

\[
 g^sG_b=[2,b-s]\cup[2b-s+1,2b]\cup E_b                 \tag{3.1}
\]

and hence

\[
 J_b(a)=\bigcap_{s=0}^{a}g^sG_b=[2,b-a]\cup E_b.         \tag{3.2}
\]

The normalized root used in this proof is

\[
 1^{s+3}0(10)^{r-b-2}00\,1^{b-s-1}0^{b-1}.              \tag{3.3}
\]

Therefore the stable statement requires

\[
                         b\le r-2,                        \tag{3.4}
\]

in addition to the displayed \(b\)-range. The case \(b=r-1\) is not
covered by (3.3). The transition reaching \(s=b-4\) is valid; the next
transition leaves the rail because the earlier peak wins the first-maximum
tie.

The right history

\[
 \bigcap_{t=1}^{v}g^{-t}A_b=[v+1,b+1]\cup T_b            \tag{3.5}
\]

is also correct. Thus the literal E4 path has complementary core
\([v+1,b-u-1]\cup T_b\) whenever

\[
 v\ge1,\quad u\le b-5,\quad u+v\le b-1.                  \tag{3.6}
\]

The last inequality may be \(b-1\), rather than \(b-2\): when equality
holds, the low intervals in (3.2) and (3.5) are disjoint and the core is
exactly \(T_b\) at the correct width. The original proof excluded this
diagonal only because the preceding, invalid seam theorem claimed it had
already been repaired.

The component-support avoidance argument is valid for the interior E4
histories in the stable range. For the positive side, the same coordinate
test must include \(s=0\) to ensure the incoming old edge ending at \(G_b\)
is retained; it does so for \(b\ge5\). On the negative side the central
new edge ends at \(B_b=g^{-1}A_b\), while the following old edges are
indexed by \(g^{-t}A_b\), \(t\ge2\), exactly the states excluded by the
census.

## 4. The finite-top quantifier

The forced cuts in a ladder with height pentagons
\(h=2,\ldots,H-1\) are the mountains
\(A_b\), \(b=3,\ldots,H\).
The auxiliary edge used to repair \(A_b\) lies in the height-\(b\)
pentagon. It is consequently present only for

\[
                         b\le H-1.                        \tag{4.1}
\]

At \(b=H\), none of the E4 paths in the second note has been planted.
Hence the claim that the total leave over the finite ladder is
\(3H+O(1)\) does not follow: before an independent terminal rail or
alternate-occurrence theorem, the top middle family contains

\[
 |\{(u,v):u,v\ge1,\ u+v\le H-1\}|
   ={(H-1)(H-2)\over2}                                   \tag{4.2}
\]

pairs, in addition to the left boundary terms not covered by Section 2.

Switching one more full height pentagon merely moves this boundary to the
new top. A valid closure may instead plant the terminal E4 path as an
independent protected path without installing its whole pentagon, but
that is an additional host theorem, not a consequence of the current
simultaneous PBBS switch.

## 5. Proof-safe residual with the presently verified paths

At a non-top stable height, combine:

1. right-ray regeneration, which covers \(u=0\);
2. the monotone height window (2.4), which covers \(v=0,u\le b-3\);
3. the E4 path, which covers \(v\ge1,u\le b-5\) throughout the full triangle.

The remaining correct-rank pairs are then exactly

\[
\begin{aligned}
 &(b-2,0),\ (b-1,0),\ (b,0),\\
 &(b-4,1),\ (b-4,2),\ (b-4,3),\\
 &(b-3,1),\ (b-3,2),\\
 &(b-2,1).
\end{aligned}                                             \tag{5.1}
\]

Thus there are nine, not three, boundary pairs per stable non-top height.
Their values still lie in finitely many nested height chains, so this
correction does not restore a quadratic bulk obstruction away from the
top. It does require more than the three target rails in the third note.

## 6. The proposed protected bank checks the wrong palette

For adjacent rank-\(r\) complement states \(X,Y\), the physical owners are
\(U_X=[n]\setminus X\) and \(U_Y=[n]\setminus Y\). Their immediate lower
color is

\[
 U_X\cap U_Y=[n]\setminus(X\cup Y).                      \tag{6.1}
\]

Therefore simplicity of the alternating physical lift requires distinct
adjacent **unions** \(X\cup Y\), not distinct intersections \(X\cap Y\).

With the cap states in the third audited note,

\[
\begin{aligned}
 E\cup A_3&=A_3\cup A_4
            =\{1,2,3,4\}\cup T_3,\\
 F\cup A'_3&=A'_3\cup A'_4
            =\{0,2,3,4\}\cup T_3.                       \tag{6.2}
\end{aligned}
\]

Each alternating lift therefore revisits its first moving q1 vertex. The
displayed bank is not the asserted simple 2-bounded protected subgraph, so
the small protected-factor theorem cannot be applied to it.

### 6.1 A corrected two-rail bank for the three named chains

Keep

\[
 C=\{3,4,5\}\cup T_3,\qquad
 K=\{2,4,5\}\cup T_3,
\]

but replace

\[
\boxed{
 E^\star=\{2,3,5\}\cup T_3,\qquad
 F^\star=\{0,2,5\}\cup T_3.}                             \tag{6.3}
\]

Then

\[
 C-E^\star-A_3-\cdots-A_H,\qquad
 K-F^\star-A'_3-\cdots-A'_H                              \tag{6.4}
\]

are simple owner-disjoint Johnson paths. The target intersections are
unchanged:

\[
\begin{aligned}
 E^\star\cap\bigcap_{j=3}^{b}A_j
   &=\{2,3\}\cup T_b,\\
 C\cap E^\star\cap\bigcap_{j=3}^{b}A_j
   &=\{3\}\cup T_b,\\
 K\cap F^\star\cap\bigcap_{j=3}^{b}A'_j
   &=\{2\}\cup T_b.                                     \tag{6.5}
\end{aligned}
\]

The adjacent state unions on the first rail are

\[
 \{2,3,4,5\}\cup T_3,\quad
 \{1,2,3,5\}\cup T_3,\quad
 [1,b+1]\cup T_b\ (3\le b<H),                           \tag{6.6}
\]

and on the second rail they are

\[
 \{0,2,4,5\}\cup T_3,\quad
 \{0,2,3,5\}\cup T_3,\quad
 \{0\}\cup[2,b+1]\cup T_b\ (3\le b<H).                  \tag{6.7}
\]

They are pairwise distinct; the two rail families are separated by
coordinate zero. The owner sets are also disjoint. Hence the corrected
alternating incidence bank is simple and 2-bounded.

It has the same \(4H-4\) incidence edges. Therefore, under

\[
                         4H-4\le r-1,                    \tag{6.8}
\]

the small protected-factor theorem on \(ML_{r+1}\) does extend this
**corrected three-chain bank** to a spanning owner/q1 two-factor.

This repairs the abstract protected-host assertion for the three named
chains only. It does not repair the incomplete residual classification in
Section 5, the top boundary in Section 4, or any correlated
PBBS/upper/residence/cap requirement.

### 6.2 The six non-top target types fit on three corrected rails

Although (5.1) lists nine pairs, three of them have the same target and
width:

\[
 C_b(b-4,3)=C_b(b-3,2)=C_b(b-2,1)=T_b
\]

at width \(b\), which is also \(C_b(b-1,0)\).  Thus the nine pairs reduce
to the six target/width types

\[
\begin{array}{c|c}
\text{target}&\text{width}\\ \hline
\{2,3\}\cup T_b&b-2\\
\{3\}\cup T_b&b-1\\
\{2\}\cup T_b&b-1\\
\{1\}\cup T_b&b-1\\
T_b&b\\
T_{b+1}&b+1.
\end{array}                                               \tag{6.9}
\]

The first three are supplied by (6.4).  The last three admit one further
protected rail.  Choose four distinct even reservoir coordinates
\(\xi,\alpha,\beta,\gamma>H+1\), all at most \(2r\), and put

\[
\begin{aligned}
 D_b&=A_b-\{2\}+\{\xi\},\\
 S&=\{1,\xi,\alpha\}\cup T_3,\\
 R&=\{1,\alpha,\beta\}\cup T_3,\\
 Q&=\{\alpha,\beta,\gamma\}\cup T_3.
\end{aligned}                                             \tag{6.10}
\]

For \(H=O(\sqrt r)\), the required four even reservoir coordinates exist
for every sufficiently large \(r\).  The word

\[
 Q-R-S-D_3-D_4-\cdots-D_{H+1}                            \tag{6.11}
\]

is a simple Johnson path.  Its relevant intersections are

\[
\begin{aligned}
 R\cap S\cap\bigcap_{j=3}^{b}D_j
   &=\{1\}\cup T_b,\\
 Q\cap R\cap S\cap\bigcap_{j=3}^{b}D_j
   &=T_b,\\
 Q\cap R\cap S\cap\bigcap_{j=3}^{b+1}D_j
   &=T_{b+1}.
\end{aligned}                                             \tag{6.12}
\]

The corresponding owner counts are \(b,b+1,b+2\), giving exactly the
three widths in (6.9).

Every state in (6.11) omits coordinate 2.  Every adjacent union in the
two corrected rails (6.4) contains coordinate 2, so cross-rail q1
collisions are impossible.  Within the third rail the cap unions are

\[
\begin{aligned}
 Q\cup R&=\{1,\alpha,\beta,\gamma\}\cup T_3,\\
 R\cup S&=\{1,\xi,\alpha,\beta\}\cup T_3,\\
 S\cup D_3&=\{1,3,\xi,\alpha\}\cup T_3,
\end{aligned}                                             \tag{6.13}
\]

and the moving unions are

\[
 D_b\cup D_{b+1}
  =([1,b+1]-\{2\})\cup\{\xi\}\cup T_b.                   \tag{6.14}
\]

They are pairwise distinct.  Owner sets are also disjoint across all
three rails.  The complete three-rail bank therefore is simple and
2-bounded.

The first two rails have \(H-1\) Johnson edges each, and the third has
\(H+1\), for \(3H-1\) Johnson edges or \(6H-2\) incidence edges.  Hence
the small protected-factor theorem embeds all six chains whenever

\[
                         6H-2\le r-1.                    \tag{6.15}
\]

This closes the abstract owner/q1 host for every non-top boundary type in
(5.1).  It still does not supply the missing terminal E4 rail needed
before the top family reduces to those six types.

## 7. Revised frontier

The proof-safe state is:

* exact old mountain fan: proved;
* right-ray transport: proved;
* non-top E4 rail in the stable range: proved;
* most left rays by monotone height windows: proved;
* nine boundary types per stable non-top height: explicit;
* terminal top closure: open;
* corrected three-rail host for all six distinct types represented by the
  nine pairs in (5.1): proved at the abstract owner/q1 level;
* one correlated host containing the PBBS ladder, terminal rail, all
  residual rails, residence data, upper decoration, and typed cap: open.

Accordingly, none of the three audited notes presently closes the complete
forced-edge upper fan. Their literal calculations still reduce the
interior problem to finitely many height-chain interfaces; the remaining
unbounded issue is the terminal top quantifier plus correlated planting.
