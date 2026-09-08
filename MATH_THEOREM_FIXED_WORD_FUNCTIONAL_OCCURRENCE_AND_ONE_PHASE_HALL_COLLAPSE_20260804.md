# A fixed OR word has a functional occurrence graph

**Date:** 2026-08-04
**Method:** pure mathematics; no computation, search, or solver
**Status:** unconditional semantic simplification of the exact one-phase
terminal reduction.  Once one literal antecedent is fixed, the residual
target--occurrence Hall problem is exactly target coverage: distinct target
values cannot compete for one interval address.  This does not construct an
antecedent with a complete lower deck.

## 0. Outcome

Let `A` be one fixed literal word, let `C` be any bank of interval
addresses, and let `L` be a family of pairwise distinct target values.  Put

\[
                         v_A(C)=\operatorname{OR}_A(C).
\]

The exact target--occurrence graph

\[
 (S,C)\in H_A\quad\Longleftrightarrow\quad v_A(C)=S
\tag{0.1}
\]

has right degree at most one.  Consequently its matching deficiency is the
number of target values absent from the literal deck:

\[
 \boxed{
 \delta(H_A)=|\{S\in L:v_A^{-1}(S)\cap\mathcal C=\varnothing\}|.}
\tag{0.2}
\]

If an exact partial matching `Pi` is forced, every forced address has the
value of its forced target and therefore has no edge to a residual target.
Contracting `Pi` creates no additional matching loss.  In the notation of
the serial one-phase theorem,

\[
 \boxed{
 \delta(A,\Pi)=
 |\{S\in L\setminus L(\Pi):
      S\notin\operatorname{Deck}_{\le d}(A)\}|.}
\tag{0.3}
\]

Because every pinned target already occurs at its pinned address, the
right side of (0.3) is also the number of all strict-lower targets absent
from `A`.  Thus

\[
 \boxed{
 \Lambda_{\rm 1ph}(T,\epsilon)=
 \min_{A\in\mathcal A(T,\Pi^\epsilon)}
 |L\setminus\operatorname{Deck}_{\le d}(A)|.}
\tag{0.4}
\]

The final compiler gate is therefore one literal lower-deck surjectivity
problem, not a second matching or common-cap problem after the word has
been chosen.

## 1. Functional occurrence theorem

For `S in L`, write

\[
                       \mathcal C_A(S)=
 \{C\in\mathcal C:v_A(C)=S\}.
\tag{1.1}
\]

The families in (1.1) are pairwise disjoint.

### Theorem 1.1

Let `H_A` be given by (0.1).  For every `Z subseteq L`,

\[
                         |N_{H_A}(Z)|=
                         \sum_{S\in Z}|\mathcal C_A(S)|.
\tag{1.2}
\]

Hence

\[
 \max_{Z\subseteq L}(|Z|-|N_{H_A}(Z)|)_+
   =|\{S\in L:\mathcal C_A(S)=\varnothing\}|.
\tag{1.3}
\]

#### Proof

An address has one literal OR value.  Therefore
`C_A(S) intersect C_A(S')` is empty whenever `S != S'`, which proves
(1.2).  Let `M` be the set of absent targets.  Taking `Z=M` gives
deficiency `|M|`.

Conversely, split arbitrary `Z` into its absent and present targets.  Every
present target contributes at least one address to the disjoint sum (1.2),
so

\[
 |Z|-|N_{H_A}(Z)|
 \le |Z\cap M|\le |M|.
\]

This proves (1.3). \(\square\)

### Corollary 1.2 (matching is automatic after coverage)

If every target in `L` occurs in `A`, choose one address from each nonempty
family `C_A(S)`.  The chosen addresses are automatically distinct, so they
form a matching saturating `L`.

No Hall theorem beyond literal coverage is required.

## 2. Forced exact facts consume no residual target capacity

Let

\[
             \Pi=\{(S_i,C_i):i\in I\}\subseteq H_A
\tag{2.1}
\]

be target- and address-disjoint.  Put `L_*={S_i}` and `C_*={C_i}`.  The
residual exact graph is

\[
 H_A^\Pi=H_A[(L\setminus L_*)\,\cup\,
                  (\mathcal C\setminus C_*)].
\tag{2.2}
\]

### Theorem 2.1 (forced-fact neutrality)

For every residual target `S in L minus L_*`,

\[
                         \mathcal C_A(S)\cap C_*=\varnothing.
\tag{2.3}
\]

Consequently

\[
 N_{H_A^\Pi}(Z)=N_{H_A}(Z)
       \qquad(Z\subseteq L\setminus L_*),             \tag{2.4}
\]

and the residual deficiency is exactly (0.3).

#### Proof

For every forced address `C_i`, soundness of (2.1) gives
`v_A(C_i)=S_i`.  If `C_i` were also in `C_A(S)` for a residual target,
then the uniqueness of `v_A(C_i)` would give `S=S_i`, contrary to
`S notin L_*`.  This proves (2.3), hence (2.4).  Apply Theorem 1.1 to the
residual target family. \(\square\)

### Corollary 2.2

Every exact forced partial matching extends to a maximum matching of the
fixed-word occurrence graph.  It extends to a target-saturating matching
if and only if every residual target occurs at least once.

This is stronger than the generic forced-edge bound
`delta(A,Pi)<=delta(A,emptyset)+|Pi|`: in the literal fixed-word graph the
forced-edge surcharge is exactly zero.

## 3. One-phase specialization

Fix a terminal carrier `T`, one aligned phase `epsilon`, and its exact ray
matching `Pi^epsilon`.  For every
`A in A(T,Pi^epsilon)`, the pins themselves prove that every target in
`L(Pi^epsilon)` occurs.  Theorem 2.1 therefore gives

\[
 \delta(A,\Pi^\epsilon)
  =|L\setminus\operatorname{Deck}_{\le d}(A)|.
\tag{3.1}
\]

Minimizing over the pinned inverse fibre proves (0.4).  The serial bound
becomes

\[
 \nu(k)\le B(k)+u(T_0)+
 \min_{T\in\operatorname{Comp}_\Gamma(T_0)}
 \min_{\epsilon\in\mathcal E(T)}
 \min_{A\in\mathcal A(T,\Pi^\epsilon)}
 |L\setminus\operatorname{Deck}_{\le d}(A)|.
\tag{3.2}
\]

In particular, an antecedent in the pinned fibre with a complete strict-
lower deck closes the final compiler with zero loss.

## 4. Exact scope

The theorem removes only a spurious **post-selection** Hall layer.  It does
not make the construction of `A` easy.

Before `A` is fixed, one potential interval address may admit several
possible target values under different source-letter choices.  A
maximal-cap, Rado, Hall, or flow formulation can still be useful for
choosing those values consistently.  The theorem says that such a device
is a construction method for one word, not an additional acceptance gate
after that word exists.

Likewise, a native socket route may consume physical capacities other than
its exact target address.  If those routes remain part of topology,
compensation, or regeneration, their noncoalescible footprints must still
be priced.  The present theorem concerns ordinary target coverage by exact
literal interval facts.

The remaining one-phase lower problem is therefore precisely:

> construct one global nonempty antecedent extending the forced rays whose
> short-interval OR map is surjective onto every strict-lower target.

That is the integral one-copy trace/chainization problem.  It is not a
separate fixed-word Hall problem.
