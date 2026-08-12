# Audit: Catalan duplicate current, Ryser connectivity, and prepared-C6 Rado gate

**Date:** 2026-08-03  
**Scope:** pure mathematics only; no solver, finite search, or finite
existence evidence.

## 0. Binding and verdict

This audit is bound exclusively to
`MATH_THEOREM_CATALAN_DUPLICATE_CURRENT_RYSER_AND_PREPARED_C6_RADO_20260803.md`
at SHA-256

```text
ee8cb6c0ba0edf9d1ef349f6c7eac6f860c66092cbb08015b4a612b3345574a4
```

**Verdict: GO.**  Independent proof reads of the Ryser/balanced-current,
physical-C6/catalytic, Catalan-multidesign, and Rado/Hall portions found no
remaining mathematical correction.

The final source correctly includes the load-bearing scopes: edge-disjoint
perfect matchings for the turn current, palette-triviality at `q=1`, the
homogeneous-kernel status of one C6 vector, deletion rather than contraction
of atoms meeting the protected C8, and one matroid for the entire joint
compatibility system.

## 1. Self-contained labeled Ryser connectivity

Equal row and column margins make the red and blue degrees of the symmetric
difference equal at every row and column, so every nonempty difference
contains an alternating cycle.  For a shortest cycle:

* at length four, one switch removes the cycle;
* if the chord inspected in Theorem 1.1 is zero in the first matrix, the
  displayed switch removes three disagreements and creates at most one;
* if the chord is one, a red chord would give a shorter alternating cycle,
  so it is common and the corresponding switch in the second matrix again
  decreases Hamming distance by two.

Every switch preserves both margins.  Induction reaches equality, and
reversing the switches made on the second matrix gives a path from the
original first matrix to the original second matrix.  This proves the
labeled theorem, not merely an unlabeled degree-sequence statement.

Consequently equal coordinate degrees are necessary and sufficient for
abstract switch reachability of labeled constant-row-sum incidence
matrices.

## 2. Catalan duplicate current and explicit multidesign

With

\[
 \mathcal U={[2m-1]\choose m+1},\quad
 W={2m-1\choose m},\quad
 U=|\mathcal U|,
\]

the identity `W-U=Cat_m` is exact.  For two edge-disjoint perfect
middle-levels matchings, every turn has rank `m+1` and the coordinate
current is

\[
 2{2m-2\choose m-1}-{2m-2\choose m-2}.
\]

For Proposition 1.3 put

\[
 v=2m-1,\quad k=m+1,\quad
 b=\operatorname{Cat}_m,\quad
 \lambda=2\operatorname{Cat}_{m-1}.
\]

The Catalan identities give `bk=v lambda`.  Since `m>=3`, `k<v`, so each
cyclic interval

\[
 D_j=\{jk,jk+1,\ldots,jk+k-1\}\pmod v
\]

has `k` distinct points.  Before reduction modulo `v`, the labeled block
slots concatenate to the interval `0,...,bk-1`; because `bk=v lambda`, each
residue occurs exactly `lambda` times.  Repeated blocks are permitted and
do not affect the replication calculation.

Adding one copy of every upper colour gives `U+Cat_m=W` rows.  If

\[
 A={2m-2\choose m-1},\qquad B={2m-2\choose m-2},
\]

then the complete upper layer has coordinate replication `B`, and

\[
 B+2\operatorname{Cat}_{m-1}=B+2(A-B)=2A-B.
\]

Thus Corollary 1.4 gives an upper-surjective target in the same abstract
Ryser fibre of every two-perfect-matching cycle palette.  It does not give
a literal owner factor or an occurrence-compatible C6 lift.

## 3. Balanced repair equivalence

Section 3 explicitly works on the two-edge-disjoint-perfect-matching face,
so the row total and current required for the Catalan identities are fixed.
For an integer vector `z`, the first two equations in (3.2) preserve those
margins, while the lower bounds are exactly `mu+z>=1`.  Hence (3.2) is
necessary and sufficient for an abstract upper-surjective target.

Writing `mu+z=1+nu`, subtraction of one complete upper layer gives exactly

\[
 \sum_R\nu_R=\operatorname{Cat}_m,qquad
 \sum_{R\ni x}\nu_R=2\operatorname{Cat}_{m-1}.
\]

Conversely every such nonnegative duplicate multidesign gives a valid
`z=1+nu-mu`.  Theorem 1.1 then connects every labeling of the two endpoint
multisets.  One physical C6 vector is correctly described only as a
homogeneous current-kernel vector; it need not satisfy the positivity part
of a complete repair by itself.

## 4. Exact physical-C6 projection and obstruction

For a palette-nontrivial row-oriented switch, a physical C6 rectangle has
old rows

\[
 P=K+p+e,\qquad Q=K+q+f,qquad |K|=m-1,
\]

and new rows `K+q+e,K+p+f`.  Thus the old rows meet in exactly `m-1`
coordinates.  Conversely, a switch with that intersection has this form.
After the selected swapped elements and row pairing are fixed, the third
hole `b_0` ranges bijectively over `K`, giving exactly `m-1` possible common
retained turn colours.

At `q=1`, the switch merely exchanges the two labeled row contents and is
the identity after occurrence labels are forgotten.  Theorems 2.1 and 2.3
therefore correctly restrict their nontrivial claims to `q>=2`.

For Proposition 2.2, the construction uses `m+4` coordinates and therefore
exists exactly in the stated range `m>=5`.  Both matrices have the same
column margins, but their only old row pair intersects in
`m-2=(m+1)-3`, so no distance-two physical C6 move is available.  This is
an abstract two-row obstruction, not a literal-host existence result.

## 5. Catalytic reserve-row induction

For `q=2`, the desired switch is already distance two and needs no reserve.
For `q>2`, choose `a_2,b_2` as in the theorem and set

\[
 H=P-\{a,a_2\}+\{b,b_2\},\qquad
 H'=H-b+a=P-a_2+b_2.
\]

The pair `P,H` has intersection size `k-2`, so one C6-palette switch creates
the desired final first row and changes `H` to `H'`.  Moreover

\[
 H'\setminus Q=(P\setminus Q)\setminus\{a_2\},\qquad
 Q\setminus H'=(Q\setminus P)\setminus\{b_2\},
\]

so the distance drops exactly from `q` to `q-1`, while `a,b` remain the
elements exchanged by the recursive problem.  The recursive output sends
`H'` back to `H`, restores every subordinate reserve, and changes `Q` to
`Q-b+a`.  Therefore the exact costs are `q-1` distance-two switches and
`q-2` restored labeled reserves.  In particular, `q=3` uses two switches
and one reserve.

This is only a palette factorization.  Every distance-two step still needs
a compatible common turn and physical occurrence; those requirements are
explicitly left open.

## 6. Prepared Rado and private Hall faces

Under premise (4.1), the independent sets of one matroid are **exactly**
the simultaneously applicable complete atoms.  Rado's theorem therefore
gives an independent transversal precisely when

\[
 r_N\!\left(\bigcup_{R\in X}\mathcal A_R\right)\ge |X|
 \qquad(X\subseteq H).
\]

Each atom includes its complete old/new C6, designation, companion colour,
reserve witnesses, and every consumed physical token.  Thus the exact
matroid premise is strong enough to coinstantiate the selected repairs.
Atoms intersecting the complete protected C8 support are deleted before
the matroid is formed; no unsupported contraction is used.

On the private-socket face, the atom ground has the rank-one-per-socket
partition matroid.  Its rank on the union of menus indexed by `X` is exactly
the number `|Gamma(X)|` of accessible sockets, so Rado reduces to the stated
Hall inequalities.

The source correctly warns that the entire compatibility relation must be
one proved matroid.  Pairwise resource-disjoint compound atoms need not be
a matroid: the `{1,2}` versus `{1}`,`{2}` example violates augmentation.
Consequently raw rectangle menus or arbitrary intersections of matroid
constraints do not license Rado.

## 7. Scope

The theorem establishes abstract fixed-margin connectivity, explicit
balanced targets, exact palette-level C6 factorization with catalytic rows,
and a conditional Rado/Hall selection criterion.  It provides no solver or
finite existence evidence and makes no claim that the reserve rows, common
turns, literal C6 occurrences, and protected C8 coexist in one resident
factor.  That reserve-atlas construction remains the open theorem.
