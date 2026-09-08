# Two-SCD diagonal seams: exact predecessor-root rigidity

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Audited conclusion

The forward-\(\rho\), bridge-one seam mechanism in Theorem 8.2 of
`MATH_THEOREM_N_GLOBAL_TWO_SCD_PROMOTION_SELECTOR_AND_HOLONOMY_GATE_20260726.md`
cannot occur on a nontrivial owner orbit.

The obstruction is stronger than owner/target neutrality. It is an exact
chronological rigidity statement:

> Fix the target full state and the source middle owner. Then every
> owner-changing bridge-one predecessor has the same lower root at every
> controlled depth.

Consequently, if two SCD states have the same owner but distinct
rank-\((m-q_0)\) roots, deleting one of them cannot be repaired by joining
the other directly to the deleted state's bridge-one successor.

In the notation

\[
 \rho=\mu_1^{-1}\mu_0,
 \qquad \mu_1(\rho T)=\mu_0(T),
\]

if

\[
 \omega_1(\rho T)\longrightarrow\omega_1(\rho^2T)
\]

is the first legal edge of a colour-one run, then

\[
 \omega_0(T)\longrightarrow\omega_1(\rho^2T)
\]

can be bridge-one only if \(T=\rho T\). A genuine cyclic
\(0\to1\) seam always has \(T\ne\rho T\), so every diagonal seam required
by that theorem is impossible.

This rules out every one-letter bypass which deletes one member of a
distinct-root duplicate-owner pair and redirects the other member into
the deleted state's exact owner-changing successor. This fork obstruction
is orientation-free. It does **not** rule out a different seam target, a
different deletion convention, or a multi-letter seam whose total toll is
proved separately to be \(o(W)\).

## 1. State convention and the universal lower FIFO law

Let a full radius-\(H\) state centered at an \(m\)-set \(X\) have deletion
queue

\[
 \alpha(v)=(\alpha_1(v),\ldots,\alpha_H(v)).
\]

For \(1\le q\le H\), its depth-\(q\) lower set is

\[
 L_q(v)=X\setminus\{\alpha_1(v),\ldots,\alpha_q(v)\}.
\tag{1.1}
\]

Suppose \(v\to w\) is a bridge-one arc with distinct owners \(X\) and
\(Y\). Necessarily

\[
 Y=X-a+b,
 \qquad a\in X,\quad b\notin X.
\tag{1.2}
\]

The exact bridge classification, in both the rotor and promotion cases,
gives

\[
 a=\alpha_1(v),
 \qquad
 \alpha_i(w)=\alpha_{i+1}(v)\quad(1\le i<H).
\tag{1.3}
\]

At the last position, \(\alpha_H(w)\) is the reserve element appended to
the source deletion queue. In particular, the target lower queue never
contains the newly inserted owner coordinate \(b\).

### Lemma 1.1 (exact depth-\(q\) root update)

For every \(1\le q\le H\), put

\[
 R=L_q(v),\qquad R'=L_q(w),\qquad c=\alpha_q(w).
\]

Then

\[
 \boxed{R'=R-c+b,\qquad b\in R'.}
\tag{1.4}
\]

#### Proof

If \(q<H\), (1.3) gives

\[
 R=X\setminus
 \{a,\alpha_1(w),\ldots,\alpha_{q-1}(w)\}.
\]

Using \(Y=X-a+b\) in (1.1),

\[
 \begin{aligned}
 R'
 &=Y\setminus\{\alpha_1(w),\ldots,\alpha_q(w)\}\\
 &=R-\alpha_q(w)+b.
 \end{aligned}
\]

If \(q=H\), the same calculation applies with
\(c=\alpha_H(w)\), the appended reserve. This reserve lies in \(R\),
whereas \(b\notin X\), and therefore \(b\in R'\). \(\square\)

Nothing in this proof uses the upper-cache alternative distinguishing a
rotor from a promotion. Thus (1.4) covers both owner-changing bridge-one
types.

## 2. The predecessor-root rigidity theorem

### Theorem 2.1 (unique predecessor root)

Fix integers \(H\ge q\ge1\), a target full state \(w\) with owner \(Y\),
and an \(m\)-set \(X\ne Y\). Suppose there exists a bridge-one arc from a
full state centered at \(X\) to \(w\). Write

\[
 Y=X-a+b
\]

with \(a=X\setminus Y\) and \(b=Y\setminus X\). If

\[
 R'=L_q(w),
\]

then the depth-\(q\) lower set of every such predecessor is forced to be

\[
 \boxed{R=R'-b+\alpha_q(w).}
\tag{2.1}
\]

In particular, two states centered at the same owner \(X\) but having
different depth-\(q\) lower sets cannot both have bridge-one arcs to the
same target state \(w\).

#### Proof

The elements \(b\), \(\alpha_q(w)\), and \(R'\) are determined by the
fixed pair \((X,w)\). Lemma 1.1 rearranges to (2.1). \(\square\)

The theorem asserts uniqueness of the predecessor **lower root**, not
necessarily uniqueness of its whole collar. The source upper cache can
have more than one inverse completion. That freedom cannot change (2.1).

## 3. First immediate obstruction: the forward colour-zero track

Let \(\mathscr D_0,\mathscr D_1\) be SCDs on the common root set

\[
 \mathcal R=\binom{[2m]}{m-q_0},
\]

with common active middle-owner image and bijections

\[
 \mu_c:\mathcal R\longrightarrow\Omega.
\]

Define

\[
 \rho=\mu_1^{-1}\mu_0.
\tag{3.1}
\]

For each colour \(c\), let \(\omega_c(T)\) be any full collar extending
the chain of \(\mathscr D_c\) through \(T\). Thus

\[
 L_{q_0}(\omega_c(T))=T,
 \qquad \operatorname{owner}(\omega_c(T))=\mu_c(T).
\tag{3.2}
\]

### Proposition 3.1 (no forward-\(\rho\) colour-zero edge)

If \(T\ne\rho T\), then no collar choices can make

\[
 \omega_0(T)\longrightarrow\omega_0(\rho T)
\tag{3.3}
\]

an owner-changing bridge-one arc.

#### Proof

Put

\[
 X=\mu_0(T),\qquad Y=\mu_0(\rho T).
\]

The injectivity of \(\mu_0\) and \(T\ne\rho T\) give \(X\ne Y\). If
(3.3) were bridge-one, write \(Y=X-a+b\). Lemma 1.1 at depth \(q_0\)
would imply

\[
 b\in L_{q_0}(\omega_0(\rho T))=\rho T.
\tag{3.4}
\]

On the other hand, (3.1) gives

\[
 \mu_1(\rho T)=\mu_0(T)=X.
\]

Since \(\rho T\) is a lower member of its colour-one SCD chain, it is
contained in that chain's middle owner:

\[
 \rho T\subset X.
\tag{3.5}
\]

But \(b=Y\setminus X\notin X\), contradicting (3.4)--(3.5). \(\square\)

Thus Condition 1 of the cited Theorem 8.2 is already incompatible with
any forward-\(\rho\) colour-zero run of length at least two on a
nontrivial orbit.

The colour-reversed companion is equally exact:

\[
 T\ne\rho T
 \quad\Longrightarrow\quad
 \omega_1(\rho T)\not\longrightarrow\omega_1(T).
\tag{3.6}
\]

Indeed, the proposed target root \(T\) lies in the source owner
\(\mu_1(\rho T)=\mu_0(T)\), whereas Lemma 1.1 says that an
owner-changing target root contains the newly inserted coordinate outside
that owner. Hence colour zero cannot move one step forward toward its
duplicate root, and colour one cannot move one step backward toward its
duplicate root. This is a directed, or chiral, owner-orbit constraint.

## 4. Decisive obstruction to the diagonal deletion seam

### Theorem 4.1 (duplicate-head fork obstruction)

Let \(T\in\mathcal R\). Assume

\[
 \omega_1(\rho T)\longrightarrow\omega_1(\rho^2T)
\tag{4.1}
\]

is a bridge-one arc. If

\[
 \omega_0(T)\longrightarrow\omega_1(\rho^2T)
\tag{4.2}
\]

is also a bridge-one arc, then

\[
 \boxed{T=\rho T.}
\tag{4.3}
\]

#### Proof

The two proposed predecessors in (4.1)--(4.2) have the same owner:

\[
 \operatorname{owner}(\omega_1(\rho T))
 =\mu_1(\rho T)
 =\mu_0(T)
 =\operatorname{owner}(\omega_0(T)).
\tag{4.4}
\]

They have depth-\(q_0\) lower sets \(\rho T\) and \(T\), respectively.
Their target is the same full state \(w=\omega_1(\rho^2T)\).

If \(T\ne\rho T\), then injectivity of \(\mu_0\) gives

\[
 \mu_0(T)\ne\mu_0(\rho T)
 =\mu_1(\rho^2T),
\]

so both arcs would be owner-changing. Theorem 2.1 applied at depth
\(q_0\) says that their predecessor lower sets must coincide. Hence
\(T=\rho T\), a contradiction. Therefore (4.2) can coexist with (4.1)
only in the fixed-point case (4.3). \(\square\)

### Corollary 4.2 (Theorem-8.2 seam hypothesis is empty)

Let \(z\) be a cyclic binary selector on a \(\rho\)-orbit. Suppose
\(z(T)=0\), \(z(\rho T)=1\), the colour-one run has length at least two,
and its first directed run edge is (4.1). Then the replacement diagonal
(4.2) is not bridge-one.

#### Proof

A genuine \(0\to1\) transition on a cyclic orbit implies
\(T\ne\rho T\). Apply Theorem 4.1. \(\square\)

Therefore the number \(a\) of \(0\to1\) seams in Theorem 8.2 must be zero
whenever all its stated bridge-one diagonal conditions hold. What remains
is only the constant-colour-orbit case; the proposed pair-of-SCD seam
mechanism supplies no fusion across colours.

## 5. Orientation, rotor, and scope audit

1. **The fork obstruction is orientation-free.** Whenever one deletes a
   state and redirects its distinct-root owner duplicate into the same
   owner-changing successor, Theorem 2.1 forbids the redirect. Merely
   reversing \(\rho\) does not repair that bypass. An independently
   redesigned ladder may still choose a different post-seam target; that
   broader possibility is not classified here. Proposition 3.1 and
   (3.6) also show the chiral same-colour restrictions in the two orbit
   directions.

2. **Rotor cases are included.** Rotor and promotion bridge-one arcs have
   different upper-cache updates but the identical lower FIFO update
   (1.3). No owner-changing rotor exception exists.

3. **Owner-preserving bridge types are irrelevant off fixed points.**
   Identity and the owner-preserving singleton promotions are not covered
   by Theorem 2.1. At a nonfixed seam they cannot apply, because the target
   owner is
   \(\mu_1(\rho^2T)=\mu_0(\rho T)\ne\mu_0(T)\).

4. **The fixed-point conclusion is only necessary.** If \(T=\rho T\),
   Theorem 4.1 gives no contradiction; it does not prove that a diagonal
   exists. Moreover, a cyclic selector has no genuine \(0\to1\) seam on
   a singleton orbit.

5. **All depths are exact.** The predecessor-root identity holds for
   every \(1\le q\le H\), including \(q=H\). The SCD application needs
   only \(q=q_0\), where the lower set is the actual common root label,
   not an arbitrary collar extension.

6. **No multi-letter lower bound is claimed.** The argument forbids a
   direct bridge-one skip. It does not prove that every literal repair
   from \(\omega_0(T)\) to \(\omega_1(\rho^2T)\) costs \(\Omega(H)\), nor
   does it preclude routing through extra intermediate states. Such a
   repair would require its own disjointness and total-cost ledger.

7. **Meaning of “arc” in Theorem 8.2.** If Condition 2 uses “legal arc”
   as shorthand for a bridge-one state arc, Corollary 4.2 directly makes
   every nontrivial seam impossible. If it permits a bridge of length
   \(d>1\), then the theorem's length proof must add the exact seam excess
   \(\sum_{m seams}(d-1)\) (and separately verify the shadows crossing
   those extra letters). The present theorem then supplies only
   \(d\ge2\), not an asymptotically fatal lower bound.

## 6. Exact boundary for the constant-one program

The all-depth holonomy equations may still be useful algebraically, but
they cannot turn duplicate-owner deletion into the one-letter physical
splice asserted in Theorem 8.2. A viable two-SCD construction must change
at least one of the following features:

* which duplicate-owner occurrence is deleted;
* the identity of the state following a colour seam;
* or the one-letter requirement, replacing it by a quantitatively audited
  short connector.

Changing orientation alone is insufficient if the new scheme still
redirects the retained duplicate into the deleted duplicate's exact next
state.

Absent one of these changes, the exact common-core/path atlas cannot be
assembled by the proposed diagonal ladder, regardless of how small the
provider holonomy exponents are.
