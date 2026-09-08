# The `54/32` automorphism current cancellation is exactly two inverse backtracks

**Date:** 2026-08-06  
**Method:** pure mathematics; literal path identities and the exact nested
rail current formula  
**Status:** unconditional no-go for the shortest automorphism-orbit closure
of the persistent `54/32` anti-pair.  Longer changing-slot circuits and
external absorbers are not excluded.

## 0. Verdict

The negative edge `54` and positive edge `32` of the suspended `D_3`
pentagon have opposite q1 and `Y`-rail currents.  Their remaining all-width
current is one nested square

\[
 R_j=[T_j25]+[T_j34]-[T_j24]-[T_j35].                       \tag{0.1}
\]

Both port automorphisms

\[
                    \alpha=(2\ 3),\qquad\beta=(4\ 5)         \tag{0.2}
\]

send `R_j` to `-R_j`.  Hence either four-term sum

\[
       C_{54}+C_{32}+gC_{54}+gC_{32}=0,
       \qquad g\in\{\alpha,\beta\},                           \tag{0.3}
\]

vanishes at every width.

Nevertheless (0.3) is dynamically useless.  Directly on the literal path
packets, `g54` and `g32` are the inverse transitions of `54` and `32`, in
the crossed pairing described below.  Thus (0.3) is exactly two forward--
backward pairs.  Its old and new row-incidence vectors agree identically,
and its net tracked-row action is trivial.

So the shortest `Aut(D_3)` orbit cancellation of the only q1 anti-pair is
not an absorber; it is a disguised identity.

## 1. The two old pair packets

Let `N` be the old two-row packet on negative edge `54`:

\[
 \begin{aligned}
 N_5&:134-234-236-256,\\
 N_4&:135-235-245-246.
 \end{aligned}                                                \tag{1.1}
\]

Let `P` be the old two-row packet on positive edge `32`:

\[
 \begin{aligned}
 P_3&:125-235-236-346,\\
 P_2&:124-234-345-356.
 \end{aligned}                                                \tag{1.2}
\]

Apply `alpha=(23)` and `beta=(45)` coordinatewise.  Directly,

\[
 \begin{array}{c|cc}
 &\text{first row}&\text{second row}\\ \hline
 \alpha P&135-235-236-246&134-234-245-256\\
 \alpha N&124-234-236-356&125-235-345-346\\
 \beta N&135-235-236-246&134-234-245-256\\
 \beta P&124-234-236-356&125-235-345-346.
 \end{array}                                                \tag{1.3}
\]

Consequently, as unordered two-row packets,

\[
                         \alpha P=\beta N,
       \qquad            \alpha N=\beta P.                   \tag{1.4}
\]

## 2. Literal native transitions

### Lemma 2.1

The two native substitutions are

\[
                         T_{54}:N\longrightarrow\alpha P,
       \qquad            T_{32}:P\longrightarrow\alpha N.    \tag{2.1}
\]

#### Proof

For edge `54`, use the aligned orders

\[
 (4,3,2,6,5,\mathord\infty,1),
 \qquad
 (3,5,2,4,6,\mathord\infty,1).
\]

The native double swap gives

\[
 (3,4,2,5,6,\mathord\infty,1),
 \qquad
 (5,3,2,6,4,\mathord\infty,1).
\]

Cutting after `infinity` reconstructs exactly the two paths in `alpha P`
from (1.3).  The calculation for edge `32` is the same normal form with
the active endpoints reversed and gives `alpha N`.  \(\square\)

Conjugating (2.1) and using (1.4) gives

\[
 \begin{array}{c|c}
 \alpha T_{54}:\alpha N\longrightarrow P&T_{32}^{-1},\\
 \alpha T_{32}:\alpha P\longrightarrow N&T_{54}^{-1},\\
 \beta T_{54}:\alpha P\longrightarrow N&T_{54}^{-1},\\
 \beta T_{32}:\alpha N\longrightarrow P&T_{32}^{-1}.
 \end{array}                                                \tag{2.2}
\]

Thus both residual-flipping automorphisms turn the selected moves into the
same two reverse transitions.

## 3. All-width current and triviality

The persistent-current theorem gives, for every intermediate tail depth,

\[
                         C_{54,j}+C_{32,j}=R_j.                \tag{3.1}
\]

Since either `alpha` or `beta` interchanges one side of the `2 x 2` square
(0.1),

\[
                         gR_j=-R_j.                            \tag{3.2}
\]

At q1 and at the two endpoint widths the same sum is already zero.  Hence
(0.3) holds for the complete all-width current vector.

### Theorem 3.1 (automorphism closure is incidence-trivial)

For `g=alpha` or `g=beta`, the four native transitions represented in
(0.3) are, after literal row identification,

\[
                         T_{54}+T_{32}
                         +T_{54}^{-1}+T_{32}^{-1}.             \tag{3.3}
\]

Their aggregate signed row-incidence vector is zero before any palette or
tail projection.  Every serial realization is two backtracks, up to their
order, and has trivial final tracked-row action.

#### Proof

Equation (2.2) identifies the conjugate transitions with the two inverses.
Each row packet therefore appears once positively and once negatively in
(3.3).  This proves literal incidence cancellation and triviality of each
backtrack.  \(\square\)

The remaining automorphism `alpha beta` fixes `R_j` rather than negating it,
so it does not close (3.1).  Therefore no element of the four-element port
automorphism group converts the `54/32` residual into a nontrivial marked
zero-current circuit.

## 4. Exact consequence

Together with the conjugate-square owner-multiplicity obstruction, this
closes both shortest `Aut(D_3)` ideas:

1. the signed edge-`12` square cancels current but is not a simple packet;
2. the positive `54/32` orbit square is a simple algebraic cancellation but
   is literally two inverse backtracks.

A productive circuit must therefore leave the fixed port-automorphism
orbit, change the slot through a transport not equivalent to native
inversion, or export the residual square (0.1) to an exterior halo.
