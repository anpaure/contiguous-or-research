# Audit of the pentagon diagonal-voltage no-go

Date: 2026-07-26

Audited file:
`MATH_ATTACK_K_DIAGONAL_VOLTAGE_PRODUCT_NOGO_20260726.md`.

Method: independent pure-mathematical audit.  No computation, finite
search, solver, or web input was used.

## 1. Verdict

The no-go is valid for the stated architecture: a literal serial product
of disjoint suspended-pentagon slots retaining every physical `X/Y` token,
root port, complement port, and spectator context.

The decisive statewise statement is

\[
                         \boxed{\chi\ge5^{fk}},        \tag{A.1}
\]

where `f` is the fraction of the `k5^(k-1)` complete axis fibres carrying
the local pentagon trade.  Thus bounded component moment permits only
`f=O(1/k)`, while positive action density forces exponential moment.  In
particular an order-five diagonal component can support at most one slot
fibre.

This closes cyclic, diagonal, subdirect, auxiliary-sheet, and arbitrarily
correlated voltage compression of the literal product overlay.  It does
not address a new nonproduct/interleaved exact factor whose product-token
addresses are absent and whose complete ownership map is rebuilt.

## 2. Local colour graph

The seven owner permutations read from the two five-row tables are

\[
\begin{array}{c|c}
x_0&1\\
x_1&(1\ 4\ 3\ 5\ 2)\\
x_2&(1\ 4\ 5\ 3\ 2)\\
x_3&1\\
y_0&(2\ 4\ 3\ 5)\\
y_1&(1\ 4\ 2)(3\ 5)\\
y_2&(2\ 4\ 5\ 3).
\end{array}                                             \tag{A.2}
\]

Direct table tracing verifies every entry.  With `a=pi_(x_1)` and
`b=pi_(x_2)`, one has

\[
                         a^{-1}b=(3\ 5\ 4).            \tag{A.3}
\]

The two five-cycles generate `A_5`, and the odd four-cycle `pi_(y_0)`
enlarges the group to `S_5`.  Therefore the local graph is connected and
primitive.  Its only invariant port equivalences are equality and the
universal relation.  An abelian quotient factors through parity and kills
the active five-cycles, so there is no cyclic five-state presentation of
the complete colour ledger.

## 3. Product-address rigidity

At a phase internal to slot `h`, all earlier slots are complement ports
and all later slots are root ports.  Restriction of a physical resource to
the disjoint carriers therefore determines:

1. the active slot `h`;
2. every spectator row coordinate; and
3. the local resource colour and its opposite-shore owner.

Consequently every ownership edge has the axis form

\[
 (i_1,\ldots,i_h,\ldots,i_k)_-
 \longleftrightarrow
 (i_1,\ldots,\pi_c(i_h),\ldots,i_k)_+.                \tag{A.4}
\]

The full monodromy contains, and in the serial product equals, `S_5^k`.
It is transitive on `[5]^k`; hence a full `k`-slot skeleton is one
component of shore size `5^k` and has component moment `5^k`.

A diagonal subgroup is only an abstract subgroup obtained after deleting
the axis generators.  A quotient which identifies axis factors identifies
distinct root ports and spectator-labelled physical resources.  Restoring
those labels restores the full product component.

## 4. Entropy inequality and correlated states

For `C subset [5]^k`, let `L(C)` count complete axis-parallel five-point
lines contained in `C`.  If `X` is uniform on `C`, then a complete
`h`-fibre contributes `5/|C|` to
`H_5(X_h | X_(-h))`.  Hence

\[
 {5L(C)\over|C|}
 \le\sum_hH_5(X_h\mid X_{-h}).                       \tag{A.5}
\]

Han--Shearer gives

\[
 \sum_hH_5(X_h\mid X_{-h})\le H_5(X)=\log_5|C|,     \tag{A.6}
\]

so

\[
                         5L(C)\le|C|\log_5|C|.        \tag{A.7}
\]

The constant is exact for coordinate subcubes.  Applying (A.7) to every
port-closed component `C_K`, and using weighted AM--GM, gives (A.1).
This proof allows arbitrary correlated active-fibre choices; independence
and translation invariance are nowhere assumed.

Each active tagged fibre has full `l_1` variation eighteen and half-`l_1`
action nine.  Thus

\[
 \mathcal L_1^{\rm tag}=18L,
 \qquad
 \mathcal A_1^{\rm tag}=9L,                           \tag{A.8}
\]

and bounded moment retains only a vanishing fraction of the available
tagged action.

## 5. Growing-scale constants

For the full size-`r` Catalan tensor,

\[
 \sum_{T\in D_r}k(T)=5\binom{2r-8}{r-4},
 \qquad
 \mathbb E k(T)=\left({5\over256}+o(1)\right)r.       \tag{A.9}
\]

Therefore

\[
 \chi_r=\mathbb E5^{k(T)}
 \ge5^{(5/256+o(1))r}.                               \tag{A.10}
\]

The exact tagged totals and densities, with
`W_r=(2r+1)C_r`, are

\[
 \mathcal L_1^{\rm tag}=18\binom{2r-8}{r-4},
 \quad
 {\mathcal L_1^{\rm tag}\over W_r}\to{9\over256},   \tag{A.11}
\]

\[
 \mathcal A_1^{\rm tag}=9\binom{2r-8}{r-4},
 \quad
 {\mathcal A_1^{\rm tag}\over W_r}\to{9\over512}.  \tag{A.12}
\]

Each slot has carrier width at most nine.  The union-of-blocks
two-boundary argument therefore gives, at every fixed nondegenerate depth,

\[
 {1\over2}\|\mu_q^+-\mu_q^-\|_1
 \le90\binom{2r-8}{r-4}
 =\left({45\over256}+o(1)\right)W_r.                 \tag{A.13}
\]

Thus the tensor reaches the critical carrier/action scale.  Its failure is
not subcritical support but exponential product-resource indivisibility.
Tagged variation remains only a reservoir quantity; physical target
aggregation may cancel it, so no cap gain is inferred.

## 6. Precise CRH boundary

The proposed voltage lift is not a viable bounded-moment `CRH_A` pair.
Positive-density use of its local action forces (A.10), while a bounded
component family can retain only `O(1/r)` of the slot-fibre action at
critical `k=Theta(r)`.

This is not a universal no-go for the original two endpoint factors: a
special directed choice of their giant skeleton components is not ruled
out by the moment calculation alone.  What is rigorously closed is the
claimed diagonal compression into bounded components.  Any remaining
escape must supply a new nonproduct physical ledger, not a quotient of the
old one.
