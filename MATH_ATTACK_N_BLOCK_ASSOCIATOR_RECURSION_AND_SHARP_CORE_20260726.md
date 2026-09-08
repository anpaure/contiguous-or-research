# Lane N: block-associator recursion, exact first-column quotas, and the sharp invariant core

Date: 2026-07-26

Method: pure mathematics only.  No finite search, computation, solver, or
web input is used.

Write \(C_n=\operatorname {Cat}_n\), put

\[
 C(z)=\sum_{n\geq0}C_nz^n,
 \qquad C(z)=1+zC(z)^2,
\]

and let \(\mathcal D_s\) be the Dyck \(s\)-subsets of \([2s]\).

## 0. Outcome

There is an exact completed root-scale first matching which is strictly
more dispersive than the single transposition \((2\ 3)\).  Set

\[
 r=s-1,
 \qquad
 \eta_s=\prod_{i=1}^{r}(2i\ \ 2i+1),                 \tag{0.1}
\]

where the factors are disjoint, and let \(F_s\) be the canonical exact
\(\mathcal D_s\)-port factor.  Define

\[
                       G_s(P)=\eta_sF_s(\eta_sP).      \tag{0.2}
\]

The permutation \(\eta_s\) preserves \(\mathcal D_s\), so (0.2) is a
literal exact factor through every \(X\)- and \(Y\)-column and has the
correct complementary endpoint in every row.

The exact quota matrix of its first matching has a closed recursive
formula.  Define \(a_n\) by

\[
 A(z)=\sum_{n\geq0}a_nz^n
     ={1\over1-z(C(z)-1)}
     ={C(z)^2\over2C(z)-1}.                            \tag{0.3}
\]

Thus \(a_n\) is the number of Dyck words of semilength \(n\) having no
singleton primitive component \(10\).  If

\[
 M^{(s)}_{jk}
 =\#\{P:\text{the first-return class of }P\text{ is }j,
          \text{ and that of }\eta_sP\text{ is }k\},                \tag{0.4}
\]

then, for \(1\leq j<k\leq r\),

\[
\begin{aligned}
 M^{(s)}_{jk}
   &=a_{j-1}C_{k-j-1}C_{r-k+1},\\
 M^{(s)}_{js}
   &=a_{j-1}C_{r-j},\\
 M^{(s)}_{kj}&=M^{(s)}_{jk},\\
 M^{(s)}_{jj}&=0\quad(j\leq r),\\
 M^{(s)}_{ss}&=a_r.                                      \tag{0.5}
\end{aligned}
\]

On the cell indexed by \((j,k)\), the first inserted physical coordinate
of (0.2) is

\[
                         2k+1\quad(k\leq r),
             \qquad     2s\quad(k=s).                  \tag{0.6}
\]

Consequently (0.5) is the exact fibre-resolved first-insertion quota
matrix.  For every \(s\geq3\),

\[
 \boxed{\max_{j,k}M^{(s)}_{jk}=a_{s-1}.}                \tag{0.7}
\]

Moreover,

\[
 {a_n\over C_n}\longrightarrow {4\over9},
 \qquad
 {a_{s-1}\over C_s}\longrightarrow {1\over9}.         \tag{0.8}
\]

Thus this exact factor splits every canonical first-return fibre below a
hard cap \(p\) whenever

\[
                         p\geq a_{s-1}.                 \tag{0.9}
\]

In the normalization \(\theta=C_s/p\), its asymptotic range is
\(\theta\leq9-o(1)\).  This improves the one-transposition range
\(\theta\leq16/3-o(1)\).

There is a sharp qualification.  Let

\[
 H_s=\langle(2i\ \ 2i+1):1\leq i\leq s-1\rangle.       \tag{0.10}
\]

For every \(h\in H_s\), the conjugate factor \(hF_s(h\cdot)\) has at
least \(a_{s-1}\) rows simultaneously in the top first-return fibre and
at first target \(2s\).  The all-block choice (0.1) attains equality.
Hence (0.7) is optimal in the full adjacent-block conjugation grammar,
not merely for one selected conjugate.

The certified two-cut leaf rectangles do not escape this obstruction.
A rectangle placed after phase zero leaves the first matching unchanged;
a phase-zero rectangle has first-insertion labels among the first four
local coordinates (among the first five after an \(H_s\)-conjugation),
and hence never changes the \(2s\)-target rows when \(s\geq3\).  Any
support-disjoint family of the presently certified rectangles therefore
retains the same lower bound \(a_{s-1}\).

Finally, the \(2s\)-column has an exact recursive constraint in *every*
completed factor.  The \(C_{s-1}\) rows which insert \(2s\) first exhaust
all lower and upper states containing \(\{1,2s\}\).  Stripping this pair
and complementing produces a complete rank-\((s-1)\) complement-path
factor.  Therefore a proposed floor/ceiling selection of the roots assigned
to target \(2s\) is legal only if its facets form the port set of such a
rank-\((s-1)\) exact factor.  Cardinality quotas and ordinary first-column
Hall conditions do not see this recursive port constraint.

This is the precise boundary.  Exact floor/ceiling quotas are impossible
inside the adjacent-block-plus-certified-leaf-rectangle grammar once the
requested top/\(2s\) quota is below \(a_{s-1}\).  For unrestricted growing
root packets, the recursive port condition below is necessary but is not
proved sufficient.

## 1. The one-flaw middle word

Every \(P\in\mathcal D_s\) contains coordinate \(1\) and omits coordinate
\(2s\), so it has the unique form

\[
                              P=1E0,                    \tag{1.1}
\]

where \(E\) is a balanced \(0\)-\(1\) word of length \(2r\).  Give a
\(1\) step height \(+1\) and a \(0\) step height \(-1\).  The Dyck
condition on (1.1) is precisely

\[
             \text{every prefix height of }E\text{ is at least }-1.
                                                               \tag{1.2}
\]

Cut \(E\) into the consecutive two-letter blocks

\[
                 (E_1E_2),(E_3E_4),\ldots,(E_{2r-1}E_{2r}).     \tag{1.3}
\]

The height after every complete block is even.  By (1.2) it is therefore
nonnegative.

At a zero-height block boundary the next block can have one of three
forms:

* \(10\), a positive singleton atom, denoted \(+\);
* \(01\), a negative singleton atom, denoted \(-\); or
* the beginning \(11\) of a positive primitive Dyck word of semilength
  at least two.

The block \(00\) is impossible at height zero.  Cutting whenever the even
boundary height returns to zero gives a unique factorization of \(E\) into

\[
        +,\qquad -,\qquad
        \text{positive primitive Dyck atoms of semilength }\ell\geq2.
                                                               \tag{1.4}
\]

The generating function of the last type is

\[
 R(z)=\sum_{\ell\geq2}C_{\ell-1}z^\ell=z(C(z)-1).       \tag{1.5}
\]

Conversely, every sequence of atoms in (1.4) satisfies (1.2).  Hence the
generating function of all possible middle words is

\[
 {1\over1-2z-R(z)}=C(z)^2,                              \tag{1.6}
\]

where the last equality follows from

\[
 1-z(C(z)+1)=C(z)^{-2}.                                 \tag{1.7}
\]

The coefficient of \(z^r\) in (1.6) is \(C_{r+1}=C_s\), as required.

### Lemma 1.1 (first return from the atom word)

The first-return class of \(P=1E0\) is the semilength position of the
first \(-\) atom of \(E\).  If no \(-\) atom occurs, its class is \(s\).

#### Proof

An outer return before the final symbol means that the height of an odd
prefix of \(E\) is \(-1\).  At the preceding even block boundary the
height is even and nonnegative.  It can fall to \(-1\) in one step only
from height zero, and the corresponding block is \(01\).  The first such
block gives the first outer return.  If there is none, (1.1) remains
strictly positive until its final \(0\).  \(\square\)

## 2. The all-block involution and exact completion

The permutation \(\eta_s\) fixes the exterior symbols in (1.1) and
reverses every block in (1.3).  It preserves every even block-boundary
height.  A swapped mixed block can lower an intermediate height by two,
but at a positive even boundary that height is at least two; at height
zero it merely exchanges \(10\) and \(01\).  Thus condition (1.2) is
preserved.

### Lemma 2.1

The permutation \(\eta_s\) maps \(\mathcal D_s\) bijectively to itself.
On the atom decomposition (1.4), it exchanges \(+\) and \(-\), while it
maps every positive primitive atom of semilength at least two to another
positive primitive atom of the same semilength.

#### Proof

Even boundary heights, and hence the zero-boundary cuts, are unchanged.
At a zero boundary the two singleton blocks are exchanged.  A longer atom
has strictly positive internal even boundary heights.  Reversing a mixed
block there cannot make an intermediate height negative, so the image is
again positive and primitive.  Since \(\eta_s\) is an involution, the map
is bijective.  \(\square\)

Combining Lemmas 1.1 and 2.1 gives the key grammar rule:

\[
\begin{array}{c|c}
P&\eta_sP\\ \hline
\text{first-return class} &
\text{position of the first }+\text{ atom of }E,
\end{array}                                               \tag{2.1}
\]

with class \(s\) when the indicated atom is absent.

Now define every state of (0.2), not merely its first state, by

\[
\begin{aligned}
 X_t^{G_s}(P)&=\eta_sX_t^{F_s}(\eta_sP),\\
 Y_t^{G_s}(P)&=\eta_sY_t^{F_s}(\eta_sP).                \tag{2.2}
\end{aligned}
\]

### Theorem 2.2 (literal completed factor)

For every \(s\geq2\), (2.2) is an exact
\(\mathcal D_s\)-port complement-path factor.  In particular, every
first arc prescribed by (0.5)--(0.6) has a completion satisfying the full
\(X\)-ledger, the full \(Y\)-ledger, and rowwise complement monodromy.

#### Proof

Lemma 2.1 says that \(P\mapsto\eta_sP\) permutes the port labels.
Coordinate permutation preserves cardinality, containment, and Johnson
adjacency.  It also permutes each complete ownership shore.  At the two
endpoints,

\[
 X_0^{G_s}(P)=\eta_s(\eta_sP)=P,
 \qquad
 X_s^{G_s}(P)=\eta_s([2s]\setminus\eta_sP)=[2s]\setminus P.
\]

Thus every ownership and endpoint assertion follows from the corresponding
assertion for \(F_s\).  No residual Hall or cycle-closure assumption is
being made.  \(\square\)

If \(\eta_sP\) has first-return class \(k\), its canonical first inserted
coordinate is \(2k\).  Applying \(\eta_s\) sends this to \(2k+1\) for
\(k\leq r\), and fixes \(2s\).  This proves (0.6).

## 3. Exact recursive quota matrix

The atom sequences with no singleton atoms have generating function

\[
                       A(z)={1\over1-R(z)}.             \tag{3.1}
\]

This is (0.3).  Atom sequences allowing just one of the two signs have
generating function

\[
 {1\over1-z-R(z)}={1\over1-zC(z)}=C(z),                \tag{3.2}
\]

and arbitrary suffixes have generating function \(C(z)^2\), by (1.6).

### Theorem 3.1 (quota formula)

The matrix (0.4) is exactly (0.5).

#### Proof

Suppose first that \(1\leq j<k\leq r\).  By Lemma 1.1 and (2.1), the
atom sequence has the unique form

\[
 \underbrace{\mathcal R^*}_{j-1}\;-;
 \underbrace{(\mathcal R\cup\{-\})^*}_{k-j-1}\;+\;
 \underbrace{(\mathcal R\cup\{+,-\})^*}_{r-k},         \tag{3.3}
\]

where a subscript records total semilength and \(\mathcal R\) is the
family of positive primitive atoms of size at least two.  The three
coefficients are respectively

\[
                         a_{j-1},\qquad
                         C_{k-j-1},\qquad
                         C_{r-k+1}.                     \tag{3.4}
\]

Their product gives the first line of (0.5).  Exchanging \(+\) and \(-\)
proves symmetry.  Two different singleton signs cannot first occur at the
same atom, so the finite diagonal is zero.

If the original class is \(j\leq r\) and the image class is \(s\), there
is no \(+\) atom and the unique form is

\[
                    \mathcal R^*\;-\;
                    (\mathcal R\cup\{-\})^*.           \tag{3.5}
\]

The prefix and suffix counts are \(a_{j-1}\) and \(C_{r-j}\), giving
the second line.  If both classes are \(s\), there is no singleton atom
of either sign, giving \(a_r\).  \(\square\)

The row sum of (0.5) is automatically

\[
                         C_{j-1}C_{s-j},                \tag{3.6}
\]

because the row partitions the canonical first-return fibre
\(\mathcal F_{s,j}\).  Thus (0.5) gives exact integral quotas without a
rounding lemma.

## 4. Sharp maximum and constants

Concatenation of Dyck words gives, for nonnegative indices,

\[
                  C_{n_1}\cdots C_{n_t}leq
                  C_{n_1+\cdots+n_t}.                  \tag{4.1}
\]

Also \(a_n\leq C_n\).  Hence every finite off-diagonal cell in (0.5) is
at most \(C_{r-1}\), because its three indices sum to \(r-1\).  Every
top--finite cell has the same bound.

For \(r\geq2\), the injection

\[
             W\in\mathcal D_{r-1}\longmapsto1W0        \tag{4.2}
\]

lands among the no-singleton Dyck words of semilength \(r\).  Therefore

\[
                              C_{r-1}\leq a_r.          \tag{4.3}
\]

The top--top cell equals \(a_r\), proving (0.7).  The exceptional rank
\(s=2\) has maximum one and causes no asymptotic issue.

For the constant, write \(u=\sqrt{1-4z}\).  Since

\[
 C(z)={2\over1+u},
\]

(0.3) gives

\[
 A(z)={4\over(1+u)(3-u)}
     ={4\over3}-{8\over9}u+O(u^2),                    \tag{4.4}
\]

whereas

\[
 C(z)=2-2u+O(u^2).                                     \tag{4.5}
\]

The standard square-root coefficient extraction applied to (4.4)--(4.5)
gives

\[
                         {a_n\over C_n}\to
                         {(8/9)\over2}={4\over9}.       \tag{4.6}
\]

Finally \(C_{s-1}/C_s\to1/4\), proving the second limit in (0.8).

## 5. Optimality inside the adjacent-block grammar

For \(S\subseteq[r]\), let

\[
                         \eta_S=\prod_{i\in S}(2i\ \ 2i+1).    \tag{5.1}
\]

Let \(\mathcal A_r\) be the \(a_r\) Dyck words of semilength \(r\)
with no singleton primitive component.  Their even-boundary skeletons
have no zero-height mixed block.  Any \(\eta_S\) preserves the skeleton;
it only changes mixed-block orientations at positive height.  Thus

\[
                         \eta_S\mathcal A_r=\mathcal A_r.       \tag{5.2}
\]

### Theorem 5.1 (sharp common core)

For every \(S\subseteq[r]\), the conjugate factor

\[
                         G_{s,S}(P)=\eta_SF_s(\eta_SP)          \tag{5.3}
\]

has at least \(a_r\) rows in the cell

\[
          \{\text{initial first-return class }s,
             \text{ first inserted coordinate }2s\}.          \tag{5.4}
\]

Equality holds for \(S=[r]\).

#### Proof

For every \(E\in\mathcal A_r\), both \(1E0\) and
\(1\eta_SE0\) have class \(s\).  Since \(\eta_S\) fixes coordinate
\(2s\), the row rooted at \(1E0\) in (5.3) inserts \(2s\) first.  This
gives the lower bound.  For \(S=[r]\), a Dyck middle word containing a
singleton \(+\) has that first singleton changed into \(-\), and hence
leaves class \(s\).  Exactly \(\mathcal A_r\) remains, proving equality.
\(\square\)

Thus uniform floor/ceiling division of the forced \(2s\)-column among the
\(s\) canonical first-return fibres cannot be obtained from this grammar
once

\[
                         a_{s-1}>
                         \left\lceil{C_{s-1}\over s}\right\rceil.     \tag{5.5}
\]

In particular (5.5) holds for every \(s\geq5\), and asymptotically the
left side is a fixed \(4/9\) fraction of the column rather than \(1/s\).

### Proposition 5.2 (certified two-cut rectangles do not break the core)

Start with any factor (5.3), and perform any support-disjoint family of
the certified two-row, two-cut leaf rectangles in concatenation-aligned
contexts.  For \(s\geq3\), the cell (5.4) is unchanged.

#### Proof

A context rectangle whose slab starts after phase zero does not alter
\(P\to Y_0\to X_1\).  If the slab starts at phase zero, the displayed
rank-two rectangle changes only first-insertion labels in local
coordinates \(2,3,4\).  An \(H_s\)-conjugation can move these only within
\(\{2,3,4,5\}\), which excludes \(2s\) for \(s\geq3\).  Every other row
is untouched.  Disjointness permits the argument rectangle by rectangle.
\(\square\)

Proposition 5.2 is intentionally limited to the presently certified leaf
rectangle.  It does not exclude a new growing root packet whose first
edge genuinely enters or leaves target \(2s\).

## 6. The universal forced-core recursion

Let \(\mathscr H\) now be an arbitrary exact \(\mathcal D_s\)-port factor.  For
a row rooted at \(P\), let \(u_P(2s)\) be the insertion time of coordinate
\(2s\), and \(d_P(1)\) the deletion time of coordinate \(1\).

For one row, let \(N_X(P)\) and \(N_Y(P)\) be the numbers of its lower
and upper states containing \(\{1,2s\}\).  The pair is present in a lower
state exactly for times

\[
                         u_P(2s)\leq t<d_P(1),
\]

and hence

\[
                         N_X(P)=(d_P(1)-u_P(2s))_+.      \tag{6.1a}
\]

At the insertion or deletion transition, the intervening upper state
contains both coordinates.  It follows row by row that

\[
 N_Y(P)-N_X(P)=
 \mathbf 1_{\{u_P(2s)\leq d_P(1)\}}.                  \tag{6.1b}
\]

Exact lower- and upper-shore ownership for the coordinate pair
\(\{1,2s\}\) gives

\[
 \#\{P:u_P(2s)\leq d_P(1)\}=C_{s-1}.                  \tag{6.1}
\]

Indeed, (6.1) is the difference

\[
 \binom{2s-2}{s-1}-\binom{2s-2}{s-2}=C_{s-1}          \tag{6.2}
\]

between the numbers of upper and lower states containing the pair.
Furthermore exact lower-state ownership gives

\[
 \sum_P(d_P(1)-u_P(2s))_+
 =\binom{2s-2}{s-2}=(s-1)C_{s-1}.                    \tag{6.3}
\]

Every positive summand in (6.3) is at most \(s-1\), and there are at most
\(C_{s-1}\) rows which can contribute, by (6.1).  Equality therefore
forces all \(C_{s-1}\) candidate rows to contribute the maximum and hence

\[
                 u_P(2s)=1,\qquad d_P(1)=s             \tag{6.4}
\]

on all of them.  Denote this root set by \(\mathcal S\).  Thus

\[
                         |\mathcal S|=C_{s-1}.          \tag{6.5}
\]

Put \(I=[2,2s-1]\), so \(|I|=2r\).  For
\(P\in\mathcal S\), write

\[
                         E_P=P\setminus\{1\}\subset I.             \tag{6.6}
\]

Because of (6.4), every upper state in such a row contains
\(\{1,2s\}\), and every internal lower state does as well.  The counts are

\[
\begin{aligned}
 sC_{s-1}&=\binom{2r}{r},\\
 (s-1)C_{s-1}&=\binom{2r}{r-1}.                       \tag{6.7}
\end{aligned}
\]

These are exactly the numbers of all upper and lower states containing the
pair.  Hence the rows in \(\mathcal S\) exhaust those two induced shores.

Strip \(\{1,2s\}\) from their states.  If the original row is

\[
 X_0\subset Y_0\supset X_1\subset\cdots\subset Y_{s-1}\supset X_s,
\]

write

\[
 U_t=Y_t\setminus\{1,2s\}\quad(0\leq t\leq r),
 \qquad
 L_t=X_t\setminus\{1,2s\}\quad(1\leq t\leq r).       \tag{6.8}
\]

Then

\[
 U_0\supset L_1\subset U_1\supset\cdots\supset L_r\subset U_r,
 \qquad
 U_0=E_P,\quad U_r=I\setminus E_P.                    \tag{6.9}
\]

Complementing every state inside \(I\) turns (6.9) into a standard
rank-\(r\) complement path

\[
 Q_0\subset Z_0\supset Q_1\subset\cdots\subset Z_{r-1}\supset Q_r,
 \qquad
 Q_0=I\setminus E_P,\quad Q_r=E_P.                    \tag{6.10}
\]

### Theorem 6.1 (forced-core factor theorem)

For every exact \(\mathcal D_s\)-port factor, the rows which insert
\(2s\) first induce, by (6.8)--(6.10), an exact rank-\((s-1)\)
complement-path factor on \(I\), with port set

\[
              \mathcal Q=
              \{I\setminus(P\setminus\{1\}):P\in\mathcal S\}.       \tag{6.11}
\]

#### Proof

Equations (6.7) and exact ownership show that the stripped \(U\)-states
exhaust \(\binom Ir\) once and the stripped \(L\)-states exhaust
\(\binom I{r-1}\) once.  Complementation turns them into the two standard
middle shores \(\binom Ir\) and \(\binom I{r+1}\), preserving incidence.
Equation (6.10) gives the complementary endpoint pairing.  Hence the
result is an exact rank-\(r\) factor with precisely the port set (6.11).
\(\square\)

### Corollary 6.2 (root-refined quota obstruction)

Suppose a proposed first matching assigns target \(2s\) to a specified
root set \(\mathcal S_0\subseteq\mathcal D_s\).  If that first matching
extends to an exact factor, then necessarily

\[
 |\mathcal S_0|=C_{s-1}                                  \tag{6.12}
\]

and the family

\[
 \{I\setminus(P\setminus\{1\}):P\in\mathcal S_0\}       \tag{6.13}
\]

is the port set of an exact rank-\((s-1)\) complement-path factor.
In particular it is complement-free.  Equivalently, writing
\(\mathcal E_0=\{P\setminus\{1\}:P\in\mathcal S_0\}\),

\[
             \mathcal E_0\cap
             \{I\setminus E:E\in\mathcal E_0\}=\varnothing.          \tag{6.14}
\]

Indeed, if both \(Q\) and \(I\setminus Q\) were initial ports of the
lower-rank factor, then \(I\setminus Q\) would occur both as the terminal
state of the row rooted at \(Q\) and as an initial state, contradicting
exact ownership.

This is a genuine obstruction to a *root-refined* quota prescription:
failure of (6.13) rules out completion even when every scalar fibre count
and every first-column capacity is correct.  It is not, by itself, a new
inequality on the unrefined vector
\((|\mathcal S_0\cap\mathcal F_{s,j}|)_{j=1}^s\).  Nor is the converse
proved: a lower-rank factor with port set (6.13) need not lift together
with the complementary outer rows.

### Theorem 6.3 (inverse forced-core suspension)

Theorem 6.1 is reversible at the level of the saturated packet.  Let
\(\mathscr K\) be any exact rank-\(r\) complement-path factor on \(I\),
with port set \(\mathcal Q\).  Assume

\[
                     \{1\}\cup(I\setminus Q)\in\mathcal D_s
                     \qquad(Q\in\mathcal Q).                       \tag{6.15}
\]

Then \(\mathscr K\) lifts canonically to \(C_r\) pairwise disjoint
rank-\(s\) complement paths rooted at

\[
                     P_Q=\{1\}\cup(I\setminus Q),                  \tag{6.16}
\]

all of which insert \(2s\) first and delete \(1\) last.  These paths
exhaust exactly

* every rank-\(s\) upper state containing \(\{1,2s\}\); and
* every rank-\(s\) lower state containing \(\{1,2s\}\), together with
  the selected roots (6.16) and their complements.

#### Proof

Write a row of \(\mathscr K\) as

\[
 Q_0\subset Z_0\supset Q_1\subset\cdots
      \subset Z_{r-1}\supset Q_r,
 \qquad Q_r=I\setminus Q_0.                            \tag{6.17}
\]

Put

\[
 U_t=I\setminus Q_t\quad(0\leq t\leq r),
 \qquad
 L_{t+1}=I\setminus Z_t\quad(0\leq t<r).              \tag{6.18}
\]

Define the lifted row by

\[
\begin{aligned}
 X_0&=\{1\}\cup U_0,\\
 Y_t&=\{1,2s\}\cup U_t &&(0\leq t\leq r),\\
 X_t&=\{1,2s\}\cup L_t &&(1\leq t\leq r),\\
 X_{r+1}&=\{2s\}\cup U_r.                             \tag{6.19}
\end{aligned}
\]

Complementing the incidences in (6.17) gives every containment in
(6.19).  Since \(U_0=I\setminus Q_0\) and \(U_r=Q_0\), its endpoints
are (6.16) and its complement.  The first upper state adjoins \(2s\),
and the last transition deletes \(1\).

Exact ownership in \(\mathscr K\) says that the \(Q_t\)'s exhaust
\(\binom Ir\) and the \(Z_t\)'s exhaust \(\binom I{r+1}\).  Their
complements therefore make the \(U_t\)'s exhaust \(\binom Ir\) and the
\(L_t\)'s exhaust \(\binom I{r-1}\).  Formula (6.19) proves both palette
claims and pairwise disjointness.  Assumption (6.15) is exactly the outer
Dyck-port requirement.  \(\square\)

Thus (6.13) is necessary and sufficient for constructing the complete
*forced-core packet*.  It remains only necessary for constructing the
whole rank-\(s\) factor: the residual states avoiding simultaneous
\(\{1,2s\}\) still have their own Hall and marked-monodromy conditions.

Because every original root \(P\) is Dyck, its facet \(E_P\) satisfies
the one-flaw condition (1.2).  Thus a proposed set of \(C_{s-1}\) roots
for the forced target \(2s\) must satisfy two simultaneous requirements:

1. their facets lie in the one-flaw family (1.2); and
2. their complementary facets form the port set of an exact rank-
   \((s-1)\) factor.

This is a recursive palette-and-monodromy condition, not a scalar quota.
It is forced because \(\{1,2s\}\) is the unique coordinate pair with one
coordinate in every Dyck port and the other in none.  No other target
column yields the same saturated induced-shore factor by this argument.

## 7. Precise implication boundary

The following are proved.

1. The all-block associator (0.1) gives a literal completed exact factor.
2. Its fibre-resolved first quota matrix is exactly (0.5), with no
   unproved rounding or Hall step.
3. Its largest quota is exactly \(a_{s-1}\), asymptotic to \(C_s/9\).
4. The same number is the sharp unavoidable top/\(2s\) cell throughout
   the full adjacent-block conjugation grammar.
5. Support-disjoint certified two-cut leaf rectangles do not alter that
   cell.
6. In an arbitrary exact factor, the forced \(2s\)-column induces the
   exact lower-rank factor of Theorem 6.1.

What is not proved is equally important.

* Theorem 6.1 is necessary, not sufficient, for extending an arbitrary
  balanced choice of \(2s\)-roots to the whole rank-\(s\) factor.
* A genuinely growing root packet might change the lower-rank port set in
  (6.11) and break the \(a_{s-1}\) core.  No such clean packet is presently
  constructed or ruled out.
* Therefore this report does not prove coefficient one and does not give
  unrestricted floor/ceiling quotas.  It isolates the exact recursive
  condition that any such theorem must overcome.
