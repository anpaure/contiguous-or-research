# The weakest even-terminal tap and the exact closed-splice parity toll

**Date:** 2026-08-04  
**Status:** unconditional implication and length ledger; conditional
construction target.  No even tap, even chronology, or new bound on
`nu(k)` is asserted to exist.

## 0. Verdict

Let the persistent construction run through odd dimensions

\[
                         n_m=2m+1
\]

and suppose one compatible selected odd spine already has terminal charge
at most `q_o`.  To obtain the same bound in all dimensions, the weakest
architecture-relative extra hypothesis is this:

> On each selected odd state, there is one separate terminal certificate in
> dimension `n_m+1` whose total physical terminal charge is at most `q_e`.

No even-to-even regeneration is needed.  The even certificates need not be
compatible with one another.  They need not use the odd terminal word,
chronology, cap, compiler, or physical assignment.  They meet the odd
construction only on data declared persistent in the selected source state.
If an even choice changes the exported odd child, it is not terminal-only
and must instead be co-instantiated with the odd transition.

The exact conclusion is

\[
             \nu(k)\le B(k)+\max\{q_o,q_e\}             \tag{0.1}
\]

for all sufficiently large `k`.  Thus an odd `B+1` spine needs only even
terminal charge at most one.  In the current nonnegative-excess convention,
an even tap of charge at most one may be either

\[
 (c,R({\cal H}))=(1,0)\quad\hbox{or}\quad
 (c,R({\cal H}))=(0,0)\ \hbox{or}\ (0,1).             \tag{0.2}
\]

In particular, a tap whose scaffold already has length `B+1` must have no
terminal omission.  A different even architecture may instead use a
length-`B` scaffold and one unit of literal repair.  The zero-omission rule
for the odd one-pivot branch is therefore not a universal rule for a
separate even tap; it follows there because the pivot has already spent the
one available position.

The unconditional closed top-bit splice is a valid even tap in the broad
sense, but not a bounded-charge tap.  From an odd universal word of length
`B(K-1)+q`, where `K` is even, its exact even excess is

\[
       2q+\chi_K,
       \qquad \chi_K:=2d_{K-1}-d_K
       \in\{d_K,d_K+2\}=\Theta(\sqrt K).              \tag{0.3}
\]

Consequently an odd `B+O(1)` or `B+1` spine does not by itself imply an
all-dimensional constant-additive bound.  A splice-derived tap must cancel
the unbounded parity toll by an actual physical recompilation, not by a
conditional owner/chronology count.

## 1. Terminal charge

Put

\[
 r_k=\left\lceil{k\over2}\right\rceil,
 \qquad w_k={k\choose r_k},
 \qquad B(k)=w_k+d_k,                                  \tag{1.1}
\]

where `d_k` is the monotone-deadline depth.  A terminal certificate in
dimension `k` consists of a concrete nonempty-set word `Z`, a final literal
replay, and the exact family `H(Z)` of targets absent from that replay.  Let
`R(H)` be the minimum length of a nonempty-set repair word whose interval
unions contain every member of `H`, with `R(emptyset)=0`.  Define

\[
 c(Z)=|Z|-B(k),
 \qquad
 \tau(Z)=c(Z)+R({\cal H}(Z)).                         \tag{1.2}
\]

Appending a shortest repair word gives a universal word of the exact
physical length

\[
              |Z|+R({\cal H}(Z))=B(k)+\tau(Z).        \tag{1.3}
\]

All scaffold positions, pivot stars, collar cells, hard terminal cells, and
repair letters are counted in (1.2).  A dummy port, an owner-surplus entry,
or a matching deficiency has no length credit until one concrete word is
fixed, replayed, and assigned its actual omitted family.

## 2. Selected-spine even-tap theorem

Let `G_m` be any declared family of auxiliary states on `n_m=2m+1`
coordinates.  Suppose there are complete states `g_m in G_m` and complete
odd transition/terminal certificates `O_m` such that

\[
                       g_m\longrightarrow g_{m+1}     \tag{2.1}
\]

is one compatible infinite odd spine and `O_m` terminalizes dimension
`n_m`.  An **even terminal tap on `g_m`** is a separate complete certificate
`E_m` in dimension `n_m+1`.  It may make arbitrary terminal-only choices.
Every choice it shares with (2.1) is required to equal the corresponding
datum in `g_m`.

### Theorem 2.1 (weakest selected-spine tap implication)

If

\[
 \sup_m\tau(O_m)\le q_o,
 \qquad
 \sup_m\tau(E_m)\le q_e,                              \tag{2.2}
\]

then (0.1) holds in every dimension covered by the spine and its taps.
The finitely many smaller dimensions can be absorbed into the constant.

### Proof

For `k=n_m`, append the repair word of `O_m`; (1.3) gives length at most
`B(k)+q_o`.  For `k=n_m+1`, append the repair word of `E_m`; (1.3) gives
length at most `B(k)+q_e`.  The odd transition (2.1) is used only to choose
the next auxiliary state.  Neither terminal repair nor any terminal-only
choice is exported, so no charge is added at a later level.  These two
parities exhaust the covered dimensions.  \(\square\)

The top-level quantifier is

\[
 \exists (g_m,O_m,E_m)_{m\ge m_0}\quad
 \forall m\ge m_0,                                    \tag{2.3}
\]

with the `g_m` forming one path.  It is not necessary to provide a tap on
every admissible state, a common odd/even terminal word, or an even
successor state.  If the even certificate uses no persistent source datum
at all, independent per-dimension even certificates are logically still
weaker, but that is simply the even upper-bound problem restated rather
than a tap construction.

### Corollary 2.2 (`B+1`)

An odd spine with `tau(O_m)<=1`, together with even taps satisfying
`tau(E_m)<=1`, gives

\[
                         \nu(k)\le B(k)+1             \tag{2.4}
\]

in every covered dimension.  If an even tap has nonnegative scaffold
excess `c(E_m)`, the integer inequality `c(E_m)+R(H(E_m))<=1` gives exactly
the cases (0.2).  In particular,

\[
 |E_m|=B(n_m+1)+1\quad\Longrightarrow\quad
                         {\cal H}(E_m)=\varnothing.    \tag{2.5}
\]

To state (2.4) for literally every `k`, the finitely many dimensions before
the spine starts must separately satisfy the same `B+1` bound; unlike an
unspecified `O(1)` constant, the sharp constant one cannot absorb a worse
finite exception.

### Corollary 2.3 (`B+O(1)`)

Uniformly bounded odd charge and uniformly bounded even-tap charge are
sufficient for `nu(k)<=B(k)+O(1)`.  A bounded number of fresh casualties at
each tap is not the hypothesis: the complete terminal charge at that level
must be uniformly bounded.  Persistent odd-side defects must separately be
replaced or reset rather than accumulated.

## 3. Exact closed-splice parity toll

Let `K` be even, let `X=(x_0,...,x_(N-1))` be universal on `K-1`
coordinates, and let `z` be fresh.  The closed splice is

\[
 S_z(X)=X\,[\{z\}]\,
       (\{z\}\cup x_0,\ldots,\{z\}\cup x_{N-2}).     \tag{3.1}
\]

It is universal and has length `2N`: old targets occur in the first copy,
`{z}` occurs at the singleton, a tagged target whose selected old witness
does not end at `x_(N-1)` occurs in the tagged copy, and one whose witness
does end there occurs in the old suffix followed by the singleton.

Write

\[
                         |X|=B(K-1)+q.                \tag{3.2}
\]

Since `w_K=2w_(K-1)`, direct subtraction gives

\[
 \begin{aligned}
 |S_z(X)|-B(K)
   &=2(w_{K-1}+d_{K-1}+q)-(w_K+d_K)\\
   &=2q+2d_{K-1}-d_K
    =2q+\chi_K.                                      \tag{3.3}
 \end{aligned}
\]

The even depth dichotomy gives

\[
 d_K\le d_{K-1}\le d_K+1,
 \qquad
 \chi_K\in\{d_K,d_K+2\}.                            \tag{3.4}
\]

Because `d_K=sqrt(pi K/8)+O(1)`, the quantity `chi_K` is unbounded.  Thus
the unmodified splice yields only an even `B+Theta(sqrt K)` bound from an
odd constant-charge word.  This is an arithmetic obstruction to the splice
implication, not a nonexistence theorem for other even constructions.

If `X` was obtained by repairing an odd terminal certificate of charge
`tau_o`, then `q=tau_o` in (3.3).  This benchmark honestly counts two copies
of every physical odd repair position.  A more economical even
recompilation may avoid that duplication, but the saving must then appear
as an actual reduction in the new word length.

## 4. Splice-relative physical saving ledger

Fix `X` and `S_z(X)` as in Section 3.  Suppose a proposed even tap produces
one concrete word `Y` and define its signed physical saving by

\[
                         s=|S_z(X)|-|Y|.              \tag{4.1}
\]

After the final literal replay of `Y`, let its exact omitted family be `H`.
Then its repaired even terminal charge is the identity

\[
 \boxed{
 \tau_{\rm ev}
  =(|Y|-B(K))+R({\cal H})
  =2q+\chi_K-s+R({\cal H}).}                         \tag{4.2}
\]

Consequently this particular certificate ends at length at most `B(K)+Q`
if and only if

\[
                 s-R({\cal H})\ge2q+\chi_K-Q.        \tag{4.3}
\]

This is an exact ledger, not an existence theorem.  It applies whether `Y`
is a subsequence, collar surgery, or a fresh recompilation; only the literal
length difference (4.1) is called a saving.

For a bounded odd charge `q=O(1)`, a splice-relative all-even
constant-additive theorem therefore needs

\[
                    s-R({\cal H})\ge\chi_K-O(1).      \tag{4.4}
\]

For an odd word of exact excess `q=1`, an even `B+1` conclusion needs

\[
                    s-R({\cal H})\ge\chi_K+1.         \tag{4.5}
\]

If `q=0`, the corresponding threshold is `chi_K-1`.  The frequently stated
phrase “compress the two parent halos to one child halo” is not (4.4) until
it produces a physical `Y` and the replay defining `H`.

## 5. What the even bilayer ledger does and does not provide

For `K=2r`, put

\[
 W={2r\choose r},
 \qquad C_r={W\over r+1}.
\]

On a *given* cyclic q1-surjective even diagonal row, the addressed
lower-port occurrence shore has `W` entries: one occurrence of each of the
`W-C_r` lower q1 values and exactly `C_r` dummy occurrences.  The two
literal diagonal phases form zero-overload full occurrence routers once one
compatible unused typed socket per owner occurrence is separately supplied.
Linearization has `W+1` physical lower ports, so an injective exact-lower
compiler necessarily leaves at least `C_r+1` of those cells unused.

Those statements are exact conditional accounting.  They do not construct

1. the cyclic q1-surjective even row;
2. a linear chronology covering every middle and upper target;
3. a safe upper opening;
4. the compatible post-compensation socket bank;
5. the second occurrence coordinate or global product closure; or
6. a final word and its omitted family.

Accordingly the dummy count, zero-overload router, boundary split, and
single-role capacity formulas cannot be entered as the physical saving `s`
in (4.1).  They become part of an even tap only after all six rows coexist
in one literal terminal certificate.  The typed terminal cut in the
bilayer theorem is likewise scoped to its declared single-role face; a
dual-role or remote socket bank may evade it.

There is also a separate fixed-fibre obstruction in the one-pivot overlay.
If the rooted connector fibre and its ports are frozen and only closed
`C6` switches are allowed, component parity is invariant.  This blocks a
bad fixed fibre, not a fresh even terminal host: reselecting the host or
using an authenticated odd actuator can evade it.  Neither this scoped
parity invariant nor the bilayer ledger is an unconditional all-even no-go.

## 6. Exact frontier

The strongest proof-safe conclusion is therefore:

\[
\boxed{
\begin{array}{c}
\text{one compatible selected odd spine with odd charge }\le q_o\\
+\ \text{one terminal-only even certificate on each selected state}\\
\text{with complete physical charge }\le q_e
\end{array}
\Longrightarrow
\nu(k)\le B(k)+\max\{q_o,q_e\}.}
\tag{6.1}
\]

For `B+1`, the weakest tap row is `tau_ev<=1`; for `B+O(1)`, it is
`sup tau_ev<infinity`.  Within a splice-derived route, these are exactly the
net-saving inequalities (4.3)--(4.5).  The existence of such taps remains
open.  In particular, the current even diagonal chronology and boundary
formulas are not promoted from conditional ledgers to existence.

## 7. Frozen dependencies

This note uses the following files at the displayed SHA-256 digests.

```text
072daa9a76e4d2fccb9fa39f5bb59f3c90e0012147ea871d14ebde18d45cc9e6  MATH_THEOREM_EVEN_DIAGONAL_BILAYER_LITERAL_ROUTER_AND_BOUNDARY_LEDGER_20260803.md
2635e32142db89714177e0b017a5f98d2e20fb91e11864cf22905b4ec40efcdd  MATH_THEOREM_BPLUS1_ONE_TOKEN_REGENERATIVE_OVERLAY_AND_FIXED_FIBRE_OBSTRUCTION_20260803.md
0959212ab0d1b945b560ee578b856304496aaec0cddd116d755b031b7ee3ab77  MATH_SYNTHESIS_EXACT_B_BPLUS1_ZERO_CHARGE_COINSTANTIATION_20260803.md
67a6ffaf8e3a193b654ae2faa0cef5963274be811bec233d37e0cb2a4beffaaa  MATH_THEOREM_R_EVEN_CLOSED_SPLICE_THREE_DELETION_AND_18CELL_COLLAR_20260731.md
66fe394573d3bc5228294e2a6ae70ffa136682cb8b743a92a97aaab1d5a50f88  MATH_AUDIT_EVEN_OPTIMAL_SPLICE_SHAVING_LINEAGE_20260731.md
659779fbf1236344a84734ec01b36de50b75a351e7e57f3646946b96eb9118d0  MATH_THEOREM_EVEN_SPLICE_EXCESS_TWO_RANK_CARRIER_GATE_20260731.md
8d0426e74e9de040f15a468aa7fe801a4512ccd5d061de2c97f12d9371a36a06  MATH_THEOREM_EVEN_TOPBIT_SPLICE_RECURRENCE_20260731.md
25bca7bdaba8ce5ec9334fcd74cbfaf71874e7d5f43e4d1764ade0d467d426e2  MATH_THEOREM_UNIFORM_COINSTANTIATED_BOUNDED_CHARGE_RESET_SPINE_REDUCTION_20260803.md
a07ac985c4d2c28918efe09db311f463bcf461f0d5999edb85536bc3d9a875c6  MATH_THEOREM_EQUIVARIANT_SAME_PARITY_TAP_DECORATED_ORBIT_FLOW_INDUCTION_20260803.md
0b069898885e643f21dfb3f9481110dfd9a177a2d11aa34eccc445faa675e11c  MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md
cf0b2aac79f4a86edcf0ec1138ea8795c3e339013037caca3b24b4b29e0e247b  MATH_SYNTHESIS_SHORTEST_ALL_K_O1_IMPLICATION_20260803.md
```
