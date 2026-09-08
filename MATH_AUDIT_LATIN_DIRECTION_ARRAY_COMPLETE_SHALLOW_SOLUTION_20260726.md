# Audit of the claimed Latin-direction shallow solution: two fatal gaps

Date: 2026-07-26

## 0. Verdict

`MATH_THEOREM_LATIN_DIRECTION_ARRAY_COMPLETE_SHALLOW_SOLUTION_20260726.md`
is **invalid**.  There are two independent failures.

1. The crossed `Q_4 x Q_4` recursion does not preserve the same-owner
   direction relation.  Consequently the recursive double factor and the
   parity-Latin column equations are not established.
2. Even if that algebraic failure were repaired, a single physical lower
   or upper target does not identify the completed-pair support `J`.
   Therefore injectivity of the augmented code `(J,p|J^c,x|J^c)` does not
   imply physical trace injectivity, and half-step completion is not a
   deterministic function of the unaligned target.

The puncturing lemma and the algebraic recovery in Section 5 are correct
**conditional on `J` being supplied externally**.  They do not prove the
stated physical theorem.

## 1. Explicit failure of the crossed recursion

At the first doubling, the note defines

\[
P^0(u,v)=
\begin{cases}
(G_4^0u,v),&\epsilon(u,v)=0,\\
(u,G_4^0v),&\epsilon(u,v)=1,
\end{cases}
\]

and

\[
P^{1,\times}(u,v)=
\begin{cases}
(u,G_4^1v),&\epsilon(u,v)=0,\\
(G_4^1u,v),&\epsilon(u,v)=1.
\end{cases}
\]

The proposed coordinate involution sends

\[
                         S_8(Li)=R(S_4i),
 \qquad S_4=(2\ 4).                                      \tag{1.1}
\]

Take

\[
                         u=0000,\qquad v=1100.             \tag{1.2}
\]

Both have even weight, so `epsilon(u,v)=0`.  In the common-phase `Q_4`
table,

\[
                         \delta_4^0(u)=1,
 \qquad                  \delta_4^1(v)=3.                  \tag{1.3}
\]

Therefore the outgoing direction of `P^0` at `(u,v)` is `L1`, and

\[
                         S_8\delta_{P^0}(u,v)=R1.           \tag{1.4}
\]

But the outgoing direction of `P^{1,times}` at the same owner is `R3`.
Hence

\[
 \boxed{
 \delta_{P^{1,\times}}(u,v)\ne S_8\delta_{P^0}(u,v).}       \tag{1.5}
\]

The error is structural.  The base identity

\[
                         \delta_4^1(z)=S_4\delta_4^0(z)
\]

holds at the **same** vertex `z`.  The crossed child compares
`delta_4^0(u)` with `delta_4^1(v)`.  The condition
`|u|+|v|=0 mod 2` synchronizes only the parities of their phase colours,
not the full phase colours.  It cannot justify this comparison.

Thus Lemma 2.1 is false already at `R=8`, and equations (3.3) and the
claimed Latin column bijections do not follow.

## 2. The augmented trace code is not the physical trace

Sections 5--6 treat the completed support `J` as if it were determined by
one signed physical target.  It is not.

On one physical coordinate pair `(a_i,b_i)`, write its state as two bits.
A completed coarse move has the adjacent physical trajectory

\[
                         00\longrightarrow01\longrightarrow11. \tag{2.1}
\]

The lower intersection on this pair is `00`.  But an untouched pair which
starts in state `00` has the identical lower trace `00`.  Likewise, for an
upper target a completed pair has trace `11`, indistinguishable from an
untouched pair initially in state `11`.

Therefore a lower or upper target does not tell which empty/full pairs
belong to `J`.  The code

\[
                         (J,p|J^c,x|J^c)                         \tag{2.2}
\]

is strictly richer than the physical target.  Injectivity of (2.2) can at
most prove injectivity after the support has been tagged; it does not prove
literal shadow injectivity.

The same issue invalidates the half-step argument.  A pair retaining one
endpoint in an unaligned lower target can be either

* an untouched split pair, or
* the partial boundary pair.

Thus the unaligned target does not identify its boundary pair, and the
proposed aligned completion is not a deterministic function of that
target.

## 3. What survives

Assume hypothetically that an exact fixed-point-free double factor were
available and that `J` were supplied as an external tag.  Then Section 5's
index calculation is correct:

\[
 y_k=x_k+p_{S_Rk}qquad(k\notin J\cup S_RJ),                    \tag{3.1}
\]

and, once the puncturing decoder recovers `y`, disjointness gives

\[
 p_j=y_{S_Rj}+x_{S_Rj},\qquad x_j=y_j+p_{S_Rj}.                 \tag{3.2}
\]

The reverse puncturing statement is also sound: an incoming direction
fibre is the corresponding outgoing fibre translated by its direction,
so coordinate-deletion injectivity is preserved.

These conditional facts do not repair either (1.5) or the loss of `J` in
the physical target.

## 4. Correct replacement target

A valid local theorem must satisfy both stronger requirements.

1. Its recursive double-factor relation must be verified at the same
   composite owner, rather than inferred from parity synchronization.
2. Its decoder must recover the varied-pair support from the literal lower
   target alone and from the literal upper target alone.  Equivalently,
   empty/full untouched pairs must be distinguished by an intrinsic code,
   not by adjoining `J` as metadata.

Until both are supplied, the local parity compiler remains open.

