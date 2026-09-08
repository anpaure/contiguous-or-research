# Two SCDs at the common-core gate: half-splice holonomy and exact diagonal-fork obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
\]

and use the tuned annular scales

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad H=\lfloor\sqrt{m\log m}\rfloor.
\tag{0.1}
\]

Thus

\[
 N_H=(1+o(1))\frac Wm,
 \qquad HN_H=o(W),
 \qquad N_H=o(W/H).
\tag{0.2}
\]

This note gives a positive algebraic theorem and a negative physical
theorem.

1. **Bounded provider holonomy is constructible.**  If one SCD admits a
   radius-preserving permutation of its chains whose central moves are
   lower-aligned, then splicing the old lower half of a chain to the
   middle owner and upper half of its successor produces a second full
   SCD.  Relative to the common lower-root indexing, its provider powers
   are exactly

   \[
      \phi_{q,-}=\rho^0,\qquad \phi_{q,+}=\rho.
   \tag{0.3}
   \]

   Hence all provider commutators vanish and the displacement bound is
   one at every depth.  This is the precise two-SCD form suggested by a
   common-core promotion path.

2. **The proposed duplicate-head diagonal is exactly impossible.**  For
   a bridge-one FIFO arc, fixing the target state and the source middle
   owner fixes the source lower root.  At a proposed \(0\to1\) seam, the
   deleted colour-one head and the colour-zero predecessor have the same
   middle owner but different lower roots.  Consequently they cannot
   both point by bridge-one arcs to the same next colour-one state.

   In the notation of the bounded-holonomy ladder,

   \[
   \omega _1(\rho T)\longrightarrow\omega _1(\rho ^2T)
   \quad\Longrightarrow\quad
   \omega _0(T)\not\longrightarrow\omega _1(\rho ^2T)
   \tag{0.4}
   \]

   whenever \(T\ne\rho T\).  Every genuine \(0\to1\) seam has
   \(T\ne\rho T\).  Thus Conditions 1 and 2 of the one-letter diagonal
   ladder in Theorem 8.2 of
   `MATH_THEOREM_N_GLOBAL_TWO_SCD_PROMOTION_SELECTOR_AND_HOLONOMY_GATE_20260726.md`
   are mutually inconsistent whenever the selector has a nontrivial
   colour run.

3. **A weaker reading collapses to one SCD.**  If the deleted head's old
   outgoing edge is exempted from the same-colour-run hypothesis, then a
   second exact invariant forbids two consecutive colour-zero states in
   the forward-\(\rho\) order.  Every zero is isolated.  If \(a\) is the
   number of \(0\to1\) seams and \(c\) the number of constant-orbit
   tracks, the selected annulus can be replaced by a pure colour-one path
   cover with

   \[
                             p_1\le 3a+c.
   \tag{0.5}
   \]

   Therefore \(a+c=O(N_H)\) already implies the desired component scale
   for one constituent SCD.  Sparse two-colour switching supplies no new
   escape.

4. **The obstruction is sharp in scope.**  For every
   \(2\le q_0<H\), an
   isolated diagonal satisfying all local root and common-core
   containments can exist if the old head-to-successor edge is discarded
   and the target collar is redesigned.  What is closed is the operation
   “delete one copy of a duplicate owner and redirect the other copy into
   the deleted copy's exact successor.”  Multi-letter connectors, a
   different target, or a genuinely rebuilt dominant one-SCD atlas remain
   outside the theorem.

Accordingly, the common-core/path-atlas lane has a definitive boundary.
The group/holonomy part has an exact solution conditional on a global
radius-preserving path factor, but that premise already contains the hard
physical factor.  The proposed one-letter diagonal does not repair the
missing closures.  A new seam must change the post-seam state or pay for
more than one physical edge.

## 1. SCD states and the lower FIFO law

Let \(\mathscr D\) be a full SCD of \(2^{[2m]}\).  A full
radius-\(H\) refinement of one of its middle states will be written

\[
 v=(X;\boldsymbol\alpha_v,\boldsymbol\beta_v),
 \qquad
 \boldsymbol\alpha_v=(\alpha_1(v),\ldots,\alpha_H(v)),
\tag{1.1}
\]

where \(X\in\binom{[2m]}m\) is the middle owner.  Its lower depth-\(q\)
state is

\[
 L_q(v)=X\setminus
 \{\alpha_1(v),\ldots,\alpha_q(v)\},
 \qquad 1\le q\le H.
\tag{1.2}
\]

Suppose \(v\to w\) is an owner-changing bridge-one arc in the audited
rotor/promotion normal form.  Write the target owner as

\[
 Y=X-a+b,
 \qquad a\in X,\quad b\notin X.
\tag{1.3}
\]

The lower FIFO rule is

\[
 a=\alpha_1(v),
 \qquad
 \alpha_i(w)=\alpha_{i+1}(v)\quad(1\le i<H),
\tag{1.4}
\]

with \(\alpha_H(w)\) the appended reserve coordinate.  This lower rule
is common to a promotion and a genuine rotor; their distinction is in the
upper cache.

### Lemma 1.1 (arrival belongs to the target root)

For every \(1\le q\le H\), put

\[
 R=L_q(v),\qquad R'=L_q(w),\qquad c=\alpha_q(w).
\]

Then

\[
 \boxed{R'=R-c+b.}
\tag{1.5}
\]

In particular,

\[
                         b\in R'.
\tag{1.6}
\]

#### Proof

For \(q<H\), equations (1.2)--(1.4) give

\[
 R=X\setminus
 \{a,\alpha_1(w),\ldots,\alpha_{q-1}(w)\}.
\]

Therefore

\[
 \begin{aligned}
 R'
 &=Y\setminus\{\alpha_1(w),\ldots,\alpha_q(w)\}\\
 &=(X-a+b)\setminus
   \{\alpha_1(w),\ldots,\alpha_q(w)\}\\
 &=R-\alpha_q(w)+b.
 \end{aligned}
\]

For \(q=H\), the identical calculation uses the appended reserve
\(c=\alpha_H(w)\).  Since the arrival \(b\) was outside \(X\), it is not
one of the target deletion coordinates and hence belongs to \(R'\).
\(\square\)

### Theorem 1.2 (predecessor-root rigidity)

Fix a target full state \(w\), with owner \(Y\) and lower depth-\(q\)
root \(R'=L_q(w)\).  Fix an adjacent source owner \(X\ne Y\), and write

\[
 Y=X-a+b,
 \qquad b=Y\setminus X.
\]

Every bridge-one predecessor of \(w\) centered at \(X\) has the same
depth-\(q\) lower root, namely

\[
 \boxed{R=R'-b+\alpha_q(w).}
\tag{1.7}
\]

Thus two states with the same middle owner and distinct depth-\(q\) roots
cannot both have bridge-one arcs into one fixed target state.

#### Proof

The target data determine \(R'\) and \(\alpha_q(w)\), while the ordered
pair of owners determines \(b\).  Rearranging (1.5) proves (1.7).
\(\square\)

The theorem fixes the predecessor root, not necessarily its whole upper
cache.  No upper-cache freedom can change (1.7).

## 2. Two SCDs on one active owner baseline

Let

\[
 \mathcal R=\binom{[2m]}{m-q_0}.
\tag{2.1}
\]

Let \(\mathscr D_0,\mathscr D_1\) be two SCDs whose chains through
\(\mathcal R\) have the same active middle-owner image \(\Omega\).  Write

\[
 \mu_c:\mathcal R\longrightarrow\Omega
\]

for the two owner bijections and define

\[
 \rho=\mu_1^{-1}\mu_0,
 \qquad
 \mu_1(\rho T)=\mu_0(T).
\tag{2.2}
\]

Let \(\omega_c(T)\) be any full collar extending the colour-\(c\) SCD
state through \(T\).  Hence

\[
 L_{q_0}(\omega_c(T))=T,
 \qquad
 \operatorname{owner}(\omega_c(T))=\mu_c(T).
\tag{2.3}
\]

### Proposition 2.1 (no forward-\(\rho\) colour-zero edge)

If \(T\ne\rho T\), there is no bridge-one arc

\[
                 \omega_0(T)\longrightarrow\omega_0(\rho T).
\tag{2.4}
\]

Symmetrically, there is no bridge-one arc

\[
                 \omega_1(\rho T)\longrightarrow\omega_1(T).
\tag{2.5}
\]

#### Proof

Put

\[
 X=\mu_0(T),\qquad Y=\mu_0(\rho T).
\]

The injectivity of \(\mu_0\) makes \(X\ne Y\).  If (2.4) were a bridge,
write \(Y=X-a+b\).  Lemma 1.1 at depth \(q_0\) would give

\[
 b\in L_{q_0}(\omega_0(\rho T))=\rho T.
\tag{2.6}
\]

But the owner identity (2.2) and the SCD containment give

\[
 \rho T\subset\mu_1(\rho T)=\mu_0(T)=X.
\tag{2.7}
\]

This contradicts \(b\notin X\).  The proof of (2.5) is the same with
the colours and direction reversed: the target root \(T\) is contained
in the source owner \(\mu_1(\rho T)=\mu_0(T)\), while a bridge target
root must contain the newly arrived coordinate outside that owner.
\(\square\)

This is a chiral obstruction.  In the forward-\(\rho\) order, colour zero
cannot form a run of length two.  In the backward order, colour one cannot
form a run of length two.

## 3. Exact failure of the duplicate-head diagonal

Consider a \(0\to1\) seam in the forward-\(\rho\) selector.  Put

\[
 v=\omega_0(T),
 \qquad u=\omega_1(\rho T),
 \qquad w=\omega_1(\rho^2T).
\tag{3.1}
\]

The owner identity says

\[
 \operatorname{owner}(v)
 =\mu_0(T)
 =\mu_1(\rho T)
 =\operatorname{owner}(u).
\tag{3.2}
\]

The proposed operation deletes \(u\), retains the rest of its colour-one
run beginning with \(w\), and asks for the diagonal \(v\to w\).

### Theorem 3.1 (duplicate-head fork obstruction)

Assume the first edge of the colour-one run is a bridge-one arc

\[
                            u\longrightarrow w.
\tag{3.3}
\]

If \(T\ne\rho T\), then

\[
                            v\not\longrightarrow w
\tag{3.4}
\]

by any bridge-one rotor or promotion, for every choice of nonnative collar
extensions.

#### Proof

The two prospective predecessors \(u,v\) have the same source owner by
(3.2).  Their depth-\(q_0\) lower roots are respectively \(\rho T\) and
\(T\), which are distinct.  The fixed target is \(w\).  Theorem 1.2 says
that every bridge-one predecessor of \(w\) with this source owner has one
unique depth-\(q_0\) root.  Hence (3.3) and (3.4) cannot both hold.
\(\square\)

### Corollary 3.2 (the bounded-holonomy one-letter ladder has no seams)

Suppose the hypotheses of Theorem 8.2 in the preceding two-SCD report are
read literally:

1. every selected same-colour run, before duplicate-head deletion, has
   legal consecutive bridge-one edges; and
2. every colour-one run beginning at a \(0\to1\) seam has length at least
   two.

Then its number \(a\) of \(0\to1\) seams satisfies

\[
                              \boxed{a=0.}
\tag{3.5}
\]

#### Proof

At every \(0\to1\) seam, the selector bits at \(T\) and \(\rho T\)
differ, so \(T\ne\rho T\).  The length assumption makes \(\rho^2T\)
the next colour-one root.  The run hypothesis supplies (3.3), while the
diagonal hypothesis asks for (3.4), contradicting Theorem 3.1.
\(\square\)

Thus the positive implication in that earlier theorem remains valid only
as a conditional implication with an empty nontrivial hypothesis.  It
cannot be used as an existence route for the stated one-letter seam.

The fork theorem is orientation-free: reversing an orbit does not help if
one still deletes a state and redirects its duplicate-owner mate into the
deleted state's exact successor.  Reversal only exchanges which colour
is forbidden from having a same-colour run in Proposition 2.1.

## 4. Exact identities forced by an isolated diagonal

The fork obstruction does not say that one isolated diagonal between
otherwise redesigned collars is impossible.  The following identities
are useful for any attempted replacement.

Assume

\[
                 v=\omega_0(T)\longrightarrow
                 w=\omega_1(\rho^2T)
\tag{4.1}
\]

is a legal bridge-one promotion.  Assume

\[
                         1\le q=q_0<H.
\]

Put

\[
 X=\mu_0(T),qquad
 Y=\mu_1(\rho^2T)=\mu_0(\rho T),
\tag{4.2}
\]

and write

\[
 a=\alpha_1(v),qquad
 b=Y\setminus X=\beta_\ell(v),qquad
 c=\alpha_{q+1}(v).
\tag{4.3}
\]

For native upper targets to remain injective through depth \(q\), the
outer-slot theorem requires

\[
                              \ell>q.
\tag{4.4}
\]

The FIFO/cache formulas give

\[
 Y=X-a+b,
\tag{4.5}
\]

\[
 \boldsymbol\alpha_w
 =\bigl(\alpha_2(v),\ldots,\alpha_H(v),x\bigr),
 \qquad x\in L_H(v),
\tag{4.6}
\]

and

\[
 \boldsymbol\beta_w
 =\bigl(a,\boldsymbol\beta_v\setminus b\bigr),
\tag{4.7}
\]

with the unaffected cache entries retaining their order.  At the entrance
root,

\[
 \boxed{\rho^2T=T-c+b.}
\tag{4.8}
\]

Define the entrance insertion sets

\[
 A_c(R)=\mu_c(R)\setminus R
\]

and the native upper depth-\(q\) insertion sets \(B_c(R)\).  Direct
substitution gives

\[
 \boxed{A_1(\rho^2T)=A_0(T)-a+c,}
\tag{4.9}
\]

\[
 \boxed{B_1(\rho^2T)=B_0(T)-\beta_q(v)+a,}
\tag{4.10}
\]

and

\[
 \boxed{U_q(w)=U_q(v)-\beta_q(v)+b,}
 \qquad
 \boxed{U_H(w)=U_H(v).}
\tag{4.11}
\]

The intermediate root \(S=\rho T\) lies in both owners:

\[
 S\subset\mu_1(S)=X,
 \qquad
 S\subset\mu_0(S)=Y.
\tag{4.12}
\]

Since \(|S|=m-q\) and \(|X\cap Y|=m-1\), there is a
\((q-1)\)-set \(C\) such that

\[
 \boxed{X\setminus S=C\mathbin{\dot\cup}\{a\},
 \qquad
 Y\setminus S=C\mathbin{\dot\cup}\{b\}.}
\tag{4.13}
\]

For \(q=1\), (4.13) makes \(S=X-a\).  But the source root is also
\(T=X-a\), hence \(S=T\).  Therefore no nontrivial isolated diagonal of
this form exists at \(q=1\).

### Proposition 4.1 (local sharpness for \(2\le q<H\))

For every \(H\ge3\), \(2\le q<H\), and \(m\ge3H+1\), the set identities
(4.5)--(4.13) admit a local realization with three distinct roots

\[
                         T,\quad S,\quad T'.
\]

The realization may be chosen so that all displayed roots and owners
contain one prescribed \(2H\)-core.

#### Proof

Choose pairwise distinct coordinates and write

\[
 X=L\mathbin{\dot\cup}\{a_1,\ldots,a_H\},
 \qquad |L|=m-H,
\]

with \(b_1,\ldots,b_H\notin X\).  Take

\[
 a=a_1,qquad b=b_{q+1},qquad c=a_{q+1},
\]

and use the legal promotion normal form with outer slot \(\ell=q+1\).
Put

\[
 T=X\setminus\{a_1,\ldots,a_q\},
 \qquad
 T'=T-a_{q+1}+b.
\tag{4.14}
\]

Choose \(r\in L\), use \(x=r\) as the appended reserve in (4.6), and put

\[
 C=\{a_2,\ldots,a_{q-1},r\},
 \qquad
 S=X\setminus(\{a_1\}\cup C).
\tag{4.15}
\]

For \(q=2\), this means \(C=\{r\}\).  Then \(|C|=q-1\), the three
roots are distinct, and with

\[
 Y=X-a_1+b
\]

one has

\[
 S\subset X\cap Y,
 \qquad
 X\setminus S=C+a_1,
 \qquad
 Y\setminus S=C+b.
\]

Assign locally

\[
 \mu_0(T)=X=\mu_1(S),
 \qquad
 \mu_0(S)=Y=\mu_1(T').
\tag{4.16}
\]

The promotion gives the diagonal \(T\to T'\).  Finally choose the
common core inside \(L\setminus\{r\}\).  The inequality on \(m\) leaves at least \(2H\)
available coordinates.  This verifies local consistency; it does not
assert extension of (4.16) to two global SCDs. \(\square\)

Thus no support-only or common-core Hall cut can exclude an isolated
diagonal for \(q\ge2\).  The obstruction in Theorem 3.1 is the retained
predecessor history.

## 5. A tailored pair with provider powers \(0,1\)

The next theorem shows that the provider-holonomy part of the proposal is
not itself an obstruction.

Index the chains of a full SCD \(\mathscr D_0\) by \(i\).  If chain \(i\)
has radius \(r_i>0\), write it as

\[
 A_{i,r_i}\subset\cdots\subset A_{i,1}=R_i
 \subset X_i\subset
 B_{i,1}\subset\cdots\subset B_{i,r_i},
\tag{5.1}
\]

where \(|X_i|=m\).  Radius-zero chains are middle singletons.

### Theorem 5.1 (radius-preserving half-splice SCD)

Suppose \(P\) is a permutation of all SCD chains satisfying

\[
 r_{Pi}=r_i
\tag{5.2}
\]

and, whenever \(r_i>0\),

\[
                              R_i\subset X_{Pi}.
\tag{5.3}
\]

Then the chains

\[
 A_{i,r_i}\subset\cdots\subset R_i
 \subset X_{Pi}\subset
 B_{Pi,1}\subset\cdots\subset B_{Pi,r_i}
\tag{5.4}
\]

form a second full SCD \(\mathscr D_1\).  On radius-zero chains use the
singleton \(X_{Pi}\).

For every depth \(q\), restricted to the chains in \(I_q\), on the common
lower-root indexing,

\[
 \boxed{\phi_{q,-}=\operatorname{id},
 \qquad \phi_{q,+}=P^{-1}.}
\tag{5.5}
\]

The owner permutation is

\[
 \boxed{\rho=P^{-1}.}
\tag{5.6}
\]

Consequently

\[
 \boxed{\phi_{q,-}=\rho^0,
 \qquad \phi_{q,+}=\rho}
\tag{5.7}
\]

at every depth.

#### Proof

The two middle links in (5.4) are saturated containments: (5.3) gives
the lower link, and \(X_{Pi}\subset B_{Pi,1}\) gives the upper link.
Equation (5.2) makes the new chain symmetric.

As \(i\) varies, the old lower halves partition every rank below \(m\).
The middle owners \(X_{Pi}\) partition the middle rank because \(P\) is
a permutation.  The upper halves indexed by \(Pi\) partition every rank
above \(m\).  Hence (5.4) is a full SCD.

The lower target of the new chain indexed by \(i\) is the old lower
target of chain \(i\), proving \(\phi_{q,-}=\operatorname{id}\).  Its
upper target is the old upper target of chain \(Pi\); therefore the new
provider of the old upper target of \(i\) is chain \(P^{-1}i\), proving
the second identity in (5.5).

The new owner at lower-root index \(i\) is \(X_{Pi}\).  Hence the new
root providing old owner \(X_i\) is \(P^{-1}i\), which is (5.6).
Equation (5.7) follows. \(\square\)

If \(X_i\to X_{Pi}\) is a legal physical promotion, then (5.3) is
automatic: its departure is the unique element of \(X_i\setminus R_i\),
so the arrival owner is the opposite middle corner above \(R_i\).
Therefore a radius-preserving physical cycle factor on the SCD chains
produces a genuine tailored pair with provider displacement one.

It does not follow that such a factor exists.  Indeed, it is already a
global H-safe middle path/cycle factor of the kind Stage A is trying to
construct.

### Proposition 5.2 (exact radius-mismatch ledger)

Drop (5.2), and truncate (5.4) to radius

\[
                         \min(r_i,r_{Pi}).
\]

Let

\[
 I_q=\{i:r_i\ge q\}.
\]

The number of missing lower targets and the number of missing upper
targets at depth \(q\) are both

\[
 h_q=|I_q\setminus P^{-1}I_q|
 =\frac12|I_q\mathbin\triangle P^{-1}I_q|.
\tag{5.8}
\]

Moreover,

\[
 \boxed{
 \sum_{q\ge1}h_q
 =\frac12\sum_i|r_i-r_{Pi}|.}
\tag{5.9}
\]

Thus exact all-depth half-splice provider balance is equivalent to
pointwise radius preservation along \(P\).

#### Proof

At depth \(q\), the new chain indexed by \(i\) exists precisely when
both \(i\) and \(Pi\) lie in \(I_q\).  The represented index set is
therefore \(I_q\cap P^{-1}I_q\).  Since \(P\) is a permutation,
\(|I_q|=|P^{-1}I_q|\), proving (5.8).

For a fixed \(i\), the number of thresholds \(q\) at which exactly one
of \(r_i,r_{Pi}\) reaches \(q\) is \(|r_i-r_{Pi}|\).  Summing the
symmetric differences over \(q\) and using (5.8) proves (5.9).
\(\square\)

For the clipped annulus through depth \(H\), the corresponding exact
identity is

\[
 \boxed{
 \sum_{q=1}^{H}h_q
 =\frac12\sum_i
 \left|\min(r_i,H)-\min(r_{Pi},H)\right|.}
\tag{5.10}
\]

Thus clipped provider exactness requires only preservation of the clipped
radii \(\min(r_i,H)\).  Pointwise preservation of the full radii is
equivalent to exactness at every depth of the full SCD and is the
hypothesis needed for the untruncated half-splice (5.4).

This is the exact fixed-skeleton obstruction.  A more general upper-half
repair is a nested Hall problem and need not retain the clean provider
powers (5.7).

## 6. Why the common-core atlas does not complete the half-splice theorem

For one common-core top \(U\), the literal path theorem supplies an open
promotion path of

\[
                         L=m-3H+1
\]

middle phases.  Its middle omissions are consecutive \(H\)-windows of
one injective tail word.  Hence every internal physical edge gives the
lower alignment (5.3), and on every constant-radius cyclic subtrack the
half-splice theorem would give provider exponents \(0,1\).

Three global hypotheses are still absent.

1. The core-constrained clone Hall theorem assigns arbitrary distinct
   admissible \(H\)-omission sets.  It does not make them one tight path:

   \[
   J_{j+1}=J_j-w_j+w_{j+H}.
   \tag{6.1}
   \]

2. The separate signed-rank Hall matchings do not enforce the one-word
   interval identities

   \[
   I_{j,\ell}
   =\{w_{j+2H-\ell},\ldots,w_{j+2H-1}\}
   \qquad(1\le\ell\le2H)
   \tag{6.2}
   \]

   simultaneously on the same phases.

3. The literal common-core objects are open paths with arbitrary tag
   profiles.  They do not supply a radius-preserving successor
   permutation \(P\), nor exact cyclic closure.  Proposition 5.2 shows
   that radius mismatch is measured exactly by
   \(\frac12\sum_i|r_i-r_{Pi}|\).

Even if these three gates were solved, Theorem 3.1 would forbid using the
half-splice pair in the proposed duplicate-head diagonal.  The deleted
head is the canonical predecessor of the retained target, so its
duplicate-owner mate has the wrong lower root.  The obstruction is
therefore chronological, not a failure of common-core containment or
provider commutation.

### 6.1 Exact bulk and tag arithmetic

The tag census itself can be packed at the correct component scale; it is
not the missing theorem.  Put

\[
 K=N_H,
 \qquad
 B=W-LK=(\Lambda-L)N_H.
\tag{6.3}
\]

The common-core calibration gives

\[
 B=\Theta(HN_H)=o(W),
\tag{6.4}
\]

but also

\[
 \frac{B}{W/H}=\Theta(H^2/m)=\Theta(\log m).
\tag{6.5}
\]

Thus the boundary mass is small in length but too large to open one
component per missing phase.

Let

\[
 c_d=N_d-N_{d+1}\quad(0\le d<H),
 \qquad c_H=N_H=K
\tag{6.6}
\]

be the clipped exact-radius census.  It sums to \(W\).  Every common-core
top permits at most one tag-\(H\) phase, and (6.6) requires exactly one on
each of the \(K\) paths.

### Lemma 6.1 (monochromatic-run tag packing)

After reserving one tag-\(H\) phase on each common-core path, one may tag
the remaining \(K(L-1)\) phases so that:

1. no lower tag \(d<H\) is used more than \(c_d\) times;
2. the unused lower-tag quota has total size exactly \(B\); and
3. the total number of constant-tag runs on all \(K\) paths is at most

   \[
                              2K+H.
   \tag{6.7}
   \]

#### Proof

The total lower-tag quota is

\[
 \sum_{d<H}c_d=W-K,
\]

whereas the available nonanchor phases have total size

\[
 K(L-1)=LK-K=(W-K)-B.
\]

Choose integers \(0\le b_d\le c_d\) with
\(\sum_{d<H}b_d=K(L-1)\); a greedy choice suffices.  Concatenate
\(b_0\) copies of tag zero, then \(b_1\) copies of tag one, and so on,
and cut this global word into \(K\) consecutive bins of length \(L-1\).
The number of monochromatic runs in the bins is at most the number of bins
plus the number of tag-block boundaries, hence at most \(K+H\).  Attach
one tag-\(H\) anchor to each bin.  This adds at most \(K\) runs.  The
unused quota is

\[
 \sum_{d<H}(c_d-b_d)=B.
\]

This proves all three assertions. \(\square\)

Consequently, once one globally owner/trace-simple tight path per top is
available **and the prescribed tags are realizable by the native nested
flags on those same phases**, the retained bulk may be cut into only
\(O(N_H)\) constant-radius physical runs.  Its hard-start toll is

\[
 O(HN_H)=o(W).
\tag{6.8}
\]

The \(K=N_H\) tag-\(H\) anchors may be treated as exceptional fixed
points for the half-splice permutation and omitted from the physical
bulk, since

\[
 K=o(W/H),\qquad HK=o(W).
\tag{6.9}
\]

Here \(B\) is only the numerical owner/tag deficit conditional on a full
tight-path fusion; no family of \(B\) actual boundary chains has yet been
constructed.  Equation (6.5) says that this residual quota cannot simply
be realized as one separate component per unit.  A sufficient completion
would pack it into \(O(B/H)=O(N_H)\) coherent runs.

There is also no hidden short-run problem in the bulk tag assignment.
Place each tag-\(H\) anchor at an endpoint of its path.  A bin from the
proof of Lemma 6.1 is nonmonochromatic only if it contains one of the at
most \(H-1\) lower-tag block boundaries.  Declare those at most \(H-1\)
bins exceptional.  Their total mass is

\[
 O(HL)=O(Hm)=o(W/H).
\tag{6.10}
\]

Every remaining nonanchor run has length exactly \(L-1\ge H-1\) for all
sufficiently large \(m\).  Thus, conditional on the missing global
owner/trace-simple tight paths, all but a polynomial exceptional family
already have the length needed for one-seam stateful closure.

### 6.2 The sharp stateful endpoint closure

Suppose, conditionally, that the bulk has already been partitioned into
same-radius legal H-safe promotion paths, each with at least \(H-1\)
internal transitions.  Treat radius-zero chains as fixed singleton
exceptions.  For each radius \(d\ge1\), form a
bipartite graph \(\mathcal B_d\) whose left shore is the set of tails and
whose right shore is the set of heads of the radius-\(d\) paths.  Join a
tail \(i\) to a head \(j\) exactly when

1. the central lower neighbour at the tail is contained in the head
   owner, as in (5.3);
2. the two endpoint collars obey the full bridge-one FIFO/cache equations
   for a promotion or genuine rotor; and
3. writing \(S(e)\) for the two-coordinate support of a transition, for
   every \(0\le r<H\) the seam support, the last \(r\) tail supports,
   and the first \(H-1-r\) head supports are pairwise disjoint.

### Proposition 6.2 (radius-stratified seam Hall criterion)

The given internal paths extend, without changing an internal edge, to a
radius-preserving H-safe successor permutation \(P\) if and only if

\[
 \boxed{
 |N_{\mathcal B_d}(\mathcal F)|\ge|\mathcal F|
 \quad\text{for every radius }d
 \text{ and every tail family }\mathcal F.}
\tag{6.11}
\]

When (6.11) holds, Theorem 5.1 produces the full tailored SCD pair with
provider powers \(0,1\), and the number of resulting owner cycles is at
most the number of input paths.

#### Proof

A radius-preserving completion pairs every tail bijectively to one head of
the same radius.  The three displayed edge conditions are precisely
central alignment, legal state chronology, and full H-history safety.
The length hypothesis ensures that an H-window crosses at most one new
seam.  Hence such a completion is exactly a perfect matching in each
\(\mathcal B_d\).  Hall's theorem gives (6.11).  Closing paths cannot
create more cycles than the number of open
paths, and Theorem 5.1 supplies the SCD pair. \(\square\)

No present common-core theorem proves (6.11).  More importantly for the
two-colour proposal, Theorem 3.1 proves that the specific duplicate-head
diagonal is not an edge of any \(\mathcal B_d\) when the old head edge is
retained.  Endpoint closure therefore requires a different stateful seam,
not a re-interpretation of the same diagonal.

## 7. The weakened seam interpretation collapses to one SCD

One might weaken the same-colour-run condition by deleting the head first
and declining to require its old edge into the retained suffix.  Then
Theorem 3.1 no longer applies directly.  Proposition 2.1 still applies.

Use a cyclic binary selector \(z\) on every forward-\(\rho\) orbit.  Let
\(a\) be the total number of \(0\to1\) transitions, and let \(c\) be the
number of constant-orbit tracks which are retained as one path.

### Theorem 7.1 (one-SCD collapse)

Assume every retained colour-zero or colour-one run is a two-sided H-safe
bridge-one path, except that the outgoing edge of a deleted colour-one
head need not have existed.  Assume also that every retained
constant-orbit track is H-safe and has a one-component pure-colour
realization.  Then every zero on a nontrivial mixed \(\rho\)-orbit is
isolated.  Replacing the selection by all colour-one chains gives an
exact pure-\(\mathscr D_1\) annular path cover with

\[
                              \boxed{p_1\le3a+c.}
\tag{7.1}
\]

#### Proof

Two consecutive zeros would require the forbidden edge (2.4).  Hence
every zero is followed by a one, and on each mixed orbit the number of
zeros equals its number of \(0\to1\) transitions.

For each mixed colour-one run, retain the colour-one suffix beginning
after its deleted head.  This is at most one H-safe path component.  For the isolated
zero immediately preceding the run, add the colour-one chain at that
root as a singleton path.  Also add the deleted colour-one head as a
singleton path.  Thus one \(0\to1\) seam costs at most three pure
colour-one components.  A nontrivial constant-zero orbit is impossible
by Proposition 2.1 under the retained-edge hypothesis.  Thus a constant
track is either an H-safe all-one track or a \(\rho\)-fixed zero
singleton; replacing it by colour one costs at most its one stipulated
component.

Every root is now used exactly once in colour one.  Therefore the owner
and every native signed provider ledger are exactly those of
\(\mathscr D_1\), with no selector mismatch.  Summing the components
gives (7.1). \(\square\)

At the tuned scale, if

\[
                            a+c=O(N_H),
\tag{7.2}
\]

then

\[
 p_1=O(N_H)=o(W/H),
 \qquad
 2Hp_1=O(HN_H)=o(W).
\tag{7.3}
\]

Thus any weakened sparse-seam construction already proves the one-SCD
annular gate for \(\mathscr D_1\).  The second SCD is asymptotically
dispensable.

There is a useful quantitative corollary.  Let

\[
 M_x(\Omega)=|\{X\in\Omega:x\in X\}|.
\]

The frozen point-margin theorem applied to the pure colour-one path cover
gives

\[
 p_1\ge\frac1{2q_0^2}
 \sum_{x=1}^{2m}|2M_x(\Omega)-|\Omega||.
\tag{7.4}
\]

Combining (7.1) and (7.4),

\[
 \boxed{
 \sum_x|2M_x(\Omega)-|\Omega||
 \le2q_0^2(3a+c)
 \le6q_0^2(a+c).}
\tag{7.5}
\]

Hence a baseline with point skew at least \(\kappa W\) forces

\[
                         a+c\ge\frac{\kappa W}{6q_0^2}.
\tag{7.6}
\]

If, in addition, no within- or cross-orbit endpoint fusion is allowed and
the stipulated separate-reset compiler books the standard \(2H\) entries
at every hard start, then its **booked** collar charge is at least

\[
                         \frac{\kappa H}{3q_0^2}W.
\tag{7.7}
\]

For the canonical BTK active baseline, the proved skew lower bound allows
one to take

\[
 \kappa=\frac4{\sqrt\pi}+o(1)
 \quad\text{as a lower-bound coefficient},
 \qquad
 \frac H{q_0^2}=(1+o(1))\sqrt{\log m}.
\]

Thus that particular unfused separate-reset implementation books at least

\[
 \left(\frac4{3\sqrt\pi}+o(1)\right)
 W\sqrt{\log m},
\tag{7.8}
\]

entries.  This is not a lower bound on every literal OR compiler: a new
endpoint-fusion theorem could share collars and would need its own exact
seam ledger.  The numerical obstruction is scoped both to the stated
frozen-skew baseline and to the stipulated separate-reset implementation.
A point-balanced common-core baseline is not excluded by (7.8), but it is
still subject to the fork obstruction.

## 8. Final proved boundary

Proved exactly:

1. the arrival-in-root identity (1.5) for every bridge-one rotor or
   promotion;
2. uniqueness of the predecessor lower root for a fixed target state and
   source owner;
3. the chiral no-forward-colour-zero/no-backward-colour-one owner-orbit
   obstruction;
4. incompatibility of the old head edge and the proposed one-letter
   diagonal into its exact successor;
5. exact seam formulas (4.5)--(4.13), including impossibility at
   \(q_0=1\);
6. local consistency of an isolated redesigned diagonal for every
   \(2\le q_0<H\);
7. the full radius-preserving half-splice SCD theorem with provider
   exponents exactly \(0,1\);
8. the exact full and clipped radius-mismatch costs (5.9)--(5.10); and
9. under the H-safe retained-run and pure-constant-track hypotheses of
   Theorem 7.1, collapse of the weakened forward-\(\rho\) sparse-seam
   ladder to a pure constituent-SCD path cover with at most \(3a+c\)
   components.

Not proved, and not ruled out here:

1. a global radius-preserving H-safe successor permutation on a tailored
   SCD;
2. integral fusion of the common-core clone Hall assignment into one
   tight path per top;
3. simultaneous nesting of the separate signed-rank Hall matchings;
4. a seam which changes the post-seam target state;
5. a multi-letter connector with total target displacement and literal
   cost \(o(W)\); or
6. a genuinely one-SCD long factor with balanced point margins.

The old bounded-holonomy gate is therefore resolved as follows:

\[
 \boxed{
 \begin{array}{c}
 \text{provider powers }0,1\text{ are compatible with a tailored pair,}\\
 \text{but the duplicate-head one-letter diagonal is impossible;}\\
 \text{after weakening it, }O(N_H)\text{ switching collapses to one SCD.}
 \end{array}}
\tag{8.1}
\]

This obstruction is strictly stronger than component neutrality.  It
uses the ordered deletion queue and survives arbitrary upper-cache
choices and arbitrary nonnative collar extensions.
