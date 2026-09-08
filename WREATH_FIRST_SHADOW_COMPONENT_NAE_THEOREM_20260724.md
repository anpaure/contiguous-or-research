# First-shadow component exchanges: exact NAE reduction and drift law

## 1. Setting and the elementary ledgers

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\frac Wn,\qquad N=\binom n{m-1}=\frac m{m+2}W,
\]

and assume (m\ge2).  For an unoriented cyclic order (C), let
\(\mathcal W_r(C)\) be its family of (n) cyclic (r)-intervals.  An
exact middle wreath factor is a family (F) of (B) cyclic orders whose
families \(\mathcal W_m(C)\) partition \(\binom{[n]}m\).

For (S\in\binom{[n]}{m-1}), write

\[
 \mu_F(S)=|\{C\in F:S\in\mathcal W_{m-1}(C)\}|,
 \qquad M(F)=|\{S:\mu_F(S)=0\}|.
\]

The exact slot and duplicate identities are

\[
 \sum_S\mu_F(S)=W,
 \qquad
 M(F)=\sum_S(\mu_F(S)-1)_+-(W-N),
 \qquad W-N=\frac{2W}{m+2}.                 \tag{1.1}
\]

There are two useful refinements.  Put

\[
 P(F)=\sum_S\binom{\mu_F(S)}2.
\]

No ((m-1))-interval repeats inside one cyclic order, so equivalently

\[
 P(F)=\sum_{\{C,D\}\in\binom F2}
       |\mathcal W_{m-1}(C)\cap\mathcal W_{m-1}(D)|. \tag{1.2}
\]

Since

\[
 \binom t2-(t-1)=\binom{t-1}2\qquad(t\ge1),
\]

we have the exact collision identity

\[
 \boxed{
 M(F)=P(F)-(W-N)
       -\sum_S\binom{(\mu_F(S)-1)_+}{2}.}           \tag{1.3}
\]

In particular,

\[
 M(F)\le P(F)-(W-N),                                \tag{1.4}
\]

with equality precisely when every first-shadow multiplicity is at most
two.

For every coordinate (x), one cyclic order has exactly (m-1) cyclic
((m-1))-intervals containing (x).  Hence

\[
 \sum_{S\ni x}\mu_F(S)=(m-1)B.                     \tag{1.5}
\]

Subtracting the incidence of the complete ((m-1))-layer gives

\[
 \boxed{
 \sum_{S\ni x}(\mu_F(S)-1)
   =\frac{2W(m-1)}{n(m+2)}.}                        \tag{1.6}
\]

Thus, if \(\mathcal H=\{S:\mu_F(S)=0\}\) and
\(e(S)=(\mu_F(S)-1)_+\), then

\[
 \sum_{S\ni x}e(S)-|\{S\in\mathcal H:x\in S\}|
   =\frac{2W(m-1)}{n(m+2)}.                         \tag{1.7}
\]

This is the exact signed one-design constraint on holes and duplicate
mass.

Finally, one occurrence of (S) has two boundary coordinates
\(a,b\notin S\); its two adjacent middle intervals are
\(S\cup\{a\}\) and \(S\cup\{b\}\).  Exact middle factorization implies
that the boundary pairs belonging to the occurrences of a fixed (S)
form a matching on \([n]\setminus S\).  Therefore

\[
 0\le\mu_F(S)\le\left\lfloor\frac{m+2}{2}\right\rfloor. \tag{1.8}
\]

Equations (1.1), (1.3), (1.6), and (1.8) are necessary for every proposed
first-shadow multiplicity vector.

## 2. Legal transposition-component exchanges

Fix a coordinate transposition \(\tau=(u\ v)\).  Form the bipartite
middle-incidence multigraph \(G_\tau(F)\):

* its left vertices are a copy of (F);
* its right vertices are a copy of \(\tau F\);
* every middle set (A\) gives an edge joining the unique left wreath and
  unique right wreath which contain (A).

Every vertex has degree (n), counting multiplicity.  If (K) is one
connected component, write (L_K\subseteq F) and
\(R_K\subseteq\tau F\) for its two sides.

### Lemma 2.1 (component equivariance)

For every component (K),

\[
 \boxed{R_K=\tau L_K.}                              \tag{2.1}
\]

Consequently, if

\[
 a_{K,r}=\sum_{C\in L_K}{\bf1}_{\mathcal W_r(C)},
\]

then the rank-(r) incidence vector on the right side of the component is
exactly

\[
 \boxed{a^{\rm right}_{K,r}=\tau a_{K,r}.}          \tag{2.2}
\]

#### Proof

Let (C) be a cyclic order.  Across its (n) cyclic middle intervals,
the total number of incidences with (u,v) is (2m=n-1).  Therefore not
every interval contains exactly one of (u,v).  Some middle interval
contains both or neither, is fixed setwise by \(\tau\), and belongs to
both \(\mathcal W_m(C)\) and \(\mathcal W_m(\tau C)\).  Hence the left
vertex (C) and right vertex \(\tau C\) lie in the same component.

Thus \(\tau L_K\subseteq R_K\).  A finite regular bipartite component has
the same number of vertices on its two sides, so equality holds.  Applying
\(\tau\) to every cyclic interval proves (2.2).  \(\square\)

For every choice \(\varepsilon_K\in\{0,1\}\), choose (L_K) when
\(\varepsilon_K=0\) and (R_K) when \(\varepsilon_K=1\).  The resulting
family

\[
 F_\varepsilon=
 \bigcup_K\bigl((1-\varepsilon_K)L_K
                    \cup\varepsilon_KR_K\bigr)       \tag{2.3}
\]

is again an exact middle wreath factor: the two sides of one component
cover the same middle masks, and distinct components have disjoint middle
supports.  These are therefore genuine factor-preserving exchanges, not
signed kernel moves.

At the first shadow, put

\[
 x_K(S)=(a_{K,m-1})_S.
\]

Lemma 2.1 gives the exact local update

\[
 \boxed{
 \mu_{F_\varepsilon}(S)=
 \sum_K\bigl((1-\varepsilon_K)x_K(S)
                +\varepsilon_Kx_K(\tau S)\bigr).}   \tag{2.4}
\]

In particular, every \(\tau\)-fixed target has its **multiplicity**, not
merely its support, unchanged by every component exchange.

The usual quadratic-energy variance gate also becomes targetwise.  For a
nonfixed pair \(p=\{S,\tau S\}\), put

\[
 d_{K,p}=x_K(S)-x_K(\tau S).
\]

Then

\[
 \|c-\tau c\|_2^2
   =2\sum_p\left(\sum_Kd_{K,p}\right)^2,\qquad
 \sum_K\|\tau a_K-a_K\|_2^2
   =2\sum_p\sum_Kd_{K,p}^2.                         \tag{2.5}
\]

Thus mean smoothing beats component noise exactly when the cross-component
correlations

\[
 \sum_p\sum_{K\ne L}d_{K,p}d_{L,p}
\]

are positive.  The component signs cannot be discarded from an energy
argument.

If \(G_\tau(F)\) is connected, there is only one component choice, so the
two resulting factors are \(F\) and \(\tau F\).  Their missing counts agree
at every rank.  Hence:

\[
 \boxed{\text{a connected transposition overlay admits no vertical
 improvement at all.}}                              \tag{2.6}
\]

Disconnectedness is therefore a necessary condition for a nontrivial
one-step transposition heat bath.

## 3. Exact NAE reduction of the missing-shadow objective

Partition \(\binom{[n]}{m-1}\) into orbits under \(\tau\).  Fixed orbits
are already handled by (2.4).  Let

\[
 p=\{S,T\},\qquad T=\tau S\ne S,
\]

be a two-element orbit, and abbreviate

\[
 x_K=x_K(S),\qquad y_K=x_K(T).
\]

Choosing the right side of (K) swaps the pair \((x_K,y_K)\).  There are
three cases.

1. If some (K) has (x_Ky_K>0), both (S,T) remain covered for every
   component choice.
2. If every (x_K=y_K=0), both targets remain holes.
3. Otherwise assume (x_Ky_K=0) for every (K), and let

   \[
    A_p=\{K:x_K+y_K>0\},\qquad h_p=|A_p|.
   \]

   Give (K\in A_p) a literal sign (b_{p,K}=0) when (x_K>0), and
   (b_{p,K}=1) when (y_K>0).  After the exchange, the positive
   occurrence in (K) is assigned to one of (S,T) according to the bit

   \[
                 b_{p,K}\oplus\varepsilon_K.         \tag{3.1}
   \]

   Both targets are covered exactly when these effective bits are not all
   equal.

Thus every unresolved transposition orbit is literally a not-all-equal
clause on the component variables.

### Theorem 3.1 (component-NAE identity)

Let (H_{\rm fix}\) be the number of \(\tau\)-fixed holes of (F), let
\(P_0\) be the set of nonfixed target pairs absent on both sides, and let
\(\mathcal Q\) consist of the remaining nonfixed pairs for which no
component has (x_Ky_K>0).  Then

\[
\boxed{
 M(F_\varepsilon)=H_{\rm fix}+2|P_0|
  +\sum_{p\in\mathcal Q}
    \left(
      {\bf1}\{b_{p,K}\oplus\varepsilon_K=0\ \forall K\in A_p\}
     +{\bf1}\{b_{p,K}\oplus\varepsilon_K=1\ \forall K\in A_p\}
    \right).}                                      \tag{3.2}
\]

For (h_p\ge1), exactly one of the two indicators can hold.  In
particular, an orbit with (h_p=1) always retains one hole, irrespective
of the multiplicity concentrated in that single component.

If the component choices are independent fair bits, then

\[
\boxed{
 \mathbb E M(F_\varepsilon)
 =H_{\rm fix}+2|P_0|+
   \sum_{p\in\mathcal Q}2^{1-h_p}.}                 \tag{3.3}
\]

Moreover, a deterministic choice attaining at most the right side of
(3.3) exists and is found by ordinary conditional expectation.

#### Proof

The three cases above prove (3.2) orbit by orbit.  For (h_p\ge1), each
of the two monochromatic assignments has probability (2^{-h_p}), giving
(3.3).  Exposing the component bits one at a time and retaining the value
with no larger conditional expectation proves the deterministic assertion.
\(\square\)

This is an exact legal-factor theorem.  No completion, factorability, or
rounding step follows it.

### Corollary 3.2 (simultaneous multidepth version)

Nothing in Lemma 2.1 or the orbit calculation used \(r=m-1\).  For every
rank \(r\), define

\[
 x_{K,r}(S)=|\{C\in L_K:S\in\mathcal W_r(C)\}|.
\]

Then

\[
 \mu_{F_\varepsilon,r}(S)=
 \sum_K\bigl((1-\varepsilon_K)x_{K,r}(S)
       +\varepsilon_Kx_{K,r}(\tau S)\bigr).          \tag{3.4}
\]

Consequently the missing targets at every rank reduce to NAE clauses on
the **same** component variables.  If \(\mathcal Q_r\), \(h_{p,r}\), and
the fixed/zero-pair terms are defined rank by rank, then a uniform random
component choice has

\[
 \mathbb E\sum_{r\in R}w_rM_r(F_\varepsilon)
 =\sum_{r\in R}w_r\left(
 H_{{\rm fix},r}+2|P_{0,r}|
 +\sum_{p\in\mathcal Q_r}2^{1-h_{p,r}}\right)        \tag{3.5}
\]

for arbitrary nonnegative weights \(w_r\).  Conditional expectation gives
one exact factor no worse than (3.5).  Thus a proposed multidepth component
switching proof is an explicit weighted Max-NAE problem; optimizing each
rank with unrelated component choices would be invalid.

## 4. Exact drift law from a given factor

Classify the nonfixed pairs according to their multiplicities in the
original factor.

* A **hole--duplicate pair** has multiplicities (0,t) with (t\ge2).
  Let (h_p) be the number of interaction components containing the
  occurrences of the duplicate colour.
* A **separated covered pair** has both multiplicities positive, but no
  component contains occurrences of both colours.  Again let (h_p) be
  its number of active components.

Hole--hole and hole--singleton pairs keep respectively two and one holes.
Covered pairs with a bi-covered component keep zero holes.  Subtracting the
old defect from (3.3) therefore gives the exact expected drift

\[
\boxed{
 \mathbb E[M(F_\varepsilon)-M(F)]
 =\sum_{p\in\mathcal C_{\rm sep}}2^{1-h_p}
  -\sum_{p\in\mathcal H\mathcal D}
       \left(1-2^{1-h_p}\right).}                  \tag{4.1}
\]

The (h_p=1) terms in the second sum are zero.  Hence a transposition heat
bath has a certified strict descent whenever its scattered
hole--duplicate gain in (4.1) exceeds the separated-covered risk.  This is
the exact missing inequality; smoothing of the mean multiplicity vector
alone does not imply it.

There is also an exact deterministic floor.  A nonfixed pair can lose a
hole only when it is a hole--duplicate pair and the duplicate occurrences
meet at least two components.  Let (s_\tau(F)) be the number of such
**split** hole--duplicate pairs.  Then every component hybrid satisfies

\[
 \boxed{M(F_\varepsilon)\ge M(F)-s_\tau(F).}         \tag{4.2}
\]

Even this floor need not be attainable, because the resulting NAE clauses
may conflict.

## 5. Two averaging barriers and a quantitative target

### 5.1 Fixed holes

A transposition fixes an ((m-1))-set (S) setwise exactly when both
swapped coordinates lie in (S), or both lie outside it.  Therefore a
uniform random transposition fixes (S) with probability

\[
 p_{\rm fix}
 =\frac{\binom{m-1}{2}+\binom{m+2}{2}}{\binom n2}
 =\frac{m^2+2}{m(2m+1)}
 =\frac12+O(m^{-1}).                                \tag{5.1}
\]

Consequently

\[
 \mathbb E_\tau H_{\rm fix}=p_{\rm fix}M(F),         \tag{5.2}
\]

and every component hybrid for that \(\tau\) retains all of these holes.
On the positive side, some transposition has at most
\(p_{\rm fix}M(F)\) fixed holes.  On the negative side, one transposition
heat bath can never alter its fixed half of the hole family.

### 5.2 Independent-side averaging

Let (q=|\mathcal Q|).  Every active pair-component incidence consumes at
least one first-shadow occurrence on the left side, so

\[
 \sum_{p\in\mathcal Q}h_p\le W.                    \tag{5.3}
\]

Convexity of (2^{-x}) and (3.3) give

\[
 \sum_{p\in\mathcal Q}2^{1-h_p}
 \ge 2q\,2^{-W/q}.                                  \tag{5.4}
\]

Thus, if (q\ge cW) for a fixed (c>0), the independent component heat
bath has expected defect at least

\[
 2c\,2^{-1/c}W.                                     \tag{5.5}
\]

Accordingly, the fair-bit/conditional-expectation argument by itself can
certify (o(W)) first-shadow defect only after all but (o(W)) nonfixed
target pairs have become bi-covered inside one component (or have otherwise
left \(\mathcal Q\)).  A clever deterministic NAE assignment may do much
better than (3.3), but then a genuine Max-NAE structural theorem is needed;
plain averaging is insufficient.

### 5.3 Johnson-edge transport capacity

Let \(\mathcal H=\{S:\mu_F(S)=0\}\) and
\(\mathcal D=\{T:\mu_F(T)\ge2\}\).  A nonfixed transposition pair is an
edge of the Johnson graph (J(n,m-1)), and every Johnson edge corresponds
to one unique coordinate transposition.  Hence

\[
 \sum_\tau |\{\{S,T\}:S\in\mathcal H,
       T\in\mathcal D,\ T=\tau S\}|
 =e_{J(n,m-1)}(\mathcal H,\mathcal D).              \tag{5.6}
\]

Ignoring component concentration, the maximum possible one-step reduction
for \(\tau\) is no larger than the number of these hole--duplicate pairs.
With the legal component structure included, only the split pairs counted
by (s_\tau(F)) in (4.2) can actually help.  Therefore the next positive
theorem must supply both:

1. many Johnson-adjacent hole--duplicate pairs for some transposition; and
2. scattering of each useful duplicate colour across at least two
   interaction components, together with a low-conflict NAE assignment.

Neither conclusion follows from the exact slot count, the signed point
margins (1.6), or the spectral contraction of the averaged multiplicity
vector.

## 6. Relation to shortest alternating switches

For completeness, an alternating even cycle (Z) in the odd graph toggles
an ordinary spanning 2-factor.  At a touched middle vertex (X), let
\(h_X\) be its retained factor neighbour, (r_X) its removed neighbour,
and (a_X) its added neighbour.  The old and new first-shadow colours are

\[
 c_X^-=h_X\cap r_X,\qquad c_X^+=h_X\cap a_X.        \tag{6.1}
\]

If \(\rho_Z,\alpha_Z\) are their removal and addition histograms, then

\[
 \boxed{\mu_{F\triangle Z}=\mu_F-\rho_Z+\alpha_Z.}  \tag{6.2}
\]

Toggling preserves the exact wreath condition only with additional cycle
length constraints.  No alternating cycle of length below eight can do so.
At length eight it must cut two old wreaths twice each.  If the two cuts
split their vertex cycles into lengths (a,n-a) and (b,n-b), exactness is
equivalent to

\[
 \boxed{\{a,n-a\}=\{b,n-b\},}                      \tag{6.3}
\]

together with the reconnection producing two components rather than one.
These balanced two-wreath switches are the shortest local legal moves.
The component exchanges of Sections 2--5 are a different, generally
nonlocal, legal move class and expose the exact NAE structure hidden by a
mean-energy calculation.

## 7. Proved conclusion and open gate

The first-shadow optimization under a transposition component cube is not a
vague rounding problem.  It is exactly a Max-NAE instance with immutable
fixed targets, automatic bi-covered targets, locked one-component targets,
and clauses whose widths are the numbers of interaction components carrying
the corresponding occurrences.

The first currently unjustified step in a proposed transposition-diffusion
proof is therefore one of the following equivalent quantitative inputs:

* prove the negative drift inequality in (4.1) for some \(\tau\);
* prove that the resulting NAE instance has (o(W)) violated clauses; or
* prove a multistep version in which fixed holes and locked clauses shrink
  geometrically while no comparable family of separated-covered clauses is
  created.

Without such an input, averaging (F) with \(\tau F\), spectral smoothing
of the mean, and legal middle completion do not imply
\(M_1=o(W)\).
