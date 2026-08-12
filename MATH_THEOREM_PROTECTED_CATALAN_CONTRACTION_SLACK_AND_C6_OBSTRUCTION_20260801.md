# Protected Catalan contraction: exact Rado cuts, sharp SBE slack, and the six-cycle obstruction

**Date:** 2026-08-01  
**Status:** exact general contraction identities and a sharp obstruction to
deducing protected extension from strict balanced expansion alone.  This does
not disprove extension of the specific Boolean reset path; it identifies the
extra robust-surplus statement that path must satisfy.

## 0. Outcome

Let `P` be the phase-common protected link path supplied by the opened
complete-reversal packet.  It has

\[
                         h=4d+1
\]

graphic-independent links, distinct immediate-upper colours, and a common
literal contraction in the two phases.  The protected Catalan problem has
two exact stages already isolated in the current handoff:

1. choose one residual occurrence of each unprotected upper colour in the
   matroid contracted by `P`;
2. after the resulting Catalan forest is fixed, choose one terminal/connector
   atom for each residual component destination in a second contracted
   matroid.

The exact conditions are Rado rank inequalities in the two contracted
matroids.  The new point of this note is what strict balanced expansion says
about those contractions.

If a rank-`C` matroid on `N` atoms has the balanced density

\[
                         \rho={C\over N},
\]

then contracting an independent protected bank of order `h` leaves the
unconditional rank bound

\[
 r_{M/P}(X)\ge \rho |X|-(1-\rho)h.                    \tag{0.1}
\]

For two such matroids, a common basis containing `P` can consequently fail
by at most

\[
                         \lfloor(1-\rho)h\rfloor       \tag{0.2}
\]

atoms.  This loss is sharp: two partition matroids on the six-cycle have the
exact uniform common-base distribution, yet a two-edge common-independent
protected bank has no common-base extension and attains equality in (0.2).

Therefore SBE by itself does **not** prove that the `4d+1`-edge protected
packet extends.  Since in the Catalan application `rho=Theta(1/m)`, its
generic guarantee is only an `O(d)` residual defect.  Exact protected
extension requires either the robust contracted surplus in Theorem 2.1
below or the private/aligned Rado host already formulated in the nonlexical
host theorem.

## 1. The two exact protected Rado stages

Let `P_0` be a prescribed upper-rainbow directed forest.  For each residual
upper colour `R`, let `E_R` be its prepared occurrence menu.  Let `N_0` be a
matroid which represents all remaining head, lower-colour, graphic, and
payload conditions on this prepared face, and suppose `P_0` is independent
in `N_0`.

Then a protected upper-exact Catalan forest exists on this represented face
if and only if

\[
 r_{N_0/P_0}\!\left(\bigcup_{R\in S}E_R\right)\ge |S|
 \qquad(S\subseteq U\setminus U(P_0)).                 \tag{1.1}
\]

This is Rado's theorem in the contraction `N_0/P_0`.

After a forest `Q_0` is fixed, let `D(Q_0)` be its component destinations,
let `F_D` be the prepared connector-terminal menu for destination `D`, and
let `P_1` be a prescribed connector bank independent in the represented
terminal matroid `N_1(Q_0)`.  The components admit the required terminal
assignment and connector tree exactly when

\[
 r_{N_1(Q_0)/P_1}\!\left(\bigcup_{D\in Y}F_D\right)\ge |Y|
 \quad
 (Y\subseteq D(Q_0)\setminus D(P_1)).                  \tag{1.2}
\]

The two stages remain jointly quantified:

\[
 \exists Q_0\text{ satisfying (1.1) such that (1.2) holds for every }Y.
                                                               \tag{1.3}
\]

Equations (1.1)--(1.3) are the exact positive protected-host criterion.
The phase-common reset contributes no second instance: both phases contract
the same undirected protected link path.

## 2. Exact loss of balanced rank density under contraction

Let `M` be a matroid of rank `C` on a ground set `E` of order `N`, and put

\[
                         \rho={C\over N}.
\]

Assume the balanced rank-density inequalities

\[
                         r_M(A)\ge\rho |A|
                         \qquad(A\subseteq E).          \tag{2.1}
\]

Equivalently, the constant vector `rho 1_E` lies in the base polytope of
`M`.  Let `P` be independent in `M`, with `|P|=h`, and put `E'=E\P`.

### Theorem 2.1 (contracted density and exact robust-surplus criterion)

For every `X subseteq E'`,

\[
 \boxed{
 r_{M/P}(X)=r_M(X\cup P)-h
       \ge \rho |X|-(1-\rho)h.}
                                                               \tag{2.2}
\]

Let

\[
 \rho_P={C-h\over N-h}
\]

be the balanced density of the contracted matroid.  Define the original
surplus above (2.1) along the protected bank by

\[
 \sigma_P(X)=r_M(X\cup P)-\rho(|X|+h).                 \tag{2.3}
\]

Then the balanced vector `rho_P 1_(E')` lies in `B(M/P)` if and only if

\[
 \boxed{
 \sigma_P(X)\ge
 (1-\rho)h\left(1-{|X|\over N-h}\right)
 \qquad(X\subseteq E').}                               \tag{2.4}
\]

#### Proof

The contraction rank identity gives the equality in (2.2), and applying
(2.1) to `X union P` gives its inequality.

The vector `rho_P 1_(E')` has the correct total mass `C-h`; it belongs to
the contracted base polytope exactly when

\[
 r_M(X\cup P)-h\ge\rho_P|X|
\]

for every `X`.  Substitute (2.3) and use

\[
 \rho-\rho_P={(1-\rho)h\over N-h}
\]

to obtain (2.4).  \(\square\)

Thus uncontracted SBE supplies nonnegative surplus, whereas protected SBE
requires the explicitly positive triangular surplus on the right of (2.4).
The demand is largest, `(1-rho)h`, at the empty residual set and decreases
linearly to zero on the full residual ground.

## 3. Exact common-base extension cut

Let `M_1,M_2` both have rank `C` on the same `N`-element ground, and assume
`P` is independent in both.  Edmonds' matroid-intersection theorem applied
after contraction gives the following exact criterion.

### Theorem 3.1 (protected common-basis cut)

The bank `P` extends to a common basis of `M_1,M_2` if and only if

\[
 \boxed{
 r_{M_1}(X\cup P)+r_{M_2}((E'\setminus X)\cup P)
       \ge C+h
 \quad(X\subseteq E').}                                \tag{3.1}
\]

If both matroids satisfy the balanced density (2.1), then their largest
common independent extension of `P` has order at least

\[
 C-h-\lfloor(1-\rho)h\rfloor                           \tag{3.2}
\]

outside `P`.  Equivalently, its deficiency from a common basis is at most
`floor((1-rho)h)`.

#### Proof

The contracted matroids have common rank target `C-h`.  Edmonds' criterion
is

\[
 r_{M_1/P}(X)+r_{M_2/P}(E'\setminus X)\ge C-h.
\]

Substitution of the two contraction rank identities gives (3.1).

The two applications of (2.1) have set-size sum

\[
 |X\cup P|+|(E'\setminus X)\cup P|=N+h.
\]

After subtracting `2h`, every contracted intersection cut is at least

\[
 C-h-(1-\rho)h.
\]

The min--max value is integral, giving (3.2). \(\square\)

For the reset seed `h=4d+1`, this gives only an `O(d)` unconditional
deficiency.  It cannot by itself prove an additive-constant word.

## 4. Sharp six-cycle obstruction

Let the common ground be the six edges of the bipartite cycle

\[
\begin{array}{lll}
 a=u_1v_1,&b=u_1v_2,&c=u_2v_2,\\
 d=u_2v_3,&e=u_3v_3,&f=u_3v_1.
\end{array}                                             \tag{4.1}
\]

Let `M_L` be the partition matroid imposing at most one edge at each `u_i`,
and `M_R` the partition matroid imposing at most one edge at each `v_j`.
Both have rank `C=3` on `N=6`, so `rho=1/2`.  The two common bases are

\[
                         \{a,c,e\},\qquad\{b,d,f\}.     \tag{4.2}
\]

Their uniform mixture has exact marginal `1/2` on every ground element.
Thus the same constant vector belongs to both base polytopes and even to the
common-base polytope.

Now protect

\[
                         P=\{a,d\}.                     \tag{4.3}
\]

The two edges are disjoint, so `P` is independent in both matroids, but no
common basis in (4.2) contains it.  More explicitly, take

\[
                         X=\{b,c\}.
\]

Then `X` uses only the already occupied left vertices `u_1,u_2`, while
`E'\setminus X={e,f}` uses only the already occupied right vertices
`v_3,v_1`.  Hence

\[
 r_{M_L/P}(X)+r_{M_R/P}(E'\setminus X)=0<C-h=1.        \tag{4.4}
\]

The maximum common extension has deficiency one, exactly

\[
                         (1-\rho)h=1.                  \tag{4.5}
\]

This proves that (3.2) is sharp and that uniform common-base marginals do
not imply positive cylinder probability for a prescribed independent bank.
In particular, an averaging/avoidance argument for the reset footprint
cannot be reversed into a containment argument.

The example is abstract.  It does not assert that the specific Boolean
`4d+1`-link path creates this cut; it proves that its special geometry must
be used to rule the cut out.

## 5. Consequence for the protected Catalan host

The phase-common packet has already closed these rows:

* its protected links are upper-rainbow and graphic-independent;
* their rooted tails extend to all immediate-upper colours;
* the two phases induce the same contraction.

The remaining positive statement can now be written without ambiguity.

### Robust protected-host criterion

Construct represented matroids `N_0,N_1(Q_0)` and prepared menus such that:

1. the protected bank is independent;
2. every first-stage residual upper family satisfies (1.1);
3. the selected `Q_0` makes every second-stage destination family satisfy
   (1.2);
4. the unprotected bulk carries the required residence and all-width OR
   payload represented in those matroids.

For an SBE-based proof of row 2, it is enough to verify the robust surplus
(2.4) on the relevant pulled-back strict matroid; ordinary SBE is not
enough.  Alternatively, the aligned/private construction of the existing
nonlexical Rado theorem proves (1.1) directly and bypasses balanced-density
contraction.

The exact frontier is therefore

\[
 \boxed{
 \text{prove robust SBE surplus for the Boolean reset path, or construct
 the aligned/private two-stage Rado host directly.}}
\]

No TU or laminar-intersection claim is involved.

