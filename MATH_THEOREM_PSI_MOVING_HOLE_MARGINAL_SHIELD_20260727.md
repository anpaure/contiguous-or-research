# The deterministic common-core collision gate: exact moving-hole audit and a coordinate-marginal shield

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{m-H},
\tag{0.1}
\]

and let

\[
 d=m-3H+1,\qquad K=W-dN.
\tag{0.2}
\]

Assume the packing calibration

\[
                         0\le K=o(W).
\tag{0.3}
\]

For an integer middle-load vector \(L=(L_D)_{D\in\binom{[2m]}m}\),
write

\[
 \Psi(L)=\sum_D\binom{L_D}{2},\qquad
 b_i(L)=\sum_{D\ni i}L_D.
\tag{0.4}
\]

This note audits the three-top/two-base conveyor, the two-, four-, and
eight-top moving-hole exchanges, and the catalysed six-frame
mixed-placeholder exchange against the deterministic common-core objective
\(\Psi\).  It proves the following.

1.  The three-top/two-base, two-top moving-hole, four-top moving-hole,
    and eight-top moving-hole exchanges have **zero middle-load
    derivative**.  They change configuration chronology at other ranks,
    but they cannot change \(\Psi\), singly or in composition.

2.  The catalysed six-frame exchange is the sole middle-nonneutral move in
    this list.  At the middle row its derivative is a sum of \(2H\)
    support-disjoint four-cell rectangles, has squared norm \(8H\), and,
    with its fixed closing catalyst and no exterior load, decreases
    \(\Psi\) by exactly \(2H\).  It embeds into the full all-core
    common-core path catalogue for all sufficiently large calibrated
    \(m\).

3.  Every such six-frame derivative preserves all coordinate marginals:

    \[
                          b_i(\Delta)=0\quad(1\le i\le2m).
    \tag{0.5}
    \]

    Consequently no composition of the audited moves can produce a unit
    Robin--Hood transfer \(e_X-e_Y\) between two distinct middle targets.

4.  This invariant supports a sharp nonlinear load-space obstruction.
    There is an explicit nonnegative integral vector \(L^\sharp\), of the
    exact common-core total mass \(dN\), such that

    \[
       \Psi(L^\sharp)=\binom{2m-2}{m-2}
                    =\left(\frac14+o(1)\right)W,
    \tag{0.6}
    \]

    yet \(L^\sharp\) is a global minimizer of \(\Psi\) on its entire
    integer fibre with fixed total mass and fixed coordinate marginals.
    Therefore every finite composition of the audited moves is
    nondecreasing at \(L^\sharp\).

The last vector is a genuine integral load state, but Section 4 proves that
it **cannot** be a coefficient of the common-core product polynomial: its
first two coordinate marginals violate an exact path-incidence cap.  Thus
(0.6) is not a counterexample to \(\min\Psi=o(W)\).  It is a rigorous
algebraic no-go for a descent theorem based only on total mass and collision
energy.  A physical no-go would require a high-energy shield satisfying the
common-core marginal caps; no such shield is proved here.

## 1. Exact quadratic derivative

For every integer vector \(\Delta\) with \(\sum_D\Delta_D=0\), direct
expansion gives

\[
 \boxed{
 \Psi(L+\Delta)-\Psi(L)
   =\langle L,\Delta\rangle+\frac12\|\Delta\|_2^2.}
\tag{1.1}
\]

This identity is valid whenever \(L+\Delta\) is nonnegative; the algebraic
identity itself needs no sign assumption.  The common-core floor energy is

\[
 \Phi_{\rm cc}(L)=\Psi(L)+K,
\tag{1.2}
\]

so \(\Phi_{\rm cc}\) and \(\Psi\) have exactly the same exchange
derivatives.

## 2. Middle-load audit of the exchange library

### Proposition 2.1 (the owner-preserving moves are \(\Psi\)-neutral)

At the middle row, each of the following exchanges has derivative zero:

1. the three-top/two-base full-frame conveyor, including its symmetric
   six-top realization;
2. the two-top moving-hole exchange;
3. the squarefree four-top moving-hole cube; and
4. the squarefree eight-top moving-hole cube.

Consequently each exchange preserves \(\Psi\) exactly in every ambient
state.

#### Proof

For the three-top conveyor, equation (2.5) of its theorem gives
\(\Delta_h=0\) for every \(h\le H\), in particular at \(h=H\).
Equivalently, its two shores have the identical squarefree middle support.
The symmetric six-top realization has the same endpoint derivative and
also states literal equality of its two middle supports.

For the two-top moving-hole exchange, equation (2.12) of its theorem is
literal equality of the complete retained middle-owner vectors.  The two
individual shores have \(H-1\) internal repeats, but that legality defect
does not alter the equality of their aggregate load vectors.

For the four-top cube, equation (3.1) gives equality of the punctured
core-only \(H\)-window families and equation (2.4) then gives middle
derivative zero.  Theorem 3.1 additionally proves that both shores are
squarefree.  The eight-top proof is identical in form: equation (2.9)
gives equality of the punctured \(H\)-window families and hence zero
middle derivative, while Theorem 3.2 supplies squarefreeness.

Since \(\Psi\) depends only on the middle-load vector, zero middle
derivative implies exact \(\Psi\)-neutrality in every ambient state.
\(\square\)

The positive-depth actions of these exchanges remain valid and useful for
the signed trace problem.  They simply do not act on the present middle
objective.

### Proposition 2.2 (exact catalysed six-frame derivative)

Use the notation of
`MATH_THEOREM_SIX_FRAME_MIXED_PLACEHOLDER_RECTANGLE_AND_MINIMALITY_20260726.md`.
At the middle row the six changed frames have derivative

\[
                       \Delta=d_w^H-d_z^H.
\tag{2.1}
\]

Under the separated-placeholder hypothesis, \(\Delta\) is the sum of
\(2H\) vectors with pairwise disjoint supports, each a context lift or a
global complement of

\[
 \eta=e_{\{x_5,z\}}-e_{\{x_0,z\}}
       +e_{\{x_0,w\}}-e_{\{x_5,w\}}.
\tag{2.2}
\]

In particular,

\[
                         \|\Delta\|_2^2=8H.
\tag{2.3}
\]

Keep the closing top \(V_z\) in its minus frame.  If \(L_{\rm old}\)
is the load of the six plus frames and this fixed catalyst, and
\(L_{\rm new}=L_{\rm old}+\Delta\) is the load after changing the six
frames, then

\[
                \Psi(L_{\rm new})-\Psi(L_{\rm old})=-2H.
\tag{2.4}
\]

More generally, if \(R\) is the load of every untouched path, then

\[
 \boxed{
 \Psi(R+L_{\rm new})-\Psi(R+L_{\rm old})
      =-2H+\langle R,\Delta\rangle.}
\tag{2.5}
\]

Thus the catalyst is essential and the compound move is a descent in a
global state precisely when \(\langle R,\Delta\rangle<2H\).

#### Proof

The phasewise telescope is equation (2.1) of the cited theorem.  At
root-complementary length \(H\), exactly the \(H\) intervals through
placeholder \(A\) and the \(H\) intervals through placeholder \(B\)
contribute.  Lemma 3.1 identifies each contribution with (2.2), up to
context lift, complementation, and sign.  The separated-placeholder
condition makes their supports disjoint.  Since \(\|\eta\|_2^2=4\),
equation (2.3) follows.

Proposition 5.3 of the cited theorem states more precisely that the old
seven-frame packet has exactly \(2H\) colliding unordered target pairs,
with no triple collision, while the new packet is pairwise disjoint.
This proves (2.4).  Adding the same exterior \(R\) to both endpoints and
using (1.1), or subtracting the two quadratic expansions directly, adds
exactly \(\langle R,\Delta\rangle\), proving (2.5). \(\square\)

### Lemma 2.3 (common-core suspension)

For all sufficiently large \(m\) in the calibrated regime \(H=o(m)\),
the seven paths in Proposition 2.2 may all be chosen as actual length-
\(d\) all-core common-core path options, with the same conclusions
(2.1)--(2.5).

#### Proof

It is enough to give the construction once \(M\ge12H+10\), which holds
eventually when \(H=o(m)\).  Choose a \(2H\)-set \(Q\subset C\), put its
labels consecutively in the cyclic positional word, and put every other
label in the complementary linear segment.  Place \(A,B,D\) in the
interior of that segment so that they are pairwise more than \(2H\)
apart and each is more than \(2H\) from both ends.  Fill the remaining
positions arbitrarily with \(C\setminus Q\).

For every one of the seven tops, use \(Q\) as its common core.  The
core-safe partial-ring theorem retains precisely

\[
 (M-2H)-2H+1=M-4H+1=d
\]

consecutive phases.  Swapping the labels at \(A,B\) does not change this
retained positional phase set.  Every length-\(H\) interval through
\(A\) or \(B\) is retained, and no such interval reaches \(D\) or the
core block.  Hence all \(2H\) nonzero rectangles in Proposition 2.2
survive the restriction.  Restricting decks cannot introduce a target
collision, while all \(2H\) collisions counted there occur on retained
phases.  Therefore the exact derivative, norm, collision count, and
energy formulas survive. \(\square\)

This lemma uses the full all-core catalogue.  It does not place the move
inside an independently preassigned core system or a fixed mechanical
atlas.

## 3. The coordinate-marginal invariant

### Lemma 3.1 (every six-frame rectangle is marginal-neutral)

For the middle derivative \(\Delta\) of Proposition 2.2,

\[
                         \sum_{D\ni i}\Delta_D=0
                         \qquad(1\le i\le2m).
\tag{3.1}
\]

The same holds after an arbitrary common phase restriction, under a
coordinate relabelling, and for every finite sum of such derivatives.

#### Proof

The four coefficients of \(\eta\) sum to zero.  At each of
\(x_0,x_5,z,w\), its two incident coefficients cancel, so its singleton
incidence vector is zero.  Adjoining a fixed context preserves this:
every context coordinate sees the total coefficient sum zero, and every
external coordinate sees its incidence in \(\eta\).  Global
complementation also preserves zero singleton incidence, because the
complementary incidence at coordinate \(i\) is the total coefficient
sum minus the original incidence at \(i\).  Summation, restriction, and
relabeling preserve the identity. \(\square\)

Let

\[
 \mathcal K=\left\{\Delta\in\mathbb Z^{\binom{[2m]}m}:
   \sum_D\Delta_D=0,
   \ \sum_{D\ni i}\Delta_D=0\ (1\le i\le2m)\right\}.
\tag{3.2}
\]

Every net middle derivative generated by the audited library lies in
\(\mathcal K\): Proposition 2.1 contributes zero, and Lemma 3.1 handles
the sole nonzero primitive.

### Corollary 3.2 (unit Robin--Hood transfers are impossible)

If \(X,Y\in\binom{[2m]}m\) are distinct, then

\[
                         e_X-e_Y\notin\mathcal K.
\tag{3.3}
\]

Hence no finite composition of the audited moves realizes a unit transfer
from one distinct target to another.

#### Proof

Choose \(i\in X\triangle Y\).  The coordinate-\(i\) marginal of
\(e_X-e_Y\) is \(+1\) or \(-1\), contradicting (3.2). \(\square\)

This obstruction survives the use of the middle-neutral gadgets as
configuration catalysts: they can make a later six-frame exchange legal,
but the net middle derivative of the whole sequence remains in
\(\mathcal K\).

## 4. A positive-density collision shield

### Theorem 4.1 (high-energy global minimum in a marginal fibre)

Assume (0.3).  For all sufficiently large \(m\), there is a nonnegative
integer load vector \(L^\sharp\) satisfying

\[
                         \sum_D L_D^\sharp=dN
\tag{4.1}
\]

and (0.6), such that for every \(\Delta\in\mathcal K\) with
\(L^\sharp+\Delta\ge0\) coordinatewise,

\[
                         \Psi(L^\sharp+\Delta)
                         \ge\Psi(L^\sharp).
\tag{4.2}
\]

#### Proof

Fix two coordinates, denoted \(1,2\).  The number of middle sets
containing exactly one of them is

\[
                         2\binom{2m-2}{m-1}
                         =\left(\frac12+o(1)\right)W.
\tag{4.3}
\]

Since \(K=o(W)\), choose a family

\[
 \mathcal H\subseteq
 \{D:|D\cap\{1,2\}|=1\},\qquad |\mathcal H|=K.
\tag{4.4}
\]

Define

\[
 L_D^\sharp={\bf1}_{\{1\in D\}}+{\bf1}_{\{2\in D\}}
                    -{\bf1}_{\{D\in\mathcal H\}}.
\tag{4.5}
\]

This is nonnegative.  Each coordinate belongs to exactly \(W/2\)
middle sets, so the first two terms in (4.5) have total mass \(W\).
Deleting the \(K\) selected unit occurrences proves (4.1).

The load is two exactly on the sets containing both \(1,2\), is zero or
one everywhere else, and \(\mathcal H\) meets only load-one cells before
the deletion.  Therefore

\[
 \Psi(L^\sharp)=\#\{D:1,2\in D\}
  =\binom{2m-2}{m-2}
  =\frac{m-1}{2(2m-1)}W,
\tag{4.6}
\]

which is (0.6).

Now let \(\Delta\in\mathcal K\).  Its zero coordinate marginals at
\(1,2\) give

\[
 \langle L^\sharp,\Delta\rangle
                  =-\sum_{D\in\mathcal H}\Delta_D.
\tag{4.7}
\]

Put

\[
 P(\Delta)=\sum_{\Delta_D>0}\Delta_D.
\tag{4.8}
\]

Since \(\sum_D\Delta_D=0\), one has

\[
 P(\Delta)=\frac12\|\Delta\|_1.
\tag{4.9}
\]

Moreover,

\[
 \sum_{D\in\mathcal H}\Delta_D\le P(\Delta),
 \qquad
 \frac12\|\Delta\|_2^2
      \ge\frac12\|\Delta\|_1=P(\Delta),
\tag{4.10}
\]

where the second inequality uses \(a^2\ge|a|\) for every integer \(a\).
Combining (1.1), (4.7), and (4.10) yields

\[
 \Psi(L^\sharp+\Delta)-\Psi(L^\sharp)
 =-\sum_{D\in\mathcal H}\Delta_D
      +\frac12\|\Delta\|_2^2\ge0.
\tag{4.11}
\]

This proves (4.2). \(\square\)

Equality in (4.11) can occur only if every nonzero coefficient of
\(\Delta\) is \(\pm1\), every positive coefficient lies in
\(\mathcal H\), and no negative coefficient lies there.  Thus the shield
is not an artefact of a loose norm estimate.

### Corollary 4.2 (exchange-descent no-go)

No theorem using only finite compositions of the audited exchanges can
assert that every integral load state of common-core total mass and
\(\Psi=\Omega(W)\) has a decreasing exchange.  The state
\(L^\sharp\) is a counterexample to that load-space assertion.

This remains true if arbitrary middle-neutral three-top or moving-hole
configuration exchanges are interspersed between six-frame moves.

### Proposition 4.3 (exact common-core coordinate cap)

Every genuine choice of one length-\(d\) common-core path at every root has
middle marginals satisfying, for every coordinate \(i\),

\[
 dN\frac{m-H}{2m}
 \le b_i
 \le dN\frac{m-H}{2m}
       +HN\frac{m+H}{2m}.
\tag{4.12}
\]

In particular, both endpoints in (4.12) are
\((1/2+o(1))W\).  The shield \(L^\sharp\) violates the upper bound:

\[
 b_1(L^\sharp)
 \ge \frac W2+\binom{2m-2}{m-2}-K
 =\left(\frac34-o(1)\right)W.
\tag{4.13}
\]

Hence \(L^\sharp\) is not in the support of the common-core product.

#### Proof

The number of roots \(A\in\binom{[2m]}{m-H}\) containing \(i\) is

\[
 \binom{2m-1}{m-H-1}=N\frac{m-H}{2m}.
\tag{4.14}
\]

Every one of the \(d\) targets selected at such a root contains \(i\),
which proves the lower bound in (4.12).

There are \(N(m+H)/(2m)\) roots not containing \(i\).  At one such root,
the extra \(H\)-set in a middle target is one edge of an injective tight
\(H\)-path.  A fixed coordinate belongs to at most \(H\) consecutive
edges of that path.  Thus these roots contribute at most
\(HN(m+H)/(2m)\) further occurrences, proving the upper bound.

For (4.13), the first indicator in (4.5) contributes \(W/2\), the second
contributes \(\binom{2m-2}{m-2}\) among targets already containing \(1\),
and deletion of \(\mathcal H\) removes at most \(K\) such occurrences.
Equation (0.3) and (4.6) prove the asymptotic statement. \(\square\)

## 5. Adversarial audit and exact remaining boundary

The strongest claim above is deliberately a load-space theorem.  Its
limitations are as follows.

1. **The formal shield is physically excluded.**  Proposition 4.3 proves
   that \(L^\sharp\) violates a necessary common-core marginal cap.  Thus
   Theorem 4.1 neither produces a statewise local minimum in the product
   support, nor proves \(\min\Psi=\Omega(W)\), nor refutes coefficient one.

2. **The catalyst descent is exact but conditional.**  Proposition 2.2
   needs the six specified old paths and the fixed closing path.  In a
   global state its sign is (2.5), not automatically negative.

3. **The common-core suspension is all-core.**  Lemma 2.3 does not prove
   availability inside a preassigned core assignment, a fixed mechanical
   support, or a positive-density packing of disjoint gadgets.

4. **Neutral moves may change future availability, not the invariant.**
   The three-, four-, and eight-top exchanges could expose a later
   six-frame packet.  Nevertheless every complete sequence still has net
   derivative in \(\mathcal K\), so Theorem 4.1 applies to the net change.

5. **New primitives can escape.**  A legal common-core exchange with
   nonzero coordinate-marginal derivative is not ruled out and would not
   be covered by the shield.

Accordingly, the smallest replacement lemma for this lane is one of the
following genuinely support-sensitive statements.

* **capped-fibre descent:** prove that every legal common-core coefficient
  satisfying (4.12) and \(\Psi=\Omega(W)\) admits a lower-energy legal
  coefficient in the same coordinate-marginal fibre; or
* **marginal-changing exchange:** construct a legal bounded or globally
  packable path exchange whose middle derivative is not in \(\mathcal K\),
  and prove a charged-copy theorem for it.

The audited three-top/two-base and moving-hole identities alone prove
neither statement.
