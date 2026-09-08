# Dynamic position group of native inverse pairs, and the four-move commutator gate

**Date:** 2026-08-06  
**Method:** pure mathematics; no finite search, solver, or computation  
**Status:** unconditional in the pointed row model.  The ideal-helper
transitivity statement is explicitly conditional on physical availability of
the required companion row at each step.

## 0. Verdict

The time-zero span deficiency of the native MSW inverse-pair catalogue is not
explained by a static invariant of the local position generators.  A native
move right-multiplies each of its two cyclic orders by

\[
             g_i=(i\ i+1)(i+m\ i+m+1),
             \qquad i\in\mathbb Z_{2m+1},                 \tag{0.1}
\]

and these separated double swaps generate the full alternating group

\[
                         \langle g_i:i\in\mathbb Z_{2m+1}\rangle
                         =A_{2m+1}.                         \tag{0.2}
\]

Moreover one formal aligned substitution can expose, in the raw row-order
model, a different aligned slot which was absent before.  Thus the initial
catalogue is not dynamically closed for a formal reason.

There is nevertheless an exact invariant.  Every tracked pointed row keeps
its permutation parity.  On unpointed unoriented wreath supports this parity
is intrinsic when `m` is even.  In a role-complete ideal helper model the
result is sharp: individual wreaths have one native position orbit when `m`
is odd and exactly the two parity orbits when `m` is even.

The shortest natural commutator does not provide a zero-current escape.  A
four-move `V`-commutator on three rows leaves the two outer rows fixed and
acts on the middle row by `[g_i,g_j]`.  For `m>=4`, if all four steps were
literal native inverse-pair substitutions in exact factors, central-palette
rigidity would force `[g_i,g_j]=1`.  Hence every legal such commutator is
host-trivial; its all-width current is zero only for that trivial reason.
The tempting choice `j=i+m`, whose formal middle-row action is an adjacent
three-cycle, is therefore not physically realizable by this four-step
commutator.

What remains is a genuine host-extension problem: build a longer sequence
with fresh companion rows whose successive slots realize a word in the
`g_i`, while keeping the complete exact-factor ledgers.  No one-row
permutation invariant beyond parity obstructs that programme in the
ideal-helper model.

## 1. Pointed inverse-pair normal form

Put

\[
                         N=2m+1,
                         \qquad m\ge2,                         \tag{1.1}
\]

and index positions cyclically by `Z_N`.  Let

\[
                         t_i=(i\ i+1)                           \tag{1.2}
\]

be the adjacent position transposition.  Define

\[
 \begin{aligned}
   g_i&=t_i t_{i+m},\\
   h_i&=(i\ i+1\ i+m+1\ i+m).
 \end{aligned}                                                \tag{1.3}
\]

The two edges in `g_i` are disjoint.  A pointed cyclic row is a bijection
`pi:Z_N -> [N]`; position permutations act on the right.

### Lemma 1.1 (aligned functional atom normal form)

Independently point the two rows at their respective active starts and use
the same local position indices in the two charts.  The aligned native
inverse-pair family used in the exact birail theorem has, up to interchanging
the two rows and reversing the atom orientation, the form

\[
                             (\pi,\pi h_0).             \tag{1.4}
\]

The native substitution is

\[
 \boxed{
   (\pi,\pi h_0)
      \longmapsto
   (\pi g_0,\pi h_0 g_0)
      =(\pi g_0,\pi g_0 h_0^{-1}).}                    \tag{1.5}
\]

Thus this directed functional atom is reversed at the same slot.  No
converse classification of every inverse triple-role matching is asserted.

#### Proof

In the two local charts, at the four active positions

\[
                 0, 1, m, m+1                               \tag{1.6}
\]

write the first row as `(a,b,c,d)`.  The companion row in the inverse-pair
normal form has entries `(b,d,a,c)`.  Reading the latter entries from the
former is exactly the four-cycle `h_0` in (1.3).

The substitution swaps the first two and the last two active positions in
both rows, hence right-multiplies both by `g_0`.  Direct conjugation gives

\[
                         g_0 h_0 g_0=h_0^{-1}.           \tag{1.7}
\]

Equation (1.5) follows.  \(\square\)

In particular the output pair always retains the reverse move at the same
slot.  Any genuinely new dynamic aperture must involve another row or
another start.

If fixed global pointings put the two active starts at `p` and `q`, the
same literal move right-multiplies the first row by `g_p` and the second by
`g_q`.  The starts need not agree.  This row-specific indexing is
load-bearing in serial compositions.

## 2. The single-row position group

### Theorem 2.1 (alternating generation)

For every `m>=2`,

\[
                         \langle g_i:i\in\mathbb Z_N\rangle=A_N.
                                                               \tag{2.1}
\]

#### Proof

Every `g_i` is a product of two transpositions, so the generated group is
contained in `A_N`.  Since `2m=-1 mod N`,

\[
 \begin{aligned}
 g_i g_{i+m}
   &=t_i t_{i+m}\,t_{i+m}t_{i+2m}\\
   &=t_i t_{i-1}.                                      \tag{2.2}
 \end{aligned}
\]

The right side is an adjacent three-cycle on
`{i-1,i,i+1}`.  Adjacent three-cycles generate `A_N`, proving (2.1).
\(\square\)

This is an algebraic generation theorem only.  It does not assert that the
companion row needed for each `g_i` occurs in one incumbent exact factor.

### Corollary 2.2 (ideal-helper orbit and its exact invariant)

Assume an ideal role-complete environment in which, whenever the currently
tracked row is `pi` and a start `i` is requested, a fresh compatible
companion `pi h_i` is available and the native move is physically allowed.
Then the pointed orders reachable from `pi` are exactly

\[
                              \pi A_N.                  \tag{2.3}
\]

After forgetting the pointing and orientation of a wreath row, the ideal
native action has

\[
 \begin{cases}
   1\text{ orbit},&m\text{ odd},\\
   2\text{ orbits, distinguished by permutation parity},&m\text{ even}.
 \end{cases}                                             \tag{2.4}
\]

#### Proof

The ideal helper premise realizes any word in the generators `g_i`, and
Theorem 2.1 identifies the resulting pointed orbit.

An unpointed unoriented cyclic order is a right coset modulo the dihedral
position group `D_N`.  Every rotation of `N=2m+1` positions is even.  A
reflection has `m` transpositions and therefore sign `(-1)^m`.  If `m` is
odd, `D_N` contains an odd permutation and `A_ND_N=S_N`, giving one orbit.
If `m` is even, `D_N` is contained in `A_N`, giving the two parity orbits.
\(\square\)

### Corollary 2.3 (physical parity obstruction for even semilength)

Every literal sequence of native inverse-pair substitutions preserves the
parity of each naturally tracked pointed row.  When `m` is even, this is a
well-defined invariant of the unpointed unoriented wreath support itself.
Consequently full native slot-transitivity across all shortest-wreath
factors is false for every even `m`.

#### Proof

Each time a row participates it is right-multiplied by the even permutation
`g_i`.  Corollary 2.2 shows that, for even `m`, changing the dihedral
representative cannot alter this sign.  \(\square\)

The invariant concerns host states.  It does not by itself give a q1
current invariant, because q1 targets do not remember the parity of the row
which supplies them.

## 3. A native move can create a new raw slot

The static catalogue is not closed even in the smallest unconstrained
row-order model.

### Theorem 3.1 (one-step slot birth)

Let `m>=4`, fix `i`, and put `j=i+2`.  In the aligned-start raw model there
are three pointed rows such
that:

1. rows 0 and 1 form the aligned inverse-pair pattern at `i`;
2. rows 0 and 2 do not form that pattern at any start before the move;
3. after substituting rows 0 and 1 at `i`, the new row 0 and row 2 form an
   aligned inverse-pair pattern at `j`.

#### Proof

Choose any pointed row `pi` and set

\[
              R_0=\pi,
              \qquad R_1=\pi h_i,
              \qquad R_2=\pi g_i h_j.                 \tag{3.1}
\]

The supports of `g_i` and `h_j` are disjoint when `j=i+2` and `m>=4`.
Therefore the old relative permutation from `R_0` to `R_2` has cycle type

\[
                         (2)(2)(4),                    \tag{3.2}
\]

whereas a native inverse-pair relation `h_u^{+/-1}` is one four-cycle.
Thus rows 0 and 2 do not initially have an aligned inverse-pair pattern.

After applying the first move, row 0 is `pi g_i`, and

\[
                    (\pi g_i)^{-1}R_2=h_j.             \tag{3.3}
\]

So the second raw pattern is now present.  \(\square\)

This theorem deliberately makes no disjoint-support or exact-factor
embedding claim.  It proves
that “absent at time zero” is not a preserved law of the native atom action;
the unresolved issue is simultaneous ownership of the three row supports
and their central palettes.

## 4. The natural four-move commutator

For formal row indices `u,v`, let `G_{uv}(a,b)` denote the underlying
position action which right-multiplies row `u` by `g_a` and row `v` by
`g_b`.  It is the action of a native substitution when the corresponding
inverse pair is present at those two row-specific starts.

Consider the `V`-commutator

\[
 \mathcal K(a,b;c,d)=
 G_{12}(a,b)G_{23}(c,d)G_{12}(a,b)G_{23}(c,d).        \tag{4.1}
\]

Since the `g_i` are involutions, its final row action is

\[
        (\text{row 1},\text{row 2},\text{row 3})
        \longmapsto
        (\text{row 1},\text{row 2}[g_b,g_c],\text{row 3}),
                                                               \tag{4.2}
\]

where

\[
                         [g_b,g_c]=g_b g_c g_b g_c.     \tag{4.3}
\]

### Theorem 4.1 (nontrivial four-move commutator no-go)

Let `m>=4`.  If all four steps in (4.1) are literal native inverse-pair
substitutions through exact shortest-wreath factors, then

\[
                              [g_b,g_c]=1.              \tag{4.4}
\]

Consequently the final factor is identical to the initial factor row by
row, and its signed interval current is zero at every width.  There is no
nontrivial zero-all-width host reconfiguration of this three-row,
four-move commutator form.

#### Proof

Every native inverse-pair substitution preserves the aggregate cyclic
length-`m` palette.  If all four moves in (4.1) are legal, the initial and
final aggregate central palettes are equal.  Rows 1 and 3 return literally
to their initial pointed orders, so row 2 alone must satisfy

\[
                E_m(\pi)=E_m(\pi[g_b,g_c]).            \tag{4.5}
\]

The middle support of a cyclic order determines that order up to rotation
and reversal.  Hence

\[
                            [g_b,g_c]\in D_N.           \tag{4.6}
\]

On the other hand, the support of the commutator is contained in the union
of the four cycle edges occurring in `g_b` and `g_c`, so it has at most
eight points.  A nonidentity rotation in `D_N` moves all `N` points.  A
reflection moves `N-1` points.

For `N>9`, this already excludes every nonidentity dihedral element.  When
`N=9`, a reflection would require support eight.  Four cycle edges can meet
eight distinct vertices only when the four edges are pairwise disjoint; in
that case `g_b` and `g_c` commute and the commutator is the identity.
Therefore (4.6) implies (4.4) for every `m>=4`.

The final pointed rows are then unchanged, so every cyclic interval palette,
not only the central one, is unchanged.  \(\square\)

### Corollary 4.2 (the adjacent-three-cycle commutator is forbidden)

If the two starts used on the shared middle row satisfy `c=b+m`, then

\[
        g_b g_{b+m}=t_b t_{b-1},
        \qquad
        [g_b,g_{b+m}]=(t_b t_{b-1})^2,                \tag{4.7}
\]

and the latter is a nontrivial adjacent three-cycle.  Hence the four
formal moves (4.1) cannot all be native inverse-pair substitutions in exact
factors.

This distinguishes two facts which otherwise look contradictory:

* the same overlapping generators prove `A_N` generation in Theorem 2.1;
* reusing only three rows in the shortest commutator cannot realize that
  generator dynamically.

Fresh helper rows, or a longer aggregate trade in which at least two rows
remain changed and cancel each other's central palettes, are necessary.

## 5. Exact remaining dynamic theorem

The native two-row route is now bounded by the following host statement.

> **Fresh-helper native closure.**  Construct, inside one exact
> shortest-wreath factor orbit, a sequence of inverse pairs whose tracked
> row action contains a generating set for the appropriate ideal orbit
> (`A_N`, modulo the even-semilength parity sector), while the other changed
> rows close into an aggregate all-width zero-current trade.

Theorems 2.1 and 3.1 show that the requested dynamic growth is algebraically
possible.  Corollary 2.3 and Theorem 4.1 give the exact restrictions:

1. even-semilength row parity cannot be crossed;
2. the three-row four-move commutator cannot supply a nontrivial closure;
3. a useful closure must leave at least two rows changed before their
   interval currents cancel, or use a larger exact-ledger packet.

This is strictly narrower than arbitrary coordinate-conjugate
slot-transitivity, and strictly stronger than the deficient time-zero span.
It is the remaining native inverse-pair serialization gate.
